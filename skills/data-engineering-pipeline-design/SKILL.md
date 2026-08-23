---
name: data-engineering-pipeline-design
description: Use when choosing ETL vs ELT, picking an idempotency pattern, requiring exactly-once-effective semantics, naming a data owner/steward, routing a schema change through change control, retiring an unused hop, structuring a task graph, or authoring a dbt-style model.
metadata:
  axis: pipeline-design
  rule_count_floor: 10
---

# Pipeline design — decision rules

Condition → choice → source. Each rule is `addition` or `**REMOVAL**`.

## Trigger

Apply this skill when choosing ETL vs ELT (or a split) for a new
pipeline, choosing an idempotency pattern for a batch or streaming
sink, deciding whether a business-critical use case needs
exactly-once-effective semantics, naming a data owner/steward,
routing a schema-affecting change through change control, retiring
an unused hop or a duplicated pre-load check, structuring multi-step
dependencies as a task graph, or authoring/reviewing a dbt-style
transform model's naming and test conventions. This is distinct from
data-quality (authoring completeness/uniqueness/accuracy/freshness
checks) and failure-handling (retry/DLQ classification, recovery,
RTO) — both are separate axes in this family.

## Procedure

1. Choose ETL, ELT, or a per-domain split by compute location, team
   skill, and regulatory constraints (rules 1-3).
2. Design any retryable transform/sink step to be idempotent before
   it ships (rule 4).
3. Pick the idempotency pattern for the step: overwrite-partition for
   a batch load, upsert-on-primary-key for a streaming/incremental
   sink (rules 5-6).
4. For an aggregation-sensitive or business-critical use case,
   require exactly-once-effective semantics via idempotent upsert
   (rule 7).
5. Name an accountable owner and a day-to-day steward before the
   pipeline ships (rule 8).
6. Route any schema- or semantics-affecting change through the named
   owner as change control, not a silent deploy (rule 9).
7. Drop a transform step or table that no downstream consumer reads,
   and remove a pre-load check that duplicates an existing
   warehouse-side gate (rules 10-11).
8. Express real multi-step dependencies as an explicit task graph
   with per-task retry/backfill, rather than a flat script (rule 12).
9. In a SQL transform chain, reference each upstream model by name
   and attach at least one machine-checkable test to its output
   (rule 13).
10. Once ownership spans more than a few pipelines, publish each
    dataset's owner, schema, and lineage to a queryable central
    location (rule 14).
11. Before authoring a new dbt-style model, read 2-3 existing models
    in the project and match their naming/layering convention
    (rule 15).

## Output shape

A pipeline-design decision: the applicable rule number(s), the
pattern chosen (ETL/ELT, idempotency approach, orchestration shape,
or ownership/change-control action), and the resulting design or
governance artifact.

