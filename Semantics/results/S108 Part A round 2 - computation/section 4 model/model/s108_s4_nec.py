# S108 Part A, section 4: (Nec)'s exposure conjunct (D16.XV; L538), for V4.5. Is there a transport t' from D to E that is
# faithful (D5.7: (F1) ∧ (F2)) on a contract? Searched class [S108-4-I5]:
#   σ   every map from the boundaries of C to B_E;
#   τ   every map on the closure of C's edits under D's composition (with 1) into A_E meeting Hom (D5.5, I18, I84: dom τ
#       closed); each τ is fixed by its values on C's edits other than 1, its values on the closure forced by Hom;
#   π   any function X_D ⇀ X_E defined on the solutions at the pairs of C (D5.1 as written, wider than the program's I81);
#   λ   for each k ∈ Γ: N_k ⊆ J_D nonempty, θ_k: V_k → V_{N_k} injective with X^D_{θ(v)} = X^E_v and κ the identity
#       (D5.1: 'the identity where the domains agree'); value maps between different domains are not searched.
# A transport found is a witness in D5.1's class too (the class is a subclass); "none found" is a result over the class only.
# Standard library only; reads core; changes nothing.
import itertools
import time

from .core import ONE


def closure(D, edits):
    dom = set(edits) | {ONE}
    changed = True
    while changed:
        changed = False
        for a1 in list(dom):
            for a2 in list(dom):
                c = D.compose(a2, a1)
                if c is not None and c not in dom:
                    dom.add(c)
                    changed = True
    return dom


def _lambda_options(D, E, k, pairs):
    """(N, θ, projected relation at each pair) for k: θ carries each port of V_k to a port of V_N with the same domain."""
    Vk = E.foot[k]
    out = []
    comps = list(D.comps)
    for r in range(1, len(comps) + 1):
        for N in itertools.combinations(comps, r):
            N = frozenset(N)
            VN = None
            sols = {}
            for (a, b) in pairs:
                VN_, S = D.sol_sub(N, a, b)
                VN = VN_
                sols[(a, b)] = S
            if VN is None:
                continue
            cands = [[u for u in VN if tuple(D.dom[u]) == tuple(E.dom[v])] for v in Vk]
            for th in itertools.product(*cands):
                if len(set(th)) != len(th):
                    continue
                idx = [VN.index(u) for u in th]
                P = {x: frozenset(tuple(z[i] for i in idx) for z in S) for x, S in sols.items()}
                out.append((N, th, P))
    return out


class _Deadline(Exception):
    pass


def _pi_exists(D, E, tau, sigma, pairs, deadline=None):
    """∃π: X_D ⇀ X_E with π[Sol_D(a,b)] = Sol_E(τ(a),σ(b)) at every pair (D5.1). Past the deadline: raises _Deadline.
    π(z) must lie in A(z), the intersection of the T's of the pairs whose solutions hold z (then π[S_x] ⊆ T_x); and every
    y ∈ T_x must be hit by some z ∈ S_x. Search: branch on the uncovered (x, y) with the fewest z that can hit it (complete:
    any π covers each (x, y) by one such z)."""
    S = {x: frozenset(D.sol(*x)) for x in pairs}
    T = {x: frozenset(E.sol(tau[x[0]], sigma[x[1]])) for x in pairs}
    for x in pairs:
        if bool(S[x]) != bool(T[x]):
            return False
    Z = set().union(*S.values()) if S else set()
    A = {}
    for z in Z:
        acc = None
        for x in pairs:
            if z in S[x]:
                acc = T[x] if acc is None else (acc & T[x])
        if not acc:
            return False
        A[z] = acc
    need = sorted(set((x, y) for x in pairs for y in T[x]), key=repr)
    assign = {}

    def rec():
        if deadline is not None and time.time() > deadline:
            raise _Deadline()
        best, by = None, None
        for (x, y) in need:
            if any(assign.get(z) == y for z in S[x]):
                continue
            cands = [z for z in S[x] if z not in assign and y in A[z]]
            if not cands:
                return False
            if best is None or len(cands) < len(best):
                best, by = cands, y
        if best is None:
            return True
        for z in sorted(best, key=repr):
            assign[z] = by
            if rec():
                return True
            del assign[z]
        return False

    return rec()


