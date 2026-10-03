# S108 Part A, section 3: the generated worlds at scale 4, each section-3 variant off and on (rule 5.4).
#   PYTHONHASHSEED=0 python3 -B s108_s3_worlds.py KIND OUT.json [--scale 4] [--sizes SMALL|MID] [--seed N] [--valuemaps] [--proper]
# KIND:
#   cands   the program's candidate generator (claims_a.gen_p_cand: gen_org, gen_question, any_candidate), 40 models per size
#           times the scale, one seeded stream, sizes ascending. Per candidate, under 'none' and each reading: Acc(ℰ); Dec(t) and
#           Account ∧ ¬Dec(t) on hand-set histories (Θ by hand, I90): 'Dec', 'Con', 'Sel' (provenance_of), 'Con-chg (tags)',
#           'Con-chg (chain, cut)' for the four cuts, 'Sel-parts' (S108-3-I4), 'Con-explu (self)', 'Con-explu (widest)'
#           (S108-3-I5: the claim used is Acc of the same transport on the widest contract it translates), Build with ExplUse
#           computed; and t' = t plus a part the stated construction lacks (S108-3-I4): 'copy' (redundant) and 'deviate' (on the
#           queried port at one pair of C∖H): Acc(t'), Dec(t') on a Sel history with the parts stated, and the pairs of C∖H at
#           which the survivors on H = {(1, b0)} of the population differ.
#   chains  every chain o1 ≺ … ≺ on, n ≤ 4: (held, trace, Sel's conditions) per occurrence, contracts in {C, C'} with every
#           change recorded or not; Con, Sel, Dec at the output under each cut (U, K, T, T′), under 'none' and V3.5; and for V3.4
#           with CT reading ExplUse (S108-3-I2), n ≤ 3 with ExplUse per occurrence.
#   args    the argument generator of FC56 (random premises over p, q, r; accepted subsets; forms; every argument of height ≤ 2),
#           400 models times the scale: X_j(φ) for φ among the atoms and their denials, and usability, under 'none' and V3.1–V3.3.
#   routes  every history as a circuit of ≤ 4 occurrences (an input i and up to three nodes, each with one or two earlier parents
#           and a function from a fixed set; S108-3-I6), every R ∋ i, r (r the last node), K = {(0, 1)}: ActRoute under 'none'
#           and V3.7, and ProducedBy (some R active from i to r).
#   createx every chain n ≤ 3 with held, trace per occurrence and a criticism label per occurrence (none; a criticism of an earlier
#           design; a question about the brief labelled a criticism), one contract, the 2^10 Θ-values of (EX)'s other conjuncts
#           (as FC84.new1 (a4)): CreateEx under 'none' and V3.8.
# Reports, per reading: how many results differ from 'none', how many of each kind, and the smallest witness of each kind (the
# first found in ascending size order). Writes only OUT.json.
import argparse
import itertools
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import s108s3  # noqa: E402
from model.core import ONE, account, faithful  # noqa: E402
from model.claims_a import SMALL, MID, gen_p_cand  # noqa: E402
from model.claims_b import (Hist, sel, con, chain_eps, prov_fixed_points, build_at, faithful_on, rand_formula, ATOMS)  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
from model.args import Not, Assessor, X, usable, enumerate_args, show, canon  # noqa: E402
from model.phys import Circuit, act_route  # noqa: E402
import s108_s3_cases as K  # noqa: E402

READINGS = [(v, "prepares") for v in s108s3.VARIANTS if v != "none"] + [("V3.4", "build")]
CUTS = ("U", "K", "T", "T'")


def rn(v, ct):
    return v + ("-ctbuild" if ct == "build" else "")


def bump(d, k, n=1):
    d[k] = d.get(k, 0) + n


# ---- cands -----------------------------------------------------------------------------------------------------------------

