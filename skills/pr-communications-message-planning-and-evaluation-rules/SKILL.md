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

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — When the audience for a message is not yet named, choose the channel (paid/earned/shared/owned) by who the objective's target audience actually is, not by which channel…
- 1.2 — When more than one audience segment exists for the same activity (e.g. end users vs. press vs. internal stakeholders), split into separate messages per segment rather th…
- 1.3 — **REMOVAL**: when a communications plan lists more than one core message, cut it down to exactly one core message and demote the rest to supporting messages — two or mor…
- 1.4 — When a key message has no proof point attached, either attach a concrete proof point (data, example, quote, or artifact link) before publishing, or drop the message — an…
- 1.5 — When choosing which of ethos, pathos, or logos to lead with, match it to the audience's actual objection: lead with logos (data/evidence) for a technical/regulatory audi…
- 1.6 — When a message states a change as a gain-or-loss trade-off (e.g. a deprecation, a price change, a scope cut), frame the loss explicitly rather than folding it into neutr…
- 1.7 — When a communications activity touches a live incident or negative news, prepare Q&A material (anticipated question + pre-approved answer) before the first public statem…
- 1.8 — When a Q&A entry has a drafted answer, route it through an explicit approval workflow (PR/comms owner, then legal if the answer makes a factual or liability claim, then…
- 1.9 — When more than one spokesperson may face the same question, use one shared pre-approved holding statement across all of them rather than letting each improvise their own…
- 1.10 — **REMOVAL**: when a risk/Q&A document accumulates answers for questions that stopped being plausible (the underlying feature shipped, the concern was already resolved pu…
- 1.11 — When defining success criteria for a communications activity, define them across all three of outputs (what was produced/sent), outtakes (what the audience understood or…
- 1.12 — When an outcome claim ("this changed perception/behavior") has no outtake-level evidence under it (a measured comprehension or recall check), do not report the outcome a…
- 1.13 — **REMOVAL**: when a supporting message restates the core message in different words rather than adding a distinct sub-claim, cut it — a message house with N supporting m…
- S1 — Counter-example → references/rules.md
- S2 — Open gap → references/rules.md
