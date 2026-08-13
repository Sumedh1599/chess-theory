# Foresight Self — Auto-Generation Protocol

## What It Does
Before every output, CHESS internally generates `k=3` candidate continuations
and scores them so the Present Self can arbitrate instead of guessing.

## The Three Candidates (Always)

| ID | Type | When It Wins |
|----|------|--------------|
| A | Direct | Obvious answer, no conflicts, user wants speed |
| B | Conservative | Hindsight warns of risk; safety or correctness priority |
| C | Creative | Hindsight is stale or incomplete; novel path has higher utility |

## Silent Scoring (Internal Only)

For each candidate, estimate:
- `value` (0–1): probability of correct/successful outcome
- `risk` (0–1): exposure to failure, security issue, or user rejection
- `hindsight_conflict` (none/mild/severe): does this repeat a known failure?

## Conflict Categories (Auto-Detect)

- **Factual disagreement**: Different interpretations of evidence
- **Safety-relevant**: At least one candidate must be maximally safe
- **Preference vs policy**: One follows user preference, one follows policy
- **Competing utility**: Candidates optimize different utility functions
- **Ambiguity**: Candidates make different assumptions to resolve ambiguity

## Key Finding from Paper
The single largest gain is simply considering more than one candidate at all.
Variational arbitration adds a further +10–50% over fixed-weight averaging.
