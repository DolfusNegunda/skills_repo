---
name: mapping-processes
description: Map business processes as clear, accurate flows — documenting the as-is state, identifying bottlenecks, waste, and hand-off risks, and designing an improved to-be state. Use when the user asks to "map this process", "document our workflow", "create a process/swimlane diagram", "find inefficiencies", or improve how work flows. Uses standard notation (flowchart/BPMN/swimlanes). Produces accurate process maps plus an improvement analysis, not just a diagram.
---

# Mapping Processes

## Scope
Documenting how work actually flows and designing how it should flow — as-is maps,
bottleneck/waste analysis, and to-be redesign, in standard notation (flowchart,
swimlane, BPMN). Feeds requirements, automation, and change work.

## Purpose
Make an invisible process visible and improvable: capture reality accurately, expose
where it breaks down, and design a better flow — not draw a tidy diagram of the ideal
nobody follows.

## When to use this skill
- "Map / document this process or workflow."
- "Create a process / swimlane / BPMN diagram."
- "Find inefficiencies / bottlenecks / where work gets stuck."
- Before automating, redesigning, or handing off a process.

## When NOT to use this skill
- Detailed system requirements → [gathering-requirements](../gathering-requirements/SKILL.md).
- Org decision rights → [establishing-governance](../establishing-governance/SKILL.md).
- Project schedule → [planning-projects](../planning-projects/SKILL.md).

## Inputs
- The process boundaries (start/trigger and end), and access to people who do the work.
- The goal (document, improve, automate, comply) and any metrics (time, volume, error rate).

## Outputs
- An as-is process map (with roles/swimlanes), an analysis of bottlenecks/waste/
  risks, and a to-be map with the changes and their expected benefit.

## Workflow
```
Progress:
- [ ] 1. Define scope: trigger, boundaries, and end state
- [ ] 2. Capture the as-is from the people who actually do it
- [ ] 3. Map with roles/swimlanes and decision points
- [ ] 4. Analyze: bottlenecks, waste, delays, hand-offs, rework loops
- [ ] 5. Design the to-be; quantify the improvement
- [ ] 6. Validate both maps with participants
```

**Step 2 — map reality, not the manual.** Talk to the people doing the work; the
documented process and the actual one usually differ, and the gap is where problems
live. **Step 3 — swimlanes** show who does what and expose risky hand-offs. **Step 4**
— look for the classic wastes: waiting, rework loops, redundant approvals, and
hand-off gaps.

## Principles
1. **As-is before to-be.** You can't improve what you haven't honestly captured.
2. **Map reality,** not the official version.
3. **Hand-offs are where processes fail** — make them explicit with swimlanes.
4. **Quantify the pain** (time, cost, errors) so improvement is measurable.
5. **Validate with participants** — an unvalidated map is a guess.

## Decision framework
- **Simple linear flow?** Flowchart. **Multiple roles/hand-offs?** Swimlanes.
- **Formal/complex/system-integrated?** BPMN.
- **Goal is automation?** Map to-be at the detail an automation needs.
- **Cross-functional pain?** Swimlanes to expose the hand-off failures.

## Common mistakes
- **Mapping the ideal** instead of the real process.
- **Skipping the as-is** and jumping to redesign.
- **Omitting exceptions/rework loops** — the happy path only.
- **No roles** — can't see accountability or hand-off risk.
- **Unquantified improvement** — "better" with no measure.
- **Not validating** with the people who run it.

## Validation checklist
- [ ] Scope (trigger, boundaries, end) defined.
- [ ] As-is captured from actual practitioners, including exceptions.
- [ ] Roles/swimlanes and decision points shown.
- [ ] Bottlenecks, waste, delays, and hand-off risks identified.
- [ ] To-be designed with quantified expected benefit.
- [ ] Both maps validated with participants.

## Edge cases
- **Undocumented tribal processes:** observe and interview; expect variation between people.
- **Highly variable processes:** map the common path + major variants, not every branch.
- **Compliance processes:** capture controls and evidence points explicitly.
- **Pre-automation:** the to-be must be clean enough that you don't automate waste.

## Related skills
- [performing-business-analysis](../performing-business-analysis/SKILL.md), [gathering-requirements](../gathering-requirements/SKILL.md).
- [managing-change](../managing-change/SKILL.md) — to land the to-be process.

## Examples
**Input:** "Map our invoice-approval process — it takes too long."
**Output:** As-is swimlane (requester → manager → finance → AP) showing two
sequential approvals and a manual re-key step; analysis flags 3-day waits at the
manager stage and a rework loop from missing PO numbers; to-be removes the redundant
approval and validates PO at entry, cutting cycle time from 6 days to ~2; both maps
validated with finance.

## Automation opportunities
- A clean to-be map is the spec for workflow automation — don't automate the waste.
- Instrument the process to measure cycle time and validate the improvement.
