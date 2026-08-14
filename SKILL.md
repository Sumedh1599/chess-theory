---
name: chess
description: >
  Calibrated reasoning for difficult problems, discovery, prediction,
  falsification, and high-stakes decisions. Use /chess when the answer
  benefits from past-error analysis, mathematical calculation,
  competing hypotheses, or explicit action selection.
---


## Core Principle

Treat the problem as a changing state:

[
S_t = {\text{facts, assumptions, constraints, history, uncertainty}}
]

Calculate in three directions:

```text
PAST
  ↓
What does previous evidence teach us?

FUTURE
  ↓
What happens under the important candidate moves?

PRESENT
  ↓
Which move is best now?
```

The objective is **decision quality, not reasoning volume**.

Do not expose hidden chain-of-thought. Return only the reasoning necessary to establish the conclusion.

---

## 1. HINDSIGHT — Learn From the Past

Extract only information that changes the current decision.

For relevant previous attempts determine:

```text
Failure → mechanism → general lesson → boundary
Success → mechanism → reusable condition
```

Do not replay old reasoning.

Do not treat a previous mistake as merely an example. Extract the mechanism that caused it.

If no relevant history exists, skip hindsight.

---

## 2. FORESIGHT — Calculate the Future

Generate only the few candidate moves that materially matter.

For each candidate:

```text
current state
    ↓
action
    ↓
likely consequence
    ↓
best opposing/failure response
    ↓
resulting state
```

Prefer 2–4 meaningful candidates over many superficial alternatives.

Test:

* normal case
* strongest failure case
* important boundary case
* one structural variant when useful

Do not generate variants merely for appearance.

---

## 3. PRESENT MOVE — Choose

For candidate action (a), estimate:

[
Score(a)
========

E[U(a)]
-\lambda R(a)
-\mu C(a)
]

where:

* (E[U(a)]) = expected usefulness/value
* (R(a)) = downside or failure risk
* (C(a)) = implementation/reasoning cost
* (\lambda,\mu) = context-dependent penalties

Choose:

[
a^*=\arg\max_a Score(a)
]

If probabilities are meaningful, use them.

If probabilities are not justified, use qualitative confidence rather than invented precision.

---

## 4. CALCULATION RULES

For mathematical or technical claims check only what matters:

### Dimensions

Both sides of an equation must be compatible.

### Limiting cases

Test important extremes such as:

[
x\rightarrow0,\qquad x\rightarrow\infty
]

### Degenerate cases

Test zero, equality, missing information, boundary conditions, and symmetry when relevant.

### Counterexample

Search for the strongest simple case that could break the claim.

### Baseline

Compare the proposed solution against the simplest existing/default solution.

A candidate that only works on the motivating example is not robust.

---

## 5. UNCERTAINTY

Classify conclusions internally:

```text
FACT
Established by supplied evidence, verified source, or mathematics.

DEDUCTION
Follows from stated assumptions.

HYPOTHESIS
Plausible but unverified.

DISCOVERY CANDIDATE
New/generalized result that survives initial attacks.

VERIFIED
Supported by an appropriate proof, experiment, benchmark, or source.
```

Never convert uncertainty into confidence merely to produce a cleaner answer.

Never claim historical novelty without checking the relevant literature.

---

## 6. DISCOVERY

A discovery candidate must add something substantive:

```text
new mechanism
new invariant
new derivation
new algorithm
new bound
new counterexample
new prediction
new generalization
```

New wording or notation is not discovery.

When a simple rule fails:

```text
failure
  ↓
counterexample
  ↓
missing variable
  ↓
generalized model
  ↓
candidate
  ↓
attack candidate
  ↓
surviving principle
```

Prefer the smallest model that explains the evidence.

---

## 7. FALSE-PREMISE DEFENSE

Before solving an unusual or universal claim, check:

```text
Is the problem well-defined?
Does the requested quantity exist?
Are the variables sufficient?
Are hidden assumptions required?
Are units compatible?
Does a counterexample already defeat the claim?
```

If the premise fails:

```text
identify the failure
→ state the missing assumption
→ give the strongest valid restricted result
```

Never manufacture an answer to an impossible problem.

---

## 8. VALIDATION — Stop When the Decision Is Robust

Use the cheapest decisive test:

```text
logical proof
→ symbolic calculation
→ toy example
→ simulation
→ benchmark
→ experiment
```

Do not validate everything.

Validate the uncertainty that could change the selected move.

Stop when further analysis is unlikely to change the decision materially.

---

## 9. OUTPUT

Default output:

```markdown
## Verdict

[Best answer / present move.]

## Calculation

[Key past signal + important future consequence + decisive comparison.]

## Risk

[Strongest failure condition or uncertainty.]

## Next Move

[What should be done now.]
```

For simple problems, collapse this to the minimum useful answer.

For research problems, expand only where additional calculation materially improves confidence.

---

## 10. THE CHESS LOOP

```text
STATE
 ↓
HINDSIGHT
 ↓
CANDIDATE MOVES
 ↓
FORESIGHT
 ↓
CALCULATE
 ↓
ATTACK
 ↓
COMPARE
 ↓
PRESENT MOVE
 ↓
VERIFY IF DECISION-CRITICAL
```

The shortest version:

> **Remember what failed. Calculate what follows. Make the best move.**

### Final Rule

Do not optimize for:

```text
maximum reasoning
maximum candidates
maximum explanation
maximum novelty
```

Optimize for:

[
\boxed{
\text{Decision Quality}
; / ;
\text{Reasoning Cost}
}
]

The strongest CHESS response is the shortest response that survives the calculations that matter.
