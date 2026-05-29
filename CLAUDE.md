# AI PM Agents Suite — Claude Code Instructions

## Project overview

This is a unified suite of AI agents for product managers. It consolidates two complementary patterns:

- **`pipelines/feedback-to-strategy/`** — a sequential 6-agent pipeline that turns raw customer feedback into PRDs, strategy, and stakeholder communications.
- **`agents/`** — standalone single-purpose agents (decision-engine, financial-analyst, stakeholder-translator).

**Built by Varun Kulkarni** with Claude Code and GitHub Copilot.

## Architecture

- **Frontend (repo root)**: React 19 + Vite 7 + Tailwind CSS v4. Zero external UI libraries — all components hand-rolled.
- **Pipeline backend** (`pipelines/feedback-to-strategy/pipeline/`): Python orchestrator with typed structured outputs.
- **Standalone agents** (`agents/`): each self-contained with `SKILL.md` + `README.md`.
- **State management**: custom hooks (`usePipelineRunner`, `useTypewriter`).
- **Data**: 100% synthetic — no real customer data anywhere.

## Key files

| Path | Purpose |
|------|---------|
| `src/hooks/usePipelineRunner.js` | Pipeline orchestration state machine (frontend) |
| `src/hooks/useTypewriter.js` | RAF-based typewriter effect |
| `src/components/` | React components (one per file) |
| `src/data/` | Synthetic feedback, metrics, and pre-computed agent outputs |
| `pipelines/feedback-to-strategy/pipeline/orchestrator.py` | Python pipeline orchestrator |
| `pipelines/feedback-to-strategy/pipeline/models.py` | Typed payload contracts |
| `pipelines/feedback-to-strategy/agents/0N-name/` | Per-pipeline-agent docs + config |
| `agents/<name>/SKILL.md` | Canonical skill definition for standalone agents |

## Code style

### JavaScript / React
- ES modules with named exports.
- Functional components with hooks only (no class components).
- One component per file.
- Tailwind utility classes for styling; CSS custom properties for theming.
- kebab-case filenames, PascalCase component names.
- `const` by default, `let` when reassignment is needed, never `var`.
- No inline styles — use Tailwind or CSS classes.

### Python
- Type hints on all public functions.
- `snake_case` modules and functions, `PascalCase` classes.
- Black-formatted (line length 100).
- Pydantic models for typed agent input/output contracts.

## Security rules

- **NEVER** commit API keys, tokens, or credentials.
- **ALL** data must be synthetic — no real customer data.
- **NO** external API calls in the demo — use pre-computed outputs.
- Validate and sanitize all rendered content.

## Pipeline agent order

1. **Customer Feedback Pipeline** → Pattern Recognition
2. **Data Scientist** → Quantitative Validation
3. **Metrics Narrator** → Synthesis
4. **Chief of Staff** → Strategic Reasoning
5. **PRD Architect** → Specification
6. **Stakeholder Translator** → Audience Adaptation

## Standalone agents

| Agent | Cognitive function |
|-------|--------------------|
| Decision Engine | Strategic Reasoning |
| Financial Analyst | Quantitative Modeling |
| Stakeholder Translator (standalone) | Audience Adaptation |

> The standalone Stakeholder Translator and pipeline Stakeholder Translator are intentionally distinct — see [`agents/STAKEHOLDER_TRANSLATOR_NOTES.md`](./agents/STAKEHOLDER_TRANSLATOR_NOTES.md).

## Commands

```bash
# Frontend
npm install
npm run dev      # http://localhost:5173
npm run build
npm run lint

# Pipeline backend
cd pipelines/feedback-to-strategy
pip install -e ".[dev]"
pipeline run     # full pipeline
pipeline agents  # list all agents
pytest           # run tests
```
