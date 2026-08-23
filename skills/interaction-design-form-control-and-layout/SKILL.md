---
name: interaction-design-form-control-and-layout
description: >-
  Use when you are choosing a form control for a single-select field, deciding how to lay out
  or group related fields, sizing navigation depth vs. breadth, checking a text or non-text
  contrast floor, deciding whether an existing modal should be removed, or naming a semantic
  token for a spacing/color/type value, and need a condition-matched rule rather than general
  interaction-design advice. Trigger on requests like "radio vs dropdown for this field",
  "should this stay a modal", "semantic token naming", "폼 컨트롤이랑 레이아웃 정해줘". Do NOT use for the
  ux-engineering family's narrower single-axis control question (use
  ux-engineering-control-selection).
---

# Playbook: form controls, grouping, navigation, contrast (issue-1174 batch 1)

Each `## R<n>` heading below is one condition -> choice -> source
decision rule. REMOVAL rules mark a pattern to actively strip when
found, not merely avoid adding.

## Trigger

Use this skill when a concrete change or evaluation touches one of:
- a single-select field's control type is being chosen or reconsidered
  (radio group vs. dropdown/listbox) — not a general "is this form
  usable?" question.
- related or unrelated fields are being laid out or grouped, and the
  spacing/column choice is in question.
- a navigation structure's depth (nested drill-down) vs. breadth (flat,
  wide menu) is being decided for a given destination count.
- a text or non-text (icon/control-boundary) contrast pair's WCAG floor
  is in question.
- an existing modal is interrupting a task, gating already-navigated-to
  content, or stacking on another modal, and whether to remove it is in
  question.
- a spec element carries a contrast-bearing color or a spacing/type
  value and needs a semantic token name, even pre-design-system.
Do not use this skill for interaction-design topics outside these six
axes (e.g. animation/motion, drag-and-drop, error-message copy) — it
carries no rules for those.

## Procedure

1. Identify which `## R<n>` rule matches the decision at hand from the
   Trigger conditions above; more than one rule can apply to the same
   component (e.g. R5 and R8 both bear on the same contrast-carrying
   color value).
2. For a control-type decision: apply R1 (2-4 short options -> radio
   buttons) unless its counter-example applies (any label runs long
   enough to wrap), in which case apply R2 (5+ options, or a
   space-constrained layout -> dropdown/listbox) instead.
3. For a field-layout decision: apply R3 — group semantically related
   fields with tighter spacing than unrelated groups, default to a
   single column, and reserve a same-row layout for atomic pairs.
4. For a navigation-structure decision: apply R4, checking the reachable
   destination count against its >50 (flatten) vs. <15-or-hierarchical
   (keep nested, add breadcrumbs) thresholds.
5. For a contrast decision: classify the element as text or non-text
   first, then apply R5 (text: >=4.5:1, or >=3:1 at the large-text
   threshold, excluding disabled/decorative text) or R6 (non-text
   meaning-carrying boundary/icon: >=3:1, excluding purely decorative
   icons).
6. For an existing modal: apply R7 — remove it if it interrupts a task
   with unrelated content, gates already-navigated-to content, or stacks
   on an open modal, unless it is confirming a destructive/irreversible
   action, which R7's counter-example keeps.
7. For any value R5 or R6 covers: apply R8 — name the semantic token the
   value maps to, flagged as provisional if no design-system document
   exists yet, rather than passing through the raw value.
8. Cite the matched rule number(s) and, where the rule carries one, its
   `Source:` URL alongside the resulting decision so it is traceable
   back to this playbook.

## Output shape

A single decision (control type chosen, field-layout/grouping choice,
navigation depth/breadth choice, contrast pass/fail/exempt verdict,
modal keep/remove verdict, or semantic token name) paired with the rule
number(s) it was derived from and that rule's `Source:` citation where
one exists — not a general interaction-design audit or a restatement of
the whole playbook.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- R1 — control type by option count (small sets)
- R2 — control type by option count (large sets)
- R3 — field grouping by proximity, not by column
- R4 — navigation depth vs. breadth
- R5 — text contrast floor
- R6 — non-text (icon/control-boundary) contrast floor
- R7 — REMOVAL: modal used for non-blocking or mid-task content
- R8 — semantic token reference by default, even pre-design-system
- S1 — Rule table (condition -> choice, quick reference) → references/rules.md
- S2 — Provenance → references/rules.md
