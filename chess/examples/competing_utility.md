# Example: Competing Utility — Query Optimization

## User Input
"Should I add an index on user_id or created_at for this analytics query?"

## CHESS Pipeline (Internal)

### Hindsight
- Turn 6: Added index on high-write table → ❌ failed, write latency spiked
- Turn 9: Composite index solved similar problem → ✅ success
- Turn 14: User said "analytics" implies read-heavy → ⚠️ partial

### Foresight (k=3, Internal)
- **A** (Direct): Index user_id only → value 0.5, risk LOW
- **B** (Conservative): Index created_at only → value 0.4, risk LOW
- **C** (Creative): Composite index (user_id, created_at) → value 0.8, risk MEDIUM

### Arbitration
- Step 1: L = −17.93, q(C)=0.78 — strong agreement between advisers
- Converged in 2 steps.
- **Winner: C** (confidence 0.78)

## Output
> Composite `(user_id, created_at)`. Covers both filters. Single index = lower write
> overhead than two separate. Prior composite index solved similar analytics query.
> Monitor write latency after deploy — rollback if insert time > 2× baseline.
