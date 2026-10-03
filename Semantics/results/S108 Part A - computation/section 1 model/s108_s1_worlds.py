# S108 Part A, section 1: the generated worlds at scale 4, each section-1 variant off and on (rule 5.4).
#   PYTHONHASHSEED=0 python3 -B s108_s1_worlds.py OUT.json [--scale 4] [--sizes SMALL|MID] [--seed 108001]
# The program's generators (claims_a.gen_p_cand: gen.gen_org, gen.gen_question, gen.any_candidate), over the sizes
# claims_a.SMALL, 40 models per size times the scale, one seeded stream in ascending size order. Candidates are built once,
# with D1.4 read as after round 4 (core.S108_S1_GEN = "fixed"), and judged under 'none' and under every variant, so the
# same candidate is compared. For each: Acc(ℰ) with conjuncts; Dec(t) and Account ∧ ¬Dec(t) with t's history set by hand
# as a selection on H = {(1, b0)} (claims_s41.provenance_of 'Sel', Θ by hand, I90); and, of (D, C, Q) alone, Set_v, asg,
# the families on C (D4.6, under core.OBS_READING), Prod(p) (D3.3) and Ident's contract clause read on the designated
# port (D3.3; the generated queries read a port, so Ident itself, which asks a fibre, holds under no reading).
# Reports, per variant: the candidates whose Acc or Account ∧ ¬Dec(t) differs from 'none', how many of each kind
# (candidate generator × target family × direction), the conjunct that moved, and the smallest witness of each kind
# (the first found in ascending size order); and how many (D, C, Q) the other items move on. Writes only OUT.json.
import argparse
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, BOT, account, Roles, ident_contract  # noqa: E402
from model.claims_a import SMALL, MID, gen_p_cand  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402

core.S108_S1_GEN = "fixed"
VARIANTS = [v for v in core.S108_S1_VARIANTS if v != "none"]
PSEUDO = "V1.5 (ρ_p constructed by hand)"


def set_variant(v):
    core.S108_S1 = v
    core.OBS_READING = "R-i" if v == "V1.3" else "R-ii"


def prod(p, R):
    if getattr(p.Q, "kind", None) != "port":
        return False
    w, D = p.deltaD, p.D
    if not any(R.output(w, j) for j in D.comps):
        return False
    return any(a in R.Set[v] and R.upstream(v, w) for (a, b) in p.C for v in D.ports)


def judge(c):
    acc, d = account(c, detail=True)
    s, k, dec = provenance_of(c, "Sel", [(ONE, c.p.b0)])
    conj = tuple((key, bool(d[key])) for key in ("F1", "F2", "A", "Dep", "NonVacuous") if key in d) + ((("question", False),) if d.get("question") is False else ())
    return dict(acc=bool(acc), conj=conj, dec=bool(dec), expl=bool(acc and not dec))


