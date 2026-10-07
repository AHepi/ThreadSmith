# S108 Part A round 2, section 3: the worked cases, the owner's cases and the reply's small cases, each round-2 variant (and each
# round-1 candidate C7–C10 under round 2's readings) off and on.
#   PYTHONHASHSEED=0 python3 -B s108r2_s3_cases.py [A|B|C|D|E ...]
# A. Every worked case the program builds (s106_cases.py's, collected as round 1 did) and the owner's cases (the second checker's
#    owner_cases.py: the weathervane and the shop sign with one part and with two, the change as an edit and as a boundary):
#    Acc(ℰ), and Dec(t) and Account ∧ ¬Dec(t) on every history of s108r2_s3_common.judge, under each state of
#    s108r2_s3_common.STATES against its baseline.
# B. The student's declared copy (FC30.new1 (d)) and the bridge (FC84.new1 (a1), (a2)), each state.
# C. The reply's small cases, R2V3.1–R2V3.7, each built and run (every "after" of the reply was marked not run).
# D. Arguments: R2V3.8 (D9.2), R2V3.9 (D9.1), the reply's cases and the (Suff) defeat by a premise alone.
# E. R2V3.10 (D15.5): Can, Deploy and CreateEx over Θ's values.
# Writes nothing (prints).
import contextlib
import io
import itertools
import sys

import s108r2_s3_common as K
from s108r2_s3_common import set_state, reset, STATES, BASE, judge, chain_dec, chain_out, claim_ep, acc_of, extras
from model import s108s3, s108r2s3  # noqa: F401
from model.core import ONE, Question, PortQuery, account, faithful
from model.args import Not, And, Imp, Leaf, Step, Assessor, X, usable, rules_out, enumerate_args
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate
from model.claims_a import pole_contracts
from model.claims_b import Hist, sel, con, prov_fixed_points, prov_show, build_at, faithful_on, chain_eps, fwd_pole_cand
from model.claims_s41 import suff_defeats, not_using_E, provenance_of
import s106_cases
import s108_s3_cases as R1
import s108r2_owner_cases as OC


def tf(x):
    return "T" if x is True else ("F" if x is False else repr(x))


def section(t):
    print("=" * 150)
    print(t)
    print("-" * 150)


def worked_cases():
    got = []
    orig = s106_cases.case
    s106_cases.case = lambda label, where, c, note="": got.append((label, where, c))
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            s106_cases.main()
    finally:
        s106_cases.case = orig
    return got


def all_cases():
    cs = [(lab, c) for lab, where, c in worked_cases()]
    cs += [("owner: " + n, f()) for n, f in OC.CASES]
    return cs


# ---- A --------------------------------------------------------------------------------------------------------------------

def part_a():
    section("A. Worked cases (s106_cases.py's 27) and the owner's cases (8): Acc; Dec(t), Account ∧ ¬Dec(t) per history; each state against its baseline")
    cases = all_cases()
    print("%d cases. Histories (s108r2_s3_common.HIST_NOTE):" % len(cases))
    for k, v in K.HIST_NOTE.items():
        print("   %-28s %s" % (k, v))
    res = {}
    for name, kw in STATES:
        set_state(**kw)
        res[name] = {lab: judge(c, [(ONE, c.p.b0)]) for lab, c in cases}
    reset()
    base = res["none"]
    print("\n--- 'none': Acc T on %d of %d; per case: Acc, Acc(ℰ′) for the claims own/widest/designation/gamma/port" % (sum(r["Acc"] for r in base.values()), len(cases)))
    for lab, c in cases:
        r = base[lab]
        print("   %-70s Acc %s; ℰ′: %s" % (lab[:70], tf(r["Acc"]), " ".join("%s %s" % (w, tf(r.get("Acc(ℰ′) " + w))) for w in K.CLAIMS)))
    summary = {}
    for name, kw in STATES[1:]:
        b = res[BASE.get(name, "none")]
        e = res[name]
        cnt, rows = {}, []
        for lab, c in cases:
            for k in e[lab]:
                if k in b[lab] and e[lab][k] != b[lab][k]:
                    key = k
                    if k.startswith("Expl"):
                        d = "in" if (e[lab][k] is True or (isinstance(e[lab][k], tuple) and any(e[lab][k]))) else "out"
                        key = "%s %s" % (k, d)
                        rows.append("   %s | %s: %s → %s" % (lab[:70], k, tf(b[lab][k]), tf(e[lab][k])))
                    elif k.startswith("Dec"):
                        key = "%s (Acc %s)" % (k, tf(e[lab]["Acc"]))
                    cnt[key] = cnt.get(key, 0) + 1
        summary[name] = cnt
        print("\n--- %s (against %s): %s" % (name, BASE.get(name, "none"), cnt if cnt else "no move"))
        for r in rows:
            print(r)
    print("\n--- summary: moves of Account ∧ ¬Dec(t) (Expl …) per state")
    for name, cnt in summary.items():
        print("   %-55s %s" % (name, {k: v for k, v in cnt.items() if k.startswith("Expl")} or "0"))
    return res


