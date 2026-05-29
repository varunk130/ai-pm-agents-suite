# Stakeholder Translator (standalone)

> Audience adaptation agent for one-off product communications.

## What it does

Takes a single product update and produces five tailored communications — each with the right tone, detail level, technical depth, and framing for its audience. Includes sensitivity classification so PMs know what's shareable and what's not.

## Inputs

- One raw product update (free text — features, status, decisions, risks)
- Optional: target audience emphasis, sensitive topic flags

## Outputs

| Output | Audience | Framing |
|--------|----------|---------|
| Engineering Update | Dev team | Technical decisions, code references, debt trade-offs |
| Executive Summary | Leadership | Business impact, metrics, decisions needed |
| Board Narrative | Board of Directors | Strategic positioning, speaker notes |
| Customer Changelog | End users | Benefits-focused, no internal details |
| Sales Enablement | Sales team | Objection handling, competitive positioning, talk tracks |

Plus a **sensitivity classification table** (Safe / Caution / Internal Only) per piece of information.

## When to use

- A single update needs to be reshaped for 5 different audiences
- You want to make share-vs-don't-share decisions explicit

## Relationship to the pipeline variant

There is also a `stakeholder-translator` inside the [6-agent pipeline](../../pipelines/feedback-to-strategy/agents/06-stakeholder-translator/). The pipeline variant is the *terminal* step of the multi-agent workflow and operates on the full upstream context (PRD, strategy, metrics). This standalone variant operates on a raw, free-text update.

> See [`../STAKEHOLDER_TRANSLATOR_NOTES.md`](../STAKEHOLDER_TRANSLATOR_NOTES.md) for the full reconciliation decision and when each variant is the right choice.

## Files

- [`SKILL.md`](./SKILL.md) — the full skill definition
- See [`../SAMPLES.md`](../SAMPLES.md) for end-to-end examples (use cases 1 and 2)
- Screenshot: [`../screenshots/stakeholder-translator.png`](../screenshots/stakeholder-translator.png)
