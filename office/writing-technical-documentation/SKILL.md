---
name: writing-technical-documentation
description: Write clear technical documentation — READMEs, how-to guides, tutorials, API/reference docs, runbooks, and architecture docs — organized by the reader's goal and kept accurate against the system. Use when the user asks to "write documentation", "document this API/system/process", "write a README/runbook/how-to guide", or improve existing docs. Applies the Diátaxis model (tutorial/how-to/reference/explanation). Produces task-oriented, testable documentation.
---

# Writing Technical Documentation

## Scope
Documentation of software, systems, and technical processes, chosen and structured
by the reader's need: tutorials, how-to guides, reference, and explanation
(Diátaxis), plus READMEs and runbooks. Not general prose ([writing-business-prose](../writing-business-prose/SKILL.md))
or user-facing reports ([writing-reports](../writing-reports/SKILL.md)).

## Purpose
Let a reader accomplish a specific goal — learn, do a task, look something up, or
understand a design — without asking a human, and keep the doc accurate as the
system changes.

## When to use this skill
- "Write documentation / a README / how-to / tutorial / runbook / architecture doc."
- "Document this API / system / process / configuration."
- Improving docs that are outdated, disorganized, or unusable.

## When NOT to use this skill
- Business prose/memos → [writing-business-prose](../writing-business-prose/SKILL.md).
- ADRs specifically → capture with [../../writing-change-notes](../writing-change-notes/SKILL.md) or an architecture skill.
- Policy documents → [writing-policies](../writing-policies/SKILL.md).

## Inputs
- The system/API/process being documented and access to see how it actually works.
- The reader (new user? operator? integrator?) and their goal.
- Which doc type is needed; existing docs to update.

## Outputs
- Documentation of the right Diátaxis type, task-oriented, with tested commands/
  examples, clear prerequisites, and a maintenance note (owner, last-verified).

## Workflow
```
Progress:
- [ ] 1. Identify the reader and their specific goal
- [ ] 2. Pick the doc type (tutorial / how-to / reference / explanation)
- [ ] 3. Structure by task/goal, not by system internals
- [ ] 4. Write with tested, copy-pasteable examples
- [ ] 5. Add prerequisites, expected output, and troubleshooting
- [ ] 6. Verify every command/step actually works
- [ ] 7. Add ownership + last-verified date
```

**Step 1 — Reader & goal.** "New developer wants to make a first API call" needs a
different doc than "operator restoring a failed service." Name it.

**Step 2 — Doc type (Diátaxis).** **Tutorial** = learning by guided doing (for
newcomers). **How-to** = steps to achieve a specific goal (for someone who knows the
domain). **Reference** = dry, complete, lookup-oriented (API/config). **Explanation**
= the why, concepts, trade-offs. Don't mix them in one document.

**Step 3 — Structure by goal.** Organize around what the reader is trying to do, not
around the code's module layout. Headings should be tasks/questions.

**Step 4 — Tested examples.** Every command, code block, and config must be
copy-pasteable and *actually run*. Show expected output. Untested examples are the
top reason docs lose trust.

**Step 5 — Context.** State prerequisites up front, show expected results, and add a
troubleshooting section for common failures.

**Step 6 — Verify.** Run every step end-to-end as a fresh reader would. If you can't
run it, mark it explicitly as unverified.

**Step 7 — Maintenance.** Docs rot. Record an owner and a last-verified date, and
keep docs near the code so they change together.

## Principles
1. **One doc, one type.** Tutorials, how-tos, reference, and explanation are separate.
2. **Task-oriented.** Structure around the reader's goal, not the system's structure.
3. **Tested examples only.** If it isn't verified, say so.
4. **Show, don't just tell.** Concrete commands + expected output beat description.
5. **Documentation rots** — assign ownership and a verification date.

## Decision framework
- **Reader learning from zero?** Tutorial.
- **Reader has a specific task?** How-to.
- **Reader needs to look up a parameter?** Reference.
- **Reader asks "why is it like this?"** Explanation.
- **New repo/project?** README that routes to the above.

## Common mistakes
- **Mixing types** — a "tutorial" that's really scattered reference the newcomer can't follow.
- **Untested commands** that fail on a clean machine.
- **Assuming context** the reader lacks; no prerequisites.
- **Documenting the code structure** instead of the reader's task.
- **No troubleshooting** for the predictable failure modes.
- **Stale docs** with no owner or date, silently wrong.

## Validation checklist
- [ ] Reader and goal named; doc type chosen and not mixed.
- [ ] Structured by task/goal; headings are tasks or questions.
- [ ] Every command/example tested and shows expected output.
- [ ] Prerequisites stated up front.
- [ ] Troubleshooting covers common failures.
- [ ] Owner and last-verified date present.
- [ ] Links and cross-references resolve.

## Edge cases
- **Fast-changing systems:** generate reference from source (docstrings/OpenAPI) so it stays current.
- **Multiple audiences:** separate docs per audience, linked from a hub, not one doc for all.
- **Legacy/undocumented systems:** document observed behavior; flag assumptions.
- **Runbooks:** must be executable under stress — exact commands, no ambiguity, decision points explicit.

## Related skills
- [writing-business-prose](../writing-business-prose/SKILL.md) — clarity base.
- [writing-reports](../writing-reports/SKILL.md), [writing-policies](../writing-policies/SKILL.md).
- [../../writing-change-notes](../writing-change-notes/SKILL.md) — release notes and change records.

## Examples
**Input:** "Write a README for our internal data-ingest service."
**Output:** README with a one-line what/why, prerequisites, a tested quickstart
(clone → configure → run → expected output), a "common tasks" how-to section, a
link to reference config, a troubleshooting table, and an owner + last-verified date.

## Templates
- [templates/readme-template.md](templates/readme-template.md) — a project README skeleton.

## Automation opportunities
- Generate reference docs from code (OpenAPI, docstrings) to prevent drift.
- CI check that documented commands still run (doctest-style).
- Templatize README/runbook structure across all repos.
