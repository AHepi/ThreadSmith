#!/usr/bin/env python3
"""s112_read_what_the_programs_compute_from_avidas_traces.py

What it does, in plain words: for log S112, reads what each evolved program computes, from Avida's own TRACE of the
program running alone in the test processor on the fixed inputs. It does not run any program itself: it follows the
trace Avida wrote, step by step, and for every register and stack place it keeps a note of where the number there came
from (an input read by IO, a constant such as a length written by h-alloc, or an operation such as nand on two earlier
numbers). Which registers and stack places each instruction reads and writes is taken from Avida's source
(source/cpu/cHardwareCPU.cc, Inst_Nand, Inst_TaskIO, Inst_Swap, Inst_Push, Inst_Pop, ...; the register an instruction
acts on is chosen by the nop that follows it, FindModifiedRegister; the stacks as in source/cpu/cCPUStack.h). After every
step, the numbers the notes carry are compared with the numbers in the trace; every difference is counted.

Each output written by IO is put to Avida's check for the nine sums (source/main/cTaskLib.cc, SetupTests, the "logic id"
rule; the lists of ids each sum accepts, lines 513-575). The first accepted output for each sum is compared with the step
at which the trace's own count for that sum goes from 0 to 1. Every accepted output is a "route" for the sum; for each
route the script records the instructions that made it (with their positions and roles: output write, input read, gate,
arithmetic, mover, register choice) and the circuit: the operations from the inputs to the output, with the movers left
out, constant parts folded (ZERO, ONES, OTHER), and a canonical form (identical parts merged, operands of nand and add
sorted, the three inputs renamed to give the smallest written form).

  python3 -B Semantics/tools/s112_read_what_the_programs_compute_from_avidas_traces.py all [jobs]
      every living genotype of the nine S111 runs at update 50,000; one JSON line per genotype into the scratch space
      (s112/traces/<run>.jsonl); the traces themselves are deleted after reading.
  python3 -B Semantics/tools/s112_read_what_the_programs_compute_from_avidas_traces.py one <letters>
      one program, printed.

Written 30 September 2026 by the one Opus 5.5 agent of log S112.
"""
import json, os, shutil, sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s112_run_programs_in_avidas_test_processor as P  # noqa: E402

OUT = P.SCRATCH + '/s112/traces'
BATCH = 300
M32 = 0xffffffff

# The ids each sum accepts (cTaskLib.cc 513-575).
ACCEPT = {'NOT': {15, 51, 85}, 'NAND': {63, 95, 119}, 'AND': {136, 160, 192},
          'ORN': {175, 187, 207, 221, 243, 245}, 'OR': {238, 250, 252}, 'ANDN': {10, 12, 34, 48, 68, 80},
          'NOR': {3, 5, 17}, 'XOR': {60, 90, 102}, 'EQU': {153, 165, 195}}
REGMOD = {'if-n-equ', 'if-less', 'set-flow', 'shift-r', 'shift-l', 'inc', 'dec', 'push', 'pop', 'swap', 'add', 'sub',
          'nand', 'IO', 'nor', 'and', 'or', 'xor'}
HEADMOD = {'mov-head', 'jmp-head', 'get-head'}
LABEL = {'if-label', 'h-search'}
CONTROL = {'if-n-equ', 'if-less', 'if-label', 'mov-head', 'jmp-head', 'get-head', 'set-flow', 'h-search'}
COPYING = {'h-copy', 'h-alloc', 'h-divide'}
NOPS = {'a': 0, 'b': 1, 'c': 2}


def s32(v):
    v &= M32
    return v - (1 << 32) if v & 0x80000000 else v


