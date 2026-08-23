# experiment-trust — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] Evidence grade — read before citing this to anyone

Three lines of honesty, stated every time this skill is invoked:

- **(a) Confirmed, from primary industry-research sources (KDD / Microsoft experimentation-platform
  papers)** — real measured platform data, not RCT evidence about experimentation as a practice: SRM's
  definition, its chi-square detection method with the verified concrete examples below, its
  invalidating consequence for causal inference, and its measured platform prevalence.
- **(b) Confirmed, prescribed procedure with a checkable numeric criterion, same lineage**: the A/A
  test validation method and its ~5% false-positive-rate criterion.
- **(c) NEVER EXAMINED — a coverage gap, not a negative finding**: sample-size / power-analysis
  specifics, and the peeking (early-stopping) type-I-error-inflation literature. These were not
  refuted; no verifier ever voted on them (the research round extracted 99 claims and verified 25, so
  the remainder was never adjudicated). Do not report them as unsupported. The gates below still
  REQUIRE a pre-committed sample size and a no-peeking rule — that is a procedural design choice
  consistent with the verified A/A false-positive semantics (a fixed nominal α presumes a fixed
  horizon), not a claim this skill's research checked. For the pre-registration discipline itself — metric, threshold, decision
  rule, date-stamped before the run — route to `hypothesis-testing`; do not re-derive it here.

Additionally, at medium grade (2-1 vote each, name the grade when citing): Twyman's law as a
skepticism heuristic for anomalous results, and the base-rate reminder that most experiments do not
produce a positive significant effect.

**MUST NOT claim**: that chi-square (with KS / Anderson-Darling) is "the industry-standard
randomization-validation method used at Google, Microsoft and LinkedIn" — that broader industry-wide
framing was refuted. Chi-square for SRM specifically is confirmed via the examples in Step 4; the
broader attribution is not. No invented statistics beyond what is listed in this file.

