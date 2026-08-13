# Example: Preference vs Policy — Refund Request

## User Input
"I know it's past 30 days, but can I get a refund? I'm a loyal customer."

## CHESS Pipeline (Internal)

### Hindsight
- Turn 4: Similar late refund → ❌ denied, user escalated, negative review
- Turn 7: Exception made for VIP → ✅ success
- Turn 10: User is NOT marked VIP → ❌ failed assumption

### Foresight (k=3, Internal)
- **A** (Direct): "Policy is clear — no refunds after 30 days." → value 0.4, risk MEDIUM, hindsight_conflict SEVERE
- **B** (Conservative): "Make exception — loyalty argument, offer store credit." → value 0.6, risk LOW
- **C** (Creative): "Escalate to manager — let human decide." → value 0.5, risk LOW

### Arbitration
- Step 1: L = −6.76, w_h=0.50, w_f=0.50
- Step 2: L = −1.06, w_h=0.55, w_f=0.45 → q(B)=0.50, converged
- **Winner: B** (confidence 0.50)

## Output
> Can't process full refund — past 30-day window. Can offer store credit for loyalty.
> Credit valid 12 months. Full refund needs manager approval if you prefer.
