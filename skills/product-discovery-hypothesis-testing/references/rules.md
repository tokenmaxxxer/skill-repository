# product-discovery-hypothesis-testing — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] The carrying file

Every hypothesis lives in one specification file under `docs/proposals/`,
e.g. `docs/proposals/2026-07-25-onboarding-checklist.md`, with YAML
frontmatter:

```
---
status: idle
hypothesis_statement:
metric:
threshold:
decision_rule:
fail_condition:
time_box:
confidence_level:
---
```

`status` is the state field. `hypothesis_statement`, `metric`,
`threshold`, `decision_rule`, `fail_condition`, and `time_box` are the
pre-registration fields; `confidence_level` is optional and never gates a
transition. All live in this one file — do not split them across files,
and do not track state anywhere else (no separate ledger, no database, no
state stored only in conversation).

`hypothesis_statement` is one falsifiable sentence ("We believe <X> will
happen for <target market> because <reason>; we'll know we're right if
<signal>") — distinct from the "Candidate Hypotheses" list drafted in the
one-pager (early, unranked guesses) and from the registered
`metric`/`threshold`/`decision_rule` package below (the mechanical test of
that one sentence). `decision_rule` keeps the mechanical rule as a whole;
`fail_condition` states the kill trigger alone, pulled out of it for
`grep`-ability; `time_box` states the measurement window alone, same
reason. `confidence_level` records how confident the team is in the
hypothesis at registration time, if the user offers one — the skill may
ask for it but must never refuse a transition for its absence.

## Moving through the states

1. **role intake**: the user hands you an idea. open the record
   and write down what the idea claims and who it is for. Nothing else is
   required to open the role.

2. **scoping to researching**: begin gathering evidence — user interviews,
   existing data, competitive signal, whatever grounds the claim. Set
   `status: researching`. Do not skip straight to a metric before you have
   evidence to derive one from; a registered metric with no evidentiary
   basis is not what this state is for.

3. **researching to hypothesis-registered**: write the falsifiable
   `hypothesis_statement`, then propose the metric, the threshold, and the
   decision rule (with `fail_condition` and `time_box` broken out
   separately), and write them all into the file's frontmatter, e.g.:

   ```
   hypothesis_statement: We believe adding a checklist to onboarding will
     raise 7-day activation among new signups because the drop-off
     interviews point at "didn't know what to do first"; we'll know we're
     right if 7-day activation clears 20% within 2 weeks.
   metric: 7-day activation rate among new signups
   threshold: >= 20% within a 2-week measurement window
   decision_rule: if the 7-day activation rate is >= 20% at the end of the
     2-week window, persist and move to the next milestone; if it is below
     15%, kill; between 15% and 20%, extend the window once by 2 weeks and
     re-measure, no further extensions.
   fail_condition: 7-day activation rate below 15% at the end of the
     2-week window.
   time_box: 2-week measurement window from first exposure, one 2-week
     extension permitted per decision_rule, no further extensions.
   confidence_level: medium (optional; asked but never gates the move to
     measuring)
   ```

   The rule must be a decision procedure that a fresh reader could apply
   mechanically to the data — not "we'll see how it feels." Fix it before
   any data collection starts; this is the whole point of pre-registration.
   If the hypothesis cannot be stated in a way any outcome could falsify,
   do not force a registration — say so and treat it as a
   `hypothesis-not-falsifiable` refusal (see loop_state vocabulary below)
   until it can be restated as testable. Set `status:
   hypothesis-registered`.

## [S2] Common mistakes this skill exists to prevent

- Registering a metric with no threshold ("we'll track activation and see")
  — not a testable hypothesis, and the gate will refuse it.
- Treating the user's silence, or a file simply containing all three
  fields, as approval — it is not; the gate requires an actual approval
  token from the user's own turn.
- Rationalizing a different decision than the registered rule once the
  numbers come in. The value of pre-registration is precisely that the
  rule was fixed before anyone had a stake in a particular answer.
- Editing `threshold` after `measuring` starts because new information
  makes the original number look wrong. If the threshold was genuinely
  mis-set, kill the hypothesis and register a new one — do not move the
  goalposts on the one in flight.
- Registering a package around a `hypothesis_statement` no outcome could
  ever contradict — that is `hypothesis-not-falsifiable`, not a
  registration.
- Collapsing `recommendation` and `verdict` into one line, or writing a
  verdict when the cited evidence log does not actually resolve
  (`evidence-log-unreadable` exists precisely for that case).

