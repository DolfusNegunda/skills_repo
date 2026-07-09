---
name: reviewing-code
description: Review source code in any language for correctness, design, readability, security, performance, error handling, and test coverage — producing severity-ranked findings with specific fixes and a merge verdict. Use when the user asks to "review this code", "do a code review", "check this PR/diff", or assess code quality before merge. Language-agnostic; pairs with language-specific reviews. Inherits the shared severity/scoring model. Produces an actionable review, not a rewrite.
---

# Reviewing Code

## Scope
Language-agnostic evaluation of source code and changes (PRs/diffs) for correctness
and quality, with a merge verdict. Inherits method/severity/scoring from
[conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).
Language specifics live in [reviewing-python](../reviewing-python/SKILL.md) and
[reviewing-sql](../reviewing-sql/SKILL.md).

## Purpose
Catch defects before they ship and improve maintainability — with evidence, ranked
by severity, each finding carrying a concrete fix, ending in a clear merge decision.

## When to use this skill
- "Review this code / do a code review / check this PR or diff."
- A quality/security gate before merge or release.
- Assessing an unfamiliar codebase's quality.

## When NOT to use this skill
- Language-specific idiom depth → [reviewing-python](../reviewing-python/SKILL.md), [reviewing-sql](../reviewing-sql/SKILL.md).
- System-level design → [reviewing-architecture](../reviewing-architecture/SKILL.md).
- Writing the code/fix → an authoring/refactoring skill.

## Inputs
- The code or diff, its language, and what it's supposed to do.
- Context: tests, requirements, and the change's intent (for a PR).
- The bar: prototype vs. production; any security/compliance needs.

## Outputs
- A review: merge verdict + dimension scores, severity-ranked findings (file:line +
  why + fix), and strengths.

## Evaluation rubric (dimensions)
1. **Correctness** — does it do the right thing? Edge cases, off-by-one, nulls, concurrency.
2. **Design** — sound structure, right abstractions, no needless coupling/duplication.
3. **Readability** — clear names, reasonable function size, self-evident intent.
4. **Error handling** — failures caught, surfaced, and not silently swallowed.
5. **Security** — input validation, injection, secrets, authz, unsafe deserialization.
6. **Performance** — no obvious hotspots, N+1s, or needless allocations for the scale.
7. **Tests** — meaningful coverage of the change, including edge/failure cases.
8. **Dependencies** — justified, maintained, no license/supply-chain red flags.

## Scoring & severity
Score dimensions 1–5; rank findings Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = SQL injection, or a logic bug producing wrong results;
**Major** = no error handling on a fallible call, or an untested critical path;
**Minor** = a function doing two things; **Nit** = a naming preference.

## Workflow
```
Progress:
- [ ] 1. Understand intent: what should this change do?
- [ ] 2. Correctness pass: trace logic and edge cases
- [ ] 3. Security + error-handling pass
- [ ] 4. Design + readability pass
- [ ] 5. Performance + tests + dependencies pass
- [ ] 6. Severity-rank, score, verdict; fixes per finding
```

**Step 1** — never review a diff blind; know the intended behavior first.
**Step 2** — correctness is the priority; a beautifully written wrong answer still
fails. **Prioritize Blockers/security over style** — don't bury a vulnerability
under naming nits.

## Recommended-improvements guidance
Give the fix at the right altitude: correctness → the specific case to handle;
security → the validation/parameterization to add; design → the extraction/
boundary to introduce; tests → the exact missing case. Reference file:line.

## Validation checklist
- [ ] Change intent understood before reviewing.
- [ ] Correctness, security, and error handling explicitly checked.
- [ ] Tests assessed for the changed behavior, not just presence.
- [ ] Findings carry file:line, severity, and a fix.
- [ ] Merge verdict + scores given; strengths noted.
- [ ] Style nits kept subordinate to substantive findings.

## Common mistakes
- **Style-only review** that misses a real bug or vuln.
- **No intent context** — can't judge correctness.
- **Nit-flooding** — many Nits, no severity signal.
- **"Looks good" with no evidence** — rubber-stamping.
- **Ignoring tests** — approving untested critical paths.

## Edge cases
- **Large PR:** review by concern (correctness first) and flag that size itself is a risk; suggest splitting.
- **Generated/vendored code:** review the integration and config, not the generated internals.
- **Prototype:** relax design/test bars but never security/correctness; say so.
- **Unfamiliar language:** apply universal dimensions; defer idiom to the language skill.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-python](../reviewing-python/SKILL.md), [reviewing-sql](../reviewing-sql/SKILL.md).
- [reviewing-architecture](../reviewing-architecture/SKILL.md) — for system-level concerns.

## Examples
**Input:** "Review this PR that adds a user-search endpoint."
**Output:** Verdict: Request changes (Security 1/5, Correctness 3/5, Tests 2/5).
**Blocker:** query built by string interpolation — SQL injection at `search.py:42`;
fix: parameterize. **Major:** no test for empty/oversized input. **Minor:** handler
does validation + DB + formatting; extract. **Praise:** clear pagination logic.

## Automation opportunities
- Run linters/SAST/tests first; reserve human review for what tools can't judge (design, correctness of intent).
- Gate merges on no open Blocker/Major security findings.
- Mirror this rubric in the repo's PR template.
