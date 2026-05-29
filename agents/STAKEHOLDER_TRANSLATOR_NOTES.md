# Reconciliation Notes — Two `stakeholder-translator` agents

> Resolves chore issue #5.

## TL;DR

We intentionally keep **two `stakeholder-translator` implementations** in this repo:

| Variant | Path | Operates on |
|---------|------|-------------|
| **Pipeline** | [`pipelines/feedback-to-strategy/agents/06-stakeholder-translator/`](../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/) | The full upstream context of the 6-agent pipeline (theme analysis + correlations + narrative + strategic recommendation + PRD) |
| **Standalone** | [`agents/stakeholder-translator/`](./stakeholder-translator/) | A single raw, free-text product update |

They solve **different problems** and have **different input contracts**, so merging them would either bloat the standalone agent with unused interfaces or strip the pipeline agent of context it depends on.

## Why we considered consolidating

When this suite was first assembled from two separate repos (`multi-ai-agent-pm-team` + `pm-copilots`), both contained an agent named `stakeholder-translator`. The natural first instinct was "deduplicate."

## Why we chose to keep both

1. **Different input contracts.** The pipeline variant expects a `StakeholderTranslatorInput` payload assembled from agents #1–5. The standalone variant expects a single raw string. Forcing one shape on the other would either bloat or break it.
2. **Different cognitive emphasis.** The standalone variant adds an explicit **sensitivity classification** step (Safe / Caution / Internal Only) because its caller has *only* the raw update — there's no upstream metadata to mark what's sensitive. The pipeline variant inherits that signal from upstream agents.
3. **Different latency profile.** The standalone agent is meant to be called interactively for a one-off update. The pipeline agent runs after several seconds of upstream processing.
4. **Composability is preserved.** A caller who runs the full pipeline gets the pipeline-grounded comms automatically. A caller who has only one update reaches for the standalone agent.

## What changed as part of this chore

- Both READMEs now explicitly cross-reference each other and explain the difference at the top.
- This notes document captures the decision rationale for future contributors.
- `docs/agent-catalog.md` and `docs/comparison.md` were updated to remove "PR 5 will reconcile" breadcrumbs.
- The cognitive-function index in `docs/agent-catalog.md` lists both variants under Audience Adaptation.

## When to revisit

If we ever introduce a third stakeholder-translator (or a generic "audience adaptation" interface), reconsider extracting the shared parts into a common module under `agents/_shared/`. Until then, the duplication is intentional and load-bearing.
