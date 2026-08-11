# Chess Theory — Installation Guide

## Quick Start (All Platforms)

```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/install.sh | bash

# Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/install.ps1 | iex
```

~60 seconds. Needs Node.js ≥18. Safe to re-run.

**Activate:** Type `/chess` in your agent.

---

## Manual Platform-Specific Install

### Claude Code

```bash
# Option 1: Auto-install (uses install.js)
npm install -g chess-theory
chess-init

# Option 2: Manual
curl -fsSL https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/install.sh | bash

# Then in Claude Code:
/chess
```

### Cursor

```bash
# 1. Download rules
mkdir -p ~/.cursor/rules
curl -o ~/.cursor/rules/chess.mdc https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/.cursor/rules/chess.mdc

# 2. In Cursor, type:
/chess
```

### Windsurf / Cline / Copilot

Same as Cursor, but replace `~/.cursor/rules` with:
- Windsurf: `~/.windsurf/rules`
- Cline: `~/.cline/rules`
- Copilot: `~/.github/copilot/rules`

### Gemini CLI

```bash
gemini extensions install https://github.com/Sumedh1599/chess-theory
/chess
```

---

## Uninstall

```bash
# Auto-uninstall
curl -fsSL https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/uninstall.sh | bash

# Manual (Cursor example)
rm ~/.cursor/rules/chess.mdc
rm -rf .chess/ # (if in a project repo)
```

---

## Troubleshooting

### "Node not found"

Install Node.js ≥18 from https://nodejs.org

### "curl: command not found" (Windows Git Bash)

Use PowerShell instead:
```powershell
irm https://raw.githubusercontent.com/Sumedh1599/chess-theory/main/install.ps1 | iex
```

### "EACCES: permission denied"

On macOS/Linux, you may need sudo:
```bash
sudo bash install.sh
```

Or install to user directory:
```bash
npm install --prefix ~/.local chess-theory
export PATH=~/.local/bin:$PATH
```

### Chess not activating

1. Confirm the ruleset file was installed: `cat ~/.cursor/rules/chess.mdc | head`
2. Restart the agent (close and reopen Cursor/Claude Code)
3. Type `/chess` (capitalization doesn't matter)
4. If still broken, check `~/.chess-theory/settings.json` exists

---

## What Gets Installed

- **Rule files** → agent-specific directories (`.cursor/rules`, `.claude/skills`, etc.)
- **Config** → `~/.chess-theory/settings.json`
- **Per-project** → `.chess/` dir created on first `/chess init`

All paths are **standard conventions**. Nothing hidden or invasive.

---

## First Run Checklist

1. Install via one-liner
2. Open Cursor / Claude Code / etc.
3. Type: `/chess`
4. You should see: "♟ Chess mode ON. Three Selves active."
5. Ask a code question that you've failed at before
6. Check `.chess/history.jsonl` exists
7. Type: `/chess verbose` to see [P][F][B] blocks
8. Type: `/chess off` to disable

---

## Feedback

Issues or weird behavior? Open a GitHub issue: https://github.com/Sumedh1599/chess-theory/issues
