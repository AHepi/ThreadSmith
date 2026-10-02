#!/usr/bin/env python3
"""s129_compute_what_reading_c_commits_the_theory_to.py

What it does, in plain words: for log S129 (decisions S83 and S84). Computes, on the S129 copy of the model program
(results/S129 Reading C carried into copies/model after Reading C/), the cases S127 named as consequences of Reading C
and a few more found while carrying it into the copies, each at the declared boundaries that matter, with the copy's
own provenance functions (sel, con, prov_fixed_points, entered_whole) and its (Suff) functions. Each case is a small
history whose facts are set by hand (Θ by hand, I90): which occurrences represent what, which holding is a record of
which, which occurrences a construction trace prepares, and whether doing the task changed the rate of copying. These
encodings are this script's, not the text's; the verdicts are the copy's. Cases:
  K1  one transport selected at one boundary and declared at another: the owner's condition (S41 Q2) and (Suff) as
      conjectured, with 'explanation' read once for both (unindexed) and once per boundary (FC30.new1 (c) recomputed)
  K2  the student's copied pendulum formula (FC30.new1 (d)) at the student's own boundary, two encodings of the copy
  K3  a bred animal: the boundary of the farm (breeder inside) and of the lineage (breeder outside)
  K4  a trait shaped by mate choice (a chooser inside the lineage whose preference was itself selected there)
  K5  a trait of a living species with no chooser: graded advantage stated true, stated false, not stated
  K6  a search people scored: the scoring code written outside the run's boundary; and a person scoring live
  K7  a live driver (Claude's growing-list runner) outside, inside, and with its writer inside the boundary
  K8  learning from a teacher within a life (S128): the labels a record of the teacher's, the weights built
  K9  rote learning, then reconstruction: is the reconstruction new to the learner (Deploy, (N), (G))?
  K10 Enable's non-question-begging clause (D16.3) at β, on every chain of up to three holdings
  K11 the bridge to a fixed brief (FC84.new1) with the client outside the engineer's boundary
  K12 the creative transport experiment (S104, CT8) with the designer's scorer outside the run's boundary
Output: printed, and results/S129 Reading C carried into copies/what Reading C commits the theory to - computed.json.

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s129_compute_what_reading_c_commits_the_theory_to.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import itertools, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')
OUTF = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'what Reading C commits the theory to - computed.json')
sys.path.insert(0, COPY)
os.environ.setdefault('S129_READING_C', '1')
os.environ.setdefault('S129_GRADED', '1')

from model import claims_b as cb  # noqa: E402
from model.core import ONE, account, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on, prov_fixed_points, fwd_pole_cand  # noqa: E402
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok  # noqa: E402
from model.args import Assessor, Imp, Not  # noqa: E402

OUT = {}


def lab(sc):
    return 'Sel' if sc[0] else ('Con' if sc[1] else 'Dec')


def fp(n, held, trace, selc, rec_of=None, beta=None):
    """The one fixed point's verdict per occurrence (cut T′), or the list when there are several."""
    f = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=rec_of, beta=beta)
    vs = [{'o%d' % (o + 1): lab(sc[o]) for o in range(n) if cb._in(beta, o)} for R, sc in f]
    reps = [sorted('o%d' % (o + 1) for o in R) for R, sc in f]
    return {'verdicts': vs[0] if len(vs) == 1 else vs, 'represent (Rep) at this boundary': reps[0] if len(reps) == 1 else reps}


def sv(c, H, h):
    s, k = sel(c, H, h), con(h)
    return {'Sel': s, 'Con': k, 'Dec': (not s and not k)}


