# S108 Part A, section 4: the whole suite under one reading (S108_S4_VARIANT in the environment; "none" = after round 4).
#   PYTHONHASHSEED=0 S108_S4_VARIANT=V4.1 python3 -B s108_s4_suite.py OUT.json [--scale 4] [--time-cap 45] [--claim FCnn ...]
# Writes one JSON: per claim, status and per part (label, kind, status, counterexample/witness/result text).
# Standard library only; imports the package model/ of this folder; writes only OUT.json.
import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import s108_s4  # noqa: E402
from model.run import run_claim, REG  # noqa: E402
from model.harness import Settings  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--time-cap", type=float, default=45.0)
    ap.add_argument("--claim", action="append")
    a = ap.parse_args()
    S = Settings(scale=a.scale, time_cap=a.time_cap)
    ids = a.claim or sorted(REG, key=lambda s: (int(s[2:].split(".")[0]), s))
    out = dict(variant=s108_s4.VARIANT, v41_suff=s108_s4.V41_SUFF, v41_q=s108_s4.V41_Q, v42_suff=s108_s4.V42_SUFF,
               v43_read=s108_s4.V43_READ, scale=a.scale, time_cap=a.time_cap, claims=[])
    t0 = time.time()
    for cid in ids:
        r = run_claim(cid, S)
        parts = []
        for p in r["parts"]:
            parts.append({k: p.get(k) for k in ("label", "kind", "status", "counterexample", "witness", "result", "why",
                                                 "models_tried", "hypothesis_met", "smallest_size", "stopped")})
        out["claims"].append(dict(id=cid, status=r["status"], error=r["error"], seconds=r["seconds"], parts=parts))
        print("%s %s (%.1f s)" % (cid, r["status"], r["seconds"]))
        sys.stdout.flush()
    out["seconds"] = round(time.time() - t0, 1)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=repr)
    print("total %.1f s" % out["seconds"])


if __name__ == "__main__":
    main()
