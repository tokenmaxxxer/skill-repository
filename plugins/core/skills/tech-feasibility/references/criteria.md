# Tech Feasibility — objective criteria and their sources

Grades: ●●● official/quantitative · ●●○ industry standard · ●○○ folklore.

## Technology maturity — TRL (●●●)

NASA Technology Readiness Levels 1-9: 1 basic principles, 3 analytical/experimental proof-of-concept, 4 lab validation, 5 validation in relevant environment, 6 prototype demo in relevant environment, 7 prototype in operational environment, 8 system complete and qualified, 9 proven in operations. Federal standard (NASA/DoD/ESA). Use as a shared vocabulary for "how proven is this really." Limit: built for hardware; software/AI mapping is fuzzy and self-assessment skews optimistic — hence "locate the claim honestly," don't just accept a vendor's readiness label.

## Build vs buy (●○○ concept / ●●○ TCO)

Core vs context (Geoffrey Moore): core = differentiates you to customers → build with your best people; context = necessary but undifferentiating → buy/outsource/standardize. Management framework, not empirical; "core" migrates over time (yesterday's context becomes today's core), so state the assumption. TCO (Gartner, ●●○): acquisition + operation + maintenance + staffing + downtime + switching/exit costs; buy hides integration and lock-in, build hides perpetual maintenance and team opportunity cost. Gartner itself warns against deciding on TCO alone — it misses strategic option value and agility.

## Open-source health

- **Bus factor / truck factor (●●●)**: minimum contributors whose loss stalls the project. Empirical: of 133 popular GitHub projects, ~65% had bus factor ≤2, <10% above 10 — dependency on a solo maintainer is the norm and a real migration risk. (Data 2015-16; treat as order-of-magnitude.)
- **OpenSSF Scorecard (●●○)**: automated 0-10 across ~20 checks (branch protection, code review, CI tests, pinned dependencies, SAST, signed releases, known vulnerabilities via OSV, maintenance). Open algorithm, reproducible. Limit: security-focused; doesn't measure code quality or community health.
- **CHAOSS metrics (●●○)**: time-to-first-response, change-request closure ratio, contributor absence factor (= bus factor), release frequency. Community-standard, quantifiable, but large-scale outcome correlations are thin.

## License compatibility (●●○)

Permissive (MIT/BSD/Apache-2.0) compose with each other and most things. GPL is one-way: permissive code can flow into GPL, not vice versa. GPLv2 and GPLv3 are mutually incompatible. LGPL is weak copyleft (middle ground). No universal matrix exists — static vs dynamic linking and derivative-work questions change the answer, so flag non-trivial cases for legal review rather than ruling.

## PoC / spike discipline (●●○ / ●○○)

Spike (XP origin): simplest possible program to answer one uncertain technical question; timeboxed; **code is throwaway by design**. PoC success/failure criteria must be written before the PoC (else the outcome is unfalsifiable) — industry consensus, not academic. PoC ("is it technically possible", internal) vs prototype ("how will it look/work", UX) vs pilot ("does it work in limited real operation", scale decision) — terms are used loosely; define which you mean. Fail-fast / risk-first sequencing traces to Boehm's spiral model (risk-driven iteration): validate the highest-uncertainty, highest-impact assumption first because late-discovered failure carries the largest sunk cost.

## Vendor evaluation (●○○ / ●●○)

Weighted RFP scoring: stakeholders agree categories and weights (e.g., functionality 30%, cost 25%, experience 25%, approach/innovation 20%) summing to 100%, score 1-5, multiply and sum — industry standard for choosing "best fit" over cheapest/most-featured; weights are subjective. Lock-in assessment: data portability/export format, API openness, contract exit clauses, switching-cost estimate, multi-vendor alternatives (checklist-level, ●○○). SLA verification: cross-check contractual SLAs against actual uptime/incident history; independent reference interviews with current and former customers.

## Architecture Decision Record (●●○)

Michael Nygard's template (2011), endorsed by Fowler: Title, Status (proposed/accepted/deprecated/superseded), Context, Decision, Consequences (what gets easier/harder). Value: historical record ("why is it built this way") and forced clarity (writing surfaces disagreement). No effectiveness study, but broad practitioner adoption. Keep depth-1 and maintained, or it rots.

## DORA / Accelerate context (●●●)

Forsgren, Humble, Kim — multi-year State of DevOps survey (tens of thousands), factor analysis / SEM. Four metrics: deployment frequency, lead time for changes, change failure rate, time to restore. Relevance to *selection*: it validated which *practices* (trunk-based dev, test automation, loosely-coupled architecture) correlate with measurable delivery performance — so judge an architecture choice partly by its effect on these. Limit: self-report data, correlation not proven causation.

## ThoughtWorks Technology Radar (●○○)

Adopt / Trial / Assess / Hold(Caution) rings, assigned by an advisory board from consultants' real project experience; Trial requires actual production use as its gate. Transparent on who and how (experienced practitioners, consensus), but non-reproducible closed deliberation — expert judgment, not a metric. Useful as a signal, not proof.