#!/usr/bin/env python3
"""s113_run_the_avida_execution_environments.py

What it does, in plain words: runs Avida (the evolutionary-computation simulator built in log S111) once per Avida
execution environment and per seed, for log S113. Every run starts from the same Avida program (Avida's default
ancestor, S111's default-heads.org), with the same instruction set, world size (60 x 60), instruction-change rate
(copy error 0.0075 per copied instruction, S111's default) and every other setting of S111's avida.cfg. Only the
Avida execution environment differs: which of Avida's 77 logic tasks are rewarded, by how much, and whether the reward
comes from a resource that runs down when many programs use it, or grows as the program population becomes able to do
more.

Every run is made of 50 pieces of 1,000 updates each. At the end of each piece Avida saves the whole program
population (every Avida program, where it sits, its Avida fitness), and the next piece is a new Avida process that
loads that saved program population and goes on. All environments are run this same way, so the pieces do not differ
between them. Only the GROWING LIST environment uses the break: between pieces this script reads how many programs
performed each task and, by a rule written before running, may add the next harder tasks to the rewarded list.
For COMMON TASKS PAY LESS the amount left of each resource at the end of a piece is carried into the next piece.

All 77 tasks are listed in every environment, so that Avida counts which programs perform each of them; a task that
is not rewarded is listed with reward value 0 (Avida multiplies the program's processor-time share by 2 to the power of
the value, so 0 changes nothing).

Raw output stays in the scratch space (runs/<environment>_seed<k>/piece_<nn>/). Every Avida process runs under a
timeout. Avida's programs copy themselves only inside Avida's simulated processor; nothing here copies itself on the
real machine. Run with no argument to run everything (at most 3 runs at once); with "test" to run a short test.
Written 30 September 2026 by the one Opus 5.5 agent of log S113.
"""
import json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
OUT = SCRATCH + '/s113/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(os.path.dirname(HERE), 'results')
S111CONF = os.path.join(RESULTS, 'S111 Avida - the runs', 'configuration')
S113RUNS = os.path.join(RESULTS, 'S113 Which execution environments learn - the runs')
RANKS = os.path.join(S113RUNS, 'the 77 tasks ranked by the fewest nand steps.json')

PIECE = 1000            # updates per piece
PIECES = 50             # 50,000 updates in all, as S111
SEEDS = [1, 2, 3]
COMMON = 0.10           # a task is "common" when at least this share of the program population performs it
PIECE_TIMEOUT = 900     # seconds, per Avida process
KEEP_EVERY = 5          # keep the saved program population of every 5th piece (every 5,000 updates)

ENVIRONMENTS = ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']

TWO = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']


def load_ranks():
    rows = json.load(open(RANKS))['tasks']
    return [(r['task'], r['fewest_nand_steps']) for r in rows]


def reaction_name(task):
    return task.upper() if task in TWO else 'LOG3' + task[-2:].upper()


def environment_text(env, ranks, unlocked=0, resources=None):
    """The environment.cfg of one piece. unlocked: the highest level rewarded (growing list only).
    resources: amount left of each resource at the end of the last piece (common_pays_less only)."""
    lines = ['# log S113, environment "%s" (written by tools/s113_run_the_avida_execution_environments.py)' % env]
    if env == 'common_pays_less':
        for t in TWO:
            init = '' if not resources else ':initial=%.6f' % resources.get('res' + t.upper(), 0.0)
            lines.append('RESOURCE res%s:inflow=100:outflow=0.01%s' % (t.upper(), init))
    for task, level in ranks:
        if env == 'fixed_graded':
            value = level if task in TWO else 0
        elif env == 'equ_only':
            value = level if task == 'equ' else 0
        elif env == 'no_rewards':
            value = 0
        elif env == 'growing':
            value = level if level <= unlocked else 0
        elif env == 'fixed_large':
            value = level
        elif env == 'common_pays_less':
            value = level if task in TWO else 0
        else:
            raise ValueError(env)
        if env == 'common_pays_less' and task in TWO:
            proc = 'process:resource=res%s:value=%.1f:type=pow:frac=0.0025:max=1.0' % (task.upper(), value)
        else:
            proc = 'process:value=%.1f:type=pow' % value
        lines.append('REACTION %s %s %s requisite:max_count=1' % (reaction_name(task), task, proc))
    return '\n'.join(lines) + '\n'


def events_text(first):
    ev = ['u begin Inject default-heads.org' if first else 'u begin LoadPopulation start.spop']
    ev += ['u 250:250:%d PrintTasksData' % PIECE,
           'u 250:250:%d PrintCountData' % PIECE,
           'u %d PrintAverageData' % PIECE,
           'u %d PrintDominantData' % PIECE,
           'u %d PrintResourceData' % PIECE,
           'u %d SavePopulation' % PIECE,
           'u %d Exit' % PIECE]
    return '\n'.join(ev) + '\n'


def read_dat(path):
    rows = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        rows.append([float(x) for x in line.split()])
    return rows


def resources_left(piece_dir):
    path = os.path.join(piece_dir, 'data', 'resource.dat')
    names, rows = [], read_dat(path)
    for line in open(path):
        if line.startswith('#') and ':' in line and line[1:].strip()[:1].isdigit():
            names.append(line.split(':', 1)[1].strip())
    # columns: update, then one per resource
    last = rows[-1]
    res = {}
    for i, n in enumerate(names[1:], start=1):
        res[n] = last[i]
    return res


