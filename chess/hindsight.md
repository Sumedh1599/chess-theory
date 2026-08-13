# Hindsight Self — Compression Protocol

## Purpose
Generate `H(t)`: a compressed, content-rich summary of prior interaction that
improves task performance when reinjected into working context.

## Input
- Full session history (all prior turns)
- Current turn index `t`
- Target compression ratio: ~70% token reduction

## Output Format

```
H(t) = {
  "turns_summarized": <count>,
  "compression_ratio": <tokens_in / tokens_out>,
  "lessons": [
    {"turn": <n>, "action": "...", "outcome": "✅|❌|⚠️|❓", "lesson": "..."},
    ...
  ],
  "recency_bias": <0.0-1.0>,
  "stale_warnings": ["..."],
  "injected": true
}
```

## Compression Rules

1. **Causal links only**: Keep "X caused Y", drop "X happened then Y happened" without mechanism
2. **Outcome tagging**: Every lesson must have an outcome tag
   - ✅ success — repeat if conditions match
   - ❌ failure — avoid unless position changed significantly
   - ⚠️ partial — context-dependent, flag for re-evaluation
   - ❓ unknown — insufficient data, do not weight heavily
3. **Recency weighting**: Last turn gets 2× weight in summary; turns older than `t-5` compressed to single line each
4. **Noise rejection**: Drop pleasantries, off-topic digressions, failed tool calls that were retried successfully
5. **Stale detection**: If a lesson references a file that no longer exists, a variable that was renamed, or a requirement that was changed, tag it `[STALE]` and move to `stale_warnings`

## Ablation Reference

| Condition | Expected Accuracy | When to Use |
|-----------|------------------|-------------|
| Full hindsight (all turns) | Highest | Default |
| Last-turn-only | ~same as full for 2/3 models | When context budget is tight |
| Noise (length-matched random) | Much lower | Never — proves content matters |

## Injection Point
Insert `H(t)` immediately after system prompt and before user message.
Mark with `[HINDSIGHT SIGNAL]` so Present Self recognizes it.
