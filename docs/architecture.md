# Architecture

> 🚧 Skeleton — full content lands in PR 4.

## Two complementary patterns

### 1. Sequential pipeline (multi-agent orchestration)

Used for end-to-end synthesis tasks. Each agent operates on the *full upstream context*, not just the previous agent's output, which enables emergent strategic insights.

```
[Feedback + Metrics] → A1 → A2 → A3 → A4 → A5 → A6 → [PRD + Strategy + Comms]
                       │     │     │     │     │     │
                       └─────┴─────┴─────┴─────┴─────┘
                          shared context grows with each step
```

Why this works:
- **Cognitive specialization** — focused single-purpose agents outperform monolithic prompts on complex reasoning.
- **Structured handoffs** — agents pass typed payloads (theme clusters, statistical correlations, prioritized options), not raw text.
- **Context accumulation** — downstream agents reason over everything that came before.

### 2. Standalone agents (single-step skills)

Used when the input maps directly to a useful output without needing multiple cognitive stages.

```
[Input] → Agent → [Output]
```

Examples:
- One product update → 5 audience-tailored versions
- One strategic question → 4-framework analysis
- One feature → financial model with sensitivity

## Shared principles

- All data is synthetic.
- No external API calls in the demo — pre-computed outputs only.
- Structured output schemas, not freeform text.
- Audience-aware framing where relevant.
