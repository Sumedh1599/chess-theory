"""
CHESS Experiment Runners
Implements H1 (Positional Retrieval), H2 (Hindsight Injection), H3 (Arbitration)
"""

import numpy as np
import json
from typing import List, Dict, Tuple, Callable, Optional
from dataclasses import dataclass, field, asdict
from scipy.optimize import curve_fit
from scipy.stats import wilcoxon
import warnings

from chess_core import (
    CHESSAgent, HindsightCompressor, ForesightGenerator,
    VariationalArbitrator, GreedyPolicy, FixedWeightPolicy,
    cohens_d, run_wilcoxon
)


@dataclass
class H1Result:
    model_name: str
    depth: float
    context_length: int
    budget: int
    retrieved: bool

    def to_dict(self):
        return asdict(self)


@dataclass
class H1Aggregate:
    model_name: str
    depth_accuracy: Dict[float, float]
    budget_accuracy: Dict[int, float]
    exp_r2: float
    linear_r2: float
    exp_beats_linear: bool
    k_decay: float
    k_ci: Tuple[float, float]
    budget_monotonic: bool


class H1Runner:
    """H1: Positional Retrieval (Board Perception)"""

    def __init__(self, model_fn: Callable[[str, int], str], model_name: str = "model"):
        self.model_fn = model_fn
        self.model_name = model_name

    def _embed_fact(self, context: str, fact: str, depth: float) -> str:
        tokens = context.split()
        pos = int(len(tokens) * depth)
        new_tokens = tokens[:pos] + [f"[CRITICAL FACT: {fact}]"] + tokens[pos:]
        return " ".join(new_tokens)

    def _test_retrieval(self, context: str, fact: str, question: str, budget: int) -> bool:
        prompt = f"""Based on the following context, answer the question.
You have up to {budget} tokens to reason.

Context:
{context}

Question: {question}

Answer:"""
        response = self.model_fn(prompt, budget)
        return fact.lower() in response.lower()

    def run(self, base_context: str, critical_fact: str, question: str,
            depths: List[float] = None, budgets: List[int] = None,
            replicates: int = 5, short_context: str = None, long_context: str = None) -> List[H1Result]:
        if depths is None:
            depths = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95]
        if budgets is None:
            budgets = [50, 100, 200]

        results = []
        for depth in depths:
            for rep in range(replicates):
                context = self._embed_fact(base_context, critical_fact, depth)
                retrieved = self._test_retrieval(context, critical_fact, question, budget=100)
                results.append(H1Result(
                    model_name=self.model_name, depth=depth,
                    context_length=len(context.split()), budget=100, retrieved=retrieved
                ))

        for budget in budgets:
            for rep in range(replicates):
                context = self._embed_fact(base_context, critical_fact, 0.50)
                retrieved = self._test_retrieval(context, critical_fact, question, budget)
                results.append(H1Result(
                    model_name=self.model_name, depth=0.50,
                    context_length=len(context.split()), budget=budget, retrieved=retrieved
                ))

        if short_context and long_context:
            for depth in [0.15, 0.50, 0.85]:
                for ctx in [short_context, long_context]:
                    context = self._embed_fact(ctx, critical_fact, depth)
                    retrieved = self._test_retrieval(context, critical_fact, question, 100)
                    results.append(H1Result(
                        model_name=self.model_name, depth=depth,
                        context_length=len(context.split()), budget=100, retrieved=retrieved
                    ))

        return results

    def analyze(self, results: List[H1Result]) -> H1Aggregate:
        depth_groups: Dict[float, List[bool]] = {}
        for r in results:
            depth_groups.setdefault(r.depth, []).append(r.retrieved)

        depth_accuracy = {d: np.mean(vals) for d, vals in depth_groups.items()}
        depths = np.array(sorted(depth_accuracy.keys()))
        accs = np.array([depth_accuracy[d] for d in depths])

        def exp_decay(d, p_inf, p0, k):
            return p_inf + (p0 - p_inf) * np.exp(-k * d)

        try:
            popt, _ = curve_fit(exp_decay, depths, accs, p0=[0.5, 1.0, 5.0], maxfev=10000)
            p_inf, p0, k = popt
            y_pred = exp_decay(depths, *popt)
            ss_res = np.sum((accs - y_pred) ** 2)
            ss_tot = np.sum((accs - np.mean(accs)) ** 2)
            exp_r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

            k_bootstrap = []
            for _ in range(100):
                idx = np.random.choice(len(depths), len(depths), replace=True)
                try:
                    pb, _ = curve_fit(exp_decay, depths[idx], accs[idx], p0=[0.5, 1.0, 5.0], maxfev=5000)
                    k_bootstrap.append(pb[2])
                except:
                    pass
            k_ci = (np.percentile(k_bootstrap, 2.5), np.percentile(k_bootstrap, 97.5)) if k_bootstrap else (k, k)
        except Exception:
            exp_r2 = -999
            k = 999
            k_ci = (999, 999)

        linear_coef = np.polyfit(depths, accs, 1)
        linear_pred = np.polyval(linear_coef, depths)
        linear_r2 = 1 - np.sum((accs - linear_pred) ** 2) / ss_tot if ss_tot > 0 else 0

        budget_results = [r for r in results if r.depth == 0.50]
        budget_groups: Dict[int, List[bool]] = {}
        for r in budget_results:
            budget_groups.setdefault(r.budget, []).append(r.retrieved)
        budget_accuracy = {b: np.mean(vals) for b, vals in budget_groups.items()}

        sorted_budgets = sorted(budget_accuracy.keys())
        budget_monotonic = all(
            budget_accuracy[sorted_budgets[i]] <= budget_accuracy[sorted_budgets[i+1]]
            for i in range(len(sorted_budgets)-1)
        )

        return H1Aggregate(
            model_name=self.model_name, depth_accuracy=depth_accuracy,
            budget_accuracy=budget_accuracy, exp_r2=exp_r2, linear_r2=linear_r2,
            exp_beats_linear=exp_r2 > linear_r2, k_decay=k, k_ci=k_ci,
            budget_monotonic=budget_monotonic
        )


