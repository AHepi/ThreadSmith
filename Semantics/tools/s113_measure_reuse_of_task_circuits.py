#!/usr/bin/env python3
"""s113_measure_reuse_of_task_circuits.py

What it does, in plain words: for log S113 (measure M6 of the plan), asks whether the instructions an Avida program
needs for a task that appeared later in its run are also needed for a task that appeared earlier, more often than
chance would give. For each run it takes the most common distinct instruction sequence alive at update 50,000 and runs
it alone in Avida's test processor (Avida's analysis mode, no instruction changes, the 77 logic tasks listed at value
0, the do-nothing instruction nop-X added as a 27th instruction, as in S111 and S112). Then it runs every copy of it
with one instruction ablated (replaced by nop-X). An instruction is **required for replication** if its ablation stops
the program making an exact copy of itself; it is **required for a task** if its ablation stops that task while the
program still replicates (S112's definition). For every pair of tasks the program performs, where one task first
appeared in the run (performed by any program) before the other, it takes the share of the later task's required
instructions that are also required for the earlier task, and compares it with the share expected if the later task's
required instructions were placed at random among the program's instructions not required for replication (the
earlier task's count divided by that number). More than expected is read as the later task's circuit reusing parts
of the earlier task's.

Raw output stays in the scratch space (s113/reuse/); the summary is written to s113/reuse/reuse_summary.json, which
tools/s113_count_new_capabilities_over_time.py adds to the results. Every Avida process runs under a timeout; Avida's
programs copy themselves only inside Avida's simulated processor.
Written 30 September 2026 by the one Opus 5.5 agent of log S113.
"""
import json, os, shutil, statistics, subprocess, sys, tempfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R      # noqa: E402  (paths, task list, environment text)
import s113_count_new_capabilities_over_time as C           # noqa: E402  (reading the runs)

WORK = R.SCRATCH + '/s113/reuse'
NULL = 'A'


def evaluate(seqs, tasks, timeout=1800):
    os.makedirs(WORK, exist_ok=True)
    d = tempfile.mkdtemp(prefix='a_', dir=WORK)
    for f in ['avida.cfg', 'instset-heads.cfg']:
        shutil.copy(os.path.join(R.S111CONF, f), d)
    with open(os.path.join(d, 'instset-heads.cfg'), 'a') as f:
        f.write('\nINST nop-X         # A (log S113 analysis only: an ablation that does nothing and is no label)\n')
    with open(os.path.join(d, 'environment.cfg'), 'w') as f:
        f.write(R.environment_text('no_rewards', R.load_ranks()))
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write('u begin Exit\n')
    fields = ['viable'] + ['task.%d' % i for i in range(len(tasks))] + ['sequence']
    with open(os.path.join(d, 'analyze.cfg'), 'w') as f:
        f.write('\n'.join(['LOAD_SEQUENCE ' + s for s in seqs] + ['RECALCULATE', 'DETAIL out.dat ' + ' '.join(fields)])
                + '\n')
    argv = ['timeout', str(timeout), 'nice', '-n', '10', R.AVIDA, '-a', '-s', '1', '-set', 'VERBOSITY', '0']
    rc = subprocess.run(argv, cwd=d, stdout=open(os.path.join(d, 'analyze.log'), 'w'), stderr=subprocess.STDOUT,
                        stdin=subprocess.DEVNULL).returncode
    if rc != 0:
        raise RuntimeError('Avida analysis mode exited %d in %s' % (rc, d))
    rows = []
    for line in open(os.path.join(d, 'data', 'out.dat')):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        rows.append({'viable': int(w[0]), 'tasks': [int(float(x)) > 0 for x in w[1:-1]], 'sequence': w[-1]})
    if len(rows) != len(seqs) or any(r['sequence'] != s for r, s in zip(rows, seqs)):
        raise RuntimeError('rows out of order in ' + d)
    shutil.rmtree(d)
    return rows


def most_common_at_end(run_dir):
    sp = os.path.join(run_dir, 'piece_49', 'data', 'detail-1000.spop')
    best = None
    for line in open(sp):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        n, seq = int(w[4]), w[16]
        if best is None or n > best[0]:
            best = (n, seq)
    return best


