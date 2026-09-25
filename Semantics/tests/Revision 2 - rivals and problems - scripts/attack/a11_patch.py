#!/usr/bin/env python3
"""A11 - "easy to vary" against any candidate on a question narrower than the admitted changes.

Deutsch p.27: Aristarchus could modify the tilt theory: "In the known world, the seasons happen at the times
of year predicted by the axis-tilt theory; everywhere else on Earth, they also happen at those times of year."
Here: the tilt, and the tilt with its geometry component patched at the far south (same cut, same anchors,
different relation only at pairs outside the Greek question). Question p_greek (the two Greek pairs);
admitted: the six (place, half) pairs. Established: the Greek-era answers.
"""
from ext import Org, Cand, key, fits, draft_verdict, verdict_fix, one_account, rule
import seasons as S


def main():
    print('=' * 100)
    print('A11  THE p.27 VARIANT: A SAME-CUT PATCH OUTSIDE THE QUESTION')
    print('=' * 100)
    T = S.tilt('p_greek')
    geo = frozenset((p, h, (S.LAT[p] * S.SG[h] if p != 'S' else S.SG[h])) for p in S.PLACES for h in S.HALVES)
    comps = dict(T.org.comps)
    comps['geo'] = (('place', 'half', 'exp'), geo)
    P27 = Cand('tilt, in phase in the south (p.27)', Org('p27', T.org.ports, comps), 'season', T.tau, T.pi, T.anchors,
               T.gamma, 'p_greek')
    est = {key(x): ('ans', S.D.ans(x)) for x in S.GREEK}
    print('  accounts of p_greek: tilt %s, p.27 variant %s; of the world question: tilt %s, variant %s' % (
        T.account(S.GREEK, S.B0, S.D), P27.account(S.GREEK, S.B0, S.D), T.account(S.PAIRS, S.B0, S.D),
        P27.account(S.PAIRS, S.B0, S.D)))
    print('  one account on C_greek (draft parenthesis): %s' % (one_account(T, P27, S.GREEK),))
    print('  draft:      %s' % draft_verdict(T, P27, S.GREEK, S.D, est, True, 'functional'))
    print('  03b repair: %s' % ' '.join(verdict_fix(T, P27, S.GREEK, S.PAIRS, S.D, est, True, 'functional')))
    print('  -> under the repair (and under the owner\'s refinement 2) the tilt is "easy to vary" on p_greek once anyone')
    print('     offers the p.27 variant; the same construction works for any candidate that claims anything at an')
    print('     admitted change outside the contract (patch one component\'s relation there: Derivation 3\'s proof).')


if __name__ == '__main__':
    main()
