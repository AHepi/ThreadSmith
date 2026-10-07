#!/usr/bin/env python3
"""R1 - the repaired wording of 05, run against the counterexamples of 04b.

Repaired (H*) (05, section 2): if some member v0 of a declared family V satisfies Account(E_v0, f) for every
f in F and not Account(E_v0, f*), then v0 is in Pres(F) but not in Pres(F + f*), so the containment is strict.
The witness hypothesis is stated at the level of Account, under whatever interpretation V gives v0,
not as "E_1,v0 = E0" (the 03 wording that CE1 broke).

Bridge (05, section 2): E_v0 has the earlier candidate's verdicts on every job when E_v0 is that candidate
together with, at most, input ports that every pair sets and on which no relation depends. It can fail
when the change adds a port that the transport reads from the target (CE1, Emb-1).

Narrowing clause (05, section 2): needs the identity edit in V (CE3).

Checks:
  R1  the repaired (H*) and the (a) iff, over every family and job set below: the hypothesis holds exactly
      when the containment is strict; the counterexamples of 04b are the cases where it does not hold.
  R2  the bridge: Emb-2's v0 and E0 have the same Account verdict on all 32,768 contracts holding the
      baseline; Emb-1's switched-off and deleted versions do not.
  R3  the narrowing clause with and without the identity edit.
  R4  the repair (a) of 04b: a family of candidate edits that holds E0 with its own transport.
  R5  the clean control for "v0 fails f*", with jobs read as questions and as pairs.
  R6  limit (i) reworded: what survives at unreached pairs is fixed by the family.
Uses ../attack/fe.py (full (E), Part II solution semantics) and ../attack/pl.py (pair level, (A) only).
Standard library only.
"""
import os
import random
import sys
from itertools import combinations, product

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'attack'))
from fe import (E0, B0, SHADE, ESHADE, FSTAR, SEED, RAIN, SETTINGS, emb1_member, emb1_alpha, emb2_member,  # noqa: E402
                PRED_V, SUNMAPS, freeze, truth, show)
import pl  # noqa: E402

random.seed(5)
FULL = ('A', 'F1', 'F2', 'NC')
AONLY = ('A',)
JOBS = {
    'j_seen': [B0, SHADE],
    'j_eshade': [B0, ESHADE],
    'j_fail': [B0, FSTAR],
    'j_seed': [B0, SEED],
    'j_rain': [B0, SHADE, RAIN],
    'j_rain_nc': [B0, RAIN],
    'j_open': list(SETTINGS),
}
JN = list(JOBS)


def table(fam, conj):
    return {id(m): {j: m.account(JOBS[j], conj) for j in JN} for m in fam}


def sweep(fam, conj, maxF=3):
    """For every F (a set of jobs, size <= maxF) and every f* outside F: (hypothesis, strict) counts."""
    t = table(fam, conj)
    counts = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}
    for r in range(0, maxF + 1):
        for F in combinations(JN, r):
            PF = [m for m in fam if all(t[id(m)][f] for f in F)]
            for fs in JN:
                if fs in F:
                    continue
                hyp = any(not t[id(m)][fs] for m in PF)
                PFs = [m for m in PF if t[id(m)][fs]]
                strict = len(PFs) < len(PF)
                counts[(hyp, strict)] += 1
    return counts


def fams():
    emb1 = [emb1_member(g, p) for g in SUNMAPS for p in PRED_V]
    emb2 = [emb2_member(g, p) for g in SUNMAPS for p in PRED_V]
    emb2_nooff = [emb2_member(g, p) for g in SUNMAPS for p in PRED_V if p != 'off']
    ident = emb2_member('id', 'off')
    v1 = [emb2_member(g, 'off') for g in ('allS', 'allN', 'swap')]
    v2 = [emb2_member(g, 'early') for g in SUNMAPS]
    rich = []
    configs = list(product(('late', 'early'), ('dry', 'wet'), ('calm', 'windy')))
    for g in SUNMAPS:
        for outs in product((0, 1), repeat=len(configs)):
            tab = dict(zip(configs, outs))
            rich.append(emb1_member(g, None, var_ports=('V', 'W', 'Wi'),
                                    pred=lambda v, w, wi, t=tab: t[(v, w, wi)], label=''.join(map(str, outs))))
    return [
        ('Emb-1 (16, E1\'s transport)', emb1),
        ('Emb-1 + alpha (17)', emb1 + [emb1_alpha()]),
        ('Emb-1 + E0 with its own transport (17)', emb1 + [E0]),
        ('Emb-2 (16)', emb2),
        ('Emb-2 without the "off" setting (12)', emb2_nooff),
        ('A2 V1 (3)', v1),
        ('A2 V1 + identity (4)', v1 + [ident]),
        ('A2 V2 (4)', v2),
        ('A2 V2 + identity (5)', v2 + [ident]),
        ('A7 rich sun\' x var[V,W,Wi] (1024)', rich),
    ], ident, emb1, emb2


