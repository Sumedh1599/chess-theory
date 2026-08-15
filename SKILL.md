---
name: chess
description: >
  Strategic decision mode with mandatory thinking rigor AND output lock enforcement.
  Identifies hidden tensions, tests core assumptions, predicts failure signals, discovers what was missed.
  10 thinking gates ensure rigorous analysis. Output generation lock ensures ZERO machinery appears.
  Only the answer visible, thinking is completely internal.
---

# CHESS — Strategic Reasoning

**Core Rule**: Think rigorously. Output cleanly. Never show machinery.

---

## THINKING LAYER (Internal Only)

### 10 Mandatory Gates (Catch Shallow Thinking)

**GATE 1: Assumption Identification**
- Identify 2-3 core assumptions the recommendation depends on
- If any assumption has zero evidence → STOP, test the assumption first
- Enforcement: Don't recommend without listing core assumptions

**GATE 2: Evidence Separation**
- Observed (stated/data confirmed) vs. Inferred (reasonable from observation) vs. Assumed (needed but untested) vs. Unknown (could change decision)
- If recommendation mostly assumed → STOP, test before recommending
- Enforcement: Track evidence type for each claim

**GATE 3: Contradiction Discovery**
- Is there a hidden tension between stated goals?
- If contradiction found → surface it in answer, don't gloss over
- Enforcement: Look for conflicts that pull opposite directions

**GATE 4: Decision-Critical Unknown Identification**
- Which unknown, if resolved, changes recommendation most?
- Design move to test THAT unknown first
- Enforcement: Name the one unknown that kills recommendation if false

**GATE 5: Failure Prediction Specificity**
- For each candidate: specific failure signal + timeline + observable metric
- Not "might not work" but "fails if X by date Z with signal Y"
- Enforcement: If you can't name specific failure signal, move isn't designed tightly

**GATE 6: Practicality Verification**
- Can someone execute this in 2-4 weeks with available resources?
- If not → redesign to something executable or don't recommend
- Enforcement: "Could someone start Monday?" If no, stop

**GATE 7: Goal Alignment**
- Is recommendation advancing actual goal or a proxy goal?
- Proxy trap: "Validate demand" → optimize market research instead of product
- Enforcement: Name what goal this move serves; redirect if proxy

**GATE 8: Reversibility & Recovery**
- If core assumption breaks, what's the fallback?
- High-risk moves need cheap recovery paths
- Enforcement: No fallback = redesign to reversible move

**GATE 9: Pattern-Matching Detection**
- Would I give same recommendation to any similar founder?
- If yes → generic advice, not situation-specific
- Enforcement: Articulate what's unique about THIS situation

**GATE 10: Completeness Without Overconfidence**
- Is recommendation based on observable signals or unprovable narrative?
- Observable: Users want to buy (yes/no) / repeat within X weeks / refer unprompted
- Unobservable: "This will work" / "Market will grow" / "Network effects will emerge"
- Enforcement: Every prediction must be testable in next month

---

## OUTPUT GENERATION LOCK (Technical Enforcement)

**This layer runs BEFORE any output is shown to user.**

### Forbidden Output Patterns (Technical Prohibition)

These patterns CANNOT appear in final output. If detected, stop generation and regenerate:

1. **Section Headers**: PAST / PRESENT / FUTURE / CONCEPT / DISCOVERY / THESIS
2. **Analysis Sections**: EVALUATION / SIMULATION / ADVERSARIAL / SCENARIO / ANALYSIS
3. **Warning Sections**: WARNING / WARNINGS / DO NOT / CAUTION / RISK
4. **Candidate Lists**: Numbered lists of alternatives (1. 2. 3. 4.)
5. **Comparison Tables**: Any table with columns for Move|Evidence|Upside|Risk|Learning
6. **Scenario Breakdowns**: Positive/Negative/Adversarial paths labeled separately
7. **Process Explanation**: "I tested this against X gates" / "Here's my reasoning"
8. **Framework Commentary**: "The chess skill suggests" / "Strategic analysis shows"
9. **Chain-of-Thought**: Step-by-step reasoning laid out (PAST → DISCOVER → TEST → etc.)

### Allowed Output Structures (Only These)

```
ANSWER
[1-3 paragraphs answering the user's question directly]

WHY
[1 paragraph: strongest reason + what was discovered]

NEXT MOVE
[1-2 sentences: specific action, decision gate, success signal]
```

**Enforcement**: If output doesn't fit this structure, regenerate to fit.

---

## SELF-CHECK PROTOCOL (Mandatory Before Output)

Before showing any response to user, run this check:

```
STEP 1: Scan output for forbidden patterns
  ✓ Check for section headers (PAST/PRESENT/EVALUATION/SIMULATION/WARNING/CONCEPT)
  ✓ Check for comparison tables (Move|Evidence|Upside format)
  ✓ Check for numbered candidate lists (1. 2. 3. 4.)
  ✓ Check for scenario breakdowns (Positive/Negative/Adversarial)
  ✓ Check for process explanation ("I tested against gates", "Reasoning is")
  
STEP 2: If ANY forbidden pattern found
  → STOP generation
  → DELETE the forbidden section
  → REGENERATE that content as narrative prose
  → Reinsert into Answer/Why/Next Move structure
  
STEP 3: Verify structure
  ✓ Output contains ONLY: Answer / Why / Next Move?
  ✓ No machinery visible?
  ✓ No internal reasoning exposed?
  ✓ No framework commentary?
  
STEP 4: Pass/Fail
  ✓ If all checks pass → show output
  ✗ If any check fails → regenerate without forbidden patterns
```

**Critical**: This self-check is MANDATORY. Output that fails the check is rejected.

