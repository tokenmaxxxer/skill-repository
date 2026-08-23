---
name: defect-verification-severity-band-assignment
description: >-
  Use when assigning a severity band to a reproduced defect — reading the band
  off the fixed technical-impact lookup table by halting/degrading/cosmetic
  tier, independent of business priority or how clean the upstream review
  record looks. Trigger on requests like "what severity band is this defect",
  "blocking or degraded tier", "severity vs priority call", "재현된 결함 심각도 등급
  매겨줘". Do NOT use for deciding whether the defect reproduced at all (use
  defect-verification-reproduction-evidence-quality); for writing the band
  onto a verify-record.md finding block, see verify-severity-classification.
metadata:
  axis: severity-band-assignment
  rule_count_floor: 8

---

# Severity-band assignment for a reproduced defect

## Trigger

Apply this skill when assigning a severity band to a reproduced
defect.

## Procedure

1. Assign severity by technical impact on functionality alone — never
   by business urgency, deadline pressure, or reporter annoyance
   (rule 1).
2. Band a defect that halts the system, blocks the user from
   proceeding, or blocks further verification work at the top tier
   (blocking) (rule 2).
3. Band a defect that degrades core functionality without halting it
   below the halting tier (rule 3).
4. Apply the same band criteria the same way every time rather than
   re-deriving them per finding (rule 4).
5. Band a cosmetic or non-required, non-functional defect at the
   lowest tier rather than the mid tier (rule 5).
6. Do not let a clean review record pull a reproduced defect's
   severity down (rule 6).
7. When a reproduced defect only manifests under a narrow, hard-to-hit
   precondition, band by the impact if it fires, not by how rarely it
   fires (rule 7).
8. State which band criterion actually drove the assignment (halts the
   system / degrades core function / cosmetic only) alongside the band
   itself (rule 8).
9. Retire any locally-improvised severity vocabulary outside the
   deterministic band's defined tiers (rule 9), and retire treating
   priority language (urgent, do this sprint, can wait) as an input to
   the severity call (rule 10).
10. Apply the band lookup as a fixed intersection table (technical-
    impact tier x criterion), not a per-finding freehand weighing
    (rule 11).

## Output shape

A severity band read off the fixed technical-impact x criterion lookup
table, attributed to the criterion that drove it, held independent of
priority language and upstream review cleanliness, and applied
consistently across similar defects.

Research trail: bug severity vs. priority literature (QAmadness defect-management guide, Kualitee severity-level and severity-vs-priority guides, Bird Eats Bug severity guide, QATestLab severity-levels article). All fetched/searched this session.

## Rules

1. Assign severity by technical impact on functionality alone — never by business urgency, deadline pressure, or how annoying the defect is to the reporter — because severity is a technical measure while priority (a business decision review/coding may make later) is a different axis entirely, and conflating the two is "one of the most common sources of triage dysfunction." source: https://www.qamadness.com/bug-severity-vs-priority/

2. When a reproduced defect halts the system, blocks the user from proceeding, or blocks further verification/testing work itself, band it at the top tier (blocking) — some teams reserve a level above "critical" specifically for defects that "halt all testing or development work entirely, not just the affected feature," and a defect that stops your own verification pass from continuing meets that bar by construction. source: https://www.kualitee.com/blog/guide/bug-severity-levels-explained/

3. When a reproduced defect degrades core functionality without halting it (wrong output on a valid input, a requirement silently unmet) but leaves the system otherwise usable, band it below the halting tier — severity ranges "from complete system crashes to minor cosmetic issues," so a mid-band defect needs mid-band language, not automatic escalation to blocking just because it is real. source: https://www.qamadness.com/bug-severity-vs-priority/

4. Never let severity ratings fluctuate between similar defects on ad hoc judgment — when severity ratings are unreliable, "every defect list needs a second pass before anyone can trust it," which is exactly the failure a deterministic band lookup exists to prevent; apply the same band criteria the same way every time rather than re-deriving them per finding. source: https://www.kualitee.com/blog/guide/bug-severity-levels-explained/

5. When a defect is cosmetic or affects only a non-required, non-functional surface (naming, formatting, a nice-to-have polish gap), band it at the lowest tier rather than the mid tier — severity's low end is explicitly "minor cosmetic issues," distinct from defects that touch actual functionality even mildly. source: https://www.qamadness.com/bug-severity-vs-priority/

6. Do not let a clean review record pull a reproduced defect's severity down — severity is a property of the defect's technical impact as independently reproduced, not a function of how thorough or clean the upstream review looked; a blocking-banded finding stays blocking even against a review record with zero open items.

7. When a reproduced defect only manifests under a narrow, hard-to-hit precondition (a specific race, a rare input), band by the impact IF it fires, not by how rarely it fires — severity measures technical impact, and likelihood/frequency is a priority-side concern (how soon to fix), not a severity-side one; downgrading a would-be-blocking defect because it is rare conflates severity with priority the same way rule 1 forbids.

8. State which band criterion actually drove the assignment (halts the system / degrades core function / cosmetic only) alongside the band itself, rather than recording a bare band with no rationale — an unattributed severity call cannot be checked against the deterministic lookup by a later reader, which defeats the purpose of having a lookup instead of freehand judgment.

9. **REMOVAL**: Retire any locally-improvised severity vocabulary that isn't one of the deterministic band's defined tiers (ad hoc labels like "annoying," "nice to fix," "urgent") — QA guidance is explicit that severity and priority are "distinct" axes with their own defined vocabularies, and inventing a third informal vocabulary on top reintroduces the exact ambiguity the severity/priority split exists to remove. source: https://www.kualitee.com/blog/bug-management/severity-levels-vs-priority-levels-bug-tracking/

10. **REMOVAL**: Stop treating "priority" language (urgent, do this sprint, can wait) as an input to the severity call — priority is "a business decision" that belongs to whoever owns scheduling (coding or a human), and the deterministic band lookup this axis governs must stay upstream of and blind to that decision, never downstream of it. source: https://www.qamadness.com/bug-severity-vs-priority/

11. Apply the band lookup as a fixed intersection table (technical-impact tier x criterion), not a per-finding freehand weighing — deterministic severity classification tooling is built so "given the same inputs, every engineer... reaches the same row," and a lookup that is re-derived by judgment each time rather than read off a fixed table reintroduces exactly the rating drift rule 4 already forbids, just at the mechanism level instead of the outcome level. Adoption evidence: multi-source coverage of deterministic severity/priority matrix tooling, fetched 2026-08-13 (qamadness.com/bug-severity-vs-priority, softwaretestershub.in/tools/severityprioritymatrix).
