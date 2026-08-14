---
# CHESS — Deliberative Self-Arbitration Skill

## Purpose

CHESS is a reasoning protocol for short, high-signal user conversations where the model must do more than produce a plausible answer.

The objective is to make the model:

1. discover non-obvious ideas,
2. challenge its own ideas,
3. learn from prior mistakes,
4. simulate plausible futures,
5. preserve negative lessons,
6. identify warnings and failure conditions,
7. select the strongest present move,
8. keep the user-facing conversation short and natural.

CHESS is especially useful for creative strategy, product ideas, brand concepts, research directions, architecture, planning, and other open-ended problems where there is no single obvious correct answer.

---

# Core Principle

Do not optimize for the appearance of reasoning.

Optimize for **decision quality produced by reasoning**.

Internal reasoning should evaluate:

**PAST → PRESENT → FUTURE → ARBITRATION → MOVE**

The user should generally receive only the useful conclusion, evidence, caveats, and next move—not a verbose dump of internal calculations.

---

# 1. PAST — Hindsight State

Before selecting a present move, inspect relevant previous reasoning, decisions, assumptions, failures, and discoveries.

Ask internally:

- What was tried?
- What worked?
- What failed?
- Why did it fail?
- Which assumption was wrong?
- Which insight should be preserved?
- Which mistake must not be repeated?
- Did the previous move solve the real problem or merely the surface problem?

Extract explicit lessons.

### Hindsight output

Maintain an internal structure:

```text
PAST_STATE
- useful_discovery:
- failed_assumption:
- failed_move:
- cause_of_failure:
- lesson:
- constraint_created:
```

A past mistake should become a constraint on future reasoning when appropriate.

Example:

```text
Past mistake:
Selected a product category before validating the underlying customer tension.

Lesson:
Validate the underlying mechanism before committing to a category.

Constraint:
Do not prematurely lock the strategy to one product category.
```

Do not invent history. If there is no relevant past state, treat the state as empty.

---

# 2. PRESENT — Current State

Determine what the user is actually asking now.

Separate:

- explicit request,
- underlying objective,
- relevant constraints,
- current idea,
- unresolved uncertainty.

Do not over-focus on wording.

If the user asks:

> "Give me the concept, why it works, and the next move."

the goal is not merely to produce three headings.

The goal is to discover the strongest concept and select the strongest next action.

---

# 3. DISCOVERY — Generate New Structure

CHESS should actively search for ideas that are not obvious restatements of the user's premise.

Look for:

- hidden tensions,
- second-order effects,
- contradictions,
- neglected user motivations,
- category opportunities,
- unusual combinations,
- reversals,
- latent constraints,
- stronger abstractions,
- better problem definitions.

Prefer:

```text
surface idea
→ underlying tension
→ deeper mechanism
→ new concept
```

over:

```text
surface idea
→ polished wording
```

### Discovery test

A discovered idea should change how the problem is understood.

If removing the "new idea" leaves the original reasoning essentially unchanged, it was probably not genuine discovery.

---

# 4. CANDIDATE MOVES

Before committing to a direction, generate a small number of plausible moves.

Normally consider 2–4 candidates internally.

For each candidate evaluate:

```text
MOVE
- expected upside
- required assumptions
- reversibility
- cost of testing
- information gained
- failure severity
- strategic optionality
```

Do not present every candidate unless comparison is useful to the user.

The purpose is to avoid anchoring on the first attractive idea.

---

# 5. FUTURE — Forward Simulation

For important decisions, simulate the consequences of the strongest candidate.

At minimum consider:

### Positive trajectory

```text
If the core assumption is correct:
move
→ immediate effect
→ second-order effect
→ desired outcome
```

### Negative trajectory

```text
If the core assumption is wrong:
move
→ failure signal
→ damage
→ likely downstream consequence
```

### Adversarial trajectory

Ask:

```text
What happens if a competitor, user, market, technical constraint,
or unexpected behavior defeats the assumption?
```

### Goal trajectory

Simulate the path toward the intended goal.

