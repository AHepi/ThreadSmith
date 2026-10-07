# S108 Part A, section 1: V1.1's generated moves, examined. Same stream as s108_s1_worlds.py (seed, sizes, scale); for every
# candidate whose Acc moves under V1.1: at which pairs of C (F1) differs between I14 and V1.1, and whether Sol_D is empty
# there; for every 'out' move whether each failing counterpart is a proper subnetwork (N_k ≠ J_D).
#   PYTHONHASHSEED=0 python3 -B s108_s1_v11_in.py [--scale 4] [--seed 108001] [--valuemaps] [--proper] [--sizes SMALL|MID]
import argparse
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from model import core  # noqa: E402
from model.core import account, F1_at, proj_lam  # noqa: E402
from model.claims_a import SMALL, MID, gen_p_cand  # noqa: E402

core.S108_S1_GEN = "fixed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--seed", type=int, default=108001)
    ap.add_argument("--valuemaps", action="store_true")
    ap.add_argument("--proper", action="store_true")
    ap.add_argument("--sizes", default="SMALL")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    per = max(1, int(40 * a.scale))
    tally = {}
    for size in (SMALL if a.sizes == "SMALL" else MID):
        for i in range(per):
            m = gen_p_cand(rng, size, valuemaps=a.valuemaps, proper=a.proper)
            if m is None:
                continue
            p, c = m
            core.S108_S1 = "none"
            off = account(c)
            core.S108_S1 = "V1.1"
            on = account(c)
            if off == on:
                continue
            D = p.D
            diff_pairs = []
            for (x, y) in p.C:
                core.S108_S1 = "none"
                f0 = F1_at(c, x, y)
                core.S108_S1 = "V1.1"
                f1 = F1_at(c, x, y)
                if f0 != f1:
                    diff_pairs.append((x, y))
            empty = [pr for pr in diff_pairs if not D.sol(*pr)]
            key = ("in" if on else "out", "every differing pair has Sol_D empty" if len(empty) == len(diff_pairs) else
                   ("some differing pair has Sol_D empty" if empty else "no differing pair has Sol_D empty"))
            tally[key] = tally.get(key, 0) + 1
            if on and not empty:
                print("in, at nonempty solutions (size %r, model %d): the pairs where (F1) differs %s" % (size, i, sorted(diff_pairs, key=repr)))
                print(p.describe())
                print(D.describe(pairs=sorted(p.C, key=repr)))
                print(c.describe())
            core.S108_S1 = "none"
    for k, v in sorted(tally.items()):
        print("%s: %d" % (" | ".join(k), v))


if __name__ == "__main__":
    main()
