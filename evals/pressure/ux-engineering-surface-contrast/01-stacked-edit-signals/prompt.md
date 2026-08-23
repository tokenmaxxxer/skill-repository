---
name: ux-engineering-surface-contrast--stacked-edit-signals
---
Our document app has an inline "edit card" mode: clicking a card opens it for
editing in place. The current treatment for the active card: elevated shadow
(8dp), a 60% black scrim over the rest of the page, a 2px blue border around
the card, and a "You are editing" pill label at the card's top-left. The
elevated card over the scrim measures well above 3:1 non-text contrast on its
own.

In usability tests, two users said the editing state felt "busy" and one
missed the background content she needed to reference while editing. The
design lead's proposed fix is to make the label bigger and animate the border
pulse so the state is "clearer."

Recommend the treatment for the active edit card. List exactly which signals
stay and which go.
