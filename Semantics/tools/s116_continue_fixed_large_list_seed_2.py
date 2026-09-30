#!/usr/bin/env python3
"""s116_continue_fixed_large_list_seed_2.py

What it does, in plain words (log S116, the extension proposed by the S113 settlement): S113's run FIXED LARGE LIST
seed 2 was the one run whose count of common computational capabilities was still rising at update 50,000 (28 at
40,000, 37 at 45,000, 41 at 50,000). This script continues it for 25,000 more updates exactly as S113 ran it: S113's own
runner function (run_one in tools/s113_run_the_avida_execution_environments.py, imported and called UNCHANGED) on a copy
of that run's state and of its last piece (the program population saved at 50,000), so 25 more pieces of 1,000 updates,
each a new Avida process that loads the program population the last piece saved (Avida seeds 2,050 to 2,074, the same
rule as S113's). It carries every reload caveat of S113's pieces (S114 restart audit; FIXED LARGE LIST never audited).

Then it counts as S113 did: (i) Avida's world count, from tasks.dat and count.dat every 250 updates (common = at least
10% of the programs; S113's runner's own reading code); (ii) the test-processor count on the program populations saved
at 50,000 (the copy, as a check: it must give 41 common), 55,000, 60,000, 65,000, 70,000 and 75,000, with S113's own
measuring function (one_snapshot in tools/s113_measure_capabilities_in_the_saved_program_populations.py, imported and
called UNCHANGED, its working folder pointed into the S116 scratch space).

Nothing is written into S113's folder. Run the whole script under nice -n 19; every Avida process has a time limit
(900 s per piece, S113's; 3,600 s per test-processor call, S113's). Raw output: scratch s116/extension/.
  python3 s116_continue_fixed_large_list_seed_2.py run       the 25 pieces
  python3 s116_continue_fixed_large_list_seed_2.py count     both counts, into s116/extension/counts.json
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import json, os, shutil, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R            # noqa: E402  (S113's runner, unchanged)
import s113_measure_capabilities_in_the_saved_program_populations as M   # noqa: E402  (S113's measure, unchanged)

EXT = R.SCRATCH + '/s116/extension'
RUNS = EXT + '/runs'
KEY = 'fixed_large_seed2'
PIECES = 75


def prepare():
    src = os.path.join(R.OUT, KEY)
    dst = os.path.join(RUNS, KEY)
    if os.path.exists(os.path.join(dst, 'state.json')):
        return
    os.makedirs(dst)
    shutil.copy(os.path.join(src, 'state.json'), dst)
    shutil.copy(os.path.join(src, 'run.log'), dst)
    shutil.copytree(os.path.join(src, 'piece_49'), os.path.join(dst, 'piece_49'))


def world_count():
    """Avida's count in the world at every 250-update sample, as S113's runner reads a piece end."""
    tasks = [t for t, _ in R.load_ranks()]
    out = {}
    for k in range(49, PIECES):
        pdir = os.path.join(RUNS, KEY, 'piece_%02d' % k)
        trows = R.read_dat(os.path.join(pdir, 'data', 'tasks.dat'))
        crows = R.read_dat(os.path.join(pdir, 'data', 'count.dat'))
        for tr, cr in zip(trows, crows):
            assert tr[0] == cr[0]
            if tr[0] == 0:
                continue          # update 0 of a piece counts every loaded program as a birth (S114); not sampled
            label = k * 1000 + int(tr[0])
            programs = cr[2]
            shares = [tr[i + 1] / programs if programs else 0.0 for i in range(len(tasks))]
            out[label] = {'common': sum(s >= R.COMMON for s in shares), 'present': sum(s > 0 for s in shares),
                          'programs': int(programs)}
    return out


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else 'run'
    if what == 'run':
        prepare()
        ok = R.run_one('fixed_large', 2, pieces=PIECES, out=RUNS)
        print('finished' if ok else 'FAILED', flush=True)
    elif what == 'count':
        R.OUT = RUNS                      # S113's measuring function reads R.OUT/<key>/piece_<nn>/data/detail-1000.spop
        M.WORK = EXT + '/test_processor'  # and works in M.WORK; both pointed into the S116 scratch space
        tasks = [t for t, _ in R.load_ranks()]
        tp = {}
        for mark in [50000, 55000, 60000, 65000, 70000, 75000]:
            _, _, snap = M.one_snapshot((KEY, mark, tasks))
            common = [tasks[j] for j in range(len(tasks)) if snap['performing'][j] / snap['programs'] >= M.COMMON]
            common_rep = [tasks[j] for j in range(len(tasks))
                          if snap['performing_and_replicating'][j] / snap['programs'] >= M.COMMON]
            tp[str(mark)] = {'programs': snap['programs'], 'distinct_sequences': snap['distinct_sequences'],
                             'common': len(common), 'present': sum(x > 0 for x in snap['performing']),
                             'common_and_replicating': len(common_rep), 'common_tasks': common}
            print(mark, tp[str(mark)]['common'], tp[str(mark)]['present'], flush=True)
        wc = world_count()
        hist = json.load(open(os.path.join(RUNS, KEY, 'state.json')))['history']
        json.dump({'what': 'log S116 extension: FIXED LARGE LIST seed 2 continued from 50,000 to 75,000 in S113\'s '
                           'pieces; both S113 counts', 'test_processor': tp,
                   'world_count_every_250': {str(k): v for k, v in sorted(wc.items())},
                   'pieces': [h for h in hist if h['piece'] >= 50]},
                  open(os.path.join(EXT, 'counts.json'), 'w'), indent=1)
        print('written', os.path.join(EXT, 'counts.json'))


if __name__ == '__main__':
    main()
