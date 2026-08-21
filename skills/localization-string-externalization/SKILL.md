---
name: localization-string-externalization
description: Use when you need guidance on Decision axis: string externalization & key management. Applies to the string-externalization-and-key-management axis.
axis: string-externalization-and-key-management
rule_count_floor: 10
axes:
  - string-externalization-and-key-management
  - pluralization-and-grammar
  - locale-convention-formatting
  - text-expansion-and-layout
  - rtl-and-script-support
---

# Decision axis: string externalization & key management

Checklist-axis rules (checklist basis: `localization/plugins/verdict-axis/checklists/locale-fitness-checklist.md`).

## Rules

1. **when** a user-facing string (including error messages, tooltips,
   placeholder text, and outbound email/notification templates) is
   found hard-coded in source rather than a resource file (.json/.po/
   .xliff/.arb/etc.) **choose** externalize it into the resource file
   before any translation work starts — do not translate in place.
   source: "All user-facing text ... must be stored outside of the
   source code" — Crowdin, "i18n Explained: Process and Tools to Use"
   (https://crowdin.com/blog/complete-i18n-guide).

2. **when** a sentence needs a variable value embedded mid-string (a
   count, a name, a date) **choose** one complete ICU MessageFormat key
   holding the whole sentence with the variable interpolated inside it,
   never string-concatenation of multiple keys around the variable.
   source: "A critical best practice is to embed variables within a
   single, complete translation key using ICU MessageFormat rather than
   concatenating multiple keys and variables ... only works for simple
   languages like English" — Lokalise, "Guide to ICU message format &
   syntax" (https://lokalise.com/blog/complete-guide-to-icu-message-format/).

3. **when** a key's translated value could plausibly be reused for a
   grammatically different sentence position (e.g. a status label reused
   as a sentence subject vs. object) **choose** split it into a separate
   key per grammatical role, since a shared key that happens to work in
   English will not hold across languages with case/gender agreement.
   source: same ICU-concatenation-pitfall finding as rule 2 (Lokalise,
   ICU message format guide).

4. **REMOVAL — when** a role or team requests a brand-new bespoke
   placeholder/interpolation syntax for a specific feature instead of
   using the project's existing ICU MessageFormat convention **choose**
   drop the bespoke syntax and route the feature through the existing
   ICU key, rather than adding a second parallel formatting mechanism —
   two coexisting interpolation syntaxes forces every locale's
   translators and every downstream tool to special-case the feature.
   source: ICU MessageFormat's stated purpose is to give one
   language-aware mechanism translators and tools can share — Phrase,
   "A Practical Guide to the ICU Message Format"
   (https://phrase.com/blog/posts/guide-to-the-icu-message-format/).

5. **when** an error/log string is genuinely developer-only (never
   rendered to an end user in any locale) **choose** leave it
   un-externalized — externalization is required only for user-facing
   strings, not internal diagnostics, so this is an N/A-checklist case
   rather than a violation.
   source: Crowdin, "i18n Explained" (as rule 1) — scope is stated as
   "user-facing text," which implicitly excludes internal-only strings.

6. **when** verifying the checklist axis's key-completeness item
   **choose** run an automated diff of the target locale's key set
   against the base-locale key set (flagging missing/extra/empty keys),
   never a manual read-through of the resource file — this is the
   design move commercial translation-management platforms center the
   whole workflow on, not an incidental feature.
   source: adoption evidence — Crowdin holds 708 customers (0.25% market
   share, 6th-ranked) vs. Lokalise's 318 customers (0.11% share,
   8th-ranked) in 6sense's Translation and Localization category
   (https://6sense.com/tech/translation-and-localization/crowdin-vs-lokalise);
   both center automated base-locale key diffing as the mechanism behind
   "software teams ... want localization integrated with developer
   workflows."

7. **when** a target locale's translated message would otherwise be
   forced to mirror the source string's sentence structure (one key,
   one slot, one fixed shape) **choose** let the target message carry
   its own structure driven by the source data (count, gender, etc.)
   rather than only reusing the source's shape with a substituted key —
   splitting the key (rule 3) is necessary but not sufficient when the
   target grammar needs a different shape than English entirely, not
   just a different key.
   source: Project Fluent's "asymmetric localization" design (spec repo
   993 stars, JS implementation 915 stars —
   https://github.com/projectfluent/fluent,
   https://github.com/mozilla-l10n) — "the developer provides ... a
   unique ID and the necessary data ... and the translator has full
   autonomy to use that data however their language requires," unlike
   formats that "force a 1-to-1 relationship between the source and the
   translation."

8. **when** a translation batch spans many keys or is split across
   multiple agents/passes **choose** extract a canonical terminology
   table (proper nouns, product names, domain terms) up front and
   inject it into every chunk's translation prompt as a hard
   constraint, before any chunk-level translation begins — terminology
   drift across chunks is a key-completeness and terminology failure
   the checklist axis cannot catch after the fact, so the constraint
   has to be structural, not a post-hoc consistency pass.

9. **when** translation work is split across chunk or batch boundaries
   **choose** give each chunk's translator a short read-only excerpt of
   the immediately adjacent chunks (not just its own chunk) so
   pronouns and entity references that span a boundary stay resolvable
   — a chunk translated in isolation from its neighbors will silently
   guess a referent's gender/number/identity instead of resolving it.
