---
name: accessibility-aria-and-contrast-rules
description: >-
  Use when you are deciding an ARIA role, an accessible name, a text/background contrast pair,
  a focus-order or focus-visibility change, or an evidence-field entry for an accessibility
  criterion, and need a condition-matched rule rather than a general accessibility overview.
  Trigger on requests like "which ARIA role here", "accessible name for this button", "focus
  order after dialog close", "접근성 검토해줘". Do NOT use for general design-side color-set choice
  beyond conformance floors (use ux-engineering-color-visibility).
---

# Operational playbook: ARIA usage, contrast, and focus (issue-1174)

Numbered condition → choice → source rules. Practitioner-depth decision
rules, not methodology-name pointers. Each rule cites the fetched source
it is derived from; conflicting guidance is flagged where found.

## Trigger

Use this skill when a concrete change or evaluation touches one of:
- an ARIA `role` is being added, removed, or reconsidered on an element
  (native vs. custom widget) — not a general "is this accessible?"
  question.
- an element's accessible name is being set or is ambiguous between
  visible text, `aria-label`/`aria-labelledby`, and `title`/`placeholder`.
- a text/background color pair's WCAG 1.4.3 contrast ratio is in
  question, including whether an exemption (disabled, decorative, logo,
  incidental-in-photo, invisible) applies.
- a component's focus order diverges from its visual order, or a
  `:focus` style change risks suppressing the visible focus indicator.
- an accessibility checklist/evaluation entry's `evidence` or
  `assertedBy`/`verdict` field needs to state AT-tool specificity,
  machine-suggestion provenance, automated-scan coverage limits, or a
  `not-applicable` tradeoff rationale.
Do not use this skill for accessibility topics outside these five axes
(e.g. captions, motion/animation, internationalization) — it carries no
rules for those.

## Procedure

1. Identify which of the five rule sections (`## 1`–`## 5`) matches the
   decision at hand from the Trigger conditions above.
2. Within that section, match the specific `Condition:` line of each
   rule to the case in front of you; more than one rule in a section can
   apply (e.g. Rule 1.1 and Rule 1.3 can both bear on the same widget).
3. For an ARIA role decision: apply Rule 1.4 (does a native element
   already give you this for free?) first, then Rule 1.1 (can you fully
   implement the role?), Rule 1.2 (does an existing role cloak native
   semantics and need removal?), then Rule 1.3 (is this actually a state
   attribute, not a role/name change?).
4. For an accessible-name decision: apply Rule 2.1 (remove an
   overriding `aria-label`/`aria-labelledby` on a naming-from-content
   role), Rule 2.2 (prefer visible text as the name source), Rule 2.3
   (never let `title`/`placeholder` be the only name source), and Rule
   2.4 (when the computed name is wrong, walk the accname precedence
   order to find which source is actually winning).
5. For a contrast decision: determine text size/weight first to select
   Rule 3.1 (standard, ≥4.5:1) vs. Rule 3.2 (large text, ≥3:1) without
   rounding, then check Rule 3.3's five exemption conditions before
   flagging or remediating.
6. For a focus decision: apply Rule 4.1 (DOM order vs. visual order) and
   Rule 4.2 (never suppress the focus indicator without an equivalent
   replacement); consult the recorded Open gap note under `## 4` before
   asserting a roving-tabindex rule not present in this playbook.
7. For an evidence-field decision: apply Rule 5.1 (name the specific AT
   tool), Rule 5.2 (treat a machine-suggested name/alt text as a draft
   pending human review), Rule 5.3 (automated-scan evidence alone does
   not close a criterion outside its coverage ceiling), and Rule 5.4 (a
   tradeoff-driven `not-applicable` note states the rationale, not just
   the boundary).
8. Cite the matched rule number(s) and source URL alongside the
   resulting decision so it is traceable back to this playbook.

## Output shape

A single decision (ARIA role kept/removed/added, accessible-name source
chosen, contrast pass/fail/exempt verdict, focus-order/visibility fix,
or evidence-field wording) paired with the rule number(s) it was derived
from and that rule's `Source:` citation — not a general accessibility
audit or a restatement of the whole playbook.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — a custom widget needs a non-native interaction pattern (e.g. `role="tablist"`, `role="slider"`) → only apply the role if every required keyboard interaction and
- 1.2 — [REMOVAL] an ARIA role is present on an element where it overrides what the underlying HTML element already communicates (e.g. `role="navigation"` on a `<ul>` of unrelat… → remove the role; let the native element's semantics stand, or
- 1.3 — a native element already carries correct role and accessible name, but needs to expose additional state (pressed, expanded, selected) → add the single state attribute (`aria-pressed`, `aria-expanded`,
- 1.4 — a component is being built and a native HTML element (`<button>`, `<nav>`, `<input>`, `<a href>`, ...) already provides the role, state, and keyboard behavior the compon… → use the native element; do not reach for `role`/`aria-*`
- 2.1 — [REMOVAL] an element with a role that derives its name from descendant content (button, link, checkbox, radio, switch, tab, heading, menuitem, option, …) also carries `a… → delete the `aria-label`/`aria-labelledby`; let the visible
- 2.2 — a control needs an accessible name and visible text already exists that could serve as it → use the visible text (native `<label>`, or `aria-labelledby`
- 2.3 — [REMOVAL] an interactive element's only accessible name comes from a `title` or `placeholder` attribute → remove the naming dependency on `title`/`placeholder`; add a
- 2.4 — an element's computed accessible name does not match what was intended, and multiple naming sources are present at once (`aria-labelledby`, `aria-label`, native labeling… → resolve the mismatch by walking the Accessible Name and
- 3.1 — text is under 18pt non-bold (~24px) or under 14pt bold (~18.5px equivalent) → require ≥ 4.5:1 contrast against its background, computed
- 3.2 — the text is (a) part of an inactive/disabled control, (b) purely decorative with no informational or functional purpose, (c) part of a logo/brand name, (d) incidental te… → 3:1 is sufficient; do not require 4.5:1 for text meeting this
- 4.1 — a component's DOM order and its visual (CSS) order diverge → reorder the DOM to match the meaningful reading/interaction
- 4.2 — [REMOVAL] a stylesheet sets `outline: none` or overrides borders on `:focus` without supplying an equivalent visible replacement → remove the outline-suppressing rule, or replace it with an
- 5.1 — an evaluation entry's `evidence` field cites assistive-technology testing (screen reader, switch, or magnification tool) as the technique used → name the specific tool and version tested (e.g. "NVDA 2026.1 +
- 5.2 — an accessible-name or alt-text value under evaluation was produced by a suggestion tool (spell/AI-assisted drafting) rather than authored or reviewed by a person → do not record the entry's `assertedBy` as a person, and do not
- 5.3 — the only evidence gathered for a criterion is an automated scanner's result (axe-core, Lighthouse, Pa11y, or an equivalent engine), and the criterion is one automated to… → do not close the criterion on scan evidence alone; add a
- 5.4 — a criterion is marked `not-applicable` because a deliberate design tradeoff excludes it (not because the criterion structurally cannot apply to the artifact type at all) → distinguish the two cases in the scope note. A boundary-
- S1 — Sources → references/rules.md
