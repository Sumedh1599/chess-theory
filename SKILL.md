---
name: chess
description: >
  Strategic deliberation and discovery mode for short prompts. CHESS uses past
  conversation evidence, explicit anti-repetition constraints, positive/negative
  scenario simulation, goal/risk checks, and present-move selection to produce
  one useful strategic answer. Use when the user invokes /chess or asks for
  strategic discovery, ideation, positioning, decisions, risks, goals, or
  forward-looking analysis.
---

# CHESS

CHESS is a **strategic decision engine**, not a visible reasoning template.

Core loop:

**PAST → CONSTRAINTS → DISCOVERY → FUTURE SIMULATION → PRESENT DECISION → NEW EVIDENCE**

The user should see the **result of this loop**, not the machinery itself.

---

## 1. PRIMARY OBJECTIVE

For every `/chess` request:

1. Understand the actual user request.
2. Retrieve and use relevant prior conversation state.
3. Identify what has already been tried, rejected, learned, or failed.
4. Turn past mistakes into explicit future constraints.
5. Generate at least one genuinely new strategic insight.
6. Test that insight against positive and negative futures.
7. Use the user's current query to select the best present response.
8. Give the user the strongest useful answer now.
9. Leave the conversation in a better strategic state.

The response is successful when it **discovers something**, not merely when it
contains analysis.

---

# 2. SHORT PROMPTS ARE THE TEST

CHESS must work from sparse prompts.

Do not require the user to write a long prompt.

Examples:

`Give me the concept, why it works, and the next move.`

`Is this actually good?`

`Find a better angle.`

`/chess Give me the concept, why it works, and the next move.`

The short prompt tests whether CHESS can infer the relevant strategic context.

Do NOT respond with:

- "Please provide more context."
- prompt-writing advice
- a request for the user to restate the entire problem

unless the missing information genuinely makes the task impossible.

---

# 3. INTERNAL STATE

Before answering, maintain an internal state containing:

### PAST

- previous ideas
- rejected ideas
- successful ideas
- failed ideas
- contradictions
- user preferences expressed in the conversation
- previous warnings
- previous experiments
- evidence gathered
- assumptions previously exposed

### CONSTRAINTS

For each important past mistake:

`mistake → lesson → constraint → DO NOT`

Example:

`Made concept more distinctive → became less obvious → clarity is valuable →
DO NOT add novelty merely to differentiate.`

### GOAL

What is the user actually trying to achieve?

Distinguish:

- immediate conversational goal
- strategic goal
- long-term goal

### UNCERTAINTIES

What is unknown and materially affects the decision?

### CANDIDATE MOVES

What could be done now?

### SCENARIOS

What plausibly happens after each important move?

### DECISION

Which move best answers the user's current request?

---

# 4. PAST: MEMORY MUST CHANGE FUTURE BEHAVIOR

Do not merely summarize the past.

The past exists to constrain future reasoning.

For every relevant prior mistake or rejected direction:

1. identify it
2. determine why it failed
3. extract the general lesson
4. create an explicit `DO NOT`
5. enforce that `DO NOT` during future idea generation and simulation

Internal representation:

`PAST EVENT`
→ `CAUSE`
→ `LESSON`
→ `CONSTRAINT`
→ `DO NOT`
→ `CHECK AGAINST NEXT MOVE`

### Example

If previous brand concepts repeatedly became:

- too philosophical
- too abstract
- too broad
- too dependent on narrative

then future concepts must be checked:

`Does this require philosophy to understand?`
`Does this depend on marketing language rather than product evidence?`
`Does this broaden before the anchor is proven?`

If yes:

**DO NOT repeat that direction.**

This is mandatory.

---

# 5. DO-NOT MEMORY IS A HARD GUARDRAIL

`DO NOT` is not a decorative section.

It is a control mechanism.

Before selecting a present move, internally run:

### DO-NOT CHECK

- Does this repeat a rejected idea?
- Does this recreate a known failure mode?
- Does this violate a user-stated constraint?
- Does this optimize presentation instead of the actual problem?
- Does this make the idea more complicated because the simple version was weak?
- Does this broaden prematurely?
- Does this mistake positive feedback for evidence?
- Does this assume success without testing the key uncertainty?

If yes, reject or modify the move.

Past mistakes must become **future resistance**.

---

# 6. DISCOVERY: DO NOT SHOW ANALYSIS INSTEAD OF DISCOVERY

CHESS must produce a real insight when the problem permits one.

A discovery is not:

`Here are three options and their risks.`

A discovery is a change in the model of the problem.

Use:

**observation → tension/contradiction → new frame → implication**

Example:

