---
status: proposed
files:
  - docs/issue-90/reports/knowledge-management/survey.md
  - docs/issue-90/reports/knowledge-management/scout-brief.md
  - docs/issue-90/proposals/game-development-skill-families.md
  - skills/game-design-core-loop-and-progression/SKILL.md
  - skills/game-feel-juice-and-feedback/SKILL.md
  - skills/html5-game-rendering-loop/SKILL.md
  - skills/game-ui-board-and-lane-layout/SKILL.md
  - docs/issue-90/reports/knowledge-management.md
---

# Game-development skill families (phase 1: research + proposal)

Note on survey location (skip record for the generic survey path only —
scouting itself was NOT skipped): the current-state survey required by
the survey-before-proposal norm exists and lives at
`docs/issue-90/reports/knowledge-management/survey.md`, role-scoped per
contract v3 s11/s19, rather than the generic
`docs/issue-90/reports/implementation/survey.md` path, because this role
writes only its own record area and never another role's
`reports/implementation/` tree. No design decision is left open by that
path choice, and a second copy of the survey at the implementation path
would add nothing. Scouting ran in full; its output is
`docs/issue-90/reports/knowledge-management/scout-brief.md`.

## Request

Issue #90 (requirement R1): four skill-family gaps surfaced by the
tm-dicequest game dogfood have no coverage in this repository, and
sessions had to improvise at each of them. Author, research-first, four
new skills — core-loop/progression math, game-feel/juice, HTML5
rendering-loop discipline, and board/lane UI layout — each with sourced
grounding from established game-design and HTML5 game-loop literature,
condition-matched "Use when" triggers, and decision-point rules rather
than overviews, with `python3 scripts/check_skill_conformance.py` green
over the result. Two-phase: this document is phase 1.

## Constraints

- `scripts/check_skill_conformance.py` must exit 0 after phase 2. That
  means, per skill: frontmatter `name:` equal to the directory name, a
  `description:` carrying a trigger marker, `axis:` present alongside
  `rule_count_floor:`, and — the binding one — every `### N. <title>`
  block under `## Rules` carrying at least one `source: <URL>` line.
- Every rule traces to a source listed in the scout brief; a claim with
  no live URL is dropped or labelled an assumption, never asserted.
- No content overlap with `accessibility-aria-and-contrast-rules`,
  `ux-engineering-*`, `interaction-design-form-control-and-layout`, or
  `implementation-performance-data-structure-choice`; where a rule
  genuinely chains to one of those, it is recorded as an associative
  `## Related skills` link, not a re-statement.
- Skills stay portable: no tm-dicequest paths, no repo-specific secrets
  or assumptions (README design principle).
- Phase 2 only after an approvers.md Approve; the delivery record
  `docs/issue-90/reports/knowledge-management.md` is phase-2 output.

## Rationale

The chosen shape is **four sibling skills, one axis each, directory
names exactly as the issue names them**, each following the repo's
dominant condition -> choice -> why -> source -> counter-example rule
format at `tier: sparse`.

Alternatives considered and rejected:

- **One combined `game-development-playbook` skill** covering all four
  areas, in the style of the existing
  `interaction-design-form-control-and-layout` batch playbook. Rejected:
  the four axes have disjoint triggers (balancing a curve, polishing
  feedback, writing a frame loop, laying out a board) and a single
  `description:` would have to be broad enough to fire on all of them,
  which is exactly the retrieval failure the repo's one-axis-per-skill
  convention avoids (Diataxis reference-shape: one entry answers one
  query). The issue also names four skills explicitly.
- **Folding the loop skill into `implementation-performance-*` and the
  board skill into `ux-engineering-*`** rather than starting a new
  family. Plausible given both families exist and are healthy — the
  survey confirms they are the nearest neighbours. Rejected because the
  host families' scopes would have to widen to admit them: the
  ux-engineering family is form/enterprise-UI scoped (Gestalt field
  grouping, control-per-field-type) with no spatial-play surface, and
  `implementation-performance-data-structure-choice` is about asymptotic
  cliffs, not frame budgets. Widening a family's scope to host an
  unrelated axis is the false-hierarchy failure; the correct encoding is
  a separate term plus an associative cross-link.
- **Seven-to-eight finer-grained skills** (splitting economy from
  progression, splitting tween timing from screen-shake restraint).
  Rejected: the evidence base found in the sweep does not support that
  many independently-triggered condition sets — several would land at
  one or two rules, below the family's useful floor, and would split a
  single authoring moment across two lookups.