@dataclass
class H2Result:
    task_id: str
    task_type: str
    with_hindsight_score: float
    without_hindsight_score: float

    @property
    def uplift(self) -> float:
        return self.with_hindsight_score - self.without_hindsight_score


@dataclass
class H2Aggregate:
    model_name: str
    with_mean: float
    without_mean: float
    uplift: float
    uplift_ci: Tuple[float, float]
    cohens_d: float
    wilcoxon_stat: float
    wilcoxon_p: float
    ablation_full: float
    ablation_last: float
    ablation_noise: float


class H2Runner:
    """H2: Hindsight Injection"""

    TASK_TYPES = [
        "factual_qa", "code_generation", "logical_reasoning", "multi_hop_reasoning",
        "sentiment_classification", "translation", "summarization", "arithmetic",
        "medical_reasoning", "legal_reasoning"
    ]

    def __init__(self, model_fn: Callable[[str, int], str], model_name: str = "model",
                 scorer_fn: Optional[Callable[[str, str], float]] = None):
        self.model_fn = model_fn
        self.model_name = model_name
        self.scorer_fn = scorer_fn or self._default_scorer

    def _default_scorer(self, reference: str, prediction: str) -> float:
        ref_words = set(reference.lower().split())
        pred_words = set(prediction.lower().split())
        if not ref_words:
            return 0.0
        overlap = len(ref_words & pred_words)
        return min(1.0, overlap / len(ref_words))

    def _run_single(self, task: Dict, hindsight_mode: str = "full") -> float:
        agent = CHESSAgent(hindsight_budget=200, foresight_k=1, arbitration_policy="greedy")

        if "history" in task:
            for h in task["history"]:
                agent.hindsight.add_turn(h)

        if hindsight_mode == "full":
            H_t = agent.hindsight.compress()
        elif hindsight_mode == "last":
            H_t = agent.hindsight.last_turn_only()
        elif hindsight_mode == "noise":
            H_t = agent.hindsight.noise_ablation()
        else:
            H_t = None

        prompt = task["prompt"]
        if H_t:
            prompt = H_t.to_prompt_fragment() + "\n\n" + prompt

        response = self.model_fn(prompt, max_tokens=task.get("max_tokens", 200))
        score = self.scorer_fn(task.get("reference", ""), response)
        return score

    def run(self, tasks: List[Dict], replicates: int = 1) -> Tuple[List[H2Result], H2Aggregate]:
        results = []
        for task in tasks:
            for _ in range(replicates):
                score_with = self._run_single(task, hindsight_mode="full")
                score_without = self._run_single(task, hindsight_mode="none")
                results.append(H2Result(
                    task_id=task.get("id", "unknown"),
                    task_type=task.get("task_type", "unknown"),
                    with_hindsight_score=score_with,
                    without_hindsight_score=score_without
                ))

        aggregate = self._aggregate(results)
        return results, aggregate

    def run_ablation(self, tasks: List[Dict]) -> Dict[str, float]:
        scores = {"full": [], "last": [], "noise": []}
        for task in tasks:
            for mode in ["full", "last", "noise"]:
                score = self._run_single(task, hindsight_mode=mode)
                scores[mode].append(score)
        return {k: np.mean(v) for k, v in scores.items()}

    def _aggregate(self, results: List[H2Result]) -> H2Aggregate:
        with_scores = np.array([r.with_hindsight_score for r in results])
        without_scores = np.array([r.without_hindsight_score for r in results])

        uplift = with_scores - without_scores
        uplift_mean = float(np.mean(uplift))
        uplift_ci = (float(np.percentile(uplift, 2.5)), float(np.percentile(uplift, 97.5)))

        d = cohens_d(with_scores, without_scores)
        w_stat, w_p = run_wilcoxon(with_scores, without_scores)

        return H2Aggregate(
            model_name=self.model_name, with_mean=float(np.mean(with_scores)),
            without_mean=float(np.mean(without_scores)), uplift=uplift_mean,
            uplift_ci=uplift_ci, cohens_d=d, wilcoxon_stat=w_stat, wilcoxon_p=w_p,
            ablation_full=0.0, ablation_last=0.0, ablation_noise=0.0
        )


