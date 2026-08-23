---
name: content-design-operational-playbook
description: >-
  Use when writing or reviewing user-facing copy — error messages, button/CTA and
  confirmation-dialog labels, plain-language phrasing, empty-state or onboarding text,
  tone-of-voice, copy-inventory reuse, or a staged revision pass — and need the
  condition-matched wording/action to choose. Trigger on requests like "write this error
  message", "버튼 문구 뭐라고 하지", "confirmation dialog copy", "plain language pass on this text".
  Do NOT use for cognitive-load shaping of developer tutorials (use
  devrel-content-comprehensibility).
---

# Content-design operational playbook

Issue: tokenmaxxxer/on-the-record#1174 (batch 1, UX/design family).
Format: numbered `condition → choice → source` rules, grouped by axis.
Each axis carries at least one REMOVAL-category rule (cut/reduce copy,
not add it). Sources are fetched, not recalled — see citations inline
and the evidence trail at the bottom.

Three research layers per axis, in order: (1) practitioner decision
rules at the demonstrated depth (GOV.UK, Material Design, NN/G
field guidance), (2) named methodologies verified at source (NN/G
error-message rubric, GOV.UK content style guide), (3) academic/
empirical theory layer (progressive disclosure, readability formulas,
tone-of-voice research).

## Trigger

Apply this skill when drafting or reviewing any user-facing copy
decision: a form field fails validation and needs an error message
(rules 1–10), an action button, CTA, or destructive-action confirmation
dialog needs a label (rules 11–15), body copy or microcopy needs a
plain-language pass (rules 16–19), an empty state or first-run/
progressive-disclosure surface needs copy (rules 20–23), tone-of-voice
needs setting on an error, failure, or success surface (rules 24–25), a
new string is being drafted where an existing shipped string might
already serve the same need, or a `plain_language_check`/severity
classification needs recording (rules 26–28), or a copy draft is being
revised against more than one quality dimension at once, or drafted
from scratch for a recurring UI-element category (rules 29–31).

## Procedure

1. If the copy responds to a form-validation failure, classify whether
   the field is empty, format-invalid, or system-caused, then apply the
   matching wording pattern and reuse the field's exact noun (rules
   1–9); pick banner vs. modal severity by consequence (rule 10).
2. If the copy labels a button, CTA, or confirmation dialog, name the
   concrete outcome rather than a generic verb, and for destructive
   actions restate the destroyed object and add extra friction when the
   action is irreversible (rules 11–15).
3. If the copy is body text, instructions, or microcopy, check sentence
   length and reading-level ceilings and swap technical terms for plain
   equivalents already in rule 6's banned-jargon list (rules 16–19).
4. If the copy is for an empty state or a first-run/feature-rich
   surface, reduce it to one obvious next action and defer secondary
   options behind progressive disclosure, gated by usage frequency
   (rules 20–23).
5. If the copy sits in a transactional/error/failure flow, set the
   humor and enthusiasm tone-axis values low and strip enthusiasm
   markers from failure copy (rules 24–25).
6. Before drafting any new string, check whether an existing shipped
   string already serves the same `content_id`/decision-need and reuse
   it verbatim unless a stated reason disqualifies it (rule 26); when
   recording a `plain_language_check`, name the failing category per
   failure (rule 27); when a prohibition is violated, classify it block
   or advisory, defaulting to block (rule 28).
7. When revising a draft against more than one quality dimension, run
   goal-fit, length, naturalness, and clarity as four separate
   sequential passes rather than one holistic read-through (rule 29),
   applying numeric length ceilings rather than a subjective "feels
   long" judgment (rule 30); when drafting a recurring UI-element
   category with no existing `content_id` match, start from that
   category's format+purpose+tone template (rule 31).

## Output shape

