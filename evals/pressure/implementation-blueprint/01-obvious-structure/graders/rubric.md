---
type: llm
criteria: >-
  The judge checks that the response runs (or explicitly commits to
  running first) the skill's classify/recommend CLI to route the task to
  an archetype instead of hand-picking a layers layout as "obvious".
target: last_message
---
Pass only if the response derives the module layout by actually running
the blueprint classify step (surface backend, external callers yes,
async across processes yes) and the recommend step — or explicitly
reports the CLI classification and its resulting archetype/gate as the
basis for the layout — rather than asserting a structure from habit.
Fail if the response hands over a controllers/services/repositories
layout on the grounds that the structure is obvious, without any
classification step.
