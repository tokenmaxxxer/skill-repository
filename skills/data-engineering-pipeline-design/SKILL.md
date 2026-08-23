---
name: data-engineering-pipeline-design
description: >-
  Use when choosing ETL vs ELT, picking an idempotency pattern, requiring
  exactly-once-effective semantics, naming a data owner/steward, routing a
  schema change through change control, retiring an unused hop, structuring a
  task graph, or authoring a dbt-style model. Trigger on requests like "ETL이 나아
  ELT가 나아", "idempotent pipeline design", "exactly-once semantics", "dbt model
  naming conventions". Do NOT use for classifying failures, DLQ routing, and
  recovery once the pipeline breaks (use data-engineering-failure-handling).
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

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When the destination warehouse/lakehouse has enough spare compute to run transforms in-place and the team's strongest skill is SQL, choose ELT (land raw, transform in th…
- 1.2 — When the destination system has limited compute, or a regulation (GDPR/HIPAA/CCPA-class) requires masking/validation before data is persisted, choose ETL (transform befo…
- 1.3 — When some source domains need strict pre-load validation (PII, financial) and others don't, split the pipeline: run ETL for the regulated domains and ELT for the rest, r…
- 1.4 — When a task can be retried by an orchestrator (network blip, timeout, restart — the normal case for any scheduled pipeline), design the transform/sink step to be idempot…
- 1.5 — When idempotency is needed for a batch load, prefer overwrite-the- whole-partition (replace the complete partition for the period being processed) over row-level dedup l…
- 1.6 — When idempotency is needed for a streaming/incremental sink, prefer upsert-on-primary-key (MERGE / ON CONFLICT) at the destination over building custom duplicate-suppres…
- 1.7 — When the use case is aggregation-sensitive or business-critical (fraud detection, inventory counts, billing), require exactly-once *effective* semantics (via idempotent…
- 1.8 — When a dataset has more than one plausible owning team, name exactly one accountable data owner (decision authority) plus a data steward (day-to-day quality/definitions)…
- 1.9 — When a pipeline change alters a downstream-consumed schema or semantics, route it through the named data owner as a change-control decision (not a silent deploy) — DAMA-…
- 1.10 — When a transform step or intermediate table exists only because an earlier design assumed a downstream consumer that no longer reads it, drop the step/table rather than…
- 1.11 — When a hybrid ETL/ELT pipeline has accreted pre-load validation steps that duplicate checks the warehouse-side data-quality gate already enforces, remove the duplicated…
- 1.12 — When a pipeline has more than a couple of sequential steps with real dependencies between them (extract must finish before transform, transform before load), express tho…
- 1.13 — When a transform step is a chain of SQL models, reference each upstream model by name rather than a hard-coded table path, and attach at least one machine-checkable test…
- 1.14 — When more than a handful of pipelines read from or write to a shared warehouse, publish each dataset's owner, schema, and upstream/downstream lineage to a queryable cent…
- 1.15 — When authoring a new dbt-style transform model or changing an existing one, read 2-3 existing models in the same project first and match their naming/layering convention…
