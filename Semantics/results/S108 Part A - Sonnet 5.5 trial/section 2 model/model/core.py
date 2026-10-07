# S104 round 2 (maths): the formal core of `formal core.md`, encoded on small finite models.
# Standard library only. Every place where the code needs something the formal core leaves open is
# tagged with the id of an invention in `inventions register.md` (I01-I76 from the formal core,
# I77 onward from this program; see model/inventions_model.py). Nothing tagged is the text's own
# content. Definitions are cited by their D-number in `formal core.md`.
import itertools

# ---- the undetermined answer (D3.2, I21) -----------------------------------------------------


class _Bot:
    __slots__ = ()

    def __repr__(self):
        return "⊥"

    def __reduce__(self):
        return (_bot, ())


def _bot():
    return BOT


BOT = _Bot()
ONE = "1"  # the identity edit of every organization (D1.1)


def powerset(xs):
    xs = list(xs)
    for r in range(len(xs) + 1):
        for c in itertools.combinations(xs, r):
            yield frozenset(c)


def solve(ports, dom, constraints):
    """All valuations of `ports` (ordered) meeting every constraint.
    constraints: list of (tuple of ports, relation as a set of tuples in that order).
    Backtracking; each constraint is checked as soon as its last port is assigned."""
    pos = {p: i for i, p in enumerate(ports)}
    by_last = [[] for _ in ports]
    for fp, rel in constraints:
        if not fp:
            if () not in rel:
                return []
            continue
        idx = tuple(pos[p] for p in fp)
        by_last[max(idx)].append((idx, rel))
    out = []
    cur = [None] * len(ports)

    def rec(i):
        if i == len(ports):
            out.append(tuple(cur))
            return
        for x in dom[ports[i]]:
            cur[i] = x
            ok = True
            for idx, rel in by_last[i]:
                if tuple(cur[k] for k in idx) not in rel:
                    ok = False
                    break
            if ok:
                rec(i + 1)
        cur[i] = None

    rec(0)
    return out


# ---- organizations (D1.1-D1.4) ----------------------------------------------------------------


class Org:
    """D = (V, (X_v), J, (V_j), B, A, ·, 1, L) (D1.1).
    ports: ordered names; dom: port -> tuple of values (finite, nonempty) [I77];
    comps: ordered names; foot: comp -> ordered tuple of ports; B: boundary labels;
    A: edit labels with ONE among them; compose(a2, a1) -> edit or None (partial; I01, I78);
    Lfun(j, a, b) -> frozenset of tuples over foot[j] (I02: no law is imposed by this class)."""

    def __init__(self, name, ports, dom, comps, foot, B, A, compose, Lfun, meta=None):
        self.name = name
        self.ports = tuple(ports)
        self.dom = {p: tuple(dom[p]) for p in self.ports}
        self.comps = tuple(comps)
        self.foot = {j: tuple(foot[j]) for j in self.comps}
        self.B = tuple(B)
        self.A = tuple(A)
        assert ONE in self.A
        self._compose = compose
        self._L = Lfun
        self.deleted = frozenset()
        self.override = {}  # (j, a, b) -> relation: hypothetical relations at one pair (D8.1)
        self.meta = dict(meta or {})
        self._full = {}
        self._cache = {}

    # copies ------------------------------------------------------------------------------------
    def _copy(self):
        o = Org.__new__(Org)
        o.__dict__.update(self.__dict__)
        o._cache = {}
        return o

    def delete(self, G):
        """D - G (D1.3): every component of G imposes the full relation at every (a, b)."""
        o = self._copy()
        o.deleted = self.deleted | frozenset(G)
        o.name = self.name + "-" + "{" + ",".join(sorted(G)) + "}"
        return o

    def with_relations_at(self, a, b, R):
        """D^R (D8.1): the relations at the one pair (a, b) replaced by R (comp -> relation)."""
        o = self._copy()
        o.override = dict(self.override)
        for j, rel in R.items():
            o.override[(j, a, b)] = frozenset(rel)
        return o

    # relations ---------------------------------------------------------------------------------
    def full(self, j):
        if j not in self._full:
            self._full[j] = frozenset(itertools.product(*[self.dom[v] for v in self.foot[j]]))
        return self._full[j]

    def L(self, j, a, b):
        if j in self.deleted:
            return self.full(j)
        if (j, a, b) in self.override:
            return self.override[(j, a, b)]
        return frozenset(self._L(j, a, b))

    def compose(self, a2, a1):
        """a2·a1 (partial). The identity law is built in (D1.1)."""
        if a1 == ONE:
            return a2
        if a2 == ONE:
            return a1
        return self._compose(a2, a1)

    # solutions ---------------------------------------------------------------------------------
    def sol(self, a, b):
        """Sol_D(a, b) (O), as tuples over self.ports."""
        key = ("sol", a, b)
        if key not in self._cache:
            cons = [(self.foot[j], self.L(j, a, b)) for j in self.comps]
            self._cache[key] = frozenset(solve(self.ports, self.dom, cons))
        return self._cache[key]

    def ports_of(self, N):
        vs = []
        for j in self.comps:
            if j in N:
                for v in self.foot[j]:
                    if v not in vs:
                        vs.append(v)
        return tuple(v for v in self.ports if v in vs)

    def sol_sub(self, N, a, b):
        """Sol_N(a, b) (D1.4, I14): the constraints of N alone, over V_N (ordered as self.ports)."""
        N = frozenset(N)
        key = ("sub", N, a, b)
        if key not in self._cache:
            # Area 2 [A2-04, amends I14]: the whole target as a subnetwork keeps every port of D,
            # a port in no footprint included, so Sol_{J_D} = Sol_D (FC25 (b)).
            VN = self.ports if N >= frozenset(self.comps) else self.ports_of(N)
            cons = [(self.foot[j], self.L(j, a, b)) for j in self.comps if j in N]
            self._cache[key] = (VN, frozenset(solve(VN, self.dom, cons)))
        return self._cache[key]

    def proj(self, sols, ports, onto):
        idx = [ports.index(p) for p in onto]
        return frozenset(tuple(z[i] for i in idx) for z in sols)

    def as_dict(self, z):
        return dict(zip(self.ports, z))

    # description -------------------------------------------------------------------------------
    def describe(self, pairs=None, comps=None):
        lines = ["organization %s" % self.name]
        lines.append("  ports: " + "; ".join("%s ∈ {%s}" % (p, ",".join(map(str, self.dom[p]))) for p in self.ports))
        lines.append("  components: " + "; ".join("%s on (%s)" % (j, ",".join(self.foot[j])) for j in self.comps))
        lines.append("  boundaries B = {%s}; edits A = {%s}" % (",".join(map(str, self.B)), ",".join(map(str, self.A))))
        comp_tab = []
        for a2 in self.A:
            for a1 in self.A:
                if ONE in (a1, a2):
                    continue
                c = self.compose(a2, a1)
                comp_tab.append("%s·%s=%s" % (a2, a1, c if c is not None else "undef"))
        if comp_tab:
            lines.append("  composition (other than with 1): " + ", ".join(comp_tab))
        if self.deleted:
            lines.append("  deleted: " + ",".join(sorted(self.deleted)))
        prs = pairs if pairs is not None else [(a, b) for a in self.A for b in self.B]
        for j in (comps or self.comps):
            for (a, b) in prs:
                rel = sorted(self.L(j, a, b), key=repr)
                full = self.L(j, a, b) == self.full(j)
                lines.append("  L_%s(%s,%s) = %s" % (j, a, b, "full" if full and len(rel) > 1 else "{" + " ".join("(" + ",".join(map(str, w)) + ")" for w in rel) + "}"))
        return "\n".join(lines)


