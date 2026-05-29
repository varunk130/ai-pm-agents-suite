# Changelog

All notable changes to the AI PM Agents Suite.

## [1.0.0] — 2026-05-29

Initial consolidated release. This repository merges two earlier projects (`multi-ai-agent-pm-team` and `pm-copilots`) into a single suite of AI agents for product managers.

### Added

- **6-agent pipeline** in `pipelines/feedback-to-strategy/`: customer-feedback-pipeline → data-scientist → metrics-narrator → chief-of-staff → prd-architect → stakeholder-translator (pipeline variant). Migrated from `multi-ai-agent-pm-team` in PR #2.
- **3 standalone agents** in `agents/`: decision-engine, financial-analyst, stakeholder-translator (standalone variant). Migrated from `pm-copilots` in PR #3.
- **React 19 + Vite 7 dashboard** at the repo root with a custom `usePipelineRunner` hook. Migrated from `multi-ai-agent-pm-team` in PR #2.
- **Unified documentation** in `docs/`: overview, architecture, agent-catalog, comparison guide, and real use-case mapping. Added in PR #4.
- **Foundation files**: LICENSE (MIT), CONTRIBUTING.md, .gitignore, GitHub Copilot instructions, PR template, chore issue template. Added in PR #1.
- **Reconciliation decision** for the two stakeholder-translator variants in `agents/STAKEHOLDER_TRANSLATOR_NOTES.md`. Added in PR #5 (closed chore issue #5).

### PR history

| PR | Title | Commits |
|----|-------|---------|
| #1 | Scaffold + foundation | 10 |
| #2 | Migrate 6-agent pipeline | 12 |
| #3 | Migrate standalone agents | 10 |
| #4 | Unified docs + agent catalog | 6 |
| #5 | chore — reconcile duplicate stakeholder-translator | 4 |
| #7 | Final polish | 2 |

### Issues resolved

- #5 — `chore: consolidate duplicate stakeholder-translator implementations` (resolved in PR #6 by documenting the intentional dual implementation).

### Removed

After this release, the two source repositories will be deleted:

- `varunk130/multi-ai-agent-pm-team`
- `varunk130/pm-copilots`

All history is preserved in this repo's commit log and the `agents/ATTRIBUTION.md` file.
