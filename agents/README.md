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

## Two `stakeholder-translator` implementations

A `stakeholder-translator` also exists in [`../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/`](../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/). The pipeline variant is the *terminal* stage of the multi-agent pipeline and operates on the full upstream context. This standalone variant operates on a raw, free-text update. See [`./STAKEHOLDER_TRANSLATOR_NOTES.md`](./STAKEHOLDER_TRANSLATOR_NOTES.md) for when to use which.
