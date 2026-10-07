#!/usr/bin/env python3
"""s128_confirm_the_store_equation.py

What it does, in plain words (log S128, decision S82): one short run of stock Avida to see whether the stores of S113's
COMMON TASKS PAY LESS execution environment fill and drain along the curve that Avida's own code gives, which is the
same curve as the "fading trace" of the owner's report on temporal computation in neurons.

The rule read from Avida's code (commit 47f13dad; `avida-core/source/main/cResourceCount.cc` lines 35-37, 336-343,
814-825; `cPopulation.cc` line 443; `targets/avida/Avida2Driver.cc` lines 107-114): a global store with inflow I and
outflow o is advanced in tiny steps of 1/10,000 of an update; in each step the store is multiplied by (1 - o)^(1/10,000)
and I/10,000 is added. Time advances only while programs run (one share of an update per executed instruction; with no
program in the world the store does not move at all). So, between task performances, over t updates:
    R(t) = R* + (R(0) - R*) * exp(-k t),   k = -ln(1 - o),   R* = I / k        (continuous form)
    exactly, per whole update:  R <- R*(1-o) + I*D*(1-(1-o))/(1-(1-o)^D),  D = 1/10,000 (the step form)
For S113's stores (I = 100, o = 0.01): k = 0.0100503, time constant 1/k = 99.50 updates, R* = 9,949.8 (step form
9,949.8 as well, to 0.01). The rival rule a reader might assume, R <- 0.99 R + 100 once per update, has R* = 10,000.

WRITTEN BEFORE RUNNING (S128; this docstring is committed before the run):
- The run: stock Avida 47f13dad (the S113/S126 binary), S111's avida.cfg, instruction set and ancestor, S113's
  environment text for COMMON TASKS PAY LESS made by S113's own function, with only the stores' starting levels set:
  NOT 290 (about where S126 found it), NAND 0, AND 400 (the full-pay threshold), ORN 4,300 (about S126's peak),
  OR 9,949.75 (at R*), ANDN 20,000 (above), NOR 1,000, XOR 5,000, EQU 10,000 (the rival rule's resting level).
  One program, the default ancestor, which performs no logic task, injected at the start; copy errors as S113 (0.0075);
  seed 128; 50 updates; every store and every task count printed at every update; under timeout and nice -n 19.
- What counts as confirming: no task performed in the 50 updates (tasks.dat all zero); and every store at every
  printed update within 0.05 of the step form's prediction, with the time offset (print label u = u or u+1 updates
  elapsed) fixed once for all stores by the first row. In particular EQU must fall from 10,000 toward 9,949.8
  (to about 9,980 after 50 updates) and OR stay at 9,949.75.
- What counts against: any store more than 1 away from the prediction with no task performed; EQU staying at 10,000;
  or stores moving in proportion to elapsed time in a way neither form gives.
- If a task is performed, that task's store is reported apart and not used for the verdict.

Raw output stays in the scratch space (s128/run/). Nothing here copies itself on the real machine.
Usage: python3 s128_confirm_the_store_equation.py run      (prepare and run Avida once)
       python3 s128_confirm_the_store_equation.py read     (compare with the predictions; writes the .json)
Written 2 October 2026 by the one Opus 5.5 agent of log S128.
"""
import json, math, os, shutil, subprocess, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as S113  # noqa: E402  (its environment text and the task ranks)

SCRATCH = S113.SCRATCH
AVIDA = S113.AVIDA
RUN = os.path.join(SCRATCH, 's128', 'run')
CONF = S113.S111CONF
RESULTS = os.path.join(os.path.dirname(HERE), 'results')
OUTJSON = os.path.join(RESULTS, 'S128 The neuron mathematics against the semantics\' kernel - the confirming run.json')

START = {'resNOT': 290.0, 'resNAND': 0.0, 'resAND': 400.0, 'resORN': 4300.0, 'resOR': 9949.75,
         'resANDN': 20000.0, 'resNOR': 1000.0, 'resXOR': 5000.0, 'resEQU': 10000.0}
INFLOW, OUTFLOW = 100.0, 0.01
UPDATES = 50
SEED = 128


