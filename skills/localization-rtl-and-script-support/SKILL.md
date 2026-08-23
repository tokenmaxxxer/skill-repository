---
name: localization-rtl-and-script-support
description: >-
  Use when a target locale uses a right-to-left script, when deciding whether an icon or
  directional CSS property needs mirroring, or when a locale pair has no RTL/bidi
  requirement to check. Trigger on requests like "RTL support for Arabic", "should this icon
  mirror", "아랍어 레이아웃 미러링 해줘", "CSS logical properties for dir=rtl". Do NOT use for width
  headroom or character budgets for translated text (use
  localization-text-expansion-and-layout).
metadata:
  axis: rtl-and-script-support
  rule_count_floor: 10
  axes:
    - string-externalization-and-key-management
    - pluralization-and-grammar
    - locale-convention-formatting
    - text-expansion-and-layout
    - rtl-and-script-support
---

# Decision axis: RTL & script/encoding support

Checklist-axis rules (encoding / script-fitness).

## Trigger

Apply this skill when a target locale uses a right-to-left script, when
deciding whether an icon or a directional CSS property needs mirroring,
when a mirrorable character appears in RTL-resolved text, or when a
locale pair has no RTL/bidi requirement to check.

## Procedure

1. When a target locale uses a right-to-left script, set `dir` at the
   document/root level and build layout with CSS logical properties,
   never physical-direction properties (rule 1).
2. When deciding whether an icon needs mirroring for RTL, mirror only
   directional icons and leave non-directional icons unmirrored
   (rule 2).
3. When a mirrorable character (per Unicode Bidi_Mirrored) appears in
   RTL-resolved text, trust the Unicode Bidirectional Algorithm's
   automatic glyph substitution rather than hand-authoring a mirrored
   variant (rule 3).
4. When a component uses a directional `box-shadow`/`text-shadow`/
   `linear-gradient` offset, flag it as a separate manual-flip
   requirement rather than assuming logical properties already handled
   it (rule 4).
5. When a locale pair has no dedicated RTL/bidi requirement, mark the
   RTL axis N/A for that pair rather than running the mirroring
   checklist (rule 5).

## Output shape

A per-component RTL/script verdict: the applicable rule number(s),
whether `dir`/logical-property coverage is complete, which icons or
directional CSS properties still need a manual flip, and an N/A marker
when the locale pair has no RTL requirement.

## Rules

1. **when** a target locale uses a right-to-left script (Arabic,
   Hebrew, etc.) **choose** set `dir` at the document/root level and
   build layout with CSS logical properties (`margin-inline-start`,
   not `margin-left`), never physical-direction properties, so the
   whole layout mirrors from one flag instead of per-component patches.
   source: "The foundation is dir on <html>, CSS logical properties
   throughout, and direction-aware handling of icons, animations, and
   form fields" — SimpleLocalize, "RTL design guide for developers"
   (https://simplelocalize.io/blog/posts/rtl-design-guide-developers/).

2. **when** deciding whether an icon needs mirroring for RTL **choose**
   mirror only *directional* icons (back/forward arrows, progress
   indicators) and leave *non-directional* icons (X/close, bookmark
   star, any icon depicting code, which stays LTR by convention)
   unmirrored — mirroring every icon uniformly is itself a defect.
   source: "the general rule is that directional elements mirror while
   non-directional elements don't ... icons related to code (which is
   always LTR), don't need mirroring" — LinkedIn/SimpleLocalize RTL
   guidance synthesis (https://simplelocalize.io/blog/posts/rtl-design-guide-developers/).

3. **when** a character is mirrorable per the Unicode Bidi_Mirrored
   property (e.g. parentheses, brackets) and appears in RTL-resolved
   text **choose** trust the Unicode Bidirectional Algorithm's automatic
   glyph substitution rather than hand-authoring a mirrored variant of
   the string — the mirroring is a rendering-layer property of the
   character, not a translation-content decision.
   source: "a character is depicted by a mirrored glyph if and only if
   (a) the resolved directionality of that character is R ... and (b)
   the Bidi_Mirrored property value of that character is Yes" — Unicode
   UAX #9, Unicode Bidirectional Algorithm (https://unicode.org/reports/tr9/).

4. **REMOVAL — when** a component uses `box-shadow`, `text-shadow`, or
   `linear-gradient` with a directional offset/angle tuned for LTR
   **choose** do not assume CSS logical properties already handled it —
   flag it explicitly as a separate manual-flip requirement and remove
   any reliance on the logical-properties migration alone covering it,
   since these properties stay physical and do not auto-mirror.
   source: "Shadows and gradients do not auto-flip; CSS logical
   properties mirror layout, but box-shadow, text-shadow, and
   linear-gradient offsets/angles are physical and stay fixed when
   direction flips" — SimpleLocalize, RTL design guide (as rule 1).

5. **when** a source/target locale pair covers a language with no
   dedicated public RTL/bidi requirement (the overwhelming majority of
   LTR-to-LTR locale pairs) **choose** mark the RTL axis N/A for that
   pair rather than running the mirroring checklist — this axis only
   applies when the target locale's script direction differs from the
   source's.
   source: derived from UAX #9's own scope statement — the algorithm
   activates only when mixed/RTL-resolved directionality is present in
   the text (https://unicode.org/reports/tr9/); no RTL-resolved text
   means no bidi mirroring decision to make.
