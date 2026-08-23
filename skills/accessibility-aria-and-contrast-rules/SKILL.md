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

## 1. ARIA role selection

**Rule 1.1 — Do not assign a role you cannot fully implement.**
Condition: a custom widget needs a non-native interaction pattern (e.g.
`role="tablist"`, `role="slider"`).
Choice: only apply the role if every required keyboard interaction and
state-management behavior for that role (per the APG pattern) is also
implemented in the same change. If the interactions cannot be delivered
in this change, do not add the role — ship the plain element instead.
Why: "Using a role without fulfilling the promise of that role is
similar to making a 'Place Order' button that abandons an order and
empties the shopping cart."
Source: https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ (fetched 2026-08-13)

**Rule 1.2 [REMOVAL] — Remove ARIA roles that cloak native semantics.**
Condition: an ARIA role is present on an element where it overrides
what the underlying HTML element already communicates (e.g.
`role="navigation"` on a `<ul>` of unrelated links, `role="log"` on a
`<table>`).
Choice: remove the role; let the native element's semantics stand, or
replace the element with the one whose native semantics already match
the intended role.
Why: "Authors can inadvertently override accessibility semantics" —
ARIA that cloaks native meaning is actively harmful, not neutral.
Source: https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ (fetched 2026-08-13)
Counter-example: `aria-pressed="false"` added to a native `<button>` is
NOT covered by this rule — it supplements state without overriding the
button's native role, matching Rule 1.3 below.

**Rule 1.3 — Use ARIA to add state, not to replace role/name.**
Condition: a native element already carries correct role and accessible
name, but needs to expose additional state (pressed, expanded,
selected).
Choice: add the single state attribute (`aria-pressed`, `aria-expanded`,
`aria-selected`) without touching role or name.
Source: https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ (fetched 2026-08-13)

**Rule 1.4 — First Rule of ARIA: prefer a native element over ARIA-on-a-`<div>`.**
Condition: a component is being built and a native HTML element
(`<button>`, `<nav>`, `<input>`, `<a href>`, ...) already provides the
role, state, and keyboard behavior the component needs.
Choice: use the native element; do not reach for `role`/`aria-*`
attributes on a generic `<div>`/`<span>` to re-implement semantics and
keyboard handling a native element gives for free.
Why: the WAI-ARIA Authoring Practices' own "No ARIA is better than Bad
ARIA" / First Rule of ARIA states that if a native HTML element or
attribute has the semantics and behavior you require, use it instead of
re-purposing an element and adding ARIA to make it accessible.
Source: https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ (fetched 2026-08-22)

## 2. Accessible naming

**Rule 2.1 [REMOVAL] — Remove `aria-label`/`aria-labelledby` that
overrides visible child content on naming-from-content roles.**
Condition: an element with a role that derives its name from descendant
content (button, link, checkbox, radio, switch, tab, heading, menuitem,
option, …) also carries `aria-label`/`aria-labelledby` whose text
differs from or duplicates the visible content.
Choice: delete the `aria-label`/`aria-labelledby`; let the visible
child content be the accessible name. If the visible text is
insufficient, edit the visible text itself rather than layering a
hidden override on top of it.
Why: "If an element with one of the above roles that supports naming
from child content is named by using `aria-label` or `aria-labelledby`,
content contained in the element and its descendants is hidden from
assistive technology users" — the override, not just a mismatch, is the
defect.
Source: https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/ (fetched 2026-08-13)

**Rule 2.2 — Prefer visible text as the accessible name source.**
Condition: a control needs an accessible name and visible text already
exists that could serve as it.
Choice: use the visible text (native `<label>`, or `aria-labelledby`
pointing at the visible node) rather than an invisible `aria-label`
carrying separately-maintained text.
Why: "using the visible text for the accessible name simplifies
maintenance" — reduces drift, translation duplication, and bugs on UI
changes.
Source: https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/ (fetched 2026-08-13)