## What will be done

Phase 1 (this PR): the survey, the scout brief, and this proposal. Stop.

Phase 2 (after Approve), four `SKILL.md` files:

1. **`game-design-core-loop-and-progression`** — axis
   `core-loop-and-progression`, floor 5. Rules: a progression milestone
   must never reduce effective power (the dogfood's x3.0-reset-below-
   x1.5^6 defect, stated as a monotonicity check against the compounded
   value at the threshold); pick the cost-curve direction from where the
   design wants attention (increasing curve -> early game, decreasing ->
   late game); every currency needs a named sink sized against its
   sources before the source ships; choose deterministic acquisition
   when the item gates progression and random acquisition only for
   non-gating content; state each curve as an explicit function before
   tuning constants. Sources: Schreiber "Game Balance Concepts" Level 3
   (cost curves), Unity balanced-economy guide (sources/sinks, soft
   caps, diminishing returns).
2. **`game-feel-juice-and-feedback`** — axis `juice-and-feedback`,
   floor 4. Rules: stage the build layout -> animation -> juice and do
   not ship at stage 1 (the operator-rejected "text + buttons" case);
   every player action gets readable feedback within the same frame the
   input is accepted; add juice as layered, individually-removable
   effects over a working prototype, never as a rewrite; apply
   screen-shake only to events the design wants read as impactful, and
   cap it so ordinary repeated actions do not shake. Sources: Jonasson &
   Purho "Juice it or lose it", Nijman "The art of screenshake", Swink
   *Game Feel* (real-time control / polish decomposition), Disney
   squash-and-stretch lineage.
3. **`html5-game-rendering-loop`** — axis `rendering-loop`, floor 5.
   Rules: drive rendering from one `requestAnimationFrame` loop, never
   from per-event ad hoc draws once anything animates; advance logic on
   a fixed timestep via an accumulator and render at the variable rate;
   the render path must not mutate logic state (animate the
   representation, not the model); interpolate between previous and
   current state with the accumulator remainder when render rate exceeds
   tick rate, and snap only when the state is discrete/non-interpolable;
   keep short-lived effects on a separate effect layer/canvas that can
   be cleared without redrawing the board. Sources: Fiedler "Fix Your
   Timestep!", MDN "Anatomy of a video game", MDN
   `Window.requestAnimationFrame`.
4. **`game-ui-board-and-lane-layout`** — axis `board-and-lane-layout`,
   floor 4. Rules: any drag/merge gesture ships with a single-pointer
   (tap-tap) alternative (WCAG 2.2 SC 2.5.7); interactive board cells
   and tokens meet the 24x24 CSS-px target floor, and 44-48px on
   touch-primary surfaces; a pip/token count above the threshold where
   pips stop being countable at the shipped size switches to a numeral;
   lanes and the HUD are separated by an explicit spatial boundary so
   board state is never read as chrome. Sources: WCAG 2.2 Understanding
   2.5.7 / 2.5.8, NN/g touch-target-size, Apple HIG / Material touch
   minimums.

Each file also carries `## Trigger`, `## Procedure`, `## Output shape`
(so the skills can later join `procedure_authored_skills.txt` without
rework) and a `## Related skills` section cross-linking
`accessibility-aria-and-contrast-rules`,
`ux-engineering-color-visibility`, and
`implementation-performance-data-structure-choice` at the point each
link is load-bearing.

## Out of scope

- Any change to existing skills, to `scripts/`, or to the conformance
  checker itself.
- Adding the new skills to `procedure_authored_skills.txt` or the
  use-when manifest (a separate manifest decision; the bodies will be
  written to satisfy it either way).
- Game engine, audio, netcode, monetization, or level-design skills —
  not among the four gaps the dogfood surfaced.
- Any change to tm-dicequest itself; this repository ships skills only.

## How you'll know it worked

- `python3 scripts/check_skill_conformance.py` prints `269 skills
  checked` and exits 0 (265 today + 4).
- `python3 -m pytest test/ -q` stays green.
- Each new `SKILL.md` frontmatter `name:` matches its directory; each
  `description:` contains a distinct "Use when" trigger naming its own
  conditions.
- Every numbered rule block contains a `source:` URL, and every URL is
  one verified live during phase 2.
- The delivery record `docs/issue-90/reports/knowledge-management.md`
  lists the research sources (issue acceptance).
