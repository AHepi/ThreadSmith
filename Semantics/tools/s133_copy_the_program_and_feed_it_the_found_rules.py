#!/usr/bin/env python3
"""s133_copy_the_program_and_feed_it_the_found_rules.py

What it does, in plain words: for log S133 (decisions S87 and S88). The owner's outside experiment (a four-stage visual
experiment with no neural network, built on the owner's own computer; only its read-me and report are here, in
tests/S133 Material - ...; its code is NOT here and is not run) reports three "found rules":
    a filled square of half-side 3:          max(abs(x), abs(y)) <= 3
    a filled disc of radius 3:               x*x + y*y <= 9
    straight-line motion:                    next = cur + (cur - prev) * lag
found by a "first-exact-fit search" over a fixed arithmetic grammar against supplied teaching measurements, with two
invented words ("tov", "mip") attached to the two shape rules afterwards.

This script
  1. copies S131's program copy (results/S131 Explanation by construction carried into copies/model after Reading C and
     explanation by construction/) into results/S133 The found rules fed to the copy/model, a copy of S131's program
     copy/, byte for byte, and checks every file's md5 against S131's (S129's and S131's files are read, never written);
  2. encodes the case by hand as MC2 of S133 (the name MC2 is the task's; S117's and S129's feeding uses MC2 for a
     different case, two programs differing at an unseen order, so this one is always written "MC2 (S133)"):
       - each found rule as an organization on a small finite world (the shapes on the integer grid from -4 to 4; the
         motion on positions 0 to 5 and lags 1 and 2), with the world's own law as the target, and asks the copy
         whether the rule, taken whole, meets the test of an account (E);
       - the search's history at two boundaries (the machine as run, with the scorer and the teaching measurements
         inside it and their writers outside; and a boundary taking in the designers), under two readings of the one
         fact the report does not give: whether the search's feedback only filters proposals from the grammar in a
         fixed order (reading S, the main reading: a population, a variation, a survival condition, no trace that
         prepares) or steers what is proposed next with the teaching measurements held (reading K, as S129's K8 reads
         training on a teacher's answers);
       - the two invented words, as content handed in by the teacher and stored against a slot;
       - the motion rule in two changed worlds (constant acceleration; a wall that bounces), where it fails: the
         copy's prediction, violation and surprise (D12.7) at each pair;
     and computes the verdicts under the copy's three decision switches (S83 Reading C, S84 graded advantage, S86
     explanation kept for what was worked out), all eight settings;
  3. checks, on templates (no data: nothing has run), that the provenance test of the S133 design tells its arms apart
     when encoded the same way: the subject's built repair, the repair handed over, and a search with a scorer and no
     held target.
Θ by hand (I90): which occurrence represents what, which holding is a record of which, and the rate fact are this
script's encoding, stated beside each case; the verdicts are the copy's.
Output: printed, and results/S133 The found rules fed to the copy/the found rules fed to the copy - computed.json.

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s133_copy_the_program_and_feed_it_the_found_rules.py

Written 3 October 2026 by the one Opus 5.5 agent of log S133. No Avida run, no outside model, nothing of the owner's
outside experiment run.
"""
import hashlib, json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S131_COPY = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies',
                         'model after Reading C and explanation by construction')
OUT_DIR = os.path.join(ROOT, 'results', 'S133 The found rules fed to the copy')
COPY = os.path.join(OUT_DIR, "model, a copy of S131's program copy")
OUTF = os.path.join(OUT_DIR, 'the found rules fed to the copy - computed.json')


def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def files_of(top):
    out = {}
    for d, dirs, fs in os.walk(top):
        dirs[:] = [x for x in dirs if x != '__pycache__']
        for f in fs:
            if f.endswith('.pyc'):
                continue
            p = os.path.join(d, f)
            out[os.path.relpath(p, top)] = md5(p)
    return out


