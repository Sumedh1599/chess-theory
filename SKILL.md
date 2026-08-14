---
name: chess
description: >
  Strategic discovery and decision mode. Use when the user invokes /chess or
  asks for a non-trivial strategy, idea, positioning, decision, prediction,
  trade-off, or breakthrough. Use the conversation as accumulated evidence:
  learn from what already failed or worked, discover a better frame, consider
  plausible futures, and give the strongest present move. Think freely and
  deeply internally; do not expose the deliberation unless the user asks.
---

# CHESS

**Think freely. Direction is fixed; reasoning is not.**

CHESS exists to improve the **present answer** using the **past conversation**
and plausible **future consequences**.

Do not turn this into a visible checklist, consulting report, or reasoning dump.

## Core

Internally do this:

```text
PAST → DISCOVER → FUTURE → SELECT → ANSWER
```

### PAST
Use relevant conversation history as evidence.

Recover:
- what was tried
- what worked
- what failed
- why it failed
- what should be preserved
- what must not be repeated

Convert important failures into internal guardrails:

```text
failure → mechanism → lesson → DO NOT
```

A `DO NOT` constraint must affect later idea generation and choice.

Do not invent history. Do not repeat a rejected move just because it has been
reworded.

### DISCOVER
Do not merely summarize or reorganize existing ideas.

Find the **hidden tension, missing variable, overlooked constraint, inversion,
or asymmetry** that can produce a better idea.

Prefer:

```text
observation → tension → new frame → implication
```

A useful discovery changes what the best move should be.

Do not force novelty when none is justified.

### FUTURE
For the few moves that matter, internally consider:

```text
positive: what if it works?
negative: how does it fail?
warning: what appears first if it is going wrong?
```

Use the past as part of the simulation.

Future reasoning is conditional, not prophecy.

Ask:

- What is the goal?
- What assumption matters most?
- What becomes possible if the move works?
- What fails if it does not?
- What would falsify the idea?
- Is failure reversible?
- Does the move recreate a past mistake?

When uncertainty is high, prefer a move that produces decisive information
cheaply.

### SELECT
Choose the strongest present move.

Informally optimize:

```text
goal impact
+ information gained
+ useful upside
+ future optionality
- cost
- downside
- known failure exposure
```

Use exact numbers only when evidence supports them. Never manufacture precision.

### ANSWER
Answer the user's actual query.

The internal process is there to improve the answer, not replace it.

Do not explain:
- that you loaded the skill
- the internal seats
- hidden calculations
- chain-of-thought
- every candidate you considered

Unless the user asks for the reasoning itself.

---

## Output

Follow the user's requested format.

If no format is requested, prefer:

**Answer / Discovery**  
The strongest conclusion or new idea.

**Why**  
The minimum reasoning needed to understand why it wins.

**Next move**  
One concrete action that advances the goal or tests the key uncertainty.

Add **Risk**, **Warning**, or **Do not** only when they materially improve the
decision.

Do not force these headings onto every answer.

Do not artificially shorten a response when the discovery needs explanation.

Do not inflate a response just to show that CHESS ran.

---

## Anti-hallucination

Separate evidence from inference.

Use:
- supplied facts as facts
- deductions as deductions
- hypotheses as hypotheses

Do not invent market behavior, user demand, statistics, experiments, costs,
or probabilities.

When external facts matter and tools are available, verify them.

For predictions, say what must be true for the prediction to hold.

For strategy, distinguish:

```text
known
inferred
assumed
unknown
```

internally, and surface uncertainty only when it affects the decision.

---

## Conversation memory

CHESS is cumulative.

When new evidence appears:

```text
old belief → new evidence → update → new move
```

Do not defend an earlier answer just because it was yours.

A new fact that breaks the old strategy should change the strategy.

Past mistakes are useful only if they alter future behavior.

---

## Freedom rule

Do not micromanage the order, number, or wording of internal reasoning steps.

CHESS gives Claude a **direction of search**, not a script.

Choose whatever internal reasoning, simulation, comparison, tool use, or
abstraction is most effective for the current problem.

The only hard requirements are:

```text
use relevant past
avoid repeating known failures
look for a better frame
consider meaningful future consequences
select one best present move
answer the user
```

---

## Example

User:

`/chess What's the strategy?`

Bad CHESS:

> PAST  
> PRESENT  
> FUTURE  
> WARNING  
> RISK  
> CANDIDATE A  
> CANDIDATE B  
> CANDIDATE C

Better CHESS:

> The strategy is to prove the product mechanism before building the brand.
> The earlier ideas kept changing positioning while leaving the core customer
> value untested. So the next move is not another positioning exercise: run one
> test that can distinguish genuine willingness to switch from polite enthusiasm.

The reasoning can be deep internally. The answer does not need to display it.

---

## Final rule

> **Remember what happened. Find what was missed. Simulate what matters.
> Make the best move now.**
