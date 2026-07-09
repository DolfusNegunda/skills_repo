---
name: maintaining-risk-registers
description: Build and maintain a risk register — identifying risks, scoring likelihood and impact, assigning owners, and defining mitigation and contingency responses. Use when the user asks to "create a risk register", "do a risk assessment", "identify project risks", or track and manage risks. Produces a scored, owned, actionable register with response strategies, not a static list of worries. Pairs with planning-projects and reviewing-business-cases.
---

# Maintaining Risk Registers

## Scope
Systematic risk management: identifying risks, scoring them by likelihood × impact,
assigning owners, and defining responses (avoid/reduce/transfer/accept) plus
contingency. A living register, not a one-off list.

## Purpose
Turn vague worries into a prioritized, owned, actionable register so the risks that
matter get managed before they become issues — and so contingency exists for those
that can't be prevented.

## When to use this skill
- "Create a risk register / do a risk assessment / identify risks."
- Tracking and managing risks on a project, program, or operation.
- A risk section for a plan or business case.

## When NOT to use this skill
- Justifying an investment → [writing-business-cases](../writing-business-cases/SKILL.md).
- Planning the whole project → [planning-projects](../planning-projects/SKILL.md).
- Reviewing a case's risk treatment → [reviewing-business-cases](../../review/reviewing-business-cases/SKILL.md).

## Inputs
- The initiative/context and its objectives (what the risks threaten).
- Known concerns, history from similar efforts, and stakeholder input.

## Outputs
- A risk register: each risk described as cause→event→effect, scored (likelihood,
  impact, rating), with owner, response strategy, mitigation actions, and contingency.

## Workflow
```
Progress:
- [ ] 1. Identify risks (brainstorm, checklists, past projects, stakeholders)
- [ ] 2. Describe each as cause -> event -> effect
- [ ] 3. Score likelihood and impact; compute a rating
- [ ] 4. Prioritize (risk matrix); focus on high ratings
- [ ] 5. Assign an owner and a response strategy per risk
- [ ] 6. Define mitigation + contingency; set review cadence
```

**Step 2 — describe risks properly.** "The vendor" is not a risk. "Because the
vendor is single-source (cause), they may miss the deadline (event), delaying launch
(effect)" is. This makes likelihood, impact, and mitigation assessable.

**Step 3–4 — score and prioritize.** Likelihood × impact (e.g. 1–5 each) gives a
rating; a matrix separates the critical few from the trivial many. **Step 5 — every
risk has one owner** and a strategy: **avoid** (remove the cause), **reduce**
(lower likelihood/impact), **transfer** (insure/contract), or **accept** (with
contingency). **Step 6 — it's living;** review and re-score on a cadence.

## Principles
1. **Cause → event → effect.** A well-formed risk is assessable and mitigable.
2. **Score to prioritize.** Manage the high ratings, not every worry equally.
3. **Every risk has an owner.** Unowned risks aren't managed.
4. **A response per risk** (avoid/reduce/transfer/accept) — plus contingency.
5. **Living register.** Re-assess regularly; risks and scores change.

## Decision framework
- **High likelihood + high impact?** Avoid or reduce aggressively; escalate.
- **Low likelihood + high impact?** Contingency plan + transfer (insurance).
- **High likelihood + low impact?** Reduce or accept with monitoring.
- **Low + low?** Accept and monitor.
- **Can't mitigate cost-effectively?** Accept explicitly, with contingency and a trigger.

## Common mistakes
- **Risks stated as vague nouns** ("budget", "resources") not cause→event→effect.
- **No scoring** — can't prioritize; everything or nothing gets attention.
- **No owner** — the register is a list nobody acts on.
- **Identify-once and forget** — never re-reviewed.
- **Confusing risks (may happen) with issues (already happening).**
- **Mitigation with no contingency** for when it fails.

## Validation checklist
- [ ] Risks described as cause → event → effect.
- [ ] Each scored for likelihood and impact with a rating.
- [ ] Prioritized via a matrix; focus on the top risks.
- [ ] Each has a named owner and a response strategy.
- [ ] Mitigation actions and contingency defined; triggers set.
- [ ] Review cadence established; issues tracked separately.

## Edge cases
- **Opportunities (positive risk):** register and pursue (exploit/enhance), not only threats.
- **Interdependent risks:** note where one triggers another (cascades).
- **Black-swan/low-probability-catastrophic:** contingency and early-warning triggers matter most.
- **Risk appetite:** align accept/mitigate decisions with the organization's tolerance.

## Related skills
- [planning-projects](../planning-projects/SKILL.md), [writing-business-cases](../writing-business-cases/SKILL.md).
- [reviewing-business-cases](../../review/reviewing-business-cases/SKILL.md), [managing-change](../managing-change/SKILL.md).

## Examples
**Input:** "Risk register for our data-center migration."
**Output:** Register with risks as cause→event→effect (e.g. "legacy app
undocumented → migration breaks it → outage"), each scored (that one L4×I5=20,
critical), owned, with strategy (reduce: pre-migration discovery + parallel run) and
contingency (rollback plan + trigger), reviewed weekly; issues tracked separately.

## Templates
- [templates/risk-register.md](templates/risk-register.md) — scored register with response columns.

## Automation opportunities
- Auto-sort by rating and flag top risks for the status report.
- Alert owners when a review is due or a trigger condition is met.
