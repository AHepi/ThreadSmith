#!/usr/bin/env python3
"""s116_probe_the_saved_program_populations_after_the_cross_examination.py

A corrected copy of s116_probe_the_saved_program_populations.py (kept unchanged), made when log S116's GLM
cross-examination was settled. One change, marked [Xb5]: in the growing list, a task first rewarded during piece k is
first rewarded after update k x 1000 (piece k runs from k x 1000 to (k + 1) x 1000, and the save at k x 1000 is the end
of piece k - 1), so its first reward is recorded as k x 1000 + 1, not k x 1000; the summariser's "rewarded_by_snapshot"
label is then no longer one save early. That label feeds no number or verdict in the S116 results, so this copy was not
run; everything else is the original, line for line.

What the original does, in plain words:

What it does, in plain words (log S116, batch 2 of S115's plan): takes a copy of every program population S113 saved
(18 runs x the saves at 5,000, 10,000, ..., 50,000 updates) and runs GPT 6 Astra's probe battery from reply 01
(tools/s115/01/probe_task_audit.py, UNCHANGED) on the copies: every living distinct instruction sequence is run alone on
Avida's test CPU with 8 fixed input triples, every checkable task listed at reward 0 (profiles "core" and "logic_high").
Then it runs reply 01's summariser (tools/s115/01/summarize_probes.py, UNCHANGED) with a reward history made from S113's
own environments, and adds its own summary of what the plan (results/S116 ... written before running.md, section 1)
measures: per run and saved update, how many logic and never-rewarded arithmetic capabilities were present and common,
ever seen, kept; the same for logic_high. It also gives one reading the plan did not name (added after the first results,
descriptive only): logic tasks credited on at least ONE of the 8 inputs (and viable), to set beside S113's test
processor, which used one set of inputs; and logic tasks on the logic_high input triples whose numbers come in the
order Avida's world gives them (credited on all of those and viable).

Avida is called through a wrapper (scratch s116/bin/avida) that adds nice -n 19 and a one-hour time limit to every Avida
process. At most two probe processes at once (the caller keeps the whole job at three Avida processes or fewer).
Nothing is written into S113's folder: the saved populations are copied first. Raw output stays in the scratch space.
Avida's programs copy themselves only inside Avida's simulated processor; nothing here copies itself on the real machine.

  python3 s116_probe_the_saved_program_populations.py probe [N]   run the probes (N at once, default 2)
  python3 s116_probe_the_saved_program_populations.py summary     write s116/probes/summary.json
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import csv, json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R      # noqa: E402  (paths, task list; read only)

SCRATCH = R.SCRATCH
S116 = SCRATCH + '/s116'
COPIES = S116 + '/copies'
PROBES = S116 + '/probes'
RUNDIR = S116 + '/probe_rundir'
WRAPPER = S116 + '/bin/avida'
SOURCE = SCRATCH + '/avida'
REPLY01 = os.path.join(HERE, 's115', '01')
MARKS = list(range(5000, 50001, 5000))
KEYS = ['%s_seed%d' % (e, s) for e in R.ENVIRONMENTS for s in R.SEEDS]
LOGIC = [t for t, _ in R.load_ranks()]
COMMON = 0.10


def copy_saves():
    os.makedirs(RUNDIR, exist_ok=True)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(R.S111CONF, f), RUNDIR)
    for key in KEYS:
        d = os.path.join(COPIES, key)
        os.makedirs(d, exist_ok=True)
        for m in MARKS:
            src = os.path.join(R.OUT, key, 'piece_%02d' % (m // 1000 - 1), 'data', 'detail-1000.spop')
            dst = os.path.join(d, 'u%d.spop' % m)
            if not (os.path.exists(dst) and os.path.getsize(dst) == os.path.getsize(src)):
                shutil.copyfile(src, dst)


def reward_history(key):
    """First update at which each probe task was rewarded in this S113 run; 'never' otherwise."""
    env = key.rsplit('_seed', 1)[0]
    ranks = dict(R.load_ranks())
    first = {}
    if env == 'growing':
        hist = json.load(open(os.path.join(R.OUT, key, 'state.json')))['history']
        for t, level in ranks.items():
            when = [h['piece'] * 1000 + 1 for h in hist if h['unlocked_during_piece'] >= level]   # [Xb5]
            first[t] = min(when) if when else 'never'
    else:
        for t in ranks:
            paid = {'fixed_graded': t in R.TWO, 'common_pays_less': t in R.TWO, 'equ_only': t == 'equ',
                    'no_rewards': False, 'fixed_large': True}[env]
            first[t] = 0 if paid else 'never'
    return first


def probe_one(key):
    out = os.path.join(PROBES, key)
    if os.path.exists(os.path.join(out, 'summary', 'capabilities.tsv')):
        return key, 'already done'
    if os.path.exists(out):
        shutil.rmtree(out)
    argv = ['python3', '-B', os.path.join(REPLY01, 'probe_task_audit.py'), '--source', SOURCE, '--run-dir', RUNDIR]
    for m in MARKS:
        argv += ['--snapshot', 'u%d' % m, str(m), os.path.join(COPIES, key, 'u%d.spop' % m)]
    argv += ['--out', out, '--avida', WRAPPER, '--profiles', 'core,logic_high', '--run']
    log = open(os.path.join(PROBES, key + '.log'), 'w')
    rc = subprocess.run(argv, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    if rc != 0:
        return key, 'probe exit %d' % rc
    tasks = [r for r in csv.DictReader(open(os.path.join(out, 'tasks.tsv')), delimiter='\t')
             if r['profile'] == 'core' and r['name'] == r['canonical'] and r['name'] != 'dontcare']
    first = reward_history(key)
    with open(os.path.join(out, 'reward_history.tsv'), 'w') as f:
        f.write('canonical\tfirst_reward_update\n')
        for r in tasks:
            f.write('%s\t%s\n' % (r['canonical'], first.get(r['canonical'], 'never')))
    rc = subprocess.run(['python3', '-B', os.path.join(REPLY01, 'summarize_probes.py'), out, '--rewards',
                         os.path.join(out, 'reward_history.tsv')], stdout=log, stderr=subprocess.STDOUT).returncode
    return key, 'summary exit %d' % rc


def arithmetic(name):
    return name in ('echo', 'add', 'add3', 'sub') or name.startswith('math_')


def world_order_inputs(out):
    """logic_high input triples whose three numbers come in the order Avida's world gives them (high bytes 15, 51, 85)."""
    ids = []
    for r in csv.DictReader(open(os.path.join(out, 'inputs.tsv')), delimiter='\t'):
        if r['profile'] == 'logic_high' and [int(r['input%d' % j]) >> 24 for j in range(3)] == [15, 51, 85]:
            ids.append(int(r['input_id']))
    return ids