# ---- 1. the copy ------------------------------------------------------------------------------------------------------
before = files_of(S131_COPY)
if not os.path.isdir(COPY):
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copytree(S131_COPY, COPY, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
mine = files_of(COPY)
assert mine == before, 'the copy differs from S131 program copy'
sys.path.insert(0, COPY)
for k in ('S129_READING_C', 'S129_GRADED', 'S131_EXPL_BY_CONSTRUCTION'):
    os.environ.setdefault(k, '1')

from model import claims_b as cb  # noqa: E402
assert os.path.dirname(os.path.dirname(os.path.abspath(cb.__file__))) == COPY, cb.__file__
from model.core import ONE, Org, Question, PortQuery, Candidate, Translation, account, faithful, F1_at, F2eq_at, A_at  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on, prov_fixed_points, viol_at  # noqa: E402
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok  # noqa: E402
from model.args import Assessor, Imp, Not  # noqa: E402

SETTINGS = [('C on, graded on, S86 on', True, True, True), ('C on, graded on, S86 off', True, True, False),
            ('C off, graded off, S86 on', False, False, True), ('C off, graded off, S86 off', False, False, False),
            ('C on, graded off, S86 on', True, False, True), ('C off, graded on, S86 on', False, True, True),
            ('C on, graded off, S86 off', True, False, False), ('C off, graded on, S86 off', False, True, False)]


def org(name, ports, dom, comps, foot, B, A, rel):
    return Org(name, ports, dom, comps, foot, B, A, lambda a2, a1: None, rel)


def ident(ports):
    return {v: Translation((v,)) for v in ports}


# ---- 2a. the found rules as organizations on small finite worlds ------------------------------------------------------
GRID = range(-4, 5)
SQUARE = lambda x, y: int(max(abs(x), abs(y)) <= 3)
DISC = lambda x, y: int(x * x + y * y <= 9)


def shape_case(world, rule, wname, rname):
    """The world's shape (the target) and a found rule (the candidate), one boundary label per grid point; the question
    reads the port 'on' (is the pixel at (x, y) lit?). As S117's NOT program: one component sets the place from the
    boundary label, one holds the law."""
    B = ['x%+dy%+d' % (x, y) for x in GRID for y in GRID]
    xy = {('x%+dy%+d' % (x, y)): (x, y) for x in GRID for y in GRID}
    dom = {'x': tuple(GRID), 'y': tuple(GRID), 'on': (0, 1)}
    D = org('D_world(%s)' % wname, ['x', 'y', 'on'], dom, ['c_xy', 'c_shape'], {'c_xy': ('x', 'y'), 'c_shape': ('x', 'y', 'on')},
            B, [ONE], lambda j, a, b: {xy[b]} if j == 'c_xy' else {(x, y, world(x, y)) for x in GRID for y in GRID})
    p = Question(D, [(ONE, b) for b in B], B[0], PortQuery(), 'on', name='p_%s' % wname)
    E = org('E_rule(%s)' % rname, ['x', 'y', 'on'], dom, ['e_xy', 'e_rule'], {'e_xy': ('x', 'y'), 'e_rule': ('x', 'y', 'on')},
            B, [ONE], lambda j, a, b: {xy[b]} if j == 'e_xy' else {(x, y, rule(x, y)) for x in GRID for y in GRID})
    c = Candidate(E, p, ident(['x', 'y', 'on']), {ONE: ONE}, {b: b for b in B},
                  {'e_xy': (frozenset(['c_xy']), ident(['x', 'y'])), 'e_rule': (frozenset(['c_shape']), ident(['x', 'y', 'on']))},
                  ['e_xy', 'e_rule'], 'on', name=rname)
    return p, c


POS, LAGS = range(0, 6), (1, 2)
WALL = 7


def straight(p, c, l):
    return c + (c - p) * l


def accelerating(p, c, l):            # the velocity grows by one each frame: a constant pull
    return c + (c - p) * l + l * (l + 1) // 2


def bouncing(p, c, l):                # straight-line motion with a wall at position 7 that reflects
    r = c + (c - p) * l
    return 2 * WALL - r if r > WALL else r


WORLDS = {ONE: straight, 'accelerating': accelerating, 'bounce at a wall': bouncing}


def motion_case(edits):
    """The world's motion (the target, with the admitted edits in `edits`, each a changed world) and the found motion
    rule (the candidate, whose law does not change with the edit). One boundary label per (prev, cur, lag)."""
    trip = [(p, c, l) for p in POS for c in POS for l in LAGS]
    B = ['p%dc%dl%d' % t for t in trip]
    tv = dict(zip(B, trip))
    vals = sorted({f(*t) for f in WORLDS.values() for t in trip})
    dom = {'prev': tuple(POS), 'cur': tuple(POS), 'lag': LAGS, 'nxt': tuple(vals)}
    ports = ['prev', 'cur', 'lag', 'nxt']
    A = [ONE] + [a for a in edits if a != ONE]
    D = org('D_world(motion)', ports, dom, ['c_in', 'c_motion'], {'c_in': ('prev', 'cur', 'lag'), 'c_motion': tuple(ports)},
            B, A, lambda j, a, b: {tv[b]} if j == 'c_in' else {t + (WORLDS[a](*t),) for t in trip})
    E = org('E_rule(cur + (cur - prev) * lag)', ports, dom, ['e_in', 'e_rule'], {'e_in': ('prev', 'cur', 'lag'), 'e_rule': tuple(ports)},
            B, A, lambda j, a, b: {tv[b]} if j == 'e_in' else {t + (straight(*t),) for t in trip})
    C = [(a, b) for a in A for b in B]
    p = Question(D, C, B[0], PortQuery(), 'nxt', name='p_motion(%s)' % ', '.join(str(a) for a in A))
    c = Candidate(E, p, ident(ports), {a: a for a in A}, {b: b for b in B},
                  {'e_in': (frozenset(['c_in']), ident(['prev', 'cur', 'lag'])), 'e_rule': (frozenset(['c_motion']), ident(ports))},
                  ['e_in', 'e_rule'], 'nxt', name='motion_rule')
    return p, c, tv


# ---- 2b. the search's history at two boundaries -----------------------------------------------------------------------
DESIGNERS = "the designers write the grammar, the scorer, the world renderer and the teaching measurements"
TEACH = 'the scorer and the teaching measurements, run inside the machine'
GRAMMAR = 'the grammar proposes expressions (29,174 proposals in all)'
FIT = 'first exact fit on the teaching measurements is kept'


def search_histories(occurs, steered):
    """Θ by hand (I90). The designers' occurrence represents the survival condition (an exact fit), the codomain (the
    world's shape or motion) and the teaching pairs H; the scorer with its measurements, run inside the machine, is a
    record of theirs (it entered whole, I200), with the same tags. steered False (reading S): the grammar's proposals
    come in an order the feedback does not change; a population, a variation and a survival condition; no trace
    prepares the rule. steered True (reading K): the feedback steers what is proposed next with the measurements held;
    read as a construction trace that prepares the rule (as S129's K8 reads training on a teacher's answers).
    Advantage True: fidelity on H decided which proposal was kept."""
    occ = [DESIGNERS, TEACH, GRAMMAR, FIT, 'o_t (the learned bank holds the rule)']
    tags = [(DESIGNERS, 'surv'), (DESIGNERS, 'cod'), (DESIGNERS, 'H'), (TEACH, 'surv'), (TEACH, 'cod'), (TEACH, 'H')]
    src = {TEACH: DESIGNERS}
    mk = lambda beta: Hist(occ, tags, occurs, admitted=not steered, prepares=steered, beta=beta, source=src, advantage=True)
    return [('the machine as run (the scorer and the teaching measurements inside, their writers outside)', mk(occ[1:])),
            ('a boundary taking in the designers and the teaching data', mk(occ))]


def says(acc, s, k):
    dec = (not s) and (not k)
    if not acc:
        return "not an account: (E) fails, so neither (Suff) nor the owner's condition speaks"
    if cb.EXPL_BY_CONSTRUCTION:
        if k:
            return "an explanation by (Suff)'s conjecture (an account whose transport was constructed): created knowledge, worked out"
        return ("no explanation, by the owner's condition (S41, S86: an account whose transport was not worked out); "
                + ('it represents: evolved knowledge' if s else 'declared: it represents nothing at this boundary'))
    if dec:
        return "no explanation, by the owner's condition (S41: declared)"
    return "an explanation by (Suff)'s conjecture (not declared)" + (', in the narrow sense' if s else '')


def provenance_rows(c, acc, H, steered):
    rows = {}
    for nm, h in search_histories(set(c.p.C), steered):
        s, k = sel(c, H, h), con(h)
        dec = (not s) and (not k)
        j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c.name))])
        out, _ = expl_ruled_out(j, c.name)
        rows[nm] = {'Sel': s, 'Con': k, 'Dec': dec,
                    'the scorer represents (survival condition, codomain, H) at this boundary': any(o == TEACH for o, _ in cb.rep_at_beta(h)),
                    'the scorer entered the boundary whole': cb.entered_whole(h, TEACH),
                    'Rep: the rule stands for the world (faithful and Sel or Con)': bool(faithful_on(c, list(c.p.C))) and (s or k),
                    '(Suff) conjectures Expl': bool(acc and (k if cb.EXPL_BY_CONSTRUCTION else not dec)),
                    "the owner's condition rules Expl out": bool(acc and ((not k) if cb.EXPL_BY_CONSTRUCTION else dec)),
                    '(Suff) defeated at L536 for an assessor holding it is no explanation': suff_defeats(acc, dec, out, 'L536', con=k),
                    'what the semantics says of the rule taken whole': says(acc, s, k)}
    return rows


