---
name: conducting-comparative-research
description: Compare options, entities, or approaches on a like-for-like basis — defining consistent criteria, gathering equivalent evidence per option, and presenting a fair, sourced comparison. Use when the user asks to "compare X and Y", "which is better", "do a comparison of", or evaluate alternatives side by side. Ensures apples-to-apples fairness and avoids bias. Produces a structured, evidenced comparison with a reasoned conclusion, not a lopsided pitch.
---

# Conducting Comparative Research

## Scope
Fair, evidenced comparison of two or more options/entities/approaches on consistent
criteria. The research discipline of like-for-like comparison; the scoring mechanics
for a decision are [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).

## Purpose
Produce a comparison the reader can trust: same criteria and equivalent evidence for
every option, so the conclusion reflects reality rather than uneven research or
hidden bias.

## When to use this skill
- "Compare X and Y / which is better / do a comparison of."
- Evaluating alternatives (tools, vendors, methods, products) side by side.
- Feeding a decision with a fair evidence base.

## When NOT to use this skill
- Weighted scoring to pick one → [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- Competitor landscape specifically → [analyzing-competitors](../analyzing-competitors/SKILL.md).
- Technology fit specifically → [evaluating-technology](../evaluating-technology/SKILL.md).

## Inputs
- The options to compare and the purpose (what the comparison decides/informs).
- The dimensions that matter and sources for equivalent evidence.

## Outputs
- A structured comparison: consistent criteria × options, evidenced per cell, with
  differences highlighted, sources cited, and a reasoned conclusion.

## Workflow
```
Progress:
- [ ] 1. Define the purpose and what the comparison must inform
- [ ] 2. Choose consistent, relevant criteria
- [ ] 3. Gather equivalent evidence for EVERY option
- [ ] 4. Populate a comparison table; cite each cell
- [ ] 5. Highlight meaningful differences (not just list attributes)
- [ ] 6. Draw a reasoned, caveated conclusion
```

**Step 2–3 — like-for-like is the whole game.** Use the same criteria for all options
and gather evidence of equal depth for each. The classic failure is researching the
favored option thoroughly and the others superficially, producing a foregone
conclusion. **Step 5 — highlight differences that matter;** a comparison is about the
distinctions that affect the decision, not an exhaustive attribute dump. **Step 6 —
conclude with caveats:** "best" is usually "best for whom/what" — state the conditions.

## Principles
1. **Same criteria for all options.**
2. **Equivalent evidence depth** per option — no favoritism.
3. **Cite every claim** — comparisons are contestable.
4. **Highlight decisive differences,** not every attribute.
5. **Conclusions are conditional** — best-for-context, not absolute.
6. **Guard against bias** — including your own prior preference.

## Decision framework
- **Need to pick one with weighted trade-offs?** Feed this into [building-decision-matrices](../../business/building-decision-matrices/SKILL.md).
- **Different use-cases?** Conclude per use-case, not a single winner.
- **Fast-changing options?** Timestamp; note that the comparison ages.
- **Incomparable on a criterion?** Say so rather than forcing a false equivalence.

## Common mistakes
- **Uneven research depth** across options — the top bias risk.
- **Inconsistent criteria** — comparing different things.
- **Attribute dump** with no analysis of what differences matter.
- **Uncited claims** in a contestable comparison.
- **Absolute "best"** ignoring context/use-case.
- **Confirmation bias** toward a pre-favored option.

## Validation checklist
- [ ] Purpose defined; criteria consistent and relevant.
- [ ] Equivalent, cited evidence for every option.
- [ ] Comparison table complete; no favored-option depth bias.
- [ ] Meaningful differences highlighted and interpreted.
- [ ] Conclusion reasoned and conditional (best-for-context).
- [ ] Bias checked; recency noted.

## Edge cases
- **Options at different maturity:** compare fairly and flag the maturity gap.
- **Missing data for one option:** note the gap; don't fill with assumption.
- **Vendor-supplied specs:** corroborate; don't compare marketing claims as facts.
- **Many options:** shortlist first, then deep-compare the finalists.

## Related skills
- [building-decision-matrices](../../business/building-decision-matrices/SKILL.md), [analyzing-competitors](../analyzing-competitors/SKILL.md), [evaluating-technology](../evaluating-technology/SKILL.md).
- [collecting-evidence](../collecting-evidence/SKILL.md), [citing-sources](../citing-sources/SKILL.md).

## Examples
**Input:** "Compare Postgres vs. MongoDB for our use case."
**Output:** Consistent criteria (data model fit, consistency, scalability, ops
maturity, cost, team skills), equally-researched and cited per database, a comparison
table, differences that matter to *this* use case highlighted (relational integrity
needs vs. flexible schema), and a conditional conclusion: Postgres for the
transactional core, with the caveat that a document store fits the separate catalog
workload.

## Automation opportunities
- Reuse a criteria template per comparison type for consistency.
- Feed the comparison table into a decision matrix for a weighted pick.
