#!/usr/bin/env python3
"""M6 - N1, Tomas with and without the sun god.

Target D: the seasons of seasons.py, with the steadiness of the axis made explicit.
  dspin   (axis,):                  the axis is kept steady (a spinning body keeps its axis)
  dexp    (place, half, axis, exp): steady -> lat * sign(half); drift -> 0
  dins, dseason as in seasons.py
Question: all six pairs of place and half, baseline (N, H1); established: the answers at all six.
Tomas (E_T): spin (anchored to dspin), geo (dexp), heat (dins), seas (dseason); all four active.
Tomas + the sun god, three readings (W33.1's CASES AT RISK, N1):
  idle      god (axis,) constrains nothing (the full relation), anchored to no component of D:
            "the sun god looks on and approves" (the case's own optional wording).
  route     god (axis,) = steady, anchored to dspin: a second component that keeps the tilt steady.
  unfaith   god (axis,) = steady, anchored to no component of D.
  zeus      the idle reading with the god renamed (the draft: "a telling that swaps the god for another
            god is one account with Tomas's").
"""
from engine import Org, Target, Cand, key, one_account, fits, problem, fmt_problem, does_no_work, supports

PLACES = ('N', 'E', 'S')
HALVES = ('H1', 'H2')
LAT = {'N': 1, 'E': 0, 'S': -1}
SG = {'H1': 1, 'H2': -1}
SEAS = {1: 'summer', 0: 'none', -1: 'winter'}
V3 = (1, 0, -1)
AX = ('steady', 'drift')
PAIRS = [{'place': p, 'half': h} for p in PLACES for h in HALVES]
B0 = {'place': 'N', 'half': 'H1'}
EXP = frozenset((p, h, a, (LAT[p] * SG[h] if a == 'steady' else 0)) for p in PLACES for h in HALVES for a in AX)
PORTS = {'place': PLACES, 'half': HALVES, 'axis': AX, 'exp': V3, 'ins': V3, 'season': ('summer', 'none', 'winter')}
D = Target(Org('D', PORTS, {'dspin': (('axis',), frozenset({('steady',)})),
                            'dexp': (('place', 'half', 'axis', 'exp'), EXP),
                            'dins': (('exp', 'ins'), frozenset((e, e) for e in V3)),
                            'dseason': (('ins', 'season'), frozenset((i, SEAS[i]) for i in V3))}), 'season')


def show(x):
    return '%s,%s' % (x['place'], x['half'])


def tomas(name, god=None, godname='god'):
    comps = {'spin': (('axis',), frozenset({('steady',)})),
             'geo': (('place', 'half', 'axis', 'exp'), EXP),
             'heat': (('exp', 'ins'), frozenset((e, e) for e in V3)),
             'seas': (('ins', 'season'), frozenset((i, SEAS[i]) for i in V3))}
    anchors = {'spin': ({'dspin'}, {'axis': 'axis'}),
               'geo': ({'dexp'}, {p: p for p in ('place', 'half', 'axis', 'exp')}),
               'heat': ({'dins'}, {'exp': 'exp', 'ins': 'ins'}),
               'seas': ({'dseason'}, {'ins': 'ins', 'season': 'season'})}
    if god:
        rel, anc = god
        comps[godname] = (('axis',), rel)
        anchors[godname] = (anc, {'axis': 'axis'})
    return Cand(name, Org(name, PORTS, comps), 'season', lambda x: dict(x), lambda z: dict(z), anchors, set(comps), 'p')


def main():
    print('=' * 100)
    print('M6  N1, TOMAS AND THE SUN GOD')
    print('=' * 100)
    FULL = frozenset({('steady',), ('drift',)})
    STEADY = frozenset({('steady',)})
    T = tomas('Tomas')
    IDLE = tomas('Tomas+god[idle]', (FULL, set()))
    ROUTE = tomas('Tomas+god[route]', (STEADY, {'dspin'}))
    UNF = tomas('Tomas+god[unfaithful]', (STEADY, set()))
    ZEUS = tomas('Tomas+zeus[idle]', (FULL, set()), godname='zeus')
    EST = {key(x): ('ans', D.ans(x)) for x in PAIRS}
    for c in (T, IDLE, ROUTE, UNF, ZEUS):
        print('  %-22s Account=%-5s fits=%-5s %s' % (c.name, c.account(PAIRS, B0, D), fits(c, EST, D),
                                                    ' '.join(c.account_why(PAIRS, B0, D, show)[:2])))
    print()
    print('  W33.1\'s test: does the god do no work by itself (every support stays one when it is added and when removed)?')
    for c, g in ((IDLE, 'god'), (ROUTE, 'god'), (UNF, 'god')):
        add, rem, S = does_no_work(c, g, PAIRS, B0, D)
        print('    %-22s addition half=%-5s removal half=%-5s supports: %s' % (
            c.name, add, rem, ', '.join('{%s}' % ','.join(sorted(W)) for W in sorted(S, key=len))))
    print()
    for other, off in ((IDLE, False), (IDLE, True), (ROUTE, True), (UNF, True)):
        print('  Tomas vs %s, offered in place of each other: %s' % (other.name, off))
        print(fmt_problem(problem(T, other, PAIRS, D, EST, offered=off, space='functional'), show))
    print('  Tomas+god[idle] vs Tomas+zeus[idle], offered in place of each other:')
    print(fmt_problem(problem(IDLE, ZEUS, PAIRS, D, EST, offered=True, space='functional'), show))
    print()
    print('  REPAIR tested: set aside every single commitment that does no work by itself (W33.1\'s test) before')
    print('  asking whether the two are one account.')
    for c in (IDLE, ROUTE, UNF):
        idle = [d for d in sorted(c.gamma) if all(does_no_work(c, d, PAIRS, B0, D)[:2])]
        red = c.restrict(c.gamma - set(idle), name=c.name + ' minus ' + (','.join(idle) or 'nothing'))
        print('    %-22s set aside: %-8s one account with Tomas: %s' % (c.name, idle or '-', one_account(T, red, PAIRS)))


if __name__ == '__main__':
    main()
