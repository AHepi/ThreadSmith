#!/usr/bin/env python3
"""s113_rank_the_tasks_by_the_fewest_nand_steps_they_need.py

What it does, in plain words: Avida's task library has 77 logic tasks on the three input numbers an Avida program reads:
the nine two-input tasks of S111 (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU) and 68 three-input tasks (logic_3AA to
logic_3CP). Each task accepts a set of "logic ids" (the 8-bit table of what the output bit is for each combination of
three input bits), read here straight from Avida's source file cTaskLib.cc. The only logic instruction in Avida's default
instruction set is nand, so this script finds, for every task, the fewest nand steps a circuit needs to compute it from
the three inputs (each step is the nand of two numbers already available, which may be the same number twice; a
result may be used more than once). It does this by trying every circuit of 1 step, then 2, and so on, until every task
has been found or 9 steps are reached; a task not found by then is given 10 (a lower bound, marked). For the nine two-input tasks this gives 1,1,2,2,3,3,4,4,5, the reward values S111 used. Log S113 uses
the step count as each task's difficulty: its reward value in the graded environments and its place in the growing list.

It writes a JSON file (the path given as the first argument). It runs nothing in Avida.
Written 30 September 2026 by the one Opus 5.5 agent of log S113.
"""
import json, re, sys

SRC = ('/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/avida/avida-core/'
       'source/main/cTaskLib.cc')
A, B, C = 0b10101010, 0b11001100, 0b11110000   # logic id bits of the three inputs (cTaskLib.cc SetupTests)
TWO = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']
TWO_FN = {'not': 'Task_Not', 'nand': 'Task_Nand', 'and': 'Task_And', 'orn': 'Task_OrNot', 'or': 'Task_Or',
          'andn': 'Task_AndNot', 'nor': 'Task_Nor', 'xor': 'Task_Xor', 'equ': 'Task_Equ'}


def ids_by_function(text):
    out = {}
    for m in re.finditer(r'double cTaskLib::(Task_\w+)\(cTaskContext& ctx\) const\s*\{(.*?)\n\}', text, re.S):
        body = m.group(2)
        ids = [int(x) for x in re.findall(r'logic_id == (\d+)', body)]
        if ids:
            out[m.group(1)] = sorted(set(ids))
    return out


def fewest_steps(targets, max_steps=9, keep_limit=1500000):
    """Breadth-first over the sets of numbers a circuit has made; returns {truth table: fewest steps}.
    Once the circuits of one size number more than keep_limit, the remaining sizes are searched depth-first from them
    without being kept (to save memory); the answer is the same."""
    best = {A: 0, B: 0, C: 0}
    frontier = {frozenset((A, B, C))}
    need = set(targets) - set(best)
    step = 0
    while need and step < max_steps and len(frontier) <= keep_limit:
        step += 1
        nxt = set()
        for s in frontier:
            items = sorted(s)
            for i, x in enumerate(items):
                for y in items[i:]:
                    z = (~(x & y)) & 0xFF
                    if z in s:
                        continue
                    if z not in best:
                        best[z] = step
                    nxt.add(s | {z})
        frontier = nxt
        need -= set(best)
        print('steps', step, 'circuits kept', len(frontier), 'tables still to find', len(need), file=sys.stderr)
    extra = 0
    while need and step + extra < max_steps:
        extra += 1
        found = set()

        def grow(items, left):
            for i, x in enumerate(items):
                for y in items[i:]:
                    z = (~(x & y)) & 0xFF
                    if z in items:
                        continue
                    if left == 1:
                        if z in need:
                            found.add(z)
                    else:
                        grow(items + (z,), left - 1)
        for s in frontier:
            grow(tuple(sorted(s)), extra)
        for z in found:
            best[z] = step + extra
        need -= found
        print('steps', step + extra, '(not kept) tables still to find', len(need), file=sys.stderr)
    return best


def main():
    text = open(SRC).read()
    fns = ids_by_function(text)
    tasks = []
    for t in TWO:
        tasks.append((t, fns[TWO_FN[t]]))
    for m in re.finditer(r'name == "(logic_3\w\w)"\)\s*NewTask\(name, "([^"]*)", &cTaskLib::(\w+)\)', text):
        tasks.append((m.group(1), fns[m.group(3)]))
    assert len(tasks) == 77, len(tasks)
    allids = [i for _, ids in tasks for i in ids]
    assert len(allids) == len(set(allids)), 'a logic id is accepted by two tasks'
    best = fewest_steps(allids)
    rows = []
    for name, ids in tasks:
        steps = sorted({best.get(i, 10) for i in ids})
        assert len(steps) == 1, (name, steps)   # a task accepts one function under swaps of the inputs
        row = {'task': name, 'logic_ids': ids, 'fewest_nand_steps': steps[0]}
        if not any(i in best for i in ids):
            row['note'] = ('not found with 9 steps or fewer; the search stopped there (a 10-step search would take '
                           'days in this script), so 10 is a lower bound, used as its level')
        rows.append(row)
    out = {'what': 'the 77 logic tasks of Avida 2.14 with the fewest nand steps each needs (log S113)',
           'source': 'avida-core/source/main/cTaskLib.cc at commit 47f13dad',
           'logic ids not accepted by any task': sorted(set(range(256)) - set(allids)),
           'tasks': rows}
    json.dump(out, open(sys.argv[1], 'w'), indent=1)
    from collections import Counter
    print(sorted(Counter(r['fewest_nand_steps'] for r in rows).items()))
    print([(r['task'], r['fewest_nand_steps']) for r in rows[:9]])


if __name__ == '__main__':
    main()
