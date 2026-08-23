---
name: pr-communications-message-planning-and-evaluation-rules
description: >-
  Use when planning, drafting, clearing, or evaluating an external communications activity (PR
  description, release note, crisis/Q&A material) and the audience, message hierarchy, approval
  routing, or success criteria aren't yet decided. Decision rules cover channel choice by named
  audience (paid/earned/shared/owned), one-core-message discipline, proof points with
  ethos/pathos/logos matched to the audience's objection, crisis Q&A approval routing and shared
  spokesperson statements, and evaluation criteria spanning activity results, outtakes, and
  outcomes. Trigger on requests like "보도자료 초안 잡아줘", "릴리스 노트 메시지 정리해줘", "draft a press release
  plan", "who needs to clear this crisis statement", "how do we measure this campaign". Do NOT use
  for product marketing copy and in-product persuasion (use marketing-message-persuasion) or for
  user-facing UI text (content-design-operational-playbook).
metadata:
  role: pr-communications
  axes:
    - objective-channel-fit
    - message-hierarchy
    - approval-sequencing
    - risk-qa-prep
    - evaluation-criteria
    - persuasion-technique
  rule_count_floor: 12
  tier: moderate
---

# pr-communications operational playbook

Condition -> choice -> source decision rules for planning, drafting,
clearing, and evaluating external communications (PR descriptions,
release notes, crisis/Q&A material). Research protocol (issue #1174
amendment 1): every rule below traces to a fetched source, not
pretrained recall — see the evidence trail in
`docs/issue-1174/reports/pr-communications/scout-brief.md` and
`playbook-evidence-trail.md` in the `on-the-record` repo for the query
log.

## Trigger

Apply this skill whenever an external communications activity (PR
description, release note, crisis/Q&A material) is being planned,
drafted, cleared, or evaluated and any of: the channel hasn't been
chosen against a named audience yet (rule 1); more than one audience
segment or more than one core message exists for the same activity
(rules 2-3, 13); a key message lacks a proof point or the ethos/pathos/
logos lead hasn't been matched to the audience's objection, including a
gain-or-loss trade-off not yet framed explicitly (rules 4-6); the
activity touches a live incident or negative news, or a Q&A entry
lacks a routed approval or a shared spokesperson statement, including a
stale Q&A entry still on file (rules 7-10); or success criteria for the
activity aren't yet defined across outputs/outtakes/outcomes, or an
outcome claim lacks outtake-level evidence (rules 11-12).

## Procedure

1. Before choosing a channel, name the objective's target audience;
   choose the channel (paid/earned/shared/owned) by who that audience
   is, not by which channel is easiest to publish to (rule 1).
2. If more than one audience segment exists for the activity, split
   into separate messages per segment; if a plan lists more than one
   core message, cut to exactly one core message and demote the rest to
   supporting messages (rules 2-3).
3. If a key message has no proof point attached, attach one (data,
   example, quote, or artifact link) or drop the message (rule 4).
4. Match the lead persuasive appeal to the audience's actual objection —
   logos for technical/regulatory audiences, ethos for skeptical
   stakeholders, pathos only for genuinely emotional resistance (rule
   5).
5. If a message states a change as a gain-or-loss trade-off, frame the
   loss explicitly rather than folding it into neutral language (rule
   6).
6. If the activity touches a live incident or negative news, prepare
   Q&A material (question + pre-approved answer) before the first
   public statement goes out (rule 7).
7. Route each drafted Q&A answer through an explicit approval workflow
   (PR/comms owner, then legal if it makes a factual/liability claim,
   then the accountable executive) and record the named approver (rule
   8).
8. If more than one spokesperson may face the same question, give them
   one shared pre-approved holding statement rather than letting each
   improvise (rule 9).
9. Delete Q&A entries that stopped being plausible (feature shipped,
   concern already resolved publicly) rather than leaving them to
   accumulate (rule 10).
10. Before the activity is sent, define success criteria across all
    three of outputs, outtakes, and outcomes — never backfilled after
    (rule 11).
