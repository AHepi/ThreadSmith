# S105 round 3, area 3 (K4): E9, the two-layer episode (L620-L630), built in the program's own terms, so that (F1), (F2),
# (A), Sel, Viol and one kind are computed by core and claims_b, not tagged. Small instance [R3A3-09]: a line of N = 4
# cells, frames t = 0..3, two things; continuity with reflection at the ends (I100's rule); occupancy per cell, 'h' where
# occluded the field shows nothing there (L624: 'the occupancy field shows nothing at its cell'); the occlusion hides cells
# 1..2 at t = 1, 2 (L_occ = 2), so a thing hidden there re-emerges at t = 3. Edits act on the initial frame (the init
# components): displace a thing to a cell, set its velocity, swap the two things' identities (initial states exchanged);
# occlude; and occlusion composed with each. Boundaries: initial states (p1, v1, p2, v2), p1 ≠ p2.
import itertools

from .core import ONE, Org, Question, PortQuery, Candidate, Translation

N, T = 4, 3                      # cells 0..N-1, frames 0..T
HIDDEN = {(c, t) for c in (1, 2) for t in (1, 2)}
POS, VEL = tuple(range(N)), (-1, 0, 1)
OCC = (0, 1)


def step(p, v):
    np_ = p + v
    if not 0 <= np_ < N:
        v = -v
        np_ = p + v
    return np_, v


def things_ports(i):
    return [("x%d_%d" % (i, t)) for t in range(T + 1)], [("u%d_%d" % (i, t)) for t in range(T + 1)]


def all_ports():
    out = []
    for t in range(T + 1):
        out += ["x1_%d" % t, "u1_%d" % t, "x2_%d" % t, "u2_%d" % t]
        out += ["o%d_%d" % (c, t) for c in range(N)]
    return out


def dom_of(v):
    return POS if v[0] == "x" else VEL if v[0] == "u" else OCC


BASIC = ([ONE, "occ", "swap"] + ["disp%d_%d" % (i, x) for i in (1, 2) for x in POS] + ["vel%d_%d" % (i, v) for i in (1, 2) for v in VEL])
EDITS = BASIC + ["occ+" + a for a in BASIC if a not in (ONE, "occ")]


def parse(a):
    """(occluded, swap, displacement (i, x) or None, velocity (i, v) or None)."""
    occ = a.startswith("occ")
    rest = a[4:] if a.startswith("occ+") else ("" if a in ("occ", ONE) else a)
    disp = (int(rest[4]), int(rest[6:])) if rest.startswith("disp") else None
    vel = (int(rest[3]), int(rest[5:])) if rest.startswith("vel") else None
    return occ, rest == "swap", disp, vel


def compose(a2, a1):
    for x, y in ((a2, a1), (a1, a2)):
        if x == "occ" and y in BASIC and y not in (ONE, "occ"):
            return "occ+" + y
    return None


BOUNDS = ["b%d%s%d%s" % (p1, "mzp"[v1 + 1], p2, "mzp"[v2 + 1]) for p1 in POS for p2 in POS if p1 != p2 for v1 in VEL for v2 in VEL]


def bval(b):
    return (int(b[1]), "mzp".index(b[2]) - 1, int(b[3]), "mzp".index(b[4]) - 1)


def cont_rel(i, t, a):
    """c_i_t on (x_i_t, u_i_t, x_i_(t+1), u_i_(t+1)): the step, under every edit (continuity; no edit replaces it)."""
    return frozenset((p, v) + step(p, v) for p in POS for v in VEL)


def init_rel(i, a, b):
    p1, v1, p2, v2 = bval(b)
    occ, sw, disp, vel = parse(a)
    s = [[p1, v1], [p2, v2]]
    if sw:
        s = s[::-1]
    if disp:
        s[disp[0] - 1][0] = disp[1]
    if vel:
        s[vel[0] - 1][1] = vel[1]
    return frozenset([tuple(s[i - 1])])


