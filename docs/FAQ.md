# FAQ

**Q: Does Chess Theory need my API key?**  
A: No. Your agent runs the protocol locally. Nothing is sent to a Chess Theory server.

**Q: Will this slow my agent down?**  
A: Negligibly. Past/Future reads are small (~100 tokens of structure). Often cheaper than re-reading a long chat.

**Q: Can I use Chess with Caveman?**  
A: Yes. Chess = deliberation; Caveman = output compression. They stack.

**Q: Where is memory stored?**  
A: Per project in `.chess/history.jsonl`. Spec/constraints in `.chess/spec.yaml`.

**Q: Why don’t I see `[P][F][B]`?**  
A: By design. Type `/chess verbose` to show them.

**Q: How do I reset history?**  
A: Truncate or delete `.chess/history.jsonl`. Prefer `/chess compact` when you only need a summary.

**Q: Node version?**  
A: ≥18 (`engines` in `package.json`).

**Q: Install didn’t activate Chess.**  
A: Confirm the rule file exists (`~/.cursor/rules/chess.mdc`), restart the agent, then type `/chess`.

**Q: Does uninstall delete my project `.chess/`?**  
A: No. Only installed global rule/skill/hook files (and optionally `~/.chess-theory`). Delete `.chess/` yourself if needed.

More install help: [INSTALL.md](../INSTALL.md). Architecture: [ARCHITECTURE.md](./ARCHITECTURE.md).
