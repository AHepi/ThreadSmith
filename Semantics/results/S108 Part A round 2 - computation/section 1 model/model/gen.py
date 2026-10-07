# S104 round 2 (maths): seeded generators of small finite organizations, questions and candidates.
# The search spaces, their bounds and both generator families are inventions of this program
# (I77, I78, I79, I81, I85); every result that uses them says so.
import itertools
import random

from .core import (ONE, Org, Question, PortQuery, Candidate, Translation, powerset, slice_rel, BOT)


# ---- sizes (I77) ---------------------------------------------------------------------------------

class Size:
    """A point of the search space: ports, largest domain, components, boundaries, generator edits."""

    def __init__(self, nports, dmax, ncomps, nB, nedits):
        self.nports, self.dmax, self.ncomps, self.nB, self.nedits = nports, dmax, ncomps, nB, nedits

    def total(self):
        return self.nports + self.dmax + self.ncomps + self.nB + self.nedits

    def __repr__(self):
        return "ports=%d dom≤%d comps=%d |B|=%d edits=%d" % (self.nports, self.dmax, self.ncomps, self.nB, self.nedits)

    def as_dict(self):
        return dict(ports=self.nports, dom_max=self.dmax, comps=self.ncomps, boundaries=self.nB, generator_edits=self.nedits)


def sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2, min_ports=1):
    out = []
    for n in range(min_ports, max_ports + 1):
        for d in range(1, max_dom + 1):
            for c in range(1, max_comps + 1):
                for nb in range(1, max_B + 1):
                    for ne in range(0, max_edits + 1):
                        out.append(Size(n, d, c, nb, ne))
    out.sort(key=lambda s: (s.total(), s.nports, s.dmax, s.ncomps, s.nB, s.nedits))
    return out


def rand_rel(rng, full, density=0.5):
    full = sorted(full)
    return frozenset(w for w in full if rng.random() < density)


# ---- family G-surg: surgical edits with override composition (I78) -----------------------------

