---
name: authoring-sql-queries
description: Write correct, performant, and injection-safe SQL — set-based thinking, right joins, early filtering, sargable predicates that hit indexes, window functions and CTEs for clarity, and always-parameterized inputs. Use when the user asks to "write a SQL query", "how do I query", "optimize this query", "why is this query slow", or needs to turn a data question into SQL.
---

# Authoring SQL Queries

## Scope
Authoring and tuning SQL that returns the right rows fast and cannot be injected.
Covers SELECT/DML shape, join and filter choice, indexing awareness, window
functions, CTEs, and parameterization. Not schema design at scale, not review.

## Purpose
Turn a data question into a query that is provably correct on edge data (NULLs,
duplicates, empty sets), reads well, uses available indexes, and passes user input
only through bound parameters.

## When to use this skill
- "Write a SQL query for…", "how do I query…", "get me the rows where…".
- "Optimize / speed up this query", "why is this slow", "it does a full scan".
- Replacing per-row application loops (N+1) with one set-based query.

## When NOT to use this skill
- Reviewing existing SQL → [reviewing-sql](../../review/reviewing-sql/SKILL.md).
- Large-scale schema / data-model design (partitioning, normalization strategy).
- Input handling in app code generally → [writing-secure-code](../writing-secure-code/SKILL.md).

## Inputs
- The question in plain language + the tables/columns and their grain (one row per what).
- Dialect (Postgres/MySQL/SQL Server/etc.), and how the query is invoked (ORM, driver).
- Known indexes, rough row counts, and whether NULLs/duplicates occur.

## Outputs
- A parameterized query, the join/filter reasoning, and expected cardinality.
- Index or rewrite notes if the plan would scan; sample bound-parameter call.

## Workflow
```
Progress:
- [ ] 1. Restate the question; pin down the grain and expected row count
- [ ] 2. Choose FROM + join types; guard against fan-out/cartesian
- [ ] 3. Filter early with sargable predicates; project only needed columns
- [ ] 4. Add grouping/windows/CTEs for shape and clarity
- [ ] 5. Handle NULLs, duplicates, empty results
- [ ] 6. Parameterize every input; check the plan; verify on real data
```

**Step 1 — Grain.** State "one row per ___" for the result and each source table.
Most wrong-count bugs are grain/fan-out surprises, not typos.

**Step 2 — Joins.** Pick INNER only when both sides are required; LEFT to keep the
left side; put filters on the *right* table of a LEFT JOIN in the ON clause, not
WHERE (a WHERE predicate on it silently turns the LEFT into an INNER). Every join
needs a key condition — a missing one is a cartesian product.

**Step 3 — Filter early, stay sargable.** Filter before aggregating. Keep the
indexed column bare on one side: `col = @x`, `col >= @start AND col < @end` — never
`WHERE func(col) = x`, `col + 1 = x`, or `col::text = x`, which defeat the index.
Watch implicit conversions (int column vs string param). Project explicit columns,
never `SELECT *`.

**Step 4 — Shape.** Use CTEs to name steps instead of nesting subqueries. Use window
functions (`ROW_NUMBER`, `SUM() OVER`, `LAG`) for running totals / top-N-per-group
instead of self-joins or correlated subqueries.

**Step 5 — Edge data.** Decide behavior for NULLs (they fail `=`, sort apart, and
break `NOT IN`), duplicates (`DISTINCT` vs fixing the join), and empty inputs.

**Step 6 — Parameterize & verify.** Bind every value; read the plan; run it.

## Principles
- Think in sets, not rows: one query over a loop of queries.
- Correct first, then fast; a fast wrong answer is still wrong.
- Filter and reduce as early as possible; carry the fewest rows/columns forward.
- Make predicates sargable so indexes are usable.
- Inputs are parameters, never string fragments — no exceptions.

## Decision framework
- **INNER vs LEFT:** need matches on both sides → INNER; keep unmatched left rows → LEFT.
- **IN vs EXISTS:** correlated existence check or nullable subquery column → EXISTS.
- **NOT IN vs NOT EXISTS:** if the subquery can yield NULL, use NOT EXISTS (NOT IN returns no rows).
- **Subquery vs CTE vs window:** per-group ranking/running math → window; reused/named step → CTE.
- **GROUP BY vs DISTINCT:** aggregating → GROUP BY; only de-duping identical rows → DISTINCT (often a join-fanout smell).

## Common mistakes
- **String-concatenating input** into SQL → injection; always bind parameters.
- **Non-sargable predicate** (`WHERE YEAR(d)=2026`, `LOWER(email)=…`) forcing a scan.
- **`NOT IN` with a NULL** in the list → empty result set.
- **LEFT JOIN filtered in WHERE** on the right table → accidental INNER.
- **Missing join key** → cartesian product; **fan-out** → inflated SUM/COUNT.
- **`SELECT *`** — extra I/O, brittle to schema change, breaks covering indexes.
- **N+1**: querying inside an application loop instead of one set-based query.
- **Implicit conversion** (int vs varchar) silently disabling an index.

## Validation checklist
- [ ] Every input is a bound parameter; no concatenated user data.
- [ ] Result grain matches the question; no unintended fan-out or cartesian join.
- [ ] Predicates are sargable; no functions/conversions wrapping indexed columns.
- [ ] NULL, duplicate, and empty-input behavior is correct (esp. `NOT IN`/`NOT EXISTS`).
- [ ] Explicit column list, not `SELECT *`.
- [ ] Plan checked on realistic volume; no surprise full scans; result verified.

## Edge cases
- **Pagination:** prefer keyset (`WHERE id > @last ORDER BY id LIMIT n`) over large OFFSET.
- **IN with many values:** pass an array/table-valued parameter, not a built-up list.
- **Timezones/dates:** compare half-open ranges (`>= start AND < next_day`), avoid `DATE(col)`.
- **Upserts / concurrency:** use dialect `MERGE`/`ON CONFLICT`; mind race conditions.
- **Big aggregations:** filter first; consider indexed/materialized paths for hot queries.

## Related skills
- [reviewing-sql](../../review/reviewing-sql/SKILL.md) — auditing existing SQL.
- [writing-secure-code](../writing-secure-code/SKILL.md) — injection and input handling.
- [optimizing-code-performance](../optimizing-code-performance/SKILL.md) — broader performance work.

## Examples
**Input:** "Get each customer's latest order, but keep customers with no orders."
**Output:** LEFT JOIN customers to a windowed order set filtered to
`ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY created_at DESC) = 1`, in a
CTE; keep the order predicate in the CTE so the LEFT JOIN still returns
order-less customers; bind any status/date filters as parameters.

## Automation opportunities
- Route all queries through parameterized statements / an ORM query builder; ban string interpolation via lint.
- Add `EXPLAIN` (or plan capture) to CI for hot queries to catch new scans.
- Test queries against fixtures containing NULLs, duplicates, and empty sets.
