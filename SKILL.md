
---
name: chess
description: >
  Calibrated discovery and decision reasoning for difficult problems.
  Use /chess when prior mistakes, competing ideas, future consequences,
  falsification, or high-value decisions matter. Calculate internally;
  return only the useful conclusion and decisive reasoning.
---


## Core Principle

CHESS treats the conversation as a changing state:

[
S_t =
{
\text{facts},
\text{assumptions},
\text{goals},
\text{constraints},
\text{history},
\text{uncertainty}
}
]

The internal calculation has three stages:

[
\boxed{
PAST
\rightarrow
FUTURE
\rightarrow
PRESENT
}
]

Past extracts lessons and prohibitions.

Future simulates candidate moves.

Present chooses the best move using both.

Do not expose hidden chain-of-thought.

---

# 1. PAST — Calculate What History Teaches

Inspect the conversation for relevant previous attempts, failures, corrections, successes, objections, and abandoned ideas.

Compress them into two internal sets:

### Positive memory

[
H^+ =
{
\text{mechanisms that worked},
\text{useful evidence},
\text{validated preferences}
}
]

### Negative memory

[
H^- =
{
\text{failed assumptions},
\text{failure mechanisms},
\text{known risks},
\text{explicit prohibitions}
}
]

For every important failure:

```text
failure
→ mechanism
→ lesson
→ boundary
→ future test
```

Do not merely remember the surface mistake.

Find the mechanism that caused it.

---

# 2. PAST NEGATIVE MEMORY — DO NOT REPEAT

Convert important past failures into explicit constraints.

Internally maintain:

```text
DO:
  preserve mechanisms that worked

DO NOT:
  repeat mechanisms that already failed

WARNING:
  conditions that previously produced failure

BOUNDARY:
  conditions under which the lesson stops applying
```

A past failure should actively modify future candidate evaluation.

If:

[
a \cap H^- \neq \varnothing
]

penalize or reject candidate (a), unless new evidence justifies violating the constraint.

Do not repeat a known failure simply because the new idea has different wording.

---

# 3. PAST POSITIVE MEMORY

Do not overcorrect from failures.

Preserve useful mechanisms.

For each strong previous success ask:

```text
What actually worked?
Why did it work?
Is the mechanism transferable?
What condition made it successful?
```

Transfer mechanisms, not superficial features.

---

# 4. FUTURE — Generate Candidate Moves

Generate only the few candidates capable of materially changing the outcome.

Default:

[
2 \leq |A| \leq 4
]

where:

[
A={a_1,a_2,\ldots,a_n}
]

Do not generate many decorative alternatives.

Candidates should represent genuinely different strategies, not synonyms.

---

# 5. FUTURE POSITIVE CALCULATION

For each candidate (a), simulate the desirable path:

[
S_t
\xrightarrow{a}
S_{t+1}
\xrightarrow{}
S_{t+2}
]

Ask internally:

```text
What goal does this achieve?
What becomes possible if it succeeds?
What advantage compounds?
What evidence would confirm success?
```

Calculate the candidate's expected goal value:

[
G(a)
]

This does not require numerical precision.

Use qualitative levels when probabilities are unsupported:

```text
high
medium
low
```

Do not invent numerical probabilities.

---

# 6. FUTURE NEGATIVE CALCULATION

For each candidate simulate failure and opposition.

Ask:

```text
What can go wrong?
What is the strongest failure mode?
What happens after that failure?
Does the failure become expensive to reverse?
Does it recreate a previous failure?
What would make us abandon the move?
```

Define:

[
R(a)
]

as the relevant downside/risk.

Also calculate exposure to known historical failures:

[
E_H(a)
]

A candidate that recreates a known failure should receive a strong penalty.

---

# 7. FUTURE WARNINGS

Generate warnings only when they can affect the decision.

```text
WARNING:
[condition that could invalidate the candidate]

TRIGGER:
[observable evidence]

RESPONSE:
[what to do if triggered]
```

Do not fill the answer with generic risk lists.

A warning is useful only if it can change the move.

---

# 8. DO-NOT-DO LIST

Before choosing the present move, derive:

```text
DO NOT:
- repeat confirmed failed mechanism
- ignore a known boundary condition
- optimize a metric that previously caused the failure
- expand scope when expansion recreates the original problem
- claim certainty without evidence
```

Add task-specific prohibitions from the conversation.

The strongest past mistake becomes the strongest future guardrail.

---

# 9. CANDIDATE CALCULATION

Evaluate each candidate internally:

[
Score(a)
========

## G(a)

## \lambda R(a)

## \mu E_H(a)

\nu C(a)
+
O(a)
]

where:

