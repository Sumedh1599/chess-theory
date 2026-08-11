# Chess Theory — Maintainer Guide

## Project Structure

```
chess-theory/
├── README.md              # User-facing intro (problem + features)
├── INSTALL.md             # Step-by-step install per platform
├── CONTRIBUTING.md        # How to patch
├── LICENSE                # MIT
├── package.json           # npm metadata
├── .gitignore
│
├── .cursor/rules/
│   └── chess.mdc          # The ruleset (single source of truth)
│
├── skills/
│   └── chess/
│       └── SKILL.md       # Claude Code skill (same rules, frontmatter)
│
├── .agents/
│   ├── cursor.mdc         # Cursor rules symlink
│   ├── windsurf.mdc       # Windsurf rules
│   ├── cline.mdc          # Cline rules
│   └── copilot.mdc        # GitHub Copilot rules
│
├── cli/
│   ├── install.js         # Main installer (detects agents)
│   ├── uninstall.js       # Cleanup script
│   └── lib/
│       ├── settings.js    # JSONC-tolerant config reader
│       └── chess-init.js  # Repo initializer
│
├── src/
│   ├── tools/
│   │   └── chess-init.js  # Standalone repo scanner
│   │
│   └── hooks/
│       ├── chess-past-cache.js    # Read history, emit [P]
│       ├── chess-future-read.js   # Read spec, emit [F]
│       ├── chess-balance.js       # Compute [B]
│       ├── chess-activate.js      # Session startup
│       └── chess-statusline.sh    # Status badge
│
├── .chess/ (created by user)
│   ├── history.jsonl      # Session transcript (auto-appended)
│   ├── spec.yaml          # Project constraints (user + auto-gen)
│   ├── deps.json          # Dependency graph
│   └── patterns.json      # Pattern library
│
├── .github/
│   └── workflows/
│       ├── test.yml       # Node tests, bash lint
│       ├── release.yml    # Tag → GitHub release
│       └── publish.yml    # npm publish
│
├── tests/
│   ├── past-self.test.js
│   ├── future-self.test.js
│   ├── balance.test.js
│   └── integration.test.js
│
├── evals/
│   ├── baseline/          # Unmodified agent responses
│   ├── chess/             # Same prompts, chess on
│   ├── caveman-blend/     # Chess + caveman together
│   └── stats.json         # Token count comparison
│
├── docs/
│   ├── ARCHITECTURE.md    # How the three selves work
│   ├── PLATFORM-SUPPORT.md # Which agent versions tested
│   ├── FAQ.md             # Common questions
│   └── examples/
│       ├── session-1.md   # Real user session with [P][F][B]
│       └── session-2.md
│
└── assets/
    ├── banner.png         # 1200×630 for GitHub
    ├── demo.gif           # 10sec showing /chess
    └── chess-board.svg    # Logo
```

## File Ownership

| File(s) | Owner | When Changed |
|---------|-------|--------------|
| `.cursor/rules/chess.mdc` | Maintainer | Core logic updates |
| `skills/chess/SKILL.md` | Maintainer (generated from `.mdc`) | After `.mdc` changes |
| `.agents/*.mdc` | Maintainer (symlinks or copies of `.mdc`) | After `.mdc` changes |
| `cli/install.js` | Maintainer | Agent detection changes |
| `src/hooks/*.js` | Maintainer | Logic changes |
| `.chess/history.jsonl` | User (auto-appended) | Every user turn |
| `.chess/spec.yaml` | User + auto-gen | User + `/chess init` |
| README.md | Maintainer | Feature adds + marketing |
| INSTALL.md | Maintainer | Platform support changes |

## Build & Release Process

### Before Every Commit

```bash
# 1. Lint
npm run lint

# 2. Test (unit + integration + platforms)
npm run test

# 3. Coverage (Node experimental; target ≥85% lines)
npm run test:coverage

# 4. Dry-run install
node cli/install.js --dry-run

# 5. History append (after Chess responses in real use)
node src/tools/chess-append.js --cat code --sig '✓' --s 2 --ctx "change summary" --fix "what-worked"
```

### Versioning

- Current: **`1.0.0-beta.1`** (see `CHANGELOG.md`)
- npm publish uses `--tag beta` while version contains `beta`

### Releasing

1. Update version in `package.json`
2. Add entry to `CHANGELOG.md`
3. Commit: `git commit -am "v1.0.x: fix past self severity calc"`
4. Tag: `git tag v1.0.x`
5. Push: `git push origin main --tags`
6. GitHub Actions auto-publishes to npm

### CI Matrix (GitHub Actions)

```yaml
strategy:
  matrix:
    node-version: [18, 20, 22]
    os: [ubuntu-latest, macos-latest, windows-latest]
    agent: [claude-code, cursor, windsurf, cline]
```

## Known Limitations

1. **History size** — `.chess/history.jsonl` kept at ~20 lines; older entries discarded. For full audit trail, add `/chess compact` command.
2. **Spec.yaml editing** — User must edit by hand (no GUI). Consider adding `/chess edit-spec` wrapper.
3. **No cross-project memory** — Each project has its own `.chess/` dir. No global learning.
4. **No multi-agent consensus** — One agent's [P] doesn't influence another's.

## Future Roadmap

- [ ] Web dashboard showing [P][F][B] over time (metrics viz)
- [ ] `/chess export-session` → JSON for analysis
- [ ] Cross-project memory store (optional Redis backend)
- [ ] Multi-model comparison (same prompt, Chess on 3 different LLMs)
- [ ] Slack integration for team debugging
- [ ] VSCode extension showing Chess status in sidebar

## Contributing

See `CONTRIBUTING.md` for patch workflow. Summary:

1. Fork
2. Branch: `git checkout -b fix/past-self-severity`
3. Write tests in `tests/`
4. Update `.cursor/rules/chess.mdc` if logic changes
5. Run `npm run test` — must pass
6. PR with description

## Maintainer Checklist (Monthly)

- [ ] Review open issues (label: `bug` vs `enhancement`)
- [ ] Run benchmarks against latest Claude/Cursor models
- [ ] Check for new agent platforms (Roo, Windsurf updates)
- [ ] Update PLATFORM-SUPPORT.md version matrix
- [ ] Verify install.sh still works (curl + bash)
