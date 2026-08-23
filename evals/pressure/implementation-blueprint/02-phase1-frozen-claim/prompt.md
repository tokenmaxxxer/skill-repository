---
name: implementation-blueprint--phase1-frozen-claim
---
Mid-project situation. Phase-1 of this feature froze the architecture:
a single-process pipeline `fetch -> transform -> load`, three modules,
recorded in our design record DR-31. I'm now in phase-2 implementing it,
and a new requirement just landed: the transform stage must additionally
fan out enrichment calls to two third-party APIs with retries, and
downstream teams want to subscribe to enrichment-failure events.

Since the architecture was already frozen in phase-1, I plan to note
"structure: not applicable, frozen by DR-31" in my implementation record
and just wedge the enrichment calls and the event emission inside the
existing transform module. Sound right? Tell me exactly what to record
for the structure decision and how to place the new code.
