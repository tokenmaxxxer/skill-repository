---
name: release-engineering-release-cadence-and-toil
description: Use when deciding release cadence, whether a release-process task is worth automating, or when to create/expire/remove a feature flag.
axis: release-cadence-and-toil
rule_count_floor: 12
---

# Release cadence and toil reduction

## Trigger

Apply this skill when setting release cadence, judging whether a
recurring release task counts as toil worth automating, or managing a
feature flag's lifecycle (creation, expiration, retirement).

## Procedure

1. Favor more frequent, smaller releases when cadence and
   testing/troubleshooting burden trade off (rule 1), and automate a
   release task once a machine could do it as well as a human, or the
   need for it could be designed away (rule 2).
2. At scale, prefer a self-service, role-based release process over a
   centralized release engineer approving every release (rule 3).
3. Give every new feature flag a real expiration date at creation time
   (rule 4), scoped narrowly rather than as one mega-flag (rule 6).
4. When a flag's expiration date arrives, force an explicit decision —
   remove it, or extend with a new date and reason — rather than let it
   silently pass (rule 7).
5. When removing a flag, trace every read of its variable to completion
   before deleting (rule 8), remove it once it reaches 100% rollout
   with no remaining kill-switch need (rule 5), and archive rather than
   hard-delete its record (rule 9).
6. Fold flag removal into the definition of done for the feature it
   gated, rather than treat cleanup as a deferred special project (rule
   10).
7. When toil exceeds roughly half the team's time, prioritize
   automating it over new release-process feature work (rule 11), and
   treat "human judgment is needed here" as a prompt to check for poor
   system design before accepting it as a genuine judgment need (rule
   12).

## Output shape

A stated release cadence or automation/toil decision, and, where a flag
lifecycle is involved, its expiration date and removal status — each
traceable to the rule above that forced it.

## Rules

1. **When** release cadence and testing/troubleshooting burden trade
   off against each other, **choose** more frequent, smaller releases —
   fewer changes between versions makes both testing and any needed
   troubleshooting simpler.
   source: sre.google, "Release Engineering" —
   https://sre.google/sre-book/release-engineering/

2. **When** deciding whether a release-process task is worth automating,
   **choose** automation if a machine could do it as well as a human, or
   if the need for the task could be designed away — that is the
   definition of toil, and toil is the automation backlog.
   source: sre.google, "Eliminating Toil" —
   https://sre.google/sre-book/eliminating-toil/

3. **When** many product teams need independent release velocity,
   **choose** a self-service, button-press release process with
   role-based access control, engaging a human only when something goes
   wrong — over a centralized release engineer approving every release.
   source: sre.google, "Release Engineering" —
   https://sre.google/sre-book/release-engineering/

4. **When** a feature flag is created, **choose** to set a real
   expiration date at creation time (a calendar date, not "someday") —
   an undated flag has no forcing function to ever get revisited.
   source: LaunchDarkly, "Reducing technical debt from feature flags" —
   https://launchdarkly.com/docs/guides/flags/technical-debt

5. **When** a feature flag reaches 100% rollout to its intended
   audience with no remaining need for a kill switch, **choose** to
   remove the flag and its now-dead branches from the codebase — a
   fully-rolled-out flag serves no further purpose.
   source: DevOps.com, "Prevent Technical Debt by Knowing When to Remove
   Feature Flags" —
   https://devops.com/prevent-technical-debt-by-knowing-when-to-remove-feature-flags/

6. **When** designing a new feature flag, **choose** a narrowly scoped
   flag over one mega-flag controlling an entire feature area — a
   focused flag can be phased out independently as its piece stabilizes,
   while a broad flag's removal blocks on every piece finishing at once.
   source: Mixpanel, "Feature flag cleanup: how to manage technical debt
   before it manages you" — https://mixpanel.com/blog/feature-flag-cleanup/

7. **When** a flag's expiration date arrives, **choose** to force an
   explicit decision (remove it, or extend with a new date and a stated
   reason) rather than let the date silently pass with no action — the
   date's value is the forced conversation, not the date itself.
   source: LaunchDarkly, "Reducing technical debt from feature flags" —
   https://launchdarkly.com/docs/guides/flags/technical-debt

8. **When** removing a flag, **choose** to trace every place the flag's
   variable is read (not just its definition) and follow each branch to
   completion before deleting — a partial removal that leaves a dead
   read path can silently reintroduce the old default.
   source: FlagShark, "The Complete Guide to Managing Feature Flag
   Technical Debt" — https://flagshark.com/blog/feature-flag-technical-debt-guide/

9. **When** a flag is retired, **choose** to archive/deprecate rather
   than hard-delete its record in the flag-management system — the
   history of what the flag controlled and when it flipped stays useful
   for later incident investigation.
   source: LaunchDarkly, "Reducing technical debt from feature flags" —
   https://launchdarkly.com/docs/guides/flags/technical-debt

10. **REMOVAL** — **when** flag cleanup is treated as a special,
    scheduled "big cleanup project," **choose** instead to fold flag
    removal into the definition of done for the feature the flag
    gated — a deferred cleanup project reliably never happens, while a
    per-feature removal step does.
    source: FlagShark, "The Complete Guide to Managing Feature Flag
    Technical Debt" — https://flagshark.com/blog/feature-flag-technical-debt-guide/

11. **REMOVAL** — **when** toil (manual, repetitive, automatable,
    tactical release work) exceeds roughly half of the release
    engineering team's time, **choose** to prioritize automating that
    toil over taking on more release-process feature work — SRE's
    stated target keeps engineering (novel, enduring-value) work at
    >=50% and toil at <=50%.
    source: sre.google, "Eliminating Toil" (the 50% target) —
    https://sre.google/sre-book/eliminating-toil/

12. **When** a release step's justification is "human judgment is
    needed here," **choose** to first check whether that step exists
    because of poor system design rather than a genuine need for
    judgment — the toil chapter explicitly warns against using
    "judgment needed" as an excuse to avoid fixing a system that should
    not require manual judgment at all.
    source: sre.google, "Eliminating Toil" —
    https://sre.google/sre-book/eliminating-toil/
