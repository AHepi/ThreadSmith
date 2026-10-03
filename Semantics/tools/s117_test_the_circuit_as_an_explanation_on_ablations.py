#!/usr/bin/env python3
"""s117_test_the_circuit_as_an_explanation_on_ablations.py

What it does, in plain words: for log S117 (computation C1 of the plan). S112 described what each evolved Avida program's
logic task "is" by a circuit: the routes, read from Avida's own step-by-step trace, along which the numbers handed in
reach the number handed out. Read as an explanatory candidate in the semantics' sense (Part V), for the question
"does this program still do this task after this one instruction is ablated?", the circuit answers "it stops" exactly
when the ablated instruction lies on every route of the task, and "it still does it" otherwise. The semantics' condition
(A) asks that the candidate's answer equal the program's at every pair of the contract. This script reads S112's raw
output only (single ablations: s112/removals/*.singles.jsonl; traces: s112/traces/*.jsonl; nothing is run, nothing in
those folders is written) and, for every program and task, at every single ablation that leaves the copying working
(the contract's stated scope), compares the circuit's answer with Avida's. Output: scratch space s117/circuit_A.json.

  python3 -B Semantics/tools/s117_test_the_circuit_as_an_explanation_on_ablations.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import json, os
from collections import defaultdict

SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
TASKS = ['NOT', 'NAND', 'AND', 'ORN', 'OR', 'ANDN', 'NOR', 'XOR', 'EQU']
RUNS = ['main_%s_seed%d' % (r, s) for r in ('low', 'default', 'high') for s in (1, 2, 3)]
OUT = SC + '/s117/circuit_A.json'


def sums_in(c):
    return {TASKS[k] for k in range(9) if (c >> 1) & (1 << k)}


def main():
    agg = defaultdict(lambda: defaultdict(int))
    examples = {}
    for run in RUNS:
        singles = {}
        for line in open(SC + '/s112/removals/%s.singles.jsonl' % run):
            r = json.loads(line)
            if (r['base'] & 1) and (r['base'] >> 1):
                singles[r['seq']] = r
        with open(SC + '/s112/traces/%s.jsonl' % run) as fh:
            for line in fh:
                tr = json.loads(line)
                r = singles.get(tr['seq'])
                if r is None:
                    continue
                n = r['organisms']
                V = [i for i, c in enumerate(r['sites']) if c & 1]
                for t in sorted(sums_in(r['base'])):
                    e = tr.get('sums', {}).get(t)
                    routes = [set(int(i) for i in ro['sites']) for ro in (e or {}).get('routes', [])]
                    a = agg[t]
                    if not routes:
                        a['pairs without a route in the trace'] += 1
                        continue
                    every = set.intersection(*routes)
                    req = {i for i in V if t not in sums_in(r['sites'][i])}
                    pred = every & set(V)
                    off = req - pred      # required, but the circuit says the task goes on
                    unreq = pred - req    # on every route, but the task goes on
                    a['program-task pairs'] += 1
                    a['programs'] += n
                    a['ablation pairs checked'] += len(V)
                    a['ablation pairs where (A) fails'] += len(off) + len(unreq)
                    a['required but not on every route'] += len(off)
                    a['on every route but not required'] += len(unreq)
                    if not off and not unreq:
                        a['program-task pairs where (A) holds at every ablation'] += 1
                        a['programs where (A) holds at every ablation'] += n
                    elif off and not unreq:
                        a['fails only by required-off-circuit'] += 1
                    elif unreq and not off:
                        a['fails only by on-circuit-not-required'] += 1
                    else:
                        a['fails both ways'] += 1
                    if t in ('NOT', 'EQU') and (off or unreq) and (t not in examples or n > examples[t]['organisms']):
                        examples[t] = {'run': run, 'seq': tr['seq'], 'organisms': n, 'length': len(tr['seq']),
                                       'required_not_on_every_route': sorted(off), 'on_every_route_not_required': sorted(unreq),
                                       'routes': len(routes)}
    total = defaultdict(int)
    for t in agg:
        for k, v in agg[t].items():
            total[k] += v
    res = {'by task': {t: agg[t] for t in TASKS if t in agg}, 'all tasks': total, 'largest failing examples': examples}
    for t in list(res['by task']) + ['all tasks']:
        a = res['by task'].get(t, total) if t != 'all tasks' else total
        a['share of program-task pairs where (A) holds'] = round(a.get('program-task pairs where (A) holds at every ablation', 0) / a['program-task pairs'], 4)
        a['share weighted by programs'] = round(a.get('programs where (A) holds at every ablation', 0) / a['programs'], 4)
        a['share of ablation pairs where (A) fails'] = round(a['ablation pairs where (A) fails'] / a['ablation pairs checked'], 4)
    json.dump(res, open(OUT, 'w'), indent=1)
    for t in TASKS + ['all tasks']:
        a = res['by task'].get(t) if t != 'all tasks' else res['all tasks']
        print(t, {k: a[k] for k in ('program-task pairs', 'share of program-task pairs where (A) holds', 'share weighted by programs',
                                    'share of ablation pairs where (A) fails', 'required but not on every route', 'on every route but not required')})
    print(json.dumps(examples, indent=0)[:1500])


if __name__ == '__main__':
    main()
