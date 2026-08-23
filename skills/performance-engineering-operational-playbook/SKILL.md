---
name: performance-engineering-operational-playbook
description: >-
  Use when diagnosing an unexplained slowdown with no prior hypothesis, setting or reporting a
  latency/SLO/error-budget target, assessing queue/pool/connection-pool pressure, or choosing
  between a removal-shaped and addition-shaped fix. Condition-matched decision rules: USE-method
  checks before profiling, percentile (never mean) latency reporting, SLI then SLO then error-
  budget ordering before alerts, Little's Law grounding for wait-time claims, and removal-first
  fixes (N+1 queries, connection leaks) before scaling a database or pool. Trigger on requests
  like "서비스가 왜 이렇게 느리지", "레이턴시 SLO 잡아줘", "p99 latency is spiking", "our queue keeps backing up",
  "set an error budget". Do NOT use for choosing a data structure or algorithm inside code (use
  implementation-performance-data-structure-choice) or for non-performance root-cause hunts
  (diagnose-first).
metadata:
  subject: issue-1174
  layer_program: docs/issue-1174/proposals/operational-playbook-program.md
---

# Performance-engineering operational playbook

Numbered condition → choice → source rules, three research layers:
(A) practitioner decision rules, (B) named methodologies verified at
source, (C) academic/theoretical grounding. REMOVAL-category rules are
marked `[REMOVAL]`.

## Trigger

Apply this skill when diagnosing a service that is "slow" with no prior
hypothesis (rule 1), reporting or alerting on request latency (rule 2),
deciding how strict an SLO/error budget should be (rule 3), a queue,
worker pool, or connection pool is running hot or periodically exhausted
(rules 4–6), choosing a fix among several that close the same
latency/capacity gap (rule 7), starting a performance investigation with
no existing dashboard coverage (rule 8), defining what "reliable enough"
means before setting alerts (rule 9), or justifying a wait-time or
capacity claim across arrival-rate variation (rule 10).

## Procedure

1. Practitioner decision rules (rules 1–7): check Utilization,
   Saturation, and Errors per resource before touching code; report
   latency by percentile, never the mean; set SLO targets below 100% and
   track error-budget burn rate; treat a hot queue/pool as an imminent
   wait-time cliff; remove N+1 queries and connection leaks before
   scaling the database or pool (`[REMOVAL]`, rules 5–6); prefer a
   removal-shaped fix over an addition-shaped one when both close the
   same gap.
2. Named methodologies verified at source (rules 8–9): apply the USE
   Method systematically before any application-level profiling; define
   SLI → SLO → error budget in that order before setting an alert
   threshold.
3. Academic/theoretical grounding (rule 10): ground any wait-time or
   capacity claim in Little's Law (L = λW) rather than a single point
   measurement, stating explicitly that it predicts long-run averages.

## Output shape

A cited condition → choice → source decision for the triggering
performance question, plus — when a REMOVAL-category rule (5, 6, or 7)
applies — which removal-shaped fix took precedence over an
addition-shaped alternative and why.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **Condition:** a service is "slow" with no prior hypothesis. **Choice:** check Utilization, Saturation, Errors for every candidate resource (CPU, memory, disk I/O, netwo…
- 1.2 — **Condition:** reporting or alerting on request latency. **Choice:** report p50/p95/p99 (or p99.9 for latency-sensitive paths like checkout/auth), never the mean — mean…
- 1.3 — **Condition:** deciding how strict an SLO/error budget should be. **Choice:** set the target below 100% deliberately and track burn rate against a budget (1 − SLO), not…
- 1.4 — **Condition:** a queue/pool/worker pool is running "hot" (util near 100%) but not yet erroring. **Choice:** treat it as an imminent wait-time cliff and act before errors…
- 1.5 — **[REMOVAL] Condition:** an ORM-driven code path issues one query per loop iteration (N+1 pattern) discovered during USE/latency triage. **Choice:** remove the per-itera…
- 1.6 — **[REMOVAL] Condition:** a connection pool is periodically exhausted or timing out under normal (non-spike) load. **Choice:** first remove connection leaks (unreleased c…
- 1.7 — **Condition:** choosing a fix among several that close the same latency/capacity gap. **Choice:** prefer the removal-shaped fix (delete redundant work: a query, a cache…
- 2.8 — **Condition:** starting any performance investigation with no existing dashboard coverage. **Choice:** apply the USE Method systematically (per-resource utilization/satu…
- 2.9 — **Condition:** defining what "reliable enough" means for a service before setting alerts. **Choice:** define SLI → SLO → error budget in that order (measure first, targe…
- 3.10 — **Condition:** justifying why a wait-time or capacity claim is valid across arrival-rate variation, not just at the measured sample. **Choice:** ground the claim in Litt…
- S1 — Evidence trail → references/rules.md