def judge(c, H):
    acc = bool(account(c))
    occ = set(c.p.C)
    res = {"Acc": acc}
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        res["Dec " + kind] = dec
    h = Hist(["o1", "o2"], [("o1", "cod")], occ, admitted=True, prepares=True, contracts=["C", "C'"], records=[False, False])
    res["Dec Con-chg (tags)"] = not sel(c, H, h) and not con(h)
    held_out = bool(faithful(c))
    for rd in CUTS:
        fps = prov_fixed_points(2, [1, held_out], [0, 1], [0, 0], rd, True, chain_eps(["C", "C'"], [False, False]))
        res["Dec Con-chg (chain, %s)" % rd] = tuple(sorted(set(not sc[1][0] and not sc[1][1] for R, sc in fps)))
    if c.E.comps:  # a stated construction lacking one of t's parts needs t to have a part
        h = Hist(["o1"], [], occ, admitted=True, prepares=False, parts=list(c.E.comps), stated=list(c.E.comps)[:-1])
        res["Dec Sel-parts"] = not sel(c, H, h) and not con(h)
    else:
        res["Dec Sel-parts"] = res["Dec Sel"]
    ex = s108s3.expl_use(True, acc)
    h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True, explu=ex)
    res["Dec Con-explu (self)"] = not sel(c, H, h) and not con(h)
    wide = frozenset((a, b) for a in c.p.D.A for b in c.p.D.B if a in c.tau and b in c.sigma)
    acc_w = bool(account(c.replace(p=c.p.with_C(wide)))) if (ONE, c.p.b0) in wide else acc
    exw = s108s3.expl_use(True, acc_w)
    h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True, explu=exw)
    res["Dec Con-explu (widest)"] = not sel(c, H, h) and not con(h)
    res["Build (self)"] = build_at(1, [1], [1], "T'", frozenset(), 0, explu=[ex])
    res["Build (widest)"] = build_at(1, [1], [1], "T'", frozenset(), 0, explu=[exw])
    for k in list(res):
        if k.startswith("Dec "):
            d = res[k]
            res["Expl" + k[3:]] = (acc and not d) if isinstance(d, bool) else tuple(acc and not x for x in d)
    return res


def extra(c, H):
    """t' with a part the stated construction (t's own parts) lacks: 'idle', 'copy' and 'deviate' (s108_s3_cases.extra_part)."""
    out = {}
    others = [x for x in sorted(c.p.C, key=repr) if x not in H and c.translates(*x)]
    variants = [("idle", K.extra_part(c, "idle")), ("copy", K.extra_part(c, "copy"))] if c.E.comps else []  # no component: no footprint to put k_x on
    if others and c.deltaE in c.E.ports:
        a, b = others[0]
        variants.append(("deviate", K.extra_part(c, "deviate", (c.tau[a], c.sigma[b]))))
    for lab, t2 in variants:
        try:
            acc2 = bool(account(t2))
            h2 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(t2.E.comps), stated=list(c.E.comps))
            h1 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(c.E.comps), stated=list(c.E.comps))
            s2 = sel(t2, H, h2)
            pop = [x for x, h in ((c, h1), (t2, h2)) if s108s3.in_population(True, h.parts, h.stated)]
            surv = [x for x in pop if faithful_on(x, H)]
            under = sum(1 for (a, b) in others if len(set(repr(x.ans_E(x.tau[a], x.sigma[b])) for x in surv)) > 1)
            out[lab] = dict(acc=acc2, dec=not s2, expl=acc2 and s2, under=under)
        except Exception as e:  # a generated E the extra part cannot be added to is recorded, not hidden
            out[lab] = dict(error=repr(e)[:200])
    return out


