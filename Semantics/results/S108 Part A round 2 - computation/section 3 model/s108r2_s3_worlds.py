# S108 Part A round 2, section 3: the generated worlds at scale 4, each round-2 state off and on (rule 5.4).
#   PYTHONHASHSEED=0 python3 -B s108r2_s3_worlds.py KIND OUT.json [--scale 4] [--sizes SMALL|MID] [--seed N] [--valuemaps] [--proper] [--nmax N]
# KIND:
#   cands     the program's candidate generator (claims_a.gen_p_cand), round 1's seeds and sizes: every result of
#             s108r2_s3_common.judge and of t′ = t + a part ('idle', 'copy', 'deviate'), under every state of STATES against its
#             baseline: how many move, of which kind, the smallest witness of each (the first in ascending size order)
#   crosscheck chain_out (the staged evaluator the chains use) against claims_b.prov_fixed_points on every chain n ≤ 3, cuts T′,
#             T, K, under the switch states the chains use
#   chains    every chain o1 ≺ … ≺ on (n ≤ nmax): held, trace, Sel's conditions per occurrence; contracts C, C′ with each change
#             recorded or not (round 1's and the second checker's enumeration); the output's trace starting at any o_s (s = t:
#             the program's one-occurrence trace). Dec at the output under 'none', V3.5 (C9), R2V3.7 and V3.5 with R2V3.7, cuts
#             T′, T, K (and U for n ≤ 3)
#   keys      as chains, with a record flag at every occurrence (a record made there of the contract operative there), so that
#             D13.8's two keys can differ: Dec at the output, key 'change' (the program) and 'contract' (the formal core's
#             words), with and without V3.5; cut T′ (n ≤ nmax) and K (n ≤ 3)
#   explu     round 1's V3.4 chains (n ≤ 3, one contract, ExplUse per occurrence) under R2V3.1's switch (V3.4 with CT reading ExplUse)
#   args      FC56's argument generator (round 1's), under 'none', R2V3.8 and R2V3.9; for R2V3.9 the atom r is typed as an answer
#             claim ('ans_r')
#   routes    round 1's circuits (≤ 4 occurrences), every R ∋ i, r; K = {(0,1)}; a represented objection ob with one role bound to i
#             (m: ob ↦ i, Rec = {id}, Chg = ∅): UsesReason (D9.11) under 'none' and V3.7, read with 'an active route' any route
#             (the words) and R itself (S108r2-3-I7); e3.34b
#   fc80x     FC80's generator with a stated construction per population (the base member's parts, S108r2-3-I8) and, for each member,
#             a twin with one more part deviating at one pair of C∖H: the survivors on H in 𝒯 and the pairs of C∖H they leave
#             underdetermined, under 'none', V3.6, R2V3.4 (ports) and R2V3.4 (edits); e3.30b
#   createx   (EX)'s e_c ⪯_h e (D14.7) on chains n ≤ 4 with e_c at each occurrence, the 1,024 Θ-values of FC84.new1 (a4), under
#             'none' and R2V3.7
# Writes only OUT.json (and prints).
import argparse
import itertools
import json
import random
import time

import s108r2_s3_common as K
from s108r2_s3_common import set_state, reset, STATES, BASE, judge, pre_of, chain_dec, chain_out, in_pop
from model import s108s3, s108r2s3
from model.core import ONE, Org, account
from model.claims_a import SMALL, MID, gen_p_cand
from model.claims_b import (Hist, sel, chain_eps, prov_fixed_points, faithful_on, rand_formula, ATOMS, D_and_p, gen_candidate, all_pairs)
from model.args import Not, Assessor, X, usable, enumerate_args, show
from model.phys import act_route
import s108_s3_cases as R1
import s108_s3_worlds as W1

CUTS = ("T'", "T", "K")


def bump(d, k, n=1):
    d[k] = d.get(k, 0) + n


