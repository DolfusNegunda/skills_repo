---
name: writing-automated-tests
description: Design and write effective automated tests — decide what is worth testing, structure with arrange-act-assert, cover boundaries and error paths, and keep tests deterministic and independent. Use when the user says "write tests for this", "add unit tests", "how do I test this", "improve test coverage", or is choosing between unit, integration, and end-to-end tests.
---

# Writing Automated Tests

## Scope
Authoring new automated tests for code you control: choosing the test level,
deciding what deserves a test, and writing tests that fail for the right reason
and pass reliably. Not reviewing existing tests, not manual QA.

## Purpose
Produce a test suite that catches real regressions, reads as executable
specification, and stays fast and trustworthy — so a green run actually means the
code works.

## When to use this skill
- "Write tests for this function/module/endpoint."
- "Add unit/integration/e2e tests" or "improve coverage" on new or changed code.
- Deciding which test level fits a given behavior.
- Building a safety net before a refactor.

## When NOT to use this skill
- Critiquing tests that already exist → [reviewing-code](../../review/reviewing-code/SKILL.md).
- Manual/exploratory QA of a running UI — that is human testing, not this.
- Adding the behavior itself → [implementing-features](../implementing-features/SKILL.md).
- Chasing a specific failure → [debugging-systematically](../debugging-systematically/SKILL.md).

## Inputs
- The code under test and its intended behavior/contract.
- Existing test framework, runners, and fixtures already in the repo.
- Known boundaries, error modes, and external dependencies (I/O, time, network).

## Outputs
- Tests named for the behavior they assert, structured arrange-act-assert.
- Coverage of happy path, boundaries, and error paths — deterministic and isolated.
- Test doubles only at genuine seams; no doubles for the code under test.

## Workflow
```
Progress:
- [ ] 1. Pin the behavior and contract to verify
- [ ] 2. Pick the test level (unit / integration / e2e)
- [ ] 3. Enumerate cases: happy path, boundaries, error paths
- [ ] 4. Write one AAA test per case; assert on behavior, not internals
- [ ] 5. Remove nondeterminism; isolate shared state and doubles
- [ ] 6. Run; confirm each fails for the right reason, then passes
```
**Step 1 — Pin the behavior.** State the contract in one sentence ("returns X given
Y, raises on Z"). If you cannot, you are testing implementation, not behavior.
**Step 2 — Pick the level.** Push logic down the pyramid: unit for pure logic,
integration for a real seam (DB, HTTP layer), e2e only for critical user journeys.
**Step 3 — Enumerate cases.** List inputs before writing code: nominal, empty,
min/max, off-by-one, null/absent, and each documented failure.
**Step 4 — Write AAA.** One reason to fail per test; arrange, act once, assert the
observable outcome. Name the test after the case.
**Step 5 — De-flake.** Inject clock/random/IDs; no sleeps, no shared mutable state,
no reliance on test order.
**Step 6 — Verify honestly.** Break the code to see the test fail, then restore.

## Principles
- Test observable behavior through the public interface, not private internals.
- Each test proves one thing and states it in its name.
- A test must be able to fail — a test that never fails verifies nothing.
- Deterministic and independent: any order, any machine, same result.
- Fast where it matters — a suite too slow to run is a suite not run.
- The test is documentation; a reader should learn the contract from it.

## Decision framework
- **Which level?** Can I exercise it with in-memory inputs → unit. Does the risk
  live in a real integration (SQL, serialization, wiring) → integration. Is it a
  user-visible journey that must not break → e2e. Prefer the lowest level that
  gives real confidence; most tests are unit.
- **Worth testing?** Yes for logic with branches, boundaries, past bugs, and public
  contracts. No for trivial getters, framework glue, or generated code.
- **Real or double?** Use the real thing across a cheap, deterministic seam; double
  only slow, nondeterministic, or hard-to-trigger dependencies (network, clock,
  payment gateway). Never mock the unit under test.
- **Coverage number?** Treat it as a spotlight on untested branches, never a target
  to hit — 100% of trivial code proves nothing.

## Common mistakes
- **Asserting on internals** (private calls, log lines) — breaks on refactor, the
  opposite of a safety net.
- **Multiple behaviors per test** — a failure no longer tells you what broke.
- **Over-mocking** until the test only verifies the mocks, not the code.
- **Nondeterminism** — real time, real random, network, order dependence → flaky.
- **Testing the framework** or generated boilerplate for coverage points.
- **Tests that cannot fail** — tautologies, or assertions that were never observed
  to go red.

## Validation checklist
- [ ] Each test names the behavior it verifies and checks one thing.
- [ ] Happy path, boundaries, and error paths all covered.
- [ ] No real clock/random/network/order dependence; doubles only at true seams.
- [ ] Assertions target observable behavior, not private internals.
- [ ] Every test was seen to fail before it passed.
- [ ] Suite runs green repeatably and in any order.

## Edge cases
- **Legacy code with no seams:** add one characterization test first, then refactor.
- **Async/concurrent:** await/settle deterministically; avoid timing races and sleeps.
- **Time/timezone/locale:** inject a fixed clock and pin locale.
- **Nondeterministic output (ordering, floats):** assert sets/tolerances, not exact.
- **External services:** contract-test the boundary; do not hit live systems in CI.

## Related skills
- [refactoring-code](../refactoring-code/SKILL.md) — tests are the safety net it requires.
- [implementing-features](../implementing-features/SKILL.md), [debugging-systematically](../debugging-systematically/SKILL.md).
- [reviewing-code](../../review/reviewing-code/SKILL.md) — for judging tests that exist.

## Examples
**Input:** "Write tests for `parse_duration(str) -> seconds`, raises on bad input."
**Output:** Unit tests: `"90s"→90`, `"2m"→120` (happy); `""`, `"0s"→0`, largest
supported value (boundaries); `"abc"`, `"5x"`, `None` → raises `ValueError` (error
paths). Each AAA, named `test_parses_minutes`, etc. No I/O, no clock — pure and
deterministic. Coverage confirms both branches of the unit hit.

## Automation opportunities
- Wire the suite into CI on every push; fail the build on red.
- Run coverage to surface untested branches — as a guide, not a gate to game.
- Add mutation testing on critical modules to catch tests that cannot fail.
- Enforce a fast unit tier separate from slow integration/e2e stages.