def logic_id(output, inbuf):
    """Avida's SetupTests (cTaskLib.cc 369-448), for an output and the input buffer (most recent first)."""
    n = len(inbuf)
    ins = [(inbuf[i] & M32) if n > i else 0 for i in range(3)]
    out = output & M32
    lo = [-1] * 8
    for _ in range(32):
        pos = sum((ins[i] & 1) << i for i in range(3))
        if lo[pos] != -1 and lo[pos] != (out & 1):
            return -1
        lo[pos] = out & 1
        out >>= 1
        ins = [x >> 1 for x in ins]
    if n < 1:
        lo[1] = lo[0]
    if n < 2:
        lo[2], lo[3] = lo[0], lo[1]
    if n < 3:
        lo[4], lo[5], lo[6], lo[7] = lo[0], lo[1], lo[2], lo[3]
    if min(lo) < 0:
        return -2          # a bit combination absent from the inputs (cannot happen with Avida's fixed inputs)
    return sum(lo[i] << i for i in range(8))


def sums_of(lid):
    return [t for t in P.TASKS if lid in ACCEPT[t]]


def parse(path):
    """Avida's trace file -> list of states (the state before each executed instruction)."""
    steps, cur = [], None
    for line in open(path):
        if line.startswith('---'):
            if cur and 'ip' in cur:
                steps.append(cur)
            cur = {}
            continue
        if cur is None:
            continue
        s = line.strip()
        if ' IP:' in line and s.split()[0].isdigit():
            w = s.split()
            cur['cycle'] = int(w[0]); cur['ip'] = int(w[1][3:]); cur['name'] = w[2].strip('()')
        elif s.startswith('AX:'):
            w = s.split()
            cur['regs'] = [int(w[0][3:]), int(w[2][3:]), int(w[4][3:])]
        elif s.startswith('R-Head:'):
            w = s.split()
            cur['heads'] = [int(w[0][7:]), int(w[1][7:]), int(w[2][7:])]
        elif 'Stack ' in s and ':' in s:
            star = s.startswith('*')
            w = s.lstrip('* ').split()
            k = int(w[1].rstrip(':'))
            cur.setdefault('stacks', [None, None])[k] = [s32(int(x[2:], 16)) for x in w[2:]]
            if star:
                cur['cur_stack'] = k
        elif s.startswith('Mem ('):
            cur['mem'] = s.split(':', 1)[1].strip()
        elif s.startswith('Task Count'):
            w = s.split(':', 1)[1].split()
            cur['tasks'] = [int(w[2 * i]) for i in range(9)]
        elif s.startswith('Input (env):'):
            cur['env'] = [s32(int(x, 16)) for x in s.split(':', 1)[1].split()]
        elif s.startswith('Input (buf):'):
            cur['buf'] = [s32(int(x, 16)) for x in s.split(':', 1)[1].split()]
        elif s.startswith('Output:'):
            cur['out'] = [s32(int(x, 16)) for x in s.split(':', 1)[1].split()]
    if cur and 'ip' in cur:
        steps.append(cur)
    return steps


