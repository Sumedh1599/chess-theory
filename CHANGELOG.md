# Changelog

## 1.0.0-beta.1 — 2026-08-11

### Added
- `src/tools/chess-append.js` — atomic history append (trim 20, validate, no crash)
- `src/tools/chess-validate.js` — `.chess/` validate + repair
- `cli/install.js --dry-run` / `--help`
- `uninstall.ps1` (+ `cli/uninstall.ps1`)
- Expanded automated tests: past, future, balance (9 LEANs), append, edge, install, integration, regression, platforms, performance
- CI matrix Node 18/20/22 × Ubuntu/macOS/Windows + dry-run smoke job
- `docs/PLATFORM-SUPPORT.md` version matrix

### Fixed
- LEAN `reassure` / `pivot` / `hedge` unreachable due to rule order + hardcoded `h=0`
- Past Self `category` field emission
- Future Self indented YAML under `future:`
- `chess-init` no longer wipes existing `history.jsonl`

### Changed
- `.cursor/rules/chess.mdc` Step 5 requires running `chess-append.js`
- Hooks export modules for unit testing (`require.main` guard)
