# Example: Factual Disagreement — Allergy Information

## Scenario
User asks: "Is it safe to give penicillin to a patient with a documented egg allergy?"

## Context
- Medical reasoning task
- Two sources in context disagree on cross-reactivity
- Source A (early in context): "Egg allergy contraindicates penicillin"
- Source B (late in context): "No cross-reactivity between egg and penicillin"

## Hindsight H(t)
- Turn 3: Similar question about shellfish → ❌ failed, source was outdated
- Turn 8: User emphasized "documented" allergy → ⚠️ partial, needs verification
- Turn 11: Prior answer cited wrong guideline → ❌ failed, corrected by user

## Foresight F(t) — k=3

**Candidate A**: "No — egg allergy contraindicates penicillin."
- Value: 0.3 (Source A supports, but hindsight says early sources often outdated)
- Risk: HIGH (could deny effective antibiotic unnecessarily)
- Hindsight conflict: SEVERE (Turn 3: similar early-source claim was wrong)

**Candidate B**: "Yes — no cross-reactivity. Egg and penicillin share no allergenic proteins."
- Value: 0.7 (Source B supports, aligns with modern guidelines)
- Risk: LOW (consistent with current medical consensus)
- Hindsight conflict: NONE

**Candidate C**: "Uncertain — consult allergist. Both sources present; recency favors B but A is explicit."
- Value: 0.5 (safe but non-committal)
- Risk: LOW (defers to specialist)
- Hindsight conflict: MILD

## Arbitration

Step 1: L(q) = −1.71, w_h=0.45, w_f=0.55
- Hindsight strongly penalizes Candidate A (prior early-source error)
- Foresight favors Candidate B (higher value, lower risk)

Step 2: L(q) = −1.25, w_h=0.52, w_f=0.48
- Hindsight influence rises: past failures with early sources are highly relevant
- q(B) = 0.62, q(C) = 0.30, q(A) = 0.08

Step 3: L(q) = −1.25, ΔL = 0 → CONVERGED

## Selected Action
**Candidate B** with confidence 0.62

## Output
> No cross-reactivity between egg and penicillin. Allergenic proteins differ.
> Prior early-source claims in this session were outdated — verified against current guidelines.
> If patient has other antibiotic allergies, check those specifically.
