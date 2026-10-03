#!/usr/bin/env python3
"""A12 - 02's option (b) for degenerate conflicts, which 02 did not run.
Option (b): two candidates conflict at x when their answers there differ, or each could meet (F1), (F2), (A)
there and no relations of the target there let both. 02 claims: (b) makes the owner's example kind (ii)
under both anchorings, and kind (ii)'s "no test the question admits is sure to solve" must then read
"no established answer"."""
from ext import key, test_solves, rule
from engine import conflict
import seasons as S


def conflict_b(c1, c2, x, D, space):
    if c1.ans(x) != c2.ans(x):
        return True
    c, a, b, n = conflict(c1, c2, x, D, space)
    return c and a and b


def main():
    print('=' * 100)
    print('A12  02\'s OPTION (b), RUN')
    print('=' * 100)
    q = 'p_greek'
    est = {key(x): ('ans', S.D.ans(x)) for x in S.GREEK}
    for real in (True, False):
        DEM = S.myth3('dem' + ('' if real else '[R-none]'), q, real=real)
        UND = S.myth2('und' + ('' if real else '[R-none]'), q, real=real)
        cb = [S.show(x) for x in S.GREEK if conflict_b(DEM, UND, x, S.D, 'functional')]
        kind = 'i' if cb else 'ii'
        sure = [S.show(x) for x in S.GREEK if test_solves(DEM, UND, x, S.D, est, 'functional', 'full')[0]]
        print('  %-26s option (b) conflicts in C: %-12s -> kind (%s); pairs of C where a relations test is sure to '
              'solve it: %s' % ('%s vs %s' % (DEM.name, UND.name), cb or 'none', kind, sure or 'none'))


if __name__ == '__main__':
    main()
