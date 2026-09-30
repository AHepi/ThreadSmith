#!/usr/bin/env python3
"""s114_restart_audit_run_the_pieces_and_the_continuous_runs.py

What it does, in plain words: log S114's restart audit. S113 runs Avida (the evolutionary-computation simulator built
in log S111) in pieces of 1,000 updates: at the end of each piece the program population is saved, and the next piece
is a new Avida process that loads it. This script asks whether that saving and reloading changes what happens, by
running the same Avida execution environment two ways, from the same Avida program and with the same settings:

  - in pieces, by S113's own runner (tools/s113_run_the_avida_execution_environments.py, its function run_one, imported
    and called unchanged, so the save and reload steps are S113's exact ones, not a copy of them);
  - in one continuous Avida process, with the same environment file, the same settings, the same printing every 250
    updates and the resource levels printed every update.

Two of S113's execution environments are used: FIXED GRADED (the nine two-input tasks rewarded, all 77 listed) and
COMMON TASKS PAY LESS (the nine rewarded through resources that run down). Three seeds each (11401, 11402, 11403;
Avida seed = 1000 x seed + piece, as S113), 10 pieces = 10,000 updates. The continuous run uses the seed of the first
piece, so its first 1,000 updates should match the first piece exactly (a check that the extra printing changes
nothing).

It also runs, first, three short checks of GPT 6 Astra's native examples (log S114): its restart-audit event files
(Avida's own actions, with SavePopulation's colon-separated arguments), its native analysis commands (LOAD, FILTER,
RECALCULATE with three manual inputs, DETAIL) and whether Avida refuses an event file with an action it does not know
(Astra's S114... actions). And, after the pieces of COMMON TASKS PAY LESS seed 11401, a rerun of its sixth piece from the
same saved program population with the resource levels printed every update from update 0, to see the levels just after
the reload, and to check that the rerun repeats the original piece exactly.

While S113's runner (process 2411) is alive, at most one Avida process of this script runs at a time; after it has
ended, at most three. Every Avida process runs under a timeout. Raw output stays in the scratch space
(s114_restart_audit/). Avida's programs copy themselves only inside Avida's simulated processor; nothing here copies
itself on the real machine. Written 30 September 2026 by the one Opus 5.5 agent of log S114.
"""
import importlib.util, os, shutil, subprocess, sys, threading, time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('s113', os.path.join(HERE, 's113_run_the_avida_execution_environments.py'))
s113 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s113)

SCRATCH = s113.SCRATCH
AVIDA = s113.AVIDA
AUDIT = SCRATCH + '/s114_restart_audit'
PIECES_OUT = AUDIT + '/runs/pieces'
CONT_OUT = AUDIT + '/runs/continuous'
CHECKS = AUDIT + '/checks'
S113_PID = 2411
ENVS = ['fixed_graded', 'common_pays_less']
SEEDS = [11401, 11402, 11403]
PIECES = 10
UPDATES = PIECES * s113.PIECE
CONT_TIMEOUT = 5400
LOG = AUDIT + '/driver.log'
lock = threading.Lock()


def log(msg):
    with lock:
        with open(LOG, 'a') as f:
            f.write(time.strftime('%H:%M:%S ') + msg + '\n')


def s113_alive():
    try:
        os.kill(S113_PID, 0)
        cmd = open('/proc/%d/cmdline' % S113_PID).read()
        return 's113_run' in cmd
    except (OSError, IOError):
        return False


