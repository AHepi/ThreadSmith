#!/usr/bin/env python3
"""A9 - the 03b repair run over 02's six models and over the seasons target with shading admitted.

For every pair: the draft (W59.1 as written), and the 03b repair (rivals: offered in place of each other and
each claims something the other does not, at admitted pairs in or outside C; kinds as in the draft). The
expected verdict is the case book's, the owner's, or 02's, as named. Pairs are offered in place of each other.
Seasons with shading (S+): the admitted changes are the six (place, half) pairs and, outside every
contract here, shading edits that set the warmth received (ins) at each of them. The myths with a grief
state translate shading as "Demeter grieves" (their grief port is anchored to the warmth received, R-real);
the two-component myths have no port for it and so predict as usual.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from ext import Org, Target, Cand, key, fits, draft_verdict, verdict_fix, rule  # noqa: E402
import garden as G  # noqa: E402
import seasons as S  # noqa: E402
import m4_d3t as M4  # noqa: E402
import m5_n25 as M5  # noqa: E402
import m6_n1 as M6  # noqa: E402

ROWS = []


def row(model, label, a, b, C, ADM, D, est, expected, space='all'):
    d = draft_verdict(a, b, C, D, est, True, space)
    f, det = verdict_fix(a, b, C, ADM, D, est, True, space)
    print('  %-4s %s\n       draft:    %s\n       03b:      %s%s\n       expected: %s' % (
        model, label, d, f, ('   [' + det + ']') if det else '', expected))
    ROWS.append((model, label, d, f + (('   [' + det + ']') if det else ''), expected))


def shade_wrap(c, mid):
    base = c.tau

    def tau(x):
        ex = base(x)
        if 'ins' in x:
            ex[mid] = x['ins']
        return ex
    return Cand(c.name, c.org, c.q, tau, c.pi, c.anchors, c.gamma, c.question)


def main():
    print('=' * 100)
    print('A9  THE 03b REPAIR OVER 02\'S MODELS')
    print('=' * 100)
    # M1
    C16 = list(G.SETTINGS)
    FINE = C16 + [dict(x, ovrD=o) for x in G.SETTINGS for o in (0, 1)]
    EST = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}
    GOOD, BAD, WIND = G.emb1('E_good', G.EARLY), G.emb1('E_bad', G.WET), G.emb1('E_windy', G.WINDY)
    E0, RULE = G.e0(), G.emb2('E_rule', lambda v, s: 'N' if v == 'early' else s)
    CREC = [G.B0, G.SHADE, G.FSTAR]
    rule('M1 the gardener (admitted: the 16 settings; M3 (b) also the 32 edits that set the variety effect)')
    row('M1', 'E_good vs E_bad, p', GOOD, BAD, C16, C16, G.D, EST, 'kind (i) (O24; 02)')
    row('M1', 'E_good vs E0, p', GOOD, E0, C16, C16, G.D, EST, 'no problem: E0 does not fit')
    Gr, Br, Wr = (c.with_question('p_rec') for c in (GOOD, BAD, WIND))
    row('M1', 'E_good vs E_bad, p_rec', Gr, Br, CREC, C16, G.D, EST, 'kind (ii) (owner, refinement 2)')
    row('M1', 'E_bad vs E_windy, p_rec', Br, Wr, CREC, C16, G.D, EST, 'kind (ii) (owner: "windy would fit as well")')
    row('M3b', 'mechanism vs rule, p (C = 16)', GOOD, RULE, C16, C16, G.D, EST, 'N7-like: compatible; 02: kind (ii)')
    row('M3b', 'mechanism vs rule, p, ovr edits admitted', GOOD, RULE, C16, FINE, G.D, EST, 'kind (ii); kind (i) on p_fine (02)')
    VP = ('V', 'W', 'Wi', 'Sun')
    A_ = G.emb1('var[early]', lambda v, w, wi, s: int(v == 'early'), var_ports=VP)
    B_ = G.emb1('var[early&sunS]', lambda v, w, wi, s: int(v == 'early' and s == 'S'), var_ports=VP)
    row('M3c', 'one answer profile, one anchor, other relations', A_, B_, C16, C16, G.D, EST, 'kind (i) (02)')
    DO = Org('door', {'push': (0, 1), 'sp_t': (0, 1), 'cb_t': (0, 1), 'ret': (0, 1)},
             {'dspring': (('push', 'sp_t'), frozenset({(0, 0), (1, 1)})),
              'dcable': (('push', 'cb_t'), frozenset({(0, 0), (1, 0)})),
              'ddoor': (('sp_t', 'cb_t', 'ret'), frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)}))})
    DD = Target(DO, 'ret')
    CD = [{'push': 0}, {'push': 1}]
    idrel = frozenset({(0, 0), (1, 1)})

    def door_cand(name, t_port, a_first, a_door):
        org = Org(name, {'push': (0, 1), 't': (0, 1), 'ret': (0, 1)},
                  {'pull': (('push', 't'), idrel), 'shut': (('t', 'ret'), idrel)})
        return Cand(name, org, 'ret', lambda x: dict(x),
                    lambda z, tp=t_port: {'push': z['push'], 't': z[tp], 'ret': z['ret']},
                    {'pull': (a_first, {'push': 'push', 't': t_port}), 'shut': (a_door, {'t': t_port, 'ret': 'ret'})},
                    {'pull', 'shut'}, 'p_door')
    SPR = door_cand('spring', 'sp_t', {'dspring'}, {'ddoor', 'dcable'})
    CAB = door_cand('cable', 'cb_t', {'dcable'}, {'ddoor', 'dspring'})
    ESTD = {key(x): ('ans', DD.ans(x)) for x in CD}
    row('M3d', 'spring vs slack cable (door)', SPR, CAB, CD, CD, DD, ESTD, 'kind (ii); a relation test in C refutes the cable (02 7b)')
    REN = G.emb1('E_good renamed', G.EARLY, effect='boost', names=('suncomp', 'boostcomp'))
    row('M3a', 'E_good vs E_good renamed', GOOD, REN, C16, C16, G.D, EST, 'not rivals (refinement 1)')

    # M2 and S+
    rule('M2 the seasons: the draft on the six pairs; the 03b repair with and without shading admitted')
    q = 'p_greek'
    T = S.tilt(q)
    DEM, DEMP = S.myth3('dem', q), S.myth3('dem_p', q, reads_place=True)
    SOR = S.myth3('sorrow', q, mid='sorrow', names=('sched', 'sorrowc', 'scold'))
    SOUTHM = S.myth3('south', q, reads_place=True, south=True)
    UND, FRE = S.myth2('und', q), S.myth2('freyr', q, state='fortune', names=('war', 'warmth'))
    DEM2 = S.myth2('dem2', q, state='grief', names=('bargain', 'griefcold'))
    DEM0, UND0 = S.myth3('dem[R-none]', q, real=False), S.myth2('und[R-none]', q, real=False)
    SH = [dict(x, ins=v) for x in S.PAIRS for v in S.V3]
    ADM6, ADMS = list(S.PAIRS), list(S.PAIRS) + SH
    ESTG = {key(x): ('ans', S.D.ans(x)) for x in S.GREEK}
    W = {id(c): shade_wrap(c, m) for c, m in ((DEM, 'grief'), (DEMP, 'grief'), (SOR, 'sorrow'), (SOUTHM, 'grief'))}
    w = lambda c: W.get(id(c), c)
    pairs = [(DEM, UND, 'owner: kind (ii)'), (UND, FRE, 'not rivals (Deutsch p.21 core; draft)'),
             (DEM, SOR, 'not rivals (label)'), (DEM, DEM2, '-'), (DEM, SOUTHM, 'N2: kind (ii)'),
             (DEMP, SOUTHM, 'N2: kind (ii)'), (T, DEM, 'kind (ii) on the Greek question (02 7a)'),
             (DEM0, UND0, 'owner: kind (ii); 02: kind (i) degenerate'), (T, DEM0, '02: kind (i) degenerate')]
    for a, b, exp in pairs:
        row('M2', '%s vs %s, Greek q., six pairs' % (a.name, b.name), a, b, S.GREEK, ADM6, S.D, ESTG, exp, 'functional')
    for a, b, exp in pairs:
        row('S+', '%s vs %s, Greek q., + shading' % (a.name, b.name), w(a), w(b), S.GREEK, ADMS, S.D, ESTG, exp, 'functional')

    # M4
    rule('M4 D3-T; M5 N25; M6 N1')
    EX, EY, EZ = M4.cand('X kept', M4.X), M4.cand('Y discarded', M4.Y), M4.cand('Z conjectured', M4.Z)
    EST_T = {key(x): ('ans', M4.D.ans(x)) for x in M4.TRIED}
    row('M4', 'X vs Y', EX, EY, M4.PAIRS, M4.PAIRS, M4.D, EST_T, 'no problem: Y fails (D3-T)')
    row('M4', 'X vs Z, tester results only', EX, EZ, M4.PAIRS, M4.PAIRS, M4.D, EST_T, 'kind (i) (D3-T "two designs")')
    # M5
    DOG, TUR, DOG0, TUR0 = M5.creature('dog'), M5.creature('turtle'), M5.creature('dog', False), M5.creature('turtle', False)
    SELF = Cand('self', Org('self', {'push': (0, 1), 'held': ('yes', 'no')}, {'self': (('held',), frozenset({('yes',)}))}),
                'held', lambda x: dict(x), lambda z: {'push': z['push'], 'held': z['held']},
                {'self': ({'dholder', 'dhold'}, {'held': 'held'})}, {'self'}, 'p')
    EST5 = {key(x): ('ans', M5.D.ans(x)) for x in M5.C}
    row('M5', 'dog vs turtle', DOG, TUR, M5.C, M5.C, M5.D, EST5, 'not rivals (N25 "idle"; draft)')
    row('M5', 'dog vs turtle, R-none', DOG0, TUR0, M5.C, M5.C, M5.D, EST5, 'not rivals')
    row('M5', 'dog vs self', DOG, SELF, M5.C, M5.C, M5.D, EST5, '02: kind (ii)')
    # M6
    FULL, STEADY = frozenset({('steady',), ('drift',)}), frozenset({('steady',)})
    TT = M6.tomas('Tomas')
    IDLE = M6.tomas('Tomas+god[idle]', (FULL, set()))
    ROUTE = M6.tomas('Tomas+god[route]', (STEADY, {'dspin'}))
    UNF = M6.tomas('Tomas+god[unfaithful]', (STEADY, set()))
    EST6 = {key(x): ('ans', M6.D.ans(x)) for x in M6.PAIRS}
    row('M6', 'Tomas vs +idle god', TT, IDLE, M6.PAIRS, M6.PAIRS, M6.D, EST6, 'not a problem (task; N1)', 'functional')
    row('M6', 'Tomas vs +route god', TT, ROUTE, M6.PAIRS, M6.PAIRS, M6.D, EST6, 'watched (W33.1)', 'functional')
    row('M6', 'Tomas vs +unfaithful god', TT, UNF, M6.PAIRS, M6.PAIRS, M6.D, EST6, 'watched (W33.1)', 'functional')

    rule('where the 03b repair and the draft differ')

    def norm(v):
        if v.startswith('PROBLEM'):
            return 'kind (ii)' if 'kind (ii)' in v else 'kind (i)'
        return 'no problem' if 'NO problem' in v else 'not rivals'
    for m, lab, d, f, e in ROWS:
        if norm(d) != norm(f):
            print('  %-4s %-48s draft: %-11s 03b: %-11s expected: %s' % (m, lab, norm(d), norm(f), e))

if __name__ == '__main__':
    main()
