#!/usr/bin/env python3
"""s117_find_programs_alike_in_behaviour_that_a_finer_change_separates.py

What it does, in plain words: for log S117 (computation C2 of the plan). The semantics says that what a part is ("its
kind") is fixed by how it responds to the changes a question admits, so that a coarser set of changes lumps together
parts that a finer set separates (formal claim FC04), and that two systems with the same outputs can be different
organizations (Argument 9, FC101). S112 ran every distinct instruction sequence alive at the end of its nine runs in
Avida's test CPU, unchanged and under changes to the environment (what nand means; other input numbers; the input
channel removed; the numbers reordered). This script reads that raw output only (s112/environment/*.jsonl; nothing is
run or written there): it groups the sequences whose observed computational behaviour is identical in the unchanged
test (same viability, same tasks), and counts, for each change, how many of these groups split, that is, hold two
sequences that behave differently once the change is made. Output: scratch space s117/alike_separated.json.

  python3 -B Semantics/tools/s117_find_programs_alike_in_behaviour_that_a_finer_change_separates.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import json
from collections import defaultdict

SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
RUNS = ['main_%s_seed%d' % (r, s) for r in ('low', 'default', 'high') for s in (1, 2, 3)]
CHANGES = ['nand read as nor', 'nand read as and', 'IO read as nop-X', 'random 32-bit inputs', 'fixed inputs reordered',
           'world-style inputs 1']


def prof(v):
    return (v['viable'], tuple(sorted(v['sums'])))


def main():
    groups = defaultdict(list)
    for run in RUNS:
        for line in open(SC + '/s112/environment/%s.jsonl' % run):
            r = json.loads(line)
            groups[prof(r['variants']['unchanged'])].append(r)
    res = {'sequences': sum(len(g) for g in groups.values()), 'groups alike when unchanged': len(groups),
           'groups with two or more sequences': sum(len(g) > 1 for g in groups.values()), 'by change': {}}
    example = None
    for ch in CHANGES:
        split = split_progs = progs_in_multi = 0
        for key, g in groups.items():
            if len(g) < 2:
                continue
            progs_in_multi += sum(r['organisms'] for r in g)
            outs = defaultdict(int)
            for r in g:
                if ch in r['variants']:
                    outs[prof(r['variants'][ch])] += r['organisms']
            if len(outs) > 1:
                split += 1
                split_progs += sum(outs.values())
                if ch == 'nand read as nor' and key[0] == 1 and key[1] and (example is None or sum(outs.values()) > example['programs']):
                    example = {'alike when unchanged': {'viable': key[0], 'tasks': list(key[1])}, 'programs': sum(outs.values()),
                               'behaviour after the change, programs per behaviour': {str(k): v for k, v in sorted(outs.items(), key=lambda kv: -kv[1])[:4]}}
        res['by change'][ch] = {'groups that split': split, 'programs in groups that split': split_progs,
                                'programs in groups of two or more': progs_in_multi}
    res['largest example (nand read as nor)'] = example
    json.dump(res, open(SC + '/s117/alike_separated.json', 'w'), indent=1)
    print(json.dumps(res, indent=1)[:3000])


if __name__ == '__main__':
    main()
