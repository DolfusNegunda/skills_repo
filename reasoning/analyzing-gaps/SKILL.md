---
name: analyzing-gaps
description: Compare current state against a defined desired state, quantify the gap, and identify what closes it. Use when the user says "where are we vs where we want to be", "what's missing to hit the target", "gap analysis", "assess our maturity against X", or has a concrete target and needs the delta and the actions to close it. Produces a quantified current-vs-target gap with prioritized closing actions.
---

# Analyzing Gaps

## Scope
Measuring the distance between where things are now and a defined target, expressing
that distance concretely, and determining the specific changes that would close it.
Covers state comparison, gap quantification, and mapping gaps to closing actions —
against capability, performance, compliance, or maturity targets.

## Purpose
Turn "we're not where we want to be" into a measured delta and a concrete list of
what must change to close it — so effort targets the real shortfall, not a vague
sense of falling short.

## When to use this skill
- "Where are we versus where we want to be / what's missing to hit X."
- Assessing against a standard, benchmark, maturity model, or target metric.
- Planning what to build/change to reach a defined goal or compliance bar.

## When NOT to use this skill
- No target state is defined yet — it's open-ended discovery → [decomposing-problems](../decomposing-problems/SKILL.md) or requirements work.
- The target is met and you're finding *why something broke* → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- Choosing between ways to close a known gap → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md) / [prioritizing-options](../prioritizing-options/SKILL.md).

## Inputs
- A defined desired/target state with measurable criteria (the "to-be").
- Evidence of the current state (the "as-is"): metrics, inventory, assessment.
- The dimensions to compare on and any deadline or budget constraint.

## Outputs
- A current-vs-target table per dimension, with the quantified gap for each.
- Gaps ranked by size × importance, with the actions that would close each.
- A closing plan sketch: what, rough effort, and sequence.

## Workflow
```
Progress:
- [ ] 1. Define the desired state as measurable criteria
- [ ] 2. Pick the comparison dimensions (MECE)
- [ ] 3. Assess the current state on each dimension with evidence
- [ ] 4. Quantify the gap per dimension (target − current)
- [ ] 5. Identify what closes each gap; size the effort
- [ ] 6. Prioritize and sequence the closing actions
```

**Step 1 — Define the target.** Make the desired state measurable before measuring
current — "99.9% uptime", "SOC 2 controls A–H in place", "onboarding ≤ 1 week". A
target you can't measure against yields a gap you can't quantify.

**Step 2 — Choose dimensions.** List the axes to compare on, MECE, so gaps don't
overlap or hide. Borrow a standard's structure (framework domains, maturity levels)
when one exists.

**Step 3 — Assess as-is.** Measure current state on each dimension with real
evidence, using the *same* units and definitions as the target. Don't estimate what
you could measure.

**Step 4 — Quantify.** Express each gap concretely: numeric delta, missing/partial/
met, or maturity-level distance. "Big gap" is not an output; "42% vs 99.9% = 57.9pt"
is.

**Step 5 — Identify closers.** For each gap, name the specific change(s) that would
close it and roughly size the effort. One gap may need several; one action may close
several.

**Step 6 — Prioritize & sequence.** Rank by gap size × importance (and dependency
order); some gaps are prerequisites for closing others. Feed into
[prioritizing-options](../prioritizing-options/SKILL.md) if the list is large.

## Principles
1. **No target, no gap** — a measurable desired state is the precondition, not an afterthought.
2. **Same yardstick both sides** — as-is and to-be measured in identical units/definitions.
3. **Quantify, don't adjective** — a number or a clear status beats "significant gap".
4. **Evidence for current state** — measure it; don't assume it.
5. **Gap ≠ action plan** — sizing the gap and choosing how to close it are distinct steps.
6. **Prioritize by size × value** — the biggest delta isn't always the one worth closing first.

## Decision framework
- **Target not measurable?** Stop and define measurable criteria first — otherwise it's discovery, not gap analysis.
- **Can't measure current state cheaply?** Use a bounded estimate and flag confidence → [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md).
- **Gap is zero or negative?** Record it — over-shooting the target is also a finding (wasted effort/scope).
- **Many gaps, limited capacity?** Rank by impact and dependencies before committing.
- **Multiple ways to close a gap?** That's a separate decision → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md).

## Common mistakes
- **No measurable target** — "improve security" with nothing to measure against, so the "gap" is opinion.
- **Mismatched units** — comparing as-is and to-be measured differently, producing a fake gap.
- **Guessing current state** instead of assessing it.
- **Overlapping dimensions** — double-counting the same shortfall across axes.
- **Stopping at the gap** — quantifying but never mapping actions to close it.
- **Vanity gaps** — measuring easy dimensions while ignoring the ones that matter.
- **Ignoring the cost/effort** to close, so priorities favor big-but-hard over small-but-easy-and-valuable.

## Validation checklist
- [ ] Desired state is defined with measurable criteria.
- [ ] Comparison dimensions are MECE and cover what matters.
- [ ] Current state assessed with evidence, in the same units as the target.
- [ ] Each gap quantified (numeric delta or clear status), not adjectival.
- [ ] Each material gap mapped to concrete closing action(s) with rough effort.
- [ ] Gaps prioritized/sequenced by size × importance and dependencies.

## Edge cases
- **Moving target:** the to-be shifts (market, regulation) — timestamp both states and re-baseline periodically.
- **Qualitative dimensions:** use a defined rubric/maturity scale so "current" and "target" are still comparable.
- **Partial credit:** allow met/partial/not-met when binary hides real progress.
- **Unknown current state:** if measuring is infeasible, bound it and mark the gap as estimated, not measured.

## Related skills
- [decomposing-problems](../decomposing-problems/SKILL.md) — when no target exists yet and the problem needs structuring first.
- [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [prioritizing-options](../prioritizing-options/SKILL.md), [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md).
- [identifying-constraints](../identifying-constraints/SKILL.md), [performing-business-analysis](../../business/performing-business-analysis/SKILL.md), [conducting-structured-reviews](../../review/conducting-structured-reviews/SKILL.md).

## Examples
**Input:** "We want SOC 2 Type II by Q4. Where are we and what's missing?"
**Output:** Target: all Trust Services controls operating for 6 months by Q4.
Dimensions = the five criteria (security, availability, etc.), MECE. As-is assessed
against each control with evidence. Gaps quantified: Security 18/22 controls in place
(4 missing), Availability 6/8, no formal change-management (0/3). Closers mapped:
implement access reviews, add uptime monitoring, write change-mgmt policy; effort
sized S/M/L. Prioritized: change-management first (prerequisite + largest gap),
access reviews next. Over-target dimensions noted so no extra effort is spent there.

## Automation opportunities
- Dashboard current-vs-target metrics so the gap is always live, not a one-off study.
- Template the as-is/to-be table per standard (SOC 2, ISO, maturity models) for reuse.
- Auto-collect current-state metrics from source systems to keep the "as-is" honest.
