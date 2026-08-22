---
name: knowledge-work-slide-density-and-layout
description: Use when checking or authoring an individual slide's content against per-slide density and accessibility limits — max lines/words, heading-level consistency, or image alt text. Applies to the slide-density-and-layout axis.
axis: slide-density-and-layout
rule_count_floor: 3
---

# Slide density and layout

Decision rules for per-slide content limits on text-source decks
(Marp, reveal.js, Slidev, Quarto), sourced from each tool's own
Markdown-source documentation fetched during issue #53's ux-engineering
research pass (2026-08-22).

## Trigger

Apply this skill when checking or authoring an individual slide's
content against density and accessibility limits — line/word count,
heading-level consistency, or image alt text — either while drafting
or when running a mechanical checker over an existing deck.
Distinguish it from deck-structure-narrative-arc (cross-slide sequencing)
and deck-toolchain-selection (which tool to author with).

## Procedure

1. Split the deck source into per-slide units at its slide-delimiter
   (`---` for Marp/reveal.js/Quarto-revealjs, frontmatter-delimited
   sections for Slidev) before counting anything (rule 1).
2. Count lines and words per slide unit and flag any unit over the
   deck's declared limit (rule 2).
3. Scan each slide unit's heading levels for a single consistent level
   used for slide titles, not a mix of heading depths (rule 3).
4. Scan for image syntax and confirm each has real alt text, not an
   empty or decorative-only placeholder (rule 4).
5. On Marp sources specifically, do not misclassify a bracket directive
   as alt text (rule 5).

## Output shape

A per-slide pass/fail list against the density/heading/alt-text checks,
each failure naming the slide index and the specific limit or check it
failed — suitable output for an external mechanical checker script, not
just human review.

## Decision rules

1. Split a deck's Markdown source into per-slide units at its
   slide-delimiter convention before running any per-slide count — a
   flat word/line count over the whole file conflates every slide into
   one number and can't localize a density failure to a slide.
   source: Marp Markdown spec (fetched 2026-08-22, https://marp.app/):
   Marp slides are delimited by `---` horizontal-rule lines in the
   Markdown source, the same per-slide unit boundary a checker must
   split on.

2. Cap each slide unit at a fixed max line count and max word count
   (choose the limit per deck audience; e.g. a talk-support deck should
   run tighter than a leave-behind reading deck) and flag any slide unit
   exceeding either limit — do not average across the deck, since a
   deck can have a low average while individual slides overflow.
   rationale: the four surveyed tools (Marp, reveal.js, Slidev, Quarto)
   are all plain-text Markdown sources with a fixed per-slide delimiter,
   so a line/word count is mechanically computable per slide unit
   without rendering the deck — this is the "mechanical checkability"
   axis the issue asked for, distinct from narrative-sequencing rules
   that aren't script-checkable.

3. Require slide titles to use one consistent heading level across the
   deck (e.g. always `#` or always `##` for a slide title), and flag any
   slide whose title heading level differs from the deck's established
   level.
   source: Quarto reveal.js presentations guide (fetched 2026-08-22,
   https://quarto.org/docs/presentations/revealjs/): Quarto's
   revealjs format maps heading levels to slide/section nesting, so an
   inconsistent heading level on a slide title changes that slide's
   structural nesting rather than only its visual size.

4. Require every image reference (`![alt](...)` or `<img alt="">`) on a
   slide to carry non-empty, non-decorative alt text describing the
   image's content, and flag any image with missing or empty alt text.
   rationale: image alt text is the same accessibility requirement
   ux-engineering-color-visibility's non-color-signal rules apply to
   other visual content — a slide-deck checker should not treat images
   as exempt from it just because the deck source is plain Markdown.

5. On Marp sources specifically, when scanning alt-text syntax, exclude
   bracket content that is a Marpit CSS-filter/sizing directive (e.g.
   `![w:200](img.png)`, `![blur](img.png)`) from counting as real
   descriptive alt text — treat a slide whose only bracket content is a
   directive as still missing alt text, not as passing.
   source: Marpit image syntax spec (fetched 2026-08-22,
   https://github.com/marp-team/marpit/blob/main/docs/image-syntax.md):
   Marpit overloads the Markdown image alt-text bracket to also carry
   keyword directives (resizing, filters, background-image markers),
   so a naive "bracket is non-empty" check will misclassify a directive
   as descriptive alt text.

## Related skills

- [knowledge-work-deck-structure-narrative-arc](../knowledge-work-deck-structure-narrative-arc/SKILL.md) — slide density decisions assume a narrative arc already fixed the deck's structure.
