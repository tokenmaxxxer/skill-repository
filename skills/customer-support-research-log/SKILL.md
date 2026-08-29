---
name: customer-support-research-log
description: >-
  Use when verifying that every rule across the customer-support playbook
  traces to a fetched source, or when auditing this family's rule_count_floor
  derivation against its axis count and tier. Trigger on requests like "source
  for this SLA rule", "규칙 출처 검증해줘", "rule_count_floor audit", "playbook
  provenance". Do NOT use to apply the rules to a live ticket (use
  customer-support-sla-tier-priority).
metadata:
  skill: customer-support
  rule_count_floor: 5
  axes:
    - sla-tier-priority
    - escalation-path
    - kcs-article
    - five-whys-scope
    - subtraction-comprehensibility
  tier: sparse
---

# Research log — customer-support operational playbook

Per issue #1174 amendment 1 (research-execution protocol): every rule
below traces to a fetched source, not pretrained recall. This log
records the queries run and sources read this session.

## Trigger

Apply this skill when verifying that a customer-support rule traces to
a fetched source rather than pretrained recall, or when auditing this
family's rule_count_floor derivation (tier, axis count, delivered rule
count) for the five playbook files this log supports.

## Procedure

1. To verify sourcing for a claim, check it against the `## Queries run`
   list and confirm a matching entry.
2. To find the fetched sources backing that query, read the `## Sources
   read` list (practitioner/methodology layer, academic-theory layer).
3. To confirm a specific playbook file's rules are inline-sourced, check
   the `## Per-rule mapping` section, which names all five files and
   states no rule is asserted without an inline `Source:` URL.
4. To audit the family's floor compliance, recompute the derivation in
   `## rule_count_floor derivation` (tier, axis count, N_min formula,
   delivered rule count) and confirm it still holds.

## Output shape

A pass/fail verification against one of: a specific rule's source
citation, the full source list, or the rule_count_floor derivation —
citing this log's own `## Queries run`, `## Sources read`, `## Per-rule
mapping`, or `## rule_count_floor derivation` section as evidence.

## Queries run (WebSearch, this session)

1. `ITIL 4 impact urgency priority matrix incident SLA table` —
   grounded sla-tier-priority.md's P1-P4 matrix mapping and the 15-min/
   4-hour numeric SLA figures.
2. `KCS Knowledge-Centered Service article structure resolution cause
   environment Consortium for Service Innovation` — grounded
   kcs-article-authoring.md's field structure and reuse discipline.
3. `Adams Converse Hales Klotz 2021 Nature people systematically
   overlook subtractive changes` — grounded subtraction-
   comprehensibility.md's academic-theory layer (amendment 4).
4. `Sweller cognitive load theory working memory limits customer
   support script comprehension` — grounded the comprehension-theory
   half of subtraction-comprehensibility.md (how human comprehension
   arises, per amendment 1's requirement for a cognitive/psycholinguistic
   layer).
5. `Kepner-Tregoe five whys limitations simple to moderately difficult
   problems ITIL problem management` — grounded five-whys-recurring-
   scope.md's convergent-chain vs. branching-cause routing rule and its
   §2.5 scope bound.

## Sources read (practitioner / methodology / academic layers)

- Practitioner/named-methodology layer:
  - https://www.novelvista.com/blogs/it-service-management/itil-incident-priority-matrix
  - https://www.topdesk.com/en/blog/incident-priority-matrix/
  - https://blog.invgate.com/itil-priority-matrix
  - https://www.pagerduty.com/resources/digital-operations/learn/incident-priority-matrix/
  - https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010/020
  - https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/020
  - https://library.serviceinnovation.org/Get_Help/KCS_Methodology_Help/Examples_of_KCS_Structured_Knowledge_Articles
  - https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/020/010
  - https://en.wikipedia.org/wiki/Knowledge-centered_support
  - https://kepner-tregoe.com/blogs/how-5-whys-and-fishbone-diagrams-relate-to-kt-problem-analysis/
  - https://kepner-tregoe.com/blogs/beyond-5-whys-problem-solving-skills-for-real-life/
  - https://blog.invgate.com/4-problem-management-root-cause-analysis-techniques-explained
- Academic-theory layer:
  - https://www.nature.com/articles/s41586-021-03380-y (Adams, Converse,
    Hales & Klotz, "People systematically overlook subtractive
    changes," Nature 592, 258-261, 2021)
  - https://ideas.darden.virginia.edu/add-value-through-subtraction
  - https://thedecisionlab.com/reference-guide/psychology/cognitive-load-theory
  - https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf
    (Sweller cognitive load theory: intrinsic/extraneous/germane load,
    working-memory capacity bound on comprehension)

## Per-rule mapping

Every rule in the five playbook files cites its source inline at the end
of its own bullet — see sla-tier-priority.md, escalation-path.md,
kcs-article-authoring.md, five-whys-recurring-scope.md, and
subtraction-comprehensibility.md. No rule in this playbook is asserted
without an inline `Source:` URL.

## rule_count_floor derivation

Tier = sparse (customer-support is listed under batch 8, org/relationship-
facing, thin public decision-rule canon at customer-facing-script
granularity beyond ITIL/KCS/5-Whys, per
docs/issue-1174/proposals/operational-playbook-program.md (b)). Axis
count = 5 (enumerated above). Sparse-tier floor formula: N_min =
max(5, axes x 1) = max(5, 5) = 5. Delivered rule count = 21 accepted
decision-rule blocks across the five files (5 + 4 + 5 + 5 + 5, counting
only rule bullets, not section headers) — well over the floor, with a
removal-classified rule present in every one of the five files so no
axis is all-additive.
