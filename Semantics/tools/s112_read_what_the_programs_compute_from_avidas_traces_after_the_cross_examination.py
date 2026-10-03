#!/usr/bin/env python3
"""s112_read_what_the_programs_compute_from_avidas_traces_after_the_cross_examination.py

A CORRECTED COPY of s112_read_what_the_programs_compute_from_avidas_traces.py (log S112), made 30 September 2026 by the
Opus 5.5 agent that settled the GLM cross-examination of S112 (results/S112 What the evolved sums are - the GLM
cross-examination, settled.md). The script as sent is kept unchanged beside it. Two changes, each marked in the code
with its objection id:
  Xc6  in the reduced circuit form, a nand whose two operands are both ONES is folded to the constant ZERO (the sent
       reader kept it as a part "nand(ONES,ONES)", so a constant part was counted as a step and the parts above it were
       not reduced; it occurred in 170 credited routes and 1,292 other routes);
  Xc3  every route also records "reduced_values": the reduced form with each constant folded as OTHER written with its
       value, so circuits that differ only in such a constant can be told apart.
And one mode, "reread": only the distinct instruction sequences listed in the settling folder's affected.json (those with
nand(ONES,ONES) in any route, or OTHER in a credited route) are traced again by Avida and read again, into
<scratchpad>/s112x_settle/traces_reread/<run>.jsonl; every other sequence's record is unchanged by these two changes.

  python3 -B Semantics/tools/s112_read_what_the_programs_compute_from_avidas_traces_after_the_cross_examination.py reread [jobs]

The original description follows.

s112_read_what_the_programs_compute_from_avidas_traces.py

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

OUT = P.SCRATCH + '/s112x_settle/traces_all'   # not the sent traces
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
    """does the number at node i depend on an input read? (worked without recursion: a node's parts are always
    earlier nodes, and chains in long runs are deep)"""
    stack = [i]
    while stack:
        j = stack[-1]
        if j in memo:
            stack.pop()
            continue
        d = nodes[j]
        if d['kind'] in ('in', 'const'):
            memo[j] = d['kind'] == 'in'
            stack.pop()
            continue
        pend = [c for c in d['kids'] if c not in memo]
        if pend:
            stack.extend(pend)
            continue
        memo[j] = any(memo[c] for c in d['kids'])
        stack.pop()
    return memo[i]


def const_class(v):
    v = s32(v)
    return 'ZERO' if v == 0 else ('ONES' if v == -1 else 'OTHER')


def reach(nodes, root):
    """all nodes the number at root was made from, earliest first"""
    seen, stack = set(), [root]
    while stack:
        i = stack.pop()
        if i in seen:
            continue
        seen.add(i)
        stack += nodes[i].get('kids', [])
    return sorted(seen)


COMMUTATIVE = ('nand', 'add', 'nor', 'and', 'or', 'xor')


def circuit_terms(nodes, root, names, memo_in, reduce=False, values=False):
    """The circuit from root as a table of distinct parts (identical parts merged): wires (movers) skipped, constant
    parts folded to ZERO, ONES or OTHER, operands of nand and add in a fixed order. names maps the input index (0, 1, 2
    = which of the three numbers handed in) to a leaf name. reduce: steps that leave a number as it is are dropped (add
    or sub of ZERO, inc after dec and dec after inc) and nand with ONES is written as nand of the number with itself
    (both are NOT). values: OTHER constants are written with their value. Returns (label of root, table) where table
    maps each part's label to (operation, labels of its operands); a leaf's label is its name.
    (Replaces the first version, which wrote the circuit out as a tree: with parts used many times the written tree
    grew too large to hold in memory; see the S112 results, departures.)"""
    import hashlib
    lab, table = {}, {}
    vals = {}
    for i in reach(nodes, root):
        d = nodes[i]
        if d['kind'] == 'wire':
            lab[i] = lab[d['kids'][0]]
            continue
        if d['kind'] == 'in':
            lab[i] = names.get(d['which'], 'in?')
            continue
        if d['kind'] == 'const' or not has_input(nodes, i, memo_in):
            r = const_class(d['value'])
            lab[i] = ('K%d' % d['value']) if (values and r == 'OTHER') else r
            continue
        ks = [lab[c] for c in d['kids']]
        op = d['op']
        r = None
        if reduce:
            if op == 'add' and 'ZERO' in ks:
                r = ks[1] if ks[0] == 'ZERO' else ks[0]
            elif op == 'sub' and ks[1] == 'ZERO':
                r = ks[0]
            elif op in ('inc', 'dec') and ks[0] in table and table[ks[0]][0] == {'inc': 'dec', 'dec': 'inc'}[op]:
                r = table[ks[0]][1][0]
            elif op == 'nand' and 'ZERO' in ks:
                r = 'ONES'
            elif op == 'nand' and ks[0] == 'ONES' and ks[1] == 'ONES':     # Xc6: nand(ONES, ONES) is the constant ZERO
                r = 'ZERO'
            elif op == 'nand' and 'ONES' in ks:
                x = ks[1] if ks[0] == 'ONES' else ks[0]
                ks = [x, x]
        if r is None:
            if op in COMMUTATIVE:
                ks = sorted(ks)
            r = 'h' + hashlib.sha1(('%s(%s)' % (op, ','.join(ks))).encode()).hexdigest()[:20]
            table[r] = (op, ks)
            vals[r] = d['value']
        lab[i] = r
    circuit_terms.values = vals
    return lab[root], table


def written_form(root, table):
    """The circuit written as numbered parts, g1 = nand(x0,x1); g2 = ..., the last part being the output; parts in
    order of height (inputs first), ties by label. Returns (written form, number of parts)."""
    if root not in table:
        return 'out=' + root, 0
    seen, stack, order = set(), [root], []
    while stack:
        h = stack.pop()
        if h in seen or h not in table:
            continue
        seen.add(h)
        stack += table[h][1]
    height = {}
    todo = sorted(seen)
    while todo:
        rest = []
        for h in todo:
            ks = [k for k in table[h][1] if k in table]
            if all(k in height for k in ks):
                height[h] = 1 + max([height[k] for k in ks] or [0])
            else:
                rest.append(h)
        todo = rest
    order = sorted(seen, key=lambda h: (height[h], h))
    name = {h: 'g%d' % (k + 1) for k, h in enumerate(order)}
    parts = ['%s=%s(%s)' % (name[h], table[h][0], ','.join(name.get(k, k) for k in table[h][1])) for h in order]
    written_form.order = order
    return '; '.join(parts), len(order)


def nested_form(root, table, limit=40):
    """the same circuit written as one nested expression, if it has at most `limit` operations written out"""
    size = {}

    def sz(h):
        if h not in table:
            return 0
        if h not in size:
            size[h] = 1 + sum(sz(k) for k in table[h][1])
        return size[h]
    try:
        if sz(root) > limit:
            return None
    except RecursionError:
        return None

    def f(h):
        if h not in table:
            return h
        op, ks = table[h]
        return '%s(%s)' % (op, ','.join(f(k) for k in ks))
    return f(root)


def circuit_string(nodes, root, names, memo_in, reduce=False, values=False):
    r, t = circuit_terms(nodes, root, names, memo_in, reduce, values)
    return written_form(r, t)


PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def canonical(nodes, root, memo_in, reduce=False, buf=None, values=False):     # Xc3: values passed on
    """the written form under the renaming of the three inputs that gives the smallest written form (so programs
    running the same circuit on different inputs are counted together), its number of parts, its nested form, and
    (with buf, the route's three most recent inputs) the logic id of each part's number in turn: which bit-by-bit
    function of the inputs it is (-1: not a bit-by-bit function, e.g. a number with carries)"""
    best = None
    for p in PERMS:
        r, t = circuit_terms(nodes, root, {k: 'x%d' % p[k] for k in range(3)}, memo_in, reduce, values)
        vals = circuit_terms.values
        s, n = written_form(r, t)
        if best is None or s < best[0]:
            ids = [logic_id(vals[h], buf) for h in written_form.order] if (buf is not None and n) else None
            best = (s, n, nested_form(r, t), ids)
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
    """The value node i would have if the gate letter meant `gate` and the inputs were env_new, on the same path.
    (Worked earliest node first, without recursion.)"""
    for j in reach(nodes, i):
        if j in memo:
            continue
        d = nodes[j]
        if d['kind'] == 'const':
            v = d['value']
        elif d['kind'] == 'in':
            v = env_new[d['which']] if d['which'] >= 0 else d['value']
        elif d['kind'] == 'wire':
            v = memo[d['kids'][0]]
        else:
            ks = [memo[c] for c in d['kids']]
            op = d['op']
            if op == 'nand':
                v = GATES[gate](ks[0], ks[1])
            elif op == 'add':
                v = ks[0] + ks[1]
            elif op == 'sub':
                v = ks[0] - ks[1]
            else:
                v = UNARY[op](ks[0])
        memo[j] = s32(v)
    return memo[i]


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
            can, gates, nested, _ = canonical(nodes, o['node'], memo_in)
            red, rgates, rnested, part_ids = canonical(nodes, o['node'], memo_in, reduce=True, buf=o['buf'])
            redv = canonical(nodes, o['node'], memo_in, reduce=True, values=True)[0]      # Xc3
            exact, _ = circuit_string(nodes, o['node'], names_exact, memo_in)
            keyv, _ = circuit_string(nodes, o['node'], names_exact, memo_in, values=True)
            gen = generality(nodes, o['node'], o['buf'], env, T, (T, keyv, tuple(env.index(x) if x in env else x
                                                                                 for x in o['buf'])))
            letters = ''.join(seq[i] for i in sorted(roles))
            entry['routes'].append({'step': o['step'], 'cycle': o['cycle'], 'output_site': o['site'],
                                    'logic_id': o['logic_id'], 'canonical': can, 'gates': gates,
                                    'reduced': red, 'reduced_values': redv, 'reduced_gates': rgates, 'generality': gen,
                                    'nested': nested, 'reduced_nested': rnested, 'reduced_part_ids': part_ids,
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


def main_reread(jobs):
    """Xc3, Xc6: trace and read again only the sequences listed in the settling folder's affected.json."""
    settle = P.SCRATCH + '/s112x_settle'
    aff = json.load(open(settle + '/affected.json'))
    os.makedirs(settle + '/traces_reread', exist_ok=True)
    for run in P.RUN_NAMES:
        target = os.path.join(settle, 'traces_reread', run + '.jsonl')
        if os.path.exists(target) or not aff.get(run):
            continue
        pop = [(s, n) for s, n, _, _ in aff[run]]
        batches = [(run, pop[i:i + 20]) for i in range(0, len(pop), 20)]
        with open(target + '.part', 'w') as f, ProcessPoolExecutor(jobs) as ex:
            for res in ex.map(work, batches):
                for r in res:
                    f.write(json.dumps(r) + '\n')
        os.rename(target + '.part', target)
        print(run, len(pop), 'sequences read again', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'reread':
        main_reread(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    elif sys.argv[1] == 'all':
        main_all(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    else:
        seq = sys.argv[2]
        d, paths = P.trace([seq])
        r = read_program(seq, paths[0])
        shutil.rmtree(d)
        print(json.dumps(r, indent=1))
