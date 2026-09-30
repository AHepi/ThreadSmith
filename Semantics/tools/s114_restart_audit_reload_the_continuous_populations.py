#!/usr/bin/env python3
"""s114_restart_audit_reload_the_continuous_populations.py

What it does, in plain words: a follow-up check of log S114's restart audit, added after the first results were seen
(so it is a departure from the plan, recorded as such). In the audit, the runs made in pieces had about twice as many
program replications per update as the continuous runs, from the second piece on. Two explanations compete: the
program populations of the two ways evolved differently (evolution), or the reload itself makes the same programs
replicate faster (the reload). This check separates them: it takes the program population the continuous run saved
at update 5,000, and loads it into a new Avida process exactly as S113's runner loads a piece (S113's own environment
and event text, from tools/s113_run_the_avida_execution_environments.py, imported unchanged; for COMMON TASKS PAY LESS
the resource levels the continuous run printed at update 5,000 are carried over as S113's runner would), and runs
1,000 updates with the program count and births printed every update. If births jump at once after the load, the reload
itself does it; if they stay as in the continuous run's updates 5,000 to 6,000, it was evolution.

One Avida process at a time while S113's runner (process 2411) is alive; every process under a 900-second timeout; raw
output in the scratch space (s114_restart_audit/checks/reload_the_continuous_population/). Avida's programs copy
themselves only inside Avida's simulated processor. Written 30 September 2026 by the one Opus 5.5 agent of log S114.
"""
import importlib.util, os, shutil, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('s113', os.path.join(HERE, 's113_run_the_avida_execution_environments.py'))
s113 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s113)

AUDIT = s113.SCRATCH + '/s114_restart_audit'
CONT = AUDIT + '/runs/continuous'
OUT = AUDIT + '/checks/reload_the_continuous_population'
AT = 5000


def resource_levels(env, seed):
    path = os.path.join(CONT, '%s_seed%d' % (env, seed), 'data', 'resource.dat')
    names = [l.split(':', 1)[1].strip() for l in open(path)
             if l.startswith('#') and ':' in l and l[1:].strip()[:1].isdigit()][1:]
    for line in open(path):
        if line.strip() and not line.startswith('#') and int(float(line.split()[0])) == AT:
            return dict(zip(names, [float(x) for x in line.split()[1:]]))


def run(env, seed):
    d = os.path.join(OUT, '%s_seed%d' % (env, seed))
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(s113.S111CONF, f), d)
    res = resource_levels(env, seed) if env == 'common_pays_less' else None
    open(os.path.join(d, 'environment.cfg'), 'w').write(s113.environment_text(env, s113.load_ranks(), 1, res))
    open(os.path.join(d, 'events.cfg'), 'w').write(
        s113.events_text(False) + 'u 0:1:1000 PrintCountData\nu 0:50:1000 PrintAverageData\n')
    shutil.copy(os.path.join(CONT, '%s_seed%d' % (env, seed), 'data', 'detail-%d.spop' % AT), os.path.join(d, 'start.spop'))
    argv = ['timeout', '900', s113.AVIDA, '-s', str(seed * 1000 + 5), '-set', 'VERBOSITY', '0',
            '-set', 'COPY_MUT_PROB', '0.0075']
    t0 = time.time()
    rc = subprocess.run(argv, cwd=d, stdout=open(os.path.join(d, 'avida.log'), 'w'), stderr=subprocess.STDOUT,
                        stdin=subprocess.DEVNULL).returncode
    with open(os.path.join(OUT, 'commands.log'), 'a') as f:
        f.write('exit %d after %.0f s: cd "%s" && %s\n' % (rc, time.time() - t0, d, ' '.join(argv)))
    return rc


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for env in sys.argv[1].split(','):
        for seed in [int(x) for x in sys.argv[2].split(',')]:
            print(env, seed, run(env, seed), flush=True)