def run_cands(a):
    sizes = SMALL if a.sizes == "SMALL" else MID
    per = max(1, int(40 * a.scale))
    rng = random.Random(a.seed)
    t0 = time.time()
    n = 0
    names = [rn(*r) for r in READINGS]
    summ = {v: dict(moves={}, kinds={}, witness={}) for v in names}
    base_counts = {}
    for size in sizes:
        for i in range(per):
            m = gen_p_cand(rng, size, valuemaps=a.valuemaps, proper=a.proper)
            if m is None:
                continue
            p, c = m
            n += 1
            H = [(ONE, p.b0)]
            s108s3.set_variant("none", "prepares")
            base = judge(c, H)
            bx = extra(c, H)
            bump(base_counts, "Acc true", base["Acc"])
            for lab, r in bx.items():
                if "error" in r:
                    bump(base_counts, "extra part %s: error" % lab)
            for v, ct in READINGS:
                s108s3.set_variant(v, ct)
                e = judge(c, H)
                ex = extra(c, H)
                s = summ[rn(v, ct)]
                for k in base:
                    if e[k] != base[k]:
                        bump(s["moves"], k)
                        if k.startswith("Expl") or k == "Acc":
                            kind = "%s | %s | %s | %s" % (k, c.E.meta.get("family", "?"), p.D.meta.get("family", "?"), "in" if (e[k] is True or (isinstance(e[k], tuple) and any(e[k]))) else "out")
                            bump(s["kinds"], kind)
                            if kind not in s["witness"]:
                                s["witness"][kind] = dict(size=repr(size), index=i, off=repr(base[k]), on=repr(e[k]), question=p.describe(), candidate=c.describe())
                for lab in ex:
                    for key in ("acc", "dec", "expl", "under"):
                        if key in ex[lab] and key in bx.get(lab, {}) and ex[lab][key] != bx[lab][key]:
                            kk = "t' %s: %s" % (lab, key)
                            bump(s["moves"], kk)
                            if key in ("expl", "under", "acc"):
                                kind = "%s | %s | %s" % (kk, c.E.meta.get("family", "?"), p.D.meta.get("family", "?"))
                                bump(s["kinds"], kind)
                                if kind not in s["witness"]:
                                    s["witness"][kind] = dict(size=repr(size), index=i, off=repr(bx[lab]), on=repr(ex[lab]), question=p.describe(), candidate=c.describe())
            s108s3.set_variant("none", "prepares")
    out = dict(kind="cands", models=n, sizes=a.sizes, per_size=per, seed=a.seed, valuemaps=a.valuemaps, proper=a.proper,
               base=base_counts, seconds=round(time.time() - t0, 1), readings=summ)
    print("cands: models %d (sizes %s, %d per size, seed %d, valuemaps %s, proper %s); %s; %.1f s" % (n, a.sizes, per, a.seed, a.valuemaps, a.proper, base_counts, out["seconds"]))
    for v in names:
        print("  %s: moves %s" % (v, summ[v]["moves"]))
        for k, cnt in sorted(summ[v]["kinds"].items()):
            print("     %-90s %d (smallest: %s)" % (k, cnt, summ[v]["witness"][k]["size"]))
    return out


# ---- chains ------------------------------------------------------------------------------------------------------------------

def chain_items(nmax, with_explu=False):
    for n in range(1, nmax + 1):
        for bits in itertools.product(itertools.product([0, 1], repeat=4 if with_explu else 3), repeat=n):
            held, trace, selc = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]
            explu = [b[3] for b in bits] if with_explu else None
            if with_explu:
                yield n, held, trace, selc, ["C"] * n, [False] * n, explu
                continue
            for steps in itertools.product(("same", "rec", "unrec"), repeat=n - 1):
                qs, rs = ["C"], [False]
                for st in steps:
                    if st == "same":
                        qs.append(qs[-1])
                        rs.append(False)
                    else:
                        qs.append("C'" if qs[-1] == "C" else "C")
                        rs.append(st == "rec")
                yield n, held, trace, selc, qs, rs, None


def out_at(n, held, trace, selc, qs, rs, explu, rd):
    fps = prov_fixed_points(n, held, trace, selc, rd, True, chain_eps(qs, rs), explu=explu)
    return tuple(sorted(set((sc[n - 1][0], sc[n - 1][1]) for R, sc in fps))), len(fps)


