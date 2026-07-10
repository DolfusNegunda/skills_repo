---
name: modeling-dimensional-warehouses
description: Design Kimball-style dimensional models — pick the grain, build fact and dimension tables, assign surrogate keys, handle slowly changing dimensions (SCD type 1/2), share conformed dimensions across marts, and avoid over-snowflaking. Use when the user says "design a star schema", "what's the grain of this fact", "how do I track history on this dimension", "SCD type 2", "build a dimensional model", or "fact vs dimension".
---

# Modeling Dimensional Warehouses

## Scope
Logical dimensional modeling the Kimball way: grain, fact/dimension design,
surrogate keys, SCDs, and conformed dimensions. Not the physical lake layout
([architecting-lakehouses](../architecting-lakehouses/SKILL.md)), not writing the
queries ([authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md)).

## Purpose
Produce a star schema whose grain is stated and consistent, whose facts are additive
and correctly keyed, whose dimensions track history deliberately (SCD 1 vs 2), and
whose conformed dimensions let separate marts be compared apples-to-apples.

## When to use this skill
- "Design a star schema / dimensional model / data mart".
- "What's the grain of this fact table?", "fact or dimension?".
- "Track history on the customer dimension", "SCD type 1 or 2?", "surrogate keys?".

## When NOT to use this skill
- Physical file layout, partitioning, Delta/Iceberg → [architecting-lakehouses](../architecting-lakehouses/SKILL.md).
- Writing/optimizing the SQL against the model → [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md).
- Making the built warehouse fast → [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md).

## Inputs
- The business process being measured and the questions it must answer.
- Available source entities, their natural keys, and which attributes change over time.
- Whether history matters per attribute (do users need "as-was" vs "as-is" reporting).

## Outputs
- A star schema: fact grain statement, fact measures + foreign keys, dimension tables.
- Surrogate-key + SCD strategy per dimension, and the set of conformed dimensions.

## Workflow
```
Progress:
- [ ] 1. Pick the business process and declare the fact grain in one sentence
- [ ] 2. Identify dimensions (the "by what" of every question)
- [ ] 3. Identify facts/measures; classify additive vs semi/non-additive
- [ ] 4. Assign surrogate keys; keep natural keys as attributes
- [ ] 5. Choose an SCD type per changing attribute (1 overwrite vs 2 history)
- [ ] 6. Conform shared dimensions across marts; resist over-snowflaking
```

