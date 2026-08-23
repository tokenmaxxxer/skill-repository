---
name: localization-pluralization-and-grammar
description: >-
  Use when a message's wording depends on a numeric placeholder, when authoring source
  plural variants, or when a target locale's grammatical gender/case could change an
  adjacent word form. Trigger on requests like "ICU MessageFormat plural", "CLDR plural
  categories", "복수형 처리 어떻게 해", "gendered string variant". Do NOT use for
  date/number/currency separator conventions (use
  localization-locale-convention-formatting).
metadata:
  axis: pluralization-and-grammar
  rule_count_floor: 10
  axes:
    - string-externalization-and-key-management
    - pluralization-and-grammar
    - locale-convention-formatting
    - text-expansion-and-layout
    - rtl-and-script-support
---

# Decision axis: pluralization & grammar rules

Checklist-axis rules.

## Trigger

Apply this skill when a message's wording changes based on a numeric
placeholder, when authoring or reviewing the source resource file's
plural variants, when a target locale's grammar (gender/case agreement)
could change an adjacent word form, or when verifying the checklist
axis's plural-rule item.

## Procedure

1. When a message's wording changes based on a numeric placeholder, use
   CLDR's plural category system via ICU MessageFormat rather than an
   if/else on the raw number (rule 1).
2. When authoring the source resource file, list all 6 CLDR plural
   variants even where the source locale only needs a subset (rule 2).
3. When a UI needs to show a count with text, branch per-locale plural
   category rather than a hardcoded suffix pattern (rule 3).
4. When a locale's plural rule set only requires a subset of
   categories, omit the unused branches for that locale's translated
   file (rule 4).
5. When a sentence's noun has grammatical gender that changes an
   adjacent word form, flag the string for a gendered-variant key and
   tag it `[Internationalization]` under MQM (rule 5).
6. When verifying the checklist axis's plural-rule item, confirm
   plural-category selection is delegated to a maintained, versioned
   CLDR-data source at runtime, never a hand-copied static table
   (rule 6).

## Output shape

A per-string plural/grammar verdict: the applicable rule number(s),
which CLDR plural categories are required or can be omitted for the
target locale, and — when a gender/case defect is found — the MQM tag
to apply.

## Rules

1. **when** a message's wording changes based on a numeric placeholder
   **choose** use CLDR's plural category system (`zero`, `one`, `two`,
   `few`, `many`, `other`) via ICU MessageFormat rather than an if/else
   on the raw number — the categories are determined by which wording
   change a numeric value triggers in that language, not by ordinary
   grammatical number.
   source: "CLDR uses six plural category tags ... The CLDR plural
   categories do not necessarily match the traditional grammatical
   categories; instead, they are determined by changes required in a
   phrase" — Unicode CLDR Plural Rules spec (https://cldr.unicode.org/index/cldr-spec/plural-rules).

2. **when** authoring the source (default-locale) resource file
   **choose** list all 6 CLDR plural variants even though English only
   needs `one`/`other` — downstream locales (e.g. Arabic, which uses
   all six; Polish, which uses `one/few/many/other`) need the slots to
   exist to be filled, and retrofitting variants after launch is more
   expensive than reserving them up front.
   source: "It is a good practice to always list all 6 variants in the
   default i18n file, even though localization teams may omit
   unnecessary variants" — locize, "i18n Pluralization: CLDR Plural
   Rules, i18next & ICU" (https://www.locize.com/blog/i18n-pluralization).

3. **when** a UI needs to show a count with text (e.g. "3 items")
   **choose** per-locale plural-category branching, never a single
   English-shaped key with a hardcoded "(s)" suffix pattern — that
   pattern only degrades gracefully for English and breaks for every
   `few`/`many`-category language.
   source: "A common mistake is creating separate translation keys for
   different quantities, an approach that doesn't scale once you
   introduce languages with more than two plural forms" — Lokalise,
   ICU message format guide.

4. **REMOVAL — when** a locale's plural rule set (per CLDR) only
   requires `one`/`other` (e.g. most Romance/Germanic languages besides
   the paucal-heavy ones) **choose** omit the unused `zero`/`two`/`few`/
   `many` branches for that locale's translated file rather than
   carrying empty or duplicate-of-`other` placeholder branches forward
   — unused branches are dead weight a translator has to skip past on
   every string.
   source: "each language uses only a subset of these categories ...
   Japanese and Chinese use only other" — locize, i18n Pluralization
   guide (as rule 2); CLDR plural-rules spec confirms per-locale subset
   membership (https://cldr.unicode.org/index/cldr-spec/plural-rules).

5. **when** a sentence's noun has grammatical gender that changes an
   adjacent adjective/article form (common in Romance/Slavic/German
   target locales) **choose** flag the string for a gendered-variant key
   rather than assuming a single translated string covers all genders —
   this is a string-external checklist finding, tag it
   `[Internationalization]` under MQM.
   source: MQM error typology's "Locale conventions" dimension covers
   locale-specific grammatical/formatting compliance separate from
   fluency — MQM Full Typology (https://themqm.org/the-mqm-full-typology/).

6. **when** verifying the checklist axis's plural-rule item **choose**
   confirm the plural-category selection is delegated to a maintained,
   versioned CLDR-data source at runtime, never a hand-copied static
   category table — CLDR's own per-locale rule data changes over time
   (e.g. its Hebrew plural rule was revised), and a hardcoded table
   silently goes stale against those updates while a data-backed library
   picks up the revision automatically.
   source: adoption evidence — the i18next ecosystem's React/Next
   bindings (react-i18next 9.9k stars, next-i18next 6.1k stars per
   GitHub Topics) ship an ICU/CLDR extension so plural-category
   evaluation stays sourced from CLDR rather than duplicated in
   application code; i18next's own issue tracker records a live CLDR
   rule revision landing in the library (i18next/i18next#1202,
   https://github.com/i18next/i18next/issues/1202).
