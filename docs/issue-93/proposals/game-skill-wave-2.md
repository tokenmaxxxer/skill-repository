---
status: proposed
files:
  - docs/issue-93/reports/knowledge-management/survey.md
  - docs/issue-93/reports/knowledge-management/scout-brief.md
  - docs/issue-93/proposals/game-skill-wave-2.md
  - skills/game-character-animation-and-motion/SKILL.md
  - skills/game-hit-reaction-and-impact/SKILL.md
  - skills/game-character-rendering-composition/SKILL.md
  - skills/game-growth-system-design/SKILL.md
  - docs/issue-93/reports/knowledge-management.md
---

# Game skill wave 2 (phase 1: research + proposal)

Note on survey location (skip record for the generic survey path only —
scouting itself was NOT skipped): the current-state survey lives at
`docs/issue-93/reports/knowledge-management/survey.md`, role-scoped per
contract v3 s11/s19, rather than the generic
`docs/issue-93/reports/implementation/survey.md`, because this role
writes only its own record area. No design decision is left open by
that path choice. Scouting ran in full; its output is
`docs/issue-93/reports/knowledge-management/scout-brief.md`.

## Request

Issue #93 (requirement R1): the tm-dicequest dogfood (cuts 2–4, operator
directive 2026-08-23) showed character rendering/motion/reaction and
growth-system coverage still too thin after wave 1. Author, research-
first, four new skills — character animation/motion state machines and
timing, hit reaction/impact conventions, character rendering
composition, and growth-system design deeper than the landed core-loop
skill — each with sourced decision rules and condition-matched "Use
when" triggers, `python3 scripts/check_skill_conformance.py` green.
Two-phase: this document is phase 1.

## Constraints

- Conformance checker must exit 0 after phase 2: `name:` == directory,
  `description:` with trigger marker, `axis:` + `rule_count_floor:`,
  every `### N.` rule block carrying a `source: <URL>` line.
- Every rule traces to a scout-brief source; unsourced claims are
  dropped or labelled assumptions.
- No restatement of wave-1 game skills or of
  `accessibility-aria-and-contrast-rules` / `ux-engineering-*`; genuine
  chains become `## Related skills` cross-links.
- Skills stay portable: no tm-dicequest paths or repo-specific
  assumptions.
- Phase 2 only after an approvers.md Approve; the delivery record
  `docs/issue-93/reports/knowledge-management.md` (with the research
  source list, per acceptance) is phase-2 output.

## Rationale

Chosen shape: **four sibling single-axis skills named exactly as the
issue names them**, sparse tier, wave-1 format (condition → choice →
why → source, `## Trigger`/`## Procedure`/`## Output shape`,
`## Related skills`).

Alternatives considered and rejected:

- **Extending the wave-1 skills in place** — folding hit-reaction into
  `game-feel-juice-and-feedback` and growth-system depth into
  `game-design-core-loop-and-progression`. Plausible: those are the
  survey-confirmed nearest neighbours, and extension avoids two new
  directory names. Rejected because the triggers are disjoint (juice
  staging vs. the combat impact contract; loop monotonicity vs.
  cross-session pacing), so extension would broaden each host's
  `description:` past single-axis retrieval — the false-hierarchy
  failure the taxonomy skill's rule 6 warns against; the correct
  encoding is a new term plus associative cross-links. The issue also
  names four skills explicitly.
- **One combined `game-character-playbook`** covering animation,
  impact, and rendering (three of the four share the character
  surface). Rejected: the authoring moments differ (animating a state
  machine, tuning a hit, drawing a rig) and a shared description would
  fire on all three, degrading retrieval; wave 1 already rejected the
  combined-playbook shape for the same reason.
- **Splitting finer** (e.g. separate `damage-numbers` or
  `i-frames` skills). Rejected: the sweep's evidence supports 1–2
  rules per such slice — below any useful `rule_count_floor:` — and
  each slice fires in the same authoring moment as its parent axis.

## What will be done

Phase 1 (this PR): the survey, the scout brief, this proposal. Stop.

Phase 2 (after Approve), four `SKILL.md` files:

1. **`game-character-animation-and-motion`** — axis
   `character-animation-and-motion`, floor 5. Rules: every animated
   character gets an explicit state machine (idle/run/jump/attack/
   hit/death) with declared transitions and interruptibility before
   any per-state art is tuned; attack/jump states carry an
   anticipation frame band and landing/stop states a 1–3-frame
   follow-through, scaled to the action's weight; choose CSS
   transition for two-state changes, keyframes + `steps()` for
   sprite-sheet states, JS-driven transform for continuous motion;
   character motion animates transform/opacity only (compositor
   discipline), never layout properties; per-state duration norms
   (snappy interruptible locomotion vs. committed attack recovery).
   Sources: sprite-ai animation-principles, gamedeveloper.com 12
   principles, pixel-editor sprite fundamentals, web.dev
   animations-guide, LogRocket/Comeau sprite `steps()`.
2. **`game-hit-reaction-and-impact`** — axis
   `hit-reaction-and-impact`, floor 5. Rules: hit-stop duration bands
   by attack weight (light/medium/heavy ≈ 9/11/13 frames as the
   fighting-game canon anchor, scaled to the game's tick rate);
   knockback magnitude as the combo/flow control, decaying curve not
   linear shove; i-frames attach to named recovery states
   (knockdown-getup, post-hit) with visible flicker signalling;
   damage numbers spawn at impact point, float and fade without
   blocking readability; screen-level feedback (shake/flash) reserved
   per `game-feel-juice-and-feedback`'s restraint rule — cross-link,
   not restatement. Sources: SmashWiki Hitlag, sonichurricane Impact
   Freeze, Sicienski Capcom hitstop, Smashpedia invincibility-frame.
3. **`game-character-rendering-composition`** — axis
   `character-rendering-composition`, floor 4. Rules: silhouette
   first — a character must read by silhouette at shipped size before
   detail passes (≈70/30 silhouette/detail weighting), build order
   trunk→limbs→head→details with a gate at each layer; shape language
   separates roles (player vs. monster vs. pickup) before color does;
   layered SVG/DOM rigs split parts by animation need (what moves
   independently gets its own node) with facing handled by transform
   flip; z-order contract between characters and field elements
   stated once, not per-frame. Sources: pixune shape-language,
   rocketbrush shape-language readability, nastyrodent art-direction
   playbook, anim.works silhouette.
4. **`game-growth-system-design`** — axis `growth-system-design`,
   floor 5. Rules: state the pacing curve across sessions (not just
   within one) — exponential cost curves set the purchase interval,
   and that interval is the tuned quantity; every currency gets a
   lifecycle audit — named sources, named sinks, and the
   inflation check (source rate vs. sink rate) before a new source
   ships; upgrade-choice cadence is designed (a meaningful choice at
   a stated interval, not whenever affordable); prefer deterministic
   progression for gating rewards, chance only for non-gating
   variety (retention evidence); return cadence (energy/regen-style
   timers) is a designed parameter with a stated target, or omitted
   entirely. Cross-links wave-1 core-loop skill for monotonicity and
   sink-before-source. Sources: gamedeveloper.com casual progression
   curve, gamedesignskills.com game-progression, dev.to currency-sink
   and economy-balancing articles, Google Play "Understanding Games
   that Retain".

Each file carries `## Trigger`, `## Procedure`, `## Output shape`, and
`## Related skills`, matching wave 1 so later manifest enrollment needs
no rework.

## Out of scope

- Changes to existing skills, `scripts/`, or the conformance checker.
- Manifest enrollment (`procedure_authored_skills.txt`,
  `issue_1996_use_when_source_manifest.txt`) — same stance as wave 1.
- 3D rig/mocap workflows, audio, monetization/IAP tuning, netcode.
- Any change to tm-dicequest itself.

## How you'll know it worked

- `python3 scripts/check_skill_conformance.py` prints `273 skills
  checked` (269 today + 4) and exits 0.
- `python3 -m pytest test/ -q` stays green.
- Each new `SKILL.md` `name:` matches its directory; each
  `description:` carries a distinct "Use when" trigger.
- Every numbered rule block carries a `source:` URL verified live
  during phase 2.
- The delivery record lists the research sources (issue acceptance).
