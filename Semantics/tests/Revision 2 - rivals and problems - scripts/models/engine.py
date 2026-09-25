#!/usr/bin/env python3
"""engine.py - a finite implementation of draft 3's Account (E), adapted from
'Revision 2 - does correction stick - model scripts/attack/fe.py', and of the drafted
definitions of W59.1 (rival, conflict, established, fits, problem for p, kinds (i) and (ii),
easy to vary) and W60.1 (a failed answer stays failed).

What is kept from fe.py
  Organization  ports (name -> domain) and components (name -> (footprint, relation)).
                Sol(x) = valuations satisfying every live component (O). The pair x sets ports.
                A DELETED component imposes the full relation on its ports (Part II).
                New here: an edit that sets a port replaces the component assigning it (Part II,
                D3:L103); the assigned port of a component is the LAST port of its footprint.
  Query         Ans(x) = the set of values of the query port across Sol(x).
  (A)           Ans_E(tau(x)) = Ans_D(x).
  (F2)          pi[Sol_D(x)] = Sol_E(tau(x)).
  (F1)          for every active component k: the projection of Sol of its anchor subnetwork
                (all other D components deleted) onto the translated ports equals k's relation
                under the translated edit.
  NonCircular   D3:L255, third sentence, as in fe.py (the first two sentences are not modelled).
  NonVacuous    Sol_D(b0) nonempty.

What is new (the draft's definitions, W59.1)
  one_account   Derivation 2 (ii)'s relation, as W59.1's parenthesis gives it: a bijection of active
                components pairing each k with a component of one anchor (the same D components,
                port translations onto the same D ports) and one kind on C (relations under each
                pair of C coincide under the footprint bijection read through the translations),
                and one answer profile on C.
  rivals        same question; offered in place of each other (a fact of history, supplied by the
                model); and not one account.
  conflict      at x: WHATEVER THE TARGET'S RELATIONS THERE, not both meet (F1), (F2), (A) there.
                "The target's relations there" = the relation of each D component at x; they are
                varied independently per pair (Derivation 3's proof: "supplied independently for
                each (a,b)"). The space is 'all' (every subset of the component's tuples that agree
                with the pair) or 'functional' (the assigned port a function of the rest).
                Reported with two extra bits: can1 / can2 = some target relation lets that
                candidate alone meet the three there. A conflict with can1 and can2 is PROPER;
                one where either cannot meet the three there whatever the target is DEGENERATE.
  established   a dict pair -> ('ans', value)  the target's answer there (a usable receipt), or
                                 ('full', rels) the target's relations there (rels None = actual).
  fits          no established result shows the candidate failing a condition of (E): the answer
                matches every established answer, and (F1), (F2), (A) hold at every pair whose
                relations are established. NonCircular is reported separately, and `fits(...,
                nc=True)` also requires it (the draft does not say whether a derivation from the
                candidate alone counts as an established result).
  problem       two rivals that both fit. Kind (i) if they conflict at some pair of C, else (ii).
  test solves   a test at x establishes what the target does there; it solves the problem
                "whatever it shows" if for EVERY target relation at x at most one still fits.
                Checked in two modes: 'full' (the relations are established) and 'ans' (only the
                answer is).
No function below lists, counts or grades rivals. Families of candidates appear only in the model
scripts, as test harnesses for universal claims (every candidate that ... ).
Standard library only.
"""
from itertools import product, combinations, permutations


def key(x):
    return tuple(sorted(x.items()))


class Org:
    def __init__(self, name, ports, comps):
        self.name = name
        self.ports = dict(ports)
        self.comps = dict(comps)            # cname -> (footprint tuple, frozenset of tuples)

    def live(self, x, deleted=(), only=None, rels=None):
        out = []
        for c, (fp, rel) in self.comps.items():
            if c in deleted:
                continue
            if only is not None and c not in only:
                continue
            if fp[-1] in x:                 # the edit sets the port this component assigns
                continue
            r = rels[c] if (rels is not None and c in rels) else rel
            out.append((fp, r))
        return out

    def sol(self, x, deleted=(), only=None, rels=None):
        fixed = {p: v for p, v in x.items() if p in self.ports}
        free = [p for p in self.ports if p not in fixed]
        lv = self.live(fixed, deleted, only, rels)
        res = []
        for vals in product(*(self.ports[p] for p in free)):
            z = dict(fixed)
            z.update(zip(free, vals))
            if all(tuple(z[p] for p in fp) in r for fp, r in lv):
                res.append(z)
        return res

    def ans(self, x, q, deleted=(), rels=None):
        return frozenset(z[q] for z in self.sol(x, deleted=deleted, rels=rels))

    def rel_under(self, c, x):
        """Component c's relation under the edit x (tuples agreeing with the ports x sets; if x sets
        the port c assigns, c is replaced and the relation is the full one with that port fixed)."""
        fp, rel = self.comps[c]
        if fp[-1] in x:
            doms = [(x[p],) if p in x else self.ports[p] for p in fp]
            return frozenset(product(*doms))
        return frozenset(t for t in rel if all(t[i] == x[p] for i, p in enumerate(fp) if p in x))


