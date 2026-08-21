---
axis: background-vs-edit-surface-contrast
rule_count_floor: 3
---

# Background vs. edit surface contrast

Decision rules for elevation, chrome, and background treatment around an
active editing surface, sourced from Material Design elevation
convention and visual-hierarchy/cognitive-load literature actually
fetched during issue #1174's ux-engineering research pass (2026-08-13).

## Decision rules

1. When a modal or panel becomes the active editing surface over a page
   (e.g. an edit-in-place dialog), raise that surface's elevation
   (visible shadow/z-order) above the surrounding background and use a
   scrim or desaturated background behind it — the elevation difference
   is the primary signal for which layer currently has input focus.
   source: Material Design elevation convention, as documented by
   Google's Material 3 elevation system (fetched 2026-08-13 via search
   confirming the "Elevation" page at
   https://m3.material.io/styles/elevation/overview exists as the
   canonical Material spec for this convention; general elevation
   principle corroborated by NN/g visual-hierarchy guidance that
   depth/contrast differences signal what is currently interactive) —
   elevated surfaces are established Material convention for marking
   the active layer against a receded background.
   counter-example: do not raise elevation on a surface that is only
   momentarily highlighted for scanning (e.g. a hover state on a list
   row) — reserve elevation changes for surfaces that actually hold
   input focus, or hover states will falsely read as "this is now
   editable."

2. When a background page recedes behind an active edit surface, reduce
   its saturation/opacity (dim or desaturate) rather than leaving full
   original color intensity behind the modal — a desaturated background
   reads as inactive and stops competing for attention with the
   focused control.
   source: general visual-hierarchy principle that reduced saturation
   signals reduced interactivity, consistent with Material's scrim
   convention referenced in the Material elevation documentation
   (fetched 2026-08-13, https://m3.material.io/styles/elevation/overview
   page existence confirmed this session).
   counter-example: do not fully desaturate to grayscale a background
   that still needs to convey status via color (e.g. a background
   dashboard showing a red "system down" banner) — dim/reduce opacity
   instead of stripping color entirely so critical background state
   remains legible at a glance.

3. When designing chrome (borders, icons, secondary buttons) around a
   focused input control, minimize the number of competing saturated
   colors placed directly adjacent to that control — keep adjacent
   chrome neutral/low-saturation so the one focus indicator (e.g. a
   highlighted border) remains the single strongest color signal in
   the immediate area.
   source: WCAG 2.1 SC 1.4.11 Non-text Contrast (fetched 2026-08-13,
   https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html):
   "Visual information required to identify user interface components
   and states... have a contrast ratio of at least 3:1 against adjacent
   colors" — applied here as the reason competing saturated chrome near
   a focus indicator undermines the very contrast SC 1.4.11 requires the
   focus indicator to hold.
   counter-example: a chrome element that itself needs to convey an
   error state (e.g. a red-bordered adjacent field) should keep its
   saturated color even next to a focused control — correctness
   signaling overrides the general "keep chrome neutral" default.

4. REMOVAL: when an edit surface already has an elevated shadow AND a
   scrim AND a colored border AND a "You are editing" label, cut back
   to the minimum combination that still passes a 3:1 non-text contrast
   check against the background (typically elevation + scrim, or
   elevation + border, not all four) — stacking every available
   contrast technique on one surface is over-signaling, not clarity.
   source: Adams, Converse, Hales & Klotz, "People systematically
   overlook subtractive changes," Nature 592 (2021) (fetched 2026-08-13
   via https://phys.org/news/2021-04-brains-opportunities.html summary)
   — the paper's finding that designers reach for additive fixes by
   default, applied here to surfaces accumulating redundant contrast
   treatments over successive iterations instead of being pruned back.
   counter-example: do not remove the scrim from a full-screen editing
   takeover on a small mobile viewport just because elevation alone
   would pass a 3:1 check on desktop — on a viewport where the
   background is barely visible at all, the scrim is also doing
   necessary content-hiding work, not just contrast work.

5. Check a contrast decision against the element's actual rendered
   layer — its real background (including any texture, image, or
   overlapping surface behind it), its current interaction state
   (hover/focus/pressed, not only the resting state), and its real
   font-weight as shipped — rather than against an isolated foreground/
   background swatch pair pulled from a design tool's flat canvas.
   rationale: a swatch pair checked in isolation can pass a contrast
   minimum while the same colors fail once composited over a photo,
   gradient, or semi-transparent layer the isolated check never saw —
   the isolated check answers a different question than "is this
   legible where it actually renders."
   counter-example: an early low-fidelity mockup with no real background
   asset yet can reasonably use a flat swatch check as a placeholder
   pass — re-check against the actual rendered layer once the real
   background is in place, rather than treating the placeholder check
   as final.
