---
name: refactoring-code
description: Improve the internal structure of code without changing its observable behavior — establish a test safety net, work in small reversible steps, apply named refactorings, and commit frequently. Use when the user says "refactor this", "clean up this code", "reduce duplication", "this function is too long", or "make this more readable" without adding features.
---

# Refactoring Code

## Scope
Behavior-preserving restructuring of existing code: rename, extract, inline,
reshape data and parameters, remove duplication. Correctness stays fixed; only
the structure improves. Not adding features, not a rewrite.

## Purpose
Leave the code measurably easier to read and change than you found it, with
behavior provably unchanged — so the next edit is safer and faster.

## When to use this skill
- "Refactor / clean up / tidy this code."
- "This function is too long / too nested / duplicated" — restructure, not extend.
- Preparing tangled code before adding a feature or fixing a bug.
- Paying down structural debt with no behavior change intended.

## When NOT to use this skill
- Adding or changing behavior → [implementing-features](../implementing-features/SKILL.md).
- A ground-up rewrite or re-architecture decision → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).
- Diagnosing a defect → [debugging-systematically](../debugging-systematically/SKILL.md).
- Speed work that trades behavior/structure → [optimizing-code-performance](../optimizing-code-performance/SKILL.md).

## Inputs
- The code to improve and its current, intended behavior.
- Existing tests (or the means to add them) covering that behavior.
- Version control with a clean working tree to commit against.

## Outputs
- Restructured code with identical observable behavior.
- A series of small, reversible commits, each green.
- Tests still passing — ideally the same suite that guarded the start.

## Workflow
```
Progress:
- [ ] 1. Confirm a green test safety net exists (or add characterization tests)
- [ ] 2. Name the specific smell and target structure
- [ ] 3. Apply ONE named refactoring
- [ ] 4. Run tests; commit if green, revert if not
- [ ] 5. Repeat in small steps
- [ ] 6. Stop when clear enough; final review of the diff
```
**Step 1 — Safety net first.** Never refactor untested code. If none exists, pin
current behavior with characterization tests before touching structure.
**Step 2 — Name the smell.** Long function, duplication, unclear name, feature
envy, primitive obsession — name it, and the target shape.
**Step 3 — One refactoring.** Extract function, rename, inline, introduce parameter
object, replace conditional — apply a single named move, not a rewrite.
**Step 4 — Test and commit.** Run the suite after every step; green → commit,
red → revert immediately. Small steps make reverts cheap.
**Step 5 — Iterate.** Many tiny reversible steps beat one large risky edit.
**Step 6 — Stop.** When the code is clear enough for the task at hand, stop —
perfect is out of scope.

## Principles
- Behavior is invariant: same inputs, same outputs, same side effects, throughout.
- Green-to-green: never leave the suite red between steps.
- Small and reversible — each step trivially undoable; commit at each green point.
- Separate refactoring commits from behavior commits; never mix the two in one diff.
- Refactor to enable a change, or to leave code you touched cleaner — with purpose.
- Automated rename/extract over hand edits when the tool guarantees safety.

## Decision framework
- **Do I have a net?** No passing tests → add characterization tests first, or do
  not refactor. This is non-negotiable.
- **Which refactoring?** Duplication → extract + call. Long function → extract by
  responsibility. Unclear name → rename. Long parameter list → parameter object.
  Temporary variable sprawl → inline / extract. Match the move to the smell.
- **How big a step?** As small as still leaves tests runnable. If a step needs a
  comment to justify it, it is too big — split it.
- **When to stop?** When the smell that prompted this is gone and the next reader
  will understand it. Do not gold-plate unrelated code.
- **Mixing with a feature?** Refactor first on green, commit, then add behavior in a
  separate commit — never interleave.

## Common mistakes
- **Refactoring without tests** — you cannot know behavior held.
- **Big-bang rewrite** disguised as refactoring — high risk, unreviewable diff.
- **Mixing behavior changes in** — now a "refactor" can introduce bugs invisibly.
- **Not running tests between steps** — a break hides among many edits.
- **Not committing** — losing the last green state when a step goes wrong.
- **Endless polishing** — refactoring code unrelated to the task at hand.

## Validation checklist
- [ ] A green test suite guarded the whole process.
- [ ] Observable behavior is unchanged (same tests, still green).
- [ ] Each step was small, named, and committed while green.
- [ ] No behavior change is mixed into the refactoring commits.
- [ ] The diff is readable and the original smell is resolved.
- [ ] Working tree is clean; nothing left half-restructured.

## Edge cases
- **No tests and no easy seam:** add characterization tests capturing current
  output first, even if the behavior looks wrong — preserve, then fix separately.
- **Public API rename:** keep a deprecated alias or do it as a coordinated change.
- **Huge function:** extract in slices, testing after each — not one giant extract.
- **Shared/hot code:** smaller steps, more frequent commits, tighter test runs.

## Related skills
- [writing-automated-tests](../writing-automated-tests/SKILL.md) — build the safety net first.
- [implementing-features](../implementing-features/SKILL.md), [debugging-systematically](../debugging-systematically/SKILL.md).
- [reviewing-code](../../review/reviewing-code/SKILL.md) — to check the resulting diff.

## Examples
**Input:** "Clean up this 120-line `process_order` function — it is unreadable."
**Output:** Confirm tests cover order processing (add characterization tests if
not). Then, step by step: extract `validate_order`, extract `apply_discounts`,
rename `d` → `discount_rate`, introduce an `OrderContext` parameter object for the
five threaded args. Run tests and commit after each. Result: a short orchestrator
calling named steps, behavior identical, six small green commits.

## Automation opportunities
- Use IDE-verified refactorings (rename, extract) over manual edits.
- Run the test suite automatically after each step (watch mode / pre-commit).
- Let linters and formatters handle mechanical style so review focuses on structure.
- Track structural smells (complexity, duplication) in CI to spot debt early.
