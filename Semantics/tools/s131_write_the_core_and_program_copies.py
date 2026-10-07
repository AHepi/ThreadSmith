#!/usr/bin/env python3
"""s131_write_the_core_and_program_copies.py

What it does, in plain words: for log S131 (decision S86, "Knowledge doesn't need to be worked out, explanation
does"). Writes COPIES of S129's formal core copy and S129's program copy (which already carry Reading C, S83, and the
graded survival condition, S84) into results/S131 Explanation by construction carried into copies/, with the third
decision carried in, in S130's smallest wording (S130 results, section 4.1):
  the owner's condition in D16.XV: "Acc and Dec implies not Expl" becomes "Acc and not Con implies not Expl";
  (Suff)'s defeat condition in D16.XV: "Acc and not Dec and ..." becomes "Acc and Con and ...";
  under Reading C both read Con and Expl at the declared boundary (S129's K1 proposal; I201 in S129's copy);
  FC30 ((E) takes no provenance) is not touched.
In the program copy: a third switch, S131_EXPL_BY_CONSTRUCTION, beside S129's S129_READING_C and S129_GRADED (all on by
default), read by the two functions that encode D16.XV (claims_s41.suff_defeats, claims_s41.expl_ok) and by D18.1's
graph node for D16.XV; the claims that encode the owner's condition or (Suff) (FC30.new1 parts (a), (b), (c), (d), (e),
(g), (h); FC23.new2 part (f)) pass Con to them and, with the decision on, check their S131 wording; a fourth switch,
S131_CLAIMS_REWORDED (on by default), set to 0 makes those claims check their round-4 wording against the decision
instead, to show which would flip as written. With S131_EXPL_BY_CONSTRUCTION=0 the copy computes what S129's copy does.
Every change is an exact replacement that must match once, or the script stops; each is marked [S131: ...] in the core
copy and "S131" in the program copy. The originals (S107's core and program; S129's core copy and program copy) are
read, never written; the script checks their md5s before and after, and that the program copy's other files are
byte-equal to S129's.

  python3 -B Semantics/tools/s131_write_the_core_and_program_copies.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import hashlib, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S107 = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading')
S129 = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies')
SRC_CORE = os.path.join(S129, 'formal core, after round 4, with Reading C and the graded survival condition - a copy.md')
SRC_MODEL = os.path.join(S129, 'model after Reading C')
OUT_DIR = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies')
CORE_NAME = 'formal core, after round 4, with Reading C, the graded survival condition and explanation by construction - a copy.md'
OUT_CORE = os.path.join(OUT_DIR, CORE_NAME)
OUT_MODEL = os.path.join(OUT_DIR, 'model after Reading C and explanation by construction')


def md5f(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def tree_md5(d):
    out = {}
    for r, _, fs in os.walk(d):
        if '__pycache__' in r:
            continue
        for f in fs:
            p = os.path.join(r, f)
            out[os.path.relpath(p, d)] = md5f(p)
    return out


def replace_once(s, old, new, label):
    n = s.count(old)
    if n != 1:
        sys.exit('%s: expected one match, found %d' % (label, n))
    return s.replace(old, new)


# ---- the formal core -------------------------------------------------------------------------------------------------
CORE_NOTE = """*S131 (decision S86), 2 October 2026: a COPY, not the theory's formal core. It is S129's copy, `results/S129 Reading C carried into copies/formal core, after round 4, with Reading C and the graded survival condition - a copy.md` (md5 {md5}; not written to), itself the formal core after round 4 (`results/S107 Round 4 - maths after the reading/formal core, after round 4.md`, md5 {md5_107}; not written to) with S83 and S84 carried in; here the owner's third decision is carried in, each change marked [S131: S86 …] with what it was, and two notes marked [S131: S86, a consequence, not a change]; nothing else is altered. S86 ("Correct. Knowledge doesn't need to be worked out, explanation does."): "explanation" is kept for an account whose transport was constructed (S130 results, section 4.1: the owner's condition Acc(ℰ) ∧ ¬Con(t) ⇒ ¬Expl(ℰ); (Suff) defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ Con(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]; text 131 L17, L49, L61, L69, L536 in text 107's numbering). Under Reading C, Con and Expl are read at the boundary β declared for the claim (S129's K1 proposal; D12.2 of this copy, I201). (E) still takes no provenance (FC30, unchanged). Inventions of this copy, provisional and not in the register (the register is the theory's; S129's copy used I198 to I201): **[I202]** Expl read at the declared boundary, Expl_β(ℰ), as S129's K1 proposed, with Con_β; a claim with no boundary declared is read as S129's copy reads it (I198) (other: Expl unindexed, which S129 computed has no common model with the owner's condition once one transport has two provenances at two boundaries). **[I203]** the owner's condition widened from 'declared' to 'not constructed' (Acc ∧ ¬Con ⇒ ¬Expl), so a selected account is no explanation, the smallest of S130's ladder (¬Dec ⊃ Con ⊃ Build with ExplUse ⊃ (EX); S130 section 4.4, item 4) (others: Build with ExplUse, or (EX) only, for a higher line, if the owner would also withhold 'explanation' from content learned from a teacher's answers). Program: `model after Reading C and explanation by construction/` beside this file (its `model/corefile.py` reads this file); record: `results/S131 Explanation by construction carried into copies - what changes.md`. Nothing is settled (S28).*

