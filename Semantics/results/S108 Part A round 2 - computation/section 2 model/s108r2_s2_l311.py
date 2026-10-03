# S108 Part A round 2, section 2 (the computing agent, rule 5 (2)): round 1's claimed-only edges e2.03 (V2.2 blocks L311.s2,
# '(B) records the collective contribution') and e2.26 (V2.2 blocks L313.n3, 'When Γ is infinite, a block of such commitments
# can still be critical'), settled on the reply's proposal (Inv-R2-7): L311's candidate given symbolically, not through the
# program's finite powerset (which cannot hold an infinite Γ, round 1's P-S2-4).
# The case (P-R2S2-8, this agent's encoding of L311 and I31): one real port x; commitments d_n: |x| ≤ 1/n (n ≥ 1); C = {(1,b0),
# (e,b0)}; at (1,b0) no commitment constrains x (x free: Ans ⊥); at (e,b0) each d_n imposes |x| ≤ 1/n; the target holds every
# d_n, so Ans_p(e,b0) = 0; ℰ = the target with the identity transport, Γ = {d_n}. For W ⊆ Γ, E|W keeps the d_n with n ∈ W.
#   ∩_{n∈W} [−1/n, 1/n] = {0} exactly when W is infinite (for finite nonempty W it is [−1/max W, 1/max W]; for W = ∅ it is ℝ),
# so Ans_{E|W}(e,b0) = 0 when W is infinite and ⊥ otherwise; (A) and the (F2) equation at (e,b0) hold exactly then; (F1) holds
# (each d_n is the target's own); NonVacuous holds. Index sets W are taken in the class of ultimately periodic subsets of
# ℕ⁺ (a finite part below N plus the n > N with n mod m ∈ R): W is infinite exactly when R ≠ ∅, and W ∖ G for a representable G
# is representable. Every set, contrast and loss below is computed on that class, exhaustively up to the bounds given.
# Standard library only; imports nothing of the program; writes nothing. Run: python3 -B s108r2_s2_l311.py
import itertools

NMAX, MMAX = 4, 3
BOT = "⊥"


class UP:
    """An ultimately periodic subset of ℕ⁺: F ⊆ {1..N} ∪ {n > N : n mod m ∈ R}."""

    def __init__(self, F, N, m, R):
        self.F, self.N, self.m, self.R = frozenset(F), N, m, frozenset(R)

    def has(self, n):
        return (n in self.F) if n <= self.N else ((n % self.m) in self.R)

    def infinite(self):
        return bool(self.R)

    def minus(self, G):
        """self ∖ G, G an UP: represented on the common refinement (N' = max, m' = lcm)."""
        N = max(self.N, G.N)
        m = self.m * G.m // gcd(self.m, G.m)
        F = [n for n in range(1, N + 1) if self.has(n) and not G.has(n)]
        R = [r for r in range(m) if all((self.has(n) and not G.has(n)) for n in (N + 1 + ((r - (N + 1)) % m) + k * m for k in range(3)))]
        return UP(F, N, m, R)

    def elements_up_to(self, k):
        return [n for n in range(1, k + 1) if self.has(n)]

    def __repr__(self):
        return "{%s}∪{n>%d: n mod %d ∈ %s}" % (",".join(map(str, sorted(self.F))), self.N, self.m, sorted(self.R))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def single(n):
    return UP([n], max(n, 1), 1, [])


def ans(W, pair):
    """Ans_{E|W} at a pair: ⊥ at (1,b0); at (e,b0) 0 exactly when W is infinite."""
    if pair == "(1,b0)":
        return BOT
    return 0 if W.infinite() else BOT


def contrast(W):
    return ans(W, "(e,b0)") != ans(W, "(1,b0)")


def lost(W, G):
    """Lost(E|W, G; x) (D6.4) with x = (e,b0), x0 = (1,b0)."""
    WG = W.minus(G)
    ax, ax0 = ans(WG, "(e,b0)"), ans(WG, "(1,b0)")
    if ax != BOT and ax0 != BOT and ax == ax0:
        return True
    return any(ans(W, y) != BOT and ans(WG, y) == BOT for y in ("(e,b0)", "(1,b0)"))


