---
name: release-engineering-semver-bump-selection
description: Use when selecting a MAJOR/MINOR/PATCH version bump for a release, deciding whether a change is actually breaking, or versioning a pre-release/build-metadata artifact.
metadata:
  axis: semver-bump-selection
  rule_count_floor: 12
---

# Semver bump selection

## Trigger

Apply this skill when a release needs a version number: classifying a
change's severity (breaking / additive / fix-only), resolving which
bump wins when multiple changes land together, or versioning a
pre-release or build-metadata artifact.

## Procedure

1. Classify the change: removing/renaming a public export, signature,
   config key, or CLI flag is MAJOR (rule 1); an additive, non-breaking
   change is MINOR (rule 2); an internal-only bug fix is PATCH (rule 3).
2. When changes of different severities land in the same release, the
   release's version is set by the highest-severity change, never
   averaged (rule 4); when unsure whether a change is actually breaking,
   treat it as breaking (rule 5).
3. Accompany any MAJOR bump with a migration note (what changed, who's
   affected, what to do, when the old behavior disappears) (rule 6),
   and hold a scheduled-for-removal deprecated surface's actual removal
   for the next MAJOR rather than removing it in a MINOR/PATCH (rule
   7).
4. Correct over-cautious version churn by re-auditing releases against
   the actual API diff, rather than adding a second parallel versioning
   scheme (rule 8).
5. Version a pre-release/experimental feature with a pre-release
   identifier rather than a MINOR/MAJOR bump (rule 9), and use a `+`
   build-metadata suffix (never a new version) for artifacts differing
   only in build metadata (rule 10).
6. Propagate a MAJOR bump to a consuming library when a dependency's own
   MAJOR bump forces a change to the consumer's public contract (rule
   11), and when in doubt between two adjacent severities, bump higher
   (rule 12).

## Output shape

A selected version bump (MAJOR/MINOR/PATCH, or pre-release/build-
metadata identifier) for the release, with a migration note attached
when MAJOR, each traceable to the rule above that forced it.

## Rules

1. **When** a change removes or renames a public export, function
   signature, config key, or CLI flag that a consumer could already be
   depending on, **choose** a MAJOR bump — never fold it into MINOR/PATCH
   even if the removal "seems small."
   source: Semantic Versioning 2.0.0, spec item 8 — https://semver.org/spec/v2.0.0.md

2. **When** a change adds a new function, optional parameter, export, or
   CLI flag without altering any existing caller's behavior, **choose** a
   MINOR bump.
   source: Semantic Versioning 2.0.0, spec item 7 — https://semver.org/spec/v2.0.0.md

3. **When** a change only corrects internal behavior to match already-
   documented behavior (a bug fix) and touches no public interface,
   **choose** a PATCH bump.
   source: Semantic Versioning 2.0.0, spec item 6 — https://semver.org/spec/v2.0.0.md

4. **When** a MAJOR-worthy breaking change and a MINOR-worthy addition
   land in the same release, **choose** MAJOR — a release's version
   number is set by its highest-severity change, never averaged or
   chosen per-file.
   source: Semantic Versioning 2.0.0, spec item 8 (incompatible changes
   dominate) — https://semver.org/spec/v2.0.0.md

5. **When** unsure whether a change is actually breaking (e.g. a
   behavior change a consumer is unlikely to rely on), **choose** the
   higher bump — treat ambiguity as breaking rather than assume safety.
   source: jsmanifest, "Semantic Versioning: When to Bump Major, Minor,
   or Patch" — https://jsmanifest.com/semantic-versioning-when-to-bump

6. **When** a MAJOR bump ships, **choose** to accompany it with a
   migration note stating what changed, who is affected, what to do,
   and when the old behavior disappears — a bare version bump with no
   migration path is an incomplete release, not a complete one.
   source: PkgPulse, "Semantic Versioning: Breaking Changes Guide" —
   https://www.pkgpulse.com/blog/semantic-versioning-guide-breaking-changes-2026

7. **REMOVAL** — **when** a MINOR or PATCH release still carries a
   deprecated API surface that was scheduled for removal in this
   version, **choose** to hold the removal for the next MAJOR and instead
   only mark it deprecated in this release's changelog — do not perform
   the actual removal outside a MAJOR bump, even if the maintainer
   judges the surface unused.
   source: Semantic Versioning 2.0.0, spec item 8 — https://semver.org/spec/v2.0.0.md

8. **REMOVAL** — **when** version churn from over-cautious bumping (every
   PATCH bumped to MINOR "just in case") accumulates, **choose** to
   simplify by re-auditing recent releases against the actual API diff
   and correcting the versioning policy going forward, rather than
   adding a second parallel versioning scheme (e.g. a build-number
   suffix) to work around it.
   source: Baeldung, "A Guide to Semantic Versioning" —
   https://www.baeldung.com/cs/semantic-versioning

9. **When** a pre-release or experimental feature is versioned,
   **choose** a pre-release identifier (e.g. `-alpha.1`) rather than
   bumping MINOR/MAJOR for it — pre-release tags have lower precedence
   than the associated normal version and signal instability explicitly.
   source: Semantic Versioning 2.0.0, spec item 9 —
   https://semver.org/spec/v2.0.0.md

10. **When** two build artifacts share every version field but differ
    only in build metadata (e.g. a CI build number), **choose** to
    append build metadata with a `+` separator rather than mint a new
    version — build metadata does not participate in precedence
    comparisons.
    source: Semantic Versioning 2.0.0, spec item 10 —
    https://semver.org/spec/v2.0.0.md

11. **When** a dependency's own MAJOR bump forces a consuming library to
    change its public contract, **choose** to propagate a MAJOR bump to
    the consuming library too — a version bump is transitive across a
    breaking dependency change, not absorbed silently as a PATCH.
    source: Zuplo, "Semantic Versioning for APIs" —
    https://zuplo.com/learning-center/semantic-api-versioning

12. **When** in doubt between two adjacent severities on a specific
    change, **choose** to bump higher rather than lower — the cost of an
    unnecessary MAJOR is a consumer re-reading a changelog; the cost of
    a missed MAJOR is a silent production break.
    source: jsmanifest, "Semantic Versioning: When to Bump Major, Minor,
    or Patch" — https://jsmanifest.com/semantic-versioning-when-to-bump

## Related skills

- [release-engineering-changelog-entry-categorization](../release-engineering-changelog-entry-categorization/SKILL.md) — a semver bump and a changelog entry's category are usually decided from the same change; check both together.
