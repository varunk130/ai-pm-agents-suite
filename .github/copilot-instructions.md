# AI PM Agents Suite — GitHub Copilot Instructions

## Project overview

This is a unified suite of AI agents for product managers. It consolidates two earlier projects:

- **`pipelines/feedback-to-strategy/`** — a sequential 6-agent pipeline that turns raw customer feedback into PRDs, strategy, and stakeholder communications.
- **`agents/`** — standalone single-purpose agents (decision-engine, financial-analyst, stakeholder-translator).

**Built by Varun Kulkarni** with Claude Code and GitHub Copilot.

## Architecture

- **Frontend (root)**: React 19 + Vite 7 + Tailwind CSS v4. Zero external UI libraries — components are hand-rolled.
- **Pipeline backend** (`pipelines/feedback-to-strategy/`): Python, sequential agents with typed structured outputs.
- **Standalone agents** (`agents/`): Python, each self-contained with its own SKILL.md and samples.
- **State management**: custom hooks (`usePipelineRunner`, `useTypewriter`).

## Code conventions

### JavaScript / React
- ES module imports/exports.
- Functional components with hooks only (no class components).
- One component per file with a named export.
- Tailwind utility classes for styling, CSS custom properties for theming.
- File naming: kebab-case for files, PascalCase for component names.
- Use `const` by default, `let` when reassignment is needed, never `var`.

### Python
- Type hints on all public functions.
- `snake_case` modules and functions, `PascalCase` classes.
- Black-formatted, line length 100.

## Agent structure

- Pipeline agents live in `pipelines/feedback-to-strategy/agents/0N-name/` with `README.md` and `config.js`.
- Standalone agents live in `agents/<name>/` with `SKILL.md` describing inputs, outputs, and cognitive function.

## Security requirements

- **No** API keys, tokens, or secrets in any file.
- **All** customer data is synthetic and fictional.
- **No** external API calls in the demo — pre-computed outputs only.
- Sanitize all user-facing rendered content.

## Testing

- `npm run dev` — frontend dev server.
- `npm run build` — verify production build.
- `npm run lint` — ESLint check.
- `cd pipelines/feedback-to-strategy && pytest` — Python agent tests (103 tests).