1. When the destination warehouse/lakehouse has enough spare compute to
   run transforms in-place and the team's strongest skill is SQL, choose
   ELT (land raw, transform in the warehouse) over ETL. **addition**
   source: [Fivetran — Data Pipeline vs. ETL](https://www.fivetran.com/learn/data-pipeline-vs-etl), [Stripe — ETL vs ELT Pipelines](https://stripe.com/resources/more/etl-vs-elt-pipelines)

2. When the destination system has limited compute, or a regulation
   (GDPR/HIPAA/CCPA-class) requires masking/validation before data is
   persisted, choose ETL (transform before load) over ELT. **addition**
   source: [Domo — ETL Pipeline vs Data Pipeline](https://www.domo.com/learn/article/etl-pipeline-vs-data-pipeline)

3. When some source domains need strict pre-load validation (PII,
   financial) and others don't, split the pipeline: run ETL for the
   regulated domains and ELT for the rest, rather than forcing one
   pattern across the whole pipeline. **addition**
   source: [Domo — ETL Pipeline vs Data Pipeline](https://www.domo.com/learn/article/etl-pipeline-vs-data-pipeline)

4. When a task can be retried by an orchestrator (network blip, timeout,
   restart — the normal case for any scheduled pipeline), design the
   transform/sink step to be idempotent (same input twice = same
   downstream state) rather than relying on "this won't run twice."
   **addition**
   source: [Airbyte — Idempotency in Data Pipelines](https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines)

5. When idempotency is needed for a batch load, prefer overwrite-the-
   whole-partition (replace the complete partition for the period being
   processed) over row-level dedup logic — it is the simplest pattern
   that is provably correct under retries. **addition**
   source: [Airbyte — Idempotency in Data Pipelines](https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines)

6. When idempotency is needed for a streaming/incremental sink, prefer
   upsert-on-primary-key (MERGE / ON CONFLICT) at the destination over
   building custom duplicate-suppression logic in the pipeline code.
   **addition**
   source: [Airbyte — Idempotency in Data Pipelines](https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines)

7. When the use case is aggregation-sensitive or business-critical
   (fraud detection, inventory counts, billing), require exactly-once
   *effective* semantics (via idempotent upsert, not a literal
   exactly-once delivery guarantee, which distributed systems rarely
   provide) — do not settle for plain at-least-once with no dedup layer.
   **addition**
   source: [Airbyte — Idempotency in Data Pipelines](https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines)

8. When a dataset has more than one plausible owning team, name exactly
   one accountable data owner (decision authority) plus a data steward
   (day-to-day quality/definitions) before the pipeline ships — per
   DAMA-DMBOK's owner/steward/custodian split — rather than leaving
   ownership implicit in "whoever built it." **addition**
   source: [OvalEdge — DAMA-DMBOK Data Governance Framework](https://www.ovaledge.com/blog/dama-dmbok-data-governance-framework)

9. When a pipeline change alters a downstream-consumed schema or
   semantics, route it through the named data owner as a change-control
   decision (not a silent deploy) — DAMA-DMBOK treats governance as
   control-plus-planning, not a one-time design artifact. **addition**
   source: [OvalEdge — DAMA-DMBOK Data Governance Framework](https://www.ovaledge.com/blog/dama-dmbok-data-governance-framework)

10. When a transform step or intermediate table exists only because an
    earlier design assumed a downstream consumer that no longer reads
    it, drop the step/table rather than keeping it "in case something
    still needs it" — an unused hop is pure risk (a place data can go
    stale or leak) with no offsetting benefit. **REMOVAL**
    source: [Adams, Converse, Hales & Klotz — People systematically overlook subtractive changes, *Nature* 592 (2021)](https://www.nature.com/articles/s41586-021-03380-y) (people default to additive fixes and under-consider removing the unneeded hop)

11. When a hybrid ETL/ELT pipeline has accreted pre-load validation
    steps that duplicate checks the warehouse-side data-quality gate
    already enforces, remove the duplicated pre-load check rather than
    keeping both — duplicated validation is an additive habit, not
    evidence of extra safety. **REMOVAL**
    source: [Adams, Converse, Hales & Klotz — People systematically overlook subtractive changes, *Nature* 592 (2021)](https://www.nature.com/articles/s41586-021-03380-y)

12. When a pipeline has more than a couple of sequential steps with
    real dependencies between them (extract must finish before
    transform, transform before load), express those dependencies as
    an explicit task graph with per-task retry and backfill, rather
    than encoding order as one monolithic script or a flat cron
    sequence — a task graph lets a failed downstream step be retried
    or backfilled on its own, without rerunning upstream steps that
    already succeeded. This is a separate concern from idempotency
    (items 4-7): idempotency makes a rerun safe, a task graph makes a
    partial rerun possible in the first place. **addition**
    source: [Apache Airflow — GitHub](https://github.com/apache/airflow)

13. When a transform step is a chain of SQL models, reference each
    upstream model by name rather than a hard-coded table path, and
    attach at least one machine-checkable test to each model's output
    (not-null / accepted-values / referential integrity at minimum) —
    a named-reference chain plus per-model tests keeps the transform
    DAG's shape and correctness verifiable from the code itself,
    rather than resting on tribal knowledge of execution order.
    **addition**
    source: [dbt-core — GitHub](https://github.com/dbt-labs/dbt-core)

14. When more than a handful of pipelines read from or write to a
    shared warehouse, publish each dataset's owner, schema, and
    upstream/downstream lineage to a queryable central location,
    rather than leaving that information only inside a pipeline's own
    code or a single owner's head — the goal is that an unfamiliar
    team can look up a dataset's lineage without asking a person. This
    goes beyond naming an owner once (item 8): it makes the ownership
    and lineage lookup itself a first-class, shared artifact.
    **addition**
    source: [DataHub — GitHub](https://github.com/datahub-project/datahub)

15. When authoring a new dbt-style transform model or changing an
    existing one, read 2-3 existing models in the same project first and
    match their naming/layering convention, rather than writing to a
    generic best-practice pattern that may not be this project's own —
    an agent (human or AI) that skips convention discovery produces a
    model that compiles but doesn't fit the project's actual DAG shape.
    **addition**
    source: [AltimateAI — data-engineering-skills, 118 GitHub stars](https://github.com/AltimateAI/data-engineering-skills), [Altimate AI — Teaching Claude Code the art of data engineering](https://blog.altimate.ai/teaching-claude-code-the-art-of-data-engineering-introducing-altimate-skills)
