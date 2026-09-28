# S108 Part A, section 4: the generated worlds (rule 5.4), each variant off and on, at scale 4 (160 models per size of
# claims_a.SMALL, one seeded stream, sizes ascending: the first witness found is the smallest found, as the harness takes it).
#   PYTHONHASHSEED=0 python3 -B s108_s4_worlds.py PART OUT.json      PART: cands | pops | chains | toy | graph
# cands  gen_p_cand's stream (gen_org G-surg or G-free, gen_question, any_candidate: E_enc-built 60%, random 20%,
#        lookup 20%), with the kind recorded: Acc; Slot; being an explanation under the hand-set histories of
#        s108_s4_cases.py (V4.1, V4.2, V4.3); the (Suff) defeat set with an argument citing a rival's Acc (V4.4); (Nec)'s
#        exposure now and on C alone (V4.5, class S108-4-I5); Acc under each port of E as δ against the designated one (V4.6)
# pops   FC80's populations (a base candidate and three alterations; H random): Underdet and (Prov)(i) now and under V4.8
# chains every provenance chain of 1 to 3 holdings (held, trace, Sel's conditions, transfers), cuts U, K, T, T′: where
#        ¬Dec(t) and Sel ∨ CT at the holding part (V4.3)
# toy    V4.7's nearest statable reading (S108-4-I7): Enable and UU on hand-set realizations, NQB read from provenance chains
# graph  D18.1's graph (the program's DEP) under each variant: ancestors of (E), Dec, DefeatConds, 𝔈, UU, UECS, Underdet
# Standard library only; imports the package model/ of this folder; writes only OUT.json.
import itertools
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core, s108_s4, s108_s4_nec as NEC  # noqa: E402
from model.core import ONE, account, faithful, slot, SLOT_QUANTIFIERS, Org  # noqa: E402
from model.gen import gen_surg, gen_free, gen_question, gen_candidate, gen_random_candidate, gen_lookup  # noqa: E402
from model.claims_a import SMALL  # noqa: E402
from model.claims_b import (Hist, sel, con, prov_fixed_points, _prov_step, faithful_on, all_pairs, dep_edges)  # noqa: E402
from model import claims_b  # noqa: E402
from model.claims_s41 import provenance_of, suff_defeats, not_using_E  # noqa: E402
from model.args import Not, Imp, Leaf, Step, Assessor, X  # noqa: E402
import s108_s4_cases as SC  # noqa: E402

PER = int(os.environ.get("S108_S4_PER", "160"))  # 40 × scale 4
NSIZES = int(os.environ.get("S108_S4_NSIZES", "0"))  # 0: every size of SMALL (a smaller number only for timing tests)


def size_d(s):
    return dict(ports=s.nports, dom=s.dmax, comps=s.ncomps, B=s.nB, edits=s.nedits)


def gen_world(rng, size):
    fam = rng.choice(["G-surg", "G-free"])
    D = gen_surg(rng, size, "D") if fam == "G-surg" else gen_free(rng, size, "D")
    p = gen_question(rng, D)
    r = rng.random()
    if r < 0.6:
        c, kind = gen_candidate(rng, p, name="ℰ"), "E_enc-built"
    elif r < 0.8:
        c, kind = gen_random_candidate(rng, p, size, name="ℰ"), "random"
    else:
        c, kind = gen_lookup(rng, p, name="ℰ"), "lookup"
    return fam, kind, p, c


class Tally:
    def __init__(self):
        self.n, self.first = {}, {}

    def add(self, key, witness):
        self.n[key] = self.n.get(key, 0) + 1
        if key not in self.first:
            self.first[key] = witness

    def out(self):
        return [dict(key=list(k) if isinstance(k, tuple) else k, count=self.n[k], smallest=self.first[k]) for k in sorted(self.n, key=repr)]


