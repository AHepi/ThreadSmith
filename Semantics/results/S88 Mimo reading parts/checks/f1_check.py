"""Exact check of the F1 instances in Mimo's reply (and one instance of the reader's own).
Relations are affine subspaces of Q^n; every right-hand side is affine in the edit value c,
stored as (const, coef_of_c) in Fractions. Elimination pivots only on numeric LHS coefficients,
so a canonical form that holds here holds for every real c. The baseline (1,b0) has u = 0."""
from fractions import Fraction as F
from itertools import combinations, permutations

def aff(k=0, kc=0): return (F(k), F(kc))
def asub(p, q, m): return (p[0]-m*q[0], p[1]-m*q[1])
def adiv(p, m): return (p[0]/m, p[1]/m)

class Comp:
    def __init__(self, name, ports, eqs, assigns=None):
        # eqs: list of (dict port->coef, aff rhs); relation on ports
        self.name, self.ports, self.eqs, self.assigns = name, list(ports), eqs, assigns
    def under(self, edit):
        # edit: 'base' or 'do' (do(x=c)); the component assigning x is replaced by x=c; at base x=u=0
        if self.assigns == 'x':
            return [({'x': F(1)}, aff(0, 1) if edit == 'do' else aff(0))]
        return self.eqs

def rref(eqs, order):
    rows = [([F(e.get(v, 0)) for v in order], r) for e, r in eqs]
    piv_rows, col = [], 0
    rows = [list(x) for x in rows]
    r0 = 0
    for col in range(len(order)):
        p = next((i for i in range(r0, len(rows)) if rows[i][0][col] != 0), None)
        if p is None: continue
        rows[r0], rows[p] = rows[p], rows[r0]
        pv = rows[r0][0][col]
        rows[r0] = [[x/pv for x in rows[r0][0]], adiv(rows[r0][1], pv)]
        for i in range(len(rows)):
            if i != r0 and rows[i][0][col] != 0:
                m = rows[i][0][col]
                rows[i] = [[a-m*b for a, b in zip(rows[i][0], rows[r0][0])], asub(rows[i][1], rows[r0][1], m)]
        r0 += 1
    out = []
    for lhs, rhs in rows:
        if all(x == 0 for x in lhs):
            if rhs != aff(0): return 'EMPTY-or-c-dependent'
            continue
        out.append((tuple(lhs), rhs))
    return out

def proj(eqs, allports, keep):
    """Canonical form of the projection onto the ordered tuple keep."""
    hidden = [v for v in allports if v not in keep]
    R = rref(eqs, hidden + list(keep))
    if isinstance(R, str): return R
    kept = [(lhs[len(hidden):], rhs) for lhs, rhs in R if all(x == 0 for x in lhs[:len(hidden)])]
    return tuple(kept)

def sol_eqs(comps, edit):
    eqs, ports = [], []
    for k in comps:
        eqs += k.under(edit)
        for v in k.ports:
            if v not in ports: ports.append(v)
    return eqs, ports

EDITS = ['base', 'do']
def rel(comps, keep, edit):
    eqs, ports = sol_eqs(comps, edit)
    return proj(eqs, ports, keep)

def rename(eqs, m): return [({m[v]: c for v, c in e.items()}, r) for e, r in eqs]

def sig(k, edit, beta=None):
    eqs = k.under(edit)
    if beta: eqs = rename(eqs, beta)
    keep = [beta[v] for v in k.ports] if beta else k.ports
    return eqs, keep

def one_kind(k, k2):
    """Cross-candidate kind (finding's typing, tau = tau' = identity): some footprint bijection beta
    with beta[L_k(a)] = L_k2(a) for every a in C (baseline and do(x=c) for all c)."""
    if len(k.ports) != len(k2.ports): return False
    for perm in permutations(k2.ports):
        beta = dict(zip(k.ports, perm))
        if all(proj(rename(k.under(e), beta), list(perm), tuple(k2.ports)) ==
               proj(k2.under(e), k2.ports, tuple(k2.ports)) for e in EDITS):
            return True
    return False

def check_F1(E, anchors, D):
    ok = True
    for k in E:
        sub, rho = anchors[k.name]
        subcomps = [j for j in D if j.name in sub]
        for e in EDITS:
            lhs = rel(subcomps, tuple(rho[v] for v in k.ports), e)
            rhs = proj(rename(k.under(e), rho), [rho[v] for v in k.ports], tuple(rho[v] for v in k.ports))
            ok &= (lhs == rhs)
    return ok