def direction(v):
    return "in" if (v is True or (isinstance(v, tuple) and any(v))) else "out"


# ---- cands -----------------------------------------------------------------------------------------------------------------

def extras_pre(c, H):
    """t′ = t + k_x ('idle', 'copy', 'deviate'), each with Acc(t′) (no switch of section 3 reaches account)."""
    out = []
    others = [x for x in sorted(c.p.C, key=repr) if x not in H and c.translates(*x)]
    vs = [("idle", R1.extra_part(c, "idle")), ("copy", R1.extra_part(c, "copy"))] if c.E.comps else []
    if others and c.deltaE in c.E.ports:
        a, b = others[0]
        vs.append(("deviate", R1.extra_part(c, "deviate", (c.tau[a], c.sigma[b]))))
    for lab, t2 in vs:
        try:
            out.append((lab, t2, bool(account(t2))))
        except Exception as e:  # recorded, not hidden
            out.append((lab, None, repr(e)[:120]))
    return out, others


def extras_eval(c, H, xs, others):
    res = {}
    for lab, t2, acc2 in xs:
        if t2 is None:
            res["t′ %s" % lab] = ("error", acc2)
            continue
        h2 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(t2.E.comps), stated=list(c.E.comps))
        h1 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(c.E.comps), stated=list(c.E.comps))
        s2 = sel(t2, H, h2)
        pop = [x for x, h in ((c, h1), (t2, h2)) if in_pop(x, h)]
        surv = [x for x in pop if faithful_on(x, H)]
        under = sum(1 for (a, b) in others if len(set(repr(x.ans_E(x.tau[a], x.sigma[b])) for x in surv)) > 1)
        res["Expl t′ %s" % lab] = acc2 and s2
        res["Dec t′ %s" % lab] = not s2
        res["under t′ %s" % lab] = under
    return res


def run_cands(a):
    sizes = SMALL if a.sizes == "SMALL" else MID
    per = max(1, int(40 * a.scale))
    rng = random.Random(a.seed)
    t0 = time.time()
    n = 0
    names = [nm for nm, _ in STATES]
    summ = {v: dict(moves={}, kinds={}, witness={}) for v in names[1:]}
    base_counts = {}
    for size in sizes:
        for i in range(per):
            m = gen_p_cand(rng, size, valuemaps=a.valuemaps, proper=a.proper)
            if m is None:
                continue
            p, c = m
            n += 1
            H = [(ONE, p.b0)]
            pre = pre_of(c)
            xs, others = extras_pre(c, H)
            bump(base_counts, "Acc true", pre["acc"])
            for w in K.CLAIMS:
                if pre["acc"] and pre[w] is False:
                    bump(base_counts, "Acc T, Acc(ℰ′) F: " + w)
                if pre[w] is None:
                    bump(base_counts, "no ℰ′: " + w)
            res = {}
            for nm, kw in STATES:
                set_state(**kw)
                r = judge(c, H, pre=pre)
                r.update(extras_eval(c, H, xs, others))
                res[nm] = r
            reset()
            for nm in names[1:]:
                b, e = res[BASE.get(nm, "none")], res[nm]
                s = summ[nm]
                for k in e:
                    if k in b and e[k] != b[k]:
                        if k.startswith("Expl"):
                            kk = "%s %s" % (k, direction(e[k]))
                        elif k.startswith("Dec"):
                            kk = "%s (Acc %s)" % (k, "T" if pre["acc"] else "F")
                        elif k.startswith("under"):
                            kk = "%s %s" % (k, "up" if e[k] > b[k] else "down")
                        else:
                            kk = k
                        bump(s["moves"], kk)
                        if (k.startswith("Expl") or k.startswith("under")) and kk not in s["witness"]:
                            s["witness"][kk] = dict(size=repr(size), index=i, off=repr(b[k]), on=repr(e[k]),
                                                    family=(c.E.meta.get("family", "?"), p.D.meta.get("family", "?")),
                                                    question=p.describe(), candidate=c.describe())
    out = dict(kind="cands", models=n, sizes=a.sizes, per_size=per, seed=a.seed, valuemaps=a.valuemaps, proper=a.proper,
               base=base_counts, seconds=round(time.time() - t0, 1), states=summ)
    print("cands: models %d (sizes %s, %d per size, seed %d, valuemaps %s, proper %s); %s; %.1f s" % (n, a.sizes, per, a.seed, a.valuemaps, a.proper, base_counts, out["seconds"]))
    for v in names[1:]:
        mv = summ[v]["moves"]
        print("  %s (against %s): %s" % (v, BASE.get(v, "none"), {k: x for k, x in sorted(mv.items()) if k.startswith(("Expl", "under"))} or "no move of Account ∧ ¬Dec(t)"))
        other = {k: x for k, x in sorted(mv.items()) if not k.startswith(("Expl", "under"))}
        if other:
            print("      other moves: %s" % other)
        for k, w in sorted(summ[v]["witness"].items()):
            print("      smallest for %-50s size %s, families %s, %s → %s" % (k, w["size"], w["family"], w["off"], w["on"]))
    return out