def part_cands(seed):
    rng = random.Random(seed)
    t0 = time.time()
    n = accT = 0
    expl_moves = Tally()      # (variant, history, kind, family, direction)
    v44 = Tally()             # (kind, family, which) the (Suff) or (Nec) defeat set grows
    v45 = Tally()             # (kind, family, Acc) exposure moves
    v45_stops = 0
    v46 = Tally()
    v46_gen_not_desig = 0
    slot_q = Tally()
    exp_tot = {"now": 0, "V4.5": 0}
    for si, size in enumerate(SMALL[:NSIZES] if NSIZES else SMALL):
        print("size %d %r: %.0f s" % (si, size, time.time() - t0), file=sys.stderr, flush=True)
        for i in range(PER):
            fam, kind, p, c = gen_world(rng, size)
            n += 1
            acc = account(c)
            wit = dict(size=size_d(size), index=i, family=fam, kind=kind, question=p.describe(), candidate=c.describe()[:3000])
            sr = SC.slot_row(c)
            s_every = bool(sr and sr["every"])
            if acc:
                accT += 1
                for q in SLOT_QUANTIFIERS:
                    if sr and sr[q]:
                        slot_q.add((q, kind, fam), wit)
            # being an explanation (V4.1, V4.2, V4.3)
            for h in SC.HISTS:
                s, k, dec, sa, sb = SC.prov(c, h)
                ex = SC.expl_all(acc, dec, s_every, sa, sb)
                for v in SC.VREADS[1:]:
                    if ex[v] != ex["none"]:
                        expl_moves.add((v, h, kind, fam, "in" if ex[v] else "out"), wit)
            # V4.4: [Acc(ℰ′), Acc(ℰ′) → ¬Expl(ℰ)] and, for (Nec), [Acc(ℰ′), Acc(ℰ′) → Expl(ℰ)]
            e = "Expl_" + c.name
            ao = "Acc_ℰ′"
            g = Step("MP", Not(e), [Leaf(ao), Leaf(Imp(ao, Not(e)))])
            xg = X(Assessor(["MP"], [ao, Imp(ao, Not(e))]), e, [g])
            gn = Step("MP", e, [Leaf(ao), Leaf(Imp(ao, e))])
            xn = X(Assessor(["MP"], [ao, Imp(ao, e)]), Not(e), [gn])
            for h in ("Con", "Sel", "Dec"):
                s, k, dec = provenance_of(c, h, [(ONE, p.b0)])
                d = {rd: suff_defeats(acc, dec, bool([a for a in xg if not_using_E(a, c.name, rd)]), "L536") for rd in ("symbol", "instance")}
                if d["symbol"] != d["instance"]:
                    v44.add(("(Suff)", h, kind, fam), wit)
            nn = {rd: bool([a for a in xn if not_using_E(a, c.name, rd)]) for rd in ("symbol", "instance")}
            # V4.5: exposure; t faithful on C is a witness against both
            if faithful(c):
                en, e5 = False, False
            else:
                en, _, st1 = NEC.exposed_none(p.D, c.E, list(c.Gamma), time_cap=20)
                e5, w5, st2 = NEC.exposed_v45(p.D, c.E, list(c.Gamma), p.C, time_cap=20)
                if st1 or st2:
                    v45_stops += 1
                    en = e5 = None
            if en:
                exp_tot["now"] += 1
            if e5:
                exp_tot["V4.5"] += 1
            if en is not None and en != e5:
                v45.add(("exposed now %s → on C alone %s" % (en, e5), kind, fam, "Acc %s" % acc), wit)
            # with V4.4 too: (Nec) defeated by the rival-citing argument
            if e5 and not en and nn["instance"] and not nn["symbol"]:
                v44.add(("(Nec), with V4.5", "-", kind, fam), wit)
            # V4.6: designation
            if getattr(p.Q, "kind", None) == "port":
                desig = [v for v in c.E.ports if tuple(c.pi[v].dports) == (p.deltaD,)]
                if c.deltaE not in desig:
                    v46_gen_not_desig += 1
                a_des = any(account(c.replace(deltaE=v)) for v in desig)
                a_any = any(account(c.replace(deltaE=v)) for v in c.E.ports)
                if a_any and not a_des:
                    v46.add(("(E) met with some δ, not with the designated one", kind, fam, "designated ports %d" % len(desig)), wit)
                others = [v for v in c.E.ports if v not in desig and account(c.replace(deltaE=v))]
                if a_des and others:
                    v46.add(("(E) met with the designated δ and also with another", kind, fam, "-"), wit)
    return dict(seed=seed, models=n, acc_true=accT, seconds=round(time.time() - t0, 1),
                expl_moves=expl_moves.out(), slot_among_acc=slot_q.out(), v44=v44.out(), v45=v45.out(), v45_time_cap_stops=v45_stops, exposed_totals=exp_tot,
                v46=v46.out(), v46_generator_delta_not_designated=v46_gen_not_desig)