class Replay:
    """Follows one trace; carries where each number came from; checks against the trace at every step."""

    def __init__(self, steps, seq):
        self.steps, self.seq, self.L = steps, seq, len(seq)
        self.nodes = []                     # each: dict(kind, op, kids, site, mod, cycle, value, ...)
        self.mismatch = []                  # (cycle, instruction, what)
        self.outputs = []                   # dict(step, cycle, site, mod, reg, node, buf, value)
        self.executed = {}                  # site -> set of roles in which it was read or executed
        self.control_reads = []             # (site, node) for every register value a control instruction read
        self.end = len(steps) - 1           # the step of the first successful split (h-divide), or the last step
        self.divided = False
        z = self.node('const', value=0, why='start')
        self.reg = [z, z, z]
        self.stk = [[z] * 10, [z] * 10]

    def node(self, kind, value, **kw):
        d = dict(kind=kind, value=s32(value), **kw)
        self.nodes.append(d)
        return len(self.nodes) - 1

    def mark(self, site, role):
        if site is not None and site < self.L:
            self.executed.setdefault(site, set()).add(role)

    def run(self):
        st = self.steps
        for k, s in enumerate(st):
            mem, ip, name = s['mem'], s['ip'], s['name']
            n = len(mem)
            nxt = mem[(ip + 1) % n]
            mod = None
            if (name in REGMOD or name in HEADMOD) and nxt in NOPS:
                mod = (ip + 1) % n
            self.mark(ip, name)
            if mod is not None:
                self.mark(mod, 'modifier of ' + name)
            if name in LABEL:
                j = ip + 1
                while mem[j % n] in NOPS and j - ip <= n:
                    self.mark(j % n, 'label of ' + name)
                    j += 1
            regsel = NOPS[mem[mod]] if mod is not None else None
            after = st[k + 1] if k + 1 < len(st) else None
            self.step(k, s, after, name, ip, mod, regsel)
            if after is None:
                self.divided = (name == 'h-divide')      # the trace ends with the split
                break
            if name == 'h-divide' and len(after['mem']) != len(s['mem']):
                # the first successful split ends the program's first run; what follows in the trace file (the
                # processor reset, or the offspring's own run) is not part of it
                self.end, self.divided = k, True
                break
            self.check(after, name)

    def check(self, after, name):
        for r in range(3):
            v = self.nodes[self.reg[r]]['value']
            if v != after['regs'][r]:
                self.mismatch.append((after['cycle'], name, 'register %d' % r))
                self.reg[r] = self.node('const', value=after['regs'][r], why='unexplained after ' + name)
        for q in range(2):
            for i in range(10):
                v = self.nodes[self.stk[q][i]]['value']
                if v != after['stacks'][q][i]:
                    self.mismatch.append((after['cycle'], name, 'stack %d place %d' % (q, i)))
                    self.stk[q][i] = self.node('const', value=after['stacks'][q][i], why='unexplained after ' + name)

    def step(self, k, s, after, name, ip, mod, regsel):
        R = self.reg
        cs = s.get('cur_stack', 0)
        site = ip if ip < self.L else None
        msite = mod if (mod is not None and mod < self.L) else None
        BX, CX = 1, 2
        if name in ('nand', 'add', 'sub', 'nor', 'and', 'or', 'xor'):
            dst = regsel if regsel is not None else BX
            a, b = self.nodes[R[BX]]['value'], self.nodes[R[CX]]['value']
            v = {'nand': ~(a & b), 'add': a + b, 'sub': a - b, 'nor': ~(a | b), 'and': a & b, 'or': a | b,
                 'xor': a ^ b}[name]
            R[dst] = self.node('op', value=v, op=name, kids=[R[BX], R[CX]], site=site, mod=msite, cycle=s['cycle'],
                               dst=dst)
        elif name in ('shift-r', 'shift-l', 'inc', 'dec'):
            r = regsel if regsel is not None else BX
            a = self.nodes[R[r]]['value']
            v = {'shift-r': a >> 1, 'shift-l': a << 1, 'inc': a + 1, 'dec': a - 1}[name]
            R[r] = self.node('op', value=v, op=name, kids=[R[r]], site=site, mod=msite, cycle=s['cycle'], dst=r)
        elif name == 'swap':
            r1 = regsel if regsel is not None else BX
            r2 = (r1 + 1) % 3
            a, b = R[r1], R[r2]
            R[r1] = self.node('wire', value=self.nodes[b]['value'], op='swap', kids=[b], site=site, mod=msite,
                              cycle=s['cycle'], dst=r1)
            R[r2] = self.node('wire', value=self.nodes[a]['value'], op='swap', kids=[a], site=site, mod=msite,
                              cycle=s['cycle'], dst=r2)
        elif name == 'push':
            r = regsel if regsel is not None else BX
            w = self.node('wire', value=self.nodes[R[r]]['value'], op='push', kids=[R[r]], site=site, mod=msite,
                          cycle=s['cycle'], stack=cs)
            self.stk[cs] = [w] + self.stk[cs][:9]
        elif name == 'pop':
            r = regsel if regsel is not None else BX
            top = self.stk[cs][0]
            z = self.node('const', value=0, why='emptied stack place')
            self.stk[cs] = self.stk[cs][1:] + [z]
            R[r] = self.node('wire', value=self.nodes[top]['value'], op='pop', kids=[top], site=site, mod=msite,
                             cycle=s['cycle'], stack=cs, dst=r)
        elif name == 'swap-stk':
            pass                                   # which stack is current: read from the trace ('*')
        elif name == 'IO':
            r = regsel if regsel is not None else BX
            out_node = R[r]
            self.outputs.append(dict(step=k, cycle=s['cycle'], site=site, mod=msite, reg=r, node=out_node,
                                     buf=list(s.get('buf', [])), value=self.nodes[out_node]['value']))
            if after is not None:
                v = after['regs'][r]
                which = s['env'].index(v) if v in s['env'] else -1
                R[r] = self.node('in', value=v, which=which, site=site, mod=msite, cycle=s['cycle'], dst=r)
        elif name == 'h-alloc':
            if after is not None and len(after['mem']) != len(s['mem']):
                R[0] = self.node('const', value=after['regs'][0], why='h-alloc (length)', site=site)
        elif name == 'h-search':
            if after is not None:
                R[1] = self.node('const', value=after['regs'][1], why='h-search (distance)', site=site)
                R[2] = self.node('const', value=after['regs'][2], why='h-search (label size)', site=site)
        elif name == 'get-head':
            if after is not None:
                R[2] = self.node('const', value=after['regs'][2], why='get-head (position)', site=site)
        elif name in ('if-n-equ', 'if-less'):
            r1 = regsel if regsel is not None else BX
            self.control_reads += [(site, R[r1]), (site, R[(r1 + 1) % 3])]
        elif name == 'jmp-head':
            self.control_reads.append((site, R[CX]))
        elif name == 'set-flow':
            self.control_reads.append((site, R[regsel if regsel is not None else CX]))
        # every other instruction of the default set writes no register or stack place (cHardwareCPU.cc)


