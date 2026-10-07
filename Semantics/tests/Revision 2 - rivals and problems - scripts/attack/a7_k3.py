#!/usr/bin/env python3
"""A7 - a rival that fits only because of a background assumption (K3).

The gardener. The result at the failed summer FSTAR (N first) has a receipt whose premises are the record
of the harvest (I) and "the two beds were watered alike that summer" (B). The earlier results (B0, SHADE)
have receipts with premises the two assessors share. Assessor j1 holds B and I live; assessor j2 has
withdrawn B (K2: withdrawing a premise removes a license), silently, without offering any claim about the
water. Harness: the 1,041 candidates of 02's M1 (6), used only to test the universal claim "alike".
"""
from itertools import product
from ext import key, fits, draft_verdict, rule
import garden as G

C = list(G.SETTINGS)
RECEIPTS = {key(G.B0): {'I'}, key(G.SHADE): {'I'}, key(G.FSTAR): {'I', 'B'}}


def established(live):
    return {k: ('ans', G.D.ans(dict(k))) for k, prem in RECEIPTS.items() if prem <= live}


def harness():
    hs = [G.e0()]
    cfgs = list(product(('late', 'early'), ('dry', 'wet'), ('calm', 'windy')))
    for g in G.SUNMAPS:
        for outs in product((0, 1), repeat=8):
            tab = dict(zip(cfgs, outs))
            hs.append(G.emb1('E1[%s,%s]' % (g, ''.join(map(str, outs))), lambda v, w, wi, t=tab: t[(v, w, wi)], g=g))
    for outs in product(('N', 'S'), repeat=4):
        tab = dict(zip(product(('late', 'early'), ('S', 'N')), outs))
        hs.append(G.emb2('E2[%s]' % ''.join(outs), lambda v, s, t=tab: t[(v, s)]))
    return hs


def main():
    print('=' * 100)
    print('A7  A RIVAL THAT FITS ONLY THROUGH A BACKGROUND ASSUMPTION (K3)')
    print('=' * 100)
    E0, GOOD = G.e0(), G.emb1('E_good', G.EARLY)
    j1, j2 = {'I', 'B'}, {'I'}
    for nm, live in (('j1 (holds B)', j1), ('j2 (dropped B)', j2)):
        est = established(live)
        print('  %-15s established pairs: %-60s E0 fits: %-5s  E_good vs E0: %s' % (
            nm, ', '.join(G.show(dict(k)) for k in est), fits(E0, est, G.D), draft_verdict(GOOD, E0, C, G.D, est, True)))
    rule('W60.1 "if they come into question, the exclusion does too, for every such candidate alike"')
    hs = harness()
    S = frozenset({'S'})
    rep = [c for c in hs if c.ans(G.FSTAR) == S]
    only_f = [c for c in rep if fits(c, established({'I'}), G.D)]          # fit everything but FSTAR
    e1, e2 = established(j1), established(j2)
    print('  harness: %d candidates; %d answer S at FSTAR; of these %d fit every result except FSTAR\'s' % (
        len(hs), len(rep), len(only_f)))
    print('  for j1: of those %d, fitting: %d' % (len(only_f), sum(fits(c, e1, G.D) for c in only_f)))
    print('  for j2: of those %d, fitting: %d  (revived alike: %s)' % (
        len(only_f), sum(fits(c, e2, G.D) for c in only_f), all(fits(c, e2, G.D) for c in only_f)))
    print('  no candidate answering N at FSTAR changes status between j1 and j2: %s' % all(
        fits(c, e1, G.D) == fits(c, e2, G.D) for c in hs if c.ans(G.FSTAR) != S))
    print('  -> the problem "E_good vs E0" exists for j2 and not for j1: the draft\'s "problem for p" is relative to '
          'an assessor, through "established", but the Problems paragraph does not say so.')


if __name__ == '__main__':
    main()
