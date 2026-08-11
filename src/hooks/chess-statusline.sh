#!/bin/bash
# Chess Theory — Status Line

FLAG_FILE="$HOME/.chess-active"
HISTORY_FILE=".chess/history.jsonl"

if [ -f "$FLAG_FILE" ]; then
    TURNS=0
    if [ -f "$HISTORY_FILE" ]; then
        TURNS=$(wc -l < "$HISTORY_FILE" | tr -d ' ')
    fi
    echo "[CHESS] ♟ $TURNS turns"
else
    echo "[CHESS] ○ off"
fi
