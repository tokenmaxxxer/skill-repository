---
name: ux-engineering-color-visibility
description: Use when you need guidance on Color combination visibility. Applies to the color-combination-visibility axis.
axis: color-combination-visibility
rule_count_floor: 3
---

# Color combination visibility

Decision rules for contrast minimums and colorblind-safe color
combinations, sourced from WCAG 2.1 success criteria fetched directly
from w3.org during issue #1174's ux-engineering research pass
(2026-08-13).

## Decision rules

1. When normal-size body text (below 18pt, or below 14pt bold) is
   placed on a background color, pick a foreground/background pair with
   a contrast ratio of at least 4.5:1; do not round a computed ratio
   up to reach the threshold.
   source: WCAG 2.1 SC 1.4.3 Contrast (Minimum) (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html):
   "The visual presentation of text and images of text has a contrast
   ratio of at least 4.5:1" and "computed values should not be rounded
   (e.g., 4.499:1 fails the 4.5:1 requirement)."
   counter-example: pure decorative text that conveys no information
   (e.g. a background watermark) is exempt from the 4.5:1 minimum per
   the same SC's own "Incidental" exception — do not apply the ratio
   requirement to text that carries no informational content.

2. When text is large-scale (at least 18pt, or 14pt bold and larger),
   pick a foreground/background pair with a contrast ratio of at least
   3:1 — the relaxed threshold applies specifically to large text, not
   to normal text set in a bold weight below 14pt.
   source: WCAG 2.1 SC 1.4.3 Contrast (Minimum) (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html):
   "Large Text: Large-scale text and images of large-scale text have a
   contrast ratio of at least 3:1."
   counter-example: do not apply the 3:1 large-text threshold to a
   14pt-bold label that a CJK locale renders at an equivalent-weight but
   visually smaller glyph size — check actual rendered size per locale,
   not just the nominal point size and weight.

3. When designing a non-text UI component's visible boundary or state
   indicator (e.g. a checkbox outline, a toggle's on-state fill, an
   input field's focus ring) against its adjacent background, pick
   colors with at least a 3:1 contrast ratio against that adjacent
   color — an inactive component is exempt, but any interactive,
   currently-usable component is not.
   source: WCAG 2.1 SC 1.4.11 Non-text Contrast (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html):
   "Visual information required to identify user interface components
   and states... have a contrast ratio of at least 3:1 against adjacent
   color(s)... except for inactive components."
   counter-example: a disabled/inactive form control that is
   intentionally low-contrast to signal "not currently usable" is
   correctly exempt under SC 1.4.11's own inactive-component exception —
   do not force full 3:1 contrast onto disabled-state styling.

4. When a UI distinction (error vs. success, selected vs. unselected,
   category A vs. category B) is currently conveyed only through hue
   (e.g. red vs. green), add a second, non-color signal — an icon,
   text label, pattern, or shape — so the distinction survives for
   colorblind users; do not rely on hue alone even if the hue pair has
   adequate contrast against the background.
   source: WCAG 2.1 SC 1.4.1 Use of Color (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html):
   "Color is not used as the only visual means of conveying
   information, indicating an action, prompting a response, or
   distinguishing a visual element" — with acceptable supplements
   listed as "text labels or cues," "icons or symbols," and "patterns
   or shapes."
   counter-example: a color swatch picker whose entire purpose is
   letting the user choose a color is inherently color-only and does
   not need a redundant label per swatch — SC 1.4.1 targets color used
   to convey non-color information, not tools whose subject is color
   itself.

5. When choosing a distinguishable multi-value color set (e.g. a chart
   legend, category tags), vary lightness/luminance between adjacent
   hues in addition to hue itself, rather than relying on hue rotation
   at constant lightness — red-green-only distinctions specifically
   fail for the most common form of color vision deficiency even when
   the two hues are technically "different colors."
   source: WCAG 2.1 SC 1.4.1 Use of Color (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)
   acceptable-supplement guidance naming "sufficient contrast ratios
   (3:1 or greater when combining hue with lightness differences)" as
   one of the ways to keep a color-based distinction legible.
   counter-example: do not vary lightness so far between two category
   colors that one reads as "highlighted/active" and the other as
   "dimmed/inactive" when both categories are meant to carry equal
   importance — large lightness gaps introduce an unintended hierarchy
   signal.

6. REMOVAL: when a status system has accumulated more distinct status
   colors than can be told apart at both the 3:1 non-text-contrast
   minimum and a colorblind-safe distance from each other (commonly
   past 5-6 simultaneous status hues), cut the palette down rather than
   adding yet another non-color cue to prop up an overloaded color set —
   consolidate rarely-distinguished statuses into fewer visually
   distinct buckets instead of layering more icons/patterns onto a
   palette that is fundamentally too large to read at a glance.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021) (fetched 2026-08-13
   via https://phys.org/news/2021-04-brains-opportunities.html summary)
   — the paper's finding that people default to additive fixes (add one
   more icon, one more pattern) over subtractive ones (cut the number of
   statuses), applied to color-system sprawl.
   counter-example: do not merge two statuses that are operationally
   distinct just to shrink the palette (e.g. "failed" and "cancelled"
   read similarly but drive different downstream actions) —
   consolidate only where the underlying states are genuinely
   redundant, not wherever the color count is inconvenient.

7. A color value is only safe to reuse across a design surface and its
   shipped code once it resolves through one source-of-truth layer read
   by both sides; flag any color decision that hard-codes a literal
   value bypassing that layer, even when the hard-coded value happens
   to match the intended color today.
   rationale: a color that exists in two places (a design file's fill
   and a stylesheet's literal) drifts the moment either side changes
   independently — neither side can tell it has drifted until a visual
   diff catches it, by which point the mismatch has usually already
   shipped.
   counter-example: a one-off illustration or marketing asset with no
   reused semantic meaning (not a token candidate) does not need to
   route through the shared layer — the rule targets colors that carry
   a reusable design decision, not incidental art.

8. When defining a new color token or a derived palette, default to a
   wide-gamut, perceptually-uniform color space (e.g. OKLCH) over sRGB
   hex, and prefer deriving a full palette from a single hue variable
   plus systematic lightness/chroma steps over hand-picking each step
   independently.
   rationale: a perceptually-uniform space keeps equal numeric steps
   reading as equal visual steps, so a palette generated from one
   derived hue stays consistent across light/dark and across the full
   ramp; hex-based hand-picked steps drift unevenly and require
   re-eyeballing every time the palette is extended.
   counter-example: a token whose value is fixed by an external brand
   guideline or a legally mandated color (e.g. a safety-signal red) is
   not a candidate for derivation — record it as its exact specified
   value rather than approximating it from a derived ramp.