# ------------------------------------------------------------------ per-pair decomposition of Account
def witness_at(c, x):
    """The non-circular-dependence witness at pair x, exactly as fe.Cand.noncirc tests it."""
    g = sorted(c.gamma)
    ab = c.org.ans(B0)
    ax = c.org.ans(x)
    if ax == ab:
        return False
    det = lambda a: len(a) == 1
    for r in range(1, len(g) + 1):
        for G in combinations(g, r):
            ax2, ab2 = c.org.ans(x, G), c.org.ans(B0, G)
            if (det(ax2) and det(ab2) and ax2 == ab2) or (det(ax) and not det(ax2)) or (det(ab) and not det(ab2)):
                return True
    return False


def masks(c):
    good = wit = 0
    for i, x in enumerate(SETTINGS):
        if c.A(x) and c.F2(x) and c.F1(x):
            good |= 1 << i
        if witness_at(c, x):
            wit |= 1 << i
    return good, wit


B0I = [i for i, x in enumerate(SETTINGS) if freeze(x) == freeze(B0)][0]


def acct_mask(good, wit, C):
    return bool(C >> B0I & 1) and (C & ~good) == 0 and (C & wit) != 0


def contracts_with_b0():
    others = [i for i in range(16) if i != B0I]
    for bits in range(1 << 15):
        C = 1 << B0I
        for k, i in enumerate(others):
            if bits >> k & 1:
                C |= 1 << i
        yield C


def as_list(C):
    return [SETTINGS[i] for i in range(16) if C >> i & 1]


