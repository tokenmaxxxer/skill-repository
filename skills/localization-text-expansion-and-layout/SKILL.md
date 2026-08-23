---
name: localization-text-expansion-and-layout
description: >-
  Use when laying out a fixed-width UI element that will carry translated text, budgeting a
  per-locale character limit, or a container/source string risks breaking under text
  expansion. Trigger on requests like "German text overflow", "label character budget per
  locale", "번역하면 버튼 텍스트 넘칠 것 같아", "width headroom for localization". Do NOT use for
  mirroring layout or icons for right-to-left scripts (use
  localization-rtl-and-script-support).
metadata:
  axis: text-expansion-and-layout
  rule_count_floor: 10
  axes:
    - string-externalization-and-key-management
    - pluralization-and-grammar
    - locale-convention-formatting
    - text-expansion-and-layout
    - rtl-and-script-support
---

# Decision axis: text expansion & layout

Style-guide axis rules.

## Trigger

Apply this skill when laying out a fixed-width UI element that will
carry translated text, when budgeting a character limit for a
translated label, when a container is implemented as a fixed
pixel-fit width, or when a source string is padded with content-free
filler.

## Procedure

1. When laying out a fixed-width UI element, reserve ~30-40% extra
   width headroom beyond the English source string's natural width
   (rule 1).
2. When budgeting a character limit for a short UI label, size the
   German variant at roughly 60-70% and the French variant at roughly
   80-85% of the English character count rather than reusing the
   English cap unchanged (rule 2).
3. When a container's width is a fixed pixel/point value that only
   just fits the English source string, flag it as a checklist-axis
   N/A-blocking finding and require a responsive/elastic container
   before translation lands (rule 3).
4. When an English source string is wordy or redundant with no
   functional content beyond its literal words, flag it for content
   design's copy pass to shorten before translation rather than
   translating the padding into every locale (rule 4).
5. When a menu header or short label is translated into German, budget
   roughly 60% of the English character allowance rather than treating
   short and long strings as having the same expansion ratio (rule 5).

## Output shape

A per-element expansion/layout verdict: the applicable rule number(s),
the width-headroom or per-locale character-budget figure to apply, and
— when a fixed-width container or padded source string is found — the
specific fix required before translation lands.

## Rules

1. **when** laying out a fixed-width UI element (button, menu item, form
   label) that will carry translated text **choose** reserve ~30-40%
   extra width headroom beyond the English source string's natural
   width, not a pixel-exact fit to the English string.
   source: "When you proactively design with additional space, ideally
   around 30-40% for potential expansion, UI components can more easily
   accommodate various language needs" — Crowdin, "Advanced UI
   Localization Guide" (https://crowdin.com/blog/best-practices-for-ui-localization).

2. **when** budgeting a character limit for a short UI label translated
   into German or French **choose** size the German variant's limit at
   roughly 60-70% of the English character count and the French variant
   at roughly 80-85% (i.e. expect German to run longest, French
   moderately longer than English) rather than reusing the English
   character cap unchanged for either.
   source: "German text can require up to 70% more space than English
   ... For button labels (2-3 words), German typically expands by
   30-40% ... French typically expands by 20-35% ... For button labels
   (2-3 words), French expands by 20-25%" — POEditor/intlpull text-
   expansion synthesis (https://intlpull.com/blog/ui-localization-technical-guide-2026,
   https://poeditor.com/blog/text-expansion-and-contraction-localization/).

3. **when** a container's width is implemented as a fixed pixel/point
   value that only just fits the English source string **choose** flag
   it as a checklist-axis N/A-blocking finding (layout will break for
   German-class expansion) and require conversion to a
   responsive/elastic container before translation lands.
   source: "Avoid fixed-width containers and embrace responsive, elastic
   layouts that can accommodate varying language needs" — Crowdin, UI
   Localization Guide (as rule 1).

4. **REMOVAL — when** an English source string is a wordy or redundant
   construction with no functional content beyond its literal words
   (e.g. filler phrasing that exists only because English idiom allows
   it) **choose** flag it for content-design's copy pass to shorten the
   source before translation, rather than translating the padding into
   every locale and inheriting a multiplied expansion cost per language
   — this is a hand-off, not a localization-side rewrite, per this
   role's own fluency-rewrite boundary.
   source: derived from the text-expansion multiplication finding
   itself (rule 2 sources: German ~70% max expansion) — a shorter
   source string reduces every locale's absolute expansion budget
   simultaneously, so removing unnecessary source-copy bulk is the
   highest-leverage expansion-risk reduction available at this axis.

5. **when** a menu header or short label is translated into German
   **choose** budget roughly 60% of the English character allowance
   (e.g. English 10 chars -> German ~6) rather than treating menu
   headers and full sentences as having the same expansion ratio —
   short strings expand proportionally more than long ones.
   source: "Menu headers (English limit 10) -> German limit 6, French
   limit 8" — intlpull, "UI Translation & Localization Guide"
   (https://intlpull.com/blog/ui-localization-technical-guide-2026).
