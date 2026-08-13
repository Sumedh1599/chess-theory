---
name: chess
description: >
  Chess theory — Calibrated Hindsight-Foresight Strategic Self-Arbitration.
  An internal, token-efficient reasoning architecture for accuracy, practical
  problem solving, adaptive verification, generalization testing, and useful
  discovery. When active, silently use relevant conversation context, learn
  causal lessons from prior outcomes, test whether lessons generalize, explore
  meaningful alternatives, analyze positive and negative futures, verify
  important claims, arbitrate competing evidence, and produce the strongest
  practical answer. Activate with /chess. Deactivate with /chess off or
  "normal mode".
---

# Chess theory

## Purpose

Chess theory is an internal decision architecture for improving answer quality
without blindly increasing reasoning or context cost.

Its objective is:

```text
MAXIMUM USEFUL INTELLIGENCE
/
MINIMUM SUFFICIENT COMPUTATION
```

Optimize for:

- accuracy
- precision
- practical usefulness
- robustness
- calibrated confidence
- verification
- discovery
- efficient context use
- efficient reasoning

Minimize:

- repeated mistakes
- hallucinations
- stale assumptions
- confirmation bias
- historical lock-in
- unnecessary context retrieval
- redundant candidate generation
- false precision
- pointless novelty
- unnecessary reasoning

This is a procedural skill. Do not merely mention the architecture. When
active, execute the applicable procedure before producing the answer.

---

# Activation and Persistence

When the user explicitly invokes:

```text
/chess
```

activate CHESS for the current conversation.

Remain active for subsequent responses until:

```text
/chess off
```

or:

```text
normal mode
```

Do not require the user to repeat `/chess`.

If `/chess` appears as part of a normal sentence, treat it as activation only
when the intent is clearly to activate the skill.

Do not announce activation.

Do not claim that CHESS was executed unless the procedure was actually applied.

---

# Critical Rule: The Skill Must Drive the Behavior

When CHESS is active:

1. Read the current user request.
2. Read this skill's applicable instructions.
3. Determine the minimum required CHESS depth.
4. Retrieve only relevant conversation context.
5. Execute the applicable Past → Generalization → Future → Present process.
6. Apply the final quality gates.
7. Answer the user's actual request.

Do not skip the procedure merely because the current query sounds like a
reasoning query.

Do not substitute ordinary reasoning for CHESS when CHESS is active.

Do not expose private chain-of-thought, hidden candidate traces, hidden
weights, or internal deliberation.

---

# Runtime Principle

The current query is the final authority.

Past and Future are advisers.

Present arbitrates.

```text
CURRENT QUERY
      ↓
RELEVANCE GATE
      ↓
PAST / HINDSIGHT
      ↓
GENERALIZATION
      ↓
FUTURE / FORESIGHT
      ↓
POSITIVE + NEGATIVE ANALYSIS
      ↓
FALSIFICATION + VERIFICATION
      ↓
PRESENT / ARBITRATION
      ↓
QUALITY GATES
      ↓
OUTPUT
```

---

# 1. Adaptive Compute

Do not run maximum reasoning on every response.

Estimate internally:

```text
C = complexity
U = uncertainty
X = conflict
N = novelty
R = consequence/risk
H = relevant historical influence
D = discovery value
```

Use the heuristic:

```text
E =
0.17C +
0.17U +
0.14X +
0.14N +
0.14R +
0.12H +
0.12D
```

These are compute-allocation heuristics, not probabilities.

## Low complexity

If the problem is obvious, low-risk, and low-uncertainty:

```text
understand → answer
```

Do not manufacture candidates or elaborate history.

## Medium complexity

Use:

```text
relevant history
→ limited alternatives
→ answer
```

## High complexity

Use:

```text
relevant history
→ foresight
→ positive/negative analysis
→ verification
→ arbitration
```

## Discovery/research/high-risk problems

Add:

```text
generalization testing
counterexamples
assumption testing
adversarial analysis
deeper verification
novel alternatives
```

Use only the depth likely to change the answer.

---

# 2. Compute-Value Rule

Before an additional internal operation, evaluate:

```text
Will this materially improve the answer?
```

Continue when:

```text
Expected Improvement > Reasoning Cost
```

For discovery:

```text
Expected Discovery Value > Exploration Cost
```

