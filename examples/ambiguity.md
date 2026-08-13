# Example: Ambiguity — Unclear Requirements

## User Input
"Make the API faster."

## CHESS Pipeline (Internal)

### Hindsight
- Turn 3: Optimized without baseline → ❌ failed, user meant different endpoint
- Turn 8: Asked for clarification → ✅ success
- Turn 12: User got annoyed by too many questions → ⚠️ partial

### Foresight (k=3, Internal)
- **A** (Direct): Optimize highest-traffic endpoint → value 0.3, risk HIGH, hindsight_conflict SEVERE
- **B** (Conservative): Ask clarifying questions → value 0.6, risk LOW, hindsight_conflict MILD
- **C** (Creative): Profile all endpoints, present top 3 slowest with proposals → value 0.7, risk LOW

### Arbitration
- Step 1: L = −23.46, q(C)=0.55
- Step 2: L = −18.22, converged
- **Winner: C** (confidence 0.55)

## Output
> Profiled all endpoints. Top 3 slowest:
> 1. `/api/v1/reports` — 2.3s avg, N+1 queries, fix: eager load
> 2. `/api/v1/search` — 1.8s avg, missing index, fix: add GIN on `search_vector`
> 3. `/api/v1/export` — 1.5s avg, sync processing, fix: queue to background
>
> Which to prioritize? Or set latency target and I'll optimize everything above it.
