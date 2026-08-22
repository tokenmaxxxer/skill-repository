---
Subject: issue-50
---

# Current-state survey: design-artifact skill family

## Write surface

`skills/` gains five new skill directories (one `SKILL.md` each):
`design-artifact-storyboard`, `design-artifact-information-architecture`,
`design-artifact-user-flow`, `design-artifact-user-scenario`,
`design-artifact-html-demo`. No existing skill file is edited.

## What exists today

`skills/ux-engineering-*` (6 skills: color-visibility, control-selection,
layout-grouping, navigation-depth, research-log, surface-contrast) cover
in-screen decisions — which control, which color, which grouping, which
nav depth. None of them cover authoring a design *artifact* (a document
or demo produced during the design process itself): no skill exists for
storyboards, IA documents, user-flow diagrams, user-scenario/journey
writing, or HTML/CSS demo construction. This confirms the issue's empty
state.

## Conformance shape (from `scripts/check_skill_conformance.py`)

- Frontmatter: `name` (== directory name), `description` containing a
  "use when"-style trigger clause.
- Body: `## Trigger`, `## Procedure`, `## Output shape` headings
  (enforced via `--manifest`), plus a `## Decision rules` section with
  numbered rules, each carrying a `source:` line with an `http(s)://`
  URL (enforced via `--require-use-when-and-source`).
- Observed convention (not mechanically enforced but consistent across
  all 6 existing `ux-engineering-*` skills): `axis:` and
  `rule_count_floor:` frontmatter fields; each decision rule also
  carries a `counter-example:` or `rationale:` line; one rule is often
  tagged `REMOVAL:` to counter additive bias. 240 skills currently pass
  conformance.

## Unknowns going into scouting

- What do practitioners (NN/g) actually say distinguishes a user
  *journey* from a user *flow*, and IA depth-vs-breadth — thin/contested
  areas the issue names directly (misconceptions like the "3-click
  rule").
- What does ISO 9241-210 actually specify about scenarios/personas/
  prototyping as HCD process outputs — the issue asks for this as an
  anchor source.
- HTML-demo construction: no NN/g-equivalent single canonical source;
  needs semantic-HTML/accessibility-baseline grounding (MDN) since the
  issue asks for "semantic structure, no-build single-file demo,
  responsive + accessible defaults."

## Skip condition

Does not apply — scouting ran (see
`docs/issue-50/reports/ux-engineering/scout-brief.md`).