class Target:
    def __init__(self, org, q):
        self.org, self.q = org, q

    def ans(self, x, rels=None):
        return self.org.ans(x, self.q, rels=rels)

    def variants(self, x, space='all'):
        """Every assignment of relations to the target's components at the pair x."""
        per = []
        for c, (fp, rel) in self.org.comps.items():
            if fp[-1] in x:                 # replaced by the edit: its relation is fixed by it
                per.append((c, [rel]))
                continue
            doms = [(x[p],) if p in x else self.org.ports[p] for p in fp]
            lt = list(product(*doms))
            if space == 'all':
                opts = [frozenset(s) for r in range(len(lt) + 1) for s in combinations(lt, r)]
            else:
                groups = {}
                for t in lt:
                    groups.setdefault(t[:-1], []).append(t)
                opts = [frozenset(ch) for ch in product(*groups.values())]
            per.append((c, opts))
        names = [c for c, _ in per]
        for combo in product(*(o for _, o in per)):
            yield dict(zip(names, combo))

    def n_variants(self, x, space='all'):
        n = 1
        for c, (fp, rel) in self.org.comps.items():
            if fp[-1] in x:
                continue
            doms = [(x[p],) if p in x else self.org.ports[p] for p in fp]
            lt = list(product(*doms))
            if space == 'all':
                n *= 2 ** len(lt)
            else:
                groups = {}
                for t in lt:
                    groups.setdefault(t[:-1], []).append(t)
                for g in groups.values():
                    n *= len(g)
        return n


class Cand:
    """An explanatory candidate (E, p, t, Gamma). question: a label naming p = (D, C, b0, Q)."""

    def __init__(self, name, org, q, tau, pi, anchors, gamma, question):
        self.name, self.org, self.q, self.tau, self.pi = name, org, q, tau, pi
        self.anchors, self.gamma, self.question = anchors, set(gamma), question

    def restrict(self, W, name=None):
        comps = {c: v for c, v in self.org.comps.items() if c in W or c not in self.gamma}
        return Cand(name or '%s|%s' % (self.name, '+'.join(sorted(W)) or '{}'),
                    Org(self.org.name + '|W', self.org.ports, comps), self.q, self.tau, self.pi,
                    {k: v for k, v in self.anchors.items() if k in W}, W, self.question)

    def with_question(self, question, name=None):
        return Cand(name or self.name, self.org, self.q, self.tau, self.pi, self.anchors, self.gamma, question)

    def ans(self, x):
        return self.org.ans(self.tau(x), self.q)

    def A(self, x, D, rels=None):
        return self.ans(x) == D.ans(x, rels)

    def F2(self, x, D, rels=None):
        return {key(self.pi(z)) for z in D.org.sol(x, rels=rels)} == {key(z) for z in self.org.sol(self.tau(x))}

    def F1(self, x, D, rels=None, which=False):
        ex = self.tau(x)
        bad = []
        for k in sorted(self.gamma):
            fp, rel = self.org.comps[k]
            dcomps, tr = self.anchors[k]
            proj = {tuple(z[tr[p]] for p in fp) for z in D.org.sol(x, only=set(dcomps), rels=rels)}
            if proj != set(self.org.rel_under(k, ex)):
                bad.append(k)
                if not which:
                    return False
        return (not bad) if not which else bad

    def meets(self, x, D, rels=None):
        return self.F1(x, D, rels) and self.F2(x, D, rels) and self.A(x, D, rels)

    def why(self, x, D, rels=None):
        out = []
        if not self.A(x, D, rels):
            out.append('A')
        if not self.F2(x, D, rels):
            out.append('F2')
        b = self.F1(x, D, rels, which=True)
        if b:
            out.append('F1[%s]' % ','.join(b))
        return out

    def nc(self, C, b0):
        g = sorted(self.gamma)
        ab = self.ans(b0)
        det = lambda a: len(a) == 1
        for x in C:
            ax = self.ans(x)
            if ax == ab:
                continue
            for r in range(1, len(g) + 1):
                for G in combinations(g, r):
                    ax2 = self.org.ans(self.tau(x), self.q, deleted=G)
                    ab2 = self.org.ans(self.tau(b0), self.q, deleted=G)
                    if (det(ax2) and det(ab2) and ax2 == ab2) or (det(ax) and not det(ax2)) or (det(ab) and not det(ab2)):
                        return True
        return False

    def account(self, C, b0, D):
        if not D.org.sol(b0):
            return False
        return all(self.meets(x, D) for x in C) and self.nc(C, b0)

    def account_why(self, C, b0, D, show):
        bad = []
        for x in C:
            w = self.why(x, D)
            if w:
                bad.append('%s@%s' % ('+'.join(w), show(x)))
        if not self.nc(C, b0):
            bad.append('NonCircular')
        return bad


