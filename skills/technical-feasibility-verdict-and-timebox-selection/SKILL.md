---
name: technical-feasibility-verdict-and-timebox-selection
description: Use when the four feasibility probes have resolved (or a spike timebox has expired) and you must set the bare verdict field, route conditions/prerequisites/scope-constraints to the correct record location, or decide whether a blocked probe, an inconclusive timebox, or new post-verdict evidence changes the verdict rather than being logged as prose.
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

## Rules

1. **when** a blocking condition can only be resolved outside this
   repo's own work (e.g. a vendor contract, a third-party API grant, a
   legal sign-off) **choose** `verdict: conditional` with that
   condition in the `conditions:` list — never `go` with the condition
   buried in prose, because a condition outside `conditions:` is
   invisible to any automated gate checking for open blockers.
   source: this role's own directive (feasibility/hooks/directive.sh,
   this repo): "a blocking condition that cannot proceed until
   resolved EXTERNALLY ... -> verdict: conditional, the blocking
   condition in the conditions: list".

2. **when** a prerequisite is two-way (reversible) and resolvable
   entirely within this repo's own future work **choose** `verdict:
   go` with the prerequisite recorded via the `verdict_provisional`
   body convention, never placed in `conditions:` — `conditions:` is
   reserved for external blockers only, so an internal prerequisite
   there would misrepresent an in-repo task as an external dependency.
   source: same role directive, this repo: "a prerequisite that is
   two-way (reversible) and resolvable WITHIN the repo's own work ->
   verdict: go, with the prerequisite recorded via the
   verdict_provisional convention ... never in conditions:".

3. **when** the evaluation only covered a bounded scope (e.g. one
   deployment target, one data region) and found no blocker within
   that scope **choose** `verdict: go` with the scope boundary stated
   plainly in the record body — a scope constraint is not a condition
   and not a prerequisite, and forcing it into either field
   misclassifies a boundary-of-what-was-checked as a thing that must
   still happen.
   source: same role directive, this repo: "a scope constraint only
   (no blocking or resolvable prerequisite, just a boundary on what
   was evaluated) -> verdict: go, the constraint stated in the record
   body".

4. **when** filling in the `verdict` field itself **choose** the bare
   enum value only (`go`, `no-go`, or `conditional`) — never append
   the condition text, a percentage, or a qualifier to the field value
   — because every condition/prerequisite/constraint narrative belongs
   in the record body, and encoding it into the field breaks any
   mechanical parser that expects one of exactly three values.
   source: same role directive, this repo: "The verdict field itself
   carries the bare enum value only — every condition, prerequisite,
   or constraint narrative lives in the record body, never appended to
   or encoded in the field."

5. **when** all four probes (technical, prior_art, legal_regulatory,
   threat_model) have not yet each individually resolved to
   pass/fail/blocked with cited evidence **choose** withhold any
   verdict at all, not a placeholder `conditional` — a verdict issued
   before all four probes resolve is not provisional caution, it is a
   rule violation of this role's own gating requirement.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "No verdict until ALL FOUR probes
   resolve to pass:<evidence> | fail:<evidence> | blocked:<evidence>."

6. **when** a market argument was supplied alongside the spec (a
   business case, revenue projection, or urgency narrative) **choose**
   read and evaluate the specification with that argument explicitly
   set aside, and record `market_argument_supplied: false` (or
   `true` with the argument's presence noted but excluded from the
   verdict reasoning) — a verdict argued from "but this will make
   money" is not a feasibility verdict, it is advocacy wearing a
   feasibility record's shape.
   source: role directive, this repo (feasibility/hooks/directive.sh):
   "read the specification DELIBERATELY WITHOUT the market argument
   that motivated it ... Record market_argument_supplied: false
   explicitly: the record must SAY the argument was withheld, not
   merely omit it."

7. **when** a spike's timebox (1-3 days) expires with an inconclusive
   finding **choose** stop and escalate extend-vs-stop to the human,
   never quietly extend the box or quietly issue a verdict on
   incomplete evidence to avoid the escalation — both silent paths
   defeat the reason a pre-agreed timebox exists.
   source: role directive, this repo (feasibility/hooks/directive.sh):
   "A timebox that expires without a conclusive answer STOPS and puts
   extend-vs-stop to the human — never silently continues."

8. **when** a verdict has already been reached and new information
   surfaces that seems to call it into question **choose** require a
   new probe finding (fresh evidence on one of the four probes) before
   revising — an unsupported "on reflection" revision without a new
   probe result is not a legitimate basis to reopen a closed verdict.
   source: role directive, this repo (feasibility/hooks/directive.sh):
   "Once at verdict, refuse to revise without a new probe finding."

9. **when** deciding between a `conditional` verdict with many
   conditions versus splitting the spec into a smaller feasible slice
   plus a separately-gated remainder **choose** the split when the
   blocking conditions only affect part of the spec's scope — a
   `conditional` verdict that bundles a genuinely feasible core with
   an infeasible periphery under one blanket condition list obscures
   which part is actually blocked and delays shipping the feasible
   core.
   source: verdict-selection-criteria mechanical rule (per condition
   class, evaluated per blocking item, not per whole spec), role
   directive, this repo (feasibility/hooks/directive.sh) — the
   per-condition-class mechanism implies per-condition scoping rather
   than whole-spec bundling.

10. **REMOVAL — when** a `verdict_provisional` prerequisite recorded
    in an earlier `go` record has since been completed and merged
    **choose** remove the stale `verdict_provisional` line from the
    record on the next update rather than leaving it dangling as an
    apparently-still-open prerequisite — a completed prerequisite left
    in the body reads as an unresolved condition to any later reader
    or gate, misrepresenting a closed item as open.
    source: `verdict_provisional` body-level convention definition,
    role directive, this repo (feasibility/hooks/directive.sh): "it
    marks a go verdict's in-repo-resolvable prerequisite" — a marker
    for an open prerequisite has no defined meaning once that
    prerequisite is closed, so carrying it forward stale is an
    unsupported claim.

11. **when** a probe finding resolves to `blocked:<evidence>` **choose**
    treat that as a mechanical hard stop on the verdict field itself,
    not as a caveat noted in the record body while an otherwise-ready
    verdict still gets written — a blocking condition logged only as
    prose next to a passing-looking verdict lets a later reader (or an
    automated gate scanning for the verdict field) miss that the
    verdict was never actually cleared to resolve.
    source: survey of vulnerability-scanning tools' CI gates —
    a quick-scan pipeline can ship a "fail-on" gate that mechanically
    stops the pipeline outcome on a qualifying finding, rather than
    surfacing the finding only as an informational note in a report
    that still reads as passing.
