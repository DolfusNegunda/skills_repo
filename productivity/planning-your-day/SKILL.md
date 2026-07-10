---
name: planning-your-day
description: Plan a day or week that fits reality — pick the few most important tasks, time-block the calendar, protect focus time, and leave buffer for the unexpected. Use when the user says "plan my day", "plan my week", "help me structure tomorrow", "I have too much to do", or wants a realistic schedule instead of an overloaded to-do list.
---

# Planning Your Day

## Scope
Turning a pile of commitments into a realistic schedule for a single day or week:
choosing the vital few tasks, placing them on the calendar as time blocks,
protecting focus time, and reserving buffer. Not project or backlog planning.

## Purpose
End the day having moved the things that mattered, not just cleared easy items —
by committing to a plan the calendar can actually hold, with slack for surprises.

## When to use this skill
- "Plan my day / plan my week / structure tomorrow."
- The to-do list is longer than the hours available and needs triage into a schedule.
- Recurring overwhelm: everything feels urgent and nothing finishes.

## When NOT to use this skill
- Multi-month project planning → [planning-projects](../../business/planning-projects/SKILL.md).
- Ordering a large backlog by value → [prioritizing-options](../../reasoning/prioritizing-options/SKILL.md).
- Running the ongoing task system itself → [managing-tasks](../managing-tasks/SKILL.md).

## Inputs
- The candidate tasks (from [managing-tasks](../managing-tasks/SKILL.md)), with deadlines and rough sizes.
- Fixed commitments already on the calendar (meetings, appointments).
- Energy pattern (when focus is highest) and hard constraints (school run, hours).

## Outputs
- A time-blocked calendar for the day/week: 1–3 priorities placed first, then the rest.
- At least one protected focus block and explicit buffer time.
- A short "if the day derails" fallback: what still ships no matter what.

## Workflow
```
Progress:
- [ ] 1. List candidate tasks and today's fixed commitments
- [ ] 2. Pick the 1-3 that matter most; mark one as "must ship"
- [ ] 3. Estimate each block's real duration (round up)
- [ ] 4. Place priorities in peak-energy slots; then fit the rest
- [ ] 5. Add buffer and a protected focus block; check it fits the hours
- [ ] 6. Set the fallback: what ships even if the day derails
```

**Step 1 — Gather.** Pull candidate tasks from the trusted list and the fixed
calendar. Do not plan against memory; see [managing-tasks](../managing-tasks/SKILL.md).

**Step 2 — Choose the vital few.** Select 1–3 outcomes that make the day a success;
name one "must ship." If prioritizing is hard, use [prioritizing-options](../../reasoning/prioritizing-options/SKILL.md).

**Step 3 — Size honestly.** Estimate each task's real duration and round up — most
plans fail on optimism, not effort. Split anything over ~90 min with [breaking-down-tasks](../breaking-down-tasks/SKILL.md).

**Step 4 — Block.** Put priorities in your peak-energy hours as calendar blocks,
before meetings colonize the day. Batch shallow work (email, admin) into one slot.

**Step 5 — Buffer.** Leave 20–30% of the day unscheduled and add one protected
focus block. If it no longer fits, cut tasks — do not shrink the buffer.

**Step 6 — Fallback.** Decide what still ships if the day derails, so a bad morning
does not sink the whole plan.

## Principles
1. **Priorities before the calendar fills** — place what matters first, not last.
2. **Plan to ~70% capacity** — the unplanned 30% absorbs reality.
3. **Time blocks, not just a list** — a task without a slot rarely happens.
4. **Match hard work to peak energy;** batch shallow work to the trough.
5. **Fewer, finished beats many, started.**
6. **A plan is a hypothesis** — re-plan when it breaks, don't abandon it.

## Decision framework
- **More must-dos than hours?** Cut or move, don't compress the buffer away.
- **Day already full of meetings?** Protect one focus block; decline or shorten the rest ([managing-time](../managing-time/SKILL.md)).
- **Task too big to place?** Break it down ([breaking-down-tasks](../breaking-down-tasks/SKILL.md)).
- **Can't pick top 3?** Ask which one, if done, makes the rest easier or moot.
- **Recurring overrun?** Your estimates are low — track actuals and adjust.

## Common mistakes
- **Overpacking the day with zero buffer** — one delay collapses everything.
- **A flat to-do list with no time blocks** — no slot, no reality check.
- **Scheduling deep work into low-energy afternoons.**
- **Back-to-back meetings that leave no focus time.**
- **Optimistic estimates** repeated daily without ever learning from actuals.
- **Re-choosing priorities all day** instead of committing to the morning's plan.

## Validation checklist
- [ ] 1–3 priorities chosen; one marked "must ship."
- [ ] Every priority has a calendar block in an appropriate energy slot.
- [ ] At least one protected focus block exists.
- [ ] 20–30% of the day is left as buffer.
- [ ] Total blocked time ≤ available hours (no overpacking).
- [ ] A fallback names what ships if the day derails.

## Edge cases
- **Reactive/on-call day:** block one priority early; treat the rest as buffer.
- **Weekly plan:** set 3–5 weekly outcomes, then time-block only 1–2 days ahead.
- **Interrupt-heavy role:** shorten blocks, widen buffer, batch responses.
- **Low-energy day:** keep only the must-ship; defer the rest deliberately.

## Related skills
- [managing-tasks](../managing-tasks/SKILL.md) — the list this plan draws from.
- [managing-time](../managing-time/SKILL.md) — protecting the focus blocks you schedule.
- [breaking-down-tasks](../breaking-down-tasks/SKILL.md), [setting-and-tracking-goals](../setting-and-tracking-goals/SKILL.md).
- [prioritizing-options](../../reasoning/prioritizing-options/SKILL.md), [planning-projects](../../business/planning-projects/SKILL.md).

## Examples
**Input:** "Plan my day — I have 11 things to do and 3 meetings."
**Output:** Chose 3 priorities (must-ship: send the client proposal). Sized them at
90/60/45 min, rounded up. Blocked the proposal 9–10:30 (peak focus) before the 11:00
meeting; batched the 6 small items into a 2–3pm admin slot; left 3:30–5 as buffer.
Fallback: if meetings run over, the proposal still ships. The other 5 items rolled
to tomorrow's list, not crammed in.

## Automation opportunities
- Template a daily block layout (focus / meetings / admin / buffer) in the calendar.
- Auto-pull today's tasks from the task manager into a morning planning view.
- Recurring calendar holds for peak-energy focus blocks so they default to protected.
