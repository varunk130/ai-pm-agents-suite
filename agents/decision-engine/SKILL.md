---
name: decision-engine
description: 'Multi-framework strategic analysis for product decisions. Use when: prioritize features, evaluate trade-offs, strategic decision, impact analysis, pre-mortem, ship or sunset, quarterly planning, compare options, confidence scoring.'
---

# Decision Engine

Apply four analytical frameworks to any product decision, then synthesize into a single prioritized recommendation with confidence scoring and pre-mortem analysis.

## Output
Save to `outputs/decision-[topic]-[YYYY-MM-DD].md`

## When to Use
- Quarterly prioritization with competing initiatives
- Ship / iterate / sunset decisions for features
- Build vs. buy vs. partner evaluations
- Any decision where you need structured reasoning, not gut feel

## What You'll Get

| Framework | What It Evaluates |
|-----------|-------------------|
| **Impact × Confidence Matrix** | Revenue impact weighted by execution certainty |
| **Strategic Alignment** | Weighted scoring against company goals |
| **Second-Order Effects** | Downstream consequences (positive and negative) |
| **Pre-Mortem Analysis** | "It's December and this failed — what went wrong?" |

Plus:
- **Synthesized Recommendation** with confidence score
- **Actionable Next Steps** with owners and dates
- **Risk Register** with mitigation strategies

## Process

### Step 1: Define the Decision
I'll ask:
> "What decision are you facing? List the options you're considering (2-4 options work best). Include any context about constraints, timeline, or strategic priorities."

### Step 2: Impact × Confidence Matrix
For each option, I'll score:
- **Impact** (1-10): Revenue potential, user value, market differentiation
- **Confidence** (1-10): Technical feasibility, team capability, timeline certainty
- **Weighted Score** = Impact × Confidence / 10

### Step 3: Strategic Alignment
I'll score each option against your company's strategic pillars:
- Growth & Revenue (weight: 30%)
- Customer Retention (weight: 25%)
- Technical Excellence (weight: 20%)
- Market Positioning (weight: 15%)
- Team Development (weight: 10%)

### Step 4: Second-Order Effects
For each option, I'll map:
- **Positive cascades**: What else gets better if this succeeds?
- **Negative cascades**: What breaks or gets harder?
- **Opportunity costs**: What can't you do if you pick this?

### Step 5: Pre-Mortem
For the top option:
> "It's 6 months from now. This initiative failed. What went wrong?"
I'll generate 4-5 failure scenarios with probability estimates and mitigations.

### Step 6: Synthesis
I'll combine all four frameworks into:
- **Recommended option** with overall confidence
- **Key conditions** that must be true for this to work
- **Decision reversibility** — how easy is it to change course?
- **Next steps** with specific owners and timelines

## Demo Scenario: Quarterly Prioritization

**Input:**
> "We need to pick one initiative for Q2. Options: (A) AI-powered analytics dashboard, (B) Enterprise SSO + compliance features, (C) Mobile app v2 redesign. We're a B2B SaaS with 200 enterprise customers, $15M ARR, trying to move upmarket."

**Sample Impact × Confidence Matrix:**

| Option | Impact | Confidence | Weighted | Rationale |
|--------|--------|------------|----------|-----------|
| A: AI Analytics | 8 | 6 | 4.8 | High differentiation but unproven tech stack |
| B: Enterprise SSO | 7 | 9 | 6.3 | Clear requirements, proven patterns, direct revenue |
| C: Mobile Redesign | 5 | 7 | 3.5 | Nice-to-have, not blocking deals |

**Sample Pre-Mortem (Option B: Enterprise SSO):**

| Failure Scenario | Probability | Mitigation |
|---|---|---|
| SSO integration testing takes 3x longer due to customer IdP variations | 35% | Start with top 3 IdPs only (Okta, Azure AD, OneLogin) |
| Compliance certifications (SOC2 Type II) delayed by audit backlog | 25% | Begin audit prep in parallel, don't gate launch on cert |
| Enterprise deals close but at lower ACV than modeled | 20% | Pre-negotiate 2 pilot deals before committing Q2 scope |
| Team morale drops working on "boring" infrastructure | 15% | Frame as career growth; SSO expertise is marketable |

## Tips
1. **Include constraints** — Budget, timeline, team size, technical debt
2. **Be honest about unknowns** — "We're not sure if X" is better than guessing
3. **3 options is ideal** — 2 feels binary, 4+ gets noisy