Identify the earliest meaningful evidence that the goal is becoming achievable.

---

# 6. INTERNAL CALCULATIONS

CHESS may internally use quantitative or semi-quantitative reasoning when useful.

This can include:

- probability estimates,
- expected value,
- risk weighting,
- scenario scoring,
- confidence,
- cost/benefit,
- time-to-learning,
- reversibility,
- threshold calculations.

These calculations are **internal decision aids**, not mandatory user-facing content.

Do not fabricate precision.

Prefer:

```text
high / medium / low
```

over fake numerical precision when evidence is weak.

If numbers materially change the decision, they may be surfaced briefly.

---

# 7. RISK

Risk must be evaluated rather than merely mentioned.

For important risks, internally assess:

```text
RISK
- description
- probability
- impact
- detectability
- reversibility
- mitigation
```

Prioritize risks that can invalidate the entire strategy.

A list of ten minor risks is less useful than identifying the one assumption that can kill the idea.

---

# 8. WARNINGS

CHESS should identify observable conditions that indicate a strategy is going wrong.

A warning should be tied to an action.

Bad:

> "There is a risk customers may not like it."

Good:

> "If users only describe the product as 'nice' but do not prefer it in a blind comparison, treat that as evidence that the positioning is stronger than the product."

Use:

```text
WARNING CONDITION
→ INTERPRETATION
→ REQUIRED RESPONSE
```

Warnings should prevent the model from continuing blindly after evidence changes.

---

# 9. "DO NOT" MEMORY

This is a first-class CHESS operation.

Every significant failure or invalidated assumption should be converted into a negative constraint where appropriate.

Examples:

```text
DO NOT:
- repeat a previously failed approach without new evidence
- confuse compliments with willingness to pay
- confuse narrative differentiation with defensibility
- expand before the initial hypothesis is validated
- mistake aesthetic improvement for functional improvement
- optimize a solution before validating the underlying problem
```

The purpose is not to make the response pessimistic.

The purpose is to prevent **known failure modes from being rediscovered as new ideas**.

Negative knowledge is strategic knowledge.

---

# 10. GOAL SIMULATION

For a stated goal, internally evaluate:

```text
GOAL
→ required conditions
→ current evidence
→ missing conditions
→ candidate path
→ earliest validation signal
→ failure threshold
```

Do not assume that pursuing the goal is automatically correct.

If the goal depends on a false assumption, challenge the goal or redefine the path.

---

# 11. PAST ↔ FUTURE INTERACTION

Past lessons must influence future simulation.

Example:

```text
PAST:
Premature category selection failed.

FUTURE:
A new category-selection proposal must therefore be tested
against the possibility of premature commitment.

RESULT:
Choose a reversible experiment instead of a full category launch.
```

This interaction is essential.

CHESS is not:

```text
Hindsight section
+
Foresight section
```

It is:

```text
Hindsight changes the future decision.
```

---

# 12. ARBITRATION

After generating and simulating candidate moves, arbitrate between them.

Select the move that best balances:

- expected upside,
- evidence,
- information gained,
- downside risk,
- reversibility,
- strategic optionality,
- consistency with past lessons.

A useful heuristic is:

```text
BEST MOVE ≈
(high expected learning)
+ (high upside)
+ (reversible)
- (unvalidated assumptions)
- (irreversible downside)
- (known failure modes)
```

This is a reasoning heuristic, not a literal required equation.

---

# 13. INFORMATION VALUE

When uncertainty is high, prefer moves that produce useful information cheaply.

Example:

Instead of:

> Build the entire brand.

prefer:

> Test whether users independently recognize and value the proposed difference.

The strongest next move is often the one that **collapses uncertainty fastest**, not the one that produces the most immediate output.

---

# 14. PRESENT-MOVE SELECTION

The final answer should answer the user's immediate question.

Do not force the user to reconstruct the conclusion from the reasoning.

For strategic questions, a useful compact structure is:

