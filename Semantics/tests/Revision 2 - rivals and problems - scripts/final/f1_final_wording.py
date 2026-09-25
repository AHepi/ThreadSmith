#!/usr/bin/env python3
"""f1_final_wording.py - the draft-4 wording of W59.1 re-run against every pair that 02 built and that the two
attacks (03a, 03b) used to refute or test the drafted wording.

For each pair it prints the drafted wording's verdict (01, "not one account on C"), the 03b repair's verdict
(each claims something the other does not), the final verdict (final_def.verdict_final: rivals by conflict at
some admitted pair, the physics' quantifier, "has been offered"), the verdict expected by the owner, the case
book or the attack, and the checks of the text's claims about the kind found (final_def.check_claims).
The 03a definition is the final one without the physics filter; the two differ only in A8, which is run both ways.

Sections: (1) 02's six models and the seasons with shading admitted (the rows of A9); (2) A3's look-alike and
look-different pairs; (3) A1, rivals that conflict only where nobody can act; (4) A5, narrowing; (5) A8, the
physics; (6) A11, the p.27 variant; (7) 03a's m2b (the owner's example) and m3d (the door); (8) a summary.
Run from this folder with python3; standard library only.
"""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ('models', 'attack'):
    sys.path.insert(0, os.path.join(HERE, '..', sub))
sys.path.insert(0, HERE)

from engine import Org, Target, Cand, key, fits  # noqa: E402
from ext import verdict_fix, draft_verdict, rule  # noqa: E402
from final_def import verdict_final, check_claims, conflicts  # noqa: E402
import garden as G  # noqa: E402
import seasons as S  # noqa: E402
import m4_d3t as M4  # noqa: E402
import m5_n25 as M5  # noqa: E402
import m6_n1 as M6  # noqa: E402
import a9_regression as A9  # noqa: E402
import a3_redescription as A3  # noqa: E402
import a1_unperformable as A1  # noqa: E402
import a8_physics as A8  # noqa: E402

SUMMARY = []


def norm(v):
    if v.startswith('PROBLEM'):
        return 'kind (ii)' if 'kind (ii)' in v else 'kind (i)'
    if 'NO problem' in v:
        return 'no problem'
    return 'not rivals'


def show_row(model, label, a, b, C, ADM, D, est, expected, space='all', b0=None, phys=None, variants=None,
             draft=True, fix=True):
    print('  %-4s %s' % (model, label))
    d = draft_verdict(a, b, C, D, est, True, space) if draft else '-'
    f = ' '.join(verdict_fix(a, b, C, ADM, D, est, True, space)).strip() if fix else '-'
    v, info = verdict_final(a, b, C, ADM, D, est, True, space, phys, variants)
    print('       drafted (01): %s' % d)
    print('       03b repair:   %s' % f)
    print('       FINAL:        %s' % v)
    if info.get('conflicts'):
        routes = sorted({r for _, r in info['conflicts']})
        print('                     routes: %s' % '; '.join(routes))
    print('       expected:     %s' % expected)
    for c in check_claims(a, b, C, ADM, D, est, info, b0, space, phys, variants):
        print('       check: %s' % c)
    SUMMARY.append((model, label, norm(d) if draft else '-', norm(f) if fix else '-', norm(v), expected))
    return v, info


# ------------------------------------------------------------------------------------------------ (1)
B0S = {'M1': G.B0, 'M3a': G.B0, 'M3b': G.B0, 'M3c': G.B0, 'M3d': {'push': 0}, 'M2': S.B0, 'S+': S.B0,
       'M4': M4.B0, 'M5': M5.B0, 'M6': M6.B0}


def a9_row(model, label, a, b, C, ADM, D, est, expected, space='all'):
    show_row(model, label, a, b, C, ADM, D, est, expected, space, b0=B0S.get(model))


def section1():
    A9.row = a9_row
    A9.main()


