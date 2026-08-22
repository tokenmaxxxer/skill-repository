---
name: knowledge-work-deck-toolchain-selection
description: Use when choosing which tool (Marp, reveal.js, Slidev, or Quarto) to author a text-source slide deck with, before any slide content exists. Applies to the deck-toolchain-selection axis.
axis: deck-toolchain-selection
rule_count_floor: 3
---

# Deck toolchain selection

Decision rules for picking a text-source slide-deck tool, sourced from
each tool's own CLI/export documentation fetched during issue #53's
ux-engineering research pass (2026-08-22).

## Trigger

Apply this skill when deciding which tool to author a new text-source
slide deck with, before any slide content exists — a one-time choice at
the start of a deck's lifecycle. Distinguish it from
deck-structure-narrative-arc (how to sequence content once a tool is
chosen) and slide-density-and-layout (per-slide checks once content
exists).

## Procedure

1. Identify the authoring constraint that actually matters for this
   deck: no-build/single-file portability, live component/interactivity
   needs, membership in a larger document-generation pipeline, or full
   hand-authored HTML control (rule 1-4).
2. Cross-check the constraint against each tool's headless-render
   maturity to the delivery format actually needed (HTML for live
   presenting, PDF for distribution) before finalizing (rule 5).
3. Do not pick a tool by general reputation or default habit; require
   the concrete condition below to be true before selecting it.

## Output shape

A single tool selection (Marp, reveal.js, Slidev, or Quarto) plus the
one concrete authoring requirement that drove the pick, stated so the
choice can be re-derived later if the requirement changes.

## Decision rules

1. When the deck must be authored as a single Markdown file with no
   npm project, no build step, and CLI render straight to HTML/PDF,
   choose Marp.
   source: Marp CLI README (fetched 2026-08-22,
   https://github.com/marp-team/marp-cli): Marp CLI converts Markdown
   into HTML/PDF/PPTX slide decks directly from the command line, with
   no project scaffolding required.

2. When the deck needs live interactive or component-rich slides (e.g.
   embedded Vue components, client-side state) and an npm project is
   already an acceptable authoring cost, choose Slidev.
   source: Slidev CLI export guide (fetched 2026-08-22,
   https://sli.dev/guide/exporting and https://sli.dev/builtin/cli):
   Slidev decks are Vue-component-capable Markdown presentations with a
   first-party CLI (`slidev export`) for headless PDF/PNG export.

3. When the deck is one output artifact of a larger Quarto or
   R-Markdown document-generation pipeline (the same source also
   produces a paper, report, or website), choose Quarto's revealjs
   format rather than introducing a second, separate slide tool.
   source: Quarto reveal.js presentations guide (fetched 2026-08-22,
   https://quarto.org/docs/presentations/revealjs/): Quarto renders the
   same `.qmd` source to reveal.js-based HTML presentations alongside
   its other document output formats from one pipeline.

4. When the deck requires full hand-authored HTML/CSS/JS control over
   the runtime (custom transitions, plugins, or embedded web content
   beyond what a Markdown-to-slide converter exposes) and PDF export is
   an acceptable secondary step through an external tool, choose
   reveal.js directly, paired with Decktape for headless PDF export.
   source: reveal.js PDF export docs (fetched 2026-08-22,
   https://revealjs.com/pdf-export/) and a documented Decktape headless
   workflow (fetched 2026-08-22,
   https://gist.github.com/jillesvangurp/56b66cbfd35c33d622948302f98538ed):
   reveal.js itself ships no first-party PDF CLI — its own docs point to
   print-stylesheet or Decktape-driven export as the headless path,
   unlike Marp/Slidev's built-in CLI export.

5. Do not select a tool before checking whether its headless-render path
   reaches the format the deck actually needs to ship (HTML-only
   presenting vs. PDF distribution) — a tool with first-party PDF CLI
   export (Marp, Slidev) is a poor fit to swap in later if a
   reveal.js/Quarto choice was made for its content-pipeline fit and PDF
   turns out to be required day-of, since the PDF step then depends on
   an external renderer (Decktape) that must be separately installed and
   run.
   source: reveal.js PDF export docs (fetched 2026-08-22,
   https://revealjs.com/pdf-export/): reveal.js documents PDF export as
   a print-CSS-driven browser-print step or an external headless-Chrome
   tool, not a bundled CLI command, in contrast to Marp CLI's and
   Slidev's one-command PDF export.