# ---- chains ----------------------------------------------------------------------------------------------------------------

def items(nmax, records_anywhere=False, starts=True, nmin=1):
    for n in range(nmin, nmax + 1):
        for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n):
            held, trace, selc = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]
            if records_anywhere:
                seqs = []
                for sw in itertools.product([0, 1], repeat=n - 1):
                    qs = ["C"]
                    for x in sw:
                        qs.append(("C'" if qs[-1] == "C" else "C") if x else qs[-1])
                    for rs in itertools.product([False, True], repeat=n):
                        seqs.append((qs, list(rs)))
            else:
                seqs = []
                for steps in itertools.product(("same", "rec", "unrec"), repeat=n - 1):
                    qs, rs = ["C"], [False]
                    for st in steps:
                        if st == "same":
                            qs.append(qs[-1])
                            rs.append(False)
                        else:
                            qs.append("C'" if qs[-1] == "C" else "C")
                            rs.append(st == "rec")
                    seqs.append((qs, rs))
            for qs, rs in seqs:
                for s_out in (range(n) if starts else [n - 1]):
                    start = list(range(n))
                    start[n - 1] = s_out
                    yield n, held, trace, selc, qs, rs, start


def run_crosscheck(a):
    t0 = time.time()
    states = [("none", {}), ("V3.5", dict(r1="V3.5")), ("key contract", dict(reckey="contract")), ("R2V3.7", dict(r2="R2V3.7")),
              ("V3.5 + R2V3.7", dict(r1="V3.5", r2="R2V3.7")), ("V3.5 + key contract", dict(r1="V3.5", reckey="contract"))]
    res = {}
    for nm, kw in states:
        set_state(**kw)
        cnt = dict(chains=0, mismatch=0, first=None)
        for m in itertools.chain(items(3, records_anywhere=True, starts=False)):
            n, held, trace, selc, qs, rs, start = m
            for rd in CUTS:
                cnt["chains"] += 1
                fps = prov_fixed_points(n, held, trace, selc, rd, True, chain_eps(qs, rs))
                ref = [sc for R, sc in fps]
                mine = chain_out(n, held, trace, selc, qs, rs, rd)
                if len(ref) != 1 or [ref[0][o] for o in range(n)] != mine:
                    cnt["mismatch"] += 1
                    if cnt["first"] is None:
                        cnt["first"] = dict(n=n, held=held, trace=trace, selc=selc, qs=qs, rs=rs, rd=rd, ref=repr(ref), mine=repr(mine))
        res[nm] = cnt
        print("crosscheck %-22s (chain, cut) pairs %d, mismatches %d %s" % (nm, cnt["chains"], cnt["mismatch"], cnt["first"] or ""))
    reset()
    return dict(kind="crosscheck", seconds=round(time.time() - t0, 1), states=res)


