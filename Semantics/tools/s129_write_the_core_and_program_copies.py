#!/usr/bin/env python3
"""s129_write_the_core_and_program_copies.py

What it does, in plain words: for log S129 (decisions S83 and S84), writes COPIES of the formal core after round 4 and
of the model program after round 4 into results/S129 Reading C carried into copies/, with the two decisions carried in:
  S83 (Reading C): the history in the definition of a selected correspondence (D12.1) is read inside the system boundary
      declared for the claim; a holding whose correspondence entered the boundary whole from outside represents
      nothing there (D12.1, D12.2, D12.3, D12.4, D12.5, D15.4 of the core copy; Hist, sel, con and the provenance fixed
      points of the program copy);
  S84 (the graded survival condition): D12.1's survival condition asks that fidelity on H changes which members persist
      or are copied (Adv in the core copy's D12.1; Hist.advantage and sel in the program copy).
Every change is an exact replacement that must match once, or the script stops; each is marked [S129: ...] in the core
copy and "# S129" in the program copy. Notes (not changes) are added where Reading C reaches a definition that is not
changed here (D13.1, D16.3, D16.XV). The originals in results/S107 Round 4 - maths after the reading/ are read, never
written; the script checks their md5s before and after, and checks that the program copy's other files are byte-equal
to the original's.

  python3 -B Semantics/tools/s129_write_the_core_and_program_copies.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import hashlib, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading')
SRC_CORE = os.path.join(SRC_DIR, 'formal core, after round 4.md')
SRC_MODEL = os.path.join(SRC_DIR, 'model after round 4')
OUT_DIR = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies')
CORE_NAME = 'formal core, after round 4, with Reading C and the graded survival condition - a copy.md'
OUT_CORE = os.path.join(OUT_DIR, CORE_NAME)
OUT_MODEL = os.path.join(OUT_DIR, 'model after Reading C')


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
CORE_NOTE = """*S129 (decisions S83 and S84), 2 October 2026: a COPY, not the theory's formal core. It is `results/S107 Round 4 - maths after the reading/formal core, after round 4.md` (md5 {md5}; not written to) with the owner's two decisions of 2 October 2026 carried in, each change marked [S129: S83 …] or [S129: S84 …] with what it was, and three notes marked [S129: … a consequence, not a change] where Reading C reaches a definition left as it is; nothing else is altered, and every line below this note is the original's or a marked change of it. S83 (Reading C, "Oh clearly C."): the history in the definition of a selected correspondence is read inside the system boundary β declared for the claim (D12.1, D12.2, D12.3, D12.4, D12.5, D15.4; text 129 L193, L195, L522, which are text 107's L193, L195, L522). S84 ("Well yes. That is how selected is defined."): the survival condition asks a graded advantage, Adv (D12.1; text 129 L195). Inventions of this copy, provisional and not in the register (the register is the theory's): **[I198]** h_β(t), the occurrences of h(t, o_t) inside β with ≺ restricted; a case that states a history and declares no boundary is read with every occurrence it states inside β, which gives the original's verdicts (others: such a case left open, as text 129's L522 would have it read strictly; β the holder's own occurrences only). **[I199]** Adv_{{h(t)}}(H) read through Θ, by hand in the program (I90); a case that states no fact about rates is read as a requirement of fidelity, one such condition, which gives the original's verdicts (others: such a case left open; 'other things in the population being equal' made a computed comparison, which S127's item 4 (b), linked correspondences, would need). **[I200]** EnteredWhole_β computed from D12.3's chain of content-preserving transfers: a holding inside β reached by such transfers from a holding outside β; a routine written outside β and run inside it counts, its correspondence a record of its writers' (L211, L427) (others: EnteredWhole a primitive read through Θ; 'whole' read part by part, D12.4, a binding newly built inside β being constructed, L405). **[I201]** Reading C applied to Con (an episode of h_β) and to Sel's ¬CT (h′ ⊆ h_β(t)) as well as to Sel's exclusion, reading text 129's "A provenance is relative to the boundary declared" as said of all three provenances (other: C applied only to D12.1's exclusion and D12.3's record clause, the two places S127's formal sketch names). Program: `model after Reading C/` beside this file (its `model/corefile.py` reads this file); record: `results/S129 Reading C carried into copies - what changes.md`. Nothing is settled (S28).*

