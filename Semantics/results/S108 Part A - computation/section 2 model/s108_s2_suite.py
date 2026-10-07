# S108 Part A, section 2 (the computing agent, rule 5): the whole suite with each in-scope variant on, against the
# whole suite with every variant off, run on this copy of the program. Each run is `python3 -B -m model.run --scale 4
# --time-cap 45 --no-write` with S108_S2_VARIANT set, PYTHONHASHSEED=0, under a timeout; outputs are saved to OUTDIR.
# The comparison reads every claim's status and, part by part, its status and its written result, counterexample, witness
# or reason; the lines that depend on the time a search had (models tried, hypothesis met, stopped, seconds) are left out.
#   python3 -B s108_s2_suite.py run OUTDIR VARIANT [VARIANT ...]     run the suite (sequentially) for each variant
#   python3 -B s108_s2_suite.py diff OUTDIR VARIANT [--claims]      compare OUTDIR/suite.VARIANT.txt with suite.off.txt
# Standard library only; writes only into OUTDIR.
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TIMED = ("models_tried:", "hypothesis_met:", "stopped:", "seed:", "smallest_size:", "space:")


def run(outdir, variants):
    for v in variants:
        env = dict(os.environ, PYTHONHASHSEED="0", S108_S2_VARIANT=v)
        t0 = time.time()
        with open(os.path.join(outdir, "suite.%s.txt" % v), "w", encoding="utf-8") as f:
            r = subprocess.run([sys.executable, "-B", "-m", "model.run", "--scale", "4", "--time-cap", "45", "--no-write"],
                               cwd=HERE, env=env, stdout=f, stderr=subprocess.STDOUT, timeout=5400)
        print("%s exit %s, %.0f s" % (v, r.returncode, time.time() - t0))
        sys.stdout.flush()


def parse(path):
    """claim id -> (status, [(label, kind, status, text)])"""
    claims = {}
    cur = None
    part = None
    field = None
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    for ln in lines:
        m = re.match(r"^(FC[0-9A-Za-z.]+)  (.+?)  \(([0-9.]+) s\)$", ln)
        if m:
            cur = m.group(1)
            claims[cur] = [m.group(2), []]
            part, field = None, None
            continue
        if cur is None:
            continue
        m = re.match(r"^-- (.*) \[(.+?)\] (.+)$", ln)
        if m:
            part = [m.group(1), m.group(2), m.group(3), []]
            claims[cur][1].append(part)
            field = None
            continue
        if part is None:
            if ln.startswith("Traceback") or ln.startswith("  File") or (ln and not ln.startswith("=")):
                claims[cur].append(ln)
            continue
        s = ln.strip()
        if ln.startswith("   ") and not ln.startswith("      "):
            key = s.split(":")[0] + ":"
            field = key
            if key in TIMED:
                continue
            part[3].append(s)
            continue
        if ln.startswith("      "):
            if field in TIMED:
                continue
            part[3].append(s)
    return claims


def diff(outdir, v, show_claims=False):
    a = parse(os.path.join(outdir, "suite.off.txt"))
    b = parse(os.path.join(outdir, "suite.%s.txt" % v))
    moved = []
    for cid in a:
        if cid not in b:
            moved.append((cid, "missing under the variant"))
            continue
        sa, pa = a[cid][0], a[cid][1]
        sb, pb = b[cid][0], b[cid][1]
        notes = []
        if sa != sb:
            notes.append("claim status %s -> %s" % (sa, sb))
        la = {p[0]: p for p in pa}
        lb = {p[0]: p for p in pb}
        for lab in la:
            if lab not in lb:
                notes.append("part '%s' missing" % lab)
                continue
            x, y = la[lab], lb[lab]
            if x[2] != y[2]:
                notes.append("part '%s' [%s]: %s -> %s" % (lab[:70], x[1], x[2], y[2]))
            elif x[3] != y[3]:
                notes.append("part '%s' [%s]: same status (%s), its written result differs" % (lab[:70], x[1], x[2]))
        if len(a[cid]) > 2 or len(b[cid]) > 2:
            if a[cid][2:] != b[cid][2:]:
                notes.append("error text differs")
        if notes:
            moved.append((cid, "; ".join(notes)))
    tot = {}
    for s, _ in b.values():
        tot[s] = tot.get(s, 0) + 1
    tot_a = {}
    for s, _ in a.values():
        tot_a[s] = tot_a.get(s, 0) + 1
    print("%s: claims %d; statuses off %s; on %s; claims whose result moves: %d" % (v, len(b), tot_a, tot, len(moved)))
    for cid, n in moved:
        print("   %s: %s" % (cid, n))
    return moved


if __name__ == "__main__":
    cmd, outdir = sys.argv[1], sys.argv[2]
    if cmd == "run":
        run(outdir, sys.argv[3:])
    else:
        diff(outdir, sys.argv[3], "--claims" in sys.argv)