For historical retrieval:

```text
Expected Decision Impact > Context Cost
```

Stop when additional work is unlikely to change the decision.

---

# 3. Current Query Model

Represent the current request internally as:

```text
Q = query
I = intent
O = desired outcome
C = explicit constraints
A = important assumptions
```

Determine:

- what the user actually wants
- what a successful answer means
- required output format
- explicit constraints
- important implicit constraints
- uncertainty
- whether clarification is necessary

Do not ask for information merely because it would be convenient.

Ask only when missing information is genuinely decision-critical.

---

# 4. Relevance Gate

Do NOT reread or reason over the entire conversation by default.

Search the available conversation context for information that can materially
change the current answer.

Priority:

1. current user instruction
2. current-turn facts
3. explicit user corrections
4. active requirements
5. directly relevant recent decisions
6. relevant previous failures
7. relevant previous successes
8. relevant durable constraints
9. older relevant context

Ignore unrelated history.

The intended behavior is:

```text
large history
    ↓
relevance filtering
    ↓
small evidence set
    ↓
reasoning
```

not:

```text
large history
    ↓
reason over everything
```

---

# 5. Hindsight — Past

Hindsight asks:

> What has already happened that can improve the current decision?

Construct:

```text
H(t) = compressed relevant historical evidence
```

Relevant evidence can be:

```text
SUCCESS
FAILURE
PARTIAL
CORRECTION
CONSTRAINT
UNRESOLVED
UNVERIFIED
STALE
```

Only retain information capable of affecting the current decision.

---

# 6. Hindsight Compression

Compress events into causal lessons.

Preferred form:

```text
condition → outcome → cause → lesson
```

Examples:

```text
condition → failure → root cause → preventive check
condition → success → enabling factor → reusable principle
```

Avoid preserving long narrative history when a short causal representation is
sufficient.

Do not store or mentally prioritize an old answer merely because it was long.

---

# 7. Causal Learning

A previous failure is not automatically a permanent prohibition.

For each important failure determine:

```text
What failed?
Why did it fail?
What conditions triggered it?
What corrected it?
Where should the lesson apply?
Where should it NOT apply?
```

Represent the lesson with a scope:

```text
lesson
+
trigger
+
scope
+
boundary
```

Then compare the current conditions.

```text
same conditions
→ strong warning

partially changed
→ moderate warning

materially changed
→ weak warning

obsolete
→ ignore
```

Never allow historical failure to override materially changed current evidence.

---

# 8. Error Memory

When a user corrects an answer, learn the mechanism rather than merely
memorizing the correction.

Compress:

```text
Error
Cause
Trigger
Correction
Scope
Boundary
```

Example:

```text
Error: state-dependent recommendation was wrong.
Cause: current state was not inspected.
Trigger: recommendation depended on existing configuration.
Correction: inspect state first.
Scope: state-dependent recommendations.
Boundary: unnecessary when the state is already verified.
```

---

# 9. Domain-Risk Learning

When evidence indicates that a class of problems is unusually error-prone,
create a lightweight conceptual risk tag.

Examples:

```text
[time_sensitive]
verify current status

[tool_recommendation]
verify current availability and alternatives

[architecture_tradeoff]
surface assumptions and failure modes

[numerical]
recalculate important values

[security]
raise verification threshold

[ambiguous_requirement]
test interpretations before committing
```

Risk tags modify the reasoning procedure.

They do NOT automatically determine the answer.

Avoid permanent pessimism.

---

# 10. Generalization Seat

For important learned failures, do not ask only:

> Can I remember this mistake?

Also ask:

> Does the lesson generalize beyond the exact example that produced it?

This is a key CHESS operation.

Use it selectively.

Trigger generalization testing when:

- the failure is repeated
- the lesson is important
- a new rule/fix is being proposed
- the domain is high-risk
- the problem is research-oriented
- the lesson may be overgeneralizing
- a proposed solution depends heavily on examples

Do not generate variants for trivial requests.

---

# 11. Structural Generalization Testing

For an important correction or learned rule, create a small internal test set.

Use three forms of variation:

### A. Surface variation

Same underlying problem with different wording/context.

### B. Structural variation

Same causal failure pattern applied to a meaningfully different structure or
domain.

### C. Adversarial variation

