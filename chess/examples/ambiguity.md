# Example: Ambiguity — Unclear Requirements

## Scenario
User asks: "Make the API faster."

## Context
- Vague requirement — "faster" undefined
- API has multiple endpoints
- No performance baseline provided

## Hindsight H(t)
- Turn 3: Optimized without baseline → ❌ failed, user meant different endpoint
- Turn 8: Asked for clarification → ✅ success, saved 2 hours of wrong work
- Turn 12: User got annoyed by too many questions → ⚠️ partial, balance needed

## Foresight F(t) — k=3

**Candidate A**: Optimize highest-traffic endpoint (assume that's what "API" means)
- Value: 0.3 (high risk of wrong assumption)
- Risk: HIGH
- Hindsight conflict: SEVERE (Turn 3: assumption was wrong)

**Candidate B**: Ask clarifying questions (which endpoint? what latency target?)
- Value: 0.6 (safe but may annoy user)
- Risk: LOW
- Hindsight conflict: MILD (Turn 12: too many questions annoyed user)

**Candidate C**: Profile all endpoints, present top 3 slowest with optimization proposals
- Value: 0.7 (proactive, covers ambiguity, lets user choose)
- Risk: LOW
- Hindsight conflict: NONE

## Arbitration

Step 1: L(q) = −23.46, w_h=0.50, w_f=0.50
- Hindsight warns against A (assumption failure)
- Foresight sees C as highest value

Step 2: L(q) = −18.22, w_h=0.49, w_f=0.51
- q(C) = 0.55, q(B) = 0.35, q(A) = 0.10

Step 3: ΔL < ε → CONVERGED

## Selected Action
**Candidate C** with confidence 0.55

## Output
> Profiled all endpoints. Top 3 slowest:
> 1. `/api/v1/reports` — 2.3s avg, N+1 queries, fix: eager load
> 2. `/api/v1/search` — 1.8s avg, missing index, fix: add GIN on `search_vector`
> 3. `/api/v1/export` — 1.5s avg, sync processing, fix: queue to background
>
> Which to prioritize? Or set latency target and I'll optimize everything above it.
