---
name: launch-readiness
description: >-
  Use when the user wants to check whether a launch is actually ready to ship, or wants a
  canary/staged-rollout plan. A pre-launch readiness review procedure for user-facing
  launches and significant changes, in the Google Launch Coordination Engineering (LCE)
  lineage; the hard rule is that every checklist item must resolve to a yes/no backed by a
  pointable artifact (a config, a dashboard URL, a runbook document) — "we have monitoring"
  with nothing to link is a FAIL. Trigger on "출시 준비됐는지 점검해줘", "런치 체크리스트 만들어줘", "go/no-go
  체크리스트", "launch readiness review", "rollout plan before we ship this". Do NOT use for
  routine deploys of unchanged behavior with no user-visible or load-profile change, for
  post-incident retrospectives (use blameless-postmortem), or for doing the underlying
  implementation work.
---

# Launch Readiness

## First: does this even need the procedure?

Two checks before you run the full review, because dragging a launch review into a
non-launch conversation is its own waste of the user's time:

- **Scope gate.** Does the change alter user-visible behavior or load profile? If the answer
  is a clean no — an internal refactor with no externally observable effect, a config tweak
  already covered by an existing reviewed rollout, a dev-only tool — exit here. Note it as
  "trivial, no launch review needed" and, at most, flag one directly relevant risk you notice.
  Do not produce the checklist for it.
- **Is the thing itself still being built?** If the feature isn't implemented yet, this skill
  is the wrong tool right now — come back to it once there's something concrete to review
  (a rollback procedure to point at, a dashboard to link, a rollout plan to write down).
  Don't use it as a design exercise for something that doesn't exist yet.

Everything below applies once you have a real, user-facing launch or significant change to
put through review.

## The procedure

### Step 1 — Scope gate (formal)

**Objective test:** does this change alter user-visible behavior or load profile? Yes/no,
decided before anything else. A "no" exits the process (see above). A "yes" means every area
below applies — there is no partial-launch exemption for "it's just a small change."

### Step 2 — Readiness checklist by area

#### Step 2a — Classification (area risk tier)

Before item-by-item expansion, classify each checklist area by risk:

| Area | Tier | Rationale |
|------|------|-----------|
| Rollback | High | Inability to roll back extends outage → user safety / data loss / revenue |
| Monitoring & alerting | High | Undetected issues bypass all other safeguards → safety / data loss |
| Failure modes | High | Unrecognized failure modes become unmitigated incidents → safety / data loss / revenue |
| Capacity | Medium | Revenue-affecting on overload; typically does not cause data loss |
| Dependencies | Medium | Cascading-failure risk exists but is indirect |
| Gradual rollout plan | Medium | Blast-radius control; revenue-affecting |
| Communication | Low | Coordination aid; does not directly prevent or detect incidents |

Tier rules:
- **High**: must produce binary yes/no + verifiable artifact.
- **Medium**: binary yes/no required; artifact optional, note when absent.
- **Low**: aggregate check ("N items reviewed, no blockers").

This classification table is part of the audit record — include it in the final output.

---

Each area below must be checked against its tier rule above. Leave no High item as prose reassurance.

**Rollback**
- [ ] A documented rollback procedure exists — *artifact: runbook/doc link*
- [ ] That procedure has actually been exercised at least once (a dry run, not just written
  down) — *artifact: dated record of the exercise, who ran it, what happened*

**Monitoring & alerting**
- [ ] Dashboards exist covering this launch's key metrics — *artifact: dashboard URL*
- [ ] Alerts are configured against those metrics — *artifact: alert config / rule ID*
- [ ] Each alert has a named owner who will act on it — *artifact: on-call/ownership entry*

**Capacity**
- [ ] A load estimate for this launch is written down — *artifact: capacity doc with the
  number*
- [ ] Headroom is stated as a number (e.g. "provisioned for 3x expected peak," not "should be
  fine") — *artifact: same doc, the number*

**Dependencies**
- [ ] A list of external/internal dependencies this launch relies on exists — *artifact:
  dependency doc*
- [ ] Each dependency has a documented failure-mode note (what happens to us if it goes down)
  — *artifact: same doc, per-dependency*

**Failure modes**
- [ ] The top failure modes for this launch are enumerated — *artifact: doc listing them*
- [ ] Each enumerated failure mode has a stated mitigation — *artifact: same doc*

**Gradual rollout plan**
- [ ] Staged rollout percentages are written down **before** launch — *artifact: rollout plan
  doc*
- [ ] Promotion criteria between stages are written down **before** launch, in numeric terms
  — *artifact: same doc*

**Communication**
- [ ] A named person (or rotation) who gets paged on issues is identified — *artifact:
  paging/on-call config*
- [ ] Named people or a channel who are kept informed of launch status are identified —
  *artifact: comms plan / channel link*

### Step 3 — Canary procedure

Before any traffic is exposed, three things must already be written down — not decided in
the moment once numbers start coming in:

- [ ] **Canary population size** is defined (e.g. 1% of traffic, a specific region/cohort) —
  *artifact: rollout plan doc*
- [ ] **Success metrics** are defined numerically and tied to the dashboards from Step 2 —
  *artifact: same doc, with metric + threshold*
- [ ] **Abort thresholds** are defined numerically, in advance — *artifact: same doc*

**Promotion rule:** advance to the next stage only when the pre-written criteria are met.
**Any abort-threshold breach means rollback — no exceptions negotiated in the moment.** If
you find yourself debating whether a breach "really counts" during the rollout, that
debate itself is the failure mode this step exists to prevent; the pre-written threshold
already made the call.

### Step 4 — Verdict

**Launch-ready** means:
- Every **High** area item from Step 2 is a yes backed by an artifact.
- Every **Medium** area item from Step 2 is a yes (artifact optional, noted when absent).
- Every **Low** area from Step 2 passes its aggregate check.
- Every Step 3 canary item is a yes backed by an artifact (no tier relaxation — canary items
  directly affect safety).

There is no weighted score and no "mostly ready" — these gates are per-tier, not averaged.

If any item fails its tier rule, the launch is **not ready**. Output the result as a blocking
list grouped by tier: each failing item, its area, what's missing, and which tier rule it
broke. The blocking list is the entire output of a failed review — do not average it into an
overall percentage or soften it into "mostly ready, just needs monitoring."

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — The hard rule that makes this a review and not a vibe check → references/rules.md
- S2 — Evidence grade (read before presenting this as more than it is) → references/rules.md
