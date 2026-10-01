#!/usr/bin/env python3
"""s118_run_the_two_pilots.py

What it does, in plain words: runs the two small pilots of log S118 in Avida (the evolutionary-computation simulator
built in log S111; stock, commit 47f13dad, unchanged). Each pilot asks whether an Avida execution environment can push
a program population to solve problems without naming which problem (which logic function) it wants.

  ANY FUNCTION, RARE PAYS MORE ("any_function"): every one of the 251 logic functions of the three numbers handed in
      that is neither a constant nor "hand back one of the numbers unchanged" (Avida's 77 logic tasks, which between
      them accept exactly these 251 of the 256; checked from Avida's source in S118) is paid the same: at most a doubling of the program's processor-time share,
      once per copy. Each task draws its pay from its own resource that runs down when many programs use it (inflow,
      outflow and draw exactly as S113's COMMON TASKS PAY LESS), so whichever function is rare pays more than whichever
      is common. The environment never says which function is wanted.

  SOLVE SOMETHING TO REPLICATE, NOTHING PAID ("must_solve"): the same 77 tasks are listed, none paid (value 0, which
      changes nothing). From update 5,000 on (Avida's own SetConfig event), a program can complete a copy of itself
      only if, during that copy, it performed at least one of them (Avida's REQUIRE_SINGLE_REACTION 1). Before 5,000
      the run is S113's NO TASK REWARDS exactly (same list, same values). The environment never says which function is required.

Everything else is S113's: Avida's default ancestor (S111's default-heads.org, which performs no task), S111's avida.cfg
and instruction set, 60 x 60 world, copy error 0.0075 per copied instruction. Unlike S113 (pieces of 1,000 updates with
a save and reload between them), each run here is ONE continuous Avida process of 20,000 updates (no reload, so the
counting fault S113 found after a reload cannot occur). The Avida seed of seed k is 1000 k, the seed of S113's first
piece of seed k. Avida prints which tasks each program performed and the program count every 250 updates, the resource
levels every 1,000, and saves the whole program population every 5,000.

Every Avida process runs under nice -n 19 and a timeout; at most three at once. Raw output stays in the scratch space
(s118/runs/<pilot>_seed<k>/), never in git. Avida's programs copy themselves only inside Avida's simulated processor;
nothing here copies itself on the real machine.

Use: python3 s118_run_the_two_pilots.py test <pilot> <updates> [switch-on update]
         (a timing and mechanics test, seed 99, in s118/test/ or s118/test_switch<update>/)
     python3 s118_run_the_two_pilots.py                           (the six pilot runs: 2 pilots x seeds 1, 2, 3)
Written 1 October 2026 by the one Opus 5.5 agent of log S118.
"""
import json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
OUT = SCRATCH + '/s118/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(os.path.dirname(HERE), 'results')
S111CONF = os.path.join(RESULTS, 'S111 Avida - the runs', 'configuration')
RANKS = os.path.join(RESULTS, 'S113 Which execution environments learn - the runs',
                     'the 77 tasks ranked by the fewest nand steps.json')

UPDATES = 20000
SWITCH_ON = 5000          # must_solve: the update from which a copy needs at least one performed task
SEEDS = [1, 2, 3]
PILOTS = ['any_function', 'must_solve']
RUN_TIMEOUT = 7200        # seconds per Avida process
TWO = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']


def task_list():
    """S113's 77 tasks in S113's order (so the task columns match S113's). Echo is left out (decided after the
    mechanics test, before the plan: see the plan, section 3)."""
    rows = json.load(open(RANKS))['tasks']
    return [r['task'] for r in rows]


def reaction_name(task):
    if task == 'echo':
        return 'ECHO'
    return task.upper() if task in TWO else 'LOG3' + task[-2:].upper()


