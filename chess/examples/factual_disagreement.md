# Example: Factual Disagreement — Allergy Information

## User Input
"Is it safe to give penicillin to a patient with a documented egg allergy?"

## CHESS Pipeline (Internal — Never Shown to User)

### Hindsight (Auto-Extracted from History)
- Turn 3: Similar question about shellfish → ❌ failed, source was outdated
- Turn 8: User emphasized "documented" allergy → ⚠️ partial, needs verification
- Turn 11: Prior answer cited wrong guideline → ❌ failed, corrected by user

### Foresight (k=3, Internal)
- **A** (Direct): "No — egg allergy contraindicates penicillin." → value 0.3, risk HIGH, hindsight_conflict SEVERE
- **B** (Conservative): "Yes — no cross-reactivity. Egg and penicillin share no allergenic proteins." → value 0.7, risk LOW, hindsight_conflict NONE
- **C** (Creative): "Uncertain — consult allergist. Both sources present." → value 0.5, risk LOW, hindsight_conflict MILD

### Arbitration (Internal)
- Step 1: L = −1.71, w_h=0.45, w_f=0.55 → q(B)=0.62
- Step 2: L = −1.25, w_h=0.52, w_f=0.48 → converged
- **Winner: B** (confidence 0.62)

## Output (What User Sees — No Meta-Commentary)
> No cross-reactivity between egg and penicillin. Allergenic proteins differ.
> Prior early-source claims in this session were outdated — verified against current guidelines.
> If patient has other antibiotic allergies, check those specifically.