def part_pops(seed, wide=False):
    """FC80's generator; Sel(t) on H by hand (H occurred, admitted, no Rep, no trace: sel computes Faithful_H and H ≠ ∅).
    wide: the base's τ random half the time (as FC80 (d)'s gen_step) and each member altered at one or two pairs."""
    rng = random.Random(seed)
    t0 = time.time()
    n = 0
    ud = Tally()
    prov = Tally()
    models_moved = [0]

    def value(c, a, b):
        return (c.tau[a], c.sigma[b], tuple(c.E.L(k, c.tau[a], c.sigma[b]) for k in c.E.comps))

    for size in SMALL:
        for i in range(PER):
            fam = rng.choice(["G-surg", "G-free"])
            D = gen_surg(rng, size, "D") if fam == "G-surg" else gen_free(rng, size, "D")
            p = gen_question(rng, D)
            if len(p.C) < 2:
                continue
            base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=(rng.choice([0.0, 0.5]) if wide else 0.0), demote_p=0.0)
            if not base.E.comps:
                continue
            pop = [base]
            for j in range(3):
                E = base.E
                alts = []
                for r in range(rng.choice([1, 2]) if wide else 1):
                    k = rng.choice(list(E.comps))
                    x = rng.choice(all_pairs(D))
                    w = rng.choice(sorted(E.full(k))) if E.full(k) else None
                    if w is not None:
                        alts.append((k, x, w))
                if not alts:
                    continue
                E2 = Org("E_%d" % j, E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                         (lambda al: (lambda jj, a, b: E.L(jj, a, b) ^ frozenset(w_ for (k_, x_, w_) in al if (jj, a, b) == (k_, x_[0], x_[1]))))(alts))
                pop.append(base.replace(E=E2, name="t%d" % j))
            H = [x for x in p.C if rng.random() < 0.5] or [(ONE, p.b0)]
            n += 1
            moved_before = sum(prov.n.values())
            wit = dict(size=size_d(size), index=i, family=fam, question=p.describe(), H=sorted(map(list, H)))
            surv = [c for c in pop if faithful_on(c, H)]
            h = Hist(["o1"], [], set(p.C), admitted=True, prepares=False)
            for (a, b) in sorted(p.C, key=repr):
                if (a, b) in H or not all(c.translates(a, b) for c in pop):
                    continue
                vals_s = set(value(c, a, b) for c in surv)
                vals_all = set(value(c, a, b) for c in pop)
                for t in surv:
                    vt = value(t, a, b)
                    now = any(value(u, a, b) != vt for u in surv)
                    v48 = any(value(u, a, b) != vt for u in pop)
                    if now != v48:
                        ud.add(("Underdet(t;a,b) now %s, under V4.8 %s" % (now, v48), fam), dict(wit, pair=[a, b], t=t.name))
                    func = len(vals_s) == 1
                    s_ok = sel(t, H, h)
                    pn, p48 = s_ok and now and func, s_ok and v48 and func
                    if pn != p48:
                        prov.add(("(Prov)(i) now %s, under V4.8 %s" % (pn, p48), fam), dict(wit, pair=[a, b], t=t.name, members=len(pop), survivors=len(surv)))
                    if pn:
                        prov.add(("(Prov)(i) now True (against FC80 (a))", fam), dict(wit, pair=[a, b]))
            if sum(prov.n.values()) > moved_before:
                models_moved[0] += 1
    return dict(seed=seed, models=n, models_with_a_prov_i_move=models_moved[0], seconds=round(time.time() - t0, 1), underdet=ud.out(), prov_i=prov.out())


