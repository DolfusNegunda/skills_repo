---
name: governing-data-and-lineage
description: Establish data governance — a metadata-rich catalog, end-to-end lineage, clear ownership and stewardship, least-privilege access control, PII/sensitive-data classification, and retention policies. Use when the user says "set up a data catalog", "we need data lineage", "who owns this table", "classify our PII", "lock down access", or "nobody can trace where this data came from".
---

# Governing Data and Lineage

## Scope
Making data discoverable, traceable, owned, protected, and time-bounded across the
platform: catalog + metadata, column-level lineage, stewardship, least-privilege
access, sensitivity classification, and retention. Assumes pipelines and tables
already exist and need governance layered on.

## Purpose
Turn an opaque data estate into a governed one where anyone can find a dataset,
trust its provenance, know who owns it, see only what they're entitled to, and know
when it will be deleted — so incidents are traceable and audits pass.

## When to use this skill
- "Stand up a data catalog / capture metadata / make datasets discoverable."
- "We need lineage" or "we can't do root-cause because we don't know upstreams."
- Assigning ownership/stewardship; enforcing least privilege; classifying PII.
- Defining retention/deletion for regulated or sensitive data.

## When NOT to use this skill
- Testing/validating data correctness → [ensuring-data-quality](../ensuring-data-quality/SKILL.md).
- Org-level decision rights and policy bodies → [establishing-governance](../../business/establishing-governance/SKILL.md).
- Pipeline-level metrics/freshness/alerting → [observing-data-pipelines](../observing-data-pipelines/SKILL.md).
- Secure coding of the platform itself → [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md).

## Inputs
- Inventory of sources, tables, and pipelines; the platform (e.g. Unity Catalog, Glue, BigQuery, Snowflake).
- Regulatory context (GDPR, HIPAA, CCPA), data residency, and existing IAM/groups.
- Business domains and candidate owners; existing tags/glossary if any.

## Outputs
- A populated catalog: descriptions, tags, glossary terms, owners per dataset.
- Column-level lineage from source to consumption, queryable for impact analysis.
- An access model (RBAC/ABAC) with least-privilege grants to groups, not people.
- A classification scheme applied to columns; masking/row-filter policies for sensitive data.
- Documented retention/deletion policies, enforced by schedule.

## Workflow
```
Progress:
- [ ] 1. Inventory data assets and their current state
- [ ] 2. Stand up / populate the catalog with metadata and a glossary
- [ ] 3. Capture end-to-end, column-level lineage
- [ ] 4. Assign ownership and stewardship per domain/dataset
- [ ] 5. Classify sensitivity and apply masking/row policies
- [ ] 6. Design least-privilege access; grant to groups
- [ ] 7. Define and enforce retention/deletion
- [ ] 8. Wire governance into CI/CD so it stays current
```

**Step 1 — Inventory.** Enumerate sources, tables, views, and pipelines. Mark what's
undocumented, unowned, or unclassified — that gap list is your backlog.

**Step 2 — Catalog.** Register assets in the catalog (Unity Catalog-style three-level
namespace, Glue, or equivalent). Require a description, domain tag, and business
glossary terms per table. Prefer metadata harvested from code/DDL over hand-entry so
it doesn't rot.

**Step 3 — Lineage.** Capture lineage at **column** level, not just table level —
automatically from query/pipeline parsing (Unity Catalog, OpenLineage, dbt) rather
than a hand-drawn diagram that drifts. Verify you can answer "if I drop this column,
what breaks?" No lineage means impossible root-cause analysis when data is wrong.

**Step 4 — Ownership.** Assign a single accountable **owner** and a **steward** per
dataset/domain. Record them as catalog metadata, not a wiki. Unowned data is
ungoverned data — every asset must resolve to a name.

**Step 5 — Classify.** Tag columns by sensitivity (public / internal / confidential /
PII / regulated). Automate PII detection (name, email, SSN patterns) as a first pass,
then confirm. Apply column masking and row-level filters bound to the tags. Unclassified
PII is a breach waiting to happen.