# ------------------------------------------------------------------------------------------------ (2)
def a3_report(label, a, b, C, ADM, D, est, b0, show, space='all', do4=True):
    exp = {
        'WETM': 'kind (i): they differ in the background, which (F2) reads (03b A3 (a))',
        '(b) admitted': 'not rivals: they claim the same (03b A3 (b))',
        "(b')": 'kind (ii) (03b A3 (b\'))',
        'value-map': 'not rivals: a redescription (refinement 1)',
        'rename-only': 'not rivals if the recoded candidate can never be faithful (03b A3 (c))',
        'duplicate': 'not rivals (03b A3 (d))',
        '(e1)': 'not rivals: the coarsening claims nothing the tilt does not (03b A3 (e1))',
        '(e2)': 'kind (ii) (03b A3 (e2))',
        'P vs Q': 'the residual: 03b gives kind (ii); both stand or fall together (03b A3 (f))',
    }
    e = next((v for k, v in exp.items() if k in label), '-')
    show_row('A3', label, a, b, C, ADM, D, est, e, space, b0=b0)


def section2():
    A3.report = a3_report
    A3.part_a()
    A3.part_b()
    A3.part_c()
    A3.part_d()
    A3.part_e()
    A3.part_f()


# ------------------------------------------------------------------------------------------------ (3)
def section3():
    rule('(3) A1: rivals that conflict only at an admitted change nobody can perform')
    R1, R2 = A1.cand('R1 tilt', A1.INS, 'p_dep'), A1.cand('R2 eccentricity', A1.INS_ECC, 'p_dep')
    EST = {key(x): ('ans', A1.D.ans(x)) for x in A1.HERE}
    show_row('A1', 'R1 vs R2 on p_dep (contract: all four pairs)', R1, R2, A1.PAIRS, A1.PAIRS, A1.D, EST,
             'kind (i): at most one is an account whether or not anyone can establish it (03b FIX-3)', b0=A1.B0)
    H1_, H2_ = R1.with_question('p_here'), R2.with_question('p_here')
    show_row('A1', 'R1 vs R2 on p_here (contract: the tilt-1 pairs)', H1_, H2_, A1.HERE, A1.PAIRS, A1.D, EST,
             'kind (ii) (refinement 2; 03b A1 (3))', b0=A1.B0)


# ------------------------------------------------------------------------------------------------ (4)
def section4():
    rule('(4) A5: a problem "solved" by narrowing the question; the final wording reads "has been offered"')
    C = list(G.SETTINGS)
    EST = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}
    GOOD, BAD = G.emb1('E_good', G.EARLY), G.emb1('E_bad', G.WET)
    conf = [x for x, _ in conflicts(GOOD, BAD, C, G.D)]
    Cn = [x for x in C if all(key(x) != key(y) for y in conf)]
    log = [(1, 'E_good', 'p', 'offered'), (1, 'E_bad', 'p', 'offered'),
           (2, 'E_good', 'p', 'withdrawn'), (2, 'E_bad', 'p', 'withdrawn'),
           (2, 'E_good', 'p_n', 'offered'), (2, 'E_bad', 'p_n', 'offered')]

    def has_been_offered(c, q, t):
        return any(cn == c and qq == q and act == 'offered' and tt <= t for (tt, cn, qq, act) in log)
    Gn, Bn = GOOD.with_question('p_n'), BAD.with_question('p_n')
    print('  conflict pairs on p: %d; the narrowed contract C_n keeps %d settings' % (len(conf), len(Cn)))
    for t in (1, 2):
        op = has_been_offered('E_good', 'p', t) and has_been_offered('E_bad', 'p', t)
        opn = has_been_offered('E_good', 'p_n', t) and has_been_offered('E_bad', 'p_n', t)
        vp = verdict_final(GOOD, BAD, C, C, G.D, EST, op)[0]
        vn = verdict_final(Gn, Bn, Cn, C, G.D, EST, opn)[0]
        print('  t%d  p: %-80s\n      p_n: %s' % (t, vp, vn))
    print('  -> at t2 the problem for p stands (nothing was established at its conflict pairs); on p_n the two are')
    print('     rivals of kind (ii), and the narrowing solved nothing on p: the text\'s narrowing sentence (03b FIX-5).')
    SUMMARY.append(('A5', 'E_good vs E_bad on p after narrowing (t2)', 'no problem (now)', '-',
                    norm(verdict_final(GOOD, BAD, C, C, G.D, EST, True)[0]), 'kind (i): the problem for p stands'))