# ---- B --------------------------------------------------------------------------------------------------------------------

def part_b():
    section("B. The student's declared copy (FC30.new1 (d)) and the bridge (FC84.new1 (a1), (a2)), each state")
    D = pole()
    C1, _, _ = pole_contracts(D)
    for name, kw in STATES:
        set_state(**kw)
        c = pole_fwd_candidate(Question(D, C1, "b1_45", PortQuery(), "L", name="p"))
        acc = bool(account(c))
        rows = []
        for Hx, lab in (([(ONE, "b1_45")], "H={(1,b1_45)}"), ([], "H=∅")):
            held_o = bool(faithful(c))
            selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
            fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], "T'", True)
            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
            rows.append("%s: Dec(t) at o2 %s, Expl %s" % (lab, decs, [acc and not d for d in decs]))
        br = []
        for key, held_, trace_ in (("a1", [0, 1], [0, 1]), ("a2", [0, 0, 1], [0, 0, 1])):
            n_ = len(held_)
            fps = prov_fixed_points(n_, held_, trace_, [0] * n_, "T'", True, chain_eps(["C_brief"] * n_, [False] * n_))
            conv = [sc[n_ - 1][1] for R, sc in fps]
            h_ = Hist(["o%d" % (i + 1) for i in range(n_)], [("o%d" % n_, "cod")], set(), prepares=True, contracts=["C_brief"] * n_, records=[False] * n_)
            br.append("(%s) Con at the output %s, Build %s, tag model Con %s" % (key, conv, build_at(n_, held_, trace_, "T'", fps[0][0] if fps else frozenset(), n_ - 1), con(h_)))
        print("%-55s student: Acc %s | %s || bridge: %s" % (name, tf(acc), " | ".join(rows), "; ".join(br)))
    reset()


# ---- C --------------------------------------------------------------------------------------------------------------------

def pole_p():
    D = pole()
    C1, _, _ = pole_contracts(D)
    return D, Question(D, C1, "b1_45", PortQuery(), "L", name="p_C1")


