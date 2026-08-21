---
name: technical-feasibility-license-and-regulatory-risk
description: Use when the spec's open questions turn on DPIA necessity, GDPR high-risk classification, dependency license compatibility, or regulatory applicability given the spec's data-subject and jurisdiction footprint.
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

## Rules

1. **when** the spec involves processing personal data and the
   proposal must decide whether a DPIA is needed **choose** treat "is
   likely to result in high risk to individuals' rights and freedoms"
   as the trigger, not "we process personal data at all" — DPIA is a
   high-risk-processing gate, not a blanket personal-data gate, so
   over-triggering it on every data-touching spec dilutes the signal
   for the specs that actually need it.
   source: "A DPIA is required under Article 35 when processing is
   likely to result in a high risk to individuals' rights and
   freedoms" — Recording Law, "GDPR DPIA: When Is a Data Protection
   Impact Assessment Required?"
   (https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-dpia/).

2. **when** classifying whether a specific processing activity clears
   the high-risk threshold **choose** check it against the concrete
   examples first (systematic/extensive profiling with significant
   effects, large-scale special-category or criminal-conviction data,
   large-scale systematic monitoring of a public area) before falling
   back to judgment — the examples are the operationalized version of
   an otherwise undefined term.
   source: "Systematic and extensive profiling with significant
   effects on individuals, large-scale processing of special category
   data or criminal conviction data, and systematic monitoring of a
   publicly accessible area on a large scale are considered high-risk
   activities" — Recording Law, GDPR DPIA guide
   (https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-dpia/).

3. **when** none of the enumerated high-risk examples clearly match
   the spec's processing **choose** still require an explicit
   documented judgment call in the record (yes/no + one-line reason),
   never silence-as-no — the regulator's own guidance places the
   screening decision on the controller when the activity isn't listed,
   so an undocumented skip is a compliance gap, not a resolved probe.
   source: "If your intended processing is not described under UK
   GDPR Article 35(3), the ICO list or European guidelines then
   ultimately, it's up to you to decide whether your processing is of
   a type likely to result in high risk" — ICO, "When do we need to do
   a DPIA?"
   (https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/).

4. **when** a DPIA is required and the spec is already past design and
   moving toward build **choose** flag this as a `no-go`-class blocker
   pending the DPIA rather than a `conditional` note to revisit later —
   Article 35 requires the DPIA to run BEFORE the high-risk processing
   starts, not concurrently with or after build, so late discovery here
   is exactly the failure this role exists to prevent.
   source: "DPIAs are not optional for high-risk processing" and the
   DPIA-before-processing framing of Article 35 — Recording Law GDPR
   DPIA guide
   (https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-dpia/);
   also this role's own directive: "DPIA-before-processing pattern"
   (feasibility/hooks/directive.sh, this repo).

5. **when** citing the cost of skipping a required DPIA in the risk
   register **choose** cite the actual statutory ceiling (up to EUR 10
   million or 2% of worldwide annual turnover under Article 83(4)(a))
   rather than a vague "large fine" — a bare severity adjective is not
   evidence under this role's citation rule.
   source: "failing to conduct one when required can result in fines
   of up to EUR 10 million or 2% of worldwide annual turnover under
   Article 83(4)(a)" — Recording Law GDPR DPIA guide
   (https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-dpia/).

6. **when** the legal_regulatory probe covers dependency licensing
   **choose** produce a per-dependency license verdict (each dependency
   gets its own accept/reject line), never one blanket "licenses look
   fine" line for the whole dependency set — the role's own directive
   requires per-dependency granularity precisely because one
   incompatible license in a large tree is enough to block.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "legal_regulatory: a
   per-dependency license verdict (scan evidence) ... (skill:
   license-scan)".

7. **when** a regulatory-applicability note is written for a spec with
   no EU nexus at all (no EU users, no EU data, no EU establishment)
   **choose** state that explicitly with the disqualifying fact named
   (e.g. "no EU data subjects, Article 3 territorial scope not met")
   rather than omitting the GDPR line entirely — an omitted regulation
   reads as "not considered," while a stated non-applicability reads
   as "considered and ruled out," and only the latter satisfies this
   role's no-bare-assertion, no-silent-omission evidence bar.
   source: evidence-citation directive, this repo — "A claim with no
   citation is not evidence" applies symmetrically to a claim of
   non-applicability.

8. **when** the four probes are being scored and legal_regulatory has
   an open DPIA or license question **choose** mark that probe
   `blocked:<evidence>`, never `pass` with a caveat buried in the
   record body — the role's own execution-judgment rule is that an
   empty or in-progress field is not a resolution, and a "pass, but
   see below" is functionally in-progress.
   source: feasibility role directive, this repo
   (feasibility/hooks/directive.sh): "No verdict until ALL FOUR probes
   resolve to pass:<evidence> | fail:<evidence> | blocked:<evidence>
   ... An empty or in-progress field is not a resolution."

9. **when** a spec touches criminal-conviction or special-category
   data under Article 9/10-equivalent categories **choose** treat that
   alone as sufficient to trigger the DPIA screening question (rule 1),
   independent of processing scale — the enumerated high-risk examples
   list "large-scale processing of special category data" as one
   trigger, but the safer operational default under this role's
   no-late-discovery mandate is to screen rather than pre-judge scale.
   source: Recording Law GDPR DPIA guide, high-risk examples list
   (https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-dpia/);
   role directive's no-late-discovery framing
   (feasibility/hooks/directive.sh, this repo).

10. **REMOVAL — when** a dependency's license verdict was already
    resolved and cited in phase 1 and nothing about that dependency's
    license has changed **choose** carry the same citation forward
    into phase 2 verbatim rather than re-deriving or re-stating it
    from memory — phase-2 citation policy for this role explicitly
    forbids re-deriving a phase-1-cited claim from memory.
    source: this session's SessionStart hook, Evidence citation
    section: "Phase 2 ... citations from phase 1 must be carried
    forward, not re-derived from memory ... If a claim was cited in
    phase 1 and still holds in phase 2, carry the same citation
    forward."

11. **when** recording a per-dependency license verdict **choose** a
    graded tier (safe / caution-weak-copyleft / high-risk-strong-copyleft
    / blocked-proprietary-or-unlicensed / unknown-needs-verification)
    rather than a binary accept/reject — a weak-copyleft dependency
    that requires only file-level attribution and a strong-copyleft
    dependency that could force releasing proprietary source carry
    very different remediation costs, and collapsing both into one
    "reject" verdict loses the information needed to decide whether to
    swap the dependency or just add an attribution notice.
    source: survey of license-scanning tools — classifies each scanned
    package into "Safe / Caution (weak copyleft) / High risk
    (GPL/AGPL) / Blocked (proprietary/unlicensed) / Unknown," and
    "only reports findings — it never removes a dependency ... on its
    own," keeping the verdict a graded input to a human decision
    rather than an automatic block.