* (G(a)) = expected goal gain
* (R(a)) = future downside/risk
* (E_H(a)) = exposure to known historical failures
* (C(a)) = cost, complexity, or delay
* (O(a)) = useful option value / future flexibility
* (\lambda,\mu,\nu) = context-dependent weights

This is a reasoning model, not a requirement to invent numbers.

Use explicit numbers only when evidence supports them.

---

# 10. ATTACK THE LEADING MOVE

After selecting the provisional best candidate:

[
a^*=\arg\max_a Score(a)
]

attack it.

Ask:

```text
What is the strongest reason this move is wrong?
What evidence would reverse the decision?
Does it violate a past lesson?
Is there a simpler candidate that achieves the same goal?
```

If the attack changes the ranking, recalculate.

If it does not, proceed.

Do not endlessly recurse.

---

# 11. DISCOVERY

A discovery is not merely a better phrasing of an existing idea.

A strong discovery candidate should contain at least one:

```text
new mechanism
new relationship
new synthesis
new generalization
new prediction
new constraint
new strategy
new counterexample
```

The ideal pattern is:

```text
past failure
→ hidden mechanism
→ contradiction
→ generalized principle
→ new candidate
```

Prefer discoveries that solve the underlying contradiction rather than cosmetically improving the original idea.

Never claim historical novelty without appropriate external research.

---

# 12. PRESENT MOVE

After hindsight and foresight, choose the action:

[
\boxed{
M_t = \arg\max_a Score(a)
}
]

The present move must answer:

```text
What should the user do now?
Why this move?
What should they NOT do?
What evidence should they obtain next?
```

The move should be concrete enough to execute.

Do not end with an abstract analysis if an actionable decision is possible.

---

# 13. CHEAPEST DECISIVE VALIDATION

Do not validate everything.

Find the cheapest test capable of changing the decision.

Priority:

```text
logical check
→ toy test
→ small experiment
→ prototype
→ benchmark
→ expensive experiment
```

If a cheap test can eliminate the leading candidate, run that reasoning first.

Stop when additional analysis is unlikely to change the decision materially.

---

# 14. MATHEMATICAL / TECHNICAL SANITY

When the problem contains mathematical or technical claims, apply only relevant checks:

```text
dimensions
limiting cases
degenerate cases
symmetry
counterexamples
boundary conditions
baseline comparison
```

Do not force mathematics onto problems where it adds no information.

The mathematical framework is primarily for **internal calculation**, not for making ordinary answers look mathematical.

---

# 15. UNCERTAINTY

Internally distinguish:

```text
FACT
Supported by evidence or established mathematics.

DEDUCTION
Follows from explicit assumptions.

HYPOTHESIS
Plausible but unverified.

DISCOVERY CANDIDATE
A new/generalized idea that survives initial attacks.

VERIFIED
Demonstrated by appropriate evidence.
```

Do not convert uncertainty into confidence for rhetorical effect.

---

# 16. DEFAULT OUTPUT

Do not expose the internal calculation process.

Return:

```markdown
## Verdict

[Best present conclusion.]

## Calculation

[The decisive hindsight + future comparison.]

## Risk

[Strongest remaining failure condition.]

## Do Not Do

[Most important thing to avoid.]

## Next Move

[Concrete action or experiment.]
```

For simple requests, compress further.

For research problems, expand only where the extra reasoning changes the result.

---

# 17. INTERNAL CHESS LOOP

```text
CURRENT STATE
      ↓
PAST POSITIVE
      +
PAST NEGATIVE
      ↓
DO / DO NOT / WARNINGS
      ↓
CANDIDATE MOVES
      ↓
POSITIVE FUTURE
      +
NEGATIVE FUTURE
      ↓
GOAL / RISK / HISTORY / COST
      ↓
PROVISIONAL BEST MOVE
      ↓
ATTACK
      ↓
RECALCULATE IF NECESSARY
      ↓
PRESENT MOVE
      ↓
CHEAPEST VALIDATION
```

---

# 18. COMPRESSION RULE

Do not maximize:

```text
number of candidates
number of tests
length of reasoning
number of warnings
```

Maximize:

[
\boxed{
\frac{\text{Decision Quality}}
{\text{Reasoning Cost}}
}
]

The internal calculation can be deep.

The external answer should be compact.

---

# 19. FINAL PRINCIPLE

> **Past tells us what to preserve and what never to repeat.**
>
> **Future tells us what each move could create or destroy.**
>
> **Calculation compares those futures against the goal and risk.**
>
> **Present chooses the strongest surviving move.**

The shortest CHESS rule:

[
\boxed{
\text{Remember}
\rightarrow
\text{Predict}
\rightarrow
\text{Attack}
\rightarrow
\text{Move}
}
]

**Past mistakes become constraints.
Future possibilities become simulations.
The present becomes a decision.**
