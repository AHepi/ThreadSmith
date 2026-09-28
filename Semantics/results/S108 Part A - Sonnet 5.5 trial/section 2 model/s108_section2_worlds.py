# S108 Part A, Sonnet 5.5 trial, section 2: generated worlds at scale 4, one variant against no variant.
# The same worlds (same seed, same generator, same order) are computed with the variant off and on, in one process, and every
# world whose result differs is counted by kind; the smallest witness of each kind is the first found, sizes ascending.
#   V2.1 V2.2 V2.3 V2.3b V2.4 V2.5:  worlds (p, candidate) from claims_a.gen_p_cand over SMALL (3 ports, 2 values, 3 components, 2 boundaries,
#                                    2 edits), 40 x scale per size; Acc off vs on, its conjuncts, the routes S for |Gamma| <= 5, and Acc and not Dec
#                                    in the three provenance scenarios ((i) constructed, (ii) declared with no pair tried, (iii) declared with one
#                                    pair tried) through claims_s41.provenance_of.
#   V2.6:                            pairs of candidates (claims_b.gen_pair) over CONF, 10 x scale per size; conflict pairs, Riv, problem kind off vs on.
#   V2.7:                            worlds (D, p, candidate, an Allow) as FC52 builds them, CONF, 10 x scale per size; the two disjuncts of ConfCl
#                                    and ConfCl itself off vs on, at every pair the candidate translates.
# Run from the folder "section 2 model":  PYTHONHASHSEED=0 python3 -B s108_section2_worlds.py <V> <scale> [json path]
# Standard library only. Nothing here changes the theory (S40); "model" in the program's code is the program's word for a generated world.
import hashlib
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
from model.core import ONE, account, routes, NC2, all_pairs, conflict_pairs, rivals, problem_kind, conf_claim, all_R, meets_ab  # noqa: E402
from model.claims_a import SMALL, gen_p_cand, D_and_p  # noqa: E402
from model.claims_b import gen_pair, rand_allow, CONF, small_enough  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
from model.gen import any_candidate  # noqa: E402

VARIANT = sys.argv[1]
SCALE = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
JSON = sys.argv[3] if len(sys.argv) > 3 else None
WALL = float(os.environ.get("S108_WALL", "2700"))  # seconds; the loop stops at a size boundary once this is passed and says so
SEED = {"V2.1": 108101, "V2.2": 108101, "V2.3": 108101, "V2.3b": 108101, "V2.4": 108101, "V2.5": 108101, "V2.6": 108106, "V2.7": 108107}[VARIANT]
GAMMA_MAX = 5


def set_on(on):
    core.S2_ON.clear()
    if on:
        core.S2_ON.add(VARIANT)
    claims_b.SEL_H_NONEMPTY = "V2.5" not in core.S2_ON


def tf(x):
    return "T" if x else "F"


def fam_of(c):
    return c.E.meta.get("family", "E_enc")


def fmt(W):
    return "{" + ",".join(sorted(W)) + "}"


def fmt_S(S):
    return "{" + ", ".join(sorted(fmt(W) for W in S)) + "}"


def shape(S, G):
    """A few readable features of a set of routes S over commitments G."""
    Gs = frozenset(G)
    out = []
    if not S:
        out.append("S empty")
        return out
    if frozenset() in S:
        out.append("empty set is a route")
    if Gs not in S:
        out.append("interference (a subset is a route, the full set of commitments is not)")
    mins = [W for W in S if not any(U < W for U in S)]
    if any(len(W) == 1 for W in mins) and len(mins) >= 2 and all(len(W) == 1 for W in mins):
        out.append("several one-commitment routes (redundancy)")
    if S and not any(len(W) <= 1 for W in S) and len(Gs) >= 3:
        out.append("no route of fewer than two commitments")
    return out


