# S104 round 2 (maths): run the counterexample search.
#   python3 -m model.run                 every claim; writes search results.md and .json
#   python3 -m model.run --claim FC23    one claim, printed in full (reproduces its counterexamples)
# Run from the folder "results/S104 Round 2 - maths". Standard library only.
# S106: run from "results/S106 The written-in test taken out/model after S106"; S106_ACCOUNT_READING=r3 in the
# environment computes round 3's (E) (NC1 a conjunct) for comparison; the default is (E) after S106.
# S107 round 4: run from "results/S107 Round 4 - maths after the reading/model after round 4" (the three areas merged).
import argparse
import json
import os
import sys
import time
import traceback

from .harness import REG, Settings, overall
from . import claims_a  # noqa: F401
from . import claims_b  # noqa: F401
from . import claims_area1  # noqa: F401  (area 1 new claims)
from . import claims_s41  # noqa: F401  (the owner's answers, S41: FC30.new1, FC84.new1)
from . import claims_r3a1  # noqa: F401  (S105 round 3, area 1: FC12.new2, FC12.new3, FC13.new1, FC28.new1, FC28.new2, FC84.new2, FC97.new1, FC98.new1, FC104.new1)
from . import claims_r3a2  # noqa: F401  (S105 round 3, area 2: FC23.new1, FC25.new1, FC47.new1)
from . import claims_r3a3  # noqa: F401  (S105 round 3, area 3: FC98.new2, FC72.new1, FC80.new1, FC32.new1, FC90.new1, FC102.new1, FC103.new1)
from . import claims_s106  # noqa: F401  (S106, the written-in test taken out: FC23.new2, FC23.new3, FC25.new2)
from . import claims_r4a2  # noqa: F401  (S107 round 4, area 2: FC27.new1, FC23.new4, FC23.new5, FC42.new1)
from . import claims_r4a3  # noqa: F401  (S107 round 4, area 3: FC72.new2, K1 the winter-myth knock-on)
# S107 round 4, integration: the one merge conflict (both areas added an import after claims_s106's); both kept.

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_claim(cid, S):
    fn, invs = REG[cid]
    t0 = time.time()
    try:
        parts = fn(S)
        err = None
    except Exception:
        parts = []
        err = traceback.format_exc()
    return dict(id=cid, parts=parts, status=overall(parts) if parts else "NOT TESTED", error=err,
                program_inventions=invs, seconds=round(time.time() - t0, 2))


def print_result(r, full=True):
    print("=" * 100)
    print("%s  %s  (%.1f s)" % (r["id"], r["status"], r["seconds"]))
    if r["error"]:
        print(r["error"])
    for p in r["parts"]:
        print("-- %s [%s] %s" % (p["label"], p["kind"], p["status"]))
        print("   statement: %s" % p["statement"])
        for k in ("seed", "models_tried", "hypothesis_met", "smallest_size", "stopped"):
            if p.get(k) is not None:
                print("   %s: %s" % (k, p[k]))
        if p.get("space"):
            print("   space: %s" % p["space"])
        for k in ("counterexample", "witness", "result", "why"):
            if p.get(k):
                txt = p[k] if full else p[k][:600]
                print("   %s:\n      %s" % (k, txt.replace("\n", "\n      ")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claim", action="append")
    ap.add_argument("--scale", type=float, default=1.0)
    ap.add_argument("--time-cap", type=float, default=20.0)
    ap.add_argument("--no-write", action="store_true")
    ap.add_argument("--brief", action="store_true")
    a = ap.parse_args()
    S = Settings(scale=a.scale, time_cap=a.time_cap)
    ids = a.claim or sorted(REG, key=lambda s: (int(s[2:].split(".")[0]), s))
    out = []
    t0 = time.time()
    for cid in ids:
        r = run_claim(cid, S)
        out.append(r)
        print_result(r, full=not a.brief)
        sys.stdout.flush()
    print("total %.1f s" % (time.time() - t0))
    if not a.claim and not a.no_write:
        from .report import write_results
        write_results(out, S, round(time.time() - t0, 1))


if __name__ == "__main__":
    main()