def gen_surg(rng, size, name="D", cycles=True, dvar=True):
    """Ports p0.., each with a home component h_v (footprint v plus up to two parents); optional extra
    constraint components; edits = closure under override of up to `nedits` generators (a setting of a
    port to a value, or an alternative relation of a component). L at an edit is the surgery applied:
    the home component of a set port gets the slice v = x (D2.1), an altered component its alternative
    relation, every other its base relation (an action law: I02's alternative, recorded as I78)."""
    n, dmax = size.nports, size.dmax
    ports = ["p%d" % i for i in range(n)]
    dom = {v: tuple(range(rng.randint(1, dmax) if dvar else dmax)) for v in ports}
    B = ["b%d" % i for i in range(size.nB)]
    comps, foot = [], {}
    home = {}
    ncomp = max(1, size.ncomps)
    # home components for the first min(n, ncomp) ports; the rest are extra constraints
    for i, v in enumerate(ports[:ncomp]):
        others = [u for u in ports if u != v and (cycles or ports.index(u) < i)]
        par = rng.sample(others, min(len(others), rng.randint(0, 2)))
        j = "h_" + v
        comps.append(j)
        foot[j] = tuple(sorted([v] + par, key=ports.index))
        home[j] = v
    for i in range(ncomp - len(comps)):
        j = "k%d" % i
        fp = rng.sample(ports, min(n, rng.randint(1, 2)))
        comps.append(j)
        foot[j] = tuple(sorted(fp, key=ports.index))
    base, alt = {}, {}

    def full(j):
        return frozenset(itertools.product(*[dom[v] for v in foot[j]]))

    for j in comps:
        for b in B:
            if j in home and rng.random() < 0.7:
                # functional in the home port given the others
                v = home[j]
                i = foot[j].index(v)
                others = [u for u in foot[j] if u != v]
                rel = set()
                for rest in itertools.product(*[dom[u] for u in others]):
                    x = rng.choice(dom[v])
                    w = list(rest)
                    w.insert(i, x)
                    rel.add(tuple(w))
                base[(j, b)] = frozenset(rel)
            else:
                base[(j, b)] = rand_rel(rng, full(j), rng.choice([0.4, 0.6, 0.8]))
    # generator edits
    gens = []
    for _ in range(size.nedits):
        if rng.random() < 0.7 and home:
            j = rng.choice(sorted(home))
            v = home[j]
            gens.append(("set", v, rng.choice(dom[v])))
        else:
            j = rng.choice(comps)
            gens.append(("alt", j, None))
            for b in B:
                alt[(j, b)] = rand_rel(rng, full(j), rng.choice([0.4, 0.6]))
    # closure under override
    def canon(sm, am):
        return (tuple(sorted(sm.items())), tuple(sorted(am)))

    def label(key):
        sm, am = key
        if not sm and not am:
            return ONE
        parts = ["%s=%s" % kv for kv in sm] + ["alt:%s" % j for j in am]
        return "[" + ",".join(parts) + "]"

    start = canon({}, set())
    gen_keys = []
    for g in gens:
        if g[0] == "set":
            gen_keys.append(canon({g[1]: g[2]}, set()))
        else:
            gen_keys.append(canon({}, {g[1]}))
    keys = {start}
    frontier = [start]

    def over(k2, k1):
        sm = dict(k1[0])
        sm.update(dict(k2[0]))
        am = set(k1[1]) | set(k2[1])
        return canon(sm, am)

    while frontier:
        k = frontier.pop()
        for g in gen_keys:
            for kk in (over(g, k), over(k, g)):
                if kk not in keys:
                    keys.add(kk)
                    frontier.append(kk)
    keys = sorted(keys, key=lambda k: (len(k[0]) + len(k[1]), repr(k)))
    lab = {k: label(k) for k in keys}
    inv = {lab[k]: k for k in keys}
    A = [lab[k] for k in keys]

    def compose(a2, a1):
        return lab[over(inv[a2], inv[a1])]

    def Lfun(j, a, b):
        sm, am = inv[a]
        sm = dict(sm)
        if j in home and home[j] in sm:
            v = home[j]
            i = foot[j].index(v)
            return frozenset(w for w in full(j) if w[i] == sm[v])
        if j in am:
            return alt[(j, b)]
        return base[(j, b)]

    return Org(name, ports, dom, comps, foot, B, A, compose, Lfun, meta=dict(family="G-surg", home=home))


# ---- family G-free: abstract edits, only compositions with 1 defined, arbitrary relations --------

def gen_free(rng, size, name="D", dvar=True):
    n, dmax = size.nports, size.dmax
    ports = ["p%d" % i for i in range(n)]
    dom = {v: tuple(range(rng.randint(1, dmax) if dvar else dmax)) for v in ports}
    comps = ["c%d" % i for i in range(max(1, size.ncomps))]
    foot = {j: tuple(sorted(rng.sample(ports, min(n, rng.randint(1, 2))), key=ports.index)) for j in comps}
    B = ["b%d" % i for i in range(size.nB)]
    A = [ONE] + ["e%d" % i for i in range(1, size.nedits + 1)]
    table = {}

    def full(j):
        return frozenset(itertools.product(*[dom[v] for v in foot[j]]))

    for j in comps:
        for b in B:
            table[(j, ONE, b)] = rand_rel(rng, full(j), rng.choice([0.5, 0.7, 1.0]))
        for a in A[1:]:
            for b in B:
                r = rng.random()
                if r < 0.4:
                    table[(j, a, b)] = table[(j, ONE, b)]
                elif r < 0.7:
                    v = rng.choice(foot[j])
                    table[(j, a, b)] = slice_rel_raw(foot[j], full(j), v, rng.choice(dom[v]))
                else:
                    table[(j, a, b)] = rand_rel(rng, full(j), 0.5)

    def compose(a2, a1):
        return None

    return Org(name, ports, dom, comps, foot, B, A, compose, lambda j, a, b: table[(j, a, b)], meta=dict(family="G-free"))


def slice_rel_raw(fp, full, v, x):
    i = fp.index(v)
    return frozenset(w for w in full if w[i] == x)


