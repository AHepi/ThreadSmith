#!/usr/bin/env python3
"""A1 - does the witness v0 survive when Account is (E), not (A) alone, under ONE interpretation?

(H*) hypotheses (03, section 2): a family V of organization edits of the later organization E1 with a
member v0 such that E1_v0 = E0 ("the earlier candidate's organization, each component it keeps with its
earlier anchor, and the named background fixed"); Account(E0, f) for f in F; not Account(E0, f*).
Conclusion: v0 in Pres(F) minus Pres(F + f*), so Pres(F + f*) is strictly inside Pres(F).

File 00 (F00:L294): "Each pair retains its edited components, background, and interpretation."
03 (section 2): "(H*) relates two subsets of one family of one organization under one interpretation".
So each member of V is assessed with E1's transport. E0 is assessed with its own.

Two embeddings of ONE correction (the neighbour's early variety), with the same final answers everywhere:
  Emb-1  the correction posits a mechanism with its own port: var: ovr = [V=early]; sun': N if ovr else
         g(Sun). E1's transport reads ovr from the target's variety effect (ovrD).
  Emb-2  the same correction written as a changed rule with no new port: rule: N if P(V) else g(Sun).
Jobs (each a contract holding the baseline):
  j_seen   = {the recorded summers, the shading test}
  j_eshade = {baseline, a shaded year in which the neighbour planted early}   E0 answers north: right
  j_fail   = {baseline, the failed sixth summer}                                E0 answers south: wrong
"""
from fe import (E0, B0, SHADE, ESHADE, FSTAR, SETTINGS, emb1_member, emb1_alpha, emb2_member, pres, show,
                PRED_V, SUNMAPS, truth)

J_SEEN = [B0, SHADE]
J_ESHADE = [B0, ESHADE]
J_FAIL = [B0, FSTAR]
J_OPEN = list(SETTINGS)
FULL = ('A', 'F1', 'F2', 'NC')
AONLY = ('A',)


def names(P):
    return '{' + ', '.join(m.name for m in P) + '}'


def main():
    print('=' * 100)
    print('A1  THE WITNESS UNDER FULL (E), ONE INTERPRETATION PER FAMILY')
    print('=' * 100)
    print('E0 (own transport) on each job, full (E):')
    for nm, C in (('j_seen', J_SEEN), ('j_eshade', J_ESHADE), ('j_fail', J_FAIL), ('j_open', J_OPEN)):
        print('   %-9s Account=%-5s %s' % (nm, E0.account(C), ' '.join(E0.why(C)[:3])))

    emb1 = [emb1_member(g, p) for g in SUNMAPS for p in PRED_V]
    alpha = emb1_alpha()
    beta = [m for m in emb1 if m.name == "(sun'=id, var=off)"][0]
    good1 = [m for m in emb1 if m.name == "(sun'=id, var=early)"][0]
    emb2 = [emb2_member(g, p) for g in SUNMAPS for p in PRED_V]
    v0_2 = [m for m in emb2 if m.name == '(rule: N if off else id(Sun))'][0]
    good2 = [m for m in emb2 if m.name == '(rule: N if early else id(Sun))'][0]

    print()
    print('Sanity: the corrected candidate is an account on the open question (all 16 pairs), full (E):')
    print('   Emb-1 %-28s %s' % (good1.name, good1.account(J_OPEN)))
    print('   Emb-2 %-28s %s' % (good2.name, good2.account(J_OPEN)))
    print('   answers of the two corrected candidates agree at every pair? %s' % all(
        good1.org.ans(x) == good2.org.ans(x) == truth(x) for x in SETTINGS))

    print()
    print('Literal hypothesis "E1_v0 = E0": port sets')
    print('   E0 ports           :', sorted(E0.org.ports))
    print('   every Emb-1 member :', sorted(emb1[0].org.ports), '(an organization edit cannot delete a port)')
    print('   Emb-2 v0 ports     :', sorted(v0_2.org.ports), '(E0 plus the input V, read by nothing)')
    print('   any Emb-1 member with E0\'s port set? %s' % any(set(m.org.ports) == set(E0.org.ports) for m in emb1 + [alpha]))

    fams = [
        ('Emb-1, v0 = var switched off (beta)', emb1, beta),
        ('Emb-1 + v0 = sun restored, var deleted (alpha)', emb1 + [alpha], alpha),
        ('Emb-2, v0 = rule ignoring V', emb2, v0_2),
    ]
    for conj, cn in ((AONLY, '(A) ONLY, as in ratchet/models'), (FULL, 'FULL (E): (A), (F1), (F2), NonCircular')):
        print()
        print('-' * 100)
        print('Account read as ' + cn)
        print('-' * 100)
        for F, fn in (([J_SEEN], 'F = {j_seen}'), ([J_SEEN, J_ESHADE], 'F = {j_seen, j_eshade}')):
            e0F = all(E0.account(C, FULL) for C in F)
            e0f = E0.account(J_FAIL, FULL)
            print('%s   [E0 own, full (E): does F? %s  does f*? %s]' % (fn, e0F, e0f))
            for fam_name, fam, v0 in fams:
                P = pres(fam, F, conj)
                Pp = pres(fam, F + [J_FAIL], conj)
                strict = set(map(id, Pp)) < set(map(id, P))
                print('   %-46s |Pres(F)|=%d |Pres(F+f*)|=%d  strict? %-5s  v0 in Pres(F)? %-5s  Pres(F+f*)=%s'
                      % (fam_name, len(P), len(Pp), strict, v0 in P, names(Pp)))
                if conj == FULL and v0 not in P:
                    bad = [C for C in F if not v0.account(C, FULL)]
                    print('      v0 fails:', '; '.join(' '.join(v0.why(C)[:4]) for C in bad))

    print()
    print('-' * 100)
    print('What v0 (beta) asserts that E0 did not: its ovr port against the target\'s variety effect')
    print('-' * 100)
    for x in (B0, SHADE, ESHADE, FSTAR):
        print('   %-26s E0 answer %-5s v0 answer %-5s v0 ovr %s  target ovrD %s' % (
            show(x), sorted(E0.org.ans(x)), sorted(beta.org.ans(x)),
            sorted({z['ovr'] for z in beta.org.sol(x)}), 1 if x['V'] == 'early' else 0))


if __name__ == '__main__':
    main()
