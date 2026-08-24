#!/usr/bin/env python3
"""Corpus lint for issue-109 retired vocabulary.

Reads scripts/retired_vocabulary.txt — the committed list of retired
rulebook-era terms (state names, role-state phrasings, roles-as-entities,
retired record types, wake machinery, unconditional test-default
guidance) — and asserts zero matches across every skills/**/*.md file
(SKILL.md and references/ alike).

The vocabulary file also carries an allowlist: ``ALLOW|<regex>|<pointer>``
entries for terms verified still live (each with its verification
pointer). A line that matches a retired pattern is exempt when it also
matches an ALLOW regex.

Exit 0 with a summary on success; exit 1 listing every violation as
``path:lineno: [pattern] line-excerpt``.
"""
import os
import re
import sys

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, "..", "skills")
VOCAB = os.path.join(HERE, "retired_vocabulary.txt")


def load_vocabulary(path=VOCAB):
    """Return (patterns, allows): compiled retired patterns and allow rules.

    patterns: list of (source_regex, compiled) — flags line format
    ``<flags>|<regex>`` with i=case-insensitive, c=case-sensitive.
    allows: list of (compiled_regex, pointer).
    """
    patterns, allows = [], []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line or line.lstrip().startswith("#"):
                continue
            if line.startswith("ALLOW|"):
                _, rx, pointer = line.split("|", 2)
                allows.append((re.compile(rx, re.IGNORECASE), pointer))
                continue
            flags, rx = line.split("|", 1)
            patterns.append(
                (rx, re.compile(rx, re.IGNORECASE if "i" in flags else 0)))
    return patterns, allows


def iter_markdown(root=ROOT):
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def check(root=ROOT, vocab=VOCAB):
    patterns, allows = load_vocabulary(vocab)
    errors = []
    files = 0
    for path in iter_markdown(root):
        files += 1
        rel = os.path.relpath(path, os.path.join(root, ".."))
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                for rx_src, rx in patterns:
                    if not rx.search(line):
                        continue
                    if any(a.search(line) for a, _ in allows):
                        continue
                    errors.append("%s:%d: [%s] %s"
                                  % (rel, lineno, rx_src, line.strip()[:120]))
    return errors, files, len(patterns), len(allows)


def main():
    errors, files, n_pat, n_allow = check()
    if errors:
        print("retired-vocabulary lint: %d violation(s):" % len(errors))
        for e in errors:
            print("  " + e)
        return 1
    print("retired-vocabulary lint: OK — %d files scanned, %d patterns, "
          "%d allowlist entries, 0 matches" % (files, n_pat, n_allow))
    return 0


if __name__ == "__main__":
    sys.exit(main())
