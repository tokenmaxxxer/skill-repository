---
name: product-discovery-rice-ice-prioritization
description: >-
  Use when comparing more than one opportunity or solution candidate for build priority and
  scoring or citing the evidence behind each score. Applies to the rice-ice-prioritization
  axis. Trigger on requests like "RICE 점수 매겨줘", "prioritize these opportunities", "should
  this be RICE or ICE", "what confidence do we really have behind this score". Ties
  Confidence to admissible Mom Test evidence (count + date range + paraphrase), flags ICE
  fallbacks explicitly, and surfaces near-ties instead of silently breaking them. Do NOT use
  to place or prune candidates on the tree before comparison (use
  product-discovery-opportunity-solution-tree-branching).
metadata:
  axis: rice-ice-prioritization
  rule_count_floor: 10
---

# RICE / ICE prioritization and evidence citation

Research trail: Intercom's original RICE model and the ICE simplification, fetched this session via ProductPlan glossary, PM Toolkit's RICE-vs-ICE comparison, and Evelance's research-integration guide; cross-checked against the Mom Test's evidence-admissibility rule (stated preference/hypothetical response is not admissible evidence) already binding on this role's proposal facet.

## Trigger

Apply this skill when more than one opportunity or solution candidate is
being compared for build priority and each candidate needs a RICE or
ICE score with its supporting evidence cited.

## Procedure

1. Score each candidate with RICE by default (rule 1); fall back to ICE,
   explicitly flagged, only when reach data is genuinely unavailable
   (rules 2-3).
2. Cite evidence for any Reach or Impact estimate as one line with
   count, approximate date range, and paraphrase (rule 4); exclude
   stated preference or hypothetical response from the Confidence input
   (rule 5); tie Confidence to the strength of the admissible evidence
   actually cited (rule 6).
3. Use the same effort unit across every candidate in one prioritization
   pass (rule 7).
4. When two or more candidates land within a narrow score band, state
   the near-tie explicitly and resolve it by re-examining the
   weakest-evidenced input, rather than picking the numerically higher
   score (rule 8).
5. Drop the RICE/ICE scoring step entirely when only one candidate
   exists to compare (rule 9), and remove any evidence line missing a
   count or date range rather than keeping it as a lesser citation
   (rule 10).

## Output shape

A RICE (or explicitly-flagged ICE-fallback) score per compared
candidate, each Reach/Impact input backed by a count+date+paraphrase
citation, near-ties flagged rather than silently broken, using one
consistent effort unit across the whole comparison.

## Rules

1. When more than one opportunity or solution candidate is being compared for build priority, score each with RICE (Reach, Impact, Confidence, Effort) as the default framework, not ICE — RICE is preferred "when you have specific reach data, detailed effort estimates, and need precise prioritization for roadmap planning," and differentiates impact from reach where ICE "mushes together" the two. source: https://pmtoolkit.ai/compare/rice-vs-ice

2. When reach data is genuinely unavailable (no usage/traffic baseline exists yet, e.g. pre-launch or a brand-new segment), fall back to ICE (Impact, Confidence, Effort) explicitly flagged as a fallback in the record, rather than fabricating a reach estimate to force a RICE score — ICE exists specifically because "startups often lack the historical data needed to accurately estimate Reach in RICE scoring," so an invented reach number is worse than an honestly-flagged ICE substitute. source: https://pmtoolkit.ai/compare/rice-vs-ice

3. When a fallback to ICE is used, write the flag next to the score itself (e.g. "ICE (RICE unavailable: no reach baseline)"), not in a separate methodology footnote — a bare ICE score presented without the flag reads as a deliberate framework choice rather than a data-availability compromise, which misleads a later reader comparing it against RICE-scored items. source: https://pmtoolkit.ai/compare/rice-vs-ice

4. When citing evidence to support a Reach or Impact estimate, write it as one line containing interview/observation count, an approximate date range, and a short paraphrase (e.g. "6 interviews, 2026-06 to 2026-07: users described re-entering the same filter every session") — a bare claim with no count or date is not a citation and cannot be weighed against other evidence when opportunities are compared. source: (role's own binding Mom Test rule, applied at prioritization time)

5. When the only evidence available for an opportunity is a stated preference or a hypothetical response ("I would use X if you built it"), exclude it from the Confidence input to the RICE/ICE score — the Mom Test rule this role already carries holds that stated preference or hypothetical response is not admissible evidence, so admitting it into a Confidence score silently launders inadmissible evidence into a numeric-looking score.

6. When Confidence is scored, tie the percentage to the strength of the admissible evidence actually cited (e.g. 100% = hard data/observed behavior, 80% = solid but incomplete data, 50% = qualitative/anecdotal only) rather than to gut feeling — Intercom's original RICE model defines Confidence precisely to let a team be honest that a promising-looking Impact/Reach combination might be based on weak evidence, so an ungrounded Confidence score defeats that purpose. source: https://www.productplan.com/glossary/rice-scoring-model

7. When Effort is estimated for the denominator, use the same unit (e.g. person-weeks) across every candidate being compared in one prioritization pass — RICE divides the numerator by Effort specifically to compare "bang for the buck" across otherwise-unlike candidates, so mixing units (one item in days, another in months) breaks the comparability the score exists to provide. source: https://www.productplan.com/glossary/rice-scoring-model

8. When two or more candidates land within a narrow score band of each other (a near-tie), do not silently pick the numerically higher one — state the near-tie explicitly and resolve it by re-examining the weakest-evidenced input (usually Confidence or Reach) rather than treating a fractional score gap as a decisive signal; RICE scores are estimates multiplied together, so small gaps are within the framework's own estimation noise.

9. **REMOVAL**: When a proposal has only one opportunity or solution candidate (nothing to compare it against), drop the RICE/ICE scoring step entirely rather than computing a score with nothing to rank it against — this facet's own gate applies "when more than one opportunity or solution candidate is compared"; scoring a lone candidate produces a number with no comparative meaning and should not be presented as a prioritization result.

10. **REMOVAL**: When an evidence line cannot state an approximate date range or a count (e.g. a claim sourced from "general market impression" or an uncited secondary summary), remove it from the cited evidence list rather than including it as a weaker-but-still-present citation — the required shape is count + date range + paraphrase, not a lesser format; an entry missing the count or date is a bare claim wearing a citation's formatting and must be cut or reworked into a real citation.
