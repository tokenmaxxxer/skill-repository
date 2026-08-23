---
name: technical-feasibility-verdict-and-timebox-selection
description: >-
  Use when the four feasibility probes have resolved (or a spike timebox has
  expired) and you must set the bare verdict field, route
  conditions/prerequisites/scope-constraints to the correct record location, or
  decide whether a blocked probe, an inconclusive timebox, or new post-verdict
  evidence changes the verdict rather than being logged as prose. Trigger on
  requests like "verdict go로 할까 conditional로 할까", "feasibility verdict field",
  "timebox expired without an answer", "where do the conditions go". Do NOT use
  for classifying a decision's reversibility or scoping the spike itself (use
  technical-feasibility-reversibility-and-spike-scoping).
metadata:
  axis: verdict-and-timebox-selection
  rule_count_floor: 10
  axes:
    - reversibility-and-spike-scoping
    - build-vs-buy-dependency-health
    - license-and-regulatory-risk
    - threat-model-disposition
    - verdict-and-timebox-selection
---

# Decision axis: verdict selection & timebox governance

## Trigger

Use this axis once the other four probes (technical, prior_art,
legal_regulatory, threat_model) have each individually reported a
pass/fail/blocked result, or once an in-flight spike's timebox has
expired — the question here is not whether a dependency is healthy, a
license is compatible, or a threat is disposed (those are the sibling
axes' job), but how to fold those already-settled findings into the
single `verdict` field, where to place any condition/prerequisite/
scope-constraint text, and whether a blocked probe, an inconclusive
timebox, or fresh post-verdict evidence should change that field at
all.

## Procedure

1. If a blocker can only be resolved by an outside party (vendor,
   third party, legal), set `verdict: conditional` and record the
   blocker in `conditions:` (rule 1).
2. If a prerequisite is reversible and resolvable entirely in-repo,
   set `verdict: go` and record it via the `verdict_provisional`
   convention, not in `conditions:` (rule 2).
3. If the evaluation only covered a bounded scope and found no
   blocker there, set `verdict: go` and state the scope boundary
   plainly in the record body (rule 3).
4. When writing the `verdict` field, use only the bare enum value
   (`go`, `no-go`, `conditional`) and keep all narrative in the record
   body (rule 4).
5. Withhold any verdict, including a placeholder `conditional`, until
   all four probes have each resolved with cited evidence (rule 5).
6. If a market argument accompanied the spec, evaluate the spec with
   that argument set aside and record `market_argument_supplied`
   explicitly (rule 6).
7. When a spike's timebox expires inconclusively, stop and escalate
   extend-vs-stop to a human — do not silently extend or force a
   verdict (rule 7).
8. Refuse to revise an already-reached verdict unless new evidence
   from one of the four probes supports the revision (rule 8).
9. When conditions would only block part of the spec's scope, split
   the spec into a feasible slice plus a separately-gated remainder
   instead of bundling everything under one `conditional` verdict
   (rule 9).
10. When an earlier `go` record's `verdict_provisional` prerequisite
    has since been completed and merged, remove the stale line on the
    next update rather than leaving it dangling (rule 10).
11. Treat any probe finding resolved as `blocked:<evidence>` as a
    mechanical hard stop on the verdict field itself, not merely a
    caveat noted in the body next to an otherwise-passing verdict
    (rule 11).

## Output shape

Applying this skill produces a feasibility record's final `verdict`
field carrying a bare `go` / `no-go` / `conditional` value, together
with any conditions, provisional prerequisites, or scope constraints
placed in their correct dedicated location in the record body (never
folded into the field itself) — this is the axis that closes out the
record, so its output is the durable, mechanically parseable verdict
for the record, not a new timebox or reversibility tag (those are set
upstream by the sibling axes and only carried forward here).

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **when** a blocking condition can only be resolved outside this repo's own work (e.g. a vendor contract, a third-party API grant, a legal sign-off) **choose** `verdict:…
- 1.2 — **when** a prerequisite is two-way (reversible) and resolvable entirely within this repo's own future work **choose** `verdict: go` with the prerequisite recorded via th…
- 1.3 — **when** the evaluation only covered a bounded scope (e.g. one deployment target, one data region) and found no blocker within that scope **choose** `verdict: go` with t…
- 1.4 — **when** filling in the `verdict` field itself **choose** the bare enum value only (`go`, `no-go`, or `conditional`) — never append the condition text, a percentage, or…
- 1.5 — **when** all four probes (technical, prior_art, legal_regulatory, threat_model) have not yet each individually resolved to pass/fail/blocked with cited evidence **choose…
- 1.6 — **when** a market argument was supplied alongside the spec (a business case, revenue projection, or urgency narrative) **choose** read and evaluate the specification wit…
- 1.7 — **when** a spike's timebox (1-3 days) expires with an inconclusive finding **choose** stop and escalate extend-vs-stop to the human, never quietly extend the box or quie…
- 1.8 — **when** a verdict has already been reached and new information surfaces that seems to call it into question **choose** require a new probe finding (fresh evidence on on…
- 1.9 — **when** deciding between a `conditional` verdict with many conditions versus splitting the spec into a smaller feasible slice plus a separately-gated remainder **choose…
- 1.10 — **REMOVAL — when** a `verdict_provisional` prerequisite recorded in an earlier `go` record has since been completed and merged **choose** remove the stale `verdict_provi…
- 1.11 — **when** a probe finding resolves to `blocked:<evidence>` **choose** treat that as a mechanical hard stop on the verdict field itself, not as a caveat noted in the recor…
