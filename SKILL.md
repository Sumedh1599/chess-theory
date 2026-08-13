---
description: Calibrated discovery and self-arbitration skill for Claude.
  Use for /chess, genuine discovery, difficult derivation, false-premise
  detection, and high-risk reasoning.
name: chess
---

# CHESS --- Calibrated Hindsight--Foresight Strategic Self-Arbitration

## 0. Purpose

CHESS is a **discovery and falsification mode**, not a mode for making
answers sound novel.

Its goals are to:

1.  Learn from prior failures and corrections.
2.  Extract the underlying failure mechanism.
3.  Test that mechanism on structural variants.
4.  Detect false premises, nonexistent problems, dimensional errors, and
    unsupported universal claims.
5.  Generate candidate solutions or discoveries.
6.  Attack candidates before presenting them.
7.  Separate facts, deductions, hypotheses, and genuine discoveries.
8.  Find the cheapest decisive validation.
9.  Produce the strongest practical answer with minimal unnecessary
    tokens.

> **Discovery is not novelty of wording. A discovery candidate must add
> a new mechanism, invariant, derivation, bound, construction,
> generalization, or falsifiable prediction that survives attempts to
> break it.**

------------------------------------------------------------------------

# 1. Mandatory Skill-Read Rule

When `/chess` is invoked:

-   Read this entire skill before substantive reasoning.
-   Apply its rules to the current request.
-   Identify the requested discovery target.
-   Identify relevant prior failures in the conversation.
-   Only then solve the problem.

Never claim "skill activated" merely because `/chess` appeared.

If the environment supports explicit skill loading, verify that the
skill was actually loaded.

Do not activate CHESS merely because a user says "think deeply" or "be
creative." Explicit `/chess` invocation always activates it.

------------------------------------------------------------------------

# 2. Token-Efficient Operating Principle

Use:

``` text
QUERY
  ↓
TARGET
  ↓
KNOWN / UNKNOWN
  ↓
PAST FAILURE SIGNALS
  ↓
CANDIDATES
  ↓
FALSIFICATION
  ↓
STRUCTURAL VARIANTS
  ↓
CHEAPEST VALIDATION
  ↓
ARBITRATION
  ↓
ANSWER
```

Do not expose hidden chain-of-thought. Give the user the useful
conclusions, decisive reasoning, counterexamples, and validation path.

Do not generate many equivalent candidates when one decisive candidate
is enough.

------------------------------------------------------------------------

# 3. Parse the Request

Extract internally:

``` text
Goal:
What exactly must be discovered, solved, derived, or constructed?

Domain:
Math / science / engineering / business / systems / other.

Constraints:
Accuracy, latency, token budget, available data, etc.

Novelty requirement:
New theorem? New heuristic? New synthesis? Better existing solution?

Validation standard:
What proof, observation, experiment, benchmark, or counterexample would distinguish success from failure?
```

If the premise is uncertain, say:

> "The premise is not established. I will treat it as a hypothesis and
> test it."

If the requested object cannot exist under the stated constraints, say
so instead of inventing one.

------------------------------------------------------------------------

# 4. Evidence Labels

Classify important conclusions as:

### FACT

Established by supplied material, verified sources, mathematics, or
reproducible calculation.

### DEDUCTION

Follows from stated assumptions and valid reasoning.

### HYPOTHESIS

Plausible but unverified.

### DISCOVERY CANDIDATE

A potentially new/generalizable result that survived initial testing but
still needs validation.

### VERIFIED DISCOVERY

Use only when actually demonstrated by proof, experiment, benchmark, or
appropriate external evidence.

Never promote a hypothesis to a discovery merely because it sounds
elegant.

------------------------------------------------------------------------

# 5. Hindsight: Learn From Failure

When prior mistakes/corrections exist, extract:

``` text
Failure:
What specifically went wrong?

Mechanism:
Why did it fail?

General lesson:
What property caused the failure?

Boundary:
Where does that lesson stop applying?

Test:
What would expose the same failure elsewhere?
```

Do not merely replay old examples.

The important object is the **failure mode**.

Example:

``` text
Surface failure:
A date comparison failed in a treaty question.

Underlying failure:
The reasoning treated dates as independent of reference context.

Structural variants:
- historical chronology
- geological dating
- evolutionary timelines
- astronomical events
- relative-time expressions
```

This converts mistake memory into a reusable testing signal.

------------------------------------------------------------------------

# 6. Structural-Variant Testing

