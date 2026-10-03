# S109 Part B round 1: a copy of Part A round 2's `section 2 model/s108r2_owner_cases.py` (unchanged below this line), read by
# s109b_scope.py for the owner's two cases under the three readings of the owner's change (edit, boundary, mixed).
# S108 Part A round 2, section 2 (the computing agent, rule 5.1 and its first special case): the owner's two cases, the
# weathervane (S41 Q15) and the two-part shop sign (S44), with the owner's change read three ways (R2V2.1's reading):
#   edit      the program's: the wind and Tuesday are edits (claims_r3a2.m13; claims_s106.sign_two, sign_one, sign_mech);
#   boundary  round 1's second checker (results/S108 Part A - computation/second checker/owner_cases.py): the wind and the
#             day are boundaries (FC28.new2's D_vane with Γ = {cP} or {cW, cP}; the sign with B = {mon, tue}, A = {1});
#   mixed     the reply's D_vane^mix (Inv-R2-1: the wind reaches the target as a boundary b_north and as an edit setW1;
#             ℰ_mix = D, identity maps, Γ = {cW}), with Γ = {cP} and {cW, cP} added (P-R2S2-6), and a mixed sign built the
#             same way (P-R2S2-7: B = {mon, tue}, A = {1, tue_e}, C = {(1,mon), (1,tue), (tue_e,mon)}; the reply gives the
#             vane only).
# Plus E_enc (D6.10) on each question. Standalone: imports only the package `model` of the folder it is run from (any
# section copy after round 4), writes nothing. Each target is tagged with its phenomenon (read by R2V2.8's switch).
from model.core import ONE, Org, Question, PortQuery, Candidate, Translation
from model.claims_r3a2 import m13
from model.claims_s106 import sign_question, sign_two, sign_one, sign_mech
from model.claims_a import table_candidate

COL = ("red", "blue", "green")


def T(*vs):
    return {v: Translation([v]) for v in vs}


def _tag(D, ph):
    D.meta["phenomenon"] = ph
    return D


# ---- the vane ------------------------------------------------------------------------------------------------------

def vane_boundary(gamma):
    """Round 1's second checker: FC28.new2's D_vane (W the wind 0 still, 1 north, 2 gusty; P where it points), C = still/north."""
    def Lf(j, a, b):
        if j == "cW":
            return frozenset([({"b_still": 0, "b_north": 1, "b_gusty": 2}[b],)])
        return frozenset([(0, "n"), (0, "s"), (1, "n"), (2, "s"), (2, "e")])
    D = _tag(Org("D_vane", ["W", "P"], {"W": (0, 1, 2), "P": ("n", "s", "e")}, ["cW", "cP"], {"cW": ["W"], "cP": ["W", "P"]},
                 ["b_still", "b_north", "b_gusty"], [ONE], lambda a2, a1: ONE, Lf), "vane")
    p = Question(D, [(ONE, "b_still"), (ONE, "b_north")], "b_still", PortQuery(), "P", name="p_vane_b")
    lam = {"cW": (frozenset(["cW"]), {"W": Translation(["W"])}),
           "cP": (frozenset(["cP"]), {"W": Translation(["W"]), "P": Translation(["P"])})}
    return Candidate(D, p, T("W", "P"), {ONE: ONE}, {b: b for b in D.B}, lam, list(gamma), "P", name="vane-boundary Γ=" + "".join(gamma))


def _mix_compose(a2, a1):
    """1 the identity; setW1·setW1 = setW1 (a setting repeated); the reply states no composition (P-R2S2-6)."""
    if a1 == ONE:
        return a2
    if a2 == ONE:
        return a1
    return a1 if a1 == a2 else None


