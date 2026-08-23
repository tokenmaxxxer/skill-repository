---
name: ux-engineering-color-visibility--status-palette-sprawl
---
Our CI pipeline dashboard shows each job as a colored dot. Over two years
the status set has grown to nine simultaneous colors:

  queued (gray), starting (light blue), running (blue), passing (green),
  flaky-pass (yellow-green), warning (yellow), failing (orange-red),
  failed (red), cancelled (dark gray)

Colorblind users report they cannot tell passing / flaky-pass / warning
apart, or failing / failed. Several pairs also sit under 3:1 contrast from
each other and from the dark background.

The team's proposed fix, already ticketed: keep all nine colors and add a
tiny unique icon inside each dot, plus a pattern overlay for the three
green-yellow ones, "so nobody loses information they have today." Each
status maps to a distinct DB state, though triage treats starting/running
the same, flaky-pass/warning the same, and failing/failed the same.

As the reviewer, decide the remediation approach for this status system and
spell it out concretely.