def k1():
    p, c = fwd_pole_cand()
    acc = account(c)
    j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    H = [(ONE, 'b1_45')]
    occ = ['writer of the check', 'check', 'o_t']
    tags = [('writer of the check', 'surv'), ('writer of the check', 'cod'), ('check', 'surv'), ('check', 'cod')]
    h1 = Hist(occ, tags, set(p.C), beta=['check', 'o_t'], source={'check': 'writer of the check'}, advantage=True)
    h2 = Hist(occ, tags, set(p.C), beta=occ, source={'check': 'writer of the check'}, advantage=True)
    d1, d2 = sv(c, H, h1)['Dec'], sv(c, H, h2)['Dec']
    # unindexed: one value of Expl(ℰ) must meet (Suff) at β1 (Acc ∧ ¬Dec ⇒ Expl) and the owner's condition at β2 (Acc ∧ Dec ⇒ ¬Expl)
    unindexed = [e for e in (False, True) if ((not (acc and not d1)) or e) and expl_ok(acc, d2, e)]
    indexed = [(e1, e2) for e1 in (False, True) for e2 in (False, True)
               if ((not (acc and not d1)) or e1) and expl_ok(acc, d1, e1) and ((not (acc and not d2)) or e2) and expl_ok(acc, d2, e2)]
    return {'candidate': "the pole's forward candidate (FC30.new1's), Acc %s" % acc,
            'Dec at boundary 1 (the check inside, its writer outside)': d1, 'Dec at boundary 2 (both inside)': d2,
            '(Suff) defeated at boundary 1 for an assessor with an argument not using (E) that rules out Expl': suff_defeats(acc, d1, out, 'L536'),
            'values of an unindexed Expl meeting both': unindexed,
            'values of (Expl at 1, Expl at 2) meeting both, read per boundary': indexed,
            'reading': 'with one Expl for both boundaries there is no common model; read per boundary (L524) there is one, Expl true at 1 and false at 2'}


def k2():
    p, c = fwd_pole_cand()
    acc = account(c)
    j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    rows = {}
    for Hx, hl in (([(ONE, 'b1_45')], 'one pair tried'), ([], 'no pair tried')):
        held_o = bool(faithful(c))
        selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
        for enc, rof in (("the suite's encoding: components copied, bindings declared (not a transfer)", None),
                         ('the copy read as a transfer from the book (a record of its source)', [None, 0])):
            for bl, beta in (('the whole stated history (book and student)', None), ("the student's own boundary (the book outside)", {1})):
                r = fp(2, [1, held_o], [1, 0], [0, selc_o], rec_of=rof, beta=beta)
                v = r['verdicts']['o2'] if isinstance(r['verdicts'], dict) else r['verdicts']
                dec = v == 'Dec'
                rows['%s | %s | %s' % (hl, enc, bl)] = {'student holding': v,
                                                         "S41's condition applies (Acc and Dec)": bool(acc and dec),
                                                         '(Suff) defeated by the argument (L536)': suff_defeats(acc, dec, out, 'L536')}
    return rows


def k3():
    """A dog breed. o_b the breeder's wanting short legs (the breeder's own, formed inside any boundary that holds the
    breeder); o_pick the breeder picking parents each generation; o_t the trait's holding in a dog."""
    p, c = fwd_pole_cand()   # any faithful transport serves: the verdict turns on the history, not on the transport
    H = [(ONE, 'b1_45')]
    occ = ['breeder wants short legs', 'breeder picks parents', 'o_t']
    tags = [('breeder wants short legs', 'surv'), ('breeder wants short legs', 'cod'), ('breeder picks parents', 'surv')]
    rows = {}
    for bl, beta in (('the farm (breeder inside)', occ), ('the lineage of dogs (breeder outside)', ['o_t'])):
        rows[bl] = sv(c, H, Hist(occ, tags, set(p.C), beta=beta, advantage=True))
    occ2 = ['kennel club writes the breed standard', 'hired hand picks parents by the standard', 'o_t']
    tags2 = [('kennel club writes the breed standard', 'surv'), ('hired hand picks parents by the standard', 'surv')]
    src = {'hired hand picks parents by the standard': 'kennel club writes the breed standard'}
    for bl, beta in (('the farm, the standard written outside it and applied inside', occ2[1:]), ('the farm and the kennel club', occ2)):
        rows[bl] = sv(c, H, Hist(occ2, tags2, set(p.C), beta=beta, source=src, advantage=True))
    return rows


def k4():
    p, c = fwd_pole_cand()
    H = [(ONE, 'b1_45')]
    occ = ["peahens' preference (selected in the lineage)", 'peahens choose mates', 'o_t']
    tags = [("peahens' preference (selected in the lineage)", 'surv'), ("peahens' preference (selected in the lineage)", 'cod'),
            ('peahens choose mates', 'surv')]
    rows = {}
    for bl, beta in (('the lineage, both sexes (the choosers inside)', occ), ('the original: no boundary declared', None),
                     ('the tail alone (the choosers outside)', ['o_t'])):
        rows[bl] = sv(c, H, Hist(occ, tags, set(p.C), beta=beta, advantage=True))
    return rows