def read_logic_high(out, key, only=None):
    """Same rule as the summariser (credited on all 8 inputs and viable), for the logic_high profile; with only=[ids],
    on those input triples only."""
    tasks = [r for r in csv.DictReader(open(os.path.join(out, 'tasks.tsv')), delimiter='\t')
             if r['profile'] == 'logic_high' and r['name'] == r['canonical']]
    schema = [r['column'] for r in sorted((r for r in csv.DictReader(open(os.path.join(out, 'schema.tsv')),
                                                                       delimiter='\t') if r['profile'] == 'logic_high'),
                                          key=lambda r: int(r['position']))]
    res = {}
    for m in MARKS:
        per = {}
        total = None
        for i in (only if only is not None else range(8)):
            rows = []
            for line in open(os.path.join(out, 'results', 'logic_high', 'u%d-input%d.dat' % (m, i))):
                if line.startswith('#') or not line.strip():
                    continue
                rows.append(dict(zip(schema, line.split())))
            for r in rows:
                p = per.setdefault(r['id'], {'n': int(r['num_units']), 'ok': [True] * len(tasks)})
                for j, t in enumerate(tasks):
                    if not (int(r['task.%s' % t['task_index']]) > 0 and int(r['viable']) > 0):
                        p['ok'][j] = False
        total = sum(p['n'] for p in per.values())
        counts = [sum(p['n'] for p in per.values() if p['ok'][j]) for j in range(len(tasks))]
        res[m] = {'present': sorted(t['name'] for j, t in enumerate(tasks) if counts[j] > 0),
                  'common': sorted(t['name'] for j, t in enumerate(tasks) if total and counts[j] / total >= COMMON)}
    return res