def eval_world(p, c, need_prov):
    v, d = account(c, detail=True)
    out = {"acc": bool(v), "conj": {k: bool(d[k]) for k in ("F1", "F2", "A", "NC1", "NC2", "Dep", "NonVacuous") if k in d}}
    if len(c.Gamma) <= GAMMA_MAX:
        S = routes(c)
        out["S"] = S
    else:
        out["S"] = None
    try:
        w = NC2(c, witness=True)
    except Exception:  # noqa: BLE001
        w = None
    out["witness"] = w
    if need_prov:
        prov = {}
        for lab, kind, H in (("i", "Con", [(ONE, p.b0)]), ("ii", "Sel", []), ("iii", "Sel", [(ONE, p.b0)])):
            s, k, dec = provenance_of(c, kind, H)
            prov[lab] = (bool(v and not dec), bool(dec))
        out["prov"] = prov
    return out


def describe(p, c):
    return p.describe() + "\n" + p.D.describe() + "\n" + c.describe()


def run_candidate_worlds():
    rng = random.Random(SEED)
    per = max(1, int(40 * SCALE))
    t0 = time.time()
    n = 0
    dig = hashlib.sha256()
    cnt = Counter()
    wit = {}
    by_fam = {}
    rows = []
    need_prov = VARIANT in ("V2.5",)
    stopped = None
    size_last = None
    per_size_rows = Counter()
    for size in SMALL:
        size_last = size
        for _ in range(per):
            m = gen_p_cand(rng, size)
            if m is None:
                continue
            p, c = m
            n += 1
            dig.update((p.describe() + "|" + c.describe()).encode("utf-8"))
            fam = fam_of(c)
            f = by_fam.setdefault(fam, Counter())
            f["worlds"] += 1
            set_on(False)
            off = eval_world(p, c, need_prov)
            set_on(True)
            on = eval_world(p, c, need_prov)
            set_on(False)
            cnt["worlds"] += 1
            cnt["acc off"] += off["acc"]
            cnt["acc on"] += on["acc"]
            f["acc off"] += off["acc"]
            f["acc on"] += on["acc"]
            g = len(c.Gamma)
            cnt["Gamma=%d worlds" % min(g, 6)] += 1
            # contract shapes
            allone = all(a == ONE for (a, b) in p.C)
            tau_allone = all(c.tau.get(a) == ONE for (a, b) in p.C if a in c.tau)
            cnt["C in {1} x B worlds"] += allone
            cnt["C in {1} x B, acc off"] += allone and off["acc"]
            cnt["C in {1} x B, acc on"] += allone and on["acc"]
            cnt["tau[C] in {1} x B worlds"] += tau_allone
            cnt["tau[C] in {1} x B, acc off"] += tau_allone and off["acc"]
            cnt["tau[C] in {1} x B, acc on"] += tau_allone and on["acc"]
            moved = None
            if off["acc"] and not on["acc"]:
                moved = "Acc T->F"
            elif on["acc"] and not off["acc"]:
                moved = "Acc F->T"
            if moved:
                cnt[moved] += 1
                f[moved] += 1
                # which conjunct moved
                for k in ("F1", "F2", "A", "NC1", "NC2", "Dep", "NonVacuous"):
                    if k in off["conj"] and off["conj"][k] != on["conj"].get(k):
                        cnt["%s: conjunct %s %s->%s" % (moved, k, tf(off["conj"][k]), tf(on["conj"][k]))] += 1
                key = "%s, |Gamma|=%d" % (moved, g)
                cnt[key] += 1
                if moved not in wit:
                    wit[moved] = dict(size=repr(size), family=fam, Gamma=g, off=dict(acc=off["acc"], conj=off["conj"], S=fmt_S(off["S"]) if off["S"] is not None else None, witness=repr(off["witness"])),
                                      on=dict(acc=on["acc"], conj=on["conj"], S=fmt_S(on["S"]) if on["S"] is not None else None, witness=repr(on["witness"])), description=describe(p, c))
                if moved == "Acc F->T":
                    cnt["Acc F->T with no commitments (Gamma empty)"] += (g == 0)
                    cnt["Acc F->T with commitments"] += (g > 0)
                    if g == 0 and "Acc F->T, Gamma empty" not in wit:
                        wit["Acc F->T, Gamma empty"] = dict(size=repr(size), family=fam, description=describe(p, c))
                    if g > 0 and "Acc F->T, Gamma nonempty" not in wit:
                        wit["Acc F->T, Gamma nonempty"] = dict(size=repr(size), family=fam, off=dict(conj=off["conj"], S=fmt_S(off["S"]) if off["S"] is not None else None),
                                                               on=dict(conj=on["conj"], S=fmt_S(on["S"]) if on["S"] is not None else None), description=describe(p, c))
            # conjunct-level moves that do not move Acc
            for k in ("F1", "F2", "A", "NC1", "NC2", "Dep", "NonVacuous"):
                if k in off["conj"] and off["conj"][k] != on["conj"].get(k):
                    cnt["conjunct %s moves (any world)" % k] += 1
            # witness pair (a, b) and its block, off vs on
            if off["witness"] != on["witness"]:
                cnt["NC2 witness differs (pair or block)"] += 1
            # routes
            if off["S"] is not None and on["S"] is not None:
                if off["S"] != on["S"]:
                    cnt["routes S differ"] += 1
                    if off["acc"] and on["acc"]:
                        cnt["routes S differ, Acc T both"] += 1
                    lost = off["S"] - on["S"]
                    gained = on["S"] - off["S"]
                    if lost:
                        cnt["routes: some route leaves S"] += 1
                    if gained:
                        cnt["routes: some route enters S"] += 1
                    if frozenset() in gained:
                        cnt["routes: the empty set enters S"] += 1
                        if "empty set enters S" not in wit:
                            wit["empty set enters S"] = dict(size=repr(size), family=fam, off=fmt_S(off["S"]), on=fmt_S(on["S"]), description=describe(p, c))
                for lab, S in (("off", off["S"]), ("on", on["S"])):
                    for sh in shape(S, c.Gamma):
                        cnt["shape %s: %s" % (lab, sh)] += 1
                so, sn = set(shape(off["S"], c.Gamma)), set(shape(on["S"], c.Gamma))
                for sh in sorted(sn - so):
                    cnt["shape enters (on, not off): %s" % sh] += 1
                    if "shape enters: " + sh not in wit:
                        wit["shape enters: " + sh] = dict(size=repr(size), family=fam, off=fmt_S(off["S"]), on=fmt_S(on["S"]), description=describe(p, c))
                for sh in sorted(so - sn):
                    cnt["shape leaves (off, not on): %s" % sh] += 1
            # provenance scenarios
            if need_prov:
                for lab in ("i", "ii", "iii"):
                    a0, a1 = off["prov"][lab][0], on["prov"][lab][0]
                    d0, d1 = off["prov"][lab][1], on["prov"][lab][1]
                    cnt["scenario (%s): Acc and not Dec, off" % lab] += a0
                    cnt["scenario (%s): Acc and not Dec, on" % lab] += a1
                    cnt["scenario (%s): Dec, off" % lab] += d0
                    cnt["scenario (%s): Dec, on" % lab] += d1
                    if a0 != a1:
                        k2 = "scenario (%s): Acc and not Dec %s->%s" % (lab, tf(a0), tf(a1))
                        cnt[k2] += 1
                        if k2 not in wit:
                            wit[k2] = dict(size=repr(size), family=fam, description=describe(p, c))
                    if d0 != d1:
                        cnt["scenario (%s): Dec differs (Acc or not)" % lab] += 1
                        if off["acc"] or on["acc"]:
                            cnt["scenario (%s): Dec differs among Acc worlds" % lab] += 1
                    if lab == "ii" and off["acc"] and not on["prov"][lab][1]:
                        cnt["scenario (ii): Acc worlds that are not Dec under the variant"] += 1
                    if lab == "ii" and off["acc"] and on["acc"] and on["prov"][lab][0] != on["acc"]:
                        cnt["scenario (ii): Acc worlds still Dec under the variant"] += 1
            if time.time() - t0 > WALL:
                stopped = "wall-clock cap %.0f s reached at size %r after %d worlds" % (WALL, size, n)
                break
        if stopped:
            break
    return dict(kind="candidate worlds", variant=VARIANT, scale=SCALE, seed=SEED, per_size=per, worlds=n, digest=dig.hexdigest(), stopped=stopped,
                last_size=repr(size_last), first_size=repr(SMALL[0]), n_sizes=len(SMALL), counts=dict(sorted(cnt.items())), by_family={k: dict(v) for k, v in by_fam.items()},
                witnesses=wit, seconds=round(time.time() - t0, 1))