def k5():
    p, c = fwd_pole_cand()
    H = [(ONE, 'b1_45')]
    rows = {}
    for adv, al in ((True, 'doing it raised the rate of copying'), (False, 'it changed nothing about copying'), (None, 'no rate fact stated')):
        for g in (False, True):
            cb.GRADED = g
            rows['%s | graded %s' % (al, 'on' if g else 'off')] = sv(c, H, Hist(['world', 'o_t'], [], set(p.C), beta=['world', 'o_t'], advantage=adv))
    cb.GRADED = True
    return rows


def k6():
    p, c = fwd_pole_cand()
    H = [(ONE, 'b1_45')]
    occ = ['people write the scoring function', 'the scoring code runs', 'o_t']
    tags = [('people write the scoring function', 'surv'), ('people write the scoring function', 'cod'),
            ('the scoring code runs', 'surv'), ('the scoring code runs', 'cod')]
    src = {'the scoring code runs': 'people write the scoring function'}
    rows = {}
    for bl, beta in (("the run (the code inside, its writers outside)", occ[1:]), ('the run and the people', occ)):
        rows['fixed scoring code | ' + bl] = sv(c, H, Hist(occ, tags, set(p.C), beta=beta, source=src, advantage=True))
    occ2 = ['a person scores each generation by hand', 'o_t']
    tags2 = [('a person scores each generation by hand', 'surv'), ('a person scores each generation by hand', 'cod')]
    for bl, beta in (('the run with the person inside', occ2), ('the run with the person outside', ['o_t'])):
        rows['live scoring by a person | ' + bl] = sv(c, H, Hist(occ2, tags2, set(p.C), beta=beta, advantage=True))
    return rows


def k7():
    p, c = fwd_pole_cand()
    H = [(ONE, 'b1_45')]
    occ = ['Claude writes the runner', 'the runner adds tasks between pieces', 'Avida execution environment', 'o_t']
    tags = [('Claude writes the runner', 'surv'), ('the runner adds tasks between pieces', 'surv')]
    src = {'the runner adds tasks between pieces': 'Claude writes the runner'}
    rows = {}
    for bl, beta in (('S72: the execution environment (the runner outside)', occ[2:]),
                     ('the execution environment and the runner (its writer outside)', occ[1:]),
                     ('the execution environment, the runner and its writer', occ)):
        rows[bl] = sv(c, H, Hist(occ, tags, set(p.C), beta=beta, source=src, advantage=True))
    return rows


def k8():
    # o1 the teacher's own representation of the target (built by the teacher: trace, held); o2 the labels as the
    # learner receives them (a record of o1); o3 the learner's weights, built by its training run (trace), holding t
    rows = {}
    for bl, beta in (('the teacher and the learner', None), ("the learner's own boundary (the teacher outside)", {1, 2})):
        rows[bl] = fp(3, [1, 1, 1], [1, 0, 1], [0, 0, 0], rec_of=[None, 0, None], beta=beta)
    return rows


def k9():
    # o1 the teacher's (built); o2 the learner's rote copy (a record of o1); o3 the learner's later reconstruction (a trace)
    rows = {}
    for bl, beta in (('the teacher and the learner', None), ("the learner's own boundary", {1, 2})):
        r = fp(3, [1, 1, 1], [1, 0, 1], [0, 0, 0], rec_of=[None, 0, None], beta=beta)
        rep_o2 = 'o2' in (r['represent (Rep) at this boundary'] or [])
        # Deploy, Integrated, Can, Attempt, Build's other conjuncts set to hold (Θ by hand, I90): the rote copy is in the
        # learner's repertoire before the reconstruction exactly when it represents (D13.1); New (N) fails then.
        rows[bl] = dict(r, **{'the rote copy represents at this boundary': rep_o2,
                              'the rote copy is in the repertoire before the reconstruction (Deploy, other conjuncts set)': rep_o2,
                              'the reconstruction is new to the learner (N)': not rep_o2,
                              'the reconstruction is an origin (G), with Attempt and Build': not rep_o2})
    return rows


