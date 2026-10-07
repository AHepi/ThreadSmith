# S104 round 2 (maths), addendum: the owner's creative transport experiment
# (`tests/S104 Case - creative transport experiment, supplied by the owner/`) encoded on the S104 model,
# as a probe of the text's definitions. It is not a case with a fixed verdict. Run from the folder
# "results/S104 Round 2 - maths":
#   python3 -B s104_creative_transport.py
# Standard library only. It imports the package `model/` as committed and `s104_external.py` (for its
# surgical organizations) and changes neither; it imports the saved experiment script only to read the
# archive's rounds (grow_library) and to compare scores; it reads the text under review and the saved
# results only to compare their md5s; it writes nothing. Every choice this file makes that the text
# leaves open is an invention: I01-I102 in `inventions register.md`, I103-I108 in the addendum for the
# external examples, I109-I121 in `inventions register - addendum for the creative transport case.md`;
# the tags in the code say which. The card that reads its output is
# `results/S104 Round 2 - case card, the creative transport experiment.md`.
import hashlib
import importlib.util
import itertools
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model.core import (ONE, BOT, Question, PortQuery, Candidate, Translation, account,  # noqa: E402
                        F1_at, F2eq_at, A_at)
from model.claims_b import Hist, sel, con, faithful_on  # noqa: E402
from s104_external import surgical_org, edit  # noqa: E402

SEM = os.path.normpath(os.path.join(HERE, "..", "..", ".."))  # area 3 copy: one level deeper
TEXT = os.path.join(SEM, "tests", "103 The semantics, standing alone, after round 1.md")
TEXT_MD5 = "f31ebb1f050783f1a84f6136cec20fcd"
CASE = os.path.join(SEM, "tests", "S104 Case - creative transport experiment, supplied by the owner")
CASE_MD5 = {"README.md": "da89b7b85ec06262cadd83f4d4912557",
            "creative_transport_agent.py": "777a50780fd6be96e04cb646980a808c",
            "results.json": "2becf45d5d1abd41e8876275b361eb2c"}

ROWS = ((0, 0), (0, 1), (1, 0), (1, 1))  # the experiment's order of a two-input table (its `signature`)
EQ, XOR, FIRST, SECOND = (1, 0, 0, 1), (0, 1, 1, 0), (0, 0, 1, 1), (0, 1, 0, 1)
ALL16 = [tuple(t) for t in itertools.product((0, 1), repeat=4)]


def yn(x):
    return "yes" if x else "no"


