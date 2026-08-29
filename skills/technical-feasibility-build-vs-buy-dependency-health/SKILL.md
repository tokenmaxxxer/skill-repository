---
name: technical-feasibility-build-vs-buy-dependency-health
description: >-
  Use when a comparison record must score a candidate dependency or vendor's
  per-check health (Scorecard Maintained/Code-Review/Vulnerabilities, or vendor
  SLA/incident history) and decide build vs. buy on that graded, cited evidence
  rather than on license terms, threat modeling, or timebox/verdict selection.
  Trigger on requests like "OpenSSF Scorecard check", "is this library still
  maintained", "dependency health 평가해줘", "vendor SLA evidence for buy decision".
  Do NOT use for running the feasibility skill's prior-art probe and its
  comparison-table workflow (use technical-feasibility-build-vs-buy).
metadata:
  axis: build-vs-buy-dependency-health
  rule_count_floor: 10
  axes:
    - reversibility-and-spike-scoping
    - build-vs-buy-dependency-health
    - license-and-regulatory-risk
    - threat-model-disposition
    - verdict-and-timebox-selection
---

# Decision axis: build-vs-buy & dependency health

## Trigger

Use this axis when the decision at hand is whether to score and compare a
specific candidate dependency or vendor's health as evidence for a build-vs-buy
call — i.e. the open question is "how healthy/maintained is this candidate,
and does that justify buy over build," not whether its license is compatible
(license-and-regulatory-risk), whether it poses a security/abuse threat
(threat-model-disposition), how reversible adopting it is or how to scope a
spike (reversibility-and-spike-scoping), or which verdict/timebox format to
write the decision up in (verdict-and-timebox-selection).

## Procedure

1. Pull the OpenSSF Scorecard `Maintained` check for the candidate and cite it
   as the activity/maintenance evidence line (rule 1).
2. Pull the Scorecard `Code-Review` check separately and cite it as its own
   evidence line — do not merge it into the `Maintained` score (rule 2).
3. If the record only has an aggregate Scorecard score, reject that citation
   and require the per-check `check-name score` breakdown instead (rule 3).
4. Default to evaluating "buy" first for the needed capability, and block
   "build" from being chosen until per-dependency health evidence is on the
   record (rule 4).
5. If no Scorecard run exists yet for the candidate, run one before citing it
   — do not substitute star counts or blog opinions (rule 5).
6. When two candidates are close on aggregate score, prefer the one without an
   open `Vulnerabilities` finding, even if its other checks score marginally
   lower (rule 6).
7. When "build" wins over "buy," require the record to name the specific
   check and score that made the rejected "buy" candidate fail, as its
   one-line rejection reason (rule 7).
8. For a SaaS vendor where Scorecard doesn't apply, substitute cited SLA/
   uptime and incident-disclosure evidence in place of a bare "reputable
   vendor" claim (rule 8).
9. When citing a currently-passing `Maintained` check, include the check date
   so the citation isn't read as a durable property (rule 9).
10. When a candidate has been deprecated in favor of the vendor's own
    successor, drop it from the comparison table with an explicit
    `dropped: <reason>` rather than carrying it as a scored row (rule 10).
11. Calibrate the pass/fail health bar to the consuming project's own
    maturity and stakes rather than applying one fixed bar to every project
    (rule 11).

## Output shape

Applying this axis produces one graded, per-dependency (or per-vendor) health
entry in the build-vs-buy comparison record: a health score or pass/fail read
per named check (`check-name score`, e.g. Scorecard `Maintained`,
`Code-Review`, `Vulnerabilities`, or vendor SLA/incident-history citation),
dated where currency matters, calibrated to the consuming project's maturity,
with any "build" verdict or dropped candidate carrying its own one-line,
evidence-cited reason rather than a bare assertion.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — **when** grading a candidate dependency's ongoing maintenance **choose** run the OpenSSF Scorecard `Maintained` check (activity and maintenance status of the project) ra…
- 1.2 — **when** grading a candidate dependency's contribution-quality controls **choose** the `Code-Review` check (does the project require human review before merge) as a dist…
- 1.3 — **when** a candidate dependency scores well on Scorecard but the record cites only the aggregate score **choose** reject the citation and require per-check breakdown (wh…
- 1.4 — **when** comparing build vs. buy for a capability the spec needs **choose** treat "buy" (adopt an existing dependency/vendor) as the default candidate to evaluate first,…
- 1.5 — **when** no OpenSSF Scorecard run exists for a candidate dependency **choose** run one before citing it, rather than substituting a GitHub star count or a blog post's op…
- 1.6 — **when** two candidate dependencies are close on Scorecard but one has a known unpatched vulnerability in its `Vulnerabilities` check **choose** the one without the open…
- 1.7 — **when** a "build" option is chosen over "buy" **choose** require the record to name the specific health gap in the rejected buy candidate (which check failed, what scor…
- 1.8 — **when** the candidate is a SaaS vendor rather than an open-source dependency and Scorecard does not apply **choose** substitute the closest equivalent evidence: the ven…
- 1.9 — **when** a dependency's Scorecard `Maintained` check is currently passing but the record only checked it once **choose** note the check date in the citation (the score i…
- 1.10 — **REMOVAL — when** a dependency candidate has been superseded by the vendor's own successor project (deprecated upstream, migration guide published) **choose** drop it f…
- 1.11 — **when** scoring a candidate dependency's health **choose** calibrate the bar to the consuming project's own maturity/stage (a pre-launch prototype vs. a production syst…
