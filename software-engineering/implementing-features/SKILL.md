---
name: implementing-features
description: Turn a requirement or ticket into working, tested code — clarify intent, plan the change, implement in small verifiable steps, add tests, and self-review before handing off. Use when the user says "implement this feature", "build this ticket", "add support for X", "make it do Y", or hands over a spec/story to code up.
---

# Implementing Features

## Scope
Taking a defined requirement to merged, tested code: clarifying intent, planning
the smallest correct change, building it incrementally with tests, and
self-reviewing before handoff. Assumes the code lives in a real repo with existing
conventions to honor.

## Purpose
Ship a change that does exactly what was asked, fits the codebase, and is proven to
work — without scope creep, broken neighbors, or a reviewer catching what you should
have.

## When to use this skill
- "Implement / build / add / wire up this feature or ticket."
- A story, spec, or acceptance criteria handed over to code.
- Extending existing behavior with new functionality.

## When NOT to use this skill
- Pure design decisions (API shape, contracts) → [designing-apis](../designing-apis/SKILL.md).
- Fixing a defect in existing behavior → [debugging-systematically](../debugging-systematically/SKILL.md).
- Reviewing code someone else wrote → [reviewing-code](../../review/reviewing-code/SKILL.md).
- The requirement itself is unclear or contested → [gathering-requirements](../../business/gathering-requirements/SKILL.md).

## Inputs
- The requirement/ticket and its acceptance criteria; the definition of done.
- The target repo: build/test commands, conventions, and the area to change.
- Constraints: compatibility, deadlines, non-functional needs (perf, security).

## Outputs
- A working change matching the acceptance criteria, in small reviewable commits.
- Tests that prove the new behavior and guard against regression.
- A short handoff note: what changed, why, how it was verified, what's out of scope.

## Workflow
```
Progress:
- [ ] 1. Clarify the requirement and acceptance criteria; note the definition of done
- [ ] 2. Locate the change site; learn build/test/run commands and conventions
- [ ] 3. Plan the smallest correct change; list the steps and test points
- [ ] 4. Implement one thin slice; keep it compiling/green throughout
- [ ] 5. Add tests for behavior + edges; run the full suite
- [ ] 6. Self-review the diff; write the handoff note
```

**Step 1 — Clarify.** Restate the requirement in one sentence and list concrete
acceptance criteria. Surface ambiguity now (empty states, limits, permissions,
error paths) rather than guessing — one question up front beats a rewrite.

**Step 2 — Locate.** Find where the change belongs and confirm how to build, test,
and run it *before* editing. Read the neighbors to absorb conventions. If the area
is unfamiliar, use [reading-unfamiliar-codebases](../reading-unfamiliar-codebases/SKILL.md).

**Step 3 — Plan.** Choose the smallest change that satisfies the criteria and fits
existing patterns. Break it into slices that each keep the build green. Decide test
points per slice before writing code.

**Step 4 — Implement.** Build one slice at a time. Keep it compiling and tests
passing after every slice — never a big-bang commit. Match surrounding style; don't
reformat unrelated code.

**Step 5 — Test.** Cover the happy path plus edges and failure modes from Step 1.
Run the *whole* suite, not just your new tests. See [writing-automated-tests](../writing-automated-tests/SKILL.md).

**Step 6 — Self-review.** Read your own diff as a hostile reviewer would; write the
handoff note. See [reviewing-code](../../review/reviewing-code/SKILL.md).

## Principles
1. **Smallest change that's correct** — fit the codebase, don't reinvent it.
2. **Always green** — the tree compiles and tests pass at every commit boundary.
3. **Match the requirement exactly** — no more (scope creep), no less (silent gaps).
4. **Tests are part of done,** not a follow-up ticket.
5. **Follow local convention** over personal preference.
6. **Make the diff easy to review** — small, focused, self-explaining.

## Decision framework
- **Requirement ambiguous?** Ask before coding; don't encode a guess.
- **Change touches unfamiliar code?** Trace it first; borrow the existing pattern.
- **Tempted to refactor while you're in there?** Split it out — separate commit or ticket ([refactoring-code](../refactoring-code/SKILL.md)).
- **Slice getting big?** Cut it thinner; land a smaller correct piece.
- **New dependency needed?** Justify it first ([managing-dependencies](../managing-dependencies/SKILL.md)).

## Common mistakes
- **Coding before understanding** the acceptance criteria or the surrounding code.
- **Scope creep** — gold-plating or bundling unrelated refactors.
- **Big-bang commits** that can't be reviewed or bisected.
- **Testing only the happy path;** skipping error and edge cases.
- **Running only new tests,** missing regressions elsewhere.
- **Ignoring conventions** — new patterns where the repo already has one.

## Validation checklist
- [ ] Every acceptance criterion is met and demonstrably exercised.
- [ ] Edge cases and error paths handled, not just the happy path.
- [ ] Full test suite runs green; new tests fail without the change.
- [ ] Diff is minimal and focused; no unrelated churn.
- [ ] Matches repo conventions (naming, structure, error handling, logging).
- [ ] No secrets, debug prints, or commented-out code left behind.
- [ ] Handoff note states what/why/how-verified and what's out of scope.

## Edge cases
- **Under-specified requirement:** stop and clarify; document assumptions you had to make.
- **Cross-cutting change (many files):** land a scaffold slice first, then fill in.
- **Feature behind rollout risk:** gate behind a flag; keep the old path until proven.
- **Public API or contract change:** version/deprecate rather than break ([designing-apis](../designing-apis/SKILL.md)).

## Related skills
- [reading-unfamiliar-codebases](../reading-unfamiliar-codebases/SKILL.md), [writing-automated-tests](../writing-automated-tests/SKILL.md), [refactoring-code](../refactoring-code/SKILL.md).
- [debugging-systematically](../debugging-systematically/SKILL.md), [using-git-workflows](../using-git-workflows/SKILL.md), [reviewing-code](../../review/reviewing-code/SKILL.md).
- [gathering-requirements](../../business/gathering-requirements/SKILL.md), [designing-apis](../designing-apis/SKILL.md).

## Examples
**Input:** "Add a 'remember me' option to the login form."
**Output:** Clarified: extend session to 30 days when checked; default off; respect
existing logout. Located auth handler + session config. Plan: (1) add checkbox +
form field, (2) plumb flag to session creation, (3) set longer TTL when set. Built
in three green slices; added tests for checked/unchecked and logout-clears-session;
ran full suite. Diff touches only auth path. Handoff note: behavior, TTL choice,
out of scope (no "remember device" UI).

## Automation opportunities
- Run the linter, type checker, and test suite locally before every commit.
- Wire acceptance criteria to automated tests so "done" is machine-checkable.
- Use a PR template that prompts for what/why/how-verified/out-of-scope.