def occ_rel(c, t, a):
    occ = parse(a)[0]
    if occ and (c, t) in HIDDEN:
        return frozenset((x1, x2, 0) for x1 in POS for x2 in POS)
    return frozenset((x1, x2, int(c in (x1, x2))) for x1 in POS for x2 in POS)


def object_layer():
    """P (the target D): init_i, c_i_t (continuity), o_c_t (occupancy)."""
    ports = all_ports()
    dom = {v: dom_of(v) for v in ports}
    foot = {}
    for i in (1, 2):
        foot["init%d" % i] = ("x%d_0" % i, "u%d_0" % i)
        for t in range(T):
            foot["c%d_%d" % (i, t)] = ("x%d_%d" % (i, t), "u%d_%d" % (i, t), "x%d_%d" % (i, t + 1), "u%d_%d" % (i, t + 1))
    for t in range(T + 1):
        for c in range(N):
            foot["o%d_%d" % (c, t)] = ("x1_%d" % t, "x2_%d" % t, "o%d_%d" % (c, t))

    def Lf(j, a, b):
        if j.startswith("init"):
            return init_rel(int(j[4]), a, b)
        if j.startswith("c"):
            return cont_rel(int(j[1]), int(j[3]), a)
        c, t = int(j[1]), int(j[3])
        return occ_rel(c, t, a)

    comps = list(foot)
    return Org("P", ports, dom, comps, foot, BOUNDS, EDITS, compose, Lf)


def sim_layer_S1():
    """S1: init_i, a persistence component k_i per thing carrying position and velocity through every frame (occlusion
    included), and the occupancy components; its own relations, computed by its own step rule. Ports listed thing by
    thing (the order core.solve assigns them in; a solution is the same set in any order)."""
    ports = [p for i in (1, 2) for t in range(T + 1) for p in ("x%d_%d" % (i, t), "u%d_%d" % (i, t))] + ["o%d_%d" % (c, t) for t in range(T + 1) for c in range(N)]
    dom = {v: dom_of(v) for v in ports}
    foot = {}
    for i in (1, 2):
        xs, us = things_ports(i)
        foot["init%d" % i] = (xs[0], us[0])
        foot["k%d" % i] = tuple(p for t in range(T + 1) for p in (xs[t], us[t]))
    for t in range(T + 1):
        for c in range(N):
            foot["o%d_%d" % (c, t)] = ("x1_%d" % t, "x2_%d" % t, "o%d_%d" % (c, t))

    def persist(i, a):
        out = set()
        for p in POS:
            for v in VEL:
                traj = [(p, v)]
                for t in range(T):
                    x_, u_ = traj[-1]
                    rel = [w for w in cont_rel(i, t, a) if w[0] == x_ and w[1] == u_]
                    traj.append((rel[0][2], rel[0][3]))
                out.add(tuple(z for xu in traj for z in xu))
        return frozenset(out)

    cache = {}

    def Lf(j, a, b):
        if j.startswith("init"):
            return init_rel(int(j[4]), a, b)
        if j.startswith("k"):
            key = (j, a)
            if key not in cache:
                cache[key] = persist(int(j[1]), a)
            return cache[key]
        return occ_rel(int(j[1]), int(j[3]), a)

    return Org("S1", ports, dom, list(foot), foot, BOUNDS, EDITS, compose, Lf)


def psi_edit(a):
    """ψ on edits: the exchange of the two things."""
    def sw(x):
        if x.startswith("disp") or x.startswith("vel"):
            k = 4 if x.startswith("disp") else 3
            return x[:k] + ("2" if x[k] == "1" else "1") + x[k + 1:]
        return x
    if a.startswith("occ+"):
        return "occ+" + sw(a[4:])
    return sw(a)


def psi_bound(b):
    p1, v1, p2, v2 = bval(b)
    return "b%d%s%d%s" % (p2, "mzp"[v2 + 1], p1, "mzp"[v1 + 1])


def question(D, C, delta="o1_3"):
    b0 = BOUNDS[0]
    from . import s108r2_s4 as _R2S4  # S108 Part A round 2, R2V4.5
    if _R2S4.VARIANT == "R2V4.5":
        return Question(D, C, b0, _R2S4.q_id(), delta, name="p_E9")
    return Question(D, C, b0, PortQuery(), delta, name="p_E9")