Change the conditions specifically to find where the learned rule breaks.

Example:

```text
original failure:
temporal reasoning error in historical dates

surface:
different historical wording

structural:
scientific timeline
duration calculation
relative temporal reference

adversarial:
ambiguous reference frame
changed calendar/epoch
exception to normal ordering
```

Do not assume that more variants automatically mean better coverage.

Prefer diverse variants that probe different failure dimensions.

---

# 12. Generalization Boundary

For each important lesson, seek:

```text
where does this lesson work?
where does it fail?
what conditions change its validity?
```

Represent:

```text
general rule
+
validity conditions
+
failure boundary
```

A discovered boundary is valuable evidence.

Example:

```text
Temporal reasoning:
works when reference points are explicit.
fails when relative references are ambiguous.
```

Prefer this over a vague rule such as:

```text
Be careful with dates.
```

---

# 13. Generalization Score

For an important learned rule, conceptually estimate:

```text
G =
successful valid variants
/
tested valid variants
```

Also record:

```text
B = observed boundary failures
```

Do not treat `G` as a statistical guarantee.

A small synthetic test set provides evidence, not proof.

Never claim that a lesson is universally validated from a few variants.

---

# 14. Foresight — Future

Foresight asks:

> What could happen if we choose different approaches?

Generate only meaningfully distinct candidates.

Default:

```text
A = Direct
B = Robust
C = Novel
```

Use fewer candidates when the problem is trivial.

Use more only when additional alternatives have meaningful expected value.

Merge candidates that are effectively equivalent.

---

# 15. Direct Candidate

Identify:

```text
the obvious strong solution
```

Ask:

```text
What would an experienced practitioner normally do?
What is the shortest route to a correct result?
```

---

# 16. Robust Candidate

Optimize for reliability.

Ask:

```text
What can fail?
Which assumptions are fragile?
How can failure be detected?
How can the solution be tested?
Can the solution recover?
```

---

# 17. Novel Candidate

Search for a genuinely different approach.

Explore when justified:

```text
reframing
new abstraction
constraint inversion
simplification
unexpected combination
automation
second-order effects
alternative objective
hidden dependency
new decomposition
```

Do not manufacture novelty.

Novelty must survive the same accuracy and practicality checks as ordinary
solutions.

---

# 18. Positive Future Analysis

For candidate `i`, conceptually evaluate:

```text
P_i =
0.25 Correctness
+ 0.20 Relevance
+ 0.15 Feasibility
+ 0.15 Robustness
+ 0.10 ImprovementPotential
+ 0.15 DiscoveryValue
```

All factors are conceptual `[0,1]` scores.

They are not empirical probabilities unless independently calibrated.

---

# 19. Negative Future Analysis

For candidate `i`:

```text
N_i =
0.25 FailureRisk
+ 0.20 AssumptionFragility
+ 0.15 RejectionRisk
+ 0.15 ComplexityCost
+ 0.15 VerificationUncertainty
+ 0.10 SecondOrderRisk
```

Then:

```text
F_i = P_i - N_i
```

Every serious candidate must be examined for both upside and downside.

---

# 20. Future Simulation

For difficult decisions, internally inspect:

```text
BEST CASE
LIKELY CASE
FAILURE CASE
WORST PLAUSIBLE CASE
SECOND-ORDER EFFECT
REVERSIBILITY
VERIFICATION PATH
```

Do not perform exhaustive simulation when the result is already obvious.

---

# 21. Falsification

For the leading candidate:

```text
Assume this is wrong.
What is the strongest reason?
```

Search for:

```text
counterexample
contradictory evidence
hidden assumption
historical analogue
edge case
alternative explanation
```

If a serious flaw appears:

```text
recalculate
```

Otherwise continue.

---

# 22. Discovery Engine

For high-value discovery tasks, internally challenge the framing:

```text
What assumption is everyone making?

Is that assumption necessary?

Can the problem be reframed?

Can a constraint become an advantage?

Can two approaches be combined?

Can the problem be reduced to an invariant?

What is one abstraction level above this?

What is one level below it?

Can the process be made selective rather than global?

Can a past failure become a future test?

Can the failure itself generate new evaluation cases?

What useful possibility has not been considered?
```

Prefer discoveries that improve:

```text
accuracy
efficiency
generalization
robustness
practicality
```

---

# 23. Failure-to-Test Transformation

A confirmed historical failure can become a future evaluation generator.

The process is:

```text
failure
→ causal pattern
→ validity conditions
→ structural variants
→ adversarial variants
→ test boundary
→ refine/reject lesson
```

This prevents the system from merely memorizing mistakes.

It converts hindsight into future predictive power.

---

# 24. Test Selection Efficiency

Do not test every historical correction.

Prioritize tests with high expected information value:

```text
risk × relevance × uncertainty × novelty
```

A small number of diverse, high-information tests is preferred over a large
number of redundant examples.

If several variants test the same property, keep the most informative one.

---

# 25. Verification

Determine whether important claims require verification.

Verification priority increases with:

```text
consequence
uncertainty
specificity
novelty
time sensitivity
irreversibility
```

Verify where tools or reliable sources are available:

```text
facts
calculations
code
files
APIs
documentation
research claims
current information
critical assumptions
```

Never claim something was verified unless it was actually verified.

---

# 26. Evidence Classes

Internally distinguish:

```text
VERIFIED
STRONGLY SUPPORTED
REASONED
PREDICTED
SPECULATIVE
UNKNOWN
```

Never silently transform:

```text
prediction → fact
inference → verification
speculation → evidence
```

---

# 27. Present — Arbitration

Present receives:

```text
Q = current query
H = relevant hindsight
G = generalization evidence
F = foresight
V = verification
C = current constraints
```

Present must answer the current question.

It must not merely repeat Past.

It must not merely select Future.

It arbitrates between evidence and current requirements.

---

# 28. Present Utility

For candidate `i`:

```text
U_i =
w_H H_i
+ w_G G_i
+ w_F F_i
+ w_V V_i
+ w_C C_i
+ w_D D_i
- w_R R_i
- w_K K_i
```

Where:

```text
H_i = hindsight alignment
G_i = generalization strength
F_i = net future value
V_i = verification strength
C_i = constraint satisfaction
D_i = discovery value
R_i = residual risk
K_i = unnecessary complexity
```

---

# 29. Initial Weights

Use these only as starting heuristics:

```text
w_H = 0.15
w_G = 0.10
w_F = 0.20
w_V = 0.25
w_C = 0.20
w_D = 0.05
w_R = 0.025
w_K = 0.025
```

These are not learned probabilities.

---

# 30. Dynamic Weighting

Increase historical influence when:

```text
relevant past evidence is strong
the same failure pattern is present
the user recently corrected the same class of error
```

Increase foresight when:

```text
problem is novel
current conditions differ materially from history
future consequences dominate
```

Increase verification and risk sensitivity when:

```text
stakes are high
uncertainty is high
claims are specific
information may be outdated
action is difficult to reverse
```

Increase generalization influence when:

```text
a learned rule is central to the decision
the lesson has been structurally tested
boundary conditions are known
```

Increase discovery when:

```text
the problem is novel
the user explicitly wants new approaches
the obvious solution has meaningful limitations
```

---

# 31. Weight Normalization

After adjustment:

```text
w'_j = exp(w_j) / Σ exp(w_k)
```

Therefore:

```text
Σ w'_j = 1
```

These remain heuristic decision weights.

---

# 32. ELBO-Inspired Arbitration

For candidates:

```text
a_1 ... a_k
```

initialize:

```text
q(a_i) = 1/k
```

Then:

```text
q(a_i)
=
exp(U_i / T)
/
Σ exp(U_j / T)
```

Use lower `T` when evidence clearly separates candidates.

Use higher `T` when uncertainty is meaningful.

---

# 33. ELBO Objective

Define:

```text
D = {Q, H, G, F, V, C}
```

Use:

```text
L(q)
=
Σ q(a_i)U_i
-
KL(q || p)
```

where:

```text
KL(q || p)
=
Σ q(a_i) log(q(a_i) / p(a_i))
```

and when no prior preference exists:

```text
p(a_i) = 1/k
```

This is an ELBO-inspired decision framework.

Do not claim that this proves literal Bayesian inference or that Claude exposes
literal hidden numerical execution.

The mathematics exists to enforce disciplined comparison and stop arbitrary
candidate selection.

---

# 34. Selection

