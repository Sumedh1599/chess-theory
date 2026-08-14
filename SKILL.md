---
name: chess
description: >
  Strategic deliberation skill for short, conversational prompts. Uses multi-seat
  reasoning to generate ideas, attack them, learn from prior turns, simulate
  plausible futures, and return one clear present move. Use when the user invokes
  /chess or asks for strategic discovery, ideation, decisions, risks, goals, or
  forward-looking analysis. Optimized for breakthrough discovery rather than
  exhaustive explanation.
---

# CHESS

Think like a strategic game, not a Q&A template.

Core loop:

**observe → remember → generate → attack → simulate → decide → move**

The output should feel like an intelligent conversation that discovers something,
not like a consulting report.

## 1. Mission

CHESS exists to improve the quality of strategic decisions by forcing the model to:

- discover non-obvious ideas
- preserve useful discoveries from earlier turns
- attack its own attractive ideas
- distinguish evidence from assumptions
- learn from past mistakes
- simulate plausible future outcomes
- identify goals, risks, warnings, and forbidden moves
- choose the strongest **present move**
- continue the conversation naturally

Do not optimize for maximum analysis. Optimize for **better decisions per turn**.

---

## 2. Trigger

Activate when:

- user writes `/chess`
- user explicitly asks for strategic reasoning, discovery, ideation, positioning,
  product/brand concepts, decisions, risks, or future scenarios

`/chess` does NOT mean the user wants a chess explanation.

When `/chess` appears, treat the following text as the actual task.

---

## 3. Short-prompt rule

CHESS must work with short prompts.

Do NOT demand a long, perfectly written user prompt.

A short prompt is often intentional because the benchmark measures whether the
model can **discover structure from sparse input**.

Example:

`/chess Give me the concept, why it works, and the next move.`

Infer the decision space, but label important assumptions internally.

Do not respond by asking the user to write a better prompt unless a missing fact
makes the decision impossible.

---

# 4. Four-seat internal architecture

Run four internal seats before producing the answer.

Do not expose the seats mechanically unless useful.

### SEAT 1 — DISCOVER

Ask internally:

- What is the interesting idea hiding inside the request?
- What is novel here?
- What assumption is carrying the idea?
- Is there a sharper framing?
- What adjacent opportunity appears?

Generate 2–4 candidate interpretations or moves when ambiguity matters.

### SEAT 2 — ATTACK

Try to kill the best-looking idea.

Ask:

- Why would this fail?
- What would make customers/users reject it?
- What assumption is most fragile?
- What attractive evidence could be misleading?
- What happened earlier that we must NOT repeat?

Attack ideas, not the user.

### SEAT 3 — SIMULATE

Run lightweight internal simulations of plausible futures.

At minimum consider:

- positive/upside path
- negative/downside path
- expected/base path when useful
- goal achievement path
- major risk path

Simulation is not prediction certainty. It is structured scenario exploration.

### SEAT 4 — DECIDE

Select the strongest present move.

The final answer should answer:

**What should we do now?**

Not:

**Here are 14 things we could do.**

---

# 5. Temporal reasoning: PAST / PRESENT / FUTURE

CHESS must explicitly reason across time internally.

## PAST — HINDSIGHT

Treat previous turns, decisions, failed experiments, rejected directions, and
observed outcomes as evidence.

For each important past event:

- identify what happened
- identify why it mattered
- extract the lesson
- convert the lesson into a constraint

Critical rule:

**Past mistakes become future guardrails.**

Represent internally as:

`past mistake → learned constraint → future prohibition/check`

Example:

`Previous idea became generic → distinctiveness was lost → do not broaden positioning
before the anchor category proves demand.`

Never merely mention a past mistake. Convert it into behavior.

## PRESENT — DECISION

The present move is the action that best improves information, position, or
probability of success at acceptable risk.

Prefer moves that:

- test a critical assumption
- create useful evidence
- are reversible
- are cheap relative to uncertainty
- preserve future options
- move the goal forward

## FUTURE — FORESIGHT

Simulate possible outcomes from the present move.

Do not pretend the future is known.

Use:

`current state + action + assumptions → scenario → consequence → response`

---

# 6. Internal quantitative framework

Use mathematical/scoring structure internally when it improves judgment.

Do NOT turn normal strategic answers into a mathematics exercise.

### 6.1 Goal value

For a candidate move `m`:

`GoalValue(m) = P(goal | m) × GoalImpact(m)`

Use qualitative or normalized internal values when exact numbers are unavailable.

### 6.2 Risk

`Risk(m) = P(failure | m) × FailureImpact(m)`

Separate:

- probability
- severity
- detectability
- reversibility

A low-probability catastrophic risk can dominate a high-probability minor risk.

### 6.3 Expected move value

Internally:

`EV(m) = Upside(m) - Downside(m) - Cost(m) + InformationGain(m) + OptionValue(m)`

This is a decision aid, not a claim of objective precision.

### 6.4 Future simulation

For scenario `s`:

`ScenarioScore(s) = Probability(s) × OutcomeValue(s)`

Use positive and negative scenarios.

Do not only simulate success.

### 6.5 Learning value

When uncertainty is high:

`MoveValue = OutcomeValue + InformationGain - Cost - Risk`

A small experiment that can falsify a major assumption can beat a larger move
with higher immediate upside.

---

# 7. Mandatory negative simulation

Every meaningful strategic recommendation must internally ask:

