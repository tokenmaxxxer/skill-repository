---
axis: tool-landscape
rule_count_floor: 4
---

# Tool-landscape learnings

Distilled design moves from the incident-management/postmortem tool
ecosystem this role's practitioners actually use (issue #1199,
northpole req#1/req#5), folded into this role's own decision axes —
never a tool catalog. Adoption-evidence citations (stars, reported
customer counts, acquisition/market signal, multi-source comparison
mentions) are in `docs/issue-1199/reports/incident-response/scout-brief.md`
in the `on-the-record` repo; this file states only the design move and
which existing axis it upgrades.

## Rules

1. When building the `timeline` field, capture events into it AS the
   incident unfolds (paste/export from the live incident channel at
   record time) rather than reconstructing from memory after the
   incident closes — this is the capture-timing discipline that makes
   [[timeline-construction]] rule 1's falsifiable-event standard
   actually achievable, the design move behind Rootly's and incident.io's
   auto-timeline-capture-from-chat feature.

2. When classifying an incident SEV1 or SEV2, name the escalation-chain
   shape (who gets paged, in what order) as part of the severity
   classification itself, not a separate concern left to whichever
   paging tool happens to be configured — PagerDuty's and Opsgenie's
   core design move is that severity drives escalation-chain routing,
   not a flat notify-everyone default. Upgrades
   [[severity-classification-scoping]], currently silent on who gets
   paged and scoped only to document depth.

3. When drafting an action item, treat a missing owner, verb, outcome,
   or deadline as a BLOCKING gap that stops the item from entering the
   tracked list at all, not an advisory shape check applied after the
   fact — mirrors how the surveyed postmortem tools structurally refuse
   to create an action item without those fields. Upgrades
   [[action-item-quality]] rule 1 from advisory framing to blocking
   framing, matching this role's own
   `incident-response-action-item-gate`'s mechanical enforcement instead
   of merely restating it in prose.

4. When the org already tracks the live incident somewhere (an issue,
   a channel, a paging event), link the postmortem's timeline/impact
   sections to that live record instead of re-typing its content —
   Upptime collapses the incident record and the public communication
   artifact into the same GitHub Issue rather than hand-copying between
   a postmortem doc and a status page. Upgrades
   [[timeline-construction]] and [[blameless-language-editing]], both of
   which currently assume the postmortem doc is authored from scratch.

5. **REMOVAL**: when a postmortem draft re-types timeline or impact
   content that already exists verbatim in a linked incident channel,
   paging event, or tracking issue, delete the re-typed copy and replace
   it with a link/reference to the live record — hand-copied duplicate
   content drifts from its source the moment either one is edited, the
   same failure mode rule 4's link-don't-duplicate move exists to
   prevent.
