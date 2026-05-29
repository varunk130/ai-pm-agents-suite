# Standalone Agents

Single-purpose AI agents for product managers. Use these when an input maps directly to a useful output without needing the multi-stage pipeline.

## Agents

| Agent | Cognitive function | Input | Output |
|-------|--------------------|-------|--------|
| [Decision Engine](./decision-engine/) | Strategic Reasoning | A strategic question + options | Multi-framework scored analysis with synthesized recommendation |
| [Financial Analyst](./financial-analyst/) | Quantitative Modeling | A feature description | Full financial model with sensitivity analysis and ship/no-ship decision |
| [Stakeholder Translator](./stakeholder-translator/) | Audience Adaptation | One product update | 5 audience-tailored communications (Engineering, Exec, Board, Customer, Sales) with sensitivity classification |

## Samples

See [`./SAMPLES.md`](./SAMPLES.md) for end-to-end example scenarios.

## Origin

These agents were migrated from the `pm-copilots` repository. See [`./ATTRIBUTION.md`](./ATTRIBUTION.md).

> **Note:** A `stakeholder-translator` also exists in [`../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/`](../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/). The pipeline variant is the *terminal* stage of the multi-agent pipeline; this standalone variant is for ad-hoc one-off communications. PR 5 reconciles overlap between them.
