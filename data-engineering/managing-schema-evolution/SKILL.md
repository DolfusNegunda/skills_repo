---
name: managing-schema-evolution
description: Evolve data schemas without breaking consumers — distinguish additive from breaking changes, maintain data contracts and versioning, guarantee backward/forward compatibility, detect and absorb schema drift, and run safe migrations. Use when the user says "I need to change this schema", "will this break downstream", "add a column safely", "rename/drop a field", "version this table", or "our schema keeps drifting".
---

# Managing Schema Evolution

## Scope
Changing the shape of data over time without breaking the systems that read it:
classifying changes, enforcing data contracts, versioning, keeping compatibility,
detecting drift, and migrating safely. Assumes a model already exists and now must
change under live consumers.

## Purpose
Let producers evolve schemas at the speed the business needs while consumers keep
working — no silent breakage, no 3am pipeline failure from a column that vanished.

## When to use this skill
- "Add / rename / drop / retype a column and I don't want to break downstream."
- "Will this schema change break anyone?" / impact of a producer change.
- Establishing data contracts or a versioning scheme for tables/topics/events.
- "Our upstream keeps changing shape and it breaks us" (schema drift).

## When NOT to use this skill
- Designing the model from scratch → [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md).
- Versioning code libraries/packages → [managing-dependencies](../../software-engineering/managing-dependencies/SKILL.md).
- Data correctness rules/tests → [ensuring-data-quality](../ensuring-data-quality/SKILL.md).
- Cataloging/classifying the schema → [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md).

## Inputs
- The current schema and the proposed change; the storage/serialization format (Delta, Parquet, Avro, Protobuf, JSON).
- The consumer list and how they read (SQL, `SELECT *`, schema-on-read, contracts).
- Lineage (which columns feed what) and any schema registry / contract in place.

## Outputs
- A change classified additive vs breaking, with a compatibility verdict.
- A data contract and version bump (semver) reflecting the change.
- A migration plan (expand/contract) with rollback, and drift detection wired in.

## Workflow
```
Progress:
- [ ] 1. Specify the change and inventory consumers via lineage
- [ ] 2. Classify: additive (compatible) vs breaking
- [ ] 3. Check backward AND forward compatibility for the format
- [ ] 4. Update the data contract and version (semver)
- [ ] 5. Choose a rollout: additive-only, or expand/contract migration
- [ ] 6. Execute with dual-write/backfill; verify consumers; then contract
- [ ] 7. Wire schema-drift detection to catch future unplanned changes
```

**Step 1 — Specify & find consumers.** State the exact change. Use lineage to list every
consumer — you cannot judge safety without knowing who reads the column. `SELECT *`
consumers are fragile: assume the worst.

**Step 2 — Classify.** **Additive/safe:** adding a nullable column, adding an enum value
(usually), widening a type. **Breaking:** rename, drop, retype-narrowing, making a
column non-nullable, changing units/semantics, reordering positional formats. Renaming
or dropping a column a downstream job selects **will** break it — treat as breaking even
if "nobody uses it."

**Step 3 — Compatibility.** Check both directions for your format. **Backward** = new
readers read old data. **Forward** = old readers read new data. Avro/Protobuf give
rules (Protobuf: never reuse field numbers; keep fields optional). Delta/Parquet:
column add is safe; drop/rename/retype needs a rewrite or overwrite schema.

**Step 4 — Contract & version.** Encode the schema as a **data contract** (schema
registry, dbt contract, or Protobuf/Avro IDL). Bump **semver**: patch = docs, minor =
additive/backward-compatible, **major = breaking**. A major bump signals consumers must
act and lets you run versions side by side.

**Step 5 — Choose rollout.** Additive → ship directly. Breaking → use **expand/contract
(parallel change)**: add the new form alongside the old, migrate consumers, then remove
the old. Never rename-in-place under live consumers.

**Step 6 — Execute.** Expand: add new column/version, dual-write or backfill both.
Verify every consumer moved (lineage confirms zero readers of the old form). Only then
contract: drop the old. Keep a rollback (the old column still exists until contract).

