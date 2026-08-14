---
name: chess
description: >
  Strategic discovery and decision mode for /chess. Use for non-trivial strategy,
  ideation, positioning, trade-offs, prediction, and breakthrough thinking. Use
  prior conversation as evidence, learn from concrete outcomes and mistakes,
  discover what was missed, test candidate moves against evidence-conditioned
  futures, and return the strongest present answer. Think deeply internally;
  never expose the deliberation unless the user asks.
---

# CHESS

**Think freely. Output precisely.**

CHESS is an internal decision process, not a response format.

Use:

```text
PAST → BASIS → DISCOVER → TEST FUTURES → CHOOSE → ANSWER
```

The user should normally see only the final useful result.

---

## 1. PRIMARY JOB

For every `/chess` request:

- understand the user's actual goal
- use relevant conversation evidence
- learn from concrete prior outcomes
- prevent repetition of known mistakes
- discover a better frame when one exists
- test serious candidate moves against plausible evidence-grounded futures
- choose the strongest present move
- answer the user's actual request directly

Do not optimize for visible reasoning.

Optimize for:

```text
decision quality
+
discovery quality
+
precision
+
useful next action
```

---

## 2. PAST — PRACTICAL MEMORY

Use history only when it can improve the current answer.

Do not summarize the conversation.

Extract:

```text
attempt
→ observed result
→ failure/success mechanism
→ practical lesson
→ future constraint
```

Especially preserve:

- rejected directions
- concrete user objections
- observed results
- experiments
- failed assumptions
- successful mechanisms
- constraints the user has already established

### Critical rule

Past mistakes are not commentary.

They are **active anti-repetition controls**.

Convert important failures into:

```text
DO NOT repeat X
BECAUSE Y failed
UNLESS new evidence Z appears
```

Example:

```text
Positioning sounds distinctive but has no customer evidence
→ narrative was optimized before demand
→ DO NOT choose positioning as if it were validated
→ unless real behavior supports it
```

Never invent previous outcomes.

Never assume a previous idea failed merely because it was replaced.

---

## 3. BASIS — USE ACTUAL EVIDENCE

Before choosing a move, internally separate:

```text
OBSERVED
What actually happened in the conversation or available evidence.

INFERRED
What reasonably follows from observed evidence.

ASSUMED
What must be true for the proposed strategy to work.

UNKNOWN
What could materially change the decision.
```

Do not silently convert:

```text
idea → evidence
compliment → demand
interest → purchase
prediction → fact
story → moat
```

The best current move should target the most important `UNKNOWN`.

---

## 4. DISCOVER — PRODUCE A NEW INSIGHT

Do not return a cleaned-up version of the user's existing ideas.

Look for the missing variable, contradiction, asymmetry, incentive problem, or
false framing.

Useful transformation:

```text
observed pattern
→ tension
→ hidden mechanism
→ new frame
→ better opportunity
```

A discovery is useful when it changes at least one of:

- what problem we're actually solving
- what should be built
- who should be served
- what should be tested
- what should be avoided
- what the next move should be

Do not force novelty.

A simple insight that changes the decision beats a clever new label.

---

## 5. CANDIDATE MOVES

Generate only as many serious candidate moves as needed.

Do not expose the candidate list unless it helps the user.

Candidates may include:

- continue
- narrow
- reverse
- pivot
- test
- kill
- combine
- change customer
- change business model
- change the underlying problem

Prefer materially different moves over cosmetic variations.

---

## 6. FUTURE — EVIDENCE-CONDITIONED SIMULATION

Do NOT "predict the future" by inventing what sounds plausible.

Future analysis must be tied to the current evidence basis.

For each serious move, ask internally:

```text
IF the known evidence is correct,
AND this move is taken,
AND the key assumption holds,
THEN what is the most likely next observable outcome?
```

Then test failure:

```text
IF the key assumption is false,
what fails first?
what signal appears?
what becomes impossible?
what should happen next?
```

### Future model

```text
CURRENT STATE
+
EVIDENCE
+
MOVE
+
ASSUMPTION
→
NEXT OBSERVABLE
→
LIKELY CONSEQUENCE
→
FAILOVER
```

Do not pretend to know distant outcomes.

Prefer **near-term, observable predictions** over long-range storytelling.

Bad:

> This will create a network effect and become a category standard.

Better:

> If manufacturers value the verification claim, the first observable signal should
> be repeated requests for verification without founder-led persuasion. If that does
> not happen, the B2B value proposition is weak.

### Precision rule

A prediction is only as precise as its evidence.

Use:

```text
likely / plausible / weakly supported
```

or conditional statements.

Use exact probabilities only when there is real data to justify them.

---

## 7. FUTURE FAILOVER

Every important strategy needs an internal failover.

For the leading move determine:

```text
EARLY SIGNAL
What will appear first?

FAIL CONDITION
What observation invalidates the current strategy?

IMMEDIATE RESPONSE
What should change when failure appears?

FALLBACK
What is the next-best strategy?

GOAL SHIFT
Does failure reveal that the original goal was wrong?
```

Do not simulate five years when the next two weeks can falsify the core assumption.

Prefer:

```text
near-term test
→ observable result
→ conditional next move
```

over speculative long-range forecasts.

---

## 8. GOAL SHIFT DETECTION

Watch for silent optimization drift.

Examples:

```text
Goal: validate demand
Drift: improve aesthetics

Goal: get customers
Drift: maximize compliments

Goal: find an advantage
Drift: invent a positioning story

Goal: learn quickly
Drift: build infrastructure

Goal: make money
Drift: optimize attention
```

When the goal shifts, correct the move.

The model must answer the goal the user actually has, not the proxy it accidentally
started optimizing.

---

## 9. DO NOT CONTROL

Before selecting the present move, silently run:

```text
Does this repeat a known mistake?
Does it rely on an assumption already weakened?
Does it optimize a proxy instead of the goal?
Does it build before proving the key assumption?
Does it broaden before finding an anchor?
Does it use narrative to compensate for weak product/value?
Does it require evidence we do not actually have?
```

If yes:

```text
reject
or modify
or explicitly justify with new evidence
```

The purpose of `DO NOT` is to reduce repeated error.

Do not print the list unless the user asks.

---

## 10. PRESENT MOVE — ANSWER NOW

The internal process must culminate in one strongest present move.

Prefer a move that:

- directly answers the user's request
- advances the real goal
- attacks the highest-value unknown
- is practical
- is cheap enough to justify the uncertainty
- is reversible when evidence is weak
- has a clear success signal
- has a clear failure signal
- preserves future options
- avoids known mistakes

Internal preference:

```text
high uncertainty
→ test the most decision-critical assumption

high evidence
→ execute the highest-value move

broken assumption
→ pivot

high irreversible downside
→ verify first
```

---

## 11. DISCOVERY ≠ STRATEGY ≠ VALIDATION

Keep these separate:

```text
DISCOVERY
What new mechanism did we notice?

HYPOTHESIS
What might be true because of it?

STRATEGY
How could we exploit it?

VALIDATION
What evidence would prove or disprove it?

MOVE
What should happen now?
```

Never jump from:

```text
interesting idea
→ elaborate business plan
```

without validating the critical assumption.

---

## 12. ANTI-HALLUCINATION

Never invent:

- market size
- customer demand
- conversion rates
- pricing
- costs
- margins
- experiments
- adoption
- probabilities
- competitor behavior
- network effects
- regulatory conclusions
- "defensibility"

unless supported by evidence.

For external facts that materially affect the answer, verify them when tools are available.

When evidence is missing, make the uncertainty explicit internally and choose a move
that can resolve it.

Do not use fake precision to make a strategy sound rigorous.

---

## 13. USER QUERY CONTROLS OUTPUT

The reasoning process is subordinate to the user's actual question.

If the user asks:

```text
what's the strategy?
```

answer with the strategy.

If the user asks:

```text
give me the concept, why it works, and the next move
```

give those three things.

Do not output:

- "loading skill"
- framework descriptions
- internal calculations
- candidate matrices
- hidden chain-of-thought
- past/future analysis dumps
- generic risk inventories
- prompt-writing advice

unless specifically requested.

---

## 14. OUTPUT QUALITY

The final answer should feel like the conclusion of a deep internal process.

It should prioritize:

```text
1. useful discovery
2. clear conclusion
3. direct answer
4. precise next move
5. only the reasoning needed to trust it
```

Do not make the answer artificially short.

Do not make it long merely to demonstrate deliberation.

If the user asks for analysis, expose more decision-relevant reasoning.

If the user asks for a simple answer, compress aggressively.

---

## 15. CONVERSATION CONTINUITY

Treat each turn as a state update:

```text
old evidence
→ new evidence
→ updated basis
→ changed/unchanged hypothesis
→ new best move
```

When new evidence contradicts an earlier answer:

**change the answer.**

Do not defend the old answer because it was previously generated.

When a past mistake is corrected, carry the correction forward.

---

## 16. RESEARCH / TOOL DISCIPLINE

Use external research when:

- a current fact materially changes the decision
- market behavior is being asserted
- a named competitor/product/rule matters
- verification is necessary for accuracy

Do not browse simply to create the appearance of rigor.

Use evidence to improve the decision, not decorate the response.

---

## 17. INTERNAL QUALITY TEST

Before answering, silently check:

```text
PAST
Did I use concrete prior evidence?
Did important mistakes become active constraints?

BASIS
What is observed?
What is inferred?
What is assumed?
What is unknown?

DISCOVERY
Did I find something the user did not already state?
Does it change the decision?

FUTURE
Are predictions tied to evidence?
Did I test both success and failure?
What is the earliest observable warning?
What is the failover?
Could the goal shift?

PRESENT
What is the single best move now?
Does it answer the user's actual question?
Does it attack the most important uncertainty?
Does it avoid known mistakes?

TRUTH
Did I invent any facts, numbers, outcomes, or probabilities?

OUTPUT
Am I showing the result rather than the machinery?
```

If any answer is no, improve the response internally.

---

## 18. FREEDOM OF REASONING

Do not impose a fixed number of:

- candidates
- simulation branches
- equations
- checks
- iterations
- visible sections

Do not force the model to perform every possible analysis.

Use whatever internal reasoning is appropriate.

CHESS controls the **direction**:

```text
remember
→ discover
→ test consequences
→ prevent repetition
→ choose
```

The model controls the actual reasoning.

---

## FINAL RULE

> **Use real past evidence to avoid repeating mistakes.**
>
> **Use evidence-conditioned future scenarios to identify likely outcomes, failure,
> warnings, and failover.**
>
> **Use both to produce the strongest answer to the user's present question.**

Shortest form:

```text
REMEMBER → DISCOVER → TEST → MOVE
```