def main():
    print('=' * 100)
    print('R1  THE REPAIRED WORDING AGAINST THE COUNTEREXAMPLES')
    print('=' * 100)
    families, ident, emb1, emb2 = fams()

    print()
    print('-' * 100)
    print('R1  repaired (H*) and the (a) iff: every F (up to 3 of the 7 jobs) and every f* outside F')
    print('    counts of (witness hypothesis, strict containment); only (T,T) and (F,F) may occur')
    print('-' * 100)
    print('    jobs: ' + ', '.join('%s=%s' % (j, '{' + ', '.join(show(x) for x in JOBS[j]) + '}' if j != 'j_open'
                                   else 'all 16 pairs') for j in JN))
    total_bad = 0
    for name, fam in families:
        for conj, cn in ((AONLY, '(A) only'), (FULL, 'full (E)')):
            c = sweep(fam, conj)
            bad = c[(True, False)] + c[(False, True)]
            total_bad += bad
            print('  %-40s %-9s (T,T)=%4d (F,F)=%4d  hypothesis true but not strict=%d  strict without hypothesis=%d'
                  % (name, cn, c[(True, True)], c[(False, False)], c[(True, False)], c[(False, True)]))
    print('  failures of the repaired (H*) or of the iff, all families: %d' % total_bad)

    print()
    print('  The counterexamples of 04b under the repaired hypothesis (full (E)):')
    beta = [m for m in emb1 if m.name == "(sun'=id, var=off)"][0]
    alpha = emb1_alpha()
    v0_2 = [m for m in emb2 if m.name == '(rule: N if off else id(Sun))'][0]
    F = ['j_seen', 'j_eshade']
    for label, fam, v0 in (('CE1 Emb-1, v0 = beta (switched off)', emb1, beta),
                           ('CE1 Emb-1 + alpha, v0 = alpha (deleted)', emb1 + [alpha], alpha),
                           ('CE2 Emb-2, v0 = rule ignoring V', emb2, v0_2),
                           ('R4  Emb-1 + E0 with its own transport', emb1 + [E0], E0)):
        hyp_v0 = all(v0.account(JOBS[f], FULL) for f in F) and not v0.account(JOBS['j_fail'], FULL)
        hyp_any = any(all(m.account(JOBS[f], FULL) for f in F) and not m.account(JOBS['j_fail'], FULL) for m in fam)
        P = [m for m in fam if all(m.account(JOBS[f], FULL) for f in F)]
        Pp = [m for m in P if m.account(JOBS['j_fail'], FULL)]
        print('   %-42s F={j_seen, j_eshade}, f*=j_fail: hypothesis for the named v0? %-5s for some member? %-5s'
              '  |Pres| %d -> %d  strict? %s' % (label, hyp_v0, hyp_any, len(P), len(Pp), len(Pp) < len(P)))
    print('   -> CE1: the repaired hypothesis is false, so the lemma makes no claim, and indeed 1 -> 1.')
    print('      CE2 and R4: it is true, and the containment is strict (2 -> 1).')

    print()
    print('-' * 100)
    print('R2  the bridge: does v0 have E0\'s Account verdict on every contract holding the baseline? (full (E))')
    print('-' * 100)
    g0, w0 = masks(E0)
    for label, v in (('Emb-2 v0: rule ignoring V (added port V is an input the pair sets)', v0_2),
                     ('Emb-1 beta: var switched off (added port ovr read from the target)', beta),
                     ('Emb-1 alpha: sun restored, var deleted (ovr left free)', alpha),
                     ('E0 itself, with its own transport', E0)):
        gv, wv = masks(v)
        n = diff = e0yes = 0
        example = None
        for C in contracts_with_b0():
            n += 1
            a0, av = acct_mask(g0, w0, C), acct_mask(gv, wv, C)
            e0yes += a0
            if a0 != av:
                diff += 1
                if example is None or bin(C).count('1') < bin(example).count('1'):
                    example = C
        ex = ''
        if example is not None:
            ex = '  smallest: {%s}' % ', '.join(show(x) for x in as_list(example))
        print('  %-72s contracts=%d  E0 an account on %d  verdicts differ on %d%s' % (label, n, e0yes, diff, ex))
    # sanity: the per-pair decomposition agrees with fe's own Account
    agree = True
    sample = random.sample(list(contracts_with_b0()), 300)
    for v in (E0, v0_2, beta, alpha):
        gv, wv = masks(v)
        for C in sample:
            if acct_mask(gv, wv, C) != v.account(as_list(C), FULL):
                agree = False
    print('  sanity: per-pair decomposition equals fe Account on 300 random contracts x 4 candidates: %s' % agree)

    print()
    print('-' * 100)
    print('R3  narrowing clause: E = E0 (the identity edit), accounts on F, not on f*; is Pres(F) strictly larger?')
    print('-' * 100)
    for name, fam in families:
        if not any(m is ident for m in fam) and name not in ('A2 V1 (3)', 'A2 V2 (4)'):
            continue
        for conj, cn in ((AONLY, '(A) only'), (FULL, 'full (E)')):
            t = table(fam, conj)
            ti = {j: ident.account(JOBS[j], conj) for j in JN}
            inst = strict = 0
            for r in range(0, 4):
                for Fs in combinations(JN, r):
                    if not all(ti[f] for f in Fs):
                        continue
                    for fs in JN:
                        if fs in Fs or ti[fs]:
                            continue
                        inst += 1
                        PF = [m for m in fam if all(t[id(m)][f] for f in Fs)]
                        if any(not t[id(m)][fs] for m in PF):
                            strict += 1
            print('  %-28s %-9s identity in V? %-5s  instances=%3d  strict=%3d  not strict=%3d'
                  % (name, cn, any(m is ident for m in fam), inst, strict, inst - strict))

    print()
    print('-' * 100)
    print('R5  the clean control for "v0 fails f*" (a job the witness also does)')
    print('-' * 100)
    fam = families[3][1]   # Emb-2
    for conj, cn in ((AONLY, '(A) only'), (FULL, 'full (E)')):
        for fs in ('j_rain', 'j_rain_nc'):
            P = [m for m in fam if m.account(JOBS['j_seen'], conj)]
            Pp = [m for m in P if m.account(JOBS[fs], conj)]
            print('  Emb-2, F={j_seen}, f*=%-9s %-9s v0 does f*? %-5s  |Pres| %d -> %d  strict? %s'
                  % (fs, cn, v0_2.account(JOBS[fs], conj), len(P), len(Pp), len(Pp) < len(P)))
    fam_pl = pl.family(pl.SUN4, [pl.pred_menu(('V',))])
    a, b = pl.count(fam_pl, pl.J_BEFORE), pl.count(fam_pl, pl.J_BEFORE | pl.mask([pl.RAIN]))
    print('  pair level, sun x var[V], F=J_before, f*=another wet spring (usual planting): |Pres| %d -> %d  strict? %s'
          % (a, b, b < a))
    print('  -> with jobs as questions, {B0, wet spring} has no contrast, so NO member does it (strict for a')
    print('     reason unrelated to the witness); with a contrast held ({B0, shade, wet spring}), E0 does it and')
    print('     the shrink is not strict. The hypothesis "v0 fails f*" is needed.')

    print()
    print('-' * 100)
    print('R6  limit (i): members of Pres(F + f*) repeating E0\'s wrong answer at pairs no job holds (full (E))')
    print('-' * 100)
    M0 = [x for x in SETTINGS if E0.org.ans(x) != truth(x)]
    for name, fam in (families[3], families[9]):
        for Fn in (('j_seen', 'j_fail'), ('j_seen', 'j_fail', 'j_seed'), ('j_open',)):
            inside = {freeze(x) for f in Fn for x in JOBS[f]}
            P = [m for m in fam if all(m.account(JOBS[f], FULL) for f in Fn)]
            H = [m for m in P if any(freeze(x) not in inside and m.org.ans(x) == E0.org.ans(x) for x in M0)]
            print('  %-36s F=%-32s |Pres|=%3d  repeating E0 at an unreached pair: %3d'
                  % (name, '{' + ', '.join(Fn) + '}', len(P), len(H)))
    print('  -> the same jobs leave the mistake open in the rich family and closed in the poor one: fixed by V.')


if __name__ == '__main__':
    main()