"""

CORE_CHANGES = [
    ('D12.1 surv (S84)',
     "surv(t, H) :⟺ Faithful_H(t) (D5.7) ∧ Env_{h(t)}(value_t|_H), ",
     "surv(t, H) :⟺ Faithful_H(t) (D5.7) ∧ Env_{h(t)}(value_t|_H) ∧ Adv_{h(t)}(H), "),
    ('D12.1 Adv (S84)',
     "none given: Env ≡ ⊤ **[I177]** [r3: A3; W6: was 'Faithful_H(t) (D5.7)' alone; FC80.new1]",
     "none given: Env ≡ ⊤ **[I177]** [r3: A3; W6: was 'Faithful_H(t) (D5.7)' alone; FC80.new1]; Adv_{h(t)}(H) :⟺ in h(t), "
     "fidelity on H changes which members of 𝒯 persist or are copied: members faithful on H persist or are copied at a higher "
     "rate than members not faithful on H, other things in the population being equal, read through Θ; a requirement (only "
     "members faithful on H persist or are copied) is one such condition, and a history in which fidelity on H made no "
     "difference to persisting or being copied gives ¬Adv **[I199]** [S129: S84, copy only: was 'surv(t, H) :⟺ "
     "Faithful_H(t) (D5.7) ∧ Env_{h(t)}(value_t|_H)'; text 129 L195]"),
    ('D12.1 exclusion (S83)',
     "and ¬∃o ≺_{h(t)} o_t, x ∈ {t, H, surv, cod t}: Rep(o, x) (D12.5; x typed by D11.2), where Sel, Con and Dec are of a "
     "holding (t, o_t), o_t an occurrence at which t is held, and h(t) := h(t, o_t) is the history that produced that holding, "
     "its preparing episode included **[I52, I53, I128, I162, I167]**",
     "and ¬∃o ≺_{h_β(t)} o_t, x ∈ {t, H, surv, cod t}: Rep_β(o, x) (D12.5; x typed by D11.2), where Sel, Con and Dec are of a "
     "holding (t, o_t) at a declared boundary β (D15.4), o_t an occurrence at which t is held, h(t) := h(t, o_t) is the "
     "history that produced that holding, its preparing episode included **[I52, I53, I128, I162, I167]**, and h_β(t) := "
     "h_β(t, o_t) is its occurrences inside β, ≺ restricted; a holding inside β whose correspondence entered β whole "
     "represents nothing at β (D12.3) **[I198, I200]** [S129: S83, copy only: was '¬∃o ≺_{h(t)} o_t, x ∈ {t, H, surv, cod "
     "t}: Rep(o, x)', h(t) read whole, no β; text 129 L193, L195]"),
    ('D12.1 no trace (S83)',
     "and ¬∃h' ⊆ h(t): CT(h', t) (D12.2) **[I161]**",
     "and ¬∃h' ⊆ h_β(t): CT(h', t) (D12.2) **[I161, I201]** [S129: S83, copy only: was 'h' ⊆ h(t)']"),
    ('D12.2 (S83)',
     "Con(t; h, e) :⟺ some episode h' of h up to e",
     "Con(t; h, e) :⟺ at the declared β, some episode h' of h_β up to e [S129: S83, copy only: was 'some episode h' of h "
     "up to e'; I201]"),
    ('D12.3 (S83)',
     "**D12.3 Declared.** A holding (t, o') reached from a holding (t, o) by a composition of content-preserving transfers "
     "(relay, record; TransferComposite, D13.3) has prov(t, o') := prov(t, o), part by part (D12.4); for every other holding, "
     "Dec(t, o_t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·), both read on h(t, o_t) (D12.1)",
     "**D12.3 Declared.** At a declared boundary β (D15.4): a holding (t, o') with o' inside β reached from a holding (t, o) "
     "with o inside β by a composition of content-preserving transfers (relay, record; TransferComposite, D13.3) has "
     "prov_β(t, o') := prov_β(t, o), part by part (D12.4); a holding (t, o') with o' inside β reached so from a holding "
     "outside β has entered β whole, EnteredWhole_β(t, o'), and Dec_β(t, o'): it represents nothing at β, and what it "
     "carries is a contribution from outside β (L427); a routine written outside β and run inside it is such a holding, its "
     "correspondence a record of its writers' (L211) **[I200]** [S129: S83, copy only: was 'A holding (t, o') reached from a "
     "holding (t, o) by a composition of content-preserving transfers … has prov(t, o') := prov(t, o), part by part (D12.4)', "
     "with no β; text 129 L195]; for every other holding, Dec_β(t, o_t) :⟺ no parameters give Sel(t; ·) and none give "
     "Con(t; ·) at β, both read on h_β(t, o_t) (D12.1)"),
    ('D12.4 (S83)',
     "A content-preserving transfer (relay or record) from carrier o to o' gives each part at o' the value it had at o; a "
     "binding newly built gets Con.",
     "A content-preserving transfer (relay or record) from carrier o to o' gives each part at o' the value it had at o, "
     "when o and o' are inside the declared β; from outside β, Dec_β (D12.3) [S129: S83, copy only: 'when o and o' are "
     "inside …' added]; a binding newly built gets Con."),
    ('D12.5 (S83)',
     "and some parameters give Sel(t; ·) or Con(t; ·). Org_ℓ is the one thing (R) takes from Θ (L213).",
     "and some parameters give Sel(t; ·) or Con(t; ·) at β (D12.1, D12.2, read on h_β); Rep_ℓ with no β written is "
     "Rep_{ℓ,β} at the boundary declared for the claim (L524) [S129: S83, copy only: was '… give Sel(t; ·) or Con(t; ·).', "
     "no β]. Org_ℓ is the one thing (R) takes from Θ (L213)."),
    ('D15.4 (S83)',
     "Both are fixed before the attribution (L473).",
     "Both are fixed before the attribution (L473). β also indexes a claim of provenance, and so of representation "
     "(D12.1–D12.5; text 129 L193, L195, L522): which occurrences of a history are inside the system whose holding is in "
     "question; it is declared before the attribution, not chosen after it [S129: S83, copy only: sentence added]."),
    ('D13.1 note (S83)',
     "Can_{Ω,β}(ξ, U; χ) holds for some χ with a realization that uses o **[I55]**.",
     "Can_{Ω,β}(ξ, U; χ) holds for some χ with a realization that uses o **[I55]**. [S129: S83, a consequence, not a change: "
     "Rep_ℓ(o, c) here is read at Deploy's β (D12.5 in this copy), so content that entered β whole by relay (Dec_β, D12.3) "
     "is not deployable at β, and not in R_{β,ℓ} (D13.2) or R_{<e} (N), until it is reconstructed inside β (Build; L405: "
     "'Reconstruction by a learner is construction') or selected there]"),
    ('D16.3 note (S83)',
     "whose provenance was relayed from outside β **[I154]**.",
     "whose provenance was relayed from outside β **[I154]**. [S129: S83, a consequence, not a change: at β, an occurrence "
     "whose provenance was relayed from outside β has Dec_β (D12.3 in this copy) and no Rep_β, so read at β this clause is "
     "never met and NQB asks nothing; it needs rewording, for example 'an occurrence o with Held_ℓ(o, c) and "
     "EnteredWhole_β', or Rep read at a boundary that contains the source; not made here]"),
    ('D16.XV note (S83)',
     "the program's reading of a definition]",
     "the program's reading of a definition] [S129: S83, a consequence, not a change: Dec(t) is Dec_β(t) at the boundary "
     "declared for the claim, and Expl(ℰ), like every claim, is read at the same β (L524); read with no index, the owner's "
     "condition (Acc ∧ Dec ⇒ ¬Expl, S41 Q2) and (Suff) as conjectured (Acc ∧ ¬Dec ⇒ Expl) have no common model once one t "
     "is Sel at one declared boundary and Dec at another (S129, FC30.new1 (c) recomputed across two boundaries); with "
     "Expl_β they have one]"),
]

# ---- the program --------------------------------------------------------------------------------------------------
PROG_CHANGES = [
    ('import os', "import itertools\nimport inspect\n",
     "import itertools\nimport inspect\nimport os  # S129 (copy only): the two switches below are read from the environment\n"),
    ('Hist', """    def __init__(self, occ, rep, occurs, admitted=True, prepares=False, contracts=None, records=None):
        self.occ, self.rep, self.occurs, self.admitted, self.prepares = occ, set(rep), set(occurs), admitted, prepares
