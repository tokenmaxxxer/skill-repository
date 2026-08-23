---
name: ux-engineering-color-visibility
description: >-
  Use when choosing or reviewing a color combination for text, a non-text UI component, a
  color-only distinction, or a multi-value color set. Applies to the
  color-combination-visibility axis. Trigger on requests like "text contrast ratio check",
  "colorblind safe palette", "status colors distinguishable", "색 대비 검토해줘". Do NOT use for
  elevation/scrim treatment of an active editing surface (use
  ux-engineering-surface-contrast).
metadata:
  axis: color-combination-visibility
  rule_count_floor: 3
---

# Color combination visibility

Decision rules for contrast minimums and colorblind-safe color
combinations, sourced from WCAG 2.1 success criteria fetched directly
from w3.org during issue #1174's ux-engineering research pass
(2026-08-13).

## Trigger

Apply this skill when choosing or reviewing a color combination for
text, a non-text UI component, a color-only distinction, or a
multi-value color set — distinguishing it from control-selection
(which widget to use), layout-grouping (spatial arrangement), and
surface-contrast (elevation/chrome around an active edit surface).

## Procedure

1. For normal-size body text on a background, require at least 4.5:1
   contrast, unrounded (rule 1).
2. For large-scale text, require at least 3:1 contrast (rule 2).
3. For a non-text UI component's visible boundary or state indicator,
   require at least 3:1 contrast against its adjacent background
   unless the component is inactive (rule 3).
4. For any UI distinction currently conveyed only through hue, add a
   second non-color signal (rule 4).
5. For a distinguishable multi-value color set, vary lightness/
   luminance between adjacent hues, not hue rotation alone (rule 5).
6. REMOVAL: when a status system has accumulated more colors than can
   be told apart at the 3:1 minimum and a colorblind-safe distance,
   consolidate the palette rather than layering on more non-color cues
   (rule 6).
7. Route a color value through one source-of-truth layer shared by
   design and code rather than a hard-coded literal (rule 7).
8. When defining a new color token or palette, default to a
   wide-gamut, perceptually-uniform color space and derive steps
   systematically rather than hand-picking each one (rule 8).

## Output shape

A pass/fail contrast verdict per checked pair or component state, plus
— where a rule fires — a concrete remediation: an added non-color
signal, a consolidated palette, a routed color token, or a
derived-palette recommendation.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When normal-size body text (below 18pt, or below 14pt bold) is placed on a background color, pick a foreground/background pair with a contrast ratio of at least 4.5:1; d…
- 1.2 — When text is large-scale (at least 18pt, or 14pt bold and larger), pick a foreground/background pair with a contrast ratio of at least 3:1 — the relaxed threshold applie…
- 1.3 — When designing a non-text UI component's visible boundary or state indicator (e.g. a checkbox outline, a toggle's on-state fill, an input field's focus ring) against its…
- 1.4 — When a UI distinction (error vs. success, selected vs. unselected, category A vs. category B) is currently conveyed only through hue (e.g. red vs. green), add a second,…
- 1.5 — When choosing a distinguishable multi-value color set (e.g. a chart legend, category tags), vary lightness/luminance between adjacent hues in addition to hue itself, rat…
- 1.6 — REMOVAL: when a status system has accumulated more distinct status colors than can be told apart at both the 3:1 non-text-contrast minimum and a colorblind-safe distance…
- 1.7 — A color value is only safe to reuse across a design surface and its shipped code once it resolves through one source-of-truth layer read by both sides; flag any color de…
- 1.8 — When defining a new color token or a derived palette, default to a wide-gamut, perceptually-uniform color space (e.g. OKLCH) over sRGB hex, and prefer deriving a full pa…
