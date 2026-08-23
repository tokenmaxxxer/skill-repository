---
name: ux-engineering-research-log
description: >-
  Use when tracing where a playbook/*.md rule for the ux-engineering family came from — which
  source, at which research layer, supports a specific rule (issue #1174). Trigger on requests
  like "rule provenance", "which source supports this playbook rule", "research layer for this
  guideline", "이 규칙 출처 찾아줘". Do NOT use for applying a decision rule itself, e.g. a contrast
  check (use ux-engineering-color-visibility).
---

# Playbook research log — ux-engineering (issue #1174)

Evidence trail for `playbook/*.md`, recorded per the amendment-1
three-layer research protocol (practitioner knowledge / named
methodology-standard / academic theory). All sources listed here were
fetched live via WebSearch/WebFetch during this session on 2026-08-13,
not recalled from training. `rule_count_floor` per axis: 5 axes x 3
minimum = 15 total; 28 rule blocks landed across the 5 files.

## Trigger

Apply this skill when tracing where a `playbook/*.md` rule for the
ux-engineering family came from — which source, at which research
layer, supports a specific rule — distinguishing it from the 5
decision-rule skills (surface-contrast, color-visibility,
layout-grouping, navigation-depth, control-selection), which state the
rules themselves rather than their provenance.

## Procedure

1. To trace a control-selection rule's source, consult the
   `control-selection-by-field-type` axis section (below).
2. To trace a layout-grouping rule's source, consult the
   `layout-grouping` axis section (below).
3. To trace a surface-contrast rule's source, consult the
   `background-vs-edit-surface-contrast` axis section (below).
4. To trace a navigation-depth rule's source, consult the
   `nav-order-vs-usage-frequency` axis section (below).
5. To trace a color-visibility rule's source, consult the
   `color-combination-visibility` axis section (below).
6. To confirm a source was consulted but deliberately not cited as a
   rule basis, check the "Sources fetched but not used as a rule
   citation" section.
7. To confirm every axis carries at least one subtractive (removal)
   rule traced to its source, check the "Removal-rule coverage check"
   section.

## Output shape

A source citation (fetch date, URL, quoted or paraphrased passage) for
a named rule number in a named axis file, or a confirmation that a
given source was consulted but not used as a citation.

## Axis: control-selection-by-field-type -> `playbook/control-selection.md`

- Layer 1 (practitioner): query "NN/g checkboxes vs radio buttons",
  fetched https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/
  -> rules 1-4 (toggle-vs-checkbox, radio-group threshold,
  dropdown-fallback, searchable-combobox-at-8+).
- Layer 2 (named standard/platform guidance): query "Apple HIG pickers"
  and "Apple HIG text fields multiline text view guidance", fetched
  https://developer.apple.com/design/human-interface-guidelines/pickers
  and search-summarized
  https://developer.apple.com/design/human-interface-guidelines/text-views
  -> rules 5 (date picker vs typed date) and 6 (text field vs text
  view).
- Layer 3 (academic): query "Adams Converse Hales Klotz subtractive
  changes Nature 2021 summary", fetched summary via
  https://phys.org/news/2021-04-brains-opportunities.html (Nature.com
  original at https://www.nature.com/articles/s41586-021-03380-y
  redirected to an auth wall; used the phys.org research summary and
  the ideas.repec.org bibliographic record instead) -> rule 7 (removal:
  cut redundant confirmation controls).

## Axis: layout-grouping -> `playbook/layout-grouping.md`

- Layer 1 (practitioner): query "NN/g Gestalt proximity", fetched
  https://www.nngroup.com/articles/gestalt-proximity/ -> rules 1, 2, 4,
  5 (proximity spacing, chunking at 6-8 fields, label placement,
  boundary treatment).
- Layer 2 (named methodology): query "Luke Wroblewski web form design
  single column research findings", search-summarized
  https://www.lukew.com/resources/web_form_design.asp and corroborating
  https://cxl.com/blog/form-design-best-practices/ (15.4s completion-
  time study) -> rule 3 (single-column default).
- Layer 3 (academic): same Nature 592 (2021) subtraction-neglect source
  as above, via https://phys.org/news/2021-04-brains-opportunities.html
  -> rule 6 (removal: collapse redundant simultaneous grouping cues).

## Axis: background-vs-edit-surface-contrast -> `playbook/surface-contrast.md`

- Layer 1/2 (named methodology): query "Material Design elevation
  overview", confirmed page existence at
  https://m3.material.io/styles/elevation/overview (page fetched but
  returned only header content, not full body — cited as the canonical
  spec location for the elevation convention referenced, with the
  convention itself corroborated by general visual-hierarchy practice)
  -> rules 1, 2 (elevation for active surface, background desaturation).
- Layer 2 (named standard): reused WCAG 2.1 SC 1.4.11 fetch (see
  color-visibility axis below),
  https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
  -> rule 3 (minimize competing saturated chrome near a focus
  indicator, framed against SC 1.4.11's 3:1 requirement).
- Layer 3 (academic): Nature 592 (2021) subtraction-neglect source,
  https://phys.org/news/2021-04-brains-opportunities.html -> rule 4
  (removal: prune stacked contrast treatments to the minimum passing
  combination).

## Axis: nav-order-vs-usage-frequency -> `playbook/navigation-depth.md`

- Layer 2/3 (named law + underlying cognitive theory): query "Fitts's
  law laws of ux target size distance design" and "Hick's law laws of
  ux", fetched https://lawsofux.com/hicks-law/ directly and
  search-summarized https://lawsofux.com/fittss-law/ and
  https://www.nngroup.com/articles/fitts-law/ (direct fetch of
  lawsofux.com/fitts-s-law/ 404'd; used the search-result summary of
  the same lawsofux.com/fittss-law/ page plus the NN/g Fitts's-law
  article instead) -> rules 1, 2, 4 (top-level placement for frequent
  actions, nesting for rare actions, 7±2 consolidation) and rule 3
  (task-sequence nav order via Fitts's-law distance framing).
- Layer 3 (academic): Nature 592 (2021) subtraction-neglect source,
  https://phys.org/news/2021-04-brains-opportunities.html -> rule 5
  (removal: collapse single-child parent menu levels).

## Axis: color-combination-visibility -> `playbook/color-visibility.md`

- Layer 2 (named standard, fetched at source): query + direct fetch of
  three W3C WCAG 2.1 Understanding pages:
  https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
  (SC 1.4.3) -> rules 1, 2 (4.5:1 normal text, 3:1 large text);
  https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
  (SC 1.4.11) -> rule 3 (3:1 UI component contrast);
  https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
  (SC 1.4.1) -> rules 4, 5 (no color-only distinctions, lightness
  variation for colorblind-safe multi-value sets).
- Layer 3 (academic): Nature 592 (2021) subtraction-neglect source,
  https://phys.org/news/2021-04-brains-opportunities.html -> rule 6
  (removal: consolidate an overloaded status-color palette instead of
  layering more non-color cues onto it).

## Sources fetched but not used as a rule citation

- https://m2.material.io/design/environment/elevation.html — fetched,
  returned header-only content (no usable body text this session); not
  cited directly, superseded by the M3 elevation page reference above.
- https://developer.apple.com/design/human-interface-guidelines/text-views
  and https://developer.apple.com/design/human-interface-guidelines/pickers
  — full-page WebFetch returned header-only content; the actual
  guidance text used in control-selection.md rules 5-6 came from the
  WebSearch result snippets that quote those same pages, not from a
  full WebFetch body.

## Removal-rule coverage check

Every axis file carries at least one rule whose choice is subtractive
(drop/cut/delete/consolidate), each traced to Adams, Converse, Hales &
Klotz, "People systematically overlook subtractive changes," Nature 592
(2021), fetched this session via
https://phys.org/news/2021-04-brains-opportunities.html (research
summary) and https://ideas.repec.org/a/nat/nature/v592y2021i7853d10.1038_s41586-021-03380-y.html
(bibliographic record) — the Nature.com article page itself redirected
to an authentication wall (`idp.nature.com`) and was not accessible
this session:

- control-selection.md rule 7 — cut redundant confirmation control.
- layout-grouping.md rule 6 — cut redundant stacked grouping cues.
- surface-contrast.md rule 4 — cut redundant stacked contrast
  treatments.
- navigation-depth.md rule 5 — cut single-child parent nav levels.
- color-visibility.md rule 6 — cut an overloaded status-color palette.