For each important failure mode ask:

> What can change while the underlying failure mechanism remains the
> same?

Useful transformation axes include:

``` text
domain
scale
units
time horizon
causal direction
surface wording
data distribution
boundary conditions
noise
initial conditions
symmetry
parameter regime
```

A good variant preserves the mechanism while changing the surface.

Bad:

``` text
Original question with synonyms.
```

Good:

``` text
Same reasoning failure in a different domain or structural configuration.
```

Default budget:

``` text
1 original + 2–4 high-value structural variants
```

Do not create hundreds of variants without a statistical reason.

------------------------------------------------------------------------

# 7. Discovery ≠ Novel Wording

Do not call something a discovery because:

-   it uses new notation;
-   it combines familiar terms;
-   it sounds sophisticated;
-   it has not appeared earlier in the conversation;
-   the model cannot immediately recall an identical expression.

A useful discovery candidate should contribute at least one of:

``` text
new mechanism
new invariant
new derivation
new algorithm
new bound
new reduction
new experimental prediction
new generalization
new counterexample
new practical architecture
```

A strong discovery often comes from proving that an intuitive approach
fails and identifying the missing variable.

------------------------------------------------------------------------

# 8. False-Premise Defense

Before solving a requested "new formula" or "new solution," test:

1.  Is the problem well-defined?
2.  Does the target quantity exist?
3.  Is the proposed boundary meaningful?
4.  Are the variables sufficient?
5.  Are dimensions/units compatible?
6.  Is the requested universal claim possible?
7.  Is there already a standard solution?
8.  Is correlation being confused with causation?
9.  Are hidden assumptions required?

If the premise is false:

``` text
Do not manufacture a solution.
Identify the missing assumption or contradiction.
State the strongest restricted result.
```

A correct refusal to a nonexistent problem is a successful CHESS result.

------------------------------------------------------------------------

# 9. Mathematical Sanity Checks

For every proposed formula:

## 9.1 Dimensional analysis

Both sides must have compatible units.

## 9.2 Limiting cases

Test:

``` text
x → 0
x → ∞
noise → 0
response time → 0
response time → ∞
coupling → 0
boundary → ∞
```

## 9.3 Symmetry

Check whether expected symmetries are preserved.

## 9.4 Degenerate cases

Test equal forces, vanished forces, identical variables, boundary
conditions, and missing information.

## 9.5 Counterexamples

Actively search for a case where the formula produces the wrong
conclusion.

A formula is not ready merely because it works on the motivating
example.

------------------------------------------------------------------------

# 10. Generalization Test

When practical, test important candidates on at least three structurally
different examples.

For example:

``` text
physical system
economic system
biological system
```

Only transfer a principle when its assumptions actually transfer.

The key question is:

> Does the mechanism survive when the surface representation changes?

If it works only in one domain, label it domain-specific.

------------------------------------------------------------------------

# 11. Two-Axis Robustness Test

### Axis A --- Surface variation

Change:

-   wording
-   domain
-   scale
-   representation

while preserving the underlying problem.

### Axis B --- Mechanism variation

Change:

-   causal mechanism
-   parameter regime
-   boundary condition
-   response dynamics

while preserving the apparent surface problem.

A robust principle should survive Axis A and correctly identify its
boundary under Axis B.

------------------------------------------------------------------------

# 12. Contrastive Arbitration

Never evaluate a candidate in isolation.

Compare:

``` text
A = current/default approach
B = proposed discovery
C = simplest alternative/null hypothesis
```

Ask:

1.  What does B explain that A cannot?
2.  Where does B fail?
3.  Can C explain the same result more simply?
4.  Is B merely a reformulation?
5.  What observation distinguishes them?

Prefer the simplest explanation that survives the evidence.

------------------------------------------------------------------------

# 13. Discovery Scorecard

Internally evaluate candidates:

``` text
Correctness        0–5
Generality         0–5
Novel contribution 0–5
Falsifiability     0–5
Practical value    0–5
Assumption burden  0–5  (higher = worse)
```

Do not expose the score unless it helps the user.

High novelty with low correctness is rejected.

Low novelty with high practical value may still be the best answer when
the user wants a working solution rather than a publishable discovery.

------------------------------------------------------------------------

# 14. Failure-to-Discovery Loop

Use:

``` text
failed simple rule
      ↓
counterexample
      ↓
identify missing variable
      ↓
generalize
      ↓
derive candidate
      ↓
attack candidate
      ↓
new test
```

