# Contributing to AI PM Agents Suite

Thanks for your interest! This repo is a curated showcase of AI agents for product managers — a 6-agent orchestrated pipeline plus 3 standalone single-purpose agents.

## Local setup

```bash
# Frontend (run from repo root)
npm install
npm run dev          # http://localhost:5173
npm run build        # production build → dist/
npm run lint

# Python pipeline (run from pipelines/feedback-to-strategy)
python -m venv .venv
.\.venv\Scripts\Activate.ps1     # Windows
# source .venv/bin/activate      # macOS / Linux
pip install -r requirements.txt
cd pipelines/feedback-to-strategy
pip install -e ".[dev]"
pytest                            # 103 tests
pipeline run                      # full pipeline
```

## Repo layout

```
ai-pm-agents-suite/
├── src/                                 React 19 + Vite frontend (overview dashboard)
├── pipelines/feedback-to-strategy/      Sequential 6-agent pipeline
│   ├── pipeline/                         Python package
│   ├── agents/                           Per-agent docs + configs
│   ├── tests/                            Pytest suite (103 tests)
│   └── pyproject.toml                    Pipeline package definition
├── agents/                               Standalone single-purpose agents
├── docs/                                 Architecture, overview, agent catalog
└── assets/                               Hero image and other branding assets
```

## Conventions

- **JavaScript/React**: ES modules, functional components with hooks, kebab-case files, PascalCase components, Tailwind utility classes.
- **Python**: Black-formatted (line length 100), `snake_case` modules, type hints required on public functions.
- **No external UI libraries** — components are hand-rolled.
- **All data is synthetic.** Never commit real customer data, credentials, or PII.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(agents): add decision-engine scoring matrix
fix(pipeline): handle empty feedback array
chore(deps): bump vite to 7.1
docs(catalog): document new agent
```

## Pull requests

1. Branch from `main`: `git checkout -b <type>/<short-description>`.
2. Keep PRs focused — one logical change per PR.
3. Make sure `npm run lint`, `npm run build`, and `pytest` all pass.
4. Fill out the PR template.

## Reporting issues

- **Bugs** → `bug` label
- **Routine maintenance** → `chore` label
- **New ideas** → `enhancement` label


- **JavaScript/React**: ES modules, functional components with hooks, kebab-case files, PascalCase components, Tailwind utility classes.
- **Python**: Black-formatted (line length 100), `snake_case` modules, type hints required on public functions.
- **No external UI libraries** — components are hand-rolled.
- **All data is synthetic.** Never commit real customer data, credentials, or PII.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(agents): add decision-engine scoring matrix
fix(pipeline): handle empty feedback array
chore(deps): bump vite to 7.1
docs(catalog): document new agent
```

## Pull requests

1. Branch from `main`: `git checkout -b <type>/<short-description>`.
2. Keep PRs focused — one logical change per PR.
3. Make sure `npm run lint`, `npm run build`, and `pytest` all pass.
4. Fill out the PR template.

## Reporting issues

- **Bugs** → `bug` label
- **Routine maintenance** → `chore` label
- **New ideas** → `enhancement` label
