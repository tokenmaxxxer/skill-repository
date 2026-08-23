---
code_under_review: 9578cea98aad87431760854f4c713cf0acb5939c
loop_state: landed
type: skill-deepening
breaking: false
verdict: delivered
---

# Issue #96 phase-2 delivery record — knowledge-management

kind: implementation
loop_state: landed

## What was done

Implemented the approved proposal
`docs/issue-96/proposals/motion-design-depth.md` exactly, deepening the
three game-art skills so their checklists can no longer be satisfied by a
single flat geometric token:

- `skills/game-character-animation-and-motion/SKILL.md` — added rules 7-9
  (layered rig floor with named head/torso/limbs/weapon parts; six
  canonical cycles idle/walk/jump/attack/hurt/death authored key-poses
  first with per-cycle frame budgets; silhouette test per key pose at
  target render scale), each with a `source:` line traceable to the scout
  brief's Sources list; Procedure steps 7-9 and Output shape amended so a
  missing recorded rig decision fails the output shape;
  `rule_count_floor` raised 5→9; Related-skills cross-references extended.
- `skills/game-character-rendering-composition/SKILL.md` — rule 4 and
  Output shape amended: animated entities must name the rig part split,
  the rig decision is recorded explicitly, and a single-primitive build
  without a recorded exception fails the spec.
- `skills/game-hit-reaction-and-impact/SKILL.md` — impact contract
  amended: hit reactions name which rig layer(s) flash/recoil; contract
  declared unfillable for an entity with no recorded rig decision;
  cross-references to both sibling skills added.

Verification: `python3 scripts/check_skill_conformance.py` exit 0
("273 skills checked"); `python3 -m pytest test/ -q` → 12 passed
(0 skipped) in 0.04s, including `test_check_skill_conformance.py`.

## Why

Issue #96 / requirement R1: tm-dicequest cuts 2-5 shipped flat geometric
tokens with these three skills mounted (user rejection tm-dicequest#58,
2026-08-23). Root cause per the approved proposal's Rationale: the
checklists were satisfiable without rig or keyframe decisions, so the fix
changes what the checklists demand rather than adding a fourth skill or a
mechanical gate.

## Upstream

basis: docs/issue-96/proposals/motion-design-depth.md (approved via
issue-level comment `APPROVE issue-96/knowledge-management` from
JiwonJung94, an approvers.md account, single-account mode).

## What did not work

None.

## Skill verdicts

- skill-verdict: knowledge-management-curation-pruning — not-applicable: update-vs-supersede decision for these entries was already made and approved in phase 1.
- skill-verdict: knowledge-management-structure-findability — not-applicable: no new entry filed; existing entries deepened in place with names and structure unchanged.
- skill-verdict: knowledge-management-taxonomy-tagging — not-applicable: no vocabulary term added, merged, or re-scoped.
- skill-verdict: knowledge-management-supersession-lifecycle — not-applicable: edits are additive deepening, not replacement/deprecation; no supersession marker warranted.
- skill-verdict: knowledge-management-pattern-extraction — not-applicable: no retrospective lesson extracted this phase; the root-cause pattern was applied in phase 1's proposal.
- skill-verdict: game-character-rendering-composition — applied: invoked; its rule 4 (group-by-animation-need) and Output shape wording anchored the rig-floor cross-references and the amended fail condition in that skill.

## Open findings

None.