def restrict_valuation(org, z, onto):
    return tuple(z[org.ports.index(p)] for p in onto)


# ---- setting edits, roles (D2.1-D2.5) ----------------------------------------------------------


def slice_rel(org, j, v, x):
    i = org.foot[j].index(v)
    return frozenset(w for w in org.full(j) if w[i] == x)


def sets_through(org, a, b, v, j):
    """a sets port v through component j at b (D2.1, I04)."""
    if v not in org.foot[j]:
        return False
    rel = org.L(j, a, b)
    i = org.foot[j].index(v)
    xs = set(w[i] for w in rel)
    if len(xs) != 1:
        return False
    x = next(iter(xs))
    if rel != slice_rel(org, j, v, x):
        return False
    for k in org.comps:
        if k != j and org.L(k, a, b) != org.L(k, ONE, b):
            return False
    return True


# area 1 (S104 round 2 reading): the observation reading the maths now uses (D2.4 settled to R-ii,
# with composites of settings excluded, D2.4' in "area 1 - verdicts and formal fixes.md"). Claims that
# report both readings still compute both; OBS_READING is the one D4.6 uses.
OBS_READING = "R-ii"


class Roles:
    """Set_v, asg, Input, Output, Obs under both readings, families (D2.1-D2.4, D4.5-D4.6).
    exclude_identity: I80. Area 1 fix: default True (D2.1: a setting edit is an edit other than 1;
    L103 'replaces', L141 baseline, T13). Pass False for the round-2 literal reading."""

    def __init__(self, org, exclude_identity=True):
        self.org = org
        self.exclude_identity = exclude_identity
        self.Set = {}
        self.through = {}
        for v in org.ports:
            S, T = [], set()
            for a in org.A:
                if exclude_identity and a == ONE:
                    continue
                ok = True
                js_a = set()
                for b in org.B:
                    js = [j for j in org.comps if sets_through(org, a, b, v, j)]
                    if not js:
                        ok = False
                        break
                    js_a.update(js)
                if ok:
                    S.append(a)
                    T.update(js_a)
            self.Set[v] = frozenset(S)
            self.through[v] = T
        # asg(v): the one component the setting edits of v set it through; undefined otherwise (I04)
        self.asg = {v: next(iter(self.through[v])) for v in org.ports if len(self.through[v]) == 1}
        self.alt = {j: frozenset(a for a in org.A if any(org.L(j, a, b) != org.L(j, ONE, b) for b in org.B)) for j in org.comps}
        # Slc_j (area 1, D2.6 new, A1-04): the edits that alter j and, at every b where they alter it, replace
        # it by a slice on a port j assigns: interventions on j, single or composite, whatever else they
        # alter. L57 sets them apart from edits to j's rule (H01).
        self.slc = {j: frozenset(a for a in self.alt[j] if self._slices(j, a)) for j in org.comps}

    def _slices(self, j, a):
        org = self.org
        for b in org.B:
            rel = org.L(j, a, b)
            if rel == org.L(j, ONE, b):
                continue
            ok = False
            for i, v in enumerate(org.foot[j]):
                if self.asg.get(v) != j:
                    continue
                xs = set(w[i] for w in rel)
                if len(xs) == 1 and rel == slice_rel(org, j, v, next(iter(xs))):
                    ok = True
                    break
            if not ok:
                return False
        return True

    def input(self, v):
        return bool(self.Set[v])

    def output(self, v, j):
        """Out(v, j) (D2.3, I05): at the identity edit, at most one value of v given the others."""
        org = self.org
        if v not in org.foot[j]:
            return False
        i = org.foot[j].index(v)
        for b in org.B:
            seen = {}
            for w in org.L(j, ONE, b):
                key = w[:i] + w[i + 1:]
                if key in seen and seen[key] != w[i]:
                    return False
                seen[key] = w[i]
        return True

    def outputs_of(self, j):
        """o_j: the ports j assigns. Where j assigns several, Set_{o_j} is the union [I102]."""
        return [v for v, k in self.asg.items() if k == j]

    def set_oj(self, j):
        s = set()
        for v in self.outputs_of(j):
            s |= self.Set[v]
        return frozenset(s)

    def obs(self, reading):
        """Obs (D2.4) under reading 'R-i' or 'R-ii' (I06). An (o, m) with asg(m) undefined yields no
        observation edits [I102]."""
        org = self.org
        out = set()
        for o, j in self.asg.items():
            for m in org.foot[j]:
                if m == o or m not in self.asg:
                    continue
                jm = self.asg[m]
                for a in org.A:
                    if a not in self.alt[j]:
                        continue
                    if any(org.L(jm, a, b) != org.L(jm, ONE, b) for b in org.B):
                        continue
                    if reading == "R-ii" and (a in self.Set[o] or a in self.slc[j]):
                        continue
                    out.add(a)
        return frozenset(out)

    def obs_pairs(self, reading):
        org = self.org
        res = {}
        for o, j in self.asg.items():
            for m in org.foot[j]:
                if m == o or m not in self.asg:
                    continue
                jm = self.asg[m]
                s = set()
                for a in org.A:
                    if a in self.alt[j] and all(org.L(jm, a, b) == org.L(jm, ONE, b) for b in org.B):
                        if reading == "R-ii" and (a in self.Set[o] or a in self.slc[j]):
                            continue
                        s.add(a)
                res[(o, m)] = frozenset(s)
        return res

    # change and invariance on a contract (D4.5, I09) ------------------------------------------
    def changes(self, j, X, C):
        org = self.org
        return any(a in X and org.L(j, a, b) != org.L(j, ONE, b) for (a, b) in C)

    def inv(self, j, X, C):
        org = self.org
        return all(org.L(j, a, b) == org.L(j, ONE, b) for (a, b) in C if a in X)

    # families (D4.6) ---------------------------------------------------------------------------
    def causal(self, j, C, reading):
        return self.changes(j, self.set_oj(j), C) and self.inv(j, self.obs(reading), C)

    def meas(self, j, m, C, reading):
        org = self.org
        if m not in org.foot[j] or m not in self.asg or self.asg.get(m) == j:  # area 1: asg(m) defined (U5)
            return False
        MR = self.alt[j] if reading == "R-i" else self.alt[j] - self.set_oj(j) - self.slc[j]
        return self.inv(j, self.Set[m], C) and self.changes(j, MR, C)

    def world(self, j):
        s = set()
        for v in self.org.ports:
            if self.asg.get(v) != j:  # includes ports with asg undefined [I102]
                s |= self.Set[v]
        return frozenset(s)

    def rule(self, j, C):
        # area 1: an edit to the rule is an edit that alters j and is no (single or composite) setting (H01, L57)
        return self.inv(j, self.world(j), C) and self.changes(j, self.alt[j] - self.set_oj(j) - self.slc[j], C)

    def upstream(self, v, w):
        """v ⇝ w (D3.3 as fixed in area 1): components j_1..j_n and ports u_1..u_n with v ∈ V_{j_1} ∖ {u_1},
        Out(u_i, j_i) for every i ≤ n, u_i ∈ V_{j_{i+1}} ∖ {u_{i+1}} for i < n, and u_n = w."""
        org = self.org
        # frontier of (port u reached as an output of some component, having entered from a port ≠ u)
        start = set()
        for j in org.comps:
            if v in org.foot[j]:
                for u in org.foot[j]:
                    if u != v and self.output(u, j):
                        start.add(u)
        seen, todo = set(start), list(start)
        while todo:
            u = todo.pop()
            for j in org.comps:
                if u in org.foot[j]:
                    for u2 in org.foot[j]:
                        if u2 != u and u2 not in seen and self.output(u2, j):
                            seen.add(u2)
                            todo.append(u2)
        return w in seen

    def families(self, C, reading):
        org = self.org
        return {
            "causal": sorted(j for j in org.comps if self.causal(j, C, reading)),
            "meas": sorted((j, m) for j in org.comps for m in org.foot[j] if self.meas(j, m, C, reading)),
            "rule": sorted(j for j in org.comps if self.rule(j, C)),
        }


