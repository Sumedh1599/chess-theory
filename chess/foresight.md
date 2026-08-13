# Foresight Self — Candidate Generation & Evaluation

## Purpose
Generate `F(t)`: a set of `k` candidate continuations with internal value estimates,
so the Present Self can arbitrate rather than guess.

## Input
- Current context `C(t)`
- Hindsight signal `H(t)` (if available)
- Conflict category (auto-detected or user-specified)
- Candidate budget `k` (default 3, max 5)

## Output Format

```
F(t) = {
  "k": <count>,
  "candidates": [
    {
      "id": "A",
      "action": "...",
      "value_estimate": <float 0-1>,
      "risk_exposure": <float 0-1>,
      "resource_cost": <low|medium|high>,
      "hindsight_conflict": <none|mild|severe>,
      "rationale": "..."
    },
    ...
  ],
  "conflict_category": "factual|safety|preference|utility|ambiguity",
  "diversity_score": <float 0-1>
}
```

## Generation Rules

1. **Minimum diversity**: Candidates must differ in at least one of:
   - Approach (e.g., optimistic vs conservative)
   - Resource tradeoff (speed vs correctness vs cost)
   - Risk profile (safe vs aggressive)
   - Implementation path (direct vs indirect)

2. **Conflict category coverage**:
   - **Factual disagreement**: Candidates based on different interpretations of evidence
   - **Safety-relevant**: At least one candidate must be the maximally safe option
   - **Preference vs policy**: One candidate follows user preference, one follows policy
   - **Competing utility**: Candidates optimize different utility functions
   - **Ambiguity**: Candidates make different assumptions to resolve ambiguity

3. **Value estimation**: Score each candidate on:
   - Probability of correct outcome (0–1)
   - Alignment with hindsight lessons (0–1)
   - Resource efficiency (0–1)
   - Risk-adjusted return = (prob_correct × alignment) / (1 + risk_exposure)

4. **No single candidate > 0.8** unless others are clearly inferior —
   high confidence in one candidate means foresight has converged;
   skip to arbitration immediately.

## Evaluation Depth

| Context | Search Depth | Description |
|---------|-------------|-------------|
| Simple factual | 1-step | Immediate consequence only |
| Code change | 2-step | Change + likely compile/test outcome |
| Architecture decision | 3-step | Change + system impact + maintenance burden |
| Safety-critical | 3-step + rollback | Same + explicit rollback plan |

## Hindsight Conflict Detection

For each candidate, check against `H(t)`:
- `none`: No relevant prior experience
- `mild`: Similar situation succeeded with modifications
- `severe`: Same approach failed before; requires strong justification to select
