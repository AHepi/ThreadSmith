# S108 Part A round 2, section 2 (the computing agent, rule 5.4): the generated worlds at scale 4, each in-scope variant of
# round 2's reply off and on, on round 1's populations and seeds (s108_s2_gen.py: single, single-valuemaps, single-MID-proper
# over the program's own generators; pairs; claims), so that counts compare with round 1's. For each setting: the candidates
# whose Acc, or whose Account ∧ ¬Dec(t) under the four histories set by hand (P-S2-3), differs from off; how many of each kind;
# the smallest witness of each kind (sizes ascend). Also: C6, C11 per quantifier (R2V2.2); C7 on one-holding chains (R2V2.3);
# D6.9's coverage (R2V2.5); the student-copy shape under R2V2.6; the two extents of violation at pairs of H (R2V2.10);
# FC21.v1 / FC21.v2's separating candidates (R2V2.11); {1}×B contracts under V2.3 and V1.4 (e2.07); the argument from ConfCl
# on round 1's claims population and ConfG_χ on its pairs (e2.19, e2.33).
# Run from "results/S108 Part A round 2 - computation/section 2 model":
#   PYTHONHASHSEED=0 python3 -B s108r2_s2_gen.py [--scale 4] [--pop single|single-valuemaps|single-MID-proper|pairs|claims] [--json FILE]
# Standard library only; imports this copy's model/ and round 1's s108_s2_gen.py (its populations); writes only the --json file.
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, BOT, account, slot, faithful, NC2, routes, conf_claim, conf_given, meet_table, all_pairs, relabeling, F1_at, F2eq_at, A_at, SLOT_QUANTIFIERS  # noqa: E402
from model.claims_b import CONF, gen_pair, small_enough, rand_allow, Hist, sel, prov_fixed_points, faithful_on  # noqa: E402
from model.claims_a import D_and_p  # noqa: E402
from model.claims_r3a1 import obs_value  # noqa: E402
from model.gen import any_candidate  # noqa: E402
from model.claims_s108r2 import block_carries_contrast  # noqa: E402
import s108_s2_gen as R1G  # noqa: E402
import s108r2_s2_cases as RC  # noqa: E402  (SETTINGS, setting, expl_row, alpha_from_confcl)

ACC_SETTINGS = ["R2V2.5", "R2V2.8 target", "R2V2.8 program", "R2V2.8 widest", "R2V2.9", "R2V2.10", "q some", "q some-exempt",
                "q some-exempt-set", "V2.4 q every", "V2.4 q some", "V2.4 q some-exempt", "V2.4 q some-exempt-set"]
EXPL_SETTINGS = ["R2V2.3a", "R2V2.6 written", "R2V2.6 HS", "R2V2.6 reply", "V2.5 (C7)", "V2.5 (C7) × R2V2.3a"]


def conj(d):
    return RC.conj(d)


def bump(tab, key, size, desc):
    e = tab.setdefault(key, [0, None, None])
    e[0] += 1
    if e[1] is None:
        e[1], e[2] = repr(size), desc


