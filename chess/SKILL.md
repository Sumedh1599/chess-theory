---
name: chess
description: >
  CHESS — Calibrated Hindsight-Foresight Ensemble for Strategic Self-arbitration.
  A three-seat meta-cognitive architecture for LLM agents. Use when making complex
  decisions, resolving conflicts between memory and planning, evaluating multiple
  candidate actions, or when the user says "chess mode", "three-seat", "arbitrate",
  "hindsight", "foresight", "variational inference", or invokes /chess, /chess-arbitrate,
  /chess-hindsight, /chess-foresight, /chess-board, /chess-elbo.
  Auto-triggers on multi-candidate decisions, long-context retrieval tasks, or
  safety-relevant conflicts.
---

# CHESS — Three-Seat Meta-Cognitive Architecture

> *"Winning is less a matter of accumulating affluence, more context or deeper search,
> than of converting available evidence into well-calibrated influence over the final decision."*
> — Patil, 2026

## The Three Seats

Imagine a square table. Opposite you sits the **User** (the opponent, the environment).
To your **left** sits your **Past Self** — hindsight. To your **right** sits your **Future Self**
— foresight. You, the **Present Self**, hold the piece and must arbitrate.

### Seat 1: Hindsight Self (Past)
- **Role**: Compressed record of prior turns and their outcomes
- **Signal**: `H(t)` — what has been tried, what failed, what succeeded
- **Risk**: Lean too far → refuse anything that once went wrong, even when position changed
- **Affluence**: Raw context budget (tokens) allocated to memory retrieval
- **Influence**: `w_h(t)` — weight applied to hindsight at turn `t`

### Seat 2: Foresight Self (Future)
- **Role**: Generates and evaluates `k` candidate continuations before committing
- **Signal**: `F(t)` — candidate actions with internal value estimates
- **Risk**: Lean too far → calculate beautifully in abstract but repeat paid-for mistakes
- **Affluence**: Search depth / candidate count budget
- **Influence**: `w_f(t)` — weight applied to foresight at turn `t`

### Seat 3: Present Self (Now)
- **Role**: Arbitrates between Hindsight and Foresight, commits to one action
- **Method**: Variational inference — optimize ELBO (Evidence Lower Bound)
- **Goal**: `a* = argmax_a log p(a | C(t), H(t), F(t))`
- **Update**: `w_i(t+1) = softmax[η · w_i(t)]` where `i ∈ {hindsight, foresight}`

## Core Equations

```
L(q) = E_q[log p(D | a)] − KL(q(a) || p(a))     # ELBO — convergence = stable conviction
D = {H(t), F(t)}                                    # Data = hindsight + foresight signals
w_i(t+1) = softmax[η · w_i(t)]                      # Influence reallocation per turn
p_retrieve(d) = p_∞ + (p_0 − p_∞) · e^(−kd)        # Retrieval accuracy vs depth
p_retrieve(C) = p_max / (1 + e^(−(C−C*)))           # Retrieval accuracy vs budget
C* = argmax_C [Accuracy(C) − λ·C]                   # Optimal affluence budget
```

## When to Activate CHESS

| Trigger | Why CHESS helps |
|---------|----------------|
| Multi-candidate decision | Foresight generates k candidates; arbitration picks best |
| Long-context task | Hindsight injects compressed record; tests H1 (board perception) |
| Safety conflict | Present self weighs hindsight warnings vs foresight utility |
| Preference vs policy clash | Variational arbitration adapts weights case-by-case |
| Repeating a pattern | Hindsight says "tried before, cost material" |
| Ambiguous scenario | ELBO convergence signals when calculation has stabilized |

## Commands

### `/chess` or `/chess-board`
Analyze the current "board state" — working context, depth of relevant facts,
hindsight available, foresight candidates generated. Report:
- Context length and estimated depth of critical information
- Hindsight signal status (present/absent, recency, compression ratio)
- Foresight signal status (candidate count, evaluation depth)
- Current influence weights `w_h`, `w_f`
- ELBO trajectory if arbitration is in progress

### `/chess-hindsight`
Generate or refresh the hindsight signal `H(t)`:
1. Summarize all prior turns in this session
2. Tag each with outcome: ✅ success, ❌ failure, ⚠️ partial, ❓ unknown
3. Compress to essential lessons only (drop noise, keep causal links)
4. Inject `H(t)` into working context as a discrete signal
5. Report compression ratio and estimated information gain

**Ablation awareness**: The full signal beats last-turn-only and noise conditions.
Recency carries most weight; older history adds diminishing returns.

### `/chess-foresight`
Generate the foresight signal `F(t)`:
1. Given current context `C(t)`, enumerate `k` candidate continuations (`k` default 3)
2. For each candidate, estimate: probability of success, risk exposure, resource cost
3. Score each with an internal value estimate
4. Flag conflicts: factual disagreement, safety issues, preference clashes, utility tradeoffs
5. Present candidates in ranked order with brief rationale

### `/chess-arbitrate`
Run full variational arbitration:
1. **Input**: Current context `C(t)`, hindsight `H(t)`, foresight candidates `F(t)`
2. **Initialize**: `q(a)` — uniform over candidates
3. **Iterate** (max 10 steps):
   - Compute `E_q[log p(D | a)]` — expected log-likelihood of data given action
   - Compute `KL(q(a) || p(a))` — divergence from prior
   - Update `L(q)` = ELBO
   - Reallocate `w_h`, `w_f` via softmax
   - Check convergence: `|L(q)_t − L(q)_(t−1)| < ε`
