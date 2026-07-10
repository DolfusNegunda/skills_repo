---
name: planning-learning
description: Build a plan to learn a skill or subject — define target proficiency, map prerequisites, choose resources, set milestones, and design practice with feedback loops. Use when the user says "help me learn X", "make a study plan / roadmap for Y", "how do I get good at Z", "what should I learn first", or hands over a subject to structure into a learning path. Produces a milestone-based plan with resources, practice, and checkpoints.
---

# Planning Learning

## Scope
Turning "I want to learn X" into a concrete, milestone-based plan: a defined target
proficiency, mapped prerequisites, chosen resources, spaced milestones, and built-in
practice and feedback. Covers the *curriculum*, not the study techniques used to work
through it ([studying-effectively](../studying-effectively/SKILL.md)).

## Purpose
Replace aimless consumption with a path that reaches a specific, testable level of
skill — sequenced so each milestone unlocks the next, with practice and feedback that
prove progress instead of assuming it.

## When to use this skill
- "Help me learn / get good at X"; "make me a roadmap or study plan."
- A subject or skill that needs sequencing into an ordered path.
- Deciding what to learn first, and which resources are worth the time.

## When NOT to use this skill
- The study/retention techniques themselves → [studying-effectively](../studying-effectively/SKILL.md).
- Evaluating a technology to adopt for work → [evaluating-technology](../../research/evaluating-technology/SKILL.md).
- Setting non-learning goals → [setting-and-tracking-goals](../setting-and-tracking-goals/SKILL.md).
- Scheduling the plan into days/weeks → [managing-time](../managing-time/SKILL.md).

## Inputs
- The subject/skill, the motivation, and the concrete reason to learn it.
- Current level, available time per week, and a target date or deadline.
- Constraints: budget for resources, preferred formats, prior related knowledge.

## Outputs
- A target proficiency stated as observable behavior ("can do X unaided").
- An ordered prerequisite map and a milestone plan with dates.
- A short resource shortlist per milestone, plus defined practice and feedback points.

## Workflow
```
Progress:
- [ ] 1. Define target proficiency as an observable outcome
- [ ] 2. Assess current level and the gap
- [ ] 3. Map prerequisites and order them into a path
- [ ] 4. Choose minimal resources per stage
- [ ] 5. Set spaced milestones with dates
- [ ] 6. Design practice and feedback into every milestone
- [ ] 7. Schedule a review cadence to adjust the plan
```

**Step 1 — Define the target.** State proficiency as something observable and
testable: "build and deploy a small REST API alone," not "know backend." Vague
targets can't be planned toward or checked off.

**Step 2 — Assess the gap.** Honestly locate the current level and name the delta to
the target. This sizes the plan and prevents starting too high or too low.

**Step 3 — Map prerequisites.** List what must be understood before what, and order
into a dependency chain. Cut anything not on the path to the target — scope is where
learning plans bloat.

**Step 4 — Choose resources.** Pick the *fewest* good resources per stage (one
primary, one reference). More sources means more switching cost, not more learning.
Prefer a resource that forces output over one that only explains.

**Step 5 — Set milestones.** Break the path into checkpoints, each a demonstrable
capability with a date. Space them; a plan with no milestones is a wish, not a plan.

**Step 6 — Build in practice + feedback.** Every milestone needs a way to *apply* the
material and a way to *check* it (self-test, project, mentor, community). A plan with
no feedback loop can't detect that it's failing.

**Step 7 — Schedule review.** Set a recurring point to compare progress vs. plan and
re-sequence. Learning plans are estimates; expect to adjust.

## Principles
1. **Target first** — an observable outcome anchors every other decision.
2. **Prerequisites before topics** — order by dependency, not by interest.
3. **Fewest resources that work** — depth over a sprawling reading list.
4. **Milestones are demonstrable** — a capability shown, not hours logged.
5. **Practice is planned, not hoped for** — output points are in the plan.
6. **Feedback closes the loop** — every stage has a way to know it stuck.
7. **The plan is a draft** — review and re-sequence as reality lands.

## Decision framework
- **Target vague?** Rewrite it as "can do X unaided" before planning further.
- **Don't know the prerequisites?** Do a quick landscape pass, or borrow an existing
  roadmap, before committing an order.
- **Too many resources?** Cut to one primary per stage; add others only on a gap.
- **Deadline fixed but scope large?** Narrow the target, not the practice.
- **Milestone has no way to be tested?** It's a topic, not a milestone — add a check.

## Common mistakes
- **A plan with no milestones** — an open-ended reading list that never converges.
- **All input, no output** — resources queued but no practice or projects scheduled.
- **No feedback loop** — no test, project, or reviewer to catch misunderstanding.
- **Skipping prerequisites** — starting at the exciting part and stalling on gaps.
- **Resource hoarding** — collecting courses/books instead of working through one.
- **Vague target** — "learn Python" with no defined finish line to plan toward.
- **Set and forget** — never revisiting the plan as progress diverges.

## Validation checklist
- [ ] Target proficiency is stated as an observable, testable outcome.
- [ ] Current level and gap are named.
- [ ] Prerequisites are mapped and ordered by dependency.
- [ ] Each stage has a minimal resource shortlist, not a pile.
- [ ] Milestones have dates and are demonstrable capabilities.
- [ ] Every milestone includes a practice activity and a feedback check.
- [ ] A review cadence is scheduled to adjust the plan.

## Edge cases
- **Open-ended subject (no clear end):** pick a bounded first target and re-plan after.
- **Fast-moving field:** favor fundamentals and primary sources over dated courses.
- **No mentor available:** substitute community review, tests, or public sharing for feedback.
- **Very limited time:** shrink target scope rather than removing practice or feedback.
- **Skill vs. knowledge:** for skills, weight practice heavily; for knowledge, weight retention ([studying-effectively](../studying-effectively/SKILL.md)).

## Related skills
- [studying-effectively](../studying-effectively/SKILL.md) — the techniques for working through the plan.
- [setting-and-tracking-goals](../setting-and-tracking-goals/SKILL.md), [managing-time](../managing-time/SKILL.md), [breaking-down-tasks](../breaking-down-tasks/SKILL.md).
- [managing-personal-knowledge](../managing-personal-knowledge/SKILL.md), [evaluating-technology](../../research/evaluating-technology/SKILL.md).

## Examples
**Input:** "I want to learn data visualization in about three months, a few hours a week."
**Output:** Target: "build a clear, annotated dashboard from a raw dataset, unaided."
Gap: comfortable with spreadsheets, new to design. Prereqs ordered: data cleaning →
chart-type selection → color/encoding → tools. One primary resource per stage.
Milestones: (M1) recreate three charts by wk 3; (M2) critique + fix a bad chart by
wk 6; (M3) build a dashboard from scratch by wk 12 — each with a practice deliverable
and a feedback source (community critique). Fortnightly review to re-sequence.

## Automation opportunities
- Track milestones and review dates in the task/goal system, not a static doc.
- Set recurring calendar checkpoints for practice sessions and plan reviews.
- Keep a running resource shortlist in personal knowledge notes, pruned each stage.
