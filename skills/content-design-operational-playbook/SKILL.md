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

## Axis 1 — Error messages

1. Condition: a form field fails validation on submit → Choice: place
   the message directly adjacent to the field AND in a page-level error
   summary that links to each field; do not rely on either alone.
   Source: NN/G error-message scoring rubric, "Display close to error
   source" (https://www.nngroup.com/articles/error-messages-scoring-rubric/).
2. Condition: a field is empty → Choice: word the message as an
   instruction ("Enter your first name"), never as a statement about
   the field ("First name must have an entry"). Source: GOV.UK Design
   System, error message component
   (https://design-system.service.gov.uk/components/error-message/).
3. Condition: a field violates a format/length constraint → Choice:
   word the message as a description of the constraint ("Name must be
   35 characters or less"), distinct from the empty-field instruction
   pattern in rule 2. Source: GOV.UK Design System, error message
   component.
4. Condition: writing any error message → Choice: reuse the exact noun
   from the question/field label inside the message so the two visibly
   match; never introduce a synonym. Source: GOV.UK Design System,
   error message component.
5. Condition: the system, not the user, caused the failure (timeout,
   500, integration failure) → Choice: the message must place
   accountability on the system, never imply user fault; avoid humor in
   this state. Source: NN/G error-message scoring rubric, "Positive
   tone, no blame."
6. Condition: writing any error copy → Choice: target 7th–8th-grade
   reading level (Flesch-Kincaid) and ban jargon strings a support log
   would show users don't recognize (e.g. raw error codes, "form post
   error"). Source: NN/G error-message scoring rubric, "Human-readable
   language"; GOV.UK Design System, error message component (banned
   word list: "forbidden," "illegal," "forgot," "please," "sorry,"
   "valid/invalid," "oops").
7. Condition: an error is correctable with a known fix → Choice: the
   message must state the fix, not just name the problem; if the fix
   has low interaction cost, offer to do it for the user (auto-format,
   suggest corrected value) rather than only describing it. Source:
   NN/G error-message scoring rubric, "Offer constructive advice" +
   "Reduce correction effort."
8. Condition: user input triggers an error → Choice: preserve the
   original input in the field (never clear it) so the user corrects
   in place. Source: GOV.UK Design System, error message component,
   "Format Requirements."
9. **REMOVAL.** Condition: an error state already shows the constraint
   as hint text directly below the field → Choice: do not restate the
   same example/constraint inside the error message; delete the
   redundant clause. Source: GOV.UK Design System, error message
   component, "Rules to Avoid — redundant examples already shown as
   hint text."
10. Condition: an error message needs a severity read → Choice: use a
    modal only when the decision is consequential (data loss, payment);
    use an inline banner/toast for recoverable, low-stakes issues.
    Source: NN/G error-message scoring rubric, "Design based on
    impact."

## Axis 2 — Buttons, CTAs, and confirmation dialogs

11. Condition: labeling any action button → Choice: name the concrete
    outcome, never a generic verb; "Unmute now" over "Yes," "Delete
    repository" over "Delete." Source: NN/G microcopy guidance (button
    label clarity), corroborated by Material Design confirmation-dialog
    practice (https://www.nngroup.com/articles/error-messages-scoring-rubric/
    search context; UX Planet confirmation-dialog analysis
    https://uxplanet.org/confirmation-dialogs-how-to-design-dialogues-without-irritation-7b4cf2599956).
12. Condition: a confirmation dialog gates a destructive action → Choice:
    never use bare "Yes/No" — restate the destroyed object in the
    affirmative button ("Delete account"), not on the dialog title
    alone. Source: UX Planet, confirmation dialog design; Design Systems
    Collective, "Designing better buttons: how to handle destructive
    actions" (https://www.designsystemscollective.com/designing-better-buttons-how-to-handle-destructive-actions-d7c55eef6bdf).
13. Condition: a destructive action is irreversible and high-cost to
    undo (account deletion, permanent data loss) → Choice: require an
    extra confirmation step (typed confirmation phrase or second modal)
    beyond the single dialog used for reversible destructive actions.
    Source: Design Systems Collective, destructive-action buttons,
    "Intentional Friction."
14. Condition: labeling a multi-step flow's forward action → Choice:
    keep the label identical across every step ("Continue" throughout),
    never alternate with a near-synonym ("Next") on some pages. Source:
    GOV.UK Design System, forms guidance (https://design-system.service.gov.uk/components/error-message/
    cross-reference; UK Parliament Design System, "Designing forms"
    https://designsystem.parliament.uk/how-tos/designing-forms/).
15. **REMOVAL.** Condition: a confirmation dialog's body text restates
    information already visible in the triggering screen (e.g. the
    item name already shown in a list row) → Choice: cut the
    restatement from the dialog body; keep only the consequence and the
    two action labels. Source: UX Planet, confirmation dialog design
    (minimal-friction principle) — derived from the same "reduce
    interaction cost" logic as rule 7's low-cost-fix requirement.

## Axis 3 — Plain language and readability

16. Condition: writing body copy, instructions, or help text → Choice:
    keep sentences to 15–20 words on average, and to 5–8 words for
    microcopy (labels, tooltips, inline hints) specifically. Source:
    Plain-language readability synthesis (MSKTC Plain Language Tool,
    NN/G "Legibility, Readability, and Comprehension"
    https://www.nngroup.com/articles/legibility-readability-comprehension/).
17. Condition: a technical or internal term has a plain-language
    equivalent users already use → Choice: use the plain term
    ("Log in to your account") over the technical one ("Authenticate
    your credentials"). Source: plain-language microcopy synthesis
    (Bird, UX writing best practices, cross-checked against GOV.UK
    banned-jargon list in rule 6).
18. Condition: any user-facing copy is drafted → Choice: write in
    active voice and target ~8th-grade reading level as the default
    ceiling, not a stretch goal. Source: NN/G, "Legibility, Readability,
    and Comprehension"; MSKTC Plain Language Tool.
19. **REMOVAL.** Condition: a paragraph of instructional copy exceeds
    six sentences → Choice: cut it to fewer than six sentences per
    paragraph before shipping, splitting into a list or additional
    step rather than keeping one long block. Source: plain-language
    guideline synthesis (MSKTC Plain Language Tool; Governor's Office
    plain-language guidelines, https://governor.wa.gov/issues/efficient-government/plain-language/plain-language-guidelines).

## Axis 4 — Empty states and progressive disclosure

20. Condition: designing an empty state (no data yet, first-run,
    zero search results) → Choice: reduce the state to exactly one
    obvious next action in the copy and CTA; do not list every possible
    action available elsewhere in the product. Source: empty-state UX
    synthesis (Tim Graf, "The UX of Empty States,"
    https://timgraf.com/ui/the-ux-of-empty-states-designing-moments-of-nothing-into-something-exceptional/).
21. Condition: onboarding a first-time user into a feature-rich surface
    → Choice: surface only the copy/controls needed for the immediate
    task; defer secondary options behind progressive disclosure
    (tooltip, "advanced" expander) rather than presenting them upfront.
    Source: Nielsen's progressive-disclosure pattern (1995), as
    synthesized in UXPin, "What Is Progressive Disclosure in UX?"
    (https://www.uxpin.com/studio/blog/what-is-progressive-disclosure/).
22. Condition: choosing whether a secondary option's copy appears
    inline or behind a disclosure control → Choice: measure by
    frequency of use, matching this playbook's field-type-to-control
    logic — options used by most users in the common path stay inline;
    options used by a minority move behind progressive disclosure.
    Source: UXPin progressive disclosure synthesis (task-completion-time
    and support-ticket reduction findings cited as the empirical
    grounding for this cutoff).
23. **REMOVAL.** Condition: an empty state or onboarding screen's copy
    duplicates guidance already given in a preceding step (e.g. a
    tooltip repeating the empty-state headline) → Choice: delete the
    duplicate; progressive disclosure fails as a technique if the
    "disclosed" copy is something the user already read. Source: UXPin
    progressive disclosure synthesis, cognitive-load rationale.

## Axis 5 — Tone-of-voice axis application (NN/G 4-axis)

24. Condition: setting tone on the humor axis for transactional/error
    flows (payments, account deletion, data loss) → Choice: default to
    the low-humor end of NN/G's humor axis; reserve any humor for
    low-stakes, non-error, celebratory moments only. Source: NN/G
    error-message scoring rubric, "avoid humor" in blame/tone guidance;
    NN/G four-tone-dimension framework (humor, formality,
    respectfulness, enthusiasm) as surfaced in the microcopy sweep
    (https://www.nngroup.com/articles/error-messages-scoring-rubric/).
25. **REMOVAL.** Condition: draft copy scores high on the enthusiasm
    axis (exclamation points, "Awesome!," "Great job!") inside an error
    or failure state → Choice: strip enthusiasm-axis markers entirely
    from error/failure copy; enthusiasm is reserved for success states.
    Source: NN/G four-tone-dimension framework, cross-applied with the
    error-rubric's "positive tone, no blame ≠ celebratory tone"
    distinction (same source as rule 24).

## Axis 6 — Copy inventory reuse and severity-tiered rules

26. **REMOVAL.** Condition: drafting new copy for a decision-need
    (`user_need`) that an existing shipped string already serves under
    the same `content_id` → Choice: reuse the existing string verbatim;
    do not draft a near-duplicate variant. A new string is warranted
    only with a stated reason the existing one fails this decision
    (wrong tone-axis target, wrong content_id, stale reference) —
    "reads better" is not a reason. Source: GOV.UK Design System
    content style guide, consistency principle
    (https://www.gov.uk/guidance/content-design/writing-for-gov-uk).
27. Condition: recording `plain_language_check` → Choice: a `fail`
    result names which category failed — sentence over ~20 words on
    the decision-critical clause, passive voice hiding who does what,
    unexplained jargon, or a hedge word ("might," "could," "try to")
    that obscures the actual outcome — with a one-line fix note per
    failing category; a bare `pass`/`fail` with no category is
    incomplete. Source: plain-language readability synthesis (Flesch-
    Kincaid sentence-length research; hedge-word comprehension
    findings cross-checked against rule 16's synthesis).
28. Condition: a copy string violates one of this handbook's
    prohibitions → Choice: classify the violation before recording it
    — **block** (the string does not ship until the phrase is removed
    or replaced) or **advisory** (it may ship with the reason stated
    inline) — and default to block when the violation is not
    classified. Source: editorial style-guide severity-tiering
    convention (rule severity distinct from a single binary pass/
    fail, applied here to this handbook's own prohibitions).

## Axis 7 — Staged single-dimension revision and element-type templates

29. Condition: editing a copy draft against more than one quality
    dimension at once (does it achieve the goal, is it short enough,
    does it read naturally, is it unambiguous) → Choice: run the
    revision as four separate sequential edit rounds — goal-fit, then
    length, then naturalness, then clarity — each round changing only
    that one dimension, instead of judging all four in a single
    read-through. A holistic single-pass edit is prone to fixing one
    dimension by breaking another (e.g. shortening a sentence into
    ambiguity) because nothing forces the dimensions apart.
30. Condition: the length round of rule 29 → Choice: apply numeric
    ceilings, not a subjective "feels long" judgment — roughly 8-14
    words per sentence and 40-60 characters per line for interface
    copy — and cite the ceiling crossed when trimming.
31. Condition: drafting copy for a recurring UI-element category
    (button, error, notification, form field) with no existing
    content_id match under rule 26 → Choice: start from that
    category's format+purpose+tone template (e.g. errors: state what
    happened, why if known, and the next action, low-humor tone) 
    rather than free-drafting; deviate from the template only with a
    stated reason. This is distinct from rule 26 — rule 26 reuses a
    specific string for a specific content_id, this rule reuses a
    starting shape for a category of element that has no matching
    string yet.

## Evidence trail (fetched sources)

- NN/G, "An Error Messages Scoring Rubric" —
  https://www.nngroup.com/articles/error-messages-scoring-rubric/
  (fetched in full; 12-criteria rubric across visibility/communication/
  efficiency dimensions — basis for rules 1, 5–10, 24, 25).
- GOV.UK Design System, error message component —
  https://design-system.service.gov.uk/components/error-message/
  (fetched in full; wording patterns, format rules, banned-word list —
  basis for rules 2, 3, 4, 6, 8, 9).
- NN/G, "Legibility, Readability, and Comprehension: Making Users Read
  Your Words" — https://www.nngroup.com/articles/legibility-readability-comprehension/
  (basis for rules 16, 18).
- UX Planet, "Confirmation dialogs: how to design dialogs without
  irritation" — https://uxplanet.org/confirmation-dialogs-how-to-design-dialogues-without-irritation-7b4cf2599956
  (basis for rules 11, 12, 15).
- Design Systems Collective, "Designing better buttons: how to handle
  destructive actions" — https://www.designsystemscollective.com/designing-better-buttons-how-to-handle-destructive-actions-d7c55eef6bdf
  (basis for rules 12, 13).
- UK Parliament Design System, "Designing forms" —
  https://designsystem.parliament.uk/how-tos/designing-forms/
  (basis for rule 14, consistent-label requirement).
- Claude Code plugin/skill ecosystem survey (issue-1199, 2026-08-14
  amendment; adoption-evidence method) — a purpose-built UX-writing
  skill (147 GitHub stars at the time of the survey, independently
  surfaced across two search angles) fetched in full — basis for
  rules 29-31 (staged single-dimension revision, per-round numeric
  ceilings, per-UI-element-type template).
- Governor of Washington, plain-language guidelines —
  https://governor.wa.gov/issues/efficient-government/plain-language/plain-language-guidelines
  (basis for rule 19).
- Tim Graf, "The UX of Empty States: Designing Moments of Nothing into
  Something Exceptional" — https://timgraf.com/ui/the-ux-of-empty-states-designing-moments-of-nothing-into-something-exceptional/
  (basis for rule 20).
- UXPin, "What Is Progressive Disclosure in UX?" —
  https://www.uxpin.com/studio/blog/what-is-progressive-disclosure/
  (basis for rules 21, 22, 23; cites Nielsen 1995 as the named
  methodology origin and reports task-completion-time/support-ticket
  empirical findings as the academic-theory layer).

- GOV.UK, "Writing for GOV.UK" content style guide —
  https://www.gov.uk/guidance/content-design/writing-for-gov-uk
  (consistency principle — basis for rule 26).
- Plain-language readability synthesis, extended (Flesch-Kincaid
  sentence-length research plus hedge-word comprehension findings) —
  basis for rule 27, applying rule 16's existing synthesis at
  per-category granularity.

## Depth note

25 rules landed in the original batch (condition + choice + source
each), 5 of them REMOVAL-category (one per axis, per issue #1174
requirement 4). A sixth axis (rules 26–28, one REMOVAL) landed
separately under issue #1199, tightening copy-inventory reuse and
severity classification rather than adding new axis coverage.
Phase-1 N for content-design was not separately re-negotiated in this
session; this count is offered as the phase-1 candidate for reviewer
spot-check, matching the technical-writing exemplar's shape (rules are
decisions, not glossary definitions) at roughly half its volume — the
remainder of the axis space (localization interplay, voice-and-tone
per product surface, notification copy) is open for a follow-up batch
under the same issue.
