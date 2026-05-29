# Decision Engine

> Multi-framework strategic reasoning agent.

## What it does

Takes a strategic question (or a set of options) and produces a structured analysis that scores each option against multiple frameworks, then synthesizes a recommendation.

## Inputs

- A clear strategic question (e.g. "Should we build, buy, or partner for capability X?")
- A list of candidate options (2–6)
- Optional: constraints, success criteria, decision deadline

## Outputs

- Per-option score against each framework
- An Impact × Confidence matrix
- Pre-mortem ("how could this go wrong")
- A synthesized recommendation with the reasoning chain

## Frameworks

| Framework | What it measures |
|-----------|------------------|
| RICE | Reach × Impact × Confidence ÷ Effort |
| ICE | Impact × Confidence × Ease |
| Cost of Delay | Value lost per week of delay |
| Pre-mortem | Failure modes ranked by likelihood × severity |

## When to use

- A single decision needs structured, multi-framework analysis
- You want to make the trade-offs explicit and defensible

## Files

- [`SKILL.md`](./SKILL.md) — the full skill definition
- See [`../SAMPLES.md`](../SAMPLES.md) for end-to-end examples (use cases 3 and 4)
- Screenshot: [`../screenshots/decision-engine.png`](../screenshots/decision-engine.png)
