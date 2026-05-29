# Real PM use cases → agent mapping

End-to-end scenarios drawn from typical PM workflows, mapped to the agent(s) that solve them.

> For full worked examples with inputs and outputs, see [`../agents/SAMPLES.md`](../agents/SAMPLES.md).

## 1. Quarterly strategy ritual

**Scenario:** End of Q. You have a quarter's worth of support tickets, NPS responses, churn interviews, and product metrics. You need to brief the exec team on what to prioritize next quarter.

**Use:** The 6-agent pipeline. Drop all the qualitative and quantitative inputs in; you get back a prioritized strategic recommendation, a PRD for the top initiative, and stakeholder comms for 5 audiences.

## 2. Feature prioritization argument

**Scenario:** Three features are competing for the next sprint. Engineering, design, and sales each have a favorite.

**Use:** Decision Engine. Feed it the three options. It produces RICE / ICE / Cost of Delay / Pre-mortem scores per option plus a synthesized recommendation with the reasoning chain.

## 3. Build-vs-buy / partner decision

**Scenario:** You need a capability X. You can build it (6 months), buy a vendor (signed contract by next week), or partner with a third party (3 month integration).

**Use:** Decision Engine. The pre-mortem framework surfaces the failure modes that usually decide these — vendor lock-in for buy, integration debt for partner, opportunity cost for build.

## 4. Feature business case

**Scenario:** You're proposing a new capability. Finance wants ARR impact + payback period before approving the headcount.

**Use:** Financial Analyst. Provides the model with explicit assumption sourcing so the conversation focuses on the assumptions, not the math.

## 5. Pricing model change

**Scenario:** You're shifting from seat-based to usage-based pricing. You need to model the impact on existing accounts and on new-customer acquisition.

**Use:** Financial Analyst. The sensitivity analysis is the centerpiece — it tells you which assumptions matter most.

## 6. Major launch communication

**Scenario:** You're shipping a flagship feature next Tuesday. You need to brief engineering on the technical decisions, send an exec summary, prep a board narrative, write a customer changelog, and arm sales with talk tracks — all from the same raw context.

**Use:** Stakeholder Translator (standalone). One raw update goes in, five tailored versions come out, with explicit sensitivity classification so you don't accidentally share competitive intel in the customer changelog.

## 7. Missed-deadline escalation

**Scenario:** A critical release just slipped by two weeks. You need to communicate to everyone without creating panic.

**Use:** Stakeholder Translator (standalone). Particularly the sensitivity classification — it draws the line between what executives need to know and what's safe to put in the customer changelog.

---

## Cross-pattern: pipeline → standalone follow-up

Sometimes you run the pipeline, and then a downstream conversation surfaces a specific question the pipeline didn't address. That's a fine fit for a standalone agent:

| Pipeline produced... | Follow-up | Use |
|----------------------|-----------|-----|
| A prioritized recommendation that the CFO is skeptical of | Build the business case | Financial Analyst |
| A PRD with three implementation options | Pick the implementation approach | Decision Engine |
| Stakeholder comms that need re-framing for a sixth audience | Generate the additional audience version | Stakeholder Translator (standalone) |
