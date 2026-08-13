#!/usr/bin/env python3
"""
ELBO Convergence Checker for CHESS (Calibrated Hindsight-Foresight Ensemble)

Usage:
    python elbo.py --candidates 3 --steps 10 --epsilon 0.01
    python elbo.py --from-json arbitration_input.json

Input JSON format:
{
  "candidates": [
    {"id": "A", "log_p_H": 0.2, "log_p_F": 0.7},
    {"id": "B", "log_p_H": 0.8, "log_p_F": 0.4},
    {"id": "C", "log_p_H": 0.5, "log_p_F": 0.5}
  ],
  "w_h": 0.5,
  "w_f": 0.5,
  "eta": 1.0,
  "epsilon": 0.01,
  "max_steps": 10
}
"""

import json
import math
import argparse
from typing import List, Dict, Tuple


def softmax(values: List[float]) -> List[float]:
    """Numerically stable softmax."""
    max_val = max(values)
    exps = [math.exp(v - max_val) for v in values]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]


def compute_kl(q: List[float], p: List[float]) -> float:
    """KL divergence KL(q || p)."""
    kl = 0.0
    for qi, pi in zip(q, p):
        if qi > 1e-12 and pi > 1e-12:
            kl += qi * math.log(qi / pi)
    return kl


def compute_entropy(q: List[float]) -> float:
    """Entropy of distribution q."""
    h = 0.0
    for qi in q:
        if qi > 1e-12:
            h -= qi * math.log(qi)
    return h


def elbo_step(
    candidates: List[Dict],
    w_h: float,
    w_f: float,
    prior: List[float]
) -> Tuple[List[float], float, float, float]:
    """
    Perform one ELBO optimization step.

    Returns:
        q: updated distribution over candidates
        elbo: evidence lower bound
        exp_log_lik: expected log likelihood term
        kl: KL divergence term
    """
    k = len(candidates)

    # Compute log p(D | a_i) for each candidate
    log_p_D = []
    for c in candidates:
        log_p_H = c.get("log_p_H", 0.0)
        log_p_F = c.get("log_p_F", 0.0)
        log_p_D.append(w_h * log_p_H + w_f * log_p_F)

    # Update q(a) ∝ exp(log p(D | a))
    q = softmax(log_p_D)

    # Compute expected log likelihood: E_q[log p(D | a)]
    exp_log_lik = sum(qi * lpd for qi, lpd in zip(q, log_p_D))

    # Compute KL divergence
    kl = compute_kl(q, prior)

    # ELBO
    elbo = exp_log_lik - kl

    return q, elbo, exp_log_lik, kl


def reallocate_weights(
    candidates: List[Dict],
    q: List[float],
    w_h: float,
    w_f: float,
    eta: float
) -> Tuple[float, float]:
    """
    Reallocate influence weights based on contribution to ELBO.
    Simplified: weight by expected alignment score.
    """
    contrib_h = sum(qi * c.get("log_p_H", 0.0) for qi, c in zip(q, candidates))
    contrib_f = sum(qi * c.get("log_p_F", 0.0) for qi, c in zip(q, candidates))

    # Softmax reallocation
    weights = softmax([eta * contrib_h, eta * contrib_f])
    return weights[0], weights[1]


def arbitrate(
    candidates: List[Dict],
    w_h: float = 0.5,
    w_f: float = 0.5,
    eta: float = 1.0,
    epsilon: float = 0.01,
    max_steps: int = 10
) -> Dict:
    """
    Run full variational arbitration.
    """
    k = len(candidates)
    prior = [1.0 / k] * k

    trace = []
    q = prior.copy()

    for step in range(1, max_steps + 1):
        q, elbo, exp_ll, kl = elbo_step(candidates, w_h, w_f, prior)

        trace.append({
            "step": step,
            "elbo": round(elbo, 4),
            "exp_log_lik": round(exp_ll, 4),
            "kl": round(kl, 4),
            "w_h": round(w_h, 4),
            "w_f": round(w_f, 4),
            "q": {c["id"]: round(qi, 4) for c, qi in zip(candidates, q)}
        })

        # Check convergence
        if step > 1:
            delta = abs(elbo - trace[-2]["elbo"])
            if delta < epsilon:
                trace[-1]["status"] = "CONVERGED"
                break
            else:
                trace[-1]["status"] = f"Improving (Δ={round(delta, 4)})"
        else:
            trace[-1]["status"] = "Initialized"

        # Reallocate weights for next step
        w_h, w_f = reallocate_weights(candidates, q, w_h, w_f, eta)
    else:
        trace[-1]["status"] = "MAX_STEPS"

    # Select winner
    winner_idx = max(range(k), key=lambda i: q[i])
    winner = candidates[winner_idx]
    confidence = q[winner_idx]

    return {
        "winner": winner["id"],
        "confidence": round(confidence, 4),
        "final_weights": {"w_h": round(w_h, 4), "w_f": round(w_f, 4)},
        "steps": len(trace),
        "trace": trace,
        "converged": trace[-1]["status"] == "CONVERGED",
        "candidates": [c["id"] for c in candidates]
    }


def main():
    parser = argparse.ArgumentParser(description="CHESS ELBO Arbitration Checker")
    parser.add_argument("--from-json", type=str, help="Load arbitration from JSON file")
    parser.add_argument("--candidates", type=int, default=3, help="Number of candidates")
    parser.add_argument("--steps", type=int, default=10, help="Max steps")
    parser.add_argument("--epsilon", type=float, default=0.01, help="Convergence threshold")
    parser.add_argument("--w-h", type=float, default=0.5, help="Initial hindsight weight")
    parser.add_argument("--w-f", type=float, default=0.5, help="Initial foresight weight")
    parser.add_argument("--eta", type=float, default=1.0, help="Learning rate")
    args = parser.parse_args()

    if args.from_json:
        with open(args.from_json) as f:
            data = json.load(f)
        candidates = data["candidates"]
        w_h = data.get("w_h", 0.5)
        w_f = data.get("w_f", 0.5)
        eta = data.get("eta", 1.0)
        epsilon = data.get("epsilon", 0.01)
        max_steps = data.get("max_steps", 10)
    else:
        # Demo data
        candidates = [
            {"id": "A", "log_p_H": 0.2, "log_p_F": 0.7},
            {"id": "B", "log_p_H": 0.8, "log_p_F": 0.4},
            {"id": "C", "log_p_H": 0.5, "log_p_F": 0.5},
        ]
        w_h = args.w_h
        w_f = args.w_f
        eta = args.eta
        epsilon = args.epsilon
        max_steps = args.steps

    result = arbitrate(candidates, w_h, w_f, eta, epsilon, max_steps)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
