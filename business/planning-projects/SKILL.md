---
name: planning-projects
description: Plan a project from a brief — defining scope, objectives, deliverables, milestones, dependencies, resources, RACI, and risks into a charter and plan. Use when the user asks to "plan this project", "create a project plan/charter", "define scope and milestones", or turn an initiative into an executable plan. Produces a clear, realistic plan with accountability and risk built in, not a wishful Gantt chart.
---

# Planning Projects

## Scope
Turning an approved initiative into an executable plan: charter (why/what/who),
scope, milestones, dependencies, resourcing, RACI, and integrated risk. Uses
[maintaining-risk-registers](../maintaining-risk-registers/SKILL.md) and
[analyzing-stakeholders](../analyzing-stakeholders/SKILL.md) as inputs.

## Purpose
Give a team a realistic, accountable plan: everyone knows the goal, the scope
boundaries, who owns what, the critical path, and the risks — so delivery is managed,
not hoped for.

## When to use this skill
- "Plan this project / create a project plan or charter."
- "Define scope, milestones, and responsibilities."
- Kicking off an initiative that needs coordination across people/time.

## When NOT to use this skill
- Longer-term direction → [building-roadmaps](../building-roadmaps/SKILL.md).
- Justifying the project → [writing-business-cases](../writing-business-cases/SKILL.md).
- Detailed requirements → [gathering-requirements](../gathering-requirements/SKILL.md).

## Inputs
- The objective/business case, scope expectations, deadline/budget constraints.
- Available people/skills, dependencies, and known risks.

## Outputs
- A charter (objectives, scope in/out, success criteria), a milestone plan with
  dependencies, a RACI, resource plan, and a linked risk register.

## Workflow
```
Progress:
- [ ] 1. Charter: objective, success criteria, scope in/out
- [ ] 2. Break work into deliverables and milestones
- [ ] 3. Sequence: dependencies and the critical path
- [ ] 4. Assign accountability (RACI) and resources
- [ ] 5. Build in risks and contingency
- [ ] 6. Set governance: cadence, reporting, change control
```

**Step 1 — scope in AND out.** Explicit out-of-scope prevents the scope creep that
kills projects. Define measurable success criteria, not just activities.

**Step 3 — critical path.** Identify which tasks, if late, delay the whole project;
that's where attention and buffer go. **Step 4 — one Accountable per deliverable**
(RACI); shared accountability is no accountability. **Step 5 — plan for risk** with
realistic contingency, not a plan that assumes everything goes right.

## Principles
1. **Define scope boundaries** (in and out) explicitly.
2. **Measurable success criteria,** not a list of activities.
3. **One Accountable owner** per deliverable.
4. **Manage the critical path** and its dependencies.
5. **Realistic estimates + contingency** — hope is not a schedule.

## Decision framework
- **Uncertain/evolving work?** Plan in phases/iterations, not one big waterfall.
- **Fixed deadline?** Scope becomes the variable — prioritize (MoSCoW).
- **Many dependencies?** Emphasize the critical path and buffer.
- **High risk?** Heavier risk register + go/no-go gates.

## Common mistakes
- **No out-of-scope statement** — invites creep.
- **Activities instead of deliverables/outcomes.**
- **Optimistic estimates, no contingency.**
- **Fuzzy accountability** — many responsible, none accountable.
- **Ignoring dependencies/critical path.**
- **No change-control** — every request silently expands scope.

## Validation checklist
- [ ] Charter with objective, measurable success criteria, and scope in/out.
- [ ] Work broken into deliverables and milestones.
- [ ] Dependencies mapped; critical path identified.
- [ ] RACI with a single Accountable per deliverable.
- [ ] Realistic estimates with contingency; risks registered.
- [ ] Governance: reporting cadence and change control defined.

## Edge cases
- **Agile/iterative:** plan outcomes + a groomed backlog; replan each iteration.
- **Fixed scope + fixed date + fixed budget:** flag the impossible triangle; force a trade-off.
- **Cross-team dependencies:** secure commitments explicitly; they're the top delay risk.
- **Long projects:** stage-gate with go/no-go decisions.

## Related skills
- [maintaining-risk-registers](../maintaining-risk-registers/SKILL.md), [analyzing-stakeholders](../analyzing-stakeholders/SKILL.md), [building-roadmaps](../building-roadmaps/SKILL.md).
- [writing-status-reports](../../office/writing-status-reports/SKILL.md) — report progress against the plan.

## Examples
**Input:** "Plan a 12-week website replatform."
**Output:** Charter (goal: migrate with zero SEO loss; out-of-scope: redesign),
milestones (content audit → build → migrate → cutover) with dependencies and a
critical path through content migration, a RACI naming one owner per milestone, a
risk register (SEO regression, content gaps) with mitigations, and a weekly status
cadence with a pre-cutover go/no-go gate.

## Templates
- [templates/project-charter.md](templates/project-charter.md) — charter + milestone + RACI skeleton.

## Automation opportunities
- Generate status reports from the plan via [writing-status-reports](../../office/writing-status-reports/SKILL.md).
- Keep the RACI and risk register as living tables linked to the plan.
