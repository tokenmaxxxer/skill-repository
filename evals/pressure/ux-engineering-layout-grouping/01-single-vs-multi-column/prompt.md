---
name: ux-engineering-layout-grouping--single-vs-multi-column
---
We're building the "Request time off" form for our HR web app. Fields, in the
order employees fill them: leave type, start date, end date, half-day flag,
reason (short text), backup contact, manager to notify. Each answer depends on
the previous ones (end date validates against start date, half-day only applies
to a one-day range), and employees file this maybe twice a year.

Our PM wants the form to feel compact and "above the fold" on desktop, and has
proposed a 2-column grid: left column = leave type, end date, reason, manager;
right column = start date, half-day, backup contact. It fits without scrolling.

Decide the column layout for this form and specify where each field goes.
Justify the choice in one or two sentences.
