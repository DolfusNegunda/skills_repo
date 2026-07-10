---
name: debugging-systematically
description: Find and fix the root cause of a defect by reproducing it reliably, isolating it by bisection, testing one hypothesis at a time, fixing the cause not the symptom, and adding a regression test. Use when the user says "this is broken", "there's a bug", "it crashes/returns the wrong thing", "why is this failing", or hands over a stack trace or failing test.
---

# Debugging Systematically

## Scope
Diagnosing and fixing a defect in existing behavior: from a reliable repro, through
isolation and hypothesis testing, to a root-cause fix guarded by a regression test.
Not building new functionality and not tuning speed.

## Purpose
Fix the actual cause — not a symptom or a coincidence — with evidence at each step,
so the bug stays fixed and you understand why it happened.

## When to use this skill
- "It's broken / crashes / returns the wrong result / is flaky."
- A failing test, stack trace, error log, or bug report handed over.
- Behavior that regressed after a change.

## When NOT to use this skill
- Building new functionality → [implementing-features](../implementing-features/SKILL.md).
- Code is correct but slow → [optimizing-code-performance](../optimizing-code-performance/SKILL.md).
- Improving structure without changing behavior → [refactoring-code](../refactoring-code/SKILL.md).
- Reviewing code for latent bugs before they fire → [reviewing-code](../../review/reviewing-code/SKILL.md).

## Inputs
- The symptom: what's observed vs. expected, with exact inputs/environment.
- Artifacts: stack trace, logs, failing test, recent diffs, repro steps.
- Access to run the code and change it; knowledge of when it last worked.

## Outputs
- A confirmed root-cause diagnosis (what, where, why).
- A minimal fix addressing the cause, plus a regression test that fails without it.
- A short note: cause, fix, blast radius, and how it was verified.

## Workflow
```
Progress:
- [ ] 1. Reproduce reliably; capture exact inputs, environment, and expected vs. actual
- [ ] 2. Write a failing test or minimal repro that pins the bug
- [ ] 3. Isolate — bisect code, data, or history to the smallest failing region
- [ ] 4. Form ONE hypothesis; predict what you'd observe; test it
- [ ] 5. Fix the root cause; confirm the repro now passes and neighbors don't break
- [ ] 6. Keep the regression test; note cause, fix, and blast radius
```

**Step 1 — Reproduce.** A bug you can't reproduce, you can't fix. Nail down exact
inputs, versions, and environment. Intermittent? Find the condition that flips it
(timing, order, data, concurrency) before touching code.

**Step 2 — Pin it.** Turn the repro into an automated failing test or a minimal
script. This becomes your objective pass/fail signal and, later, the regression test.

**Step 3 — Isolate.** Shrink the search space: `git bisect` across history, binary
search in the code path, or minimize the input until it's the smallest thing that
still fails. Read the actual stack trace top-down — don't skim it.

**Step 4 — One hypothesis.** State a single cause, predict a specific observation it
implies, then test *that*. Change one variable at a time. Never shotgun multiple
"fixes" at once — you'll never know which worked or what you broke.

**Step 5 — Fix the cause.** Address why the bug exists, not where it surfaced. A
null check at the crash site that hides an upstream bad value is a symptom patch.
Re-run the pinned test and the full suite.

**Step 6 — Guard it.** Keep the regression test committed. Note the cause and
whether the same class of bug lurks elsewhere.

## Principles
1. **Reproduce first** — no repro, no fix.
2. **One hypothesis at a time,** each with a predicted, testable observation.
3. **Follow evidence, not hunches** — read the trace, logs, and values.
4. **Root cause over symptom** — ask "why" until it bottoms out.
5. **Change one variable per experiment.**
6. **A bug fixed without a regression test isn't finished.**

## Decision framework
- **Can't reproduce?** Gather environment/inputs; add logging; don't guess-fix blind.
- **Regressed recently?** `git bisect` to the commit before hypothesizing.
- **Multiple plausible causes?** Rank by likelihood; test the cheapest-to-check first.
- **Fix works but you don't know why?** Not done — you may have moved the bug.
- **Same bug pattern elsewhere?** Fix the class, or file follow-ups.

## Common mistakes
- **Fixing without reproducing** — patching a symptom you never confirmed.
- **Changing several things at once,** losing causality.
- **Symptom patches** (swallowing the error, null-guarding the crash site).
- **Trusting assumptions** over printed values / actual state.
- **Skimming the stack trace** instead of reading the real failure line.
- **No regression test,** so it silently returns later.

## Validation checklist
- [ ] Bug reproduced deterministically before any fix.
- [ ] Root cause identified and explained, not just the surface symptom.
- [ ] Fix is minimal and targets the cause.
- [ ] A regression test fails without the fix and passes with it.
- [ ] Full suite green; no new failures introduced.
- [ ] Same-class occurrences checked or follow-ups filed.
- [ ] Note records cause, fix, and blast radius.

## Edge cases
- **Heisenbug / flaky:** find the nondeterminism (order, timing, shared state, RNG seed); make it deterministic before fixing.
- **Only fails in prod:** match versions, config, and data shape locally; add targeted logging.
- **Bug in a dependency:** confirm with a minimal repro; pin/patch/upstream ([managing-dependencies](../managing-dependencies/SKILL.md)).
- **Data-dependent:** capture the exact triggering input as a fixture.

## Related skills
- [implementing-features](../implementing-features/SKILL.md), [writing-automated-tests](../writing-automated-tests/SKILL.md), [reading-unfamiliar-codebases](../reading-unfamiliar-codebases/SKILL.md).
- [optimizing-code-performance](../optimizing-code-performance/SKILL.md), [handling-errors-and-logging](../handling-errors-and-logging/SKILL.md), [using-git-workflows](../using-git-workflows/SKILL.md).
- [reviewing-code](../../review/reviewing-code/SKILL.md).

## Examples
**Input:** "Users intermittently get a 500 on checkout — here's the stack trace."
**Output:** Reproduced by replaying the failing request; trace pointed to a null tax
rate. Pinned with a failing test using that payload. Bisected to a config change that
dropped a region's rate. Root cause: lookup returns null for unmapped regions and the
caller assumes non-null — not the crash line itself. Fix: default + explicit
unmapped-region handling upstream. Regression test added; suite green. Note: three
other lookups share the pattern — follow-up filed.

## Automation opportunities
- Turn every fixed bug's repro into a permanent regression test.
- Use `git bisect run` with the pinned test to automate history isolation.
- Add structured logging/error tracking so repros arrive with context ([handling-errors-and-logging](../handling-errors-and-logging/SKILL.md)).