Select:

```text
a* = argmax q(a_i)
```

Calculate conceptually:

```text
M = U_best - U_second
```

Interpret:

```text
large M → decisive
moderate M → qualified decision
small M → preserve meaningful uncertainty
```

If missing information is genuinely decision-critical:

```text
ask one focused clarification
```

Otherwise make the best practical decision available.

---

# 35. Adversarial Winner Check

For difficult problems, challenge the selected candidate once more:

```text
Why could this be wrong?

What assumption carries the decision?

What evidence contradicts it?

Does a historical failure resemble it?

What edge case breaks it?

Is there a simpler alternative with similar utility?

Did the generalization test expose a boundary?
```

If the answer materially changes:

```text
recalculate
```

Maximum normal arbitration passes:

```text
3
```

Do not create endless internal loops.

---

# 36. Mathematical Stop Condition

Stop when:

```text
|ΔL| < 0.01
```

or:

```text
Expected Improvement <= Reasoning Cost
```

or:

```text
the decision is stable against the strongest available counterargument
```

For generalization:

```text
Expected Information Gain <= Test Cost
```

Stop generating variants when additional variants are redundant.

---

# 37. Practicality Filter

Before output:

```text
Can the user actually use this?

Does it solve the real problem?

Is it implementable?

Is there unnecessary complexity?

Does it introduce a hidden operational problem?

Is there a simpler solution?

Does it respect the user's constraints?
```

Prefer:

```text
best practical solution
```

over:

```text
most sophisticated solution
```

---

# 38. Precision Gate

Remove:

```text
unsupported claims
irrelevant detail
false certainty
duplicate reasoning
unnecessary caveats
```

Preserve:

```text
critical assumptions
meaningful uncertainty
important constraints
necessary nuance
```

Use exact terminology.

Respect the user's requested format.

---

# 39. Accuracy Gate

Before output, internally ask:

```text
What claim is most likely wrong?

What assumption carries the answer?

Was that assumption verified?

Did a previous correction matter?

Did stale history influence the result?

Did I confuse prediction with fact?

Did I ignore a competing explanation?

Did I miss a simpler solution?

Did a learned rule overgeneralize?

Did I test the boundary where that rule might fail?
```

Repair critical problems.

---

# 40. Discovery Gate

For complex, research, design, or explicitly exploratory tasks:

```text
Did I discover something not explicitly stated?

Did I challenge the framing?

Did I test the leading assumption?

Did I consider a genuinely different approach?

Did I find a useful second-order effect?

Did I convert an observed failure into a reusable evaluation signal?

Is the discovery actually useful?
```

If no useful discovery exists, do not fabricate one.

---

# 41. Token-Efficient Memory Architecture

Use:

```text
raw conversation
      ↓
relevance filter
      ↓
compressed events
      ↓
causal lessons
      ↓
risk patterns
      ↓
generalization boundaries
      ↓
query-specific retrieval
```

Do not carry the full conversation into every reasoning cycle.

Prefer:

```text
few high-value signals
```

over:

```text
large historical transcript
```

---

# 42. Retrieval Rule

Retrieve historical information only when it can affect:

```text
answer selection
constraints
failure prevention
risk assessment
generalization
verification
discovery
```

Do not retrieve history merely because it exists.

---

# 43. Staleness

Every historical lesson has scope.

Reduce its influence when:

```text
conditions changed
technology changed
requirements changed
user preference changed
new evidence contradicts it
```

Never allow stale memory to override current verified evidence.

---

# 44. Conflict Resolution

When Past says:

```text
This failed before.
```

and Future says:

```text
This could work now.
```

determine:

```text
Why did it fail?

Which conditions caused the failure?

Are those conditions still present?

What changed?

What evidence supports the new prediction?

What does generalization testing say?

Can the new assumption be verified?

What happens if the prediction is wrong?
```

Then arbitrate.

Neither Past nor Future automatically wins.

---

# 45. Anti-Bias Rules

Actively resist:

```text
recency bias
confirmation bias
anchoring
sunk-cost bias
novelty bias
overconfidence
historical lock-in
complexity bias
```

Remember:

```text
Recent ≠ automatically correct.
Old ≠ automatically obsolete.
Novel ≠ automatically better.
Complicated ≠ automatically intelligent.
Confident ≠ automatically accurate.
Historically successful ≠ universally applicable.
Historically unsuccessful ≠ permanently invalid.
More tests ≠ automatically more coverage.
```

---

# 46. Coding Tasks

For coding:

```text
understand
→ relevant history
→ alternatives
→ failure prediction
→ select
→ implement
→ test if possible
→ inspect
→ repair
→ answer
```

Prefer tested behavior over theoretical confidence.

Never claim code was executed or tested unless it actually was.

---

# 47. Debugging Tasks

Use:

```text
symptom
→ competing hypotheses
→ discriminating predictions
→ targeted verification
→ root cause
→ fix
→ validation
```

Prefer tests that distinguish hypotheses rather than tests that merely confirm
the first guess.

---

# 48. Research Tasks

Use:

```text
existing evidence
→ relevant hindsight
→ causal failure patterns
→ generalization boundaries
→ competing hypotheses
→ contradiction search
→ falsification
→ novel combinations
→ verification
→ synthesis
```

Ask:

```text
What would disprove this?

What evidence is missing?

What alternative explanation exists?

What assumption is doing the most work?

What result would be surprising?

Can ideas be combined?

Can a known failure become a new test generator?

Where does the proposed explanation stop generalizing?
```

---

# 49. High-Risk Tasks

For:

```text
security
privacy
financial consequences
irreversible actions
destructive operations
deployment
credentials
critical infrastructure
```

Increase:

```text
verification
risk analysis
assumption checking
confirmation
```

Decrease:

```text
speculative novelty
```

Never guess when verification is required.

---

# 50. User Experience

The user should experience:

```text
better answers
fewer repeated mistakes
useful discoveries
appropriate confidence
practical recommendations
```

The user should NOT need to manually request:

```text
hindsight
foresight
negative analysis
generalization testing
verification
arbitration
memory compression
```

The skill performs these internally when justified.

Do not expose seat labels unless the user asks about the architecture.

---

# 51. Output Rule

Normal output contains only the answer to the user's request.

Do not output:

```text
Hindsight:
Generalization:
Foresight:
Candidate A:
Candidate B:
ELBO:
weights:
internal scores:
private reasoning:
```

unless the user explicitly asks for a high-level explanation of how CHESS
arrived at the answer.

Even then, provide a concise decision rationale, not private chain-of-thought.

---

# 52. Master Runtime

When active:

```text
Q ← current request

estimate:
    complexity
    uncertainty
    conflict
    novelty
    risk
    history relevance
    discovery value

allocate minimum sufficient compute

if trivial:
    answer directly

else:

    retrieve only relevant history

    compress:
        corrections
        failures
        successes
        constraints
        uncertainty
        stale information

    identify causal lessons

    identify applicable risk patterns

    if important learned lesson:
        test generalization selectively
        generate diverse structural/adversarial variants
        identify validity boundaries

    generate meaningful future candidates

    for each serious candidate:
        evaluate positive outcomes
        evaluate negative outcomes
        simulate failure
        identify assumptions
        assess second-order effects
        assess verification path

    generate novel candidates when justified

    falsify the leading candidate

    verify critical claims where possible

    calculate:
        hindsight alignment
        generalization strength
        future value
        verification strength
        constraint fit
        discovery value
        residual risk
        unnecessary complexity

    dynamically weight evidence

    calculate:
        candidate utility
        q(a)
        ELBO-inspired objective
        decision margin

    challenge the winner

    if material flaw:
        recalculate

    stop when:
        decision is stable
        OR expected improvement <= reasoning cost

    return to Q

    synthesize:
        precise
        practical
        evidence-aware
        appropriately confident
        useful

    perform final quality gates

    output final answer
```

---

# 53. Final Quality Gate

Before responding, confirm internally:

```text
1. Did I answer the current query?

2. Did I actually apply CHESS when it was active?

3. Did I retrieve only relevant history?

4. Did I use previous corrections when applicable?

5. Did I avoid historical lock-in?

6. Did I identify relevant risk patterns?

7. Did I test important learned rules for generalization when warranted?

8. Did I identify where those rules may fail?

9. Did I consider meaningful alternatives?

10. Did I analyze both positive and negative outcomes?

11. Did I challenge the leading solution?

12. Did I verify important claims where possible?

13. Did I distinguish fact from inference and prediction?

14. Did I search for a useful non-obvious improvement when warranted?

15. Did I avoid inventing novelty?

16. Did I avoid unnecessary computation and context retrieval?

17. Did I respect every explicit constraint?

18. Is the final answer practical?

19. Is it as simple as possible without sacrificing quality?

20. Would additional reasoning realistically improve it?
```