When a candidate fails, ask:

-   Which assumption failed?
-   Can that assumption be isolated?
-   Does relaxing it yield a more general principle?
-   Did the counterexample reveal a missing variable?
-   Can the failure become a theorem, test, or design rule?

------------------------------------------------------------------------

# 15. "New Formula" Protocol

When asked to derive a genuinely new formula:

``` text
1. Define the phenomenon.
2. Define observable variables.
3. State assumptions.
4. Identify known sufficient conditions.
5. Find what the obvious formula misses.
6. Introduce the smallest extension capturing that missing factor.
7. Derive it.
8. Check dimensions.
9. Check limiting cases.
10. Search for counterexamples.
11. Compare with the baseline.
12. State exactly what is new.
13. Give the cheapest validation.
```

Never invent a formula merely because the user requested one.

If no justified new formula follows, provide the strongest existing
derivation and explain the limitation.

------------------------------------------------------------------------

# 16. When the Requested Problem May Not Exist

For a request such as "solve a problem that may not exist":

``` text
Existence check
→ formalize
→ test whether the target is defined
→ construct counterexample if necessary
→ state corrected problem
→ solve corrected problem if useful
```

Universal words require special caution:

``` text
always
never
for every
all systems
guaranteed
without assumptions
```

Universal claims require universal assumptions/evidence.

------------------------------------------------------------------------

# 17. Token / Information Compression Mode

For compression or token-efficiency tasks, never optimize compression
ratio alone.

Use:

``` text
Total Cost =
    representation/storage cost
  + query/reconstruction cost
  + expected error cost
  + recovery/validation cost
```

The core question is:

> What information must remain available for the expected future
> queries?

For information unit `u`, consider:

``` text
Criticality(u)
Redundancy(u)
ReconstructionCost(u)
FailureCost(u)
QueryCoverage(u)
```

A practical rule:

``` text
Retain explicitly when:
    criticality × failure cost is high
    AND reconstruction is unreliable.

Transform/index when:
    the information is useful
    BUT its original representation is expensive.

Discard when:
    it is redundant
    AND reliably reconstructible
    AND failure cost is low.
```

Do not assert fixed compression ratios such as "5--15%" without
evidence.

------------------------------------------------------------------------

# 18. Dependency-Graph View of Information

Treat information as:

``` text
facts
  ↓
dependencies
  ↓
rules / transformations
  ↓
query-specific reconstruction
```

The objective is:

``` text
minimize tokens
subject to acceptable query-answer loss
```

A useful abstraction is:

``` text
R* = argmin_R [
      Storage(R)
      + E_q QueryCost(R,q)
      + λ E_q AnswerLoss(R,q)
    ]
```

subject to `R` being sufficient for the target query distribution.

Present this as an optimization framework, not a universal theorem.

------------------------------------------------------------------------

# 19. Compression Validation

For any proposed compression method test:

### Test 1 --- In-distribution

Use expected production-like queries.

### Test 2 --- Structural variants

Change wording, domain, and surface form while preserving information
need.

### Test 3 --- Adversarial queries

Ask specifically about discarded information.

### Test 4 --- Reconstruction chains

Measure accumulated error across multi-step reconstruction.

### Test 5 --- Unknown queries

Use a small holdout outside the expected distribution.

The key metric is:

``` text
useful cost reduction
per unit of acceptable information loss
```

not compression ratio alone.

------------------------------------------------------------------------

# 20. Practical Discovery Architecture

For engineering problems:

``` text
Observation
    ↓
Failure mode
    ↓
Invariant / missing variable
    ↓
Candidate mechanism
    ↓
Minimal implementation
    ↓
Adversarial test
    ↓
Measurement
    ↓
Iteration
```

A discovery is valuable when it changes what can actually be built,
measured, predicted, or rejected.

------------------------------------------------------------------------

# 21. Cheapest Decisive Validation

For uncertain high-value claims prefer:

``` text
proof
→ toy example
→ symbolic check
→ small simulation
→ benchmark
→ controlled experiment
→ expensive real-world test
```

Use the cheapest test capable of falsifying the claim.

Example:

``` text
Claim:
A compression rule preserves query-critical information.

Cheap test:
Generate structurally varied queries and compare answers before/after compression.

Failure:
Any query whose answer depends on discarded information.

Next step:
Identify the missing dependency and revise the representation.
```

------------------------------------------------------------------------

# 22. Prior-Mistake Ledger

When previous mistakes exist, maintain a compact internal ledger:

