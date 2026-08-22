# Survey — issue #63: never-mounted skill curation pass

## Skill catalog

`skills/` holds 248 skill directories today (checked out at this session's HEAD, `fa1b95b`). Matches the issue's `206/248` denominator.

## Census reproduction attempt

Tried to reproduce "42/248 never mounted, 614 session logs" from on-disk evidence under `~/.tokenmaxxxer/work` (1218 `consult-log.md` files, 623 `*.session.*.log` files, 322 `*.task.txt` files). Three independent mount signals were searched:

1. **Explicit `Skill` tool invocations** — `"name":"Skill"` tool-use events with a `"skill":"<name>"` input, grepped across all `*.session.*.log`. Found 18 distinct skills invoked this way (e.g. `market-recon` ×8, `content-design-operational-playbook` ×2, 16 others ×1).
2. **`verb=skill_judge` picks** — the `consult-log.md` line format this session itself just wrote (`outcome='ok: picked=[...] rejected=[...]'`). Only 32 such entries exist across all 1218 `consult-log.md` files repo-wide; extracting `picked=[...]` skill names added a handful more to the mounted set.
3. **Role→family mapping headers** — the `"이 역할은 skill-repository(...)로 매핑됐다: 스킬 X — ..., Y — ..."` block that this very session's own prompt carries (5 skills mounted for `knowledge-management`). Searched for this marker text and the `available for use with the Skill tool` framing across every log/task file; only 40 files carry either marker at all, out of 945 candidate files.

Union of all three signals: **31 skills with any observed mount signal**, leaving 217 with zero — nowhere close to the issue's `206 mounted / 42 never`.

**Conclusion (open finding):** the role-mapping header and the `Skill`-tool-invocation instrumentation are recent additions to the harness — they appear in a small, recent slice of the corpus (the 40-file / 18-skill signal), not uniformly across the 614 logs the original census drew on. Whatever produced the `614 logs` count either read a broader/different log corpus than what is present under `~/.tokenmaxxxer/work` in this checkout, or used mount telemetry not persisted to a grep-able text artifact here (e.g. in-memory routing state, or a harness-internal event store). **A byte-for-byte reproduction of the orchestrator's original 42-skill list is not achievable from the artifacts available to this session.** This is flagged as an open finding rather than papered over with a fabricated list.

## Structural analysis (used in place of exact log reproduction)

Since the issue's own reasoning for *why* a skill goes unmounted is structural — "the role→family mapping structurally never picks" a skill — that structure can be checked directly from the catalog, independent of log volume. Skills fall into two shapes:

- **Family-routable**: 3+ skills share a domain prefix that maps onto an existing role (`api-design-*`, `architecture-*`, `brand-design-*`, `capacity-planning-*`, `conformance-review-*`, `customer-support-*`, `localization-*`, `ml-engineering-*`, `pricing-*`, `release-engineering-*`, `sales-*`, `secure-coding-*`, `technical-writing-*`, `ux-engineering-*`, `finance-unit-economics-*`, `growth-analytics-*`, `partnerships-bd-*`, `legal-compliance-*`, `market-analysis-*`, `data-engineering-*`, `data-modeling-*`, `incident-response-*`, `kubernetes-workload-*`, `risk-management-*`, `defect-verification-*`, `user-discovery-*`, `devrel-*`, `marketing-*`, `implementation-*` where multiple exist, `observability-*`). A brand-new such family (`design-artifact-*`, a `knowledge-work` deck family, if/when it lands) is the issue's "too-new" bucket — it will mount once matching issues route to it; no action needed beyond time.
- **Orchestrator/general-methodology-shaped**: skills that are standalone (no sibling in the catalog shares a role-mappable prefix) and whose trigger describes a cross-cutting judgment call rather than a role's domain: e.g. `decision-brief`, `diagnose-first`, `fmea`, `premortem`, `adversarial-review`, `stride`, `flow-metrics`, `compliance-scan`, `decision-records`, `agent-coordination`, `blameless-postmortem`, `overengineering-audit`, `parallel-decomposition`, `merge-gates`, `model-routing`, `premature-scaling`, `market-recon`, `prior-art-scan`, `reference-forecast`, `launch-readiness`, `hypothesis-testing`, `experiment-trust`, `team-safety-measure`, `tech-feasibility`, `silent-failure-audit`, `work-in-english`, `prose-modes`. These match every skill the issue names explicitly, confirming the structural test is a reasonable proxy for the real 42, even though it is not a verified enumeration of it.

## Consulted skill influence

`knowledge-management-curation-pruning` was consulted (see `docs/issue-63/reports/consult-log.md`). Its rule 10 is load-bearing for this proposal's verdict criteria: **never-mounted alone is not grounds for merge/retire** — pruning targets inaccurate, outdated, or redundant content, not merely-unpopular content. A correct, unique, never-cited skill is exactly the kind of tail knowledge a curated library should keep (route), not cut. Rule 4/9 (merge near-duplicates into the single best-written entry, fold attribution into provenance) shapes the merge-retire verdict's mechanics; rule 3 (supersede when the underlying decision no longer holds, vs. update in place when only a fact changed) maps directly onto the reclassify vs. merge-retire boundary in the proposal.

## Open finding carried into the proposal

The proposal below defines verdict criteria and applies them to the issue's explicitly-named skills plus the structurally-derived orchestrator-shaped set, but **cannot certify that this list is the exact 42** the orchestrator counted. The proposal's first mechanical step is a runnable census script so phase 2 (or a re-run with access to the orchestrator's original log corpus) can confirm or correct the list before the mechanical follow-through (trigger edits, merges, retirements) executes against it.
