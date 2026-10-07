#!/usr/bin/env python3
"""s113_measure_capabilities_in_the_saved_program_populations.py

What it does, in plain words: a second way of counting, for log S113, the computational capabilities (the 77 logic
tasks) present in each program population, written after the runs because the first way (Avida's own count in the world,
tasks.dat) turned out to count too few programs in some environments. Avida's world count credits a program with a task
only if the program's last completed copy (or its parent's) included it; each piece of a run starts by loading the saved
program population, and a loaded program has an empty record until it completes a copy of its own. Where processor
time is spread very unevenly (programs whose Avida fitness is thousands of times lower get almost no processor time),
many programs complete no copy within a 1,000-update piece and are counted as performing nothing.

This script instead takes the program population saved every 5,000 updates in each run, runs every distinct instruction
sequence alone in Avida's test processor (Avida's analysis mode, no instruction changes, the 77 tasks listed at value 0,
the same test processor as S111 and S112), and counts, for each task, how many Avida programs carry an instruction
sequence that performs it there. A task counts as present if at least one program's sequence performs it, and common if
the sequences of at least 10% of the programs do (the plan's share). It counts both "performs it" and "performs it and
replicates" (Avida's viable: makes an exact copy of itself). The counts at the ten saved updates give the counts over
time, the first saved update at which each task is present and common, keeping, and the last new high, as in
tools/s113_count_new_capabilities_over_time.py, but at 5,000-update steps.

Raw output stays in the scratch space (s113/test_processor/); the summary goes to
s113/test_processor/summary.json, which tools/s113_count_new_capabilities_over_time.py adds to the results. Every Avida
process runs under a timeout; Avida's programs copy themselves only inside Avida's simulated processor.
Written 30 September 2026 by the one Opus 5.5 agent of log S113, after the runs, as a departure from the plan
(recorded in the results and the exact commands).
"""
import json, os, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R      # noqa: E402  (paths, task list, environment text)

WORK = R.SCRATCH + '/s113/test_processor'
CHUNK = 3000
COMMON = 0.10
MARKS = list(range(5000, 50001, 5000))


def evaluate(seqs, ntasks, timeout=3600):
    os.makedirs(WORK, exist_ok=True)
    d = tempfile.mkdtemp(prefix='a_', dir=WORK)
    for f in ['avida.cfg', 'instset-heads.cfg']:
        shutil.copy(os.path.join(R.S111CONF, f), d)
    with open(os.path.join(d, 'environment.cfg'), 'w') as f:
        f.write(R.environment_text('no_rewards', R.load_ranks()))
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write('u begin Exit\n')
    fields = ['viable'] + ['task.%d' % i for i in range(ntasks)] + ['sequence']
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
        rows.append((int(w[0]), [int(float(x)) > 0 for x in w[1:-1]], w[-1]))
    if len(rows) != len(seqs) or any(r[2] != s for r, s in zip(rows, seqs)):
        raise RuntimeError('rows out of order in ' + d)
    shutil.rmtree(d)
    return rows


def read_spop(path):
    out = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        n = int(w[4])
        if n > 0:
            out.append((w[16], n))
    return out


def one_snapshot(args):
    key, mark, tasks = args
    piece = mark // 1000 - 1
    sp = os.path.join(R.OUT, key, 'piece_%02d' % piece, 'data', 'detail-1000.spop')
    pop = read_spop(sp)
    seqs = [s for s, _ in pop]
    rows = []
    for i in range(0, len(seqs), CHUNK):
        rows += evaluate(seqs[i:i + CHUNK], len(tasks))
    total = sum(n for _, n in pop)
    perf = [0] * len(tasks)
    perf_viable = [0] * len(tasks)
    viable_programs = 0
    for (s, n), (v, t, _) in zip(pop, rows):
        viable_programs += n if v else 0
        for j in range(len(tasks)):
            if t[j]:
                perf[j] += n
                if v:
                    perf_viable[j] += n
    return key, mark, {'programs': total, 'distinct_sequences': len(pop), 'programs_replicating': viable_programs,
                       'performing': perf, 'performing_and_replicating': perf_viable}


def summarise(snaps, tasks):
    """snaps: {mark: snapshot} for one run."""
    out = {}
    for kind in ['performing', 'performing_and_replicating']:
        anyc, com, first_any, first_common, ever = {}, {}, {}, {}, set()
        for m in MARKS:
            s = snaps[m]
            present = [s[kind][j] > 0 for j in range(len(tasks))]
            common = [s[kind][j] / s['programs'] >= COMMON for j in range(len(tasks))]
            anyc[str(m)] = sum(present)
            com[str(m)] = sum(common)
            for j, t in enumerate(tasks):
                if present[j] and t not in first_any:
                    first_any[t] = m
                if common[j] and t not in first_common:
                    first_common[t] = m
                if common[j]:
                    ever.add(t)
        end = snaps[MARKS[-1]]
        end_common = {t for j, t in enumerate(tasks) if end[kind][j] / end['programs'] >= COMMON}
        end_present = {t for j, t in enumerate(tasks) if end[kind][j] > 0}
        high, last_high = -1, None
        for m in MARKS:
            if com[str(m)] > high:
                high, last_high = com[str(m)], m
        two = set(R.TWO)
        out[kind] = {'any_at_marks': anyc, 'common_at_marks': com,
                     'any_at_end': anyc[str(MARKS[-1])], 'common_at_end': com[str(MARKS[-1])],
                     'common_two_input_at_end': len(end_common & two),
                     'common_three_input_at_end': len(end_common - two),
                     'any_two_input_at_end': len(end_present & two), 'any_three_input_at_end': len(end_present - two),
                     'ever_common': len(ever), 'kept_common_at_end': len(ever & end_common),
                     'ever_common_performed_by_none_at_end': len(ever - end_present),
                     'last_new_high_of_common': last_high, 'levelled_off': last_high <= 40000,
                     'rise_of_common_over_last_10000': com[str(MARKS[-1])] - com[str(MARKS[-3])],
                     'first_any': first_any, 'first_common': first_common,
                     'share_at_end': {t: round(end[kind][j] / end['programs'], 4) for j, t in enumerate(tasks)
                                      if end[kind][j]}}
    out['programs_at_marks'] = {str(m): snaps[m]['programs'] for m in MARKS}
    out['replicating_share_at_marks'] = {str(m): round(snaps[m]['programs_replicating'] / snaps[m]['programs'], 4)
                                         for m in MARKS}
    out['distinct_sequences_at_marks'] = {str(m): snaps[m]['distinct_sequences'] for m in MARKS}
    return out


def main():
    tasks = [t for t, _ in R.load_ranks()]
    keys = ['%s_seed%d' % (e, s) for e in R.ENVIRONMENTS for s in R.SEEDS]
    jobs = [(k, m, tasks) for k in keys for m in MARKS]
    raw = {}
    with ThreadPoolExecutor(max_workers=3) as pool:
        for key, mark, snap in pool.map(one_snapshot, jobs):
            raw.setdefault(key, {})[mark] = snap
            print(key, mark, snap['programs'], snap['distinct_sequences'], flush=True)
    json.dump({k: {str(m): v for m, v in d.items()} for k, d in raw.items()},
              open(os.path.join(WORK, 'raw_counts.json'), 'w'))
    summary = {'what': 'log S113: capabilities counted in Avida\'s test processor over the program populations saved '
                       'every 5,000 updates (tools/s113_measure_capabilities_in_the_saved_program_populations.py)',
               'tasks': tasks, 'per run': {k: summarise(raw[k], tasks) for k in keys}}
    json.dump(summary, open(os.path.join(WORK, 'summary.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
