#!/usr/bin/env python3
"""s126_run_the_arms.py

What it does, in plain words: for log S126 (the closing knock-out test), prepares and runs the arms of the test on the
two saved program populations of S113's COMMON TASKS PAY LESS execution environment (seeds 1 and 2, at 50,000
updates). Every arm is one Avida process that reloads a saved program population into the same execution environment,
with every resource store set to its level at the save, under S113's own runner settings (S111's avida.cfg, copy error
0.0075, the nine two-input tasks paid from their own stores, the other 68 tasks listed at pay 0), and records every
store and every task execution at every update.

  rig        the unchanged population, 200 updates, with Avida's 26 instructions and with the 27th (nop-X, never made by
             copying errors) added: the data files must be identical
  prepare    writes the program populations of the arms: L0 (unchanged, passed through the same editing), Lq (every
             program that does q cut, from s126_find_the_cuts_and_the_shams.py), Ls (the sham replacements), Lr (Lq's
             file with every removed instruction put back by the same editing; must equal L0's file byte for byte)
  phase1     runs L0, Lq, Ls (2,000 updates, two Avida seeds each) and Lr (1,000 updates, the first seed), both
             populations (lengths as in the addendum to the plan, written before any arm was run)
  restore    takes Lq's program population saved at 1,000 updates and writes Lq-then-restored (every nop-X put back to
             the instruction the best-matching cut site held) and Lq-then-reloaded (unchanged), with Lq's store levels
             at that update; probes the restored programs in Avida's analysis mode
  phase2     runs Lq-then-restored and Lq-then-reloaded, 1,000 updates each

Raw output in the scratch space (s126/runs/...), never in the repository; S113's scratch folder is only read (through
the copies in s126/source/). Every Avida process runs under a time limit and at the lowest priority (nice 19), at most 3
at once; the CPU time of each is recorded. Avida's programs copy themselves only inside Avida's simulated processor;
nothing here copies itself on the real machine.

  python3 -B Semantics/tools/s126_run_the_arms.py rig|prepare|phase1|restore|phase2

Written 2 October 2026 by the one Opus 5.5 agent of log S126.
"""
import filecmp, json, os, shutil, subprocess, sys, threading, time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as S113  # noqa: E402  (its environment text and task ranks)
import s126_find_the_cuts_and_the_shams as F  # noqa: E402  (the probe, the instruction set with nop-X)

SCRATCH = F.SCRATCH
AVIDA = F.AVIDA
OUT = F.OUT
RUNS = OUT + '/runs'
PREP = OUT + '/prep'
CONF = F.CONF
POPS = [1, 2]
SEEDS = {1: [1050, 1150], 2: [2050, 2150]}
TIMEOUT = 2400
MAX_AT_ONCE = 3
NULL = F.NULL
CONTEXT = 10
TASKS = F.TASKS
LOCK = threading.Lock()


def read_cuts(pop):
    return json.load(open(os.path.join(PREP, 'cuts_seed%d.json' % pop)))


def stores_at(resource_dat, update=None):
    """{'resNOT': level, ...} at the given update (default: the last row), as S113's runner carried them."""
    rows = [l.split() for l in open(resource_dat) if l.strip() and not l.startswith('#')]
    row = rows[-1] if update is None else [r for r in rows if int(float(r[0])) == update][-1]
    return {'res' + t.upper(): float(row[1 + k]) for k, t in enumerate(TASKS)}


def edit_spop(src, dst, edit):
    """Copy a saved program population line by line; edit(line_number, sequence) gives the new sequence of a living
    program's line (or the same). The sequence is field 17; every other byte is kept."""
    fmt = None
    with open(src) as f, open(dst, 'w') as g:
        for n, line in enumerate(f):
            if line.startswith('#format'):
                fmt = line.split()[1:]
            if line.startswith('#') or not line.strip():
                g.write(line)
                continue
            body = line.rstrip('\n')
            parts = body.split(' ')
            i = fmt.index('sequence')
            if int(parts[fmt.index('num_units')]) > 0:
                new = edit(n, parts[i])
                if len(new) != len(parts[i]):
                    raise RuntimeError('an edit changed a length')
                parts[i] = new
            g.write(' '.join(parts) + line[len(body):])


def living_lines(spop):
    fmt, out = None, {}
    for n, line in enumerate(open(spop)):
        if line.startswith('#format'):
            fmt = line.split()[1:]
            continue
        if line.startswith('#') or not line.strip():
            continue
        p = line.split()
        r = dict(zip(fmt, p))
        if int(r['num_units']) > 0:
            out[n] = (r['sequence'], int(r['num_units']))
    return out


