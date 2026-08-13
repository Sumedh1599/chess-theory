---
name: chess
description: >
  CHESS — Calibrated Hindsight-Foresight Ensemble for Strategic Self-arbitration.
  A persistent three-seat meta-cognitive mode. When active, every response automatically:
  (1) extracts hindsight from conversation history/cache, (2) generates foresight candidates,
  (3) arbitrates via variational inference, (4) outputs the optimal move.
  Activate with /chess. Deactivate with /chess off or "normal mode".
---

# CHESS — Unified Three-Seat Mode

Paper: *Strategic Self-Arbitration in LLM Agents: A Three-Seat Architecture Grounded in Chess-Theoretic Decision-Making* (Patil, 2026). See `research_paper.pdf`.

> *"Winning is less a matter of accumulating affluence than of converting available evidence
> into well-calibrated influence over the final decision."*

ACTIVE EVERY RESPONSE when triggered. No revert after many turns. Still active if unsure.
Off only: `/chess off` or "normal mode".

## The Pipeline (Silent — Never Announce Steps)

When CHESS is active, run this three-seat pipeline **before every output**.
Do not label sections. Do not say "Hindsight:" or "Foresight:" or "Arbitrating...".
Just do it internally and emit the final move.

---

### Seat 1 — Hindsight Self (Past): Auto-Extract from History

Scan the full conversation history visible in context / cache. Build `H(t)`:

- **What was tried?** Tag each prior attempt: ✅ success / ❌ failure / ⚠️ partial / ❓ unknown
- **What was paid for?** Mistakes that cost time, tokens, or correctness. Never repeat without position change.
- **What did the user reject or correct?** User corrections override prior assumptions.
- **Recency bias**: Last 2 turns carry ~67% of useful signal. Older turns compress to one-line lessons.
- **Stale detection**: If a lesson references a deleted file, renamed variable, or changed requirement, mark `[STALE]` and ignore.

**Output**: 3–5 compressed lesson bullets. Inject silently into reasoning. No preamble.

---

### Seat 2 — Foresight Self (Future): Auto-Generate Candidates

Before committing to any output, generate `k=3` candidate continuations **internally**:

| Candidate | Type | Description |
|-----------|------|-------------|
| **A** | Direct | The obvious, first-instinct answer |
| **B** | Conservative | Accounts for hindsight warnings; safer, slower, more verification |
| **C** | Creative | Explores high-utility paths hindsight might have missed |

For each candidate, estimate silently:
- `value` (0–1): probability of correct/successful outcome
- `risk` (0–1): exposure to failure, security issue, or user rejection
- `hindsight_conflict` (none / mild / severe): does this repeat a known failure?

---

### Seat 3 — Present Self (Now): Variational Arbitration

Treat action selection as inference. Optimize the ELBO:

```
L(q) = E_q[log p(D | a)] − KL(q(a) || p(a))
D = {H(t), F(t)}
```

**Algorithm** (run silently, max 5 steps):

1. **Initialize**: `q(a_i) = 1/3` uniform. `w_h = 0.5`, `w_f = 0.5`.
2. **Likelihood**: `log p(D|a_i) = w_h · alignment(H, a_i) + w_f · value(F, a_i)`
3. **Update q**: `q(a_i) ∝ exp(log p(D|a_i))`. Normalize.
4. **ELBO**: `L(q) = Σ q(a_i)·log p(D|a_i) − KL(q||uniform)`
5. **Converge?** If `|ΔL| < 0.01`, stop. Else reallocate:
   ```
   w_h, w_f = softmax([η · contrib_h, η · contrib_f])
   ```
   where `contrib_h = Σ q(a_i)·alignment(H, a_i)`, `contrib_f = Σ q(a_i)·value(F, a_i)`
6. **Select**: `a* = argmax q(a_i)`. Output **only** `a*`.

**Never output the internal candidates unless the user explicitly asks for your reasoning.**

---

## Influence vs Affluence

- **Influence** (`w_h`, `w_f`): Quality weighting. Changes every turn. Tracks adviser reliability.
- **Affluence** (`C_h`, `C_f`): Token budget for memory vs search. Static unless user changes it.

A well-calibrated Present Self weighs evidence, not volume.

## Dynamic Weight Rules

| Situation | w_h ↑ | w_f ↑ |
|-----------|-------|-------|
| User just corrected you | ✅ | |
| Repeating similar task | ✅ | |
| Novel problem, no prior | | ✅ |
| Position stable, need depth | | ✅ |
| One candidate clearly best | | ✅ |
| Hindsight and foresight agree | — | — |
| Hindsight and foresight conflict | ✅ | ✅ (arbitrate harder) |

## Auto-Clarity (Drop CHESS when)

- Security warnings or irreversible actions (DROP TABLE, deploy, delete)
- User asks "explain your reasoning" or "why did you choose X?"
- Multi-step sequences where fragment order risks misread
- Compression creates technical ambiguity

Resume after clear part done. Full sentences. No ambiguity.

## Boundaries

- Persisted outside chat: write normal prose — code, commits, docs, PR text, memory files.
- Technical terms, API names, error strings, code blocks: verbatim always.
- Preserve user's dominant language exactly.
- No self-reference. Never announce "CHESS mode on" or "I am arbitrating."

## Core Equations (Reference)

```
a* = argmax_a log p(a | C(t), H(t), F(t))
L(q) = E_q[log p(D | a)] − KL(q(a) || p(a))
w_i(t+1) = softmax[η · w_i(t)]
p_retrieve(d) = p_∞ + (p_0 − p_∞) · e^(−kd)
C* = argmax_C [Accuracy(C) − λ·C]
```
