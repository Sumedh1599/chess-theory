#!/usr/bin/env bash
set -e

echo "♟ CHESS THEORY — Uninstaller"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/cli/uninstall.js" ]; then
  SOURCE_DIR="$SCRIPT_DIR"
elif [ -f "$HOME/.chess-theory/cli/uninstall.js" ]; then
  SOURCE_DIR="$HOME/.chess-theory"
elif [ -f "cli/uninstall.js" ]; then
  SOURCE_DIR="$(pwd)"
else
  echo "📁 Fallback: removing known rule/skill paths..."
  rm -f "$HOME/.cursor/rules/chess.mdc"
  rm -f "$HOME/.windsurf/rules/chess.mdc"
  rm -f "$HOME/.cline/rules/chess.mdc"
  rm -f "$HOME/.github/copilot/rules/chess.mdc"
  rm -f "$HOME/.claude/skills/chess.md"
  for f in chess-past-cache.js chess-future-read.js chess-balance.js chess-activate.js chess-statusline.sh; do
    rm -f "$HOME/.claude/hooks/$f"
  done
  if [ "${1:-}" != "--keep-cache" ]; then
    rm -rf "$HOME/.chess-theory"
  fi
  echo "✅ Done (fallback cleanup)."
  exit 0
fi

if ! command -v node &>/dev/null; then
  echo "❌ Node.js not found. Install from https://nodejs.org"
  exit 1
fi

node "$SOURCE_DIR/cli/uninstall.js" "$@"

echo ""
echo "🎉 Uninstall finished."
