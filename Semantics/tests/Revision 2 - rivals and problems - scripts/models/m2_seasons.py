#!/usr/bin/env python3
"""M2 - the seasons: "Demeter grieves" against "Persephone is underground" on the Greek question
(kind (ii)?), the tilt against the myth (kind (i), separated at the far south?), label swaps, the
amended myth (N2), and the anchoring of the gods.

Questions: p_greek (contract GREEK = the two halves of the year at Greece, baseline N,H1) and p_world
(all six pairs). Established in the Greek era: the answers at the two Greek pairs. After the sailor:
also the answers at the two southern pairs. Space of target relations: functional (see engine.py;
M1 found no difference between 'all' and 'functional').
"""
from engine import key, one_account, conflict, conflict_route, fits, problem, test_solves, fmt_problem
from seasons import D, PAIRS, GREEK, SOUTH, B0, show, tilt, myth3, myth2

SP = 'functional'


def est_of(pairs):
    return {key(x): ('ans', D.ans(x)) for x in pairs}


def verdict(a, b, C, est, oa_C=None, offered=True, detail=True):
    res = problem(a, b, C, D, est, offered=offered, space=SP, oa_C=oa_C)
    print('  %s vs %s' % (a.name, b.name))
    if detail:
        print(fmt_problem(res, show))
    else:
        print('    VERDICT: %s' % res['verdict'])
    return res


def main():
    print('=' * 100)
    print('M2  THE SEASONS')
    print('=' * 100)
    EG = est_of(GREEK)
    ES = est_of(GREEK + SOUTH)
    q = 'p_greek'
    T = tilt(q)
    DEM = myth3('dem', q)
    DEMP = myth3('dem_p', q, reads_place=True)
    SOR = myth3('sorrow', q, mid='sorrow', names=('sched', 'sorrowc', 'scold'))
    SOUTHM = myth3('south', q, reads_place=True, south=True)
    SOUTH3 = myth3('south_nop', q, reads_place=True, south=True)
    UND = myth2('und', q)
    DEM2 = myth2('dem2', q, state='grief', names=('bargain', 'griefcold'))
    FRE = myth2('freyr', q, state='fortune', names=('war', 'warmth'))
    DEM0 = myth3('dem[R-none]', q, real=False)
    UND0 = myth2('und[R-none]', q, real=False)
    cands = [T, DEM, DEMP, SOR, SOUTHM, UND, DEM2, FRE, DEM0, UND0]

    print()
    print('-' * 100)
    print('(1) each candidate: Account on p_greek, on p_world; fits the Greek-era results; fits after the sailor')
    print('-' * 100)
    for c in cands:
        print('  %-12s greek=%-5s world=%-5s fitsG=%-5s fitsS=%-5s  world fails: %s' % (
            c.name, c.account(GREEK, B0, D), c.account(PAIRS, B0, D), fits(c, EG, D), fits(c, ES, D),
            ' '.join(c.account_why(PAIRS, B0, D, show)[:3])))
    print('  R-none myths on p_greek fail: %s' % ' '.join(DEM0.account_why(GREEK, B0, D, show)))

    print()
    print('-' * 100)
    print('(2) the draft on p_greek (Greek-era results; "one account" judged on C = the Greek pairs)')
    print('-' * 100)
    for a, b in ((DEM, UND), (UND, DEM2), (UND, FRE), (DEM, SOR), (T, DEM), (T, UND), (DEM, SOUTHM), (DEMP, SOUTHM)):
        verdict(a, b, GREEK, EG)

    print()
    print('-' * 100)
    print('(3) R-none: the gods anchored to nothing (Part IV still requires an anchor)')
    print('-' * 100)
    for a, b in ((DEM0, UND0), (T, DEM0)):
        verdict(a, b, GREEK, EG)
    x = GREEK[1]
    print('  test at %s (full) solves dem[R-none] vs und[R-none]? %s ; (answer only)? %s' % (
        show(x), test_solves(DEM0, UND0, x, D, EG, SP, 'full')[0], test_solves(DEM0, UND0, x, D, EG, SP, 'ans')[0]))

    print()
    print('-' * 100)
    print('(4) the draft on p_world, before the sailor (tilt against the myth), and after')
    print('-' * 100)
    Tw, DEMw, DEMPw, SOUTHw = (c.with_question('p_world') for c in (T, DEM, DEMP, SOUTHM))
    r = verdict(Tw, DEMw, PAIRS, EG)
    for xx in PAIRS:
        if conflict(Tw, DEMw, xx, D, SP)[0]:
            print('    test at %-5s full solves=%-5s ans solves=%s' % (
                show(xx), test_solves(Tw, DEMw, xx, D, EG, SP, 'full')[0], test_solves(Tw, DEMw, xx, D, EG, SP, 'ans')[0]))
    print('  after the sailor\'s report:')
    verdict(Tw, DEMw, PAIRS, ES, detail=False)
    verdict(DEMPw, SOUTHw, PAIRS, EG, detail=False)
    verdict(Tw, SOUTHw, PAIRS, ES)

    print()
    print('-' * 100)
    print('(5) REPAIR tested: "one account" judged on every admitted pair (all six), for the Greek-question pairs')
    print('-' * 100)
    for a, b in ((DEM, UND), (UND, DEM2), (UND, FRE), (DEM, SOR), (DEM, SOUTHM), (DEMP, SOUTHM), (T, DEM)):
        verdict(a, b, GREEK, EG, oa_C=PAIRS, detail=False)


if __name__ == '__main__':
    main()
