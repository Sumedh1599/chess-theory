# Platform Support Matrix

Chess Theory installs via agent-specific rule/skill directories. **Node.js ≥18** required.

| Agent | Version | Install path | Activation | Status | Notes |
|-------|---------|--------------|------------|--------|-------|
| Cursor | 0.40+ | `~/.cursor/rules/chess.mdc` | `/chess` | ✅ Supported | Rules auto-apply when `alwaysApply: true` |
| Claude Code | 2.0+ | `~/.claude/skills/chess.md` + `~/.claude/hooks/*` | `/chess` | ✅ Supported | Hooks emit [P]/[F]/[B]; append via `chess-append.js` |
| Windsurf | 1.0+ | `~/.windsurf/rules/chess.mdc` | `/chess` | ✅ Supported | Same ruleset as Cursor (`.agents/windsurf.mdc`) |
| Cline | 3.0+ | `~/.cline/rules/chess.mdc` | `/chess` | ✅ Supported | Same ruleset (`.agents/cline.mdc`) |
| GitHub Copilot Chat | 1.50+ | `~/.github/copilot/rules/chess.mdc` | `@chess` / `/chess` | ✅ Supported | Same ruleset (`.agents/copilot.mdc`) |
| Gemini CLI | 1.0+ | Extension / skill install | `/chess` | ⚠️ Best-effort | Not covered by `cli/install.js` auto-detect yet |
| Codex / others | — | Universal installer / manual copy | `/chess` | ⚠️ Best-effort | Copy `.cursor/rules/chess.mdc` into agent rules dir |

## Runtime verification (this repo)

Automated checks in `tests/platforms.test.js`:
- Core `chess.mdc` present with `alwaysApply: true` + append instructions
- `.agents/{cursor,windsurf,cline,copilot}.mdc` present
- `skills/chess/SKILL.md` present
- Installer/uninstaller reference major agents

Manual smoke (per machine):

```bash
node cli/install.js --dry-run   # preview
node cli/install.js             # install
# Restart agent, then:
# /chess
# /chess verbose
node src/tools/chess-append.js --cat code --sig '✓' --s 2 --ctx "smoke ok" --fix none
node src/hooks/chess-past-cache.js
```

## CI Node / OS matrix

`.github/workflows/test.yml` runs on:

| Node | Ubuntu | macOS | Windows |
|------|--------|-------|---------|
| 18 | ✅ | ✅ | ✅ |
| 20 | ✅ | ✅ | ✅ |
| 22 | ✅ | ✅ | ✅ |

## Install entrypoints

| OS | Command |
|----|---------|
| macOS / Linux / WSL | `curl -fsSL …/install.sh \| bash` |
| Windows PowerShell | `irm …/install.ps1 \| iex` |
| Local clone | `node cli/install.js` |
| Dry-run | `node cli/install.js --dry-run` |

## Uninstall

```bash
./uninstall.sh
# Windows:
./uninstall.ps1
# or
node cli/uninstall.js
```

`--keep-cache` leaves `~/.chess-theory`. Project `.chess/` history is **not** deleted by default.

## Protocol fidelity

Chess Theory is a **deliberation protocol** enforced by agent rules. Memory requires the agent (or hooks) to run:

```bash
node src/tools/chess-append.js --cat … --sig … --s … --ctx "…" --fix …
```

after each turn. Without append, Past Self has nothing to learn from.
