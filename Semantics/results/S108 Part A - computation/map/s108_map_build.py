#!/usr/bin/env python3
"""S108 Part A, rule 6: build the dependency map (.json, and the tables of the .md) from
the frozen template, the frozen set, the tabulation's variant list, the four
'variants computed' files' edge .json and the program's D18.1 graph (after round 4).

Reads only; writes only the two map files given on the command line. Changes nothing in the
theory's text, formal core, claims or program (rule 11). "Candidate"/"explanation" for what the
theory judges; "model" only for the program's own small structures (S43).

usage: python3 -B s108_map_build.py <out.json> <out-tables.md>
"""
import ast
import collections
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RES = HERE.parents[1]                       # Semantics/results
TEMPLATE = RES / "S108 Part A - the frozen template.md"
FROZEN = RES / "S108 Part A - the frozen set.json"
TAB = RES / "S108 Part A - tabulation of the replies, before any ruling.md"
SEC = {i: RES / f"S108 Part A - section {i} - variants computed.json" for i in (1, 2, 3, 4)}
SECMD = {i: RES / f"S108 Part A - section {i} - variants computed.md" for i in (1, 2, 3, 4)}
PROG = RES / "S107 Round 4 - maths after the reading" / "model after round 4" / "model" / "claims_b.py"


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


# ---------------------------------------------------------------- the template's items
PART_SEC = {"Part 0": "S1", "Part I": "S1", "Part II": "S1", "Part III": "S1",
            "Part IV": "S2", "Part V": "S2", "Part VI": "S2", "Part VII": "S2",
            "Part VIII": "S3", "Part IX": "S3", "Part X": "S3", "Part XI": "S3", "Part XII": "S3",
            "Part XIII": "S4", "Part XIV": "S4", "Part XV": "S4", "Part XVI": "S4"}


def parse_template():
    lines = TEMPLATE.read_text(encoding="utf-8").split("\n")
    sents, defs, claims = collections.OrderedDict(), collections.OrderedDict(), collections.OrderedDict()
    part = None
    in_claims = False
    for i, l in enumerate(lines):
        m = re.match(r"^# (Part [0IVX]+) —", l)
        if m:
            part = m.group(1)
        m = re.match(r"^`(L(\d+)\.[sn]\d+)` \| (FROZEN|S[1-4]) \| (.*)$", l)
        if m:
            sents[m.group(1)] = {"id": m.group(1), "kind": "sentence", "line": int(m.group(2)),
                                 "mark": m.group(3), "part": part, "stretch": PART_SEC[part],
                                 "text": m.group(4)[:200]}
        m = re.match(r"^⟦(FROZEN|S[1-4])⟧ (\S+)$", l)
        if m:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            t = re.match(r"^\*\*\S+ (.*?)\*\*", nxt)
            defs[m.group(2)] = {"id": m.group(2), "kind": "definition", "mark": m.group(1),
                                "title": (t.group(1) if t else nxt[:120]).rstrip(". ")}
        if l.startswith("## 5. The claims, by section"):
            in_claims = True
        if in_claims:
            m = re.match(r"^\| (FC[\w.]+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", l)
            if m:
                claims[m.group(1)] = {"id": m.group(1), "kind": "claim", "title": m.group(2),
                                      "lines": m.group(3), "mark": m.group(4), "result_after_round_4": m.group(5)}
    fs = json.loads(FROZEN.read_text(encoding="utf-8"))
    for d in fs["definitions"]:
        if d["id"] in defs:
            defs[d["id"]]["part"] = d["part"]
            defs[d["id"]]["stretch"] = PART_SEC.get(d["part"])
    assert len(sents) == 688 and len(defs) == 127, (len(sents), len(defs))
    return sents, defs, claims


# ---------------------------------------------------------------- D18.1's graph (the program's DEP)
def parse_dep():
    src = PROG.read_text(encoding="utf-8")

    def grab(name):
        i = src.index("\n" + name + " = {") + 1
        j = src.index("{", i)
        depth, k = 0, j
        while True:
            c = src[k]
            depth += c == "{"
            depth -= c == "}"
            k += 1
            if depth == 0:
                break
        return ast.literal_eval(src[j:k])
    dep = grab("DEP")
    d2n = grab("D_TO_NODE")
    dep = {k: [x[1] if isinstance(x, tuple) else x for x in v] for k, v in dep.items()}
    return dep, d2n


def nat(x):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", x)]


def ancestors(dep, node):
    seen, stack = set(), [node]
    while stack:
        n = stack.pop()
        for m in dep.get(n, []):
            if m not in seen:
                seen.add(m)
                stack.append(m)
    return seen


# ---------------------------------------------------------------- the parts of the explanation definition
XNODES = collections.OrderedDict([
    ("X:(E)", {"name": "(E), Account(ℰ) = Acc(ℰ)", "defined_by": ["D6.7"], "dep": "(E)",
               "statement": "Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous; arguments (D, C, b0, Q, δ_D, E, t, Γ, δ_E, Σ): no assessor, no history, no provenance, no grain (FC30)",
               "reads": ["X:(F1)", "X:(F2)", "X:(A)", "X:Dependence", "X:NonVacuous"]}),
    ("X:(F1)", {"name": "(F1) component fidelity", "defined_by": ["D5.4"], "dep": "(F1)",
                "statement": "∀k ∈ Γ ∀(a,b) ∈ C: proj^λ_{V_k}[Sol_{N_k}(a,b)] = L^E_k(τ(a),σ(b))",
                "reads": ["D1.4", "D5.2", "D5.1", "D5.3", "D1.1"]}),
    ("X:(F2)", {"name": "(F2) solutions carried; Hom(τ)", "defined_by": ["D5.5"], "dep": "(F2)",
                "statement": "∀(a,b) ∈ C: π[Sol_D(a,b)] = Sol_E(τ(a),σ(b)); Hom(τ)",
                "reads": ["D1.2", "D5.1", "D1.1"]}),
    ("X:(A)", {"name": "(A) question fidelity", "defined_by": ["D5.6"], "dep": "(A)",
               "statement": "∀(a,b) ∈ C: Ans_E(τ(a),σ(b)) = Ans_p(a,b), ⊥ = ⊥",
               "reads": ["D3.2", "D5.3", "D5.1"]}),
    ("X:Dependence", {"name": "Dependence = NC0 ∧ NC2", "defined_by": ["D6.5", "D6.4", "D6.2", "D6.1"], "dep": "Dep",
                      "statement": "∃(a,b) ∈ C, ∅ ≠ G ⊆ Γ: Contrast(E;x) ∧ Lost(E,G;x); NC0 holds of every candidate",
                      "reads": ["D6.4", "D6.2", "D6.1", "D1.3", "D3.2", "D5.3"]}),
    ("X:NonVacuous", {"name": "NonVacuous", "defined_by": ["D6.6"], "dep": "NV",
                      "statement": "Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ)", "reads": ["D1.2", "D3.5", "D0.2"]}),
    ("X:Dec", {"name": "Dec(t), declared", "defined_by": ["D12.3"], "dep": "Dec",
               "statement": "a holding reached by transfer inherits prov (D12.4); otherwise Dec(t,o_t) :⟺ no parameters give Sel(t;·) and none give Con(t;·), on h(t,o_t)",
               "reads": ["D12.1", "D12.2", "D12.4", "D13.3", "D15.8", "D13.8", "D5.7", "D12.5"]}),
    ("X:Expl", {"name": "being an explanation", "defined_by": ["D16.XV"], "dep": "DefeatConds",
                "statement": "Expl an atom; Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) (S41 Q2); written in the text as Account(ℰ) ∧ ¬Dec(t) (L17.n2, L49.n3, L61.n2, L69.n3)",
                "reads": ["X:(E)", "X:Dec"]}),
    ("X:(Suff)", {"name": "(Suff), L536 and L17", "defined_by": ["D16.XV"], "dep": "DefeatConds",
                  "statement": "defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]",
                  "reads": ["X:(E)", "X:Dec", "D9.8", "D9.6", "D9.7"]}),
    ("X:(Nec)", {"name": "(Nec), L538", "defined_by": ["D16.XV"], "dep": "DefeatConds",
                 "statement": "defeated for j ⟺ ∃ℰ [∃α ∈ X_j(¬Expl(ℰ)): Acc ∉ Uses(α) ∧ ∀C′ on D ∀t′: ¬Faithful_{C′}(t′: D → E)]",
                 "reads": ["D9.8", "D9.6", "D9.7", "D5.7"]}),
])

# ---------------------------------------------------------------- the variants (tabulation §2, §6; computing files §1)
V = collections.OrderedDict()


def var(vid, sec, varied, kind, new, impl, inv, dep_node, with_sents=()):
    V[vid] = {"id": vid, "section": sec, "varied": list(varied) + list(with_sents), "definitions_varied": list(varied),
              "sentences_varied_with_it": list(with_sents), "kind": kind, "new": new, "implemented": impl,
              "inventions": inv, "d18_node": dep_node}