"""

CORE_CHANGES = [
    ('D16.XV owner condition (S86)',
     "Expl(ℰ): an atom, no definition uses it; Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) [owner S41: Q2]: a candidate meeting (E) whose "
     "transport is declared is no explanation. (E) still takes no provenance (FC30); ¬Dec(t) stands beside it (FC30.new1).",
     "Expl(ℰ): an atom, no definition uses it; read at the boundary β declared for the claim, Expl_β(ℰ) (L524) **[I202]** "
     "[S131: S86 with S83, copy only: S129's K1 proposal, 'write Expl_β(ℰ) in D16.XV'; was 'Expl(ℰ): an atom, no definition "
     "uses it']; Acc(ℰ) ∧ ¬Con_β(t) ⇒ ¬Expl_β(ℰ) [owner S41: Q2; S85; S86] **[I203]** [S131: S86, copy only: was 'Acc(ℰ) ∧ "
     "Dec(t) ⇒ ¬Expl(ℰ) [owner S41: Q2]']: a candidate meeting (E) whose transport is declared or selected at β is no "
     "explanation at β [S131: S86, copy only: was 'whose transport is declared is no explanation']; a construction whose "
     "target is held only outside β is declared at β (D12.2 of this copy, I201), so no explanation there. (E) still takes no "
     "provenance (FC30); Con_β(t) stands beside it (FC30.new1) [S131: S86, copy only: was '¬Dec(t) stands beside it']."),
    ('D16.XV (Suff) (S86)',
     "- (Suff), L536 and L17: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)];",
     "- (Suff), L536 and L17: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ Con_β(t) ∧ ∃α ∈ X_j(Expl_β(ℰ)): Acc ∉ Uses(α)] [S131: S86 with "
     "S83, copy only: was '∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]'; text 131 L17 and L536 write "
     "Account(ℰ) ∧ Con(t) and 'whose provenance is constructed' (text 107 numbering)];"),
    ('D16.XV note (S86)',
     "with Expl_β they have one]",
     "with Expl_β they have one] [S131: S86, a consequence, not a change: with Con_β and Expl_β written in (above), Expl_β := "
     "Acc ∧ Con_β is a common model of (Suff) and the owner's condition at every β (FC30.new1 (c) of the program copy); the "
     "round-4 (Suff) (Acc ∧ ¬Dec ⇒ Expl) and S86's owner's condition (Acc ∧ ¬Con ⇒ ¬Expl) have none wherever an account is "
     "selected, so the decision changes both lines or neither; with (Nec) as conjectured (Expl only for candidates some "
     "transport preserves), the owner's condition makes Acc ∧ Con_β necessary for an account to be an explanation at β, "
     "and (Suff) conjectures it sufficient]"),
    ('D14.7 note (S86)',
     "FC90.new1 (c): the pole's forward candidate meets (E) with δ = L, not with δ = H; L449 unchanged]",
     "FC90.new1 (c): the pole's forward candidate meets (E) with δ = L, not with δ = H; L449 unchanged] [S131: S86, a "
     "consequence, not a change: no conjunct of (EX) asks Con_β(t_c): Origin asks Build of c (D13.3: a trace that Prepares c "
     "and holds it), and D12.2 asks a trace that holds t_c at its output, while a transport assembled later from a trace's "
     "outputs is not thereby prepared by it (I168); so an instance of (EX) whose t_c is not constructed at β would be a "
     "created explanation that D16.XV of this copy says is no explanation at β. Whether (EX) should carry Con_β(t_c) as a "
     "conjunct is left to the owner (S130 section 4.3, 'to check'); not changed here]"),
]

# ---- the program --------------------------------------------------------------------------------------------------
B_CHANGES = [
    ('switch', 'GRADED = os.environ.get("S129_GRADED", "1") == "1"\n',
     'GRADED = os.environ.get("S129_GRADED", "1") == "1"\n'
     '# S131 (decision S86, copy only): EXPL_BY_CONSTRUCTION, "explanation" kept for an account whose transport was\n'
     '# constructed: D16.XV\'s owner\'s condition reads Acc ∧ ¬Con ⇒ ¬Expl and (Suff)\'s defeat condition Acc ∧ Con ∧ … (the\n'
     '# S131 core copy; text 131 L17, L49, L61, L69, L536). On by default; S131_EXPL_BY_CONSTRUCTION=0 computes what S129\'s\n'
     '# copy does. CLAIMS_REWORDED: with the decision on, the claims that encode the owner\'s condition or (Suff) check their\n'
     '# S131 wording (default); S131_CLAIMS_REWORDED=0 makes them check their round-4 wording against the decision instead,\n'
     '# to show which would flip as written. It changes nothing when the decision is off.\n'
     'EXPL_BY_CONSTRUCTION = os.environ.get("S131_EXPL_BY_CONSTRUCTION", "1") == "1"\n'
     'CLAIMS_REWORDED = os.environ.get("S131_CLAIMS_REWORDED", "1") == "1"\n\n\n'
     'def s131_wording():\n'
     '    """S131: the claims check their S86 wording (the decision on and the claims reworded)."""\n'
     '    return EXPL_BY_CONSTRUCTION and CLAIMS_REWORDED\n'),
    ('DEP DefeatConds', 'DEP_EXPLUSE_PRIMITIVE = dict(DEP, ExplUse=[])\n',
     '# S131 (S86, copy only): D16.XV\'s owner\'s condition and (Suff) read Con, not Dec (Dec still reaches Con through D12.3).\n'
     'if EXPL_BY_CONSTRUCTION:\n'
     '    DEP["DefeatConds"] = ["Con" if _x == "Dec" else _x for _x in DEP["DefeatConds"]]\n'
     'DEP_EXPLUSE_PRIMITIVE = dict(DEP, ExplUse=[])\n'),
]

S41_CHANGES = [
    ('import', "from .cases import pole_rev_candidate  # S107 round 4, area 3 (W5): FC30.new1 (h)\n",
     "from .cases import pole_rev_candidate  # S107 round 4, area 3 (W5): FC30.new1 (h)\n"
     "from . import claims_b as _cb  # S131 (copy only): the S86 switches, read at call time\n"),
    ('suff_defeats', '''def suff_defeats(acc, dec, out, reading):
    """ℰ ∈ Def_j(reading): L536 and L17 as S41 writes it ask Acc ∧ ¬Dec(t) ∧ an argument not using (E) that
    rules out Expl(ℰ); L17 as text 104 words it has no ¬Dec(t) (E06)."""
    if reading == "L17 as text 104 words it":
        return bool(acc and out)
    return bool(acc and not dec and out)


def expl_ok(acc, dec, expl):
    """The owner's condition on the atom (S41, Q2): Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ)."""
    return not (acc and dec and expl)