# ---- kinds (D4.1-D4.3, I10, I12) --------------------------------------------------------------


def rename_rel(rel, perm):
    """β_*: a tuple w over (v_1..v_n) becomes w' over (u_1..u_n) with w'[perm[i]] = w[i]."""
    out = set()
    for w in rel:
        w2 = [None] * len(w)
        for i, x in enumerate(w):
            w2[perm[i]] = x
        out.add(tuple(w2))
    return frozenset(out)


def footprint_bijections(org1, j1, org2, j2):
    f1, f2 = org1.foot[j1], org2.foot[j2]
    if len(f1) != len(f2):
        return
    for perm in itertools.permutations(range(len(f2))):
        if all(set(org1.dom[f1[i]]) == set(org2.dom[f2[perm[i]]]) for i in range(len(f1))):
            yield perm


def sig_fn(org, j, C, through=None):
    """sig_C(j) as a function on C (D4.1); through a transport (tau, sigma) it is read at
    (tau(a), sigma(b)) (D4.3, I12)."""
    if through is None:
        return {(a, b): org.L(j, a, b) for (a, b) in C}
    tau, sigma = through
    return {(a, b): org.L(j, tau[a], sigma[b]) for (a, b) in C}


def one_kind(org1, j1, org2, j2, C, t1=None, t2=None, witness=False):
    s1, s2 = sig_fn(org1, j1, C, t1), sig_fn(org2, j2, C, t2)
    for perm in footprint_bijections(org1, j1, org2, j2):
        if all(rename_rel(s1[x], perm) == s2[x] for x in C):
            return perm if witness else True
    return None if witness else False