# ---- 2c. the invented words -------------------------------------------------------------------------------------------
def words():
    """A chain of holdings (prov_fixed_points, cut T′): o1 the designers choose the word and pair it with a concept
    slot (held: the pairing is theirs; no trace, no population: a convention written down); o2 the teaching item that
    carries the word to the machine (a record of o1); o3 the machine's stored pairing of word and slot (a record of o2:
    stored as given). Boundaries: the machine (o2, o3) and one taking in the designers (o1 to o3)."""
    out = {}
    for bl, beta in (('the machine as run', {1, 2}), ('a boundary taking in the designers', None)):
        f = prov_fixed_points(3, [1, 1, 1], [0, 0, 0], [0, 0, 0], "T'", True, rec_of=[None, 0, 1], beta=beta)
        assert len(f) == 1, f
        R, sc = f[0]
        v = {'o%d' % (o + 1): ('Sel' if sc[o][0] else 'Con' if sc[o][1] else 'Dec') for o in range(3) if cb._in(beta, o)}
        out[bl] = {'verdicts': v, 'represent (Rep)': sorted('o%d' % (o + 1) for o in R), "the machine's pairing (o3)": v['o3']}
    return out


# ---- 2d. the motion rule where the world changes ----------------------------------------------------------------------
def changed_worlds():
    p, c, tv = motion_case([ONE, 'accelerating', 'bounce at a wall'])
    H = [(ONE, b) for b in c.p.D.B]                 # the teaching measurements: the straight-line world only
    acc, d = account(c, detail=True)
    out = {'(E) of the motion rule on the question with the two changed worlds admitted': acc,
           'conditions': {k: bool(v) for k, v in d.items()}}
    for steered, rl in ((False, 'reading S'), (True, 'reading K')):
        for nm, h in search_histories(set(c.p.C), steered):
            s = sel(c, H, h)
            per = {}
            for a in ('accelerating', 'bounce at a wall'):
                pairs = [(a, b) for b in c.p.D.B]
                v = sum(viol_at(c, *x) for x in pairs)
                wrong = sum(not A_at(c, *x) for x in pairs)
                per[a] = {'pairs': len(pairs), 'violation (D12.7: F1 or F2eq fails at the pair)': v,
                          'the answer is wrong at the pair ((A) fails: what the machine would see)': wrong,
                          'surprise (Sel, outside H, violated)': (v if s else 0)}
            ok = sum(viol_at(c, ONE, b) for b in c.p.D.B)
            out['%s | %s' % (rl, nm.split(' (')[0])] = {'Sel on the straight-line history': s, 'Con': con(h),
                                                        'violations in the straight-line world': ok, 'changed worlds': per}
    # a worked example at one pair, for the plain file
    b = 'p2c3l1'
    name = lambda a: 'straight-line world (no change)' if a == ONE else a
    out['one pair: prev 2, cur 3, lag 1'] = {name(a): {"the world's next position": WORLDS[a](*tv[b]), "the rule's forecast": straight(*tv[b])}
                                             for a in WORLDS}
    b = 'p3c5l2'
    out['one pair: prev 3, cur 5, lag 2'] = {name(a): {"the world's next position": WORLDS[a](*tv[b]), "the rule's forecast": straight(*tv[b])}
                                             for a in WORLDS}
    # a repair: the world's own law under each edit, as a candidate (what a constructor would have to build)
    E2 = org('E_repaired', list(c.E.ports), c.E.dom, ['e_in', 'e_rule'], dict(c.E.foot), list(c.E.B), list(c.E.A),
             lambda j, a, b2: {tv[b2]} if j == 'e_in' else {t + (WORLDS[a](*t),) for t in tv.values()})
    c2 = c.replace(E=E2, name='repaired_rule')
    out['(E) of a repaired rule (the world\'s law under each change) on the same question'] = account(c2)
    return out


