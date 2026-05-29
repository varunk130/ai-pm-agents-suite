# Agent Catalog

A quick reference for every agent in the suite. 6 pipeline agents + 3 standalone agents = **9 agents** (with one cognitive function — Audience Adaptation — appearing in two variants).

## Pipeline agents (`pipelines/feedback-to-strategy/`)

These run sequentially. Each receives the full upstream context.

| # | Agent | Cognitive function | Reads | Produces |
|---|-------|--------------------|-------|----------|
| 1 | [Customer Feedback Pipeline](../pipelines/feedback-to-strategy/agents/01-customer-feedback-pipeline/) | Pattern Recognition | 50 raw feedback tickets | Theme clusters scored by severity and ARR impact |
| 2 | [Data Scientist](../pipelines/feedback-to-strategy/agents/02-data-scientist/) | Quantitative Validation | Themes + 6mo product metrics | Cohort + funnel correlations with confidence intervals |
| 3 | [Metrics Narrator](../pipelines/feedback-to-strategy/agents/03-metrics-narrator/) | Synthesis | Themes + correlations | Strategic narrative with leading indicators |
| 4 | [Chief of Staff](../pipelines/feedback-to-strategy/agents/04-chief-of-staff/) | Strategic Reasoning | Narrative + all upstream | Prioritized recommendation with pre-mortem |
| 5 | [PRD Architect](../pipelines/feedback-to-strategy/agents/05-prd-architect/) | Specification | Top recommendation + full context | Complete PRD for top initiative |
| 6 | [Stakeholder Translator (pipeline)](../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/) | Audience Adaptation | Full PRD + strategy + metrics | 5 audience-tailored communications |

## Standalone agents (`agents/`)

These run independently on direct input.

| Agent | Cognitive function | Reads | Produces |
|-------|--------------------|-------|----------|
| [Decision Engine](../agents/decision-engine/) | Strategic Reasoning | Strategic question + options | Per-option scores (RICE, ICE, Cost of Delay, Pre-mortem) + recommendation |
| [Financial Analyst](../agents/financial-analyst/) | Quantitative Modeling | Feature description | Full financial model with sensitivity analysis and ship/no-ship decision |
| [Stakeholder Translator (standalone)](../agents/stakeholder-translator/) | Audience Adaptation | One raw product update | 5 audience-tailored communications + sensitivity classification |

## Cognitive function index

Group agents by what they're good at:

| Cognitive function | Pipeline agents | Standalone agents |
|--------------------|-----------------|-------------------|
| Pattern Recognition | #1 Customer Feedback Pipeline | — |
| Quantitative Validation | #2 Data Scientist | — |
| Quantitative Modeling | — | Financial Analyst |
| Synthesis | #3 Metrics Narrator | — |
| Strategic Reasoning | #4 Chief of Staff | Decision Engine |
| Specification | #5 PRD Architect | — |
| Audience Adaptation | #6 Stakeholder Translator | Stakeholder Translator |

## Stakeholder Translator — two variants

| | Pipeline variant | Standalone variant |
|---|------------------|--------------------|
| **Input** | Full PRD + strategy + metrics (terminal stage of pipeline) | One raw, free-text product update |
| **Use when** | You ran the end-to-end pipeline | You have a one-off update to communicate |
| **Output** | 5 communications grounded in the strategic context | 5 communications + explicit sensitivity classification |

> See [`../agents/STAKEHOLDER_TRANSLATOR_NOTES.md`](../agents/STAKEHOLDER_TRANSLATOR_NOTES.md) for the full reconciliation decision and when each variant is the right choice.
