---
name: breaking-down-tasks
description: Turn a big, vague, or intimidating task into a short sequence of small, concrete, doable steps with an obvious first action. Use when a task feels too large to start, a to-do reads as a fuzzy outcome instead of an action, work stalls because the next move is unclear, or a plan needs its next physical actions spelled out. Not for MECE analytical decomposition or multi-workstream project planning.
---

# Breaking Down Tasks

## Scope
Converting one big or fuzzy task into an ordered list of small, concrete steps
where the first action is unambiguous and startable now. Operates at the level of a
single task or deliverable, not a whole project or an abstract problem.

## Purpose
Kill the "where do I even start" stall. Reduce a task until each step is a plain
physical action that fits one sitting, so momentum comes from doing rather than
deciding.

## When to use this skill
- A task feels too big, vague, or intimidating to begin.
- A to-do names an outcome ("launch site") but no action.
- Work has stalled because the next move is unclear.
- Handing off or scheduling work that needs concrete next actions.

## When NOT to use this skill
- Analytical decomposition into MECE parts → [decomposing-problems](../../reasoning/decomposing-problems/SKILL.md).
- Multi-workstream project planning with owners and timelines → [planning-projects](../../business/planning-projects/SKILL.md).
- Ongoing prioritization of an existing list → [managing-tasks](../managing-tasks/SKILL.md).

## Inputs
- The task and its desired outcome (what "done" looks like).
- Any known deadline, dependencies, or constraints.
- Whatever is already known vs. still unknown about how to do it.

## Outputs
- An ordered list of 3–7 right-sized steps, each a concrete action.
- A named, startable first action.
- Flags on unknowns, dependencies, and per-step done-checks.

## Workflow
```
Progress:
- [ ] 1. State the outcome in one sentence (the done condition)
- [ ] 2. Brain-dump every piece the task involves, unordered
- [ ] 3. Chunk and sequence into 3–7 steps by dependency
- [ ] 4. Right-size: split any step bigger than one sitting
- [ ] 5. Define the first action as a concrete physical next step
- [ ] 6. Flag unknowns, dependencies, and a done-check per step
```

**Step 1 — Outcome.** Write what "done" looks like in one sentence. If that is
hard, the task is under-defined — resolve the ambiguity before decomposing.

**Step 2 — Brain-dump.** List everything the task touches without ordering or
judging. Getting it out of your head beats getting it right the first pass.

**Step 3 — Chunk and sequence.** Group the dump into a handful of steps and order
them by what must happen before what. Aim for 3–7; more means it is really a project.

**Step 4 — Right-size.** Split any step that won't fit one focused session or whose
action is unclear. Each step should start with a verb you could act on today.

**Step 5 — First action.** Make step 1 a concrete physical action ("open the repo
and create the branch"), not a category ("set up"). This is the whole point.

**Step 6 — Flag.** Mark steps that depend on others or on unknowns; add a one-line
done-check so each step has a clear finish. Route unknowns to a research spike.

## Principles
1. **An obvious first action** is the deliverable — vagueness is the enemy.
2. **One sitting per step** — if it needs a break to finish, split it.
3. **Verbs, not nouns** — "draft the email," not "email."
4. **Sequence by dependency,** not by importance or mood.
5. **Good enough to start** beats a perfect plan that delays action.
6. **Externalize** — a written list frees working memory for the work.

## Decision framework
- **Can't state the outcome?** It's under-specified — clarify before breaking down.
- **More than ~7 steps or multiple owners?** It's a project → [planning-projects](../../business/planning-projects/SKILL.md).
- **A step feels heavy or you avoid it?** It's too big — split again.
- **Blocked by an unknown?** Make the next step "find out X," not the blocked work.
- **Need to understand the problem, not just do it?** → [decomposing-problems](../../reasoning/decomposing-problems/SKILL.md).

## Common mistakes
- **First step too big or undefined** — "start the report" instead of "open the doc and write the heading."
- **Naming outcomes as steps** — "working login" is a goal, not an action.
- **Over-planning** — 30 micro-steps for a two-hour task; plan enough to start.
- **Ignoring dependencies** — steps that can't run in the listed order.
- **No done-check** — steps with no clear finish drift.
- **Planning instead of doing** — refining the list to avoid starting.

## Validation checklist
- [ ] The outcome is stated in one sentence.
- [ ] Steps are ordered by dependency; 3–7 of them.
- [ ] Each step starts with an action verb and fits one sitting.
- [ ] Step 1 is a concrete physical action startable right now.
- [ ] Unknowns and dependencies are flagged, not buried.
- [ ] Each step has a clear done-check.

## Edge cases
- **Fully unfamiliar task:** make the first steps pure discovery (read, ask, prototype).
- **Recurring task:** capture the breakdown as a reusable checklist/template.
- **Task grows into a project mid-breakdown:** stop and switch to [planning-projects](../../business/planning-projects/SKILL.md).
- **Emotionally daunting task:** shrink step 1 until starting feels trivial (two-minute rule).

## Related skills
- [managing-tasks](../managing-tasks/SKILL.md), [planning-your-day](../planning-your-day/SKILL.md), [managing-time](../managing-time/SKILL.md).
- [decomposing-problems](../../reasoning/decomposing-problems/SKILL.md), [planning-projects](../../business/planning-projects/SKILL.md).

## Examples
**Input:** "I need to write the quarterly report — no idea where to start."
**Output:** Outcome: a 4-page report sent to the team by Friday. Steps: (1) open the
doc and paste last quarter's outline, (2) pull the three metrics from the dashboard,
(3) draft each section as bullets, (4) write the summary, (5) proofread and send.
First action: "open the doc and paste the old outline." Unknown flagged: metric #3
source — step 0 is "ask Dana where the churn number lives."

## Automation opportunities
- Save recurring breakdowns as checklist templates in your task manager.
- Use a task tool that supports subtasks so steps live under the parent.
- Prompt an assistant to draft a first-pass breakdown, then right-size it yourself.
