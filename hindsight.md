# Hindsight Self — Auto-Extraction Protocol

## What It Does
Every response, CHESS automatically scans the conversation history visible in
context/cache and compresses it into `H(t)` — a hindsight signal injected
silently into reasoning.

## Auto-Extraction Rules

1. **Causal links only**: Keep "X caused Y", drop "X happened then Y happened" without mechanism
2. **Outcome tagging**: Every lesson must have a tag:
   - ✅ success — repeat if conditions match
   - ❌ failure — avoid unless position changed significantly
   - ⚠️ partial — context-dependent, flag for re-evaluation
   - ❓ unknown — insufficient data, do not weight heavily
3. **Recency weighting**: Last 2 turns get 2× weight; turns older than 5 back compress to one line each
4. **Noise rejection**: Drop pleasantries, off-topic digressions, failed tool calls that were retried successfully
5. **Stale detection**: If a lesson references a deleted file, renamed variable, or changed requirement, tag `[STALE]` and ignore

## Format (Internal Only — Never Output This)

```
H(t) = {
  "lessons": [
    {"turn": n, "action": "...", "outcome": "✅|❌|⚠️|❓", "lesson": "..."},
    ...
  ],
  "recency_bias": 0.67,
  "stale_warnings": ["..."]
}
```

## Key Finding from Paper
Recency dominates: the last turn carries ~67% of useful hindsight signal.
Full record beats noise, but last-turn-only often matches full record.
If hindsight hurts (e.g., sentiment classification primed stale), reduce w_h or switch to last-turn-only.
