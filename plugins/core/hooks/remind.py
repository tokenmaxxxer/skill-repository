#!/usr/bin/env python3
"""Inject a standing reminder that this plugin's skills apply.

Skill descriptions are already always-on, so this adds pressure, not
information: the failure mode it targets is the model reading the task, not
thinking about skills, and answering directly. Two events cover the gap:

  UserPromptSubmit — every turn. SessionStart injects once and gets buried;
    repeating keeps the reminder adjacent to the request being judged.
  SubagentStart    — subagents start cold. They inherit no conversation and
    no earlier injection, so without this they never see the policy at all.

The reminder must never name individual skills. It is paid on every turn, and
a list here would be a second place to update on every skill added — one that
rots silently when someone forgets. Claude already has the descriptions; this
only has to make it look.

Every turn is reminded, with no prefilter for greetings or short prompts.
A prefilter only pays off when something expensive (e.g. a subprocess
retrieval) runs behind the gate; this only echoes a constant, so there is
nothing to save. A
prefilter would also be actively wrong here: a bare "응" / "그래" / "네" is how
a Korean user approves work, and that turn is the last injection point before
a long stretch with no further prompts — exactly the one worth keeping.

SubagentStart accepts only the JSON hookSpecificOutput form — plain stdout
fires the hook but reaches nothing (verified empirically; not documented).
UserPromptSubmit accepts either; both use JSON here for one code path.

Dependency-free (Python 3.9+ stdlib). Always exits 0 — a broken reminder must
never block a turn.
"""
from __future__ import annotations

import json
import sys

REMINDER = (
    "The skill-registry (core) skills are active. If one applies to this "
    "task, invoke it with the Skill tool before answering; use them "
    "actively. If none applies, proceed."
)

SUBAGENT_REMINDER = (
    "The skill-registry (core) skills are active. You are a subagent and "
    "inherit no conversation context, so nothing else will surface them: if "
    "one applies to your brief, invoke it with the Skill tool and use it "
    "actively. If none applies, proceed."
)


def emit(event: str, context: str) -> None:
    json.dump(
        {"hookSpecificOutput": {"hookEventName": event,
                                "additionalContext": context}},
        sys.stdout,
        ensure_ascii=False,
    )


def main() -> int:
    if "--subagent" in sys.argv:
        emit("SubagentStart", SUBAGENT_REMINDER)
    else:
        emit("UserPromptSubmit", REMINDER)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # never block a turn