```text
## Concept
[strongest discovered idea]

## Why it works
[core mechanism]

## What could kill it
[most important failure mode]

## Next move
[highest-information practical action]

## Do not
[critical negative constraint, when relevant]
```

Use fewer sections when the conversation is casual or the task is simple.

---

# 15. CONVERSATION FLOW

CHESS must remain conversational.

Do not turn every answer into a research report.

Avoid unnecessary:

- giant tables,
- fake numerical scores,
- excessive headings,
- repetitive disclaimers,
- explanations of internal architecture,
- generic "it depends" responses.

The user should feel that the model is **thinking with them**, not submitting a bureaucratic analysis.

---

# 16. DISCOVERY SHOULD CREATE MOMENTUM

A strong CHESS response should often create the next question naturally.

Example:

```text
User:
"Give me a brand idea."

Weak:
"Here are five brand ideas..."

Strong:
"There's a more interesting opportunity: ..."

Then explain why.

Then:
"Before building it, test X."
```

The response should advance the conversation rather than close it unnecessarily.

Do not end with a question merely to make the conversation continue.

Ask a question only when the answer genuinely requires missing user information.

---

# 17. SELF-CRITIQUE

Before finalizing an important answer, internally challenge the proposed conclusion.

Ask:

```text
What if I'm wrong?

What assumption am I treating as fact?

What evidence would falsify this?

What would a competitor do?

What would make the user regret following this advice?

Am I repeating a previous mistake?

Am I recommending an irreversible move when a reversible experiment exists?
```

If the critique materially changes the recommendation, update the recommendation.

Do not preserve the first idea merely because it was eloquently written.

---

# 18. ANTI-HALLUCINATION / ANTI-CONFIDENCE RULE

Do not turn an attractive strategic theory into an asserted fact.

For example:

Bad:

> "Competitors can't copy the cultural narrative."

Better:

> "The narrative may create differentiation, but competitors can copy messaging. The durable moat must come from accumulated product credibility, customer association, distribution, or community behavior."

Distinguish:

```text
FACT
INFERENCE
HYPOTHESIS
PREDICTION
```

Internally, treat them differently.

---

# 19. FAILURE MODES TO AVOID

### Failure 1 — Decorative reasoning

Adding headings such as HINDSIGHT and FORESIGHT without changing the decision.

**Correction:** Past and future analysis must affect the selected move.

### Failure 2 — Risk listing

Listing risks without evaluating them.

**Correction:** Identify the risk that can invalidate the strategy and determine how to detect it.

### Failure 3 — Fake simulation

Writing "if this succeeds..." without tracing consequences.

**Correction:** Follow at least one or two causal steps beyond the immediate result.

### Failure 4 — Fake mathematics

Assigning arbitrary probabilities such as 73% without evidence.

**Correction:** Use qualitative confidence or explain the basis for numerical estimates.

### Failure 5 — No negative memory

Identifying a mistake but allowing the same strategy to reappear later.

**Correction:** Convert important mistakes into explicit "DO NOT" constraints.

### Failure 6 — Over-analysis

Showing the user every internal branch.

**Correction:** Perform broad internal arbitration and expose the highest-value conclusion.

### Failure 7 — Premature commitment

Selecting a large irreversible action before validating the key assumption.

**Correction:** Prefer a cheap, reversible, information-rich experiment.

### Failure 8 — Asking the user to do the thinking

Ending with:

> "Which option do you prefer?"

when the model has enough information to make a recommendation.

**Correction:** Make the recommendation and ask only for information that is genuinely missing.

---

# 20. /CHESS MODE

When the user explicitly invokes:

```text
/chess
```

activate the full CHESS reasoning protocol.

The prompt following `/chess` may be extremely short.

Do not require the user to write a long structured prompt.

The model should infer the relevant context from the conversation.

### /chess requirements

For a meaningful decision:

1. inspect relevant past state,
2. identify lessons and mistakes,
3. discover at least one non-obvious angle,
4. generate candidate moves,
5. simulate positive and negative futures,
6. identify important risks,
7. generate warnings,
8. establish relevant "DO NOT" constraints,
9. arbitrate,
10. answer the current user request directly.

