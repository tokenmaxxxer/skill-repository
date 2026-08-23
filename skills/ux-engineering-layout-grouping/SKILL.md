---
name: ux-engineering-layout-grouping
description: >-
  Use when arranging related fields into groups, choosing single- vs. multi-column layout,
  placing labels, or adding a visible group boundary. Applies to the layout-grouping axis.
  Trigger on requests like "single vs multi column form", "label placement", "fieldset
  grouping", "폼 레이아웃 그룹핑해줘". Do NOT use for deciding which widget fits a field in the first
  place (use ux-engineering-control-selection).
metadata:
  axis: layout-grouping
  rule_count_floor: 3
---

# Layout and grouping

Decision rules for proximity grouping, column layout, and label
placement, sourced from Gestalt grouping literature and form-layout
practitioner research actually fetched during issue #1174's
ux-engineering research pass (2026-08-13).

## Trigger

Apply this skill when arranging related fields into groups, choosing
single- vs. multi-column layout, placing labels, or adding a visible
group boundary — distinguishing it from control-selection (which
widget per field) and surface-contrast (elevation around an active
edit surface, not grouping within a static layout).

## Procedure

1. For semantically related fields, use tighter spacing between them
   than to the next unrelated group, letting proximity alone signal
   the grouping (rule 1).
2. For a form with more than roughly 6-8 fields, split into labeled
   sub-groups of 3-5 related fields (rule 2).
3. For a form whose fields form one linear sequence, use a
   single-column layout by default (rule 3).
4. For a short or expert-repeated form, place labels to the left of
   inputs; for a longer or first-time-user form, place labels above
   inputs (rule 4).
5. When whitespace alone is insufficient to show a group boundary, use
   a subtle border or background-tint container rather than a hard
   divider line (rule 5).
6. REMOVAL: when a group already carries a divider, a background
   tint, AND a bordered card, cut down to one grouping signal (rule
   6).
7. Prove a grouped layout's empty, loading, error, and populated
   states correct in isolation before assembling the full screen
   (rule 7).
8. Before specifying a new component for a grouped layout's slot,
   check the live component library for an existing match rather than
   relying on a stale mental snapshot (rule 8).

## Output shape

A layout spec: which fields group together, spacing/boundary
treatment per group, column count, and label placement — plus, where
rule 6 or 7 fires, a flagged over-boundaried group or an untested
non-populated state.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When two or more fields are semantically related (e.g. city/state/ zip, or start-date/end-date), place them with less vertical/ horizontal whitespace between them than t…
- 1.2 — When a form has more than roughly 6-8 fields, split them into labeled sub-groups of 3-5 related fields each rather than presenting one long undifferentiated list — chunk…
- 1.3 — When a form's fields form one linear sequence with no independent sub-tasks, use a single-column layout, not a multi-column layout — default to single-column unless ther…
- 1.4 — When a form is short (roughly under 5 fields) or used repeatedly by an expert user who already knows the field order, place labels to the left of inputs to compress vert…
- 1.5 — When grouped fields need a visible boundary because whitespace alone is not enough (e.g. dense enterprise UI with limited margin budget), use a subtle border or backgrou…
- 1.6 — REMOVAL: when a form's fields are already grouped by whitespace and a group also carries a redundant divider line, a background tint, AND a bordered card around it, cut…
- 1.7 — Prove a grouped layout's individual states — empty, loading, error, and populated — correct in isolation before assembling the group into a full screen; do not sign off…
- 1.8 — Before specifying a new component to fill a grouped layout's slot, check whether an existing component in the live library already covers the need, against the actual cu…
