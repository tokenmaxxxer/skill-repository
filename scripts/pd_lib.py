"""Shared parsing helpers for progressive disclosure (issue-100).

A SKILL.md is split into frontmatter + body. The body is a preamble plus
a list of `## ` sections. Sections are classified KEEP (Trigger /
Procedure / Output shape and other invocation-time framing) or MOVE
(full rule text, citations, evidence legends) — MOVE content lives in
references/rules.md, and the body carries a parseable rule index.

Rule extraction supports the corpus's four rule formats:
  a. `**Rule <id> — title.**` blocks (Condition:/Choice:/Source: lines)
  b. `### <n>. <title>` blocks with `- condition:` / `- choice:` bullets
  c. top-level markdown numbered-list rules (`1. When ... , do ...`)
  d. `## R<n> — <title>` heading-per-rule sections
Sections with no parseable rules are indexed section-level with ids
S1..Sn.
"""
import re
from collections import Counter

KEEP_RE = re.compile(
    r"^##\s+("
    r"trigger|procedure|the procedure|procedures|output shape|verdict|"
    r"first[:,]|related skills|when not to delegate|when this skill says stop|"
    r"where this skill fits|the pattern$|what this skill is actually for|"
    r"report format"
    r")",
    re.I,
)

RULE_A = re.compile(r"^\*\*Rule\s+([0-9][\w.\-]*)\s*(\[[A-Z]+\])?\s*[—-]\s*(.*)")
RULE_B = re.compile(r"^###\s+([0-9][\w.\-]*)\.\s+(.*)")
RULE_C = re.compile(r"^([0-9]{1,2})\.\s+(\S.*)")
RULE_D = re.compile(r"^##\s+(R[0-9]+)\s*[—-]\s*(.*)")


def split_frontmatter(text):
    lines = text.split("\n")
    assert lines[0] == "---", "no frontmatter"
    end = lines.index("---", 1)
    return lines[: end + 1], lines[end + 1 :]


def sections(body_lines):
    """Yield (heading_or_None, lines) — first item is the preamble."""
    out = []
    cur_head, cur = None, []
    fence = False
    for ln in body_lines:
        if ln.startswith("```"):
            fence = not fence
        if not fence and ln.startswith("## "):
            out.append((cur_head, cur))
            cur_head, cur = ln, []
        else:
            cur.append(ln)
    out.append((cur_head, cur))
    return out


def is_keep(heading):
    if heading is None:
        return True
    return KEEP_RE.match("## " + heading[3:].strip()) is not None


def _one_line(text, limit=170):
    s = re.sub(r"\s+", " ", text).strip().rstrip(".")
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def extract_rules(lines):
    """Extract rules from a flat list of lines (one or more sections).

    Returns list of dicts: {id, cond, verdict}. Ids are made unique.
    Heading lines (##) reset numbered-list section counters.
    """
    rules = []
    fence = False
    i = 0
    sec_ord = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            fence = not fence
            i += 1
            continue
        if fence:
            i += 1
            continue
        if ln.startswith("## "):
            sec_ord += 1
            m = RULE_D.match(ln)
            if m:
                rules.append({"id": m.group(1), "cond": _one_line(m.group(2)), "verdict": ""})
            i += 1
            continue
        m = RULE_A.match(ln)
        if m:
            rid = m.group(1).rstrip(".")
            title = m.group(3)
            j = i + 1
            cond = verd = ""
            while j < len(lines) and not RULE_A.match(lines[j]) and not lines[j].startswith("## "):
                if lines[j].startswith("Condition:"):
                    k = j
                    buf = [lines[j][len("Condition:"):]]
                    while k + 1 < len(lines) and lines[k + 1] and not re.match(r"^(Choice|Source|Condition):", lines[k + 1]) and not lines[k + 1].startswith(("**", "## ")):
                        k += 1
                        buf.append(lines[k])
                    cond = " ".join(buf)
                if lines[j].startswith("Choice:") and not verd:
                    verd = lines[j][len("Choice:"):]
                j += 1
            tag = (m.group(2) + " ") if m.group(2) else ""
            rules.append({"id": rid, "cond": _one_line(tag + (cond or title)), "verdict": _one_line(verd or title, 120)})
            i = j
            continue
        m = RULE_B.match(ln)
        if m:
            rid = m.group(1)
            title = m.group(2)
            j = i + 1
            cond = verd = ""
            while j < len(lines) and not RULE_B.match(lines[j]) and not lines[j].startswith("## "):
                s = lines[j].strip()
                if s.startswith("- condition:"):
                    cond = s[len("- condition:"):]
                if s.startswith("- choice:") and not verd:
                    k = j
                    buf = [s[len("- choice:"):]]
                    while k + 1 < len(lines) and lines[k + 1].strip() and not lines[k + 1].strip().startswith("- "):
                        k += 1
                        buf.append(lines[k].strip())
                    verd = " ".join(buf)
                j += 1
            rules.append({"id": rid, "cond": _one_line(title), "verdict": _one_line(verd or title, 140)})
            i = j
            continue
        m = RULE_C.match(ln)
        if m and not ln.startswith(" "):
            num = m.group(1)
            j = i + 1
            buf = [m.group(2)]
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or lines[j] == ""):
                if lines[j].strip().lower().startswith(("source:", "counter-example:", "why:", "evidence:")):
                    break
                buf.append(lines[j].strip())
                j += 1
            stmt = " ".join(b for b in buf if b)
            rid = f"{max(sec_ord, 1)}.{num}"
            rules.append({"id": rid, "cond": _one_line(stmt), "verdict": ""})
            while j < len(lines) and not RULE_C.match(lines[j]) and not lines[j].startswith("## "):
                j += 1
            i = j
            continue
        i += 1
    # de-duplicate ids
    seen = Counter()
    for r in rules:
        seen[r["id"]] += 1
        if seen[r["id"]] > 1:
            r["id"] = f"{r['id']}({seen[r['id']]})"
    return rules


INDEX_LINE = re.compile(r"^- ([\w.()\-]+) — (.*)$")


def parse_index(body_lines):
    """Return list of ids from the body's '## Rule index' section (None if absent)."""
    secs = sections(body_lines)
    for head, lines in secs:
        if head and head[3:].strip().lower() == "rule index":
            ids = []
            for ln in lines:
                m = INDEX_LINE.match(ln)
                if m:
                    ids.append(m.group(1))
            return ids
    return None


def reference_ids(ref_lines):
    """Ids extractable from a references/rules.md, incl. S-section anchors."""
    ids = [r["id"] for r in extract_rules(ref_lines)]
    for ln in ref_lines:
        m = re.match(r"^## \[S(\d+)\]", ln)
        if m:
            ids.append(f"S{m.group(1)}")
    return ids


def tokens(text):
    return Counter(re.findall(r"[0-9A-Za-z가-힣]+", text.lower()))
