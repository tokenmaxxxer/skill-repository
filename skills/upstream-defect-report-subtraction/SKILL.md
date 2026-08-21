---
axis: subtraction
rule_count_floor: 5
role: upstream-defect-report
---

# Subtraction — what to remove before filing

Decision rules for what to cut from a defect report before it reaches
an upstream maintainer. Default human behavior is additive (see
Sources) — this axis exists because reporters over-include by default,
not because removal is a stylistic nicety.

## Rules

1. **When** the report author is a fluent field-time (verbose, cognitively
   easy) provider and finds themselves adding another paragraph "just in
   case" — **choice**: cut it. Re-derive the report by asking "does
   removing this sentence change whether the bug reproduces" rather than
   "could this sentence conceivably help." People systematically search
   the additive branch and skip the subtractive one unless prompted, so
   the correct default action is deliberate removal, not deliberate
   addition. source: Adams, Converse, Hales & Klotz, "People
   systematically overlook subtractive changes," *Nature* 592, 258–261
   (2021), https://www.nature.com/articles/s41586-021-03380-y

2. **When** a stack trace, log dump, or screenshot is attached alongside
   a text description that already states the same failure —
   **choice**: keep exactly one representation of the failure signal
   (the one a maintainer can grep/diff) and drop the redundant copy, or
   collapse the raw dump behind a `<details>` fold rather than inline.
   source: Ten Simple Rules for Reporting a Bug, rule 8 "Be concise,"
   PLOS Comput Biol (2022),
   https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010540

3. **When** the reproduction steps include environment setup, data
   fixtures, or app code unrelated to the failing code path —
   **choice**: delete every line that still reproduces the bug when
   removed; keep binary-searching for cuts until removing one more line
   makes the bug stop reproducing. This is the operational definition of
   "minimal" in "minimal reproducible example," not a size guideline.
   source: Minimal Reproducible Example, Wikipedia,
   https://en.wikipedia.org/wiki/Minimal_reproducible_example ;
   Matthew Rocklin, "Craft Minimal Bug Reports,"
   https://matthewrocklin.com/minimal-bug-reports/

4. **When** the report narrates the investigation history ("first I
   tried X, then I suspected Y, then I found Z") instead of stating the
   conclusion — **choice**: 삭제 the narrative chain and state only the
   final condition→symptom pair; move the investigation trail to a
   collapsed/linked appendix if it has independent diagnostic value.
   source: Ten Simple Rules for Reporting a Bug, rule 8, PLOS Comput
   Biol (2022) (as above).

5. **When** a proprietary or reporter-specific dependency (private data,
   internal service, non-public model/config) appears in the repro but
   a public substitute reproduces the same failure — **choice**: cut the
   private dependency and replace it with the public substitute; a
   report a maintainer cannot run is not minimal, it is merely short.
   source: Ultralytics, "Creating a Minimum Reproducible Example for Bug
   Reports," https://docs.ultralytics.com/help/minimum-reproducible-example

6. **When** the same defect has already been filed (duplicate search
   returns a hit) — **choice**: omit filing a new report; instead
   subtract the whole report down to one comment adding new
   reproduction detail on the existing issue. Filing a parallel report
   duplicates maintainer triage load rather than reducing it.
   source: Ten Simple Rules for Reporting a Bug, rule 3, PLOS Comput
   Biol (2022) (as above).

7. **When** a suspected upstream defect is about to be drafted into an
   issue — **choice**: before filing, re-run the exact reproduction
   against the current on-the-record state one more time as a dedicated
   verification step, separate from the original observation that
   surfaced it; do not file straight off the first detection. A defect
   that looked real at observation time can already be stale (fixed,
   config-drifted, or an artifact of the observing session's own state)
   by filing time, and a false-positive upstream report costs the
   maintainer the same triage load as a true one.