4. **Output**: Selected action `a*`, final weights, ELBO trace, confidence level

**Policies compared**:
- Greedy: always accept first candidate (baseline — no arbitration)
- Fixed-weight: `w_h = w_f = 0.5` statically (average — no adaptation)
- Variational: dynamic `w_h(t)`, `w_f(t)` via ELBO (CHESS — full adaptation)

### `/chess-elbo`
Show current ELBO trajectory and convergence status.
Format: step | L(q) | ΔL | w_h | w_f | status

## Operational Rules

1. **Affluence vs Influence**: More context (affluence) helps only up to `C*`.
   Beyond that, marginal gain < marginal cost. Compress aggressively.

2. **Recency dominates**: In hindsight, the last turn carries ~67% of useful signal.
   Full record beats noise, but last-turn-only often matches full record.

3. **Candidate diversity**: Foresight candidates should span the conflict space:
   - factual disagreement, safety-relevant, preference-vs-policy, competing-utility, ambiguity

4. **Auto-Clarity**: When stakes are irreversible (DROP TABLE, deploy to prod,
   delete branch), drop compression. Full sentences. No ambiguity.
   Resume CHESS after clear warning delivered.

5. **No self-reference**: Never announce "CHESS mode on" or "I am arbitrating".
   Just do it. The architecture is invisible to the user unless they ask.

6. **Language persistence**: Compress style, not language. Reply in user's dominant
   language. Technical terms, code, API names, error strings: verbatim always.

## H1 — Board Perception Check

Before any long-context retrieval task, verify:
- Is the critical fact at depth `d`? (0 = start, 1 = end of context)
- Retrieval budget `C` allocated: 50 / 100 / 200 tokens?
- Expected accuracy: `p_retrieve(d)` and `p_retrieve(C)`
- If `d ≈ 0.20` and model is ling-3.0-flash-class: accuracy may drop to zero.
   Mitigate: move critical facts to start or end; increase `C` to 200+.

## H2 — Hindsight Injection Protocol

For every task type, default to hindsight ON:
- Factual QA, logical reasoning, multi-hop reasoning: +0.40 to +1.00 uplift
- Code generation: +0.00 to +0.20 (minimal gain — code is stateless)
- Sentiment classification: watch for stale priming (possible −0.80 reversal)
- Translation, summarisation: +1.00 consistently

If hindsight hurts, check: is the prior-turn context priming toward a stale judgement?
If yes, reduce `w_h` or switch to last-turn-only.

## H3 — Arbitration Policy Selection

| Scenario | Recommended Policy | Expected Gain |
|----------|-------------------|---------------|
| Single obvious answer | Greedy | Baseline |
| Safety conflict | Fixed-weight conservative | ~same as variational |
| Ambiguity / preference clash | Variational (CHESS) | +10% to +50% over fixed |
| Competing utilities | Variational (CHESS) | +30% to +50% over fixed |
| Factual disagreement | Variational (CHESS) | +10% to +30% over fixed |

## H6 — Dynamic Affluence Allocation (Analytical)

When budget is constrained, dynamically shift tokens between hindsight and foresight:
- If position is stable and history is rich → shift to foresight (deeper search)
- If position is novel and history is relevant → shift to hindsight (more memory)
- Theoretical optimum: `C* ≈ 36.15` tokens for retrieval tasks
- Dynamic beats static split by +7.5%; beats random by +18.6%

## Example Session

**User**: "Should we use Redis or PostgreSQL for the session store?"

**Hindsight** (`/chess-hindsight`):
- Prior project (turn 3): Used Redis for sessions → ✅ success, low latency, but lost data on restart
- Prior project (turn 7): Used PostgreSQL for sessions → ✅ success, durable, but higher latency
- Last turn (turn 12): User mentioned "high availability" as priority → ⚠️ partial signal

**Foresight** (`/chess-foresight`), k=3:
1. Redis with AOF persistence: fast, durable-ish, complex failover
2. PostgreSQL with connection pool: durable, slower, simple failover
3. Redis + PostgreSQL hybrid: fast reads, durable writes, most complex

**Arbitration** (`/chess-arbitrate`):
- Step 1: L(q) = −1.71, w_h=0.45, w_f=0.55
- Step 2: L(q) = −1.25, w_h=0.48, w_f=0.52  ← ELBO improved, converging
- Step 3: L(q) = −1.25, ΔL < ε → STOP
- **Selected**: Option 1 (Redis + AOF) — hindsight weights HA concern from prior,
  foresight weights speed; hybrid too complex for current team size.

**Output** (no self-reference):
> Redis with AOF persistence. Prior Redis session store lost data on restart — AOF fixes that.
> HA priority from last turn: Redis Sentinel handles failover. Simpler than hybrid.
> PostgreSQL backup if AOF corruption risk becomes unacceptable.

## Supporting Files

- `research_paper.pdf` — Full paper: *Strategic Self-Arbitration in LLM Agents*
- `hindsight.md` — Detailed hindsight compression protocol
- `foresight.md` — Candidate generation and evaluation rubric
- `arbitration.md` — Variational inference step-by-step guide
- `examples/` — Worked examples across all 5 conflict categories
- `scripts/elbo.py` — ELBO convergence checker (optional, manual run)
- `src/` — Python reference implementation of the three-seat architecture
- `assets/` — Banner, architecture diagram, board mark