def of_question(p):
    D = p.D
    R = Roles(D)
    w = p.deltaD

    def obs(a, b):
        vals = set(z[D.ports.index(w)] for z in D.sol(a, b))
        return next(iter(vals)) if len(vals) == 1 else BOT
    return dict(Set=tuple(sorted((v, tuple(sorted(R.Set[v]))) for v in D.ports)), asg=tuple(sorted(R.asg.items())),
                Input=tuple(sorted(v for v in D.ports if R.input(v))), Slc=tuple(sorted((j, tuple(sorted(R.slc[j]))) for j in D.comps)),
                Obs_R_ii=tuple(sorted(R.obs("R-ii"))),
                families=repr(R.families(p.C, core.OBS_READING)), prod=prod(p, R), ident_clause=ident_contract(obs, p.C, p.b0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=4.0)
    ap.add_argument("--sizes", default="SMALL")
    ap.add_argument("--seed", type=int, default=108001)
    ap.add_argument("--valuemaps", action="store_true")
    ap.add_argument("--proper", action="store_true")
    a = ap.parse_args()
    sizes = SMALL if a.sizes == "SMALL" else MID
    per = max(1, int(40 * a.scale))
    rng = random.Random(a.seed)
    t0 = time.time()
    n = 0
    names = VARIANTS + [PSEUDO]
    summ = {v: dict(acc_moves=0, expl_moves=0, dec_moves=0, kinds={}, conj_moved={}, witness={}, other={}) for v in names}
    base_acc_true = 0
    for size in sizes:
        for i in range(per):
            m = gen_p_cand(rng, size, valuemaps=a.valuemaps, proper=a.proper)
            if m is None:
                continue
            p, c = m
            n += 1
            ckind = c.E.meta.get("family", "?")
            dfam = p.D.meta.get("family", "?")
            set_variant("none")
            base = judge(c)
            base_acc_true += base["acc"]
            baseq = of_question(p)
            for v in names:
                if v == PSEUDO:
                    set_variant("V1.5")
                    p.rho = "constructed"
                    e = judge(c)
                    q = of_question(p)
                    p.rho = None
                else:
                    set_variant(v)
                    e = judge(c)
                    q = of_question(p)
                s = summ[v]
                if v == "V1.1":
                    # D4.4 (FROZEN) for N = {j}: sig_C({j}) = sig_C(j) at every pair of C? (I14: always; V1.1: where siblings constrain, no)
                    D = p.D
                    d44 = any(D.proj(D.sol_sub([j], a_, b_)[1], D.sol_sub([j], a_, b_)[0], D.foot[j]) != D.L(j, a_, b_)
                              for j in D.comps for (a_, b_) in p.C)
                    if d44:
                        s["other"]["D4.4: sig({j}) ≠ sig(j) somewhere on C"] = s["other"].get("D4.4: sig({j}) ≠ sig(j) somewhere on C", 0) + 1
                if v == "V1.2":
                    # L103.s2 (FROZEN): the new setting edits (in Set_v under V1.2, not under 'none'), and those at which Sol_D is empty at some b
                    D = p.D
                    set_variant("V1.2")
                    R2 = Roles(D)
                    set_variant("none")
                    R0 = Roles(D)
                    set_variant("V1.2")
                    new_ = set((v_, a_) for v_ in D.ports for a_ in R2.Set[v_] - R0.Set[v_])
                    if new_:
                        s["other"]["V1.2: new setting edits (targets with any)"] = s["other"].get("V1.2: new setting edits (targets with any)", 0) + 1
                        s["other"]["V1.2: new (port, setting edit) pairs"] = s["other"].get("V1.2: new (port, setting edit) pairs", 0) + len(new_)
                        emp = sum(1 for (v_, a_) in new_ if any(not D.sol(a_, b_) for b_ in D.B))
                        s["other"]["V1.2: of them, Sol_D empty at some b"] = s["other"].get("V1.2: of them, Sol_D empty at some b", 0) + emp
                        old_emp = sum(1 for v_ in D.ports for a_ in R0.Set[v_] if any(not D.sol(a_, b_) for b_ in D.B))
                        s["other"]["V1.2: (same targets) old (port, setting edit) pairs"] = s["other"].get("V1.2: (same targets) old (port, setting edit) pairs", 0) + sum(len(R0.Set[v_]) for v_ in D.ports)
                        s["other"]["V1.2: (same targets) old ones with Sol_D empty at some b"] = s["other"].get("V1.2: (same targets) old ones with Sol_D empty at some b", 0) + old_emp
                if v == "V1.8":
                    # L347.s2 (FROZEN): a rule family anywhere (rule(j) on C for some j), under 'none' and under V1.8
                    D = p.D
                    set_variant("none")
                    r0 = any(Roles(D).rule(j, p.C) for j in D.comps)
                    m0 = any(Roles(D).meas(j, m_, p.C, "R-ii") for j in D.comps for m_ in D.foot[j])
                    set_variant("V1.8")
                    r8 = any(Roles(D).rule(j, p.C) for j in D.comps)
                    m8 = any(Roles(D).meas(j, m_, p.C, "R-ii") for j in D.comps for m_ in D.foot[j])
                    set_variant("none")
                    o0 = bool(Roles(D).obs("R-ii"))
                    set_variant("V1.8")
                    o8 = bool(Roles(D).obs("R-ii"))
                    for key, val in (("Obs (R-ii) nonempty under none", o0), ("Obs (R-ii) nonempty under V1.8", o8),
                                     ("rule family nonempty under none", r0), ("rule family nonempty under V1.8", r8),
                                     ("measurement family nonempty under none (R-ii)", m0), ("measurement family nonempty under V1.8 (R-ii)", m8)):
                        if val:
                            s["other"][key] = s["other"].get(key, 0) + 1
                for key in baseq:
                    if q[key] != baseq[key]:
                        s["other"][key] = s["other"].get(key, 0) + 1
                if e["dec"] != base["dec"]:
                    s["dec_moves"] += 1
                if e["acc"] != base["acc"] or e["expl"] != base["expl"]:
                    if e["acc"] != base["acc"]:
                        s["acc_moves"] += 1
                    if e["expl"] != base["expl"]:
                        s["expl_moves"] += 1
                    direction = "in" if e["acc"] and not base["acc"] else ("out" if base["acc"] and not e["acc"] else "expl only")
                    kind = "%s | %s | %s" % (ckind, dfam, direction)
                    s["kinds"][kind] = s["kinds"].get(kind, 0) + 1
                    moved = ",".join(k for (k, x), (_, y) in zip(base["conj"], e["conj"]) if x != y) or ("question" if dict(e["conj"]).get("question") is False else "-")
                    s["conj_moved"][moved] = s["conj_moved"].get(moved, 0) + 1
                    if kind not in s["witness"]:
                        s["witness"][kind] = dict(size=repr(size), index=i, off=dict(base, conj=dict(base["conj"])), on=dict(e, conj=dict(e["conj"])),
                                                  question=p.describe(), candidate=c.describe(), target=p.D.describe(pairs=sorted(p.C, key=repr)))
            set_variant("none")
    out = dict(models=n, sizes=a.sizes, n_sizes=len(sizes), per_size=per, seed=a.seed, valuemaps=a.valuemaps, proper=a.proper, gen="fixed (D1.4 as after round 4 when building)",
               acc_true_under_none=base_acc_true, seconds=round(time.time() - t0, 1), variants=summ)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("models %d (sizes %s, %d per size, seed %d, valuemaps %s, proper %s); Acc true under none: %d; %.1f s" % (n, a.sizes, per, a.seed, a.valuemaps, a.proper, base_acc_true, out["seconds"]))
    for v in names:
        s = summ[v]
        print("%s: Acc moves %d; Account ∧ ¬Dec(t) moves %d; Dec(t) moves %d; conjuncts %s; other %s" % (v, s["acc_moves"], s["expl_moves"], s["dec_moves"], s["conj_moved"], s["other"]))
        for k, cnt in sorted(s["kinds"].items()):
            print("   %-40s %d (smallest: %s)" % (k, cnt, s["witness"][k]["size"]))


if __name__ == "__main__":
    main()
