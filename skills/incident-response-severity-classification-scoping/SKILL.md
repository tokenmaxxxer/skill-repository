---
axis: severity-classification-scoping
rule_count_floor: 4
---

# Severity classification / postmortem depth scoping

Decision rules for how much postmortem depth a given incident earns
(this rulebook's `note: severity-tiered document depth` field). Layer 1
(practitioner canon: incident.io/PagerDuty/Xurrent severity playbooks),
layer 2 (named framework: SEV0-SEV5 tiering), layer 3 (impact-scoping
theory: proportionality of response cost to blast radius).

## Rules

1. When the incident is a full outage, data loss, or business-stopping
   event, classify SEV1 and require a full postmortem — full
   `impact_statement`, complete `timeline`, RCA, and tracked
   `action_items` — never an abbreviated form, because SEV1 is defined
   by business-stopping blast radius that only a full document can
   scope. source: https://pulsetic.com/glossary/incident-severity/

2. When the incident is major degradation affecting many users with no
   clean workaround, classify SEV2 and require a team-level postmortem
   (RCA + action items required, timeline may be summarized to the
   response window rather than full instrumentation-grade detail) —
   Facebook's and Xurrent's tiering both gate full RCA rigor at SEV1/2,
   not below. source: https://pulsetic.com/glossary/incident-severity/

3. When the incident is minor/partial with a workaround and affects a
   small user fraction, classify SEV3 and write summary-only
   (`impact_statement` + one-line `root_cause`, no full 5-Whys chain
   required) — postmortem is optional/summary-only at this tier because
   forcing full RCA rigor here spends investigation cost disproportionate
   to blast radius. source: https://pulsetic.com/glossary/incident-severity/

4. When classifying severity, use affected-user-count as the primary
   signal, not response effort or how loud the report was — the same
   underlying defect can be SEV3 at 1% of users and SEV1 at 50%, so
   severity (and therefore postmortem depth) tracks blast radius, not
   symptom visibility. source: https://pulsetic.com/glossary/incident-severity/

5. **REMOVAL**: when a SEV3/minor incident's draft postmortem already
   contains a full timeline reconstruction or a multi-branch RCA tree,
   strip it back to the summary-only form the tier requires — over-depth
   on a low-severity incident is not rigor, it is scoping failure that
   wastes the same investigation budget a SEV1 needs, and it invites the
   next SEV3 to also over-invest by precedent. source:
   https://pulsetic.com/glossary/incident-severity/
