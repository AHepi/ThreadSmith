#!/usr/bin/env python3
"""s118_gather_the_results.py

What it does, in plain words: reads the raw output of log S118's six pilot runs (tools/s118_run_the_two_pilots.py) and
the matching raw output of S113's runs, and writes every number the S118 results use into
"results/S118 An instinct without a named target - results.json". It measures, as the plan written before running
fixed them:

  M1  how many of the 77 logic tasks are present (performed by at least one Avida program) and common (by at least 10%
      of the program population) at updates 5,000, 10,000, 15,000 and 20,000: by Avida's own count in the world
      (tasks.dat against count.dat) and by the test processor (every distinct instruction sequence of the saved program
      population run alone in Avida's analysis mode, the 77 tasks listed at value 0, with S113's own function);
  M2  the share of programs whose instruction sequence performs at least one task, and how many distinct tasks a
      program performs (middle and largest, counting every program);
  M3  how hard the common tasks are (the fewest nand steps each needs, from S113's ranking file);
  M4  for the pilot in which a copy needs a performed task: program count, births and deaths every 250 updates around
      update 5,000, and whether the program population died out;
  M5  the same counts for S113's runs at the same updates (test processor; S113's summary for M1, and S113's saved
      program populations at 5,000 and 20,000 for M2 and M3), and a check that the pilot without pay matches S113's
      NO TASK REWARDS first piece exactly up to update 1,000.

Avida is run here only in analysis mode (the test processor), under nice and a timeout, never evolving anything.
Raw output and the test processor's working files stay in the scratch space. Written 1 October 2026 by the one Opus 5.5
agent of log S118.
"""
import json, os, statistics, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R113                         # noqa: E402
import s113_measure_capabilities_in_the_saved_program_populations as M113         # noqa: E402

SCRATCH = R113.SCRATCH
RUNS = SCRATCH + '/s118/runs'
S113RUNS = SCRATCH + '/s113/runs'
M113.WORK = SCRATCH + '/s118/test_processor'      # the test processor's working files for this job
OUTJSON = os.path.join(os.path.dirname(HERE), 'results', 'S118 An instinct without a named target - results.json')
MARKS = [5000, 10000, 15000, 20000]
SEEDS = [1, 2, 3]
PILOTS = ['any_function', 'must_solve']
COMMON = 0.10
COMPARE = ['fixed_large', 'common_pays_less', 'fixed_graded', 'growing', 'no_rewards']


def rows(path):
    out = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        out.append([float(x) for x in line.split()])
    return out


def ranks():
    return R113.load_ranks()      # [(task, fewest nand steps)] in S113's order, the order of the task columns


def avida_count(run_dir):
    """Avida's own count in the world at every printed update: {update: (programs, [performers per task])}."""
    t = {int(r[0]): r[1:] for r in rows(os.path.join(run_dir, 'data', 'tasks.dat'))}
    c = {int(r[0]): r for r in rows(os.path.join(run_dir, 'data', 'count.dat'))}
    return t, c


def per_snapshot(spop_path, tasks):
    pop = M113.read_spop(spop_path)
    seqs = [s for s, _ in pop]
    res = []
    for i in range(0, len(seqs), M113.CHUNK):
        res += M113.evaluate(seqs[i:i + M113.CHUNK], len(tasks))
    total = sum(n for _, n in pop)
    perf = [0] * len(tasks)
    distinct = []                # (number of distinct tasks, programs)
    any_task = 0
    replicating = 0
    for (s, n), (v, t, _) in zip(pop, res):
        k = sum(1 for x in t if x)
        distinct.append((k, n))
        if k:
            any_task += n
        if v:
            replicating += n
        for j in range(len(tasks)):
            if t[j]:
                perf[j] += n
    expanded = sorted(k for k, n in distinct for _ in range(n))
    common = [tasks[j][0] for j in range(len(tasks)) if total and perf[j] / total >= COMMON]
    present = [tasks[j][0] for j in range(len(tasks)) if perf[j] > 0]
    steps = dict(tasks)
    cs = [steps[t] for t in common]
    return {'programs': total, 'distinct_sequences': len(pop), 'replicating_share': round(replicating / total, 4) if total else None,
            'present': len(present), 'common': len(common), 'common_tasks': common,
            'share_performing_at_least_one_task': round(any_task / total, 4) if total else None,
            'distinct_tasks_per_program_middle': statistics.median(expanded) if expanded else None,
            'distinct_tasks_per_program_largest': max(expanded) if expanded else None,
            'fewest_nand_steps_of_common_tasks_largest': max(cs) if cs else None,
            'fewest_nand_steps_of_common_tasks_middle': statistics.median(cs) if cs else None,
            'share_per_task': {tasks[j][0]: round(perf[j] / total, 4) for j in range(len(tasks)) if perf[j]}}