# ---- questions and queries (D3.1-D3.2, I20, I21) ---------------------------------------------


class PortQuery:
    """Q_w (D3.2): the single value of the projection of Sol on the designated port, else ⊥."""
    kind = "port"

    def __call__(self, org, a, b, delta):
        vals = set(z[org.ports.index(delta)] for z in org.sol(a, b))
        return next(iter(vals)) if len(vals) == 1 else BOT

    def __repr__(self):
        return "Q_w (reads the designated port)"


class FnQuery:
    """A query given as a function of (org, a, b, delta); used for the text's worked cases [I82]."""
    kind = "fn"

    def __init__(self, fn, name):
        self.fn, self.name = fn, name

    def __call__(self, org, a, b, delta):
        return self.fn(org, a, b, delta)

    def __repr__(self):
        return self.name


class Question:
    """p = (D, C, b0, Q, δ_D, O_p, ρ_p) (D3.1). Σ: Excl(Σ) ⊆ A × B (D3.5, I27); by default every
    pair outside C is excluded by the stated scope [I85]."""

    def __init__(self, D, C, b0, Q, deltaD, excl=None, name="p"):
        self.D, self.C, self.b0, self.Q, self.deltaD = D, frozenset(C), b0, Q, deltaD
        assert (ONE, b0) in self.C
        allpairs = frozenset((a, b) for a in D.A for b in D.B)
        self.excl = (allpairs - self.C) if excl is None else frozenset(excl)
        self.name = name

    def ans(self, a, b, D=None):
        return self.Q(D or self.D, a, b, self.deltaD)

    def with_C(self, C, excl=None, name=None):
        return Question(self.D, C, self.b0, self.Q, self.deltaD, excl, name or self.name + "'")

    def describe(self):
        return "question %s: target %s, b0 = %s, query %r designating %s, C = {%s}%s" % (
            self.name, self.D.name, self.b0, self.Q, self.deltaD,
            ", ".join("(%s,%s)" % x for x in sorted(self.C, key=repr)),
            "" if self.excl == frozenset((a, b) for a in self.D.A for b in self.D.B) - self.C else
            "; stated scope excludes {%s}" % ", ".join("(%s,%s)" % x for x in sorted(self.excl, key=repr)))


# ---- transports and candidates (D5.1-D5.3, I14, I16, I17, I81) --------------------------------


def ident(x):
    return x


class Translation:
    """A port translation for one port v of E: the D ports it reads and a value map. With one D port
    and a value map it is I14's θ_k(v) with κ_{k,v}; with several D ports it is a derived port [I81]."""

    def __init__(self, dports, fn=None, name=None):
        self.dports = tuple(dports)
        self.fn = fn or (lambda xs: xs[0])
        self.name = name or ("id(%s)" % ",".join(self.dports) if fn is None else "f(%s)" % ",".join(self.dports))

    def simple(self):
        return len(self.dports) == 1


class Candidate:
    """ℰ = (E, p, t, Γ, δ_E) (D5.3). t = (π, τ, σ, λ):
    pi: E port -> Translation (π induced by port translations, total on X_D) [I81];
    tau: D edit -> E edit (partial, a dict), sigma: D boundary -> E boundary (partial) [I17];
    lam: k -> (N_k frozenset of D comps, {v in V_k: Translation}) [I14]."""

    def __init__(self, E, p, pi, tau, sigma, lam, Gamma, deltaE, name="ℰ"):
        self.E, self.p, self.pi, self.tau, self.sigma, self.lam = E, p, dict(pi), dict(tau), dict(sigma), dict(lam)
        self.Gamma = tuple(Gamma)
        self.deltaE = deltaE
        self.name = name

    def replace(self, **kw):
        c = Candidate.__new__(Candidate)
        c.__dict__.update(self.__dict__)
        c.__dict__.update(kw)
        return c

    def translates(self, a, b):
        return a in self.tau and b in self.sigma

    def pi_of(self, D, z):
        d = D.as_dict(z)
        return tuple(self.pi[v].fn(tuple(d[u] for u in self.pi[v].dports)) for v in self.E.ports)

    def ans_E(self, a2, b2, E=None):
        return self.p.Q(E or self.E, a2, b2, self.deltaE)

    def describe(self):
        lines = ["candidate %s for %s: Γ = {%s}, δ_E = %s" % (self.name, self.p.name, ",".join(self.Gamma), self.deltaE)]
        lines.append("  π: " + "; ".join("%s := %s" % (v, self.pi[v].name) for v in self.E.ports))
        lines.append("  τ: " + ", ".join("%s↦%s" % kv for kv in self.tau.items()) + "; σ: " + ", ".join("%s↦%s" % kv for kv in self.sigma.items()))
        for k, (N, tr) in self.lam.items():
            lines.append("  λ(%s) = ({%s}, %s)" % (k, ",".join(sorted(N)), "; ".join("%s:=%s" % (v, tr[v].name) for v in self.E.foot[k])))
        lines.append(self.E.describe(pairs=sorted(set((self.tau[a], self.sigma[b]) for a in self.tau for b in self.sigma), key=repr)))
        return "\n".join(lines)


