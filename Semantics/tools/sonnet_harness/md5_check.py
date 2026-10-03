#!/usr/bin/env python3
"""Check files against the md5s a record gives.

  python3 -B md5_check.py --expect "PATH=MD5" [--expect "PATH=MD5" ...]
  python3 -B md5_check.py --manifest MANIFEST.json      # {"files": [{"path": ..., "md5": ...}, ...]} or {"PATH": "MD5"}

Paths are relative to the repository root unless absolute. ok = every file exists and has its md5.
"""
import argparse
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expect", action="append", default=[])
    ap.add_argument("--manifest")
    a = ap.parse_args()
    pairs = []
    for s in a.expect:
        p, _, m = s.rpartition("=")
        pairs.append((p, m.strip().lower()))
    if a.manifest:
        man = H.load_json(a.manifest)
        items = man["files"] if isinstance(man, dict) and "files" in man else [dict(path=k, md5=v) for k, v in man.items()]
        pairs += [(x["path"], x["md5"].lower()) for x in items]
    if not pairs:
        H.refuse("give --expect PATH=MD5 or --manifest")
    rows = []
    for p, m in pairs:
        full = p if os.path.isabs(p) else os.path.join(H.REPO, p)
        if H.KEYLIKE.search(full):
            H.refuse("refused: a key-like path")
        got = H.md5_file(full) if os.path.isfile(full) else None
        rows.append(dict(path=p, expected=m, got=got, ok=got == m))
    H.emit(dict(ok=all(r["ok"] for r in rows), job="md5_check", checked=len(rows),
                mismatches=[r for r in rows if not r["ok"]], files=rows))


if __name__ == "__main__":
    main()
