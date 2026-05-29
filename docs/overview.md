# Overview

The AI PM Agents Suite is a single home for two complementary collections of AI agents purpose-built for product managers.

## What's inside

### 1. A 6-agent orchestrated pipeline

Located in [`pipelines/feedback-to-strategy/`](../pipelines/feedback-to-strategy/).

Turns **50 raw customer feedback tickets + 6 months of product metrics** into:
- A prioritized strategic recommendation
- A complete PRD
- 5 audience-tailored stakeholder communications

The 6 agents run sequentially, each operating on the *full upstream context*, not just the previous agent's output. This enables emergent strategic reasoning that no single agent could produce.

### 2. Three standalone single-purpose agents

Located in [`../agents/`](../agents/).

- **Decision Engine** — multi-framework strategic analysis (RICE, ICE, Cost of Delay, Pre-mortem) with a synthesized recommendation
- **Financial Analyst** — full feature business case with assumption sourcing, sensitivity analysis, and ship/no-ship decision
- **Stakeholder Translator (standalone)** — 5 audience-tailored versions of any product update, with sensitivity classification

## Why both patterns

The two patterns solve different problems:

- The **pipeline** is for *end-to-end synthesis* — when you have heterogeneous inputs (qualitative + quantitative + temporal) that need to be transformed into a coherent strategic artifact over multiple cognitive stages.
- The **standalone agents** are for *single-step skills* — when an input maps directly to a useful output without needing multiple stages.

## When to use which

| Situation | Reach for |
|-----------|-----------|
| End-to-end synthesis of qualitative + quantitative data into strategy | The 6-agent pipeline |
| A single decision needs multi-framework analysis | Decision Engine |
| You need a feature business case | Financial Analyst |
| You need to communicate a single update to 5 audiences | Stakeholder Translator |

See [`comparison.md`](./comparison.md) for a full decision tree.

## What makes this interesting

- **Cognitive specialization** — focused single-purpose agents consistently outperform generalist ones on complex reasoning tasks.
- **Structured handoffs** — agents pass typed payloads (theme clusters with ARR impact, statistical correlations with confidence intervals, prioritized options with pre-mortem analysis), not raw text.
- **Audience-aware generation** — same information, different framing per stakeholder.
- **All synthetic data** — no real customer data, no external API calls in the demo.