""", """    def __init__(self, occ, rep, occurs, admitted=True, prepares=False, contracts=None, records=None,
                 beta=None, source=None, advantage=None):
        self.occ, self.rep, self.occurs, self.admitted, self.prepares = occ, set(rep), set(occurs), admitted, prepares
        # S129 (decision S83, Reading C; copy only): beta, the occurrences inside the system boundary declared for the
        # claim (None: every occurrence the case states is inside, I198, which gives the original's verdicts); source,
        # o -> the occurrence whose holding o's holding is a content-preserving transfer (relay, record) of, so that a
        # holding reached from outside beta has entered it whole (D12.3 in the core copy, I200). S129 (decision S84):
        # advantage, read through Θ by hand (I90, I199): True, fidelity on H raised the rate at which members persisted or
        # were copied in h(t); False, it made no difference; None, the case states no rate fact (read as a requirement of
        # fidelity, one such condition, which gives the original's verdicts).
        self.beta = None if beta is None else set(beta)
        self.source = dict(source or {})
        self.advantage = advantage
"""),
    ('helpers', "def faithful_on(cand, H):\n", '''# ---- S129 (decisions S83 and S84), copy only ------------------------------------------------------------------
# READING_C: D12.1's history read inside the declared boundary (text 129 L193, L195, L522; the core copy's D12.1 to
# D12.5 and D15.4). GRADED: D12.1's survival condition read as a graded advantage (text 129 L195; Adv in the core copy's
# D12.1). Both on by default; S129_READING_C=0 or S129_GRADED=0 in the environment switches one off, for comparison.
# With both off, or with no boundary and no rate fact stated by a case, the program computes what the original does.
READING_C = os.environ.get("S129_READING_C", "1") == "1"
GRADED = os.environ.get("S129_GRADED", "1") == "1"


def _in(beta, x):
    """x is inside the declared boundary beta (a set), or no boundary is declared, or Reading C is off (I198)."""
    return (not READING_C) or beta is None or x in beta


def inside(h, o):
    """o is inside the boundary h declares for the claim (I198)."""
    return _in(getattr(h, "beta", None), o)


def entered_whole(h, o):
    """EnteredWhole_β (D12.3 in the core copy, I200): o is inside β and its holding is reached, by content-preserving
    transfers (h.source), from a holding outside β. False when Reading C is off or no boundary is declared."""
    beta = getattr(h, "beta", None)
    if not READING_C or beta is None or o not in beta:
        return False
    seen, x = set(), o
    while x in h.source and x not in seen:
        seen.add(x)
        x = h.source[x]
        if x not in beta:
            return True
    return False


def rep_at_beta(h):
    """The (occurrence, item) tags that count as Rep at β (Sel's exclusion): inside β and not entered whole."""
    return [(o, x) for (o, x) in h.rep if inside(h, o) and not entered_whole(h, o)]


def held_at_beta(h):
    """The tags that count as Held for Con (Held asks no provenance, D18.1): inside β, entered whole or not."""
    return [(o, x) for (o, x) in h.rep if inside(h, o)]


def faithful_on(cand, H):
'''),
    ('sel graded', """    if env is not None and not env(cand, H):
        return False
    if not (h.admitted and pop_admitted):
""", """    if env is not None and not env(cand, H):
        return False
    # S129 (S84, copy only): surv asks also Adv_{h(t)}(H), that fidelity on H changed which members persisted or were
    # copied (a requirement is one such condition); a history stated to give no such difference fails it (I199).
    if GRADED and getattr(h, "advantage", None) is False:
        return False
    if not (h.admitted and pop_admitted):
"""),
    ('sel exclusion', "    return not any(x in banned for (_, x) in h.rep)\n",
     "    # S129 (S83, copy only): only occurrences inside β that did not enter it whole can represent at β (D12.1, D12.3 of\n"
     "    # the core copy); with no boundary declared every tag counts, as before.\n"
     "    return not any(x in banned for (_, x) in rep_at_beta(h))\n"),
    ('con 1', "        return episode(None, None, reading) and any(x in (\"t\", cod) for (_, x) in h.rep)\n",
     "        return episode(None, None, reading) and any(x in (\"t\", cod) for (_, x) in held_at_beta(h))  # S129 (S83): inside β\n"),
    ('con 2', "        if episode(qs[i:], rs[i:] if rs else None, reading) and any(x in (\"t\", cod) and o in sub for (o, x) in h.rep):\n",
     "        if episode(qs[i:], rs[i:] if rs else None, reading) and any(x in (\"t\", cod) and o in sub for (o, x) in held_at_beta(h)):  # S129 (S83)\n"),
    ('_con_at sig', "def _con_at(o, held, trace, rd, R, eps=None):\n", "def _con_at(o, held, trace, rd, R, eps=None, beta=None):\n"),
    ('_con_at body', """        if rd == "U":
            ok = any(x in R for x in range(i, o + 1))
        elif rd == "K":
            ok = any(x in R for x in range(i, o))
        else:
            ok = any(held[x] for x in range(i, o + 1))
        if ok:
            return True
    return False
""", """        if rd == "U":
            ok = any(x in R for x in range(i, o + 1) if _in(beta, x))
        elif rd == "K":
            ok = any(x in R for x in range(i, o) if _in(beta, x))
        else:
            ok = any(held[x] for x in range(i, o + 1) if _in(beta, x))  # S129 (S83): only what is held inside β
        if ok:
            return True
    return False
"""),
    ('_prov_step', """def _prov_step(n, held, trace, selc, rd, i161, R, eps=None, rec_of=None):
    out = {}
    for o in range(n):
""", """def _prov_step(n, held, trace, selc, rd, i161, R, eps=None, rec_of=None, beta=None):
    out = {}
    for o in range(n):
        # S129 (S83, copy only): at a declared β (a set of indices), an occurrence outside β has no provenance at β (it is
        # not in h_β), and a holding inside β reached by a transfer from outside β has entered it whole: Dec_β (D12.3 of
        # the core copy, I200). A relay inside β of such a holding inherits Dec_β below.
        if not _in(beta, o):
            out[o] = (False, False)
            continue
        if rec_of is not None and rec_of[o] is not None and not _in(beta, rec_of[o]):
            out[o] = (False, False)
            continue
"""),
    ('_prov_step sets', """        before, upto = range(o), range(o + 1)
        c_ = _con_at(o, held, trace, rd, R, eps)
""", """        before, upto = [x for x in range(o) if _in(beta, x)], [x for x in range(o + 1) if _in(beta, x)]  # S129 (S83)
        c_ = _con_at(o, held, trace, rd, R, eps, beta)
"""),
    ('build_at', """def build_at(n, held, trace, rd, R, o):
    \"\"\"Build at o (D13.3): a construction trace whose output o is a represented organization, 'represented'
    read as the cut reads it (ExplUse, BindingConstruction, Owned, ¬TransferComposite set to hold, I56).\"\"\"
    if not trace[o]:
        return False
""", """def build_at(n, held, trace, rd, R, o, beta=None):
    \"\"\"Build at o (D13.3): a construction trace whose output o is a represented organization, 'represented'
    read as the cut reads it (ExplUse, BindingConstruction, Owned, ¬TransferComposite set to hold, I56).\"\"\"
    if not trace[o] or not _in(beta, o):  # S129 (S83): Build's subhistory is owned, inside β (D13.7)
        return False
"""),
    ('prov_fixed_points', """def prov_fixed_points(n, held, trace, selc, rd, i161=True, eps=None, rec_of=None):""",
     """def prov_fixed_points(n, held, trace, selc, rd, i161=True, eps=None, rec_of=None, beta=None):"""),
    ('prov_fixed_points call', "        sc = _prov_step(n, held, trace, selc, rd, i161, R, eps, rec_of)\n",
     "        sc = _prov_step(n, held, trace, selc, rd, i161, R, eps, rec_of, beta)  # S129 (S83): beta, the declared boundary\n"),
    ('DEP beta', "DEP_EXPLUSE_PRIMITIVE = dict(DEP, ExplUse=[])\n",
     "# S129 (S83, copy only): under Reading C, Sel, Con and Dec read the declared boundary β (D12.1 to D12.3 of the core copy).\n"
     "if READING_C:\n    for _n in (\"Sel\", \"Con\", \"Dec\"):\n        DEP[_n] = DEP[_n] + [\"β\"]\n"
     "DEP_EXPLUSE_PRIMITIVE = dict(DEP, ExplUse=[])\n"),
    ('surv sink', '             "Event": "defined (D11.1: a nonempty set of occurrences of a history; I45)"}\n',
     '             "Event": "defined (D11.1: a nonempty set of occurrences of a history; I45)"}\n'
     'if GRADED:  # S129 (S84, copy only): the survival condition asks also the graded advantage Adv (D12.1 of the core copy)\n'
     '    D0_2_R3A3["surv"] = D0_2_R3A3["surv"] + "; and Adv: fidelity on H changes which members persist or are copied, read through Θ (S84; I199)"\n'),
]

COREFILE_CHANGE = ('NAME = "formal core, after round 4.md"  # the formal core this program formalizes',
                   'NAME = "%s"  # S129 (copy only): the core copy beside this program\'s folder' % CORE_NAME)


def main():
    before = {'core': md5f(SRC_CORE), 'model': tree_md5(SRC_MODEL)}
    os.makedirs(OUT_DIR, exist_ok=True)
    core = open(SRC_CORE, encoding='utf-8').read()
    for lab, old, new in CORE_CHANGES:
        core = replace_once(core, old, new, lab)
    core = CORE_NOTE.format(md5=before['core']) + core
    open(OUT_CORE, 'w', encoding='utf-8').write(core)
    if os.path.exists(OUT_MODEL):
        shutil.rmtree(OUT_MODEL)
    shutil.copytree(SRC_MODEL, OUT_MODEL, ignore=shutil.ignore_patterns('__pycache__'))
    cb = os.path.join(OUT_MODEL, 'model', 'claims_b.py')
    s = open(cb, encoding='utf-8').read()
    for lab, old, new in PROG_CHANGES:
        s = replace_once(s, old, new, 'claims_b: ' + lab)
    s = ('# S129 (decisions S83 and S84), 2 October 2026: a COPY of model after round 4/model/claims_b.py with Reading C and the\n'
         '# graded survival condition carried in (every change marked "S129"); written by tools/s129_write_the_core_and_program_copies.py.\n') + s
    open(cb, 'w', encoding='utf-8').write(s)
    cf = os.path.join(OUT_MODEL, 'model', 'corefile.py')
    t = open(cf, encoding='utf-8').read()
    t = replace_once(t, COREFILE_CHANGE[0], COREFILE_CHANGE[1], 'corefile')
    open(cf, 'w', encoding='utf-8').write(t)
    after = {'core': md5f(SRC_CORE), 'model': tree_md5(SRC_MODEL)}
    assert before == after, 'an original changed'
    copy = tree_md5(OUT_MODEL)
    changed = sorted(k for k in copy if copy[k] != before['model'].get(k))
    assert changed == ['model/claims_b.py', 'model/corefile.py'], changed
    assert set(copy) == set(before['model'])
    print('original core md5 %s (unchanged); copy %s' % (before['core'], md5f(OUT_CORE)))
    print('program copy: %d files; changed: %s; the other %d byte-equal to the original' % (len(copy), changed, len(copy) - len(changed)))
    for k in changed:
        print('  %s: original %s, copy %s' % (k, before['model'][k], copy[k]))


if __name__ == '__main__':
    main()
