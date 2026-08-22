---
status: proposed
files:
  - skills/knowledge-work-deck-structure-narrative-arc/SKILL.md
  - skills/knowledge-work-slide-density-and-layout/SKILL.md
  - skills/knowledge-work-deck-toolchain-selection/SKILL.md
---

# Slide-deck authoring skill family (issue #53)

## Request

Add a condition-matched skill family for text-source slide-deck
authoring and mechanical deck-quality checking, covering deck narrative
structure, per-slide density/layout limits, and toolchain selection
among Marp, reveal.js, Slidev, and Quarto — each source-anchored, each
with a Use-when trigger, `scripts/check_skill_conformance.py`-passing
shape, and research sources recorded in this PR body. This is the
research-first groundwork step for a knowledge-work deliverables
program; no `skills/` files land in this phase.

No scout-skip condition applies: this proposal follows a completed
current-state survey and research scout pass, recorded at
`docs/issue-53/reports/ux-engineering/survey.md` (this role's own
record area per contract v3 s11 — `docs/issue-53/reports/implementation/`
belongs to a different role and is not used here).

## Constraints

- Must follow the existing conformance shape used across the repo's
  skills: frontmatter `name`/`description` (with a "use when" trigger
  clause), body `## Trigger` / `## Procedure` / `## Output shape` /
  `## Decision rules`, each decision rule carrying a `source:` line with
  a live http(s) URL. `python3 scripts/check_skill_conformance.py` must
  stay green over the full repository, both now and after phase 2.
- ≥3 skills required by the issue's acceptance criterion, naming
  deck-structure/narrative-arc, slide-density-and-layout, and
  deck-toolchain-selection specifically — deliver all 3.
- The toolchain-selection skill's decision rules must name concrete
  tools (Marp, reveal.js, Slidev, Quarto) and the concrete conditions
  that select each one, not a generic "pick a good tool" rule.
- Scope for this and the following phase: `skills/`, `scripts/`, `docs/`
  only.
- Phase-1 only: this PR delivers survey + proposal; no `skills/` files
  land until a human Approve reopens phase 2.

## Rationale

Two structural questions needed a decision before writing rules, both
grounded in the tool comparison in
`docs/issue-53/reports/ux-engineering/survey.md`.

