#!/usr/bin/env python3
"""Counterexample hunt on the gardener model (M1). Uses the machinery of m1_gardener.py.

CX1  a good correction (passes (A) on a contract holding the failed case) that leaves
     the old mistake refittable;
CX2  a bad rescue that does not enlarge Pres under any family treating the two
     rescues alike (a symmetry of the record);
CX3  verdicts that flip with the variation family;
CX4  the containment (H) holding non-strictly (file 00's caveat), and what idle
     parts do to the counts;
CX5  a history-free test (leave-one-out) against the history-using test (leave the
     failure out) on the gardener.
"""
from itertools import combinations, product
from m1_gardener import (Family, SUN_MENU, fn_menu, single_menu, literal_menu, SETTINGS, NS, TRUTH, show, jl, get,
                         pres, pres_count, J_BEFORE, J_AFTER, C_FULL, FSTAR, BG_SEED, BG_RAIN, B0, SIDX, rel)

fam0 = Family('E0', [('sun', SUN_MENU)])
P0 = fam0.profile(fam0.find(sun='id'))
MIST = [j for j in range(NS) if P0[j] != TRUTH[j]]


def reinstating(fam, P):
    return [v for v in P if any(fam.profile(v)[j] == P0[j] for j in MIST)]


def cx1():
    print('=' * 78)
    print('CX1  A GOOD CORRECTION THAT LEAVES THE OLD MISTAKE REFITTABLE')
    print('=' * 78)
    for ports in (('V',), ('V', 'W'), ('V', 'W', 'Wi')):
        fam = Family('E_good, var reads %s' % '+'.join(ports), [('sun', SUN_MENU), ('var', fn_menu(ports))])
        # the correct variety component: fires exactly when V=early (the unique version with the true profile
        # and sun=id; it is also the unique one whose override fires on every early config and no late one)
        good = [v for v in fam.versions() if fam.profile(v) == TRUTH and fam.label(v).startswith('(sun=id')
                and all(fam.menus[1][v[1]][1][j] == (get(SETTINGS[j], 'V') == 'early') for j in range(NS))][0]
        print('\nFamily: sun x var[%s]  |V|=%d   E_good = %s' % ('+'.join(ports), fam.size(), fam.label(good)))
        print('  E_good passes (A) on J_after (holds f*)? %s   on C_full? %s' % (
            all(fam.profile(good)[j] == TRUTH[j] for j in J_AFTER), fam.profile(good) == TRUTH))
        rest = [j for j in MIST if j != FSTAR]
        for r in range(len(rest) + 1):
            for T in combinations(rest, r):
                J = J_AFTER + list(T)
                P = pres(fam, J)
                R = reinstating(fam, P)
                tag = 'jobs = J_after + ' + (jl(T) if T else '{}')
                line = '  %-75s |Pres|=%3d  mistake-reinstating=%3d' % (tag, len(P), len(R))
                if R and r == 0:
                    ex = R[0]
                    line += '\n      e.g. %s  gives E0\'s wrong S at %s' % (fam.label(ex), jl([j for j in MIST if fam.profile(ex)[j] == P0[j]]))
                print(line)
        P = pres(fam, J_AFTER + BG_SEED)
        print('  %-75s |Pres|=%3d  mistake-reinstating=%3d' % ('jobs = J_after + BG_seed (the seed trial)', len(P), len(reinstating(fam, P))))
        P = pres(fam, C_FULL)
        print('  %-75s |Pres|=%3d  mistake-reinstating=%3d' % ('jobs = C_full (the world\'s contract)', len(P), len(reinstating(fam, P))))
        # sanity: nothing in Pres(J_after) repeats the mistake AT f*
        assert not [v for v in pres(fam, J_AFTER) if fam.profile(v)[FSTAR] == P0[FSTAR]]
    print('\n  (check: in every family above no version in Pres(J_after) repeats E0\'s answer at f* itself)')


def swap_setting(s):
    """Exchange the roles of W and V: W=0<->late, W=1<->early."""
    W, Wi, V, Sun = s
    return ({'late': 0, 'early': 1}[V], Wi, {0: 'late', 1: 'early'}[W], Sun)