def has_input(nodes, i, memo):
    if i in memo:
        return memo[i]
    d = nodes[i]
    if d['kind'] == 'in':
        r = True
    elif d['kind'] == 'const':
        r = False
    else:
        r = any(has_input(nodes, c, memo) for c in d['kids'])
    memo[i] = r
    return r


def const_class(v):
    v = s32(v)
    return 'ZERO' if v == 0 else ('ONES' if v == -1 else 'OTHER')


def circuit_string(nodes, root, names, memo_in, reduce=False, values=False):
    """Written form of the circuit from root: wires skipped, constant parts folded, nand/add operands sorted.
    names maps env input index -> leaf name. reduce: steps that leave a number as it is are dropped (add or sub of
    ZERO, inc after dec and dec after inc) and nand with ONES is written as nand of the number with itself (both are
    NOT). values: OTHER constants are written with their value. Returns (string, set of distinct operation strings)."""
    memo, ops = {}, set()

    def f(i):
        if i in memo:
            return memo[i]
        d = nodes[i]
        if d['kind'] == 'wire':
            r = f(d['kids'][0])
        elif d['kind'] == 'in':
            r = names.get(d['which'], 'in?')
        elif d['kind'] == 'const' or not has_input(nodes, i, memo_in):
            r = const_class(d['value'])
            if values and r == 'OTHER':
                r = 'K%d' % d['value']
        else:
            ks = [f(c) for c in d['kids']]
            op = d['op']
            r = None
            if reduce:
                if op == 'add' and 'ZERO' in ks:
                    r = ks[1] if ks[0] == 'ZERO' else ks[0]
                elif op == 'sub' and ks[1] == 'ZERO':
                    r = ks[0]
                elif (op == 'inc' and ks[0].startswith('dec(')) or (op == 'dec' and ks[0].startswith('inc(')):
                    r = ks[0][4:-1]
                elif op == 'nand' and 'ONES' in ks:
                    a = ks[1] if ks[0] == 'ONES' else ks[0]
                    ks = [a, a]
            if r is None:
                if op in ('nand', 'add', 'nor', 'and', 'or', 'xor'):
                    ks = sorted(ks)
                r = '%s(%s)' % (op, ','.join(ks))
                ops.add(r)
        memo[i] = r
        return r
    return f(root), ops


PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def canonical(nodes, root, memo_in, reduce=False):
    best = None
    for p in PERMS:
        s, ops = circuit_string(nodes, root, {k: 'x%d' % p[k] for k in range(3)}, memo_in, reduce)
        if best is None or s < best[0]:
            best = (s, len(ops))
    return best