def fn(table):
    return dict(zip(ROWS, table))


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def load_case_script():
    spec = importlib.util.spec_from_file_location("creative_transport_agent", os.path.join(CASE, "creative_transport_agent.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod  # its dataclass looks its module up here
    spec.loader.exec_module(mod)
    return mod


# ---- the target and the question (I109) ---------------------------------------------------------------

def target(sender, name="D", b_dom=(0, 1), two_polarities=False, with_sender=True):
    """I109: the transmission with the sender in place. Ports m (message bit), s (previous sent level),
    b (polarity; b1, b2 when it may change between the two levels, I121 (b)), x (sent level), rp and rc
    (previous and current received levels). Background c_m, c_s, c_b: m = s = b = 0 (the baseline), each
    replaced by the settings of its port (I04, I78, I79). enc: x = sender(s, m) (the experiment's
    encoder.run(previous_sent, message)); chp: rp = s xor b; chc: rc = x xor b (its `observations`).
    with_sender=False leaves x free (reading R-B)."""
    e = fn(sender)
    pol = ["b1", "b2"] if two_polarities else ["b"]
    ports = ["m", "s"] + pol + ["x", "rp", "rc"]
    dom = {v: (0, 1) for v in ports}
    for v in pol:
        dom[v] = tuple(b_dom)
    bp, bc = (pol[0], pol[-1])
    comps = {"c_m": (("m",), "m"), "c_s": (("s",), "s")}
    base = {"c_m": {(0,)}, "c_s": {(0,)}}
    for v in pol:
        comps["c_" + v] = ((v,), v)
        base["c_" + v] = {(dom[v][0],)}
    if with_sender:
        comps["enc"] = (("s", "m", "x"), "x")
        base["enc"] = {(s, m, e[(s, m)]) for s, m in ROWS}
    comps["chp"] = (("s", bp, "rp"), "rp")
    base["chp"] = {(s, b, s ^ b) for s in (0, 1) for b in dom[bp]}
    comps["chc"] = (("x", bc, "rc"), "rc")
    base["chc"] = {(x, b, x ^ b) for x in (0, 1) for b in dom[bc]}
    return surgical_org(name, ports, dom, comps, tuple(["m", "s"] + pol), base), pol


def full_settings(D, pol):
    """The experiment's local cases: every full setting of (m, s, polarity) (its FULL_CASES, I109)."""
    out = []
    for vals in itertools.product((0, 1), (0, 1), *[D.dom[v] for v in pol]):
        kw = dict(zip(["m", "s"] + pol, vals))
        out.append(((edit(D, **kw), "b0"), kw))
    return out


def question(D, pol, name="p", which=None):
    cases = full_settings(D, pol)
    if which is not None:
        cases = [c for c in cases if which(c[1])]
    C = [(ONE, "b0")] + [x for x, _ in cases]
    return Question(D, C, "b0", PortQuery(), "m", name=name), cases


# ---- the candidate (I110) ---------------------------------------------------------------------------

def candidate(p, sender, receiver, pol, history=True, with_sender=True, name="E"):
    """I110: a copy of the target with the receiver added: dec: y = receiver(rp, rc) (its
    decoder.run(previous_received, current_received)); with history=False, y = receiver(0, rc), the
    experiment's disconnected first port tied to 0 (also its missing reference level, I121 (c)).
    π: identity on the target's ports, y := m; τ, σ the identity; λ(j) = {j} for the copies;
    λ(dec) = {enc, chp, chc} (the sender and the channel, no input component) with rp, rc to themselves
    and y to m. Γ = {enc, dec} (or {dec} when the target has no sender); the rest is named background."""
    D = p.D
    d = fn(receiver)
    bp, bc = pol[0], pol[-1]
    ports = list(D.ports) + ["y"]
    dom = dict(D.dom)
    dom["y"] = (0, 1)
    comps = {j: (D.foot[j], None) for j in D.comps}
    base = {}
    e = fn(sender)
    for j in D.comps:
        if j.startswith("c_"):
            v = j[2:]
            comps[j] = ((v,), v)
            base[j] = {(D.dom[v][0],)}
    comps["enc"] = (("s", "m", "x"), "x")
    base["enc"] = {(s, m, e[(s, m)]) for s, m in ROWS}
    comps["chp"] = (("s", bp, "rp"), "rp")
    base["chp"] = {(s, b, s ^ b) for s in (0, 1) for b in D.dom[bp]}
    comps["chc"] = (("x", bc, "rc"), "rc")
    base["chc"] = {(x, b, x ^ b) for x in (0, 1) for b in D.dom[bc]}
    comps["dec"] = (("rp", "rc", "y"), "y")
    base["dec"] = {(a, c, d[(a if history else 0, c)]) for a, c in ROWS}
    settable = tuple(v for v in ("m", "s") + tuple(pol))
    E = surgical_org(name, ports, dom, {j: v for j, v in comps.items()}, settable, base)
    pi = {v: Translation((v,)) for v in D.ports}
    pi["y"] = Translation(("m",))
    lam = {j: (frozenset([j]), {v: Translation((v,)) for v in E.foot[j]}) for j in E.comps if j in D.comps}
    counterpart = ["enc", "chp", "chc"] if with_sender else ["chp", "chc"]
    lam["dec"] = (frozenset(counterpart), {"rp": Translation(("rp",)), "rc": Translation(("rc",)), "y": Translation(("m",))})
    if not with_sender:
        lam.pop("enc", None)
    Gamma = ["enc", "dec"] if with_sender else ["dec"]
    return Candidate(E, p, pi, {a: a for a in D.A}, {"b0": "b0"}, lam, Gamma, "y", name=name)


def a_count(c, cases):
    return sum(1 for (x, _) in cases if A_at(c, *x))


def exp_score(ct, sender, receiver, history=True, cases=None):
    """The experiment's own score for the pair with these tables (its evaluate), for comparison."""
    e, d = fn(sender), fn(receiver)
    cases = cases if cases is not None else ct.FULL_CASES
    return sum(int(d[((s ^ b) if history else 0, e[(s, m)] ^ b)] == m) for m, s, b in cases)


# ---- the runs ---------------------------------------------------------------------------------------

def main():
    if md5(TEXT) != TEXT_MD5:
        sys.exit("the text under review has md5 %s, not %s; nothing run" % (md5(TEXT), TEXT_MD5))
    for f, h in CASE_MD5.items():
        if md5(os.path.join(CASE, f)) != h:
            sys.exit("the saved case file %s has md5 %s, not %s; nothing run" % (f, md5(os.path.join(CASE, f)), h))
    ct = load_case_script()
    with open(os.path.join(CASE, "results.json"), encoding="utf-8") as f:
        res = json.load(f)
    P = print

    # CT1 (E) on the task's contract, reading R-A, the chosen pair and the others (I109, I110)
    D, pol = target(EQ, "D_EQ")
    p, cases = question(D, pol, "p_EQ")
    c = candidate(p, EQ, EQ, pol, name="E_EQ,EQ")
    val, det = account(c, detail=True)
    P("CT1  (E) for the chosen pair (sender and receiver both equality) on the question p_EQ: target D_EQ (the sender in place),")
    P("     query the value of m, contract the baseline and the eight settings of (m, s, b).")
    P("     " + ", ".join("%s %s" % (k, yn(det[k])) for k in ("F1", "F2eq", "Hom", "A", "NC1", "NC2", "NonVacuous")) + " => (E) %s" % yn(val))
    P("     (A) at %d of the 8 settings; the experiment's score for the pair: %d of 8." % (a_count(c, cases), exp_score(ct, EQ, EQ)))

    # CT2 the whole population of 256 pairs: (A) counts against the experiment's histogram; (E); fidelity on H
    hist, meets, faith, mismatch = {}, [], [], 0
    Dc, pc, cc = {}, {}, {}
    for e in ALL16:
        De, pole = target(e, "D_e")
        pe, ce = question(De, pole, "p_e")
        Dc[e], pc[e], cc[e] = De, pe, ce
        H = [x for x, _ in ce]
        for d in ALL16:
            cand = candidate(pe, e, d, pole)
            k = a_count(cand, ce)
            if k != exp_score(ct, e, d):
                mismatch += 1
            hist[k] = hist.get(k, 0) + 1
            if account(cand):
                meets.append((e, d))
            if faithful_on(cand, H):
                faith.append((e, d))
    want = {int(k): v for k, v in res["score_histogram_correct_out_of_8"].items()}
    P("CT2  All 256 pairs of two-input tables, each on its own target (reading R-A):")
    P("     (A) counts per pair, histogram %s; the experiment's histogram %s; same: %s; pairs whose (A) count differs from the experiment's score: %d."
      % (dict(sorted(hist.items())), dict(sorted(want.items())), yn(hist == want), mismatch))
    P("     pairs meeting (E): %s" % ["%s/%s" % ("".join(map(str, e)), "".join(map(str, d))) for e, d in meets])
    P("     pairs faithful ((F1) and (F2)) on H = the eight settings: %s; the same pairs: %s" % (len(faith), yn(sorted(faith) == sorted(meets))))

    # CT3 reading R-B: the channel without the sender (x free)
    D0, pol0 = target(EQ, "D_nosender", with_sender=False)
    p0, cases0 = question(D0, pol0, "p_nosender")
    c0 = candidate(p0, EQ, EQ, pol0, with_sender=False, name="E_EQ,EQ on R-B")
    v0, d0 = account(c0, detail=True)
    P("CT3  Reading R-B, the target without the sender (x free), the chosen pair with Γ = {dec}:")
    P("     " + ", ".join("%s %s" % (k, yn(d0[k])) for k in ("F1", "F2eq", "Hom", "A", "NC1", "NC2", "NonVacuous")) + " => (E) %s" % yn(v0))
    anyB = any(account(candidate(p0, e, d, pol0, with_sender=False)) for e in ALL16 for d in ALL16)
    P("     any of the 256 pairs meeting (E) on R-B: %s" % yn(anyB))

    # CT4 the archive's rounds, with and without the receiver's history port (I113, I117)
    snaps, _ = ct.grow_library()
    tabs = [sorted(set(tuple(ex.signature) for ex in s)) for s in snaps]
    row = []
    for history in (False, True):
        for r, lib in enumerate(tabs):
            best = max(a_count(candidate(pc[e], e, d, ["b"], history=history), cc[e]) for e in lib for d in lib)
            row.append("%s round %d (%d parts): best (A) %d of 8" % ("history" if history else "no history", r, len(lib), best))
    P("CT4  Per round of the archive (the experiment's grow_library), best (A) count over its pairs:")
    for x in row:
        P("     " + x)
    traj = ["%s r%d %.3f" % ("h" if t["receiver_history"] else "-", t["round"], t["accuracy"]) for t in res["trajectory"]]
    P("     the experiment's trajectory: %s" % ", ".join(traj))
    anyE_nohist = any(account(candidate(pc[e], e, d, ["b"], history=False)) for e in ALL16 for d in ALL16)
    P("     any pair of the no-history population meeting (E): %s (L481: a transport that needs a part every member is built without is not in the population)" % yn(anyE_nohist))

    # CT5 training on the noninverted channel (I121 (a)); Argument 3 (FC80)
    survA, survF = [], []
    for e in ALL16:
        Hn_e = [x for x, kw in cc[e] if kw["b"] == 0]
        for d in ALL16:
            cand = candidate(pc[e], e, d, ["b"])
            if all(A_at(cand, *x) for x in Hn_e):
                survA.append((e, d, sum(1 for x, kw in cc[e] if kw["b"] == 1 and A_at(cand, *x))))
            if faithful_on(cand, Hn_e):
                survF.append((e, d, sum(1 for x, kw in cc[e] if kw["b"] == 1 and A_at(cand, *x))))
    P("CT5  Noninverted training, as H_n = the four settings with b = 0 on the full target (reading R-A):")
    P("     survivors when survival is (A) at every pair of H_n (the experiment's score): %d; their (A) counts at the four inverted settings: %s"
      % (len(survA), sorted(k for _, _, k in survA)))
    P("     survivors when survival is fidelity on H_n ((F1) and (F2), I52): %d; their (A) counts at the four inverted settings: %s"
      % (len(survF), sorted(k for _, _, k in survF)))
    P("     the direct pair (sender sends m, receiver reads the current level) among the (A) survivors: %s; among the fidelity survivors: %s"
      % (yn(any((e, d) == (SECOND, SECOND) for e, d, _ in survA)), yn(any((e, d) == (SECOND, SECOND) for e, d, _ in survF))))
    Dn, poln = target(SECOND, "D_noninverting", b_dom=(0,))
    pn, casesn = question(Dn, poln, "p_noninverting")
    vn, dn = account(candidate(pn, SECOND, SECOND, poln, name="E_direct"), detail=True)
    P("     on a target whose polarity cannot invert (b ∈ {0}): the direct pair: " + ", ".join("%s %s" % (k, yn(dn[k])) for k in ("F1", "F2", "A", "NC1", "NC2", "NonVacuous")) + " => (E) %s" % yn(vn))
    vfull = account(candidate(pc[SECOND], SECOND, SECOND, ["b"]))
    P("     the direct pair on the full target p (b ∈ {0,1}): (E) %s; (A) at %d of 8" % (yn(vfull), a_count(candidate(pc[SECOND], SECOND, SECOND, ["b"]), cc[SECOND])))

    # CT6 polarity that may change between the two levels (I121 (b)): a new question
    polcp = ["b1", "b2"]
    for s_, r_, nm in ((EQ, EQ, "equality pair"), (XOR, XOR, "xor pair")):
        Dx, _ = target(s_, "D_changing", two_polarities=True)
        px, cx = question(Dx, polcp, "p_changing")
        cand = candidate(px, s_, r_, polcp)
        vcp, dcp = account(cand, detail=True)
        P("CT6  Varying polarity (b1 for the previous level, b2 for the current), the %s: (A) at %d of %d settings; (E) %s (F2 %s)"
          % (nm, a_count(cand, cx), len(cx), yn(vcp), yn(dcp["F2"])))
    P("     the experiment's changing-polarity accuracy for its chosen pair: %s" % res["changing_polarity"]["accuracy"])

    # CT7 the missing reference level (I121 (c))
    cm = candidate(pc[EQ], EQ, EQ, ["b"], history=False, name="E_EQ,EQ, no reference")
    P("CT7  The chosen pair with the previous-level port fed 0 (no reference level): (A) at %d of 8; (E) %s; the experiment's first-bit accuracy %s"
      % (a_count(cm, cc[EQ]), yn(account(cm)), res["missing_initial_reference"]["first_bit_accuracy"]))

    # CT8 provenance under readings of 'represents' and of Build (I114, I115; D12.1, H05)
    H = [x for x, _ in cc[EQ]]
    cq = candidate(pc[EQ], EQ, EQ, ["b"])
    occ = ["o_cases", "o_score", "o_trees", "o_channel", "o_switch"]
    readings = [
        ("R1", "the run's carriers represent in the ordinary sense: its case table H, its scoring (the survival condition), the pair t, and the codomain; Build's primitives met",
         [("o_cases", "H"), ("o_score", "surv"), ("o_trees", "t"), ("o_trees", "cod")], True),
        ("R2", "as R1; Build's primitives not met (exhaustive composition is not a binding construction for explanatory use)",
         [("o_cases", "H"), ("o_score", "surv"), ("o_trees", "t"), ("o_trees", "cod")], False),
        ("R3", "the designer's code declared, so it represents nothing under (R); the expression trees built in the run represent the codomain's generated components; Build met",
         [("o_trees", "cod")], True),
        ("R4", "as R3; Build not met", [("o_trees", "cod")], False),
        ("R5", "nothing in the run represents under (R) (the designer's code declared, the trees' own correspondences not representations); Build met or not",
         [], True),
    ]
    P("CT8  Provenance of the chosen pair's transport on one history of the run (Θ set by hand, I90): H = the eight settings, all occurring;")
    P("     Sel as D12.1 has it after round 2 (D12.1': no represented codomain; I161: no trace in the history prepares t), and with L201 and L411 read into it.")
    for rid, text, rep, prep in readings:
        h = Hist(occ, rep, set(H), admitted=True, prepares=prep)
        s1 = sel(cq, H, h)
        s2 = s1 and not any(x in ("t", "cod") for (_, x) in h.rep)
        k = con(h)

        def cls(s, k):
            return "both" if (s and k) else ("selected" if s else ("constructed" if k else "neither (declared by exclusion)"))
        P("     %s  %s" % (rid, text))
        P("         D12.1: Sel %s, Con %s => %s;  with L201 and L411: Sel %s, Con %s => %s" % (yn(s1), yn(k), cls(s1, k), yn(s2), yn(k), cls(s2, k)))
    P("     faithful on H (the survival condition read as fidelity): %s" % yn(faithful_on(cq, H)))


if __name__ == "__main__":
    main()
