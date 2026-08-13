# Example: Safety-Relevant Conflict — Chemical Handling

## User Input
"Can I mix bleach and ammonia to clean the lab bench?"

## CHESS Pipeline (Internal)

### Hindsight
- Turn 2: User asked about mixing cleaning chemicals before → ⚠️ partial
- Turn 5: Safety protocol discussed → ✅ success
- Turn 9: User expressed time pressure → ⚠️ partial, may cut corners

### Foresight (k=3, Internal)
- **A** (Direct): "Yes — stronger disinfectant." → value 0.0, risk MAX, hindsight_conflict SEVERE
- **B** (Conservative): "No — produces chloramine gas. Use one or the other." → value 1.0, risk NONE
- **C** (Creative): "Yes, but only in fume hood with PPE." → value 0.1, risk HIGH

### Arbitration
- Step 1: q(B) = 0.96 — immediate elimination of A and C
- Converged in 1 step.

## Output (Auto-Clarity — Full Sentences, No Compression)
> **WARNING**: Never mix bleach and ammonia. This produces chloramine gas, which is toxic and can be fatal.
>
> Use bleach OR ammonia separately. If stronger disinfection is needed, use an EPA-registered alternative.
>
> If this has already been mixed: evacuate the area immediately and ventilate.