# ---------------------------------------------------------------------------------- W59.1
def one_account(c1, c2, C):
    if len(c1.gamma) != len(c2.gamma):
        return False, 'active components %d vs %d: no bijection' % (len(c1.gamma), len(c2.gamma))
    if any(c1.ans(x) != c2.ans(x) for x in C):
        return False, 'answer profiles differ on the pairs compared'
    g1 = sorted(c1.gamma)
    reasons = set()
    for perm in permutations(sorted(c2.gamma)):
        ok = True
        for k1, k2 in zip(g1, perm):
            fp1, fp2 = c1.org.comps[k1][0], c2.org.comps[k2][0]
            a1, tr1 = c1.anchors[k1]
            a2, tr2 = c2.anchors[k2]
            if set(a1) != set(a2) or sorted(tr1[p] for p in fp1) != sorted(tr2[p] for p in fp2):
                ok = False
                reasons.add('no pairing with one anchor')
                break
            inv2 = {tr2[q]: q for q in fp2}
            beta = [fp2.index(inv2[tr1[p]]) for p in fp1]
            for x in C:
                l1 = c1.org.rel_under(k1, c1.tau(x))
                l2 = c2.org.rel_under(k2, c2.tau(x))
                if l1 != {tuple(t[j] for j in beta) for t in l2}:
                    ok = False
                    reasons.add('one anchor, not one kind on C (%s vs %s)' % (k1, k2))
                    break
            if not ok:
                break
        if ok:
            return True, 'paired: ' + ', '.join('%s~%s' % (a, b) for a, b in zip(g1, perm))
    return False, '; '.join(sorted(reasons))


def conflict(c1, c2, x, D, space='all'):
    """Returns (conflict, can1, can2, n_variants_checked)."""
    can1 = can2 = joint = False
    n = 0
    for rels in D.variants(x, space):
        n += 1
        m1 = c1.meets(x, D, rels)
        m2 = c2.meets(x, D, rels)
        can1 |= m1
        can2 |= m2
        if m1 and m2:
            joint = True
            break
    if joint:
        can1 = can2 = True
    return (not joint), can1, can2, n


def conflict_route(c1, c2, x):
    """Which of the draft's two named routes applies at x (independent of the target)."""
    routes = []
    if c1.ans(x) != c2.ans(x):
        routes.append('answers differ')
    for k1 in c1.gamma:
        for k2 in c2.gamma:
            fp1, fp2 = c1.org.comps[k1][0], c2.org.comps[k2][0]
            a1, tr1 = c1.anchors[k1]
            a2, tr2 = c2.anchors[k2]
            if set(a1) == set(a2) and sorted(tr1[p] for p in fp1) == sorted(tr2[p] for p in fp2):
                inv2 = {tr2[q]: q for q in fp2}
                beta = [fp2.index(inv2[tr1[p]]) for p in fp1]
                l1 = c1.org.rel_under(k1, c1.tau(x))
                l2 = {tuple(t[j] for j in beta) for t in c2.org.rel_under(k2, c2.tau(x))}
                if l1 != l2:
                    routes.append('one anchor, different relations (%s/%s)' % (k1, k2))
    return routes