def shares_at_end(piece_dir, ranks):
    tasks = read_dat(os.path.join(piece_dir, 'data', 'tasks.dat'))[-1]
    count = read_dat(os.path.join(piece_dir, 'data', 'count.dat'))[-1]
    programs = count[2]      # count.dat column 3: number of organisms
    return {task: (tasks[i + 1] / programs if programs else 0.0) for i, (task, _) in enumerate(ranks)}


def next_unlocked(unlocked, shares, ranks):
    """Growing list rule (written before running): after a piece, if at least one task of the highest level now
    rewarded is performed by at least COMMON of the program population, the next level is added to the rewarded list.
    At most one level is added per piece."""
    top = max(level for _, level in ranks)
    if unlocked >= top:
        return unlocked
    at_top = [t for t, level in ranks if level == unlocked]
    if any(shares[t] >= COMMON for t in at_top):
        return unlocked + 1
    return unlocked


def run_one(env, seed, pieces=PIECES, out=OUT):
    ranks = load_ranks()
    run_dir = os.path.join(out, '%s_seed%d' % (env, seed))
    os.makedirs(run_dir, exist_ok=True)
    log = open(os.path.join(run_dir, 'run.log'), 'a')
    state_path = os.path.join(run_dir, 'state.json')
    state = json.load(open(state_path)) if os.path.exists(state_path) else {'done': 0, 'unlocked': 1, 'history': []}
    while state['done'] < pieces:
        k = state['done']
        pdir = os.path.join(run_dir, 'piece_%02d' % k)
        if os.path.exists(pdir):
            shutil.rmtree(pdir)          # a piece that did not finish is run again from its start
        os.makedirs(pdir)
        for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
            shutil.copy(os.path.join(S111CONF, f), pdir)
        prev = os.path.join(run_dir, 'piece_%02d' % (k - 1)) if k else None
        resources = resources_left(prev) if (prev and env == 'common_pays_less') else None
        with open(os.path.join(pdir, 'environment.cfg'), 'w') as f:
            f.write(environment_text(env, ranks, state['unlocked'], resources))
        with open(os.path.join(pdir, 'events.cfg'), 'w') as f:
            f.write(events_text(k == 0))
        if k:
            shutil.copy(os.path.join(prev, 'data', 'detail-%d.spop' % PIECE), os.path.join(pdir, 'start.spop'))
        piece_seed = seed * 1000 + k
        argv = ['timeout', str(PIECE_TIMEOUT), AVIDA, '-s', str(piece_seed), '-set', 'VERBOSITY', '0',
                '-set', 'COPY_MUT_PROB', '0.0075']
        t0 = time.time()
        rc = subprocess.run(argv, cwd=pdir, stdout=open(os.path.join(pdir, 'avida.log'), 'w'),
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
        secs = time.time() - t0
        ok = rc == 0 and os.path.exists(os.path.join(pdir, 'data', 'detail-%d.spop' % PIECE))
        log.write('%s seed %d piece %d: exit %d after %.0f s; command: cd "%s" && %s\n'
                  % (env, seed, k, rc, secs, pdir, ' '.join(argv)))
        log.flush()
        if not ok:
            log.write('piece failed; stopping this run\n')
            return False
        shares = shares_at_end(pdir, ranks)
        rec = {'piece': k, 'update_end': (k + 1) * PIECE, 'unlocked_during_piece': state['unlocked'],
               'seconds': round(secs), 'seed': piece_seed}
        if env == 'growing':
            new = next_unlocked(state['unlocked'], shares, ranks)
            rec['unlocked_after_piece'] = new
            state['unlocked'] = new
        state['history'].append(rec)
        state['done'] = k + 1
        # the previous piece's saved program population is no longer needed unless it ends at a multiple of 5,000
        # updates; this piece's copy of it (start.spop) is not needed either
        if prev and (k % KEEP_EVERY) != 0:
            sp = os.path.join(prev, 'data', 'detail-%d.spop' % PIECE)
            if os.path.exists(sp):
                os.remove(sp)
        st = os.path.join(pdir, 'start.spop')
        if os.path.exists(st):
            os.remove(st)
        json.dump(state, open(state_path, 'w'), indent=1)
    return True


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        out = SCRATCH + '/s113/test_runs'
        env = sys.argv[2] if len(sys.argv) > 2 else 'fixed_large'
        print(run_one(env, 99, pieces=int(sys.argv[3]) if len(sys.argv) > 3 else 2, out=out))
        return
    jobs = [(e, s) for s in SEEDS for e in ENVIRONMENTS]
    if len(sys.argv) > 1:
        wanted = sys.argv[1].split(',')
        jobs = [(e, s) for e, s in jobs if '%s_seed%d' % (e, s) in wanted or e in wanted]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for (e, s), ok in zip(jobs, pool.map(lambda j: run_one(*j), jobs)):
            print(e, s, 'finished' if ok else 'FAILED', time.strftime('%H:%M:%S'), flush=True)


if __name__ == '__main__':
    main()
