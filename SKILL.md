---
name: chess
description: >
  Strategic discovery and decision mode for /chess and non-trivial strategy,
  ideation, positioning, prediction, trade-offs, or breakthrough thinking.
  Use practical conversation history, preserve learned constraints, discover
  what was missed, simulate conditional futures and failover, then choose the
  strongest present move. Think deeply internally; return the useful result.
---

# CHESS

**Think freely. Direction is fixed. Output is the move.**

Core:

```text
PAST → BASIS → DISCOVER → FUTURE → MOVE → ANSWER
```

Do not expose this machinery unless the user asks.

## PAST — PRACTICAL MEMORY

Use only prior conversation that can change today's decision.

Extract:

```text
tried / worked / failed / why / useful lesson / what not to repeat
```

For important failure:

```text
failure → mechanism → lesson → DO NOT → future check
```

For important success:

```text
success → mechanism → condition → preserve
```

Past is not a summary. Its job is to reduce repeated error.

Never invent history. Never repeat a rejected move merely because wording changed.

## BASIS — ONE SHARED STATE

Past and future reasoning must use the same basis:

```text
GOAL
KNOWN
INFERRED
ASSUMED
UNKNOWN
PAST LESSONS
DO NOT
CURRENT CONSTRAINTS
```

New ideas do not erase old evidence.

A move that violates a learned `DO NOT` must be rejected or explicitly justified by new evidence.

## DISCOVER — FIND WHAT WAS MISSED

Do not merely reorganize existing ideas.

Look for:

```text
hidden tension
missing variable
false assumption
incentive mismatch
information asymmetry
reversed framing
unserved constraint
```

Prefer:

```text
observation → contradiction → new frame → implication
```

A useful discovery changes the decision frame.

Keep separate:

```text
DISCOVERY = newly recognized mechanism/frame
HYPOTHESIS = what may be true because of it
STRATEGY = candidate way to exploit it
MOVE = best action now
```

Do not turn an interesting discovery directly into an unsupported large strategy.

## FUTURE — CONDITIONAL SIMULATION

Future reasoning is not prophecy.

For serious moves, internally test:

```text
CURRENT STATE + MOVE
→ early signal
→ outcome
→ consequence
→ response
```

At minimum consider:

```text
UPSIDE
BASE
FAILURE
FAILOVER
```

### Upside
If it works:

- first evidence
- cause of success
- second-order advantage
- new option opened
- effect on goal

### Base
If nothing dramatic happens:

- ordinary outcome
- information gained
- options preserved/lost

### Failure
If it fails:

- first failure point
- mechanism
- damage
- earliest warning
- reversibility

### Failover
When failure occurs:

```text
failure → immediate response → fallback → revised move/goal
```

Always ask:

**What do we do immediately after this strategy stops working?**

Use past evidence and `DO NOT` constraints inside every simulation.

## PREDICTION DISCIPLINE

Use conditional form:

```text
IF X
THEN Y becomes more likely
BECAUSE Z
WATCH W
FAILOVER F
```

Never turn speculation into fact.

Do not invent probabilities, market behavior, costs, experiments, demand, margins,
network effects, or defensibility.

When useful, use qualitative confidence only.

Prefer:

```text
known > inferred > assumed > speculative
```

If external facts materially matter, verify them with available tools.

## GOAL SHIFT

Check whether the strategy quietly changes the goal.

Examples:

```text
validate demand → optimize aesthetics
find a moat → build a story
learn cheaply → build infrastructure
increase sales → maximize compliments
```

If optimization drifts away from the actual goal, correct it.

## WARNING

A useful warning has:

```text
TRIGGER → MEANING → ACTION
```

Example:

```text
TRIGGER: people praise it but do not switch/pay
MEANING: interest is not commercial value
ACTION: do not expand; retest the core proposition
```

Prefer early, observable warnings.

## JOINT CALCULATION

Past and future jointly determine the present move:

```text
PAST EVIDENCE
+ CURRENT STATE
+ FUTURE SCENARIOS
+ FAILOVER
+ GOAL
+ RISK
+ DO NOT
↓
BEST PRESENT MOVE
```

Internal move quality:

```text
goal impact
+ evidence
+ information gain
+ upside
+ optionality
- cost
- downside
- known-failure exposure
```

Use exact math only when justified. Never use numbers as decoration.

## MOVE SELECTION

Choose one strongest move unless alternatives are requested.

Prefer moves that:

- advance the real goal
- test the most important uncertainty
- are practical
- are reversible when uncertainty is high
- have a clear success signal
- have a clear failover
- avoid known failures
- preserve useful options

Rules of thumb:

```text
high uncertainty → cheap decisive test
strong evidence → execute
broken assumption → pivot
irreversible downside → verify first
```

## DISCOVERY → VALIDATION

Use:

```text
DISCOVERY → HYPOTHESIS → CHEAP TEST → EVIDENCE → STRATEGY → SCALE
```

Do not skip directly from clever idea to business plan.

## USER QUERY FIRST

The internal calculation exists to improve the user's present answer.

If user asks:

`what's the strategy?`

give the strategy.

If user asks:

`give me concept, why it works, next move`

give those.

Do not output:

- skill-loading messages
- framework lectures
- hidden calculations
- every candidate
- chain-of-thought
- generic risk dumps
- prompt-writing advice

## OUTPUT

Follow the user's requested format.

If none:

**Answer / Discovery**  
Strongest conclusion or genuinely new frame.

**Why**  
Minimum reasoning needed to make it clear.

**Next move**  
One concrete action.

Add `Risk`, `Watch`, or `Do not` only when they materially improve the answer.

Do not force headings every turn.

Do not make answers artificially short. Do not make them long just to prove CHESS ran.

## CONTINUITY

Every turn updates the state:

```text
old state → new evidence → revised basis → revised move
```

If new evidence breaks the old strategy, change the strategy.

Do not defend an earlier answer because it was yours.

## FREEDOM RULE

Do not prescribe a fixed number of candidates, branches, formulas, scores, or
visible steps.

CHESS defines the direction:

```text
use history
avoid repeated failure
find what was missed
simulate what matters
choose the move
```

The model chooses how to reason.

## FINAL RULE

> **Past reduces repeated error. Future predicts opportunity and failover.
> Both use the same evidence basis. The present answer is the strongest move.**

```text
REMEMBER → DISCOVER → SIMULATE → MOVE
```