**Step 1 — Grain first.** State "one row per ___" for the fact (e.g. "one row per
order line") before anything else. The grain is the single most important decision;
mixing grains in one fact is the root cause of double-counting.

**Step 2 — Dimensions.** Every "by/per" in a business question is a dimension
(date, product, customer, store). Prefer wide, denormalized, descriptive dimensions
over normalized lookup chains.

**Step 3 — Facts.** Facts hold numeric measures at the grain plus foreign keys to
dimensions. Classify each measure: additive (sums across all dims), semi-additive
(balances — not additive over time), non-additive (ratios — store components, not the ratio).

**Step 4 — Surrogate keys.** Give each dimension an integer surrogate PK; facts
reference the surrogate, not the source natural key. This decouples from source
systems, enables SCD-2 history, and handles late/unknown members via a `-1` "unknown" row.

**Step 5 — SCD choice.** Per attribute: SCD-1 overwrites (no history — current state
only); SCD-2 adds a new dimension row with effective/expiry dates + a current flag
(preserves history). Facts join to the surrogate valid at the event time, giving true
"as-was" reporting. Getting SCD-2 date ranges/current-flag wrong is the classic bug.

**Step 6 — Conform, don't snowflake.** Share identical conformed dimensions across
facts/marts so metrics are comparable. Keep the star flat; only snowflake when a
sub-hierarchy is genuinely reused or huge.

## Principles
- Declare the grain before columns; every measure must live at that one grain.
- One fact = one business process at one grain; don't blend processes or grains.
- Surrogate keys everywhere; natural keys ride along as attributes only.
- Denormalize dimensions for query clarity; the star, not the snowflake, is the default.
- Conformed dimensions are the contract that makes marts comparable — design them once.

## Decision framework
- **Fact vs dimension:** numeric, measured, event-driven → fact; descriptive context you filter/group by → dimension.
- **SCD-1 vs SCD-2:** history irrelevant / correcting an error → type 1; must report "as it was" → type 2 (add row + date range + current flag). Type 3 only for a single "previous value".
- **Fact type:** event → transaction fact; state over intervals → periodic snapshot; lifecycle milestones → accumulating snapshot.
- **Additivity:** additive → sum freely; semi-additive (inventory) → sum across all but time; non-additive (ratios) → store numerator/denominator.
- **Snowflake vs star:** default star; snowflake only for a large, genuinely shared hierarchy.

## Common mistakes
- **Wrong or mixed grain** — combining header and line detail in one fact → double-counting.
- **SCD-2 mishandled** — overlapping/gapped effective dates, missing/multiple current flags, or facts joining to the wrong version.
- **Using source natural keys as fact FKs** — breaks on source reuse and blocks SCD-2.
- **Over-snowflaking** — normalizing dimensions into lookup chains, forcing many joins.
- **Storing non-additive measures** (ratios/percentages) instead of their components.
- **No "unknown" member** — losing fact rows on unmatched/late-arriving dimensions.
- **Degenerate dimension ignored** — dropping order/invoice numbers that belong on the fact.

## Validation checklist
- [ ] Fact grain stated in one sentence; every measure lives at that grain.
- [ ] Each dimension has an integer surrogate PK; facts use surrogates, not natural keys.
- [ ] SCD type chosen per attribute; SCD-2 has non-overlapping date ranges + exactly one current row.
- [ ] Measures classified (additive/semi/non-additive); ratios stored as components.
- [ ] Shared dimensions are conformed across all marts.
- [ ] An "unknown/-1" member handles unmatched and late-arriving keys.
- [ ] Model stays a star; snowflaking justified case-by-case.

## Edge cases
- **Late-arriving facts:** look up the dimension version valid at the event date, not today's.
- **Late-arriving dimensions:** insert an inferred member, backfill attributes when they arrive.
- **Many-to-many:** use a bridge table with an allocation/weighting factor.
- **Multi-valued attributes:** bridge with a group key; avoid comma-lists in a column.
- **Fact-less facts:** model coverage/event occurrence (e.g. attendance) as a keys-only fact.
- **Rapidly changing attributes:** split into a mini-dimension to avoid SCD-2 row explosion.

## Related skills
- [architecting-lakehouses](../architecting-lakehouses/SKILL.md) — physical layout the star is materialized on.
- [tuning-warehouse-performance](../tuning-warehouse-performance/SKILL.md) — making the built model fast.
- [authoring-sql-queries](../../software-engineering/authoring-sql-queries/SKILL.md) — querying the star schema.
- [reviewing-sql](../../review/reviewing-sql/SKILL.md) — reviewing the transformation SQL that loads it.

## Examples
**Input:** "Model retail sales; customers change address over time and we need to
report sales by the address at time of sale."
**Output:** Grain: one row per sales line. Fact `sales` holds quantity/amount +
FKs to `dim_date`, `dim_product`, `dim_store`, `dim_customer`. Make `dim_customer`
SCD-2 (surrogate key, effective/expiry dates, `is_current`); the fact joins the
surrogate valid at sale date, so "as-was" address reporting is correct. `dim_date`
and `dim_product` are conformed for reuse across marts.

## Automation opportunities
- Generate SCD-2 loads with `MERGE` (expire current row, insert new) from a template.
- Test grain in CI: assert fact row count equals the source at the declared grain.
- Add checks for SCD-2 integrity: no overlapping ranges, exactly one current row per key.
