---
Subject: issue-53
---

# Current-state survey + scout brief: slide-deck skill family

## Write surface

No slide-deck skill exists today. `skills/` has no `knowledge-work-*` or
`deck-*` prefix at all — this is a wholly new family, not an extension of
an existing one. The nearest neighbors are `technical-writing-*` (prose
document structure, not slide-shaped) and `brand-design-*` (visual system
rules, not deck-authoring rules). Neither covers text-source slide-deck
authoring, toolchain selection between Marp/reveal.js/Slidev/Quarto, or
mechanical deck-quality checks (lines/words per slide, heading structure,
image alt).

## Category must-bes (from the four tools compared)

- **Marp**: single Markdown file is the native source format; slides
  split on `---`. `marp-cli` renders headlessly to HTML/PDF/PPTX/PNG from
  that one file with no project scaffolding or build step; PDF/PPTX/PNG
  require a Chromium-family browser on the machine, HTML does not. Three
  built-in themes (default/gaia/uncover) plus custom-CSS themes.
  (https://github.com/marp-team/marp-cli, https://marp.app/)
- **reveal.js**: the deck itself is an HTML file referencing the
  reveal.js runtime — not single-file-portable the way Marp/Slidev
  Markdown is, since it depends on the library assets being present.
  No first-party CLI ships with reveal.js itself; headless PDF needs an
  external tool (Decktape) or a manually driven headless-Chromium
  print-to-PDF pass, and reveal.js's own built-in print stylesheet is
  documented as imperfect for complex layouts.
  (https://revealjs.com/pdf-export/,
  https://gist.github.com/jillesvangurp/56b66cbfd35c33d622948302f98538ed)
- **Slidev**: Markdown source (with embedded Vue components), but it is
  a project (npm-based), not a single portable file, once components or
  custom layouts are used. `slidev export` uses Playwright-Chromium
  under the hood for headless PDF/PNG/PPTX export — CI-runnable but
  requires a Node toolchain and browser install, heavier than Marp's
  single-binary-ish CLI. Theming via swappable theme packages or
  `slidev theme eject` to customize locally.
  (https://sli.dev/guide/exporting, https://sli.dev/guide/)
- **Quarto**: `.qmd` Markdown source compiled via `quarto render` to a
  reveal.js-based HTML deck (`format: revealjs`); this is a real build
  step (Quarto's own toolchain, not just Markdown-to-HTML), so it is the
  least "no-build" of the four. Headless PDF is not first-class for the
  revealjs format — the documented workarounds are Decktape or a
  headless-Chromium print pass, same gap as raw reveal.js, because
  Quarto's revealjs output *is* a reveal.js deck. 11 built-in themes plus
  custom `.scss` theme files declared in YAML frontmatter.
  (https://quarto.org/docs/presentations/revealjs/,
  https://quarto.org/docs/presentations/revealjs/themes.html,
  https://github.com/quarto-dev/quarto-cli/discussions/7018)

## Performance axes the tools compete on

1. **No-build portability vs. tooling weight**: Marp (single .md file,
   lightest) > Slidev (Markdown + npm project) > Quarto (Markdown +
   Quarto's compiler toolchain) ≈ reveal.js (hand-authored HTML +
   runtime assets, heaviest to hand-author, lightest to just view).
2. **Headless render maturity**: Marp and Slidev ship first-party CLI
   commands that go straight to PDF/HTML in one command
   (`marp-cli`, `slidev export`) and are the two tools where "CI-runnable
   headless render" needs no extra glue. reveal.js and Quarto's revealjs
   output both push PDF export to a second, external tool (Decktape or
   manual headless-Chromium print) — a materially worse CI story for
   PDF specifically, though both render fine to HTML headlessly (a
   static file, or `quarto render`, respectively).
3. **Mechanical checkability of source**: all four are plain-text-source
   at the authoring layer (Marp/Slidev/Quarto Markdown, reveal.js HTML),
   so all four support external mechanical checks (word/line counts per
   slide via a `---`/heading-delimited parse, heading-level scans, image
   alt-text presence via Markdown `![alt](...)` or HTML `<img alt="">`
   regex/AST scan) — none of the four tools themselves ship a built-in
   "max words per slide" linter; that layer is DIY regardless of tool
   choice. Marp's image syntax overloads alt text for CSS-filter/sizing
   directives (e.g. `![width:100px](img.png)`), which a naive alt-text
   checker must account for so it doesn't misclassify filter syntax as
   real alt text.
   (https://github.com/marp-team/marpit/blob/main/docs/image-syntax.md)

## Adopt / skip

- **Adopt**: source-anchored, tool-conditional toolchain selection —
  "no-build + first-party headless CLI to both HTML and PDF" (Marp) vs.
  "Vue-component-rich decks where npm tooling is already acceptable"
  (Slidev) vs. "deck is one output of a larger Quarto/R-Markdown
  document-generation pipeline" (Quarto) vs. "hand-rolled HTML deck with
  full runtime control, PDF export accepted as a secondary/external
  step" (reveal.js) — rather than naming one universal "best" tool.
- **Skip**: building or recommending a bespoke deck-checking script in
  this phase. The four tools converge on "no built-in mechanical
  checker" — that gap is real but is an *implementation* concern for
  phase 2's skill rules (which can point at a generic Markdown-AST/
  regex approach), not a research finding that changes which skills to
  propose.

## Segment fit

This is a new **authoring-practice family for knowledge-work text-source
deliverables**, sibling in spirit to `design-artifact-*` (produce the
artifact well) but for slide decks specifically, and adjacent to
`technical-writing-*` (which governs prose document types, not slide
density/toolchain decisions).

## Gap line

Current state (`skills/`) has zero coverage of slide-deck authoring:
no Use-when trigger anywhere in the repo covers "choose a deck tool,"
"structure a deck's narrative," or "check slide density/heading/alt-text
mechanically." This family fills all three: deck-toolchain-selection
(which tool for which authoring/rendering profile), deck-structure/
narrative-arc (how to sequence a deck's content), and slide-density-and-
layout (mechanical per-slide limits: lines/words/heading levels/alt
text).

## Unknowns / not scouted further

- Exact numeric thresholds for "max lines/words per slide" are not
  standardized by any of the four tools or a single canonical style
  guide; phase 2's density skill will need to pick defensible defaults
  (e.g. commonly cited presentation-design guidance) and cite that
  source explicitly rather than inventing a number.

## Sources

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
