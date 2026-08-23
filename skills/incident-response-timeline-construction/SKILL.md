---
name: incident-response-timeline-construction
description: >-
  Use when building or reviewing an incident postmortem's timeline field —
  what events to log, at what resolution, and how to verify them. Applies to
  the timeline-construction axis. Trigger on requests like "build the incident
  timeline", "timestamped detection vs mitigation events", "cross-check
  responder memories against logs", "장애 타임라인 정리해줘". Do NOT use for how the
  entries are worded once chosen (use
  incident-response-blameless-language-editing).
metadata:
  axis: timeline-construction
  rule_count_floor: 4

---

# Timeline construction

Decision rules for the `timeline` field: what belongs in it and at what
resolution. Layer 1 (practitioner: Google SRE workbook, PagerDuty
postmortem meeting guide), layer 2 (named practice: event-vs-narrative
timeline separation), layer 3 (impact-scoping proportionality, shared
with [[severity-classification-scoping]]).

## Trigger

Apply this skill when building or reviewing a postmortem's `timeline`
field — deciding what events belong in it, at what resolution, tagging
detection versus mitigation steps, cross-checking responder memories, or
compressing it for a lower-severity incident — distinguishing it from
blameless-language-editing (how those entries are worded once chosen).

## Procedure

1. Log timestamped, falsifiable events rather than narrative summary
   sentences (rule 1).
2. Tag detection/escalation steps distinctly from mitigation/remediation
   steps (rule 2).
3. Cross-check entries gathered from multiple responders' memories
   against an objective source before entering them (rule 3).
4. When the incident is SEV3/minor, compress the timeline to the
   detection-to-mitigation window only (rule 4).
5. When a draft entry restates the narrative summary instead of a
   discrete event, delete it (rule 5).

## Output shape

A timeline of timestamped, falsifiable, source-verified events, tagged
detection-vs-mitigation, scoped to full pre-incident reconstruction or
compressed to the detection-to-mitigation window per the incident's
severity tier.

## Rules

1. When building the timeline, log timestamped, falsifiable events
   (deploy at 2:14 PM, alert fired at 2:16 PM, mitigation applied at
   2:31 PM) rather than narrative summary sentences — an entry must be
   independently checkable against logs/dashboards by a reader who was
   not present, the same standard the action-item gate applies to
   action items. source: https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

2. When an event in the timeline is a detection or escalation step
   (alert fired, page acknowledged, second responder paged), tag it
   distinctly from mitigation/remediation steps — separating
   detection-phase events from fix-phase events is what lets the second
   5-Whys chain in [[rca-method-selection]] (rule 2) be built directly
   from the timeline instead of reconstructed later.
   source: https://sre.google/workbook/postmortem-analysis/

3. When timeline entries are gathered from multiple responders'
   memories, cross-check each against an objective source (chat log
   timestamp, deploy log, monitoring graph) before entering it — a
   memory-only timestamp is a guess, not a fact, and blameless framing
   depends on fact-only timeline entries per [[blameless-language-editing]]
   (rule 3, observable-fact standard).
   source: https://belikenative.com/write-post-mortem-report-without-blame-language/

4. When the incident is SEV3/minor, compress the timeline to the
   detection-to-mitigation window only rather than reconstructing every
   preceding minor signal — full pre-incident timeline reconstruction is
   SEV1/2-depth work; applying it to a SEV3 duplicates the over-depth
   failure [[severity-classification-scoping]] rule 5 already flags.
   source: https://pulsetic.com/glossary/incident-severity/

5. **REMOVAL**: when a draft timeline entry restates the postmortem's
   own narrative summary instead of a discrete event ("team continued to
   investigate the root cause"), delete it — a non-event entry adds rows
   without adding checkable information, the same defect this program's
   depth gate rejects when a playbook rule reads like a definition
   instead of a decision. source: https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

## Related skills

- [incident-response-rca-method-selection](../incident-response-rca-method-selection/SKILL.md) — a constructed timeline is the input rca-method-selection reasons over to pick a root-cause method.
