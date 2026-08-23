---
name: ux-engineering-control-selection
description: >-
  Use when picking which UI control fits a given field's type, option count, or interaction
  contract. Applies to the control-selection-by-field-type axis. Trigger on requests like
  "radio group vs dropdown", "which control for this field", "date picker or text input", "어떤
  컨트롤 쓸지 정해줘". Do NOT use for arranging already-chosen controls into columns or groups (use
  ux-engineering-layout-grouping).
metadata:
  axis: control-selection-by-field-type
  rule_count_floor: 3
---

# Control selection by field type

Decision rules for which UI control fits which field type, sourced from
practitioner canon and platform component-selection guidance actually
fetched during issue #1174's ux-engineering research pass (2026-08-13).

## Trigger

Apply this skill when picking which UI control fits a given field's
type, option count, or interaction contract — distinguishing it from
color-visibility (contrast/color) and layout-grouping (spatial
arrangement of already-chosen controls).

## Procedure

1. For a true binary choice with an immediate, visible effect, pick a
   toggle switch over a checkbox (rule 1).
2. For 3-7 mutually-exclusive options with room to show them all, pick
   a radio group over a dropdown (rule 2).
3. For mutually-exclusive options under space constraints or at the
   upper edge of that range, pick a dropdown/select over a radio group
   (rule 3).
4. For 8 or more option values, pick a searchable select/combobox over
   a plain dropdown or radio group (rule 4).
5. For a calendar-date field, pick a date picker for visual browse/
   confirm needs, or permit a validated free-text date field when
   users already know the exact date (rule 5).
6. For free text, pick a single-line input for short content and a
   sized text view/textarea for long or multi-paragraph content
   (rule 6).
7. REMOVAL: when a control choice adds a confirmation step duplicating
   information an adjacent control already shows, cut the redundant
   control (rule 7).
8. For an interactive pattern with an established role-and-keyboard
   contract, pick the control that matches that contract rather than a
   visual look-alike that skips it (rule 8).
9. Name accessibility as a co-equal constraint at spec time, not a
   pass deferred until after visual/interaction design is settled
   (rule 9).

## Output shape

A named control choice per field (toggle, checkbox, radio group,
dropdown, combobox, date picker, free-text date, text input, or text
view), with the triggering rule number and, where rule 7 or 9 fires, a
flagged redundant control or a named accessibility constraint to
record at spec time.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When a field is a true binary choice with an immediate, visible effect (e.g. a setting that applies instantly, no separate "save" step), pick a toggle switch rather than…
- 1.2 — When 3-7 options are mutually exclusive and screen space allows all options to be shown at once, pick a radio button group over a dropdown/select — radio groups keep eve…
- 1.3 — When options are mutually exclusive but space is constrained (dense table row, narrow sidebar) or the option count is at the upper edge of the 3-7 range, choose a dropdo…
- 1.4 — When an option set has 8 or more values, pick a searchable select/combobox over a plain dropdown or radio group — remove the need to scroll a long closed list by adding…
- 1.5 — When a field is a specific calendar date and users need to browse or confirm a date visually, pick a date picker; when users routinely know and can type the exact date f…
- 1.6 — When free text is short (a name, email, single line of an address), pick a single-line text input; when the expected content is long, multi-paragraph, or needs visible l…
- 1.7 — REMOVAL: when a form field's control choice adds an extra confirmation step that duplicates information already implied by an adjacent control (e.g. a "confirm date" dro…
- 1.8 — For an interactive pattern with an established role-and-keyboard- interaction contract (a dialog's focus trap and Escape-to-close, a combobox's arrow-key/typeahead behav…
- 1.9 — Name accessibility as a co-equal technical constraint alongside framework and performance at spec time, not as a separate pass deferred to after the visual/interaction d…
