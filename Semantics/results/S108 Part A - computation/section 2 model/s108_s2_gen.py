# S108 Part A, section 2 (the computing agent, rule 5.4): the generated worlds at scale 4, each in-scope variant of
# section 2 off and on. Three populations, each drawn by the program's own generators, sizes in ascending order, seeded:
#   single  gen_p_cand (claims_a) over SMALL, both families, 40 × scale per size (FC30.new1 (b)'s generator): Acc (E)
#           under off and every variant; Account ∧ ¬Dec(t) under four histories set by hand (Θ, I90; claims_s41).
#   pairs   gen_pair (claims_b) over CONF, 20 × scale per size (FC43's generator): Conf pairs, rivals, kind (D8.2, D10.2).
#   claims  FC52's generator over CONF, 10 × scale per size: ConfCl at every translated pair (D8.5).
# For each variant: the candidates (or pairs) whose result differs between off and on, how many of each kind, and the
# smallest witness of each kind (the first found; sizes ascend, so the first is at the smallest size tried).
# Run from "results/S108 Part A - computation/section 2 model":
#   PYTHONHASHSEED=0 python3 -B s108_s2_gen.py [--scale 4] [--pop single|pairs|claims] [--json FILE]
# Standard library only; imports the package model/ of this folder (the copy); writes only the --json file.
import json
import random
import sys
import time
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, account, conflict_pairs, problem_kind, rivals, conf_claim, all_pairs, hom  # noqa: E402
from model.claims_a import SMALL, MID, gen_p_cand, gen_p_cand_proper  # noqa: E402
from model.claims_b import CONF, gen_pair, small_enough, rand_allow, Hist, sel, con  # noqa: E402
from model.claims_a import D_and_p  # noqa: E402
from model.gen import any_candidate  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402

VARIANTS = [v for v in core.S2_VARIANTS if v != "off"]
HISTORIES = ("Con", "Sel H={(1,b0)}", "nothing tried, H=∅", "Dec (not admitted)")


def with_variant(v, fn, *a, **k):
    old = core.S2_VARIANT
    core.S2_VARIANT = v
    try:
        return fn(*a, **k)
    finally:
        core.S2_VARIANT = old


def dec_of(c, hist):
    if hist == "Con":
        return provenance_of(c, "Con", [(ONE, c.p.b0)])[2]
    if hist == "Sel H={(1,b0)}":
        return provenance_of(c, "Sel", [(ONE, c.p.b0)])[2]
    if hist == "Dec (not admitted)":
        return provenance_of(c, "Dec", [(ONE, c.p.b0)])[2]
    h = Hist([], [], set(c.p.C), admitted=True, prepares=False)
    return not sel(c, [], h) and not con(h)


def kind_of(c):
    return "%s target, %s candidate" % (c.p.D.meta.get("family", "?"), c.E.meta.get("family", "?"))


def conj(d):
    return ",".join("%s%s" % (k, "T" if d.get(k) else "F") for k in ("F1", "F2", "A", "Dep", "NonVacuous", "NC1") if k in d)


def describe(p, c):
    return "%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe())


SINGLE = {  # name -> (sizes, generator, per size before scale, seed)
    "single": (SMALL, lambda rng, size: gen_p_cand(rng, size), 40, 1082100),
    "single-valuemaps": (SMALL, lambda rng, size: gen_p_cand(rng, size, valuemaps=True), 40, 1082110),
    "single-MID-proper": (MID, gen_p_cand_proper, 20, 1082120),
}


def pop_single(scale, name="single"):
    sizes_, gen, per_size, seed = SINGLE[name]
    rng = random.Random(seed)
    per = max(1, int(per_size * scale))
    n = 0
    t0 = time.time()
    diff = {v: {} for v in VARIANTS}  # v -> kind label -> [count, smallest witness]
    ediff = {v: {} for v in VARIANTS}
    acc_true = {v: 0 for v in core.S2_VARIANTS}
    for size in sizes_:
        for i in range(per):
            m = gen(rng, size)
            if m is None:
                continue
            p, c = m
            n += 1
            res = {}
            for v in core.S2_VARIANTS:
                val, d = with_variant(v, account, c, detail=True)
                res[v] = (bool(val), d)
                acc_true[v] += bool(val)
            decs = {}
            for v in ("off", "V2.5"):
                decs[v] = {h: with_variant(v, dec_of, c, h) for h in HISTORIES}
            for v in VARIANTS:
                a0, a1 = res["off"][0], res[v][0]
                if a0 != a1:
                    k = "Acc %s->%s; %s; conjuncts off [%s] on [%s]" % ("T" if a0 else "F", "T" if a1 else "F", kind_of(c), conj(res["off"][1]), conj(res[v][1]))
                    e = diff[v].setdefault(k, [0, None, None])
                    e[0] += 1
                    if e[1] is None:
                        e[1] = repr(size)
                        e[2] = describe(p, c)
                dv = decs["V2.5" if v == "V2.5" else "off"]
                for h in HISTORIES:
                    x0 = a0 and not decs["off"][h]
                    x1 = a1 and not dv[h]
                    if x0 != x1:
                        k = "Account ∧ ¬Dec(t) %s->%s; history '%s'; %s" % ("T" if x0 else "F", "T" if x1 else "F", h, kind_of(c))
                        e = ediff[v].setdefault(k, [0, None, None])
                        e[0] += 1
                        if e[1] is None:
                            e[1] = repr(size)
                            e[2] = describe(p, c) + ("\nHom(τ) %s" % hom(c))
    return dict(population=name, drawn=n, per_size=per, sizes=len(sizes_), seconds=round(time.time() - t0, 1),
                acc_true=acc_true, acc_diff=diff, expl_diff=ediff)