def cx2():
    print()
    print('=' * 78)
    print('CX2  A BAD RESCUE THAT DOES NOT ENLARGE Pres: the record cannot tell wet from early')
    print('=' * 78)
    sw = {SIDX[s]: SIDX[swap_setting(s)] for s in SETTINGS}
    print('swap(J_after) == J_after as a set? %s ; truth kept on J_after under the swap? %s' % (
        set(sw[j] for j in J_AFTER) == set(J_AFTER), all(TRUTH[sw[j]] == TRUTH[j] for j in J_AFTER)))
    print('swap(C_full truth) == truth? %s  (the world is not symmetric)' % all(TRUTH[sw[j]] == TRUTH[j] for j in C_FULL))
    pairs = [(('V',), ('W',)), (('V', 'Wi'), ('W', 'Wi')), (('V', 'Sun'), ('W', 'Sun')), (('V', 'W'), ('W', 'V')),
             (('V', 'W', 'Wi'), ('W', 'V', 'Wi'))]
    print('%-14s %-14s %10s %10s %14s %12s %12s' % ('good reads', 'bad reads', '|Pres_g|', '|Pres_b|', 'swap bijection',
                                                 '|Pres_g|full', '|Pres_b|full'))
    for pg, pb in pairs:
        fg = Family('g', [('sun', SUN_MENU), ('var', fn_menu(pg))])
        fb = Family('b', [('sun', SUN_MENU), ('rain', fn_menu(pb))])
        Pg = pres(fg, J_AFTER)
        Pb = pres(fb, J_AFTER)
        # map each good-version profile through the swap and compare the profile multisets on C_full
        prof_g = sorted(tuple(fg.profile(v)[sw[j]] for j in range(NS)) for v in Pg)
        prof_b = sorted(fb.profile(v) for v in Pb)
        print('%-14s %-14s %10d %10d %14s %12d %12d' % ('+'.join(pg), '+'.join(pb), len(Pg), len(Pb), prof_g == prof_b,
                                                     pres_count(fg, C_FULL), pres_count(fb, C_FULL)))
    fl = Family('lit', [('sun', SUN_MENU), ('cond', literal_menu())])
    P = pres(fl, J_AFTER)
    print('\nPort-swap family (override fires on one literal): Pres(J_after) =', [fl.label(v) for v in P])
    print('  -> "windy would fit as well" and "wet would fit as well" hold of the GOOD rescue too.')
    P = pres(fl, J_AFTER + BG_SEED)
    print('  with the seed trial BG_seed added:', [fl.label(v) for v in P])
    P = pres(fl, J_AFTER + BG_RAIN)
    print('  with another wet spring BG_rain added:', [fl.label(v) for v in P])
    fp = Family('patch', [('sun', SUN_MENU), ('exc', single_menu())])
    print('\nDo-nothing patch, single-exception family: |Pres(J_after)| = %d (E_good with var[V]: %d; E0 before: %d)' % (
        pres_count(fp, J_AFTER), pres_count(Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))]), J_AFTER),
        pres_count(fam0, J_BEFORE)))


def cx3():
    print()
    print('=' * 78)
    print('CX3  VERDICTS THAT FLIP WITH THE VARIATION FAMILY')
    print('=' * 78)
    gp = [('V',), ('V', 'Wi'), ('V', 'Sun'), ('V', 'W', 'Wi')]
    bp = [('W',), ('W', 'Wi'), ('W', 'Sun'), ('W', 'Wi', 'Sun')]
    print('|Pres(J_after)| for E_good (rows: ports its variety component reads) vs E_bad (columns)')
    print('%-12s' % '' + ''.join('%-16s' % ('bad:' + '+'.join(b)) for b in bp))
    cache_b = {b: pres_count(Family('b', [('sun', SUN_MENU), ('rain', fn_menu(b))]), J_AFTER) for b in bp}
    for g in gp:
        ng = pres_count(Family('g', [('sun', SUN_MENU), ('var', fn_menu(g))]), J_AFTER)
        cells = []
        for b in bp:
            nb = cache_b[b]
            verdict = 'bad easier' if nb > ng else ('good easier' if ng > nb else 'equal')
            cells.append('%d:%d %-10s' % (ng, nb, verdict))
        print('%-12s' % ('good:' + '+'.join(g)) + ''.join('%-16s' % c for c in cells))
    fpa = Family('patch-all', [('sun', SUN_MENU), ('exc', fn_menu(('W', 'Wi', 'V', 'Sun')))])
    fps = Family('patch-single', [('sun', SUN_MENU), ('exc', single_menu())])
    print('\nDo-nothing patch: single-exception family |Pres(J_after)|=%d ; any-predicate family |Pres(J_after)|=%d'
          % (pres_count(fps, J_AFTER), pres_count(fpa, J_AFTER)))


def cx4():
    print()
    print('=' * 78)
    print('CX4  (H) NON-STRICT, AND IDLE PARTS IN THE COUNT')
    print('=' * 78)
    fg = Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))])
    A = pres(fg, J_AFTER)
    B = pres(fg, J_AFTER + BG_RAIN)
    print('E_good family sun x var[V]: Pres(J_after + BG_rain) vs Pres(J_after): %s (%d vs %d)'
          % (rel(B, A), len(B), len(A)))
    print('  -> a genuinely new job (another wet spring) is added and nothing is excluded.')
    U = Family('U', [('sun', SUN_MENU), ('var', fn_menu(('V',))), ('rain', fn_menu(('W',))), ('exc', single_menu())])
    P = pres(U, C_FULL)
    print('Fully common family U: |Pres(C_full)| = %d, although only one answer profile survives:' % len(P))
    for v in P:
        print('   ', U.label(v))
    print('  -> every surviving version gives the true answers; the count is inflated by idle')
    print('     exceptions that fire where the answer is N anyway (counting versions is no warrant).')


def cx5():
    print()
    print('=' * 78)
    print('CX5  LEAVE-ONE-OUT (history-free) vs LEAVE-THE-FAILURE-OUT, gardener')
    print('=' * 78)
    fams = [('E_good var[V]', Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))])),
            ('E_bad rain[W]', Family('b', [('sun', SUN_MENU), ('rain', fn_menu(('W',)))]))]
    for jn, J in (('J_after', J_AFTER), ('J_after + BG_seed', J_AFTER + BG_SEED)):
        for nm, fam in fams:
            P = pres(fam, [j for j in J if j != FSTAR])
            ans = sorted({fam.profile(v)[FSTAR] for v in P})
            Pfull = pres(fam, J)
            print('  jobs %-18s %-14s passes (A) on the jobs? %-5s  answers at f* fixed by the other jobs: %s' % (
                jn, nm, bool(Pfull), ans))


if __name__ == '__main__':
    cx1()
    cx2()
    cx3()
    cx4()
    cx5()
