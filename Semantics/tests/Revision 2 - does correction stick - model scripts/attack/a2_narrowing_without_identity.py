#!/usr/bin/env python3
"""A2 - the narrowing clause of (H*) and pointer (c), taken at their word.

03, section 2(b): "The same argument, with the identity edit as the witness, covers a narrowing. If E is an
account on every job of F and not on f*, then Pres(F) strictly contains Pres(F + f*)."
Pointer (c): "A narrowing that omits a job its candidate fails enlarges Pres whether or not that job was
ever claimed".
Stated hypotheses: E accounts on F; E does not account on f*. Not stated: that the identity edit is a
member of the declared family V. D3:L301 says only "a declared family V of organization edits".
"""
from fe import (E0, B0, SHADE, FSTAR, emb2_member, pres, SUNMAPS, Cand, Org, PORTS2, pi2)

J_SEEN = [B0, SHADE]
J_FAIL = [B0, FSTAR]
FULL = ('A', 'F1', 'F2', 'NC')


def e0_variant(g):
    """E0's organization with its sun map replaced by g (E0's transport, on E0's ports + V as unread input)."""
    return emb2_member(g, 'off')


def run(label, V):
    for conj, cn in ((('A',), '(A) only'), (FULL, 'full (E)')):
        P = pres(V, [J_SEEN], conj)
        Pp = pres(V, [J_SEEN, J_FAIL], conj)
        print('  %-58s %-9s |Pres(F)|=%d  |Pres(F+f*)|=%d  strictly larger after the narrowing? %s'
              % (label, cn, len(P), len(Pp), len(P) > len(Pp)))


def main():
    print('=' * 100)
    print('A2  NARROWING CLAUSE: E = E0 narrowed to the summers seen (F = {j_seen}), f* = the failed summer')
    print('=' * 100)
    print('Hypotheses: E0 accounts on j_seen? %s   E0 accounts on j_fail? %s' % (
        E0.account(J_SEEN), E0.account(J_FAIL)))
    ident = e0_variant('id')
    others = [e0_variant(g) for g in ('allS', 'allN', 'swap')]
    add_var = [emb2_member(g, 'early') for g in SUNMAPS]
    print()
    run('V1 = the other three sun maps (every edit changes something)', others)
    run('V2 = edits that add the variety part, any sun map', add_var)
    run('V1 + identity', others + [ident])
    run('V2 + identity', add_var + [ident])
    print()
    print('  V2 members in Pres(F) and in Pres(F+f*):', [m.name for m in pres(add_var, [J_SEEN], FULL)],
          [m.name for m in pres(add_var, [J_SEEN, J_FAIL], FULL)])


if __name__ == '__main__':
    main()
