"""Settling S116's GLM cross-examination (input-order finding, X1.2 / X2.3): the SAME three numbers given in each of the
six orders, S113's own test-processor numbers in each order, fresh numbers in the world's order, and the same numbers
made small, run on the test CPU for every distinct instruction sequence saved at update 50,000 (copies made by S116;
nothing is read from or written into S113's folder). Analyze mode only; nothing is advanced; every Avida process under
nice -n 19 and a time limit (S116's wrapper). Counts, weighted by programs: viable (Avida's check that the program
completes a copy of itself) and viable-and-NOT."""
import itertools, json, os, random, shutil, subprocess, sys
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
HERE = SC + '/s116x_settle'
RUN = HERE + '/order_rundir'
def triples():
    t = {}
    s113 = [0x0f13149f, 0x3308e53e, 0x556241eb]           # Avida's test-CPU default (cEnvironment::SetupInputs, random = false)
    probe0 = [267186772, 869243842, 1433523350]            # the probe's logic_high set 0 (world order)
    for name, base in (('S113 default', s113), ('probe set 0', probe0)):
        for p in itertools.permutations(range(3)):
            v = [base[i] for i in p]
            t['%s, top bytes %s' % (name, [x >> 24 for x in v])] = v
    rnd = random.Random(116)
    for k in range(4):
        v = [(15 << 24) + rnd.getrandbits(24), (51 << 24) + rnd.getrandbits(24), (85 << 24) + rnd.getrandbits(24)]
        t['fresh world order %d' % k] = v
    t['S113 default made small (top byte 0)'] = [x & 0xffffff for x in s113]
    t['probe set 0 made small (top byte 0)'] = [x & 0xffffff for x in probe0]
    for k, tops in enumerate(([40, 90, 120], [120, 40, 90], [15, 51, 51], [15, 15, 85])):
        t['other top bytes %s' % tops] = [(b << 24) + rnd.getrandbits(24) for b in tops]
    return t
def main(key):
    os.makedirs(RUN, exist_ok=True)
    for f in ['avida.cfg', 'instset-heads.cfg', 'default-heads.org']:
        shutil.copy(SC + '/s116/probe_rundir/' + f, RUN)
    out = HERE + '/order_' + key
    os.makedirs(out, exist_ok=True)
    shutil.copy(SC + '/s116/probes/%s/logic_high/environment.cfg' % key, out + '/environment.cfg')
    shutil.copy(SC + '/s116/probes/%s/events.cfg' % key, out + '/events.cfg')
    T = triples()
    lines = ['PURGE_BATCH', 'LOAD %s/s116/copies/%s/u50000.spop' % (SC, key), 'FILTER num_units > 0']
    names = list(T)
    for i, n in enumerate(names):
        lines += ['RECALCULATE 0 -1 0 %d %d %d' % tuple(T[n]), 'DETAIL t%02d.dat id num_units viable ' % i + ' '.join('task.%d' % j for j in range(77))]
    open(out + '/analyze.cfg', 'w').write('\n'.join(lines) + '\n')
    rc = subprocess.run([SC + '/s116/bin/avida', '-c', RUN + '/avida.cfg', '-a', '-set', 'ENVIRONMENT_FILE', out + '/environment.cfg',
                         '-set', 'ANALYZE_FILE', out + '/analyze.cfg', '-set', 'EVENT_FILE', out + '/events.cfg',
                         '-set', 'DATA_DIR', out + '/data', '-set', 'RANDOM_SEED', '20260930', '-set', 'VERBOSITY', '1',
                         '-set', 'TASK_REFRACTORY_PERIOD', '0', '-set', 'TEST_CPU_TIME_MOD', '20'], cwd=RUN,
                        stdout=open(out + '/run.log', 'w'), stderr=subprocess.STDOUT).returncode
    res = {}
    for i, n in enumerate(names):
        tot = via = nt = 0
        per = [0] * 77
        for line in open(out + '/data/t%02d.dat' % i):
            if line.startswith('#') or not line.strip():
                continue
            w = line.split()
            num, v = int(w[1]), int(w[2]) > 0
            tot += num; via += num * v; nt += num * (v and int(w[3]) > 0)
            for j in range(77):
                if v and int(w[3 + j]) > 0:
                    per[j] += num
        res[n] = {'inputs': [hex(x) for x in T[n]], 'programs': tot, 'viable': via, 'viable_and_NOT': nt,
                  'logic_present': sum(p > 0 for p in per), 'logic_common': sum(p / tot >= 0.10 for p in per)}
    json.dump({'key': key, 'exit': rc, 'results': res}, open(out + '/result.json', 'w'), indent=1)
    print(key, 'exit', rc)
    for n, r in res.items():
        print('  %-48s viable %5d  viable+NOT %5d  of %d  present %2d common %2d' % (n, r['viable'], r['viable_and_NOT'], r['programs'], r['logic_present'], r['logic_common']))
if __name__ == '__main__':
    main(sys.argv[1])