var("V1.1", "S1", ["D1.4"], "swap", "Sol_N(a,b) := {y|V_N : y ∈ Sol_D(a,b)}", "yes", ["S108-1-I1", "S108-1-I2"], "(O)")
var("V1.2", "S1", ["D2.1"], "delete", "a sets v through j at b without '∀k ≠ j: L_k(a,b) = L_k(1,b)'", "yes", [], "Roles")
var("V1.3", "S1", ["D2.4"], "weaken", "Obs(o,m) := {a ∈ Alt_j : L_asg(m)(a,b) = L_asg(m)(1,b) ∀b} (reading R-i)", "yes", [], "Roles")
var("V1.4", "S1", ["D3.3"], "swap", "Ident's contract clause: ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0)", "yes", ["S108-1-I4"], "Respects")
var("V1.5", "S1", ["D3.4"], "delete", "ρ_p ∈ {selected, constructed}; a contract with neither history is no question's contract", "nearest reading", ["S108-1-I5"], "ProvC", ["L155.s2", "L155.s5"])
var("V1.6", "S1", ["D3.6"], "strengthen", "BadTarget(p) ∨ BadReq(p) ⇒ ∀ℰ ¬Acc(ℰ,p) (+ a new sentence)", "no (flagged: out of scope in effect; adds prose, S40)", [], "Defects")
var("V1.7", "S1", ["D0.2"], "other", "Excl(Σ) := (A×B) ∖ C, defined; Stated(C,Σ) always holds", "no (flagged: rewrites D3.5 [FROZEN] in effect)", [], "Σ")
var("V1.8", "S1", ["D2.6"], "weaken", "Slc_j := Alt_j", "yes", [], "Roles")
var("V2.1", "S2", ["D6.4"], "weaken", "NC2(ℰ) :⟺ ∃(a,b) ∈ C: Contrast(E;x)", "yes", [], "Dep", ["L255.n2"])
var("V2.2", "S2", ["D6.4"], "strengthen", "NC2(ℰ) :⟺ ∃(a,b) ∈ C, d ∈ Γ: Contrast(E;x) ∧ Lost(E,{d};x)", "yes", [], "Dep")
var("V2.3", "S2", ["D6.4"], "strengthen", "NC2(ℰ) :⟺ ∃(a,b) ∈ C with a ≠ 1, ∅ ≠ G ⊆ Γ: Contrast(E;x) ∧ Lost(E,G;x)", "yes", [], "Dep")
var("V2.4", "S2", ["D6.7"], "strengthen", "Acc(ℰ) :⟺ F1 ∧ F2 ∧ A ∧ NC0 ∧ NC1 ∧ NC2 ∧ NonVacuous (round 3's (E); Slot 'every')", "yes", [], "(E)", ["L261.n1"])
var("V2.5", "S2", ["D12.1"], "weaken", "Sel: H ⊆ C finite (H = ∅ allowed)", "yes", [], "Sel", ["L195.s2", "L195.s3", "L195.n4", "L195.s6"])
var("V2.6", "S2", ["D8.2"], "weaken", "Conf(ℰ,ℰ′;a,b) only for (a,b) ∈ C", "yes", [], "Conf", ["L315.n2"])
var("V2.7", "S2", ["D8.5"], "weaken", "ConfCl: the first disjunct (through the answer) alone", "yes", [], "ConfCl", ["L315.n11"])
var("V2.8", "S2", ["D9.8"], "swap", "Out_j('Acc(ℰ)') :⟺ ∃α ∈ X_j('Acc(ℰ)') with Acc(ℰ) ∈ Uses(α)", "no (flagged: names L315.s7 [FROZEN]; its trace is V4.4's reading)", [], "OutCand", ["L315.s6", "L315.s7"])
var("V3.1", "S3", ["D9.7"], "delete", "RO(α,φ) :⟺ Incons(φ, concl(α))", "yes", [], "RO", ["L397.n14", "L397.s16"])
var("V3.2", "S3", ["D9.4"], "delete", "Live_j(d;u) :⟺ d ∈ Accepted_j(ξ)", "yes", [], "Live")
var("V3.3", "S3", ["D9.6"], "delete", "Usable_j(α) :⟺ ∀u ∈ steps(α) Usable_j(u) (a premise alone usable by every j)", "yes", [], "(K2)")
var("V3.4", "S3", ["D13.3"], "strengthen", "ExplUse(o,c) :⟺ UsesClaim(o,'Acc(ℰ)') ∧ Acc(ℰ)", "yes (the reply's chain Build → CT only under S108-3-I2)", ["S108-3-I1", "S108-3-I2", "S108-3-I5"], "ExplUse")
var("V3.5", "S3", ["D13.8"], "delete", "Episode(h′) :⟺ h′ ⊆ h is a subhistory", "yes", [], "Episode")
var("V3.6", "S3", ["D15.8"], "delete", "𝒯 := {t : Θ admits t}", "nearest reading", ["S108-3-I3", "S108-3-I4"], "𝒯pop", ["L481.s3"])
var("V3.7", "S3", ["D11.4"], "delete", "ActRoute without '∃(x,x′) ∈ K: val_r differs'", "yes", ["S108-3-I6"], "ActRoute")
var("V3.8", "S3", ["D14.7"], "delete", "CreateEx without CreativeCriticalEpisode(s,Δ,h,e)", "yes", [], "(EX)", ["L445.s1"])
var("V4.1", "S4", ["D16.XV"], "strengthen", "Expl :⟺ Acc ∧ ¬Dec(t) ∧ ¬Slot_C(ℰ) (Slot 'every')", "yes", ["S108-4-I1", "S108-4-I9"], "DefeatConds")
var("V4.2", "S4", ["D16.XV"], "delete", "Expl :⟺ Acc (the rule Acc ∧ Dec ⇒ ¬Expl deleted)", "yes", ["S108-4-I2", "S108-4-I9"], "DefeatConds")
var("V4.3", "S4", ["D16.XV"], "swap", "¬Dec(t) → ¬Dec(t) ∧ (Sel(t) ∨ CT(t)), in (Suff) and in being an explanation", "nearest reading (at the holding)", ["S108-4-I3", "S108-4-I9"], "DefeatConds")
var("V4.4", "S4", ["D16.XV"], "swap", "'not using (E)' at the instance: Acc(ℰ) ∉ Uses(α)", "yes", ["S108-4-I4"], "DefeatConds")
var("V4.5", "S4", ["D16.XV"], "weaken", "(Nec)'s exposure: ∀t′ ¬Faithful_C(t′: D → E) (C only)", "nearest reading (a searched class)", ["S108-4-I5"], "DefeatConds", ["L538.s1"])
var("V4.6", "S4", ["D16.4"], "delete", "𝔈_Θ without 'δ the designation of Q in c'", "nearest reading (searched witnesses)", ["S108-4-I6"], "𝔈", ["L497.s1"])
var("V4.7", "S4", ["D16.3"], "delete", "Enable :⟺ Θ admits χ ∧ χ an enabling condition (NQB dropped)", "nearest reading, on a toy only", ["S108-4-I7"], "Enable")
var("V4.8", "S4", ["D12.9", "D16.XV"], "weaken", "Underdet :⟺ ∃t′ ∈ 𝒯: value_t′(a,b) ≠ value_t(a,b); (Prov)(i) through Underdet", "yes", ["S108-4-I8"], "Underdet", ["L572.s2", "L574.n4", "L576.s1", "L576.s4"])

# ---------------------------------------------------------------- the computed effect on the explanation definition
# (section files: §9 of sections 1, 3, 4; 'Findings in brief' and §2, §5, §6 of section 2). Counts: worked cases;
# generated SMALL / SMALL value maps / proper / MID (section 2: single / value maps / MID proper).
EFFECT = collections.OrderedDict([
    ("V1.1", ("out 15 of 27 worked (E1 forward C1–C3, E_rev on C_id, M13, E5 ×2, E8, E9 ×2, the two-part sign, …); in ℰ_bv (S108-1-I1 (i)); generated in 16 / 13 / 1 / 19, out 199 / 203 / 30 / 358", "moves exactly where Acc moves", "(as now)", "Dec moves alone through Sel's fidelity (1,360 / 1,211 / 106 / 2,212), never moving Account ∧ ¬Dec(t) alone", "21 claims")),
    ("V1.2", ("0", "0", "(as now)", "Set_v, asg, Prod (549 of 17,280), families; FC06, FC09 (L347.s2 [FROZEN])", "5 claims")),
    ("V1.3", ("0", "0", "(as now)", "families (57 of 17,280)", "0 claims")),
    ("V1.4", ("0", "0", "(as now)", "Ident's contract clause (1,113 of 17,280; C_id no longer an identification contract)", "3 claims")),
    ("V1.5", ("out: every candidate of a question with no recorded contract history, under S108-1-I5: 22 of 22 worked with Acc T; generated 961 / 886 / 221 / 1,674; with ρ_p recorded by hand: 0", "moves exactly where Acc moves", "(as now)", "reads nothing of (D, C, Q) but ρ_p", "15 claims")),
    ("V1.6", ("not computed (flagged)", "not computed", "not computed", "–", "–")),
    ("V1.7", ("not computed (flagged); I85's default scope already equals V1.7's formula on every question the program builds", "not computed", "(as now)", "–", "–")),
    ("V1.8", ("0", "0", "(as now)", "rule and measurement families emptied (2,413 and 169 of 17,280 → 0); idle on the pole", "1 claim")),
    ("V2.1", ("in: generated 57 / 74 / 8; worked 0", "the same movers (Con, Sel histories)", "(as now)", "routes: ∅ ∈ S for 63; 120 routes with no critical block", "0 claims")),
    ("V2.2", ("out: generated 23 / 20 / 4; the built L307 case; worked 0", "the same", "(as now)", "every route has a critical singleton; L307's S realized by none (17 → 0)", "0 claims")),
    ("V2.3", ("out: generated 253 / 213 / 65 (every account on {1}×B: 168 → 0); E_rev and E_fwd on C_id", "the same (4 worked (case, history))", "(as now)", "–", "2 claims")),
    ("V2.4", ("out: 11 worked (E_enc C1, C2; 'p because p'; M1–M3; the one-part sign; ℰ_myth1; the hand-turned vane; E8's identity candidate; E_rev τ′); generated 972 / 776 / 301 of 1,027 / 847 / 310", "the same (22 worked (case, history))", "(as now)", "Bearing (D9.10) of K1's criticism; (E) reads D6.3's quantifier again", "6 claims + 2 parts")),
    ("V2.5", ("0", "in: every account on a history with nothing tried and no earlier representation: 28 of 28 worked; generated 1,027 / 847 / 310; FC30.new1 (e) in, (d) stays out", "(as now)", "FC77 counterexample", "2 claims")),
    ("V2.6", ("0", "0", "(as now)", "rivalry and kind ii: 310 of 310 kind-ii pairs lose rivalry; 492 kind-i pairs lose outside-C conflicts", "1 claim")),
    ("V2.7", ("0", "0", "(as now)", "ConfCl: 410 of 1,822 lost", "1 claim")),
    ("V2.8", ("not computed (flagged); its reading computed as V4.4", "not computed", "(as now)", "–", "–")),
    ("V3.1", ("0", "0", "(as now)", "Out_j: 1,677 of 9,600 F → T; (Suff)/(Nec) defeat sets by acceptance alone", "5 claims")),
    ("V3.2", ("0", "0", "(as now)", "usability 8,983 T → F; problems grow (FC47.new1)", "7 claims")),
    ("V3.3", ("0", "0", "(as now)", "usability 2,621 F → T; Out_j 703; ruling out no longer depends on j for premises alone", "2 claims")),
    ("V3.4", ("0", "0 with D12.2 as written; under S108-3-I2: out 122 / 93 / 36 / 200 (claim used on the widest contract), and in and out on provenance chains (Dec F → T 546, T → F 92, T′)", "(as now)", "Build T → F on every use of an account failing (E) (L403.s3 [FROZEN])", "1 claim")),
    ("V3.5", ("0", "0 under D12.2's cut T′ (and T) for every candidate meeting (E); in, in the tag encoding: 22 of 27 worked, 1,013 / 881 / 232 / 1,670; under the rejected cut K: 5,118 chains", "(as now)", "Episode; Con at holdings whose t is not held", "1 claim")),
    ("V3.6", ("0", "in (S108-3-I4): 22 of 27 worked ('Sel-parts'); generated 1,013 / 881 / 232 / 1,670", "(as now)", "pairs newly underdetermined 1,141 / 859 / 469 / 2,577", "0 claims (text only)")),
    ("V3.7", ("0", "0", "(as now)", "ActRoute 1,436 of 5,724 F → T; ProducedBy, ProducesVia", "1 claim")),
    ("V3.8", ("0", "0", "(as now)", "CreateEx 7,086 of 1,929,216 valuations F → T", "1 claim")),
    ("V4.1", ("0", "0", "out: 10 of 29 worked (the one-part sign, E_enc, 'p because p', M1–M3, the hand-turned vane, E8's identity candidate, E_rev τ′ on C_H); generated 941 of 1,019 (MID 1,590 of 1,686)", "(Suff) fails by definition unless its antecedent co-varies", "1–2 claims")),
    ("V4.2", ("0", "0", "in: 24 of 24 worked under a declared or unrecorded history; the student's declared copy; a link no pair tried; CT8's R2, R4; FC-E 7; CT 4; generated 1,019 (MID 1,686)", "FC30.new1 (c), FC23.new2 (f) fail", "2 claims")),
    ("V4.3", ("0", "0", "out, only at holdings reached by a transfer: reading (a) 24 + 24 worked, 1,019 + 1,019 generated; (b) 24, 1,019; (c) 0", "D12.4's inherited provenance no longer enough", "0 claims (text only)")),
    ("V4.4", ("0", "0", "(as now)", "(Suff) defeat set grows 1,019 (Con), 1,019 (Sel); (Nec) 3,979", "0 claims")),
    ("V4.5", ("0", "0", "(as now)", "(Nec) exposure +4 worked, +2,138 generated, all with Acc F", "0 claims")),
    ("V4.6", ("0", "0", "(as now)", "𝔈_Θ +1 of 17,280, +2 of 25,920 searched witnesses", "0 claims")),
    ("V4.7", ("0", "0", "(as now)", "toy only: UU F → T on 217 of 484", "0 claims")),
    ("V4.8", ("0", "0", "(as now)", "(Prov)(i) satisfiable: 1,647 of 9,768 wide populations; 0 of FC80's own", "0 claims (text only)")),
])

