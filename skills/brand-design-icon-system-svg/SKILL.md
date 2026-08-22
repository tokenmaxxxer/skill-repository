---
name: brand-design-icon-system-svg
description: Use when drawing or reviewing an icon for an SVG icon system, sizing an icon to a keyline grid, deciding an icon's color/viewBox/aria attributes, or checking an icon's pixel-fitting at its target render size.
axis: icon-system-svg
rule_count_floor: 5
globs:
  - "**/*.svg"
---

# SVG icon system rules

## Trigger

Apply this skill when authoring a new icon for a shared icon set,
reviewing an icon PR for grid/stroke consistency, deciding how an icon
SVG should expose color and sizing to its consumer, or checking whether
an icon reads cleanly at its actual rendered pixel size.

## Procedure

1. Draw every icon on the same keyline grid (Material uses 24x24) and
   align major shapes to its keylines, not freehand at arbitrary
   coordinates (rule 1).
2. Use one consistent stroke weight across the whole icon set, never
   mixed per-icon (rule 2).
3. Expose color via `currentColor`, and size via `viewBox` with no
   hardcoded `width`/`height` on the root SVG (rule 3).
4. Mark a purely decorative icon `aria-hidden="true"`; give a
   meaningful icon-only control an accessible name instead (rule 4).
5. Nudge vector points to fall on whole pixels at the icon's actual
   target render size before shipping (rule 5).

## Output shape

An icon SVG (or review verdict) stating: grid/keyline conformance,
stroke-weight consistency with the set, `currentColor`+`viewBox` usage
with no hardcoded dimensions, the `aria-hidden`/accessible-name
decision, and pixel-fitting at target size — each traceable to the
rule below that forced the choice.

## Rules

1. Draw every icon in a set on the same keyline grid (Material's system
   uses a 24x24dp grid with defined keyline shapes — circle, square,
   rectangles) and align each icon's major forms to those keylines
   rather than placing shapes at arbitrary freehand coordinates — a
   shared grid is what makes icons in the same row read as visually
   consistent in size and optical weight, even though their literal
   silhouettes differ (a circle vs. a square icon are still both drawn
   to fill the same keyline area). source: https://m3.material.io/styles/icons/designing-icons

2. Use one consistent stroke weight for every icon in the set (Shopify
   Polaris specifies a fixed stroke width for its icon system) — never
   let individual icons carry their own stroke weight, since mixed
   weights within one UI read as visually inconsistent even when each
   icon looks fine in isolation. source: https://polaris.shopify.com/icons

3. Author the icon's SVG root with a `viewBox` attribute and no
   hardcoded `width`/`height`, and use `fill="currentColor"` (or
   `stroke="currentColor"` for stroke-based icons) instead of a
   hardcoded hex color — `viewBox`-only sizing lets the consumer scale
   the icon via CSS/font-size-relative units without distortion, and
   `currentColor` lets the icon inherit its color from CSS context
   (theming, hover states, dark mode) instead of requiring per-instance
   overrides. source: https://m3.material.io/styles/icons/designing-icons

4. For a purely decorative icon (one accompanied by adjacent visible
   text that already conveys its meaning), mark it `aria-hidden="true"`
   so assistive technology skips it; for an icon-only interactive
   control with no adjacent text, give the control itself an accessible
   name (`aria-label` on the button/link, not on the icon) — an icon
   left unmarked either way forces AT to guess whether it is
   decorative or meaningful. source: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html

5. Before shipping, check the icon at its actual target render size(s)
   (commonly 16px/24px) and nudge vector points onto whole pixel values
   where the design allows — an SVG drawn cleanly at large size can
   still render with blurry or uneven strokes at small sizes if its
   paths don't land on pixel boundaries once scaled; WCAG 1.4.11
   requires non-text UI components (including icons conveying meaning
   or state) to meet a 3:1 contrast ratio against adjacent colors at
   their actual rendered size, so pixel-fitting and contrast both need
   verification at the real target size, not just at the source
   artboard size. source: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

## Sources

- https://m3.material.io/styles/icons/designing-icons
- https://polaris.shopify.com/icons
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