def proj_lam(cand, k, D, a, b):
    """proj^λ_{V_k}[Sol_{λ(k)}(a, b)] (D5.2)."""
    N, tr = cand.lam[k]
    VN, S = D.sol_sub(N, a, b)
    Vk = cand.E.foot[k]
    for v in Vk:
        for u in tr[v].dports:
            if u not in VN:
                return None  # the translation reads a port outside V_N: λ(k) is not a counterpart
    idx = {u: VN.index(u) for v in Vk for u in tr[v].dports}
    return frozenset(tuple(tr[v].fn(tuple(z[idx[u]] for u in tr[v].dports)) for v in Vk) for z in S)


# ---- fidelity and (A) (D5.4-D5.7) --------------------------------------------------------------


def F1_at(cand, a, b, D=None):
    D = D or cand.p.D
    E = cand.E
    for k in cand.Gamma:
        if proj_lam(cand, k, D, a, b) != E.L(k, cand.tau[a], cand.sigma[b]):
            return False
    return True


def F2eq_at(cand, a, b, D=None):
    D = D or cand.p.D
    img = frozenset(cand.pi_of(D, z) for z in D.sol(a, b))
    return img == cand.E.sol(cand.tau[a], cand.sigma[b])


def A_at(cand, a, b, D=None):
    return cand.ans_E(cand.tau[a], cand.sigma[b]) == cand.p.ans(a, b, D)


def hom(cand):
    """Hom(τ) (D5.5, I18). When a2·a1 is defined in D and lies outside dom τ, the clause fails
    [I84]."""
    D, E, tau = cand.p.D, cand.E, cand.tau
    if tau.get(ONE) != ONE:
        return False
    for a1 in tau:
        for a2 in tau:
            c = D.compose(a2, a1)
            if c is None:
                continue
            if c not in tau:
                return False
            r = E.compose(tau[a2], tau[a1])
            if r is None or r != tau[c]:
                return False
    return True


def translated_C(cand):
    return all(cand.translates(a, b) for (a, b) in cand.p.C)


def F1(cand):
    return translated_C(cand) and all(F1_at(cand, a, b) for (a, b) in cand.p.C)


def F2eq(cand):
    return translated_C(cand) and all(F2eq_at(cand, a, b) for (a, b) in cand.p.C)


def F2(cand):
    return F2eq(cand) and hom(cand)


def A(cand):
    return translated_C(cand) and all(A_at(cand, a, b) for (a, b) in cand.p.C)


def faithful(cand):
    """Faithful_C (D5.7, I49): the narrow extent."""
    return F1(cand) and F2(cand)


# ---- dependence, non-vacuity, Account (D6.1-D6.7) ----------------------------------------------
# S106 (decisions S44, S45): the written-in test, NC1 (no answer slot, D6.3), is taken out of (E). slot() and
# NC1() stay as defined notions criticism can point at (D6.3); the quantifier readings below now read Slot
# only. (E) is (F1) ∧ (F2) ∧ (A) ∧ Dep ∧ NonVacuous, Dep := NC0 ∧ NC2 (D6.5); account(reading="r3") keeps round 3's.


# Area 2 (S104 round 2 reading): D6.3 rewritten. NC1_READING = "area2" is I24 (b) with I83 (b):
# k is a slot when, at every pair of C at which the target's answer is determined (and there is one),
# every tuple of k's relation carries that answer on the answer port, whatever else it constrains
# (L255 with L273, L397). "registered" keeps the round-2 program's reading (I24 as registered, I83).
NC1_READING = "area2"

# S105 round 3, area 2 (W3; I136): the quantifier of Slot over Det_C. "every" is A2-02's choice (D6.3 as it
# stands, the default). "some": ∃ a determined pair (W3's proposal). "some-exempt": ∃ a determined pair at which
# τ(a) = 1 or τ(a) leaves k's relation as at 1 (a component the pair's own edit alters is exempt there; I136's
# third choice, G7-B5). "some-exempt-set": the same, exempt only where τ(a) sets δ_E through k (sets_through, D2.1).
# S105_SLOT_QUANTIFIER in the environment sets it for a whole-suite run; nothing else reads the environment.
# S106: the owner's answer to R3-Q1 (S44: "Neither"; S45: the test taken out) leaves the quantifier a reading of
# Slot alone; (E) no longer depends on it (account() under "S106" reads no slot).
import os as _os
SLOT_QUANTIFIERS = ("every", "some", "some-exempt", "some-exempt-set")
SLOT_QUANTIFIER = _os.environ.get("S105_SLOT_QUANTIFIER", "every")
assert SLOT_QUANTIFIER in SLOT_QUANTIFIERS

