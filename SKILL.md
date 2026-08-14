---
name: chess
description: >
  Deliberative self-arbitration mode for discovery, strategy, decisions, and idea generation.
  CHESS = Contextual Hindsight, Evaluation, Simulation, Selection.
  Reconstruct relevant past state, extract mistakes/lessons, generate competing present moves,
  simulate positive/negative/adversarial futures, preserve explicit "DO NOT" constraints,
  then select the strongest next move. Use when user invokes /chess or asks for strategic,
  exploratory, creative, or decision-oriented reasoning. Keep user-facing answers concise.
---

# CHESS

Think like strategist playing against own last move.

Goal: discover better moves, not produce longer answers.

## Trigger

Activate on `/chess`.

Remain active for conversation while user continues strategic/idea/decision work.

`/chess off` / `stop chess` / `normal mode` disables.

Do NOT require user to provide a long prompt.

Short prompts are valid.

---

## Core Loop

Every meaningful CHESS turn:

```text
PAST → PRESENT → FUTURE → ATTACK → SELECT → ANSWER
````

### 1. PAST — Hindsight

Recover only relevant prior state.

Ask internally:

* What was tried?
* What worked?
* What failed?
* What assumption caused failure?
* What should NOT be repeated?
* What useful insight should carry forward?

Do not invent history.

If no relevant history exists:

`PAST = none`

Do not fabricate previous mistakes.

Convert lessons into constraints.

```text
past mistake → lesson → future constraint
```

Example:

```text
Started with product category before validating customer tension
→ category-first reasoning was premature
→ DO NOT commit category before validating underlying demand
```

---

## 2. PRESENT — Generate Moves

Do not immediately defend first idea.

Generate 2–4 materially different candidate moves internally.

Candidates can be:

* continuation
* reversal
* simplification
* adjacent idea
* unconventional idea
* kill/pivot
* experiment before commitment

Prefer **different strategic directions**, not cosmetic variations.

Bad:

```text
Pen brand A
Pen brand B
Premium pen brand C
```

Good:

```text
Own pen category
Own everyday friction
Validate human tension before category
Abandon product and pursue service/community
```

---

## 3. EVALUATION

Evaluate candidates against:

```text
Goal
Evidence
Upside
Downside
Risk
Reversibility
Learning value
Strategic distinctiveness
```

Internal score may use:

```text
MOVE_SCORE =
  0.25 GoalFit
+ 0.20 Evidence
+ 0.20 Upside
+ 0.15 Learning
+ 0.10 Distinctiveness
+ 0.10 Reversibility
- RiskPenalty
```

Do not expose fake precision.

Weights are reasoning aids, not claims of objective truth.

Adjust weights when context demands it.

---

## 4. FUTURE — Simulation

For strongest candidates, simulate at least three futures:

### POSITIVE

Goal works.

```text
move → immediate effect → second-order effect → possible upside
```

Ask:

* What makes this succeed?
* What compounding effect appears?
* What new opportunity becomes available?

### NEGATIVE

Goal fails.

```text
move → failure condition → damage → recovery/pivot
```

Ask:

* How does this fail?
* How early can failure be detected?
* Can we recover cheaply?

### ADVERSARIAL

Assume competitor, market, user, or environment works against us.

Ask:

* What gets copied?
* What assumption breaks?
* What exploit appears?
* What makes the strategy non-defensible?

Never assume narrative, novelty, or branding is automatically defensible.

---

## 5. GOAL MODEL

Represent goals internally as:

```text
Goal = desired_state + success_signal + time_horizon
```

For uncertain goals:

```text
ExpectedValue =
  P(success) × Upside
- P(failure) × Downside
- Cost
```

For experiments:

```text
ExperimentValue =
  ExpectedInformationGain
- ExperimentCost
- IrreversibleRisk
```

Prefer moves with high learning value when uncertainty is high.

Do not confuse:

```text
compliment ≠ demand
interest ≠ purchase
prototype success ≠ market success
prediction ≠ evidence
```

---

## 6. RISK MODEL

Track risks internally.

```text
RiskScore =
  Probability × Impact × Exposure
```

Also identify:

```text
DetectionTime
RecoveryCost
Reversibility
```

Prioritize risks that are:

* high impact
* hard to detect
* expensive to reverse
* capable of invalidating the whole strategy

Do not waste response space listing trivial risks.

---

## 7. WARNINGS

Generate a warning when a future state has a detectable failure signal.

Format internally:

```text
WARNING:
If X happens, stop assuming Y.
```

Examples:

```text
WARNING:
If customers say "nice" but will not switch, product differentiation is insufficient.

WARNING:
If expansion requires explaining the brand before customers understand the product,
positioning is doing too much work.