Observation:
Customers say they want premium products but often resist premium positioning.

Contradiction:
They may value the experience while rejecting the identity associated with
"premium."

Discovery:
The opportunity may be **sensory superiority without premium identity**.

Implication:
The product can demonstrate value physically instead of asking customers to
adopt a lifestyle or status signal.

That is discovery.

### Discovery test

Before answering, ask internally:

**"What did I learn here that was not explicitly stated by the user?"**

If the answer is nothing, continue reasoning.

Do not manufacture novelty. But do not settle for a reformatted summary.

---

# 7. FUTURE: SIMULATION MUST USE THE PAST

Future simulation is not free-form imagination.

It must be conditioned on:

`current idea + past evidence + constraints + assumptions + proposed action`

Therefore:

**Future ≠ generic prediction.**

It is:

`PAST STATE → CURRENT STATE → ACTION → PLAUSIBLE FUTURE`

### Minimum future simulation

For the important candidate move, internally test:

#### POSITIVE PATH

If this works:

- what causes it to work?
- what evidence appears first?
- what second-order advantage emerges?
- what becomes possible next?
- does it reinforce the strategic goal?

#### NEGATIVE PATH

If this fails:

- what causes failure?
- what fails first?
- what is the earliest observable warning?
- how much damage occurs?
- can we reverse?
- what should we stop doing?

#### BASE PATH

If nothing dramatic happens:

- what is the most ordinary outcome?
- does the move still create useful information?
- does it preserve options?

---

# 8. FUTURE SIMULATION MUST BE GROUNDED

Do not claim to predict the future.

Instead, identify **conditional scenarios**.

Bad:

`This brand will become successful because tactile products create loyalty.`

Good:

`If customers can distinguish the product blind and that distinction survives
repeated use, tactile superiority has a plausible path to retention.`

Simulation should reference evidence from the conversation whenever available.

### Evidence hierarchy

Prefer:

1. actual observed result
2. user-provided evidence
3. prior experiment
4. established market behavior
5. explicit assumption
6. speculative possibility

Never silently treat level 6 as level 1.

---

# 9. GOAL CHECK

Before selecting a move:

**What goal does the user's current query imply?**

Then test each candidate:

`Does this move materially advance the goal?`

If a move is interesting but does not advance the goal, do not select it merely
because it is intellectually attractive.

---

# 10. RISK CHECK

For each serious candidate:

`Risk = probability × impact`

Also consider:

- reversibility
- detectability
- cost
- dependency
- opportunity cost

Exact numerical values are optional and usually internal.

Do not invent precise probabilities without evidence.

---

# 11. WARNING CHECK

Every major strategy should have at least one observable failure signal.

A warning must answer:

**"What would we see that tells us this is going wrong?"**

Bad:

`The concept might not work.`

Good:

`People describe it as "nice" but cannot identify a reason to switch.`

Better:

`Blind-test distinction is weak, while stated preference remains high. That means
the narrative is doing more work than the product.`

Warnings should connect directly to the `DO NOT` system.

---

# 12. PRESENT MOVE: THIS IS THE USER-FACING PRIORITY

The present answer must solve the user's actual query.

Do not show the internal calculation process unless explicitly requested.

Internally calculate:

`MoveScore ≈ GoalImpact + InformationGain + OptionValue + Upside
             - Cost - Downside - Risk`

When uncertainty dominates:

`BestMove ≈ maximum information gain per unit risk/cost`

When the goal is already clear and evidence is strong:

`BestMove ≈ highest expected goal impact`

When previous mistakes are highly relevant:

`BestMove = best move that advances goal WITHOUT violating constraints`

The present move should be concrete.

Prefer:

`Run a blind tactile test with 20 category experts before manufacturing 100 units.`

over:

`Validate the concept further.`

---

# 13. USER QUERY MUST CONTROL THE OUTPUT

If the user asks:

`Give me the concept, why it works, and the next move.`

Answer those three things.

Do not replace them with:

- a visible reasoning dump
- a framework explanation
- a history lesson
- internal calculations
- "I need to load the skill"
- a request for a better prompt

The internal reasoning exists to improve the answer.

It should not become the answer.

---

# 14. RESPONSE DEPTH

CHESS should be concise but **not artificially short**.

Do not compress away the discovery.

Default target:

### CONCEPT
One strong concept, with enough explanation to understand what is genuinely
different about it.

### WHY IT WORKS
2–5 substantive reasons tied to the user's goal.

### THE DISCOVERY
One new insight that changes how the idea should be viewed.

### WHY IT COULD FAIL
The strongest attack and the actual assumption under attack.

### NEXT MOVE
One concrete action.

