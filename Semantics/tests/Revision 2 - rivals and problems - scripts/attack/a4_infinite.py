#!/usr/bin/env python3
"""A4 - infinitely many rivals.

A continuous family, stated symbolically (exact rationals; nothing is enumerated as a list of rivals):
  target: the variety effect fires when spring rainfall r exceeds 3 (r a rational >= 0).
  E_t (t >= 0 rational): "the effect fires when r > t". Same cut, same anchor for every t.
  The admitted changes: every rational rainfall r >= 0 (an infinite set).
  p_dry: contract = {r in {0, 1, 2}} (the dry-climate question). p_all: contract = every admitted r.
  Established: the target's answer (fires or not) at r = 0, 1, 2.
Claims tested, for arbitrary members (quantified symbolically, then spot-checked on a sample):
  - E_s and E_t (s < t) conflict exactly at the r with s < r <= t (one anchor, different relations).
  - on p_dry: E_s and E_t both fit iff s, t >= 2; they are then kind (ii) (draft as repaired) or "one account"
    (draft as written, the same-cut defect); on p_all they are kind (i).
  - one test at r = 4 solves every problem among pairs with s < 4 <= t, and no other; infinitely many
    problems remain; no finite set of tests solves them all, and none of the draft's claims needs it to.
  - "easy to vary" of E_3 (the true member) on p_dry needs ONE exhibited rival.
"""
from fractions import Fraction as F


def fires(t, r):
    return r > t


def conflict_set_desc(s, t):
    lo, hi = min(s, t), max(s, t)
    return lo, hi   # conflict at r iff lo < r <= hi


def conflicts_at(s, t, r):
    lo, hi = conflict_set_desc(s, t)
    return lo < r <= hi


def fits(t, est):
    return all(fires(t, r) == v for r, v in est.items())


def main():
    print('=' * 100)
    print('A4  INFINITELY MANY RIVALS (symbolic)')
    print('=' * 100)
    TRUE_T = F(3)
    est = {F(r): fires(TRUE_T, F(r)) for r in (0, 1, 2)}
    C_dry = [F(0), F(1), F(2)]
    sample = [F(n, 4) for n in range(0, 41)]            # t in [0, 10] step 1/4: a spot check only
    # (1) conflict set, checked on the sample against an independent pointwise test
    ok = all(conflicts_at(s, t, r) == (fires(s, r) != fires(t, r))
             for s in sample[::3] for t in sample[::5] for r in sample)
    print('  (1) E_s, E_t conflict exactly at s < r <= t (spot check, %d triples): %s' % (
        len(sample[::3]) * len(sample[::5]) * len(sample), ok))
    # (2) which members fit on p_dry: t >= 2 (symbolic: fires(t, r) must be False for r = 0,1,2 -> t >= 2)
    fitset = [t for t in sample if fits(t, est)]
    print('  (2) members that fit the dry-climate results: every t >= 2 (sample: min fitting t = %s, all t >= 2 fit: %s)' % (
        min(fitset), all(fits(t, est) for t in sample if t >= 2)))
    s, t = F(3), F(5)
    k_dry = 'i' if any(conflicts_at(s, t, r) for r in C_dry) else 'ii'
    print('      E_3 vs E_5 on p_dry: conflict inside C_dry: %s -> kind (%s) (as repaired); draft as written: '
          'same cut, same anchor, same relations on C_dry -> "one account", not rivals' % (k_dry == 'i', k_dry))
    print('      E_3 vs E_5 on p_all: they conflict at every r in (3, 5] -> kind (i)')
    # (3) one test at r = 4
    r_test = F(4)
    print('  (3) a test at r = 4 solves the problem of E_s vs E_t iff s < 4 <= t (or t < 4 <= s):')
    for (a, b) in ((F(2), F(5)), (F(3), F(7, 2)), (F(9, 2), F(6)), (F(5, 2), F(4))):
        solved = conflicts_at(a, b, r_test)
        print('      E_%s vs E_%s: solved by the test at 4: %s' % (a, b, solved))
    print('      after it, the fitting members are t in [2, 4) (every one fires at r = 4 iff t < 4, target fires): '
          'infinitely many; pairs among them still pose problems of kind (i) on p_all.')
    print('      no finite set of tests {r_1..r_n} leaves one member: between two consecutive tested values lie '
          'infinitely many t, all agreeing on every tested r.')
    # (4) easy to vary with one exhibited rival
    print('  (4) E_3 is "easy to vary" on p_dry as soon as ONE rival (say E_5) is offered: kind (ii) as repaired. '
          'Nothing counts the members or lists them.')
    # (5) W60.1 over the family
    bad_r = F(1)   # suppose some E_t had answered "fires" at r = 1 (t < 1): the target does not fire there
    print('  (5) W60.1 over the family: every E_t with t < 1 answers "fires" at r = 1, the target does not: '
          'excluded alike, for all (infinitely many) at once; sample check: %s' % all(
              not fits(t, {bad_r: False}) for t in sample if t < 1))


if __name__ == '__main__':
    main()