def run_pair_worlds():
    """V2.6: pairs of candidates over CONF; conflict pairs, Riv, problem kind, off vs on."""
    rng = random.Random(SEED)
    per = max(1, int(10 * SCALE))
    t0 = time.time()
    n = 0
    dig = hashlib.sha256()
    cnt = Counter()
    wit = {}
    stopped = None
    size_last = None
    for size in CONF:
        size_last = size
        for _ in range(per):
            m = gen_pair(rng, size)
            if m is None:
                continue
            p, c1, c2 = m
            n += 1
            dig.update((p.describe() + "|" + c1.describe() + "|" + c2.describe()).encode("utf-8"))
            res = {}
            for lab in ("off", "on"):
                set_on(lab == "on")
                cps = conflict_pairs(c1, c2)
                res[lab] = dict(pairs=cps, riv=rivals(c1, c2), kind=problem_kind(c1, c2), acc1=bool(account(c1)), acc2=bool(account(c2)))
            set_on(False)
            o, x = res["off"], res["on"]
            cnt["pairs"] += 1
            cnt["Riv off"] += o["riv"]
            cnt["Riv on"] += x["riv"]
            cnt["kind i off"] += o["kind"] == "i"
            cnt["kind ii off"] += o["kind"] == "ii"
            cnt["kind i on"] += x["kind"] == "i"
            cnt["kind ii on"] += x["kind"] == "ii"
            cnt["Acc moves"] += (o["acc1"] != x["acc1"]) + (o["acc2"] != x["acc2"])
            if o["riv"] and not x["riv"]:
                cnt["rivalry lost (Riv T->F)"] += 1
                if o["kind"] == "ii":
                    cnt["rivalry lost, was kind ii"] += 1
                if o["acc1"] and o["acc2"]:
                    cnt["rivalry lost, both candidates Acc"] += 1
                if "rivalry lost" not in wit:
                    wit["rivalry lost"] = dict(size=repr(size), pairs_off=[list(z) for z in o["pairs"]], kind_off=o["kind"], contract=sorted(map(list, p.C)), acc=[o["acc1"], o["acc2"]],
                                               description=p.describe() + "\n" + p.D.describe() + "\n" + c1.describe() + "\n" + c2.describe())
                if o["acc1"] and o["acc2"] and "rivalry lost, both Acc" not in wit:
                    wit["rivalry lost, both Acc"] = dict(size=repr(size), pairs_off=[list(z) for z in o["pairs"]], kind_off=o["kind"], contract=sorted(map(list, p.C)),
                                                         description=p.describe() + "\n" + p.D.describe() + "\n" + c1.describe() + "\n" + c2.describe())
            if not o["riv"] and x["riv"]:
                cnt["rivalry gained (Riv F->T)"] += 1
            if o["kind"] != x["kind"]:
                cnt["kind differs: %s -> %s" % (o["kind"], x["kind"])] += 1
            if o["pairs"] != x["pairs"]:
                cnt["conflict pairs differ"] += 1
                if not set(x["pairs"]) <= set(o["pairs"]):
                    cnt["on has a pair off lacks"] += 1
                if all(z in p.C for z in x["pairs"]):
                    cnt["on: every conflict pair lies in C"] += 1
            if time.time() - t0 > WALL:
                stopped = "wall-clock cap %.0f s reached at size %r after %d worlds" % (WALL, size, n)
                break
        if stopped:
            break
    return dict(kind="pairs of candidates", variant=VARIANT, scale=SCALE, seed=SEED, per_size=per, worlds=n, digest=dig.hexdigest(), stopped=stopped,
                last_size=repr(size_last), first_size=repr(CONF[0]), n_sizes=len(CONF), counts=dict(sorted(cnt.items())), witnesses=wit, seconds=round(time.time() - t0, 1))


