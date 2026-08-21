---
name: incident-response-timeline-construction
description: Use when you need guidance on Timeline construction. Applies to the timeline-construction axis.
axis: timeline-construction
rule_count_floor: 4
---

# Timeline construction

Decision rules for the `timeline` field: what belongs in it and at what
resolution. Layer 1 (practitioner: Google SRE workbook, PagerDuty
postmortem meeting guide), layer 2 (named practice: event-vs-narrative
timeline separation), layer 3 (impact-scoping proportionality, shared
with [[severity-classification-scoping]]).

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
