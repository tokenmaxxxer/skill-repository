---
Subject: issue-53
code_under_review: pending
loop_state: phase-2-complete
type: feature
breaking: false
verdict: pass
---

# Phase-2 record: slide-deck skill family

## What was done

Authored three new skills under `skills/knowledge-work-*/`, per the
merged phase-1 proposal
(`docs/issue-53/proposals/slide-deck-skill-family.md`, PR #54):

- `knowledge-work-deck-toolchain-selection` — which of Marp, reveal.js,
  Slidev, or Quarto to author a deck with, before content exists; rules
  name each tool with its concrete selection condition (no-build →
  Marp, component-rich → Slidev, part of a Quarto/R-Markdown pipeline →
  Quarto, full hand-authored HTML with Decktape PDF export → reveal.js).
- `knowledge-work-deck-structure-narrative-arc` — deck outlining/
  sequencing: pyramid-vs-SCQA argument order, and agenda/transition/
  summary signposting, sourced from presentation-structure guidance
  found during this phase's own scouting (per the proposal's
  instruction to cite a concrete source rather than invent one in
  phase 1).
- `knowledge-work-slide-density-and-layout` — per-slide mechanical
  checks: line/word count per slide-delimited unit, heading-level
  consistency, image alt-text presence, with a Marp-specific rule
  excluding Marpit's CSS-filter/sizing bracket directives from counting
  as real alt text.

Each skill carries `name`/`description` (with a "Use when..." trigger),
`axis:`/`rule_count_floor:` frontmatter, and `## Trigger` / `## Procedure`
/ `## Output shape` / `## Decision rules` bodies with ≥3 source-anchored
rules (each including a `REMOVAL:`-tagged or counter-example-style
rule), matching the conformance shape of the existing
`ux-engineering-*`/`design-artifact-*` families.

`python3 scripts/check_skill_conformance.py` passes over the full
repository: 248 skills checked, 0 failures (245 pre-existing + 3 new).

## Why

Program knowledge-work-deliverables groundwork (issue #53):
skill-repository had no deck-authoring skills and no recorded toolchain
comparison for text-source slide-deck tools. This closes that gap per
the issue's frozen Acceptance, gated on the phase-1 proposal's Approve.

## Upstream

`docs/issue-53/proposals/slide-deck-skill-family.md` (merged via PR
#54), grounded in `docs/issue-53/reports/ux-engineering/survey.md`.

Approval note: the issue-53 comment intended as the single-account
Approve token
(`gh issue view 53 --json comments`, JiwonJung94) has a first line
reading exactly `APPROVE issue-53/ux-engineering` but continues with an
explanatory paragraph below it, so its full body is not byte-identical
to the bare token string — a near-miss under the strict
whole-body-equality test, recorded here per the near-miss disclosure
duty rather than silently treated as a clean match. Phase 2 proceeded
because the same human account also directly instructed this session,
in-turn, to execute phase 2 per the merged proposal.

## Research sources (restated per acceptance)

Carried over from the phase-1 proposal (toolchain-selection axis):

- https://github.com/marp-team/marp-cli
- https://marp.app/
- https://github.com/marp-team/marpit/blob/main/docs/image-syntax.md
- https://revealjs.com/pdf-export/
- https://revealjs.com/
- https://gist.github.com/jillesvangurp/56b66cbfd35c33d622948302f98538ed
- https://sli.dev/guide/exporting
- https://sli.dev/guide/
- https://sli.dev/builtin/cli
- https://quarto.org/docs/presentations/revealjs/
- https://quarto.org/docs/presentations/revealjs/themes.html
- https://github.com/quarto-dev/quarto-cli/discussions/7018

New in this phase (narrative-arc axis, fetched 2026-08-22):

- https://a1slides.com/mckinsey-presentation-framework/
- https://www.antonilacinai.com/news/signposts-in-speech/

## What did not work

None.

## Open findings

None — all three skills pass conformance and match the proposal's
per-skill trigger/scope split and toolchain rule's per-tool condition
requirement.

## kind

implementation
