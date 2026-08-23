---
status: proposed
files:
  - docs/issue-96/reports/knowledge-management/survey.md
  - docs/issue-96/reports/knowledge-management/scout-brief.md
  - docs/issue-96/proposals/motion-design-depth.md
  - skills/game-character-animation-and-motion/SKILL.md
  - skills/game-hit-reaction-and-impact/SKILL.md
  - skills/game-character-rendering-composition/SKILL.md
  - docs/issue-96/reports/knowledge-management.md
---

# Motion-design depth for the game-art skill family (phase 1: research + proposal)

Note on survey location (path note only — scouting was NOT skipped): the
current-state survey lives at
`docs/issue-96/reports/knowledge-management/survey.md`, role-scoped per
contract v3 s11/s19, rather than the generic
`docs/issue-96/reports/implementation/survey.md`, because this role
writes only its own record area. Scouting ran in full; its output is
`docs/issue-96/reports/knowledge-management/scout-brief.md`.

## Request

Issue #96 (requirement R1): tm-dicequest cuts 2-5 shipped flat geometric
tokens despite the three game-art skills being mounted; the user
rejected this on 2026-08-23 demanding MapleStory-grade motion
(tm-dicequest#58). Deepen `game-character-animation-and-motion` with
condition-matched rules for (a) layered rig decomposition
(head/torso/limbs/weapon), (b) the 6 canonical cycles
(idle/walk/jump/attack/hurt/death) with anticipation-contact-recover
pose breakdowns, (c) a silhouette-readability test at target render
scale — each rule with an evidence/source line; add cross-references to
`game-hit-reaction-and-impact` and `game-character-rendering-composition`
so a session that draws an entity as a single primitive without a
recorded rig decision fails the skills' own checklists; keep the
conformance suite green.

## Constraints

- `python3 scripts/check_skill_conformance.py` exits 0 after phase 2:
  rule blocks stay `### N. <title>` with a `source: <http(s) URL>` line
  each; frontmatter shape unchanged; `rule_count_floor` never exceeds
  actual rule count.
- `python3 -m pytest test/ -q` stays green (includes
  `test_full_repo_tree_is_conformant`).
- New rules must not restate what adjacent skills own
  (`game-feel-juice-and-feedback` owns juice; `html5-game-rendering-loop`
  owns tick mechanics) — survey's overlap list governs.
- Every claim traces to the scout brief's Sources list.
- One commit per subject with `Subject: issue-96` trailer; phase-2 work
  waits for a human Approve per contract v3 s19.

## Rationale

The observed failure (tm-dicequest#58) is that all three skills'
checklists are satisfiable by a single-primitive entity: rendering-
composition rule 4 lets a session declare "nothing moves independently"
and keep one node; animation rule 2 is satisfiable by tweening one shape.
The fix must therefore change what the checklists *demand*, not add more
prose.

Considered alternative A — author a NEW fourth skill
(`game-character-rig-and-keyframe-poses`) instead of deepening the three:
rejected because the dogfood failure happened *with the three skills
mounted*; a fourth skill would not be mounted more reliably than the
existing ones, and it would split the rig decision from the skills whose
output shapes (build spec, animation spec, impact contract) are the
artifacts sessions actually produce. Per the pattern-extraction skill's
root-cause rule, the root cause is "checklist satisfiable without the
behavior" — fixed at the checklists, not by a new entry.

Considered alternative B — enforce rig decomposition mechanically in
`check_skill_conformance.py` (a repo gate): rejected because the checker
validates SKILL.md files in this repo, not game sessions' output in other
repos; there is no mechanical surface here that sees a consuming
session's SVG.

Chosen: deepen the three existing skills in place — new numbered rules in
animation-and-motion (rig floor, 6-cycle pose breakdowns, per-pose
silhouette test), plus output-shape/checklist amendments in all three so
"no recorded rig decision" is an explicit fail condition, cross-referenced
between the skills.

## What will be done

Phase 2, on this branch after Approve:

1. `skills/game-character-animation-and-motion/SKILL.md` — add 3-4 rules
   with sources from the scout brief:
   - Layered rig floor: an animated gameplay entity decomposes into
     named parts (head / torso / limbs / weapon-or-tool at minimum),
     hierarchy parent→child, joint overlap; a single primitive is a
     recorded exception, never a default. (drawphics, Toon Boom cut-out
     docs, game-ace)
   - 6 canonical cycles: idle/walk/jump/attack/hurt/death each authored
     as key poses first — walk as contact/down/pass/up on a fixed frame
     grid; attack (and jump/hurt/death one-shots) as
     anticipation → contact → recover pose triads; per-cycle frame
     budgets (idle ~2, walk 4-12, attack 3+) per the MapleStory-anchor
     sources. (Wikipedia walk cycle, stevenschubert, garagefarm,
     mapleanime, sprite-ai)
   - Silhouette test per key pose at target render scale: each cycle's
     key poses filled solid black at shipped size must read as their
     action from outline alone. (animotionx, anim.works, parkland
     lecture)
   - Amend `## Procedure` and `## Output shape` so the animation spec
     includes the rig part list and per-cycle key-pose sheet with
     silhouette pass/fail — absence of a recorded rig decision fails
     the output shape.
   - Raise `rule_count_floor` to match.
2. `skills/game-character-rendering-composition/SKILL.md` — amend rule 4
   and the output shape: an animated gameplay entity's part split must
   name head/torso/limbs/weapon (cross-ref to animation-and-motion's
   rig floor); the build spec records the rig decision explicitly, and
   a single-primitive build without that recorded decision fails the
   spec.
3. `skills/game-hit-reaction-and-impact/SKILL.md` — amend the impact
   contract: hit reactions name which rig layer(s) flash/recoil (hurt
   pose from the rig, not whole-token tint); contract is unfillable for
   an entity with no recorded rig decision — cross-ref to both skills.
4. Run conformance + pytest; write the delivery record
   `docs/issue-96/reports/knowledge-management.md`; push to this PR.

## Out of scope

- New skills; changes to `game-feel-juice-and-feedback`,
  `html5-game-rendering-loop`, or any non-game skill.
- Checker/gate script changes; manifest opt-ins.
- Fixing tm-dicequest itself — this repo ships guidance, not that game.

## How you'll know it worked

- All three acceptance checks: (a) animation-and-motion carries sourced
  rules for rig decomposition, 6 cycles with pose breakdowns, and
  silhouette-at-render-scale; (b) the other two skills' checklists fail
  a single-primitive entity with no recorded rig decision (grep-able
  cross-references + explicit fail wording in Output shape sections);
  (c) `check_skill_conformance.py` exits 0 and pytest is green.
- A future dogfood session following the amended Output shapes cannot
  ship a flat token without writing down a rig exception.