def k10():
    """NQB (D16.3): 'no realization ... uses an occurrence o with Rep_ℓ(o, c) whose provenance was relayed from outside β'.
    On every chain of ≤ 3 holdings with records, and every β that keeps the last holding: count the occurrences inside β
    that represent at β and whose holding is relayed from outside β (the clause's antecedent), with Rep read at β, and
    with Rep read on the whole history (the original)."""
    at_beta = whole = chains = 0
    for n in (2, 3):
        for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n):
            for rof in itertools.product(*[[None] + list(range(o)) for o in range(n)]):
                held = [1 if rof[o] is not None else b[0] for o, b in enumerate(bits)]
                trace, selc = [b[1] for b in bits], [b[2] for b in bits]
                full = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=list(rof))
                for r in range(n):
                    for sub in itertools.combinations(range(n - 1), r):
                        beta = set(sub) | {n - 1}
                        if len(beta) == n:
                            continue
                        chains += 1
                        relayed_in = [o for o in beta if rof[o] is not None and rof[o] not in beta]
                        fb = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=list(rof), beta=beta)
                        at_beta += sum(1 for R, sc in fb for o in relayed_in if o in R)
                        whole += sum(1 for R, sc in full for o in relayed_in if o in R)
    return {'chains and narrower boundaries tried': chains,
            'relayed-in holdings that represent, Rep read at β (the clause as Reading C reads it)': at_beta,
            'relayed-in holdings that represent, Rep read on the whole history (as the original reads it)': whole,
            'reading': 'at β the clause is never met, so NQB asks nothing; on the whole history it bites'}


def k11():
    # o1 the client's brief (the client's own: trace, held); o2 the brief as the engineer holds it (a record of o1);
    # o3 the design, built by the engineer's construction trace and holding the target
    rows = {}
    for bl, beta in (('the client and the engineer', None), ("the engineer's own boundary (the client outside)", {1, 2})):
        rows[bl] = fp(3, [1, 1, 1], [1, 0, 1], [0, 0, 0], rec_of=[None, 0, None], beta=beta)
    return rows


def k12():
    """S104's creative transport experiment, CT8's readings R1 (the run's carriers represent in the ordinary sense) and R3
    (the designer's code declared), with the designer's case table and scoring written outside the run's boundary."""
    sys.path.insert(0, COPY)
    import s104_creative_transport as ct
    EQ = ct.EQ
    D, pol = ct.target(EQ, 'D_EQ')
    p, cases = ct.question(D, pol, 'p_EQ')
    cq = ct.candidate(p, EQ, EQ, ['b'])
    H = [x for x, _ in cases]
    occ = ['designer writes cases and scoring', 'o_cases', 'o_score', 'o_trees', 'o_channel', 'o_switch']
    rows = {}
    for rid, rep, prep in (('R1', [('designer writes cases and scoring', 'H'), ('designer writes cases and scoring', 'surv'),
                                   ('o_cases', 'H'), ('o_score', 'surv'), ('o_trees', 't'), ('o_trees', 'cod')], True),
                           ('R2', [('designer writes cases and scoring', 'H'), ('designer writes cases and scoring', 'surv'),
                                   ('o_cases', 'H'), ('o_score', 'surv'), ('o_trees', 't'), ('o_trees', 'cod')], False),
                           ('R1 without the trees representing (only the designer\'s code and its writer)',
                            [('designer writes cases and scoring', 'H'), ('designer writes cases and scoring', 'surv'),
                             ('o_cases', 'H'), ('o_score', 'surv')], False)):
        for bl, beta in (("the run (the designer outside)", occ[1:]), ('the run and the designer', occ)):
            h = Hist(occ, rep, set(H), admitted=True, prepares=prep, beta=beta,
                     source={'o_cases': 'designer writes cases and scoring', 'o_score': 'designer writes cases and scoring'}, advantage=True)
            rows['%s | %s' % (rid, bl)] = sv(cq, H, h)
    return rows


def main():
    for name, fn in (('K1', k1), ('K2', k2), ('K3', k3), ('K4', k4), ('K5', k5), ('K6', k6), ('K7', k7), ('K8', k8),
                     ('K9', k9), ('K10', k10), ('K11', k11), ('K12', k12)):
        OUT[name] = fn()
    OUT['about'] = ('S129: consequences of Reading C (S83) and the graded survival condition (S84), computed on the S129 copy of the '
                    'model (switches: READING_C %s, GRADED %s). Θ by hand (I90): every occurrence, tag, record and rate fact is '
                    'this script\'s encoding. Built by tools/s129_compute_what_reading_c_commits_the_theory_to.py.' % (cb.READING_C, cb.GRADED))
    json.dump(OUT, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print(json.dumps(OUT, indent=1, ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
