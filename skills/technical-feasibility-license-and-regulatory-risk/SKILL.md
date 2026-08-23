---
name: technical-feasibility-license-and-regulatory-risk
description: >-
  Use when the spec's open questions turn on DPIA necessity, GDPR high-risk
  classification, dependency license compatibility, or regulatory applicability
  given the spec's data-subject and jurisdiction footprint. Trigger on requests
  like "DPIA 필요한지 판단해줘", "GDPR high-risk screening", "is this license compatible
  with commercial distribution", "which regulations apply here". Do NOT use for
  running the probing-state legal-regulatory probe's user-interview and
  record-writing workflow (use technical-feasibility-license-scan).
metadata:
  axis: license-and-regulatory-risk
  rule_count_floor: 10
  axes:
    - reversibility-and-spike-scoping
    - build-vs-buy-dependency-health
    - license-and-regulatory-risk
    - threat-model-disposition
    - verdict-and-timebox-selection
---

# Decision axis: license & regulatory risk

## Trigger

Use this axis when the spec's open questions turn on whether processing
personal data requires a DPIA, whether a specific data-handling activity
clears the GDPR high-risk threshold, whether a dependency's license is
compatible with the intended distribution, or whether a regulation applies
at all given the spec's data-subject and jurisdiction footprint — as
opposed to whether a change is reversible (reversibility-and-spike-scoping),
whether a dependency is healthy to depend on (build-vs-buy-dependency-health),
whether a security threat needs disposition (threat-model-disposition), or
how to time-box and score the overall verdict (verdict-and-timebox-selection).

## Procedure

1. Screen whether the spec's processing is "likely to result in high risk
   to individuals' rights and freedoms," not merely whether personal data
   is touched at all, to decide if a DPIA is needed (rule 1).
2. Check the processing against the concrete high-risk examples
   (systematic/extensive profiling, large-scale special-category or
   criminal-conviction data, large-scale public monitoring) before falling
   back to judgment (rule 2).
3. If no enumerated example clearly matches, still record an explicit
   documented yes/no judgment with a one-line reason rather than leaving
   the question silently unanswered (rule 3).
4. When a DPIA is required and the spec is already moving toward build,
   flag it as a `no-go`-class blocker pending the DPIA, not a `conditional`
   note for later (rule 4).
5. When citing the cost of skipping a required DPIA, cite the actual
   statutory fine ceiling rather than a vague severity adjective (rule 5).
6. Produce a per-dependency license verdict for every dependency in scope,
   never one blanket verdict for the whole dependency set (rule 6).
7. When a spec has no EU nexus, state that explicitly with the
   disqualifying fact named instead of omitting the GDPR line entirely
   (rule 7).
8. When scoring the legal_regulatory probe, mark it `blocked:<evidence>`
   if a DPIA or license question is still open — never `pass` with a
   caveat buried in the record body (rule 8).
9. Treat any processing of criminal-conviction or special-category data
   as sufficient on its own to trigger the DPIA screening question,
   independent of scale (rule 9).
10. In phase 2, carry forward any dependency license verdict already
    resolved and cited in phase 1 verbatim, rather than re-deriving or
    re-stating it from memory (rule 10).
11. Record each per-dependency license verdict on the graded tier scale
    (safe / caution-weak-copyleft / high-risk-strong-copyleft /
    blocked-proprietary-or-unlicensed / unknown-needs-verification)
    instead of a binary accept/reject (rule 11).

## Output shape

Applying this skill produces a graded license-and-regulatory-risk entry
for the record: an explicit DPIA screening determination (with statutory
citation where a blocker applies), a per-dependency license verdict on
the five-tier grading scale, an explicit non-applicability statement
where no EU nexus exists, and a probe status of pass/fail/blocked with
evidence — never a bare "looks fine" assertion.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **when** the spec involves processing personal data and the proposal must decide whether a DPIA is needed **choose** treat "is likely to result in high risk to individua…
- 1.2 — **when** classifying whether a specific processing activity clears the high-risk threshold **choose** check it against the concrete examples first (systematic/extensive…
- 1.3 — **when** none of the enumerated high-risk examples clearly match the spec's processing **choose** still require an explicit documented judgment call in the record (yes/n…
- 1.4 — **when** a DPIA is required and the spec is already past design and moving toward build **choose** flag this as a `no-go`-class blocker pending the DPIA rather than a `c…
- 1.5 — **when** citing the cost of skipping a required DPIA in the risk register **choose** cite the actual statutory ceiling (up to EUR 10 million or 2% of worldwide annual tu…
- 1.6 — **when** the legal_regulatory probe covers dependency licensing **choose** produce a per-dependency license verdict (each dependency gets its own accept/reject line), ne…
- 1.7 — **when** a regulatory-applicability note is written for a spec with no EU nexus at all (no EU users, no EU data, no EU establishment) **choose** state that explicitly wi…
- 1.8 — **when** the four probes are being scored and legal_regulatory has an open DPIA or license question **choose** mark that probe `blocked:<evidence>`, never `pass` with a…
- 1.9 — **when** a spec touches criminal-conviction or special-category data under Article 9/10-equivalent categories **choose** treat that alone as sufficient to trigger the DP…
- 1.10 — **REMOVAL — when** a dependency's license verdict was already resolved and cited in phase 1 and nothing about that dependency's license has changed **choose** carry the…
- 1.11 — **when** recording a per-dependency license verdict **choose** a graded tier (safe / caution-weak-copyleft / high-risk-strong-copyleft / blocked-proprietary-or-unlicense…