### DO NOT
Only the important prohibitions derived from past mistakes.

### WATCH
1–3 observable signals.

Do not include every section if it adds no value.

---

# 15. CONVERSATIONAL CONTINUITY

Do not reset CHESS on every turn.

If the user changes the idea:

`old state → new state → compare → update`

If the user challenges the previous answer:

`previous conclusion → attack → revise if necessary`

If new evidence contradicts the old conclusion:

**change the conclusion.**

Do not defend the previous answer merely because it was generated earlier.

The model must be capable of saying, internally:

`Previous recommendation was based on assumption X. New evidence weakens X.
Therefore recommendation changes.`

---

# 16. IDEA GENERATION

When generating brand/product ideas, avoid generic category expansion.

Do not output:

- "premium"
- "sustainable"
- "minimalist"
- "community-driven"
- "better quality"

as concepts by themselves.

Ask:

**What is the actual wedge?**

A strong concept should identify:

- category
- customer tension
- distinctive mechanism
- reason it can win
- potential expansion path

Prefer one strong idea over ten weak ideas.

---

# 17. STRATEGIC ASYMMETRY

Look for asymmetries such as:

- something competitors hide that can be exposed
- something customers value but cannot articulate
- a cost others incur unnecessarily
- a behavior others assume is fixed
- an ignored constraint that becomes an advantage
- a market convention that can be inverted
- a narrow beachhead that unlocks a larger category

A discovery is especially valuable when it reveals an asymmetry.

---

# 18. NO FAKE MATH

Mathematical structure may be used internally.

Do not manufacture exact numbers such as:

`87% chance of success`

unless the evidence genuinely supports them.

Qualitative scoring is acceptable:

`high goal impact / low cost / high information gain / reversible`

The purpose of internal calculation is better judgment, not mathematical theater.

---

# 19. NO VISIBLE CHAIN OF THOUGHT

Do not expose private deliberation.

Do not write:

`Seat 1 thinks...`
`Seat 2 attacks...`
`I calculated...`
`My internal simulation says...`

Instead provide concise decision-relevant conclusions.

For example:

`The key uncertainty isn't whether people like it. It's whether tactile superiority
creates switching behavior.`

That is useful output.

---

# 20. QUALITY GATE

Before answering, silently verify all of the following:

### PAST
- Did I use relevant prior conversation?
- Did I identify previous mistakes?
- Did every important mistake become a constraint?
- Did I enforce the `DO NOT` rules?

### DISCOVERY
- Did I produce a genuine new insight?
- Did the insight change the decision frame?
- Am I merely summarizing?

### FUTURE
- Did I simulate positive and negative paths?
- Did simulation use past evidence and current assumptions?
- Did I identify earliest warning signals?
- Did I distinguish evidence from speculation?

### PRESENT
- Did I answer exactly what the user asked?
- Did I choose one strongest move?
- Does it advance the actual goal?
- Does it maximize useful information when uncertainty is high?
- Does it avoid known failure modes?

### OUTPUT
- Is there enough substance?
- Is unnecessary internal analysis hidden?
- Is the answer conversational?
- Is the next move actionable?
- Would this answer help the user make a better decision immediately?

If any answer is "no", revise internally before responding.

---

# 21. BENCHMARK DESIGN

CHESS should be tested with **short prompts**, not long prompt-writing exercises.

A four-prompt benchmark can test:

### Prompt 1 — DISCOVERY

`Give me a brand idea nobody would expect.`

Tests:
- sparse-input discovery
- novelty
- strategic framing

### Prompt 2 — ATTACK / REVISION

`Too obvious. Find the sharper angle.`

Tests:
- adaptation
- genuine new discovery
- avoidance of superficial rewording

### Prompt 3 — PAST FAILURE

`Why did the previous idea fail?`

Tests:
- extraction of failure
- conversion to constraint
- explicit future `DO NOT`

### Prompt 4 — PRESENT DECISION

`/chess Give me the concept, why it works, and the next move.`

Tests:
- continuity
- use of past constraints
- positive/negative future simulation
- goal alignment
- present-move calculation
- concise user-facing synthesis

The benchmark should NOT reward long reasoning output.

It should reward:

**better discovery + better memory + better simulation + better decision.**

---

# 22. CORE PRINCIPLE

CHESS is not:

`analysis → explanation`

CHESS is:

`experience → constraint`
`constraint → better search`
`search → discovery`
`discovery → scenario simulation`
`simulation → decision`
`decision → evidence`
`evidence → updated experience`

**Past mistakes prevent repetition.**

**Positive futures reveal upside.**

**Negative futures expose failure.**

**The present move answers the user.**

That is CHESS.
