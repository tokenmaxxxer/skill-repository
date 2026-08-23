---
type: llm
criteria: >-
  Checks whether the response picks a radio button group (all four options
  visible with descriptions) over the dropdown for this 4-option
  mutually-exclusive field with ample space.
target: last_message
---
Pass only if the response chooses a radio group for the Severity field,
keeping all four options and their descriptions permanently visible for
comparison, and rejects the dropdown default. Fail if it picks a dropdown or
select for consistency/compactness, or hedges without committing to the radio
group.