# ---- 2e. Argument 3: what the teaching measurements leave open --------------------------------------------------------
def left_open():
    """Two expressions a grammar might hold that agree on every integer pixel and differ off the grid: the disc rule as
    found, and x*x + y*y < 10. On the integer grid they give one raster; at points of a rotated or shifted pose
    (non-integer coordinates) they part. Plain arithmetic, not the model."""
    g = [(x, y) for x in range(-5, 6) for y in range(-5, 6)]
    same = all((x * x + y * y <= 9) == (x * x + y * y < 10) for x, y in g)
    off = [(x / 4, y / 4) for x in range(-20, 21) for y in range(-20, 21)]
    differ = sum((x * x + y * y <= 9) != (x * x + y * y < 10) for x, y in off)
    return {'agree on every integer pixel from -5 to 5': same, 'quarter-pixel points (41 x 41) where they differ': differ}


# ---- 3. the design's provenance test on templates ---------------------------------------------------------------------
def design_check():
    """Templates of the S133 design's arms (no data). The subject's boundary β: the session (the model as run, the
    notebook, its own action log); outside: the rule card's writer, the world, the experimenter. Θ by hand (I90)."""
    from model.claims_b import fwd_pole_cand
    p, c = fwd_pole_cand()            # any account serves: the verdict turns on the history (as S129 and S131 did)
    H = [(ONE, 'b1_45')]
    out = {}
    CARD = 'the experimenter writes the rule card'
    HELD = 'the subject holds the inherited rule (the card, entered whole)'
    LOG = "the changed world's readouts, in the subject's log"
    DRAFT = 'the subject writes a draft repair and an expectation from it, before the test'
    occ = [CARD, HELD, LOG, DRAFT, 'o_t (the repair held in the notebook)']
    # main arm: the repair is built in the notebook, its draft held inside β before its test. The inherited rule is
    # held too, but it is not faithful to the changed world, so it carries no tag for the repair's target or codomain.
    h = Hist(occ, [(DRAFT, 't')], set(p.C), admitted=False, prepares=True,
             beta=occ[1:], source={HELD: CARD}, advantage=True)
    out['main arm: the repair built in the notebook'] = (sel(c, H, h), con(h))
    # handed-over repair: the card already holds the repaired rule; the subject stores it
    occ2 = ['the experimenter writes the repaired rule', 'o_t (the repair, as handed over)']
    h2 = Hist(occ2, [(occ2[0], 't'), (occ2[0], 'cod')], set(p.C), admitted=False, prepares=False, beta=occ2[1:],
              source={occ2[1]: occ2[0]}, advantage=True)
    out['control: the repair handed over'] = (sel(c, H, h2), con(h2))
    # search with a scorer and no held target: candidate repairs varied and kept by a scorer written outside
    occ3 = ['the experimenter writes the scorer', 'the scorer, run inside', 'candidate repairs varied and kept', 'o_t (the kept repair)']
    h3 = Hist(occ3, [(occ3[0], 'surv'), (occ3[0], 'cod'), (occ3[1], 'surv'), (occ3[1], 'cod')], set(p.C), admitted=True,
              prepares=False, beta=occ3[1:], source={occ3[1]: occ3[0]}, advantage=True)
    out['control: a search with a scorer and no held target'] = (sel(c, H, h3), con(h3))
    # I201: a repair whose draft is held only outside β (the experimenter dictates it) is declared at β
    h4 = Hist(occ, [(CARD, 't')], set(p.C), admitted=False, prepares=True, beta=occ[1:], source={HELD: CARD},
              advantage=True)
    out['the repair prepared in the session but its target held only outside (I201)'] = (sel(c, H, h4), con(h4))
    return {k: {'Sel': s, 'Con': k2, 'Dec': not s and not k2} for k, (s, k2) in out.items()}