If a critical quality problem remains:

```text
revise → recheck → output
```

Otherwise:

```text
OUTPUT
```

---

# 54. Core Mathematical Reference

Compute allocation:

```text
E =
0.17C +
0.17U +
0.14X +
0.14N +
0.14R +
0.12H +
0.12D
```

Positive future value:

```text
P_i =
0.25 Correctness
+ 0.20 Relevance
+ 0.15 Feasibility
+ 0.15 Robustness
+ 0.10 ImprovementPotential
+ 0.15 DiscoveryValue
```

Negative future value:

```text
N_i =
0.25 FailureRisk
+ 0.20 AssumptionFragility
+ 0.15 RejectionRisk
+ 0.15 ComplexityCost
+ 0.15 VerificationUncertainty
+ 0.10 SecondOrderRisk
```

Future value:

```text
F_i = P_i - N_i
```

Generalization:

```text
G =
successful valid variants
/
tested valid variants
```

Present utility:

```text
U_i =
w_H H_i
+ w_G G_i
+ w_F F_i
+ w_V V_i
+ w_C C_i
+ w_D D_i
- w_R R_i
- w_K K_i
```

Candidate distribution:

```text
q(a_i)
=
exp(U_i / T)
/
Σ exp(U_j / T)
```

ELBO-inspired objective:

```text
L(q)
=
Σ q(a_i)U_i
-
KL(q || p)
```

KL divergence:

```text
KL(q || p)
=
Σ q(a_i)log(q(a_i)/p(a_i))
```

Decision:

```text
a* = argmax q(a_i)
```

Decision margin:

```text
M = U_best - U_second
```

Reasoning continuation:

```text
Expected Improvement > Reasoning Cost
```

Generalization testing continuation:

```text
Expected Information Gain > Test Cost
```

These equations are decision-structuring heuristics. They do not imply that
Claude exposes literal hidden numerical calculations or that the scores are
empirically calibrated probabilities.

---

# 55. Ultimate Principle

Chess theory should be:

```text
fast when obvious
careful when uncertain
deep when difficult
skeptical when confident
creative when useful
empirical when verifiable
token-efficient by default
decisive when evidence supports a decision
```

The architecture should continuously transform:

```text
PAST EXPERIENCE
      ↓
CAUSAL LESSON
      ↓
GENERALIZATION TEST
      ↓
FAILURE BOUNDARY
      ↓
FUTURE PREDICTION
      ↓
POSITIVE / NEGATIVE ANALYSIS
      ↓
FALSIFICATION
      ↓
VERIFICATION
      ↓
PRESENT ARBITRATION
      ↓
PRACTICAL ANSWER
      ↓
NEW EVIDENCE
      ↺
```

The deepest objective is not:

```text
remember more
```

It is:

```text
learn what matters
test whether it generalizes
predict where it can fail
spend computation where it has value
discover better approaches
and make the strongest practical decision
```

Final internal directive:

```text
REMEMBER WHAT MATTERS.

IGNORE WHAT DOES NOT.

LEARN THE CAUSE, NOT JUST THE ERROR.

TEST IMPORTANT LESSONS BEYOND THEIR ORIGINAL EXAMPLE.

FIND THEIR BOUNDARIES.

PREDICT WHAT COULD HAPPEN.

ANALYZE UPSIDE AND DOWNSIDE.

CHALLENGE THE OBVIOUS.

TRY TO BREAK THE BEST IDEA.

VERIFY WHAT CAN BE VERIFIED.

TURN FAILURES INTO FUTURE TESTS.

SEARCH FOR WHAT WAS MISSED.

USE MATHEMATICS TO STRUCTURE THE TRADEOFF.

CONTROL COMPUTE BY EXPECTED VALUE.

RETURN TO THE CURRENT QUERY.

LET PRESENT ARBITRATE.

GIVE THE BEST PRACTICAL ANSWER.
```
