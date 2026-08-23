---
name: user-discovery-follow-up-ladder-depth
description: Use when deciding how deep to follow up on an interviewee's answer — chaining "why"/"how" questions (laddering) toward a root cause or personal value instead of accepting the first surface-level attribute or complaint.
metadata:
  axis: follow-up-ladder-depth
  rule_count_floor: 8
---

# Follow-up ladder: laddering / Five Whys depth per hypothesis

Research trail: Toyota's Five Whys (via hyperlatam and playbookux explainer pieces on customer-interview application); UXmatters and IxDF (Interaction Design Foundation) laddering-technique literature distinguishing attribute→consequence→value chains from bare root-cause chains. All searched this session.

## Trigger

Apply this skill when an interviewee gives a surface-level attribute,
complaint, or root-cause answer and you must decide whether/how far to
follow up with further "why"/"how" questions before moving to the next
script item — distinct from the sibling axis that designs the base
question wording (question-design-past-behavior).

## Procedure

1. On a surface-level attribute or preference statement, ask "why is
   that good/important" instead of advancing the script (rule 1).
2. Ask "why" up to five times in sequence on a stated problem, stopping
   earlier only once an answer names a cause the interviewee cannot
   further explain (rule 2).
3. If a "why" answer is itself another surface fact, continue laddering
   on that fact rather than accepting it as the endpoint (rule 3).
4. Ladder sideways with "how" as well as "why" to connect a value to a
   concrete design/product decision (rule 4).
5. On a vague root-cause answer, press for a concrete instance before
   continuing the why-chain (rule 5).
6. Stop and treat a personal/organizational value answer as the ladder's
   endpoint once reached (rule 6).
7. When competitive/differentiation intelligence is also a goal, run
   Five Whys and laddering together rather than either alone (rule 7).
8. Drop any scripted single-fixed-follow-up structure that caps every
   hypothesis at the surface-attribute rung (rule 8).
9. Once a root-cause or value-level answer is reached, drop remaining
   scripted "why" prompts for that thread rather than exhausting a fixed
   count (rule 9).

## Output shape

A completed ladder per hypothesis thread — the chain of why/how
follow-ups actually asked, ending at a value or verified root-cause
answer (or, for a still-surface answer, a note that the ladder did not
yet reach an endpoint) — rather than a single unfollowed first answer.

## Rules

1. When an interviewee states a surface-level complaint or attribute preference ("I chose X because it's fast"), ask "why is that good/important" rather than moving to the next script question — laddering's core move is chaining "why" questions from attribute to consequence to personal value, and stopping at the first stated attribute discards the two deeper rungs. source: https://www.uxmatters.com/mt/archives/2009/07/laddering-a-research-interview-technique-for-uncovering-core-values.php

2. When probing the root cause of a stated problem, ask "why" up to five times in sequence, stopping earlier only once an answer names a cause the interviewee cannot further explain (a true root cause, not a deflection) — the Five Whys rule targets root-cause discovery, and stopping after one or two whys usually surfaces a symptom, not the cause. source: https://www.hyperlatam.com/the-power-of-the-five-whys-rule-in-customer-interviews/

3. When the interviewee's answer to a "why" is itself another surface fact rather than a value or root cause, continue laddering on that new fact instead of accepting it as the endpoint — a chain that terminates on a still-factual (not motivational/causal) answer has not reached the value or root-cause rung the technique is for. source: https://ixdf.org/literature/topics/why-how-laddering

4. When you need to connect a stated preference to a design/product decision, ladder sideways with "how" as well as "why" — laddering explores both why (uncovers emotional/value drivers) and how (connects those values to concrete features), so a why-only chain misses the how-linkage needed to act on the value once found. source: https://ixdf.org/literature/article/laddering-questions-drilling-down-deep-and-moving-sideways-in-ux-research

5. When an interviewee gives a vague or generic root-cause answer ("it's just always been slow"), press with a concrete-instance follow-up ("what specifically was slow, the last time") before continuing the why-chain — a why-chain built on a vague premise ladders to a vague, unusable value statement regardless of how many whys are asked. source: https://www.playbookux.com/five-whys/

6. When laddering toward a personal/organizational value ("why does that matter to you/your business"), treat that value-level answer as the ladder's endpoint and stop — laddering's three-question core (attribute → consequence → value) is complete once a value or core-business-relevance answer is reached; continuing to ladder past a genuine value answer yields diminishing, off-topic returns. source: https://study.com/academy/lesson/ladder-interviews-in-qualitative-marketing-research.html

7. When competitive/differentiation intelligence is the goal (not just usability insight), apply the Five Whys and laddering together rather than either alone — the two techniques are complementary (Five Whys for root cause, laddering for value structure), and the combination surfaces both what happened and why it mattered to the interviewee. source: https://www.octopusintelligence.com/the-five-whys-and-laddering-competitive-intelligence-techniques-for-that-matter/

8. **REMOVAL**: When a scripted interview guide lists a fixed single follow-up per question with no room to re-ladder, drop the fixed-depth-one script structure — a rigid one-follow-up script structurally caps every hypothesis at the surface-attribute rung and can never reach the root cause or value rung rules 1-3 require. source: https://www.hyperlatam.com/the-power-of-the-five-whys-rule-in-customer-interviews/

9. **REMOVAL**: When the interviewer has already reached a root-cause or value-level answer (rule 6), drop any remaining scripted "why" prompts for that thread rather than mechanically exhausting a fixed why-count — Five Whys is a stopping heuristic keyed to reaching the cause, not a mandatory five-question quota, and continuing past the cause wastes interview time the ladder no longer needs. source: https://www.playbookux.com/five-whys/

## Related skills

- [user-discovery-question-design-past-behavior](../user-discovery-question-design-past-behavior/SKILL.md) — the ladder's starting rung is the past-behavior question this skill designs.
