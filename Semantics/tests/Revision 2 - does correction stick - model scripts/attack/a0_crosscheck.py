#!/usr/bin/env python3
"""A0 - independent re-derivation of the numbers 02 and 03 rely on (pair-level, Account = (A)).
Nothing is imported from ratchet/models. A mismatch would be an error in 02/03 or here."""
from pl import (pred_menu, SUN4, SINGLE, family, count, pres, J_BEFORE, J_AFTER, C_FULL, SEED, RAIN, FSTAR,
                mask, M0, R0, NS, FULLM, sun_menu, TRUTH, SETTINGS, get)

EXPECT = []


def check(label, got, want):
    ok = got == want
    EXPECT.append(ok)
    print('  %-70s got %-12s 02/03 says %-12s %s' % (label, got, want, 'OK' if ok else 'MISMATCH'))


def hybrids(fam, F):
    P = [m for _, m in fam if m & F == F]
    rest = M0 & ~F
    return len(P), sum(1 for m in P if (~m) & rest)


def main():
    print('=' * 100)
    print('A0  INDEPENDENT RE-DERIVATION OF 02/03 NUMBERS')
    print('=' * 100)
    MV, MW, MWWi = pred_menu(('V',)), pred_menu(('W',)), pred_menu(('W', 'Wi'))
    U1 = family(SUN4, [MV, MW, SINGLE])
    U2 = family(SUN4, [MV, MWWi, SINGLE])
    RICH = family(SUN4, [pred_menu(('V', 'W', 'Wi'))])
    check('|U1|', len(U1), 1088)
    check('U1 |Pres(J_before)|', count(U1, J_BEFORE), 68)
    check('U1 |Pres(J_after)|', count(U1, J_AFTER), 52)
    check('U1 |Pres(J_after + seed)|', count(U1, J_AFTER | mask([SEED])), 35)
    check('U1 |Pres(J_after + BG_rain)|', count(U1, J_AFTER | mask([RAIN])), 17)
    check('U1 |Pres(C_full)|', count(U1, C_FULL), 13)
    check('U2 |Pres(J_before)|, |Pres(J_after)|', (count(U2, J_BEFORE), count(U2, J_AFTER)), (272, 208))
    check('rich sun x var[V,W,Wi] |Pres(J_before)|, |Pres(J_after)|', (count(RICH, J_BEFORE), count(RICH, J_AFTER)), (128, 64))
    check('hybrids U1 (in Pres, repeating E0 elsewhere)', hybrids(U1, J_AFTER), (52, 18))
    check('hybrids U2', hybrids(U2, J_AFTER), (208, 71))
    check('hybrids rich', hybrids(RICH, J_AFTER), (64, 56))
    check('hybrids rich, seed trial added', hybrids(RICH, J_AFTER | mask([SEED])), (32, 24))
    check('open question: U1, U2, rich |Pres|', (count(U1, C_FULL), count(U2, C_FULL), count(RICH, C_FULL)), (13, 13, 1))
    # CX2 symmetric pairs
    for gp, bp, want in ((('V',), ('W',), (1, 1)), (('V', 'Wi'), ('W', 'Wi'), (4, 4)), (('V', 'Sun'), ('W', 'Sun'), (6, 6)),
                         (('V', 'W'), ('W', 'V'), (4, 4)), (('V', 'W', 'Wi'), ('W', 'V', 'Wi'), (64, 64))):
        g = family(SUN4, [pred_menu(gp)])
        b = family(SUN4, [pred_menu(bp)])
        check('CX2 good[%s] : bad[%s]' % ('+'.join(gp), '+'.join(bp)), (count(g, J_AFTER), count(b, J_AFTER)), want)
    # CX3 grid corners
    for gp, bp, want in ((('V',), ('W', 'Wi', 'Sun'), (1, 96)), (('V', 'W', 'Wi'), ('W',), (64, 1))):
        g = family(SUN4, [pred_menu(gp)])
        b = family(SUN4, [pred_menu(bp)])
        check('CX3 good[%s] : bad[%s]' % ('+'.join(gp), '+'.join(bp)), (count(g, J_AFTER), count(b, J_AFTER)), want)
    check('patch, single-exception family |Pres(J_after)|', count(family(SUN4, [SINGLE]), J_AFTER), 1)
    check('patch, any-predicate family (4 ports) |Pres(J_after)|',
          count(family(SUN4, [pred_menu(('W', 'Wi', 'V', 'Sun'))]), J_AFTER), 24576)
    # redescription
    check('rain split in two: |Pres(J_before)| -> |Pres(J_after)|',
          (count(family(SUN4, [MW, MW]), J_BEFORE), count(family(SUN4, [MW, MW]), J_AFTER)), (4, 3))
    check('rain split in five', (count(family(SUN4, [MW] * 5), J_BEFORE), count(family(SUN4, [MW] * 5), J_AFTER)), (32, 31))
    # extension: all 65536 F, U1
    v0keys = {k for k, _ in U1 if k[1:] == (0, 0, 0)}
    strict = 0
    for F in range(1 << NS):
        P = [k for k, m in U1 if m & F == F]
        P0 = [k for k in P if k in v0keys]
        strict += len(P0) < len(P)
    check('U1: Pres_V0(F) strictly inside Pres_V(F), number of the 65536 F', strict, 65536)
    print()
    print('  all checks agree: %s (%d of %d)' % (all(EXPECT), sum(EXPECT), len(EXPECT)))


if __name__ == '__main__':
    main()
