# Current-state survey — issue #90 (game-development skill families)

Written BEFORE the scout sweep and before the proposal, per the
survey-first ordering directive. Role-scoped path (contract v3 s11/s19):
this role writes only under `docs/issue-90/reports/knowledge-management/`,
never `reports/implementation/`.

## Write surface actually expected to be touched

Phase 1 (this PR):
- `docs/issue-90/reports/knowledge-management/survey.md` (this file)
- `docs/issue-90/reports/knowledge-management/scout-brief.md`
- `docs/issue-90/proposals/game-development-skill-families.md`

Phase 2 (gated on approval, listed here so the survey covers the real
surface, not a placeholder):
- `skills/game-design-core-loop-and-progression/SKILL.md`
- `skills/game-feel-juice-and-feedback/SKILL.md`
- `skills/html5-game-rendering-loop/SKILL.md`
- `skills/game-ui-board-and-lane-layout/SKILL.md`
- `docs/issue-90/reports/knowledge-management.md` (delivery record)

## What the repository looks like today

- 265 skills under `skills/<name>/SKILL.md`; `python3
  scripts/check_skill_conformance.py` currently prints
  `265 skills checked` and exits 0. That is the documented conformance
  command the issue's acceptance criterion points at.
- Conformance schema, read from `scripts/check_skill_conformance.py`:
  - YAML frontmatter delimited by `---`, with `name:` equal to the
    directory name and a non-empty `description:` containing a trigger
    marker (`use when`, `use whenever`, `trigger`, ...).
  - `axis:` (or `axes:`) is REQUIRED whenever the skill declares
    `rule_count_floor:` — i.e. for every numbered-decision-rule skill.
  - `globs:` is opt-in; if present it must be a non-empty YAML list of
    patterns each containing `*` or `?`.
  - Every `### N. <title>` block under a `## Rules` section must contain
    at least one `source: <http(s) URL>` line. This is the always-on
    citation gate — the sourcing requirement in issue #90's acceptance
    is mechanically enforced here, not merely conventional.
  - Two additive opt-in manifests exist:
    `scripts/procedure_authored_skills.txt` (listed skills must carry
    `## Trigger`, `## Procedure`, `## Output shape` headings) and
    `scripts/issue_1996_use_when_source_manifest.txt`.
- Family naming convention: `<discipline>-<axis>` directory names, one
  axis per skill (e.g. `ux-engineering-layout-grouping`,
  `api-design-error-design`). Largest families: technical-* (16),
  release-* (10), product-* (10), ux-* (9). A 4-skill family is squarely
  within precedent.
- `tier:` is an optional frontmatter field in use on 26 skills
  (`sparse` 12 / `moderate` 8 / `rich` 6) signalling evidence density.
- Two-phase role-handoff contract v3 s19 governs delivery: proposal PR
  first, code only after an approvers.md Approve. `CORE_BUILD_NOW` is
  unset in this session, so phase 1 only.

## Adjacent skills found (overlap risk to design around)

- `ux-engineering-layout-grouping`, `ux-engineering-control-selection`,
  `ux-engineering-color-visibility`, `ux-engineering-surface-contrast`,
  `ux-engineering-navigation-depth` — form/enterprise-UI oriented
  (Gestalt grouping, control-per-field-type). None address a spatial
  game board, lane, pip/token legibility, or a merge gesture.
- `interaction-design-form-control-and-layout` — a batch playbook
  covering form controls, grouping, nav depth, contrast. Same
  form-shaped scope; no game surface.
- `accessibility-aria-and-contrast-rules` — contrast floors and ARIA
  naming; relevant as a chain target for board/lane legibility, not a
  substitute (a canvas board has no ARIA role to pick).
- `implementation-performance-data-structure-choice` — performance
  cliffs in data structures/algorithms; nothing about a frame budget,
  requestAnimationFrame, or state/render separation.
- `brand-design-icon-system-svg` — keyline-grid icon sizing; adjacent to
  pip/token legibility at small sizes but scoped to SVG icon systems.
- Nothing matching `game`, `render`, `loop`, `anim` exists. Confirmed by
  `ls skills | grep -iE 'game|render|loop|anim'`.

## Unknowns the scout sweep must aim at

1. Progression/economy math: is there citable literature giving a *rule*
   (not an overview) for monotonic power at a milestone, for
   deterministic-vs-random acquisition, and for currency source/sink
   balance? The dogfood defect (an awakening x3.0 reset landing below a
   compounded x1.5^6) is the concrete condition to cover.
2. Game feel / juice: which of the canonical sources (Swink's *Game
   Feel*, Jonasson & Purho's "Juice it or lose it", Nijman's "The art of
   screenshake") yield numeric or condition-shaped bands — tween
   durations, screen-shake restraint — rather than inspiration talks.
3. HTML5 loop: authoritative references for fixed-timestep vs
   variable-delta, interpolation vs snapping, and the
   rAF-must-not-mutate-logic-state separation (Gaffer "Fix Your
   Timestep", MDN rAF / animation guide, Isaac Sukin's loop).
4. Board/lane layout: whether there is sourced guidance for touch target
   minimums, drag-vs-tap merge gestures with fallback, and small-token
   legibility that is not just a restatement of the existing
   accessibility / ux-engineering skills.

## Skill verdicts (issue #2039 / #2062)

- skill-verdict: knowledge-management-structure-findability — applied:
  invoked; its Diataxis reference-shape and condition-led-title rules
  drove the one-axis-per-skill decision and the rejection of a single
  combined playbook in the proposal's Rationale.
- skill-verdict: knowledge-management-taxonomy-tagging — applied:
  invoked; rules 2/6 (place a new term via broader/narrower, record
  related-but-distinct concepts as associative rather than forcing a
  false hierarchy) are why the four skills form a new family with
  `## Related skills` cross-links instead of being folded into
  `ux-engineering-*` / `implementation-performance-*`.
- skill-verdict: knowledge-management-curation-pruning — not-applicable:
  no existing entry is uncited, flagged, or up for removal; this issue
  adds new coverage.
- skill-verdict: knowledge-management-supersession-lifecycle —
  not-applicable: nothing is being replaced, dropped, or deprecated.
- skill-verdict: knowledge-management-pattern-extraction —
  not-applicable: the input is an issue-specified gap list, not a
  retrospective surfacing a candidate lesson to promote.
- skill-verdict: product-discovery-opportunity-solution-tree —
  not-applicable: no `scoping -> scoping` self-loop here; the issue
  already fixes the opportunity and the four deliverables.
- skill-verdict: conformance-review-requirement-extraction —
  not-applicable: this session authors a proposal, it does not render
  review verdicts; the acceptance criteria were already discrete and
  needed no decomposition pass.

## Skip record

Not applicable — scouting is NOT skipped for this issue. Neither skip
condition holds: this is not a pure bugfix, and the spec leaves the
whole rule set open.
