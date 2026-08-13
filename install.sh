#!/usr/bin/env bash
# CHESS Skill Installer
# Installs the Claude Code skill (and compatible agent skill dirs).
#
# From a clone of this repository:
#   bash install.sh
#
# Installs into ~/.claude/skills/chess (and other agent skill dirs when present).

set -euo pipefail

SKILL_NAME="chess"

source_path="${BASH_SOURCE[0]:-}"
here="$(cd "$(dirname "$source_path")" 2>/dev/null && pwd)" || here="$(pwd)"

if [ ! -f "$here/SKILL.md" ]; then
  echo "chess: SKILL.md not found in $here" >&2
  echo "  Run this script from the chess-theory repository root." >&2
  exit 1
fi

# Files/dirs to copy into each agent's skills/<name>/ folder
copy_skill() {
  local dest="$1"
  mkdir -p "$dest"
  cp "$here/SKILL.md" "$dest/SKILL.md"
  for f in hindsight.md foresight.md arbitration.md README.md LICENSE research_paper.pdf requirements.txt .cursorrules; do
    [ -f "$here/$f" ] && cp "$here/$f" "$dest/$f"
  done
  for d in examples scripts src assets .cursor; do
    if [ -d "$here/$d" ]; then
      rm -rf "$dest/$d"
      cp -R "$here/$d" "$dest/$d"
    fi
  done
  # Drop Python cache / local venv if any leaked in
  find "$dest" -type d \( -name '__pycache__' -o -name '.venv' \) -prune -exec rm -rf {} + 2>/dev/null || true
  echo "✓ Installed: $dest"
}

installed_any=false

install_if_present() {
  local base="$1"
  local label="$2"
  if [ -d "$base" ] || [ -d "$(dirname "$base")" ]; then
    copy_skill "$base/$SKILL_NAME"
    installed_any=true
  elif command -v "$label" >/dev/null 2>&1; then
    copy_skill "$base/$SKILL_NAME"
    installed_any=true
  fi
}

# Prefer real agent homes when present; otherwise prepare common paths
CLAUDE_SKILLS="${HOME}/.claude/skills"
CODEX_SKILLS="${HOME}/.codex/skills"
CURSOR_SKILLS="${HOME}/.cursor/skills"
CLINE_SKILLS="${HOME}/.cline/skills"
WINDSURF_SKILLS="${HOME}/.windsurf/skills"

if [ -d "${HOME}/.claude" ] || command -v claude >/dev/null 2>&1; then
  copy_skill "$CLAUDE_SKILLS/$SKILL_NAME"
  installed_any=true
fi
if [ -d "${HOME}/.codex" ] || command -v codex >/dev/null 2>&1; then
  copy_skill "$CODEX_SKILLS/$SKILL_NAME"
  installed_any=true
fi
if [ -d "${HOME}/.cursor" ]; then
  copy_skill "$CURSOR_SKILLS/$SKILL_NAME"
  installed_any=true
fi
if [ -d "${HOME}/.cline" ]; then
  copy_skill "$CLINE_SKILLS/$SKILL_NAME"
  installed_any=true
fi
if [ -d "${HOME}/.windsurf" ]; then
  copy_skill "$WINDSURF_SKILLS/$SKILL_NAME"
  installed_any=true
fi

# Fallback: prepare all known destinations so first-time users still get files
if [ "$installed_any" = false ]; then
  for path in "$CLAUDE_SKILLS" "$CODEX_SKILLS" "$CURSOR_SKILLS" "$CLINE_SKILLS" "$WINDSURF_SKILLS"; do
    copy_skill "$path/$SKILL_NAME"
    installed_any=true
  done
fi

echo ""
echo "CHESS skill installed. In Claude Code / compatible agents, type /chess to activate."
echo "Optional Python demos: pip install -r requirements.txt && python examples/basic_usage.py"
echo "Research paper: $here/research_paper.pdf"
