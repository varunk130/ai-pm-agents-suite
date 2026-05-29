# Financial Analyst

> Quantitative modeling agent for feature business cases.

## What it does

Takes a feature description and produces a complete financial model: revenue impact, cost of delivery, sensitivity to key assumptions, and a ship/no-ship recommendation.

## Inputs

- A feature description (problem, proposed solution, target user, expected adoption)
- Optional: known constraints (engineering capacity, pricing model, comparable benchmarks)

## Outputs

- Key metrics dashboard (ARR delta, payback period, NPV, expected ROI)
- Assumption sourcing (so reviewers know what's a guess vs benchmarked)
- Sensitivity analysis (which assumptions move the answer the most)
- Ship / no-ship decision with reasoning

## Methodology

1. Decompose feature into revenue and cost drivers.
2. Set base, conservative, and optimistic assumptions per driver.
3. Compute NPV and payback for each scenario.
4. Identify the 2–3 highest-leverage assumptions via tornado chart logic.
5. Emit a recommendation with confidence band.

## When to use

- You need a defensible business case for a feature
- You want to expose assumption risk explicitly
- You're presenting to finance or exec leadership

## Files

- [`SKILL.md`](./SKILL.md) — the full skill definition
- See [`../SAMPLES.md`](../SAMPLES.md) for end-to-end examples (use cases 5 and 6)
- Screenshot: [`../screenshots/financial-analyst.png`](../screenshots/financial-analyst.png)
