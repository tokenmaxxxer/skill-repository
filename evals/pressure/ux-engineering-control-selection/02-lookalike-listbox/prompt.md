---
name: ux-engineering-control-selection--lookalike-listbox
---
Our React app needs a country selector (about 200 options) in the checkout
flow. The native select is rejected by design because it can't render flag
icons and custom typography. A teammate has already prototyped a replacement:
a styled <div> that opens a scrollable list of <div> rows on click, filters
as you type into an inner input, and closes on outside click. It looks
pixel-perfect against the mockups and shipped past visual QA. It currently
handles mouse only; the teammate says keyboard and screen-reader support "can
be a fast-follow after launch since less than 2% of our users use them."

The prototype works and the deadline is in one week. Do we ship the prototype
as-is, and if not, what specifically must change before launch?