# ------------------------------------------------------------------------------------------------ (5)
def section5():
    rule('(5) A8: a conflict only the adopted physics makes (the splitter)')
    R1, R2 = A8.cand('R1 channel 1', 'm1', 'd1'), A8.cand('R2 channel 2', 'm2', 'd2')
    est = {key(x): ('ans', A8.D.ans(x)) for x in A8.C}

    def every_relation(x):
        # all relations of d1, d2 and of the two laws at x (a8's deformed-law witness is among them); dout is
        # kept to the relations whose delivered current is a function of the channels, which is enough for a
        # joint witness and keeps the run short.
        from itertools import product
        a = x['a']
        subs2 = A8.subsets([(a, 0), (a, 1)])
        cons = A8.subsets([(a, m1, m2) for m1 in (0, 1) for m2 in (0, 1)])
        outs = [frozenset(ch) for ch in product(*[[(m1, m2, o) for o in (0, 1, 2)] for m1 in (0, 1) for m2 in (0, 1)])]
        for r1, r2, rc, ro in product(subs2, subs2, cons, outs):
            yield {'d1': r1, 'd2': r2, 'dcons': rc, 'dout': ro}
    show_row('A8', 'R1 vs R2, quantifier over every relation (03a\'s wording)', R1, R2, A8.C, A8.C, A8.D, est,
             'the wrong verdict, which is why the quantifier ranges over what the physics admits: over every relation both meet the three at a=1 only with the law deformed (03b A8)', b0=A8.B0, variants=every_relation,
             draft=False, fix=False)
    show_row('A8', 'R1 vs R2, quantifier over what the physics admits (final wording)', R1, R2, A8.C, A8.C, A8.D, est,
             'kind (i) (03b A8, FIX-2)', b0=A8.B0, variants=A8.phys_variants, draft=False, fix=False)


# ------------------------------------------------------------------------------------------------ (6)
def section6():
    rule('(6) A11: the p.27 variant, a same-cut patch outside the question')
    T = S.tilt('p_greek')
    geo = frozenset((p, h, (S.LAT[p] * S.SG[h] if p != 'S' else S.SG[h])) for p in S.PLACES for h in S.HALVES)
    comps = dict(T.org.comps)
    comps['geo'] = (('place', 'half', 'exp'), geo)
    P27 = Cand('tilt, in phase in the south (p.27)', Org('p27', T.org.ports, comps), 'season', T.tau, T.pi,
               T.anchors, T.gamma, 'p_greek')
    est = {key(x): ('ans', S.D.ans(x)) for x in S.GREEK}
    show_row('A11', 'tilt vs the p.27 variant, Greek question', T, P27, S.GREEK, S.PAIRS, S.D, est,
             'kind (ii): the tilt is easy to vary on the Greek question once the variant is offered (03b FIX-11)',
             'functional', b0=S.B0)