# ---------------------------------------------------------------- the edges: each source row mapped to items
# Each value: a list of parts. A part: {"to": [...], "kind": optional override, "standing": optional override,
# "condition": optional, "note": optional}. '#' notes say why a row is split or re-kinded.
L4 = ["L17.n2", "L49.n3", "L61.n2", "L69.n3"]          # the four sentences writing Account(ℰ) ∧ ¬Dec(t)
IND = "independent of"
M = {
    # section 1
    "S1#0": [{"to": ["D4.4"]}], "S1#1": [{"to": ["D5.2"]}], "S1#2": [{"to": ["L233.s1"]}], "S1#3": [{"to": ["L556.n2"]}],
    "S1#4": [{"to": ["FC17", "FC18"]}], "S1#5": [{"to": ["X:(F1)"]}], "S1#6": [{"to": ["X:(E)", "X:Expl"]}],
    "S1#7": [{"to": ["D12.1", "X:Dec"]}], "S1#8": [{"to": ["D13.4", "D13.5"]}], "S1#9": [{"to": ["D12.5"]}],
    "S1#10": [{"to": ["D7.2", "D7.3", "D7.4"]}], "S1#11": [{"to": ["X:(E)", "FC72.new2"]}],
    "S1#12": [{"to": ["FC99", "FC101"], "note": "Arguments 7 and 9 (lines L606, L616) through their claims: FC99 (the account fails already on C), FC101 (b)"}], "S1#13": [{"to": ["X:(E)"]}],
    "S1#14": [{"to": ["L103.s2"]}], "S1#15": [{"to": ["D2.2"]}], "S1#16": [{"to": ["D2.5"]}], "S1#17": [{"to": ["D2.6"]}],
    "S1#18": [{"to": ["D2.4"]}], "S1#19": [{"to": ["E1"]}], "S1#20": [{"to": ["FC27.new1"]}], "S1#21": [{"to": ["D2.6", "L57.s1"]}],
    "S1#22": [{"to": ["X:(E)", "X:Expl"], "kind": IND, "note": "no conjunct of (E) moves (0 of 61,914 generated)"},
              {"to": ["D3.3"], "kind": "moves", "note": "Prod(p) moves on 549 of 17,280 (the respect 'production')"}],
    "S1#23": [{"to": ["L347.s2"]}], "S1#24": [{"to": ["L119.n8"]}],
    "S1#25": [{"to": ["L123.n1", "FC2.new1", "FC4.new1", "FC07", "FC08"], "note": "lines L109, L123, L127 through their claims (L123.n1 the one sentence on L123): FC2.new1, FC4.new1, FC07 → counterexample; FC08's witness lost"}],
    "S1#26": [{"to": ["FC-E3"]}], "S1#27": [{"to": ["L124.s1", "L125.s1"]}], "S1#28": [{"to": ["L123.n1", "D4.6"]}],
    "S1#29": [{"to": ["X:(E)", "X:Expl"], "kind": IND}], "S1#30": [{"to": ["L151.s1"]}], "S1#31": [{"to": ["L151.s2"]}],
    "S1#32": [{"to": ["E1", "L271.s2", "L325.n6"]}], "S1#33": [{"to": ["FC28", "FC28.new2", "FC28.new1"]}],
    "S1#34": [{"to": ["X:(E)", "X:Expl"], "kind": IND, "note": "Acc 0 moves anywhere"},
              {"to": ["D3.3"], "kind": "moves", "note": "what meeting (E) on C_id answers: C_id no longer an identification contract"}],
    "S1#35": [{"to": ["D3.3"]}], "S1#36": [{"to": ["L155.s2", "L155.s5"]}], "S1#37": [{"to": ["L155.s6", "D3.1"]}],
    "S1#38": [{"to": ["D13.8"]}], "S1#39": [{"to": ["D16.4"]}], "S1#40": [{"to": ["L544.s1"]}], "S1#41": [{"to": ["E8"]}],
    "S1#42": [{"to": ["X:(E)", "X:Expl"], "condition": "under S108-1-I5 (no recorded contract history = declared); 0 moves with ρ_p recorded"}],
    "S1#43": [{"to": ["X:(E)", "X:Expl"], "condition": "under S108-1-I5"}],
    "S1#44": [{"to": ["FC34", "FC74"]}],
    "S1#45": [{"to": ["L161.s1", "L161.s2", "L161.s3", "D6.6"]}], "S1#46": [{"to": ["X:(Suff)", "X:(Nec)", "FC106"]}],
    "S1#47": [{"to": ["X:Expl"]}], "S1#48": [{"to": ["D3.5", "L43.s4", "L159.s1"]}], "S1#49": [{"to": ["D6.6"]}],
    "S1#50": [{"to": ["L317.s15"], "kind": IND}], "S1#51": [{"to": ["X:NonVacuous"]}],
    "S1#52": [{"to": ["L347.s2"]}], "S1#53": [{"to": ["L57.s1"]}], "S1#54": [{"to": ["D4.6", "L123.n1"]}],
    "S1#55": [{"to": ["X:(E)", "X:Expl"], "kind": IND}],
    "S1#56": [{"to": ["E1"], "kind": IND, "note": "V1.8 idle on the pole: Slc_j = Alt_j there already"}],
    "S1#57": [{"to": ["FC-E3"]}],
    # section 2
    "S2#0": [{"to": ["X:Dependence", "X:(E)", "X:Expl"]}], "S2#1": [{"to": ["D7.2", "L289.s1"]}], "S2#2": [{"to": ["L275.n1"]}],
    "S2#3": [{"to": ["L311.s2"]}],
    "S2#4": [{"to": ["L299.s1"], "standing": "computed", "note": "'constrains' computed: realizations 20 → 1"},
             {"to": ["X:(E)"], "kind": "moves", "standing": "contradicted", "note": "'such a candidate now fails (E)' contradicted: one generated candidate meets (E) with a block critical and no singleton of it critical"}],
    "S2#5": [{"to": ["D10.4", "D10.6"]}],
    "S2#6": [{"to": ["L329.s3"], "standing": "contradicted", "note": "identification reads no (E); FC57, FC58, FC28's Ident unchanged"},
             {"to": ["X:(E)"], "kind": "moves", "standing": "computed", "note": "no account on a {1}×B contract: 168 → 0 of 1,953"},
             {"to": ["L331.s2", "E2"], "standing": "claimed only", "note": "settle: the two balances built as a question on {1}×B with a candidate"}],
    "S2#7": [{"to": ["D3.3"]}], "S2#8": [{"to": ["L253.s1"]}],
    "S2#9": [{"to": [], "note": "not an item: the owner's decision S45 (with S44); goes to the candidate list"}],
    "S2#10": [{"to": ["X:(E)", "D9.10"]}],
    "S2#11": [{"to": ["X:Expl", "X:(Suff)"], "standing": "computed", "note": "Expl shrinks: 22 (case, history) T → F; 1,944 generated; ℰ_one in no defeat set of (Suff) (it fails (E))"},
              {"to": ["X:(Nec)"], "standing": "claimed only", "note": "the (Nec) attack list is computed by no claim that moves"}],
    "S2#12": [{"to": ["L195.s1"]}], "S2#13": [{"to": ["L211.s3"], "kind": "blocks", "note": "in effect"}],
    "S2#14": [{"to": ["X:Dec", "X:Expl", "X:(Suff)"]}], "S2#15": [{"to": ["L315.s1", "L317.s6"]}],
    "S2#16": [{"to": ["X:(E)"], "kind": IND, "standing": "computed", "note": "0 Acc changes in every population"},
              {"to": ["D10.1", "D10.4"], "kind": "moves", "standing": "computed", "note": "no kind ii remains, so ETV_j holds of no candidate"},
              {"to": ["X:(Nec)"], "kind": "moves", "standing": "claimed only", "note": "no claim computes an attack on (Nec) through easy to vary"}],
    "S2#17": [{"to": ["L315.s12"], "kind": "blocks", "note": "in effect; where the answer itself is the excluded motion (FC53 (b)) the conflict stays"}],
    "S2#18": [{"to": ["D8.4"]}], "S2#19": [{"to": ["D8.6"]}], "S2#20": [{"to": ["D16.XV"]}], "S2#21": [{"to": ["X:(Suff)"]}],
    "S2#22": [{"to": ["L309.s1"], "kind": IND, "note": "L309.s1 stays realized under V2.1 (the reply left it open)"}],
    "S2#23": [{"to": ["D7.3", "L293.s1", "L293.s2"]}], "S2#24": [{"to": ["L313.s2"]}], "S2#25": [{"to": ["L307.s1"]}],
    "S2#26": [{"to": ["L313.n3"]}], "S2#27": [{"to": ["D7.3"]}], "S2#28": [{"to": ["X:Dependence", "X:(E)", "X:Expl"]}],
    "S2#29": [{"to": ["E8", "E1", "X:(E)"]}], "S2#30": [{"to": ["D6.10"]}], "S2#31": [{"to": ["D5.5", "X:(F2)"]}],
    "S2#32": [{"to": ["D8.3"]}], "S2#33": [{"to": ["L317.n8", "D10.6"]}],
    "S2#34": [{"to": ["D8.2", "D8.3", "D10.2"], "kind": IND}], "S2#35": [{"to": ["X:(E)"], "kind": IND}],
    "S2#36": [{"to": ["D6.3"]}], "S2#37": [{"to": ["L195.n4", "D12.1"]}],
    "S2#38": [{"to": [], "kind": IND, "note": "no claim of the suite (FC21–FC40) separates D6.4 from V2.2: a gap"}],
    "S2#39": [{"to": [], "kind": IND, "note": "no claim of the suite separates D6.4 from V2.1: a gap"}],
    # section 3
    "S3#0": [{"to": ["L397.s5"]}], "S3#1": [{"to": ["L8.s3"]}],
    "S3#2": [{"to": ["X:(Suff)", "X:(Nec)"], "standing": "computed", "note": "j accepting ¬Expl(ℰ) alone: an argument not using (E) rules out Expl(ℰ) F → T; the pole's forward candidate in Def(L536) F → T; (Nec)'s defeat by accepting Expl(ℰ) alone F → T"},
             {"to": ["X:(E)", "X:Expl"], "kind": IND, "standing": "computed", "note": "0 moves on 27 worked, FC-E, CT, 61,900 generated"}],
    "S3#3": [{"to": ["L397.n14", "L397.s16"]}], "S3#4": [{"to": ["D9.9", "FC71"]}], "S3#5": [{"to": ["FC60", "E3"]}],
    "S3#6": [{"to": ["FC72.new2"]}], "S3#7": [{"to": ["D9.8", "D10.1"]}], "S3#8": [{"to": ["L389.s1"]}],
    "S3#9": [{"to": ["D9.8"], "standing": "computed", "note": "fewer usable, fewer ruled out: 8,983 usabilities T → F, 26 Out_j T → F"},
             {"to": ["D10.1"], "standing": "contradicted", "note": "'fewer problems' contradicted: with fewer ruled out, problems grow (FC47.new1)"}],
    "S3#10": [{"to": ["L393.n2"]}], "S3#11": [{"to": ["L369.s3", "FC68"]}], "S3#12": [{"to": ["D9.9", "FC71"]}],
    "S3#13": [{"to": ["D18.1", "FC69"]}], "S3#14": [{"to": ["FC47", "FC53"]}], "S3#15": [{"to": ["L397.s5"]}],
    "S3#16": [{"to": ["L393.n2"]}], "S3#17": [{"to": ["X:(Suff)", "X:(Nec)", "D10.1"]}], "S3#18": [{"to": ["FC72.new1"]}],
    "S3#19": [{"to": ["L403.s3"]}],
    "S3#20": [{"to": ["X:Dec", "D12.2", "X:Expl"], "standing": "contradicted", "note": "D12.2 as written: CT reads Prepares, not ExplUse; 0 Dec moves"},
              {"to": ["X:Dec", "D12.2", "X:Expl"], "standing": "computed", "condition": "under S108-3-I2 (CT asks ExplUse)", "note": "the reply's case T → F; generated 122 / 93 / 36 / 200 out (widest-contract claim)"}],
    "S3#21": [{"to": ["L526.s11"]}], "S3#22": [{"to": ["D13.6", "D14.7"]}],
    "S3#23": [{"to": ["D12.1", "X:Dec"], "condition": "under S108-3-I2"}], "S3#24": [{"to": ["L55.n3"]}],
    "S3#25": [{"to": ["X:Dec", "D12.2", "X:Expl"], "standing": "contradicted", "note": "D12.2's cut T′ (and T): no candidate meeting (E) moves; the record clause idle where t is held"},
              {"to": ["X:Dec", "D12.2", "X:Expl"], "standing": "computed", "condition": "in the tag encoding, and under the rejected cuts K, U", "note": "tag: 22 of 27 worked in, 1,013 / 881 / 232 / 1,670 generated; K: 5,118 chains"}],
    "S3#26": [{"to": ["D12.2"]}], "S3#27": [{"to": ["FC84.new1", "FC84.new2"]}],
    "S3#28": None,  # 'blocks: none found' (a search): recorded as a finding with no edge
    "S3#29": [{"to": ["D12.1"]}],
    "S3#30": [{"to": ["D12.1", "X:Dec", "X:Expl"], "standing": "computed", "condition": "on S108-3-I4 (parts := E's components; stated construction := t's own)"},
              {"to": ["FC80"], "standing": "claimed only", "note": "FC80 as built does not move: its populations state no construction; settle: a stated construction in FC80's generator"}],
    "S3#31": [{"to": ["L481.s3"]}], "S3#32": [{"to": ["FC30.new1"], "kind": IND}], "S3#33": [{"to": ["L375.s2"]}],
    "S3#34": [{"to": ["D14.3", "D14.6"], "standing": "computed", "note": "ProducedBy F → T on 685 of 1,460 circuits; ProducesVia on 952 of 2,860"},
              {"to": ["D9.11"], "standing": "claimed only", "note": "UsesReason is supplied by hand in the program (I47); settle: circuits with a represented objection and role maps"},
              {"to": ["X:(E)"], "kind": IND, "standing": "computed", "note": "Acc 0 moves anywhere"}],
    "S3#35": None,  # 'blocks: none (L443.s3 …)': a finding with no edge; see S3#39
    "S3#36": [{"to": ["L443.n1"]}],
    "S3#37": [{"to": ["D18.1"], "standing": "computed", "note": "(EX) no longer reaches Crit (FC32.new1 (f))"},
              {"to": ["L628.n2"], "standing": "claimed only", "note": "the hypothesis CreativeCriticalEpisode becomes surplus, not false; the owner's part (S47 with S41 Q6) not settled by computation"}],
    "S3#38": [{"to": ["D14.7"], "standing": "computed", "note": "CreateEx F → T on 7,086 of 1,929,216 valuations; T → F 0"},
              {"to": ["X:(E)", "X:Expl", "X:(Suff)", "X:(Nec)"], "kind": IND, "standing": "computed", "note": "Acc, Dec, Account ∧ ¬Dec(t) and the defeat sets: 0 moves"}],
    "S3#39": [{"to": ["L528.s2", "L528.s3"]}],
    # section 4
    "S4#0": [{"to": ["X:Expl", "X:(Suff)", "D18.1"]}], "S4#1": [{"to": L4}],
    "S4#2": [{"to": ["L269.n1", "L269.s2", "L269.s3", "L271.s1", "L271.s2", "L273.n1", "L275.n1", "L275.s2", "L277.s1", "L277.s2", "L277.s3", "L277.s4"], "note": "line-level: L269–L277"}],
    "S4#3": [{"to": ["FC30.new1"]}], "S4#4": [{"to": ["FC23.new2"]}], "S4#5": [{"to": ["FC23.new3", "FC25.new2"]}],
    "S4#6": None,  # 'blocks: none FROZEN': a finding with no edge
    "S4#7": [{"to": ["D6.3"]}], "S4#8": [{"to": ["D6.3"]}], "S4#9": [{"to": ["X:(Suff)", "L61.n2", "L536.s1"]}],
    "S4#10": [{"to": ["E1", "D6.3"], "note": "the pole's forward candidate on C2 stays an explanation under 'every' (the reply's trace had it out); out only under 'some'"}],
    "S4#11": [{"to": ["D18.2"]}], "S4#12": [{"to": ["X:Expl"]}], "S4#13": [{"to": L4 + ["X:(Suff)", "FC30.new1"]}],
    "S4#14": [{"to": ["FC30"]}], "S4#15": [{"to": ["FC30.new1", "FC23.new2"], "note": "the owner's condition Acc ∧ Dec ⇒ ¬Expl (S41 Q2)"}],
    "S4#16": [{"to": ["CT8"]}], "S4#17": [{"to": ["D12.3", "D12.4"]}], "S4#18": [{"to": ["X:Expl", "X:(Suff)"]}],
    "S4#19": [{"to": L4 + ["FC25.new2"]}], "S4#20": [{"to": ["D12.4"]}], "S4#21": [{"to": ["D12.2"]}], "S4#22": [{"to": ["D18.2"]}],
    "S4#23": [{"to": ["D9.6", "D9.7", "D9.8"]}],
    "S4#24": [{"to": ["X:(Suff)", "X:(Nec)"], "standing": "computed", "note": "(Suff): FC30.new1 (h)'s ℰ_fwd and E9's t1∘ψ enter (instance T, symbol F), declared ones do not; generated 1,019 (Con), 1,019 (Sel); (Nec): 3,979 exposed now"},
              {"to": ["X:(E)", "X:Expl"], "kind": IND, "standing": "computed", "note": "Acc and being an explanation: 0 moves; suite: 0 claims move"}],
    "S4#25": [{"to": ["L556.s3"], "note": "the reply's nearest FROZEN item; a search finds no FROZEN item holding 'not using' or Uses"}],
    "S4#26": [{"to": ["X:(Nec)"], "note": "V4.4 × V4.5: 2,138 generated enter (Nec)'s defeat set only with both on"}],
    "S4#27": [{"to": ["L606.s4", "FC99"]}], "S4#28": [{"to": ["L538.s1", "FC30.new1", "E5"]}], "S4#29": [{"to": ["L538.s2"]}],
    "S4#30": [{"to": ["X:(Nec)"]}], "S4#31": [{"to": ["D5.3"]}],
    "S4#32": [{"to": ["D16.4"], "standing": "computed", "note": "1 of 17,280 (SMALL) and 2 of 25,920 (MID) searched witnesses meet (E) only with a non-designated δ; membership over every (p, t, Γ) not computed"}, {"to": ["X:(E)"], "kind": IND, "standing": "computed", "note": "(E) unchanged"}],
    "S4#33": [{"to": ["E1"]}],
    "S4#34": [{"to": ["L495.s1"], "condition": "on the toy only (S108-4-I7); the program computes no barrier, Enable or UU"}],
    "S4#35": [{"to": ["D16.4"]}], "S4#36": [{"to": ["D12.1", "D12.2", "D12.5", "D15.8"]}],
    "S4#37": [{"to": ["L528.s1", "L528.s2", "L528.s3", "L528.s4", "D16.5"]}],
    "S4#38": [{"to": ["D12.1", "L574.s2"]}], "S4#39": [{"to": ["D16.XV"]}],
    "S4#40": [{"to": ["L572.s2", "L574.n4", "L576.s1", "L576.s4"]}], "S4#41": [{"to": ["FC80"]}],
    "S4#42": [{"to": ["D16.XV"], "note": "its own note '(Prov)(i) unsatisfiable by definition (FC80 (a))': satisfiable under V4.8"}], "S4#43": [{"to": ["FC80"]}],
}