11. If an outcome claim has no outtake-level evidence under it, report
    it as unverified and route it back to add an outtake-level check
    rather than reporting the outcome as measured (rule 12).
12. If a supporting message restates the core message in different
    words without adding a distinct sub-claim, cut it (rule 13).

## Output shape

A cited condition -> choice -> source decision for the communications
activity at hand: the chosen channel and audience segmentation, a
single core message with distinct supporting messages each carrying a
proof point, the matched persuasive appeal, any Q&A material with its
named approver, and outputs/outtakes/outcomes success criteria defined
before send — with each REMOVAL-category rule (3, 10, 13) applied as a
cut (an extra core message, a stale Q&A entry, or a restated supporting
message removed) rather than an addition.

## Rules

1. When the audience for a message is not yet named, choose the
   channel (paid/earned/shared/owned) by who the objective's target
   audience actually is, not by which channel is easiest to publish to
   — RACE's own "Communication" step only follows a completed
   "Research" step that identifies the audience first.
   Source: Cutlip & Center, *Effective Public Relations*, planning
   sequence (fact-finding -> planning -> communicating -> evaluation);
   summarized at https://2012books.lardbucket.org/books/public-relations/s10-the-public-relations-process-r.html

2. When more than one audience segment exists for the same activity
   (e.g. end users vs. press vs. internal stakeholders), split into
   separate messages per segment rather than one generic message for
   all — a single undifferentiated message under-serves every segment's
   actual concern.
   Source: PR Academy PR planning toolkit, audience segmentation step;
   https://pracademy.co.uk/insights/pr-planning-toolkit/

3. **REMOVAL**: when a communications plan lists more than one core
   message, cut it down to exactly one core message and demote the
   rest to supporting messages — two or more "core" messages is not a
   hierarchy, it is an unranked list, and dilutes what the audience
   retains.
   Source: three-tier message-house structure (core message + supporting
   messages + proof points), as documented in PR planning practice;
   https://pracademy.co.uk/insights/pr-planning-toolkit/

4. When a key message has no proof point attached, either attach a
   concrete proof point (data, example, quote, or artifact link) before
   publishing, or drop the message — an unsupported claim is not
   persuasive under logos and invites a credibility challenge under
   ethos.
   Source: Aristotle's ethos/logos framework as applied to modern
   persuasive-message construction; https://virtualspeech.com/blog/ethos-pathos-logos-public-speaking-persuasion

5. When choosing which of ethos, pathos, or logos to lead with, match it
   to the audience's actual objection: lead with logos (data/evidence)
   for a technical/regulatory audience, ethos (credibility/track record)
   for a skeptical stakeholder audience, and pathos (concrete stakes,
   not generic sentiment) only when the audience's resistance is
   emotional rather than factual — leading with pathos against a
   factual objection reads as evasive.
   Source: Aristotle's three modes of persuasion, rhetorical-appeal
   selection; https://www.davidpublisher.com/Public/uploads/Contribute/5cc1077dd950d.pdf

6. When a message states a change as a gain-or-loss trade-off (e.g. a
   deprecation, a price change, a scope cut), frame the loss explicitly
   rather than folding it into neutral language — under prospect theory,
   audiences weigh a hidden/implied loss more harshly once discovered
   than an explicitly acknowledged one, and an unacknowledged loss reads
   as concealment once found.
   Source: Kahneman & Tversky, "Choices, Values, and Frames" (prospect
   theory, framing effects), as connected to persuasion-message design;
   https://www.ebsco.com/research-starters/social-sciences-and-humanities/theories-persuasion

7. When a communications activity touches a live incident or negative
   news, prepare Q&A material (anticipated question + pre-approved
   answer) before the first public statement goes out, not after —
   drafting the answer under live-question pressure produces slower,
   less consistent responses across spokespeople.
   Source: PRSA Crisis Communications Checklist, 24-hour response
   protocol; https://jobs.prsa.org/career-resources/finding-talent-10/crisis-communications-checklist-24-hour-response-protocol-405

