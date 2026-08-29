# technical-feasibility-verdict-and-timebox-selection — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## Rules

1. **when** a blocking condition can only be resolved outside this
   repo's own work (e.g. a vendor contract, a third-party API grant, a
   legal sign-off) **choose** `verdict: conditional` with that
   condition in the `conditions:` list — never `go` with the condition
   buried in prose, because a condition outside `conditions:` is
   invisible to any automated gate checking for open blockers.
   source: this skill's own directive (feasibility/hooks/directive.sh,
   this repo): "a blocking condition that cannot proceed until
   resolved EXTERNALLY ... -> verdict: conditional, the blocking
   condition in the conditions: list".

2. **when** a prerequisite is two-way (reversible) and resolvable
   entirely within this repo's own future work **choose** `verdict:
   go` with the prerequisite recorded via the `verdict_provisional`
   body convention, never placed in `conditions:` — `conditions:` is
   reserved for external blockers only, so an internal prerequisite
   there would misrepresent an in-repo task as an external dependency.
   source: same skill directive, this repo: "a prerequisite that is
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
   source: same skill directive, this repo: "a scope constraint only
   (no blocking or resolvable prerequisite, just a boundary on what
   was evaluated) -> verdict: go, the constraint stated in the record
   body".

4. **when** filling in the `verdict` field itself **choose** the bare
   enum value only (`go`, `no-go`, or `conditional`) — never append
   the condition text, a percentage, or a qualifier to the field value
   — because every condition/prerequisite/constraint narrative belongs
   in the record body, and encoding it into the field breaks any
   mechanical parser that expects one of exactly three values.
   source: same skill directive, this repo: "The verdict field itself
   carries the bare enum value only — every condition, prerequisite,
   or constraint narrative lives in the record body, never appended to
   or encoded in the field."

5. **when** all four probes (technical, prior_art, legal_regulatory,
   threat_model) have not yet each individually resolved to
   pass/fail/blocked with cited evidence **choose** withhold any
   verdict at all, not a placeholder `conditional` — a verdict issued
   before all four probes resolve is not provisional caution, it is a
   rule violation of this skill's own gating requirement.
   source: feasibility skill directive, this repo
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
   source: skill directive, this repo (feasibility/hooks/directive.sh):
   "read the specification DELIBERATELY WITHOUT the market argument
   that motivated it ... Record market_argument_supplied: false
   explicitly: the record must SAY the argument was withheld, not
   merely omit it."

7. **when** a spike's timebox (1-3 days) expires with an inconclusive
   finding **choose** stop and escalate extend-vs-stop to the human,
   never quietly extend the box or quietly issue a verdict on
   incomplete evidence to avoid the escalation — both silent paths
   defeat the reason a pre-agreed timebox exists.
   source: skill directive, this repo (feasibility/hooks/directive.sh):
   "A timebox that expires without a conclusive answer STOPS and puts
   extend-vs-stop to the human — never silently continues."

8. **when** a verdict has already been reached and new information
   surfaces that seems to call it into question **choose** require a
   new probe finding (fresh evidence on one of the four probes) before
   revising — an unsupported "on reflection" revision without a new
   probe result is not a legitimate basis to reopen a closed verdict.
   source: skill directive, this repo (feasibility/hooks/directive.sh):
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
   class, evaluated per blocking item, not per whole spec), skill
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
    skill directive, this repo (feasibility/hooks/directive.sh): "it
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

