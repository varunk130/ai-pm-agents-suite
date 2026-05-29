# When to use the pipeline vs a standalone agent

A short decision guide.

## Decision tree

```
Q: What kind of input do you have?
├── Heterogeneous (qualitative + quantitative + temporal)
│   └── Use the 6-agent pipeline ────────────► pipelines/feedback-to-strategy/
│
└── A single focused input
    ├── A decision to make → Decision Engine
    ├── A feature to justify financially → Financial Analyst
    └── An update to communicate → Stakeholder Translator (standalone)
```

## Side-by-side

| | Pipeline | Standalone agent |
|---|----------|------------------|
| Input shape | Multiple, heterogeneous | One focused artifact |
| Stages | 6 sequential | 1 |
| Output | PRD + strategy + comms | One focused output |
| Time to result | Tens of seconds | Seconds |
| Best for | Quarterly strategy, executive briefs | Day-to-day PM work |

## Common scenarios

| Scenario | Use |
|----------|-----|
| You just got 50 support tickets dumped in your inbox + need to brief the exec team next week | Pipeline |
| You have 3 features competing for next-quarter roadmap | Decision Engine |
| You need a CFO-ready business case for a new capability | Financial Analyst |
| You just shipped a feature and need to communicate it to engineering, exec, board, customers, and sales | Stakeholder Translator (standalone) |
| You ran the pipeline and want the final stakeholder comms | The pipeline's own stakeholder-translator (it runs as agent #6 automatically) |

## Anti-patterns

- **Don't use the pipeline for a single decision** — Decision Engine is faster and more focused.
- **Don't use a standalone agent for end-to-end synthesis** — you'll lose the upstream context the pipeline provides.
- **Don't run the standalone stakeholder-translator on pipeline outputs** — agent #6 in the pipeline already does that with richer context.
