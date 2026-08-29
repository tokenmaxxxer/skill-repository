# release-engineering-readiness-checklist — full rules and citations

Moved verbatim from SKILL.md by issue-100 progressive disclosure.
The SKILL.md body carries the rule index; read this file when a
matched rule's full text, citation, or counter-example is needed.

## [S1] The record file

`docs/issue-<n>/reports/release-engineering.md`, at the repository root the skill is being run against.
Frontmatter carries the state field:

```markdown
---
phase: readiness      # idle | readiness | rollout | steady | incident
error_budget: ok        # ok | exhausted — read only while phase: steady
postmortem: docs/reports/2026-07-25-incident-x.md   # only while closing incident to steady
---
```

Below the frontmatter, a `## Checklist` section holds one line per item,
in this exact shape (the gate's regex is strict about it):

```
- item: <what is being checked> | status: yes | artifact: <url, path, or config key>
- item: <what is being checked> | status: no | artifact:
```

A `no` item is fine — it just means the transition isn't ready yet. A
`yes` item with an empty `artifact:` field is what fails the gate: per
`launch-readiness`, "we have monitoring" with nothing to link is not a
pass. Point at something real: a dashboard URL, a runbook path, a config
key, a file in this repo.

## [S2] Working skill start

Opened when the user hands the skill a merged change plus the measurement
design `feasibility` produced (`docs/specs/agent-roles.md`, ops: "given to
start"). Write `docs/issue-<n>/reports/release-engineering.md` with `phase: readiness` and start filling in
checklist items — this transition itself is not gated by anything beyond
existing.

## [S3] Working `readiness to rollout`

Gated: every checklist item must resolve yes/no, and every yes needs a
real artifact. Before flipping `phase: rollout`, re-read the whole
checklist section and ask, for each `yes`: does the `artifact:` field name
something a stranger could actually open? If not, it is not a yes yet —
mark it `no` and keep working it, or fill in the real pointer.

If the record gate refuses the transition, its stderr names the exact item
that failed and why — fix that item's `artifact:` field (or flip it to
`no`) and retry; do not attempt to route around it by writing through Bash
redirection with a different form — the gate reads the target path for any
tool, so that produces the same refusal.

## [S4] Working `readiness to rollout`, and `rollout`'s own agent-owned steps

Once every checklist item resolves and every `yes` has a real artifact, the
agent moves itself to `rollout` — no human gate on this step. From there,
`rollout to rollout` (canary step promotion on a clean metric check) and
`rollout to incident` (breach past a hard pre-set threshold) are both
`actor: agent` rows the `rollout-plan` skill's declared thresholds drive
mechanically. See `rollout-plan/skills/rollout-plan/SKILL.md`.

## [S5] Working `rollout to steady`

There is no approval-token mechanism. This transition is `actor: user`: it
may only be taken once the user has said something in their own turn that
unambiguously states the promotion approval (e.g. "I approve promoting this
to steady state", "approved for production"). A bare "ok" or "looks good"
is not enough — if the user's turn is vague, ask them to state the
approval explicitly, naming "steady" or "production" alongside an
approval/promotion verb, rather than writing `phase: steady` on a guess.
Before writing `docs/issue-<n>/reports/release-engineering.md`, record which of the user's own utterances
you read as satisfying this precondition — the injected transition rules
require this record as a line in the state file; nothing enforces it
mechanically, so do it because the row's `actor: user` designation depends
on it having actually happened.

## [S6] Steady state and the error budget

While `phase: steady`, the `error_budget:` field is read mechanically
before any transition back toward a release (`steady to readiness`,
i.e. picking up a new change). If it reads `exhausted`, that transition is
refused outright — not a suggestion, a hard denial — regardless of how
ready the next change looks. Per Google's error-budget policy this
mirrors: only P0/security-fix work proceeds while the budget is spent; the
mechanical check here does not carve that exception in automatically, so
route a true P0 through the user rather than editing the field to `ok`
to unblock it — that would be lying to the gate about a state that isn't
true.

## [S7] Closing an incident

`steady to incident` fires on a monitored signal crossing its declared
threshold; nothing here gates that direction. Closing back to `steady` is
`actor: user` and requires more than a filled-in field: the postmortem
(`postmortem/skills/postmortem/SKILL.md`) must be filed *and* the user must
say, in their own turn, that a human reviewer has reviewed it and is
satisfied with the document and its action items — Google's own rule is
that "an unreviewed postmortem might as well never have existed," so a bare
non-empty `postmortem:` field is not sufficient on its own. `incident to
readiness` is a separate, later `actor: user` row: postmortem action-item
sign-off specifically gates re-entry into a release cycle for the affected
surface, distinct from the general close.

