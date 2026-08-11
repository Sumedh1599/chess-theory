# AGENTS.md — Chess Theory

Brief agent-facing summary. Full protocol: `.cursor/rules/chess.mdc`.

## What this repo is

**Chess Theory** is a deliberation layer for AI coding agents. When active (`/chess`), before every response:

1. **Past Self** — read `.chess/history.jsonl` (last 20 lines) → emit `[P]`
2. **Future Self** — read `.chess/spec.yaml` → emit `[F]`
3. **Balance** — merge → emit `[B]` with `LEAN→{direction}`
4. **Present Self** — one decisive action; do **not** show `[P][F][B]` unless `/chess verbose`

## Commands

| Command | Effect |
|---------|--------|
| `/chess` | ON — "♟ Chess mode ON. Three Selves active." |
| `/chess off` | OFF |
| `/chess verbose` | Show `[P][F][B]` |
| `/chess init` | Run `src/tools/chess-init.js` |
| `/chess stats` | Session stats |
| `/chess compact` | Compress long history |

## Key paths

- Rules: `.cursor/rules/chess.mdc` (also `.agents/*.mdc`)
- Skill: `skills/chess/SKILL.md`
- Hooks: `src/hooks/chess-*.js`
- Init: `src/tools/chess-init.js`
- Install: `cli/install.js` / Uninstall: `cli/uninstall.js`

## After each response

Append one JSON line to `.chess/history.jsonl` (see chess.mdc STEP 5).
