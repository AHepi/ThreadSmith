#!/usr/bin/env python3
"""A7 - can the mistake come back after a GOOD correction? Under full (E), one interpretation (E1's).

03 limit (i) and s1(1): members of Pres(F + f*) may repeat E0's wrong answer where no job reaches.
03 s1(1): "It is not a ratchet": dropping the failed job gives back the larger Pres.
Checked here with (A), (F1), (F2) and NonCircular, not (A) alone.
"""
from itertools import product
from fe import emb1_member, emb2_member, B0, SHADE, FSTAR, SEED, SETTINGS, truth, pres, E0, show

FULL = ('A', 'F1', 'F2', 'NC')
J_SEEN, J_FAIL, J_SEED, J_OPEN = [B0, SHADE], [B0, FSTAR], [B0, SEED], list(SETTINGS)
M0 = [x for x in SETTINGS if E0.org.ans(x) != truth(x)]


def repeats(m, jobs):
    inside = {tuple(sorted(x.items())) for C in jobs for x in C}
    return [x for x in M0 if tuple(sorted(x.items())) not in inside and m.org.ans(x) == E0.org.ans(x)]


def main():
    print('=' * 100)
    print('A7  THE MISTAKE COMING BACK AFTER A GOOD CORRECTION, FULL (E)')
    print('=' * 100)
    ports = ('V', 'W', 'Wi')
    configs = list(product(('late', 'early'), ('dry', 'wet'), ('calm', 'windy')))
    fam = []
    for g in ('id', 'allS', 'allN', 'swap'):
        for outs in product((0, 1), repeat=len(configs)):
            tab = dict(zip(configs, outs))
            fam.append(emb1_member(g, None, var_ports=ports, pred=lambda v, w, wi, t=tab: t[(v, w, wi)],
                                   label=''.join(map(str, outs))))
    print('family sun\' x var[V,W,Wi] with E1\'s transport: %d members' % len(fam))
    for jn, F in (('{j_seen, j_fail}', [J_SEEN, J_FAIL]), ('+ seed trial', [J_SEEN, J_FAIL, J_SEED]),
                  ('open question', [J_OPEN])):
        P = pres(fam, F, FULL)
        H = [m for m in P if repeats(m, F)]
        ex = ''
        if H:
            ex = 'e.g. %s repeats E0 at %s' % (H[0].name, ', '.join(show(x) for x in repeats(H[0], F)))
        print('  %-18s |Pres|=%3d  repeating E0\'s wrong answer at an unreached pair: %3d  %s' % (jn, len(P), len(H), ex))

    print()
    print('Not a ratchet: the corrected candidate narrowed back to the summers seen (Emb-2, rule family)')
    fam2 = [emb2_member(g, p) for g in ('id', 'allS', 'allN', 'swap') for p in ('off', 'always', 'early', 'late')]
    for jn, F in (('jobs {j_seen, j_fail}', [J_SEEN, J_FAIL]), ('narrowed to {j_seen}', [J_SEEN])):
        P = pres(fam2, F, FULL)
        print('  %-24s |Pres|=%d  members: %s' % (jn, len(P), ', '.join(m.name for m in P)))
    print('  -> the version that answers as E0 (rule: N if off ...) is back in Pres once the failed job is dropped.')


if __name__ == '__main__':
    main()
