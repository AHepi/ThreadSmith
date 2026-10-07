#!/usr/bin/env python3
"""s116_compete_a_rare_and_a_common_kind.py

What it does, in plain words (log S116, batch 3 of S115's plan, GPT 6 Astra's reply 05 "resource-frequency
competition"): tests the mechanism S113's expectation E6 relied on, that in the Avida execution environment COMMON
TASKS PAY LESS a kind of Avida program doing tasks few others do is paid more and so grows when it is rare.

Two kinds are taken from S113's COMMON TASKS PAY LESS seed 1 at update 50,000, by the rule written before running
(results/S116 ... written before running.md, section 3), using batch 2's probe (reply 01, core profile, credited on all
8 inputs and viable): A = the most common viable distinct instruction sequence; B = the most common viable sequence whose
set of the nine paid two-input tasks includes one that A lacks (else the most common with a different set).
Each run fills the whole 60 x 60 world at update 0 with A in a share s of the cells and B in the rest (cells drawn at
random by a placement seed), in S113's COMMON TASKS PAY LESS environment (S113's own function, imported unchanged), every
resource starting at the level S113's seed 1 had at update 50,000, S111's avida.cfg with every instruction change off
(copy error 0, one-instruction insertion and deletion 0). 5 shares (1%, 10%, 50%, 90%, 99%) x 3 placements x 2,000
updates, continuous (no reload). The program population is saved every 500 updates and A's share counted from it.

Every Avida process through the wrapper s116/bin/avida (nice -n 19, one-hour limit); at most three at once.
Raw output: scratch s116/competition/. Avida's programs copy themselves only inside Avida's simulated processor.
  python3 s116_compete_a_rare_and_a_common_kind.py choose     pick A and B, write their files
  python3 s116_compete_a_rare_and_a_common_kind.py run [N]    the 15 runs, N at once (default 3)
  python3 s116_compete_a_rare_and_a_common_kind.py count      A's share over time, into competition/summary.json
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import csv, json, os, random, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R      # noqa: E402  (environment text, resource reading)
import s116_probe_the_saved_program_populations as P       # noqa: E402  (probe folders, wrapper)

COMP = P.S116 + '/competition'
SOURCE_KEY = 'common_pays_less_seed1'
MARK = 50000
SHARES = [0.01, 0.10, 0.50, 0.90, 0.99]
PLACEMENTS = [1, 2, 3]
CELLS = 3600
UPDATES = 2000


def probe_rows():
    out = os.path.join(P.PROBES, SOURCE_KEY)
    tasks = [r for r in csv.DictReader(open(os.path.join(out, 'tasks.tsv')), delimiter='\t') if r['profile'] == 'core']
    idx = {r['name']: r['task_index'] for r in tasks}
    schema = [r['column'] for r in sorted((r for r in csv.DictReader(open(os.path.join(out, 'schema.tsv')),
                                                                       delimiter='\t') if r['profile'] == 'core'),
                                          key=lambda r: int(r['position']))]
    seqs = {}
    for i in range(8):
        for line in open(os.path.join(out, 'results', 'core', 'u%d-input%d.dat' % (MARK, i))):
            if line.startswith('#') or not line.strip():
                continue
            r = dict(zip(schema, line.split()))
            s = seqs.setdefault(r['id'], {'n': int(r['num_units']), 'seq': r['sequence'], 'viable': True,
                                          'tasks': set(R.TWO)})
            if int(r['viable']) <= 0:
                s['viable'] = False
            for t in R.TWO:
                if int(r['task.%s' % idx[t]]) <= 0:
                    s['tasks'].discard(t)
    order = list(seqs.values())
    order.sort(key=lambda s: -s['n'])   # stable: ties keep the file's order
    return order


def decode(seq):
    names = [l.split()[1] for l in open(os.path.join(R.S111CONF, 'instset-heads.cfg'))
             if l.startswith('INST ')]
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = dict(zip(letters, names))
    return [table[c] for c in seq]


def choose():
    order = [s for s in probe_rows() if s['viable']]
    a = order[0]
    b = next((s for s in order[1:] if s['tasks'] - a['tasks']), None)
    rule = 'has a paid task A lacks'
    if b is None:
        b = next(s for s in order[1:] if s['tasks'] != a['tasks'])
        rule = 'different set of paid tasks'
    os.makedirs(COMP, exist_ok=True)
    for name, s in (('A', a), ('B', b)):
        open(os.path.join(COMP, name + '.org'), 'w').write('#inst_set heads_default\n#hw_type 0\n\n'
                                                          + '\n'.join(decode(s['seq'])) + '\n')
    info = {'A': {'programs_at_50000': a['n'], 'paid_tasks': sorted(a['tasks']), 'length': len(a['seq']),
                  'sequence': a['seq']},
            'B': {'programs_at_50000': b['n'], 'paid_tasks': sorted(b['tasks']), 'length': len(b['seq']),
                  'sequence': b['seq'], 'chosen_because': rule},
            'viable_sequences_ranked_before_B': order.index(b)}
    json.dump(info, open(os.path.join(COMP, 'kinds.json'), 'w'), indent=1)
    print(json.dumps({k: {x: y for x, y in v.items() if x != 'sequence'} if isinstance(v, dict) else v
                      for k, v in info.items()}, indent=1))


def run_one(job):
    share, placement = job
    si = SHARES.index(share)
    d = os.path.join(COMP, 'share%02d_place%d' % (round(share * 100), placement))
    if os.path.exists(os.path.join(d, 'data', 'detail-%d.spop' % UPDATES)):
        return d, 'already done'
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg']:
        shutil.copy(os.path.join(R.S111CONF, f), d)
    for f in ['A.org', 'B.org']:
        shutil.copy(os.path.join(COMP, f), d)
    res = R.resources_left(os.path.join(R.OUT, SOURCE_KEY, 'piece_49'))
    open(os.path.join(d, 'environment.cfg'), 'w').write(
        R.environment_text('common_pays_less', R.load_ranks(), resources=res))
    rng = random.Random(1000 * placement + si)
    cells = list(range(CELLS))
    a_cells = set(rng.sample(cells, round(share * CELLS)))
    ev = ['u begin Inject %s.org %d' % ('A' if c in a_cells else 'B', c) for c in cells]
    ev += ['u 50:50:%d PrintCountData' % UPDATES, 'u 50:50:%d PrintResourceData' % UPDATES,
           'u 50:50:%d PrintTasksData' % UPDATES, 'u 500:500:%d SavePopulation' % UPDATES, 'u %d Exit' % UPDATES]
    open(os.path.join(d, 'events.cfg'), 'w').write('\n'.join(ev) + '\n')
    seed = 116000 + 10 * placement + si
    argv = [P.WRAPPER, '-s', str(seed), '-set', 'VERBOSITY', '0', '-set', 'COPY_MUT_PROB', '0',
            '-set', 'DIVIDE_INS_PROB', '0', '-set', 'DIVIDE_DEL_PROB', '0']
    t0 = time.time()
    rc = subprocess.run(argv, cwd=d, stdout=open(os.path.join(d, 'avida.log'), 'w'), stderr=subprocess.STDOUT,
                        stdin=subprocess.DEVNULL).returncode
    open(os.path.join(d, 'command.txt'), 'w').write('cd %s && %s\nexit %d after %.0f s\n'
                                                    % (d, ' '.join(argv), rc, time.time() - t0))
    return d, 'exit %d after %.0f s' % (rc, time.time() - t0)


def count():
    kinds = json.load(open(os.path.join(COMP, 'kinds.json')))
    a, b = kinds['A']['sequence'], kinds['B']['sequence']
    out = {}
    for share in SHARES:
        for placement in PLACEMENTS:
            d = os.path.join(COMP, 'share%02d_place%d' % (round(share * 100), placement))
            row = {}
            for u in range(500, UPDATES + 1, 500):
                na = nb = other = 0
                others = set()
                for line in open(os.path.join(d, 'data', 'detail-%d.spop' % u)):
                    if line.startswith('#') or not line.strip():
                        continue
                    w = line.split()
                    n = int(w[4])
                    if n <= 0:
                        continue
                    if w[16] == a:
                        na += n
                    elif w[16] == b:
                        nb += n
                    else:
                        other += n
                        others.add(w[16])
                row[str(u)] = {'A': na, 'B': nb, 'other': other, 'other_sequences': len(others),
                               'share_A': round(na / (na + nb), 4) if na + nb else None}
            out['%d%%, placement %d' % (round(share * 100), placement)] = {'start_share_A': share, 'saves': row}
    json.dump({'what': 'log S116 batch 3b: A against B under COMMON TASKS PAY LESS, instruction changes off',
               'kinds': {k: {x: y for x, y in v.items() if x != 'sequence'} if isinstance(v, dict) else v
                         for k, v in kinds.items()},
               'runs': out}, open(os.path.join(COMP, 'summary.json'), 'w'), indent=1)
    for k, v in out.items():
        print(k, [v['saves'][str(u)]['share_A'] for u in range(500, UPDATES + 1, 500)],
              'other', v['saves'][str(UPDATES)]['other'])


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else 'run'
    if what == 'choose':
        choose()
    elif what == 'run':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        jobs = [(s, p) for p in PLACEMENTS for s in SHARES]
        with ThreadPoolExecutor(max_workers=n) as pool:
            for d, status in pool.map(run_one, jobs):
                print(d, status, flush=True)
    elif what == 'count':
        count()


if __name__ == '__main__':
    main()
