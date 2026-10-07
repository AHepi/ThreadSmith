# S104 round 2 (maths): arguments, usability, ruling out (formal core §9, D9.1-D9.9).
# Claims are propositional here [I87]; the inference forms are a small fixed set [I89]; X_j ranges
# over a finite set of arguments [I88]. Each tag names the invention in `inventions register.md`.
# The owner's answers (S41, Q23): a premise alone is an argument (D9.2); its conclusion is its claim; it is
# usable by j when j tentatively accepts it (D9.6, I166). ARG_READING "I88" keeps round 2's reading (a bare
# premise is no argument).
from . import s108r2_s4 as _R2S4  # S108 Part A round 2, section 4
import itertools

# ---- claims (D9.1, I38, I87) ---------------------------------------------------------------------


def Not(f):
    return ("not", f)


def And(*fs):
    return ("and",) + tuple(fs)


def Imp(f, g):
    return ("imp", f, g)


def atoms(f):
    if isinstance(f, str):
        return {f}
    s = set()
    for g in f[1:]:
        s |= atoms(g)
    return s


def ev(f, v):
    if isinstance(f, str):
        return v[f]
    if f[0] == "not":
        return not ev(f[1], v)
    if f[0] == "and":
        return all(ev(g, v) for g in f[1:])
    if f[0] == "imp":
        return (not ev(f[1], v)) or ev(f[2], v)
    raise ValueError(f)


def models(fs):
    ats = sorted(set().union(*[atoms(f) for f in fs])) if fs else []
    for vals in itertools.product([False, True], repeat=len(ats)):
        v = dict(zip(ats, vals))
        if all(ev(f, v) for f in fs):
            yield v


def consistent(fs):
    return next(models(fs), None) is not None


def incons(f, g):
    """Classical inconsistency of {f, g} (I38)."""
    return not consistent([f, g])


def canon(f):
    """The structural reading [I87]: double negations removed, conjunctions flattened and their
    conjuncts sorted. Logical equivalence is not used (L397)."""
    if isinstance(f, str):
        return f
    if f[0] == "not":
        g = canon(f[1])
        if isinstance(g, tuple) and g[0] == "not":
            return g[1]
        return ("not", g)
    if f[0] == "and":
        cs = []
        for g in f[1:]:
            g = canon(g)
            if isinstance(g, tuple) and g[0] == "and":
                cs.extend(g[1:])
            else:
                cs.append(g)
        cs = sorted(set(cs), key=repr)
        return cs[0] if len(cs) == 1 else ("and",) + tuple(cs)
    return (f[0],) + tuple(canon(g) for g in f[1:])


def conjuncts(f):
    f = canon(f)
    if isinstance(f, tuple) and f[0] == "and":
        return set(f[1:])
    return {f}


def denial(f):
    return canon(Not(f))


def show(f):
    if isinstance(f, str):
        return f
    if f[0] == "not":
        return "¬" + show(f[1])
    if f[0] == "and":
        return "(" + " ∧ ".join(show(g) for g in f[1:]) + ")"
    return "(" + show(f[1]) + " → " + show(f[2]) + ")"


# ---- argument trees (D9.2, I40, I88, I89) ---------------------------------------------------------


ARG_READINGS = ("S41", "I88")
ARG_READING = "S41"


class Leaf:
    def __init__(self, claim, kind="assumption", made_from=None):
        self.claim, self.kind, self.made_from = claim, kind, made_from

    @property
    def concl(self):
        """concl(α) for α a premise alone: the premise's claim (D9.2) [owner S41: Q23]."""
        return self.claim

    def steps(self):
        return []

    def leaves(self):
        return [self]

    def show(self, ind=0):
        return " " * ind + "%s leaf: %s%s" % (self.kind, show(self.claim), "" if self.made_from is None else " (made from %s)" % show(self.made_from))


def form_ok(form, prem, concl):
    """Whether a step instantiates its form [I89]. 'free' is any step (an admitted form need not be in
    Forms_cl, I38)."""
    c = canon(concl)
    P = [canon(x) for x in prem]
    if form == "free":
        return True
    if form == "MP":
        return len(P) == 2 and any(isinstance(P[i], tuple) and P[i][0] == "imp" and P[i][1] == P[1 - i] and P[i][2] == c for i in (0, 1))
    if form == "MT":
        if len(P) != 2:
            return False
        for i in (0, 1):
            imp, nb = P[i], P[1 - i]
            if isinstance(imp, tuple) and imp[0] == "imp" and nb == canon(Not(imp[2])) and c == canon(Not(imp[1])):
                return True
        return False
    if form == "AndI":
        return c == canon(("and",) + tuple(P))
    if form == "AndE":
        return len(P) == 1 and c in conjuncts(P[0])
    return False


class Step:
    def __init__(self, form, concl, children, index=("C", "l", "b")):
        self.form, self.concl, self.children, self.index = form, concl, list(children), index
        self.prem = [ch.claim if isinstance(ch, Leaf) else ch.concl for ch in self.children]  # all essential [I89]

    @property
    def claim(self):
        return self.concl

    def steps(self):
        out = [self]
        for ch in self.children:
            out.extend(ch.steps())
        return out

    def below(self):
        out = []
        for ch in self.children:
            out.extend(ch.steps())
        return out

    def leaves(self):
        out = []
        for ch in self.children:
            out.extend(ch.leaves())
        return out

    def show(self, ind=0):
        s = [" " * ind + "step [%s] ⊢ %s" % (self.form, show(self.concl))]
        for ch in self.children:
            s.append(ch.show(ind + 2))
        return "\n".join(s)


