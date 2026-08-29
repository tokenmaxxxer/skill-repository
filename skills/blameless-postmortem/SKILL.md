---
name: blameless-postmortem
description: >-
  Use whenever the user needs to write up an incident after the fact. A structured-writing
  procedure for blameless incident postmortems in the Google SRE lineage: reconstruct a
  timestamped timeline, quantify impact, fill the four required sections (impact / actions
  taken / root cause / prevention follow-ups), strip blame language from the draft, and
  assign owner+deadline to every action item. Trigger on "포스트모템 써줘", "장애 회고 정리해줘", "write a
  postmortem for this outage", "blameless postmortem template", "incident review writeup".
  Do NOT use for a routine bugfix that caused no declared incident, for live incident
  response while the fire is still active (this is the after-the-fact written record, not a
  runbook), when the user wants to assign blame to a specific person, or for the
  release-skill record inside this repo's skill system (use release-engineering-postmortem).
---

# Blameless Postmortem

## First: does this even need the procedure?

Run the **scope gate** before anything else, because writing a full postmortem for a non-incident wastes the team's time and dilutes the practice for when it matters:

- **Did an incident actually occur, or was one declared?** Name the trigger condition explicitly: an SLO breach, data loss, a paging event, a customer-visible outage, or a near-miss the team has a pre-existing policy of writing up anyway. If none of these apply — this was a routine bug caught in code review or CI, with no user/system impact and no near-miss — **exit here**. Say so plainly and point back to normal code review; do not manufacture a postmortem for it.
- **Is the incident still ongoing?** If mitigation is still in progress, this isn't the right moment — the postmortem is written after resolution, from the timeline the incident left behind. Say so and offer to return once it's resolved.
- **Is the request actually "figure out who's at fault"?** If the user frames this as identifying which person or team to blame, say directly that this procedure is structurally blameless (Step 5 exists precisely to prevent that) and ask if a blameless writeup is still what they want.

Everything below applies once an incident (or declared near-miss) with a named trigger condition is confirmed and resolved.

## Evidence grade — read before citing this to anyone

- **Confirmed, primary source:** Google's *Site Reliability Engineering* book, chapter 15 ("Postmortem Culture"). It defines a postmortem as a structured **written** record and specifies the required elements this skill's Step 4 gate is built on: impact, mitigation/resolution actions taken, root cause(s), and follow-up prevention actions. It also states the blameless principle explicitly: identify contributing causes without indicting any individual or team, assuming everyone acted in good faith with the information available to them at the time. Both of these are documented, checkable claims — cite them as such.
- **Not verified in our research — do not state as fact:** the commonly told origin story crediting Etsy / John Allspaw with founding blameless postmortem culture. It is widely repeated, but the verification pass behind this skill did not confirm a primary source for it. Omit it, or if raised, mark it explicitly as "commonly attributed, not independently confirmed" — never present it as settled history.
- **Not empirically validated — say so plainly:** owner+deadline discipline on action items (Step 6) is required by this skill as a **procedural design decision**, not because a controlled study proved it works. It makes the gate objective and the item trackable — that's the justification. Likewise, no controlled study verified in this research shows that writing postmortems reduces incident recurrence. The SRE book documents the practice and its rationale; it is not a controlled-trial result. If asked "does this actually prevent repeat incidents," the honest answer is: the industry-standard source documents the practice, but we have no verified causal evidence of reduced recurrence — do not oversell it.

## Procedure

### Step 1 — Scope gate

Already covered above. Gate: **the trigger condition is named** (SLO breach / data loss / paging event / declared near-miss / other pre-existing threshold). If it can't be named, exit — this is code-review territory, not a postmortem.

### Step 2 — Timeline reconstruction

#### Step 2a — Classification (criticality triage)

Before reconstructing the timeline, classify each candidate entry by criticality:

| Tier | Criteria | Treatment |
|------|----------|-----------|
| High | Led directly to the incident OR was a missed detection opportunity | Full timestamp + artifact citation |
| Medium | Contextual / background events that shaped the incident landscape | Timestamp required; artifact citation optional |
| Low | Routine events included for completeness | Aggregate only ("N routine events during the window, no incident relevance") |

This classification is part of the audit record — include it in the final timeline output, with entries grouped or tagged by tier.

---

