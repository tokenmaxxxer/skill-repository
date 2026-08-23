---
name: user-discovery-evidence-strength-tagging
description: >-
  Use when tagging or weighting interview-log claims by evidence strength — distinguishing
  directly-observed behavioral claims from secondhand recounted ones and from stated
  opinions/intentions, or when computing an evidence count that must exclude opinion-tier
  entries. Trigger on requests like "이 인터뷰 로그 증거 등급 태깅해줘", "tag these claims
  behavioral/recounted/opinion", "does this quote count as evidence", "weight the log before
  the verdict". Do NOT use for drafting the questions that elicit the evidence (use
  user-discovery-question-design-past-behavior).
metadata:
  axis: evidence-strength-tagging
  rule_count_floor: 8
---

# Evidence-strength tagging: behavioral / recounted / opinion

Research trail: behavioral vs. attitudinal interview evidence distinction (ventureforall.com, structured-interview bias literature on ScienceDirect); the Mom Test's evidence-quality framing. All searched this session.

## Trigger

Apply this skill when logging or reviewing an interview-log claim that
needs an evidence-strength tag (`behavioral`/`recounted`/`opinion`), or
when computing a count or verdict that depends on weighting or excluding
claims by that tier — distinct from the sibling axes that design the
questions (question-design-past-behavior) or report the resulting
prevalence (verdict-prevalence-reporting).

## Procedure

1. For each claim, check whether it is grounded in something the
   interviewee did and can point to; if so tag `behavioral` (rule 1).
2. If the claim is about a real past event but not independently
   verifiable from the conversation (secondhand, a memory of someone
   else's action), tag `recounted` instead (rule 2).
3. If the claim is a stated preference, prediction, or attitude, tag
   `opinion` (rule 3).
4. Tag each occurrence of a repeated claim independently rather than
   merging phrasings across the interview (rule 4).
5. Resist upgrading a vivid hypothetical answer to `behavioral` — the
   tag follows whether the event happened, not how concrete the telling
   is (rule 5).
6. When totaling evidence toward a prevalence count, weight `behavioral`
   full, `recounted` reduced, and exclude `opinion` entirely (rule 6).
7. Tag evidence strength immediately after each answer, not
   retrospectively at interview end, to avoid confirmation-bias upgrades
   (rule 7).
8. Drop untaggable entries with no underlying event rather than
   defaulting them into `opinion` (rule 8).
9. Drop any prior binary confirmed/not-confirmed tag scheme entirely
   rather than layering the three-tier scheme on top of it (rule 9).

## Output shape

A per-claim evidence-strength tag (`behavioral`/`recounted`/`opinion`)
attached at log-write time, plus — when computing a prevalence count —
the tier-weighted total with opinion-tier entries excluded and
untaggable entries dropped rather than defaulted.

## Rules

1. When a claim in the interview log is grounded in something the interviewee did and can point to (a tool they use today, an action taken last week, a cost they paid), tag it `behavioral` — behavioral evidence is anchored in past experience and is the strongest of the three tiers because it is objective and hard to fabricate on the spot. source: https://www.ventureforall.com/p/from-assumptions-to-evidence-are

2. When a claim describes something the interviewee reports having done but you cannot independently verify from the conversation (a secondhand account, a memory of a colleague's workaround), tag it `recounted` rather than `behavioral` — recounted evidence is still about real past events but is one inferential step removed from the interviewee's own direct action, so it must not be pooled with directly-observed behavioral evidence at the same confidence weight. source: https://mtlynch.io/book-reports/the-mom-test/

3. When a claim is a stated preference, prediction, or attitude ("I'd probably use this," "I think this would help"), tag it `opinion` — attitudinal questions produce stated intentions, and intentions are a poor substitute for behavior, so opinion-tagged claims must never by themselves satisfy a pain-confirmed verdict. source: https://www.ventureforall.com/p/from-assumptions-to-evidence-are

4. When the same underlying claim appears in the log with different phrasing at different points in one interview, tag each instance independently rather than merging them into one tag — an interviewee can drift from a `behavioral` answer early on to an `opinion` restatement later once they start reasoning about your idea, and merging tags hides that drift from the saturation count. source: https://blog.uxtweak.com/the-mom-test/

5. When a candidate has answered a question about a hypothetical product feature with enthusiasm, do not upgrade that enthusiasm to `behavioral` even if phrased with specific detail — vivid hypothetical detail is still hypothetical; the tag is determined by whether the underlying event actually happened, not by how concrete or confident the description sounds. source: https://mtlynch.io/book-reports/the-mom-test/

6. When counting evidence toward a pain-confirmed verdict's "N of M" prevalence, weight `behavioral` entries at full weight, `recounted` at reduced weight, and exclude `opinion` entries from the count entirely — collapsing all three tiers into one undifferentiated N inflates confidence with the weakest tier's contribution. source: https://www.ventureforall.com/p/from-assumptions-to-evidence-are

7. When logging an interview, tag evidence strength at write time (immediately after each answer), not retrospectively at the end of the interview — retrospective tagging is vulnerable to confirmation bias, where a researcher who wants the hypothesis confirmed unconsciously upgrades ambiguous answers to `behavioral` in hindsight. source: https://www.sciencedirect.com/science/article/pii/S1576596217300427

8. **REMOVAL**: When an evidence log entry has no clear underlying event to point to (the interviewee gave a vague, ungrounded impression), do not force a tag onto it by defaulting to `opinion` and counting it anyway — drop untaggable entries from the evidence log rather than padding the opinion tier with noise that was never a real data point. source: https://www.ventureforall.com/p/from-assumptions-to-evidence-are

9. **REMOVAL**: When a prior interview log used a binary "confirmed/not confirmed" tag per claim instead of the three-tier scheme, drop the binary tag entirely rather than layering the three-tier scheme on top of it — a binary tag collapses exactly the behavioral/recounted/opinion distinction this axis exists to preserve, so keeping both invites confusion about which tag is authoritative. source: https://www.ventureforall.com/p/from-assumptions-to-evidence-are

## Related skills

- [research-evidence-discipline](../research-evidence-discipline/SKILL.md) — generalizes this skill's behavioral/recounted/opinion tiering into Fact/Inference/Assumption labeling for non-interview research records.