def part_chains():
    """Every chain of n = 1..3 holdings: held, trace, Sel's conditions per holding, each holding a transfer of an earlier one
    or not; cuts U, K, T, T′; every fixed point. V4.3 (a): Sel ∨ CT at the holding, CT := trace there; (b): CT := a trace at
    the holding or at one it was transferred from."""
    t0 = time.time()
    tal = Tally()
    n = holdings = 0
    for nh in (1, 2, 3):
        recs = list(itertools.product(*[[None] + list(range(o)) for o in range(nh)]))
        for held, trace, selc in itertools.product(itertools.product((0, 1), repeat=nh), repeat=3):
            for rec in recs:
                for rd in ("U", "K", "T", "T'"):
                    fps = prov_fixed_points(nh, list(held), list(trace), list(selc), rd, True, rec_of=list(rec))
                    for R, sc in fps:
                        n += 1
                        direct = _prov_step(nh, list(held), list(trace), list(selc), rd, True, R)
                        for o in range(nh):
                            holdings += 1
                            dec = not sc[o][0] and not sc[o][1]
                            anc, x = [o], o
                            while rec[x] is not None:
                                x = rec[x]
                                anc.append(x)
                            sa = direct[o][0] or bool(trace[o])
                            sb = direct[o][0] or any(trace[y] for y in anc)
                            src = "transfer of a %s holding" % ("Sel" if sc[anc[-1]][0] else "Con" if sc[anc[-1]][1] else "Dec") if rec[o] is not None else "no transfer"
                            if (not dec) and not sa:
                                tal.add(("V4.3a", rd, src), dict(n=nh, held=held, trace=trace, selc=selc, rec_of=rec, holding=o, fixed_point=sorted(R)))
                            if (not dec) and not sb:
                                tal.add(("V4.3b", rd, src), dict(n=nh, held=held, trace=trace, selc=selc, rec_of=rec, holding=o, fixed_point=sorted(R)))
                            if (not dec) and rec[o] is None and not (sc[o][0] or sc[o][1]):
                                tal.add(("check: ¬Dec with no Sel, no Con at a holding not transferred", rd, src), {})
    return dict(fixed_points=n, holdings=holdings, seconds=round(time.time() - t0, 1), moves=tal.out())