def run_chains(a):
    t0 = time.time()
    res = {}
    for (v, ct, nmax, wex) in (("V3.5", "prepares", 4, False), ("V3.4", "build", 3, True)):
        tag = rn(v, ct)
        r = dict(models=0, moves={}, witness={})
        for m in chain_items(nmax, wex):
            n, held, trace, selc, qs, rs, explu = m
            r["models"] += 1
            for rd in CUTS:
                s108s3.set_variant("none", "prepares")
                off, nfo = out_at(n, held, trace, selc, qs, rs, explu, rd)
                s108s3.set_variant(v, ct)
                on, nfn = out_at(n, held, trace, selc, qs, rs, explu, rd)
                s108s3.set_variant("none", "prepares")
                if off != on or nfo != nfn:
                    dec_off = tuple(sorted(set(not s and not k for s, k in off)))
                    dec_on = tuple(sorted(set(not s and not k for s, k in on)))
                    kind = "%s | held at output %s | Dec %s → %s" % (rd, bool(held[-1]), dec_off, dec_on)
                    bump(r["moves"], kind)
                    if kind not in r["witness"]:
                        r["witness"][kind] = dict(n=n, held=held, trace=trace, selc=selc, contracts=qs, records=rs, explu=explu,
                                                  off=repr(off), on=repr(on), fixed_points=(nfo, nfn))
        res[tag] = r
        print("chains %s: %d chains (n ≤ %d) × 4 cuts; moves at the output:" % (tag, r["models"], nmax))
        for k, cnt in sorted(r["moves"].items()):
            print("     %-70s %d (smallest: n=%d)" % (k, cnt, r["witness"][k]["n"]))
    return dict(kind="chains", seconds=round(time.time() - t0, 1), readings=res)


# ---- args --------------------------------------------------------------------------------------------------------------------

def run_args(a):
    rng = random.Random(a.seed)
    per = max(1, int(400 * a.scale))
    t0 = time.time()
    phis = ATOMS + [Not(x) for x in ATOMS]
    res = {v: dict(models=0, out_moves={}, usable_moves=0, witness={}) for v in ("V3.1", "V3.2", "V3.3")}
    n = 0
    for i in range(per):
        prem = [rand_formula(rng) for _ in range(rng.randint(2, 5))]
        acc = [x for x in prem if rng.random() < 0.5]
        forms = [f for f in ("MP", "MT", "AndI", "AndE") if rng.random() < 0.6]
        args = enumerate_args(prem, depth=2, max_args=300)
        j = Assessor(forms, acc)
        n += 1
        s108s3.set_variant("none")
        base_u = [usable(j, x) for x in args]
        base_x = {repr(ph): set(id(x) for x in X(j, ph, args)) for ph in phis}
        for v in res:
            s108s3.set_variant(v)
            u = [usable(j, x) for x in args]
            xs = {repr(ph): set(id(x) for x in X(j, ph, args)) for ph in phis}
            r = res[v]
            r["models"] += 1
            r["usable_moves"] += sum(1 for p_, q_ in zip(base_u, u) if p_ != q_)
            for ph in phis:
                k = repr(ph)
                if bool(base_x[k]) != bool(xs[k]):
                    kind = "Out_j(φ) %s → %s" % (bool(base_x[k]), bool(xs[k]))
                    bump(r["out_moves"], kind)
                    if kind not in r["witness"] or len(prem) < r["witness"][kind]["n_prem"]:
                        new = [x for x in args if id(x) in (xs[k] ^ base_x[k])]
                        r["witness"][kind] = dict(n_prem=len(prem), premises=[show(x) for x in prem], accepted=[show(x) for x in acc], forms=forms, phi=show(ph),
                                                  argument=new[0].show(2) if new else None)
                elif base_x[k] != xs[k]:
                    bump(r["out_moves"], "X_j(φ) differs, Out_j(φ) the same")
        s108s3.set_variant("none")
    print("args: %d models (FC56's generator, %d per the claim's size times the scale), φ ∈ {p, q, r, ¬p, ¬q, ¬r}; %.1f s" % (n, per, time.time() - t0))
    for v, r in res.items():
        print("  %s: arguments whose usability moves %d; %s" % (v, r["usable_moves"], r["out_moves"]))
        for k, w in r["witness"].items():
            print("     smallest for '%s': %d premises %s, accepted %s, forms %s, φ = %s" % (k, w["n_prem"], w["premises"], w["accepted"], w["forms"], w["phi"]))
    return dict(kind="args", models=n, seed=a.seed, seconds=round(time.time() - t0, 1), readings=res)


