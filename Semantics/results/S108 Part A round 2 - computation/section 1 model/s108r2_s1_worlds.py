# S108 Part A round 2, section 1: the generated worlds at scale 4, each in-scope variant off and on (rule 5.4).
#   PYTHONHASHSEED=0 python3 -B s108r2_s1_worlds.py OUT.json [--scale 4] [--sizes SMALL|MID] [--seed 108001] [--valuemaps] [--proper]
# The program's generators (claims_a.gen_p_cand), 40 models per size times the scale, one seeded stream in ascending size
# order; the same seeds as round 1 (108001–108004), so the base counts can be checked against round 1's. Candidates built
# once, with D1.4 as after round 4 (core.S108_S1_GEN = "fixed"), judged under each state:
#   none; I5 (round 1's V1.5); R2V1.1 with ρ recorded declared, selected, constructed (one value for every generated question,
#   S108r2-1-I1); R2V1.6 (Expl := (A) ∧ Dep ∧ NonVacuous ∧ ¬Dec(t)).
# Dec(t) with t's history set by hand (claims_s41.provenance_of, Θ by hand, I90): 'Con' (a trace, cod t represented) and
# 'Sel' (a selection on H = {(1, b0)}); under the 'Dec' history Expl is F under every state.
# R2V1.10 (S108-1-I1): no generated candidate reads I1; in addition, the ℰ_bv pattern on each generated target
# [S108r2-1-I5]: for each component j of D, E := D with j's relation replaced by the solution's projection on V_j at the
# identity edit, and at a ≠ 1 by I1's reading ((i) follows: proj Sol_D(a,b); (ii) baseline: proj Sol_D(1,b); (iii) ∪_b′ proj
# Sol_D(a,b′)); Γ = {j}, λ(j) = {j}, identity translations; Acc under none and under round 1's V1.1.
# Reports per state the candidates whose Acc or Expl differs from none, of each kind, and the smallest witness of each.
import argparse
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, Org, Candidate, Translation, account  # noqa: E402
from model.claims_a import SMALL, MID, gen_p_cand  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402

core.S108_S1_GEN = "fixed"
STATES = [("I5 (round 1's V1.5)", dict(r1="V1.5")),
          ("R2V1.1 declared", dict(r2="R2V1.1", rho="declared")),
          ("R2V1.1 selected", dict(r2="R2V1.1", rho="selected")),
          ("R2V1.1 constructed", dict(r2="R2V1.1", rho="constructed")),
          ("R2V1.6", dict(r2="R2V1.6"))]


def set_state(r1="none", r2="none", rho="declared"):
    core.S108_S1 = r1
    core.OBS_READING = "R-ii"
    core.S108R2_S1 = r2
    core.S108R2_S1_RHO = rho