def pop_single(scale, name):
    sizes_, gen, per_size, seed = R1G.SINGLE[name]
    rng = random.Random(seed)
    per = max(1, int(per_size * scale))
    t0 = time.time()
    n = 0
    acc_true = {s: 0 for s in ["off"] + ACC_SETTINGS}
    acc_diff = {s: {} for s in ACC_SETTINGS}
    expl_diff = {s: {} for s in EXPL_SETTINGS}
    c6 = {q: 0 for q in SLOT_QUANTIFIERS}
    c11 = {q: 0 for q in SLOT_QUANTIFIERS}
    c6_eq_c11 = {q: 0 for q in SLOT_QUANTIFIERS}
    extra = dict(r25_relabel_contracts=0, r25_relabel_contracts_bot=0, r210_pairs_differ=0, r210_H_pairs_differ=0,
                 v21_accounts_no_block=0, l307_pattern_off=0, l307_pattern_v22=0, ones_contracts=0, ones_ident_i163=0,
                 ones_ident_v14=0, ones_acc_off=0, ones_acc_v23=0, student_shape_dec_off=0, student_shape_sel_reply=0,
                 chain_one_holding_eq_handset=0, chain_one_holding_neq=0)
    wit = {}
    for size in sizes_:
        for i in range(per):
            m = gen(rng, size)
            if m is None:
                continue
            p, c = m
            n += 1
            desc = "%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe())
            res = {}
            with RC.setting():
                v, d = account(c, detail=True)
                res["off"] = (bool(v), d)
                slots = {q: any(slot(c, k, quantifier=q) for k in c.E.comps) for q in SLOT_QUANTIFIERS}
                e_off = RC.expl_row(c)
            acc_true["off"] += res["off"][0]
            for s in ACC_SETTINGS:
                with RC.setting(**RC.SETTINGS[s]):
                    v, d = account(c, detail=True)
                res[s] = (bool(v), d)
                acc_true[s] += bool(v)
                if res[s][0] != res["off"][0]:
                    bump(acc_diff[s], "Acc %s->%s; %s; conjuncts off [%s] on [%s]" % (
                        RC.tf(res["off"][0]), RC.tf(res[s][0]), R1G.kind_of(c), conj(res["off"][1]), conj(res[s][1])), size, desc)
            for q in SLOT_QUANTIFIERS:
                a6 = res["V2.4 q " + q][0]
                a11 = res["off"][0] and not slots[q]
                c6[q] += a6
                c11[q] += a11
                c6_eq_c11[q] += (a6 == a11)
            for s in EXPL_SETTINGS:
                with RC.setting(**RC.SETTINGS[s]):
                    e_on = RC.expl_row(c)
                for h in RC.HISTORIES:
                    if e_on[h] != e_off[h]:
                        bump(expl_diff[s], "Account ∧ ¬Dec(t) %s->%s; history '%s'; %s" % (RC.tf(e_off[h]), RC.tf(e_on[h]), h, R1G.kind_of(c)), size, desc)
            acc0 = res["off"][0]
            # R2V2.5: is C a contract of relabelings (every edit of C), under ⊥ = ⊥ and under '≠ ⊥'?
            edits = set(a for (a, b) in p.C if a != ONE)
            if edits:
                with RC.setting():
                    rl = all(relabeling(p, a) for a in edits)
                with RC.setting(**RC.SETTINGS["R2V2.5"]):
                    rl5 = all(relabeling(p, a) for a in edits)
                extra["r25_relabel_contracts"] += rl
                extra["r25_relabel_contracts_bot"] += (rl and not rl5)
            # R2V2.10: the two extents of violation, at every pair of C (translated), and at H = {(1,b0)} for a selected t
            for (a, b) in p.C:
                if c.translates(a, b):
                    nar = not (F1_at(c, a, b) and F2eq_at(c, a, b))
                    wid = nar or not A_at(c, a, b)
                    extra["r210_pairs_differ"] += (nar != wid)
            with RC.setting():
                x = (ONE, p.b0)
                if c.translates(*x) and sel(c, [x], Hist(["o1"], [], {x})):
                    nar = not (F1_at(c, *x) and F2eq_at(c, *x))
                    wid = nar or not A_at(c, *x)
                    if nar != wid:
                        extra["r210_H_pairs_differ"] += 1
                        wit.setdefault("R2V2.10: Sel on H = {(1,b0)}, Viol⁺ and not Viol at (1,b0)", (repr(size), desc))
            # R2V2.11: V2.1's accounts with no block carrying a contrast; L307's S realized, off and under V2.2
            with RC.setting(S2_VARIANT="V2.1"):
                if account(c) and not block_carries_contrast(c):
                    extra["v21_accounts_no_block"] += 1
            if len(c.Gamma) == 2:
                a_, b_ = c.Gamma
                L307 = frozenset([frozenset([a_]), frozenset([b_]), frozenset([a_, b_])])
                with RC.setting():
                    extra["l307_pattern_off"] += (acc0 and routes(c) == L307)
                with RC.setting(S2_VARIANT="V2.2"):
                    extra["l307_pattern_v22"] += (bool(account(c)) and routes(c) == L307)
            # e2.07: contracts {1}×B′ (every edit of C is 1): Ident's contract clause (I163 / V1.4) and accounts off / V2.3
            if all(a == ONE for (a, b) in p.C) and len(p.C) > 1:
                extra["ones_contracts"] += 1
                ob = {x: obs_value(p.D, p.deltaD, *x) for x in p.C}
                extra["ones_ident_i163"] += len(set(ob.values())) > 1
                extra["ones_ident_v14"] += any(a != ONE and ob[(a, b)] != ob[(ONE, p.b0)] for (a, b) in ob)
                extra["ones_acc_off"] += acc0
                with RC.setting(S2_VARIANT="V2.3"):
                    extra["ones_acc_v23"] += bool(account(c))
            # R2V2.3a: the hand-set histories against the one-holding chains, on Account ∧ ¬Dec(t)
            with RC.setting(**RC.SETTINGS["R2V2.3a"]):
                e_ch = RC.expl_row(c)
            same = all(e_ch[h] == e_off[h] for h in RC.HISTORIES)
            extra["chain_one_holding_eq_handset"] += same
            extra["chain_one_holding_neq"] += (not same)
            # R2V2.6: the student-copy shape (a source holding cod t before, no trace at the copy, H = {(1,b0)} tried)
            if acc0:
                x = (ONE, p.b0)
                with RC.setting():
                    selc = bool(c.translates(*x) and faithful_on(c, [x]))
                    fps = prov_fixed_points(2, [1, 1 if faithful(c) else 0], [1, 0], [0, 1 if selc else 0], "T'", True)
                    extra["student_shape_dec_off"] += all(not sc[1][0] and not sc[1][1] for R, sc in fps)
                with RC.setting(**RC.SETTINGS["R2V2.6 reply"]):
                    fps = prov_fixed_points(2, [1, 1 if faithful(c) else 0], [1, 0], [0, 1 if selc else 0], "T'", True)
                    extra["student_shape_sel_reply"] += all(sc[1][0] for R, sc in fps)
    return dict(population=name, drawn=n, per_size=per, sizes=len(sizes_), seconds=round(time.time() - t0, 1), acc_true=acc_true,
                acc_diff=acc_diff, expl_diff=expl_diff, c6=c6, c11=c11, c6_eq_c11=c6_eq_c11, extra=extra, witnesses=wit)