**Step 7 — Drift detection.** Compare incoming schema to the contract on every load;
fail or quarantine on unexpected change. Silent schema drift — an upstream adds/retypes
a field and you never notice — corrupts data quietly until someone spots bad numbers.

## Principles
1. **Additive by default** — prefer adding over changing; deprecate before deleting.
2. **Expand then contract** — never mutate a column in place under live readers.
3. **Contract is the interface** — the schema is a promise; changes are negotiated, versioned.
4. **Semver signals intent** — major = act now, minor = safe.
5. **Compatibility both ways** — check backward and forward, not just "it compiles."
6. **Fail loud on drift** — unexpected schema change stops the pipeline, doesn't slip through.

## Decision framework
- **Additive or breaking?** If any consumer's read could change/break → breaking.
- **Rename a column?** Add new + backfill + migrate + drop old (expand/contract); never in-place.
- **Drop a "unused" column?** Confirm zero readers via lineage first; deprecate for a release, then drop.
- **Retype a column?** Widening ~safe; narrowing/semantic change = breaking → new column + version.
- **Consumers use `SELECT *`?** Treat every change as potentially breaking; pin explicit columns.
- **Can't migrate all consumers at once?** Version and run old+new in parallel until drained.

## Common mistakes
- **Rename/drop in place** — a downstream job selecting that column breaks at next run.
- **"Nobody uses it"** without checking lineage — someone did.
- **Only checking backward compatibility,** breaking old readers of new data (forward).
- **No contract/versioning** — every change is a surprise; no signal to consumers.
- **Silent drift accepted** — schema-on-read swallows an upstream change; data rots quietly.
- **Big-bang migration** with no dual-write and no rollback.
- **Reusing a Protobuf field number** or enum ordinal after removal — corrupts decoding.

## Validation checklist
- [ ] Change classified additive vs breaking, backed by the consumer/lineage list.
- [ ] Backward and forward compatibility both assessed for the actual format.
- [ ] Data contract updated and semver bumped to match the change class.
- [ ] Breaking changes use expand/contract with dual-write/backfill and a rollback.
- [ ] All consumers verified migrated before the old form is removed.
- [ ] Schema-drift detection runs on ingest and fails/quarantines on surprise changes.

## Edge cases
- **Streaming/event schemas (Kafka + registry):** enforce registry compatibility mode; consumers may be long-lived on old versions.
- **`SELECT *` / schema-on-read consumers:** most fragile; pin columns or version aggressively.
- **Nested/struct evolution:** adding nested fields can still break strict readers; test explicitly.
- **Partition column change:** effectively a rewrite/migration, not additive.
- **Backfilling a new non-null column:** add nullable, backfill, then tighten — not non-null on day one.
- **External consumers you don't control:** longer deprecation window; announce the major bump.

## Related skills
- [modeling-dimensional-warehouses](../modeling-dimensional-warehouses/SKILL.md), [ensuring-data-quality](../ensuring-data-quality/SKILL.md), [governing-data-and-lineage](../governing-data-and-lineage/SKILL.md).
- [building-streaming-pipelines](../building-streaming-pipelines/SKILL.md), [designing-data-pipelines](../designing-data-pipelines/SKILL.md), [implementing-incremental-loading](../implementing-incremental-loading/SKILL.md).
- [managing-dependencies](../../software-engineering/managing-dependencies/SKILL.md), [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).

## Examples
**Input:** "I need to rename `cust_nm` to `customer_name` in a table 12 jobs read from."
**Output:** Classified breaking (rename). Lineage confirmed 12 readers. Plan: expand —
add `customer_name`, dual-write both columns, backfill history; bump the dbt contract to
a major version. Migrated all 12 jobs to the new column over two releases; verified zero
readers of `cust_nm` via lineage; then contracted (dropped `cust_nm`). Added a drift
check comparing load schema to the contract. No consumer broke.

## Automation opportunities
- Enforce schema-registry compatibility checks (backward+forward) in CI before deploy.
- Auto-diff proposed schema against the contract and label PRs additive vs breaking.
- Run drift detection on every ingest; quarantine and alert on unexpected columns/types.
- Generate consumer-impact reports from lineage automatically on any schema change.
