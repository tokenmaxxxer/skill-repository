# launch-readiness — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] The hard rule that makes this a review and not a vibe check

Every item in every checklist area below must produce a **binary yes/no**, and a "yes" is
only valid if it points to a **verifiable artifact** — a config, a dashboard URL, a runbook
document, a test/dry-run record, a named person in an on-call roster. "We have monitoring,"
"we have a rollback plan," "the team is aware" with nothing linkable is a FAIL, not a pass,
no matter how confident the claim sounds. If you can't produce or point to the artifact right
now, the item is a no.

## [S2] Evidence grade (read before presenting this as more than it is)

- **What's solid:** the checklist's lineage is primary-source confirmed. Google's Launch
  Coordination Checklist traces to roughly 2005; the Launch Coordination Engineering team
  that owns it formalized in 2004 from an informal volunteer group into a dedicated SRE
  team; canary deployment and staged rollout are proceduralized as required checklist items
  in that same lineage. That's a real, traceable origin for the structure above.
- **What's thin:** comparative effectiveness studies — evidence that running this kind of
  review measurably reduces incidents or improves launch outcomes versus not running one —
  are thin to absent in the current research base. This skill encodes a documented,
  industry-origin procedure, not an RCT-validated intervention. Say so if asked how well
  proven this is; don't imply a controlled study backs the outcome.
- **Do not cite as validation:** the DORA four keys (deployment frequency, lead time, change
  failure rate, MTTR) and the Accelerate research program. Their evidentiary status is
  unresolved — the underlying survey-construct-validity critique was collected but never
  reached a verified conclusion — so they are not a basis for claiming this procedure
  "works." If someone reaches for DORA/Accelerate to justify this checklist, redirect to the
  primary-source LCE lineage above instead.
- **Practical read:** use this because it is a well-specified, artifact-forcing discipline
  with a real incident-prevention pedigree — not because a controlled experiment proved it
  moves outcome metrics.