def events_text(n, save_at_1000=True):
    ev = ['u begin LoadPopulation start.spop',
          'u 0:1:%d PrintResourceData' % n,
          'u 0:1:%d PrintTasksExeData' % n,
          'u 0:10:%d PrintTasksData' % n,
          'u 0:10:%d PrintCountData' % n,
          'u 0:100:%d PrintAverageData' % n]
    if save_at_1000 and n > 1000:
        ev.append('u 1000 SavePopulation')
    ev += ['u %d SavePopulation' % n, 'u %d Exit' % n]
    return '\n'.join(ev) + '\n'


def make_run(name, spop, stores, seed, n, instset=None):
    d = os.path.join(RUNS, name)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'default-heads.org']:
        shutil.copy(os.path.join(CONF, f), d)
    open(os.path.join(d, 'instset-heads.cfg'), 'w').write(instset if instset is not None else F.instset_text())
    open(os.path.join(d, 'environment.cfg'), 'w').write(
        S113.environment_text('common_pays_less', S113.load_ranks(), 0, stores))
    open(os.path.join(d, 'events.cfg'), 'w').write(events_text(n))
    shutil.copy(spop, os.path.join(d, 'start.spop'))
    json.dump({'name': name, 'seed': seed, 'updates': n, 'spop': spop, 'stores': stores},
              open(os.path.join(d, 'run.json'), 'w'), indent=1)
    return d