# ---- routes ------------------------------------------------------------------------------------------------------------------

UNARY = {"id": lambda x: x, "not": lambda x: 1 - x, "c0": lambda x: 0, "c1": lambda x: 1}
BINARY = {"and": lambda x, y: x & y, "or": lambda x, y: x | y, "xor": lambda x, y: x ^ y, "first": lambda x, y: x, "second": lambda x, y: y}


def circuits(nmax=4):
    for n in range(2, nmax + 1):
        names = ["i"] + ["n%d" % k for k in range(1, n)]
        opts = []
        for k in range(1, n):
            earlier = names[:k]
            o = []
            for p in earlier:
                for fn in UNARY:
                    o.append(((p,), fn))
            for p, q in itertools.combinations(earlier, 2):
                for fn in BINARY:
                    o.append(((p, q), fn))
            opts.append(o)
        for choice in itertools.product(*opts):
            nodes = {}
            for k, (ps, fn) in enumerate(choice, start=1):
                nodes[names[k]] = (ps, UNARY[fn] if len(ps) == 1 else BINARY[fn])
            yield n, names, choice, Circuit(nodes, {"i": 1})


def run_routes(a):
    t0 = time.time()
    r = dict(circuits=0, routes=0, route_moves=0, producedby_moves=0, producesvia_pairs=0, producesvia_moves=0, kinds={}, witness={}, none_fail_reasons={})
    for n, names, choice, h in circuits(4):
        r["circuits"] += 1
        rr = names[-1]
        mids = names[1:-1]
        pb = {"none": False, "V3.7": False}
        pv = {"none": set(), "V3.7": set()}  # ProducesVia (D14.6): the binding occurrence b (a middle node) on some active route from i to r
        for sub in itertools.chain.from_iterable(itertools.combinations(mids, k) for k in range(len(mids) + 1)):
            R = {"i", rr} | set(sub)
            r["routes"] += 1
            res = {}
            for v in ("none", "V3.7"):
                s108s3.set_variant(v)
                res[v] = act_route(h, R, "i", rr, [(0, 1)])
                pb[v] = pb[v] or res[v][0]
                if res[v][0]:
                    pv[v] |= set(sub)
            s108s3.set_variant("none")
            if res["none"][0] != res["V3.7"][0]:
                r["route_moves"] += 1
                kind = "active F → T (none: %s)" % res["none"][1]
                bump(r["kinds"], kind)
                if kind not in r["witness"]:
                    r["witness"][kind] = dict(n=n, circuit=["%s := %s(%s)" % (names[k], fn, ",".join(ps)) for k, (ps, fn) in enumerate(choice, start=1)], R=sorted(R))
            elif not res["none"][0]:
                bump(r["none_fail_reasons"], res["none"][1].split(" (")[0] if "feeds r" not in res["none"][1] else "a member feeds r by no path inside R")
        if pb["none"] != pb["V3.7"]:
            r["producedby_moves"] += 1
        r["producesvia_pairs"] += len(mids)
        r["producesvia_moves"] += len(pv["none"] ^ pv["V3.7"])
    print("routes: %d circuits of ≤ 4 occurrences, %d (circuit, R) routes; ActRoute moves %d; ProducedBy (some R from i to r active) moves %d; "
          "ProducesVia (a middle occurrence b on some active R) moves on %d of %d (circuit, b); %.1f s"
          % (r["circuits"], r["routes"], r["route_moves"], r["producedby_moves"], r["producesvia_moves"], r["producesvia_pairs"], time.time() - t0))
    for k, cnt in r["kinds"].items():
        print("     %-70s %d; smallest: %s" % (k, cnt, r["witness"][k]))
    print("     routes inactive under both, why (none): %s" % r["none_fail_reasons"])
    return dict(kind="routes", seconds=round(time.time() - t0, 1), result=r)


