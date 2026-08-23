---
name: technical-feasibility-threat-model-disposition
description: Use when a spec's STRIDE table rows and dispositions need to be built or checked, as opposed to deciding reversibility/spike scope, dependency build-vs-buy health, license/regulatory exposure, or the final verdict/timebox.
metadata:
  axis: threat-model-disposition
  rule_count_floor: 10
  axes:
    - reversibility-and-spike-scoping
    - build-vs-buy-dependency-health
    - license-and-regulatory-risk
    - threat-model-disposition
    - verdict-and-timebox-selection
---

# Decision axis: threat-model disposition (STRIDE)

## Trigger

Use when a spec's threats need to be enumerated and each one classified into a STRIDE category and given a terminal disposition (mitigated, accepted, or deferred) — distinct from the sibling axes, which decide whether a probed element is a one-way or two-way door (reversibility-and-spike-scoping), whether a dependency itself is healthy enough to build on (build-vs-buy-dependency-health), whether a dependency or design choice carries license or regulatory exposure (license-and-regulatory-risk), or how to roll all four probes into a final verdict and timebox (verdict-and-timebox-selection).

## Procedure

1. Build a data-flow diagram of the spec (processes, data stores, data flows, external entities) and derive the elements to model from it, not from an ad hoc "important things" list (rule 3).
2. For each element, create one STRIDE table row per (element, category, trust boundary) triple — never collapse all six categories into one free-text cell (rule 1).
3. Classify each threat using only the six fixed STRIDE categories — Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege (rule 2).
4. At every trust boundary crossing two elements of different privilege levels, add a dedicated row for each plausible STRIDE category at that crossing, even if a category was already covered for one element alone (rule 4).
5. Do not drop Denial-of-service rows for elements the spec marks "not internet-facing" — assess DoS for internal actors and internal boundaries too (rule 9).
6. Give every completed row a disposition of exactly `mitigated`, `accepted`, or `deferred` — never leave a row blank or in-progress (rule 5).
7. For any row dispositioned `deferred`, attach a named follow-up (issue reference or next-review trigger) in the same row (rule 6).
8. When an element also appears in the spike report, carry its reversibility tag into the row's disposition reasoning, requiring stronger evidence for `mitigated` verdicts on one-way-door elements (rule 7).
9. When a row is dispositioned `mitigated`, tag its confidence tier (repeatable automated control vs. one-off manual review vs. documented-but-unverified assumption) (rule 11).
10. When an Elevation-of-Privilege row sits at a boundary between an external entity and a data store holding regulated data, cross-link the row to the legal_regulatory probe's findings rather than scoring the two probes in isolation (rule 8).
11. If an element from an early spike draft is dropped from the spec before the table is finalized, remove its rows entirely rather than leaving them `deferred` (rule 10).

## Output shape

Applying this skill produces a threat-model disposition entry for the record: a STRIDE table with one row per (element, category, trust boundary), each row carrying a finding, a terminal disposition (`mitigated`, `accepted`, or `deferred`), a named follow-up for any `deferred` row, a confidence tier for any `mitigated` row, and cross-links to reversibility tags and regulatory findings where applicable — with no blank, in-progress, or stale (removed-element) rows remaining.

## Rules

1. **when** building the STRIDE table's rows **choose** one row per
   (element, category, trust boundary) triple, never one row per
   element with all six categories collapsed into a single free-text
   cell — a collapsed cell hides which specific category was actually
   assessed and which was skipped.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "threat_model: a STRIDE table,
   one row per (element, category, trust boundary)".