def run_chains(a):
    t0 = time.time()
    states = [("none", {}), ("V3.5", dict(r1="V3.5")), ("R2V3.7", dict(r2="R2V3.7")), ("V3.5 + R2V3.7", dict(r1="V3.5", r2="R2V3.7"))]
    comps = [  # (label, (state, extent), (state, extent)); extent 'ot' = the program's trace at o_t, 'span' = from o_s
        ("R2V3.3 (b): the trace spanning o_s…o_t against the trace at o_t, record clause kept", ("none", "ot"), ("none", "span")),
        ("C9 (V3.5), the trace at o_t", ("none", "ot"), ("V3.5", "ot")),
        ("C9 (V3.5), the trace spanning o_s…o_t", ("none", "span"), ("V3.5", "span")),
        ("R2V3.7, the trace at o_t", ("none", "ot"), ("R2V3.7", "ot")),
        ("R2V3.7, the trace spanning o_s…o_t", ("none", "span"), ("R2V3.7", "span")),
        ("C9 (V3.5) under R2V3.7, the trace at o_t", ("R2V3.7", "ot"), ("V3.5 + R2V3.7", "ot")),
        ("C9 (V3.5) under R2V3.7, the trace spanning", ("R2V3.7", "span"), ("V3.5 + R2V3.7", "span")),
    ]
    res = {}
    for rd in CUTS + ("U",):
        nmax = a.nmax if rd != "U" else min(3, a.nmax)
        acc = {lab: dict(chains=0, moves={}, witness={}) for lab, _, _ in comps}
        for m in items(nmax):
            n, held, trace, selc, qs, rs, start = m
            spans = start[n - 1] < n - 1
            if not spans:
                enc = "trace at o_t"
            else:
                unrec = any(qs[i] != qs[i - 1] and not rs[i] for i in range(start[n - 1] + 1, n))
                enc = "trace spans an unrecorded change" if unrec else "trace spans, no unrecorded change"
            vals = {}
            for nm, kw in states:
                set_state(**kw)
                vals[(nm, "ot")] = chain_dec(n, held, trace, selc, qs, rs, rd) if not spans else None
                vals[(nm, "span")] = chain_dec(n, held, trace, selc, qs, rs, rd, start=start) if spans else None
            reset()
            for lab, x, y in comps:
                # 'ot' comparisons run on the chains whose output trace is at o_t; 'span' on those whose trace spans
                if (x[1] == "span" or y[1] == "span") and not spans:
                    continue
                if x[1] == "ot" and y[1] == "ot" and spans:
                    continue
                if x[1] == "ot" and y[1] == "span":
                    vx = chain_dec(n, held, trace, selc, qs, rs, rd)  # the same chain with the program's one-occurrence trace
                else:
                    vx = vals[x]
                vy = vals[y]
                r = acc[lab]
                r["chains"] += 1
                if vx != vy:
                    kind = "%s | held at the output %s | Dec %s → %s" % (enc, bool(held[-1]), vx, vy)
                    bump(r["moves"], kind)
                    if kind not in r["witness"]:
                        r["witness"][kind] = dict(n=n, held=held, trace=trace, selc=selc, contracts=qs, records=rs, output_trace_from="o%d" % (start[-1] + 1))
        res[rd] = acc
        print("chains, cut %s, n ≤ %d:" % (rd, nmax))
        for lab, _, _ in comps:
            r = acc[lab]
            print("   %-80s chains %7d; moves %s" % (lab, r["chains"], {k: v for k, v in sorted(r["moves"].items())} or 0))
            for k, w in sorted(r["witness"].items()):
                if "held at the output True" in k:
                    print("        smallest (held at the output): %s" % w)
    return dict(kind="chains", nmax=a.nmax, seconds=round(time.time() - t0, 1), cuts=res)