# S108 Part A, Sonnet 5.5 trial, section 2: the in-scope variants V2.1-V2.7 of the reply s108_glm_section2, each a
# switchable reading; the default (no variant on) is the round-4 definition. S108_S2 in the environment (a comma
# list) or S2_ON (a set, changed in the running process) turns them on; nothing else reads S108_S2. Record only; a
# variant is not a change to the theory (S40).
# V2.1 Dependence without loss: NC2 asks only for a contrast at a pair of C (no block, no Lost).
# V2.2 singleton block: the block G of NC2 is one commitment.
# V2.3 the witnessing pair has a different from 1 (a of the pair in C, the target side); V2.3b: tau(a) different from 1.
# V2.4 the written-in test back in (E): (E) read as round 3's (NC1 a conjunct), account reading "r3".
# V2.5 Sel with H empty allowed (claims_b.SEL_H_NONEMPTY off).
# V2.6 Conf only at pairs of the contract C of the first candidate's question.
# V2.7 ConfCl without its second disjunct (the candidate's answer only).
S2_VARIANTS = ("V2.1", "V2.2", "V2.3", "V2.3b", "V2.4", "V2.5", "V2.6", "V2.7")
S2_ON = set(x.strip() for x in _os.environ.get("S108_S2", "").split(",") if x.strip())
assert S2_ON <= set(S2_VARIANTS), sorted(S2_ON - set(S2_VARIANTS))


def slot(cand, k, reading=None, quantifier=None):
    """Slot_C(ℰ, k) (D6.3). Only for a port-reading query [I82]. Boundary coordinates are components here
    [I79]. reading "registered": exact slice at every pair, a ⊥ pair makes k no slot [I24, I83];
    reading "area2": [I24 (b), I83 (b); A2-01] — the relation by itself fixes the answer port to the
    target's answer at every pair of C where that answer is determined; the quantifier is A2-02."""
    reading = reading or NC1_READING
    p, E = cand.p, cand.E
    if getattr(p.Q, "kind", None) != "port":
        return False
    w = cand.deltaE
    if w not in E.foot[k]:
        return False
    if reading == "registered":
        for (a, b) in p.C:
            y = p.ans(a, b)
            if y is BOT:
                return False
            if E.L(k, cand.tau[a], cand.sigma[b]) != slice_rel(E, k, w, y):
                return False
        return True
    i = E.foot[k].index(w)
    det = [(a, b) for (a, b) in p.C if p.ans(a, b) is not BOT]
    if not det:
        return False
    q = quantifier or SLOT_QUANTIFIER
    if q == "every":
        for (a, b) in det:
            if not cand.translates(a, b):
                return False
            vals = set(t[i] for t in E.L(k, cand.tau[a], cand.sigma[b]))
            if vals != {p.ans(a, b)}:
                return False
        return True
    for (a, b) in det:  # "some", "some-exempt", "some-exempt-set" [S105 r3 A2: W3, I136]
        if not cand.translates(a, b):
            continue
        a2, b2 = cand.tau[a], cand.sigma[b]
        rel = E.L(k, a2, b2)
        if set(t[i] for t in rel) != {p.ans(a, b)}:
            continue
        if q == "some-exempt" and a2 != ONE and rel != E.L(k, ONE, b2):
            continue
        if q == "some-exempt-set" and a2 != ONE and sets_through(E, a2, b2, w, k):
            continue
        return True
    return False


def NC1(cand, reading=None, quantifier=None):
    return not any(slot(cand, k, reading, quantifier) for k in cand.E.comps)


# The owner's answers (S41, Q15): NC2's contrast is symmetric, "differs" in Y_p ∪ {⊥} with ⊥ ≠ y and ⊥ = ⊥,
# as D8.2 reads it; a determined answer at the edited point against ⊥ at the baseline counts. "round2" keeps
# D6.4 as written in round 2 (I22: a determined baseline asked; only ⊥ at the edited point counts).
CONTRAST_READINGS = ("S41", "round2")
CONTRAST_READING = "S41"


def contrast(ansx, ansx0, reading=None):
    """Contrast(E; x) (D6.4, I21) [owner S41: Q15]."""
    reading = reading or CONTRAST_READING
    if reading == "round2":
        return (ansx is not BOT and ansx0 is not BOT and ansx != ansx0) or (ansx is BOT and ansx0 is not BOT)
    return ansx != ansx0  # BOT equals only itself (I21)


def lost(cand, G, x, x0):
    E = cand.E
    EG = E.delete(G)
    ax, ax0 = cand.ans_E(*x, E=EG), cand.ans_E(*x0, E=EG)
    if ax is not BOT and ax0 is not BOT and ax == ax0:
        return True
    for y, ay in ((x, ax), (x0, ax0)):
        if cand.ans_E(*y) is not BOT and ay is BOT:
            return True
    return False


def NC2(cand, witness=False, reading=None):
    p = cand.p
    x0 = (ONE, cand.sigma[p.b0])
    a0 = cand.ans_E(*x0)
    blocks = [frozenset(G) for G in powerset(cand.Gamma) if G]
    if "V2.2" in S2_ON:  # S108 S2 V2.2: a block is one commitment
        blocks = [G for G in blocks if len(G) == 1]
    for (a, b) in sorted(p.C, key=repr):
        if "V2.3" in S2_ON and a == ONE:  # S108 S2 V2.3: the witnessing pair has a other than 1
            continue
        if "V2.3b" in S2_ON and cand.tau[a] == ONE:  # V2.3b: the transported edit other than 1
            continue
        x = (cand.tau[a], cand.sigma[b])
        if not contrast(cand.ans_E(*x), a0, reading):
            continue
        if "V2.1" in S2_ON:  # S108 S2 V2.1: a contrast at a pair is enough, no loss, no block
            return ((a, b), []) if witness else True
        for G in blocks:
            if lost(cand, G, x, x0):
                return ((a, b), sorted(G)) if witness else True
    return None if witness else False