def pop_pairs(scale, per_size=20, seed=1082200):
    """D8.6 ConfG_χ does not read D8.5: on round 1's pairs population, ConfG_χ with a random χ, off and under V2.7."""
    rng = random.Random(seed)
    rng_chi = random.Random(seed + 7)  # χ drawn apart, so that the pairs drawn are round 1's
    per = max(1, int(per_size * scale))
    t0 = time.time()
    n = npairs = moved = conf_g = 0
    for size in CONF:
        for i in range(per):
            m = gen_pair(rng, size)
            if m is None:
                continue
            p, c1, c2 = m
            allow, _ = rand_allow(rng_chi, p.D)
            n += 1
            for (a, b) in all_pairs(p.D):
                if not (c1.translates(a, b) and c2.translates(a, b)):
                    continue
                npairs += 1
                with RC.setting():
                    g0 = conf_given(c1, c2, a, b, allow)
                with RC.setting(S2_VARIANT="V2.7"):
                    g1 = conf_given(c1, c2, a, b, allow)
                conf_g += g0
                moved += (g0 != g1)
    return dict(population="pairs", drawn=n, translated_pairs=npairs, confg_true_off=conf_g, confg_moved_v27=moved, seconds=round(time.time() - t0, 1))


def pop_claims(scale, per_size=10, seed=1082300):
    """Round 1's claims population (FC52's generator): the (candidate, pair) with Acc T whose ConfCl V2.7 removes; the argument α
    from ConfCl (e2.19's encoding) off and under V2.7; Out_j('Acc(ℰ)') by it: the route to 'solved with no test' (D10.6)."""
    rng = random.Random(seed)
    per = max(1, int(per_size * scale))
    t0 = time.time()
    n = lost = lost_acc = lost_acc_inC = out_off = out_on = 0
    wit = None
    for size in CONF:
        for i in range(per):
            D, p = D_and_p(rng, size)
            if D is None or not small_enough(D, 1024):
                continue
            c = any_candidate(rng, p, size)
            allow, _ = rand_allow(rng, D)
            n += 1
            acc = bool(account(c))
            for (a, b) in all_pairs(D):
                if not c.translates(a, b):
                    continue
                with RC.setting():
                    f0 = bool(conf_claim(c, a, b, allow))
                with RC.setting(S2_VARIANT="V2.7"):
                    f1 = bool(conf_claim(c, a, b, allow))
                if f0 and not f1:
                    lost += 1
                    if acc:
                        lost_acc += 1
                        lost_acc_inC += (a, b) in p.C
                        o0 = RC.alpha_from_confcl(c, f0)
                        o1 = RC.alpha_from_confcl(c, f1)
                        out_off += o0
                        out_on += o1
                        if wit is None:
                            wit = "%s\n%s\n%s\nat (%s,%s)" % (p.describe(), D.describe(), c.describe(), a, b)
    return dict(population="claims", drawn=n, confcl_lost_v27=lost, lost_on_accounts=lost_acc, lost_on_accounts_in_C=lost_acc_inC,
                alpha_rules_out_acc_off=out_off, alpha_rules_out_acc_v27=out_on, smallest=wit, seconds=round(time.time() - t0, 1))