def small_r2v31():
    section("C. R2V3.1 (C8 under S108-3-I2's and I5's other choices): the pole's forward candidate; the trace's output uses 'Acc(ℰ′)'")
    D, p = pole_p()
    c = pole_fwd_candidate(p)
    print("ℰ: δ_E = %s, E's ports %s, Acc(ℰ) %s" % (c.deltaE, c.E.ports, tf(acc_of(c))))
    for w in K.CLAIMS:
        e2 = claim_ep(c, w)
        a2 = acc_of(e2) if e2 is not None else None
        desc = "none" if e2 is None else "δ′ = %s, Γ′ = %s, p′ = %s (|C′| = %d)" % (e2.deltaE, list(e2.Gamma), e2.p.name, len(e2.p.C))
        rows = []
        for name, kw in (("none", {}), ("C8: V3.4, CT reads Prepares", dict(r1="V3.4", ct="prepares")), ("R2V3.1", dict(r2="R2V3.1"))):
            set_state(**kw)
            ex = s108s3.expl_use(True, a2) if a2 is not None else True
            held_o = bool(faithful(c))
            fps = prov_fixed_points(1, [held_o], [1], [0], "T'", True, explu=[ex])
            s_, k_ = fps[0][1][0]
            h = Hist(["o1"], [("o1", "cod")], set(p.C), admitted=True, prepares=True, explu=ex)
            kt = con(h)
            b_ = build_at(1, [1], [1], "T'", frozenset(), 0, explu=[ex])
            rows.append("%s: ExplUse %s, Build %s, chain Con %s Dec %s Account ∧ ¬Dec(t) %s; tag Con %s" % (name, tf(ex), tf(b_), tf(k_), tf(not s_ and not k_), tf(bool(acc_of(c)) and (s_ or k_)), tf(kt)))
        reset()
        print("  claim %-12s ℰ′: %s; Acc(ℰ′) %s\n      %s" % (w, desc, tf(a2), "\n      ".join(rows)))


def small_r2v32():
    section("C. R2V3.2 (D13.8's key: the formal core's 'new contract' → the variant's 'the change'; the program keys by the change, I174)")
    rows = [("the reply's case: q = [C′, C, C], one record, of ρ_C, at o3; cod t tagged at o1; the trace at o3",
             ["C'", "C", "C"], [False, False, True], [1, 0, 1], [0, 0, 1], [0, 1, 0]),
            ("one contract entered twice: q = [C, C′, C, C′], records of ρ_C′ at o2, ρ_C at o3, none at o4 (the second C → C′)",
             ["C", "C'", "C", "C'"], [False, True, True, False], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 2, 0])]
    for lab, qs, rs, held, trace, start in rows:
        n = len(qs)
        print(lab)
        for key in ("contract", "change"):
            for r1 in ("none", "V3.5"):
                set_state(r1=r1, reckey=key)
                h = Hist(["o%d" % (i + 1) for i in range(n)], [("o1", "cod")], set(), admitted=True, prepares=True, contracts=qs, records=rs)
                ep_all = K.claims_b.episode(qs, rs)
                d_tag = not con(h)
                d_ch = chain_dec(n, held, trace, [0] * n, qs, rs, "T'")
                d_ch0 = chain_dec(n, [1] + [0] * (n - 1), trace, [0] * n, qs, rs, "T'")
                d_sp = chain_dec(n, held, trace, [0] * n, qs, rs, "T'", start=start)
                d_K = chain_dec(n, held, trace, [0] * n, qs, rs, "K")
                print("   key %-8s %-5s Episode(o1…o%d) %s | tag: Con %s, Dec %s | chain T′ (held at the output): Dec %s | chain T′, not held at the output: Dec %s | trace spanning o1…o%d: Dec %s | cut K: Dec %s"
                      % (key, r1, n, tf(ep_all), tf(not d_tag), tf(d_tag), tf(d_ch), tf(d_ch0), n, tf(d_sp), tf(d_K)))
        reset()
    print("before (FC84.new1 (c), the program): unrecorded C → C′, S41 reading — o1 ≺ o2 an episode: %s" % tf(K.claims_b.episode(["C", "C'"], [False, False])))


