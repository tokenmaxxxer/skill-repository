#!/usr/bin/env python3
"""Rank skills by measured use (issue #102).

Aggregates measure_skill_invocation.py output (per-session mounted/invoked
skills from ~/.tokenmaxxxer/work logs) with applied `skill-verdict:` lines
grepped from committed implementation reports. Score = 2*invoked +
2*verdicts + 1*mounted; ties broken by invoked desc, verdicts desc, name asc.
Operator-machine tool: depends on local log/report paths below.
"""
import json, subprocess, re, glob, collections, sys

MEASURE = "/home/jwjung/.claude/plugins/marketplaces/tokenmaxxxer/scripts/measure_skill_invocation.py"

invoked = collections.Counter()
mounted = collections.Counter()
sessions = 0
out = subprocess.run(["python3", MEASURE], capture_output=True, text=True).stdout
for line in out.splitlines():
    try:
        rec = json.loads(line)
    except json.JSONDecodeError:
        continue
    if rec.get("status") != "measured":
        continue
    sessions += 1
    for s in rec.get("invoked_skills", []):
        invoked[s] += 1
    for s in rec.get("mounted", []):
        mounted[s] += 1

# skill-verdict lines in reports (applied verdicts)
verdict = collections.Counter()
patterns = [
    "/home/jwjung/tm-dicequest/docs/issue-*/reports/*.md",
    "/home/jwjung/.claude/plugins/marketplaces/tokenmaxxxer/docs/**/*.md",
]
vre = re.compile(r"skill-verdict:\s*([a-z0-9-]+)")
for pat in patterns:
    for f in glob.glob(pat, recursive=True):
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in vre.finditer(text):
            verdict[m.group(1)] += 1

score = collections.Counter()
for s, c in invoked.items():
    score[s] += 2 * c          # actual invocation weighs double
for s, c in verdict.items():
    score[s] += 2 * c          # applied verdict = evidence of real use
for s, c in mounted.items():
    score[s] += c              # mounted = exposure

ranked = sorted(score, key=lambda s: (-score[s], -invoked[s], -verdict[s], s))

print(f"sessions_measured\t{sessions}")
print("rank\tskill\tinvoked\tverdicts\tmounted\tscore")
for i, s in enumerate(ranked[:30], 1):
    print(f"{i}\t{s}\t{invoked[s]}\t{verdict[s]}\t{mounted[s]}\t{score[s]}")