Build an ordered timeline from artifacts: logs, alerts, chat records, deploy history, dashboards, ticket timestamps. Apply the tier rules from Step 2a:

- **High** entries: full timestamp + artifact citation (e.g., "14:32 UTC — deploy of service X, source: deploy log #4821").
- **Medium** entries: timestamp required; artifact citation optional, note when absent.
- **Low** entries: aggregate in a summary line ("N routine events during the window, no incident relevance").

**Gate:** every **High** entry cites its source artifact. **Medium** entries require timestamps; missing artifacts are noted but not blocking. **Low** entries are aggregated. Any entry reconstructed purely from someone's memory, with no artifact behind it, is explicitly marked **"unconfirmed"** regardless of tier — "unconfirmed" entries cannot be classified as High.

### Step 3 — Impact quantification

State impact as numbers: duration of impact, count of users/requests affected, revenue or SLO-burn if available.

**Gate:** at least one measured impact number is present, OR the impact is explicitly marked **"unmeasured."** Unmeasured is not a dead end — it becomes its own action item in Step 6 (e.g., "instrument request-level error tracking for this path so impact is measurable next time").

### Step 4 — The four required sections

Per the SRE book definition, the document must contain all four of:

1. **Impact** — what broke, for whom, for how long (pulls from Step 3).
2. **Actions taken** — what mitigation/resolution steps were actually performed, in what order (pulls from Step 2).
3. **Root cause(s)** — the contributing system/process conditions, not people.
4. **Prevention follow-ups** — the concrete changes that reduce recurrence risk (feeds Step 6).

**Gate:** binary per section — each of the four is either present or it isn't. All four must be present; a postmortem missing any one of them is incomplete, full stop.

### Step 5 — Blameless check (operational, not aspirational)

Scan the entire draft for two concrete failure patterns:

- **(a) Causal-position names.** Any sentence where a person's name or a team's name is the subject of a causal verb — "Alice pushed the bad config," "the platform team broke the pipeline" — must be rewritten to name the system condition instead: "a config change reached production without automated validation." Names may still appear in the **timeline** as actors performing actions ("Alice deployed build 4821 at 14:32") — that's a factual record, not a cause. Names must never appear as the cause of the failure.
- **(b) Counterfactual/blame language.** Phrases like "should have," "failed to," "carelessly," "didn't bother to" are blame markers even without a name attached. Rewrite them into neutral conditions: "the on-call engineer should have caught this" becomes "the alert threshold did not trigger until after customer impact began."

**Gate:** zero causal-position names remain in the document, and every flagged blame phrase has been rewritten. This is a literal scan-and-fix pass over the draft text, not a vibe check — go through the document section by section and confirm each hit is resolved.

### Step 6 — Action items

#### Step 6a — Action item classification

Classify each prevention follow-up from Step 4 by criticality:

| Tier | Criteria | Fields required |
|------|----------|-----------------|
| High | Prevents recurrence of a root cause | Owner + deadline + verifiable artifact |
| Medium | Improvement that does not directly prevent recurrence | Owner + deadline |
| Low | Nice-to-have / polish | Aggregate list only |

This classification is part of the audit record.

---

Apply the tier rules from Step 6a to each prevention follow-up from Step 4:

- **High** action items require:
  - **Owner** — a specific name, not a team or "TBD."
  - **Deadline** — a specific date, not "soon" or "next sprint."
  - **Verifiable artifact** — the item is stated as a change whose existence can later be checked: a specific config, an added test, a new alert, a written runbook step. Not "improve monitoring" — "add a p99-latency alert on endpoint /checkout with a 2s threshold, owned by Priya, due 2026-08-01."
- **Medium** action items require owner + deadline only.
- **Low** action items are listed in aggregate.

**Gate:** every **High** action item has owner + date + a verifiable-artifact description. Every **Medium** action item has owner + date. **Low** items are listed in aggregate. No High or Medium action item has blanks or "TBD" owners. An item that fails its tier gate is not done — send it back for specifics.

Per the evidence-grade note above: this is enforced because it makes the gate objectively checkable later, not because a study proved owner+deadline items get done more often — don't claim the latter.

### Step 7 — Review & circulation

**Gate:** the document records at least one named reviewer who was not the primary author, before it's considered final. If no second reviewer exists yet, the postmortem is a draft, not a finished postmortem — say so and hold the "done" label until a reviewer is recorded.