def cone(nodes, root, memo_in):
    """Sites and their roles in the making of the output value at root (not counting the output write itself)."""
    roles, seen, gates_executed = {}, set(), 0
    stack = [root]
    while stack:
        i = stack.pop()
        if i in seen:
            continue
        seen.add(i)
        d = nodes[i]
        if d['kind'] == 'const':
            continue
        if d['kind'] == 'op' and not has_input(nodes, i, memo_in):
            role = 'constant-making ' + d['op']
        elif d['kind'] == 'op':
            role = 'gate' if d['op'] in ('nand', 'nor', 'and', 'or', 'xor') else 'arithmetic'
            gates_executed += 1
        elif d['kind'] == 'wire':
            role = 'mover'
        else:
            role = 'input read'
        if d.get('site') is not None:
            roles.setdefault(d['site'], set()).add(role)
        if d.get('mod') is not None:
            roles.setdefault(d['mod'], set()).add('register choice')
        for c in d.get('kids', []):
            stack.append(c)
    return roles, gates_executed


GATES = {'nand': lambda a, b: ~(a & b), 'nor': lambda a, b: ~(a | b), 'and': lambda a, b: a & b}
UNARY = {'shift-r': lambda a: a >> 1, 'shift-l': lambda a: a << 1, 'inc': lambda a: a + 1, 'dec': lambda a: a - 1}
rng_inputs = __import__('random').Random(1121)


def world_style_inputs(rng):
    """three numbers as Avida hands them to organisms in the world (cEnvironment.cc 1273-1276): the top 8 bits
    00001111, 00110011, 01010101 (so that every combination of bits occurs), the other 24 bits random"""
    return [s32((15 << 24) + rng.getrandbits(24)), s32((51 << 24) + rng.getrandbits(24)),
            s32((85 << 24) + rng.getrandbits(24))]


def all_combinations(tr):
    return len({sum(((x >> b) & 1) << i for i, x in enumerate(tr)) for b in range(32)}) == 8


OTHER_INPUTS = {'world-style inputs %d' % k: world_style_inputs(rng_inputs) for k in (1, 2, 3)}
while True:
    _t = [s32(rng_inputs.getrandbits(32)) for _ in range(3)]
    if all_combinations(_t):
        OTHER_INPUTS['random 32-bit inputs'] = _t
        break
OTHER_INPUTS['fixed inputs reordered'] = [P.FIXED_INPUTS[2], P.FIXED_INPUTS[0], P.FIXED_INPUTS[1]]
_rg = __import__('random').Random(1123)
GENERALITY_TRIPLES = [world_style_inputs(_rg) for _ in range(200)]
GENERALITY_CACHE = {}


def generality(nodes, root, buf, env, t, key):
    """share of 200 world-style input triples for which this route's operations, on the same path, give an output the
    check accepts for sum t (1.0: the circuit gives the sum for any such inputs)"""
    if key in GENERALITY_CACHE:
        return GENERALITY_CACHE[key]
    ok = 0
    for tr in GENERALITY_TRIPLES:
        v = recompute(nodes, root, 'nand', tr, {})
        b = [tr[env.index(x)] if x in env else x for x in buf]
        lid = logic_id(v, b)
        ok += lid >= 0 and t in sums_of(lid)
    GENERALITY_CACHE[key] = ok / len(GENERALITY_TRIPLES)
    return GENERALITY_CACHE[key]
PREDICTIONS = ['nand read as nor', 'nand read as and'] + list(OTHER_INPUTS)


