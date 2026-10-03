#!/usr/bin/env python3
"""Run the claim suite of a model and compare it, claim by claim and part by part, with a recorded result.

  python3 -B run_claims.py --model-dir "<folder holding model/>" --out-dir <scratch folder>
         [--claim FC30.new1 ...] [--scale 4] [--time-cap 45] [--timeout 1800]
         [--expect "<formal claims ... .json>" --expect-key after_s41] [--expect-counts H=105,CEX=3,NT=7]

It runs, from the model's parent folder, exactly
  PYTHONHASHSEED=0 python3 -B -m model.run --scale S --time-cap T --no-write --brief [--claim ...]
with a deadline on the whole run, keeps the printout (raw.txt), reads each claim's status and each part's
(label, kind, status) from it (claims.json), and, when --expect is given, compares them with the recorded ones.
It writes nothing in the model's folder (-B, --no-write) and checks that by the md5 of every file there, before and after.
ok = the run ended, nothing in the model folder changed, and (if expected values are given) every claim and part and
every count is equal. It never decides whether a claim should hold.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402

STATUS = {"HOLDS ON ALL MODELS TRIED": "H", "COUNTEREXAMPLE FOUND": "CEX", "NOT TESTED": "NT"}
CLAIM = re.compile(r"^(\S+)  (HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)  \(([\d.]+) s\)$")
PART = re.compile(r"^-- (.*) \[([^\[\]]*)\] ([^\[\]]*)$")


def tree_md5(d):
    out = {}
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            out[os.path.relpath(p, d)] = H.md5_file(p)
    pyc = [os.path.relpath(os.path.join(r, x), d) for r, ds, fs in os.walk(d) for x in ds if x == "__pycache__"]
    return out, sorted(pyc)


def parse(raw):
    claims, cur, lines = [], None, raw.split("\n")
    for i, l in enumerate(lines):
        m = CLAIM.match(l)
        if m and i > 0 and lines[i - 1].startswith("=" * 20):
            cur = dict(id=m.group(1), status=m.group(2), seconds=float(m.group(3)), parts=[], error=False)
            claims.append(cur)
            continue
        if cur is None:
            continue
        m = PART.match(l)
        if m:
            cur["parts"].append(dict(label=m.group(1), kind=m.group(2), status=m.group(3)))
        elif l.startswith("Traceback (most recent call last)"):
            cur["error"] = True
    total = re.search(r"(?m)^total ([\d.]+) s$", raw)
    return claims, (float(total.group(1)) if total else None)


def counts(claims):
    c = {"H": 0, "CEX": 0, "NT": 0}
    for x in claims:
        c[STATUS[x["status"]]] += 1
    c["of"] = len(claims)
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-dir", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--claim", action="append")
    ap.add_argument("--scale", type=float, default=4)
    ap.add_argument("--time-cap", type=float, default=45)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--expect")
    ap.add_argument("--expect-key", default="after_s41")
    ap.add_argument("--expect-counts")
    a = ap.parse_args()

    md = os.path.abspath(a.model_dir)
    if not os.path.isfile(os.path.join(md, "model", "run.py")):
        H.refuse("no model/run.py under %s" % md)
    H.guard_write(os.path.join(a.out_dir, "x"))
    os.makedirs(a.out_dir, exist_ok=True)
    before, pyc_before = tree_md5(md)

    argv = [sys.executable, "-B", "-m", "model.run", "--scale", "%g" % a.scale, "--time-cap", "%g" % a.time_cap,
            "--no-write", "--brief"]
    for c in a.claim or []:
        argv += ["--claim", c]
    r = H.run(argv, cwd=md, timeout=a.timeout, env_extra={"PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"})
    H.write_text(os.path.join(a.out_dir, "raw.txt"), r["stdout"])
    if r["stderr"].strip():
        H.write_text(os.path.join(a.out_dir, "stderr.txt"), r["stderr"])
    after, pyc_after = tree_md5(md)
    changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))

    claims, total = parse(r["stdout"])
    H.write_json(os.path.join(a.out_dir, "claims.json"), dict(command=" ".join(argv[1:]), cwd=H.rel(md), claims=claims))
    out = dict(job="claim_suite", model_dir=H.rel(md), command="PYTHONHASHSEED=0 python3 " + " ".join(argv[1:]),
               exit=r["exit"], timed_out=r["timed_out"], seconds=r["seconds"], total_reported=total,
               counts=counts(claims), claims_with_error=[c["id"] for c in claims if c["error"]],
               model_folder_changed=changed, pycache_new=sorted(set(pyc_after) - set(pyc_before)),
               raw=H.rel(os.path.join(a.out_dir, "raw.txt")), raw_md5=H.md5_bytes(r["stdout"].encode("utf-8")))
    ok = r["exit"] == 0 and not r["timed_out"] and not changed and bool(claims)

    if a.expect:
        exp = H.load_json(a.expect)
        want = {c["id"]: c.get(a.expect_key) for c in exp["claims"]}
        got = {c["id"]: c for c in claims}
        ids = [c["id"] for c in exp["claims"]] if not a.claim else list(a.claim)
        diffs = []
        for cid in ids:
            w, g = want.get(cid), got.get(cid)
            if w is None:
                diffs.append(dict(id=cid, what="no recorded result under %s" % a.expect_key))
                continue
            if g is None:
                diffs.append(dict(id=cid, what="not in this run's printout"))
                continue
            if w["status"] != g["status"]:
                diffs.append(dict(id=cid, what="status", recorded=w["status"], got=g["status"]))
            wp = [(p["label"], p["kind"], p["status"]) for p in w.get("parts", [])]
            gp = [(p["label"], p["kind"], p["status"]) for p in g["parts"]]
            if wp != gp:
                diffs.append(dict(id=cid, what="parts", recorded=wp, got=gp))
        extra = sorted(set(got) - set(ids))
        out.update(expect=H.rel(a.expect), expect_md5=H.md5_file(a.expect), expect_key=a.expect_key,
                   claims_compared=len(ids), claims_equal=len(ids) - len({d["id"] for d in diffs}),
                   differences=diffs, claims_not_in_record=extra)
        ok = ok and not diffs and not extra
    if a.expect_counts:
        want_c = dict((k, int(v)) for k, v in (kv.split("=") for kv in a.expect_counts.split(",")))
        out["expect_counts"] = want_c
        out["counts_equal"] = all(out["counts"].get(k) == v for k, v in want_c.items())
        ok = ok and out["counts_equal"]
    out["ok"] = ok
    H.write_json(os.path.join(a.out_dir, "result.json"), out)
    H.emit(out)


if __name__ == "__main__":
    main()
