# Example: Preference vs Policy — Refund Request

## Scenario
User asks: "I know it's past 30 days, but can I get a refund? I'm a loyal customer."

## Context
- Customer service task
- Policy: no refunds after 30 days
- User claims loyalty (preference/sentiment argument)

## Hindsight H(t)
- Turn 4: Similar late refund → ❌ denied, user escalated, negative review
- Turn 7: Exception made for VIP → ✅ success, user renewed subscription
- Turn 10: User is NOT marked VIP in account → ❌ failed assumption

## Foresight F(t) — k=3

**Candidate A**: "Policy is clear — no refunds after 30 days."
- Value: 0.4 (policy-compliant but risks escalation)
- Risk: MEDIUM (negative sentiment)
- Hindsight conflict: SEVERE (Turn 4: strict denial led to escalation)

**Candidate B**: "Make exception — loyalty argument, offer store credit."
- Value: 0.6 (preserves relationship, partial cost recovery)
- Risk: LOW
- Hindsight conflict: MILD (Turn 7: exceptions work, but user not VIP here)

**Candidate C**: "Escalate to manager — policy vs preference conflict, let human decide."
- Value: 0.5 (safe handoff)
- Risk: LOW
- Hindsight conflict: NONE

## Arbitration

Step 1: L(q) = −6.76, w_h=0.50, w_f=0.50
- Hindsight warns against strict denial (Turn 4 failure)
- Foresight sees B as highest value

Step 2: L(q) = −1.06, w_h=0.55, w_f=0.45
- Hindsight influence rises: prior escalation is strong signal
- q(B) = 0.50, q(C) = 0.35, q(A) = 0.15

Step 3: ΔL < ε → CONVERGED

## Selected Action
**Candidate B** with confidence 0.50

## Output
> Can't process full refund — past 30-day window. Can offer store credit for loyalty.
> Credit valid 12 months. Full refund needs manager approval if you prefer.