def summarise_run(key):
    out = os.path.join(PROBES, key)
    cap = list(csv.DictReader(open(os.path.join(out, 'summary', 'capabilities.tsv')), delimiter='\t'))
    names = sorted({r['task'] for r in cap})
    logic_names = [n for n in names if n in LOGIC]
    arith_names = [n for n in names if arithmetic(n)]
    assert len(logic_names) == 77, (key, len(logic_names))
    per = {}
    for m in MARKS:
        rows = {r['task']: r for r in cap if int(r['update']) == m}
        pres = {n for n, r in rows.items() if int(r['viable_all']) > 0}
        com = {n for n, r in rows.items() if r['fraction_all'] != '' and float(r['fraction_all']) >= COMMON}
        # an added, descriptive reading (not in the plan): credited on at least one of the 8 inputs and viable
        pres1 = {n for n, r in rows.items() if int(r['viable_any']) > 0}
        com1 = {n for n, r in rows.items() if int(r['population']) and int(r['viable_any']) / int(r['population']) >= COMMON}
        per[m] = {'population': int(next(iter(rows.values()))['population']),
                  'logic_present_on_any_input': sorted(pres1 & set(logic_names)),
                  'logic_common_on_any_input': sorted(com1 & set(logic_names)),
                  'logic_present': sorted(pres & set(logic_names)), 'logic_common': sorted(com & set(logic_names)),
                  'arith_present': sorted(pres & set(arith_names)), 'arith_common': sorted(com & set(arith_names))}
    ever = set()
    table = {}
    for m in MARKS:
        now = set(per[m]['logic_present']) | set(per[m]['arith_present'])
        ever |= now
        table[str(m)] = {'present_logic': len(per[m]['logic_present']), 'common_logic': len(per[m]['logic_common']),
                         'present_arith': len(per[m]['arith_present']), 'common_arith': len(per[m]['arith_common']),
                         'present_all': len(now), 'ever_seen_all': len(ever), 'population': per[m]['population'],
                         'present_logic_on_any_input': len(per[m]['logic_present_on_any_input']),
                         'common_logic_on_any_input': len(per[m]['logic_common_on_any_input'])}
    ret = list(csv.DictReader(open(os.path.join(out, 'summary', 'retention.tsv')), delimiter='\t'))
    r25 = [r for r in ret if r['from_label'] == 'u25000' and r['to_label'] == 'u50000'][0]
    # the summariser's sets are all core tasks (fib_ included); recompute on logic + arithmetic for the plan's reading
    sets = {m: set(per[m]['logic_present']) | set(per[m]['arith_present']) for m in MARKS}
    base = sets[25000]
    cont = set(base)
    for m in MARKS:
        if m >= 25000:
            cont &= sets[m]
    endpoint = base & sets[50000]
    high = read_logic_high(out, key)
    wo = world_order_inputs(out)
    world = read_logic_high(out, key, only=wo)
    dyn = list(csv.DictReader(open(os.path.join(out, 'summary', 'snapshot_dynamics.tsv')), delimiter='\t'))
    return {'per_save': table,
            'present_at_50000': per[50000],
            'retention_25000_to_50000': {'present_at_25000': len(base), 'present_at_both_ends': len(endpoint),
                                         'present_at_every_save_between': len(cont),
                                         'present_after_a_sampled_gap': len(endpoint - cont),
                                         'summariser_row_all_core_tasks': r25},
            'ever_seen_rise_25000_to_50000': table['50000']['ever_seen_all'] - table['25000']['ever_seen_all'],
            'present_change_25000_to_50000': table['50000']['present_all'] - table['25000']['present_all'],
            'logic_high': {str(m): {'present': len(high[m]['present']), 'common': len(high[m]['common'])}
                           for m in MARKS},
            'logic_high_sets_at_50000': high[50000],
            'logic_high_world_order_inputs': wo,
            'logic_high_world_order': {str(m): {'present': len(world[m]['present']), 'common': len(world[m]['common'])}
                                       for m in MARKS},
            'distinct_sequences': {r['update']: int(r['distinct_sequences']) for r in dyn},
            'arithmetic_tasks_probed': arith_names}


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else 'probe'
    if what == 'probe':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
        os.makedirs(PROBES, exist_ok=True)
        copy_saves()
        with ThreadPoolExecutor(max_workers=n) as pool:
            for key, status in pool.map(probe_one, KEYS):
                print(key, status, flush=True)
    elif what == 'summary':
        s = {'what': 'log S116 batch 2: reply 01 probe (core, logic_high; all 8 inputs, viable) on copies of S113\'s '
                     'saved program populations', 'common_share': COMMON,
             'per run': {k: summarise_run(k) for k in KEYS}}
        json.dump(s, open(os.path.join(PROBES, 'summary.json'), 'w'), indent=1)
        print('written', os.path.join(PROBES, 'summary.json'))


if __name__ == '__main__':
    main()
