#!/usr/bin/env python3
"""A5 - a problem "solved" by narrowing the question.

The gardener's two rescues, E_good ("early variety") and E_bad ("wet spring"), on p (every kind of spring
and planting, 16 settings): a problem of kind (i), conflicting at 8 settings (02, M1 (2)). Nothing is
established at those 8. The proponents then narrow: p_n has the contract C_n = the 16 settings minus the
8 where the two conflict. The offer history is a log of (time, candidate, question, offered/withdrawn).
  t1: both offered for p, in place of each other.
  t2: both withdrawn from p and offered for p_n, in place of each other.
The draft's "offered" is read two ways: (now) currently offered; (ever) has been offered.
"""
from ext import key, fits, draft_verdict, verdict_fix, conflict_p, rule, one_account
import garden as G

C = list(G.SETTINGS)
EST = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}


def offered(log, a, b, q, t, reading):
    def state(c):
        ev = [(tt, act) for (tt, cn, qq, act) in log if cn == c and qq == q and tt <= t]
        if not ev:
            return False
        return True if reading == 'ever' else ev[-1][1] == 'offered'
    return state(a) and state(b)


def main():
    print('=' * 100)
    print('A5  A PROBLEM "SOLVED" BY NARROWING THE QUESTION')
    print('=' * 100)
    GOOD, BAD = G.emb1('E_good', G.EARLY), G.emb1('E_bad', G.WET)
    conf = [x for x in C if conflict_p(GOOD, BAD, x, G.D)[0]]
    Cn = [x for x in C if all(key(x) != key(y) for y in conf)]
    print('  conflict pairs on p: %d (%s ...); C_n keeps %d settings' % (len(conf), G.show(conf[0]), len(Cn)))
    log = [(1, 'E_good', 'p', 'offered'), (1, 'E_bad', 'p', 'offered'),
           (2, 'E_good', 'p', 'withdrawn'), (2, 'E_bad', 'p', 'withdrawn'),
           (2, 'E_good', 'p_n', 'offered'), (2, 'E_bad', 'p_n', 'offered')]
    Gn, Bn = GOOD.with_question('p_n'), BAD.with_question('p_n')
    rule('(1) the draft, time by time')
    for t in (1, 2):
        for reading in ('now', 'ever'):
            op = offered(log, 'E_good', 'E_bad', 'p', t, reading)
            opn = offered(log, 'E_good', 'E_bad', 'p_n', t, reading)
            vp = draft_verdict(GOOD, BAD, C, G.D, EST, op)
            vn = draft_verdict(Gn, Bn, Cn, G.D, EST, opn) if opn else 'not rivals: not offered'
            print('  t%d, "offered" read as %-4s  p: %-58s p_n: %s' % (t, reading, vp, vn))
    print('  nothing was established at the 8 conflict pairs between t1 and t2: established pairs are %s' % (
        [G.show(dict(k)) for k in EST]))
    rule('(2) p_n under the draft (same cut: one account on C_n?) and under the 03b repair')
    print('  one account on C_n: %s' % (one_account(Gn, Bn, Cn),))
    print('  03b repair on p_n (admitted: all 16): %s' % ' '.join(verdict_fix(Gn, Bn, Cn, C, G.D, EST, True)))
    print('  03b repair on p   (admitted: all 16): %s' % ' '.join(verdict_fix(GOOD, BAD, C, C, G.D, EST, True)))


if __name__ == '__main__':
    main()