def vane_mixed_target():
    """D_vane^mix, as the reply writes it: V = {W, P}, X_W = {0, 1}, X_P = {n, s}; cW on (W), cP on (W, P); B = {b_still,
    b_north}; A = {1, setW1}; L_cW(1,b_still) = {(0)}, L_cW(1,b_north) = {(1)}, L_cW(setW1, b) = {(1)} at both b;
    L_cP = {(0,n), (0,s), (1,n)} everywhere."""
    def Lf(j, a, b):
        if j == "cW":
            if a == "setW1":
                return frozenset([(1,)])
            return frozenset([({"b_still": 0, "b_north": 1}[b],)])
        return frozenset([(0, "n"), (0, "s"), (1, "n")])
    return _tag(Org("D_vane_mix", ["W", "P"], {"W": (0, 1), "P": ("n", "s")}, ["cW", "cP"], {"cW": ["W"], "cP": ["W", "P"]},
                    ["b_still", "b_north"], [ONE, "setW1"], _mix_compose, Lf), "vane")


def vane_mixed(gamma=("cW",)):
    """ℰ_mix = (D, p_mix, identity, τ = {1 ↦ 1, setW1 ↦ setW1}, σ = id, λ = id, Γ, δ_E = P); p_mix: Q_w on P, C = {(1,b_still),
    (1,b_north), (setW1,b_still)}. The reply's Γ is {cW}."""
    D = vane_mixed_target()
    p = Question(D, [(ONE, "b_still"), (ONE, "b_north"), ("setW1", "b_still")], "b_still", PortQuery(), "P", name="p_mix")
    lam = {"cW": (frozenset(["cW"]), {"W": Translation(["W"])}),
           "cP": (frozenset(["cP"]), {"W": Translation(["W"]), "P": Translation(["P"])})}
    return Candidate(D, p, T("W", "P"), {ONE: ONE, "setW1": "setW1"}, {b: b for b in D.B}, lam, list(gamma), "P",
                     name="vane-mixed Γ=" + "".join(gamma))


def vane_edit(gamma=("cy",)):
    """M13 (claims_r3a2): Γ = {cy} as the program has it; Γ = {cx} (the wind's commitment) added (P-R2S2-6)."""
    c = m13()
    c.p.D.meta["phenomenon"] = "vane"
    if tuple(gamma) != ("cy",):
        c = c.replace(Gamma=tuple(gamma), name="ℰ_M13 Γ=" + "".join(gamma))
    return c


# ---- the sign ------------------------------------------------------------------------------------------------------

def _sign_org(name, comps, rel, B, A, compose):
    box = {}

    def Lf(j, a, b):
        return frozenset(rel[(j, a, b)]) if (j, a, b) in rel else box["o"].full(j)
    box["o"] = Org(name, ["colour"], {"colour": COL}, comps, {k: ("colour",) for k in comps}, B, A, compose, Lf)
    return box["o"]


def sign_boundary(parts):
    """Round 1's second checker: Monday and Tuesday as boundaries (B = {mon, tue}, A = {1})."""
    D = _tag(_sign_org("D_sign_b", ["r", "u"], {("r", ONE, "mon"): {("red",)}, ("u", ONE, "tue"): {("blue",)}}, ["mon", "tue"], [ONE],
                       lambda a2, a1: ONE), "sign")
    p = Question(D, [(ONE, "mon"), (ONE, "tue")], "mon", PortQuery(), "colour", name="p_sign_b")
    if parts == 2:
        E, lam, G = D, {k: (frozenset([k]), T("colour")) for k in ("r", "u")}, ["r", "u"]
    else:
        E = _sign_org("E_one_b", ["k"], {("k", ONE, "mon"): {("red",)}, ("k", ONE, "tue"): {("blue",)}}, ["mon", "tue"], [ONE], lambda a2, a1: ONE)
        lam, G = {"k": (frozenset(["r", "u"]), T("colour"))}, ["k"]
    return Candidate(E, p, T("colour"), {ONE: ONE}, {"mon": "mon", "tue": "tue"}, lam, G, "colour", name="sign-boundary %d-part" % parts)


