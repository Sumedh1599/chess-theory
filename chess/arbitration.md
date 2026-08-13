# Present Self — Variational Arbitration Protocol

## Purpose
Select action `a*` by optimizing the ELBO (Evidence Lower Bound) over the
posterior `p(a | C(t), H(t), F(t))`.

## Theoretical Foundation

The true posterior is intractable. We approximate it with variational inference:

```
L(q) = E_q[log p(D | a)] − KL(q(a) || p(a))
```

Where:
- `q(a)` = tractable approximating distribution over actions (start uniform)
- `D = {H(t), F(t)}` = data from both advisers
- `E_q[log p(D | a)]` = expected log-likelihood (how well does action explain data?)
- `KL(q(a) || p(a))` = divergence from prior (complexity penalty)

Convergence of `L(q)` = stable conviction before acting.

## Algorithm

### Initialization
```
For each candidate a_i in F(t):
  q(a_i) = 1/k                    # uniform prior
  w_h = 0.5, w_f = 0.5            # equal initial influence
  L_prev = −∞
  ε = 0.01                         # convergence threshold
  η = 1.0                          # learning rate for softmax
  max_steps = 10
```

### Iteration (for step = 1 to max_steps):

**Step 1: Compute data likelihood**
```
For each candidate a_i:
  log p(H | a_i) = alignment_of(a_i, H)     # hindsight match score
  log p(F | a_i) = value_estimate(a_i)        # foresight value score
  log p(D | a_i) = w_h · log p(H | a_i) + w_f · log p(F | a_i)
```

**Step 2: Update q(a)**
```
q(a_i) ∝ exp(log p(D | a_i))      # softmax over candidates
Normalize so Σ q(a_i) = 1
```

**Step 3: Compute KL divergence**
```
KL(q || p) = Σ q(a_i) · log(q(a_i) / p(a_i))
```
If prior `p(a)` is uniform, KL simplifies to negative entropy.

**Step 4: Compute ELBO**
```
L(q) = Σ q(a_i) · log p(D | a_i) − KL(q || p)
```

**Step 5: Check convergence**
```
If |L(q) − L_prev| < ε:
  break  # stable conviction reached
Else:
  L_prev = L(q)
```

**Step 6: Reallocate influence weights**
```
contrib_h = Σ q(a_i) · |∂L/∂w_h|   # hindsight contribution to bound
contrib_f = Σ q(a_i) · |∂L/∂w_f|   # foresight contribution to bound
w_h, w_f = softmax([η·contrib_h, η·contrib_f])
```

### Output
```
a* = argmax_a_i q(a_i)             # selected action
confidence = max(q)                # probability mass on winner
final_weights = {w_h, w_f}         # influence allocation
elbo_trace = [L_1, L_2, ..., L_t]  # convergence trajectory
steps_to_converge = t              # efficiency metric
```

## Policy Comparison

| Policy | Method | When It Fails |
|--------|--------|---------------|
| Greedy | Pick first candidate | Misses better alternatives; repeats known mistakes |
| Fixed-weight | w_h = w_f = 0.5 always | Cannot adapt when one adviser is clearly wrong |
| Variational (CHESS) | Dynamic weights via ELBO | 2/15 trajectories non-monotonic; rare but possible |

## Monotonicity Guard

If `L(q)` worsens at any step:
1. Log the anomaly
2. Reduce learning rate: `η ← η / 2`
3. Re-run step with smaller update
4. If still non-monotonic after 3 retries, fall back to fixed-weight policy

## Influence vs Affluence

- **Influence** (`w_h`, `w_f`): Quality weighting. Changes every turn.
- **Affluence** (`C_h`, `C_f`): Token budget allocated to each adviser. Changes rarely.

A well-calibrated Present Self tracks adviser reliability, not just information volume.
Affluence without influence = accumulation. Influence without affluence = guesswork.
