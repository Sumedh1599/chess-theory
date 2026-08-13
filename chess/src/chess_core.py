"""
CHESS: Calibrated Hindsight-Foresight Ensemble for Strategic Self-Arbitration
Core implementation of the three-seat meta-cognitive architecture.

Reference: Patil, S. (2025). Strategic Self-Arbitration in LLM Agents.
"""

import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, field
from scipy.special import softmax
from scipy.stats import wilcoxon
import json


@dataclass
class TurnRecord:
    """A single prior turn with outcome annotation."""
    turn_id: int
    action: str
    outcome: str
    context_summary: str = ""

    def to_dict(self) -> Dict:
        return {
            "turn_id": self.turn_id,
            "action": self.action,
            "outcome": self.outcome,
            "context_summary": self.context_summary
        }


@dataclass  
class HindsightSignal:
    """Compressed memory signal H(t) from the Past Self."""
    summary: str
    outcome_map: Dict[str, List[str]] = field(default_factory=dict)
    token_budget: int = 200

    def to_prompt_fragment(self) -> str:
        frag = f"[HINDSIGHT SUMMARY]\n{self.summary}\n"
        if self.outcome_map:
            frag += "\n[OUTCOME PATTERNS]\n"
            for outcome, actions in self.outcome_map.items():
                frag += f"- {outcome}: {', '.join(actions[:3])}\n"
        return frag


@dataclass
class CandidateContinuation:
    """A single candidate from the Foresight Self."""
    candidate_id: int
    text: str
    value_estimate: float = 0.0
    reasoning: str = ""

    def to_dict(self) -> Dict:
        return {
            "candidate_id": self.candidate_id,
            "text": self.text,
            "value_estimate": self.value_estimate,
            "reasoning": self.reasoning
        }


@dataclass
class ForesightSignal:
    """Set of candidate continuations F(t) from the Future Self."""
    candidates: List[CandidateContinuation]
    generation_params: Dict = field(default_factory=dict)

    def get_best_raw_candidate(self) -> CandidateContinuation:
        return max(self.candidates, key=lambda c: c.value_estimate)