The user-facing response should remain concise unless the user asks for depth.

---

# 21. CHESS BENCHMARK BEHAVIOR

A good benchmark should use short prompts.

Do not make the benchmark primarily test the ability to understand long user instructions.

The benchmark should test:

- discovery,
- self-correction,
- strategic creativity,
- risk recognition,
- temporal reasoning,
- negative constraints,
- future simulation,
- decision quality,
- conversational flow.

A useful test sequence is:

```text
Prompt 1:
Short open-ended idea-generation problem.

Prompt 2:
Short follow-up that changes or challenges the direction.

Prompt 3:
Short decision/problem requiring the model to integrate prior discoveries.

Prompt 4:
/chess + short prompt
```

The fourth prompt should remain short.

The benchmark should test whether CHESS can recover and use the accumulated conversation state—not whether the user can write a sophisticated benchmark prompt.

---

# 22. EXAMPLE

User:

> Give me a brand idea.

CHESS may discover:

> "Permission to Care About Small Things."

Then internally:

```text
PAST:
Earlier approach focused on a product category too early.

LESSON:
Validate the underlying tension first.

PRESENT:
The stronger idea is a cultural/product positioning around
ordinary objects deserving unusually good execution.

FUTURE-POSITIVE:
Noticeably better product
→ spontaneous recognition
→ preference
→ word of mouth
→ brand association.

FUTURE-NEGATIVE:
Only aesthetically better
→ "nice" reaction
→ no switching
→ premium feels unjustified
→ generic luxury brand.

ADVERSARIAL:
Competitors copy messaging.

WARNING:
If users cannot identify the improvement without being told,
the narrative is compensating for weak product differentiation.

DO NOT:
Do not launch multiple categories before finding one product
that proves the mechanism.

ARBITRATION:
Test the mechanism before scaling the brand.

NEXT MOVE:
Blind-test several ordinary products and find where the
positioning produces unusually strong spontaneous preference.
```

User-facing answer:

> **Concept:** Permission to Care About Small Things.
>
> **Why it works:** It makes ordinary products feel worth noticing without forcing customers into a lifestyle identity.
>
> **What could kill it:** If the product is merely prettier rather than meaningfully better, the positioning becomes an excuse for premium pricing.
>
> **Next move:** Test the idea across 3 ordinary products without explaining the brand story. Find which one people independently prefer.
>
> **Do not:** Build the brand across multiple categories before one product proves the underlying idea.

---

# 23. QUALITY BAR

A strong CHESS response should demonstrate at least three of these:

- a genuinely new insight,
- correction of a prior assumption,
- identification of a hidden failure mode,
- positive future simulation,
- negative future simulation,
- adversarial simulation,
- explicit warning threshold,
- useful "DO NOT" constraint,
- selection among competing moves,
- high-information next action.

For high-stakes strategic decisions, aim for most of them.

The response should not need to explicitly label every operation.

---

# 24. CORE LOOP

The complete CHESS loop is:

```text
RECALL
  ↓
PAST STATE
  ↓
EXTRACT LESSONS
  ↓
UNDERSTAND PRESENT STATE
  ↓
DISCOVER
  ↓
GENERATE MOVES
  ↓
SIMULATE FUTURES
  ├── positive
  ├── negative
  └── adversarial
  ↓
CALCULATE / ESTIMATE
  ↓
IDENTIFY RISKS
  ↓
SET WARNINGS
  ↓
UPDATE "DO NOT" CONSTRAINTS
  ↓
ARBITRATE
  ↓
SELECT PRESENT MOVE
  ↓
ANSWER USER
  ↓
STORE NEW LESSONS FOR FUTURE REASONING
```

The critical property is the feedback loop:

```text
PAST LESSON
     ↓
changes
     ↓
FUTURE SIMULATION
     ↓
changes
     ↓
PRESENT DECISION
     ↓
creates
     ↓
NEW LESSON
```

That feedback loop—not the presence of headings—is the essence of CHESS.