**One skill vs. three**: considered a single monolithic
"deck-authoring" skill covering structure, density, and tool choice
together, since all three questions arise when starting the same deck.
Rejected: the three questions have different triggers and different
failure modes at different times in the authoring lifecycle — tool
choice happens once, before any content exists (a Slidev-vs-Marp
decision driven by whether Vue components or a no-build pipeline
matters); narrative-arc structuring happens while drafting outline
content; density/layout checking happens per-slide, repeatedly, often
mechanically via script rather than human judgment. Collapsing them
would force one Use-when trigger to cover three different moments,
echoing the reason the `design-artifact-*` family (issue #50) kept
user-flow and user-scenario as separate skills rather than merging them
— one trigger covering distinct decision moments erases the
disambiguation the family exists to provide. A monolithic skill would
also make the mechanical-checkability rules (line/word/heading/alt
counts — checkable by a script) indistinguishable from the narrative
rules (sequencing/pacing — not mechanically checkable), when the issue
explicitly asks for "mechanical checkability" as a distinct axis.

**Toolchain-selection rule shape**: considered a rule that recommends
one tool universally (e.g. "always use Marp because it's lightest").
Rejected: the survey found the four tools trade off along at least two
independent axes — no-build portability (Marp lightest, Quarto/reveal.js
heaviest to hand-author) and headless-render maturity to PDF
specifically (Marp and Slidev have first-party CLI PDF export; reveal.js
and Quarto's revealjs output both push PDF to an external tool like
Decktape). A universal recommendation would be wrong for the Slidev
use case (decks needing live Vue components, where Marp's plain-Markdown
model can't express the requirement) and wrong for the Quarto use case
(a deck that is one output of a larger R-Markdown/Quarto
document-generation pipeline, where introducing a second tool just for
slides duplicates content-source management). The rule must instead be
conditional on the concrete authoring requirement (single-file/no-build,
component-rich, part of a larger Quarto pipeline, or full-control
hand-authored HTML), matching the tool-comparison axes the survey
actually found.

## What will be done

Phase 2 (after Approve) will author three `SKILL.md` files under
`skills/knowledge-work-<name>/`, each following the conformance shape
verified in the survey (frontmatter `name`/`description` with "use
when", body `## Trigger` / `## Procedure` / `## Output shape` /
`## Decision rules`, ≥3 rules each with a `source:` URL):

1. **knowledge-work-deck-toolchain-selection** — trigger: choosing which
   tool (Marp, reveal.js, Slidev, Quarto) to author a text-source slide
   deck with, before content exists. Rules anchored on the survey's
   axes: no-build/single-file need → Marp
   (https://github.com/marp-team/marp-cli); component-rich/interactive
   slides where an npm project is already acceptable → Slidev
   (https://sli.dev/guide/exporting); deck is one output of a larger
   Quarto/R-Markdown document pipeline → Quarto
   (https://quarto.org/docs/presentations/revealjs/); full hand-authored
   HTML/runtime control with PDF export accepted as a secondary step →
   reveal.js + Decktape
   (https://gist.github.com/jillesvangurp/56b66cbfd35c33d622948302f98538ed).
2. **knowledge-work-deck-structure-narrative-arc** — trigger: outlining
   or sequencing a deck's content before or while drafting slides.
   Rules anchored on established presentation-structure guidance (e.g.
   a documented narrative-arc/agenda-signpost-summary pattern, cited to
   a concrete source found during phase-2 scouting rather than invented
   in phase 1).
3. **knowledge-work-slide-density-and-layout** — trigger: checking or
   authoring an individual slide's content against per-slide density and
   accessibility limits (max lines/words, heading-level consistency,
   image alt text). Rules anchored on the survey's finding that all four
   tools are plain-text-source and therefore mechanically checkable via
   an external script (word/line count per `---`/heading-delimited
   slide, heading-level scan, `![alt](...)`/`<img alt="">` presence
   scan) — with the Marp-specific caveat that alt text can carry
   CSS-filter/sizing directives
   (https://github.com/marp-team/marpit/blob/main/docs/image-syntax.md)
   that a checker must not misclassify as real alt text.

Each skill gets ≥3 decision rules with `source:` lines, matching the
observed repo-wide convention. `python3 scripts/check_skill_conformance.py`
will be run and confirmed green before the phase-2 record is written.
Research sources will be restated in the phase-2 PR body per the
acceptance criterion.

## Out of scope

- Any actual `skills/knowledge-work-*` file — those are phase-2 output,
  gated on Approve.
- Changes to `scripts/check_skill_conformance.py` — the existing
  conformance shape already covers what this family needs; no gap was
  found during this survey that would require a script change.
- Any other skill family (e.g. document/report authoring beyond slide
  decks) — out of scope for issue #53.
- Building a deck-density-checking script itself — phase 2 authors the
  skill's *rules*, not a companion linter; if a companion script later
  proves necessary that is a separate, explicitly scoped follow-up.

## How you'll know it worked

- `skills/` contains 3 new `knowledge-work-*` directories, each with a
  conformant `SKILL.md` (Use-when trigger line, ≥3 source-anchored
  decision rules).
- `python3 scripts/check_skill_conformance.py` exits 0 over the full
  repository after phase 2.
- `knowledge-work-deck-toolchain-selection`'s decision rules name Marp,
  reveal.js, Slidev, and Quarto individually with the concrete condition
  that selects each, not a single universal recommendation.
- The phase-2 PR body records the research sources used (the URLs in
  this survey).