def gen_org(rng, size, family=None, name="D"):
    fam = family or rng.choice(["G-surg", "G-free"])
    return gen_surg(rng, size, name) if fam == "G-surg" else gen_free(rng, size, name)


# ---- questions ---------------------------------------------------------------------------------

def gen_question(rng, D, name="p", full_C=False):
    """A port-reading question on D: a random designated port, b0 a random boundary, C the baseline
    plus a random set of pairs (or every pair). The stated scope excludes every pair outside C [I85]."""
    b0 = rng.choice(D.B)
    pairs = [(a, b) for a in D.A for b in D.B if (a, b) != (ONE, b0)]
    if full_C:
        C = [(ONE, b0)] + pairs
    else:
        C = [(ONE, b0)] + [x for x in pairs if rng.random() < 0.5]
    w = rng.choice(D.ports)
    return Question(D, C, b0, PortQuery(), w, name=name)


def _gen_variant():
    """S108 section 1: the reading of D1.4 the generator's encodings use: the variant's under S108_S1_GEN 'follow',
    the reading after round 4 under 'fixed' (so the same candidates are built with the variant off and on)."""
    from . import core as _core
    return None if _core.S108_S1_GEN == "follow" else "none"


# ---- candidates (I81) ----------------------------------------------------------------------------

def _E_from_lam(D, name, Eports, Edom, groups, trans, extra, A=None, compose=None, B=None, tau=None, sigma=None, perturb=None, rng=None):
    """E whose components are the projections of D's subnetworks (an encoding candidate, I32's E_enc),
    optionally with background components and one perturbed relation."""
    comps, foot = [], {}
    for k, (N, fp) in groups.items():
        comps.append(k)
        foot[k] = fp
    for k, (fp, rel) in extra.items():
        comps.append(k)
        foot[k] = fp
    A = list(A or D.A)
    B = list(B or D.B)
    tau = tau or {a: a for a in D.A}
    sigma = sigma or {b: b for b in D.B}
    inv_tau = {}
    for a, a2 in tau.items():
        inv_tau.setdefault(a2, a)
    inv_sigma = {}
    for b, b2 in sigma.items():
        inv_sigma.setdefault(b2, b)
    table = {}
    for k, (N, fp) in groups.items():
        VN, _ = D.sol_sub(N, ONE, D.B[0], variant=_gen_variant())
        for a2 in A:
            for b2 in B:
                a, b = inv_tau.get(a2), inv_sigma.get(b2)
                if a is None or b is None:
                    table[(k, a2, b2)] = frozenset(itertools.product(*[Edom[v] for v in fp]))
                    continue
                VN, S = D.sol_sub(N, a, b, variant=_gen_variant())
                idx = {u: VN.index(u) for v in fp for u in trans[v].dports}
                table[(k, a2, b2)] = frozenset(tuple(trans[v].fn(tuple(z[idx[u]] for u in trans[v].dports)) for v in fp) for z in S)
    for k, (fp, rel) in extra.items():
        for a2 in A:
            for b2 in B:
                table[(k, a2, b2)] = rel
    if perturb is not None and rng is not None and groups:
        k = rng.choice(sorted(groups))
        a2, b2 = rng.choice(A), rng.choice(B)
        fullk = frozenset(itertools.product(*[Edom[v] for v in foot[k]]))
        w = rng.choice(sorted(fullk))
        table[(k, a2, b2)] = table[(k, a2, b2)] ^ {w}
    return Org(name, Eports, Edom, comps, foot, B, A, compose or D._compose, lambda j, a, b: table[(j, a, b)], meta=dict(family="E_enc"))