def prepare_and_run():
    if os.path.exists(RUN):
        shutil.rmtree(RUN)
    os.makedirs(RUN)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(CONF, f), RUN)
    ranks = S113.load_ranks()
    with open(os.path.join(RUN, 'environment.cfg'), 'w') as f:
        f.write(S113.environment_text('common_pays_less', ranks, resources=START))
    ev = ['u begin Inject default-heads.org',
          'u 0:1:%d PrintResourceData' % UPDATES,
          'u 0:1:%d PrintTasksData' % UPDATES,
          'u 0:1:%d PrintCountData' % UPDATES,
          'u %d Exit' % UPDATES]
    with open(os.path.join(RUN, 'events.cfg'), 'w') as f:
        f.write('\n'.join(ev) + '\n')
    argv = ['timeout', '600', 'nice', '-n', '19', AVIDA, '-s', str(SEED), '-set', 'VERBOSITY', '0',
            '-set', 'COPY_MUT_PROB', '0.0075']
    rc = subprocess.run(argv, cwd=RUN, stdout=open(os.path.join(RUN, 'avida.log'), 'w'),
                        stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    print('exit', rc)
    return rc


def read_cols(path):
    names, rows = [], []
    for line in open(path):
        if line.startswith('#'):
            s = line[1:].strip()
            if s[:1].isdigit() and ':' in s:
                names.append(s.split(':', 1)[1].strip())
            continue
        if line.strip():
            rows.append([float(x) for x in line.split()])
    return names, rows


def step_form(r0, n_updates):
    """Avida's rule, one whole update at a time: 10,000 steps of x*(1-o)^D + I*D, D = 1/10,000."""
    D = 1.0 / 10000.0
    sd = (1.0 - OUTFLOW) ** D
    per_update_inflow = INFLOW * D * (1.0 - sd ** 10000) / (1.0 - sd)
    out, r = [r0], r0
    for _ in range(n_updates):
        r = r * sd ** 10000 + per_update_inflow
        out.append(r)
    return out


def continuous(r0, t):
    k = -math.log(1.0 - OUTFLOW)
    rs = INFLOW / k
    return rs + (r0 - rs) * math.exp(-k * t)


def rival(r0, t):
    r = r0
    for _ in range(t):
        r = r * (1.0 - OUTFLOW) + INFLOW
    return r


def read():
    names, rows = read_cols(os.path.join(RUN, 'data', 'resource.dat'))
    tnames, trows = read_cols(os.path.join(RUN, 'data', 'tasks.dat'))
    cnames, crows = read_cols(os.path.join(RUN, 'data', 'count.dat'))
    res_names = names[1:]
    tasks_done = sum(sum(r[1:]) for r in trows)
    k = -math.log(1.0 - OUTFLOW)
    out = {'about': 'log S128: one stock Avida run of S113 COMMON TASKS PAY LESS stores from chosen starting levels, '
                    'no task performed; compared with the update rule read from Avida\'s code',
           'binary_sha256': hashlib.sha256(open(AVIDA, 'rb').read()).hexdigest(),
           'inflow': INFLOW, 'outflow': OUTFLOW, 'k': k, 'time_constant_updates': 1.0 / k,
           'half_life_updates': math.log(2) / k, 'fixed_point_continuous': INFLOW / k,
           'fixed_point_step_form': None, 'fixed_point_rival': INFLOW / OUTFLOW,
           'tasks_performed_in_run': tasks_done,
           'programs_at_labels': {int(r[0]): r[2] for r in crows},
           'stores': {}}
    D = 1.0 / 10000.0
    sd = (1.0 - OUTFLOW) ** D
    out['fixed_point_step_form'] = INFLOW * D / (1.0 - sd)
    # fix the time offset from the first printed row: label u means u + off updates elapsed
    best = None
    for off in (0, 1):
        err = max(abs(rows[0][i + 1] - step_form(START[n], off)[off]) for i, n in enumerate(res_names))
        if best is None or err < best[1]:
            best = (off, err)
    off = best[0]
    out['offset_label_to_updates_elapsed'] = off
    worst = 0.0
    for i, n in enumerate(res_names):
        pred = step_form(START[n], UPDATES + 2)
        series = []
        for r in rows:
            u = int(r[0])
            t = u + off
            obs = r[i + 1]
            p = pred[t]
            series.append({'label': u, 'updates_elapsed': t, 'observed': obs, 'step_form': p,
                           'continuous': continuous(START[n], t), 'rival': rival(START[n], t),
                           'diff_step': obs - p})
            worst = max(worst, abs(obs - p))
        out['stores'][n] = {'start': START[n], 'series': series,
                            'max_abs_diff_step_form': max(abs(s['diff_step']) for s in series),
                            'max_abs_diff_continuous': max(abs(s['observed'] - s['continuous']) for s in series),
                            'max_abs_diff_rival': max(abs(s['observed'] - s['rival']) for s in series)}
    out['max_abs_diff_step_form_all_stores'] = worst
    out['verdict_as_written_before_running'] = ('confirming' if (tasks_done == 0 and worst <= 0.05) else
                                                'against' if (tasks_done == 0 and worst > 1.0) else 'neither')
    json.dump(out, open(OUTJSON, 'w'), indent=1)
    print('offset', off, 'tasks performed', tasks_done, 'worst |obs - step form|', worst)
    print('time constant %.3f updates, half-life %.3f, R* continuous %.4f, step form %.4f, rival %.1f'
          % (1 / k, math.log(2) / k, INFLOW / k, out['fixed_point_step_form'], INFLOW / OUTFLOW))
    for n in res_names:
        s = out['stores'][n]
        ser = s['series']
        pick = [x for x in ser if x['label'] in (0, 9, 24, 49, 50)]
        print(n, 'start', s['start'], ' | '.join('L%d obs %.4f step %.4f cont %.4f rival %.4f'
              % (x['label'], x['observed'], x['step_form'], x['continuous'], x['rival']) for x in pick),
              'max|d| step %.5f cont %.5f rival %.3f' % (s['max_abs_diff_step_form'], s['max_abs_diff_continuous'],
                                                       s['max_abs_diff_rival']))
    print('programs', out['programs_at_labels'])
    print('verdict', out['verdict_as_written_before_running'])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        sys.exit(0 if prepare_and_run() == 0 else 1)
    elif len(sys.argv) > 1 and sys.argv[1] == 'read':
        read()
    else:
        print(__doc__)
