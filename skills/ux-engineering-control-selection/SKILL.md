---
name: ux-engineering-control-selection
description: Use when picking which UI control fits a given field's type, option count, or interaction contract. Applies to the control-selection-by-field-type axis.
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

## Decision rules

1. When a field is a true binary choice with an immediate, visible effect
   (e.g. a setting that applies instantly, no separate "save" step),
   pick a toggle switch rather than a checkbox — toggles communicate
   on/off state and immediacy, checkboxes communicate membership in a
   set that is committed later.
   source: NN/g, "Checkboxes vs. Radio Buttons" (fetched 2026-08-13,
   https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/) —
   general principle that control choice should match selection
   semantics, extended here to the toggle/checkbox binary-immediate
   case per the same semantics-first reasoning the article applies to
   radio-vs-checkbox.
   counter-example: a binary field inside a form that is submitted as a
   whole (e.g. "subscribe to newsletter" on a signup form with a Submit
   button) should stay a checkbox, not a toggle — there is no immediate
   effect to signal, and a toggle implies an action already took place.

2. When 3-7 options are mutually exclusive and screen space allows all
   options to be shown at once, pick a radio button group over a
   dropdown/select — radio groups keep every option visible for direct
   comparison and carry lower cognitive load than a closed list.
   source: NN/g, "Checkboxes vs. Radio Buttons" (fetched 2026-08-13,
   https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/):
   "Radio buttons have lower cognitive load because they make all
   options permanently visible so that users can easily compare them."
   counter-example: on a narrow mobile viewport where 7 radio options
   would push the primary action below the fold, drop to a select/
   dropdown despite the option count — vertical space cost outweighs
   the comparison benefit.

3. When options are mutually exclusive but space is constrained (dense
   table row, narrow sidebar) or the option count is at the upper edge
   of the 3-7 range, choose a dropdown/select over a radio group —
   trade comparison-at-a-glance for a compact footprint.
   source: NN/g, "Checkboxes vs. Radio Buttons" (fetched 2026-08-13,
   https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/) —
   "space constraints may necessitate using dropdowns instead."
   counter-example: do not use a dropdown for a 3-option field that
   fits comfortably on screen just for visual tidiness — that trades
   away real usability for no space benefit.

4. When an option set has 8 or more values, pick a searchable
   select/combobox over a plain dropdown or radio group — remove the
   need to scroll a long closed list by adding type-to-filter.
   source: NN/g, "Checkboxes vs. Radio Buttons" (fetched 2026-08-13,
   https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/),
   applying the article's space/cognitive-load tradeoff to the
   long-list case it flags as the reason plain lists lose to radio
   groups at smaller counts — inverted here for large counts where even
   a select becomes a scroll burden.
   counter-example: if the 8+ options are a small, fixed, memorized set
   users pick from repeatedly (e.g. their own 9 saved addresses),
   a plain scrollable list may outperform a combobox — forcing typing
   adds friction for a set the user already knows by position.

5. When a field is a specific calendar date and users need to browse or
   confirm a date visually, pick a date picker; when users routinely
   know and can type the exact date faster than they can navigate a
   calendar widget, permit a free-text/typed date field with format
   validation instead of forcing a picker.
   source: Apple Human Interface Guidelines, Pickers (fetched
   2026-08-13, https://developer.apple.com/design/human-interface-guidelines/pickers)
   general picker-selection guidance — pick when precision and visual
   date confirmation matter; prefer a lighter-weight input when the
   date is simple/relative or the user already knows it.
   counter-example: do not force a date picker on a birth-year-only
   field (age verification) — a picker built for day-level precision
   adds unnecessary navigation for a single value users type in one
   motion.

6. When free text is short (a name, email, single line of an address),
   pick a single-line text input; when the expected content is long,
   multi-paragraph, or needs visible line breaks, pick a text view/
   textarea sized so its visible row height previews how much space the
   answer will occupy — do not force long-form answers into a
   single-line input that hides their true length.
   source: Apple Human Interface Guidelines, Text Views (fetched
   2026-08-13, search result from
   https://developer.apple.com/design/human-interface-guidelines/text-views):
   "For multiline or multistyle text entry, use a text view instead of
   a text field... Use a text field to request a small amount of
   information... To let people input larger amounts of text, use a
   text view instead."
   counter-example: a "notes" field that is usually one short sentence
   but occasionally long should still default to a small textarea, not
   a single-line input — resizing a textarea down is cheap, but a
   single-line input truncates long answers unpredictably.

7. REMOVAL: when a form field's control choice adds an extra
   confirmation step that duplicates information already implied by an
   adjacent control (e.g. a "confirm date" dropdown next to a date
   picker that already shows the chosen date), cut the redundant
   control rather than adding a second one for reassurance — the
   picker's own visible selection already carries that information.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021) (fetched 2026-08-13
   via search summary of https://www.nature.com/articles/s41586-021-03380-y
   and https://phys.org/news/2021-04-brains-opportunities.html):
   "people are less likely to identify advantageous subtractive
   changes... additive ideas come to mind quickly and easily, but
   subtractive ideas require more cognitive effort" — applied here as
   the reason designers default to adding a confirmation control
   instead of checking whether an existing control already answers the
   need.
   counter-example: do not remove a genuinely separate confirmation
   step for a destructive, hard-to-reverse action (e.g. deleting an
   account) just because a control nearby names the target — that
   confirmation is not redundant, it is a deliberate friction gate.

8. For an interactive pattern with an established role-and-keyboard-
   interaction contract (a dialog's focus trap and Escape-to-close, a
   combobox's arrow-key/typeahead behavior, an accordion's expand/
   collapse and screen-reader state, a tab set's arrow-key roving
   focus), pick the control that matches that contract over one that
   only looks visually similar — a custom-built element that resembles
   the pattern but skips its keyboard/state contract breaks the
   expectations users and assistive tech already carry into it.
   rationale: users transfer keyboard and screen-reader expectations
   from the established pattern to anything that looks like it; a
   look-alike that silently drops the contract fails invisibly, only
   surfacing when someone actually depends on the missing behavior.
   counter-example: a genuinely novel interaction with no established
   contract to match (a bespoke visualization control, say) is not
   obligated to imitate an existing pattern's contract just because it
   shares some visual resemblance — the rule applies once a real
   established contract exists to match.

9. Name accessibility as a co-equal technical constraint alongside
   framework and performance at spec time, not as a separate pass
   deferred to after the visual/interaction design is settled.
   rationale: a constraint recorded only after the layout and
   interaction are already fixed tends to get satisfied by patching
   around the existing design rather than by a choice that was actually
   available at spec time (e.g. a control shape that cannot be made
   keyboard-operable without a rework, chosen before accessibility was
   ever named as a requirement) — naming it up front keeps it a real
   constraint on the initial choice, not a retrofit.
   counter-example: a purely internal, throwaway prototype with no path
   to shipping does not need the same spec-time discipline — the rule
   targets specs that will become real, reachable interfaces.