**Step 6 — Access.** Grant least privilege: read-only by default, to **groups** mapped
to roles, never to individuals. Use ABAC/tag-based policies so a "confidential" tag
auto-restricts. Review grants periodically; revoke standing broad access.

**Step 7 — Retention.** Define retention per classification and regulation; schedule
deletion/archival. Keeping regulated data past its window is a liability, not an asset.

**Step 8 — Automate.** Enforce "no undocumented/unowned/unclassified table" as a
pipeline gate so governance is maintained, not a one-off cleanup.

## Principles
1. **Metadata as code** — harvest from DDL/pipelines; hand-maintained docs rot.
2. **Column-level everything** — lineage and classification at column granularity.
3. **Least privilege by default** — deny-by-default, grant to groups, time-box exceptions.
4. **Every asset has an owner** — accountability is a required field.
5. **Classify before you share** — no dataset leaves a boundary unclassified.
6. **Governance in the pipeline,** not a quarterly cleanup.

## Decision framework
- **Table vs column lineage?** Column — table-level can't answer impact of a rename/drop.
- **Grant to a person or a group?** Group mapped to a role, always.
- **PII detection manual or automated?** Automated first pass, human confirm; never manual-only.
- **Who owns a shared/cross-domain dataset?** The producing domain owns; consumers are stewards of their copies.
- **Keep or delete aging data?** Delete at policy expiry unless a legal hold applies.

## Common mistakes
- **No lineage** → root-cause analysis is guesswork when a downstream number is wrong.
- **Table-only lineage** that can't trace a single column through transformations.
- **Over-broad access** — everyone in `data_readers` can see PII; grants to individuals.
- **Unclassified PII** sitting in shared schemas; classification done once and never re-run.
- **Ownership on a wiki** that's stale; assets with no accountable owner.
- **Catalog descriptions written once,** never synced to schema changes (silent drift).
- **No retention** — regulated data accumulates indefinitely.

## Validation checklist
- [ ] Every production table has a description, owner, and domain tag in the catalog.
- [ ] Column-level lineage resolves source→consumption; impact queries work.
- [ ] Sensitive columns are classified; masking/row filters enforce the tags.
- [ ] Access is least-privilege, group-based, and reviewed; no standing broad grants.
- [ ] Retention/deletion policies exist per classification and run on schedule.
- [ ] A governance gate in CI/CD blocks undocumented/unowned/unclassified assets.

## Edge cases
- **Legacy tables with no owner:** assign provisionally to the platform team; escalate to claim.
- **Cross-region/residency constraints:** classification must carry a residency tag; restrict replication.
- **External/third-party feeds:** classify on ingest; you can't trust their metadata.
- **Derived datasets:** propagate the strictest source classification downstream automatically.
- **Legal hold:** suspends retention deletion; must override the schedule.

## Related skills
- [ensuring-data-quality](../ensuring-data-quality/SKILL.md), [observing-data-pipelines](../observing-data-pipelines/SKILL.md), [managing-schema-evolution](../managing-schema-evolution/SKILL.md).
- [architecting-lakehouses](../architecting-lakehouses/SKILL.md), [designing-data-pipelines](../designing-data-pipelines/SKILL.md).
- [establishing-governance](../../business/establishing-governance/SKILL.md), [writing-secure-code](../../software-engineering/writing-secure-code/SKILL.md).

## Examples
**Input:** "Auditors asked how customer PII flows through our platform and who can see it."
**Output:** Registered all customer tables in Unity Catalog with owners and glossary
terms. Captured column-level lineage (OpenLineage) showing email/SSN from `raw.crm`
through `staging` to `marts.customer_360`. Classified those columns as PII; applied
column masking so only `pii_reader` group sees raw values. Converted individual grants
to group-based least privilege; documented 7-year retention with scheduled deletion.
Auditor question now answerable from one lineage query.

## Automation opportunities
- Auto-harvest catalog metadata and lineage from pipeline/query parsing on every run.
- Run automated PII scanners on new columns; open a ticket for unclassified sensitive data.
- Periodic access-review job flags standing broad or individual grants.
- Scheduled retention jobs delete/archive expired data with an audit log.
