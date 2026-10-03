#!/usr/bin/env python3
"""A5 - limit (iii) and the good/bad symmetry, under full (E) with one interpretation (E1's transport).

03 limit (iii): "Two members of V that are both accounts on F + f* both belong to Pres(F + f*). Only a job
on which one is an account and the other is not separates them, and that is (A) on that job, not
variation."
Attack 1: two members with the SAME answer at all 16 pairs, separated by a job through (F1)/(F2), not (A).
Attack 2: does the good/bad symmetry of 02 (CX2) survive when (F1), (F2) and NonCircular are checked?
"""
from itertools import product
from fe import emb1_member, B0, SHADE, ESHADE, FSTAR, SEED, RAIN, SETTINGS, truth, show, pres

FULL = ('A', 'F1', 'F2', 'NC')


def main():
    print('=' * 100)
    print('A5  LIMIT (iii) AND THE SYMMETRY UNDER FULL (E)')
    print('=' * 100)
    a = emb1_member('id', None, var_ports=('V', 'Sun'), pred=lambda v, s: int(v == 'early'), label='[V=early]')
    b = emb1_member('id', None, var_ports=('V', 'Sun'), pred=lambda v, s: int(v == 'early' and s == 'S'),
                    label='[V=early and Sun=S]')
    same = all(a.org.ans(x) == b.org.ans(x) for x in SETTINGS)
    print('(1) two members of sun\' x var[V,Sun]:  %s  and  %s' % (a.name, b.name))
    print('    same answer as each other at all 16 pairs? %s ; both right at all 16 pairs? %s' % (
        same, all(a.org.ans(x) == truth(x) == b.org.ans(x) for x in SETTINGS)))
    for jn, J in (('j_fail = {B0, f*}', [B0, FSTAR]), ('j_eshade = {B0, early/shadeS}', [B0, ESHADE]),
                  ('open question (16 pairs)', list(SETTINGS))):
        print('    %-32s first: %-5s second: %-5s  second fails: %s' % (
            jn, a.account(J, FULL), b.account(J, FULL), ' '.join(b.why(J)[:3]) or '-'))
    print('    -> a job separates them, and (A) holds for both at every pair: the separating conjunct is (F1)/(F2).')

    print()
    print('(2) good (var reads V) against bad (var reads W) in ONE family sun\' x var[V,W], E1\'s transport')
    good = emb1_member('id', None, var_ports=('V', 'W'), pred=lambda v, w: int(v == 'early'), label='early')
    bad = emb1_member('id', None, var_ports=('V', 'W'), pred=lambda v, w: int(w == 'wet'), label='wet')
    fam = []
    configs = list(product(('late', 'early'), ('dry', 'wet')))
    for g in ('id', 'allS', 'allN', 'swap'):
        for outs in product((0, 1), repeat=4):
            tab = dict(zip(configs, outs))
            fam.append(emb1_member(g, None, var_ports=('V', 'W'), pred=lambda v, w, t=tab: t[(v, w)],
                                   label=''.join(map(str, outs))))
    record = [[B0, SHADE], [B0, FSTAR]]
    for jn, F in (('the record + f*', record), ('+ seed trial', record + [[B0, SEED]]),
                  ('+ wet spring (with shade)', record + [[B0, SHADE, RAIN]]),
                  ('+ wet spring, no contrast', record + [[B0, RAIN]]), ('open question', [list(SETTINGS)])):
        P = pres(fam, F, FULL)
        print('    %-26s |Pres|=%2d   good in? %-5s bad in? %-5s' % (
            jn, len(P), all(good.account(C, FULL) for C in F), all(bad.account(C, FULL) for C in F)))
    print('    -> on the record both are accounts under full (E) as well; only a separating job decides.')
    print('    The job {B0, wet spring} has no pair whose answer differs from the baseline (both south), so')
    print('    NonCircular fails for EVERY member: good fails it for that reason alone: %s' % good.why([B0, RAIN]))


if __name__ == '__main__':
    main()
