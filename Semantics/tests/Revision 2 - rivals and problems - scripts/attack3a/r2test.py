#!/usr/bin/env python3
"""03a: the proposed repair of W59.1 tested on the 02 models.
R2: rivals = offered in place of each other AND they conflict at some ADMITTED pair (inside C or not),
where 'conflict' is PROPER: each alone could meet (F1), (F2), (A) there under some relations of the
target, and no relations let both. Kind (i) if they conflict at a pair of C, else kind (ii).
Also reported: the draft's 'conflict' (degenerate allowed) under R2, to show why PROPER is needed."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from engine import key, conflict, fits, one_account, Org, Target, Cand

def conflicts(c1, c2, pairs, D, space, proper=True):
    out = []
    for x in pairs:
        c, a, b, n = conflict(c1, c2, x, D, space)
        if c and (a and b or not proper):
            out.append(x)
    return out

def r2(c1, c2, C, ADM, D, est, space, offered=True, proper=True, nc=None):
    if not offered:
        return 'not rivals: not offered in place of each other'
    cf = conflicts(c1, c2, ADM, D, space, proper)
    if not cf:
        return 'not rivals: no %sconflict at any admitted pair' % ('proper ' if proper else '')
    f1, f2 = fits(c1, est, D, nc), fits(c2, est, D, nc)
    if not (f1 and f2):
        return 'rivals (conflict at %d admitted pairs); NO problem: %s does not fit' % (
            len(cf), ' and '.join(n for n, f in ((c1.name, f1), (c2.name, f2)) if not f))
    inC = [x for x in cf if any(key(x) == key(y) for y in C)]
    return 'rivals; PROBLEM kind (%s): conflict at %d pairs of C, %d admitted pairs outside C' % (
        'i' if inC else 'ii', len(inC), len(cf) - len(inC))

def line(lab, c1, c2, C, ADM, D, est, space, **kw):
    print('  %-58s R2 proper: %s' % (lab, r2(c1, c2, C, ADM, D, est, space, **kw)))
    print('  %-58s R2 degenerate allowed: %s' % ('', r2(c1, c2, C, ADM, D, est, space, proper=False, **kw)))

# ---------------- M1
import garden as G
from garden import D as GD, SETTINGS, B0, SHADE, FSTAR, emb1, emb2, e0, EARLY, WET, WINDY, PATCH
C_FULL = list(SETTINGS); C_REC = [B0, SHADE, FSTAR]
EST0 = {key(x): ('ans', GD.ans(x)) for x in C_REC}
GOOD, BAD, WIND, PAT = emb1('E_good', EARLY), emb1('E_bad', WET), emb1('E_windy', WINDY), emb1('E_patch', PATCH)
RULE = emb2('E_rule', lambda v, s: 'N' if v == 'early' else s)
E0 = e0()
print('=' * 100); print('M1 gardener (ADM = the 16 settings)'); print('=' * 100)
for a, b in ((GOOD, BAD), (GOOD, WIND), (BAD, WIND), (GOOD, E0)):
    line('%s vs %s on p (C_full)' % (a.name, b.name), a, b, C_FULL, C_FULL, GD, EST0, 'all')
for a, b in ((GOOD, BAD), (BAD, WIND)):
    line('%s vs %s on p_rec (C_rec)' % (a.name, b.name), a, b, C_REC, C_FULL, GD, EST0, 'all')
    print('    draft: one account on C_rec? %s' % (one_account(a, b, C_REC)[0],))

# ---------------- M3
print('=' * 100); print('M3 redescription and cutting'); print('=' * 100)
C_FINE = C_FULL + [dict(x, ovrD=o) for x in SETTINGS for o in (0, 1)]
REN = emb1('E_good renamed', EARLY, effect='boost', names=('suncomp', 'boostcomp'))
line('(a) E_good vs renamed (ADM = C_full)', GOOD, REN, C_FULL, C_FULL, GD, EST0, 'all')
line('(a) E_good vs renamed (ADM = C_fine)', GOOD, REN, C_FULL, C_FINE, GD, EST0, 'functional')
line('(b) mechanism vs rule, ADM = C_full only', GOOD, RULE, C_FULL, C_FULL, GD, EST0, 'all')
line('(b) mechanism vs rule, ADM = C_fine (override admitted)', GOOD, RULE, C_FULL, C_FINE, GD, EST0, 'functional')
VP = ('V', 'W', 'Wi', 'Sun')
A_ = emb1('var[early]', lambda v, w, wi, s: int(v == 'early'), var_ports=VP)
B_ = emb1('var[early & sunS]', lambda v, w, wi, s: int(v == 'early' and s == 'S'), var_ports=VP)
line('(c) same answers, one anchor, different relations', A_, B_, C_FULL, C_FULL, GD, EST0, 'all')

# ---------------- M2
print('=' * 100); print('M2 seasons (ADM = the six place/half pairs; C = Greek pairs)'); print('=' * 100)
from seasons import D as SD, PAIRS, GREEK, SOUTH, B0 as SB0, tilt, myth3, myth2
EG = {key(x): ('ans', SD.ans(x)) for x in GREEK}
q = 'p_greek'
T = tilt(q); DEM = myth3('dem', q); DEMP = myth3('dem_p', q, reads_place=True)
SOR = myth3('sorrow', q, mid='sorrow', names=('sched', 'sorrowc', 'scold'))
SOUTHM = myth3('south', q, reads_place=True, south=True)
UND = myth2('und', q); DEM2 = myth2('dem2', q, state='grief', names=('bargain', 'griefcold'))
FRE = myth2('freyr', q, state='fortune', names=('war', 'warmth'))
DEM0 = myth3('dem[R-none]', q, real=False); UND0 = myth2('und[R-none]', q, real=False)
for a, b in ((DEM, UND), (UND, DEM2), (UND, FRE), (DEM, SOR), (T, DEM), (T, UND), (DEM, SOUTHM), (DEMP, SOUTHM), (DEM0, UND0), (T, DEM0)):
    line('%s vs %s' % (a.name, b.name), a, b, GREEK, PAIRS, SD, EG, 'functional')

# ---------------- M5
print('=' * 100); print('M5 N25'); print('=' * 100)
import m5_n25 as M5
DOG, TUR, DOG0, TUR0 = M5.creature('dog'), M5.creature('turtle'), M5.creature('dog', False), M5.creature('turtle', False)
SELF = Cand('self', Org('self', {'push': (0, 1), 'held': ('yes', 'no')}, {'self': (('held',), frozenset({('yes',)}))}),
            'held', lambda x: dict(x), lambda z: {'push': z['push'], 'held': z['held']},
            {'self': ({'dholder', 'dhold'}, {'held': 'held'})}, {'self'}, 'p')
E5 = {key(x): ('ans', M5.D.ans(x)) for x in M5.C}
for a, b in ((DOG, TUR), (DOG0, TUR0), (DOG, SELF), (DOG0, SELF)):
    line('%s vs %s' % (a.name, b.name), a, b, M5.C, M5.C, M5.D, E5, 'all')

# ---------------- M6
print('=' * 100); print('M6 N1'); print('=' * 100)
import m6_n1 as M6
FULL = frozenset({('steady',), ('drift',)}); STEADY = frozenset({('steady',)})
TT = M6.tomas('Tomas')
IDLE = M6.tomas('Tomas+god[idle]', (FULL, set()))
ROUTE = M6.tomas('Tomas+god[route]', (STEADY, {'dspin'}))
UNF = M6.tomas('Tomas+god[unfaithful]', (STEADY, set()))
ZEUS = M6.tomas('Tomas+zeus[idle]', (FULL, set()), godname='zeus')
E6 = {key(x): ('ans', M6.D.ans(x)) for x in M6.PAIRS}
for o in (IDLE, ROUTE, UNF):
    line('Tomas vs %s' % o.name, TT, o, M6.PAIRS, M6.PAIRS, M6.D, E6, 'functional')
line('god[idle] vs zeus[idle]', IDLE, ZEUS, M6.PAIRS, M6.PAIRS, M6.D, E6, 'functional')
