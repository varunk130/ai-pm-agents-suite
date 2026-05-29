# Changelog

All notable changes to the AI PM Agents Suite.

## [1.0.0] — 2026-05-29

Initial release.

### Added

- **6-agent pipeline** in `pipelines/feedback-to-strategy/`: customer-feedback-pipeline → data-scientist → metrics-narrator → chief-of-staff → prd-architect → stakeholder-translator (pipeline variant).
- **3 standalone agents** in `agents/`: decision-engine, financial-analyst, stakeholder-translator (standalone variant).
- **React 19 + Vite 7 dashboard** at the repo root with a custom `usePipelineRunner` hook.
- **Unified documentation** in `docs/`: overview, architecture, agent-catalog, comparison guide, and real use-case mapping.
- **Foundation files**: LICENSE (MIT), CONTRIBUTING.md, .gitignore, GitHub Copilot instructions, PR template, chore issue template.
- **Reconciliation decision** for the two stakeholder-translator variants in `agents/STAKEHOLDER_TRANSLATOR_NOTES.md`.
- **Hero image** in `assets/hero.svg` plus polished README header.

### Build status

- `npm run lint` — passes (no warnings)
- `npm run build` — passes
- `pytest` — passes
