---
name: api-design-tool-landscape
description: Use when an interface spec, payload schema, new API version, or cross-service contract is about to ship without a generated mock server, runtime schema validator, client SDK, or consumer-driven contract test.
metadata:
  axis: tool-landscape
  rule_count_floor: 4
---

# Tool-landscape learnings

Distilled design moves from the Claude Code plugin/skill ecosystem this
role's practitioners actually use (issue #1199, 2026-08-14 amendment,
northpole req#1/req#5), folded into this role's own decision axes —
never a tool catalog. Adoption-evidence citations (stars, install
counts, marketplace listing) and fetched-source URLs are in
`docs/issue-1199/reports/api-design/scout-brief.md` in the
`on-the-record` repo; this file states only the design move and which
existing axis it upgrades.

## Trigger

Apply this skill when an interface spec is published, a payload schema
is defined, a new API version or resource ships, or two services need
to agree on a resource's shape across a version boundary — before
declaring any of those done.

## Procedure

1. Generate a mock server directly from the published interface spec
   rather than hand-writing a separate fixture server (rule 1).
2. Mirror the payload schema as an enforced runtime validator at the
   service boundary, not just spec documentation (rule 2).
3. Generate client SDK(s) from the interface spec as part of the same
   change that ships a new version or resource (rule 3).
4. Generate a consumer-driven contract test from the interface spec
   when two services must agree on a resource's shape across a version
   boundary (rule 4).

## Output shape

For the interface-spec change under review: a generated mock server, a
runtime validator wired to the service boundary, regenerated client
SDK(s), and (when a version boundary is involved) a consumer-driven
contract test — each an artifact, not a policy statement.

## Rules

1. When an interface-spec is published, generate a mock server directly
   from that same spec (rather than hand-writing a separate fixture
   server) so consumers can integrate against the contract before the
   real implementation exists — the design move behind the
   `api-mock-server` Claude Code skill (generates mock servers "from
   OpenAPI specs for testing"). Upgrades [[interface-spec]]: a spec is
   not done until it can drive a mock, which is also the cheapest
   falsifiability check that the spec is actually complete enough to
   implement against.

2. When a payload schema is defined in the interface-spec, mirror it as
   an enforced runtime validator (JSON Schema/Zod/Joi-equivalent) at the
   service boundary rather than leaving the spec as documentation the
   implementation may silently drift from — the design move behind the
   `api-schema-validator` Claude Code skill (validates "API schemas with
   JSON Schema, Joi, Yup, or Zod"). Upgrades [[payload-design]]:
   schema rules currently describe shape but not that the shape must be
   mechanically enforced where requests actually land.

3. When a new API version or resource ships, generate its client SDK(s)
   from the interface-spec as part of that same change rather than
   leaving consumers to hand-write clients against the raw spec — the
   design move behind the `api-sdk-generator` Claude Code skill
   (generates "client SDKs from OpenAPI specs for multiple languages").
   Upgrades [[versioning-evolution]]: a version bump's consumer-facing
   cost is measured by how many hand-written clients must be touched,
   which SDK generation collapses to a regeneration step instead.

4. When two services need to agree on a resource's shape across a
   version boundary, generate a consumer-driven contract test from the
   interface-spec (asserting the provider still satisfies what the
   consumer actually calls) rather than relying on the spec and the
   deprecation-plan prose alone to keep both sides honest — the design
   move behind the `api-contract-generator` Claude Code skill
   (generates "API contracts for consumer-driven contract testing").
   Upgrades [[versioning-evolution]] and [[deprecation-plan]]: both
   currently state compatibility as a policy; this makes it a run
   artifact that fails loudly when broken.