def pop_pairs(scale, per_size=20, seed=1082200):
    rng = random.Random(seed)
    per = max(1, int(per_size * scale))
    n = 0
    t0 = time.time()
    diff = {}
    offkinds = {}
    for size in CONF:
        for i in range(per):
            m = gen_pair(rng, size)
            if m is None:
                continue
            p, c1, c2 = m
            n += 1
            r = {}
            for v in ("off", "V2.6"):
                r[v] = (tuple(with_variant(v, conflict_pairs, c1, c2)), with_variant(v, problem_kind, c1, c2), bool(with_variant(v, rivals, c1, c2)))
            offkinds[str(r["off"][1])] = offkinds.get(str(r["off"][1]), 0) + 1
            if r["off"] != r["V2.6"]:
                inC = [x for x in r["off"][0] if x in p.C]
                k = "kind %s -> %s; rivals %s -> %s; conflict pairs %s -> %s (in C: %d of %d)" % (
                    r["off"][1], r["V2.6"][1], r["off"][2], r["V2.6"][2], "some" if r["off"][0] else "none",
                    "some" if r["V2.6"][0] else "none", len(inC), len(r["off"][0]))
                k = k.split(" (in C")[0]
                e = diff.setdefault(k, [0, None, None])
                e[0] += 1
                if e[1] is None:
                    e[1] = repr(size)
                    e[2] = "%s\n%s\n%s\n%s\nconflict pairs off %s; on %s" % (p.describe(), p.D.describe(), c1.describe(), c2.describe(), list(r["off"][0]), list(r["V2.6"][0]))
    return dict(population="pairs", drawn=n, per_size=per, sizes=len(CONF), seconds=round(time.time() - t0, 1), kinds_off=offkinds, diff=diff)


def pop_claims(scale, per_size=10, seed=1082300):
    rng = random.Random(seed)
    per = max(1, int(per_size * scale))
    n, npairs = 0, 0
    t0 = time.time()
    diff = {}
    conf_off = 0
    for size in CONF:
        for i in range(per):
            D, p = D_and_p(rng, size)
            if D is None or not small_enough(D, 1024):
                continue
            c = any_candidate(rng, p, size)
            allow, _ = rand_allow(rng, D)
            n += 1
            acc = account(c)
            for (a, b) in all_pairs(D):
                if not c.translates(a, b):
                    continue
                npairs += 1
                f0, s0 = with_variant("off", conf_claim, c, a, b, allow, parts=True)
                f1, s1 = with_variant("V2.7", conf_claim, c, a, b, allow, parts=True)
                conf_off += bool(f0 or s0)
                if (f0 or s0) != (f1 or s1):
                    k = "ConfCl %s -> %s at a pair %s C; first disjunct %s, second %s; candidate's (E) %s; %s" % (
                        f0 or s0, f1 or s1, "in" if (a, b) in p.C else "outside", f0, s0, acc, c.E.meta.get("family", "?"))
                    e = diff.setdefault(k, [0, None, None])
                    e[0] += 1
                    if e[1] is None:
                        e[1] = repr(size)
                        e[2] = "%s\n%s\n%s\nat (%s,%s)" % (p.describe(), D.describe(), c.describe(), a, b)
    return dict(population="claims", drawn=n, pairs=npairs, conf_off=conf_off, per_size=per, sizes=len(CONF), seconds=round(time.time() - t0, 1), diff=diff)


def show(res):
    P = print
    P("population %s: %d drawn (%s per size over %d sizes), %.1f s" % (res["population"], res["drawn"], res["per_size"], res["sizes"], res["seconds"]))
    if res["population"].startswith("single"):
        P("   Acc true: %s" % res["acc_true"])
        for v in VARIANTS:
            tot = sum(e[0] for e in res["acc_diff"][v].values())
            etot = sum(e[0] for e in res["expl_diff"][v].values())
            P("   %s: candidates whose Acc differs: %d; (candidate, history) whose Account ∧ ¬Dec(t) differs: %d" % (v, tot, etot))
            for k, e in sorted(res["acc_diff"][v].items(), key=lambda kv: -kv[1][0]):
                P("      %5d  %s  (smallest at %s)" % (e[0], k, e[1]))
            for k, e in sorted(res["expl_diff"][v].items(), key=lambda kv: -kv[1][0]):
                P("      %5d  %s  (smallest at %s)" % (e[0], k, e[1]))
    elif res["population"] == "pairs":
        P("   kinds of problem, off: %s" % res["kinds_off"])
        P("   V2.6: pairs whose conflict pairs, rivals or kind differ: %d" % sum(e[0] for e in res["diff"].values()))
        for k, e in sorted(res["diff"].items(), key=lambda kv: -kv[1][0]):
            P("      %5d  %s  (smallest at %s)" % (e[0], k, e[1]))
    else:
        P("   translated pairs: %d; ConfCl true off: %d" % (res["pairs"], res["conf_off"]))
        P("   V2.7: (candidate, pair) whose ConfCl differs: %d" % sum(e[0] for e in res["diff"].values()))
        for k, e in sorted(res["diff"].items(), key=lambda kv: -kv[1][0]):
            P("      %5d  %s  (smallest at %s)" % (e[0], k, e[1]))


def main():
    a = sys.argv
    scale = float(a[a.index("--scale") + 1]) if "--scale" in a else 4.0
    pops = [a[a.index("--pop") + 1]] if "--pop" in a else list(SINGLE) + ["pairs", "claims"]
    out = {}
    for pop in pops:
        res = pop_single(scale, pop) if pop in SINGLE else {"pairs": pop_pairs, "claims": pop_claims}[pop](scale)
        show(res)
        sys.stdout.flush()
        out[pop] = res
    if "--json" in a:
        with open(a[a.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
