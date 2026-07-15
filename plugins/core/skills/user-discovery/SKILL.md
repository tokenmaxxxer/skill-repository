---
name: user-discovery
description: >-
  A design-and-analysis harness for generative user research (discovery): it designs
  bias-controlled interview studies, then analyzes the transcripts/notes the user brings back —
  tracking saturation, grading evidence strength, and separating observation from opinion. Use
  whenever the user wants to find out what customers actually need before building — "고객 인터뷰
  설계해줘", "design user interviews", "what should I ask potential users", "analyze these
  interview notes/transcripts", "did we talk to enough users", "what jobs are customers hiring
  this for", "build personas from this research", "is this user feedback a real pattern".
  Trigger it when someone is about to build based on a few enthusiastic anecdotes or wants to
  validate a problem hypothesis with real people. Do NOT use for evaluative testing of an
  existing design (usability-eval), market sizing/competition (market-recon), or surveys whose
  goal is statistical measurement rather than discovery.
---

# User Discovery — a design & analysis harness for generative research

You cannot sit in the room with the user's customers — but everything around the conversation is yours to do rigorously: design the study so the answers can be trusted, and analyze what comes back so patterns are real, not wishful. The failure mode this skill exists to prevent: building a product on polite lies ("sounds great, I'd totally use it") and a handful of vivid anecdotes.

## First: is this the right harness?

- Testing an *existing* design/prototype → `usability-eval`. Sizing a market or mapping competitors → `market-recon`. Statistical measurement of a known question → that's a survey design problem, and its sampling rules live in market-recon's criteria.
- If the user just wants a quick opinion on an idea, give it — don't ceremonially design a study nobody asked for.

## The one rule that carries the most weight

**Past behavior over future hypotheticals.** "Would you use this?" produces politeness, not evidence — stated intent is systematically inflated (~21% on average for willingness-to-pay, more for emotionally-loaded categories). Every question you design should ask what the person *did*, *paid*, or *worked around* — "walk me through the last time this happened" — and every analysis you run should grade a claim by whether it's backed by behavior. This is the Mom Test discipline and it's the closest thing this field has to a law.

## Designing the study (what you produce before anyone talks to a user)

1. **Falsifiable hypotheses first.** Write down what the team believes ("SMB owners spend >2h/week on X and hate it") and what evidence would *disprove* it. A hypothesis you can't state a disconfirming observation for isn't ready to research.
2. **Interview guide under Mom Test rules.** Questions about their life, not your idea; specific past events, not opinions; the idea itself stays unpitched as long as possible. Include the follow-up ladder: "when did this last happen → what did you do → did you pay/spend time on anything → what happened next." Flag any question in the draft that a polite person could answer with a compliment.
3. **Screener that doesn't leak.** Recruit by behavior ("did X in the last month"), not by attitude ("interested in productivity"). Hide the qualifying answer among distractors — a screener that telegraphs who you want recruits professional respondents (panel respondents answer a median 10 surveys/month vs 3 for probability panels; they're 2-3× more likely to be in multiple panels). Prepaid incentives beat conditional ones for response (46-RCT meta-analysis); incentives don't ruin data quality but do skew *who* shows up — note it.
4. **Plan the stopping rule up front.** Saturation is quantified: expect ~80% of codes within the first 6 interviews of a homogeneous segment and code saturation by ~12 (Guest 2006); heterogeneous or meaning-level questions need 16-24. Commit to the rule: "stop when 2-3 consecutive interviews yield no new themes." Interview count is an output of saturation, not a target you set to feel done.
5. **Consider observation over interviews** when the behavior is habitual or hard to verbalize: contextual inquiry (watch them work, ask in the moment) beats recall — people can't accurately report their own workarounds. A diary study fits low-frequency or longitudinal behavior.

## Analyzing what comes back (transcripts, notes, recordings)

1. **Code before you conclude.** Run a real thematic pass (familiarize → code segments → build candidate themes → check themes against ALL the data, not just the quotes that fit). The check-back step is where confirmation bias dies — actively look for interviews that contradict each theme.
2. **Grade every finding by evidence strength.** Observed behavior / actual spend (strong) → specific recounted past events (medium) → opinions, predictions, compliments (weak — and "I'd definitely pay for that" is weak *by category*, regardless of enthusiasm). A theme built only on weak-tier quotes gets reported as a hypothesis, not a finding.
3. **Pattern threshold honesty.** There is no researched magic number for "N people said it = real pattern." What you can do honestly: report prevalence ("7 of 9 SMB interviews described this unprompted"), distinguish unprompted from prompted mentions, and never generalize a discovery-sample pattern to market size — that's a quantitative-survey job with real sampling.
4. **Track saturation in the ledger.** New themes per interview, cumulative. If the curve hasn't flattened, say so: "not saturated — patterns may still be missing," and recommend how many more conversations and with whom.
5. **Personas only if data-built.** A persona is a cluster summary of observed behavior patterns, with the evidence attached. If asked to write personas without research behind them, say plainly they'll be fiction and offer the study design instead.

## The deliverable

Study designs ship as: hypotheses + disconfirming evidence, interview guide, screener, stopping rule, and analysis plan. Analyses ship as: themes with evidence grades and prevalence, contradicting evidence noted, saturation status, and the decision each finding supports or blocks. Both end with the cheapest next step (more interviews in segment X / switch to observation / graduate to a quantitative survey or pre-sale test for demand confirmation — discovery finds problems; it does not prove purchase intent).

## References

Read `references/criteria.md` only for a high-stakes study where you need the precise numbers and their sources — saturation formulas, incentive meta-analysis, coder-reliability (kappa) thresholds and their known critiques, trustworthiness criteria (Lincoln & Guba), contextual-inquiry principles. Light requests never need it.