---
name: design-artifact-html-demo
description: Use when building an HTML/CSS demo or no-build single-file prototype — choosing semantic elements, heading structure, and responsive/accessible defaults over generic markup.
axis: semantic-html-vs-generic-div-soup
rule_count_floor: 3
---

# Semantic HTML vs. generic div soup

Decision rules for choosing semantic elements, heading structure, and
responsive/accessible defaults over generic `<div>`/`<span>` markup
in single-file HTML/CSS demos, sourced from MDN's accessibility and
semantic-HTML guidance.

## Trigger

Apply this skill when building an HTML/CSS demo or a no-build
single-file prototype and deciding how to mark up structure and
interactive controls — page landmarks, heading levels, buttons/links,
form controls, and viewport/layout defaults — rather than reaching for
generic `<div>`/`<span>` plus ARIA/JS to reimplement native behavior.

## Procedure

1. For page-level structure, use semantic landmark elements (`header`,
   `nav`, `main`, `article`, `section`, `footer`) instead of `<div>`
   with class names standing in for structure (rule 1).
2. For the demo's title, use exactly one `<h1>`, and for subsequent
   headings, never skip a level (e.g. h1 → h2, not h1 → h3) (rule 2).
3. For anything clickable or activatable, use the native interactive
   element (`<button>`, `<a href>`, form controls paired with
   `<label>`) instead of a `<div>`/`<span>` with an onclick handler
   (rule 3, REMOVAL when replacing an existing fake control).
4. For layout, use relative units and a fluid layout as the baseline,
   and include a `<meta name="viewport">` tag even in a no-build
   single-file demo, with CSS that doesn't hard-break below common
   breakpoints (rule 4).

## Output shape

A single-file HTML/CSS demo (or equivalent prototype markup) that
uses semantic landmark elements instead of generic divs, exactly one
`<h1>` with no skipped heading levels, native interactive controls
(`<button>`, `<a href>`, labeled form controls) instead of div-based
fake controls, and a responsive baseline: a `<meta name="viewport">`
tag plus relative-unit/fluid CSS that survives common breakpoints.

## Decision rules

1. When marking up page-level structure in an HTML/CSS demo (header,
   nav, main content area, footer), use the matching semantic element
   (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`,
   `<footer>`) instead of a `<div>` distinguished only by a class
   name, because semantic elements carry built-in accessible roles
   and landmark navigation for free — this is the accessible default,
   not an optional add-on layered on afterward.
   source: MDN, "HTML: A good basis for accessibility"
   (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML):
   using semantic HTML elements appropriately gives you "a lot of
   accessibility 'for free'" because browsers expose built-in roles
   and behavior that assistive technology already understands,
   whereas generic elements expose none of that.
   counter-example: do not force a semantic landmark onto content
   that has no structural role in the page (e.g. wrapping a purely
   decorative background shape in `<section>`) just to look
   semantic — a landmark element implies "there is a named region of
   content here for a screen-reader user to jump to," and applying it
   to non-content clutters the page's landmark list instead of
   helping navigation.

2. When authoring the demo's title and section headings, use exactly
   one `<h1>` per page/demo and do not skip heading levels (e.g. no
   h1 followed directly by h3 with no h2 in between), because
   screen-reader users rely on the heading hierarchy as a navigable
   outline of the page, and a broken sequence misrepresents that
   outline even if the visual size of the skipped-to heading still
   looks right.
   source: MDN, "HTML: A good basis for accessibility"
   (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML):
   heading elements provide "sensible content structure" for
   navigation, and screen-reader users commonly jump between headings
   as a way of surveying a page, which depends on the hierarchy
   staying intact.
   counter-example: do not add an `<h2>` purely to satisfy the "no
   skipped level" rule when no natural subsection exists at that
   point — an empty or content-less heading inserted only to keep the
   numbering sequential adds a confusing, contentless stop in the
   screen-reader outline; instead restructure the content so the
   heading levels reflect real subsections.

3. REMOVAL: when a demo has a `<div onclick="...">` or
   `<span onclick="...">` standing in for a button or link, remove it
   and replace it with the native `<button>` or `<a href="...">`
   element (and pair form inputs with `<label>`), because native
   interactive elements come with built-in keyboard operability (Tab
   focus, Enter/Space activation), a correct implicit accessible
   role, and correct behavior on assistive technology — all of which
   a div-based fake control must reimplement by hand and usually gets
   only partially right.
   source: MDN, "HTML: A good basis for accessibility"
   (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML):
   using `<button>` "for something that acts like a button" gets you
   keyboard accessibility, correct semantics, and built-in styling
   for free, versus a `<div>` styled to look like a button, which
   "will require a lot of extra work" (ARIA roles, keyboard event
   handlers, focus management) to get back to parity with the native
   element.
   counter-example: do not treat this as license to wrap unrelated
   inline text in `<button>` just because it happens to trigger a
   script — if the element doesn't actually navigate or submit/toggle
   state the way a button/link/control does, forcing it into a native
   interactive tag can create a confusing or unusable control class
   for assistive tech; pick the element that matches the actual
   interaction, not just "make it native at all costs."

4. When building a no-build single-file HTML/CSS demo, include a
   `<meta name="viewport" content="width=device-width, initial-scale=1">`
   tag and use relative units / a fluid layout as the baseline instead
   of a fixed-pixel layout that assumes one viewport width, because a
   demo without a viewport meta tag and without flexible sizing will
   render at desktop scale and break or become unusable at common
   narrower breakpoints, which undermines the same accessible-by-
   default posture the semantic-markup rules establish.
   source: MDN, "HTML: A good basis for accessibility"
   (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML):
   the guidance frames accessible defaults as things that should be
   present from the start of a build rather than patched on later;
   applied to responsive behavior, a demo intended to actually be
   used/tested needs a working viewport and layout baseline, not a
   desktop-only fixed canvas, for its content and controls to remain
   reachable across devices.
   rationale: a single-file demo is still something a real person may
   open on a phone or resize in a browser window during review;
   omitting the viewport tag or hard-coding pixel widths silently
   breaks that on the most common alternate viewport rather than
   failing loudly, which is exactly the kind of default gap this
   axis exists to close.
   counter-example: do not add complex media-query breakpoint sets to
   a five-minute throwaway demo when a single fluid layout using
   relative units already survives common widths — matching the
   responsiveness effort to what the demo's own scope calls for is
   still the rule; the floor is "don't hard-break," not "build a full
   responsive design system."
