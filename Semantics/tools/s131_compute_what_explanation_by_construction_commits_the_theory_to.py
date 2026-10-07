#!/usr/bin/env python3
"""s131_compute_what_explanation_by_construction_commits_the_theory_to.py

What it does, in plain words: for log S131 (decision S86, explanation kept for what was worked out). Computes, on the
S131 copy of the model program (results/S131 Explanation by construction carried into copies/model after Reading C and
explanation by construction/), what the third decision commits the theory to, case by case, each with the copy's own
provenance functions (sel, con, prov_fixed_points) and its two D16.XV functions (suff_defeats, expl_ok), and each
twice: with S86 on (explanation kept for constructed transports) and off (S129's copy: explanation for transports not
declared), both under Reading C and the graded condition. Each case is a small history whose facts are set by hand
(Θ by hand, I90), most of them S129's encodings reused (its K-cases); the verdicts are the copy's. Cases:
  N1  an adaptation of a living species, no chooser, no checker anyone wrote: doing it raised copying, or did not
  N2  a proof found by blind search against a checker people wrote; and a mathematician who works it through after
  N3  learning from a teacher's answers within a life (S128; S129's K8)
  N4  the owner's shop signs (S44, S45): the one-part and the two-part sign, with each of the three provenances
  N5  the student's copied formula at the student's own boundary (S129's K2), whole and narrow
  N6  rote learning, then reconstruction by the learner (S129's K9)
  N7  one transport at two boundaries (S129's K1): selected at one and declared at the other; constructed at one and
      declared at the other (a construction whose target is held only outside, I201)
  N8  the evolved NOT program (MC1) at the S72 boundary and at a boundary taking in Avida's authors (from the feeding)
For each: the provenance at each boundary, whether it represents (Rep: selected or constructed), whether (Suff)
conjectures it an explanation, whether the owner's condition rules that out, and in words what the semantics says.
Output: printed, and results/S131 Explanation by construction carried into copies/what explanation by construction
commits the theory to - computed.json.

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s131_compute_what_explanation_by_construction_commits_the_theory_to.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies')
COPY = os.path.join(OUT_DIR, 'model after Reading C and explanation by construction')
OUTF = os.path.join(OUT_DIR, 'what explanation by construction commits the theory to - computed.json')
FEED = os.path.join(OUT_DIR, 'map feeding with explanation by construction.json')
sys.path.insert(0, COPY)
for k in ('S129_READING_C', 'S129_GRADED', 'S131_EXPL_BY_CONSTRUCTION'):
    os.environ.setdefault(k, '1')

from model import claims_b as cb  # noqa: E402
from model.core import ONE, account, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on, prov_fixed_points, fwd_pole_cand  # noqa: E402
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok, provenance_of  # noqa: E402
from model.claims_s106 import sign_question, sign_one, sign_two  # noqa: E402
from model.args import Assessor, Imp, Not  # noqa: E402


def lab(s, k):
    return 'Sel' if s else ('Con' if k else 'Dec')


def judge(acc, s, k, name='E'):
    """Under S86 on and off: (Suff)'s conjecture, the owner's condition, and the word for it."""
    dec = not s and not k
    j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + name))])
    out = {}
    for x in (True, False):
        cb.EXPL_BY_CONSTRUCTION = x
        owner = bool(acc and ((not k) if x else dec))
        suff = bool(acc and (k if x else not dec))
        argued, _ = expl_ruled_out(j, name)
        if not acc:
            word = 'not an account'
        elif suff:
            word = 'an explanation (by the conjecture (Suff))'
        else:
            word = 'no explanation (the owner\'s condition)'
        if acc and (s or k):
            word += '; it represents (Rep): ' + ('evolved knowledge' if s else 'created knowledge')
        elif acc:
            word += '; declared: it represents nothing'
        out['S86 on' if x else 'S86 off (S129)'] = {
            '(Suff) conjectures it an explanation': suff, "the owner's condition says it is no explanation": owner,
            'in (Suff)\'s defeat set for an assessor who holds it is no explanation (L536)': suff_defeats(acc, dec, argued, 'L536', con=k),
            "the owner's condition met with Expl true": expl_ok(acc, dec, True, con=k), 'what the semantics says': word}
    cb.EXPL_BY_CONSTRUCTION = True
    return out


def row(c, H, h, acc=None):
    s, k = sel(c, H, h), con(h)
    acc = account(c) if acc is None else acc
    return dict({'Sel': s, 'Con': k, 'Dec': not s and not k, 'Acc (taken whole)': acc}, **judge(acc, s, k, c.name))


def fp_last(n, held, trace, selc, rec_of=None, beta=None):
    f = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=rec_of, beta=beta)
    assert len(f) == 1, f
    R, sc = f[0]
    return {'o%d' % (o + 1): lab(*sc[o]) for o in range(n) if cb._in(beta, o)}, sorted('o%d' % (o + 1) for o in R)


def n1():
    p, c = fwd_pole_cand()   # any account serves: the verdict turns on the history (S129's K5 did the same)
    H = [(ONE, 'b1_45')]
    out = {}
    for adv, al in ((True, 'doing it raised the rate of copying'), (False, 'it changed nothing about copying')):
        out[al] = row(c, H, Hist(['the world', 'o_t'], [], set(p.C), beta=['the world', 'o_t'], advantage=adv))
    return out


def n2():
    p, c = fwd_pole_cand()
    H = [(ONE, 'b1_45')]
    occ = ['people write the proof checker', 'the checker runs', 'the search varies proofs', 'o_t']
    tags = [('people write the proof checker', 'surv'), ('people write the proof checker', 'cod'),
            ('the checker runs', 'surv'), ('the checker runs', 'cod')]
    src = {'the checker runs': 'people write the proof checker'}
    out = {}
    for bl, beta in (('the search (the checker inside, its writers outside)', occ[1:]), ('the search and the people who wrote the checker', occ)):
        out['the proof the search found | ' + bl] = row(c, H, Hist(occ, tags, set(p.C), beta=beta, source=src, advantage=True))
    occ2 = ['the proof as found (a record)', 'a mathematician works it through, holding what it is to prove', 'o_t']
    tags2 = [('a mathematician works it through, holding what it is to prove', 'cod')]
    out["a mathematician's reconstruction | the mathematician's boundary"] = row(
        c, H, Hist(occ2, tags2, set(p.C), admitted=True, prepares=True, beta=occ2[1:], source={}))
    return out


def n3():
    # S129's K8: o1 the teacher's own representation (built: trace, held); o2 the answers as the learner gets them (a
    # record of o1); o3 the learner's weights, built by its training run (trace), holding t
    p, c = fwd_pole_cand()
    acc = account(c)
    out = {}
    for bl, beta in (('the teacher and the learner', None), ("the learner's own boundary (the teacher outside)", {1, 2})):
        v, R = fp_last(3, [1, 1, 1], [1, 0, 1], [0, 0, 0], rec_of=[None, 0, None], beta=beta)
        out[bl] = dict({'verdicts': v, 'represent (Rep)': R, "the learner's holding (o3)": v['o3']},
                       **judge(acc, v['o3'] == 'Sel', v['o3'] == 'Con', c.name))
    return out


def n4():
    p = sign_question()
    out = {}
    for c in (sign_one(p), sign_two(p)):
        acc = account(c)
        for kind in ('Dec', 'Sel', 'Con'):
            s, k, dec = provenance_of(c, kind, [(ONE, 'b0')])
            out['%s | %s' % (c.name, {'Dec': 'declared (written up)', 'Sel': 'selected (kept by trial with no target held)',
                                      'Con': 'constructed (worked out)'}[kind])] = dict({'Sel': s, 'Con': k, 'Dec': dec, 'Acc': acc}, **judge(acc, s, k, c.name))
    return out


def n5():
    p, c = fwd_pole_cand()
    acc = account(c)
    out = {}
    for Hx, hl in (([(ONE, 'b1_45')], 'one pair tried'), ([], 'no pair tried')):
        held_o = bool(faithful(c))
        selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
        for enc, rof in (("the suite's encoding: components copied, bindings declared (not a transfer)", None),
                         ('the copy read as a transfer from the book (a record of its source)', [None, 0])):
            for bl, beta in (('the whole stated history (book and student)', None), ("the student's own boundary (the book outside)", {1})):
                v, R = fp_last(2, [1, held_o], [1, 0], [0, selc_o], rec_of=rof, beta=beta)
                out['%s | %s | %s' % (hl, enc, bl)] = dict({"the student's holding": v['o2']}, **judge(acc, v['o2'] == 'Sel', v['o2'] == 'Con', c.name))
    return out


def n6():
    # S129's K9: o1 the teacher's (built); o2 the learner's rote copy (a record of o1); o3 the learner's later reconstruction
    p, c = fwd_pole_cand()
    acc = account(c)
    out = {}
    for bl, beta in (('the teacher and the learner', None), ("the learner's own boundary", {1, 2})):
        v, R = fp_last(3, [1, 1, 1], [1, 0, 1], [0, 0, 0], rec_of=[None, 0, None], beta=beta)
        out[bl] = {'verdicts': v, 'represent (Rep)': R,
                   'the rote copy (o2)': judge(acc, v['o2'] == 'Sel', v['o2'] == 'Con', c.name),
                   'the reconstruction (o3)': judge(acc, v['o3'] == 'Sel', v['o3'] == 'Con', c.name)}
    return out


def n7():
    p, c = fwd_pole_cand()
    acc = account(c)
    H = [(ONE, 'b1_45')]
    out = {}
    occ = ['writer of the check', 'check', 'o_t']
    tags = [('writer of the check', 'surv'), ('writer of the check', 'cod'), ('check', 'surv'), ('check', 'cod')]
    pairs = {'selected at boundary 1 (the check inside, its writer outside), declared at boundary 2 (both inside)':
             (Hist(occ, tags, set(p.C), beta=['check', 'o_t'], source={'check': 'writer of the check'}, advantage=True),
              Hist(occ, tags, set(p.C), beta=occ, source={'check': 'writer of the check'}, advantage=True))}
    occ2 = ['the client holds the target', 'the engineer builds t', 'o_t']
    tags2 = [('the client holds the target', 'cod')]
    pairs['constructed at boundary 1 (the target-holder inside), declared at boundary 2 (the target held only outside, I201)'] = (
        Hist(occ2, tags2, set(p.C), admitted=False, prepares=True, beta=occ2),
        Hist(occ2, tags2, set(p.C), admitted=False, prepares=True, beta=occ2[1:]))
    for name, (h1, h2) in pairs.items():
        r = {}
        for x in (True, False):
            cb.EXPL_BY_CONSTRUCTION = x
            (s1, k1), (s2, k2) = (sel(c, H, h1), con(h1)), (sel(c, H, h2), con(h2))
            d1, d2 = not s1 and not k1, not s2 and not k2
            need = lambda kk, dd: (kk if x else not dd)               # (Suff)'s antecedent
            ok = lambda kk, dd, e: expl_ok(acc, dd, e, con=kk)        # the owner's condition
            unindexed = [e for e in (False, True) if ((not (acc and need(k1, d1))) or e) and ok(k1, d1, e)
                         and ((not (acc and need(k2, d2))) or e) and ok(k2, d2, e)]
            indexed = [(e1, e2) for e1 in (False, True) for e2 in (False, True)
                       if ((not (acc and need(k1, d1))) or e1) and ok(k1, d1, e1) and ((not (acc and need(k2, d2))) or e2) and ok(k2, d2, e2)]
            r['S86 on' if x else 'S86 off (S129)'] = {'boundary 1': lab(s1, k1), 'boundary 2': lab(s2, k2),
                                                      'values of one unindexed Expl meeting (Suff) and the owner\'s condition at both': unindexed,
                                                      'values of (Expl at 1, Expl at 2), read per boundary': indexed}
        cb.EXPL_BY_CONSTRUCTION = True
        out[name] = r
    return out


def n8():
    feed = json.load(open(FEED, encoding='utf-8'))
    out = {}
    for setting in ('C on, graded on, S86 on', 'C on, graded on, S86 off'):
        rows = feed['settings'][setting]['MC1 (graded-pay run: doing NOT raised the rate of copying)']['provenance and (Suff)']
        for nm, r in rows.items():
            if nm.startswith('C at'):
                out['%s | %s' % (setting, nm.split(':')[0])] = {k: r[k] for k in ('Sel', 'Con', 'Dec', 'Rep: the program stands for NOT (faithful on the task and Sel or Con)',
                                                                                  'what the semantics says of the program taken whole')}
    return out


def main():
    OUT = {}
    for name, fn in (('N1 adaptation in nature', n1), ('N2 proof found by blind search; reconstruction', n2), ("N3 learning from a teacher's answers", n3),
                     ("N4 the owner's shop signs", n4), ("N5 the student's copied formula", n5), ('N6 rote learning, then reconstruction', n6),
                     ('N7 one transport at two boundaries', n7), ('N8 the evolved NOT program', n8)):
        OUT[name] = fn()
    OUT['about'] = ('S131: what decision S86 (explanation kept for what was worked out) commits the theory to, computed on the S131 copy '
                    '(Reading C and the graded condition on; S86 on and off for each case). Θ by hand (I90): every occurrence, tag, '
                    'record and rate fact is this script\'s encoding or S129\'s (its K1, K2, K5, K6, K8, K9). Built by '
                    'tools/s131_compute_what_explanation_by_construction_commits_the_theory_to.py.')
    json.dump(OUT, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(OUT, indent=1, ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
