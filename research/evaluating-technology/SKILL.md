---
name: evaluating-technology
description: Evaluate a technology, tool, framework, or platform for fit — assessing capability, maturity, ecosystem, cost, risk, and alignment with needs and constraints. Use when the user asks to "evaluate this technology/tool/framework", "should we use X", "tech selection", or assess a platform before adopting. Balances hype against evidence and total cost against benefit. Produces an evidence-based fit assessment and recommendation, not a hype-driven pick.
---

# Evaluating Technology

## Scope
Assessing whether a specific technology fits a need: capability, maturity, ecosystem,
cost/TCO, risk, and alignment with requirements and constraints. Feeds adoption and
build-vs-buy decisions. Weighted selection among options is
[building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Purpose
Cut through hype to an evidence-based fit judgment: does this technology actually meet
the requirements, at acceptable maturity, cost, and risk, for *this* team and context —
not "is it popular/cool."

## When to use this skill
- "Evaluate this technology / tool / framework / platform. Should we use X?"
- Tech selection or adoption decisions; build-vs-buy inputs.
- Assessing a platform's fit and risk before committing.

## When NOT to use this skill
- Weighted scoring across options → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- Architecture design review → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).
- Financial-only analysis → [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md).

## Inputs
- The technology and the specific need/requirements it must meet.
- Constraints: team skills, existing stack, budget, timeline, compliance.

## Outputs
- A fit assessment: capability vs. requirements, maturity/ecosystem, TCO, risks, and
  a recommendation (adopt / trial / avoid) with the conditions and evidence.

## Workflow
```
Progress:
- [ ] 1. Define the need and must-have requirements
- [ ] 2. Assess capability fit against those requirements
- [ ] 3. Evaluate maturity: stability, adoption, roadmap, longevity
- [ ] 4. Assess ecosystem: docs, community, support, talent, integrations
- [ ] 5. Estimate TCO and risks (lock-in, security, skills gap)
- [ ] 6. Recommend adopt/trial/avoid, with conditions
```

**Step 1–2 — requirements before technology.** Evaluate against what you actually
need, not against a feature list; the "best" technology that doesn't fit your
requirements is the wrong choice. **Step 3 — maturity over novelty:** check stability,
real-world adoption, release cadence, and whether it'll be maintained — the newest
tool is often the riskiest. **Step 5 — total cost and risk:** licensing plus
integration, migration, skills, and operational cost; plus lock-in, security posture,
and the talent market. **Step 6 — hands-on beats reading:** for anything significant,
a spike/trial is worth more than any spec sheet; recommend a time-boxed trial when
uncertainty is high.

## Principles
1. **Requirements first,** technology second.
2. **Maturity and longevity over hype/novelty.**
3. **Total cost of ownership,** not sticker price.
4. **Ecosystem matters** — docs, community, talent, support.
5. **Assess risk** — lock-in, security, abandonment, skills gap.
6. **Trial to know** — hands-on evidence over marketing.

## Decision framework
- **Mission-critical/long-lived?** Weight maturity, support, and longevity heavily.
- **Fast-moving/experimental?** Newer tech acceptable; contain the risk.
- **Team lacks the skills?** Factor ramp-up cost and talent availability.
- **High uncertainty?** Recommend a time-boxed trial/spike before committing.
- **Choosing among several?** Feed this into [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Common mistakes
- **Hype-driven choice** — picking the trendy tool, not the fitting one.
- **Evaluating features, not fit** to actual requirements.
- **Ignoring maturity** — adopting something that may be abandoned.
- **Sticker price only** — missing integration/skills/operational TCO.
- **Ignoring lock-in and exit cost.**
- **Deciding from docs alone** — no hands-on trial.

## Validation checklist
- [ ] Need and must-have requirements defined.
- [ ] Capability assessed against requirements (not a generic feature list).
- [ ] Maturity, adoption, roadmap, and longevity evaluated.
- [ ] Ecosystem (docs, community, support, talent) assessed.
- [ ] TCO and risks (lock-in, security, skills) estimated.
- [ ] Recommendation (adopt/trial/avoid) with conditions and evidence.

## Edge cases
- **Bleeding-edge tech:** high capability, high risk — recommend contained trial, not production bet.
- **Vendor/proprietary:** weight lock-in, pricing trajectory, and exit cost.
- **Open source:** check governance, maintenance health, and license fit.
- **Strong internal preference/politics:** anchor the decision to requirements and evidence.

## Related skills
- [building-decision-matrices](../../business/building-decision-matrices/SKILL.md), [analyzing-cost-benefit](../../business/analyzing-cost-benefit/SKILL.md), [conducting-comparative-research](../conducting-comparative-research/SKILL.md).
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [assessing-source-credibility](../assessing-source-credibility/SKILL.md).

## Examples
**Input:** "Should we adopt this new vector database for our RAG system?"
**Output:** Requirements defined (scale, latency, filtering, ops); capability fit
assessed against them; maturity check (age, adoption, funding, release cadence —
flagged as early); ecosystem (docs decent, small talent pool); TCO incl. self-host
ops and migration; risks (abandonment, lock-in). Recommendation: time-boxed trial
against a proven alternative before committing, with the go/no-go criteria named.

## Automation opportunities
- Maintain an evaluation rubric per technology category for consistency.
- Feed the assessment into a decision matrix when comparing multiple options.