# findings with no edge (rows whose content is 'none found')
NO_EDGE = {
    "S3#28": "V3.6 blocks no FROZEN sentence: none states the parts bound (search of the template); L481.s3 [S3] is varied with it",
    "S3#35": "V3.8 makes no FROZEN sentence about (EX) false (L443.s3 names O_ex only); but L528.s2–s3 [FROZEN] change with it (S3#39)",
    "S4#6": "V4.1: in D18.1 the only node gaining an edge is DefeatConds (D16.XV, S4); no FROZEN definition reaches Slot",
}

# summary edges from the files' own summary tables, where no row gives the effect on the explanation definition
SUMMARY = [
    ("V1.2", "S1 §9", IND, ["X:Dec"], "Dec(t) (Sel-history) 0 moves (§3)"),
    ("V1.3", "S1 §9", IND, ["X:Dec"], "0 moves (§3)"),
    ("V1.4", "S1 §9", IND, ["X:Dec"], "0 moves (§3)"),
    ("V1.8", "S1 §9", IND, ["X:Dec"], "0 moves (§3)"),
    ("V2.2", "S2 Findings, §5", "moves", ["X:Dependence", "X:(E)", "X:Expl"], "T → F on 23 / 20 / 4 generated, none F → T; the built L307 case T → F; Account ∧ ¬Dec(t): the same movers"),
    ("V2.4", "S2 Findings, §2", "moves", ["X:Expl"], "22 worked (case, history) T → F; 1,944 generated"),
    ("V2.6", "S2 Findings", IND, ["X:Expl"], "Account ∧ ¬Dec(t) unchanged"),
    ("V2.7", "S2 Findings", IND, ["X:Expl"], "Account ∧ ¬Dec(t) unchanged"),
    ("V3.2", "S3 §9", IND, ["X:(E)", "X:Expl"], "0 moves (§3, §6.1)"),
    ("V3.3", "S3 §9", IND, ["X:(E)", "X:Expl"], "0 moves (§3, §6.1)"),
    ("V3.4", "S3 §9", IND, ["X:(E)"], "Acc 0 moves (§3, §6.1)"),
    ("V3.5", "S3 §9", IND, ["X:(E)"], "Acc 0 moves"),
    ("V3.6", "S3 §9", IND, ["X:(E)"], "Acc 0 moves"),
    ("V3.7", "S3 §9", IND, ["X:Expl"], "Account ∧ ¬Dec(t) 0 moves"),
    ("V4.1", "S4 §9", IND, ["X:(E)", "X:Dec"], "Acc and Account ∧ ¬Dec(t): 0 moves (worked, scripts, 17,280 generated, suite)"),
    ("V4.2", "S4 §9", IND, ["X:(E)", "X:Dec"], "Acc and Dec: 0 moves"),
    ("V4.3", "S4 §9", IND, ["X:(E)", "X:Dec"], "Acc and Dec: 0 moves"),
    ("V4.5", "S4 §9", IND, ["X:(E)", "X:Expl"], "0 moves"),
    ("V4.6", "S4 §9", IND, ["X:Expl"], "0 moves"),
    ("V4.7", "S4 §9", IND, ["X:(E)", "X:Expl"], "0 moves"),
    ("V4.8", "S4 §9", IND, ["X:(E)", "X:Expl"], "0 moves"),
]

