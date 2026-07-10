---
name: reading-unfamiliar-codebases
description: Orient quickly in an unfamiliar codebase — find entry points, learn how to build/run/test it, trace a request or flow end-to-end, map the key modules and dependencies, and locate where to make a change safely. Use when the user says "I'm new to this repo", "help me understand this codebase", "where does X happen", "how does this work", or "where do I change Y".
---

# Reading Unfamiliar Codebases

## Scope
Getting oriented in a codebase you don't know: locating entry points, the
build/run/test loop, the shape of the system, and the exact place a change belongs —
fast enough to act with confidence. Precedes implementing or debugging in that code.

## Purpose
Build an accurate mental model of an unfamiliar system quickly, so the next change is
made in the right place, in the local idiom, without breaking things you didn't know existed.

## When to use this skill
- "I'm new to this repo / help me understand this codebase."
- "Where does X happen / how does this flow work / where do I change Y?"
- Before implementing or debugging in code you haven't worked in.

## When NOT to use this skill
- You already understand the area → go implement or fix directly.
- Building a new feature once oriented → [implementing-features](../implementing-features/SKILL.md).
- Chasing a specific defect → [debugging-systematically](../debugging-systematically/SKILL.md).
- Judging quality/architecture → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).

## Inputs
- Repo access and a goal: what you're about to change, fix, or understand.
- Any docs (README, ADRs, runbooks), and someone to ask when stuck.
- Ability to build and run the project.

## Outputs
- A working build/run/test loop you can execute.
- A map: entry points, key modules, data flow, external dependencies.
- The specific file(s)/function(s) where the intended change belongs.

## Workflow
```
Progress:
- [ ] 1. Fix the goal — what one change or question is this reading for?
- [ ] 2. Survey top-down — README, dir layout, manifest/deps, build config
- [ ] 3. Get it building/running/testing green locally
- [ ] 4. Find entry points and trace ONE representative flow end-to-end
- [ ] 5. Map key modules, boundaries, and external dependencies
- [ ] 6. Pinpoint the change site; confirm with a tiny probe
```

**Step 1 — Goal.** Read with a question, not for completeness. "Where is auth
enforced?" beats "understand everything." The goal bounds how deep to go.

**Step 2 — Survey.** README, then directory layout, then the dependency manifest and
build config — they reveal language, framework, structure, and third-party surface
faster than any file. Note conventions and where tests live.

**Step 3 — Run it.** Get build → run → test green before deep reading. A running
system with a passing suite is your safety net and your fastest teacher; change one
thing and watch what moves.

**Step 4 — Trace one flow.** Pick a representative path (an HTTP route, a CLI
command, a job) and follow it end-to-end: entry → routing → business logic → data →
response. Use call-graph search, breakpoints, or logging. One flow traced fully
teaches more than ten skimmed files.

**Step 5 — Map.** Sketch the key modules, their responsibilities, the boundaries
between them, and what's external (DB, queues, services). Note the seams where
changes are safe.

**Step 6 — Pinpoint.** Locate the exact function/file to change. Confirm your model
with a tiny probe — a log line, a failing assertion, a no-op edit that shows up —
before committing to a plan.

## Principles
1. **Read with a goal;** depth follows the question.
2. **Run before you read** — a live system beats static reading.
3. **Trace one flow fully** rather than skimming many files.
4. **Entry points and boundaries first,** details later.
5. **Trust running behavior over comments and docs,** which drift.
6. **Verify your model with a cheap probe** before acting on it.

## Decision framework
- **Big repo, small task?** Ignore everything off the target flow.
- **Can't get it running?** That's the first ticket — resolve it before reading further.
- **Docs disagree with code?** Believe the code; verify by running.
- **Multiple candidate change sites?** Trace which one the live flow actually hits.
- **Still lost after a flow trace?** Ask a maintainer a specific, narrowed question.

## Common mistakes
- **Reading top-to-bottom** instead of tracing a real path.
- **Skipping the run** and reasoning purely from source.
- **Boiling the ocean** — mapping the whole system for a one-line change.
- **Trusting stale comments/docs** over actual behavior.
- **Grepping a name and editing the first hit** without confirming the live call path.
- **Not noting conventions,** then writing against the grain.

## Validation checklist
- [ ] Goal stated; reading stayed scoped to it.
- [ ] Build, run, and test commands work locally.
- [ ] At least one representative flow traced entry-to-exit.
- [ ] Key modules, boundaries, and external deps identified.
- [ ] Change site pinpointed and confirmed with a probe.
- [ ] Local conventions (style, patterns, test layout) noted.

## Edge cases
- **No/outdated docs:** rely on tests as executable spec; they show intended behavior and usage.
- **Monorepo:** find the sub-project owning your goal; scope to it, note shared libs.
- **Generated or vendored code:** identify the source of truth; don't edit generated output.
- **No local run possible:** trace statically via tests and call graph; flag the risk before changing.
- **Legacy with no tests:** add a characterization test first to capture current behavior.

## Related skills
- [implementing-features](../implementing-features/SKILL.md), [debugging-systematically](../debugging-systematically/SKILL.md), [refactoring-code](../refactoring-code/SKILL.md).
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [writing-automated-tests](../writing-automated-tests/SKILL.md), [managing-dependencies](../managing-dependencies/SKILL.md).
- [writing-technical-documentation](../../office/writing-technical-documentation/SKILL.md).

## Examples
**Input:** "New to this service — where do I add a field to the order-confirmation email?"
**Output:** Goal fixed to that flow. Survey showed a Node service, deps reveal a
templating lib and a mail provider. Got it running with the test suite green. Traced
`POST /orders` → order service → `sendConfirmation()` → template render → provider.
Mapped: controllers, services, `email/templates`, provider adapter. Change site:
`OrderConfirmation` template + the model that populates it. Confirmed by adding a
temporary field and seeing it in the rendered test output.

## Automation opportunities
- Generate a dependency/call graph to see structure without reading every file.
- Use the test suite as living documentation of intended behavior and usage.
- Capture the build/run/test loop and the system map in the repo README ([writing-technical-documentation](../../office/writing-technical-documentation/SKILL.md)).
