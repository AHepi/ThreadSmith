#!/usr/bin/env python3
"""s129_feed_avida_cases_to_the_copy_under_reading_c.py

What it does, in plain words: for log S129 (decisions S83 and S84). A copy of S117's
tools/s117_feed_avida_cases_to_a_copy_of_the_model.py, pointed at the S129 copy of the model program (results/S129
Reading C carried into copies/model after Reading C/, which carries Reading C and the graded survival condition), and
run under the four settings of the copy's two switches. It feeds the copy the same four Avida cases S117 built (MC1 to
MC4, one bit per number, exact for Avida's bitwise logic tasks), and adds what the two decisions need:
  MC1  the most common NOT program of run low seed 2 (S112: it hands back nand(x, x)), as one block and cut into its
       instructions; its provenance and (Suff) under S117's readings A and B (no boundary declared, as S117 had them)
       and under Reading C at two declared boundaries: the S72 boundary (the whole Avida execution environment, from
       the start of a run; the task-checking code inside it, its correspondence a record of its writers', who are
       outside) and a wide boundary that also takes in the people who wrote Avida; in a run where doing NOT raised a
       program's rate of copying (graded pay: fidelity on H changed which programs were copied);
  MC1b the same program in the run that paid for nothing (S117 B4: 3,600 programs at update 50,000, 11 doing NOT),
       where doing NOT changed nothing about which programs were copied;
  MC2  two programs selected on the world's order, differing at an order the world never gives (Argument 3), at the
       S72 boundary with a graded advantage;
  MC3, MC4  as S117 (no provenance; recomputed on the copy to check they are unchanged).
The program in the repository is imported from its committed place and never written. Output: printed, and
results/S129 Reading C carried into copies/map feeding under Reading C.json (and a scratch copy, s129/model_cases_under_C.json).

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129 (from S117's script of 1 October 2026).
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s129'
OUTF = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'map feeding under Reading C.json')
sys.path.insert(0, COPY)

from model import claims_b as cb  # noqa: E402
from model.core import ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, routes  # noqa: E402
from model.core import critical_block, contributory, indispensable, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on  # noqa: E402
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok, SUFF_READINGS  # noqa: E402
from model.args import Assessor, Imp, Not  # noqa: E402

SETTINGS = [('C off, graded off', False, False), ('C on, graded off', True, False),
            ('C off, graded on', False, True), ('C on, graded on', True, True)]


def org(name, ports, dom, comps, foot, B, A, rel):
    return Org(name, ports, dom, comps, foot, B, A, lambda a2, a1: None, rel)


def ident(ports):
    return {v: Translation((v,)) for v in ports}


# ---- the NOT program, as S117 built it ---------------------------------------------------------------------------
def not_program():
    bit = (0, 1)
    B = ['u0', 'u1']
    uval = {'u0': 0, 'u1': 1}
    D = org('D_task(NOT)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_x', 'c_task'], {'c_x': ('x',), 'c_task': ('x', 'y')},
            B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'c_x' else {(x, 1 - x) for x in bit})
    C = [(ONE, 'u0'), (ONE, 'u1')]
    p = Question(D, C, 'u0', PortQuery(), 'y', name='p_task')
    nand = lambda u, v: 1 - (u & v)
    E1 = org('E_program(one block)', ['x', 'y'], {'x': bit, 'y': bit}, ['e_x', 'e_prog'], {'e_x': ('x',), 'e_prog': ('x', 'y')},
             B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'e_x' else {(x, nand(x, x)) for x in bit})
    c1 = Candidate(E1, p, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B},
                   {'e_prog': (frozenset(['c_task']), ident(['x', 'y']))}, ['e_prog'], 'y', name='program')
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
    return p, C, c1, c2


AUTHORS, CODE, WORLD, SELECTION = "Avida's authors write the task check", 'Avida task-check code', 'world runs the lineage', 'selection by replication'


def histories(occ_pairs, advantage):
    """The histories of the NOT program's holding: S117's A and B (no boundary declared), and Reading C at two boundaries.
    Θ by hand (I90): which occurrences represent what, which holding is a record of which, and the rate fact."""
    A = Hist([WORLD, SELECTION, 'o_t'], [], occ_pairs, admitted=True, prepares=False, advantage=advantage)
    B = Hist([CODE, WORLD, SELECTION, 'o_t'], [(CODE, 'surv'), (CODE, 'cod')], occ_pairs, admitted=True, prepares=False,
             advantage=advantage)
    occ5 = [AUTHORS, CODE, WORLD, SELECTION, 'o_t']
    tags = [(AUTHORS, 'surv'), (AUTHORS, 'cod'), (CODE, 'surv'), (CODE, 'cod')]
    C72 = Hist(occ5, tags, occ_pairs, admitted=True, prepares=False, beta=[CODE, WORLD, SELECTION, 'o_t'],
               source={CODE: AUTHORS}, advantage=advantage)
    Cwide = Hist(occ5, tags, occ_pairs, admitted=True, prepares=False, beta=occ5, source={CODE: AUTHORS}, advantage=advantage)
    return [("A (S117): the task-check code represents nothing in the history; no boundary declared", A),
            ("B (S117): the task-check code is an earlier occurrence that represents the survival condition and the task; no boundary declared", B),
            ("C at the S72 boundary: the whole execution environment from the start of the run, the task-check code inside it, its writers outside", C72),
            ("C at a wide boundary: the execution environment and the people who wrote Avida", Cwide)]


def provenance_rows(c1, acc1, H, advantage):
    rows = {}
    for nm, h in histories(set(H), advantage):
        s, k = sel(c1, H, h), con(h)
        dec = (not s) and (not k)
        j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c1.name))])
        out, _ = expl_ruled_out(j, c1.name)
        code_reps = any(o == CODE for o, _ in cb.rep_at_beta(h))
        rows[nm] = {'Sel': s, 'Con': k, 'Dec': dec,
                    'the task-check code represents (survival condition, task) at this boundary': code_reps if CODE in h.occ else None,
                    'the task-check code entered the boundary whole': cb.entered_whole(h, CODE) if CODE in h.occ else None,
                    'Rep: the program stands for NOT (faithful on the task and Sel or Con)': bool(faithful(c1)) and (s or k),
                    'argument not using (E) rules out Expl': out,
                    '(Suff) defeated, by reading': {r: suff_defeats(acc1, dec, out, r) for r in SUFF_READINGS},
                    'owner S41 condition Acc and Dec => not Expl, with Expl false': expl_ok(acc1, dec, False)}
    return rows


def mc1(advantage):
    p, C, c1, c2 = not_program()
    acc1, d1 = account(c1, detail=True)
    acc2, d2 = account(c2, detail=True)
    H = [(ONE, 'u0'), (ONE, 'u1')]
    return {'(E) of the program as one block': acc1, 'conditions (one block)': {k: bool(v) for k, v in d1.items()},
            '(E) of the program cut into its instructions': acc2, 'conditions (instructions)': {k: bool(v) for k, v in d2.items()},
            'rate fact (Θ by hand)': advantage,
            'provenance and (Suff)': provenance_rows(c1, acc1, H, advantage)}


def mc2():
    bit = (0, 1)
    B = ['world', 'swapped']
    D = org('D_task(NOT of the number handed first)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_task'], {'c_task': ('x', 'y')},
            B, [ONE], lambda j, a, b: {(x, 1 - x) for x in bit})
    Cw = [(ONE, 'world'), (ONE, 'swapped')]
    p_wide = Question(D, Cw, 'world', PortQuery(), 'y', name='p_wide')

    def prog(which):
        def rel(j, a, b):
            if which == 2 and b == 'swapped':
                return {(x, x) for x in bit}
            return {(x, 1 - x) for x in bit}
        return org('E_%d' % which, ['x', 'y'], {'x': bit, 'y': bit}, ['e'], {'e': ('x', 'y')}, B, [ONE], rel)
    out, cands = {}, {}
    for w in (1, 2):
        c = Candidate(prog(w), p_wide, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B}, {'e': (frozenset(['c_task']), ident(['x', 'y']))},
                      ['e'], 'y', name='program_%d' % w)
        cands[w] = c
        H = [(ONE, 'world')]
        h = Hist([CODE, 'world', 'o_t'], [(CODE, 'surv'), (CODE, 'cod')], set(Cw), admitted=True, prepares=False,
                 beta=[CODE, 'world', 'o_t'], source={CODE: AUTHORS}, advantage=True)
        out['program %d' % w] = {'faithful on the history (the world order)': faithful_on(c, H),
                                 'faithful on the wider contract (both orders)': faithful(c),
                                 'selected at the S72 boundary, graded advantage': sel(c, H, h)}
    E1, E2 = cands[1].E, cands[2].E
    out['values differ at the unseen order (D12.9 underdetermination of program 1 by the history)'] = E1.L('e', ONE, 'swapped') != E2.L('e', ONE, 'swapped')
    out['values agree at the world order'] = E1.L('e', ONE, 'world') == E2.L('e', ONE, 'world')
    return out


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


def mc4():
    bit = (0, 1)
    B = ['A0B1', 'A1B0', 'A0B0', 'A1B1']
    val = {'A0B1': (0, 1), 'A1B0': (1, 0), 'A0B0': (0, 0), 'A1B1': (1, 1)}
    A = [ONE, 'ablate_read1']
    ports = ['p1', 'r1', 'p2', 'r2', 'y']
    dom = {'p1': (0, 1), 'r1': bit, 'p2': (1, 2), 'r2': bit, 'y': bit}
    foot = {'read1': ('p1', 'r1'), 'read2': ('p1', 'p2', 'r2'), 'gate': ('r2', 'y')}

    def rel(j, a, b):
        A_, B_ = val[b]
        q = (A_, B_)
        if j == 'read1':
            return {(0, 0)} if a == 'ablate_read1' else {(1, A_)}
        if j == 'read2':
            return {(pp, pp + 1, q[pp]) for pp in (0, 1)}
        return {(r, 1 - r) for r in bit}
    D = org('D_program(fine grain)', ports, dom, list(foot), foot, B, A, rel)
    C = [(a, b) for a in A for b in B]
    p = Question(D, C, 'A0B1', PortQuery(), 'y', name='p_out')
    ans = {(a, b): p.ans(a, b) for (a, b) in C}
    Dd = D.delete(['read1'])
    ans_del = {b: p.ans(ONE, b, Dd) for b in B}
    show = lambda v: '⊥ (undetermined)' if v is BOT else v
    return {'fine grain: answer with nothing changed': {b: show(ans[(ONE, b)]) for b in B},
            'fine grain: answer after Avida ablation of read1 (an admitted edit)': {b: show(ans[('ablate_read1', b)]) for b in B},
            'fine grain: answer after the semantics deletion of read1': {b: show(v) for b, v in ans_del.items()}}


def main():
    out = {'about': 'S129: S117\'s Avida cases fed to the S129 copy of the model (Reading C, S83; graded survival condition, S84), '
                    'under the four settings of its two switches. Θ by hand (I90): which occurrences represent what, which holding '
                    'is a record of which, and whether doing NOT changed a program\'s rate of copying. Built by '
                    'tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py.',
           'model copy': COPY, 'settings': {}}
    for lab, c_on, g_on in SETTINGS:
        cb.READING_C, cb.GRADED = c_on, g_on      # the functions read these at call time
        out['settings'][lab] = {
            'MC1 (graded-pay run: doing NOT raised the rate of copying)': mc1(True),
            'MC1b (the run that paid for nothing: doing NOT changed nothing)': mc1(False),
            'MC2': mc2(), 'MC3': mc3(), 'MC4': mc4()}
    json.dump(out, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    os.makedirs(SC, exist_ok=True)
    json.dump(out, open(os.path.join(SC, 'model_cases_under_C.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    for lab, v in out['settings'].items():
        print('==', lab)
        for case in ('MC1 (graded-pay run: doing NOT raised the rate of copying)', 'MC1b (the run that paid for nothing: doing NOT changed nothing)'):
            print('  ', case.split(' (')[0], '(E) one block', v[case]['(E) of the program as one block'], '| cut', v[case]['(E) of the program cut into its instructions'])
            for nm, r in v[case]['provenance and (Suff)'].items():
                print('     %-60s Sel %-5s Con %-5s Dec %-5s Rep %-5s code represents %-5s (Suff) defeated (L536) %s' % (
                    nm[:60], r['Sel'], r['Con'], r['Dec'], r['Rep: the program stands for NOT (faithful on the task and Sel or Con)'],
                    r['the task-check code represents (survival condition, task) at this boundary'], r['(Suff) defeated, by reading']['L536']))
        print('   MC2', {k: v2 for k, v2 in v['MC2'].items()})


if __name__ == '__main__':
    main()