def gen_candidate(rng, p, name="ℰ", valuemaps=False, perturb_p=0.3, background_p=0.3, keep_all_ports_p=0.5,
                  demote_p=0.2, random_tau_p=0.1):
    """A candidate built from p's target: E's ports a subset of D's (optionally recoded by value maps),
    its components the projections of groups of D's components, τ and σ the identity (or, with a small
    probability, random), with background components and one perturbed relation at random [I81]."""
    D = p.D
    if rng.random() < keep_all_ports_p:
        Eports = list(D.ports)
    else:
        Eports = [v for v in D.ports if rng.random() < 0.6 or v == p.deltaD]
    Edom, trans = {}, {}
    for v in Eports:
        if valuemaps and rng.random() < 0.5 and len(D.dom[v]) > 1:
            m = rng.randint(1, len(D.dom[v]))
            kmap = {x: rng.randrange(m) for x in D.dom[v]}
            Edom[v] = tuple(sorted(set(kmap.values())))
            trans[v] = Translation((v,), (lambda km: (lambda xs: km[xs[0]]))(kmap), name="κ%s(%s)" % (dict(sorted(kmap.items())), v))
        else:
            Edom[v] = D.dom[v]
            trans[v] = Translation((v,))
    comps = list(D.comps)
    rng.shuffle(comps)
    used = [j for j in comps if rng.random() < 0.9]
    groups = {}
    i = 0
    while used:
        g = used[:rng.randint(1, len(used))]
        used = used[len(g):]
        fp = tuple(v for v in Eports if v in D.ports_of(g))
        groups["k%d" % i] = (frozenset(g), fp)
        i += 1
    extra = {}
    if rng.random() < background_p:
        fp = tuple(sorted(rng.sample(Eports, min(len(Eports), rng.randint(1, 2))), key=Eports.index))
        full = frozenset(itertools.product(*[Edom[v] for v in fp]))
        extra["bg"] = (fp, rand_rel(rng, full, rng.choice([0.5, 1.0])))
    tau, sigma = {a: a for a in D.A}, {b: b for b in D.B}
    if rng.random() < random_tau_p:
        tau = {a: (ONE if a == ONE else rng.choice(D.A)) for a in D.A}
    E = _E_from_lam(D, "E_" + name, Eports, Edom, groups, trans, extra, perturb=(True if rng.random() < perturb_p else None), rng=rng)
    if rng.random() < random_tau_p:
        # τ perturbed after E is built from the identity: a transport that reads the wrong edit
        tau = {a: (ONE if a == ONE else rng.choice(D.A)) for a in D.A}
    lam = {k: (N, {v: trans[v] for v in fp}) for k, (N, fp) in groups.items()}
    pi = {v: trans[v] for v in Eports}
    Gamma = [k for k in groups if rng.random() > demote_p] or list(groups)[:1]
    deltaE = p.deltaD if p.deltaD in Eports else rng.choice(Eports)
    return Candidate(E, p, pi, tau, sigma, lam, Gamma, deltaE, name=name)


def gen_lookup(rng, p, name="ℰ_lk", background=True):
    """E_lk (FC23): one commitment k on the answer port whose relation at each pair is the answer slot
    for Ans_p(a, b) (full where Ans_p is ⊥), plus random background components [I81, I83]."""
    D = p.D
    w = p.deltaD
    others = [v for v in D.ports if v != w and rng.random() < 0.5]
    Eports = [v for v in D.ports if v == w or v in others]
    Edom = {v: D.dom[v] for v in Eports}
    comps = ["k"]
    foot = {"k": (w,)}
    extra = {}
    if background and others and rng.random() < 0.7:
        fp = tuple(rng.sample(others, min(len(others), rng.randint(1, 2))))
        full = frozenset(itertools.product(*[Edom[v] for v in fp]))
        extra["bg"] = (fp, rand_rel(rng, full, rng.choice([0.0, 0.5, 1.0])))
        comps.append("bg")
        foot["bg"] = fp
    table = {}
    for a in D.A:
        for b in D.B:
            y = p.ans(a, b)
            table[("k", a, b)] = frozenset((x,) for x in D.dom[w]) if y is BOT else frozenset([(y,)])
            if "bg" in extra:
                table[("bg", a, b)] = extra["bg"][1]
    E = Org("E_lk", Eports, Edom, comps, foot, D.B, D.A, D._compose, lambda j, a, b: table[(j, a, b)], meta=dict(family="lookup"))
    N = frozenset(D.comps)
    lam = {"k": (N, {w: Translation((w,))})}
    pi = {v: Translation((v,)) for v in Eports}
    return Candidate(E, p, pi, {a: a for a in D.A}, {b: b for b in D.B}, lam, ["k"], w, name=name)