def small_r2v33():
    section("C. R2V3.3: (a) Held read as a tag at o1 before an unrecorded change, the record clause kept; (b) the trace's extent the whole subhistory")
    D, p = pole_p()
    c = pole_fwd_candidate(p)
    held_o = bool(faithful(c))
    print("the pole's forward candidate on C1: Acc %s, Faithful %s" % (tf(acc_of(c)), tf(held_o)))
    for r1 in ("none", "V3.5"):
        set_state(r1=r1)
        h = Hist(["o1", "o2"], [("o1", "cod")], {(ONE, "b1_45")}, admitted=True, prepares=True, contracts=["C", "C'"], records=[False, False])
        s_, k_ = sel(c, [(ONE, "b1_45")], h), con(h)
        rows = ["(a) the reply's Hist (tag at o1, the trace at o2): Sel %s Con %s Dec %s" % (tf(s_), tf(k_), tf(not s_ and not k_))]
        for rd in ("T'", "T", "K", "U"):
            at = chain_dec(2, [1, held_o], [0, 1], [0, 0], ["C", "C'"], [False, False], rd)
            sp = chain_dec(2, [1, held_o], [0, 1], [0, 0], ["C", "C'"], [False, False], rd, start=[0, 0])
            tg = chain_dec(2, [1, 0], [0, 1], [0, 0], ["C", "C'"], [False, False], rd)
            rows.append("%s: chain, Held computed at o2, trace at o2: Dec %s | (b) trace spanning o1…o2: Dec %s | (a) as a chain, not held at o2 (the tag): Dec %s" % (rd, tf(at), tf(sp), tf(tg)))
        print("  %s:\n      %s" % (r1, "\n      ".join(rows)))
    reset()


def small_r2v34():
    section("C. R2V3.4 (D15.8's parts as ports with their bindings, R2-3-I4; the other choice, edits): the pole, t′ = t + k_x, stated construction t's own parts")
    D, p = pole_p()
    t = pole_fwd_candidate(p)
    H = [(ONE, "b1_45")]
    for name, kw in (("components (none)", {}), ("ports (R2V3.4)", dict(r2="R2V3.4", parts="ports")), ("edits", dict(r2="R2V3.4", parts="edits")),
                     ("V3.6 (round 1, clause deleted)", dict(r1="V3.6"))):
        set_state(**kw)
        ex = extras(t, H, R1)
        print("  %-32s parts(t) %s" % (name, sorted(map(str, s108r2s3.parts_read(t, list(t.E.comps))))[:6]))
        for lab, r in ex.items():
            print("      t′ %-8s %s" % (lab, r))
        # 'Sel-parts' on t itself: stated := all but E's last component
        h = Hist(["o1"], [], set(p.C), admitted=True, prepares=False, parts=list(t.E.comps), stated=list(t.E.comps)[:-1])
        s_ = sel(t, H, h)
        print("      t on 'Sel-parts' (stated = %s): Sel %s, Dec %s, Account ∧ ¬Dec(t) %s" % (list(t.E.comps)[:-1], tf(s_), tf(not s_), tf(bool(acc_of(t)) and s_)))
    reset()


def small_r2v35():
    section("C. R2V3.5 (no construction stated ⇒ 𝒯 = ∅): the pole's forward candidate on provenance_of's 'Sel' history; the student's copy")
    D, p = pole_p()
    t = pole_fwd_candidate(p)
    for name, kw in (("none", {}), ("R2V3.5", dict(r2="R2V3.5")), ("C10: V3.6 with R2V3.5", dict(r1="V3.6", r2="R2V3.5"))):
        set_state(**kw)
        s_, k_, d_ = provenance_of(t, "Sel", [(ONE, "b1_45")])
        print("  %-24s Sel %s, Con %s, Dec %s, Account ∧ ¬Dec(t) %s" % (name, tf(s_), tf(k_), tf(d_), tf(bool(acc_of(t)) and not d_)))
    reset()