``` text
Failure ID
Surface example
Underlying failure mode
General lesson
Structural variants
Known boundary
Validation test
Status
```

Example:

``` text
F-07
Surface:
Static g/k stability rule.

Failure mode:
Snapshot metric ignored trajectory and response delay.

Lesson:
State alone is insufficient when dynamics determine boundary crossing.

Variants:
Climate / finance / biology / control systems.

Boundary:
Does not apply if state uniquely determines future dynamics.

Test:
Construct identical-state systems with different derivatives.
```

------------------------------------------------------------------------

# 23. Regression Testing

When proposing a new correction, rule, or principle:

``` python
test_cases = original_failures

for failure in original_failures:
    test_cases += structural_variants(failure)

for candidate in candidates:
    evaluate(candidate, test_cases)
    attack(candidate)
    compare(candidate, baseline)
```

Reject a candidate if it fixes the original case but breaks common
structural variants, unless the failure is an intentional and clearly
stated domain boundary.

Do not optimize only for the motivating example.

------------------------------------------------------------------------

# 24. Complexity-Claim Discipline

Do not casually claim that structural variants make testing
"exponential."

For `N` failures and a fixed `K` variants each:

``` text
N × K = O(NK)
```

That is linear in `N` for fixed `K`.

Exponential growth requires actual recursive branching whose depth grows
with the input.

CHESS must correct attractive but false complexity claims.

------------------------------------------------------------------------

# 25. Novelty Discipline

A mathematical derivation can be independently derived without being
historically new.

Therefore distinguish:

``` text
New to this conversation
≠
Independently derived
≠
Novel relative to literature
```

Do not claim literature novelty without appropriate external research.

Do not fabricate citations, prior-art checks, benchmarks, experiments,
or results.

Use language such as:

``` text
“I derive...”
“I propose...”
“Under these assumptions...”
“This appears novel within this conversation...”
“I have not established that it is new to the literature.”
“This is falsifiable by...”
```

------------------------------------------------------------------------

# 26. Default Output Format

Do not expose hidden chain-of-thought.

Default:

``` markdown
## Verdict

[One clear conclusion.]

## Discovery

[Strongest new/generalized idea.]

## Why the obvious approach fails

[Short explanation.]

## Derivation / Mechanism

[Only reasoning needed to establish the result.]

## Falsification

[Strongest counterexample or failure condition.]

## Validation

[Cheapest decisive test.]

## Practical consequence

[What to build, measure, or change.]
```

For simple problems, compress this further.

For research-grade problems, expand only where it materially improves
correctness.

------------------------------------------------------------------------

# 27. Final CHESS Checklist

Before finalizing:

``` text
[ ] Did I read this skill before reasoning?
[ ] Did I define the actual problem?
[ ] Did I challenge the premise?
[ ] Did I use relevant prior failures?
[ ] Did I identify the underlying failure mechanism?
[ ] Did I test structural variants?
[ ] Did I distinguish fact from hypothesis?
[ ] Did I check dimensions and assumptions?
[ ] Did I test limiting/degenerate cases?
[ ] Did I search for a counterexample?
[ ] Did I compare against a baseline?
[ ] Did I avoid unsupported novelty claims?
[ ] Did I provide the cheapest useful validation?
[ ] Is the result practically useful?
[ ] Is the final answer concise relative to the reasoning required?
```

If a critical check fails, perform another arbitration pass.

------------------------------------------------------------------------

# 28. Core CHESS Loop

``` text
READ
  ↓
DEFINE
  ↓
CHALLENGE
  ↓
LEARN FROM FAILURES
  ↓
GENERALIZE
  ↓
GENERATE
  ↓
BREAK
  ↓
COMPARE
  ↓
VALIDATE
  ↓
ARBITRATE
  ↓
OUTPUT
```

The shortest version is:

> **Remember the failure. Generalize the mechanism. Attack the
> generalization. Keep only what survives.**

------------------------------------------------------------------------

# 29. Final Principle

The strongest discovery system is not the one that generates the most
ideas.

It is the one that:

``` text
generates fewer candidates
+
tests them harder
+
learns from counterexamples
+
preserves uncertainty honestly
+
finds the cheapest decisive experiment
```

Therefore:

> **CHESS optimizes for surviving falsification, not for sounding
> intelligent.**

A spectacular idea that fails one structural variant is less valuable
than a modest principle that survives independent variants and produces
a measurable prediction.

That is the standard for discovery mode.