def check_F2(E, D, Eports):
    return all(rel(D, tuple(Eports), e) == rel(E, tuple(Eports), e) for e in EDITS)

def answer(comps, q, e): return rel(comps, (q,), e)

def pair_table(E1, E2):
    return [(a.name, b.name) for a in E1 for b in E2 if one_kind(a, b)]

eq = lambda d, k=0: (dict((p, F(v)) for p, v in d.items()), aff(k))
ID = lambda ps: {p: p for p in ps}

print("== Counter-instance 1")
jx = Comp('j_x', ['x'], [], 'x'); jy = Comp('j_y', ['x','y'], [eq({'y':1,'x':-2})]); jz = Comp('j_z', ['y','z'], [eq({'z':1,'y':-1}, 1)])
D1 = [jx, jy, jz]
kx = Comp('k_x', ['x'], [], 'x'); ky = Comp('k_y', ['x','y'], [eq({'y':1,'x':-2})]); kz = Comp('k_z', ['y','z'], [eq({'z':1,'y':-1}, 1)])
E1 = [kx, ky, kz]; A1 = {'k_x': ({'j_x'}, ID('x')), 'k_y': ({'j_y'}, ID('xy')), 'k_z': ({'j_z'}, ID('yz'))}
mx = Comp('m_x', ['x'], [], 'x'); mz = Comp('m_z', ['x','z'], [eq({'z':1,'x':-2}, 1)])
E2 = [mx, mz]; A2 = {'m_x': ({'j_x'}, ID('x')), 'm_z': ({'j_y','j_z'}, ID('xz'))}
print("E1 F1,F2:", check_F1(E1, A1, D1), check_F2(E1, D1, 'xyz'))
print("E2 F1,F2:", check_F1(E2, A2, D1), check_F2(E2, D1, 'xz'))
print("proj_xz Sol_{j_y,j_z} (do):", rel([jy, jz], ('x','z'), 'do'))
print("pi Sol_D (do) on (x,z):", rel(D1, ('x','z'), 'do'), " base:", rel(D1, ('x','z'), 'base'))
print("A: Ans_D, Ans_E1, Ans_E2 (do):", answer(D1,'z','do'), answer(E1,'z','do'), answer(E2,'z','do'))
print("one-kind pairs E1 x E2:", pair_table(E1, E2))

print("== Counter-instance 2")
Jx = Comp('j_x', ['x'], [], 'x'); Jy = Comp('j_y', ['x','y'], [eq({'y':1,'x':-1}, 1)]); Jz = Comp('j_z', ['y','z'], [eq({'z':1,'y':-1}, 1)]); Jw = Comp('j_w', ['z','w'], [eq({'w':1,'z':-1})])
D2 = [Jx, Jy, Jz, Jw]
ax = Comp('a_x', ['x'], [], 'x'); az = Comp('a_z', ['x','z'], [eq({'z':1,'x':-1}, 2)]); aw = Comp('a_w', ['z','w'], [eq({'w':1,'z':-1})])
Ea = [ax, az, aw]; AA = {'a_x': ({'j_x'}, ID('x')), 'a_z': ({'j_y','j_z'}, ID('xz')), 'a_w': ({'j_w'}, ID('zw'))}
bx = Comp('b_x', ['x'], [], 'x'); by = Comp('b_y', ['x','y'], [eq({'y':1,'x':-1}, 1)]); bw = Comp('b_w', ['y','w'], [eq({'w':1,'y':-1}, 1)])
Eb = [bx, by, bw]; AB = {'b_x': ({'j_x'}, ID('x')), 'b_y': ({'j_y'}, ID('xy')), 'b_w': ({'j_z','j_w'}, ID('yw'))}
print("Ea F1,F2:", check_F1(Ea, AA, D2), check_F2(Ea, D2, 'xzw'))
print("Eb F1,F2:", check_F1(Eb, AB, D2), check_F2(Eb, D2, 'xyw'))
print("A: Ans_D, Ans_Ea, Ans_Eb (do):", answer(D2,'w','do'), answer(Ea,'w','do'), answer(Eb,'w','do'))
print("one-kind pairs Ea x Eb:", pair_table(Ea, Eb))
# every bijection Ea -> Eb: how many pairs are of one kind
best = max(sum(one_kind(a, b) for a, b in zip(Ea, p)) for p in permutations(Eb))
print("max one-kind pairs over the 6 bijections:", best, "of 3")
# partitions incomparable
P1 = [{'j_x'}, {'j_y','j_z'}, {'j_w'}]; P2 = [{'j_x'}, {'j_y'}, {'j_z','j_w'}]
refines = lambda P, Q: all(any(b <= q for q in Q) for b in P)
print("Pa refines Pb:", refines(P1, P2), " Pb refines Pa:", refines(P2, P1))

