---
name: growth-analytics-experiment-trust
description: >-
  Use when an experiment's traffic split looks skewed, an anomalous win needs a trust
  verdict before it is reported, or a guardrail metric's non-significant result needs to be
  surfaced rather than dropped. Applies to the experiment-trust axis. Trigger on requests
  like "실험 결과 믿어도 돼?", "run an SRM check on this split", "this win looks too good — verify
  it", "the guardrail didn't move, do we still report it". Do NOT use for the general
  standalone A/B trustworthiness review outside a growth-analytics deliverable (use
  experiment-trust).
metadata:
  axis: experiment-trust
  rule_count_floor: 3
---

# Experiment-trust verdict rules

## Trigger

Apply this skill when an experiment's variant traffic split may deviate
from its assigned ratio, when an experiment result looks anomalously
large relative to the pre-registered expected effect, or when a
guardrail metric shows no statistically significant delta and someone is
deciding whether to include it in the report.

## Procedure

1. Before reading any effect size, run a Sample Ratio Mismatch (SRM)
   chi-square check on the variant traffic split; treat a detected SRM
   as a hard stop (rule 1).
2. When a win exceeds roughly 2x the pre-registered expected effect,
   flag it "unconfirmed, pending independent check" rather than
   reporting it as a plain result (rule 2).
3. When a guardrail metric shows no statistically significant delta,
   still report it — drop only the practice of omitting it, never the
   metric itself (rule 3).

## Output shape

A trust verdict on the experiment: SRM check result (pass/hard-stop),
any anomalous win flagged as unconfirmed pending independent check, and
every guardrail metric reported regardless of significance.

1. **When** an experiment's variant traffic split deviates from the
   assigned ratio, **run a Sample Ratio Mismatch (SRM) chi-square check
   before reading any effect size**, and treat a detected SRM as a hard
   stop — a skewed split invalidates the randomization assumption every
   downstream statistic depends on.
   Source: Kohavi, Tang & Xu, *Trustworthy Online Controlled
   Experiments*, Cambridge University Press (2020) — publisher page
   https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/
   (SRM chapter, fetched 2026-08-13 via search on trustworthy A/B
   testing guidance).

2. **When** an anomalous win exceeds roughly 2x the pre-registered
   expected effect, **flag it "unconfirmed, pending independent check"
   rather than reporting it as a plain result** — Twyman's law: any
   figure that looks too good is more likely a measurement artifact than
   a real effect.
   Source: Kohavi, Tang & Xu, *Trustworthy Online Controlled
   Experiments* (2020), Twyman's-law discussion — same citation as
   above.

3. **REMOVAL** — when a guardrail metric shows no statistically
   significant delta, **do not omit it from the report just because the
   primary metric won**; drop only the practice of silence, not the
   metric itself — a guardrail that is never reported cannot ever catch
   a regression it was added to catch.
   Source: Kohavi, Tang & Xu, *Trustworthy Online Controlled
   Experiments* (2020), guardrail-metric chapter — same citation as
   above.

## Related skills

- [research-evidence-discipline](../research-evidence-discipline/SKILL.md) — a trust verdict already turns on whether a result is real evidence or an unconfirmed/fabricated signal; this skill adds Fact/Inference/Assumption labeling and a do-not-invent list on top.