def t1_candidate(p, E, swapped=False):
    """t1: λ(k_i) = thing i's continuity subnetwork, identity translations; with swapped=True, t1∘ψ: k_i to the other
    thing's subnetwork, π, τ, σ composed with the exchange ψ."""
    other = {1: 2, 2: 1}

    def src(i):
        return other[i] if swapped else i

    def tr_port(v):
        if v[0] in "xu" and swapped:
            return v[0] + str(other[int(v[1])]) + v[2:]
        return v

    pi = {v: Translation((tr_port(v),)) for v in E.ports}
    lam = {}
    for i in (1, 2):
        xs, us = things_ports(i)
        lam["k%d" % i] = (frozenset("c%d_%d" % (src(i), t) for t in range(T)), {v: Translation((tr_port(v),)) for v in E.foot["k%d" % i]})
        lam["init%d" % i] = (frozenset(["init%d" % src(i)]), {v: Translation((tr_port(v),)) for v in E.foot["init%d" % i]})
    for t in range(T + 1):
        for c in range(N):
            j = "o%d_%d" % (c, t)
            lam[j] = (frozenset([j]), {v: Translation((tr_port(v),)) for v in E.foot[j]})
    tau = {a: (psi_edit(a) if swapped else a) for a in p.D.A}
    sigma = {b: (psi_bound(b) if swapped else b) for b in p.D.B}
    return Candidate(E, p, pi, tau, sigma, lam, list(E.comps), "o1_3", name="t1∘ψ" if swapped else "t1")


# ---- S0: a window-2 occupancy predictor [R3A3-09] ----------------------------------------------------------------
# Ports: the occupancy frames o_c_t. Frames 0 and 1 are observed: S0's components obs_0, obs_1 take the frames P gives at
# the pair (the observations). pred_t (t = 2, 3) on (frame t-2, frame t-1, frame t): at each pair, the one tuple of S0's
# own window and f of it, f a map from windows to frames (a member of the population is an f). λ(pred_t) = the whole of P
# read on those frames. So (F1) at pred_t, and (F2)'s valuation equation, hold exactly when S0's predictions are P's frames.


def frames_of(D, a, b):
    z = next(iter(D.sol(a, b)))
    d = D.as_dict(z)
    return [tuple(d["o%d_%d" % (c, t)] for c in range(N)) for t in range(T + 1)]


def sim_layer_S0(D, f, name="S0"):
    ports = ["o%d_%d" % (c, t) for t in range(T + 1) for c in range(N)]
    dom = {v: OCC for v in ports}
    fr = lambda t: tuple("o%d_%d" % (c, t) for c in range(N))
    foot = {"obs0": fr(0), "obs1": fr(1), "pred2": fr(0) + fr(1) + fr(2), "pred3": fr(1) + fr(2) + fr(3)}
    cache = {}

    def run(a, b):
        if (a, b) not in cache:
            fs = frames_of(D, a, b)
            f2 = f(fs[0], fs[1])
            f3 = f(fs[1], f2)
            cache[(a, b)] = (fs[0], fs[1], f2, f3)
        return cache[(a, b)]

    def Lf(j, a, b):
        g = run(a, b)
        if j == "obs0":
            return frozenset([g[0]])
        if j == "obs1":
            return frozenset([g[1]])
        if j == "pred2":
            return frozenset([g[0] + g[1] + g[2]])
        return frozenset([g[1] + g[2] + g[3]])

    return Org(name, ports, dom, list(foot), foot, D.B, D.A, D._compose, Lf)


def t0_candidate(p, E):
    lam = {j: (frozenset(p.D.comps), {v: Translation((v,)) for v in E.foot[j]}) for j in E.comps}
    return Candidate(E, p, {v: Translation((v,)) for v in E.ports}, {a: a for a in p.D.A}, {b: b for b in p.D.B}, lam, list(E.comps), "o1_3", name="t0")