# ------------------------------------------------------------------------------------------------ (7)
def section7():
    rule('(7) 03a m2b (the owner\'s example with a change that sets the mediating state) and m3d (the door)')
    q = 'p_greek'
    d = S.myth3('dem', q)
    u = S.myth2('und', q)
    dem = Cand('dem+', d.org, d.q, lambda x: dict({'half': x['half']}, **({'grief': x['ins']} if 'ins' in x else {})),
               d.pi, d.anchors, d.gamma, q)
    MED = [dict(x, ins=i) for x in S.PAIRS for i in (1, 0, -1)]
    EG = {key(x): ('ans', S.D.ans(x)) for x in S.GREEK}
    show_row('m2b', '"Demeter grieves" vs "Persephone is underground", mediating change admitted', dem, u, S.GREEK,
             S.PAIRS + MED, S.D, EG, 'owner: kind (ii)', 'functional', b0=S.B0, draft=False)
    show_row('m2b', 'the same, no change that sets the mediating state admitted', dem, u, S.GREEK, S.PAIRS, S.D, EG,
             'not rivals: their difference is idle, as Persephone\'s and Freyr\'s (Deutsch p.21)', 'functional',
             b0=S.B0, draft=False)
    DO = Org('door', {'push': (0, 1), 'sp_t': (0, 1), 'cb_t': (0, 1), 'ret': (0, 1)},
             {'dspring': (('push', 'sp_t'), frozenset({(0, 0), (1, 1)})),
              'dcable': (('push', 'cb_t'), frozenset({(0, 0), (1, 0)})),
              'ddoor': (('sp_t', 'cb_t', 'ret'), frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)}))})
    DD = Target(DO, 'ret')
    CD = [{'push': 0}, {'push': 1}]
    idrel = frozenset({(0, 0), (1, 1)})

    def door_cand(name, t_port, a_first, a_door, tau):
        org = Org(name, {'push': (0, 1), 't': (0, 1), 'ret': (0, 1)},
                  {'pull': (('push', 't'), idrel), 'shut': (('t', 'ret'), idrel)})
        return Cand(name, org, 'ret', tau, lambda z, tp=t_port: {'push': z['push'], 't': z[tp], 'ret': z['ret']},
                    {'pull': (a_first, {'push': 'push', 't': t_port}), 'shut': (a_door, {'t': t_port, 'ret': 'ret'})},
                    {'pull', 'shut'}, 'p_door')
    SPR = door_cand('spring', 'sp_t', {'dspring'}, {'ddoor', 'dcable'},
                    lambda x: dict({'push': x['push']}, **({'t': x['sp_t']} if 'sp_t' in x else {})))
    CAB = door_cand('cable', 'cb_t', {'dcable'}, {'ddoor', 'dspring'}, lambda x: {'push': x['push']})
    EST = {key(x): ('ans', DD.ans(x)) for x in CD}
    show_row('m3d', 'spring vs slack cable, only pushes admitted', SPR, CAB, CD, CD, DD, EST,
             '03a: not rivals (both could be faithful at once); 03b: kind (ii)', b0=CD[0], draft=False)
    show_row('m3d', 'spring vs slack cable, "hold the spring slack" admitted', SPR, CAB, CD,
             CD + [{'push': p, 'sp_t': 0} for p in (0, 1)], DD, EST, 'kind (ii) (03a m3d)', b0=CD[0], draft=False)
    est2 = dict(EST)
    est2[key({'push': 1})] = ('full', None)
    print('       with the actual relations at push=1 established: spring fits %s, cable fits %s '
          '(a failure of the cable\'s own, inside C)' % (fits(SPR, est2, DD), fits(CAB, est2, DD)))


def main():
    print('=' * 100)
    print('F1  THE DRAFT-4 WORDING OF W59.1, RE-RUN AGAINST 02\'S MODELS AND THE TWO ATTACKS')
    print('=' * 100)
    section1()
    rule('(2) A3: look alike but differ; look different but claim the same')
    section2()
    section3()
    section4()
    section5()
    section6()
    section7()
    rule('(8) summary: drafted wording, 03b repair and final wording (normalized), with the expected verdict')
    for m, lab, d, f, v, e in SUMMARY:
        flag = '' if (d == v or d == '-') else '  <- differs from the drafted wording'
        print('  %-4s %-72s drafted: %-10s 03b: %-10s FINAL: %-10s%s' % (m, lab[:72], d, f, v, flag))
        print('       expected: %s' % e)
    bad = [r for r in SUMMARY if r[4] != r[3] and r[3] != '-']
    print()
    print('  rows where the final wording and the 03b repair differ: %d' % len(bad))
    for m, lab, d, f, v, e in bad:
        print('    %-4s %-72s 03b: %-10s FINAL: %-10s expected: %s' % (m, lab[:72], f, v, e))


if __name__ == '__main__':
    main()