def main():
    OUT = {'about': ("S133: the owner's outside experiment's three found rules (and its two invented words) fed by hand to a "
                     "copy of S131's program copy (Reading C, graded advantage, explanation by construction), as MC2 (S133). "
                     'Θ by hand (I90): the encoding is this script\'s, stated in its docstrings; the verdicts are the copy\'s. '
                     'Nothing of the outside experiment was run; its claims are the owner\'s outside report, unverified here. '
                     'Built by tools/s133_copy_the_program_and_feed_it_the_found_rules.py.'),
           'program copy': os.path.relpath(COPY, ROOT),
           'program copy files byte-equal to S131 (md5, %d files)' % len(mine): True,
           'settings': {}}
    cases = {'the square rule, max(abs(x), abs(y)) <= 3, on the square world': shape_case(SQUARE, SQUARE, 'square', 'square_rule'),
             'the disc rule, x*x + y*y <= 9, on the disc world': shape_case(DISC, DISC, 'disc', 'disc_rule'),
             'the motion rule, cur + (cur - prev) * lag, on the straight-line world': motion_case([ONE])[:2]}
    rival_p, rival_c = shape_case(SQUARE, DISC, 'square', 'disc_rule_offered_for_the_square')
    for lab, c_on, g_on, x_on in SETTINGS:
        cb.READING_C, cb.GRADED, cb.EXPL_BY_CONSTRUCTION = c_on, g_on, x_on   # the functions read these at call time
        st = {}
        for nm, (p, c) in cases.items():
            acc, d = account(c, detail=True)
            H = sorted(c.p.C, key=repr)          # the teaching measurements: every pair of the small world (Θ by hand)
            st['MC2 (S133) ' + nm] = {'(E) of the rule taken whole': acc, 'conditions': {k: bool(v) for k, v in d.items()},
                                      'reading S (feedback filters a fixed order: the main reading)': provenance_rows(c, acc, H, False),
                                      'reading K (feedback steers proposals, measurements held: as S129 K8)': provenance_rows(c, acc, H, True)}
        st['MC2 (S133) the two invented words'] = words()
        OUT['settings'][lab] = st
    cb.READING_C, cb.GRADED, cb.EXPL_BY_CONSTRUCTION = True, True, True
    ra = account(rival_c)
    diff = [b for b in rival_p.D.B if rival_p.ans(ONE, b) != rival_c.ans_E(ONE, b)]
    OUT['the disc rule offered for the square world (two members of the grammar, conflicting)'] = {
        '(E)': ra, 'pixels where their answers differ': len(diff), 'which': diff}
    OUT['the motion rule where the world changes (all three decisions on)'] = changed_worlds()
    OUT["Argument 3: what the teaching measurements leave open (plain arithmetic)"] = left_open()
    OUT['the S133 design: its provenance test on templates (all three decisions on)'] = design_check()
    after = files_of(S131_COPY)
    OUT["S131's program copy unchanged (md5 of every file before and after)"] = after == before
    assert after == before
    json.dump(OUT, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    s = OUT['settings']
    for lab in s:
        print('==', lab)
        for nm, v in s[lab].items():
            if 'words' in nm:
                print('  ', nm, {bl: r["the machine's pairing (o3)"] for bl, r in v.items()})
                continue
            print('  ', nm[:70], '| (E):', v['(E) of the rule taken whole'])
            for rd in ('reading S (feedback filters a fixed order: the main reading)', 'reading K (feedback steers proposals, measurements held: as S129 K8)'):
                for bl, r in v[rd].items():
                    print('      %s | %-28s Sel %-5s Con %-5s Dec %-5s | %s' % (rd[:9], bl[:28], r['Sel'], r['Con'], r['Dec'],
                                                                         r['what the semantics says of the rule taken whole'][:95]))
    for k in ('the disc rule offered for the square world (two members of the grammar, conflicting)',
              'the motion rule where the world changes (all three decisions on)',
              'Argument 3: what the teaching measurements leave open (plain arithmetic)',
              'the S133 design: its provenance test on templates (all three decisions on)'):
        print('==', k)
        print(json.dumps(OUT[k], indent=1, ensure_ascii=False, default=str)[:3000])


if __name__ == '__main__':
    main()
