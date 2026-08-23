# Current-state survey — issue #96 (motion-design depth for the game-art skill family)

Written BEFORE the scout sweep and before the proposal, per the
survey-first ordering. Role-scoped path (contract v3 s11/s19): this role
writes only under `docs/issue-96/reports/knowledge-management/`, never
`reports/implementation/`.

## Write surface actually expected to be touched

Phase 1 (this PR):
- `docs/issue-96/reports/knowledge-management/survey.md` (this file)
- `docs/issue-96/reports/knowledge-management/scout-brief.md`
- `docs/issue-96/proposals/motion-design-depth.md`

Phase 2 (gated on Approve, listed so the survey covers the real surface):
- `skills/game-character-animation-and-motion/SKILL.md`
- `skills/game-hit-reaction-and-impact/SKILL.md`
- `skills/game-character-rendering-composition/SKILL.md`
- `docs/issue-96/reports/knowledge-management.md` (delivery record)

## What the repository looks like today

- 273 skills; `python3 scripts/check_skill_conformance.py` exits 0
  ("273 skills checked"); `python3 -m pytest test/ -q` → 12 passed.
- Conformance schema (mechanical): frontmatter `name:` == directory,
  `description:` with a trigger marker, `axis:` + `rule_count_floor:`,
  every `### N.` rule block carries a `source: <http(s) URL>` line.
- The three target skills landed in issue #93 (commit 7e39633) at
  wave-2 depth: 5-6 rules each, condition → choice → why → source →
  counter-example shape, `## Procedure` + `## Output shape` sections.

## Gap analysis against issue #96's acceptance (the unknowns scout must aim at)

Evidence: tm-dicequest#58 — sessions with all three skills mounted still
shipped single flat geometric tokens; user rejected 2026-08-23 demanding
MapleStory-grade motion.

1. **Rig decomposition** — rendering-composition rule 4 says "group parts
   by animation need" but never names a minimum part set. A session can
   satisfy it with ONE node ("nothing moves independently") — exactly the
   observed failure. No rule forces head/torso/limbs/weapon layering for
   an animated gameplay entity, and no rule requires the rig decision to
   be *recorded*.
2. **Canonical cycles with pose breakdowns** — animation-and-motion rule 1
   declares the state machine and rule 2 adds anticipation/follow-through
   frames, but no rule requires the 6 canonical cycles
   (idle/walk/jump/attack/hurt/death) to exist as *keyframed pose
   sequences* (anticipation–contact–recover key poses per cycle). A
   tween between two positions of one primitive passes today's rules.
3. **Silhouette test at render scale** — rendering-composition rule 1 has
   the silhouette gate but it lives only in the rendering skill; the
   animation skill never requires key poses to pass a silhouette-read
   test at target render scale, so motion poses are never silhouette-
   checked.
4. **Cross-reference enforcement** — hit-reaction-and-impact's checklist
   (impact contract) accepts a single-primitive entity: nothing in it
   asks "which rig layer flashes/recoils?". Related-skills links are
   hop-pointers, not checklist items — a session can complete each
   skill's Output shape without ever making a rig decision.

Unknowns for scout: authoritative sources for (a) layered rig
decomposition part sets in 2D game rigs, (b) per-cycle key-pose
breakdowns (walk cycle contact/down/pass/up canon; attack
anticipation-contact-recover), (c) silhouette testing of *poses* at
render scale, (d) MapleStory-style layered 2D character art as the
quality anchor.

## Adjacent skills (overlap risk)

- `game-feel-juice-and-feedback` — owns squash/stretch/shake; new rules
  must stay on rig/pose/silhouette, not juice.
- `html5-game-rendering-loop` — owns frame timing; keep cycle rules
  about poses, not tick mechanics.
- `brand-design-icon-system-svg` — owns icon pixel-fitting; silhouette-
  at-scale rule must cite game-art sources, not restate icon rules.

## Constraints that bind phase 2

- Each new rule needs its own evidence/source line (acceptance check a).
- Conformance suite must stay green (acceptance check c) — additions
  keep frontmatter, rule numbering (`### N.`), and source-line format.
- `rule_count_floor` may rise but must not exceed the actual rule count.
- One commit per subject with `Subject: issue-96` trailer.

## Skill-verdict lines (issue #2039; invoke-before-apply #2062)

- skill-verdict: knowledge-management-curation-pruning — not-applicable: no entry is uncited/flagged for pruning; this issue deepens live entries.
- skill-verdict: knowledge-management-structure-findability — not-applicable: no new entry is being filed or renamed in phase 1; existing skill files keep their names and Diátaxis shape.
- skill-verdict: knowledge-management-taxonomy-tagging — not-applicable: no controlled-vocabulary term is added or re-scoped; axes stay unchanged.
- skill-verdict: knowledge-management-supersession-lifecycle — not-applicable: rules are deepened in place, none superseded or deprecated.
- skill-verdict: knowledge-management-pattern-extraction — applied: invoked; used to frame tm-dicequest#58's rejection as a pattern-shaped lesson (checklist-satisfiable-without-the-behavior) feeding the proposal's cross-reference design.
- skill-verdict: game-character-rendering-composition — applied: invoked; its silhouette-gate and rig-split rules are the current-state baseline this survey's gap analysis is measured against.
- skill-verdict: technical-feasibility-build-vs-buy — not-applicable: no dependency or prior-art build-vs-buy decision arises; work is authoring skill prose.