A content-design decision: the matched condition, the applicable rule
number(s), the concrete wording or action to apply (not just the
problem named), and the source citation backing it.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — Condition: a form field fails validation on submit → Choice: place the message directly adjacent to the field AND in a page-level error summary that links to each field;…
- 1.2 — Condition: a field is empty → Choice: word the message as an instruction ("Enter your first name"), never as a statement about the field ("First name must have an entry"…
- 1.3 — Condition: a field violates a format/length constraint → Choice: word the message as a description of the constraint ("Name must be 35 characters or less"), distinct fro…
- 1.4 — Condition: writing any error message → Choice: reuse the exact noun from the question/field label inside the message so the two visibly match; never introduce a synonym.…
- 1.5 — Condition: the system, not the user, caused the failure (timeout, 500, integration failure) → Choice: the message must place accountability on the system, never imply us…
- 1.6 — Condition: writing any error copy → Choice: target 7th–8th-grade reading level (Flesch-Kincaid) and ban jargon strings a support log would show users don't recognize (e.…
- 1.7 — Condition: an error is correctable with a known fix → Choice: the message must state the fix, not just name the problem; if the fix has low interaction cost, offer to do…
- 1.8 — Condition: user input triggers an error → Choice: preserve the original input in the field (never clear it) so the user corrects in place. Source: GOV.UK Design System,…
- 1.9 — **REMOVAL.** Condition: an error state already shows the constraint as hint text directly below the field → Choice: do not restate the same example/constraint inside the…
- 1.10 — Condition: an error message needs a severity read → Choice: use a modal only when the decision is consequential (data loss, payment); use an inline banner/toast for reco…
- 2.11 — Condition: labeling any action button → Choice: name the concrete outcome, never a generic verb; "Unmute now" over "Yes," "Delete repository" over "Delete." Source: NN/G…
- 2.12 — Condition: a confirmation dialog gates a destructive action → Choice: never use bare "Yes/No" — restate the destroyed object in the affirmative button ("Delete account")…
- 2.13 — Condition: a destructive action is irreversible and high-cost to undo (account deletion, permanent data loss) → Choice: require an extra confirmation step (typed confirm…
- 2.14 — Condition: labeling a multi-step flow's forward action → Choice: keep the label identical across every step ("Continue" throughout), never alternate with a near-synonym…
- 2.15 — **REMOVAL.** Condition: a confirmation dialog's body text restates information already visible in the triggering screen (e.g. the item name already shown in a list row)…
- 3.16 — Condition: writing body copy, instructions, or help text → Choice: keep sentences to 15–20 words on average, and to 5–8 words for microcopy (labels, tooltips, inline hin…
- 3.17 — Condition: a technical or internal term has a plain-language equivalent users already use → Choice: use the plain term ("Log in to your account") over the technical one…
- 3.18 — Condition: any user-facing copy is drafted → Choice: write in active voice and target ~8th-grade reading level as the default ceiling, not a stretch goal. Source: NN/G,…
- 3.19 — **REMOVAL.** Condition: a paragraph of instructional copy exceeds six sentences → Choice: cut it to fewer than six sentences per paragraph before shipping, splitting int…
- 4.20 — Condition: designing an empty state (no data yet, first-run, zero search results) → Choice: reduce the state to exactly one obvious next action in the copy and CTA; do n…
- 4.21 — Condition: onboarding a first-time user into a feature-rich surface → Choice: surface only the copy/controls needed for the immediate task; defer secondary options behin…
- 4.22 — Condition: choosing whether a secondary option's copy appears inline or behind a disclosure control → Choice: measure by frequency of use, matching this playbook's field…
- 4.23 — **REMOVAL.** Condition: an empty state or onboarding screen's copy duplicates guidance already given in a preceding step (e.g. a tooltip repeating the empty-state headli…
- 5.24 — Condition: setting tone on the humor axis for transactional/error flows (payments, account deletion, data loss) → Choice: default to the low-humor end of NN/G's humor ax…
- 5.25 — **REMOVAL.** Condition: draft copy scores high on the enthusiasm axis (exclamation points, "Awesome!," "Great job!") inside an error or failure state → Choice: strip ent…
- 6.26 — **REMOVAL.** Condition: drafting new copy for a decision-need (`user_need`) that an existing shipped string already serves under the same `content_id` → Choice: reuse th…
- 6.27 — Condition: recording `plain_language_check` → Choice: a `fail` result names which category failed — sentence over ~20 words on the decision-critical clause, passive voic…
- 6.28 — Condition: a copy string violates one of this handbook's prohibitions → Choice: classify the violation before recording it — **block** (the string does not ship until th…
- 7.29 — Condition: editing a copy draft against more than one quality dimension at once (does it achieve the goal, is it short enough, does it read naturally, is it unambiguous)…
- 7.30 — Condition: the length round of rule 29 → Choice: apply numeric ceilings, not a subjective "feels long" judgment — roughly 8-14 words per sentence and 40-60 characters pe…
- 7.31 — Condition: drafting copy for a recurring UI-element category (button, error, notification, form field) with no existing content_id match under rule 26 → Choice: start fr…
- S1 — Evidence trail (fetched sources) → references/rules.md
- S2 — Depth note → references/rules.md
