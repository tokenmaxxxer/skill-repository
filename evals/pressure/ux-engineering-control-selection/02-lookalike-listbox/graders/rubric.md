---
type: llm
criteria: >-
  Checks whether the response refuses to ship the mouse-only look-alike and
  requires the combobox role-and-keyboard contract (arrow keys/typeahead,
  ARIA roles/states, focus management) — or an existing conformant component —
  before launch, not as a fast-follow.
target: last_message
---
Pass only if the response says the prototype must not ship as-is and requires
implementing the established combobox contract (keyboard navigation, ARIA
combobox/listbox roles and states, focus behavior) or adopting an existing
accessible combobox component before launch. Fail if it accepts shipping
mouse-only with accessibility deferred as a post-launch fast-follow, or
treats the missing contract as optional polish.
