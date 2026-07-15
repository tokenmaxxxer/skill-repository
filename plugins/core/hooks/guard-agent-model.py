#!/usr/bin/env python3
"""PreToolUse guard: an Agent call must say which model tier it wants.

The failure this kills is silent tier inheritance. Omitting `model` runs the
child on the CALLER's model, so one expensive lane quietly fans out into an
expensive cascade — measured in this repo's history: a reasoner-tier research
lane spawned three grandchildren, all inheriting its tier, +221k tokens that
nobody chose. The cost bug is never the tier someone picked; it is the tier
nobody picked.

Deny, don't rewrite. Silently downgrading unspecified calls to a cheap tier
would also "fix" the cascade, but it caps quality invisibly — the same run
showed the expensive tier catching consolidated-subsidiary double counts and
fabricated citations that the cheap tier walked past. The guard forces an
explicit choice and gets out of the way; model-routing (this plugin's skill)
is the policy for making that choice.

Two rules, one deny path:
  1. The tier must be CHOSEN — `model` explicit on every bare-type call.
  2. The tier must be one the team runs — sonnet, opus, or fable. haiku is
     below this registry's quality floor (team decision, 2026-07-15): every
     brief here carries judgment the bottom tier walks past, and a cheap
     wrong answer costs more than the tokens it saves.

Exemptions:
  - subagent_type containing ":" — plugin agents (core:executor,
    core:reasoner) pin their tier in frontmatter; that pinned tier IS
    the explicit choice (and both core agents sit inside the allowed
    set).

Uniform by design: the PreToolUse payload carries no depth/parent signal
(verified empirically — transcript_path shows the main session even for a
subagent's spawn), so depth-aware rules are impossible. Requiring the choice
at every level is the rule that needs no depth.

Safety: PreToolUse exit 2 BLOCKS the call with stderr as reason, and a hook
crash must never take Agent down with it — everything is wrapped to exit 0
(fail-open). Nested spawns are covered: this hook fires for subagents'
Agent calls too (verified empirically).
"""
from __future__ import annotations

import json
import sys


ALLOWED_TIERS = ("sonnet", "opus", "fable")


def deny(reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # unreadable payload — never block on our own failure

    tool_input = payload.get("tool_input") or {}
    subagent_type = tool_input.get("subagent_type") or ""
    if ":" in subagent_type:
        return 0  # plugin agent — tier pinned in its frontmatter

    model = (tool_input.get("model") or "").strip().lower()
    if not model:
        deny(
            "Agent call rejected: no `model` specified. Without it the "
            "subagent inherits THIS conversation's model tier — and if it "
            "spawns its own subagents they inherit it too, which is how one "
            "delegation quietly becomes an expensive cascade. Retry the same "
            "call with `model` set explicitly: `sonnet` for production and "
            "exploration work, `opus` for judgment-heavy briefs, `fable` "
            "only for the hardest long-horizon briefs (see the model-routing "
            "skill). Inheriting the session tier on purpose is fine — say so "
            "by passing its name."
        )
        return 0

    if not any(t in model for t in ALLOWED_TIERS):
        deny(
            f"Agent call rejected: model `{model}` is outside this team's "
            "allowed tiers (sonnet / opus / fable). haiku and other tiers "
            "sit below the registry's quality floor — a cheap wrong answer "
            "costs more than the tokens it saves. Retry with `sonnet` for "
            "production/exploration, `opus` for judgment-heavy briefs, or "
            "`fable` for the hardest long-horizon work."
        )
        return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # exit 2 would block the call; a broken guard must not
