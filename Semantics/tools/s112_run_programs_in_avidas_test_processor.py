#!/usr/bin/env python3
"""s112_run_programs_in_avidas_test_processor.py

What it does, in plain words: a helper for log S112. It hands programs (written as letters, one letter per instruction)
to Avida's own analysis mode, which runs each program alone in its private simulated processor (no mutations, no
neighbours), and reads back what Avida reports: whether the program makes an exact copy of itself, and which of the nine
logic sums it does. It can also ask Avida for a TRACE: Avida's own step-by-step record of a program's run (every executed
instruction, the registers, the stacks, the inputs read, the output written, the sums credited so far).

Unlike S111's helper, it can change one thing of the environment before the run: the meaning given to a letter in the
instruction set (e.g. the letter u meaning "nor" instead of "nand"), the whole assignment of meanings to letters, or
the three input numbers the processor hands in. The genomes' letters are never changed by it.

Everything runs in fresh folders in the scratch space, under a time limit; nothing is written into the repository.
Nothing that copies itself runs on the real machine: the copying happens only inside Avida's simulated processor.
Letters: a to z are the 26 instructions of Avida's default set (heads_default); A is nop-X, the do-nothing instruction
used for removals, added as a 27th instruction in these analysis runs only.

Written 30 September 2026 by the one Opus 5.5 agent of log S112.
"""
import os, shutil, subprocess, tempfile

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
WORK = SCRATCH + '/s112/work'
RUNS = SCRATCH + '/s111/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs', 'configuration')
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NAMES = ['nop-A', 'nop-B', 'nop-C', 'if-n-equ', 'if-less', 'if-label', 'mov-head', 'jmp-head', 'get-head', 'set-flow',
         'shift-r', 'shift-l', 'inc', 'dec', 'push', 'pop', 'swap-stk', 'swap', 'add', 'sub', 'nand', 'h-copy', 'h-alloc',
         'h-divide', 'IO', 'h-search']
NULL = 'A'
TASKS = ['NOT', 'NAND', 'AND', 'ORN', 'OR', 'ANDN', 'NOR', 'XOR', 'EQU']
FIELDS = ['viable', 'fitness', 'gest_time', 'length', 'exe_length'] + ['task.%d' % i for i in range(9)] + ['sequence']
CHUNK = 4000
FIXED_INPUTS = [0x0f13149f, 0x3308e53e, 0x556241eb]   # Avida's test-processor inputs, cEnvironment.cc 1284-1288
RUN_NAMES = ['main_%s_seed%d' % (c, s) for c in ('low', 'default', 'high') for s in (1, 2, 3)]


def name_of(ch, names=None):
    names = names or NAMES
    return 'nop-X' if ch == NULL else names[LETTERS.index(ch)]


def living(run):
    """All living genotypes of a run at update 50,000: list of (sequence, organisms alive), most common first."""
    path = os.path.join(RUNS, run, 'data', 'detail-50000.spop')
    fmt, out = None, []
    for line in open(path):
        if line.startswith('#format'):
            fmt = line.split()[1:]
            continue
        if line.startswith('#') or not line.strip():
            continue
        r = dict(zip(fmt, line.split()))
        if int(r['num_units']) > 0:
            out.append((r['sequence'], int(r['num_units'])))
    return sorted(out, key=lambda x: (-x[1], x[0]))


def _folder(names=None, with_null=True):
    """A fresh analysis folder; names = the 26 meanings of the letters a..z (default: Avida's default set)."""
    os.makedirs(WORK, exist_ok=True)
    d = tempfile.mkdtemp(prefix='a_', dir=WORK)
    for f in ['avida.cfg', 'environment.cfg']:
        shutil.copy(os.path.join(CONF, f), d)
    names = names or NAMES
    with open(os.path.join(d, 'instset-heads.cfg'), 'w') as f:
        f.write('INSTSET heads_default:hw_type=0\n\n')
        for k, n in enumerate(names):
            f.write('INST %-12s # %s\n' % (n, LETTERS[k]))
        if with_null:
            f.write('INST nop-X        # A (analysis only: does nothing, is no label)\n')
    with open(os.path.join(d, 'events.cfg'), 'w') as f:
        f.write('u begin Exit\n')
    argv = [AVIDA, '-a', '-s', '1', '-set', 'VERBOSITY', '0']
    return d, argv


def _run(d, argv, lines, timeout):
    with open(os.path.join(d, 'analyze.cfg'), 'w') as f:
        f.write('\n'.join(lines) + '\n')
    with open(os.path.join(d, 'analyze.log'), 'w') as log:
        rc = subprocess.run(['timeout', str(timeout), 'nice', '-n', '10'] + argv, cwd=d, stdout=log,
                            stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    if rc != 0:
        raise RuntimeError('Avida analysis mode exited %d in %s' % (rc, d))


def _read(path):
    rows = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        r = dict(zip(FIELDS, line.split()))
        for k in FIELDS:
            if k != 'sequence':
                r[k] = float(r[k]) if k == 'fitness' else int(float(r[k]))
        rows.append(r)
    return rows


def evaluate(seqs, inputs=None, names=None, with_null=True, timeout=3600):
    """Each sequence run alone in Avida's test processor; one dict per sequence, in order. inputs: three numbers handed
    in instead of the fixed ones (Avida's RECALCULATE manual inputs); names: other meanings for the letters."""
    out = []
    for start in range(0, len(seqs), CHUNK):
        part = seqs[start:start + CHUNK]
        d, argv = _folder(names, with_null)
        rc = 'RECALCULATE' if inputs is None else 'RECALCULATE 0 -1 0 %d %d %d' % tuple(inputs)
        _run(d, argv, ['LOAD_SEQUENCE ' + s for s in part] + [rc, 'DETAIL out.dat ' + ' '.join(FIELDS)], timeout)
        rows = _read(os.path.join(d, 'data', 'out.dat'))
        if len(rows) != len(part) or any(r['sequence'] != s for r, s in zip(rows, part)):
            raise RuntimeError('Avida returned %d rows for %d sequences, or out of order, in %s' % (len(rows), len(part), d))
        out += rows
        shutil.rmtree(d)
    return out


def tasks_of(row):
    return frozenset(t for k, t in enumerate(TASKS) if row['task.%d' % k] > 0)


def trace(seqs, timeout=3600):
    """Avida's TRACE of each sequence on the fixed inputs. Returns (folder, [trace file path per sequence]); the caller
    reads the files and removes the folder."""
    d, argv = _folder()
    _run(d, argv, ['LOAD_SEQUENCE ' + s for s in seqs] + ['TRACE tr/'], timeout)
    paths = [os.path.join(d, 'data', 'tr', 'org-Seq%d.trace' % (k + 1)) for k in range(len(seqs))]
    for p in paths:
        if not os.path.exists(p):
            raise RuntimeError('missing trace %s' % p)
    return d, paths


if __name__ == '__main__':
    pop = living('main_low_seed2')
    s = pop[0][0]
    print(len(pop), s)
    print(evaluate([s, s[:40] + NULL + s[41:]]))
    print(evaluate([s], names=[('nor' if n == 'nand' else n) for n in NAMES]))
