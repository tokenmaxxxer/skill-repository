---
name: ux-engineering-service-design-frontstage-backstage-separation
description: Use when deciding whether a service action, system, or actor belongs frontstage (customer-visible), backstage (invisible support for an onstage moment, possibly performed by the same frontstage employee), or a support process (infrastructural, never customer-facing) inside an already-scoped blueprint or touchpoint map.
axis: frontstage-backstage-support-perceptibility-test
rule_count_floor: 4
---

# Frontstage / backstage / support-process separation

Decision rules for classifying a service action, system, or actor as
frontstage, backstage, or support process — sourced from the Shostack/
Bitner-Ostrom-Morgan blueprinting lineage's frontstage/backstage
distinction and NN/g's service-blueprint definition, per issue #74's
phase-1 survey (`docs/issue-74/reports/ux-engineering/survey.md`,
2026-08-22).

## Trigger

Apply this skill when deciding whether a service action, system, or
actor belongs frontstage (customer-visible), backstage (invisible
support for an onstage moment), or a support process (infrastructural,
never customer-facing) inside an already-scoped blueprint or touchpoint
map. Do not use it to construct the blueprint's layers from scratch
(that is
`ux-engineering-service-design-blueprint-construction`'s job) or for a
within-screen visual-elevation decision, which
`ux-engineering-surface-contrast` governs instead.

## Procedure

1. Apply the perceptibility test to the action: would the customer
   notice if it failed or were delayed (rule 1)?
2. When a frontstage employee also performs an action invisibly to the
   customer, classify that specific action as backstage, not frontstage
   (rule 2).
3. Distinguish Support Processes from Backstage by staff role and
   function, not by proximity to the Backstage layer (rule 3).
4. Reject "internal work" alone as a classification reason; require the
   perceptibility test's answer instead (rule 4).

## Output shape

A frontstage/backstage/support-process classification for the action
or actor in question, with the perceptibility-test answer stated as the
reason, flagging any prior classification that relied on "internal
work" or org-chart location instead.

## Decision rules

1. Classify an action as frontstage when the customer directly
   perceives it during a touchpoint (onstage employee actions plus
   physical/digital evidence), and as backstage or support process when
   the customer does not — using the perceptibility test (would the
   customer notice if this action failed or were delayed?) as the
   deciding criterion, not who performs it or which department owns it.
   source: https://www.nngroup.com/articles/service-blueprints-definition/ ,
   https://ixdf.org/literature/topics/frontstage-and-backstage
   counter-example: do not classify an action as frontstage just
   because a customer-facing employee performs it — classify by
   whether the customer perceives *that specific action*, not by the
   employee's general customer-facing role.

2. When the same frontstage employee performs an action invisibly to
   the customer (e.g. a teller updating a database after a visible
   transaction), classify that action as backstage, not frontstage —
   backstage is defined by visibility to the customer, not by which
   employee or department performs it.
   source: https://www.nngroup.com/articles/service-blueprints-definition/ ,
   https://ixdf.org/literature/topics/frontstage-and-backstage
   counter-example: do not classify all of one employee's actions
   uniformly as frontstage because most of their role is
   customer-facing — classify action by action against the
   perceptibility test.

3. Distinguish Support Processes from Backstage by staff role (Support
   Process staff never interact with customers, unlike Backstage staff
   who may still be customer-adjacent) and by function (Support
   Processes are infrastructural/enabling systems — payment rails,
   logistics, IT platforms — rather than in-the-moment task execution).
   source: https://ixdf.org/literature/topics/frontstage-and-backstage ,
   https://www.nngroup.com/articles/service-blueprints-definition/
   counter-example: do not merge a payment-processing system into the
   Backstage layer just because it sits close to a backstage employee's
   workflow — if its staff never interact with customers and it is
   infrastructural, it belongs in Support Processes, a distinct layer
   with a distinct failure-visibility profile.

4. Reject "this is internal work" alone as a reason to place an action
   backstage — the perceptibility test, not organizational location, is
   what the Line of Visibility actually encodes, and placing work
   backstage purely because it is internal is a named construction
   failure mode.
   source: https://www.nngroup.com/articles/service-blueprints-definition/ ,
   https://ixdf.org/literature/topics/frontstage-and-backstage
   counter-example: an action performed entirely by internal staff can
   still be frontstage if the customer perceives its outcome directly
   (e.g. a visible wait timer driven by an internal queueing system) —
   do not default it to backstage on "internal" grounds alone.

## Related skills

- [ux-engineering-service-design-blueprint-construction](../ux-engineering-service-design-blueprint-construction/SKILL.md) — this skill classifies individual actions once that skill's blueprint layers already exist.
- [ux-engineering-surface-contrast](../ux-engineering-surface-contrast/SKILL.md) — a visually-analogous but distinct within-screen elevation/chrome decision; this skill's frontstage/backstage line is a cross-actor visibility classification, not a visual-elevation one.