# ---- createx ------------------------------------------------------------------------------------------------------------------

THETA = ("recognized difficulty", "target represented before its criticism", "a response using the criticism (D9.11)", "Conn(G, h')",
         "Repair (P)", "o in O_ex", "Attempt, New", "Deploy", "ProducesVia", "Acc(c, p_c, t_c, Γ_c, δ_c)")
LABELS = (None, ("t0 (an earlier design)", "fails the load case"), ("C_brief (the contract)", "why this brief?"))


def cx_values(crit_clause, build, v):
    s108s3.set_variant(v)
    tv = 0
    for bits in itertools.product([False, True], repeat=len(THETA)):
        w = dict(zip(THETA, bits))
        cce = (crit_clause and w["recognized difficulty"] and w["target represented before its criticism"] and w["a response using the criticism (D9.11)"]
               and w["Conn(G, h')"] and build and w["Attempt, New"])
        tv += s108s3.create_ex(cce, w["Attempt, New"] and build, w["Repair (P)"] and w["o in O_ex"] and w["Deploy"] and w["ProducesVia"] and w["Acc(c, p_c, t_c, Γ_c, δ_c)"])
    s108s3.set_variant("none")
    return tv


def run_createx(a):
    t0 = time.time()
    table = {(cc, b): (cx_values(cc, b, "none"), cx_values(cc, b, "V3.8")) for cc in (False, True) for b in (False, True)}
    r = dict(chains=0, valuations=0, moves=0, kinds={}, witness={})
    for n in (1, 2, 3):
        for bits in itertools.product(itertools.product([0, 1], repeat=2), repeat=n):
            held, trace = [b[0] for b in bits], [b[1] for b in bits]
            fps = prov_fixed_points(n, held, trace, [0] * n, "T'", True, chain_eps(["C_brief"] * n, [False] * n))
            build = build_at(n, held, trace, "T'", fps[0][0] if fps else frozenset(), n - 1)
            for labs in itertools.product(LABELS, repeat=n):
                r["chains"] += 1
                r["valuations"] += 1024
                cc = any(x is not None for x in labs)
                off, on = table[(cc, bool(build))]
                if off != on:
                    r["moves"] += on - off
                    kind = "criticism in the chain %s, Build %s: CreateEx true on %d → %d of 1024" % (cc, bool(build), off, on)
                    bump(r["kinds"], kind)
                    if kind not in r["witness"]:
                        r["witness"][kind] = dict(n=n, held=held, trace=trace, labels=[None if x is None else list(x) for x in labs])
    print("createx: %d chains (n ≤ 3; held, trace, a label per occurrence), %d valuations; CreateEx F → T on %d; %.1f s" % (r["chains"], r["valuations"], r["moves"], time.time() - t0))
    for k, cnt in sorted(r["kinds"].items()):
        print("     %-90s %d chains; smallest: %s" % (k, cnt, r["witness"][k]))
    print("     per (criticism in the chain, Build): (none, V3.8) true of 1024: %s" % {"%s,%s" % k: v for k, v in table.items()})
    return dict(kind="createx", seconds=round(time.time() - t0, 1), result=r, table={"%s,%s" % k: v for k, v in table.items()})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=("cands", "chains", "args", "routes", "createx"))
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--sizes", default="SMALL")
    ap.add_argument("--seed", type=int, default=108301)
    ap.add_argument("--valuemaps", action="store_true")
    ap.add_argument("--proper", action="store_true")
    a = ap.parse_args()
    fn = dict(cands=run_cands, chains=run_chains, args=run_args, routes=run_routes, createx=run_createx)[a.kind]
    out = fn(a)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=repr)


if __name__ == "__main__":
    main()
