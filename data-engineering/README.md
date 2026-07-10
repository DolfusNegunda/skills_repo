# Data Engineering Skills

Operational competencies for moving, modeling, and trusting data at scale: pipeline
architecture, transformation, orchestration, quality, governance, performance, cost,
and observability. Every skill here follows the house style in
[../skill-builder/SKILL.md](../skill-builder/SKILL.md).

## Design philosophy

These are **procedure and judgment skills** (like [../software-engineering](../software-engineering/README.md)
and [../review](../review/README.md)) — no bundled scripts. Each adds what a generic
model can't guess: the *disciplined workflow*, *decision rules*, and the *specific
mechanical gotchas* an expert data engineer applies (the small-file problem, wrong or
mixed fact grain, non-idempotent loads, missing watermarks, SCD-2 date-range bugs,
data skew, full-table scans, silent schema drift). Tools (Spark, Delta/Iceberg,
Kafka, Airflow, dbt, Snowflake/BigQuery/Synapse, Unity-Catalog-style catalogs) appear
as concrete techniques *inside* the relevant competency, not as one-skill-per-tool.

## The skills

**Architecture & modeling**
| Skill | Focus |
|---|---|
| [designing-data-pipelines](designing-data-pipelines/SKILL.md) | Batch vs streaming, contracts, idempotency, replay, delivery guarantees. |
| [architecting-lakehouses](architecting-lakehouses/SKILL.md) | Medallion layering, Delta/Iceberg, ACID, file layout, small-file fixes. |
| [modeling-dimensional-warehouses](modeling-dimensional-warehouses/SKILL.md) | Kimball grain, facts/dimensions, surrogate keys, SCDs, conformed dims. |

**Movement & transformation**
| Skill | Focus |
|---|---|
| [building-batch-transformations](building-batch-transformations/SKILL.md) | Idempotent, reprocessable ETL/ELT; staging; tested transforms. |
| [building-streaming-pipelines](building-streaming-pipelines/SKILL.md) | Event vs processing time, watermarks, windows, late data, exactly-once. |
| [implementing-incremental-loading](implementing-incremental-loading/SKILL.md) | High-watermark, CDC, idempotent MERGE/upsert, deletes, late arrivals. |

**Orchestration & quality**
| Skill | Focus |
|---|---|
| [orchestrating-data-workflows](orchestrating-data-workflows/SKILL.md) | DAGs, idempotent retriable tasks, backfills, schedules, SLAs. |
| [ensuring-data-quality](ensuring-data-quality/SKILL.md) | Expectations, boundary tests, quarantine, data contracts, fail-vs-warn. |

**Governance**
| Skill | Focus |
|---|---|
| [governing-data-and-lineage](governing-data-and-lineage/SKILL.md) | Catalog, lineage, ownership, least-privilege access, PII, retention. |
| [managing-schema-evolution](managing-schema-evolution/SKILL.md) | Additive vs breaking changes, contracts, compatibility, safe migrations. |

**Performance, cost & ops**
| Skill | Focus |
|---|---|
| [optimizing-spark-jobs](optimizing-spark-jobs/SKILL.md) | Skew, shuffle, broadcast joins, partition/file sizing, AQE, no driver collects. |
| [tuning-warehouse-performance](tuning-warehouse-performance/SKILL.md) | Partition pruning, clustering, materialized views, result cache, right-sizing. |
| [optimizing-data-costs](optimizing-data-costs/SKILL.md) | Storage vs compute, auto-suspend, scanned-bytes reduction, retention, attribution. |
| [observing-data-pipelines](observing-data-pipelines/SKILL.md) | Freshness/volume/schema monitors, data SLAs, alerting, lineage for RCA. |

## How they compose

- **Stand up a platform:** [designing-data-pipelines](designing-data-pipelines/SKILL.md) →
  [architecting-lakehouses](architecting-lakehouses/SKILL.md) +
  [modeling-dimensional-warehouses](modeling-dimensional-warehouses/SKILL.md).
- **Build the flow:** [building-batch-transformations](building-batch-transformations/SKILL.md) /
  [building-streaming-pipelines](building-streaming-pipelines/SKILL.md) +
  [implementing-incremental-loading](implementing-incremental-loading/SKILL.md) →
  [orchestrating-data-workflows](orchestrating-data-workflows/SKILL.md).
- **Make it trustworthy:** [ensuring-data-quality](ensuring-data-quality/SKILL.md) +
  [governing-data-and-lineage](governing-data-and-lineage/SKILL.md) +
  [managing-schema-evolution](managing-schema-evolution/SKILL.md) +
  [observing-data-pipelines](observing-data-pipelines/SKILL.md).
- **Make it fast and cheap:** [optimizing-spark-jobs](optimizing-spark-jobs/SKILL.md) /
  [tuning-warehouse-performance](tuning-warehouse-performance/SKILL.md) →
  [optimizing-data-costs](optimizing-data-costs/SKILL.md).

## Cross-category links

- **SQL authoring & app perf:** [../software-engineering/authoring-sql-queries](../software-engineering/authoring-sql-queries/SKILL.md),
  [../software-engineering/optimizing-code-performance](../software-engineering/optimizing-code-performance/SKILL.md).
- **Review gates:** [../review/reviewing-sql](../review/reviewing-sql/SKILL.md),
  [../review/reviewing-architecture](../review/reviewing-architecture/SKILL.md).
- **Reporting on top of the data:** [../office/designing-dashboards](../office/designing-dashboards/SKILL.md),
  [../office/generating-data-reports](../office/generating-data-reports/SKILL.md),
  [../business/defining-kpis](../business/defining-kpis/SKILL.md).