def run_keys(a):
    t0 = time.time()
    states = [("change", {}), ("contract", dict(reckey="contract")), ("V3.5 change", dict(r1="V3.5")), ("V3.5 contract", dict(r1="V3.5", reckey="contract"))]
    comps = [("R2V3.2: key 'contract' (the formal core's words) → 'change' (the variant; the program)", "contract", "change"),
             ("C9 (V3.5) under key 'change'", "change", "V3.5 change"),
             ("C9 (V3.5) under key 'contract'", "contract", "V3.5 contract")]
    res = {}
    for rd in ("T'", "K"):
        nmax = a.nmax if rd == "T'" else min(3, a.nmax)
        acc = {lab: dict(chains=0, moves={}, witness={}) for lab, _, _ in comps}
        for m in items(nmax, records_anywhere=True):
            n, held, trace, selc, qs, rs, start = m
            spans = start[n - 1] < n - 1
            vals = {}
            for nm, kw in states:
                set_state(**kw)
                vals[nm] = chain_dec(n, held, trace, selc, qs, rs, rd, start=start if spans else None)
            reset()
            reentry = len(set(qs)) < sum(1 for i in range(n) if i == 0 or qs[i] != qs[i - 1])
            enc = ("trace spans" if spans else "trace at o_t") + (", a contract entered twice" if reentry else "")
            for lab, x, y in comps:
                r = acc[lab]
                r["chains"] += 1
                if vals[x] != vals[y]:
                    kind = "%s | held at the output %s | Dec %s → %s" % (enc, bool(held[-1]), vals[x], vals[y])
                    bump(r["moves"], kind)
                    if kind not in r["witness"]:
                        r["witness"][kind] = dict(n=n, held=held, trace=trace, selc=selc, contracts=qs, records=rs, output_trace_from="o%d" % (start[-1] + 1))
        res[rd] = acc
        print("keys, cut %s, n ≤ %d (a record flag at every occurrence):" % (rd, nmax))
        for lab, _, _ in comps:
            r = acc[lab]
            print("   %-90s chains %7d; moves %s" % (lab, r["chains"], {k: v for k, v in sorted(r["moves"].items())} or 0))
            for k, w in sorted(r["witness"].items()):
                if "held at the output True" in k:
                    print("        smallest (held at the output): %s" % w)
    return dict(kind="keys", nmax=a.nmax, seconds=round(time.time() - t0, 1), cuts=res)


def run_explu(a):
    t0 = time.time()
    res = {}
    for rd in ("T'", "T", "K", "U"):
        r = dict(chains=0, moves={}, witness={})
        for n in (1, 2, 3):
            for bits in itertools.product(itertools.product([0, 1], repeat=4), repeat=n):
                held, trace, selc, explu = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits], [b[3] for b in bits]
                r["chains"] += 1
                vals = {}
                for nm, kw in (("none", {}), ("R2V3.1", dict(r2="R2V3.1"))):
                    set_state(**kw)
                    fps = prov_fixed_points(n, held, trace, selc, rd, True, chain_eps(["C"] * n, [False] * n), explu=explu)
                    vals[nm] = tuple(sorted(set(not sc[n - 1][0] and not sc[n - 1][1] for R, sc in fps)))
                reset()
                if vals["none"] != vals["R2V3.1"]:
                    kind = "held at the output %s | Dec %s → %s" % (bool(held[-1]), vals["none"], vals["R2V3.1"])
                    bump(r["moves"], kind)
                    if kind not in r["witness"]:
                        r["witness"][kind] = dict(n=n, held=held, trace=trace, selc=selc, explu=explu)
        res[rd] = r
        print("explu, cut %s: %d chains (n ≤ 3, ExplUse per occurrence); moves %s" % (rd, r["chains"], r["moves"]))
    return dict(kind="explu", seconds=round(time.time() - t0, 1), cuts=res)


# ---- args ------------------------------------------------------------------------------------------------------------------