def fits(c, est, D, nc=None):
    for xk, (mode, val) in est.items():
        x = dict(xk)
        if mode == 'ans':
            if c.ans(x) != val:
                return False
        elif mode == 'full':
            if not c.meets(x, D, val):
                return False
    if nc is not None:
        C, b0 = nc
        if not c.nc(C, b0):
            return False
    return True


def problem(c1, c2, C, D, est, offered, space='all', nc=None, oa_C=None):
    """Returns a dict with the draft's verdict on the pair. oa_C: the set of pairs on which 'one account'
    is judged. None = C, as the draft says ('not one account on C'). The model scripts also pass every
    admitted pair of the target, to test a repair (a redescription = one account on every admitted change)."""
    out = {'same_question': c1.question == c2.question}
    if not out['same_question']:
        out['verdict'] = 'not rivals: candidates for different questions'
        return out
    oa, why = one_account(c1, c2, C if oa_C is None else oa_C)
    out['one_account'], out['one_account_why'] = oa, why
    out['offered'] = offered
    out['rivals'] = offered and not oa
    if not out['rivals']:
        out['verdict'] = 'not rivals: ' + ('one account (%s)' % why if oa else 'not offered in place of each other')
        return out
    f1, f2 = fits(c1, est, D, nc), fits(c2, est, D, nc)
    out['fits'] = (f1, f2)
    if not (f1 and f2):
        out['verdict'] = 'rivals; NO problem: %s does not fit what is established' % (
            ' and '.join(n for n, f in ((c1.name, f1), (c2.name, f2)) if not f))
        return out
    cf = []
    for x in C:
        c, a, b, n = conflict(c1, c2, x, D, space)
        if c:
            cf.append((x, 'PROPER' if (a and b) else 'DEGENERATE (%s cannot meet the three there whatever the target)' % (
                ' and '.join(nm for nm, ok in ((c1.name, a), (c2.name, b)) if not ok)), conflict_route(c1, c2, x)))
    out['conflicts'] = cf
    out['kind'] = 'i' if cf else 'ii'
    out['verdict'] = 'PROBLEM for p, kind (%s)' % out['kind']
    return out


def test_solves(c1, c2, x, D, est, space='all', mode='full', nc=None):
    """For every target relation at x: after establishing it (mode 'full') or only its answer (mode 'ans'),
    at most one of c1, c2 fits. Returns (solves, number of outcomes where both still fit, outcomes)."""
    both = 0
    outs = 0
    for rels in D.variants(x, space):
        outs += 1
        est2 = dict(est)
        est2[key(x)] = ('full', rels) if mode == 'full' else ('ans', D.ans(x, rels))
        if fits(c1, est2, D, nc) and fits(c2, est2, D, nc):
            both += 1
    return both == 0, both, outs


def supports(c, C, b0, D):
    g = sorted(c.gamma)
    S = []
    for r in range(len(g) + 1):
        for W in combinations(g, r):
            if c.restrict(set(W)).account(C, b0, D):
                S.append(frozenset(W))
    return S


def does_no_work(c, d, C, b0, D):
    """W33.1: every support stays a support after d is added to it and after d is removed from it."""
    S = set(supports(c, C, b0, D))
    add = all((W | {d}) in S for W in S)
    rem = all((W - {d}) in S for W in S)
    return add, rem, S


def fmt_problem(res, show):
    lines = []
    lines.append('    same question: %s' % res['same_question'])
    if 'one_account' in res:
        lines.append('    one account (Derivation 2): %s  [%s]' % (res['one_account'], res['one_account_why']))
        lines.append('    offered in place of each other: %s  -> rivals: %s' % (res['offered'], res['rivals']))
    if 'fits' in res:
        lines.append('    fit what is established: %s' % (res['fits'],))
    if 'conflicts' in res:
        if res['conflicts']:
            for x, cls, routes in res['conflicts']:
                lines.append('      conflict at %-26s %-10s routes: %s' % (show(x), cls.split(' ')[0], '; '.join(routes) or 'NONE of the two named routes'))
                if cls.startswith('DEGENERATE'):
                    lines.append('         %s' % cls)
        else:
            lines.append('      conflict at no pair of C')
    lines.append('    VERDICT: %s' % res['verdict'])
    return '\n'.join(lines)
