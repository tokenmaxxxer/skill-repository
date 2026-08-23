---
code_under_review: 7e39633dfc350a949680bbd6e5ee6bda1c3bc46f
loop_state: landed
kind: implementation
type: implementation
breaking: false
verdict: delivered
---

# Issue #93 — game skill wave 2, phase-2 delivery record (knowledge-management)

## What was done

Authored the four SKILL.md files exactly as the approved proposal
(docs/issue-93/proposals/game-skill-wave-2.md) specifies, on branch
issue-93/knowledge-management:

- skills/game-character-animation-and-motion/SKILL.md — axis
  character-animation-and-motion, 6 rules (floor 5): explicit state
  machine before per-state tuning, anticipation/follow-through frame
  bands, transition vs keyframes+steps() vs JS-transform choice,
  compositor-only (transform/opacity) discipline, per-state
  duration/interruptibility table, sprite-sheet loop/one-shot norms.
- skills/game-hit-reaction-and-impact/SKILL.md — axis
  hit-reaction-and-impact, 5 rules (floor 5): hit-stop bands by attack
  weight (≈9/11/13 frames anchor), decaying knockback curves, i-frames
  bound to named recovery states with flicker, damage-number
  readability, screen-feedback restraint cross-linked to
  game-feel-juice-and-feedback.
- skills/game-character-rendering-composition/SKILL.md — axis
  character-rendering-composition, 5 rules (floor 4): silhouette-first
  gate, trunk→limbs→head→details build order, shape language before
  color, animation-need-driven SVG/DOM part split with transform-flip
  facing, named z-order layer contract.
- skills/game-growth-system-design/SKILL.md — axis growth-system-design,
  5 rules (floor 5): cross-session pacing via purchase intervals,
  per-currency source/sink lifecycle audit, designed upgrade-choice
  cadence, deterministic gating vs chance variety, return cadence as a
  stated parameter or omitted.

Each file carries the wave-1 structure (`## Trigger`, `## Procedure`,
`## Output shape`, `## Decision rules` with per-rule `source:` URL and
`counter-example:`, `## Related skills`), a "Use when" description, and
`axis:`/`rule_count_floor:` frontmatter.

Checks (executed live this session):

- `python3 scripts/check_skill_conformance.py` → `273 skills checked`,
  exit 0 (269 before + 4 new, matching the proposal's success
  criterion).
- `python3 -m pytest test/ -q` → `12 passed in 0.04s` (no SKIPPED
  lines in the output).

## Why

Operator directive 2026-08-23 / issue #93: tm-dicequest cuts 2–4 showed
character rendering/motion/reaction and growth-system coverage too thin
after wave 1; these four skills codify the missing decision rules so
later cuts stop improvising. Shape (four sibling single-axis skills,
not extensions of wave-1 hosts) per the approved proposal's rationale.

## Upstream

- Basis: docs/issue-93/proposals/game-skill-wave-2.md (approved via
  issue comment `APPROVE issue-93/knowledge-management` by JiwonJung94,
  listed in docs/specs/approvers.md; phase-1 PR #94 merged).
- Research basis: docs/issue-93/reports/knowledge-management/scout-brief.md
  and .../survey.md (merged in PR #94).

## Research sources (issue acceptance)

Animation/motion:
- https://www.sprite-ai.art/guides/animation-principles
- https://www.gamedeveloper.com/production/the-12-principles-of-animation-in-video-games
- https://www.pixel-editor.com/articles/sprite-animation-fundamentals
- https://web.dev/articles/animations-guide
- https://www.joshwcomeau.com/animation/sprites/
- https://blog.logrocket.com/making-css-animations-using-a-sprite-sheet/

Hit reaction/impact:
- https://www.ssbwiki.com/Hitlag
- https://sonichurricane.com/?p=1043
- https://shane-sicienski.com/blog/blog-post-title-one-55pmn
- https://supersmashbros.fandom.com/wiki/Invincibility_frame

Rendering composition:
- https://anim.works/silhouette-in-animation/
- https://nastyrodent.com/stylized-3d-characters-art-direction-principles/
- https://pixune.com/blog/shape-language-technique/
- https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent

Growth-system design:
- https://www.gamedeveloper.com/design/creating-a-casual-game-progression-curve
- https://gamedesignskills.com/game-design/game-progression/
- https://dev.to/sam_novak_574b07811e18495/idle-game-economy-design-what-your-currency-sinks-actually-eat-1non
- https://dev.to/hiroshi_takamura_c851fe71/game-economy-balancing-how-to-tune-rewards-costs-and-progression-2ale
- https://medium.com/googleplaydev/understanding-games-that-retain-1847b16c86a7

## Doc-placement ladder outcomes

- [x] Skill files under skills/<name>/SKILL.md (repo taxonomy home).
- [x] Delivery record at docs/issue-93/reports/knowledge-management.md
  (own record area only).
- [x] No changes to docs/specs/*, scripts/, manifests, or existing
  skills (out of scope per proposal).

## Skill verdicts

- skill-verdict: knowledge-management-structure-findability — applied: invoked; condition-led titles per rule block, one-axis-one-entry filing, load-bearing inline cross-links in `## Related skills` and rule bodies rather than restated content.
- skill-verdict: knowledge-management-taxonomy-tagging — applied: invoked; four new single-axis terms placed as siblings with associative cross-links (rule 6: association, not false hierarchy) to wave-1 hosts, distinct "Use when" scopes preventing trigger overlap.
- skill-verdict: knowledge-management-curation-pruning — not-applicable: no uncited or flagged existing entry in scope; this delivery only adds entries.
- skill-verdict: knowledge-management-supersession-lifecycle — not-applicable: nothing replaced or deprecated; wave-1 skills stay authoritative and are cross-linked, not superseded.
- skill-verdict: knowledge-management-pattern-extraction — not-applicable: no retrospective lesson to extract; content came from the phase-1 external research pass.

## What did not work

None.

## Open findings

None. Manifest enrollment of the four new skills
(procedure_authored_skills.txt / use-when-source manifest) stays out of
scope per the approved proposal, as in wave 1.