def noncircular(cand):
    """Round 3's NonCircular: NC0 ∧ NC1 ∧ NC2 (D6.5 after round 3, I25); NC0 holds of every candidate (D6.2, I23).
    S106 (S44, S45): no longer a conjunct of (E); kept for the reading "r3" of account() and for comparison."""
    return NC1(cand) and NC2(cand)


def dep(cand):
    """Dep(ℰ) :⟺ NC0 ∧ NC2 (D6.5 after S106; I24's other choice (a), I25's 'NC2 alone'). NC0 holds of every
    candidate (D6.2, I23), so Dep is NC2: some contrast of E's answers at a pair of C is lost when a nonempty
    block of Γ is deleted (D6.4)."""
    return bool(NC2(cand))


def nonvacuous(cand):
    p = cand.p
    allpairs = frozenset((a, b) for a in p.D.A for b in p.D.B)
    return bool(p.D.sol(ONE, p.b0)) and (allpairs - p.C) <= p.excl


# S106 (decisions S44, S45): the written-in test (NC1, D6.3) is taken out of (E). ACCOUNT_READING "S106" is (E) as
# it now stands: (F1) ∧ (F2) ∧ (A) ∧ Dep ∧ NonVacuous (D6.7). "r3" keeps round 3's (E), with NC1 as a conjunct, for
# comparison only (the moved cases, s106_cases.py; a whole-suite run under it must reproduce round 3's results).
# S106_ACCOUNT_READING in the environment sets it for a whole-suite run; nothing else reads the environment.
ACCOUNT_READINGS = ("S106", "r3")
ACCOUNT_READING = _os.environ.get("S106_ACCOUNT_READING", "S106")
assert ACCOUNT_READING in ACCOUNT_READINGS


def account(cand, detail=False, reading=None):
    """Acc(ℰ) (E) (D6.7). With detail, the value of each conjunct. After S106 the conjuncts are F1, F2, A, Dep
    (= NC2, NC0 holding of every candidate) and NonVacuous; NC1 (no answer slot, D6.3) is still computed and
    reported in the detail, as content criticism can point at (D6.3), and is not a conjunct. reading "r3":
    round 3's (E), NC1 a conjunct."""
    reading = reading or ("r3" if "V2.4" in S2_ON else ACCOUNT_READING)  # S108 S2 V2.4: (E) with NC1 a conjunct
    d = {}
    d["translates C"] = translated_C(cand)
    if not d["translates C"]:
        d.update({"F1": False, "F2": False, "A": False, "NC1": False, "NC2": False, "Dep": False, "NonVacuous": nonvacuous(cand)})
    else:
        d["F1"] = F1(cand)
        d["F2eq"] = F2eq(cand)
        d["Hom"] = hom(cand)
        d["F2"] = d["F2eq"] and d["Hom"]
        d["A"] = A(cand)
        d["NC1"] = NC1(cand)
        d["NC2"] = NC2(cand)
        d["Dep"] = bool(d["NC2"])
        d["NonVacuous"] = nonvacuous(cand)
    keys = ("F1", "F2", "A", "NC1", "NC2", "NonVacuous") if reading == "r3" else ("F1", "F2", "A", "Dep", "NonVacuous")
    val = all(d[k] for k in keys)
    return (val, d) if detail else val


# ---- S106: a pin (D6.3: Slot's clause at one pair, I184) -------------------------------------------------------
# Content criticism can point at (S44, S45). Nothing here orders candidates, counts questions or grades (S20, S23).
# S106, second checker on the critical review (objection 1): D6.11 withdrawn. Its (a), Pin, is D6.3's clause; its (b), (c)
# are deleted with RelQuery, further_question and leaves_open (I185, I186): LeavesOpen read a candidate only through
# dom τ × dom σ, and 'the questions it leaves open' touches what hard to vary covers, parked (P8).


def pin(cand, k, a, b):
    """Pin(ℰ, k; a, b) (D6.3, Slot's clause at one pair; I184): (a, b) ∈ Det_C, t translates it, δ_E ∈ V_k, and k's relation at
    (τ(a), σ(b)) by itself fixes δ_E to Ans_p(a, b). Only for a port-reading query (I82). Slot_C(ℰ, k) under
    D6.3's 'every' is Pin at every pair of Det_C (Det_C ≠ ∅); 'some' is Pin at one pair."""
    p, E, w = cand.p, cand.E, cand.deltaE
    if getattr(p.Q, "kind", None) != "port" or w not in E.foot[k] or not cand.translates(a, b):
        return False
    y = p.ans(a, b)
    if y is BOT:
        return False
    i = E.foot[k].index(w)
    return set(t[i] for t in E.L(k, cand.tau[a], cand.sigma[b])) == {y}


def pins(cand):
    """Every (k, (a, b)) with Pin(ℰ, k; a, b), in a fixed order."""
    return [(k, (a, b)) for k in cand.E.comps for (a, b) in sorted(cand.p.C, key=repr) if pin(cand, k, a, b)]


# ---- restriction and routes (D7.1-D7.6, I29) ---------------------------------------------------


def restrict(cand, W):
    """E|W := E - (Γ ∖ W), λ restricted, commitments W (D7.1, I29)."""
    W = tuple(k for k in cand.Gamma if k in W)
    drop = [k for k in cand.Gamma if k not in W]
    E2 = cand.E.delete(drop) if drop else cand.E
    lam = {k: v for k, v in cand.lam.items() if k not in drop}
    return cand.replace(E=E2, Gamma=W, lam=lam, name=cand.name + "|{" + ",".join(W) + "}")


def routes(cand):
    """S_{E,p} (S)."""
    return frozenset(W for W in powerset(cand.Gamma) if account(restrict(cand, W)))