2. **when** classifying a threat into a STRIDE category **choose** use
   the six fixed categories only — Spoofing, Tampering, Repudiation,
   Information disclosure, Denial of service, Elevation of privilege —
   not an ad hoc category invented for the spec, so findings stay
   comparable across specs and roles.
   source: "STRIDE ... classifies security threats into six
   categories: Spoofing, Tampering, Repudiation, Information
   disclosure, Denial of service, and Elevation of privilege" —
   Practical DevSecOps, "STRIDE Threat Model - Simplified"
   (https://www.practical-devsecops.com/what-is-stride-threat-model/).

3. **when** identifying elements to model **choose** derive them from
   an explicit data-flow diagram of the spec (processes, data stores,
   data flows, external entities) rather than an ad hoc list of
   "things that seem important" — STRIDE's per-element analysis is
   defined against DFD elements, and skipping the DFD step tends to
   miss data stores and flows that aren't user-facing.
   source: "The framework helps teams identify potential security
   threats by classifying them based on system models like data flow
   diagrams (DFDs)" — Security Compass, "What is STRIDE in Threat
   Modeling?" (https://www.securitycompass.com/blog/stride-in-threat-modeling/).

4. **when** a trust boundary crosses two elements with different
   privilege levels **choose** add a dedicated row at that crossing for
   every STRIDE category that plausibly applies, even if the same
   category was already assessed for one of the two elements alone —
   the boundary crossing itself is the risk surface, distinct from
   either element's own internal risk.
   source: "helping teams reason about potential security threats
   across trust boundaries" — Security Compass, STRIDE overview
   (https://www.securitycompass.com/blog/stride-in-threat-modeling/);
   row shape requirement, feasibility role directive, this repo.

5. **when** a threat table row is completed **choose** require a
   disposition of exactly one of `mitigated`, `accepted`, or
   `deferred` — never leave a row "in progress" or blank — because a
   record at a terminal loop_state with an undisposed risk row is
   refused outright by this role's ADR-spine gate.
   source: this session's SessionStart hook, Nygard ADR-spine
   directive: "every Risks entry must carry a disposition of
   mitigated, accepted, or deferred; a Risks section with an undisposed
   entry ... is incomplete."

6. **when** a row is dispositioned `deferred` **choose** require a
   named follow-up (an issue reference or a next-review trigger) in
   the same row, not a bare "deferred" label — an undated deferral is
   functionally identical to silently dropping the risk, which the
   role's all-four-probes-resolve rule exists to prevent.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "No verdict until ALL FOUR probes
   resolve ... An empty or in-progress field is not a resolution" —
   applied to individual STRIDE rows by extension of the same
   no-silent-gap principle.

7. **when** the same architectural element appears in both the spike
   report (technical probe) and the STRIDE table (threat_model probe)
   **choose** carry its reversibility tag into the STRIDE row's
   disposition reasoning — a `mitigated` verdict on a one-way-door
   element should cite stronger evidence than a `mitigated` verdict on
   a two-way-door element, per this role's reversibility-scales-
   evidence rule.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "Reversibility scales evidence: a
   one-way door needs more before its probe may pass; a two-way door
   may pass on less. It is a field on every finding."

8. **when** an Elevation-of-Privilege row is found at a trust boundary
   between an external entity and a data store holding regulated data
   **choose** cross-link that row to the legal_regulatory probe's
   per-dependency/regulatory findings in the same record, rather than
   scoring the two probes in isolation — a privilege-elevation path
   into regulated data is simultaneously a security finding and a
   regulatory-exposure finding, and scoring only one undercounts the
   risk.
   source: STRIDE category definitions (Information disclosure,
   Elevation of privilege) — Security Compass
   (https://www.securitycompass.com/blog/stride-in-threat-modeling/);
   combined with this role's four-probes-must-all-resolve requirement,
   feasibility/hooks/directive.sh (this repo).

9. **when** Denial-of-service is being assessed for an element the
   spec explicitly scopes as "not internet-facing" **choose** still add
   the row rather than omitting the category for that element — STRIDE
   defines DoS as disrupting availability through resource overload,
   which applies to internal actors and internal trust boundaries too,
   not only external attackers.
   source: "Denial of Service (disrupting system availability through
   resource overload)" — Security Compass, STRIDE categories
   (https://www.securitycompass.com/blog/stride-in-threat-modeling/).

10. **REMOVAL — when** an element originally modeled in an early spike
    draft is dropped from the spec before the STRIDE table is
    finalized (e.g. a considered-and-rejected integration point)
    **choose** remove its rows from the table entirely rather than
    leaving them with a `deferred` disposition — a row for an element
    that no longer exists in the spec is not a real deferred risk, and
    keeping it dilutes the signal of the rows that are.
    source: row-shape requirement (one row per element/category/
    boundary that exists in the spec), feasibility role directive,
    this repo (feasibility/hooks/directive.sh); MADR carry-forward's
    `dropped: <reason>` convention applied by analogy to threat-model
    rows, this session's SessionStart hook.

11. **when** a STRIDE row is marked `mitigated` **choose** also tag
    the disposition's confidence tier (a repeatable, automated,
    tool-enforced control vs. a one-off manual review vs. a documented
    but unverified assumption) — a `mitigated` label backed by a
    recurring automated gate and one backed by a single manual
    eyeballing are not the same strength of evidence, and collapsing
    both into one bare word hides which rows would fail to stay
    mitigated after the next change.
    source: survey of vulnerability-scanning tools' maturity rubrics —
    the rubric distinguishes "stable" (tested, documented, packaged)
    from "beta" (functional but depends on local setup or manual
    review) from "experimental" (needs reviewer control), applied per
    feature rather than asserting one blanket maturity claim for the
    whole system.
