---
name: decomposing-problems
description: Break a large, ambiguous problem into tractable, MECE parts using issue trees and problem trees, so it can be solved piece by piece. Use when the user says "this is too big to tackle", "where do I even start", "break this down", "structure this problem", or faces a sprawling question with no obvious entry point. Produces a labelled decomposition tree with prioritized branches.
---

# Decomposing Problems

## Scope
Turning one big, fuzzy problem into a structured set of smaller sub-problems that
are mutually exclusive and collectively exhaustive (MECE), then ordering them so the
highest-leverage parts get solved first. Covers issue trees, hypothesis trees, and
logic (component/formula) trees — not the solving of each leaf.

## Purpose
Make an overwhelming problem workable: give it a shape where every part is
independently solvable, nothing important is missing, and effort lands where it
matters instead of on whatever is easiest to grab.

## When to use this skill
- "This is too big / I don't know where to start / help me break it down."
- A vague objective ("grow revenue", "reduce churn", "the system is slow") with many possible angles.
- Before estimating, planning, or dividing work across people.

## When NOT to use this skill
- The problem is already scoped and just needs execution → the relevant doing skill.
- Finding the true cause of a defect or failure → [analyzing-root-causes](../analyzing-root-causes/SKILL.md).
- Weighing already-defined options against each other → [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md) or [prioritizing-options](../prioritizing-options/SKILL.md).

## Inputs
- The problem statement or objective, and who owns/asked it.
- Any known constraints and the decision or output the decomposition must feed.
- Available data and rough sense of what "solved" looks like.

## Outputs
- A decomposition tree: a top question split into MECE branches down to solvable leaves.
- Each leaf tagged with type (question / hypothesis / component) and a priority.
- A short note on which branches to pursue first and which are parked.

## Workflow
```
Progress:
- [ ] 1. State the core problem as one sharp question
- [ ] 2. Pick a tree type (issue / hypothesis / logic) fitting the problem
- [ ] 3. Split into 2–5 MECE branches at each level
- [ ] 4. Recurse until leaves are concrete and solvable
- [ ] 5. Test the whole tree for MECE and right-sizing
- [ ] 6. Prioritize branches; mark what to solve first vs park
```

**Step 1 — Frame.** Write the problem as a single answerable question ("How do we
cut onboarding time from 3 weeks to 1?"). A vague noun ("onboarding") is not a
problem; a question with a subject and a target is.

**Step 2 — Choose the tree.** *Issue tree* for open diagnosis ("why/what could
drive X"); *hypothesis tree* when you have candidate answers to test; *logic/component
tree* when the top can be split by a formula or structure (revenue = price × volume).

**Step 3 — Split MECE.** Break each node into branches that don't overlap
(exclusive) and leave no gap (exhaustive). Prefer a real partition — by formula,
stage, segment, or a spanning axis — over an ad-hoc list of whatever comes to mind.

**Step 4 — Recurse.** Go down until each leaf is small enough that one person could
tackle it with known methods or a bounded amount of data. Usually 2–4 levels.

**Step 5 — Test the tree.** Check every level for overlaps and gaps; add a
"other/remainder" branch only if you truly can't partition cleanly. Confirm leaves
are same-order-of-magnitude in scope, not one giant and three tiny.

**Step 6 — Prioritize.** Rank branches by impact × tractability (or a
[prioritizing-options](../prioritizing-options/SKILL.md) pass). Pursue the vital few;
explicitly park the rest so they're not silently dropped.

## Principles
1. **One sharp question at the top** — the whole tree inherits its clarity.
2. **MECE at every split** — no overlaps, no gaps; a real partition beats a list.
3. **Same altitude among siblings** — branches at a level should be comparable in size.
4. **Cut deep only where it pays** — decompose high-priority branches further, not all equally.
5. **Structure ≠ solution** — the tree organizes work; it doesn't answer the question.
6. **Make it disprovable** — for hypothesis trees, each branch states what evidence would confirm/kill it.

## Decision framework
- **Can the top be written as a formula/identity?** Use a logic tree — cleanest MECE.
- **Do you already suspect answers?** Hypothesis tree, then test ([testing-hypotheses](../testing-hypotheses/SKILL.md)).
- **Truly open diagnosis?** Issue tree by a spanning axis (stage, segment, cause-type).
- **Branch still too big to act on?** Recurse one more level; don't stop at abstractions.
- **Branches overlap?** Re-cut on a single dimension rather than patching exceptions.

## Common mistakes
- **Non-MECE splits** — overlapping branches (double-counting) or missing ones (blind spots); the classic is a random list instead of a partition.
- **Mixing dimensions in one level** — splitting by region *and* product together, so branches collide.
- **Uneven altitude** — one branch is the whole problem, its siblings are footnotes.
- **Bottomless recursion** — decomposing everything to dust instead of stopping at solvable leaves.
- **Confusing decomposition with root cause** — an issue tree lists *areas to check*, not the proven cause.
- **Skipping prioritization** — a tidy tree with 40 equal leaves and no plan of attack.

## Validation checklist
- [ ] Top is a single, sharp, answerable question with a target.
- [ ] Every split is MECE (no overlap, no gap); tested level by level.
- [ ] Siblings sit at comparable altitude/scope.
- [ ] Leaves are concrete enough to assign and solve.
- [ ] Branches prioritized; first moves and parked items are explicit.
- [ ] Tree type (issue/hypothesis/logic) is appropriate to the problem.

## Edge cases
- **Can't find a clean partition:** split on the best single axis and add an explicit "remainder", then revisit.
- **Interdependent branches:** note the coupling; if it dominates, model it as a system → [thinking-in-systems](../thinking-in-systems/SKILL.md).
- **Unknown unknowns suspected:** add an explicit "what we don't know" branch rather than pretending completeness.
- **Problem shifts as you learn:** treat the tree as living; re-cut when the framing changes.

## Related skills
- [analyzing-root-causes](../analyzing-root-causes/SKILL.md) — once a branch points at a defect, find its true cause.
- [prioritizing-options](../prioritizing-options/SKILL.md), [analyzing-tradeoffs](../analyzing-tradeoffs/SKILL.md), [testing-hypotheses](../testing-hypotheses/SKILL.md).
- [thinking-in-systems](../thinking-in-systems/SKILL.md), [estimating-under-uncertainty](../estimating-under-uncertainty/SKILL.md), [performing-business-analysis](../../business/performing-business-analysis/SKILL.md).

## Examples
**Input:** "Our SaaS gross margin is too low — fix it. Where do I start?"
**Output:** Top question: "How do we raise gross margin from 55% to 70%?" Logic
tree: margin = revenue − COGS. Revenue branch → price, mix, discounting. COGS branch
→ hosting, support, third-party fees. MECE-checked (no overlap between the two
sub-trees). Leaves like "hosting cost per active tenant" are measurable and ownable.
Prioritized: hosting (largest, tractable) first; discounting policy second; pricing
change parked pending a separate decision.

## Automation opportunities
- Template the tree in a mind-map/outline tool so branches and priorities stay visible.
- Keep a reusable library of standard trees (revenue, cost, funnel, reliability) to start from.
- Attach each leaf to a tracker item so decomposition flows straight into execution.