def run_args(a):
    rng = random.Random(a.seed)
    per = max(1, int(400 * a.scale))
    t0 = time.time()
    res = {}
    for typed in (False, True):
        ren = (lambda f: rename(f, "r", "ans_r")) if typed else (lambda f: f)
        atoms = [ren(x) for x in ATOMS]
        phis = atoms + [Not(x) for x in atoms]
        rng = random.Random(a.seed)
        for v in (("R2V3.8",) if not typed else ("R2V3.9",)):
            r = dict(models=0, usable_moves=0, out_moves={}, witness={})
            for i in range(per):
                prem = [ren(rand_formula(rng)) for _ in range(rng.randint(2, 5))]
                acc = [x for x in prem if rng.random() < 0.5]
                forms = [f for f in ("MP", "MT", "AndI", "AndE") if rng.random() < 0.6]
                j = Assessor(forms, acc)
                r["models"] += 1
                vals = {}
                for nm, kw in (("none", {}), (v, dict(r2=v))):
                    set_state(**kw)
                    args = enumerate_args(prem, depth=2, max_args=300)
                    vals[nm] = ({id(x) if False else show_tree(x) for x in args if usable(j, x)},
                                {repr(ph): bool(X(j, ph, args)) for ph in phis})
                reset()
                r["usable_moves"] += len(vals["none"][0] ^ vals[v][0])
                for ph in phis:
                    k = repr(ph)
                    if vals["none"][1][k] != vals[v][1][k]:
                        kind = "Out_j(φ) %s → %s" % (vals["none"][1][k], vals[v][1][k])
                        bump(r["out_moves"], kind)
                        if kind not in r["witness"] or len(prem) < r["witness"][kind]["n_prem"]:
                            r["witness"][kind] = dict(n_prem=len(prem), premises=[show(x) for x in prem], accepted=[show(x) for x in acc], forms=forms, phi=show(ph))
            res[v] = r
            print("args %s (%s): %d models; usable arguments that move %d; %s" % (v, "r typed as an answer claim 'ans_r'" if typed else "FC56's generator", r["models"], r["usable_moves"], r["out_moves"]))
            for k, w in r["witness"].items():
                print("     smallest for '%s': %s" % (k, w))
    return dict(kind="args", seed=a.seed, seconds=round(time.time() - t0, 1), states=res)


def rename(f, old, new):
    if isinstance(f, str):
        return new if f == old else f
    return (f[0],) + tuple(rename(g, old, new) for g in f[1:])


def show_tree(x):
    return x.show(0) if hasattr(x, "show") else repr(x)


# ---- routes (e3.34b) -------------------------------------------------------------------------------------------------------

