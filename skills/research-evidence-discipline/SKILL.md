---
name: research-evidence-discipline
description: >-
  Use when writing a claim into a research-shaped record (market-analysis, product-discovery,
  growth-analytics, user-discovery) and deciding whether it needs a Fact/Inference/Assumption
  label, when about to state a name/quote/figure with no source in hand, or when an open-questions
  list is growing and a call to stop asking and proceed is needed. Applies to the evidence-
  discipline axis: Fact/Inference/Assumption labeling, a do-not-invent list for names, quotes, and
  precise figures, and a question-budget cap that forces progress on labeled assumptions. Trigger
  on requests like "이 조사 기록에 근거 라벨 붙여줘", "is this claim a fact or an assumption", "source this
  figure or drop it", "open questions 너무 많은데 진행할까". Do NOT use for grading the rigor of external
  market sources themselves (use market-analysis-evidence-rigor).
metadata:
  axis: evidence-discipline
  rule_count_floor: 6
---

# Evidence-discipline rules

Decision rules for three mechanisms layered on top of this role spec's
existing per-rule `source:` citation discipline: Fact/Inference/
Assumption labeling of claims, an explicit do-not-invent list, and a
question-budget cap. Independently authored — no text ported from any
external reference repo (see `docs/issue-61/reports/knowledge-management/survey.md`
for the sourcing note).

## Trigger

Apply this skill when writing a claim into a research-shaped record and
its evidentiary status (directly sourced, derived, or assumed) has not
yet been marked; when about to state a specific name, quote, or figure
with no source in hand; or when an accumulating list of open questions
in a record signals a session should stop asking and proceed on labeled
assumptions instead.

## Procedure

1. Before writing a claim into the record, classify it as Fact
   (directly sourced), Inference (derived from sourced facts), or
   Assumption (no source found), and write the label inline (rules 1-3).
2. Before naming a person, company, quoting speech, or stating a
   precise unsourced figure, check it against the do-not-invent list;
   if it cannot be checked against a real source, do not write it down
   (rules 4-5).
3. When the running count of open questions in a record passes the
   budget cap, stop asking and proceed on the best-labeled Assumption
   instead of blocking on an answer (rule 6).

## Output shape

Every claim in the record carries an explicit Fact/Inference/Assumption
label, no do-not-invent-listed content appears without a checkable
source, and the record proceeds past its question budget on labeled
assumptions rather than stalling on unanswered questions.

## Rules

### 1. Label a directly-sourced claim Fact
When a claim can be traced to a primary or secondary source already
cited in the record (per this role spec's existing sourcing discipline),
label it `Fact:` — a labeled Fact is what lets a downstream reader
distinguish sourced content from everything else in the record without
re-deriving the sourcing chain themselves.
source: https://www.anthropic.com/research/claude-character (grounding claims in verifiable sources rather than presenting all output as equally authoritative)

### 2. Label a derived claim Inference
When a claim is not itself directly sourced but is logically derived
from one or more Fact-labeled claims already in the record (a
conclusion, a trend read off cited data points), label it `Inference:`
rather than `Fact:` — collapsing a derived conclusion into the same
label as its sourced input hides the extra reasoning step a reviewer
would need to check.
source: https://www.annualreviews.org/content/journals/10.1146/annurev-psych-020821-114157 (distinguishing observation from inference as a core critical-thinking skill)

### 3. Label an unsourced claim Assumption
When no source can be found for a claim after a genuine search, and it
is not derivable from an existing Fact via Inference, label it
`Assumption:` rather than stating it as fact with no label — an
unlabeled, uncited claim is indistinguishable from a sourced one to a
downstream reader, which is the exact failure this axis exists to
prevent.
source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/reduce-hallucinations (instructing a model to say when it doesn't know rather than presenting a guess as fact)

### 4. Never invent a name, quote, or entity with no source
When a record is about to state a specific person's name, a company
name, a direct quote, or any other named entity, and no source for that
specific detail is in hand, do not write it down — a fabricated name or
quote reads as more authoritative than a labeled assumption and is far
harder for a downstream reader to catch, so it belongs on a stricter
do-not-invent list rather than the general Assumption label.
source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/reduce-hallucinations (explicit guidance against fabricating quotes, citations, and specific factual details)

### 5. Never state a precise unsourced figure
When a record is about to state a precise number (a percentage, a
count, a dollar figure) with no source, either find the source, replace
it with a labeled `Assumption:` stated as a range, or omit the number
entirely — a bare precise figure implies a precision the record does
not actually have, and precision is exactly what makes a fabricated
number convincing.
source: https://www.researchgate.net/publication/363213009_From_Noise_to_Bias_Overconfidence_in_New_Product_Forecasting (unhedged point estimates overstating the evidence behind them)

### 6. Cap accumulating open questions with a question budget
When the running count of open questions in a record passes a small
fixed budget (a handful, not dozens), stop asking further questions and
proceed on the best-labeled `Assumption:` for the remaining unknowns
instead of blocking the record on an answer — an unbounded open-
questions list defers all judgment to a reader who never asked for that
much homework, and a capped budget forces the record to state its
weakest points as assumptions rather than as silence.
source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/reduce-hallucinations (asking clarifying questions only when truly needed, rather than accumulating open questions indefinitely, is part of reducing ungrounded output)

## Related skills

- [market-analysis-evidence-rigor](../market-analysis-evidence-rigor/SKILL.md) — evidence-rigor vets sourcing per claim; this skill adds the label, do-not-invent, and question-budget layer on top.
- [product-discovery-hypothesis-testing](../product-discovery-hypothesis-testing/SKILL.md) — a hypothesis statement is a claim that needs a Fact/Inference/Assumption label before it is registered for testing.
- [growth-analytics-experiment-trust](../growth-analytics-experiment-trust/SKILL.md) — an experiment-trust verdict turns on whether a result is real evidence or an unconfirmed/fabricated signal.
- [user-discovery-evidence-strength-tagging](../user-discovery-evidence-strength-tagging/SKILL.md) — the nearest existing analog: this skill's Fact/Inference/Assumption labels generalize the behavioral/recounted/opinion tiering to non-interview records.
