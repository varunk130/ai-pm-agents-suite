# Architecture

This suite uses **two complementary patterns** for AI agents.

## Pattern 1 — Sequential pipeline (multi-agent orchestration)

Used for end-to-end synthesis tasks where the input is heterogeneous (qualitative + quantitative + temporal) and the output requires multiple cognitive stages.

```
[Feedback + Metrics] → A1 → A2 → A3 → A4 → A5 → A6 → [PRD + Strategy + Comms]
                       │     │     │     │     │     │
                       └─────┴─────┴─────┴─────┴─────┘
                          shared context grows with each step
```

### Why this works

- **Cognitive specialization** — focused single-purpose agents outperform monolithic prompts on complex reasoning.
- **Structured handoffs** — agents pass typed payloads (theme clusters, statistical correlations, prioritized options), not raw text.
- **Context accumulation** — downstream agents reason over everything that came before, enabling emergent strategic insights.

### Implementation

- Orchestrator: [`pipelines/feedback-to-strategy/pipeline/orchestrator.py`](../pipelines/feedback-to-strategy/pipeline/orchestrator.py)
- Typed payload contracts: [`pipelines/feedback-to-strategy/pipeline/models.py`](../pipelines/feedback-to-strategy/pipeline/models.py)
- Per-agent modules: [`pipelines/feedback-to-strategy/pipeline/agents/`](../pipelines/feedback-to-strategy/pipeline/agents/)
- React dashboard: [`src/`](../src/) (with `usePipelineRunner` hook as the client state machine)

## Pattern 2 — Standalone agents (single-step skills)

Used when an input maps directly to a useful output without needing multiple cognitive stages.

```
[Input] → Agent → [Output]
```

Examples:
- One product update → 5 audience-tailored versions
- One strategic question → 4-framework analysis
- One feature → financial model with sensitivity

### Why this works

- **Fast** — no orchestration overhead.
- **Composable** — can be called independently from other tools.
- **Inspectable** — each output is a single, focused artifact.

### Implementation

Each standalone agent lives in [`agents/<name>/`](../agents/) and ships with:
- `SKILL.md` — the canonical skill definition (inputs, outputs, methodology)
- `README.md` — wrapper with quick start and links
- Outputs are illustrated by screenshots in [`agents/screenshots/`](../agents/screenshots/)

## Shared principles

| Principle | How it shows up |
|-----------|-----------------|
| All data is synthetic | No real customer data in any input |
| No external API calls in demo | Pre-computed outputs only |
| Structured output schemas | Typed payloads, not freeform text |
| Audience-aware framing | Same info, different per stakeholder |
| Cognitive specialization | One agent = one cognitive role |

## Frontend (shared)

- **React 19 + Vite 7 + Tailwind CSS v4**
- Zero external UI libraries — every component is hand-rolled
- Custom hooks for state: `usePipelineRunner` (pipeline state machine), `useTypewriter` (RAF-based reveal effect)
- File naming: kebab-case for files, PascalCase for component names