print("== Defence (iii): subnetworks of the other candidate projected onto two ports")
def sub_partners(k, F_):
    hits, count = [], 0
    for r in range(1, len(F_)+1):
        for N in combinations(F_, r):
            ports = []
            for c in N:
                for v in c.ports:
                    if v not in ports: ports.append(v)
            if len(ports) < len(k.ports): continue
            count += 1
            for keep in permutations(ports, len(k.ports)):
                if all(rel(list(N), keep, e) == proj(k.under(e), k.ports, tuple(k.ports)) for e in EDITS):
                    hits.append(([c.name for c in N], keep))
    return count, hits
for k, F_ in [(aw, Eb), (az, Eb), (by, Ea), (bw, Ea), (ky, E2), (kz, E2)]:
    n, h = sub_partners(k, F_)
    print(f"{k.name}: {n} subnetworks of the other candidate with >= {len(k.ports)} ports; partners: {h}")
print("Eb subnetworks and what they project to (edit do):")
for r in range(1, 4):
    for N in combinations(Eb, r):
        ports = []
        for c in N:
            for v in c.ports:
                if v not in ports: ports.append(v)
        for keep in combinations(ports, 2):
            print("  ", [c.name for c in N], keep, rel(list(N), keep, 'do'))
print("block {a_z,a_w} on (x,w):", rel([az, aw], ('x','w'), 'do'), " block {b_y,b_w} on (x,w):", rel([by, bw], ('x','w'), 'do'))
print("block {k_y,k_z} on (x,z) vs m_z:", rel([ky, kz], ('x','z'), 'do') == proj(mz.eqs, mz.ports, ('x','z')))

print("== Reader's instance: repair (ii) as sent, same subnetwork, port translations onto different ports")
k0 = Comp('k0', ['x'], [], 'x'); ka = Comp('ka', ['x','y'], [eq({'y':1,'x':-2})]); kb = Comp('kb', ['x','z'], [eq({'z':1,'x':-2}, 1)])
E3 = [k0, ka, kb]; A3 = {'k0': ({'j_x'}, ID('x')), 'ka': ({'j_y','j_z'}, ID('xy')), 'kb': ({'j_y','j_z'}, ID('xz'))}
h0 = Comp('h0', ['x'], [], 'x'); hd = Comp('hd', ['x','y'], [eq({'y':1,'x':-2})]); hc = Comp('hc', ['y','z'], [eq({'z':1,'y':-1}, 1)])
E4 = [h0, hd, hc]; A4 = {'h0': ({'j_x'}, ID('x')), 'hd': ({'j_y','j_z'}, ID('xy')), 'hc': ({'j_y','j_z'}, ID('yz'))}
print("E3 F1,F2,A:", check_F1(E3, A3, D1), check_F2(E3, D1, 'xyz'), answer(E3,'z','do') == answer(D1,'z','do'))
print("E4 F1,F2,A:", check_F1(E4, A4, D1), check_F2(E4, D1, 'xyz'), answer(E4,'z','do') == answer(D1,'z','do'))
for phi in [{'k0':'h0','ka':'hd','kb':'hc'}, {'k0':'h0','ka':'hc','kb':'hd'}]:
    same_sub = all(A3[k][0] == A4[v][0] for k, v in phi.items())
    same_ports = all(set(A3[k][1][p] for p in [c for c in E3 if c.name==k][0].ports) == set(A4[v][1][p] for p in [c for c in E4 if c.name==v][0].ports) for k, v in phi.items())
    kinds = {k: one_kind([c for c in E3 if c.name==k][0], [c for c in E4 if c.name==v][0]) for k, v in phi.items()}
    print(" phi", phi, "| same subnetworks (as-sent premise):", same_sub, "| same ports of D (current premise):", same_ports, "| pairs of one kind:", kinds)
