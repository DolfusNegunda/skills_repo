---
name: analyzing-root-causes
description: Find the true cause of a problem rather than its symptom, using 5-whys, fishbone/Ishikawa diagrams, and causal chains, while separating correlation from causation. Use when the user says "why does this keep happening", "we keep firefighting the same issue", "find the root cause", "get to the bottom of this", or a fix that treated a symptom failed. Produces a verified root cause with supporting evidence.
---

# Analyzing Root Causes

## Scope
Tracing a problem back from its visible symptom to the underlying cause that, if
removed, stops the problem recurring. Covers 5-whys, fishbone (Ishikawa)
categorization, causal chains, and the discipline of distinguishing correlation
from causation. Ends at a verified cause — not at designing the fix.

## Purpose
Stop treating symptoms. Identify the actual driver so a single durable fix ends the
recurrence, instead of repeated firefighting of the same issue in new clothes.

## When to use this skill
- "Why does this keep happening / we keep firefighting the same thing."
- A recurring incident, defect, or process failure where past fixes didn't stick.
- Post-incident / retrospective analysis that needs to reach a real cause.

## When NOT to use this skill
- Designing or choosing a solution before the cause is proven → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md) / a doing skill.
- Debugging a specific code defect → [debugging-systematically](../../software-engineering/debugging-systematically/SKILL.md).
- The problem is huge and unscoped and first needs breaking down → [decomposing-problems](../decomposing-problems/SKILL.md).
- You have a candidate cause and just need to test it → [testing-hypotheses](../testing-hypotheses/SKILL.md).

## Inputs
- A clear, specific problem statement with when/where it occurs and its impact.
- Evidence: logs, metrics, timelines, incident reports, eyewitness accounts.
- What has already been tried and whether it held.

## Outputs
- A causal chain from symptom to root cause, with evidence at each link.
- The identified root cause(s), stated as something actionable to remove.
- Explicitly rejected candidate causes and why (correlation, timing, no mechanism).

## Workflow
```
Progress:
- [ ] 1. State the problem precisely: what, where, when, magnitude
- [ ] 2. Gather evidence and build the event timeline
- [ ] 3. Enumerate candidate causes (fishbone categories)
- [ ] 4. Trace each promising chain with 5-whys to a root
- [ ] 5. Verify the cause: mechanism + evidence + would-removing-it-stop-it
- [ ] 6. Separate true causes from correlations; state root cause(s)
```

**Step 1 — Define the problem.** Pin it down: not "the site is slow" but "checkout
p95 latency tripled after 14:00 on Tuesdays". A fuzzy problem yields a fuzzy cause.

**Step 2 — Gather evidence.** Build a timeline of what changed and when. Anchor the
analysis in data, not recollection; note what you *don't* have.

**Step 3 — Enumerate causes.** Use fishbone categories to force breadth (e.g.
people, process, tooling, data, environment, external) so you don't tunnel on the
first guess. Cast wide before narrowing.

**Step 4 — Ask why.** For each live candidate, ask "why" repeatedly (~5 times) until
you hit a cause that is actionable and beyond which "why" only gives generic answers.
Branch when a "why" has multiple valid answers — the chain is often a tree.

**Step 5 — Verify.** For a claimed root cause, confirm three things: a plausible
**mechanism**, **evidence** it was present, and that **removing/reversing it would
have prevented** the symptom (mentally or via test → [testing-hypotheses](../testing-hypotheses/SKILL.md)).

**Step 6 — Causation vs correlation.** Reject candidates that only co-occur: check
timing (cause precedes effect), a mechanism, dose-response, and rule out a common
third driver. State the surviving root cause(s).

## Principles
1. **Symptom ≠ cause** — the loudest signal is rarely the root.
2. **Evidence over narrative** — a satisfying story that data doesn't support is a guess.
3. **Correlation is not causation** — demand mechanism + temporal order, not just co-movement.
4. **Go deep enough, then stop** — the root is the deepest cause you can *actually act on*.
5. **Expect multiple causes** — most real failures are a chain or a combination, not one villain.
6. **Blame systems, not people** — "human error" is a starting symptom; ask why the system allowed it.

## Decision framework
- **"Why" answer is generic/unactionable ("people make mistakes")?** You've gone one step too far — back up to the last actionable link.
- **Fix keeps failing?** You're treating a symptom; re-run whys from a level deeper.
- **Two candidates both fit?** Find a discriminating test or evidence that only one predicts.
- **Only correlation, no mechanism?** Do not declare it the cause; keep it as a lead.
- **Multiple genuine root causes?** Keep all; prioritize by contribution → [prioritizing-options](../prioritizing-options/SKILL.md).

## Common mistakes
- **Stopping 5-whys too early** — fixing the first plausible layer (the symptom's proxy), not the root.
- **Stopping too late** — recursing past the actionable cause into unactionable philosophy.
- **Confusing correlation with cause** — "errors rose when deploys rose" without a mechanism or a common third cause ruled out.
- **Single-cause bias** — forcing one root when several combined to trigger it.
- **Confirmation bias** — hunting only for evidence of your first hunch; ignoring disconfirming data.
- **Jumping to the fix** — proposing a solution before the cause is verified.
- **Blaming a person** and closing the analysis, leaving the enabling system intact.

## Validation checklist
- [ ] Problem stated specifically (what/where/when/magnitude).
- [ ] Causal chain documented from symptom to root, with evidence per link.
- [ ] Root cause is actionable and, if removed, would prevent recurrence.
- [ ] Correlation-only candidates rejected with a stated reason.
- [ ] Considered multiple/combined causes, not just one.
- [ ] Whys stopped at the actionable level — neither symptom nor philosophy.

## Edge cases
- **Intermittent / non-reproducible:** widen the timeline, look for a rare trigger or combination; treat as hypothesis to test rather than force a cause.
- **No hard evidence available:** state candidate causes with confidence levels; don't assert a root you can't support.
- **Systemic/emergent problems:** no single root — model feedback loops → [thinking-in-systems](../thinking-in-systems/SKILL.md).
- **Organizational/human factors:** keep asking why the process permitted the error, not who erred.

## Related skills
- [debugging-systematically](../../software-engineering/debugging-systematically/SKILL.md) — root-cause analysis specialized for code defects.
- [testing-hypotheses](../testing-hypotheses/SKILL.md), [detecting-fallacies-and-inconsistencies](../detecting-fallacies-and-inconsistencies/SKILL.md), [decomposing-problems](../decomposing-problems/SKILL.md).
- [thinking-in-systems](../thinking-in-systems/SKILL.md), [conducting-structured-reviews](../../review/conducting-structured-reviews/SKILL.md), [observing-data-pipelines](../../data-engineering/observing-data-pipelines/SKILL.md).

## Examples
**Input:** "Customers keep getting double-charged. We refund them but it keeps happening."
**Output:** Problem: duplicate charges on ~0.3% of orders, clustered at peak load.
Timeline shows retries during payment-gateway timeouts. 5-whys: charged twice → two
requests sent → client retried on timeout → no idempotency key → the API never
enforced one. Root cause: missing idempotency on the charge endpoint (mechanism +
log evidence + removing it prevents recurrence). Rejected "gateway is flaky" as
correlation — timeouts trigger it but aren't the cause. Refunds were treating the
symptom.

## Automation opportunities
- Standardize post-incident templates that force timeline, whys, and evidence per link.
- Alert on symptom recurrence to catch symptom-only fixes that didn't hold.
- Maintain a cause library / known-issues catalog so repeat root causes are recognized fast.
