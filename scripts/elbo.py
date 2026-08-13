#!/usr/bin/env python3
"""
ELBO Convergence Checker for CHESS (Calibrated Hindsight-Foresight Ensemble)

Usage:
    python elbo.py --from-json arbitration_input.json
    python elbo.py --candidates 3 --steps 10 --epsilon 0.01

Input JSON format:
{
  "candidates": [
    {"id": "A", "log_p_H": 0.2, "log_p_F": 0.7},
    {"id": "B", "log_p_H": 0.8, "log_p_F": 0.4},
    {"id": "C", "log_p_H": 0.5, "log_p_F": 0.5}
  ],
  "w_h": 0.5, "w_f": 0.5, "eta": 1.0, "epsilon": 0.01, "max_steps": 10
}
"""

import json, math, argparse
from typing import List, Dict, Tuple

def softmax(values: List[float]) -> List[float]:
    max_val = max(values)
    exps = [math.exp(v - max_val) for v in values]
    s = sum(exps)
    return [e / s for e in exps]

def compute_kl(q: List[float], p: List[float]) -> float:
    return sum(qi * math.log(qi / pi) for qi, pi in zip(q, p) if qi > 1e-12 and pi > 1e-12)

def elbo_step(candidates: List[Dict], w_h: float, w_f: float, prior: List[float]) -> Tuple[List[float], float, float, float]:
    log_p_D = [w_h * c.get("log_p_H", 0.0) + w_f * c.get("log_p_F", 0.0) for c in candidates]
    q = softmax(log_p_D)
    exp_ll = sum(qi * lpd for qi, lpd in zip(q, log_p_D))
    kl = compute_kl(q, prior)
    return q, exp_ll - kl, exp_ll, kl

def reallocate_weights(candidates: List[Dict], q: List[float], eta: float) -> Tuple[float, float]:
    ch = sum(qi * c.get("log_p_H", 0.0) for qi, c in zip(q, candidates))
    cf = sum(qi * c.get("log_p_F", 0.0) for qi, c in zip(q, candidates))
    return tuple(softmax([eta * ch, eta * cf]))

def arbitrate(candidates: List[Dict], w_h: float = 0.5, w_f: float = 0.5,
              eta: float = 1.0, epsilon: float = 0.01, max_steps: int = 10) -> Dict:
    k = len(candidates)
    prior = [1.0 / k] * k
    trace = []
    for step in range(1, max_steps + 1):
        q, elbo, exp_ll, kl = elbo_step(candidates, w_h, w_f, prior)
        trace.append({"step": step, "elbo": round(elbo, 4), "exp_log_lik": round(exp_ll, 4),
                      "kl": round(kl, 4), "w_h": round(w_h, 4), "w_f": round(w_f, 4),
                      "q": {c["id"]: round(qi, 4) for c, qi in zip(candidates, q)}})
        if step > 1 and abs(elbo - trace[-2]["elbo"]) < epsilon:
            trace[-1]["status"] = "CONVERGED"
            break
        trace[-1]["status"] = "Improving" if step > 1 else "Initialized"
        w_h, w_f = reallocate_weights(candidates, q, eta)
    else:
        trace[-1]["status"] = "MAX_STEPS"
    wi = max(range(k), key=lambda i: q[i])
    return {"winner": candidates[wi]["id"], "confidence": round(q[wi], 4),
            "final_weights": {"w_h": round(w_h, 4), "w_f": round(w_f, 4)},
            "steps": len(trace), "trace": trace, "converged": trace[-1]["status"] == "CONVERGED",
            "candidates": [c["id"] for c in candidates]}

def main():
    p = argparse.ArgumentParser(description="CHESS ELBO Arbitration Checker")
    p.add_argument("--from-json", type=str, help="Load from JSON file")
    p.add_argument("--candidates", type=int, default=3)
    p.add_argument("--steps", type=int, default=10)
    p.add_argument("--epsilon", type=float, default=0.01)
    p.add_argument("--w-h", type=float, default=0.5)
    p.add_argument("--w-f", type=float, default=0.5)
    p.add_argument("--eta", type=float, default=1.0)
    args = p.parse_args()

    if args.from_json:
        with open(args.from_json) as f:
            data = json.load(f)
        candidates, w_h, w_f = data["candidates"], data.get("w_h", 0.5), data.get("w_f", 0.5)
        eta, epsilon, max_steps = data.get("eta", 1.0), data.get("epsilon", 0.01), data.get("max_steps", 10)
    else:
        candidates = [
            {"id": "A", "log_p_H": 0.2, "log_p_F": 0.7},
            {"id": "B", "log_p_H": 0.8, "log_p_F": 0.4},
            {"id": "C", "log_p_H": 0.5, "log_p_F": 0.5},
        ]
        w_h, w_f, eta, epsilon, max_steps = args.w_h, args.w_f, args.eta, args.epsilon, args.steps

    print(json.dumps(arbitrate(candidates, w_h, w_f, eta, epsilon, max_steps), indent=2))

if __name__ == "__main__":
    main()