def recompute(nodes, i, gate, env_new, memo):
    """The value node i would have if the gate letter meant `gate` and the inputs were env_new, on the same path."""
    if i in memo:
        return memo[i]
    d = nodes[i]
    if d['kind'] == 'const':
        v = d['value']
    elif d['kind'] == 'in':
        v = env_new[d['which']] if d['which'] >= 0 else d['value']
    elif d['kind'] == 'wire':
        v = recompute(nodes, d['kids'][0], gate, env_new, memo)
    else:
        ks = [recompute(nodes, c, gate, env_new, memo) for c in d['kids']]
        op = d['op']
        if op == 'nand':
            v = GATES[gate](ks[0], ks[1])
        elif op == 'add':
            v = ks[0] + ks[1]
        elif op == 'sub':
            v = ks[0] - ks[1]
        else:
            v = UNARY[op](ks[0])
    v = s32(v)
    memo[i] = v
    return v


def predict(nodes, outputs, env, gate, env_new):
    """Sums predicted if every output were recomputed with the changed gate or inputs, along the traced path."""
    memo, got = {}, set()
    for o in outputs:
        v = recompute(nodes, o['node'], gate, env_new, memo)
        buf = [env_new[env.index(b)] if b in env else b for b in o['buf']]
        lid = logic_id(v, buf)
        if lid >= 0:
            got.update(sums_of(lid))
    return sorted(got, key=P.TASKS.index)


def read_program(seq, path):
    steps = parse(path)
    rp = Replay(steps, seq)
    rp.run()
    nodes, memo_in = rp.nodes, {}
    env = steps[0]['env']
    names_exact = {0: 'A0f', 1: 'B33', 2: 'C55'}
    outs = []
    for o in rp.outputs:
        lid = logic_id(o['value'], o['buf'])
        o['logic_id'] = lid
        o['sums'] = sums_of(lid) if lid >= 0 else []
        outs.append(o)
    steps = steps[:rp.end + 1]
    credit_step = {}
    for k in range(1, len(steps)):
        for t in range(9):
            if steps[k]['tasks'][t] > steps[k - 1]['tasks'][t] and t not in credit_step:
                credit_step[t] = k - 1
    final_tasks = [P.TASKS[t] for t in range(9) if steps[-1]['tasks'][t] > 0]
    res = {'seq': seq, 'steps': len(steps), 'divided': rp.divided, 'mismatches': len(rp.mismatch),
           'mismatch_examples': rp.mismatch[:5], 'outputs': len(outs),
           'executed': {str(k): sorted(v) for k, v in sorted(rp.executed.items())},
           'tasks_in_trace': final_tasks, 'sums': {}}
    for t, T in enumerate(P.TASKS):
        routes = [o for o in outs if T in o['sums']]
        if not routes and t not in credit_step:
            continue
        first = routes[0]['step'] if routes else None
        entry = {'credited_step_in_trace': credit_step.get(t), 'first_accepted_step': first,
                 'agree': credit_step.get(t) == first, 'routes': []}
        for o in routes:
            roles, gx = cone(nodes, o['node'], memo_in)
            if o['site'] is not None:
                roles.setdefault(o['site'], set()).add('output write')
            if o['mod'] is not None:
                roles.setdefault(o['mod'], set()).add('register choice')
            can, gates = canonical(nodes, o['node'], memo_in)
            red, rgates = canonical(nodes, o['node'], memo_in, reduce=True)
            exact, _ = circuit_string(nodes, o['node'], names_exact, memo_in)
            keyv, _ = circuit_string(nodes, o['node'], names_exact, memo_in, values=True)
            gen = generality(nodes, o['node'], o['buf'], env, T, (T, keyv, tuple(env.index(x) if x in env else x
                                                                                 for x in o['buf'])))
            letters = ''.join(seq[i] for i in sorted(roles))
            entry['routes'].append({'step': o['step'], 'cycle': o['cycle'], 'output_site': o['site'],
                                    'logic_id': o['logic_id'], 'canonical': can, 'gates': gates,
                                    'reduced': red, 'reduced_gates': rgates, 'generality': gen,
                                    'gates_executed': gx, 'exact': exact,
                                    'sites': {str(i): sorted(v) for i, v in sorted(roles.items())},
                                    'letters': letters})
        res['sums'][T] = entry
    res['env'] = env
    res['control_reads_depending_on_inputs'] = sum(1 for site, n in rp.control_reads if has_input(nodes, n, memo_in))
    res['predicted'] = {}
    for name in PREDICTIONS:
        if name.startswith('nand read as'):
            res['predicted'][name] = predict(nodes, outs, env, name.split()[-1], env)
        else:
            res['predicted'][name] = predict(nodes, outs, env, 'nand', OTHER_INPUTS[name])
    res['predicted']['unchanged'] = predict(nodes, outs, env, 'nand', env)
    return res


