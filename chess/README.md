# CHESS — Claude Code & Cursor Skill

<p align="center">
  <img src="assets/banner.png" alt="CHESS — Calibrated Hindsight-Foresight Ensemble" width="100%" />
</p>

> **C**alibrated **H**indsight-**F**oresight **E**nsemble for **S**trategic **S**elf-arbitration

A unified, single-command skill implementing the three-seat meta-cognitive architecture from
[*Strategic Self-Arbitration in LLM Agents*](research_paper.pdf) (Patil, 2026).

<p align="center">
  <img src="assets/diagram.png" alt="Three-seat CHESS architecture diagram" width="480" />
</p>

## What This Does (One Pipeline, One Command)

When `/chess` is active, **every response** automatically runs:

1. **Past (Hindsight)** — Scans conversation history/cache → extracts lessons (✅❌⚠️❓)
2. **Future (Foresight)** — Generates 3 internal candidates (Direct / Conservative / Creative)
3. **Present (Arbitration)** — Runs variational inference (ELBO) → picks the optimal move
4. **Output** — Emits only the winning move. No meta-commentary. No step labels.

No `/chess-board`, `/chess-hindsight`, `/chess-foresight` fragmentation. Just `/chess`.

## Install

### Claude Code (recommended)

**One-shot installer:**

```bash
git clone https://github.com/Sumedh1599/chess-theory.git
cd chess-theory/chess
bash install.sh
```

**Project-local** (commit into a repo):

```bash
mkdir -p .claude/skills/chess
cp SKILL.md hindsight.md foresight.md arbitration.md README.md LICENSE research_paper.pdf .claude/skills/chess/
cp -R examples scripts src assets .claude/skills/chess/
```

**Global** (personal):

```bash
mkdir -p ~/.claude/skills/chess
cp SKILL.md hindsight.md foresight.md arbitration.md README.md LICENSE research_paper.pdf ~/.claude/skills/chess/
cp -R examples scripts src assets ~/.claude/skills/chess/
```

Activate: open Claude Code, type `/chess`  
Deactivate: `/chess off` or say "normal mode"

### Cursor

#### Option A — `.cursorrules` (project root)

```bash
cp .cursorrules /path/to/your/project/
```

#### Option B — `.cursor/rules/chess.mdc` (Project Rules panel)

```bash
mkdir -p /path/to/your/project/.cursor/rules
cp .cursor/rules/chess.mdc /path/to/your/project/.cursor/rules/
```

Cursor does not use slash commands. The rule is **always on** while the file is present. To disable, rename or remove it.

## Research Paper

Full write-up (keep with the skill): [`research_paper.pdf`](research_paper.pdf)

| Hypothesis | Finding |
|-----------|---------|
| **H1** (board perception) | Mixed — 2/3 models perfect; 1 showed irregular positional degradation |
| **H2** (hindsight helps) | **Strong** — +0.56 to +0.62 uplift, p < .001 across all 3 models |
| **H3** (variational arbitration) | **Strong** — beats greedy by 48–80pp, fixed-weight by 10–50pp |
| **H6** (dynamic allocation) | Analytical — dynamic beats static by +7.5%, random by +18.6% |

## Optional: Python reference implementation

The `src/` package mirrors the paper’s H1–H3 machinery. Not required for Claude/Cursor to load the skill.

```bash
cd chess
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

PYTHONPATH=. python examples/basic_usage.py
PYTHONPATH=. python scripts/elbo.py --candidates 3 --steps 10
PYTHONPATH=. python examples/h1_positional_retrieval.py
PYTHONPATH=. python examples/h2_hindsight_injection.py
PYTHONPATH=. python examples/h3_arbitration.py
```

## File Structure

```text
chess/
├── SKILL.md                 # Claude Code skill (frontmatter + unified pipeline)
├── README.md                # This file
├── LICENSE                  # MIT
├── research_paper.pdf       # Full research paper
├── install.sh               # One-shot skill installer
├── requirements.txt         # Optional Python deps (numpy, scipy)
├── .cursorrules             # Cursor project rules (plain markdown)
├── .cursor/rules/chess.mdc  # Cursor Project Rules (frontmatter)
├── hindsight.md             # Hindsight auto-extraction protocol
├── foresight.md             # Foresight candidate generation rubric
├── arbitration.md           # Variational inference step-by-step
├── assets/
│   ├── banner.png           # Hero banner
│   ├── diagram.png          # Three-seat architecture
│   └── chess-board.svg      # Logo mark
├── examples/                # Conflict worked examples + experiment demos
├── scripts/
│   └── elbo.py              # ELBO convergence checker
└── src/                     # Python reference implementation
    ├── chess_core.py
    └── experiments.py
```

## Compatibility

| Platform | File | Location |
|----------|------|----------|
| Claude Code | `SKILL.md` | `.claude/skills/chess/` or `~/.claude/skills/chess/` |
| Cursor (global) | `.cursorrules` | Project root |
| Cursor (project rule) | `.cursor/rules/chess.mdc` | `.cursor/rules/` |
| Other agents | via `install.sh` | `~/.cursor/skills`, `~/.codex/skills`, etc. |

## License

MIT — see [`LICENSE`](LICENSE).