8. When a Q&A entry has a drafted answer, route it through an explicit
   approval workflow (PR/comms owner, then legal if the answer makes a
   factual or liability claim, then the accountable executive) and
   record who signed off — an answer with no named approver is a draft,
   not a cleared response, and should not be treated as ready to use
   under pressure.
   Source: PRSA crisis-communication-plan checklist, approval-workflow
   step; https://jobs.prsa.org/career-resources/finding-talent-10/crisis-communication-plan-a-complete-checklist-381

9. When more than one spokesperson may face the same question, use one
   shared pre-approved holding statement across all of them rather than
   letting each improvise their own phrasing — inconsistent phrasing
   across spokespeople on the same question reads as the organization
   not having a single position.
   Source: PRSA executive-communications-during-crisis spokesperson
   preparation guide; https://jobs.prsa.org/career-resources/finding-talent-10/executive-communications-during-crisis-spokesperson-preparation-guide-409

10. **REMOVAL**: when a risk/Q&A document accumulates answers for
    questions that stopped being plausible (the underlying feature
    shipped, the concern was already resolved publicly), delete those
    entries rather than leaving them to accumulate — a stale Q&A entry
    left in place gets reused as if still current and can contradict
    the now-current position.
    Source: cognitive-load reduction / minimalism-in-editing lineage
    applied to reference material upkeep; https://www.ebsco.com/research-starters/social-sciences-and-humanities/theories-persuasion (framing/attention-load discussion) plus the subtraction-neglect finding below (rule 12) as the general justification for active deletion over passive accumulation.

11. When defining success criteria for a communications activity,
    define them across all three of outputs (what was produced/sent),
    outtakes (what the audience understood or recalled), and outcomes
    (attitude/behavior change) — not outputs alone — and do so BEFORE
    the send, never backfilled after, since a criterion chosen after
    seeing results is not a criterion, it is a rationalization.
    Source: Barcelona Principles 4.0 (AMEC), outputs/outtakes/outcomes/
    impact measurement chain; https://amecorg.com/resources/barcelona-principles-4-0/

12. When an outcome claim ("this changed perception/behavior") has no
    outtake-level evidence under it (a measured comprehension or
    recall check), do not report the outcome as measured — report it as
    unverified and route it back to add an outtake-level check, since
    Barcelona's own chain requires outcome to trace to a measured
    outtake, not to be asserted on top of outputs alone.
    Source: Barcelona Principles 4.0 (AMEC), outcome/impact
    distinction and evidence-chain requirement;
    https://amecorg.com/resources/barcelona-principles-4-0/

13. **REMOVAL**: when a supporting message restates the core message in
    different words rather than adding a distinct sub-claim, cut it —
    a message house with N supporting messages that all say the same
    thing as the core is not a hierarchy, it is padding, and readers
    default to skipping repeated content, wasting the scarce attention
    a real second point would have used.
    Source: three-tier message-house discipline (one core, distinct
    supporting messages, each with its own proof point);
    https://pracademy.co.uk/insights/pr-planning-toolkit/ — general
    justification: Adams, Converse, Hales & Klotz, "People
    systematically overlook subtractive changes", *Nature* 594 (2021),
    on the human tendency to default to addition over removal even
    when removal is the better structural choice.

## Counter-example

A one-line release note ("Fixed a bug") is NOT required to run the full
message-hierarchy/Q&A/evaluation apparatus above — rules 3-13 apply when
the communications activity has an audience beyond the immediate PR
reviewer and a stated objective (per the role's own `objective` required
field). A routine internal-only changelog entry with no external
audience is out of this playbook's scope; applying the full apparatus to
it would be exactly the padding rule 13 warns against.

## Open gap

Channel-specific timing rules (e.g. embargo handling, simultaneous
multi-channel release windows) were not researched in this pass — the
fetched sources covered planning/message/evaluation but not
release-timing mechanics specifically. See the evidence trail's open
findings for the follow-up.