def run_routes(a):
    t0 = time.time()
    r = dict(circuits=0, routes=0, active_moves=0, uses_any_moves=0, uses_R_moves=0, did_no_work=0, did_no_work_uses_any_moves=0,
             did_no_work_uses_R_moves=0, did_no_work_uses_any_already=0, witness={})
    for n, names, choice, h in W1.circuits(4):
        r["circuits"] += 1
        rr = names[-1]
        mids = names[1:-1]
        subs = [{"i", rr} | set(sub) for sub in itertools.chain.from_iterable(itertools.combinations(mids, k) for k in range(len(mids) + 1))]
        act = {}
        for v in ("none", "V3.7"):
            s108s3.set_variant(v)
            act[v] = [act_route(h, R, "i", rr, [(0, 1)])[0] for R in subs]
        s108s3.set_variant("none")
        # UsesReason(R, ob): m sends ob's one role port to i ∈ R (Rec = {id}, Chg = ∅, so the recoding and change clauses hold);
        # 'some image port of m on an active route': any route through i (the words), or R itself (S108r2-3-I7)
        any_act = {v: any(act[v]) for v in act}  # every route of the circuit holds i
        for R, a0, a1 in zip(subs, act["none"], act["V3.7"]):
            r["routes"] += 1
            if a0 != a1:
                r["active_moves"] += 1
                r["did_no_work"] += 1
                if any_act["none"]:
                    r["did_no_work_uses_any_already"] += 1
                else:
                    r["did_no_work_uses_any_moves"] += 1
                r["did_no_work_uses_R_moves"] += 1
                if "no work" not in r["witness"]:
                    r["witness"]["no work"] = dict(n=n, circuit=["%s := %s(%s)" % (names[k], fn, ",".join(ps)) for k, (ps, fn) in enumerate(choice, start=1)], R=sorted(R))
            if any_act["none"] != any_act["V3.7"]:
                r["uses_any_moves"] += 1
            if a0 != a1:
                r["uses_R_moves"] += 1
    print("routes: %d circuits, %d (circuit, R); ActRoute F → T under V3.7 on %d (the routes that did no work); UsesReason(R, ob), ob's role at i:"
          % (r["circuits"], r["routes"], r["active_moves"]))
    print("   'an active route' read as any route: F → T on %d (circuit, R), of which on the routes that did no work %d; on %d of those routes UsesReason already held under 'none' (another route through i active)"
          % (r["uses_any_moves"], r["did_no_work_uses_any_moves"], r["did_no_work_uses_any_already"]))
    print("   'an active route' read as R itself: F → T on %d (circuit, R), exactly the routes that did no work (%d)" % (r["uses_R_moves"], r["did_no_work_uses_R_moves"]))
    print("   smallest: %s" % r["witness"].get("no work"))
    return dict(kind="routes", seconds=round(time.time() - t0, 1), result=r)


# ---- fc80x (e3.30b) --------------------------------------------------------------------------------------------------------

def run_fc80x(a):
    t0 = time.time()
    rng = random.Random(a.seed)
    per = max(1, int(30 * a.scale))
    states = [("none", {}), ("V3.6", dict(r1="V3.6")), ("R2V3.4 ports", dict(r2="R2V3.4", parts="ports")), ("R2V3.4 edits", dict(r2="R2V3.4", parts="edits"))]
    res = {nm: dict(models=0, underdetermined_models=0, underdetermined_pairs=0, pop=0, witness=None) for nm, _ in states}
    moves = {nm: dict(more=0, fewer=0) for nm, _ in states[1:]}
    for size in SMALL:
        for i in range(per):
            D, p = D_and_p(rng, size)
            if D is None or len(p.C) < 2:
                continue
            base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
            if not base.E.comps:
                continue
            pop = [base]
            for k_ in range(3):  # FC80's own alterations: one component's relation altered at one pair
                E = base.E
                kk = rng.choice(list(E.comps))
                x = rng.choice(all_pairs(D))
                w = rng.choice(sorted(E.full(kk))) if E.full(kk) else None
                if w is None:
                    continue
                E2 = Org("E_%d" % k_, E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                         (lambda k1, x1, w1: (lambda j, a2, b2: (E.L(j, a2, b2) ^ {w1}) if (j, a2, b2) == (k1, x1[0], x1[1]) else E.L(j, a2, b2)))(kk, x, w))
                pop.append(base.replace(E=E2, name="t%d" % k_))
            H = [x for x in p.C if rng.random() < 0.5] or [(ONE, p.b0)]
            others = [x for x in sorted(p.C, key=repr) if x not in H and base.translates(*x)]
            twins = []
            if others and base.deltaE in base.E.ports:
                ab = rng.choice(others)
                for mbr in pop:  # each member's twin with one more part deviating at one pair of C∖H (S108r2-3-I8)
                    try:
                        twins.append(R1.extra_part(mbr, "deviate", (mbr.tau[ab[0]], mbr.sigma[ab[1]])))
                    except Exception:
                        pass
            allpop = pop + twins
            per_state = {}
            for nm, kw in states:
                set_state(**kw)
                inT = [mbr for mbr in allpop if in_pop(mbr, Hist(["o1"], [], set(p.C), admitted=True, parts=list(mbr.E.comps), stated=list(base.E.comps)))]
                surv = [mbr for mbr in inT if faithful_on(mbr, H)]
                und = sum(1 for (a1, b1) in p.C if (a1, b1) not in H and base.translates(a1, b1)
                          and len(set(repr(mbr.ans_E(mbr.tau[a1], mbr.sigma[b1])) for mbr in surv)) > 1)
                per_state[nm] = und
                r = res[nm]
                r["models"] += 1
                r["pop"] += len(inT)
                r["underdetermined_pairs"] += und
                if und:
                    r["underdetermined_models"] += 1
                    if r["witness"] is None:
                        r["witness"] = dict(size=repr(size), index=i, members_in_T=len(inT), survivors=len(surv), pairs=und, question=p.describe())
            reset()
            for nm, _ in states[1:]:
                if per_state[nm] > per_state["none"]:
                    moves[nm]["more"] += 1
                elif per_state[nm] < per_state["none"]:
                    moves[nm]["fewer"] += 1
    print("fc80x: FC80's populations (SMALL, %d per size) with a stated construction (the base member's parts) and deviating twins; %.1f s" % (per, time.time() - t0))
    for nm, _ in states:
        r = res[nm]
        print("   %-14s models %d; members in 𝒯 %d; models with a pair of C∖H underdetermined by the survivors %d; such pairs %d; %s"
              % (nm, r["models"], r["pop"], r["underdetermined_models"], r["underdetermined_pairs"], ("against 'none': " + repr(moves[nm])) if nm in moves else ""))
    return dict(kind="fc80x", seed=a.seed, seconds=round(time.time() - t0, 1), states=res, moves=moves)