def run_confcl_worlds():
    """V2.7: worlds as FC52 builds them; the two disjuncts of ConfCl at every pair the candidate translates, off vs on."""
    rng = random.Random(SEED)
    per = max(1, int(10 * SCALE))
    t0 = time.time()
    n = 0
    dig = hashlib.sha256()
    cnt = Counter()
    wit = {}
    stopped = None
    size_last = None
    for size in CONF:
        size_last = size
        for _ in range(per):
            D, p = D_and_p(rng, size)
            if D is None or not small_enough(D, 1024):
                continue
            c = any_candidate(rng, p, size)
            allow, _ = rand_allow(rng, D)
            n += 1
            dig.update((p.describe() + "|" + c.describe()).encode("utf-8"))
            cnt["worlds"] += 1
            for (a, b) in all_pairs(D):
                if not c.translates(a, b):
                    continue
                set_on(False)
                f0, s0 = conf_claim(c, a, b, allow, parts=True)
                set_on(True)
                f1, s1 = conf_claim(c, a, b, allow, parts=True)
                set_on(False)
                cnt["pairs"] += 1
                cnt["ConfCl off"] += (f0 or s0)
                cnt["ConfCl on"] += (f1 or s1)
                cnt["first disjunct off"] += f0
                cnt["second disjunct off"] += s0
                cnt["first disjunct on"] += f1
                cnt["second disjunct on"] += s1
                if f0 != f1:
                    cnt["first disjunct moves"] += 1
                if (f0 or s0) and not (f1 or s1):
                    cnt["ConfCl T->F"] += 1
                    if not f0 and s0:
                        cnt["ConfCl T->F, second disjunct alone was true"] += 1
                    if "ConfCl T->F" not in wit:
                        y = c.ans_E(c.tau[a], c.sigma[b])
                        wit["ConfCl T->F"] = dict(size=repr(size), pair=[a, b], first_off=f0, second_off=s0, candidate_answer=repr(y), description=p.describe() + "\n" + D.describe() + "\n" + c.describe())
                if not (f0 or s0) and (f1 or s1):
                    cnt["ConfCl F->T"] += 1
                if s0 and not f0:
                    cnt["second only (off): the 'or' is two routes"] += 1
                if f0 and not s0:
                    cnt["first only (off)"] += 1
            if time.time() - t0 > WALL:
                stopped = "wall-clock cap %.0f s reached at size %r after %d worlds" % (WALL, size, n)
                break
        if stopped:
            break
    return dict(kind="ConfCl worlds", variant=VARIANT, scale=SCALE, seed=SEED, per_size=per, worlds=n, digest=dig.hexdigest(), stopped=stopped,
                last_size=repr(size_last), first_size=repr(CONF[0]), n_sizes=len(CONF), counts=dict(sorted(cnt.items())), witnesses=wit, seconds=round(time.time() - t0, 1))


