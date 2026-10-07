# S108 Part A round 2, section 2 (the computing agent, rule 5): single claims (not the whole suite, which is the Sonnet
# harness's job: tools/sonnet_harness/specs/s108r2 claim suites, section 2.json) run under a switch setting and compared,
# claim by claim and part by part, with the same claims run with every switch off. The comparison is round 1's
# (s108_s2_suite.parse: status; each part's status and written result, with the lines that depend on the time a search had
# left out). Each run: `python3 -B -m model.run --claim ... --scale 4 --time-cap 45 --no-write`, PYTHONHASHSEED=0, a timeout.
#   python3 -B s108r2_s2_claims.py OUTDIR LABEL "VAR=val VAR2=val" CLAIM [CLAIM ...]
# prints the claims whose result moves against OUTDIR/<the same claims>.off.txt (run first if missing). Standard library
# only; writes only into OUTDIR.
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_s2_suite as S1  # noqa: E402  (round 1's parse)

ALL_VARS = ("S108_S2_VARIANT", "S108R2_S2_VARIANT", "S108R2_S2_R26", "S108R2_S2_DESC", "S105_SLOT_QUANTIFIER",
            "S106_ACCOUNT_READING")


def run(outdir, label, envs, claims, timeout=3000):
    env = {k: v for k, v in os.environ.items() if k not in ALL_VARS}
    env["PYTHONHASHSEED"] = "0"
    for kv in envs.split():
        k, v = kv.split("=", 1)
        env[k] = v
    argv = [sys.executable, "-B", "-m", "model.run", "--scale", "4", "--time-cap", "45", "--no-write"]
    for c in claims:
        argv += ["--claim", c]
    path = os.path.join(outdir, "%s.txt" % label)
    t0 = time.time()
    with open(path, "w", encoding="utf-8") as f:
        r = subprocess.run(argv, cwd=HERE, env=env, stdout=f, stderr=subprocess.STDOUT, timeout=timeout)
    return path, r.returncode, time.time() - t0


def diff(pa, pb):
    a, b = S1.parse(pa), S1.parse(pb)
    moved = []
    for cid in b:
        if cid not in a:
            moved.append((cid, "not in the off run: %s" % b[cid][0]))
            continue
        notes = []
        if a[cid][0] != b[cid][0]:
            notes.append("claim status %s -> %s" % (a[cid][0], b[cid][0]))
        la, lb = {p[0]: p for p in a[cid][1]}, {p[0]: p for p in b[cid][1]}
        for lab in la:
            if lab not in lb:
                notes.append("part '%s' missing (label changed?)" % lab[:70])
                continue
            x, y = la[lab], lb[lab]
            if x[2] != y[2]:
                notes.append("part '%s': %s -> %s" % (lab[:70], x[2], y[2]))
            elif x[3] != y[3]:
                notes.append("part '%s': same status (%s), written result differs" % (lab[:70], x[2]))
        for lab in lb:
            if lab not in la:
                notes.append("new part label '%s'" % lab[:70])
        if a[cid][2:] != b[cid][2:]:
            notes.append("error text differs")
        if notes:
            moved.append((cid, "; ".join(notes)))
    return moved


if __name__ == "__main__":
    outdir, label, envs, claims = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    os.makedirs(outdir, exist_ok=True)
    key = "_".join(c.replace(".", "") for c in claims)[:80]
    off = os.path.join(outdir, "off - %s.txt" % key)
    if not os.path.exists(off):
        p, rc, s = run(outdir, "off - %s" % key, "", claims)
        print("off: exit %s, %.0f s" % (rc, s))
    p, rc, s = run(outdir, "%s - %s" % (label, key), envs, claims)
    print("%s (%s): exit %s, %.0f s" % (label, envs, rc, s))
    mv = diff(off, p)
    b = S1.parse(p)
    print("claims run %d; moved %d" % (len(b), len(mv)))
    for cid, n in mv:
        print("   %s: %s" % (cid, n))
    errs = [c for c, v in b.items() if len(v) > 2]
    if errs:
        print("   claims with an error or stray text: %s" % errs)