''', '''def suff_defeats(acc, dec, out, reading, con=None):
    """ℰ ∈ Def_j(reading): L536 and L17 as S41 writes it ask Acc ∧ ¬Dec(t) ∧ an argument not using (E) that
    rules out Expl(ℰ); L17 as text 104 words it has no ¬Dec(t) (E06).
    S131 (decision S86, copy only): with EXPL_BY_CONSTRUCTION on, L536 and L17 ask Acc ∧ Con(t) ∧ such an argument
    (D16.XV of the S131 core copy); Con must then be given."""
    if reading == "L17 as text 104 words it":
        return bool(acc and out)
    if _cb.EXPL_BY_CONSTRUCTION:
        if con is None:
            raise ValueError("S131: (Suff) under S86 reads Con(t), and it was not given")
        return bool(acc and con and out)
    return bool(acc and not dec and out)


def expl_ok(acc, dec, expl, con=None):
    """The owner's condition on the atom (S41, Q2): Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ).
    S131 (decision S86, copy only): with EXPL_BY_CONSTRUCTION on, Acc(ℰ) ∧ ¬Con(t) ⇒ ¬Expl(ℰ); Con must be given."""
    if _cb.EXPL_BY_CONSTRUCTION:
        if con is None:
            raise ValueError("S131: the owner's condition under S86 reads Con(t), and it was not given")
        return not (acc and not con and expl)
    return not (acc and dec and expl)
