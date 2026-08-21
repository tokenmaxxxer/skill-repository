---
name: customer-support-kcs-article-authoring
description: Use when you need guidance on KCS article-authoring decision rules.
---

# KCS article-authoring decision rules

Axis: kcs-article. Consortium for Service Innovation KCS v6 practice:
articles carry Title, Problem/Issue, Environment, Resolution, Cause —
integrating requestor, responder, and organizational perspective.
Source: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/020
and https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/020

## Rules

- When a resolution only works under a specific product version, OS, or
  plan tier, add an explicit Environment field naming that scope rather
  than stating the fix as universally applicable — a fix presented
  without environment scope will be blindly reapplied to cases where it
  does not hold. Source: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/020
- When an article also carries a five-whys block (per five-whys-scope.md),
  populate the Cause field with the five-whys chain's converged answer
  instead of leaving Cause blank while the causal reasoning sits only in
  free-form ticket notes — the KCS structure exists precisely so the
  next responder can read Cause without re-deriving it. Source:
  https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/020
- Under KCS's requestor/responder/organization split, write the Problem
  field in the requester's own symptom language (what they saw) and
  keep diagnostic jargon out of it — reserve technical framing for
  Resolution/Cause so a future requester searching by symptom can match
  the article. Source: https://library.serviceinnovation.org/Get_Help/KCS_Methodology_Help/Examples_of_KCS_Structured_Knowledge_Articles
- When a ticket's fix is identical to an existing article's Resolution,
  reuse and link that article instead of authoring a near-duplicate —
  KCS's core discipline is capture-in-the-workflow reuse, not one
  article per ticket. Source: https://en.wikipedia.org/wiki/Knowledge-centered_support
- **REMOVAL**: cut a Resolution field down to the steps that actually
  changed the outcome; delete narrated dead-ends the agent tried before
  finding the fix — KCS article structure exists to improve readability
  for the next reader, and a resolution padded with abandoned attempts
  works against that goal. Source: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/020/010