def run_avida(argv, cwd, out_name='avida.log', timeout=900):
    t0 = time.time()
    rc = subprocess.run(['timeout', str(timeout)] + argv, cwd=cwd, stdout=open(os.path.join(cwd, out_name), 'w'),
                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    log('exit %d after %.0f s: cd "%s" && timeout %d %s' % (rc, time.time() - t0, cwd, timeout, ' '.join(argv)))
    return rc


def continuous_events():
    return '\n'.join([
        'u begin Inject default-heads.org',
        'u 250:250:%d PrintTasksData' % UPDATES,
        'u 250:250:%d PrintCountData' % UPDATES,
        'u 1000:1000:%d PrintAverageData' % UPDATES,
        'u 1000:1000:%d PrintDominantData' % UPDATES,
        'u 0:1:%d PrintResourceData' % UPDATES,
        'u 1000:1000:%d SavePopulation' % UPDATES,
        'u %d Exit' % UPDATES]) + '\n'


def job_continuous(env, seed):
    d = os.path.join(CONT_OUT, '%s_seed%d' % (env, seed))
    if os.path.exists(os.path.join(d, 'data', 'detail-%d.spop' % UPDATES)):
        return True
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(s113.S111CONF, f), d)
    with open(os.path.join(d, 'environment.cfg'), 'w') as f:
        f.write(s113.environment_text(env, s113.load_ranks(), 1, None))
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write(continuous_events())
    rc = run_avida([AVIDA, '-s', str(seed * 1000), '-set', 'VERBOSITY', '0', '-set', 'COPY_MUT_PROB', '0.0075'], d,
                   timeout=CONT_TIMEOUT)
    # keep only the saved program populations at 5,000 and 10,000 updates
    for u in range(1000, UPDATES + 1, 1000):
        p = os.path.join(d, 'data', 'detail-%d.spop' % u)
        if u not in (5000, UPDATES) and os.path.exists(p):
            os.remove(p)
    return rc == 0


def job_pieces(env, seed):
    ok = s113.run_one(env, seed, pieces=PIECES, out=PIECES_OUT)
    log('pieces %s seed %d: %s' % (env, seed, 'finished' if ok else 'FAILED'))
    return ok


def job_reload_resource_check():
    """Rerun piece 5 (updates 5,000-6,000) of COMMON TASKS PAY LESS seed 11401 from the same saved program population,
    with the resource levels printed every update for the first 20 updates besides the original printing."""
    src = os.path.join(PIECES_OUT, 'common_pays_less_seed11401')
    d = os.path.join(CHECKS, 'reload_resource_check')
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org', 'environment.cfg']:
        shutil.copy(os.path.join(src, 'piece_05', f), d)
    shutil.copy(os.path.join(src, 'piece_04', 'data', 'detail-1000.spop'), os.path.join(d, 'start.spop'))
    ev = open(os.path.join(src, 'piece_05', 'events.cfg')).read()
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write(ev + 'u 0:1:20 PrintResourceData\n')
    rc = run_avida([AVIDA, '-s', str(11401 * 1000 + 5), '-set', 'VERBOSITY', '0', '-set', 'COPY_MUT_PROB', '0.0075'], d)
    return rc == 0


ASTRA_ENV = """REACTION NOT not process:value=1:type=pow requisite:max_count=1
REACTION NAND nand process:value=1:type=pow requisite:max_count=1
REACTION AND and process:value=2:type=pow requisite:max_count=1
REACTION ORN orn process:value=2:type=pow requisite:max_count=1
REACTION OR or process:value=3:type=pow requisite:max_count=1
REACTION ANDN andn process:value=3:type=pow requisite:max_count=1
REACTION NOR nor process:value=4:type=pow requisite:max_count=1
REACTION XOR xor process:value=4:type=pow requisite:max_count=1
REACTION EQU equ process:value=5:type=pow requisite:max_count=1
"""
ASTRA_FIRST = """u begin Inject default-heads.org
u 0:100:1000 PrintAverageData
u 0:100:1000 PrintCountData
u 0:100:1000 PrintTasksData
u 0:100:1000 PrintTimeData
u 0:1000:1000 SavePopulation filename=detail:save_historic=0
u 1000 Exit
"""
ASTRA_NEXT = ASTRA_FIRST.replace('u begin Inject default-heads.org', 'u begin LoadPopulation previous.spop')
ASTRA_PROBE_ENV = ''.join('REACTION %s %s process:value=0:type=pow requisite:max_count=1\n' % (t.upper(), t)
                          for t in s113.TWO)