@dataclass
class H3Result:
    scenario_id: str
    category: str
    policy: str
    selected_action: str
    oracle_score: float
    elbo_start: Optional[float] = None
    elbo_end: Optional[float] = None
    elbo_improved: Optional[bool] = None


@dataclass
class H3Aggregate:
    model_name: str
    policy_accuracy: Dict[str, float]
    delta_var_fixed: float
    delta_var_greedy: float
    elbo_improved_fraction: float
    category_breakdown: Dict[str, Dict[str, float]]


class H3Runner:
    """H3: Variational Arbitration"""

    CONFLICT_CATEGORIES = [
        "factual_disagreement", "safety_relevant", "preference_vs_policy",
        "competing_utility", "irreducible_ambiguity"
    ]

    def __init__(self, model_fn: Callable[[str, int], str], model_name: str = "model",
                 oracle_fn: Optional[Callable[[Dict, str], float]] = None):
        self.model_fn = model_fn
        self.model_name = model_name
        self.oracle_fn = oracle_fn or self._default_oracle

    def _default_oracle(self, scenario: Dict, selected: str) -> float:
        correct_answer = scenario.get("correct_answer", "")
        return 1.0 if correct_answer.lower() in selected.lower() else 0.0

    def _build_scenario_context(self, scenario: Dict) -> str:
        return f"""Scenario: {scenario['description']}

Conflict: {scenario['conflict']}

Options:
{chr(10).join(f"{i+1}. {opt}" for i, opt in enumerate(scenario['options']))}

Select the best response:"""

    def run_policy(self, scenarios: List[Dict], policy: str, log_elbo: bool = False) -> List[H3Result]:
        results = []
        for scenario in scenarios:
            agent = CHESSAgent(hindsight_budget=200, foresight_k=3, arbitration_policy=policy, eta=1.0)

            if "history" in scenario:
                for h in scenario["history"]:
                    agent.hindsight.add_turn(h)

            context = self._build_scenario_context(scenario)

            def generate_fn(prompt, params):
                n = params.get("n", 3)
                temp = params.get("temperature", 0.7)
                candidates = []
                for i in range(n):
                    t = temp + (i * 0.1)
                    resp = self.model_fn(prompt, max_tokens=200)
                    logprob = -0.5 * i
                    candidates.append((resp, logprob))
                return candidates

            action, metadata = agent.act(context, generate_fn)
            oracle_score = self.oracle_fn(scenario, action)

            elbo_start = None
            elbo_end = None
            elbo_improved = None

            if log_elbo and policy == "variational" and "arbitration" in metadata:
                arb = metadata["arbitration"]
                if "elbo_history" in arb and arb["elbo_history"]:
                    elbo_start = arb["elbo_history"][0]
                    elbo_end = arb["elbo_history"][-1]
                    elbo_improved = elbo_end > elbo_start

            results.append(H3Result(
                scenario_id=scenario.get("id", "unknown"),
                category=scenario.get("category", "unknown"),
                policy=policy, selected_action=action, oracle_score=oracle_score,
                elbo_start=elbo_start, elbo_end=elbo_end, elbo_improved=elbo_improved
            ))

        return results

    def run(self, scenarios: List[Dict], policies: List[str] = None,
            log_elbo_for_variational: bool = True) -> Tuple[Dict[str, List[H3Result]], H3Aggregate]:
        if policies is None:
            policies = ["greedy", "fixed", "variational"]

        all_results = {}
        for policy in policies:
            log_elbo = log_elbo_for_variational and (policy == "variational")
            all_results[policy] = self.run_policy(scenarios, policy, log_elbo)

        aggregate = self._aggregate(all_results)
        return all_results, aggregate

    def _aggregate(self, all_results: Dict[str, List[H3Result]]) -> H3Aggregate:
        policy_accuracy = {}
        for policy, results in all_results.items():
            scores = [r.oracle_score for r in results]
            policy_accuracy[policy] = float(np.mean(scores)) if scores else 0.0

        var_acc = policy_accuracy.get("variational", 0.0)
        fixed_acc = policy_accuracy.get("fixed", 0.0)
        greedy_acc = policy_accuracy.get("greedy", 0.0)

        delta_var_fixed = var_acc - fixed_acc
        delta_var_greedy = var_acc - greedy_acc

        var_results = all_results.get("variational", [])
        elbo_results = [r for r in var_results if r.elbo_improved is not None]
        elbo_fraction = np.mean([r.elbo_improved for r in elbo_results]) if elbo_results else 0.0

        category_breakdown = {}
        for policy, results in all_results.items():
            cat_scores: Dict[str, List[float]] = {}
            for r in results:
                cat_scores.setdefault(r.category, []).append(r.oracle_score)
            category_breakdown[policy] = {
                cat: float(np.mean(scores)) for cat, scores in cat_scores.items()
            }

        return H3Aggregate(
            model_name=self.model_name, policy_accuracy=policy_accuracy,
            delta_var_fixed=delta_var_fixed, delta_var_greedy=delta_var_greedy,
            elbo_improved_fraction=float(elbo_fraction), category_breakdown=category_breakdown
        )


def save_results(results: Dict, filepath: str):
    def serialize(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.floating, np.integer)):
            return float(obj)
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    with open(filepath, "w") as f:
        json.dump(results, f, indent=2, default=serialize)
    print(f"Results saved to {filepath}")