def main():
    if VARIANT == "V2.6":
        res = run_pair_worlds()
    elif VARIANT == "V2.7":
        res = run_confcl_worlds()
    else:
        res = run_candidate_worlds()
    print("S108 section 2, generated worlds, variant %s, scale %s, seed %s, per size %s, %d worlds over %d sizes (first %s; last reached %s)" % (
        VARIANT, SCALE, SEED, res["per_size"], res["worlds"], res["n_sizes"], res["first_size"], res["last_size"]))
    print("digest of the worlds: %s   (the same for every variant run at this scale means the same worlds)" % res["digest"])
    if res.get("stopped"):
        print("STOPPED: %s" % res["stopped"])
    print("seconds: %s" % res["seconds"])
    for k, v in res["counts"].items():
        print("  %-80s %s" % (k, v))
    if "by_family" in res:
        print("by family:")
        for k, v in res["by_family"].items():
            print("  %-10s %s" % (k, v))
    print("smallest witnesses (first found, sizes ascending):")
    for k, w in res["witnesses"].items():
        print("--- %s (size %s)" % (k, w.get("size")))
        for kk, vv in w.items():
            if kk in ("size", "description"):
                continue
            print("   %s: %s" % (kk, vv))
        print("   " + w.get("description", "").replace("\n", "\n   "))
    if JSON:
        with open(JSON, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
