#!/usr/bin/env python3
"""A6 - a correction that sticks on p while the mistake comes back on a slightly different question.

The gardener. E0 ("the sunnier bed ripens first") answered S at the failed summer FSTAR (wet/windy/early/
sunS); the target's answer there is N and is established. W60.1: every candidate answering S at FSTAR is
not an account of p, nor of any question with the same target and query whose contract contains FSTAR.
Slightly different questions:
  (1) p_nb: same target and query, contract {B0, SHADE, NB} where NB = wet/calm/early/sunS (a neighbouring
      summer, untested) and FSTAR is not in it.
  (2) p_q2: same target and contract, a coarser query: "does the south bed ripen first?" (yes/no).
  (3) p_nbr: the neighbour's garden, whose early variety has no effect; same query and contract as p.
  (4) p_sun: same target and contract, query "which bed gets more sun?" (the equivocation "I meant sun").
"""
from ext import Org, Target, Cand, key, fits, rule
import garden as G

C = list(G.SETTINGS)
NB = G.S('wet', 'calm', 'early', 'S')
EST = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}


def main():
    print('=' * 100)
    print('A6  DOES THE MISTAKE COME BACK ON A SLIGHTLY DIFFERENT QUESTION?')
    print('=' * 100)
    E0 = G.e0()
    print('  on p: E0 answers %s at FSTAR, target %s; E0 fits: %s; Account(p): %s' % (
        sorted(E0.ans(G.FSTAR)), sorted(G.D.ans(G.FSTAR)), fits(E0, EST, G.D), E0.account(C, G.B0, G.D)))
    rule('(1) p_nb: same target and query; the contract omits FSTAR and holds an untested neighbour NB')
    Cnb = [G.B0, G.SHADE, NB]
    E0nb = G.e0("p_nb")
    estnb = {key(x): v for x, v in ((G.B0, EST[key(G.B0)]), (G.SHADE, EST[key(G.SHADE)]))}
    print('  E0 at NB: %s, target at NB: %s  -> E0 Account(p_nb) = %s (a fact of (A)); fits what is established on '
          'p_nb: %s' % (sorted(E0nb.ans(NB)), sorted(G.D.ans(NB)), E0nb.account(Cnb, G.B0, G.D), fits(E0nb, estnb, G.D)))
    print('  W60.1 is silent here (NB is not the failed pair); the failure on p stands: E0 Account(p) = %s' %
          E0.account(C, G.B0, G.D))
    rule('(2) p_q2: the coarser query "does the south bed ripen first?"')
    f = lambda A: frozenset('yes' if v == 'S' else 'no' for v in A)
    print('  E0\'s answer at FSTAR under Q2: %s; the target\'s: %s -> E0 fails (A) on p_q2: %s' % (
        sorted(f(E0.ans(G.FSTAR))), sorted(f(G.D.ans(G.FSTAR))), f(E0.ans(G.FSTAR)) != f(G.D.ans(G.FSTAR))))
    print('  the receipt for Ans_p(FSTAR) = N yields, by one derivation step, one for Ans_q2(FSTAR) = no; W60.1\'s text '
          'states the exclusion only for "the same target and query".')
    rule('(3) p_nbr: the neighbour\'s garden (the early variety has no effect there)')
    DO = G.D_ORG
    comps = dict(DO.comps)
    comps['dvar'] = (('V', 'ovrD'), frozenset({('late', 0), ('early', 0)}))
    D2 = Target(Org('neighbour', DO.ports, comps), 'first')
    print('  target\'s answer at FSTAR: %s; E0 Account on the neighbour\'s question: %s' % (
        sorted(D2.ans(G.FSTAR)), E0.account(C, G.B0, D2)))
    print('  the failed answer on p is the right answer here: a different target, and W60.1 does not claim it.')
    rule('(4) p_sun: "I meant which bed gets more sun"')
    Dsun = Target(G.D_ORG, 'Sun')
    E0s = Cand('E0 read for p_sun', E0.org, 'Sun', E0.tau, E0.pi, E0.anchors, E0.gamma, 'p_sun')
    ok_A = all(E0s.ans(x) == Dsun.ans(x) for x in C)
    print('  (A) on p_sun: %s; NonCircular: %s; Account(p_sun): %s' % (ok_A, E0s.nc(C, G.B0), E0s.account(C, G.B0, Dsun)))
    print('  whatever p_sun\'s fate, it is a question with a different query; W60.1\'s last sentence names only a contract '
          'that omits the pair, while Part III and D3:L151 cover a changed query.')


if __name__ == '__main__':
    main()
