# Feedback → Strategy Pipeline

A sequential 6-agent pipeline that transforms raw customer feedback and product metrics into executive-ready strategy, a complete PRD, and 5 stakeholder communications.

## The pipeline

| # | Agent | Cognitive function |
|---|-------|--------------------|
| 1 | [Customer Feedback Pipeline](./agents/01-customer-feedback-pipeline/) | Pattern recognition |
| 2 | [Data Scientist](./agents/02-data-scientist/) | Quantitative validation |
| 3 | [Metrics Narrator](./agents/03-metrics-narrator/) | Synthesis |
| 4 | [Chief of Staff](./agents/04-chief-of-staff/) | Strategic reasoning |
| 5 | [PRD Architect](./agents/05-prd-architect/) | Specification |
| 6 | [Stakeholder Translator](./agents/06-stakeholder-translator/) | Audience adaptation |

## How it runs

```
50 raw feedback tickets + 6 months of product metrics
        ↓ 6 specialized AI agents ↓
Strategic recommendation + PRD + 5 stakeholder communications
```

Each agent operates on the **full upstream context**, not just the previous agent's output. This enables emergent strategic reasoning that no single agent could produce.

## Backend

The Python orchestrator lives in [`./pipeline/`](./pipeline/):

```
pipeline/
├── orchestrator.py    State machine + agent coordination
├── agents/            One module per pipeline stage
├── data/              Synthetic feedback + metrics
├── utils/             Shared helpers
├── models.py          Typed payload contracts
├── config.py          Model/temperature/route config
└── cli.py             Command-line runner
```

## Frontend

The React 19 + Vite dashboard at the repo root visualizes pipeline execution in real time.