**Rule 2.3 [REMOVAL] — Remove reliance on `title`/`placeholder` for
naming.**
Condition: an interactive element's only accessible name comes from a
`title` or `placeholder` attribute.
Choice: remove the naming dependency on `title`/`placeholder`; add a
native `<label>`, visible text, or explicit `aria-label`/
`aria-labelledby` instead.
Why: "Because the purpose of these attributes is not naming, their
content typically yields low quality accessible names that are not
effective."
Source: https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/ (fetched 2026-08-13)

**Rule 2.4 — Know the accname precedence order before debugging a wrong
accessible name.**
Condition: an element's computed accessible name does not match what
was intended, and multiple naming sources are present at once
(`aria-labelledby`, `aria-label`, native labeling (e.g. `<label>`),
visible content, `title`).
Choice: resolve the mismatch by walking the Accessible Name and
Description Computation precedence order, highest first:
`aria-labelledby` > `aria-label` > native host-language labeling
mechanism (e.g. `<label for>`) > element content/subtree > `title`
attribute. Fix the highest-precedence source that is present and wrong,
not a lower one — editing a `<label>` has no effect if an
`aria-labelledby` elsewhere is already winning.
Why: the accname computation is a strict precedence chain, not a merge
of all present sources — a lower-precedence value is silently ignored
whenever a higher one is present, which is the single most common cause
of "I changed the label but the accessible name didn't change."
Source: https://www.w3.org/TR/accname-1.2/ (fetched 2026-08-22)

## 3. Contrast (WCAG 1.4.3)

**Rule 3.1 — Body/standard text contrast threshold.**
Condition: text is under 18pt non-bold (~24px) or under 14pt bold
(~18.5px equivalent).
Choice: require ≥ 4.5:1 contrast against its background, computed
without rounding (4.499:1 fails the 4.5:1 threshold — do not round up).
Source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (fetched 2026-08-13)

**Rule 3.2 — Large-text contrast threshold.**
Condition: text is at or above 18pt (~24px) non-bold, or 14pt (~18.5px)
bold, or the CJK-equivalent size.
Choice: 3:1 is sufficient; do not require 4.5:1 for text meeting this
size/weight floor.
Source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (fetched 2026-08-13)

**Rule 3.3 [REMOVAL/exception] — When a contrast fix is not required.**
Condition: the text is (a) part of an inactive/disabled control, (b)
purely decorative with no informational or functional purpose, (c)
part of a logo/brand name, (d) incidental text inside a photo/image
with other significant visual content, or (e) not visible to anyone.
Choice: do not flag or remediate a contrast finding on text meeting any
of these five conditions — the criterion explicitly exempts them, so a
lint/audit rule should not raise a failure here.
Source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (fetched 2026-08-13)

## 4. Focus order and visibility

**Rule 4.1 — Focus order must follow logical/reading structure, not
arbitrary visual position.**
Condition: a component's DOM order and its visual (CSS) order diverge.
Choice: reorder the DOM to match the meaningful reading/interaction
sequence rather than relying on CSS alone to fix the visual sequence;
if CSS is used to align visual order to DOM order, verify the result
against technique C27 (DOM order matches visual order).
Source: https://www.w3.org/WAI/WCAG22/quickref/?showtechniques=241%2C242#focus-order (fetched 2026-08-13)

**Rule 4.2 [REMOVAL] — Never remove the visual focus indicator via
outline/border styling.**
Condition: a stylesheet sets `outline: none` or overrides borders on
`:focus` without supplying an equivalent visible replacement.
Choice: remove the outline-suppressing rule, or replace it with an
equally visible custom focus style that meets 2.4.7/2.4.13 — never ship
`outline: none` with no replacement.
Why: F78 names this pattern directly as a failure: "styling element
outlines and borders in a way that removes or renders non-visible the
visual focus indicator."
Source: https://www.w3.org/WAI/WCAG22/quickref/?showtechniques=241%2C242#focus-order (fetched 2026-08-13)

**Open gap (recorded, not resolved here):** WCAG's own quickref
provides no concrete decision tree for roving-tabindex vs.
`tabindex="0"`/`tabindex="-1"` patterns on composite widgets (e.g.
toolbars, listboxes) — it defers to the APG per-pattern pages. This
playbook does not assert a rule here; a follow-up rule needs a fetch of
the specific APG pattern page for the widget in question (e.g.
Listbox, Toolbar) rather than being generalized from this source.
Source: https://www.w3.org/WAI/WCAG22/quickref/?showtechniques=241%2C242#focus-order (fetched 2026-08-13)