def critical_block(S, B, W):
    return bool(B) and B <= W and W in S and (W - B) not in S


def contributory(S, d):
    return any(critical_block(S, frozenset([d]), W) for W in S)


def indispensable(S, Gamma, d):
    return frozenset(Gamma) - {d} not in S


def no_work(S, d):
    return bool(S) and all((W | {d}) in S and (W - {d}) in S for W in S)


def minimal(S):
    return [W for W in S if not any(U < W for U in S)]


def boundary(family):
    """Boundary (D) (D7.4 after S107 round 4, area 2; N1): family maps each v of a declared family 𝒱 of organization edits
    to its candidate ℰ_v = (E_v, p, t_v, Γ_v, δ_v), δ_v the designation the operation carries δ_E to (R4A2-03), as t_v
    is the transport it carries t to and Γ_v the commitments it leaves (L231). Returns {(v, w) : Acc(ℰ_v) ≠ Acc(ℰ_w)}."""
    acc = {v: account(c) for v, c in family.items()}
    return frozenset((v, w) for v in family for w in family if acc[v] != acc[w])


# ---- conflict, rivals, claims (D8.1-D8.6, I19, I33-I36) ---------------------------------------


def meets_ab(cand, a, b, R):
    """Meets_ab(ℰ, R) (D8.1, I19): (F1), the valuation equation of (F2) and (A) at (a, b) with the
    target's relations there replaced by R."""
    D = cand.p.D.with_relations_at(a, b, R)
    return F1_at(cand, a, b, D) and F2eq_at(cand, a, b, D) and A_at(cand, a, b, D)


def all_R(D, limit=200000):
    """Every assignment of relations on the footprints (D8.1). A finite enumeration; refused past
    `limit` assignments [I77]."""
    choices = [list(powerset(D.full(j))) for j in D.comps]
    n = 1
    for c in choices:
        n *= len(c)
    if n > limit:
        raise ValueError("too many hypothetical relation assignments: %d" % n)
    for combo in itertools.product(*choices):
        yield dict(zip(D.comps, combo))


def meet_table(c1, c2, a, b):
    rows = []
    for R in all_R(c1.p.D):
        rows.append((meets_ab(c1, a, b, R), meets_ab(c2, a, b, R), R))
    return rows


def conflict(c1, c2, a, b, table=None, witness=False):
    """Conf(ℰ, ℰ'; a, b) (D8.2)."""
    if not (c1.translates(a, b) and c2.translates(a, b)):
        return False
    if "V2.6" in S2_ON and (a, b) not in c1.p.C:  # S108 S2 V2.6: conflict only inside the contract
        return False
    y1, y2 = c1.ans_E(c1.tau[a], c1.sigma[b]), c2.ans_E(c2.tau[a], c2.sigma[b])
    if y1 != y2:
        return ("answers differ", y1, y2) if witness else True
    rows = table if table is not None else meet_table(c1, c2, a, b)
    m1 = any(r[0] for r in rows)
    m2 = any(r[1] for r in rows)
    both = any(r[0] and r[1] for r in rows)
    if m1 and m2 and not both:
        return ("each can meet, no relations let both",) if witness else True
    return None if witness else False


def conf_given(c1, c2, a, b, allow, table=None):
    """ConfG_χ (D8.6, I35); allow(R) -> bool is Allow_χ(a, b) (I34)."""
    rows = table if table is not None else meet_table(c1, c2, a, b)
    both = [r[2] for r in rows if r[0] and r[1]]
    return bool(both) and all(not allow(R) for R in both)


CONFCL_READING = "area2"  # Area 2 [A2-03]: D8.5 with existence clauses; "registered" = the round-2 program


def conf_claim(cand, a, b, allow, reading=None, parts=False):
    """ConfCl(ℰ, χ; a, b) (D8.5, I34). Reading "area2" [A2-03]: first disjunct = some R gives ℰ's
    answer and every such R lies outside Allow_χ; second = some R lets ℰ meet and every such R lies
    outside Allow_χ (L315: 'where some relations ... would let it meet'). "registered": both vacuous."""
    reading = reading or CONFCL_READING
    D = cand.p.D
    y = cand.ans_E(cand.tau[a], cand.sigma[b])
    first = True
    second = True
    some_ans = False
    some_meet = False
    for R in all_R(D):
        if cand.p.ans(a, b, D.with_relations_at(a, b, R)) == y:
            some_ans = True
            if allow(R):
                first = False
        if meets_ab(cand, a, b, R):
            some_meet = True
            if allow(R):
                second = False
    if reading == "area2":
        first = first and some_ans
        second = second and some_meet
    if "V2.7" in S2_ON:  # S108 S2 V2.7: the second disjunct deleted
        second = False
    return (first, second) if parts else (first or second)


def all_pairs(D):
    return [(a, b) for a in D.A for b in D.B]


def conflict_pairs(c1, c2):
    return [x for x in all_pairs(c1.p.D) if conflict(c1, c2, *x)]


def rivals(c1, c2, offered=True, both_offered=True):
    """Riv (D8.3, I33): offered is the primitive Offered (one in place of the other, either way) [I86];
    both_offered: Off(ℰ,p) ∧ Off(ℰ',p), both among the candidates someone has offered (L315; area 2)."""
    return offered and both_offered and bool(conflict_pairs(c1, c2))


def problem_kind(c1, c2):
    cps = conflict_pairs(c1, c2)
    if not cps:
        return None
    C = c1.p.C
    if any(x in C for x in cps):
        return "i"
    return "ii"