def small_r2v37():
    section("C. R2V3.7 (D11.3: ⪯_h the reflexive closure of ≺_h): o1 ≺ o2 ≺ o3, one contract, cod t tagged or held at o1, the trace at o3")
    for name, kw in (("none", {}), ("R2V3.7", dict(r2="R2V3.7"))):
        set_state(**kw)
        h = Hist(["o1", "o2", "o3"], [("o1", "cod")], set(), admitted=True, prepares=True)
        h2 = Hist(["o1", "o2", "o3"], [("o1", "cod")], set(), admitted=True, prepares=True, contracts=["C"] * 3, records=[False] * 3)
        rows = ["tag model: Con %s (contracts unstated), %s (one contract stated)" % (tf(con(h)), tf(con(h2)))]
        for held in ([1, 0, 1], [1, 0, 0], [0, 1, 0]):
            rows.append("chain held %s: %s" % (held, "; ".join("%s Dec %s" % (rd, tf(chain_dec(3, held, [0, 0, 1], [0, 0, 0], ["C"] * 3, [False] * 3, rd))) for rd in ("T'", "T", "K", "U"))))
        print("  %-8s %s" % (name, "\n           ".join(rows)))
    reset()


# ---- D --------------------------------------------------------------------------------------------------------------------

def part_d():
    section("D. Arguments: R2V3.8 (D9.2: every argument has a step) and R2V3.9 (D9.1 without 'Ans_p(a,b) = y')")
    PM, design = "PM", "design"
    for name, kw in (("none", {}), ("R2V3.8", dict(r2="R2V3.8")), ("R2V3.9 (I8 kept)", dict(r2="R2V3.9")), ("R2V3.9 (I8 dropped)", dict(r2="R2V3.9", i8="dropped"))):
        set_state(**kw)
        rows = []
        j = Assessor(["MP", "MT", "AndI", "AndE"], [Not(PM)])
        bare = Leaf(Not(PM))
        rows.append("S27/S41 Q23 (FC72 (d)): j accepts ¬PM; ¬PM alone: usable %s, rules out design ∧ PM %s; |X_j(design ∧ PM)| over every argument of height ≤ 2 from ¬PM: %d"
                    % (tf(usable(j, bare)), tf(rules_out(bare, And(design, PM))), len(X(j, And(design, PM), enumerate_args([Not(PM)], depth=2)))))
        e = "Expl_E"
        psi = And("r", Imp("r", Not(e)))
        p_, c_ = fwd_pole_cand()
        s0, k0, dec = provenance_of(c_, "Con", [(ONE, "b1_45")])
        for forms in (("MP", "AndE"), ("MP",)):
            jx = Assessor(list(forms), [psi])
            xs = [a for a in X(jx, e, enumerate_args([psi], forms=forms, depth=2)) if not_using_E(a, "E")]
            rows.append("(Suff) by a premise alone: j (forms %s) accepts ψ = r ∧ (r → ¬Expl(ℰ)); arguments not using (E) ruling out Expl(ℰ): %d (premise-alone among them: %d); the pole's constructed candidate in Def(L536): %s"
                        % ("/".join(forms), len(xs), sum(1 for a in xs if isinstance(a, Leaf)), tf(suff_defeats(bool(account(c_)), dec, bool(xs), "L536"))))
        jp = Assessor(["MP"], ["p"])
        rows.append("'p because p': j accepts p; p alone rules out ¬p: %s (D9.7's block), usable %s" % (tf(rules_out(Leaf("p"), Not("p"))), tf(usable(jp, Leaf("p")))))
        # answers: a test and FC68's argument from each candidate's own answer
        A = "Ans_ab_y"
        jt = Assessor(["MP", "MT"], ["rec", Imp("rec", Not(A))])
        test = Step("MP", Not(A), [Leaf("rec", "record"), Leaf(Imp("rec", Not(A)))])
        rows.append("a test's record rules out the answer y: X_j('Ans_p(a,b) = y') = %d; j accepting ¬(Ans = y) alone rules it out: %s"
                    % (len(X(jt, A, [test, Leaf(Not(A))])), tf(bool(X(Assessor(["MP"], [Not(A)]), A, [Leaf(Not(A))])))))
        rec, ay = "rec", "ans_is_y"
        accs = ["acc1", "acc2"]
        jj = Assessor(["MP", "MT"], [rec, Imp(rec, Not(ay))] + [Imp(a, ay) for a in accs])
        s1 = Step("MP", Not(ay), [Leaf(rec, "record"), Leaf(Imp(rec, Not(ay)))])
        args = {a: Step("MT", Not(a), [s1, Leaf(Imp(a, ay))]) for a in accs}
        rows.append("FC68 (b): the argument from the test and each candidate's own answer rules out Acc of both: %s" % tf(all(usable(jj, args[a]) and rules_out(args[a], a) for a in accs)))
        # FC47.new1's pole, forward against reversed, the test's record typed as the answer claim (Test_ab := Ans_p(a,b), D10.3)
        rt, bg, ab, acc = "Ans_rec", "bg", "A_ab_bad", "acc_bad"
        prem = [rt, bg, Imp(And(rt, bg), Not(ab)), Imp(acc, ab)]
        s0_ = Step("AndI", And(rt, bg), [Leaf(rt, "record"), Leaf(bg)])
        s1_ = Step("MP", Not(ab), [s0_, Leaf(Imp(And(rt, bg), Not(ab)))])
        alpha = Step("MT", Not(acc), [s1_, Leaf(Imp(acc, ab))])
        allargs = enumerate_args(prem, forms=("MP", "MT", "AndI"), depth=2, max_args=300) + [alpha]
        jx1 = Assessor(["MP", "MT", "AndI"], prem)
        out_bad = bool(X(jx1, acc, allargs))
        rows.append("FC47.new1's case, Test_ab typed as the answer claim: at ξ the candidate whose answer differs ruled out %s, so Solved %s and Prob_j %s"
                    % (tf(out_bad), tf(out_bad), tf(not out_bad)))
        print("  %s:\n      %s" % (name, "\n      ".join(rows)))
    reset()


