---
name: ux-engineering-surface-contrast--swatch-vs-rendered
---
Our travel app's trip page has a hero photo header (user-uploaded photos, any
brightness). An "Edit trip details" panel slides over the lower half of the
hero when activated. The design file specifies the panel as white (#FFFFFF)
with a #1A1A1A title and a #6B7280 focus-ring alternative; the designer ran
the pairs through a contrast checker: title on panel 16.7:1, focus ring on
panel 4.6:1 — both pass. The panel itself is 85% opaque so the photo shows
through slightly, and the focus ring also overlaps the photo edge at the
panel's boundary. QA asks whether the contrast work is done so they can close
the accessibility ticket.

Is the contrast verification sufficient to close the ticket? Answer yes or no
and state what, if anything, remains.
