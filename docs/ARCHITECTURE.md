# Architecture — Three Selves

Chess Theory is a deliberation layer. Before each agent response (when `/chess` is on), three voices run and compress into single-line blocks.

## Pipeline

```
User prompt
    │
    ├─► Past Self     (.chess/history.jsonl)  → [P]
    ├─► Future Self   (.chess/spec.yaml)      → [F]
    └─► Balance       merge [P]+[F]           → [B] LEAN→direction
                              │
                              ▼
                     Present Self (one decisive reply)
                              │
                              ▼
                     Append history.jsonl line
```

## Blocks

### Past `[P]`

```
[P] C:{cat}:{conf}|⚠:{n}s{r}|✓:{n}s{r}|🔄:{n}s{r}|👻:{n}s{r}|🔁:{n}s{r}|⚡:{n}|L:{lesson}|A:{action}
```

History is capped at the last 20 lines. Signals are counted from stored `sig` fields.

### Future `[F]`

```
[F] C:{cat}:{conf}|⚠:{n}s{r}|✦:{n}s{r}|🔗:{blast}b{consumers}c|🎯:{±n}g{id}|L:{lesson}|A:{alt}
```

Derived from `.chess/spec.yaml` upcoming changes, consumers, constraints, and risks.

### Balance `[B]`

```
[B] r:{x}|m:{x}|c:{x}|d:{x}|s:{x}|h:{x}|fr:{x}|fo:{x}|fd:{x}|fc:{x}|LEAN→{direction}
```

Metric formulas (reference):

| Metric | Formula (compressed) | Range |
|--------|----------------------|-------|
| r risk | `(⚠×sev×0.4)+(🔄×0.8)+(👻×sev×0.6)−(✓×0.3)` | −5…+5 |
| m momentum | `(✓×recency)−(⚠×decay)` | −5…+5 |
| c confidence | `✓/(✓+⚠+0.1)` | 0…1 |
| d drift | `(⚡×2)+contradiction_bonus` | 0…5 |
| s stuck | `(🔄×sev)+same_topic_bonus` | 0…5 |
| fr / fo | predicted risk/opportunity severity×conf / 5 | 0…5 |
| fd | blast radius | 0…10 |
| fc | goal alignment | −5…+5 |

LEAN is first-match: break-loop → slow-down → accelerate → clarify → simplify → reassure → pivot → hedge → deepen.

## Runtime pieces

| Piece | Role |
|-------|------|
| `.cursor/rules/chess.mdc` | Source-of-truth protocol for Cursor |
| `skills/chess/SKILL.md` | Claude Code skill form of the same protocol |
| `src/hooks/chess-*.js` | Machine emitters for [P]/[F]/[B] |
| `src/tools/chess-init.js` | Scans repo → `spec.yaml` + `deps.json` |
| `cli/install.js` | Detects agents and installs rules/skills |

## Design constraints

- Do not show `[P][F][B]` unless `/chess verbose`.
- One decisive Present action — no hedging language.
- Per-project memory only (`.chess/` in the repo cwd).
- History append is mandatory after each response when chess is active.
