#!/bin/bash
set -e

REPO_URL="https://github.com/Sumedh1599/chess-theory"
INSTALL_DIR="$HOME/.chess-theory"

echo "♟ CHESS THEORY — Installer"
echo ""

if [ -f "cli/install.js" ]; then
    SOURCE_DIR="$(pwd)"
    echo "📁 Installing from local directory: $SOURCE_DIR"
else
    echo "📥 Downloading Chess Theory..."
    if [ -d "$INSTALL_DIR" ]; then
        rm -rf "$INSTALL_DIR"
    fi
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR" 2>/dev/null || {
        echo "⚠️  Git clone failed. Downloading ZIP instead..."
        curl -fsSL "$REPO_URL/archive/refs/heads/main.zip" -o /tmp/chess-theory.zip
        unzip -q /tmp/chess-theory.zip -d /tmp/
        mv /tmp/chess-theory-main "$INSTALL_DIR"
    }
    SOURCE_DIR="$INSTALL_DIR"
fi

cd "$SOURCE_DIR"

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install from https://nodejs.org"
    exit 1
fi

node cli/install.js

echo ""
echo "🎉 Done! Type '/chess' in your agent to activate."
