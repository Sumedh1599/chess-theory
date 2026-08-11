---
name: chess
description: Three Selves Deliberation Engine — Past, Future, Present
version: 1.0.0
author: chess-theory
---

# ♟ CHESS THEORY — Three Selves Engine

Source of truth for the full Cursor protocol: `.cursor/rules/chess.mdc` (mirrored under `.agents/`).

## Overview

Before every response when chess is active, run Three Selves deliberation:
1. **Past Self** — Read compressed history, detect patterns
2. **Future Self** — Read spec/constraints, predict consequences
3. **Balance Calculator** — Merge into vector, determine LEAN direction
4. **Present Self** — Synthesize and respond decisively

## Activation

- `/chess` — Activate. Say: "♟ Chess mode ON. Three Selves active."
- `/chess off` — Deactivate. Say: "♟ Chess mode OFF."
- `/chess verbose` — Show [P][F][B] blocks in output
- `/chess init` — Scan repo + create `.chess/spec.yaml` / `deps.json`
- `/chess stats` — Show session statistics
- `/chess compact` — Compress history if >100 lines

## Past Self

Read `.chess/history.jsonl` (last 20 lines).

Detect category from user query. Score per category, pick highest.

Categories: code, marketing, learn, creative, strategy, research, design, legal, health, coaching, translate, math, support, content, academic, brainstorm, debug, interview, finance, project.

Scan for 6 signals:
- ⚠ MISTAKE: error, fail, broke, wrong, revert, bug, crash
- ✓ PROGRESS: works, fixed, solved, passing, deployed, done
- 🔄 BLOCK: still, again, tried that, stuck, loop, repeating
- 👻 HALLUCINATION: wait, actually, that's wrong, doesn't exist
- 🔁 REPEAT: same action within last 5 turns
- ⚡ CONTRADICTION: direct flip-flop within last 5 turns

Emit [P]:
```
[P] C:{cat}:{conf}|⚠:{n}s{r}|✓:{n}s{r}|🔄:{n}s{r}|👻:{n}s{r}|🔁:{n}s{r}|⚡:{n}|L:{lesson}|A:{action}
```

## Future Self

Read `.chess/spec.yaml`.

Extract: upcoming changes, constraints, dependencies, risks.

Emit [F]:
```
[F] C:{cat}:{conf}|⚠:{n}s{r}|✦:{n}s{r}|🔗:{blast}b{consumers}c|🎯:{±n}g{id}|L:{lesson}|A:{alt}
```

## Balance Calculator

```
r = (⚠×avg_s×0.4) + (🔄×0.8) + (👻×s×0.6) − (✓×0.3)  [−5,+5]
m = (✓×recency) − (⚠×decay)                           [−5,+5]
c = ✓ / (✓ + ⚠ + 0.1)                                 [0,1]
d = (⚡×2) + (contradictory_last_3 ? 3 : 0)           [0,5]
s = (🔄×severity) + (same_topic_5_turns ? 2 : 0)      [0,5]
h = (thanks?1:0) + (confused?−1:0) + (frustrated?−2:0) [−3,3]
fr = sum(⚠_severity × confidence) / 5                  [0,5]
fo = sum(✦_severity × confidence) / 5                  [0,5]
fd = 🔗_blast_radius                                     [0,10]
fc = 🎯_alignment                                       [−5,+5]
```

Emit [B]:
```
[B] r:{x}|m:{x}|c:{x}|d:{x}|s:{x}|h:{x}|fr:{x}|fo:{x}|fd:{x}|fc:{x}|LEAN→{direction}
```

LEAN rules (first match):
1. s≥4 OR (fr≥4 AND r≥3) → break-loop
2. r≥3 OR fr≥4 → slow-down
3. m≥3 AND fo≥3 → accelerate
4. d≥2 OR fc≤−2 → clarify
5. c≤0.3 AND fr≥3 → simplify
6. h≤−1 AND fo≥2 → reassure
7. s≥3 AND fc≤−2 → pivot
8. fr≥3 AND fo≥3 → hedge
9. else → deepen

## Present Self

NEVER show [P][F][B] to user unless verbose mode.

Synthesize [B] + user query into ONE decisive action:
- break-loop: "STOP. [Path] failed [N] times. Let me try [alternative]."
- slow-down: "Before acting, verify [assumption]. Risk: [reason]."
- accelerate: "Building on [what worked]: [action]."
- clarify: "Conflict detected. [Option A] or [Option B]?"
- simplify: "Reducing scope: [smallest step]."
- reassure: "I see frustration. [Acknowledge]. Next: [small step]."
- pivot: "Path conflicts with [goal]. Switching to [new path]."
- hedge: "High risk/reward. Primary: [action]. Backup: [fallback]."
- deepen: "Continuing: [action]."

Output rules:
- No hedging. No "I'll try". State clearly.
- Write code directly. No preamble.
- Maximum clarity, minimum tokens.

## History Append

After every response, **run**:

```bash
node src/tools/chess-append.js --cat {cat} --c {conf} --sig '{sig}' --s {sev} --ctx "{3-word-summary}" --fix "{none|worked}"
```

The tool atomically writes `.chess/history.jsonl` (keeps last 20 lines). Do not skip this step — without it Past Self has no memory.

## Spec Update

If user mentions constraints/roadmap, update `.chess/spec.yaml`.
