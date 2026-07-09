---
name: gathering-requirements
description: Elicit, structure, and document clear, testable requirements from stakeholders — using interviews, workshops, and the right requirement types (functional, non-functional, user stories) with acceptance criteria. Use when the user asks to "gather/elicit requirements", "write requirements/user stories", "capture what the business needs", or turn stakeholder input into a spec. Produces structured, prioritized, testable requirements ready to build against. Review them with reviewing-requirements.
---

# Gathering Requirements

## Scope
Eliciting what stakeholders actually need and turning it into structured, testable
requirements. Covers elicitation technique, requirement types, and documentation.
Reviewing requirements for quality is
[reviewing-requirements](../../review/reviewing-requirements/SKILL.md).

## Purpose
Capture the real need — not the first-stated solution — as unambiguous, prioritized,
testable requirements that a team can build and verify.

## When to use this skill
- "Gather / elicit / capture requirements or user stories."
- Turning stakeholder conversations into a spec.
- Discovery for a project, product, or system change.

## When NOT to use this skill
- Framing the underlying problem → [performing-business-analysis](../performing-business-analysis/SKILL.md).
- Quality-checking existing requirements → [reviewing-requirements](../../review/reviewing-requirements/SKILL.md).
- Process detail → [mapping-processes](../mapping-processes/SKILL.md).

## Inputs
- The business goal/problem, stakeholders and users, and any constraints.
- Existing systems/processes and known assumptions.

## Outputs
- Structured requirements: functional + non-functional (or user stories with
  acceptance criteria), prioritized (e.g. MoSCoW), traceable to goals.

## Workflow
```
Progress:
- [ ] 1. Identify stakeholders and what each can tell you
- [ ] 2. Elicit with the right technique (interview, workshop, observation)
- [ ] 3. Separate needs from stated solutions
- [ ] 4. Write requirements: clear, atomic, testable
- [ ] 5. Classify (functional/non-functional) and prioritize (MoSCoW)
- [ ] 6. Validate back with stakeholders; trace to goals
```

**Step 2 — technique fits the situation:** interviews for depth, workshops for
shared understanding and conflict resolution, observation for how work really
happens (vs. how people describe it), document analysis for existing rules.

**Step 3 — need vs. solution.** Stakeholders ask for solutions ("add a dropdown");
dig for the underlying need ("select from valid values quickly"). Requirements
capture the need. **Ask about non-functional needs explicitly** — they're rarely
volunteered but often decisive.

**Step 6 — validate.** Play requirements back; unconfirmed requirements are
assumptions.

## Principles
1. **Capture needs, not solutions.**
2. **Every requirement is testable** — you can prove it's met.
3. **Elicit non-functional requirements deliberately;** users won't offer them.
4. **Prioritize** — not everything is a must-have (MoSCoW).
5. **Trace to goals and validate with stakeholders.**

## Decision framework
- **Deep individual knowledge?** Interview. **Shared/conflicting views?** Workshop.
- **"How it really works"?** Observe. **Rules/regulations?** Document analysis.
- **Agile context?** User stories + acceptance criteria (INVEST).
- **Formal/regulated?** Structured functional + non-functional spec with IDs.

## Common mistakes
- **Recording solutions as requirements.**
- **Missing non-functional requirements** (performance, security, compliance).
- **Vague, untestable statements** ("must be user-friendly").
- **No prioritization** — everything "critical".
- **Skipping validation** — assumptions masquerading as requirements.
- **Consulting too narrow a stakeholder set** — missed needs surface late.

## Validation checklist
- [ ] Right stakeholders consulted with fit-for-purpose techniques.
- [ ] Needs separated from proposed solutions.
- [ ] Requirements atomic, clear, and testable.
- [ ] Functional and non-functional both captured.
- [ ] Prioritized (MoSCoW) and traced to goals.
- [ ] Validated back with stakeholders.

## Edge cases
- **Conflicting stakeholder needs:** surface and resolve in a workshop; document the decision.
- **Unavailable stakeholders:** use proxies/documents; flag the gap and confidence.
- **Evolving scope:** manage as change; keep traceability so impact is visible.
- **Regulated domains:** completeness and traceability to obligations are critical.

## Related skills
- [performing-business-analysis](../performing-business-analysis/SKILL.md), [analyzing-stakeholders](../analyzing-stakeholders/SKILL.md), [mapping-processes](../mapping-processes/SKILL.md).
- [reviewing-requirements](../../review/reviewing-requirements/SKILL.md) — quality-gate the output.

## Examples
**Input:** "Capture requirements for a new expense-approval system."
**Output:** Stakeholder-sourced set: functional ("a manager can approve/reject with a
comment"), non-functional ("approvals reflect within 5s; SOX audit trail retained 7
years"), as user stories with acceptance criteria, MoSCoW-prioritized, each traced to
the goal (faster, compliant approvals), validated with finance and managers.

## Automation opportunities
- Turn workshop notes into a first-draft requirement set, then refine.
- Maintain a traceability matrix (requirement → goal → test) automatically.
- Feed straight into [reviewing-requirements](../../review/reviewing-requirements/SKILL.md) as a gate.