def all_UP():
    out = []
    for N in range(0, NMAX + 1):
        for m in range(1, MMAX + 1):
            for R in itertools.chain.from_iterable(itertools.combinations(range(m), r) for r in range(m + 1)):
                for F in itertools.chain.from_iterable(itertools.combinations(range(1, N + 1), r) for r in range(N + 1)):
                    out.append(UP(F, N, m, R))
    return out


def blocks_of(W, cands):
    """Nonempty representable G ⊆ W among cands (and every singleton of W up to a bound)."""
    got = [G for G in cands if G.infinite() or G.F]  # nonempty
    got = [G for G in got if all(W.has(n) for n in G.elements_up_to(NMAX + 2 * MMAX * MMAX + 8)) and (not G.infinite() or W.infinite())]
    return got


def acc(W, variant, cands):
    """Acc(E|W) under D6.4 ('off') or round 1's V2.1, V2.2, V2.3: (F1) holds; (A) and (F2) at (e,b0) ⟺ W infinite; NonVacuous."""
    if not W.infinite():
        return False  # (A), (F2) fail at (e,b0)
    if not contrast(W):
        return False
    if variant == "V2.1":
        return True
    if variant == "V2.2":  # singletons {d}, d ∈ W: W ∖ {d} is W with one element dropped below the refinement bound
        return any(lost(W, single(d)) for d in W.elements_up_to(NMAX + MMAX + 3))
    # off and V2.3 (the witness pair (e,b0) has an edit e ≠ 1)
    return any(lost(W, G) for G in blocks_of(W, cands)) or lost(W, W)


def main():
    P = print
    cls = all_UP()
    P("L311's candidate on the ultimately periodic index sets W (N ≤ %d, period m ≤ %d): %d representations, %d infinite" % (NMAX, MMAX, len(cls), sum(W.infinite() for W in cls)))
    res = {}
    for v in ("off", "V2.1", "V2.2", "V2.3"):
        S = [W for W in cls if acc(W, v, cls)]
        one = [W for W in S if len(W.F) == 1 and not W.infinite()]
        minimal = [W for W in S if not any(W.has(n) and acc(W.minus(single(n)), v, cls) is False for n in W.elements_up_to(NMAX + MMAX + 3))]
        sing_crit, block_crit = 0, 0
        for W in S:
            for d in W.elements_up_to(NMAX + MMAX + 3):
                if not acc(W.minus(single(d)), v, cls):
                    sing_crit += 1
            for k in range(1, NMAX + MMAX + 2):
                B = UP([n for n in range(k, NMAX + 1) if W.has(n)], NMAX, W.m, W.R)  # W ∩ {n ≥ k}: all but finitely many of W
                if not acc(W.minus(B), v, cls):
                    block_crit += 1
        res[v] = dict(routes=len(S), all_infinite=all(W.infinite() for W in S), every_infinite_a_route=all(acc(W, v, cls) for W in cls if W.infinite()),
                      one_commitment_routes=len(one), routes_with_no_member_critical=len(minimal), critical_singletons=sing_crit, critical_blocks_tails=block_crit)
        P("%-4s routes S: %4d of the class; every route infinite %s; every infinite W a route %s; routes of one commitment %d; critical singletons (W, d) %d; critical tail blocks (W, W∩{n≥k}) %d"
          % (v, res[v]["routes"], res[v]["all_infinite"], res[v]["every_infinite_a_route"], res[v]["one_commitment_routes"], res[v]["critical_singletons"], res[v]["critical_blocks_tails"]))
    P("Reading: under D6.4 (off), V2.1 and V2.3, S = the infinite (unbounded) index sets (I31): no route of one commitment, no singleton")
    P("critical in any route, a tail block critical in every route: L311.s2 ('(B) records the collective contribution') and L313.n3 hold.")
    P("Under V2.2 (Dependence through a singleton block): S = ∅ on the class; so (B) records nothing and no block is critical: L311.s2 and")
    P("L313.n3 have no instance. For W infinite, W ∖ {d} is infinite for every d (the periodic part R is untouched), so no singleton loses")
    P("the contrast: the finite check above and this one-line step cover every ultimately periodic W; for an arbitrary W ⊆ ℕ⁺ the same step")
    P("holds (removing one element leaves an infinite set infinite), which is the reply's argument; the class computes it.")
    return res


if __name__ == "__main__":
    main()
