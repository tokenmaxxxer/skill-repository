---
name: incident-response-blameless-language-editing
description: Use when you need guidance on Blameless language editing. Applies to the blameless-language-editing axis.
axis: blameless-language-editing
rule_count_floor: 4
---

# Blameless language editing

Decision rules for turning a draft postmortem into blameless prose
(issue-1 (c): blamelessness is documented guidance, enforced here as
concrete rewrite rules). Layer 1 (practitioner: PagerDuty blameless
postmortem docs), layer 2 (named practice: "we"-framing, system-language
over person-language), layer 3 (just-culture / human-factors framing
that treats action as reasonable given the information available at the
time).

## Rules

1. When a sentence names an individual as the actor of a mistake ("X
   didn't test the change"), rewrite to "we"-framing and system-language
   ("our process didn't require a test gate before this deploy path") —
   PagerDuty's own before/after example turns "It appears you didn't
   ensure the reliability... which caused an access failure" into "we
   missed a step in the testing to confirm access." source:
   https://postmortems.pagerduty.com/culture/blameless/

2. When a sentence contains "should have" (e.g. "the deploy should have
   been tested more thoroughly"), replace it with a process question
   ("what would have needed to be true in our process for that testing
   to happen?") — "should have" is judgment about a person's choice in
   hindsight; the process question redirects to the fixable system gap.
   source: https://belikenative.com/write-post-mortem-report-without-blame-language/

3. When describing what a responder did during the incident, write the
   observable fact only ("Sam deployed the change at 2:14 PM"), never
   the hindsight judgment ("Sam should have known better") — the first
   is falsifiable from logs, the second is opinion that has no place in
   a document meant to be read by someone not present. source:
   https://belikenative.com/write-post-mortem-report-without-blame-language/

4. When investigating what a responder did, phrase interview/timeline
   questions as "what" questions ("what did you think was happening?",
   "what did you do next?") rather than "who" questions — "what"
   questions ground the record in contributing factors; "who" questions
   invite blame framing from the first question asked. source:
   https://firehydrant.com/blog/what-are-blameless-retrospectives-do-they-work-how/

5. When a word like "mistake," "fault," or "failure to" (attributed to a
   person) appears in a draft, replace it with a neutral, measurable
   observation — stick to describing events, not assigning blame, and
   replace subjective phrases with specific, measurable observations.
   source: https://medium.com/@gkunzile/blameless-incident-postmortems-templates-rca-action-items-6905c0f8ca67

6. **REMOVAL**: when a draft contains an aside praising or crediting one
   responder's individual save ("thanks to X's quick catch, impact was
   limited"), remove the individual credit line even though it reads as
   positive — praise-by-name is still person-language, and it
   establishes the same who-did-what frame that blame language uses,
   just in the opposite valence; keep the system-level fact instead
   (e.g. "the on-call rotation's escalation path reached a responder
   within N minutes"). source: https://postmortems.pagerduty.com/culture/blameless/
