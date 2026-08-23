---
name: customer-support-kcs-article-authoring
description: >-
  Use when authoring or reusing a KCS knowledge article — scoping the
  Environment field, populating Cause from a five-whys chain, writing Problem
  in requester language, or deciding reuse vs. a new article. Trigger on
  requests like "write a KB article from this ticket", "KCS 문서 만들어줘",
  "Environment field scope", "near-duplicate article or link existing". Do NOT
  use for running the root-cause chain itself (use
  customer-support-five-whys-recurring-scope).
---

# KCS article-authoring decision rules

Axis: kcs-article. Consortium for Service Innovation KCS v6 practice:
articles carry Title, Problem/Issue, Environment, Resolution, Cause —
integrating requestor, responder, and organizational perspective.
Source: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/020
and https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/020

## Trigger

Apply this skill when authoring a KCS knowledge article from a resolved
ticket: scoping an environment-specific fix, populating Cause from a
five-whys chain, writing the Problem field, deciding whether to reuse an
existing article, or trimming a Resolution field before publishing.

## Procedure

1. When a resolution only works under a specific product version, OS, or
   plan tier, add an explicit Environment field naming that scope (rule 1).
2. When an article also carries a five-whys block, populate the Cause
   field with the five-whys chain's converged answer instead of leaving
   Cause blank (rule 2).
3. Under KCS's requestor/responder/organization split, write the Problem
   field in the requester's own symptom language and keep diagnostic
   jargon out of it (rule 3).
4. When a ticket's fix is identical to an existing article's Resolution,
   reuse and link that article instead of authoring a near-duplicate
   (rule 4).
5. When drafting Resolution, cut it down to the steps that actually
   changed the outcome, deleting narrated dead-ends (rule 5).

## Output shape

One KCS article (Title, Problem, Environment, Resolution, Cause) or a
link to an existing article being reused, with Environment scoped,
Cause populated from any five-whys chain, and Resolution trimmed to the
steps that worked.

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
