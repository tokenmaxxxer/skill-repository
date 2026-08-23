---
name: release-engineering-branching-release-strategy
description: >-
  Use when choosing between trunk-based development, release branches, feature
  flags, or hotfix branching for a service, or deciding when to retire a stale
  release/feature branch. Trigger on requests like "trunk-based or release
  branches", "hotfix from the last release tag", "long-lived feature branch
  keeps conflicting", "브랜치 전략 어떻게 가져갈까". Do NOT use for a feature flag's
  expiration and removal lifecycle (use
  release-engineering-release-cadence-and-toil).
metadata:
  axis: branching-release-strategy
  rule_count_floor: 12

---

# Branching and release strategy

## Trigger

Apply this skill when choosing how a team should branch and release —
trunk-based development vs. long-lived release branches, whether
incomplete multi-day work should live behind a feature flag instead of a
branch, how to patch an old release, how to bundle config with a
release, or when to retire a release branch or a long-lived-branch
habit in favor of trunk-based development.

## Procedure

1. Default to trunk-based development for a team integrating at least
   daily (rule 1), using feature flags rather than long-lived branches
   for multi-day work (rule 2).
2. For a service needing a stabilization window before a scheduled
   release, cut a release branch from trunk near the release date and
   restrict it to cherry-picked fixes only (rule 3).
3. When patching an old release, cherry-pick onto that release's branch
   using the original toolchain, not the current one (rule 4).
4. Decide how to bundle config by its change frequency relative to the
   binary (rule 5), and favor smaller, more frequent releases when
   velocity and testing burden are in tension (rule 6).
5. At scale, prefer a self-service release process over a centralized
   gatekeeper (rule 7).
6. Where long-lived feature branches are accumulating conflicts, or a
   codebase runs both long-lived branches and feature flags for the
   same class of change, migrate toward trunk-based development and
   retire the redundant path rather than invest further in either
   (rules 8, 10).
7. Retire a release branch once its stabilization window has shipped,
   rather than leave it open indefinitely (rule 9), and prefer
   trunk-based development's per-commit control once branching overhead
   itself is the release bottleneck (rule 11).
8. For a production hotfix while trunk holds unreleased work, cut from
   the last known-good release tag and cherry-pick forward, not from
   current trunk (rule 12).

## Output shape

A stated branching/release strategy (trunk-based, release-branch, or
hotfix-branch) for the situation at hand, each choice traceable to the
rule above that forced it, plus, where applicable, a stale
branch/flag-retirement action.

## Rules

1. **When** a team integrates changes at least daily and wants the
   ability to release from the main line at any time, **choose**
   trunk-based development (short-lived branches merged straight to
   trunk) over long-lived release branches.
   source: LaunchDarkly, "Git Branching Strategies vs. Trunk-Based
   Development" —
   https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/

2. **When** a feature needs multiple days/weeks of incremental work but
   the team is on trunk-based development, **choose** to merge
   incomplete work behind a feature flag rather than keep a long-lived
   feature branch open — this is what makes trunk-based development
   viable for multi-day work.
   source: Flagsmith, "How to Use Feature Flags for Trunk-Based
   Development" —
   https://www.flagsmith.com/blog/trunk-based-development-feature-flags

3. **When** a service needs a stabilization window before a scheduled
   release (e.g. regulated or hardware-adjacent software with a fixed
   release train), **choose** a release-branch cut from trunk near the
   release date, with only fixes cherry-picked onto it — never continued
   feature development on the release branch itself.
   source: sre.google, "Release Engineering" (hermetic-build/versioning
   discussion of release branches) — https://sre.google/sre-book/release-engineering/

4. **When** an old release must be patched (e.g. a security fix on a
   version customers still run), **choose** to cherry-pick the fix onto
   that release's branch using the *original* build toolchain/compiler
   version from that time — not the current toolchain — to avoid
   introducing incompatibilities the original release never had.
   source: sre.google, "Release Engineering" (hermetic builds) —
   https://sre.google/sre-book/release-engineering/

5. **When** choosing how to bundle configuration with a release,
   **choose** based on change frequency: config that changes often goes
   in an external system separate from the binary; config that changes
   once per release is bundled with the binary in one package; config
   that must update independently of the binary is packaged separately
   with a shared label.
   source: sre.google, "Release Engineering" —
   https://sre.google/sre-book/release-engineering/

6. **When** release velocity and testing burden are in tension,
   **choose** more frequent, smaller releases over infrequent, large
   ones — fewer changes between versions simplifies both testing and
   troubleshooting when something breaks.
   source: sre.google, "Release Engineering" —
   https://sre.google/sre-book/release-engineering/

7. **When** many product teams need to release independently at scale,
   **choose** a self-service release process (teams trigger their own
   releases; humans engage only when something goes wrong) over a
   centralized release-engineering gatekeeper for every release.
   source: sre.google, "Release Engineering" —
   https://sre.google/sre-book/release-engineering/

8. **When** long-lived feature branches accumulate merge conflicts and
   integration risk grows with branch age, **choose** to migrate the
   team toward trunk-based development rather than invest further in
   branch-merge tooling — the risk source is branch lifetime itself, not
   the merge process.
   source: Ardalis, "Trunk-Based Development vs. Long-Lived Feature
   Branches" — https://ardalis.com/trunk-based-development-vs-long-lived-feature-branches/

9. **REMOVAL** — **when** a release branch has served its stabilization
   window and shipped, **choose** to delete (or archive) the branch
   rather than leave it open indefinitely as a second parallel trunk —
   an open old release branch invites accidental commits that never
   reach production.
   source: LaunchDarkly, "Git Branching Strategies vs. Trunk-Based
   Development" —
   https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/

10. **REMOVAL** — **when** a codebase runs both long-lived feature
    branches and feature flags for the same class of change, **choose**
    to retire the long-lived-branch path for that class rather than keep
    two parallel risk-management mechanisms — the overlap doubles review
    surface without doubling safety.
    source: Harness, "Trunk-based vs. Feature-based Development" —
    https://www.harness.io/blog/trunk-based-vs-feature-based-development

11. **When** classic branching's overhead (merge queues, integration
    freezes) is the actual bottleneck slowing releases, **choose**
    trunk-based development's granular, per-commit control over
    continuing to add branch-management process on top of the existing
    strategy.
    source: getunleash.io, "Trunk-based development: process, examples,
    strategy" — https://www.getunleash.io/blog/how-to-implement-trunk-based-development-a-practical-guide

12. **When** a hotfix is needed for production while trunk holds
    unreleased, unstable work, **choose** to cut the hotfix from the
    last known-good release tag (not from current trunk) and cherry-pick
    forward, so the fix ships without pulling in trunk's in-flight
    changes.
    source: sre.google, "Release Engineering" (rollback/build-artifact
    tracking) — https://sre.google/sre-book/release-engineering/