def run_avida(d):
    meta = json.load(open(os.path.join(d, 'run.json')))
    argv = ['timeout', str(TIMEOUT), 'nice', '-n', '19', AVIDA, '-s', str(meta['seed']), '-set', 'VERBOSITY', '0',
            '-set', 'COPY_MUT_PROB', '0.0075'] + EXTRA_SET
    t0 = time.time()
    with open(os.path.join(d, 'avida.log'), 'w') as log:
        p = subprocess.Popen(argv, cwd=d, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        with LOCK:
            open(os.path.join(OUT, 'logs', 'pids.txt'), 'a').write('%d %s\n' % (p.pid, d))
        _, status, ru = os.wait4(p.pid, 0)
    rc = os.waitstatus_to_exitcode(status)
    meta.update({'exit': rc, 'wall_seconds': round(time.time() - t0, 1),
                 'cpu_seconds': round(ru.ru_utime + ru.ru_stime, 1), 'command': 'cd "%s" && %s' % (d, ' '.join(argv))})
    json.dump(meta, open(os.path.join(d, 'run.json'), 'w'), indent=1)
    print('%s exit %d, %.0f s CPU, %s' % (os.path.basename(d), rc, meta['cpu_seconds'], time.strftime('%H:%M:%S')),
          flush=True)
    return rc


def run_all(dirs):
    os.makedirs(os.path.join(OUT, 'logs'), exist_ok=True)
    with ThreadPoolExecutor(max_workers=MAX_AT_ONCE) as pool:
        return list(pool.map(run_avida, dirs))


def data_lines(path):
    return [l for l in open(path) if not l.startswith('#') and l.strip()]


def source(pop):
    return os.path.join(OUT, 'source', 'seed%d' % pop)


def rig():
    pop = 1
    src = source(pop)
    stores = stores_at(os.path.join(src, 'resource.dat'))
    with open(os.path.join(CONF, 'instset-heads.cfg')) as f:
        base26 = f.read()
    a = make_run('rig_seed1_26_instructions', os.path.join(src, 'detail-1000.spop'), stores, SEEDS[pop][0], 200, base26)
    b = make_run('rig_seed1_27_instructions', os.path.join(src, 'detail-1000.spop'), stores, SEEDS[pop][0], 200)
    run_all([a, b])
    same = {}
    for f in sorted(os.listdir(os.path.join(a, 'data'))):
        pa, pb = os.path.join(a, 'data', f), os.path.join(b, 'data', f)
        if f.endswith('.spop'):
            # the saved population names the instruction set only through the letters; compare the data lines
            same[f] = data_lines(pa) == data_lines(pb)
        else:
            same[f] = data_lines(pa) == data_lines(pb)
    print(json.dumps(same, indent=1))
    json.dump(same, open(os.path.join(OUT, 'prep', 'rig_check.json'), 'w'), indent=1)


def prepare():
    for pop in POPS:
        cuts = read_cuts(pop)
        src = os.path.join(source(pop), 'detail-1000.spop')
        by_seq = {r['sequence']: r for r in cuts['records']}
        lines = living_lines(src)
        cut_line = {n: by_seq[s] for n, (s, _) in lines.items() if s in by_seq}
        d = os.path.join(PREP, 'seed%d' % pop)
        os.makedirs(d, exist_ok=True)
        edit_spop(src, os.path.join(d, 'L0.spop'), lambda n, s: s)
        edit_spop(src, os.path.join(d, 'Lq.spop'), lambda n, s: cut_line[n]['cut_sequence'] if n in cut_line else s)
        edit_spop(src, os.path.join(d, 'Ls.spop'), lambda n, s: cut_line[n]['sham_sequence'] if n in cut_line else s)

        def put_back(n, s):
            if n not in cut_line:
                return s
            r = cut_line[n]
            t = list(s)
            for i, x in zip(r['cut_sites'], r['cut_removed']):
                if t[i] != NULL:
                    raise RuntimeError('no nop-X where a cut was made')
                t[i] = x
            return ''.join(t)
        edit_spop(os.path.join(d, 'Lq.spop'), os.path.join(d, 'Lr.spop'), put_back)
        check = {
            'L0 file identical to the save': filecmp.cmp(src, os.path.join(d, 'L0.spop'), shallow=False),
            'Lr file identical to L0 file': filecmp.cmp(os.path.join(d, 'L0.spop'), os.path.join(d, 'Lr.spop'), shallow=False),
            'lines cut': len(cut_line), 'programs on lines cut': sum(lines[n][1] for n in cut_line),
            'replacements in Lq': sum(len(r['cut_sites']) * lines[n][1] for n, r in cut_line.items()),
            'replacements in Ls': sum(len(r['sham_sites']) * lines[n][1] for n, r in cut_line.items()),
            'programs': sum(n for _, n in lines.values()),
        }
        json.dump(check, open(os.path.join(d, 'prepare_check.json'), 'w'), indent=1)
        print(pop, json.dumps(check), flush=True)


def phase1():
    dirs = []
    for pop in POPS:
        stores = stores_at(os.path.join(source(pop), 'resource.dat'))
        d = os.path.join(PREP, 'seed%d' % pop)
        for seed in SEEDS[pop]:
            for arm, n in (('L0', 2000), ('Lq', 2000), ('Ls', 2000), ('Lr', 1000)):
                if arm == 'Lr' and seed != SEEDS[pop][0]:
                    continue        # addendum to the plan: Lr with the first seed only
                dirs.append(make_run('pop%d_%s_seed%d' % (pop, arm, seed), os.path.join(d, arm + '.spop'), stores, seed, n))
    # longest first, so the three slots stay full
    dirs.sort(key=lambda x: -json.load(open(os.path.join(x, 'run.json')))['updates'])
    rc = run_all(dirs)
    print('phase 1 exits:', rc)


def restore_sequence(seq, contexts):
    """Put each nop-X back to the instruction the best-matching cut site held (ten instructions each side)."""
    t = list(seq)
    notes = []
    for p, ch in enumerate(seq):
        if ch != NULL:
            continue
        left = seq[max(0, p - CONTEXT):p][::-1]
        right = seq[p + 1:p + 1 + CONTEXT]
        best, got = -1, Counter()
        for (cl, cr), origs in contexts.items():
            sc = sum(1 for a, b in zip(left, cl) if a == b) + sum(1 for a, b in zip(right, cr) if a == b)
            if sc > best:
                best, got = sc, Counter(origs)
            elif sc == best:
                got.update(origs)
        x = got.most_common(1)[0][0]
        t[p] = x
        notes.append({'site': p, 'restored': x, 'score': best, 'ambiguous': len(got) > 1})
    return ''.join(t), notes


RESTORE_AT = 100        # addendum 2 (after phase 1): restore at update 100, where population 2's q store stood high
RESTORE_POPS = [2]      # addendum 2: population 1's q store never rose, so there is nothing to return there


def restore():
    """Addendum 2 to the plan (written after phase 1, before any restoration was run): Lq is rerun from the same reload
    with the same seed to update 100 and saved there (Avida being deterministic, it must repeat phase 1's Lq exactly;
    checked); from that save, Lq-then-restored and Lq-then-reloaded."""
    report = {}
    dirs = []
    inputs = F.panel()
    for pop in RESTORE_POPS:
        cuts = read_cuts(pop)
        q = cuts['summary']['q']
        contexts = {}
        for r in cuts['records']:
            c = r['cut_sequence']
            for i, x in zip(r['cut_sites'], r['cut_removed']):
                key = (c[max(0, i - CONTEXT):i][::-1], c[i + 1:i + 1 + CONTEXT])
                contexts.setdefault(key, Counter())[x] += r['programs']
        stores0 = stores_at(os.path.join(source(pop), 'resource.dat'))
        to100 = [make_run('pop%d_Lq_to%d_seed%d' % (pop, RESTORE_AT, seed), os.path.join(PREP, 'seed%d' % pop, 'Lq.spop'),
                          stores0, seed, RESTORE_AT) for seed in SEEDS[pop]]
        run_all(to100)
        for seed, lq in zip(SEEDS[pop], to100):
            same = data_lines(os.path.join(lq, 'data', 'resource.dat')) == data_lines(
                os.path.join(RUNS, 'pop%d_Lq_seed%d' % (pop, seed), 'data', 'resource.dat'))[:RESTORE_AT + 1]
            saved = os.path.join(lq, 'data', 'detail-%d.spop' % RESTORE_AT)
            stores = stores_at(os.path.join(lq, 'data', 'resource.dat'), RESTORE_AT)
            lines = living_lines(saved)
            new_of, notes_all = {}, []
            for n, (s, k) in lines.items():
                if NULL in s:
                    ns, notes = restore_sequence(s, contexts)
                    new_of[n] = ns
                    notes_all += [dict(x, programs=k) for x in notes]
            d = os.path.join(PREP, 'seed%d' % pop)
            r_spop = os.path.join(d, 'Lq_then_restored_seed%d.spop' % seed)
            edit_spop(saved, r_spop, lambda n, s: new_of.get(n, s))
            c_spop = os.path.join(d, 'Lq_then_reloaded_seed%d.spop' % seed)
            edit_spop(saved, c_spop, lambda n, s: s)
            # probe: share of programs doing q on the panel, before and after restoration
            before = Counter()
            for s, k in lines.values():
                before[s] += k
            after = Counter()
            for n, (s, k) in lines.items():
                after[new_of.get(n, s)] += k
            pb = F.evaluate_panel(list(before), inputs)
            pa = F.evaluate_panel(list(after), inputs)
            tot = sum(before.values())
            share = lambda pr, cnt: sum(k for s, k in cnt.items() if any(q in r[2] for r in pr[s])) / tot
            copies = lambda pr, cnt: sum(k for s, k in cnt.items() if any(r[0] == 1 for r in pr[s])) / tot
            report['pop%d_seed%d' % (pop, seed)] = {
                'rerun to update %d repeats phase 1 Lq exactly (stores)' % RESTORE_AT: same,
                'programs at the restoring update in Lq': tot,
                'programs carrying at least one nop-X': sum(k for n, (s, k) in lines.items() if NULL in s),
                'nop-X sites put back (programs counted)': sum(x['programs'] for x in notes_all),
                'of which ambiguous': sum(x['programs'] for x in notes_all if x['ambiguous']),
                'share of programs doing q on the panel, before restoring': round(share(pb, before), 4),
                'share of programs doing q on the panel, after restoring': round(share(pa, after), 4),
                'share copying on some panel input, before': round(copies(pb, before), 4),
                'share copying on some panel input, after': round(copies(pa, after), 4),
                'stores at the restoring update in Lq': stores,
                'restored instructions': dict(Counter(x['restored'] for x in notes_all)),
            }
            dirs.append(make_run('pop%d_Lq-then-restored_seed%d' % (pop, seed), r_spop, stores, seed, 1000))
            dirs.append(make_run('pop%d_Lq-then-reloaded_seed%d' % (pop, seed), c_spop, stores, seed, 1000))
    json.dump(report, open(os.path.join(PREP, 'restore_report.json'), 'w'), indent=1)
    print(json.dumps(report, indent=1))
    json.dump(dirs, open(os.path.join(PREP, 'phase2_dirs.json'), 'w'))


def phase2():
    dirs = json.load(open(os.path.join(PREP, 'phase2_dirs.json')))
    print('phase 2 exits:', run_all(dirs))


def diagnose():
    """Added after phase 1 (a departure, reported): Lq of population 1, first seed, 40 updates, the program population
    saved every 5 updates, to see whether the programs born after the reload still carry the cuts."""
    pop, seed = 1, SEEDS[1][0]
    stores = stores_at(os.path.join(source(pop), 'resource.dat'))
    d = make_run('diagnose_pop1_Lq_seed%d' % seed, os.path.join(PREP, 'seed1', 'Lq.spop'), stores, seed, 40)
    ev = open(os.path.join(d, 'events.cfg')).read().replace('u 40 SavePopulation', 'u 5:5:40 SavePopulation')
    open(os.path.join(d, 'events.cfg'), 'w').write(ev)
    run_all([d])
    loaded = set(x for x, _ in living_lines(os.path.join(PREP, 'seed1', 'Lq.spop')).values())
    out = {}
    for u in range(5, 45, 5):
        fmt, a = None, Counter()
        for line in open(os.path.join(d, 'data', 'detail-%d.spop' % u)):
            if line.startswith('#format'):
                fmt = line.split()[1:]
                continue
            if line.startswith('#') or not line.strip():
                continue
            r = dict(zip(fmt, line.split()))
            k = int(r['num_units'])
            if k > 0:
                kind = 'a sequence of the loaded population' if r['sequence'] in loaded else 'a new sequence'
                a[(kind, NULL in r['sequence'])] += k
        out[u] = {'%s, with nop-X: %s' % key: v for key, v in sorted(a.items())}
    json.dump(out, open(os.path.join(PREP, 'diagnose.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


def diagnose_inject():
    """Added after phase 1 (a departure, reported): one program put alone into an empty world (no copying errors, no
    insertions or deletions), its offspring filling the world for 300 updates, every store starting full: the most
    common q-sequence of each population with a clean cut, as cut and as original, and its sham. Does the cut program
    draw q's store down in the world, although the test processor shows it not doing q?"""
    dirs = []
    for pop in POPS:
        cuts = read_cuts(pop)
        q = cuts['summary']['q']
        recs = sorted([r for r in cuts['records'] if r['cut_kind'] == 'clean'], key=lambda r: -r['programs'])[:1] + \
            sorted([r for r in cuts['records'] if r['cut_kind'] == 'collateral'], key=lambda r: -r['programs'])[:1]
        for j, r in enumerate(recs):
            for label, seq in (('original', r['sequence']), ('cut', r['cut_sequence']), ('sham', r['sham_sequence'])):
                name = 'inject_pop%d_%s_%d_%s' % (pop, r['cut_kind'], j, label)
                stores = {'res' + t.upper(): 10000.0 for t in TASKS}
                d = make_run(name, os.path.join(PREP, 'seed%d' % pop, 'L0.spop'), stores, 7, 300)
                names = F.instset_text().split('\n')
                names = [l.split()[1].split(':')[0] for l in names if l.startswith('INST ')]
                with open(os.path.join(d, 'program.org'), 'w') as f:
                    for ch in seq:
                        f.write(names[(ord(ch) - ord('a')) if ch != NULL else 26] + '\n')
                ev = open(os.path.join(d, 'events.cfg')).read().replace('u begin LoadPopulation start.spop',
                                                                       'u begin Inject program.org')
                open(os.path.join(d, 'events.cfg'), 'w').write(ev)
                meta = json.load(open(os.path.join(d, 'run.json')))
                meta.update({'q': q, 'sequence': seq, 'record_programs': r['programs']})
                json.dump(meta, open(os.path.join(d, 'run.json'), 'w'), indent=1)
                dirs.append(d)
    global EXTRA_SET
    EXTRA_SET = ['-set', 'COPY_MUT_PROB', '0', '-set', 'DIVIDE_INS_PROB', '0', '-set', 'DIVIDE_DEL_PROB', '0']
    run_all(dirs)
    out = {}
    for d in dirs:
        meta = json.load(open(os.path.join(d, 'run.json')))
        q = meta['q']
        k = TASKS.index(q)
        res = [l.split() for l in open(os.path.join(d, 'data', 'resource.dat')) if l.strip() and not l.startswith('#')]
        tsk = [l.split() for l in open(os.path.join(d, 'data', 'tasks.dat')) if l.strip() and not l.startswith('#')]
        cnt = [l.split() for l in open(os.path.join(d, 'data', 'count.dat')) if l.strip() and not l.startswith('#')]
        out[os.path.basename(d)] = {
            'q': q, 'q store at 100, 200, 300': [float(res[u][1 + k]) for u in (100, 200, 300)],
            'programs credited with q at 100, 200, 300': [int(tsk[u // 10][1 + k]) for u in (100, 200, 300)],
            'programs at 100, 200, 300': [int(cnt[u // 10][2]) for u in (100, 200, 300)],
            'all nine credited at 300': {t: int(tsk[30][1 + i]) for i, t in enumerate(TASKS)}}
    json.dump(out, open(os.path.join(PREP, 'diagnose_inject.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


EXTRA_SET = []


def keep_lines(src, dst, keep):
    """Copy a saved program population keeping only the living lines whose line number is in keep as they are; every
    other living program is replaced by a program of nop-X only, which does no task, never copies and dies of age (about
    20 times its length in executed instructions). Leaving the lines out, or writing them as no longer living, made Avida
    fail at load."""
    edit_spop(src, dst, lambda n, s: s if n in keep else NULL * len(s))


def diagnose_lines():
    """Added after phase 1 (a departure, reported): with no copying errors, insertions or deletions, 100 updates from
    the same reload: A, Lq whole; B, only the programs whose sequence was cut (every other program left out); C, the
    same programs as B with their original sequences; D, only the programs that were not cut. Which programs keep
    drawing q's store down in Lq?"""
    global EXTRA_SET
    EXTRA_SET = ['-set', 'COPY_MUT_PROB', '0', '-set', 'DIVIDE_INS_PROB', '0', '-set', 'DIVIDE_DEL_PROB', '0']
    dirs = []
    for pop in POPS:
        cuts = read_cuts(pop)
        by_seq = {r['sequence']: r for r in cuts['records']}
        src = os.path.join(source(pop), 'detail-1000.spop')
        lines = living_lines(src)
        cut_lines = set(n for n, (sq, _) in lines.items() if sq in by_seq and by_seq[sq]['cut_sites'])
        d = os.path.join(PREP, 'seed%d' % pop)
        keep_lines(os.path.join(d, 'Lq.spop'), os.path.join(d, 'diag_B_cut_only.spop'), cut_lines)
        keep_lines(os.path.join(d, 'L0.spop'), os.path.join(d, 'diag_C_same_original.spop'), cut_lines)
        keep_lines(os.path.join(d, 'L0.spop'), os.path.join(d, 'diag_D_not_cut_only.spop'), set(lines) - cut_lines)
        stores = stores_at(os.path.join(source(pop), 'resource.dat'))
        for tag, f in (('A_Lq_whole', 'Lq.spop'), ('B_cut_only', 'diag_B_cut_only.spop'),
                       ('C_same_original', 'diag_C_same_original.spop'), ('D_not_cut_only', 'diag_D_not_cut_only.spop')):
            dirs.append(make_run('diaglines_pop%d_%s' % (pop, tag), os.path.join(d, f), stores, SEEDS[pop][0], 100))
    run_all(dirs)
    out = {}
    for x in dirs:
        pop = int(os.path.basename(x).split('_')[1][3:])
        k = TASKS.index(read_cuts(pop)['summary']['q'])
        res = {int(float(l.split()[0])): float(l.split()[1 + k]) for l in open(os.path.join(x, 'data', 'resource.dat'))
               if l.strip() and not l.startswith('#')}
        cnt = {int(float(l.split()[0])): int(float(l.split()[2])) for l in open(os.path.join(x, 'data', 'count.dat'))
               if l.strip() and not l.startswith('#')}
        perf = {}
        for u in range(1, 101):
            r0 = res[u - 1]
            perf[u] = (100 - 0.01 * r0 - (res[u] - r0)) / min(1.0, 0.0025 * r0)
        out[os.path.basename(x)] = {
            'q store at 0, 8, 20, 50, 100': [round(res[u], 1) for u in (0, 8, 20, 50, 100)],
            'q performances per update (from the store), mean 1-8, 9-30, 31-100': [
                round(sum(perf[u] for u in range(a, b + 1)) / (b - a + 1), 1) for a, b in ((1, 8), (9, 30), (31, 100))],
            'programs at 0, 50, 100': [cnt[u] for u in (0, 50, 100)]}
    json.dump(out, open(os.path.join(PREP, 'diagnose_lines.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    {'diagnose_lines': diagnose_lines, 'diagnose_inject': diagnose_inject, 'diagnose': diagnose, 'rig': rig, 'prepare': prepare, 'phase1': phase1, 'restore': restore, 'phase2': phase2}[sys.argv[1]]()