## 5. Evidence-field specificity and provenance

**Rule 5.1 — Name the assistive technology, not the generic phrase.**
Condition: an evaluation entry's `evidence` field cites
assistive-technology testing (screen reader, switch, or magnification
tool) as the technique used.
Choice: name the specific tool and version tested (e.g. "NVDA 2026.1 +
Firefox"), never the bare phrase "screen reader tested." No single AT
tool represents the field — usage splits close to evenly between the
two leading screen readers and reverses by region — so an unnamed tool
cannot be checked for AT diversity across a multi-market product, nor
reproduced by a later evaluator.
Source: WebAIM Screen Reader User Survey #10 (2024),
https://webaim.org/projects/screenreadersurvey10/ (fetched 2026-08-13)

**Rule 5.2 — A machine-suggested accessible name or alt text is a
draft, not an assertion.**
Condition: an accessible-name or alt-text value under evaluation was
produced by a suggestion tool (spell/AI-assisted drafting) rather than
authored or reviewed by a person.
Choice: do not record the entry's `assertedBy` as a person, and do not
give the criterion an affirmative verdict, until a human has reviewed
the suggested value and accepted or edited it. Treat the unreviewed
suggestion the same way an inconclusive automated-scan result is
treated under this checklist's `verdict` guidance — state it in
`evidence`, do not default it to a pass.
Why: design-stage suggestion tooling now drafts alt text and naming
candidates directly inside the design surface; a draft is not
equivalent to human judgment about whether the name or description is
actually adequate for the content.
Source: WCAG 2.2 Understanding — Non-text Content,
https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
(fetched 2026-08-13)

**Rule 5.3 — Automated-scan evidence alone does not license an
affirmative verdict outside its own coverage ceiling.**
Condition: the only evidence gathered for a criterion is an automated
scanner's result (axe-core, Lighthouse, Pa11y, or an equivalent
engine), and the criterion is one automated tooling cannot fully
verify (structural relationships on custom widgets, keyboard operation,
focus order semantics — matching the SessionStart directive's own
"automated tooling cannot fully verify" list).
Choice: do not close the criterion on scan evidence alone; add a
manual technique (inspection, AT walkthrough, or functional test)
before recording a verdict other than "not yet run."
Why: automated tooling's own published ceiling is roughly 57% of
issues by volume — most of the remainder is exactly the class of
criteria (structure, keyboard, focus) this rule names.
Source: aggregate automated-tooling coverage figures reported across
the axe-core/Lighthouse/Pa11y comparison literature (fetched
2026-08-13; see https://www.a11yflow.dev/blog/axe-vs-lighthouse-vs-wave-vs-pa11y)

**Rule 5.4 — A tradeoff-driven `not-applicable` scope note states the
rationale, not just the boundary.**
Condition: a criterion is marked `not-applicable` because a deliberate
design tradeoff excludes it (not because the criterion structurally
cannot apply to the artifact type at all).
Choice: distinguish the two cases in the scope note. A boundary-
exclusion note states only the exclusion boundary (e.g. "no audio
content in this artifact — 1.2.x does not apply"). A tradeoff-rationale
note must additionally state what the tradeoff was weighed against
(e.g. why a competing constraint outweighed applying the criterion) —
mirroring ADR discipline: the decision without its rationale cannot be
re-evaluated later if the tradeoff's premises change.
Why: a bare boundary phrase silently absorbs a design tradeoff into the
same vocabulary as a criterion that never applied at all, hiding the
judgment call from a later reviewer who would otherwise re-weigh it.
Source: Architecture Decision Record rationale-capture convention
(decision + context weighed against, recorded alongside the decision).

## Sources

- https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/quickref/?showtechniques=241%2C242#focus-order
- https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/
- https://webaim.org/projects/screenreadersurvey10/
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- https://www.a11yflow.dev/blog/axe-vs-lighthouse-vs-wave-vs-pa11y
- https://www.w3.org/TR/accname-1.2/
