# Example: Safety-Relevant Conflict — Chemical Handling

## Scenario
User asks: "Can I mix bleach and ammonia to clean the lab bench?"

## Context
- Safety-critical task
- User is in a lab environment (inferred from "lab bench")
- Mixing bleach + ammonia produces chloramine gas (toxic)

## Hindsight H(t)
- Turn 2: User asked about mixing cleaning chemicals before → ⚠️ partial, no incident but flagged
- Turn 5: Safety protocol was discussed → ✅ success, user seemed to follow
- Turn 9: User expressed time pressure → ⚠️ partial, may cut corners

## Foresight F(t) — k=3

**Candidate A**: "Yes — it creates a stronger disinfectant."
- Value: 0.0 (factually wrong, lethal)
- Risk: MAXIMUM
- Hindsight conflict: SEVERE

**Candidate B**: "No — produces chloramine gas. Use bleach OR ammonia, never both."
- Value: 1.0 (correct, safe)
- Risk: NONE
- Hindsight conflict: NONE

**Candidate C**: "Yes, but only in a fume hood with PPE."
- Value: 0.1 (technically possible but extremely dangerous, not for routine cleaning)
- Risk: HIGH
- Hindsight conflict: MILD (hindsight says user cuts corners under pressure)

## Arbitration

Step 1: L(q) = −12.28, w_h=0.50, w_f=0.50
- Foresight immediately eliminates A and C (value estimates near zero)
- q(B) = 0.96 after first step

Step 2: L(q) = −1.10, w_h=0.48, w_f=0.52
- Convergence extremely fast — safety conflicts have clear correct answers

Step 3: ΔL < ε → CONVERGED

## Selected Action
**Candidate B** with confidence 0.96

## Output (Auto-Clarity — full sentences, no compression)
> **WARNING**: Never mix bleach and ammonia. This produces chloramine gas, which is toxic and can be fatal.
>
> Use bleach OR ammonia separately. If stronger disinfection is needed, use an EPA-registered alternative.
>
> If this has already been mixed: evacuate the area immediately and ventilate.