class Assessor:
    """j: Forms_j, Accepted_j (at one time ξ, I41), the scope j declares [I42]."""

    def __init__(self, forms, accepted, scope=("C", "l", "b")):
        self.forms = set(forms)
        self.accepted = set(canon(x) for x in accepted)
        self.scope = scope

    def scope_ok(self, u):
        Cu, lu, bu = u.index
        Cj, lj, bj = self.scope
        if isinstance(Cu, frozenset) and isinstance(Cj, frozenset):
            cok = Cu <= Cj
        else:
            cok = Cu == Cj
        return cok and lu == lj and bu == bj


def usable_step(j, u, memo=None):
    """(K2) with Live through a step strictly below u (D9.4, D9.6, I40): recursion on height."""
    memo = {} if memo is None else memo
    if _R2S4.VARIANT == "R2V4.7":
        return False  # S108 Part A round 2, R2V4.7: no declared input, no usable step
    if id(u) in memo:
        return memo[id(u)]
    ok = u.form in j.forms and form_ok(u.form, u.prem, u.concl) and j.scope_ok(u)
    if ok:
        below = u.below()
        for d in u.prem:
            cd = canon(d)
            live = any(canon(v.concl) == cd and usable_step(j, v, memo) for v in below) or cd in j.accepted
            if not live:
                ok = False
                break
    memo[id(u)] = ok
    return ok


def usable(j, alpha, reading=None):
    """Usable_j(α) (D9.6). A premise alone d [owner S41: Q23] is usable by j when d ∈ Accepted_j(ξ), Live_j with
    no step (I166); under ARG_READING "I88" (round 2) it is no argument."""
    if _R2S4.VARIANT == "R2V4.7":
        return False  # S108 Part A round 2, R2V4.7: nothing accepted, no form admitted
    if isinstance(alpha, Leaf):
        if (reading or ARG_READING) == "I88":
            return False  # round 2: an argument has at least one step [I88]
        return canon(alpha.claim) in j.accepted  # [I166]
    memo = {}
    return all(usable_step(j, u, memo) for u in alpha.steps())


def usable_any_step(j, alpha):
    """I40's alternative: Live through any step of the argument. Returns the least and the greatest
    fixed point of the usability operator (FC69)."""
    steps = alpha.steps()

    def F(U):
        out = set()
        for u in steps:
            if not (u.form in j.forms and form_ok(u.form, u.prem, u.concl) and j.scope_ok(u)):
                continue
            if all(any(canon(v.concl) == canon(d) and id(v) in U for v in steps) or canon(d) in j.accepted for d in u.prem):
                out.add(id(u))
        return out

    lo = set()
    while True:
        n = F(lo)
        if n == lo:
            break
        lo = n
    hi = set(id(u) for u in steps)
    while True:
        n = F(hi)
        if n == hi:
            break
        hi = n
    return lo, hi


def rules_out(alpha, phi):
    """RO(α, φ) (D9.7, I39, I87); α may be a premise alone, whose conclusion is its claim [owner S41: Q23]."""
    if not incons(phi, alpha.concl):
        return False
    d = denial(phi)
    for lf in alpha.leaves():
        if d in conjuncts(lf.claim):
            return False
        if lf.kind == "record" and lf.made_from is not None and denial(lf.made_from) == canon(phi):
            return False
    return True


def X(j, phi, args):
    """X_j(φ) over a finite set of arguments [I88]."""
    return [a for a in args if usable(j, a) and rules_out(a, phi)]


def enumerate_args(premises, forms=("MP", "MT", "AndI", "AndE"), depth=2, max_args=4000, bare=None):
    """Every argument tree of height ≤ depth over the given premise leaves with the given forms [I88]; with
    the premises alone among them (height 0) [owner S41: Q23], unless bare is False or ARG_READING is "I88"."""
    layer = [Leaf(p) for p in premises]
    allnodes = list(layer)
    if bare is None:
        bare = ARG_READING != "I88"
    out = []
    for _ in range(depth):
        new = []
        for form in forms:
            if form in ("MP", "MT", "AndI"):
                for x, y in itertools.permutations(allnodes, 2):
                    px, py = x.claim, y.claim
                    concl = None
                    if form == "MP" and isinstance(canon(py), tuple) and canon(py)[0] == "imp" and canon(py)[1] == canon(px):
                        concl = canon(py)[2]
                    if form == "MT" and isinstance(canon(py), tuple) and canon(py)[0] == "imp" and canon(px) == canon(Not(canon(py)[2])):
                        concl = canon(Not(canon(py)[1]))
                    if form == "AndI" and repr(canon(px)) < repr(canon(py)):
                        concl = canon(And(px, py))
                    if concl is not None:
                        new.append(Step(form, concl, [x, y]))
            if form == "AndE":
                for x in allnodes:
                    for c in conjuncts(x.claim):
                        if canon(x.claim) != c:
                            new.append(Step("AndE", c, [x]))
        new = new[:max_args]
        out.extend(new)
        allnodes.extend(new)
        if len(out) >= max_args:
            break
    return (list(layer) + out) if bare else out  # the stepped arguments are those of round 2; the premises alone are added
