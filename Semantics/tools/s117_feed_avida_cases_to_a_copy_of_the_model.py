#!/usr/bin/env python3
"""s117_feed_avida_cases_to_a_copy_of_the_model.py

What it does, in plain words: for log S117 (computation C4 of the plan). It copies the semantics' model program after
round 4 (results/S107 Round 4 - maths after the reading/model after round 4/model) into the scratch space
(s117/model_copy/; the program in the repository is never edited) and feeds the copy four small cases built from what
the Avida work recorded, at one bit per number (exact for Avida's bitwise logic tasks; two bits in MC2), and asks the
model's own functions for the semantics' verdicts:
  MC1  one Avida program that does NOT (S112's most common NOT program of run low seed 2: out = nand(x, x)), offered
       as an explanatory candidate for the world's task question "what number should be handed back?": (E) and each
       of its conditions, for the program as one block and for the program cut into its instructions; its provenance
       by the model's own Sel and Con under two readings of what its history holds (A: the code in Avida that checks
       the task is not an occurrence of that history that represents anything; B: it is, and it represents the survival
       condition and the task); and (Suff)'s defeat condition for an assessor who holds an argument, not using (E),
       that the program is not an explanation (the owner's reading of Avida as knowledge without explanation, S59, S60).
  MC2  two programs, both doing NOT on the numbers in the order Avida's world hands them, one also in another order
       and one not (the pattern C3 found in 16 of 18 S116 populations): fidelity on the history and on the wider
       contract, survival, and underdetermination at the unseen order (D12.9, Argument 3).
  MC3  a program that does the task in two places (S112: about 2 in 100 program-task pairs): routes, critical blocks,
       contributory and indispensable (D7.2, D7.3, D7.5).
  MC4  an extra read: Avida's instruction ablation (the read replaced by nop-X, so the next read takes this one's
       number) against the semantics' deletion (the component imposes the full relation), at two grains.
Output: printed, and scratch space s117/model_cases.json.

  python3 -B Semantics/tools/s117_feed_avida_cases_to_a_copy_of_the_model.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading', 'model after round 4', 'model')
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s117'
COPY = SC + '/model_copy'


def fresh_copy():
    if os.path.exists(COPY):
        shutil.rmtree(COPY)
    shutil.copytree(SRC, COPY + '/model', ignore=shutil.ignore_patterns('__pycache__'))
    sys.path.insert(0, COPY)


fresh_copy()
from model.core import ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, routes, restrict  # noqa: E402
from model.core import critical_block, contributory, indispensable, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on  # noqa: E402
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok, SUFF_READINGS  # noqa: E402
from model.args import Assessor, Imp, Not  # noqa: E402

OUT = {}


def org(name, ports, dom, comps, foot, B, A, rel):
    """An organization whose relation at (a, b) is rel(j, a, b), a set of tuples over foot[j]."""
    return Org(name, ports, dom, comps, foot, B, A, lambda a2, a1: None, rel)


def ident(ports):
    return {v: Translation((v,)) for v in ports}


# ---- MC1: one program, the world's NOT task, one bit --------------------------------------------------------------
def mc1():
    bit = (0, 1)
    B = ['u0', 'u1']                      # the number handed in, at one bit: 0 or 1
    uval = {'u0': 0, 'u1': 1}
    # the target: the world's task as Avida's check defines it (the number handed back should be NOT of the one handed in)
    D = org('D_task(NOT)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_x', 'c_task'], {'c_x': ('x',), 'c_task': ('x', 'y')},
            B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'c_x' else {(x, 1 - x) for x in bit})
    C = [(ONE, 'u0'), (ONE, 'u1')]
    p = Question(D, C, 'u0', PortQuery(), 'y', name='p_task')
    nand = lambda u, v: 1 - (u & v)
    # the program as one block: what Avida recorded it doing, out = nand(x, x)
    E1 = org('E_program(one block)', ['x', 'y'], {'x': bit, 'y': bit}, ['e_x', 'e_prog'], {'e_x': ('x',), 'e_prog': ('x', 'y')},
             B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'e_x' else {(x, nand(x, x)) for x in bit})
    c1 = Candidate(E1, p, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B},
                   {'e_prog': (frozenset(['c_task']), ident(['x', 'y']))}, ['e_prog'], 'y', name='program')
    acc1, d1 = account(c1, detail=True)
    # the program cut into its instructions (S112's trace: read, push, pop into a second register, nand, swap, write out)
    ports = ['x', 'bx', 'cx', 'z', 'y']
    foot = {'e_x': ('x',), 'read': ('x', 'bx'), 'copy': ('bx', 'cx'), 'nand': ('bx', 'cx', 'z'), 'out': ('z', 'y')}
    def rel2(j, a, b):
        if j == 'e_x':
            return {(uval[b],)}
        if j in ('read', 'copy', 'out'):
            return {(v, v) for v in bit}
        return {(u, v, nand(u, v)) for u in bit for v in bit}
    E2 = org('E_program(instructions)', ports, {v: bit for v in ports}, list(foot), foot, B, [ONE], rel2)
    lam = {'read': (frozenset(['c_x']), {'x': Translation(('x',)), 'bx': Translation(('x',))}),
           'copy': (frozenset(['c_x']), {'bx': Translation(('x',)), 'cx': Translation(('x',))}),
           'nand': (frozenset(['c_task']), {'bx': Translation(('x',)), 'cx': Translation(('x',)), 'z': Translation(('y',))}),
           'out': (frozenset(['c_task']), {'z': Translation(('y',)), 'y': Translation(('y',))})}
    pi2 = {'x': Translation(('x',)), 'bx': Translation(('x',)), 'cx': Translation(('x',)), 'z': Translation(('y',)), 'y': Translation(('y',))}
    c2 = Candidate(E2, p, pi2, {ONE: ONE}, {b: b for b in B}, lam, ['read', 'copy', 'nand', 'out'], 'y', name='program_steps')
    acc2, d2 = account(c2, detail=True)
    # provenance, by the model's own Sel and Con, on the history the world gave (both bit values met)
    H = [(ONE, 'u0'), (ONE, 'u1')]
    occ = set(C)
    hA = Hist(['world runs the lineage', 'selection by replication', 'o_t'], [], occ, admitted=True, prepares=False)
    hB = Hist(['Avida task-check code', 'world runs the lineage', 'selection by replication', 'o_t'],
              [('Avida task-check code', 'surv'), ('Avida task-check code', 'cod')], occ, admitted=True, prepares=False)
    rows = {}
    for nm, h in (('A: the task-check code represents nothing in the history', hA),
                  ('B: the task-check code is an earlier occurrence that represents the survival condition and the task', hB)):
        s, k = sel(c1, H, h), con(h)
        dec = (not s) and (not k)
        j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c1.name))])
        out, _ = expl_ruled_out(j, c1.name)
        rows[nm] = {'Sel': s, 'Con': k, 'Dec': dec, 'argument not using (E) rules out Expl': out,
                    '(Suff) defeated, by reading': {r: suff_defeats(acc1, dec, out, r) for r in SUFF_READINGS},
                    'owner S41 condition Acc and Dec => not Expl, with Expl false': expl_ok(acc1, dec, False)}
    return {'(E) of the program as one block': acc1, 'conditions (one block)': {k: bool(v) for k, v in d1.items()},
            '(E) of the program cut into its instructions': acc2, 'conditions (instructions)': {k: bool(v) for k, v in d2.items()},
            'provenance and (Suff) under two readings of the history': rows}


# ---- MC2: two programs selected on the world's order, differing at an order the world never gives -------------------
def mc2():
    bit = (0, 1)
    B = ['world', 'swapped']
    D = org('D_task(NOT of the number handed first)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_task'], {'c_task': ('x', 'y')},
            B, [ONE], lambda j, a, b: {(x, 1 - x) for x in bit})
    Cw = [(ONE, 'world'), (ONE, 'swapped')]
    p_wide = Question(D, Cw, 'world', PortQuery(), 'y', name='p_wide')
    # program 1 does NOT in both orders; program 2 does it in the world's order only (in the swapped order its output is
    # not NOT of its input: here, the input unchanged, a stand-in for "not NOT", which C3 records without saying what it is)
    def prog(which):
        def rel(j, a, b):
            if which == 2 and b == 'swapped':
                return {(x, x) for x in bit}
            return {(x, 1 - x) for x in bit}
        return org('E_%d' % which, ['x', 'y'], {'x': bit, 'y': bit}, ['e'], {'e': ('x', 'y')}, B, [ONE], rel)
    out = {}
    cands = {}
    for w in (1, 2):
        E = prog(w)
        c = Candidate(E, p_wide, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B}, {'e': (frozenset(['c_task']), ident(['x', 'y']))},
                      ['e'], 'y', name='program_%d' % w)
        cands[w] = c
        H = [(ONE, 'world')]
        h = Hist(['world', 'o_t'], [], set(Cw), admitted=True, prepares=False)
        out['program %d' % w] = {'faithful on the history (the world order)': faithful_on(c, H),
                                 'faithful on the wider contract (both orders)': faithful(c),
                                 'survives on the history and is selected (reading A)': sel(c, H, h)}
    E1, E2 = cands[1].E, cands[2].E
    v1 = E1.L('e', ONE, 'swapped')
    v2 = E2.L('e', ONE, 'swapped')
    out['values differ at the unseen order (D12.9 underdetermination of program 1 by the history)'] = v1 != v2
    out['values agree at the world order'] = E1.L('e', ONE, 'world') == E2.L('e', ONE, 'world')
    return out


# ---- MC3: a program that does the task in two places ----------------------------------------------------------------
def mc3():
    bit = (0, 1)
    B = ['u0', 'u1']
    uval = {'u0': 0, 'u1': 1}
    D = org('D_task(NOT)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_x', 'c_task'], {'c_x': ('x',), 'c_task': ('x', 'y')},
            B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'c_x' else {(x, 1 - x) for x in bit})
    p = Question(D, [(ONE, 'u0'), (ONE, 'u1')], 'u0', PortQuery(), 'y', name='p_task')
    foot = {'e_x': ('x',), 'place1': ('x', 'y'), 'place2': ('x', 'y')}
    E = org('E_two_places', ['x', 'y'], {'x': bit, 'y': bit}, list(foot), foot, B, [ONE],
            lambda j, a, b: {(uval[b],)} if j == 'e_x' else {(x, 1 - x) for x in bit})
    lam = {k: (frozenset(['c_task']), ident(['x', 'y'])) for k in ('place1', 'place2')}
    c = Candidate(E, p, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B}, lam, ['place1', 'place2'], 'y', name='two_places')
    S = routes(c)
    G = frozenset(['place1', 'place2'])
    return {'(E) of the whole': account(c), 'routes': sorted(sorted(W) for W in S),
            'the pair is a critical block of the whole': critical_block(S, G, G),
            'place1 alone is a critical block of the whole': critical_block(S, frozenset(['place1']), G),
            'contributory': {d: contributory(S, d) for d in ('place1', 'place2')},
            'globally indispensable': {d: indispensable(S, ['place1', 'place2'], d) for d in ('place1', 'place2')}}


# ---- MC4: an extra read: Avida's ablation against the semantics' deletion -----------------------------------------------
def mc4():
    bit = (0, 1)
    B = ['A0B1', 'A1B0', 'A0B0', 'A1B1']          # the two numbers handed out, in the world's order: first A, then B
    val = {'A0B1': (0, 1), 'A1B0': (1, 0), 'A0B0': (0, 0), 'A1B1': (1, 1)}
    A = [ONE, 'ablate_read1']
    # fine grain: the read pointer is a port. read1 takes the number at the pointer and moves it on; read2 takes the next.
    ports = ['p1', 'r1', 'p2', 'r2', 'y']
    dom = {'p1': (0, 1), 'r1': bit, 'p2': (1, 2), 'r2': bit, 'y': bit}
    foot = {'read1': ('p1', 'r1'), 'read2': ('p1', 'p2', 'r2'), 'gate': ('r2', 'y')}
    def rel(j, a, b):
        A_, B_ = val[b]
        q = (A_, B_)
        if j == 'read1':
            return {(0, 0)} if a == 'ablate_read1' else {(1, A_)}      # nop-X: pointer not moved, register left at 0
        if j == 'read2':
            return {(pp, pp + 1, q[pp]) for pp in (0, 1)}
        return {(r, 1 - r) for r in bit}                            # nand(r2, r2): NOT of the second number read
    D = org('D_program(fine grain)', ports, dom, list(foot), foot, B, A, rel)
    C = [(a, b) for a in A for b in B]
    p = Question(D, C, 'A0B1', PortQuery(), 'y', name='p_out')
    ans = {(a, b): p.ans(a, b) for (a, b) in C}
    Dd = D.delete(['read1'])
    ans_del = {b: p.ans(ONE, b, Dd) for b in B}
    # coarse grain (the grain of S112's circuits): each read takes its own fixed number; no pointer port.
    foot2 = {'read1': ('r1',), 'read2': ('r2',), 'gate': ('r2', 'y')}
    def rel2(j, a, b):
        A_, B_ = val[b]
        if j == 'read1':
            return {(A_,)}
        if j == 'read2':
            return {(B_,)}
        return {(r, 1 - r) for r in bit}
    D2 = org('D_program(coarse grain)', ['r1', 'r2', 'y'], {'r1': bit, 'r2': bit, 'y': bit}, list(foot2), foot2, B, [ONE], rel2)
    p2 = Question(D2, [(ONE, b) for b in B], 'A0B1', PortQuery(), 'y', name='p_out_coarse')
    ans2 = {b: p2.ans(ONE, b) for b in B}
    ans2_del = {b: p2.ans(ONE, b, D2.delete(['read1'])) for b in B}
    show = lambda v: '⊥ (undetermined)' if v is BOT else v
    return {'fine grain: answer with nothing changed': {b: show(ans[(ONE, b)]) for b in B},
            'fine grain: answer after Avida ablation of read1 (an admitted edit)': {b: show(ans[('ablate_read1', b)]) for b in B},
            'fine grain: answer after the semantics deletion of read1': {b: show(v) for b, v in ans_del.items()},
            'coarse grain: answer with nothing changed': {b: show(v) for b, v in ans2.items()},
            'coarse grain: answer after the semantics deletion of read1': {b: show(v) for b, v in ans2_del.items()}}


if __name__ == '__main__':
    for name, fn in (('MC1', mc1), ('MC2', mc2), ('MC3', mc3), ('MC4', mc4)):
        OUT[name] = fn()
    OUT['model source copied from'] = SRC
    json.dump(OUT, open(SC + '/model_cases.json', 'w'), indent=1, default=str, ensure_ascii=False)
    print(json.dumps(OUT, indent=1, default=str, ensure_ascii=False))