def part_toy():
    """V4.7's nearest statable reading [S108-4-I7]. The program has no Can, χ or realization. Here: a content c and two
    enabling conditions χ1, χ2, each admitted or not, each with 0-2 witnessing realizations; a realization uses one of
    three occurrences inside β: o_own (a holding of c built inside β: a chain whose first holding is inside), o_relay (a
    holding of c transferred from a holding o_out outside β), o_none (no holding of c). Rep(o, c) and the provenance at
    o are computed by prov_fixed_points (T′) on the chain; 'relayed from outside β' := the holding is a transfer of a
    holding outside β and represents c. NQB(χ) := no witnessing realization uses such an occurrence (D16.3, I154).
    Enable now := admitted ∧ NQB ∧ Can (a witnessing realization: (CT1)'s sense read as 'has one', a declared input);
    V4.7 := admitted ∧ Can. UU(c) := ∃χ Enable(χ) ∧ Can(χ). Every assignment enumerated."""
    t0 = time.time()
    # representation of c at each occurrence, from chains (held and a construction or selection at the first holding)
    reps = {}
    for nm, (held, trace, selc, rec) in {"o_own": ([1], [1], [0], [None]),
                                         "o_relay": ([1, 1], [1, 0], [0, 0], [None, 0]),
                                         "o_relay_sel": ([1, 1], [0, 0], [1, 0], [None, 0]),
                                         "o_none": ([0], [0], [0], [None])}.items():
        fps = prov_fixed_points(len(held), held, trace, selc, "T'", True, rec_of=rec)
        R, sc = fps[0]
        o = len(held) - 1
        reps[nm] = (o in R, rec[o] is not None)
    occ = sorted(reps)
    relayed = {o: reps[o][0] and reps[o][1] for o in occ}
    realizations = [()] + [(o,) for o in occ] + list(itertools.combinations(occ, 2))
    n = moves = 0
    first = None
    both = {"now": 0, "V4.7": 0}
    first_both = None
    for adm in itertools.product((0, 1), repeat=2):
        for r1 in realizations:
            for r2 in realizations:
                n += 1
                uu = {}
                # L495.s1 (FROZEN): c's domain is a barrier when every admitted, non-question-begging enabling condition
                # leaves the capability unavailable: no χ admitted ∧ NQB ∧ Can (read with NQB as the frozen words have it)
                barrier = not any(a and bool(rs) and not any(relayed[o] for o in rs) for a, rs in zip(adm, (r1, r2)))
                for rdg in ("now", "V4.7"):
                    ok = False
                    for a, rs in zip(adm, (r1, r2)):
                        can = bool(rs)
                        nqb = not any(relayed[o] for o in rs)
                        en = a and can and (nqb or rdg == "V4.7")
                        ok = ok or (en and can)
                    uu[rdg] = ok
                    if barrier and ok:
                        both[rdg] += 1
                        if rdg == "V4.7" and first_both is None:
                            first_both = dict(admitted=adm, realizations=[r1, r2])
                if uu["now"] != uu["V4.7"]:
                    moves += 1
                    if first is None:
                        first = dict(admitted=adm, realizations=[r1, r2])
    return dict(occurrences={o: dict(represents_c=reps[o][0], transferred=reps[o][1], relayed_from_outside=relayed[o]) for o in occ},
                assignments=n, uu_moves=moves, first=first, barrier_and_UU=both, first_barrier_and_UU_under_V47=first_both,
                seconds=round(time.time() - t0, 1))


def part_graph():
    import importlib
    from model import claims_r3a3
    out = {}
    base = None
    for v in s108_s4.VARIANTS:
        s108_s4.VARIANT = v
        dep = s108_s4.dep_patch(claims_b.DEP)
        res = {}
        for node in ("(E)", "Dec", "DefeatConds", "𝔈", "Enable", "UU", "UECS", "Classes", "Underdet"):
            res[node] = sorted(claims_r3a3.dep_ancestors(dep, node))
        reach = {x: sorted(n for n in dep if x in claims_r3a3.dep_ancestors(dep, n)) for x in ("Slot", "Enable", "Underdet", "surv", "CT", "Dec", "ℓ")}
        out[v] = dict(ancestors=res, reached_by=reach)
    s108_s4.VARIANT = "none"
    return out


def main():
    part, outp = sys.argv[1], sys.argv[2]
    if part == "cands":
        res = part_cands(108401)
    elif part == "pops":
        res = part_pops(108402)
    elif part == "pops-wide":
        res = part_pops(108403, wide=True)
    elif part == "chains":
        res = part_chains()
    elif part == "toy":
        res = part_toy()
    elif part == "graph":
        res = part_graph()
    else:
        sys.exit("part?")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, default=repr)
    print(json.dumps({k: v for k, v in res.items() if not isinstance(v, (list, dict))} if isinstance(res, dict) else {}, ensure_ascii=False))


if __name__ == "__main__":
    main()
