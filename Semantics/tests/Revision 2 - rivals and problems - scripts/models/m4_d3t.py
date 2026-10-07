#!/usr/bin/env python3
"""M4 - D3-T (candidate O76), the discarded lamp controller.

Target: the kept controller. Switches A, B; the lamp. Only two designs exist:
  X (kept):      lit iff A on and B off      - passes the test
  Y (discarded): lit iff A on and B on       - dark with A on, B off: fails the test
The tester tries (off,off) and (on,off); it never tries (on,on), the untried setting, where X and Y differ.
Question p: every setting (the untried one included), baseline (off,off), query: the lamp.
Established by the tester: the kept controller's lamp at (off,off) and (on,off).
Established by derivation (a receipt is a derivation tree over leaves, D3:L391): only X and Y exist,
the kept one passed, Y fails at (on,off); so the kept one is X, and its lamp at (on,on) and (off,on) is X's.
"""
from itertools import product
from engine import Org, Target, Cand, key, conflict, fits, problem, test_solves, fmt_problem

SW = ('off', 'on')
PAIRS = [{'A': a, 'B': b} for a in SW for b in SW]
B0 = {'A': 'off', 'B': 'off'}
TRIED = [{'A': 'off', 'B': 'off'}, {'A': 'on', 'B': 'off'}]
UNTRIED = {'A': 'on', 'B': 'on'}


def show(x):
    return 'A %s, B %s' % (x['A'], x['B'])


def rel(f):
    return frozenset((a, b, 'lit' if f(a, b) else 'dark') for a in SW for b in SW)


X = rel(lambda a, b: a == 'on' and b == 'off')
Y = rel(lambda a, b: a == 'on' and b == 'on')
Z = rel(lambda a, b: a == 'on')
PORTS = {'A': SW, 'B': SW, 'lamp': ('dark', 'lit')}
D = Target(Org('kept controller', PORTS, {'dctl': (('A', 'B', 'lamp'), X)}), 'lamp')


def cand(name, r):
    return Cand(name, Org(name, PORTS, {'ctl': (('A', 'B', 'lamp'), r)}), 'lamp', lambda x: dict(x), lambda z: dict(z),
                {'ctl': ({'dctl'}, {'A': 'A', 'B': 'B', 'lamp': 'lamp'})}, {'ctl'}, 'p')


def main():
    print('=' * 100)
    print('M4  D3-T, THE DISCARDED CONTROLLER')
    print('=' * 100)
    EX, EY, EZ = cand('design X (kept)', X), cand('design Y (discarded)', Y), cand('Z (a conjectured third design)', Z)
    EST_T = {key(x): ('ans', D.ans(x)) for x in TRIED}
    EST_P = dict(EST_T)
    EST_P[key(UNTRIED)] = ('ans', frozenset({'dark'}))               # derived: kept = X
    EST_P[key({'A': 'off', 'B': 'on'})] = ('ans', frozenset({'dark'}))
    for c in (EX, EY, EZ):
        print('  %-32s Account(p)=%-5s fits tester results=%-5s fits with the population receipt=%s' % (
            c.name, c.account(PAIRS, B0, D), fits(c, EST_T, D), fits(c, EST_P, D)))
    print()
    print('  Ivo: the discarded design Y, against the kept X (tester results):')
    print(fmt_problem(problem(EX, EY, PAIRS, D, EST_T, offered=True), show))
    print('  a conjectured Z against X, tester results only (population not established):')
    res = problem(EX, EZ, PAIRS, D, EST_T, offered=True)
    print(fmt_problem(res, show))
    print('    test at the untried setting: sure to solve (relations)=%s (answer)=%s' % (
        test_solves(EX, EZ, UNTRIED, D, EST_T, 'all', 'full')[0], test_solves(EX, EZ, UNTRIED, D, EST_T, 'all', 'ans')[0]))
    print('  Z against X, with the population receipt:')
    print(fmt_problem(problem(EX, EZ, PAIRS, D, EST_P, offered=True), show))

    print()
    print('  harness: all 16 lamp tables on (A, B) as candidates for p')
    tabs = []
    for outs in product((0, 1), repeat=4):
        t = dict(zip([(a, b) for a in SW for b in SW], outs))
        tabs.append(cand('T' + ''.join(map(str, outs)), rel(lambda a, b, t=t: t[(a, b)])))
    fT = [c for c in tabs if fits(c, EST_T, D)]
    fP = [c for c in tabs if fits(c, EST_P, D)]
    split = sum(1 for i in range(len(fT)) for j in range(i + 1, len(fT)) if conflict(fT[i], fT[j], UNTRIED, D)[0])
    splitP = sum(1 for i in range(len(fP)) for j in range(i + 1, len(fP)) if conflict(fP[i], fP[j], UNTRIED, D)[0])
    print('    fit the tester results: %d; pairs of these that conflict at the untried setting: %d' % (len(fT), split))
    print('    fit with the population receipt: %d (%s); such pairs: %d' % (len(fP), ', '.join(c.name for c in fP), splitP))
    lit_uu = [c for c in tabs if c.ans(UNTRIED) == frozenset({'lit'})]
    print('    every table lit at the untried setting fails once the receipt is held: %s (%d tables)' % (
        not any(fits(c, EST_P, D) for c in lit_uu), len(lit_uu)))
    print('  (K3): if the population premise is put in question the derived result is not usable; then Z fits again: %s' %
          fits(EZ, EST_T, D))


if __name__ == '__main__':
    main()
