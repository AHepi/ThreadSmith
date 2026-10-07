#!/usr/bin/env python3
"""s111_avida_test_processor.py

What it does, in plain words: a small helper for log S111 that hands programs (written as letters, one letter per
instruction) to Avida's own analysis mode, which runs each program alone in a private simulated processor with no
mutations and no neighbours, and reads back what Avida reports: whether the program makes an exact copy of itself
("viable"), its fitness, how long a copy takes, its length, and which of the nine logic tasks it performs. It can also ask
Avida to make offspring of a program under a given copy error rate (Avida's SAMPLE_OFFSPRING) and count them. Everything
runs in a fresh folder in the scratch space; nothing is written into the repository. It runs nothing that copies itself on
the real machine: the copying happens only inside Avida's simulated processor.

Letters: a to z are the 26 instructions of Avida's default set (heads_default); A is nop-X, the do-nothing instruction
used for knockouts, added as a 27th instruction only in these analysis runs.

Used by the other s111_ scripts; run on its own it tests the default ancestor and one knockout.
Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import os, shutil, subprocess, tempfile

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
WORK = SCRATCH + '/s111/analysis_work'
HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs', 'configuration')
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NAMES = ['nop-A', 'nop-B', 'nop-C', 'if-n-equ', 'if-less', 'if-label', 'mov-head', 'jmp-head', 'get-head', 'set-flow',
         'shift-r', 'shift-l', 'inc', 'dec', 'push', 'pop', 'swap-stk', 'swap', 'add', 'sub', 'nand', 'h-copy', 'h-alloc',
         'h-divide', 'IO', 'h-search']
NULL = 'A'
TASKS = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']
FIELDS = ['viable', 'fitness', 'merit', 'gest_time', 'length', 'copy_length', 'exe_length'] + \
         ['task.%d' % i for i in range(9)] + ['sequence']
CHUNK = 4000


def name_of(ch):
    return 'nop-X' if ch == NULL else NAMES[LETTERS.index(ch)]


def _folder(settings):
    os.makedirs(WORK, exist_ok=True)
    d = tempfile.mkdtemp(prefix='a_', dir=WORK)
    for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg']:
        shutil.copy(os.path.join(CONF, f), d)
    with open(os.path.join(d, 'instset-heads.cfg'), 'a') as f:
        f.write('\nINST nop-X         # A (log S111 analysis only: a knockout that does nothing and is no label)\n')
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write('u begin Exit\n')
    argv = [AVIDA, '-a', '-s', '1', '-set', 'VERBOSITY', '0']
    for k, v in (settings or []):
        argv += ['-set', k, str(v)]
    return d, argv


def _run(d, argv, lines, timeout):
    with open(os.path.join(d, 'analyze.cfg'), 'w') as f:
        f.write('\n'.join(lines) + '\n')
    with open(os.path.join(d, 'analyze.log'), 'w') as log:
        rc = subprocess.run(['timeout', str(timeout), 'nice', '-n', '10'] + argv, cwd=d, stdout=log,
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    if rc != 0:
        raise RuntimeError('Avida analysis mode exited %d in %s' % (rc, d))


def _read(path, fields):
    rows = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        r = dict(zip(fields, w))
        for k in fields:
            if k == 'sequence':
                continue
            r[k] = float(r[k]) if k in ('fitness', 'merit') else int(float(r[k]))
        rows.append(r)
    return rows


def evaluate(seqs, timeout=3600, keep=False):
    """Each sequence run alone in Avida's test processor; one dict per sequence, in the same order."""
    out = []
    for start in range(0, len(seqs), CHUNK):
        part = seqs[start:start + CHUNK]
        d, argv = _folder(None)
        lines = ['LOAD_SEQUENCE ' + s for s in part] + ['RECALCULATE', 'DETAIL out.dat ' + ' '.join(FIELDS)]
        _run(d, argv, lines, timeout)
        rows = _read(os.path.join(d, 'data', 'out.dat'), FIELDS)
        if len(rows) != len(part) or any(r['sequence'] != s for r, s in zip(rows, part)):
            raise RuntimeError('Avida returned %d rows for %d sequences, or out of order, in %s' % (len(rows), len(part), d))
        out += rows
        if not keep:
            shutil.rmtree(d)
    return out


def sample_offspring(seq, n, settings, timeout=1800):
    """n offspring of seq made in the test processor under the given settings (e.g. COPY_MUT_PROB); returns
    {offspring sequence: count}."""
    d, argv = _folder(settings)
    lines = ['LOAD_SEQUENCE ' + seq, 'SAMPLE_OFFSPRING %d' % n, 'DETAIL off.dat num_cpus sequence']
    _run(d, argv, lines, timeout)
    counts = {}
    for line in open(os.path.join(d, 'data', 'off.dat')):
        if line.startswith('#') or not line.strip():
            continue
        c, s = line.split()[:2]
        counts[s] = counts.get(s, 0) + int(c)
    shutil.rmtree(d)
    return counts


if __name__ == '__main__':
    import sys
    sys.path.insert(0, HERE)
    from s111_run_the_avida_worlds import ancestor_letters
    a = ancestor_letters()
    for r in evaluate([a, a[:-8] + NULL + a[-7:]]):
        print(r)
