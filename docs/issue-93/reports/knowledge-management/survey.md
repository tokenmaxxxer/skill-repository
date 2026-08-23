# Current-state survey — issue #93 (game skill wave 2)

Written BEFORE the scout sweep and before the proposal, per the
survey-first ordering. Role-scoped path (contract v3 s11/s19): this role
writes only under `docs/issue-93/reports/knowledge-management/`, never
`reports/implementation/`.

## Write surface actually expected to be touched

Phase 1 (this PR):
- `docs/issue-93/reports/knowledge-management/survey.md` (this file)
- `docs/issue-93/reports/knowledge-management/scout-brief.md`
- `docs/issue-93/proposals/game-skill-wave-2.md`

Phase 2 (gated on Approve, listed so the survey covers the real surface):
- `skills/game-character-animation-and-motion/SKILL.md`
- `skills/game-hit-reaction-and-impact/SKILL.md`
- `skills/game-character-rendering-composition/SKILL.md`
- `skills/game-growth-system-design/SKILL.md`
- `docs/issue-93/reports/knowledge-management.md` (delivery record)

## What the repository looks like today

- 269 skills; `python3 scripts/check_skill_conformance.py` prints
  `269 skills checked` and exits 0.
- Conformance schema (read from the checker): frontmatter `name:` ==
  directory name; non-empty `description:` with a trigger marker
  (`use when` etc.); `axis:` required alongside `rule_count_floor:`;
  every `### N. <title>` block under a rules section carries at least
  one `source: <http(s) URL>` line — the citation gate is mechanical.
- Opt-in manifests: `scripts/procedure_authored_skills.txt` (199
  entries; listed skills need `## Trigger`, `## Procedure`,
  `## Output shape`) and `scripts/issue_1996_use_when_source_manifest.txt`
  (9 entries). Wave-1 game skills are authored procedure-shaped but the
  manifest decision was left out of scope in issue #90; same stance
  applies here.
- Wave 1 (issue #90, merged) established the game family's shape:
  `game-design-core-loop-and-progression`,
  `game-feel-juice-and-feedback`, `html5-game-rendering-loop`,
  `game-ui-board-and-lane-layout` — each single-axis, sparse-tier,
  condition -> choice -> why -> source rules, `## Related skills`
  cross-links, ~200 lines.

## Adjacent skills found (overlap risk to design around)

- `game-feel-juice-and-feedback` — nearest neighbour to the new
  hit-reaction skill: it owns juice staging, feedback-per-action, and
  screen-shake restraint. The new skill must own the *combat impact
  contract* (hit-stop bands, knockback curves, i-frames, damage
  numbers) and cross-link rather than restate shake/juice rules.
- `game-design-core-loop-and-progression` — nearest neighbour to
  growth-system design: it owns monotonicity, cost-curve direction,
  sink-before-source, deterministic-when-gating. The new skill must go
  *deeper* (per the issue): cross-session pacing curves, per-currency
  sink/source lifecycle, upgrade-choice cadence, retention patterns —
  not restate wave-1 rules.
- `html5-game-rendering-loop` — owns frame timing/loop structure; the
  new animation skill owns per-character state machines and CSS/DOM
  animation discipline on top of that loop.
- `game-ui-board-and-lane-layout`, `ux-engineering-color-visibility`,
  `accessibility-aria-and-contrast-rules` — the rendering-composition
  skill touches readability/z-order; contrast and target-size rules
  stay in their home skills, cross-linked.
- No existing skill covers sprite/SVG character state machines,
  hit-stop/knockback conventions, silhouette/part-layered character
  rigs, or session-scale progression pacing — the four gaps are real.

## Unknowns the scout sweep must aim at

1. Authoritative timing bands: anticipation/follow-through durations,
   hit-stop duration norms — need practitioner sources, not folklore.
2. Knockback-curve and i-frame conventions with citable sources.
3. Silhouette-first character-readability doctrine and layered-rig
   (SVG/DOM) composition sources.
4. Deterministic-progression retention evidence (the issue names
   "RD2-class evidence") and sink/source lifecycle sources beyond the
   Unity economy guide already cited in wave 1.
