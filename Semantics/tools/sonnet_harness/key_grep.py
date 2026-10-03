#!/usr/bin/env python3
"""The key grep before every commit, run exactly as the orchestrator gives it:

  grep -rEln "(sk-[A-Za-z0-9_-]{16,}|tp-[a-z0-9]{20,}|api[_-]?key\\s*[:=]\\s*['\\"]?[A-Za-z0-9_\\-]{16,}|[0-9a-f]{32}\\.[A-Za-z0-9]{16})" Semantics/

  python3 -B key_grep.py [--root Semantics] [--paths FILE ...]

It prints the NAMES of the files that match (grep -l) and never a matched line, so no key reaches the screen.
With --paths it greps only those files (the ones about to be committed). ok = no file matches.
"""
import argparse
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402

PATTERN = r"""(sk-[A-Za-z0-9_-]{16,}|tp-[a-z0-9]{20,}|api[_-]?key\s*[:=]\s*['"]?[A-Za-z0-9_\-]{16,}|[0-9a-f]{32}\.[A-Za-z0-9]{16})"""


def grep(targets, cwd):
    r = H.run(["grep", "-rEln", PATTERN, "--"] + targets, cwd=cwd, timeout=300)
    files = [l for l in r["stdout"].split("\n") if l.strip()]
    # grep exits 0 on a match, 1 on none, 2 on an error
    return dict(exit=r["exit"], timed_out=r["timed_out"], files=files, error=r["stderr"].strip()[:300] if r["exit"] == 2 else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Semantics")
    ap.add_argument("--paths", nargs="*")
    a = ap.parse_args()
    targets = a.paths if a.paths else [a.root.rstrip("/") + "/"]
    g = grep(targets, H.REPO)
    ok = g["exit"] == 1 and not g["files"] and not g["timed_out"]
    H.emit(dict(ok=ok, job="key_grep", command='grep -rEln "<the pattern>" ' + " ".join(targets), matching_files=g["files"],
                grep_exit=g["exit"], error=g["error"]))


if __name__ == "__main__":
    main()