KINDS = {"blocks": "blocks", "constrains": "constrains", "changes with": "changes with", "moves": "moves",
         "changes with (the reply's open edge)": "changes with", "moves (trace)": "moves",
         "blocks (in effect)": "blocks", "keeps": IND, "independent of": IND, "no claim separates": IND}


def settle_text(ev):
    m = re.search(r"(?:—\s*)?\b(?:Settled by|to settle|what would settle it|settle)\b\s*:?\s*(.*)$", ev or "", flags=re.I)
    return m.group(1).strip() if m else ""


def norm_rows():
    rows = []
    for s in (1, 2, 3, 4):
        d = json.loads(SEC[s].read_text(encoding="utf-8"))
        for j, e in enumerate(d["edges"]):
            key = f"S{s}#{j}"
            if s == 1:
                named = e["named_by"] == "reply"
                st0 = e["standing"]
                ev = e.get("evidence", "")
                settle = e.get("what_would_settle") or (settle_text(ev) if st0.startswith("not settled") else "")
            elif s == 2:
                named = bool(e["named_by_reply"])
                st0 = e["standing"]
                ev = e.get("what_shows_it", "") + ((" — note: " + e["note"]) if e.get("note") else "")
                settle = e.get("what_would_settle_it", "")
            elif s == 3:
                named = bool(e["named_by_reply"])
                st0 = e["standing_class"]
                ev = e.get("evidence", "")
                settle = e.get("what_would_settle") or settle_text(ev)
            else:
                named = e["named_by"] == "reply"
                st0 = e["standing"]
                ev = e.get("evidence", "")
                settle = settle_text(ev) if st0.startswith("not settled") else ""
            base = {"computed": "computed", "added": "computed", "contradicted": "contradicted",
                    "not settled by computation": "claimed only", "computed in part": "split"}[st0]
            rows.append((s, j, key, e, named, base, st0, ev, settle))
    return rows


# the reply's own reason, from the tabulation §4, where a section file's row has none
REPLY_WHY = {
    "S1#38": "episode records and question-finding quantify over contracts that must now be non-declared (tabulation §4)",
    "S1#39": "as S1#38 (tabulation §4)", "S1#40": "as S1#38 (tabulation §4)",
    "S1#45": "defective questions stay questions; NonVacuous keeps BadBaseline, the variant adds the other two beside it",
    "S1#46": "the defeat sets would quantify over non-defective p; FC106's untested parts become testable",
    "S1#47": "gains the question's non-defect beside Account ∧ ¬Dec(t)",
    "S1#48": "'Σ is a declared input naming Excl(Σ)'; the stated-scope requirement and grievance 4's answer fall",
    "S1#49": "NonVacuous keeps its form; its second conjunct becomes vacuous",
    "S1#50": "the theory hangs together; L317.s15 is safe (narrowing still makes a new question)",
    "S1#51": "silently narrowed contracts newly meet (E)",
}

# the candidate list (rule 7), mirrored from 'S108 Part A - candidate definitions of explanation.md'
CANDIDATES = [
    {"variant": "V1.1", "moves": "(E)", "flagged": True, "decisions": ["S44"], "rests_on": ["S108-1-I1 (ℰ_bv only)"]},
    {"variant": "V1.5", "moves": "(E)", "flagged": True, "decisions": ["S44", "S41 Q15"], "rests_on": ["S108-1-I5"]},
    {"variant": "V2.1", "moves": "(E)", "flagged": False, "decisions": [], "rests_on": []},
    {"variant": "V2.2", "moves": "(E)", "flagged": False, "decisions": [], "rests_on": []},
    {"variant": "V2.3", "moves": "(E)", "flagged": False, "decisions": [], "rests_on": []},
    {"variant": "V2.4", "moves": "(E)", "flagged": True, "decisions": ["S45", "S44"], "rests_on": []},
    {"variant": "V2.5", "moves": "being an explanation", "flagged": True, "decisions": ["S41 Q2"], "rests_on": ["P-S2-3 (histories by hand)"]},
    {"variant": "V3.4", "moves": "being an explanation, only under S108-3-I2", "flagged": True, "decisions": ["S41 Q2"], "rests_on": ["S108-3-I2", "S108-3-I5"]},
    {"variant": "V3.5", "moves": "being an explanation, only in the tag encoding or under the rejected cut K", "flagged": False, "decisions": [], "rests_on": ["the tag encoding"]},
    {"variant": "V3.6", "moves": "being an explanation", "flagged": False, "decisions": [], "rests_on": ["S108-3-I3", "S108-3-I4"]},
    {"variant": "V4.1", "moves": "being an explanation", "flagged": True, "decisions": ["S45", "S44"], "rests_on": ["S108-4-I1"]},
    {"variant": "V4.2", "moves": "being an explanation", "flagged": True, "decisions": ["S41 Q2"], "rests_on": ["S108-4-I2"]},
    {"variant": "V4.3", "moves": "being an explanation", "flagged": False, "decisions": [], "rests_on": ["S108-4-I3"]},
]

