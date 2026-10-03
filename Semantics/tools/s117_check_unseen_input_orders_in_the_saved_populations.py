#!/usr/bin/env python3
"""s117_check_unseen_input_orders_in_the_saved_populations.py

What it does, in plain words: for log S117 (computation C3 of the plan), tests the semantics' Argument 3 on Avida.
Argument 3 says that a correspondence shaped by selection on the changes it met is left open, at a change it never met,
wherever its population holds another member that also passed on the changes it met and differs at the new one.
Avida's world always hands a program its three numbers in one order. So, for each of the 18 program populations that
S116 saved at update 50,000 (read only, never written), every distinct instruction sequence is run alone in Avida's
test CPU (analyze mode, stock Avida, commit 47f13dad) on the same three numbers in all six orders, and for each program
it is recorded whether it copies itself (viable) and does NOT. Then, per run and per order other than the world's, the
programs that do NOT in the world's order are split into those that also do it in that order and those that do not.
If both groups are non-empty, the population holds two members that pass on what the world gave and differ at a change
the world never gave: Argument 3's condition, exhibited on Avida's own data.
Every Avida process runs under nice -n 19 and a time limit; at most 3 at once. Output: the scratch space, s117/orders/.

  python3 -B Semantics/tools/s117_check_unseen_input_orders_in_the_saved_populations.py run      (runs Avida)
  python3 -B Semantics/tools/s117_check_unseen_input_orders_in_the_saved_populations.py summarise

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import itertools, json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SC + '/avida/cbuild/bin/avida'
OUT = SC + '/s117/orders'
KEYS = ['%s_seed%d' % (e, s) for e in ('fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large')
        for s in (1, 2, 3)]
WORLD = [0x0f13149f, 0x3308e53e, 0x556241eb]   # Avida's test-CPU numbers, in the order the world hands them out
ORDERS = list(itertools.permutations(range(3)))  # (0, 1, 2) is the world's order


def run_one(key):
    out = OUT + '/' + key
    rund = out + '/rundir'
    os.makedirs(rund, exist_ok=True)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(SC + '/s116/probe_rundir/' + f, rund)
    shutil.copy(SC + '/s116/probes/%s/logic_high/environment.cfg' % key, out + '/environment.cfg')
    shutil.copy(SC + '/s116/probes/%s/events.cfg' % key, out + '/events.cfg')
    lines = ['PURGE_BATCH', 'LOAD %s/s116/copies/%s/u50000.spop' % (SC, key), 'FILTER num_units > 0']
    for i, p in enumerate(ORDERS):
        v = [WORLD[k] for k in p]
        lines += ['RECALCULATE 0 -1 0 %d %d %d' % tuple(v),
                  'DETAIL o%d.dat id num_units viable ' % i + ' '.join('task.%d' % j for j in range(9))]
    open(out + '/analyze.cfg', 'w').write('\n'.join(lines) + '\n')
    t0 = time.time()
    rc = subprocess.run(['nice', '-n', '19', 'timeout', '1800', AVIDA, '-c', rund + '/avida.cfg', '-a',
                         '-set', 'ENVIRONMENT_FILE', out + '/environment.cfg', '-set', 'ANALYZE_FILE', out + '/analyze.cfg',
                         '-set', 'EVENT_FILE', out + '/events.cfg', '-set', 'DATA_DIR', out + '/data',
                         '-set', 'RANDOM_SEED', '20261001', '-set', 'VERBOSITY', '1', '-set', 'TASK_REFRACTORY_PERIOD', '0',
                         '-set', 'TEST_CPU_TIME_MOD', '20'], cwd=rund, stdout=open(out + '/run.log', 'w'),
                        stderr=subprocess.STDOUT).returncode
    return key, rc, round(time.time() - t0, 1)


def read(key, i):
    rows = {}
    for line in open(OUT + '/%s/data/o%d.dat' % (key, i)):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        rows[w[0]] = (int(w[1]), int(w[2]) > 0, [int(x) > 0 for x in w[3:12]])
    return rows


def summarise():
    res = {}
    for key in KEYS:
        per = [read(key, i) for i in range(len(ORDERS))]
        world = per[0]
        total = sum(n for (n, v, t) in world.values())
        not_world = {g for g, (n, v, t) in world.items() if v and t[0]}
        r = {'programs': total, 'sequences': len(world),
             'do_NOT_in_world_order': sum(world[g][0] for g in not_world), 'orders': {}}
        for i, p in enumerate(ORDERS[1:], 1):
            other = per[i]
            both = sum(world[g][0] for g in not_world if other[g][1] and other[g][2][0])
            only = sum(world[g][0] for g in not_world if not (other[g][1] and other[g][2][0]))
            r['orders'][str(p)] = {'world_and_this_order': both, 'world_order_only': only,
                                   'argument_3_condition_exhibited': both > 0 and only > 0}
        res[key] = r
    json.dump(res, open(OUT + '/summary.json', 'w'), indent=1)
    runs_exhibiting = [k for k, r in res.items() if any(o['argument_3_condition_exhibited'] for o in r['orders'].values())]
    for k, r in res.items():
        print('%-24s programs %5d NOT(world) %5d  ' % (k, r['programs'], r['do_NOT_in_world_order']) +
              '  '.join('%s:%d/%d' % (o.replace(' ', ''), v['world_and_this_order'], v['world_order_only']) for o, v in r['orders'].items()))
    print('runs where the condition is exhibited at some unseen order:', len(runs_exhibiting), 'of', len(res))


if __name__ == '__main__':
    if sys.argv[1] == 'run':
        os.makedirs(OUT, exist_ok=True)
        with ThreadPoolExecutor(max_workers=3) as ex:
            for key, rc, sec in ex.map(run_one, KEYS):
                print(key, 'exit', rc, 'seconds', sec, flush=True)
    else:
        summarise()