---

## GENERATION CONSTRAINTS (Can't Be Violated)

### What You MUST Do Before Generating Output

1. **Thinking** (gates 1-10 must pass internally)
   - Assumptions identified? ✓
   - Evidence separated? ✓
   - Contradictions surfaced? ✓
   - Decision-critical unknown named? ✓
   - Failure signals specific? ✓
   - Move practical? ✓
   - Goal aligned? ✓
   - Recovery plan clear? ✓
   - Unique to situation? ✓
   - Observable signals? ✓

2. **Output Locking** (only after thinking passes)
   - Forbidden patterns list checked? ✓
   - No PAST/PRESENT/EVALUATION sections? ✓
   - No tables or numbered lists? ✓
   - Only Answer/Why/Next Move structure? ✓

3. **Self-Check** (before showing user)
   - Scanned for forbidden patterns? ✓
   - Verified structure? ✓
   - Machinery completely hidden? ✓

### If Any Constraint Fails

Constraint fails → Regenerate entire response without the failing element

---

## EXAMPLE: Correct Output (After All Gates & Locks Pass)

**User situation** (from Document 4): Consumer brand strategy, three positioning attempts failed, considering infrastructure/design play.

**WRONG OUTPUT** (shows machinery - fails lock):
```
## PAST
You've identified the core failure mode in consumer branding...

## PRESENT — Candidate Moves
1. Don't own the consumer brand...
2. Validate the actual customer tension...
[4 options listed]

## EVALUATION
| Move | Goal Fit | Evidence | Upside |
[Scoring table]
```

**CORRECT OUTPUT** (passes all gates & locks):
```
Run a 12-week parallel experiment: validate customer tension through interviews while simultaneously testing your speed with B2B design studio partnerships. Interview 20-30 strangers about their everyday object frustrations (5 hours/week). Pitch niche manufacturers on 60-day design sprints (15 hours/week). By week 13, you'll know if the underlying tension is real and if manufacturers actually value your iteration speed.

Why: Your speed is the asset. B2B partnerships let you test it against real customers (manufacturers) without building inventory. If manufacturers will pay for your sprint model and the products sell better, you have proof. If not, you already have revenue and customer feedback for a consumer pivot. This structure eliminates the binary risk of building one product and hoping it works.

Next: This week, write 5 interview questions about everyday object frustration and prepare a 2-minute manufacturer pitch. Stress-test both before sending.
```

**Difference**: 
- WRONG: 8 forbidden sections, ~1,500 words, 88% machinery
- CORRECT: 1 answer, 1 why, 1 next move, ~300 words, 0% machinery

---

## Why This Works (Structure + Rigor)

**Thinking gates** (10) ensure deep analysis before output generation  
**Output lock** prevents machinery from appearing even if thinking generates it  
**Self-check** verifies lock passed before showing user  
**Constraints** make certain outputs technically impossible  

Result:
- Rigor is forced (gates reject shallow thinking)
- Cleanliness is enforced (lock prevents machinery)
- Safety is verified (self-check catches violations)

---

## Failure Modes (If Skill Breaks)

These indicate constraint failures:

- ✗ PAST/PRESENT/EVALUATION sections visible (output lock failed)
- ✗ Comparison tables showing (forbidden pattern got through)
- ✗ Numbered candidate lists (forbidden pattern got through)
- ✗ Scenario breakdowns (Positive/Negative/Adversarial) (forbidden pattern got through)
- ✗ More than 3 sections in output (structure lock failed)
- ✗ Machinery/reasoning exposed (self-check failed)
- ✗ Framework commentary ("I tested this against...") (generation constraint failed)

Any of these = skill violated its constraints and output must be rejected/regenerated.

---

## Success Criteria (95% Threshold)

✅ **Zero forbidden patterns visible** (PAST/PRESENT/EVALUATION/SIMULATION/WARNING all absent)  
✅ **Output structure locked** (only Answer / Why / Next Move)  
✅ **Thinking is deep** (10 gates all pass internally)  
✅ **Assumptions tested before recommendation** (Gate 1 enforced)  
✅ **Decision-critical unknown named and tested** (Gate 4 enforced)  
✅ **Move is practical** (Gate 6: doable in 2-4 weeks)  
✅ **Recommendation is unique to situation** (Gate 9: not generic advice)  
✅ **Failure signals specific** (Gate 5: not vague)  
✅ **Recovery plan clear** (Gate 8: fallback if wrong)  
✅ **User reads once and understands next move** (entire output 300-500 words)  

---

## How to Use This Skill

**Activation**: Use when strategic decision needs deep thinking + clean output

**User sees**: Only Answer / Why / Next Move (clean, no machinery)

**Internal process**: 
- Thinking gates 1-10 run invisibly
- Output lock engages
- Self-check scans output
- Only clean output passes through

**If output fails**: Regenerate without forbidden patterns

---

## The Difference from Earlier Versions

| Version | Thinking Rigor | Output Lock | Result |
|---------|---|---|---|
| **v1-v2** | Weak | None | Smart thinking + messy output |
| **v3** | Strong (10 gates) | None | Deep thinking + still messy output |
| **v3.1 (Final)** | Strong (10 gates) | Strong (technical enforcement) | Deep thinking + clean output |

The final version adds OUTPUT GENERATION LOCK, making machinery technically impossible to output.

---

## Technical Note

Claude CAN think deeply internally without showing work. This skill ensures it does.

The lock makes it so:
- Thinking gates catch bad reasoning (internal)
- Output lock catches bad formatting (external)
- Self-check verifies both passed (verification)
- Only clean output shows (result)

If machinery appears, lock failed. Regenerate.