class HindsightCompressor:
    """Past Self: compresses prior turn history into H(t)."""

    def __init__(self, budget: int = 200, recency_bias: float = 0.8):
        self.budget = budget
        self.recency_bias = recency_bias
        self.history: List[TurnRecord] = []

    def add_turn(self, record: TurnRecord):
        self.history.append(record)

    def compress(self, llm_compress_fn: Optional[Callable] = None) -> HindsightSignal:
        if not self.history:
            return HindsightSignal(summary="No prior history.", token_budget=self.budget)

        weighted_lines = []
        n = len(self.history)
        for i, rec in enumerate(self.history):
            weight = self.recency_bias ** (n - 1 - i)
            if weight > 0.3:
                detail_level = "full" if weight > 0.7 else "brief"
                if detail_level == "full":
                    line = f"T{rec.turn_id}: {rec.action} -> {rec.outcome}"
                    if rec.context_summary:
                        line += f" | ctx: {rec.context_summary}"
                else:
                    line = f"T{rec.turn_id}: {rec.outcome}"
                weighted_lines.append(line)

        raw_text = "\n".join(weighted_lines)

        if llm_compress_fn:
            summary = llm_compress_fn(raw_text, self.budget)
        else:
            summary = self._heuristic_compress(raw_text)

        outcome_map: Dict[str, List[str]] = {}
        for rec in self.history:
            outcome_map.setdefault(rec.outcome, []).append(rec.action)

        return HindsightSignal(
            summary=summary,
            outcome_map=outcome_map,
            token_budget=self.budget
        )

    def _heuristic_compress(self, text: str) -> str:
        words = text.split()
        if len(words) <= self.budget // 4:
            return text
        return " ".join(words[:self.budget // 4]) + "... [truncated]"

    def last_turn_only(self) -> HindsightSignal:
        if not self.history:
            return HindsightSignal(summary="No prior history.", token_budget=self.budget)
        rec = self.history[-1]
        summary = f"Last turn (T{rec.turn_id}): {rec.action} -> {rec.outcome}"
        return HindsightSignal(summary=summary, token_budget=self.budget)

    def noise_ablation(self) -> HindsightSignal:
        noise = " ".join(["placeholder"] * (self.budget // 10))
        return HindsightSignal(summary=noise, token_budget=self.budget)


class ForesightGenerator:
    """Future Self: generates k candidate continuations from current context."""

    def __init__(self, k: int = 3, temperature: float = 0.7):
        self.k = k
        self.temperature = temperature

    def generate(
        self,
        context: str,
        generate_fn: Callable[[str, Dict], List[Tuple[str, float]]]
    ) -> ForesightSignal:
        prompt = self._build_prompt(context)
        params = {"temperature": self.temperature, "n": self.k}
        results = generate_fn(prompt, params)

        candidates = []
        for i, (text, logprob) in enumerate(results[:self.k]):
            candidates.append(CandidateContinuation(
                candidate_id=i,
                text=text,
                value_estimate=logprob,
                reasoning=f"Generated with temp={self.temperature}"
            ))

        return ForesightSignal(candidates=candidates, generation_params=params)

    def _build_prompt(self, context: str) -> str:
        return f"""You are the Foresight Self. Given the current context, generate {self.k} distinct candidate responses.
For each candidate, consider different strategic approaches.

Current context:
{context}

Generate {self.k} candidates:"""


class VariationalArbitrator:
    """Present Self: arbitrates between H(t) and F(t) via ELBO optimization."""

    def __init__(
        self,
        eta: float = 1.0,
        prior_alpha: float = 1.0,
        max_steps: int = 100,
        convergence_tol: float = 1e-4
    ):
        self.eta = eta
        self.prior_alpha = prior_alpha
        self.max_steps = max_steps
        self.convergence_tol = convergence_tol
        self.w = np.array([0.5, 0.5])
        self.elbo_history: List[float] = []

    def arbitrate(
        self,
        context: str,
        hindsight: HindsightSignal,
        foresight: ForesightSignal,
        score_fn: Optional[Callable[[str, str, str], Tuple[float, float]]] = None
    ) -> Tuple[CandidateContinuation, Dict]:
        k = len(foresight.candidates)
        if k == 0:
            raise ValueError("Foresight signal contains no candidates")

        q = np.ones(k) / k
        p_a = self._compute_prior(foresight, hindsight)

        if score_fn is None:
            scores_h, scores_f = self._default_score(context, hindsight, foresight)
        else:
            scores_h = np.zeros(k)
            scores_f = np.zeros(k)
            for i, cand in enumerate(foresight.candidates):
                sh, sf = score_fn(context, cand.text, hindsight.to_prompt_fragment())
                scores_h[i] = sh
                scores_f[i] = sf

        scores_h = softmax(scores_h)
        scores_f = softmax(scores_f)

        prev_elbo = -np.inf
        for step in range(self.max_steps):
            log_p_D_given_a = (
                self.w[0] * np.log(scores_h + 1e-10) +
                self.w[1] * np.log(scores_f + 1e-10)
            )

            log_q = log_p_D_given_a + np.log(p_a + 1e-10)
            q_new = softmax(log_q)

            elbo = np.sum(q_new * log_p_D_given_a) - self._kl_divergence(q_new, p_a)
            self.elbo_history.append(elbo)

            if abs(elbo - prev_elbo) < self.convergence_tol:
                break

            contrib_h = np.sum(q_new * np.log(scores_h + 1e-10))
            contrib_f = np.sum(q_new * np.log(scores_f + 1e-10))

            raw_weights = np.array([
                self.eta * self.w[0] * contrib_h,
                self.eta * self.w[1] * contrib_f
            ])
            self.w = softmax(raw_weights)

            q = q_new
            prev_elbo = elbo

        best_idx = int(np.argmax(q))
        selected = foresight.candidates[best_idx]

        metadata = {
            "elbo_final": prev_elbo,
            "elbo_history": self.elbo_history,
            "steps": len(self.elbo_history),
            "influence_weights": {
                "hindsight": float(self.w[0]),
                "foresight": float(self.w[1])
            },
            "candidate_probs": q.tolist(),
            "converged": abs(elbo - prev_elbo) < self.convergence_tol if step > 0 else True
        }

        return selected, metadata

    def _compute_prior(self, foresight: ForesightSignal, hindsight: HindsightSignal) -> np.ndarray:
        k = len(foresight.candidates)
        prior = np.ones(k) * self.prior_alpha

        if hindsight.outcome_map:
            success_words = set()
            for action in hindsight.outcome_map.get("success", []):
                success_words.update(action.lower().split())

            for i, cand in enumerate(foresight.candidates):
                cand_words = set(cand.text.lower().split())
                overlap = len(cand_words & success_words)
                prior[i] += overlap * 0.5

        return prior / prior.sum()

    def _default_score(self, context: str, hindsight: HindsightSignal, foresight: ForesightSignal) -> Tuple[np.ndarray, np.ndarray]:
        k = len(foresight.candidates)
        scores_f = np.array([c.value_estimate for c in foresight.candidates])

        h_words = set(hindsight.summary.lower().split())
        scores_h = np.zeros(k)
        for i, cand in enumerate(foresight.candidates):
            c_words = set(cand.text.lower().split())
            if h_words:
                scores_h[i] = len(c_words & h_words) / len(h_words)
            else:
                scores_h[i] = 0.5

        return scores_h, scores_f

    def _kl_divergence(self, q: np.ndarray, p: np.ndarray) -> float:
        mask = q > 1e-10
        return np.sum(q[mask] * np.log(q[mask] / (p[mask] + 1e-10)))

    def reset(self):
        self.w = np.array([0.5, 0.5])
        self.elbo_history = []


class GreedyPolicy:
    def arbitrate(self, foresight: ForesightSignal) -> Tuple[CandidateContinuation, Dict]:
        if not foresight.candidates:
            raise ValueError("No candidates")
        selected = foresight.candidates[0]
        return selected, {"policy": "greedy", "candidate_idx": 0}


class FixedWeightPolicy:
    def arbitrate(self, hindsight: HindsightSignal, foresight: ForesightSignal,
                  score_fn: Optional[Callable] = None) -> Tuple[CandidateContinuation, Dict]:
        k = len(foresight.candidates)
        if k == 0:
            raise ValueError("No candidates")

        scores = np.zeros(k)
        for i, cand in enumerate(foresight.candidates):
            h_score = 0.5
            f_score = cand.value_estimate
            scores[i] = 0.5 * h_score + 0.5 * f_score

        best_idx = int(np.argmax(scores))
        return foresight.candidates[best_idx], {
            "policy": "fixed_weight",
            "candidate_idx": best_idx,
            "weights": {"hindsight": 0.5, "foresight": 0.5}
        }


class CHESSAgent:
    """Full CHESS agent combining all three seats."""

    def __init__(self, hindsight_budget: int = 200, foresight_k: int = 3,
                 arbitration_policy: str = "variational", eta: float = 1.0):
        self.hindsight = HindsightCompressor(budget=hindsight_budget)
        self.foresight = ForesightGenerator(k=foresight_k)
        self.turn_counter = 0

        if arbitration_policy == "variational":
            self.arbitrator = VariationalArbitrator(eta=eta)
        elif arbitration_policy == "greedy":
            self.arbitrator = GreedyPolicy()
        elif arbitration_policy == "fixed":
            self.arbitrator = FixedWeightPolicy()
        else:
            raise ValueError(f"Unknown policy: {arbitration_policy}")

        self.policy_name = arbitration_policy

    def act(self, context: str, generate_fn: Callable,
            compress_fn: Optional[Callable] = None,
            score_fn: Optional[Callable] = None) -> Tuple[str, Dict]:
        H_t = self.hindsight.compress(compress_fn)
        F_t = self.foresight.generate(context, generate_fn)

        if isinstance(self.arbitrator, VariationalArbitrator):
            selected, arb_meta = self.arbitrator.arbitrate(context, H_t, F_t, score_fn)
        elif isinstance(self.arbitrator, GreedyPolicy):
            selected, arb_meta = self.arbitrator.arbitrate(F_t)
        else:
            selected, arb_meta = self.arbitrator.arbitrate(H_t, F_t, score_fn)

        metadata = {
            "turn": self.turn_counter,
            "policy": self.policy_name,
            "hindsight": H_t.to_prompt_fragment(),
            "candidates": [c.to_dict() for c in F_t.candidates],
            "arbitration": arb_meta
        }

        self.turn_counter += 1
        return selected.text, metadata

    def observe_outcome(self, action: str, outcome: str, context_summary: str = ""):
        record = TurnRecord(
            turn_id=self.turn_counter,
            action=action,
            outcome=outcome,
            context_summary=context_summary
        )
        self.hindsight.add_turn(record)


def cohens_d(x: np.ndarray, y: np.ndarray) -> float:
    diff = x - y
    return float(diff.mean() / diff.std(ddof=1))


def run_wilcoxon(with_scores: np.ndarray, without_scores: np.ndarray) -> Tuple[float, float]:
    stat, p = wilcoxon(with_scores, without_scores)
    return float(stat), float(p)