ASTRA_ANALYZE = """LOAD data/detail-1000.spop
FILTER num_cpus > 0
RECALCULATE 0 -1 0 252908703 856220990 1431655765
DETAIL probe-000.dat id num_cpus viable length task_list
"""
ASTRA_B1_EVENTS = """u begin S114BountyInit
u begin Inject default-heads.org
u 0:100:50000 PrintAverageData
u 1000:1000:49000 S114BountyStep
u 50000 S114BountyFinish
u 50000 Exit
"""


def job_astra_examples():
    """Astra's native restart-audit files (first segment, then one reloaded segment), its native analysis example on the
    reloaded segment's saved program population, and its B1 event file with the unknown S114 actions."""
    base = os.path.join(CHECKS, 'astra_native_examples')
    if os.path.exists(base):
        shutil.rmtree(base)
    res = {}
    for seg, events in [('segment_0', ASTRA_FIRST), ('segment_1', ASTRA_NEXT)]:
        d = os.path.join(base, seg)
        os.makedirs(d)
        for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
            shutil.copy(os.path.join(s113.S111CONF, f), d)
        open(os.path.join(d, 'environment.cfg'), 'w').write(ASTRA_ENV)
        open(os.path.join(d, 'events.cfg'), 'w').write(events)
        if seg == 'segment_1':
            shutil.copy(os.path.join(base, 'segment_0', 'data', 'detail-1000.spop'), os.path.join(d, 'previous.spop'))
        seed = 11401 + (100000 if seg == 'segment_1' else 0)
        res[seg] = run_avida([AVIDA, '-s', str(seed), '-set', 'VERBOSITY', '0'], d)
    d = os.path.join(base, 'segment_1')
    open(os.path.join(d, 'probe_environment.cfg'), 'w').write(ASTRA_PROBE_ENV)
    open(os.path.join(d, 'analyze.cfg'), 'w').write(ASTRA_ANALYZE)
    res['analyze'] = run_avida([AVIDA, '-a', '-c', 'avida.cfg', '-set', 'ENVIRONMENT_FILE', 'probe_environment.cfg',
                                '-set', 'ANALYZE_FILE', 'analyze.cfg'], d, out_name='analyze.log', timeout=600)
    d = os.path.join(base, 'unknown_action')
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(s113.S111CONF, f), d)
    open(os.path.join(d, 'environment.cfg'), 'w').write(ASTRA_ENV)
    open(os.path.join(d, 'events.cfg'), 'w').write(ASTRA_B1_EVENTS)
    res['unknown_action'] = run_avida([AVIDA, '-s', '11411', '-set', 'VERBOSITY', '1'], d, timeout=120)
    log('astra examples exit codes: %s' % res)
    return True


def main():
    os.makedirs(AUDIT, exist_ok=True)
    jobs = [('astra', job_astra_examples, ())]
    for seed in SEEDS:
        for env in ENVS:
            jobs.append(('pieces %s %d' % (env, seed), job_pieces, (env, seed)))
            jobs.append(('continuous %s %d' % (env, seed), job_continuous, (env, seed)))
            if env == 'common_pays_less' and seed == 11401:
                jobs.append(('reload resource check', job_reload_resource_check, ()))
    running = []
    log('driver started; S113 alive: %s' % s113_alive())
    for name, fn, args in jobs:
        while True:
            running = [t for t in running if t.is_alive()]
            limit = 1 if s113_alive() else 3
            # the reload check needs its pieces finished first
            if name == 'reload resource check' and any(t.name == 'pieces common_pays_less 11401' for t in running):
                time.sleep(20)
                continue
            if len(running) < limit:
                break
            time.sleep(20)
        log('start: ' + name)
        t = threading.Thread(target=lambda fn=fn, args=args, name=name: log('done: %s -> %s' % (name, fn(*args))),
                             name=name)
        t.start()
        running.append(t)
    for t in running:
        t.join()
    log('driver finished')


if __name__ == '__main__':
    main()
