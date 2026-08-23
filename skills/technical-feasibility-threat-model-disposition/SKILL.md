---
name: technical-feasibility-threat-model-disposition
description: >-
  Use when a spec's STRIDE table rows and dispositions need to be built or
  checked, as opposed to deciding reversibility/spike scope, dependency
  build-vs-buy health, license/regulatory exposure, or the final
  verdict/timebox. Covers DFD-derived element enumeration, one row per (element,
  category, trust boundary), and terminal dispositions of exactly
  mitigated/accepted/deferred with confidence tiers. Trigger on requests like
  "STRIDE 분류해줘", "threat disposition audit", "mitigated accepted deferred
  check", "data-flow diagram threats". Do NOT use for the feasibility probe's
  interactive row-by-row walk with the user in the `probing` state (use
  technical-feasibility-stride-table).
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

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **when** building the STRIDE table's rows **choose** one row per (element, category, trust boundary) triple, never one row per element with all six categories collapsed…
- 1.2 — **when** classifying a threat into a STRIDE category **choose** use the six fixed categories only — Spoofing, Tampering, Repudiation, Information disclosure, Denial of s…
- 1.3 — **when** identifying elements to model **choose** derive them from an explicit data-flow diagram of the spec (processes, data stores, data flows, external entities) rath…
- 1.4 — **when** a trust boundary crosses two elements with different privilege levels **choose** add a dedicated row at that crossing for every STRIDE category that plausibly a…
- 1.5 — **when** a threat table row is completed **choose** require a disposition of exactly one of `mitigated`, `accepted`, or `deferred` — never leave a row "in progress" or b…
- 1.6 — **when** a row is dispositioned `deferred` **choose** require a named follow-up (an issue reference or a next-review trigger) in the same row, not a bare "deferred" labe…
- 1.7 — **when** the same architectural element appears in both the spike report (technical probe) and the STRIDE table (threat_model probe) **choose** carry its reversibility t…
- 1.8 — **when** an Elevation-of-Privilege row is found at a trust boundary between an external entity and a data store holding regulated data **choose** cross-link that row to…
- 1.9 — **when** Denial-of-service is being assessed for an element the spec explicitly scopes as "not internet-facing" **choose** still add the row rather than omitting the cat…
- 1.10 — **REMOVAL — when** an element originally modeled in an early spike draft is dropped from the spec before the STRIDE table is finalized (e.g. a considered-and-rejected in…
- 1.11 — **when** a STRIDE row is marked `mitigated` **choose** also tag the disposition's confidence tier (a repeatable, automated, tool-enforced control vs. a one-off manual re…
