---
name: performing-business-analysis
description: Analyze a business problem or opportunity end to end — frame the real problem, find root causes, model the current and future state, and produce evidence-backed options with a recommendation. Use when the user asks to "analyze this business problem", "figure out what's going wrong", "do a business analysis", or turn a vague concern into a structured case for action. Produces a problem definition, root-cause analysis, and options, not just observations.
---

# Performing Business Analysis

## Scope
The core discipline of business analysis: turning a vague concern into a defined
problem, evidenced root cause, and a set of options with a recommendation. The
front end that feeds requirements, business cases, and process work.

## Purpose
Ensure effort is spent solving the *right* problem: frame it precisely, prove the
cause instead of guessing, and present options rather than a single predetermined answer.

## When to use this skill
- "Analyze this business problem / opportunity."
- "Figure out what's really going wrong / why this isn't working."
- Turning a symptom or complaint into a structured case for action.
- The discovery phase before requirements or a business case.

## When NOT to use this skill
- Eliciting detailed requirements → [gathering-requirements](../gathering-requirements/SKILL.md).
- Mapping a specific process → [mapping-processes](../mapping-processes/SKILL.md).
- Justifying a chosen investment → [writing-business-cases](../writing-business-cases/SKILL.md).

## Inputs
- The presenting symptom/concern and who's raising it.
- Available data, stakeholders to consult, and business goals/constraints.

## Outputs
- A problem definition, root-cause analysis with evidence, current/future-state
  view, and 2–4 options with a reasoned recommendation.

## Workflow
```
Progress:
- [ ] 1. Define the problem — separate symptom from problem
- [ ] 2. Gather evidence (data + stakeholders) on the current state
- [ ] 3. Find root cause (5 Whys / fishbone) — don't stop at symptoms
- [ ] 4. Define the desired future state and success measures
- [ ] 5. Generate options (incl. do-nothing); assess each
- [ ] 6. Recommend, with rationale and risks
```

**Step 1 — problem, not symptom.** "Sales are down" is a symptom. Frame the problem
as a gap between current and desired state, in measurable terms. A wrong frame wastes
everything downstream.

**Step 3 — root cause.** Use 5 Whys or a fishbone (cause-and-effect) diagram to get
past the first plausible cause. Validate causes with evidence, not assertion.

**Step 5 — options including do-nothing.** Always include the baseline; present real
alternatives, not one option dressed up with two strawmen.

## Principles
1. **Solve the right problem.** Frame before analyzing.
2. **Evidence over opinion.** Root causes are proven, not assumed.
3. **Current → future → gap.** Analysis is about closing a defined gap.
4. **Options, not a foregone conclusion,** including do-nothing.
5. **Trace to business goals.** Every problem worth solving ties to an objective.

## Decision framework
- **Recurring/systemic symptom?** Root-cause analysis before any solution.
- **Process-specific?** → [mapping-processes](../mapping-processes/SKILL.md).
- **Ready to justify a solution?** → [writing-business-cases](../writing-business-cases/SKILL.md).
- **Many stakeholders/views?** → [analyzing-stakeholders](../analyzing-stakeholders/SKILL.md) first.

## Common mistakes
- **Jumping to solutions** before defining the problem.
- **Stopping at the first cause** — treating a symptom.
- **Confirmation bias** — gathering only evidence that fits a preferred answer.
- **No baseline/do-nothing option.**
- **Analysis with no decision** — a report that doesn't recommend.

## Validation checklist
- [ ] Problem defined as a measurable gap, distinct from the symptom.
- [ ] Current state evidenced with data and stakeholder input.
- [ ] Root cause identified and validated, not assumed.
- [ ] Future state and success measures defined.
- [ ] Options (incl. do-nothing) assessed; recommendation with rationale + risks.
- [ ] Everything traces to a business goal.

## Edge cases
- **Political problems:** the stated problem may not be the real one — probe carefully.
- **Data-poor environments:** triangulate qualitative evidence; state confidence.
- **Urgent "just fix it" pressure:** a rapid frame + root-cause still beats blind action.

## Related skills
- [gathering-requirements](../gathering-requirements/SKILL.md), [mapping-processes](../mapping-processes/SKILL.md), [analyzing-stakeholders](../analyzing-stakeholders/SKILL.md).
- [writing-business-cases](../writing-business-cases/SKILL.md), [../reasoning](../../office/comparing-documents/SKILL.md).

## Examples
**Input:** "Support tickets are up 40% — analyze it."
**Output:** Problem framed (resolution time gap, not just volume); evidence shows the
spike is concentrated in one feature post-release; 5 Whys traces to a confusing new
flow; future state defined (tickets back to baseline); options: revert, redesign
flow, add in-app help; recommendation: redesign (root cause) + interim help, with risks.

## Automation opportunities
- Pull ticket/data trends automatically to evidence the current state.
- Standardize the problem-definition + options template across analysts.
