#!/usr/bin/env python3
"""Three-way merge of the area checkers' copies of the model program, file by file, as round 2's integration did it
(git merge-file of each area's copy against the committed program). It never resolves a conflict.

  python3 -B merge_models.py --base "<committed model/ folder>" --area "A1=<area 1 model/ folder>" \\
         --area "A2=..." --area "A3=..." --out <scratch folder>

For each .py file in the base or any area copy:
  - no area changed it: the base's copy;
  - one area changed it (or several made the same change): that copy ("taken");
  - several areas changed it differently: git merge-file -p, one area after another, against the base
    ("merged clean", or "CONFLICT" with the number of conflict hunks and the line of each marker).
The merged folder is written under --out/model/ (conflict markers left in place where there are conflicts).
ok = no conflict. A conflict goes to Opus: which side, or what combination, is a judgement.
"""
import argparse
import os
import sys
import tempfile

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402


def pyfiles(d):
    out = {}
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x != "__pycache__"]
        for f in files:
            if f.endswith(".py"):
                p = os.path.join(root, f)
                out[os.path.relpath(p, d)] = open(H.guard_read(p), "rb").read()
    return out


def merge_file(cur, base, other, tmpdir):
    paths = []
    for name, data in (("cur", cur), ("base", base), ("other", other)):
        p = os.path.join(tmpdir, name)
        with open(p, "wb") as f:
            f.write(data)
        paths.append(p)
    r = H.run(["git", "merge-file", "-p", "-L", "merged", "-L", "base", "-L", "other"] + paths, timeout=120)
    return r["stdout"].encode("utf-8"), r["exit"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--area", action="append", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    H.guard_write(os.path.join(a.out, "x"))
    base = pyfiles(a.base)
    areas = []
    for s in a.area:
        name, _, d = s.partition("=")
        areas.append((name, pyfiles(d), H.rel(d)))
    names = sorted(set(base) | {f for _, fs, _ in areas for f in fs})
    rows, merged = [], {}
    with tempfile.TemporaryDirectory(dir=H.SCRATCH) as tmp:
        for f in names:
            b = base.get(f)
            changed = [(n, fs[f]) for n, fs, _ in areas if f in fs and fs[f] != b]
            row = dict(file=f, in_base=b is not None, changed_by=[n for n, _ in changed])
            if not changed:
                merged[f] = b
                row["result"] = "base"
            elif len({c for _, c in changed}) == 1:
                merged[f] = changed[0][1]
                row["result"] = "taken" if len(changed) == 1 else "taken (the same change in each)"
            else:
                cur, conflicts = changed[0][1], 0
                for n, other in changed[1:]:
                    cur, code = merge_file(cur, b or b"", other, tmp)
                    if code is None or code < 0:
                        H.refuse("git merge-file failed on %s" % f)
                    conflicts += code
                merged[f] = cur
                row["result"] = "CONFLICT" if conflicts else "merged clean"
                row["conflicts"] = conflicts
                row["marker_lines"] = [i for i, l in enumerate(cur.decode("utf-8", "replace").split("\n"), 1)
                                       if l.startswith(("<<<<<<< ", ">>>>>>> ")) or l == "======="]
            rows.append(row)
    for f, data in merged.items():
        p = os.path.join(a.out, "model", f)
        H.guard_write(p)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(data)
    conf = [r for r in rows if r["result"] == "CONFLICT"]
    H.emit(dict(ok=not conf, job="merge_models", base=H.rel(a.base), areas=[dict(name=n, dir=d) for n, _, d in areas],
                out=H.rel(os.path.join(a.out, "model")), files=len(rows), conflicts=conf,
                changed=[r for r in rows if r["result"] != "base"]))


if __name__ == "__main__":
    main()
