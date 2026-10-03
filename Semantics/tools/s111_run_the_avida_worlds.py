#!/usr/bin/env python3
"""s111_run_the_avida_worlds.py

What it does, in plain words: sets up and runs Avida's simulated worlds for log S111 (decision S59). Each world gets its
own folder in the scratch space, holding a copy of Avida's default configuration files from
"Semantics/results/S111 Avida - the runs/configuration/", an events file written here, and Avida's output. Avida is
started with only the copy error rate, the seed and (for the controls) a few named settings changed on its command line.
Every run is under a time limit, at most three run at once, and nothing is written into the repository.

  python3 Semantics/tools/s111_run_the_avida_worlds.py main       the nine main runs (3 error rates x 3 seeds, 50,000 updates)
  python3 Semantics/tools/s111_run_the_avida_worlds.py controls   the control worlds K1 to K5 of the plan
  python3 Semantics/tools/s111_run_the_avida_worlds.py --print    print the exact commands and write nothing

Written 29 September 2026 by the one Opus 5.5 agent of log S111. The plan it follows is
"Semantics/results/S111 Avida - how the three properties will be measured, written before running.md".
"""
import os, random, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
OUT = SCRATCH + '/s111/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs', 'configuration')
JOBS = 3
RATES = {'low': 0.0025, 'default': 0.0075, 'high': 0.02}
SEEDS = [1, 2, 3]
UPDATES = 50000
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NAMES = ['nop-A', 'nop-B', 'nop-C', 'if-n-equ', 'if-less', 'if-label', 'mov-head', 'jmp-head', 'get-head', 'set-flow',
         'shift-r', 'shift-l', 'inc', 'dec', 'push', 'pop', 'swap-stk', 'swap', 'add', 'sub', 'nand', 'h-copy', 'h-alloc',
         'h-divide', 'IO', 'h-search']

MAIN_EVENTS = """u begin Inject default-heads.org
u 0:1000:end PrintCountData
u 0:1000:end PrintTimeData
u 0:1000:end PrintTasksData
u 0:1000:end PrintDominantData
u 0:1000:end PrintAverageData
u 1000 SavePopulation
u 10000:10000:end SavePopulation
u {end} Exit
"""


def ancestor_letters():
    seq = []
    for line in open(os.path.join(CONF, 'default-heads.org')):
        w = line.split('#')[0].split()
        if w:
            seq.append(LETTERS[NAMES.index(w[0])])
    return ''.join(seq)


def write_org(path, letters, with_null=False):
    names = NAMES + ['nop-X']
    alpha = LETTERS + 'A'
    with open(path, 'w') as f:
        f.write('#inst_set heads_default\n#hw_type 0\n\n')
        for ch in letters:
            f.write(names[alpha.index(ch)] + '\n')


def setup(run, events, instset_extra=False):
    d = os.path.join(OUT, run)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(CONF, f), d)
    if instset_extra:   # the controls and the analysis add nop-X as a 27th instruction (letter A); the main runs never do
        with open(os.path.join(d, 'instset-heads.cfg'), 'a') as f:
            f.write('\nINST nop-X         # A (added for log S111 controls: a knockout that does nothing and is no label)\n')
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write(events)
    return d


def command(seed, sets):
    argv = [AVIDA, '-s', str(seed), '-set', 'VERBOSITY', '0']
    for k, v in sets:
        argv += ['-set', k, str(v)]
    return argv


def run(job):
    name, d, argv, limit = job
    t0 = time.time()
    with open(os.path.join(d, 'avida.log'), 'w') as log:
        rc = subprocess.run(['timeout', str(limit)] + argv, cwd=d, stdout=log, stderr=subprocess.STDOUT,
                            stdin=subprocess.DEVNULL).returncode
    secs = time.time() - t0
    with open(os.path.join(d, 'exit.txt'), 'w') as f:
        f.write('exit %d seconds %.0f\n' % (rc, secs))
    print('%s: exit %d after %.0f s' % (name, rc, secs), flush=True)
    return name, rc, secs


def main_jobs(dry):
    jobs = []
    for cond, rate in RATES.items():
        for seed in SEEDS:
            name = 'main_%s_seed%d' % (cond, seed)
            d = os.path.join(OUT, name) if dry else setup(name, MAIN_EVENTS.format(end=UPDATES))
            jobs.append((name, d, command(seed, [('COPY_MUT_PROB', rate)]), 7200))
    return jobs


def control_jobs(dry):
    anc = ancestor_letters()
    ko = anc[:anc.rindex('v')] + 'A' + anc[anc.rindex('v') + 1:]   # h-copy of the copy loop replaced by nop-X
    rng = random.Random(111)
    jobs = []
    follow = "u 0:1:end PrintCountData\nu 0:500:end SavePopulation\nu {end} Exit\n"
    # K1: 100 random programs of length 100, one per cell
    name = 'control_K1_random_programs'
    ev = ''.join('u begin Inject random_%03d.org %d\n' % (i, i * 36) for i in range(100)) + follow.format(end=2000)
    if not dry:
        d = setup(name, ev, instset_extra=True)
        for i in range(100):
            write_org(os.path.join(d, 'random_%03d.org' % i), ''.join(rng.choice(LETTERS) for _ in range(100)))
    jobs.append((name, os.path.join(OUT, name), command(1, []), 1800))
    # K2: the knocked-out ancestor alone
    for name, ev, sets in [
            ('control_K2_copy_loop_knocked_out', 'u begin Inject knocked_out.org\n' + follow.format(end=2000), []),
            ('control_K3_knocked_out_nothing_dies_of_age', 'u begin Inject knocked_out.org\n' + follow.format(end=2000),
             [('DEATH_METHOD', 0)]),
            ('control_K4_knocked_out_beside_ancestor_nothing_dies_of_age',
             'u begin Inject knocked_out.org 0\nu begin Inject default-heads.org 1\n' + follow.format(end=2000),
             [('DEATH_METHOD', 0)])]:
        if not dry:
            d = setup(name, ev, instset_extra=True)
            write_org(os.path.join(d, 'knocked_out.org'), ko)
        jobs.append((name, os.path.join(OUT, name), command(1, sets), 1800))
    # K5: no mutation at all
    name = 'control_K5_no_mutation'
    ev = MAIN_EVENTS.replace('u 10000:10000:end SavePopulation\n', 'u 5000 SavePopulation\n').format(end=5000)
    if not dry:
        setup(name, ev)
    jobs.append((name, os.path.join(OUT, name), command(1, [('COPY_MUT_PROB', 0), ('DIVIDE_INS_PROB', 0),
                                                             ('DIVIDE_DEL_PROB', 0)]), 1800))
    return jobs


def main():
    a = sys.argv[1:]
    dry = '--print' in a
    which = [x for x in a if x != '--print']
    if not which or not set(which) <= {'main', 'controls'}:
        raise SystemExit('usage: s111_run_the_avida_worlds.py main|controls [--print]')
    jobs = []
    if 'controls' in which:
        jobs += control_jobs(dry)
    if 'main' in which:
        jobs += main_jobs(dry)
    for name, d, argv, limit in jobs:
        print('%s: cd "%s" && timeout %d %s' % (name, d, limit, ' '.join(argv)))
    if dry:
        return
    with ThreadPoolExecutor(JOBS) as ex:
        list(ex.map(run, jobs))


if __name__ == '__main__':
    main()
