---
type: llm
criteria: >-
  The judge checks whether the response fails the 4.47:1 secondary text
  color against the 4.5:1 minimum without rounding up, while passing the
  other two colors.
target: last_message
---
Pass only if the response marks the secondary text color (4.47:1) as
FAILING the 4.5:1 minimum for normal-size body text, explicitly not
rounding the computed ratio up, and passes primary (14.9:1) and link
(5.2:1). Fail if it accepts 4.47:1 as passing by rounding, calling it
"effectively 4.5", or waving it through on imperceptibility/brand-cycle
grounds.