def sign_mixed(parts):
    """The mixed sign (P-R2S2-7): the day reaches the sign as a boundary (mon, tue) and as an edit tue_e (making it Tuesday on
    a Monday); C = {(1,mon), (1,tue), (tue_e,mon)}. The red part r gives red where it is Monday, the blue part u blue where it
    is Tuesday; each is off (the full relation) elsewhere."""
    def compose(a2, a1):
        return _mix_compose(a2, a1)
    rel2 = {("r", ONE, "mon"): {("red",)}, ("u", ONE, "tue"): {("blue",)}, ("u", "tue_e", "mon"): {("blue",)}, ("u", "tue_e", "tue"): {("blue",)}}
    D = _tag(_sign_org("D_sign_mix", ["r", "u"], rel2, ["mon", "tue"], [ONE, "tue_e"], compose), "sign")
    p = Question(D, [(ONE, "mon"), (ONE, "tue"), ("tue_e", "mon")], "mon", PortQuery(), "colour", name="p_sign_mix")
    if parts == 2:
        E, lam, G = D, {k: (frozenset([k]), T("colour")) for k in ("r", "u")}, ["r", "u"]
    else:
        rel1 = {("k", ONE, "mon"): {("red",)}, ("k", ONE, "tue"): {("blue",)}, ("k", "tue_e", "mon"): {("blue",)}, ("k", "tue_e", "tue"): {("blue",)}}
        E = _sign_org("E_one_mix", ["k"], rel1, ["mon", "tue"], [ONE, "tue_e"], compose)
        lam, G = {"k": (frozenset(["r", "u"]), T("colour"))}, ["k"]
    return Candidate(E, p, T("colour"), {ONE: ONE, "tue_e": "tue_e"}, {"mon": "mon", "tue": "tue"}, lam, G, "colour",
                     name="sign-mixed %d-part" % parts)


def sign_edit(kind):
    if kind == "day":
        c = sign_mech()
    else:
        p = sign_question()
        c = sign_two(p) if kind == 2 else sign_one(p)
    c.p.D.meta["phenomenon"] = "sign"
    return c


def enc(c):
    """E_enc (D6.10) on the candidate's question: one component projecting Sol_D over every port (claims_a.table_candidate)."""
    e = table_candidate(c.p, set(c.p.D.ports), encode=True)
    e.name = "E_enc on " + c.p.name
    return e


# (case label, encoding, builder); E_enc is added on each question by the callers
CASES = [
    ("vane", "edit", "M13 (Γ = {cy})", vane_edit),
    ("vane", "edit", "M13 Γ = {cx} (the wind's commitment)", lambda: vane_edit(("cx",))),
    ("vane", "boundary", "D_vane Γ = {cW} (the wind's commitment)", lambda: vane_boundary(["cW"])),
    ("vane", "boundary", "D_vane Γ = {cP}", lambda: vane_boundary(["cP"])),
    ("vane", "boundary", "D_vane Γ = {cW,cP}", lambda: vane_boundary(["cW", "cP"])),
    ("vane", "mixed", "D_vane^mix Γ = {cW} (the reply's ℰ_mix)", lambda: vane_mixed(("cW",))),
    ("vane", "mixed", "D_vane^mix Γ = {cP}", lambda: vane_mixed(("cP",))),
    ("vane", "mixed", "D_vane^mix Γ = {cW,cP}", lambda: vane_mixed(("cW", "cP"))),
    ("sign", "edit", "two parts (ℰ_two, S44)", lambda: sign_edit(2)),
    ("sign", "edit", "one part (ℰ_one)", lambda: sign_edit(1)),
    ("sign", "edit", "day port (ℰ_day)", lambda: sign_edit("day")),
    ("sign", "boundary", "two parts", lambda: sign_boundary(2)),
    ("sign", "boundary", "one part", lambda: sign_boundary(1)),
    ("sign", "mixed", "two parts", lambda: sign_mixed(2)),
    ("sign", "mixed", "one part", lambda: sign_mixed(1)),
]


def all_cases():
    """[(phenomenon, encoding, label, candidate)], with E_enc on each distinct question after its candidates."""
    out, seen = [], set()
    for ph, en, lab, f in CASES:
        c = f()
        out.append((ph, en, lab, c))
        key = (ph, en, c.p.name, c.p.D.name)
        if key not in seen:
            seen.add(key)
            out.append((ph, en, "E_enc on %s" % c.p.name, enc(c)))
    return out