HEAD = """# S108 Part A - the dependency map

*Written by the map agent (Opus 5.5, fresh; rules 6 and 7 of `S108 Part A - how the replies will be read, written before sending.md`), 28 September 2026. Built by `S108 Part A - computation/map/s108_map_build.py` from the frozen template, the frozen set, the tabulation, the four "variants computed" files and their edge `.json`, and the program's D18.1 graph after round 4 (its source read, not run); every input's md5 is in the `.json` (`inputs`). An experiment on copies (rule 11): nothing here changes the theory's text, formal core, claims or program, and nothing is ruled. "Candidate" or "explanation" for what the theory judges; "model" only for the program's own small structures (S43).*

Status: complete, 28 September 2026. The candidate list (rule 7) is `S108 Part A - candidate definitions of explanation.md`.
"""

HOWTO = """## 0. What the map holds, and how to read it

{counts}

- **from**: the item or items the variant varies (definitions; the sentences varied with them are in the `.json`). **to**: the items the edge names: template ids (`L<line>.s|n<k>`, `D…`, `E…`), the parts of the explanation definition (`X:…`, §1), claims (`FC…`) and two cases.
- **Kinds**: *blocks* (under the variant the item is false or has no reading); *constrains* (the item limits the variant and stays readable); *changes with* (the item's extension or wording moves with the variant); *moves* (what the item holds of changes); *independent of* (computed: the item does not move; a negative edge, kept so that "no move" is not read from silence, rule 3).
- **Standing**: *computed* (a run shows it); *contradicted* (a run shows otherwise); *claimed only* (the reply's argument, or the computing agent's where marked, with what would settle it). "cond." = shown only under the reading named. A source row whose parts differ in standing is split (`e<s>.<row>a`, `b`, …). Rows whose content is "none found" are listed apart (§4). Summary edges (`s<n>`) carry a file's own summary table where no row gives the variant's effect on (E) or on being an explanation.
"""

FINDINGS = """### What the computation shows about the dependencies of the explanation definition (short)

- **(E) moves only when its own reads move.** Of the 29 variants run, six move which candidates meet (E): V1.1 (D1.4, what (F1) reads), V2.1–V2.3 (D6.4, Dependence's witness), V2.4 (D6.7, (E) itself) and V1.5, whose reading adds a conjunct "p is a question" to (E) (S108-1-I5). Every other section-1 item varied (D2.1, D2.4, D2.6, D3.3) moves families, Prod or Ident and never (E) (0 of 61,914 generated candidates), as D18.1's graph has it (Roles and Respects are not upstream of (E)).
- **Being an explanation moves with Dec and with D16.XV's rule, not with (E).** With (E) unmoved: V2.5 (D12.1, Sel with H = ∅), V3.6 (D15.8, the population's parts clause; on S108-3-I4) and V4.1–V4.3 (D16.XV). V3.4 (D13.3's ExplUse) and V3.5 (D13.8's record clause) reach Dec only under a reading: D12.2 as written reads Prepares, not ExplUse (contradicted, e3.20a), and its Held(o′, x) at o′ ⪯ o_t makes the record clause idle for every candidate meeting (E) (0 of 115,400 chains, cut T′; e3.25a, e3.26).
- **D18.1's reach is needed, and not enough.** Every computed move of Acc or of Account ∧ ¬Dec(t) is of a variant whose node the graph places upstream of (E) or Dec, or of one whose reading adds that edge (V1.5: ρ_p into (E); V3.4 under S108-3-I2: ExplUse into CT). One reach carries no move for candidates meeting (E): V3.5 (Episode → Con → Dec), screened by Held at o_t (§2's last column).
- **Ruling out, conflict, creation and universality are downstream or aside.** V3.1–V3.3 (D9.7, D9.4, D9.6) and V4.4 move who has ruled what out, problems and the (Suff)/(Nec) defeat sets, never (E) or being an explanation; V2.6, V2.7 (D8.2, D8.5) move rivalry and conflict with a claim; V3.7, V3.8 (D11.4, D14.7) move (P) attribution and (EX); V4.6–V4.8 move 𝔈_Θ, UU (a toy) and (Prov)(i). Each with 0 moves of Acc and of Account ∧ ¬Dec(t) (§2).
- **Where the frozen words hold the middle.** Computed blocks of FROZEN items: D4.4, D13.4, D13.5 (V1.1); L347.s2 (V1.2, V1.8); L307.s1 (V2.2); L315.s1, L317.s6 (V2.6); L403.s3 (V3.4); L375.s2 (V3.7); L495.s1 (V4.7, toy only); and L528.s2–s3 change with V3.8. By the template's own rule a variant that blocks a FROZEN item is not a reading of the frozen words (§3). No flagged candidate of V2.4, V2.5, V4.1, V4.2 blocks a FROZEN item: what they sit against is an owner's decision (the candidate list).
- **The replies' claims the computation contradicts: 12 edges** (§5); among them the replies' routes from D13.3 and D13.8 to Dec, V2.3's block of L329.s3, V4.5's reach to E5, V4.3's "no record" case, and V3.2's "fewer problems" (problems grow).
"""

SECOND = """## 7. Is a second round of Part A needed? (rule 10)

**Yes.** The map has gaps of both kinds rule 10 names: items no variant touched (§6: {untouched} of 815 template items, {um} of 577 middle items, {udefs} middle definitions neither varied nor named) and edges the computation could not settle ({claimed} claimed only). What a second round would need to cover, from the gaps (not a plan; the rule for it is written and committed before sending):

- the middle items no variant touched, section by section (§6), in particular the middle definitions {udeflist};
- the three variants not implemented (V1.6, V1.7, V2.8), each after the orchestrator's ruling on its flag;
- the edges claimed only, each with its "settle" (§4), and the places the program cannot compute: an infinite Γ (V2.2, L311), UsesReason (V3.7), 𝔈_Θ membership (V4.6), Enable/UU/barriers (V4.7, toy only), an argument from ConfCl (V2.7), an attack on (Nec) through easy to vary (V2.4, V2.6);
- the results that rest on one reading (§6): S108-1-I5, S108-3-I2, S108-3-I4, the tag encoding, S108-4-I3, S108-4-I7, so that each candidate's reach is computed under its other choices too;
- the suite's blind spots: no claim separates D6.4 from V2.1 or V2.2 (only generated worlds and built cases do).
"""

UNSURE = """## 8. Unsure

- **Mapping rows to items** is this agent's reading of each row's item text (the table `M` in the builder): line-level references (e.g. "L17, L49, L61, L69") are mapped to the sentences on those lines that the row's words name (the four writing Account(ℰ) ∧ ¬Dec(t)), or to the claims that test the lines where the row names them (e1.12, e1.25); "the L267–L277 table" to every sentence on L269–L277.
- **Touched** counts an item touched when a variant varies it or a computed or contradicted edge names it (an edge into an `X:` node also touches the definitions that define it); an item named only in claimed-only edges is "claimed only". An item a variant reads but no edge names is counted untouched, so the count of untouched items is an upper bound on what the variants did not reach, and a lower bound on nothing (silence is not agreement, rule 3).
- **Summary edges** (`s<n>`) restate the computing files' own summary tables; they add no computation.
- **D18.1's graph** is the program's `claims_b.DEP` after round 4, read from its source; D_TO_NODE folds several definitions into one node (e.g. D13.8 into CCE, while `Episode` is its own node: mapped here to D13.8 by hand, and `CT` to D12.2). The graph's ancestors of (Suff), (Nec) and being an explanation are those of D16.XV's one node, DefeatConds.
- **Kinds** follow the computing files' kinds; "keeps", "no claim separates" and the rows "moves nothing in (E)" are read as *independent of*.
- The whole-suite runs of sections 1–4 were made by the computing agents' own scripts, under load, with capped parts re-run at cap 300 (each file's §7.1); this map takes their results as they give them and reran nothing.
"""