# ---- E --------------------------------------------------------------------------------------------------------------------

def part_e():
    section("E. R2V3.10 (D15.5: Can := owned RetReal, the construction disjunct deleted): Deploy (D13.1) and CreateEx (D14.7) over Θ's values")
    THETA = ("CCE", "Origin", "Repair, O_ex, ProducesVia, Acc, Result, e_c ⪯ e", "Rep ∧ Integrated", "owned RetReal", "an owned construction of such")
    tot = {}
    for name, kw in (("none", {}), ("R2V3.10", dict(r2="R2V3.10"))):
        set_state(**kw)
        cnt = dict(can=0, deploy=0, createx=0)
        for bits in itertools.product([False, True], repeat=len(THETA)):
            w = dict(zip(THETA, bits))
            can = w["owned RetReal"] or (w["an owned construction of such"] and not s108r2s3.on("R2V3.10"))
            deploy = w["Rep ∧ Integrated"] and can
            cx = s108s3.create_ex(w["CCE"], w["Origin"], w["Repair, O_ex, ProducesVia, Acc, Result, e_c ⪯ e"] and deploy)
            cnt["can"] += can
            cnt["deploy"] += deploy
            cnt["createx"] += cx
        tot[name] = cnt
        print("  %-8s of %d valuations: Can %d, Deploy %d, CreateEx %d; D18.1's Can → %s" % (name, 2 ** len(THETA), cnt["can"], cnt["deploy"], cnt["createx"], K.claims_b.s108r2_s3_dep(K.claims_b.DEP_S108_NONE)["Can"]))
    reset()
    print("  (E), Dec, Account ∧ ¬Dec(t): no definition of them reads Can (D18.1: Can's only readers are Deploy, Tol, Enable, UU); see A for the cases")


def main():
    which = sys.argv[1:] or ["A", "B", "C", "D", "E"]
    if "A" in which:
        part_a()
    if "B" in which:
        part_b()
    if "C" in which:
        small_r2v31()
        small_r2v32()
        small_r2v33()
        small_r2v34()
        small_r2v35()
        small_r2v37()
    if "D" in which:
        part_d()
    if "E" in which:
        part_e()


if __name__ == "__main__":
    main()