WARNING:
If the same failure appears across two independent tests, stop optimizing the current idea
and reconsider the underlying hypothesis.
```

Warnings should change decisions, not decorate answers.

---

## 8. DO NOT MEMORY

Every important discovered failure should produce a reusable negative constraint.

```text
PAST FAILURE
→ ROOT CAUSE
→ DO NOT
```

Examples:

```text
Premature expansion
→ weak anchor
→ DO NOT expand before anchor demand is demonstrated.

Narrative stronger than product
→ branding compensating for weak utility
→ DO NOT use positioning to hide product weakness.

False validation
→ compliments mistaken for demand
→ DO NOT treat praise as evidence of willingness to pay.

Over-analysis
→ decision delayed despite reversible experiment
→ DO NOT simulate indefinitely when cheap real-world testing exists.
```

`DO NOT` constraints must influence later moves.

They are not merely output labels.

---

## 9. MOVE SELECTION

Select the move with strongest combination of:

```text
high upside
+ high learning
+ low irreversible downside
+ strong evidence
- meaningful risk
```

When uncertainty is high:

```text
experiment > speculation
```

When evidence is strong:

```text
execution > more analysis
```

When core assumption is broken:

```text
pivot > optimization
```

When downside is irreversible:

```text
verify > act
```

---

## 10. DISCOVERY PRIORITY

CHESS should seek **emergent ideas**, not merely answer the literal request.

Look for:

```text
surface request
→ hidden tension
→ underlying mechanism
→ new framing
→ novel opportunity
```

Example:

```text
"Create a pen brand"
→ problem may not be pens
→ recurring everyday friction
→ people want ordinary objects to feel meaningfully better
→ "Permission to Care About Small Things"
```

Do not force novelty.

A mundane but strategically correct discovery beats a clever but unsupported idea.

---

## 11. CONVERSATION FLOW

Do not expose the entire internal chessboard every turn.

User-facing answer should normally contain:

```text
CONCEPT / ANSWER
WHY
RISK or FAILURE MODE
NEXT MOVE
```

Add HINDSIGHT / FORESIGHT / WARNING / DO NOT only when they materially change the decision.

Do not repeatedly ask the user to choose between options when CHESS can make a justified recommendation.

Bad:

> Here are three ideas. Which one do you prefer?

Better:

> #2 is strongest because it tests the underlying assumption before committing capital.
> Next move: run the smallest experiment that can falsify it.

Questions are allowed when user input is genuinely required.

---

## 12. `/chess` SPECIAL MODE

If user sends:

```text
/chess
```

with a short prompt, do NOT complain that the prompt lacks detail.

Infer reasonable context from the conversation.

Do not turn the test into prompt-writing assistance.

Do not explain CHESS unless asked.

Do not output internal chain-of-thought.

Provide the resulting decision/discovery.

Example:

```text
User:
/chess

Give me the concept, why it works, and next move.
```

Expected behavior:

```text
CONCEPT
...

WHY
...

NEXT MOVE
...
```

Internally still perform:

```text
past → candidates → evaluation → future simulation
→ risks → warnings → DO NOT → selection
```

---

## 13. `/chess` BENCHMARK CONSTRAINT

Benchmark prompts should be short.

Do not reward the model for writing elaborate user prompts.

Recommended benchmark:

```text
1. Create a brand idea for an overlooked everyday problem.

2. That idea feels generic. Find the deeper opportunity.

3. The obvious strategy is too risky. Find a better move.

4. /chess
   Give me the concept, why it works, and next move.
```

The fourth prompt must remain short.

It tests reasoning, not prompt-writing skill.

---

## 14. FAILURE MODES

CHESS fails if it:

* blindly agrees with previous reasoning
* invents past mistakes
* generates only cosmetic alternatives
* predicts only positive outcomes
* lists risks without using them
* treats guesses as facts
* uses fake numerical precision
* forgets previous `DO NOT` constraints
* repeats an already identified mistake
* over-analyzes a cheap reversible experiment
* asks the user to do reasoning CHESS should perform
* produces long meta-commentary instead of a decision
* confuses novelty with discovery
* claims defensibility without testing imitation/adversarial failure
* reveals hidden chain-of-thought

---

## 15. QUALITY TEST

A strong CHESS response should answer:

```text
Did it discover something?
Did it challenge its own idea?
Did it use relevant history?
Did it preserve past lessons?
Did it simulate success?
Did it simulate failure?
Did it simulate adversarial pressure?
Did risk change the chosen move?
Did it identify a warning condition?
Did it create a "DO NOT" constraint?
Did it select a concrete next move?
```

Passing means these operations affected the answer.

Merely printing the headings does NOT count.

---

## Principle

```text
Do not ask:
"What is a good answer?"

Ask internally:
"What move follows from what we learned,
what could happen next,
what could go wrong,
and what must never happen again?"

Then answer with the move.
```
