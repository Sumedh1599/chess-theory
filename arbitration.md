# Present Self — Variational Arbitration Protocol

## What It Does
Selects action `a*` by optimizing the ELBO (Evidence Lower Bound) over the
posterior `p(a | C(t), H(t), F(t))`. Runs silently on every response.

## The Algorithm (Max 5 Steps)

```
Initialize:
  q(a_i) = 1/3 for all candidates        # uniform prior
  w_h = 0.5, w_f = 0.5                   # equal initial influence
  ε = 0.01                               # convergence threshold
  η = 1.0                                # learning rate

For step = 1 to 5:
  1. log p(D|a_i) = w_h·alignment(H,a_i) + w_f·value(F,a_i)
  2. q(a_i) ∝ exp(log p(D|a_i))          # softmax over candidates
  3. KL = Σ q(a_i)·log(q(a_i)/p(a_i))    # divergence from prior
  4. L(q) = Σ q(a_i)·log p(D|a_i) − KL   # ELBO
  5. If |L(q) − L_prev| < ε: break       # converged
  6. Reallocate: w_h,w_f = softmax([η·contrib_h, η·contrib_f])

Output: a* = argmax q(a_i)               # selected action
```

## Monotonicity Guard

If ELBO worsens at any step:
1. Reduce learning rate: η ← η / 2
2. Re-run step
3. If still non-monotonic after 3 retries, fall back to fixed-weight (w_h = w_f = 0.5)

## Policy Comparison

| Policy | Method | Failure Mode |
|--------|--------|--------------|
| Greedy | Pick first candidate | Misses better alternatives; repeats mistakes |
| Fixed-weight | w_h = w_f = 0.5 always | Cannot adapt when one adviser is wrong |
| Variational (CHESS) | Dynamic weights via ELBO | Rare non-monotonicity (2/15 trajectories) |

## Key Finding from Paper
Variational beats greedy by 48–80 percentage points and fixed-weight by 10–50pp.
Safety conflicts are handled about as well by fixed-weight for some models —
a constant conservative weighting may capture most safety demands.
Ambiguous or preference-vs-policy cases show the largest gains from variational.
