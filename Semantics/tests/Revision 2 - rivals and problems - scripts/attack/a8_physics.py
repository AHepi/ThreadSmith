#!/usr/bin/env python3
"""A8 - rivals that can both meet the conditions at a pair only in a world the adopted physics forbids.

W59.1 defines conflict "whatever the target's relations there". Part I: which organizations a carrier can
bear is fixed by the adopted physics, and every attribution must be permitted by it. Does the quantifier
range over every relation, or over those the physics admits? The classification of a problem turns on it.

Target D (a current splitter): input a (0/1); two channels m1, m2 (0/1); out = the current delivered.
  d1    (a, m1)       actual: m1 = a            (channel 1 takes the current)
  d2    (a, m2)       actual: m2 = 0
  dcons (a, m1, m2)   LAW: m1 + m2 = a          (conservation: the adopted physics fixes it)
  dout  (m1, m2, out) LAW: out = m1 + m2
R1 "channel 1 carries it": k1 (a, m1) m1 = a anchored d1;  kc (a, out) out = a anchored {dcons, dout}.
R2 "channel 2 carries it": k2 (a, m2) m2 = a anchored d2;  kc as R1's.
Both answer out = a everywhere. Contract C: a = 0 and a = 1. Established: the answers at both.
"""
from itertools import combinations, product
from ext import Org, Target, Cand, key, fits, one_account, draft_verdict, rule

B = (0, 1)
PORTS = {'a': B, 'm1': B, 'm2': B, 'out': (0, 1, 2)}
LAW_CONS = frozenset((a, m1, a - m1) for a in B for m1 in B if a - m1 in B)
LAW_OUT = frozenset((m1, m2, m1 + m2) for m1 in B for m2 in B)
D = Target(Org('splitter', PORTS, {'d1': (('a', 'm1'), frozenset({(0, 0), (1, 1)})),
                                   'd2': (('a', 'm2'), frozenset({(0, 0), (1, 0)})),
                                   'dcons': (('a', 'm1', 'm2'), LAW_CONS),
                                   'dout': (('m1', 'm2', 'out'), LAW_OUT)}), 'out')
C = [{'a': 0}, {'a': 1}]
B0 = {'a': 0}
IDR = frozenset({(0, 0), (1, 1)})


def cand(name, port, dcomp):
    org = Org(name, {'a': B, port: B, 'out': (0, 1, 2)}, {'k': (('a', port), IDR), 'kc': (('a', 'out'), IDR)})
    return Cand(name, org, 'out', lambda x: dict(x), lambda z, p=port: {'a': z['a'], p: z[p], 'out': z['out']},
                {'k': ({dcomp}, {'a': 'a', port: port}), 'kc': ({'dcons', 'dout'}, {'a': 'a', 'out': 'out'})},
                {'k', 'kc'}, 'p')


def subsets(tuples):
    return [frozenset(s) for r in range(len(tuples) + 1) for s in combinations(tuples, r)]


def phys_variants(x):
    """The target relations at x that the adopted physics admits: d1, d2 free; the two laws fixed."""
    a = x['a']
    for r1, r2 in product(subsets([(a, 0), (a, 1)]), subsets([(a, 0), (a, 1)])):
        yield {'d1': r1, 'd2': r2, 'dcons': LAW_CONS, 'dout': LAW_OUT}


def main():
    print('=' * 100)
    print('A8  A CONFLICT THAT ONLY THE ADOPTED PHYSICS MAKES')
    print('=' * 100)
    R1, R2 = cand('R1 channel 1', 'm1', 'd1'), cand('R2 channel 2', 'm2', 'd2')
    est = {key(x): ('ans', D.ans(x)) for x in C}
    for c in (R1, R2):
        print('  %-14s Account=%-5s fits=%s   %s' % (c.name, c.account(C, B0, D), fits(c, est, D),
                                                    ' '.join(c.account_why(C, B0, D, lambda x: 'a=%d' % x['a']))))
    print('  one account (draft parenthesis): %s' % (one_account(R1, R2, C),))
    x1 = {'a': 1}
    W = {'d1': frozenset({(1, 1)}), 'd2': frozenset({(1, 1)}), 'dcons': frozenset({(1, 1, 1)}), 'dout': frozenset({(1, 1, 1)})}
    print('  witness over ALL relations at a=1 (the laws deformed: m1 = m2 = 1, delivered 1): R1 meets %s, R2 meets %s'
          % (R1.meets(x1, D, W), R2.meets(x1, D, W)))
    for x in C:
        joint = any(R1.meets(x, D, r) and R2.meets(x, D, r) for r in phys_variants(x))
        c1 = any(R1.meets(x, D, r) for r in phys_variants(x))
        c2 = any(R2.meets(x, D, r) for r in phys_variants(x))
        print('  a=%d, relations the physics admits: some let both meet: %-5s  some let R1: %-5s some let R2: %s' % (
            x['a'], joint, c1, c2))
    print('  draft verdict (conflict over all relations):          %s' % draft_verdict(R1, R2, C, D, est, True))

    def phys(rels, x):
        return rels['dcons'] == LAW_CONS and rels['dout'] == LAW_OUT
    kinds = ['i' if not any(R1.meets(x, D, r) and R2.meets(x, D, r) for r in phys_variants(x)) else '-' for x in C]
    print('  with the quantifier over what the physics admits:     PROBLEM for p, kind (%s)  (conflict at a=1)' % (
        'i' if 'i' in kinds else 'ii'))
    def with_rel(r):
        e = dict(est)
        e[key(x1)] = ('full', r)
        return e
    solves = all(not (fits(R1, with_rel(r), D) and fits(R2, with_rel(r), D)) for r in phys_variants(x1))
    print('  a test at a=1 establishing the relations: sure to solve over what the physics admits: %s' % solves)
    print('  so the draft\'s kind-(ii) sentence "no test the question admits is sure to solve" holds of this pair only by '
          'counting outcomes the physics forbids, and "the remedy is a finer contract" is not needed: a test inside C solves it.')


if __name__ == '__main__':
    main()