def judge(c):
    acc, d = account(c, detail=True)
    H = [(ONE, c.p.b0)]
    base = core.expl_base(c)
    ex = {}
    for kind in ("Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        ex[kind] = bool(base and not dec)
    conj = tuple((key, bool(d[key])) for key in ("F1", "F2", "A", "Dep", "NonVacuous") if key in d)
    return dict(acc=bool(acc), conj=conj, question=d.get("question"), expl=ex)


def bv_candidates(p):
    """The ℰ_bv pattern on a generated target [S108r2-1-I5], one per component j and I1 reading."""
    D = p.D
    out = []
    for j in D.comps:
        Vj = D.foot[j]

        def pj(a, b, Vj=Vj):
            return D.proj(D.sol(a, b), D.ports, Vj)
        for rd in ("follows", "baseline", "iii"):
            def L(k, a, b, j=j, rd=rd, pj=pj):
                if k != j:
                    return D.L(k, a, b)
                if a == ONE or rd == "baseline":
                    return pj(ONE, b)
                if rd == "follows":
                    return pj(a, b)
                return frozenset(z for b2 in D.B for z in pj(a, b2))
            E = Org("E_bv(%s)" % j, list(D.ports), dict(D.dom), list(D.comps), dict(D.foot), D.B, D.A, D._compose, L)
            c = Candidate(E, p, {v: Translation((v,)) for v in D.ports}, {a: a for a in D.A}, {b: b for b in D.B},
                          {j: (frozenset([j]), {v: Translation((v,)) for v in Vj})}, [j], p.deltaD, name="ℰ_bv(%s,%s)" % (j, rd))
            out.append((rd, c))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--sizes", default="SMALL")
    ap.add_argument("--seed", type=int, default=108001)
    ap.add_argument("--valuemaps", action="store_true")
    ap.add_argument("--proper", action="store_true")
    ap.add_argument("--no-bv", action="store_true")
    a = ap.parse_args()
    sizes = SMALL if a.sizes == "SMALL" else MID
    per = max(1, int(40 * a.scale))
    rng = random.Random(a.seed)
    t0 = time.time()
    n = 0
    summ = {s: dict(acc_moves=0, expl_moves={"Con": 0, "Sel": 0}, kinds={}, witness={}) for s, _ in STATES}
    base_acc = base_expl_con = base_expl_sel = 0
    pred = dict(A_NV_noDep=0, ADN_F1F2_both_fail=0)  # (A) ∧ NonVacuous without Dependence: out under R2V1.6 too
    bv = {rd: {"none": 0, "V1.1": 0, "in (V1.1 T, none F)": 0, "out": 0, "built": 0} for rd in ("follows", "baseline", "iii")}
    bv_w = {}
    for size in sizes:
        for i in range(per):
            m = gen_p_cand(rng, size, valuemaps=a.valuemaps, proper=a.proper)
            if m is None:
                continue
            p, c = m
            n += 1
            ckind = c.E.meta.get("family", "?")
            dfam = p.D.meta.get("family", "?")
            set_state()
            base = judge(c)
            base_acc += base["acc"]
            base_expl_con += base["expl"]["Con"]
            base_expl_sel += base["expl"]["Sel"]
            cj = dict(base["conj"])
            if cj.get("A") and cj.get("NonVacuous") and not cj.get("Dep"):
                pred["A_NV_noDep"] += 1
            if cj.get("A") and cj.get("NonVacuous") and cj.get("Dep") and not cj.get("F1") and not cj.get("F2"):
                pred["ADN_F1F2_both_fail"] += 1
            for sname, kw in STATES:
                set_state(**kw)
                e = judge(c)
                s = summ[sname]
                if e["acc"] != base["acc"]:
                    s["acc_moves"] += 1
                moved = False
                for h in ("Con", "Sel"):
                    if e["expl"][h] != base["expl"][h]:
                        s["expl_moves"][h] += 1
                        moved = True
                if moved or e["acc"] != base["acc"]:
                    direction = ("Acc in" if e["acc"] and not base["acc"] else "Acc out" if base["acc"] and not e["acc"] else
                                 "Expl in" if any(e["expl"][h] and not base["expl"][h] for h in ("Con", "Sel")) else "Expl out")
                    moved_conj = [k for (k, x) in base["conj"] if not x]
                    kind = "%s | %s | %s | failing under none: %s" % (ckind, dfam, direction, ",".join(moved_conj) or "-")
                    s["kinds"][kind] = s["kinds"].get(kind, 0) + 1
                    if kind not in s["witness"]:
                        s["witness"][kind] = dict(size=repr(size), index=i, off=dict(base, conj=dict(base["conj"])), on=dict(e, conj=dict(e["conj"])),
                                                  question=p.describe(), candidate=c.describe())
            set_state()
            if not a.no_bv:
                for rd, cb in bv_candidates(p):
                    r = {}
                    for v in ("none", "V1.1"):
                        set_state(r1=v)
                        r[v] = bool(account(cb))
                    set_state()
                    b = bv[rd]
                    b["built"] += 1
                    b["none"] += r["none"]
                    b["V1.1"] += r["V1.1"]
                    if r["V1.1"] and not r["none"]:
                        b["in (V1.1 T, none F)"] += 1
                        bv_w.setdefault(rd, dict(size=repr(size), index=i, candidate=cb.describe(), question=p.describe()))
                    if r["none"] and not r["V1.1"]:
                        b["out"] += 1
    out = dict(models=n, sizes=a.sizes, n_sizes=len(sizes), per_size=per, seed=a.seed, valuemaps=a.valuemaps, proper=a.proper,
               gen="fixed (D1.4 as after round 4 when building)", acc_true_under_none=base_acc,
               expl_true_under_none=dict(Con=base_expl_con, Sel=base_expl_sel), prediction_checks=pred, seconds=round(time.time() - t0, 1), states=summ,
               bv=bv, bv_smallest_in=bv_w)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=repr)
    print("models %d (sizes %s, %d per size, seed %d, valuemaps %s, proper %s); Acc T under none %d; Expl T under none: Con-history %d, Sel-history %d; %.1f s"
          % (n, a.sizes, per, a.seed, a.valuemaps, a.proper, base_acc, base_expl_con, base_expl_sel, out["seconds"]))
    print("(A) ∧ NonVacuous without Dependence (out under every state): %d; (A) ∧ Dep ∧ NonVacuous with (F1) and (F2) both failing: %d" % (pred["A_NV_noDep"], pred["ADN_F1F2_both_fail"]))
    for sname, _ in STATES:
        s = summ[sname]
        print("%s: Acc moves %d; Expl moves Con-history %d, Sel-history %d" % (sname, s["acc_moves"], s["expl_moves"]["Con"], s["expl_moves"]["Sel"]))
        for k, cnt in sorted(s["kinds"].items()):
            print("   %-90s %d (smallest: %s)" % (k, cnt, s["witness"][k]["size"]))
    if not a.no_bv:
        for rd, b in bv.items():
            print("ℰ_bv pattern, I1 %s: %s" % (rd, b))


if __name__ == "__main__":
    main()