def gen_random_candidate(rng, p, size, name="ℰ_r"):
    """A candidate whose organization is drawn at random over some of D's ports, with random τ, σ, λ."""
    D = p.D
    E = gen_free(rng, Size(len(D.ports), size.dmax, size.ncomps, len(D.B), max(0, len(D.A) - 1)), name="E_r", dvar=False)
    # give E D's port names and domains
    ports = list(D.ports)
    dom = dict(D.dom)
    comps = list(E.comps)
    foot = {j: tuple(sorted(rng.sample(ports, min(len(ports), rng.randint(1, 2))), key=ports.index)) for j in comps}
    table = {}
    for j in comps:
        full = frozenset(itertools.product(*[dom[v] for v in foot[j]]))
        for a in D.A:
            for b in D.B:
                table[(j, a, b)] = rand_rel(rng, full, rng.choice([0.5, 0.8, 1.0]))
    E2 = Org("E_r", ports, dom, comps, foot, D.B, D.A, D._compose, lambda j, a, b: table[(j, a, b)], meta=dict(family="random"))
    lam = {}
    for k in comps:
        # a counterpart whose ports cover k's footprint where D allows it (a well-formed λ, I14)
        N = set(rng.sample(list(D.comps), rng.randint(0, len(D.comps))))
        for v in foot[k]:
            if v not in D.ports_of(N):
                cov = [j for j in D.comps if v in D.foot[j]]
                if cov:
                    N.add(rng.choice(cov))
        lam[k] = (frozenset(N), {v: Translation((v,)) for v in foot[k]})
    Gamma = [k for k in comps if rng.random() < 0.7] or comps[:1]
    tau = {a: (ONE if a == ONE else rng.choice(D.A)) for a in D.A}
    sigma = {b: rng.choice(D.B) for b in D.B}
    sigma[p.b0] = sigma[p.b0]
    return Candidate(E2, p, {v: Translation((v,)) for v in ports}, tau, sigma, lam, Gamma, p.deltaD, name=name)


def any_candidate(rng, p, size, name="ℰ", valuemaps=False):
    r = rng.random()
    if r < 0.6:
        return gen_candidate(rng, p, name=name, valuemaps=valuemaps)
    if r < 0.8:
        return gen_random_candidate(rng, p, size, name=name)
    return gen_lookup(rng, p, name=name)


def rename_org(org, rng, suffix="'"):
    """An isomorphic copy: ports, components, boundaries and edits renamed by bijections (D18.2, I70)."""
    pm = {v: "q%d%s" % (i, suffix) for i, v in enumerate(rng.sample(list(org.ports), len(org.ports)))}
    cm = {j: "j%d%s" % (i, suffix) for i, j in enumerate(rng.sample(list(org.comps), len(org.comps)))}
    bm = {b: "B%d%s" % (i, suffix) for i, b in enumerate(org.B)}
    am = {a: (ONE if a == ONE else "E%d%s" % (i, suffix)) for i, a in enumerate(org.A)}
    icm = {v: k for k, v in cm.items()}
    ibm = {v: k for k, v in bm.items()}
    iam = {v: k for k, v in am.items()}
    ports = [pm[v] for v in org.ports]
    dom = {pm[v]: org.dom[v] for v in org.ports}
    comps = [cm[j] for j in org.comps]
    foot = {cm[j]: tuple(pm[v] for v in org.foot[j]) for j in org.comps}

    def compose(a2, a1):
        c = org.compose(iam[a2], iam[a1])
        return None if c is None else am[c]

    def Lfun(j, a, b):
        return org.L(icm[j], iam[a], ibm[b])

    o = Org(org.name + suffix, ports, dom, comps, foot, [bm[b] for b in org.B], [am[a] for a in org.A], compose, Lfun, meta=dict(org.meta))
    return o, pm, cm, bm, am