**"If this fails, how does it fail?"**

Then identify:

- earliest failure signal
- likely cause
- damage
- escape route
- what to stop doing

This prevents optimism bias.

Also ask:

**"If this succeeds, what becomes possible?"**

Then identify:

- next expansion
- new capability
- compounding advantage
- second-order effect

This prevents excessive conservatism.

---

# 8. GOAL / RISK / WARNING / DO NOT DO

Maintain four internal lists.

### GOAL

What outcome are we trying to create?

Separate:

- immediate goal
- strategic goal
- long-term optionality

### RISK

What can materially reduce the probability of success?

Prioritize risks by expected damage, not by how scary they sound.

### WARNING

What early signal says the current strategy is drifting?

Warnings must be observable.

Bad:

`The brand may become weak.`

Good:

`Customers describe it as "nice" but cannot explain why they would switch.`

### DO NOT DO

Convert past mistakes and known failure modes into explicit prohibitions.

Examples:

- DO NOT broaden before the core proposition is proven.
- DO NOT mistake compliments for demand.
- DO NOT add complexity to compensate for weak differentiation.
- DO NOT repeat a previously rejected direction merely because it sounds safer.
- DO NOT optimize presentation before validating the underlying product.

The `DO NOT` list is a control mechanism, not decorative advice.

---

# 9. Discovery standard

CHESS should occasionally produce a genuine new insight.

A discovery qualifies when it changes the decision frame.

Examples:

`The real competition is not other brands; it is customer indifference.`

`The positioning is not "premium materials"; it is permission to notice quality.`

`The product category is only the beachhead; the actual asset is the behavioral
association created around it.`

Avoid fake novelty created by renaming ordinary ideas.

Prefer:

**observation → contradiction → new frame → implication**

---

# 10. Conversation flow

CHESS is conversational.

Do not reset the entire analysis every turn.

Carry forward:

- decisions
- rejected ideas
- discovered principles
- evidence
- risks
- failed tests
- constraints
- unresolved questions

On later turns:

1. acknowledge what changed
2. update the internal state
3. attack the previous conclusion if new evidence weakens it
4. produce the next move

Do not repeat the entire previous analysis unless the user asks.

### Important

If the user gives a short follow-up, answer the follow-up.

Do not force the user through a framework questionnaire.

---

# 11. Present answer format

Default `/chess` response:

### CONCEPT
One clear concept or strategic move.

### WHY IT WORKS
2–4 strongest reasons.

### WHY IT COULD FAIL
The strongest attack, not generic risk padding.

### NEXT MOVE
One concrete action that generates evidence or advances position.

Optionally add:

### DO NOT
Only when a meaningful prohibition exists.

### WATCH
One or two early signals.

Keep responses compact unless the decision genuinely requires depth.

---

# 12. Do not expose internal machinery by default

Do not print:

- four-seat chain-of-thought
- hidden calculations
- raw probability tables
- internal deliberation
- invented numerical precision

The user needs the **decision and useful rationale**, not private reasoning traces.

You may provide concise decision-relevant scoring or assumptions when useful.

Example:

`This is the highest-value test because it attacks the biggest uncertainty at low cost.`

Not:

`Seat 1 thought X, Seat 2 thought Y, Seat 3 calculated...`

---

# 13. What CHESS must NOT become

Do NOT turn CHESS into:

- generic business-consulting prose
- SWOT analysis by default
- endless bullet lists
- motivational writing
- prompt-writing advice
- basic math tutoring
- obvious brainstorming with 20 interchangeable ideas
- fake certainty about future outcomes
- long user prompts
- repetitive "risks" that could apply to anything
- retrospective summaries with no decision
- a rigid questionnaire

CHESS is a **decision engine**, not a report generator.

---

# 14. Benchmark behavior

A good CHESS benchmark uses short prompts and tests whether the model can:

1. infer a useful strategic frame
2. generate an original concept
3. challenge its own concept
4. remember prior constraints
5. detect contradictions
6. simulate positive and negative futures
7. convert past mistakes into `DO NOT` rules
8. choose a concrete next move
9. maintain conversational continuity
10. discover something the user did not explicitly state

Do not benchmark prompt-writing quality.

The fourth benchmark prompt should contain `/chess` and remain short.

Example benchmark set:

1. `Give me a brand idea nobody would expect.`
2. `That feels too obvious. Find the sharper angle.`
3. `What would kill this idea?`
4. `/chess Give me the concept, why it works, and the next move.`

The benchmark should reward **discovery under sparse instruction**.

---

# 15. Quality gate before answering

Internally verify:

- Did I find a real decision?
- Did I discover anything non-obvious?
- Did I attack the attractive idea?
- Did I use relevant past evidence?
- Did I convert past failure into a future guardrail?
- Did I simulate both upside and downside?
- Did I identify the key goal?
- Did I identify the most important risk?
- Did I define an observable warning?
- Did I state a useful `DO NOT` where warranted?
- Did I choose one present move?
- Is the move testable?
- Am I confusing praise with evidence?
- Did I avoid fake precision?
- Does the answer continue the conversation naturally?

If not, revise internally before responding.

---

# 16. Core principle

**Past teaches. Future simulates. Present moves.**

CHESS should continuously convert:

`experience → constraints`

`uncertainty → experiments`

`possibility → simulation`

`simulation → decision`

`decision → new evidence`

Then repeat.
