# S108 Part A, Sonnet 5.5 trial, section 2: pairs of candidates, one variant against no variant, for the variants that move Acc
# (V2.1, V2.2, V2.3, V2.3b, V2.4). A problem between two candidates is taken here as: both meet Acc (E), they are rivals (core.rivals),
# and its kind is core.problem_kind ("i" a conflict pair lies in C, "ii" none does). This proxy for Prob_j (D10.4) is an invention of this
# trial (the program has no function Prob_j for two candidates; claims_b.py names it only in a dependency label). ETV_j(candidate; p) is
# read as its kind-ii clause: some rival candidate with a problem of kind ii.
# Same worlds as V2.6's run: claims_b.gen_pair over CONF, 10 x scale per size, seed 108106.
# Run from the folder "section 2 model":  PYTHONHASHSEED=0 python3 -B s108_section2_pairs.py <V> <scale> [json path]
# Standard library only. Nothing here changes the theory (S40).
import json
import os
import random
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model import claims_b  # noqa: E402
from model.core import account, rivals, problem_kind, conflict_pairs  # noqa: E402
from model.claims_b import gen_pair, CONF  # noqa: E402

VARIANT = sys.argv[1]
SCALE = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
JSON = sys.argv[3] if len(sys.argv) > 3 else None
SEED = 108106


def set_on(on):
    core.S2_ON.clear()
    if on:
        core.S2_ON.add(VARIANT)
    claims_b.SEL_H_NONEMPTY = "V2.5" not in core.S2_ON


def main():
    rng = random.Random(SEED)
    per = max(1, int(10 * SCALE))
    cnt = Counter()
    wit = {}
    t0 = time.time()
    for size in CONF:
        for _ in range(per):
            m = gen_pair(rng, size)
            if m is None:
                continue
            p, c1, c2 = m
            res = {}
            for lab in ("off", "on"):
                set_on(lab == "on")
                a1, a2 = bool(account(c1)), bool(account(c2))
                riv = rivals(c1, c2)
                res[lab] = dict(a1=a1, a2=a2, both=a1 and a2, riv=riv, kind=problem_kind(c1, c2), prob=(a1 and a2 and riv))
            set_on(False)
            o, x = res["off"], res["on"]
            cnt["pairs"] += 1
            cnt["both Acc, off"] += o["both"]
            cnt["both Acc, on"] += x["both"]
            cnt["problem (both Acc, rivals), off"] += o["prob"]
            cnt["problem (both Acc, rivals), on"] += x["prob"]
            cnt["problem of kind i, off"] += o["prob"] and o["kind"] == "i"
            cnt["problem of kind i, on"] += x["prob"] and x["kind"] == "i"
            cnt["problem of kind ii, off"] += o["prob"] and o["kind"] == "ii"
            cnt["problem of kind ii, on"] += x["prob"] and x["kind"] == "ii"
            cnt["Acc moves T->F (a candidate of a pair)"] += (o["a1"] and not x["a1"]) + (o["a2"] and not x["a2"])
            cnt["Acc moves F->T (a candidate of a pair)"] += (not o["a1"] and x["a1"]) + (not o["a2"] and x["a2"])
            if o["prob"] and not x["prob"]:
                cnt["problem lost"] += 1
                if o["kind"] == "ii":
                    cnt["problem lost, kind ii"] += 1
                if "problem lost" not in wit:
                    wit["problem lost"] = dict(size=repr(size), kind_off=o["kind"], description=p.describe() + "\n" + p.D.describe() + "\n" + c1.describe() + "\n" + c2.describe())
            if not o["prob"] and x["prob"]:
                cnt["problem gained"] += 1
                if o["kind"] == "ii" or x["kind"] == "ii":
                    cnt["problem gained, kind ii"] += 1
                if "problem gained" not in wit:
                    wit["problem gained"] = dict(size=repr(size), kind_on=x["kind"], description=p.describe() + "\n" + p.D.describe() + "\n" + c1.describe() + "\n" + c2.describe())
    print("S108 section 2, pairs of candidates, variant %s, scale %s, seed %s, per size %d, %d pairs over %d sizes; seconds %.1f" % (VARIANT, SCALE, SEED, per, cnt["pairs"], len(CONF), time.time() - t0))
    for k, v in sorted(cnt.items()):
        print("  %-60s %s" % (k, v))
    for k, w in wit.items():
        print("--- %s (size %s)" % (k, w["size"]))
        print("   " + w["description"].replace("\n", "\n   "))
    if JSON:
        with open(JSON, "w", encoding="utf-8") as f:
            json.dump(dict(variant=VARIANT, scale=SCALE, seed=SEED, counts=dict(sorted(cnt.items())), witnesses=wit), f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