def main(out_json, out_md):
    sents, defs, claims = parse_template()
    dep, d2n = parse_dep()
    n2d = collections.defaultdict(list)
    for d, n in d2n.items():
        n2d[n].append(d)
    extra = {"Episode": "D13.8", "CT": "D12.2"}
    nodes = collections.OrderedDict()
    for k, v in sents.items():
        nodes[k] = dict(v)
    for k, v in defs.items():
        nodes[k] = dict(v)
    for k, v in XNODES.items():
        anc = ancestors(dep, v["dep"])
        anc_defs = sorted({d for n in anc for d in n2d.get(n, [])} | {extra[n] for n in anc if n in extra}, key=nat)
        prims = sorted(n for n in anc if n not in n2d and n not in extra)
        nodes[k] = {"id": k, "kind": "explanation part", "mark": ", ".join(d + " [" + defs[d]["mark"] + "]" for d in v["defined_by"]),
                    "name": v["name"], "statement": v["statement"], "defined_by": v["defined_by"], "reads": v["reads"],
                    "d18_node": v["dep"], "d18_ancestor_definitions": anc_defs, "d18_ancestor_symbols": prims}
    extra_cases = {"FC-E3": "external example 2.3 (a response and a reading of one port; recalibration)",
                   "CT8": "the creative transport case, its run's own provenance (R1–R5, T′)"}

    edges, no_edge = [], []
    split_rows = 0
    for (s, j, key, e, named, base, st0, ev, settle) in norm_rows():
        if key in NO_EDGE:
            no_edge.append({"source": key, "variant": e["variant"], "finding": NO_EDGE[key], "evidence": ev})
            continue
        parts = M[key]
        split_rows += len(parts) > 1
        variants = [e["variant"]] if not re.search(r"–|,", e["variant"]) else (
            ["V2.1", "V2.2", "V2.3", "V2.4"] if e["variant"].startswith("V2.1–") else [x.strip() for x in e["variant"].split(",")])
        for pi, p in enumerate(parts):
            kind = p.get("kind") or KINDS[e["kind"]]
            standing = p.get("standing") or base
            assert standing in ("computed", "contradicted", "claimed only"), (key, standing)
            eid = f"e{s}.{j:02d}" + ("" if len(parts) == 1 else "abcd"[pi])
            frm = sorted({x for v in variants for x in V[v]["varied"]}, key=nat)
            for t in p["to"]:
                if t not in nodes and t not in claims and t not in extra_cases:
                    raise SystemExit(f"unknown target {t} in {key}")
            who = "the reply" if named else "the computing agent"
            edges.append({"id": eid, "source": f"section {s} .json, edge {j}" + (f" ({e['id']})" if e.get("id") else ""),
                          "variants": variants, "from": frm, "kind": kind, "to": p["to"],
                          "to_label": e["item"], "standing": standing, "condition": p.get("condition", ""),
                          "named_by": "reply" if named else "computation",
                          "claimed_by": (who if standing == "claimed only" else ""),
                          "source_kind": e["kind"], "source_standing": st0, "what_shows_it": ev,
                          "what_would_settle": settle if standing != "computed" else "",
                          "note": p.get("note", ""),
                          "reply_why": e.get("reply_why") or REPLY_WHY.get(key, "")})
    for n, (vid, src, kind, to, ev) in enumerate(SUMMARY):
        edges.append({"id": f"s{n:02d}", "source": f"summary: {src}", "variants": [vid], "from": V[vid]["varied"], "kind": kind,
                      "to": to, "to_label": " ; ".join(to), "standing": "computed", "condition": "", "named_by": "computation (summary table)",
                      "claimed_by": "", "source_kind": kind, "source_standing": "computed", "what_shows_it": ev, "what_would_settle": "",
                      "note": "", "reply_why": ""})

    named_targets = {t for e in edges for t in e["to"]}
    for c in sorted((t for t in named_targets if t in claims), key=nat):
        nodes[c] = dict(claims[c])
    for c in sorted(t for t in named_targets if t in extra_cases):
        nodes[c] = {"id": c, "kind": "case", "mark": "–", "title": extra_cases[c]}

    for n in nodes.values():
        n["varied_by"], n["edges_in"] = [], []
    for vid, v in V.items():
        for it in v["varied"]:
            nodes[it]["varied_by"].append(vid)
    for e in edges:
        for t in e["to"]:
            nodes[t]["edges_in"].append({"edge": e["id"], "kind": e["kind"], "standing": e["standing"], "variants": e["variants"]})
            if t.startswith("X:"):
                for d in XNODES[t]["defined_by"]:
                    nodes[d]["edges_in"].append({"edge": e["id"], "kind": e["kind"], "standing": e["standing"],
                                                 "variants": e["variants"], "via": t})
    impl = {k for k, v in V.items() if not v["implemented"].startswith("no")}
    for n in nodes.values():
        by_comp = [x for x in n["edges_in"] if x["standing"] in ("computed", "contradicted")]
        vimpl = [x for x in n["varied_by"] if x in impl]
        n["touched"] = "computed" if (vimpl or by_comp) else ("claimed only" if (n["varied_by"] or n["edges_in"]) else "untouched")

    reach = collections.OrderedDict()
    for vid, v in V.items():
        nd = v["d18_node"]
        reach[vid] = {t: (nd == t) or (nd in ancestors(dep, t)) for t in ("(E)", "Dec", "DefeatConds")}

    tmpl_ids = list(sents) + list(defs)
    by = collections.defaultdict(collections.Counter)
    untouched = collections.defaultdict(list)
    for k in tmpl_ids:
        n = nodes[k]
        by[(n.get("stretch") or "?", n["mark"] == "FROZEN")][n["touched"]] += 1
        if n["touched"] == "untouched":
            untouched[(n.get("stretch") or "?", n["kind"], n["mark"] == "FROZEN")].append(k)
    claimed = [e for e in edges if e["standing"] == "claimed only"]
    udefs = sorted((k for k in defs if nodes[k]["mark"] != "FROZEN" and nodes[k]["touched"] == "untouched"), key=nat)
    gaps = {
        "touched_counts": {f"{s} {'FROZEN' if fz else 'middle'}": dict(c) for (s, fz), c in sorted(by.items())},
        "untouched_middle_definitions": udefs,
        "untouched_frozen_definitions": sorted((k for k in defs if nodes[k]["mark"] == "FROZEN" and nodes[k]["touched"] == "untouched"), key=nat),
        "untouched_items": {f"{s} {kind} {'FROZEN' if fz else 'middle'}": v for (s, kind, fz), v in sorted(untouched.items())},
        "edges_claimed_only": [e["id"] for e in claimed],
        "variants_not_implemented": [k for k, v in V.items() if v["implemented"].startswith("no")],
        "results_resting_on_one_reading": {
            "S108-1-I5": "V1.5's whole effect (a question with no recorded contract history is declared); other choice: V1.5 computes nothing",
            "S108-1-I1": "whether ℰ_bv becomes an account under V1.1 (reading (i) yes, (ii) no)",
            "S108-3-I2": "whether V3.4 reaches Dec at all (CT asks Build's ExplUse)",
            "tag encoding / cut K": "V3.5's only moves of being an explanation",
            "S108-3-I4": "V3.6's reach (parts := E's components; stated construction := t's own)",
            "S108-4-I3": "V4.3's reach (Sel ∨ CT read at the holding; through inherited provenance it moves nothing)",
            "S108-4-I7": "V4.7 computed on a toy only",
            "I90 (Θ by hand)": "Dec(t) on every worked case and generated candidate: histories set by hand",
        },
        "not_computable_in_the_program": ["an infinite Γ (V2.2, L311)", "UsesReason over circuits (V3.7, D9.11)",
                                          "𝔈_Θ membership over every (p, t, Γ) (V4.6)", "(CT1), Can, Enable, UU, barriers (V4.7)",
                                          "an argument whose premise is a computed ConfCl (V2.7, D8.6, D10.6)",
                                          "an attack on (Nec) through easy to vary (V2.4, V2.6)", "Desc, BadTarget, BadReq (V1.6)",
                                          "a recorded contract history ρ_p (V1.5)"],
        "suite_blind_spots": ["no claim separates D6.4 from V2.1 (e2.39)", "no claim separates D6.4 from V2.2 (e2.38)"],
    }
    tm = collections.Counter(nodes[k]["touched"] for k in tmpl_ids)
    counts = {
        "template items": len(tmpl_ids), "sentences": len(sents), "definitions": len(defs),
        "FROZEN items": sum(1 for k in tmpl_ids if nodes[k]["mark"] == "FROZEN"),
        "middle items": sum(1 for k in tmpl_ids if nodes[k]["mark"] != "FROZEN"),
        "explanation-part nodes": len(XNODES), "claims named": sum(1 for n in nodes.values() if n["kind"] == "claim"),
        "cases named": sum(1 for n in nodes.values() if n["kind"] == "case"), "nodes": len(nodes),
        "edges": len(edges), "edges by standing": dict(collections.Counter(e["standing"] for e in edges)),
        "edges by kind": dict(collections.Counter(e["kind"] for e in edges)),
        "source rows": sum(len(json.loads(SEC[s].read_text(encoding="utf-8"))["edges"]) for s in (1, 2, 3, 4)),
        "rows split": split_rows, "rows with no edge": len(no_edge), "summary edges": len(SUMMARY),
        "template items touched": dict(tm),
        "middle items untouched": sum(1 for k in tmpl_ids if nodes[k]["mark"] != "FROZEN" and nodes[k]["touched"] == "untouched"),
        "variants": len(V), "variants run": len(impl),
    }
    ins = {"template": (TEMPLATE.name, md5(TEMPLATE)), "frozen set": (FROZEN.name, md5(FROZEN)),
           "tabulation": (TAB.name, md5(TAB)), "program D18.1 graph (claims_b.py, read)": (str(PROG.relative_to(RES)), md5(PROG))}
    for s in (1, 2, 3, 4):
        ins[f"section {s} .json"] = (SEC[s].name, md5(SEC[s]))
        ins[f"section {s} .md"] = (SECMD[s].name, md5(SECMD[s]))
    out = {"about": "S108 Part A, rule 6: the dependency map. Nodes: every item of the frozen template (688 sentences, 127 definitions and encodings, FROZEN and middle), the parts of the explanation definition (X:…), and the claims and cases the edges name. Edges: blocks, constrains, changes with, moves, and 'independent of' (a computed absence), each with what shows it and its standing: computed, contradicted, claimed only. Built by s108_map_build.py from the files in 'inputs'. Nothing here changes the theory (rule 11); nothing is ruled.",
           "inputs": {k: {"file": a, "md5": b} for k, (a, b) in ins.items()}, "counts": counts,
           "second_round_needed": True,
           "variants": V,
           "effect_on_the_explanation_definition": {k: dict(zip(["Acc (E)", "Account ∧ ¬Dec(t)", "being an explanation as the variant defines it", "other", "suite"], v)) for k, v in EFFECT.items()},
           "d18_static_reach": reach, "candidates": CANDIDATES,
           "nodes": list(nodes.values()), "edges": edges, "rows_with_no_edge": no_edge, "gaps": gaps}
    pathlib.Path(out_json).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # ------------------------------------------------------------------ the .md
    def mk(i):
        n = nodes.get(i)
        if n and n["kind"] in ("sentence", "definition"):
            return f"{i} [{n['mark']}]"
        if n and n["kind"] == "claim":
            return f"{i} [claim]"
        return i

    def cut(s, n=150):
        s = re.sub(r"\s+", " ", s or "").strip().replace("|", "/")
        return s if len(s) <= n else s[:n - 1].rsplit(" ", 1)[0] + " …"

    def yn(b):
        return "yes" if b else "–"
    out_md_lines = [HEAD]
    c = counts
    ctab = "\n".join([
        "| | count |", "|---|---|",
        f"| nodes | {c['nodes']}: {c['template items']} template items ({c['sentences']} sentences, {c['definitions']} definitions and encodings; {c['FROZEN items']} FROZEN, {c['middle items']} middle) + {c['explanation-part nodes']} parts of the explanation definition + {c['claims named']} claims + {c['cases named']} cases named by edges |",
        f"| variants | {c['variants']} tabulated; {c['variants run']} run; 3 flagged and not run (V1.6, V1.7, V2.8) |",
        f"| source rows | {c['source rows']} (the four `.json`); {c['rows split']} split by standing; {c['rows with no edge']} 'none found' rows kept apart (§4) |",
        f"| edges | {c['edges']} ({c['summary edges']} summary edges): " + ", ".join(f"{k} {v}" for k, v in c["edges by standing"].items()) + "; " + ", ".join(f"{k} {v}" for k, v in c["edges by kind"].items()) + " |",
        f"| template items touched | computed {tm['computed']}, claimed only {tm['claimed only']}, untouched {tm['untouched']} (middle untouched: {c['middle items untouched']} of {c['middle items']}) |",
    ])
    out_md_lines.append(HOWTO.format(counts=ctab))
    # §1
    L = ["## 1. The parts of the explanation definition (nodes `X:…`)\n",
         "Being an explanation, now: Account(ℰ) ∧ ¬Dec(t) (D16.XV; L17.n2, L49.n3, L61.n2, L69.n3), with Account = (E) = Acc (D6.7). \"Reads\": by the statement; \"D18.1 ancestors\": every definition upstream of the node in the program's graph.\n",
         "| node | defined by [mark] | statement | reads (by its statement) | D18.1 ancestors (definitions) |", "|---|---|---|---|---|"]
    for k in XNODES:
        n = nodes[k]
        L.append(f"| {k} | {n['mark']} | {n['statement'].replace('|', '/')} | {', '.join(n['reads'])} | {', '.join(n['d18_ancestor_definitions'])} |")
    L.append("\nAncestor symbols that are no definition (D0.2's primitives, declared inputs, Θ): (E): " + ", ".join(nodes["X:(E)"]["d18_ancestor_symbols"]) + "; Dec: " + ", ".join(nodes["X:Dec"]["d18_ancestor_symbols"]) + "; D16.XV's node: " + ", ".join(nodes["X:Expl"]["d18_ancestor_symbols"]) + ".\n")
    out_md_lines.append("\n".join(L))
    # §2
    L = ["## 2. How the explanation definition changes with each varied item (computed)\n",
         "Counts: worked cases; generated candidates at scale 4, SMALL / SMALL with value maps / proper targets / MID (section 2: single / value maps / MID proper). \"Being an explanation as the variant defines it\" differs from Account ∧ ¬Dec(t) only for V4.1–V4.3, which redefine it. Last column: is the varied item's node upstream of (E) / Dec / D16.XV's defeat conditions in D18.1's graph (static, not run).\n",
         "| variant | item [mark] | Acc (E) | Account ∧ ¬Dec(t) | being an explanation as redefined | what else moves | suite (claims whose status moves) | D18.1 reach (E) / Dec / defeat |",
         "|---|---|---|---|---|---|---|---|"]
    for vid, v in V.items():
        ef = EFFECT[vid]
        items = ", ".join(f"{d} [{nodes[d]['mark']}]" for d in v["definitions_varied"])
        r = reach[vid]
        L.append(f"| {vid} | {items} | {ef[0]} | {ef[1]} | {ef[2]} | {ef[3]} | {ef[4]} | {yn(r['(E)'])} / {yn(r['Dec'])} / {yn(r['DefeatConds'])} |")
    L.append("")
    L.append(FINDINGS)
    out_md_lines.append("\n".join(L))
    # §3 FROZEN items reached
    L = ["## 3. FROZEN items the variants reach\n",
         "Every edge whose target is FROZEN, by standing. A FROZEN item *blocked* (computed) marks a variant that is, by the template's rule, not a reading of the frozen words.\n",
         "| FROZEN item | edges (variant: kind, standing) |", "|---|---|"]
    fro = collections.OrderedDict()
    for e in edges:
        for t in e["to"]:
            if t in nodes and nodes[t].get("mark") == "FROZEN":
                fro.setdefault(t, []).append(f"{e['id']} {'/'.join(e['variants'])}: {e['kind']}, {e['standing']}" + (" (cond.)" if e["condition"] else ""))
    for t in sorted(fro, key=nat):
        L.append(f"| {t} | {'; '.join(fro[t])} |")
    fz_all = [k for k in tmpl_ids if nodes[k]["mark"] == "FROZEN"]
    L.append(f"\n{len(fro)} of {len(fz_all)} FROZEN items are named by an edge; blocks computed: " + ", ".join(sorted({t for e in edges if e['kind'] == 'blocks' and e['standing'] == 'computed' for t in e['to'] if t in nodes and nodes[t].get('mark') == 'FROZEN'}, key=nat)) + ".\n")
    out_md_lines.append("\n".join(L))
    # §4 edges
    L = ["## 4. The edges\n", "What shows it is cut here; whole in the `.json` (`what_shows_it`, `reply_why`, `what_would_settle`, `note`). For a claimed-only edge the cell gives the argument and what would settle it.\n"]
    for s in ("S1", "S2", "S3", "S4"):
        L.append(f"\n### Section {s[1]}\n")
        L.append("| id | variant | from | kind | to [mark] | standing | what shows it (cut) |")
        L.append("|---|---|---|---|---|---|---|")
        for vid in [k for k, v in V.items() if v["section"] == s]:
            for e in [e for e in edges if e["variants"][0] == vid]:
                st = e["standing"] + (" (the computing agent)" if e["claimed_by"] == "the computing agent" else "")
                if e["condition"]:
                    st += "; cond.: " + e["condition"]
                to = ", ".join(mk(t) for t in e["to"]) or "– (" + cut(e["note"] or e["to_label"], 80) + ")"
                shows = e["note"] if (e["note"] and (e["id"][-1] in "abcd" or not e["what_shows_it"])) else e["what_shows_it"]
                if e["standing"] == "claimed only":
                    arg = e["reply_why"] if e["named_by"] == "reply" and e["reply_why"] else (e["note"] or e["what_shows_it"])
                    shows = "argument: " + cut(arg, 90) + ((" · settle: " + cut(e["what_would_settle"], 90)) if e["what_would_settle"] else "")
                frm = sorted({d for v in e["variants"] for d in V[v]["definitions_varied"]}, key=nat)
                L.append(f"| {e['id']} | {'/'.join(e['variants'])} | {', '.join(frm)} | {e['kind']} | {cut(to, 120)} | {st} | {cut(shows, 190)} |")
    L.append("\n### Rows with no edge (a search or a 'none found' finding)\n")
    L.append("| row | variant | finding |")
    L.append("|---|---|---|")
    for r in no_edge:
        L.append(f"| {r['source']} | {r['variant']} | {r['finding']} |")
    out_md_lines.append("\n".join(L) + "\n")
    # §5 contradicted
    L = ["## 5. Contradicted edges (the computation shows otherwise)\n", "| id | variant | claimed | what the computation shows (cut) |", "|---|---|---|---|"]
    for e in edges:
        if e["standing"] == "contradicted":
            claimed_txt = f"{e['kind']} {', '.join(e['to']) or e['to_label']}"
            shown = e["note"] if (e["note"] and e["id"][-1] in "abcd") else e["what_shows_it"]
            L.append(f"| {e['id']} | {'/'.join(e['variants'])} | {cut(claimed_txt, 90)} | {cut(shown, 200)} |")
    out_md_lines.append("\n".join(L) + "\n")
    # §6 gaps
    L = ["## 6. Gaps (rule 6: listed; rule 10: they decide a second round)\n",
         "### 6.1 Items no variant touched\n",
         "| stretch | FROZEN: computed / claimed only / untouched | middle: computed / claimed only / untouched |", "|---|---|---|"]
    for sname in ("S1", "S2", "S3", "S4"):
        f_ = by[(sname, True)]
        m_ = by[(sname, False)]
        L.append(f"| {sname} | {f_['computed']} / {f_['claimed only']} / {f_['untouched']} | {m_['computed']} / {m_['claimed only']} / {m_['untouched']} |")
    L.append(f"\nMiddle definitions neither varied nor named by any edge ({len(udefs)}): " + ", ".join(udefs) + ". FROZEN definitions no edge names (" + str(len(gaps["untouched_frozen_definitions"])) + "): " + ", ".join(gaps["untouched_frozen_definitions"]) + ". Every section had its eight variants; no section is untouched as a whole.\n")
    L.append("### 6.2 Edges the computation could not settle (claimed only)\n")
    L.append(f"{len(claimed)} edges: " + ", ".join(e["id"] for e in claimed) + ". Each with its argument and what would settle it in §4; 15 of them are of the three variants not run (V1.6, V1.7, V2.8), whose standing waits on the orchestrator's ruling of the tabulation's flags (rule 4).\n")
    L.append("### 6.3 Results that rest on one reading, and what the program cannot compute\n")
    L.append("| rests on | what |")
    L.append("|---|---|")
    for k, v in gaps["results_resting_on_one_reading"].items():
        L.append(f"| {k} | {v} |")
    L.append("\nNot computable in the program as it stands: " + "; ".join(gaps["not_computable_in_the_program"]) + ". Suite blind spots: " + "; ".join(gaps["suite_blind_spots"]) + ".\n")
    L.append("### 6.4 The untouched items, by id (each node in the `.json`)\n")
    for k, v in gaps["untouched_items"].items():
        L.append(f"- **{k}** ({len(v)}): " + ", ".join(v))
    out_md_lines.append("\n".join(L) + "\n")
    out_md_lines.append(SECOND.format(untouched=tm["untouched"], um=c["middle items untouched"], udefs=len(udefs),
                                      claimed=len(claimed), udeflist=", ".join(udefs)))
    out_md_lines.append(UNSURE)
    out_md_lines.append("Built by one Opus 5.5 agent under rules 6 and 10, 28 September 2026. Nothing ruled; nothing applied to the theory (rule 11).\n")
    pathlib.Path(out_md).write_text("\n".join(out_md_lines), encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
