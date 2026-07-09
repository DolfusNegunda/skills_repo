---
name: reviewing-sql
description: Review SQL queries, DDL, and schema for correctness, performance, and safety — checking join logic, filtering, aggregation, indexing, execution cost, and destructive-statement risk. Use when the user asks to "review this SQL", "check this query", "why is this query slow", or assess a schema/migration before running it. Inherits the shared severity/scoring model. Produces severity-ranked findings with specific fixes and a run/merge verdict.
---

# Reviewing SQL

## Scope
Evaluation of SQL — queries, DDL, migrations, and schema design — for correct
results, acceptable performance, and safe execution. Inherits method/severity/
scoring from [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md).
General code concerns are in [reviewing-code](../reviewing-code/SKILL.md).

## Purpose
Confirm a query returns the *right* rows efficiently and won't cause harm (wrong
results, table scans at scale, or an unguarded destructive statement) — before it runs.

## When to use this skill
- "Review this SQL / check this query / this migration."
- "Why is this query slow?" (performance review).
- Assessing a schema change, index, or destructive statement before execution.

## When NOT to use this skill
- General (non-SQL) code → [reviewing-code](../reviewing-code/SKILL.md).
- Data-model design at large → a data-engineering/architecture skill.
- Writing the query → an authoring skill.

## Inputs
- The SQL and the dialect (Postgres, T-SQL, BigQuery, Spark SQL, …).
- Intended result and the schema (tables, keys, indexes, row counts if known).
- Where it runs (OLTP vs. warehouse) and its frequency/scale.

## Outputs
- A review: run/merge verdict + scores, severity-ranked findings (with the exact
  clause and a fix), and strengths.

## Evaluation rubric (dimensions)
1. **Correctness** — join type/keys, grain, filters, NULL handling, GROUP BY completeness, dedup.
2. **Performance** — sargable predicates, index use, avoided full scans, join order, partition pruning.
3. **Safety** — no unbounded UPDATE/DELETE without WHERE; transactions; idempotent migrations.
4. **Readability** — CTEs over nested subqueries, aliasing, formatting, no `SELECT *` in production.
5. **Portability/correctness of dialect** — functions valid for the target engine.

## Scoring & severity
Score 1–5; rank Blocker→Praise (see
[foundation reference](../conducting-structured-reviews/references/severity-and-scoring.md)).
Examples: **Blocker** = `DELETE` with no `WHERE`, or a join that silently multiplies
rows (wrong grain); **Major** = a non-sargable predicate forcing a full scan on a
large table; **Minor** = `SELECT *`; **Nit** = inconsistent keyword casing.

## Workflow
```
Progress:
- [ ] 1. Confirm intended result, dialect, schema, and scale
- [ ] 2. Correctness: trace grain, joins, filters, NULLs, grouping
- [ ] 3. Safety: destructive statements, transactions, migration reversibility
- [ ] 4. Performance: predicates, indexes, scan/plan risk
- [ ] 5. Readability and dialect validity
- [ ] 6. Severity-rank, score, verdict; fixes per finding
```

**Step 2 — grain is the #1 SQL bug.** Check that joins don't fan out rows and
aggregations group by the intended key; a query that runs is not a query that's
correct. **Step 4** — read (or reason about) the execution plan; flag full scans,
missing indexes, and functions wrapped around indexed columns.

## Recommended-improvements guidance
Give the rewrite: the correct join/keys, the sargable form of the predicate, the
index to add, the `WHERE`/transaction to guard a destructive statement, or the CTE
refactor. Quote the exact clause.

## Validation checklist
- [ ] Intended result, dialect, and scale known.
- [ ] Join grain verified (no unintended row multiplication).
- [ ] NULL and GROUP BY semantics correct.
- [ ] Destructive statements guarded; migrations reversible/idempotent.
- [ ] Performance risks (scans, non-sargable predicates, missing indexes) flagged.
- [ ] Findings carry the clause, severity, and a fix; verdict + scores given.

## Common mistakes
- **Reviewing for style while a grain bug returns wrong totals.**
- **Ignoring scale** — fine on 1k rows, catastrophic on 1B.
- **Missing the unguarded UPDATE/DELETE.**
- **Not checking dialect** — valid SQL for the wrong engine.
- **Approving without knowing the intended result.**

## Edge cases
- **Warehouse vs. OLTP:** partition/cluster pruning matters more than row indexes; adjust the perf lens.
- **Analytical one-off vs. production:** relax style, never correctness/safety.
- **Generated SQL (ORM/dbt):** review the model logic and resulting plan, not formatting.
- **No schema available:** flag assumptions; review what's verifiable.

## Related skills
- [conducting-structured-reviews](../conducting-structured-reviews/SKILL.md), [reviewing-code](../reviewing-code/SKILL.md).
- [reviewing-architecture](../reviewing-architecture/SKILL.md) — for data-model-level concerns.

## Examples
**Input:** "Review this report query — it double-counts revenue."
**Output:** Verdict: Request changes (Correctness 2/5). **Blocker:** the join to
`payments` is one-to-many, inflating `SUM(amount)`; fix: aggregate payments in a CTE
to order grain before joining. **Major:** `WHERE DATE(created_at)=…` isn't sargable;
fix: range predicate on the raw column. **Praise:** clear CTE naming.

## Automation opportunities
- Run EXPLAIN and a linter (sqlfluff) first; focus review on logic and plan.
- Gate migrations on a "no unguarded destructive statement" check.
- Reuse the rubric in a query-review PR template.