def one_run(key, tasks):
    run_dir = os.path.join(R.OUT, key)
    n, seq = most_common_at_end(run_dir)
    env, seed = key.rsplit('_seed', 1)
    _, samples = C.read_run(env, int(seed), tasks)
    first_any = C.measure(samples, tasks, {})['first_any']
    base = evaluate([seq], tasks)[0]
    abl = evaluate([seq[:i] + NULL + seq[i + 1:] for i in range(len(seq))], tasks)
    repl = [i for i, r in enumerate(abl) if not r['viable']]
    performed = [tasks[j] for j in range(len(tasks)) if base['tasks'][j]]
    req = {}
    for j, t in enumerate(tasks):
        if base['tasks'][j]:
            req[t] = [i for i, r in enumerate(abl) if r['viable'] and not r['tasks'][j]]
    free = len(seq) - len(repl)
    pairs = []
    for a in performed:
        for b in performed:
            fa, fb = first_any.get(a), first_any.get(b)
            if fa is None or fb is None or not fa < fb or not req[b] or free <= 0:
                continue
            shared = len(set(req[a]) & set(req[b])) / len(req[b])
            expected = len(req[a]) / free
            pairs.append((a, b, shared, expected))
    return {'run': key, 'programs_with_this_sequence': n, 'length': len(seq), 'replicates': bool(base['viable']),
            'required_for_replication': len(repl), 'tasks_performed': len(performed),
            'required_per_task': {t: len(v) for t, v in req.items()},
            'pairs': len(pairs),
            'mean_shared': round(statistics.mean(p[2] for p in pairs), 4) if pairs else None,
            'mean_expected': round(statistics.mean(p[3] for p in pairs), 4) if pairs else None,
            'pairs_above_expected': sum(1 for p in pairs if p[2] > p[3]),
            'pairs_below_expected': sum(1 for p in pairs if p[2] < p[3]),
            'pairs_sharing_nothing': sum(1 for p in pairs if p[2] == 0)}


def main():
    ranks = json.load(open(R.RANKS))['tasks']
    tasks = [r['task'] for r in ranks]
    out = {'what': 'log S113 measure M6: reuse of task circuits in the most common distinct instruction sequence of '
                   'each run at update 50,000 (tools/s113_measure_reuse_of_task_circuits.py)', 'runs': []}
    for env in R.ENVIRONMENTS:
        for s in R.SEEDS:
            key = '%s_seed%d' % (env, s)
            if os.path.exists(os.path.join(R.OUT, key, 'piece_49', 'data', 'detail-1000.spop')):
                rec = one_run(key, tasks)
                out['runs'].append(rec)
                print(json.dumps({k: v for k, v in rec.items() if k != 'required_per_task'}), flush=True)
    by_env = {}
    for env in R.ENVIRONMENTS:
        rs = [r for r in out['runs'] if r['run'].startswith(env + '_seed') and r['pairs']]
        if rs:
            by_env[env] = {'runs_with_pairs': len(rs), 'pairs': sum(r['pairs'] for r in rs),
                           'pairs_above_expected': sum(r['pairs_above_expected'] for r in rs),
                           'pairs_below_expected': sum(r['pairs_below_expected'] for r in rs),
                           'mean_shared_per_run': [r['mean_shared'] for r in rs],
                           'mean_expected_per_run': [r['mean_expected'] for r in rs]}
    out['by environment'] = by_env
    allp = sum(r['pairs'] for r in out['runs'])
    out['all runs'] = {'pairs': allp, 'pairs_above_expected': sum(r['pairs_above_expected'] for r in out['runs']),
                       'pairs_below_expected': sum(r['pairs_below_expected'] for r in out['runs']),
                       'runs where the mean shared exceeds the mean expected':
                           sum(1 for r in out['runs'] if r['pairs'] and r['mean_shared'] > r['mean_expected']),
                       'runs with pairs': sum(1 for r in out['runs'] if r['pairs'])}
    json.dump(out, open(os.path.join(WORK, 'reuse_summary.json'), 'w'), indent=1)
    print(json.dumps(out['all runs']))


if __name__ == '__main__':
    main()
