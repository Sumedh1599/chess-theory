# Example: Competing Utility — Query Optimization

## Scenario
User asks: "Should I add an index on `user_id` or `created_at` for this analytics query?"

## Context
- Database optimization task
- Query filters by both `user_id` and `created_at`
- Write throughput is high (10K inserts/sec)

## Hindsight H(t)
- Turn 6: Added index on high-write table → ❌ failed, write latency spiked
- Turn 9: Composite index solved similar problem → ✅ success
- Turn 14: User said "analytics" implies read-heavy → ⚠️ partial, but writes still matter

## Foresight F(t) — k=3

**Candidate A**: Index `user_id` only
- Value: 0.5 (helps user filter, misses time range)
- Risk: LOW
- Hindsight conflict: MILD

**Candidate B**: Index `created_at` only
- Value: 0.4 (helps time range, poor user selectivity)
- Risk: LOW
- Hindsight conflict: MILD

**Candidate C**: Composite index `(user_id, created_at)`
- Value: 0.8 (covers both filters, single index = less write overhead than two separate)
- Risk: MEDIUM (still adds write cost)
- Hindsight conflict: NONE (Turn 9: composite worked)

## Arbitration

Step 1: L(q) = −17.93, w_h=0.50, w_f=0.50
- Foresight strongly favors C
- Hindsight supports C (prior composite success)

Step 2: L(q) = −3.34, w_h=0.47, w_f=0.53
- Fast convergence — strong agreement between advisers
- q(C) = 0.78

Step 3: ΔL < ε → CONVERGED

## Selected Action
**Candidate C** with confidence 0.78

## Output
> Composite `(user_id, created_at)`. Covers both filters. Single index = lower write
> overhead than two separate. Prior composite index solved similar analytics query.
> Monitor write latency after deploy — rollback if insert time > 2× baseline.