def show(res):
    P = print
    P("population %s: %d drawn, %.1f s" % (res["population"], res["drawn"], res["seconds"]))
    if res["population"].startswith("single"):
        P("   Acc true: %s" % res["acc_true"])
        for s in ACC_SETTINGS:
            tot = sum(e[0] for e in res["acc_diff"][s].values())
            P("   %-22s candidates whose Acc differs from off: %d" % (s, tot))
            for k, e in sorted(res["acc_diff"][s].items(), key=lambda kv: -kv[1][0])[:8]:
                P("      %5d  %s  (smallest at %s)" % (e[0], k[:200], e[1]))
        for s in EXPL_SETTINGS:
            tot = sum(e[0] for e in res["expl_diff"][s].values())
            P("   %-22s (candidate, history) whose Account ∧ ¬Dec(t) differs from off: %d" % (s, tot))
            for k, e in sorted(res["expl_diff"][s].items(), key=lambda kv: -kv[1][0])[:8]:
                P("      %5d  %s  (smallest at %s)" % (e[0], k[:200], e[1]))
        P("   R2V2.2: accounts off %d; C6 (V2.4) keeps %s; C11 (¬Slot) keeps %s; C6 = C11 on %s candidates" % (res["acc_true"]["off"], res["c6"], res["c11"], res["c6_eq_c11"]))
        P("   extra: %s" % res["extra"])
        for k, (sz, d) in res["witnesses"].items():
            P("   smallest witness, %s (size %s):\n      %s" % (k, sz, d.replace("\n", "\n      ")))
    else:
        P("   %s" % {k: v for k, v in res.items() if k not in ("smallest",)})
        if res.get("smallest"):
            P("   smallest (candidate, pair) losing ConfCl under V2.7 with Acc T:\n      %s" % res["smallest"].replace("\n", "\n      "))


def main():
    a = sys.argv
    scale = float(a[a.index("--scale") + 1]) if "--scale" in a else 4.0
    pops = [a[a.index("--pop") + 1]] if "--pop" in a else list(R1G.SINGLE) + ["pairs", "claims"]
    out = {}
    for pop in pops:
        res = pop_single(scale, pop) if pop in R1G.SINGLE else {"pairs": pop_pairs, "claims": pop_claims}[pop](scale)
        show(res)
        sys.stdout.flush()
        out[pop] = res
    if "--json" in a:
        with open(a[a.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1, default=repr)


if __name__ == "__main__":
    main()