def environment_text(pilot):
    tasks = task_list()
    lines = ['# S118 pilot %s: written by tools/s118_run_the_two_pilots.py' % pilot]
    if pilot == 'any_function':
        for t in tasks:
            lines.append('RESOURCE res%s:inflow=100:outflow=0.01' % reaction_name(t))
        for t in tasks:
            lines.append('REACTION %s %s process:resource=res%s:value=1.0:type=pow:frac=0.0025:max=1.0 '
                         'requisite:max_count=1' % (reaction_name(t), t, reaction_name(t)))
    elif pilot == 'must_solve':
        for t in tasks:
            lines.append('REACTION %s %s process:value=0.0:type=pow requisite:max_count=1' % (reaction_name(t), t))
    else:
        raise ValueError(pilot)
    return '\n'.join(lines) + '\n'


def events_text(pilot, updates, switch_on=SWITCH_ON):
    ev = ['u begin Inject default-heads.org',
          'u 0:250:end PrintTasksData',
          'u 0:250:end PrintCountData',
          'u 0:1000:end PrintAverageData',
          'u 0:1000:end PrintResourceData',
          'u 5000:5000:end SavePopulation']
    if pilot == 'must_solve' and updates > switch_on:
        ev.append('u %d SetConfig REQUIRE_SINGLE_REACTION 1' % switch_on)
    ev.append('u %d SavePopulation' % updates)
    ev.append('u %d Exit' % updates)
    return '\n'.join(ev) + '\n'


def run_one(pilot, seed, updates=UPDATES, out=OUT, switch_on=SWITCH_ON):
    run_dir = os.path.join(out, '%s_seed%d' % (pilot, seed))
    if os.path.exists(os.path.join(run_dir, 'finished.json')):
        return True
    if os.path.exists(run_dir):
        shutil.rmtree(run_dir)     # a run that did not finish is run again from its start
    os.makedirs(run_dir)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(S111CONF, f), run_dir)
    open(os.path.join(run_dir, 'environment.cfg'), 'w').write(environment_text(pilot))
    open(os.path.join(run_dir, 'events.cfg'), 'w').write(events_text(pilot, updates, switch_on))
    argv = ['nice', '-n', '19', 'timeout', str(RUN_TIMEOUT), AVIDA, '-s', str(seed * 1000),
            '-set', 'VERBOSITY', '0', '-set', 'COPY_MUT_PROB', '0.0075']
    t0 = time.time()
    c0 = os.times()
    rc = subprocess.run(argv, cwd=run_dir, stdout=open(os.path.join(run_dir, 'avida.log'), 'w'),
                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    c1 = os.times()
    rec = {'pilot': pilot, 'seed': seed, 'avida_seed': seed * 1000, 'updates': updates, 'exit': rc,
           'wall_seconds': round(time.time() - t0, 1),
           'cpu_seconds': round((c1.children_user - c0.children_user) + (c1.children_system - c0.children_system), 1),
           'command': 'cd "%s" && %s' % (run_dir, ' '.join(argv))}
    json.dump(rec, open(os.path.join(run_dir, 'finished.json' if rc == 0 else 'failed.json'), 'w'), indent=1)
    return rc == 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        pilot = sys.argv[2]
        updates = int(sys.argv[3])
        switch_on = int(sys.argv[4]) if len(sys.argv) > 4 else SWITCH_ON
        out = SCRATCH + '/s118/test' + ('_switch%d' % switch_on if len(sys.argv) > 4 else '')
        print(run_one(pilot, 99, updates=updates, out=out, switch_on=switch_on))
        return
    jobs = [(p, s) for s in SEEDS for p in PILOTS]
    if len(sys.argv) > 1:
        wanted = sys.argv[1].split(',')
        jobs = [(p, s) for p, s in jobs if '%s_seed%d' % (p, s) in wanted or p in wanted]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for (p, s), ok in zip(jobs, pool.map(lambda j: run_one(*j), jobs)):
            print(p, s, 'finished' if ok else 'FAILED', time.strftime('%H:%M:%S'), flush=True)


if __name__ == '__main__':
    main()