REG = 'ABC'


def explain_route(seq, t, route_index=0):
    """The steps of one route of sum t (the first accepted by default), in the order they ran: for a worked example."""
    d, paths = P.trace([seq])
    try:
        steps = parse(paths[0])
    finally:
        shutil.rmtree(d)
    rp = Replay(steps, seq)
    rp.run()
    nodes, env = rp.nodes, steps[0]['env']
    routes = [o for o in rp.outputs if (lambda l: l >= 0 and t in sums_of(l))(logic_id(o['value'], o['buf']))]
    o = routes[route_index]
    seen, order, stack = set(), [], [o['node']]
    while stack:
        i = stack.pop()
        if i in seen:
            continue
        seen.add(i)
        dd = nodes[i]
        if dd['kind'] != 'const':
            order.append(i)
        stack += dd.get('kids', [])
    order.sort(key=lambda i: (nodes[i]['cycle'], i))
    names = {0: 'A0f', 1: 'B33', 2: 'C55'}
    lines = []
    for i in order:
        dd = nodes[i]
        mod = (' ' + P.name_of(seq[dd['mod']])) if dd.get('mod') is not None else ''
        val = '0x%08x' % (dd['value'] & M32)
        if dd['kind'] == 'in':
            what = 'IO reads input %s = %s into %sX' % (names.get(dd['which']), val, REG[dd['dst']])
        elif dd['kind'] == 'wire':
            what = '%s moves %s%s' % (dd['op'], val, (' into %sX' % REG[dd['dst']]) if 'dst' in dd else ' onto the stack')
        else:
            kids = ', '.join('0x%08x' % (nodes[k]['value'] & M32) for k in dd['kids'])
            what = '%sX := %s(%s) = %s' % (REG[dd['dst']], dd['op'], kids, val)
        lines.append({'cycle': dd['cycle'], 'site': dd.get('site'), 'instruction': P.name_of(seq[dd['site']]) + mod
                      if dd.get('site') is not None else '?', 'what': what})
    lines.append({'cycle': o['cycle'], 'site': o['site'],
                  'instruction': 'IO' + ((' ' + P.name_of(seq[o['mod']])) if o['mod'] is not None else ''),
                  'what': 'IO writes %sX = 0x%08x out; the check accepts it as %s (logic id %d)' % (
                      REG[o['reg']], o['value'] & M32, t, logic_id(o['value'], o['buf']))})
    return {'seq': seq, 'sum': t, 'env': ['0x%08x' % (x & M32) for x in env], 'steps': lines,
            'other_routes': len(routes) - 1}


def work(args):
    run, items = args
    d, paths = P.trace([s for s, _ in items])
    out = []
    try:
        for (s, n), p in zip(items, paths):
            r = read_program(s, p)
            r['run'], r['organisms'] = run, n
            out.append(r)
    finally:
        shutil.rmtree(d)
    return out


def main_all(jobs):
    os.makedirs(OUT, exist_ok=True)
    for run in P.RUN_NAMES:
        target = os.path.join(OUT, run + '.jsonl')
        if os.path.exists(target):
            continue
        pop = P.living(run)
        batches = [(run, pop[i:i + BATCH]) for i in range(0, len(pop), BATCH)]
        with open(target + '.part', 'w') as f, ProcessPoolExecutor(jobs) as ex:
            for res in ex.map(work, batches):
                for r in res:
                    f.write(json.dumps(r) + '\n')
        os.rename(target + '.part', target)
        print(run, len(pop), 'genotypes read', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'all':
        main_all(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    else:
        seq = sys.argv[2]
        d, paths = P.trace([seq])
        r = read_program(seq, paths[0])
        shutil.rmtree(d)
        print(json.dumps(r, indent=1))