def avida_marks(t, c, tasks):
    out = {}
    for m in MARKS:
        if m not in t or m not in c:
            out[str(m)] = None
            continue
        progs = c[m][2]
        perf = t[m]
        out[str(m)] = {'programs': int(progs),
                       'present': sum(1 for x in perf if x > 0),
                       'common': sum(1 for x in perf if progs and x / progs >= COMMON)}
    return out


def s113_avida_marks(env, seed, tasks):
    out = {}
    for m in MARKS:
        d = os.path.join(S113RUNS, '%s_seed%d' % (env, seed), 'piece_%02d' % (m // 1000 - 1), 'data')
        perf = rows(os.path.join(d, 'tasks.dat'))[-1][1:]
        progs = rows(os.path.join(d, 'count.dat'))[-1][2]
        out[str(m)] = {'programs': int(progs), 'present': sum(1 for x in perf if x > 0),
                       'common': sum(1 for x in perf if progs and x / progs >= COMMON)}
    return out


def setup_check(seed):
    """must_solve seed k against S113 NO TASK REWARDS seed k, first piece, updates 250 to 1,000: identical rows?"""
    mine_t, mine_c = avida_count(os.path.join(RUNS, 'must_solve_seed%d' % seed))
    d = os.path.join(S113RUNS, 'no_rewards_seed%d' % seed, 'piece_00')
    th, ch = avida_count(d)
    same_t = all(mine_t.get(u) == th.get(u) for u in (250, 500, 750, 1000))
    same_c = all(mine_c.get(u) == ch.get(u) for u in (250, 500, 750, 1000))
    return {'tasks_rows_identical_250_to_1000': same_t, 'count_rows_identical_250_to_1000': same_c}


def main():
    tasks = ranks()
    out = {'what': 'log S118: numbers for the results, written by tools/s118_gather_the_results.py from the raw output '
                   'of the six pilot runs and of S113 (scratch space)',
           'tasks': [t for t, _ in tasks], 'common share': COMMON, 'pilots': {}, 's113': {}}
    cpu = 0.0
    for p in PILOTS:
        for s in SEEDS:
            key = '%s_seed%d' % (p, s)
            d = os.path.join(RUNS, key)
            rec = {}
            fin = os.path.join(d, 'finished.json')
            rec['run'] = json.load(open(fin)) if os.path.exists(fin) else json.load(open(os.path.join(d, 'failed.json')))
            cpu += rec['run']['cpu_seconds']
            t, c = avida_count(d)
            rec['avida_count'] = avida_marks(t, c, tasks)
            last = max(c)
            rec['last_printed_update'] = last
            rec['died_out'] = c[last][2] == 0
            if p == 'must_solve':
                rec['around_the_switch'] = [{'update': u, 'programs': int(c[u][2]), 'births': int(c[u][8]),
                                             'deaths': int(c[u][9]),
                                             'performances_counted': int(sum(t[u])) if u in t else None}
                                            for u in sorted(c) if 4000 <= u <= 8000]
                rec['programs_every_1000'] = {str(u): int(c[u][2]) for u in sorted(c) if u % 1000 == 0}
                rec['setup_check_against_s113_no_rewards'] = setup_check(s)
            rec['test_processor'] = {}
            for m in MARKS:
                sp = os.path.join(d, 'data', 'detail-%d.spop' % m)
                if os.path.exists(sp) and c.get(m, [0, 0, 0])[2] > 0:
                    rec['test_processor'][str(m)] = per_snapshot(sp, tasks)
                else:
                    rec['test_processor'][str(m)] = None
            out['pilots'][key] = rec
            print(key, 'done', flush=True)
    out['cpu_seconds_of_the_six_runs'] = round(cpu, 1)
    summary = json.load(open(SCRATCH + '/s113/test_processor/summary.json'))
    for env in COMPARE:
        for s in SEEDS:
            key = '%s_seed%d' % (env, s)
            pr = summary['per run'][key]['performing']
            rec = {'test_processor_common_at_marks': {str(m): pr['common_at_marks'][str(m)] for m in MARKS},
                   'test_processor_present_at_marks': {str(m): pr['any_at_marks'][str(m)] for m in MARKS},
                   'avida_count': s113_avida_marks(env, s, tasks), 'test_processor_detail': {}}
            for m in (5000, 20000):
                sp = os.path.join(S113RUNS, key, 'piece_%02d' % (m // 1000 - 1), 'data', 'detail-1000.spop')
                rec['test_processor_detail'][str(m)] = per_snapshot(sp, tasks) if os.path.exists(sp) else None
            out['s113'][key] = rec
            print(key, 'done', flush=True)
    json.dump(out, open(OUTJSON, 'w'), indent=1)
    print('written', OUTJSON)


if __name__ == '__main__':
    main()
