# Scout brief — issue #93 game skill wave 2

Mode: PARALLEL fan-out (4 concurrent WebSearch calls in the sweep,
2 in one deepening round). Stages used: 2 of 5, inside the budget.
Stopped at saturation.

## Category must-bes (what strong sources assume)

- Character animation runs on Disney's 12 principles adapted per game
  state — anticipation/follow-through measured in frames (1-frame
  anticipation transforms a jump; follow-through 1-3 frames), with an
  explicit state machine (idle/run/attack/hit/death) gating transitions
  and interrupts.
- Impact is frame-quantified, not vibes: hitstop bands scale with attack
  weight (light ~9 / medium ~11 / heavy ~13 frames in fighting-game
  canon), i-frames attach to specific recovery states, and knockback
  size is the combo-length control.
- Character readability is silhouette-first (~70% of read), shape
  language separates roles (enemy vs. friendly), and layered builds
  (trunk→limbs→head→details) never advance until the silhouette reads
  at distance.
- Web character animation stays on the compositor: transform/opacity
  only; sprite sheets animate via `steps()`, transitions for two-state
  changes, keyframes for frame-by-frame.
- Progression economy: sinks sized against sources (source>sink →
  inflation), exponential cost curves set the purchase interval as the
  pacing knob, return cadence is a designed parameter, and vendor-style
  deterministic sinks convert grind into deterministic progress.

## Performance axes the field competes on

1. Responsiveness (interruptible states, low input latency) vs.
   animation fidelity (full anticipation/recovery arcs).
2. Impact weight (hitstop/knockback magnitude) vs. game flow (combo
   pacing, repeated-action fatigue).
3. Silhouette clarity at shipped size vs. detail density.

## Adopt / skip

- ADOPT: frame-band tables (anticipation, hitstop by weight class) as
  condition-matched rules — exactly the codification cut-3/5 lacked.
- ADOPT: silhouette-first layered build order as a gating rule for
  SVG part rigs; shape language as the enemy-vs-player separator.
- ADOPT: compositor-only discipline + `steps()` for sprite states as
  the DOM/CSS character-animation contract.
- SKIP: 3D rig/mocap workflow content — repo's game family is
  HTML5/2D scoped.
- SKIP: monetization/LiveOps economy content — retention patterns yes,
  IAP tuning no (out of the repo's skill scope).

## Segment fit + gap line

Same segment as wave 1: decision-point skills for small-team HTML5/2D
games, sparse tier. GAP: wave 1 already meets loop-timing, juice
staging, and economy-monotonicity must-bes; missing are per-character
state machines & timing bands (skill 1), the combat impact contract
(skill 2), silhouette/rig composition (skill 3), and session-scale
pacing/sink-lifecycle/cadence (skill 4) — the four new skills target
exactly those, cross-linking wave 1 instead of restating it.

Sources:
- https://www.sprite-ai.art/guides/animation-principles
- https://www.gamedeveloper.com/production/the-12-principles-of-animation-in-video-games
- https://www.pixel-editor.com/articles/sprite-animation-fundamentals
- https://www.ssbwiki.com/Hitlag
- https://sonichurricane.com/?p=1043
- https://shane-sicienski.com/blog/blog-post-title-one-55pmn
- https://supersmashbros.fandom.com/wiki/Invincibility_frame
- https://pixune.com/blog/shape-language-technique/
- https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent
- https://nastyrodent.com/stylized-3d-characters-art-direction-principles/
- https://anim.works/silhouette-in-animation/
- https://web.dev/articles/animations-guide
- https://blog.logrocket.com/making-css-animations-using-a-sprite-sheet/
- https://www.joshwcomeau.com/animation/sprites/
- https://medium.com/googleplaydev/understanding-games-that-retain-1847b16c86a7
- https://dev.to/sam_novak_574b07811e18495/idle-game-economy-design-what-your-currency-sinks-actually-eat-1non
- https://dev.to/hiroshi_takamura_c851fe71/game-economy-balancing-how-to-tune-rewards-costs-and-progression-2ale
- https://www.gamedeveloper.com/design/creating-a-casual-game-progression-curve
- https://gamedesignskills.com/game-design/game-progression/
