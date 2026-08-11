# Contributing to Chess Theory

Thanks for helping improve the Three Selves deliberation engine.

## Workflow

1. **Fork** the repository on GitHub.
2. **Clone** your fork and create a branch:
   ```bash
   git checkout -b fix/short-description
   ```
3. **Install** locally (optional):
   ```bash
   node cli/install.js
   ```
4. **Make changes** — prefer small, focused PRs.
5. **Add or update tests** under `tests/` when you change hooks or balance logic.
6. **Run tests**:
   ```bash
   npm test
   ```
7. **Open a PR** with:
   - What changed and why
   - How you tested it
   - Note if `.cursor/rules/chess.mdc` changed (also sync `skills/chess/SKILL.md` and `.agents/*.mdc`)

## Rules of the road

- Core protocol lives in `.cursor/rules/chess.mdc` — treat it as the source of truth.
- After editing the ruleset, update `skills/chess/SKILL.md` and copies under `.agents/`.
- Do not invent unrelated features; keep changes aligned with Past / Future / Present deliberation.
- Keep install scripts small and multi-platform friendly.
- Never commit secrets, API keys, or personal `.chess/history.jsonl` dumps.

## Code style

- Node.js ≥18, CommonJS for hooks/CLI (`require`).
- Prefer clear, minimal code over abstractions.
- Tests use Node's built-in test runner: `node --test`.

## Reporting bugs

Open an issue with:

- Agent (Cursor, Claude Code, etc.) and OS
- Steps to reproduce
- Expected vs actual behavior
- Relevant `[P]` / `[B]` lines if using `/chess verbose`

## License

By contributing, you agree your contributions are licensed under the MIT License.