'''),
    ('(a) call', '''            d = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            rows.append("%s (Sel %s, Con %s, Dec %s), argument usable %s: %s" % (kind, s, k, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS)))''',
     '''            d = {r: suff_defeats(acc, dec, out, r, con=k) for r in SUFF_READINGS}  # S131: Con passed
            rows.append("%s (Sel %s, Con %s, Dec %s), argument usable %s: %s" % (kind, s, k, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS)))'''),
    ('(a) Sel check', '''            if kind == "Con" and accepts:
                ok = ok and all(d.values())
    _, alpha = expl_ruled_out(Assessor(["MP"], []), c.name)''',
     '''            if kind == "Con" and accepts:
                ok = ok and all(d.values())
            # S131 (copy only): the claims file's (a) says also what a selected transport gives; checked here, in the
            # S86 wording (outside Def(L536) and Def(L17, S41), as a declared one) or, as written, in all three
            if kind == "Sel" and accepts and _cb.EXPL_BY_CONSTRUCTION:
                if _cb.s131_wording():
                    ok = ok and d["L17 as text 104 words it"] and not d["L536"] and not d["L17 (S41)"]
                else:
                    ok = ok and all(d.values())
    _, alpha = expl_ruled_out(Assessor(["MP"], []), c.name)'''),
    ('(a) statement', '''                          "the pole's forward candidate meets (E) (FC26); with a declared transport and an argument not using (E) that rules out Expl(ℰ), it is in Def(L17 as text 104 words it) and in neither Def(L536) nor Def(L17) as S41 writes it; with a constructed transport it is in all three",''',
     '''                          "the pole's forward candidate meets (E) (FC26); with a declared transport and an argument not using (E) that rules out Expl(ℰ), it is in Def(L17 as text 104 words it) and in neither Def(L536) nor Def(L17) as S41 writes it; with a constructed transport it is in all three"
                          + ("; with a selected transport, as with a declared one (S131: S86)" if _cb.s131_wording() else ("; with a selected transport, in all three" if _cb.EXPL_BY_CONSTRUCTION else "")),'''),
    ('(b) call', '''        d = {r: suff_defeats(a, dec, out, r) for r in SUFF_READINGS}
        if d["L17 (S41)"] != d["L536"]:
            return "Def(L17, S41) ≠ Def(L536): %s\\n%s" % (d, cand.describe())
        if d["L17 as text 104 words it"] != (d["L536"] or (a and dec and out)):''',
     '''        d = {r: suff_defeats(a, dec, out, r, con=k) for r in SUFF_READINGS}  # S131: Con passed
        if d["L17 (S41)"] != d["L536"]:
            return "Def(L17, S41) ≠ Def(L536): %s\\n%s" % (d, cand.describe())
        # S131 (S86, copy only): the accounts L17 as text 104 words it adds are those not constructed (S131 wording)
        if d["L17 as text 104 words it"] != (d["L536"] or (a and (not k if _cb.s131_wording() else dec) and out)):'''),
    ('(b) statement', '''    parts.append(forall(S, "FC30.new1", 2, "(b) one defeat set", "Def_j(L17, S41) = Def_j(L536); Def_j(L17 as text 104 words it) = Def_j(L536) ∪ {ℰ : Acc ∧ Dec(t) ∧ Expl(ℰ) ruled out}",''',
     '''    parts.append(forall(S, "FC30.new1", 2, "(b) one defeat set", "Def_j(L17, S41) = Def_j(L536); Def_j(L17 as text 104 words it) = Def_j(L536) ∪ {ℰ : Acc ∧ %s ∧ Expl(ℰ) ruled out}" % ("¬Con(t)" if _cb.s131_wording() else "Dec(t)"),'''),
    ('(c)', '''    both = True
    for a, d_ in itertools.product((False, True), repeat=2):
        expl = a and not d_  # Expl := Acc ∧ ¬Dec
        suff = (not (a and not d_)) or expl  # (Suff) as conjectured: Acc ∧ ¬Dec ⇒ Expl
        both = both and suff and expl_ok(a, d_, expl)  # the owner's condition: Acc ∧ Dec ⇒ ¬Expl
    parts.append(construction("(c) the owner's condition and (Suff) have a common model", "Expl := Acc ∧ ¬Dec meets Acc ∧ ¬Dec ⇒ Expl ((Suff) as conjectured) and Acc ∧ Dec ⇒ ¬Expl (S41, Q2), on every candidate",
                              both, "checked on the four values of (Acc, Dec); (E) itself takes no provenance (FC30): ¬Dec(t) stands beside it"))''',
     '''    both = True
    if not _cb.EXPL_BY_CONSTRUCTION:
        for a, d_ in itertools.product((False, True), repeat=2):
            expl = a and not d_  # Expl := Acc ∧ ¬Dec
            suff = (not (a and not d_)) or expl  # (Suff) as conjectured: Acc ∧ ¬Dec ⇒ Expl
            both = both and suff and expl_ok(a, d_, expl)  # the owner's condition: Acc ∧ Dec ⇒ ¬Expl
        parts.append(construction("(c) the owner's condition and (Suff) have a common model", "Expl := Acc ∧ ¬Dec meets Acc ∧ ¬Dec ⇒ Expl ((Suff) as conjectured) and Acc ∧ Dec ⇒ ¬Expl (S41, Q2), on every candidate",
                                  both, "checked on the four values of (Acc, Dec); (E) itself takes no provenance (FC30): ¬Dec(t) stands beside it"))
    else:
        # S131 (decision S86, copy only): the provenance is one of three (FC78); (Suff) Acc ∧ Con ⇒ Expl; the owner's
        # condition Acc ∧ ¬Con ⇒ ¬Expl. Reworded: Expl := Acc ∧ Con. As written (round 4): Expl := Acc ∧ ¬Dec.
        old_common = True
        for a, kind in itertools.product((False, True), ("Sel", "Con", "Dec")):
            k_, d_ = kind == "Con", kind == "Dec"
            expl = (a and k_) if _cb.CLAIMS_REWORDED else (a and not d_)
            suff = (not (a and k_)) or expl
            both = both and suff and expl_ok(a, d_, expl, con=k_)
            # the round-4 (Suff) (Acc ∧ ¬Dec ⇒ Expl) beside S86's owner's condition: is there any value of Expl meeting both?
            old_common = old_common and any(((not (a and not d_)) or e) and expl_ok(a, d_, e, con=k_) for e in (False, True))
        parts.append(construction("(c) the owner's condition and (Suff) have a common model",
                                  ("Expl := Acc ∧ Con meets Acc ∧ Con ⇒ Expl ((Suff), S86) and Acc ∧ ¬Con ⇒ ¬Expl (S41 Q2, S86), on every candidate" if _cb.CLAIMS_REWORDED
                                   else "Expl := Acc ∧ ¬Dec meets Acc ∧ ¬Dec ⇒ Expl ((Suff) as conjectured) and Acc ∧ Dec ⇒ ¬Expl (S41, Q2), on every candidate"),
                                  both, "S131 (S86): checked on the six values of (Acc, provenance), the provenance one of Sel, Con, Dec (FC78); "
                                  "(E) itself takes no provenance (FC30): Con(t) stands beside it; the round-4 (Suff) (Acc ∧ ¬Dec ⇒ Expl) "
                                  "beside S86's owner's condition has a common model: %s (none at Acc with a selected transport)" % old_common))'''),
    ('(d)', '''            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
            rows.append("%s, %s: fixed points %s; Dec(t) at o2 %s; Def(L17, S41) %s" % (lab, rd, prov_show(2, fps), decs, [suff_defeats(acc, d, out, "L17 (S41)") for d in decs]))
            if rd != "K":
                ok = ok and fps != [] and all(decs) and not any(suff_defeats(acc, d, out, "L17 (S41)") for d in decs)''',
     '''            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
            cons = [sc[1][1] for R, sc in fps]  # S131: Con(t) at o2, passed to (Suff)
            rows.append("%s, %s: fixed points %s; Dec(t) at o2 %s; Def(L17, S41) %s" % (lab, rd, prov_show(2, fps), decs, [suff_defeats(acc, d, out, "L17 (S41)", con=k_) for d, k_ in zip(decs, cons)]))
            if rd != "K":
                ok = ok and fps != [] and all(decs) and not any(suff_defeats(acc, d, out, "L17 (S41)", con=k_) for d, k_ in zip(decs, cons))'''),
    ('(e)', '''        dec = all(not sc[0][0] and not sc[0][1] for R, sc in fps)
        res[hn] = (dec, suff_defeats(acc, dec, out, "L17 (S41)"))''',
     '''        dec = all(not sc[0][0] and not sc[0][1] for R, sc in fps)
        con_ = bool(fps) and all(sc[0][1] for R, sc in fps)  # S131: Con(t), passed to (Suff)
        res[hn] = (dec, suff_defeats(acc, dec, out, "L17 (S41)", con=con_))'''),
    ('(e) check', '''    parts.append(computed("(e) a link no pair tried and nobody worked out (B8, FC77)", "after round 2 it is selected (H = ∅), so ¬Dec and Q2's condition misses it; with H ≠ ∅ it is declared and the owner's condition applies",
                          res[False] == (False, True) and res[True] == (True, False), "\\n".join(rows), ["I90"]))''',
     '''    # S131 (S86, copy only): with explanation kept for constructed transports, the owner's condition reaches the link
    # under both D12.1s (selected or declared, never constructed), so it is outside (Suff)'s defeat set under both
    e_stmt = ("after round 2 it is selected (H = ∅) and with H ≠ ∅ it is declared; neither is constructed, so under S86 the owner's condition applies under both and Q2's condition no longer misses it"
              if _cb.s131_wording() else "after round 2 it is selected (H = ∅), so ¬Dec and Q2's condition misses it; with H ≠ ∅ it is declared and the owner's condition applies")
    e_ok = (res[False] == (False, False) and res[True] == (True, False)) if _cb.s131_wording() else (res[False] == (False, True) and res[True] == (True, False))
    parts.append(computed("(e) a link no pair tried and nobody worked out (B8, FC77)", e_stmt,
                          e_ok, "\\n".join(rows), ["I90"]))'''),
    ('(g)', '''        res[kind] = (outn and not pres, outn and not (acc and not dec))''',
     '''        # S131 (S86, copy only): L61 now reads Account ∧ Con(t), so 'their' after R3A1-T1 has Acc ∧ Con as antecedent
        res[kind] = (outn and not pres, outn and not (acc and (k_ if _cb.EXPL_BY_CONSTRUCTION else not dec)))'''),
    ('(g) check', '''    ok_g = acc and pres and res["Dec"] == (False, True) and res["Con"] == (False, False) and res["Sel"] == (False, False)
    parts.append(computed("(g) L61's (Nec) against L538 (critical review, objection 3)",
                          "the student's declared copy, with an argument not using (E) that rules out ¬Expl(ℰ): in the defeat set of (Nec) as L61's 'their' reads after R3A1-T1 (necessity of Account ∧ ¬Dec), not in L538's (a transport, t, preserves E on C); with a constructed or selected transport in neither: the two differ exactly on Dec, which L538 names nowhere",''',
     '''    ok_g = acc and pres and res["Dec"] == (False, True) and res["Con"] == (False, False) and res["Sel"] == ((False, True) if _cb.s131_wording() else (False, False))
    parts.append(computed("(g) L61's (Nec) against L538 (critical review, objection 3)",
                          ("the student's declared copy, with an argument not using (E) that rules out ¬Expl(ℰ): in the defeat set of (Nec) as L61's 'their' reads after R3A1-T1 (necessity of Account ∧ Con, S131: S86), not in L538's (a transport, t, preserves E on C); a selected transport likewise; a constructed one in neither: the two differ exactly on the transports not constructed, which L538 names nowhere"
                           if _cb.s131_wording() else
                           "the student's declared copy, with an argument not using (E) that rules out ¬Expl(ℰ): in the defeat set of (Nec) as L61's 'their' reads after R3A1-T1 (necessity of Account ∧ ¬Dec), not in L538's (a transport, t, preserves E on C); with a constructed or selected transport in neither: the two differ exactly on Dec, which L538 names nowhere"),'''),
    ('(h)', '''    inside = {rd: suff_defeats(acc, dec_c, bool([a for a in xh if not_using_E(a, c.name, rd)]), "L536") for rd in USES_READINGS}''',
     '''    inside = {rd: suff_defeats(acc, dec_c, bool([a for a in xh if not_using_E(a, c.name, rd)]), "L536", con=k_c) for rd in USES_READINGS}  # S131: Con passed'''),
]

S106_CHANGES = [
    ('import', "from .args import Assessor, Imp, Not\n",
     "from .args import Assessor, Imp, Not\nfrom . import claims_b as _cb  # S131 (copy only): the S86 switches, read at call time\n"),
    ('(f)', '''            d = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            expl = acc and not dec  # Expl := Acc ∧ ¬Dec, FC30.new1 (c)'s common model
            rows.append("%s, %s (Sel %s, Con %s, Dec %s), argument usable %s: %s; Acc ∧ Dec ⇒ ¬Expl with Expl := Acc ∧ ¬Dec: %s"
                        % (c.name, kind, s_, k_, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS), expl_ok(acc, dec, expl)))
            ok_f = ok_f and out and expl_ok(acc, dec, expl) and d["L17 (S41)"] == d["L536"]
            if kind == "Dec":
                ok_f = ok_f and dec and not d["L17 (S41)"] and d["L17 as text 104 words it"]
            if kind == "Con":
                ok_f = ok_f and not dec and d["L17 (S41)"]''',
     '''            d = {r: suff_defeats(acc, dec, out, r, con=k_) for r in SUFF_READINGS}  # S131: Con passed
            # Expl := Acc ∧ ¬Dec, FC30.new1 (c)'s common model; S131 (S86, copy only): Expl := Acc ∧ Con in the S131 wording
            expl = (acc and k_) if _cb.s131_wording() else (acc and not dec)
            rows.append("%s, %s (Sel %s, Con %s, Dec %s), argument usable %s: %s; %s: %s"
                        % (c.name, kind, s_, k_, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS),
                           ("Acc ∧ ¬Con ⇒ ¬Expl with Expl := Acc ∧ Con" if _cb.s131_wording() else
                            ("Acc ∧ ¬Con ⇒ ¬Expl with Expl := Acc ∧ ¬Dec" if _cb.EXPL_BY_CONSTRUCTION else "Acc ∧ Dec ⇒ ¬Expl with Expl := Acc ∧ ¬Dec")),
                           expl_ok(acc, dec, expl, con=k_)))
            ok_f = ok_f and out and expl_ok(acc, dec, expl, con=k_) and d["L17 (S41)"] == d["L536"]
            if kind == "Dec":
                ok_f = ok_f and dec and not d["L17 (S41)"] and d["L17 as text 104 words it"]
            if kind == "Con":
                ok_f = ok_f and not dec and d["L17 (S41)"]
            if kind == "Sel" and _cb.s131_wording():  # S131 (S86): a selected sign is no explanation, as a declared one
                ok_f = ok_f and not d["L17 (S41)"] and d["L17 as text 104 words it"]'''),
    ('(f) statement', '''                          "ℰ_two and ℰ_one meet (E); with a declared transport (Dec) and an argument not using (E) that rules out Expl(ℰ), each is outside (Suff)'s defeat set as S41 writes it "
                          "and as L536 writes it (Acc ∧ Dec ⇒ ¬Expl applies), inside it as text 104's L17 words it; with a constructed transport it is inside all three (as FC30.new1 (a))",''',
     '''                          "ℰ_two and ℰ_one meet (E); with a declared transport (Dec) and an argument not using (E) that rules out Expl(ℰ), each is outside (Suff)'s defeat set as S41 writes it "
                          "and as L536 writes it (Acc ∧ Dec ⇒ ¬Expl applies), inside it as text 104's L17 words it; with a constructed transport it is inside all three (as FC30.new1 (a))"
                          + ("; with a selected transport, as with a declared one (S131: S86, Acc ∧ ¬Con ⇒ ¬Expl)" if _cb.s131_wording() else ""),'''),
]

COREFILE_CHANGE = ('NAME = "formal core, after round 4, with Reading C and the graded survival condition - a copy.md"  # S129 (copy only): the core copy beside this program\'s folder',
                   'NAME = "%s"  # S131 (copy only): the core copy beside this program\'s folder' % CORE_NAME)


def head(note):
    return '# S131 (decision S86), 2 October 2026: a COPY of S129\'s copy of this file (%s), with "explanation" kept for\n# constructed transports carried in (every change marked "S131"); written by tools/s131_write_the_core_and_program_copies.py.\n' % note


def main():
    before = {'s107 core': md5f(os.path.join(S107, 'formal core, after round 4.md')), 's107 model': tree_md5(os.path.join(S107, 'model after round 4')),
              's107 claims': md5f(os.path.join(S107, 'formal claims, after round 4.md')),
              's129 core': md5f(SRC_CORE), 's129 model': tree_md5(SRC_MODEL)}
    os.makedirs(OUT_DIR, exist_ok=True)
    core = open(SRC_CORE, encoding='utf-8').read()
    for lab, old, new in CORE_CHANGES:
        core = replace_once(core, old, new, lab)
    core = CORE_NOTE.format(md5=before['s129 core'], md5_107=before['s107 core']) + core
    open(OUT_CORE, 'w', encoding='utf-8').write(core)
    if os.path.exists(OUT_MODEL):
        shutil.rmtree(OUT_MODEL)
    shutil.copytree(SRC_MODEL, OUT_MODEL, ignore=shutil.ignore_patterns('__pycache__'))
    for fn, changes in (('claims_b.py', B_CHANGES), ('claims_s41.py', S41_CHANGES), ('claims_s106.py', S106_CHANGES)):
        p = os.path.join(OUT_MODEL, 'model', fn)
        s = open(p, encoding='utf-8').read()
        for lab, old, new in changes:
            s = replace_once(s, old, new, '%s: %s' % (fn, lab))
        open(p, 'w', encoding='utf-8').write(head(fn) + s)
    cf = os.path.join(OUT_MODEL, 'model', 'corefile.py')
    t = open(cf, encoding='utf-8').read()
    t = replace_once(t, COREFILE_CHANGE[0], COREFILE_CHANGE[1], 'corefile')
    open(cf, 'w', encoding='utf-8').write(t)
    after = {'s107 core': md5f(os.path.join(S107, 'formal core, after round 4.md')), 's107 model': tree_md5(os.path.join(S107, 'model after round 4')),
             's107 claims': md5f(os.path.join(S107, 'formal claims, after round 4.md')),
             's129 core': md5f(SRC_CORE), 's129 model': tree_md5(SRC_MODEL)}
    assert before == after, 'an original changed'
    copy = tree_md5(OUT_MODEL)
    changed = sorted(k for k in copy if copy[k] != before['s129 model'].get(k))
    assert changed == ['model/claims_b.py', 'model/claims_s106.py', 'model/claims_s41.py', 'model/corefile.py'], changed
    assert set(copy) == set(before['s129 model'])
    print('S107 core md5 %s, S107 claims md5 %s (unchanged)' % (before['s107 core'], before['s107 claims']))
    print('S129 core copy md5 %s (unchanged); S131 core copy %s' % (before['s129 core'], md5f(OUT_CORE)))
    print('program copy: %d files; changed from S129\'s copy: %s; the other %d byte-equal' % (len(copy), changed, len(copy) - len(changed)))
    for k in changed:
        print('  %s: S129 %s, S131 %s' % (k, before['s129 model'][k], copy[k]))


if __name__ == '__main__':
    main()