def exists_faithful(D, E, Gamma, C, time_cap=120.0, want_witness=False):
    """Search the class for t' faithful on C. Returns (found, witness text or None, stopped: None or 'time cap')."""
    try:
        return _exists_faithful(D, E, Gamma, C, time_cap, want_witness)
    except _Deadline:
        return False, None, "time cap %.0f s" % time_cap


def _exists_faithful(D, E, Gamma, C, time_cap, want_witness):
    t0 = time.time()
    pairs = sorted(C, key=repr)
    edits = sorted(set(a for a, _ in pairs), key=repr)
    bounds = sorted(set(b for _, b in pairs), key=repr)
    gens = [a for a in edits if a != ONE]
    domt = closure(D, edits)
    lam_opts = {k: _lambda_options(D, E, k, pairs) for k in Gamma}
    EA = list(E.A)
    for sig_vals in itertools.product(list(E.B), repeat=len(bounds)):
        sigma = dict(zip(bounds, sig_vals))
        # λ(k) options meeting (F1) at the baseline pairs (τ(1) = 1)
        opts = {}
        for k in Gamma:
            ok = [o for o in lam_opts[k] if all(o[2][(a, b)] == E.L(k, ONE, sigma[b]) for (a, b) in pairs if a == ONE)]
            if not ok:
                break
            opts[k] = ok
        if len(opts) != len(Gamma):
            continue
        for combo in itertools.product(*[opts[k] for k in Gamma]):
            if time.time() - t0 > time_cap:
                return False, None, "time cap %.0f s" % time_cap
            lam = dict(zip(Gamma, combo))
            allowed = {}
            dead = False
            for a in gens:
                bs = [b for (a2, b) in pairs if a2 == a]
                al = [x for x in EA if all(lam[k][2][(a, b)] == E.L(k, x, sigma[b]) for k in Gamma for b in bs)]
                if not al:
                    dead = True
                    break
                allowed[a] = al
            if dead:
                continue
            # τ on the generators, extended to the closure by Hom
            for vals in itertools.product(*[allowed[a] for a in gens]):
                if time.time() - t0 > time_cap:
                    return False, None, "time cap %.0f s" % time_cap
                tau = {ONE: ONE}
                tau.update(dict(zip(gens, vals)))
                if not _extend_hom(D, E, tau, domt):
                    continue
                if any(tau[a] not in allowed.get(a, [tau[a]]) for a in gens):
                    continue
                if _pi_exists(D, E, tau, sigma, pairs, deadline=t0 + time_cap):
                    w = None
                    if want_witness:
                        w = "σ %s; τ %s; λ %s" % (sigma, {a: tau[a] for a in edits}, {k: (sorted(lam[k][0]), lam[k][1]) for k in Gamma})
                    return True, w, None
    return False, None, None


def _extend_hom(D, E, tau, domt):
    """Extend τ from its given values to dom τ = domt by Hom; False if Hom fails (a product undefined, or two products
    disagreeing, or a closure element no product reaches)."""
    changed = True
    while changed:
        changed = False
        keys = list(tau)
        for a1 in keys:
            for a2 in keys:
                c = D.compose(a2, a1)
                if c is None:
                    continue
                r = E.compose(tau[a2], tau[a1])
                if r is None:
                    return False
                if c in tau:
                    if tau[c] != r:
                        return False
                else:
                    if c not in domt:
                        return False
                    tau[c] = r
                    changed = True
    return set(tau) >= domt


def exposed_none(D, E, Gamma, time_cap=120.0):
    """D16.XV's (Nec) exposure as written: ∀C' on D ∀t': ¬Faithful_{C'}(t'). A contract holds a pair (1,b) (D3.1) and
    fidelity at fewer pairs is implied by fidelity at more (per-pair (F1), (F2eq); Hom of a restriction to a closed
    subdomain), so it is: for every b ∈ B_D, no t' faithful on {(1,b)}. Returns (exposed, witness b or None, stopped)."""
    for b in D.B:
        f, w, st = exists_faithful(D, E, Gamma, [(ONE, b)], time_cap=time_cap)
        if st:
            return None, None, st
        if f:
            return False, b, None
    return True, None, None


def exposed_v45(D, E, Gamma, C, time_cap=120.0):
    """V4.5: ∀t': ¬Faithful_C(t'), over the class."""
    f, w, st = exists_faithful(D, E, Gamma, C, time_cap=time_cap, want_witness=True)
    if st:
        return None, None, st
    return (not f), w, None