# ---- createx (R2V3.7 on (EX)'s e_c ⪯ e) ------------------------------------------------------------------------------------

def run_createx(a):
    t0 = time.time()
    r = dict(pairs=0, moves=0, valuations_moved=0, by_n={})
    for v in ("none", "R2V3.7"):
        pass
    for n in (1, 2, 3, 4):
        for k in range(n):  # e_c = o_{k+1}, e = o_n
            r["pairs"] += 1
            prec = {}
            for nm, kw in (("none", {}), ("R2V3.7", dict(r2="R2V3.7"))):
                set_state(**kw)
                prec[nm] = k in s108r2s3.witnesses(0, n - 1)
            reset()
            if prec["none"] != prec["R2V3.7"]:
                r["moves"] += 1
                on = W1.cx_values(True, True, "none")  # CreateEx true on this many of the 1,024 valuations when e_c ⪯ e holds
                r["valuations_moved"] += on
                bump(r["by_n"], "n=%d" % n)
    print("createx: (n, e_c) pairs %d (n ≤ 4); e_c ⪯_h e fails under R2V3.7 on %d (e_c ≥ 2 steps before e: %s); CreateEx T → F on %d valuations (of 1,024 each)"
          % (r["pairs"], r["moves"], r["by_n"], r["valuations_moved"]))
    return dict(kind="createx", seconds=round(time.time() - t0, 1), result=r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=("cands", "crosscheck", "chains", "keys", "explu", "args", "routes", "fc80x", "createx"))
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--sizes", default="SMALL")
    ap.add_argument("--seed", type=int, default=108301)
    ap.add_argument("--valuemaps", action="store_true")
    ap.add_argument("--proper", action="store_true")
    ap.add_argument("--nmax", type=int, default=4)
    a = ap.parse_args()
    fn = dict(cands=run_cands, crosscheck=run_crosscheck, chains=run_chains, keys=run_keys, explu=run_explu, args=run_args,
              routes=run_routes, fc80x=run_fc80x, createx=run_createx)[a.kind]
    out = fn(a)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=repr)


if __name__ == "__main__":
    main()
