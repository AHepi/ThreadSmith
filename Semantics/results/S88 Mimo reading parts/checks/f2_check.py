# Exact-arithmetic checks for the F2 reading (Mimo's reply). Fractions only.
from fractions import Fraction as Fr
eps = Fr(1,10)
def geo(L, n): return sum(L**k for k in range(n))

print("== 2a (two-run reading): pi=id, S(z)=2z+1/10, T(y)=2y, z0=0, y0=-1")
S = lambda z: 2*z + eps; T = lambda y: 2*y
z, y = Fr(0), Fr(-1)
for n in range(0, 6):
    e = abs(z - y); b = eps*geo(2, n); gen = 2**n*1 + eps*geo(2, n)
    print(f" n={n} e_n={e} bound={b} fails={e>b} general bound L^n e0+eps*sum={gen} attained={e==gen}")
    z, y = S(z), T(y)
print("   same-state (y0=pi z0=0): e_n vs bound")
z, y = Fr(0), Fr(0)
for n in range(0, 6):
    print(f"  n={n} e_n={abs(z-y)} bound={eps*geo(2,n)} equal={abs(z-y)==eps*geo(2,n)}")
    z, y = S(z), T(y)

print("== 2b: S=id on R, pi(z)=(z,0), T(a,b)=(a+100b, b+1/10); squared distances exact")
def T2(p): a,b = p; return (a + 100*b, b + eps)
z = Fr(0); p = (z, Fr(0))
one_step_sq = (Fr(0))**2 + (eps)**2
print(" one-step discrepancy^2 at any z:", one_step_sq, "(so discrepancy = 1/10)")
q = p
for n in range(1, 4):
    q = T2(q); e2 = (q[0]-z)**2 + (q[1]-0)**2
    bL1 = eps*geo(1, n)
    print(f" n={n} e_n^2={e2} closed form (5n(n-1))^2+(n/10)^2={(5*n*(n-1))**2+(Fr(n,10))**2}  bound(L=1)={bL1} fails={e2>bL1**2}")
# Lip(T) = sigma, sigma^2 = largest root of x^2-10002x+1
def above(qq):  # True if rational qq > sigma
    s = qq*qq; return s > 5001 and s*s - 10002*s + 1 > 0
lo, hi = Fr(100009,1000), Fr(10001,100)
print(" sigma bracket:", float(lo), "< sigma <", float(hi), above(hi), not above(lo))
# bound with L = lo (smaller than sigma) already holds -> holds with sigma
q = p; ok = True
for n in range(1, 60):
    q = T2(q); e2 = (q[0]-z)**2 + q[1]**2
    if e2 > (eps*geo(lo, n))**2: ok = False; print(" FAIL at", n)
print(" with L=Lip(T) (>= lower bracket) the bound holds for n=1..59:", ok, "; n=2 bound with L=hi:", float(eps*(1+hi)))

print("== 2c: pi=id, T(y)=2y, S(z)=2z+1/10+z^2, z0=0")
S = lambda z: 2*z + eps + z*z
z = Fr(0); zs=[z]
for n in range(3): z = S(z); zs.append(z)
print(" orbit", zs[:4], " discrepancy at z0,z1:", eps+zs[0]**2, eps+zs[1]**2, " e_2=", zs[2], "bound", eps*geo(2,2), "fails", zs[2] > eps*geo(2,2))

print("== Mimo's scope instance: phi=0 on |z|<=1, (|z|-1)^2 outside; scope [-1,1]; L=2")
phi = lambda z: Fr(0) if abs(z) <= 1 else (abs(z)-1)**2
S = lambda z: 2*z + eps + phi(z)
z = Fr(0); zs=[z]
for n in range(6): z = S(z); zs.append(z)
for n in range(0, 7):
    e = zs[n]; b = eps*geo(2, n); inside = all(abs(w) <= 1 for w in zs[:n])
    disc = [eps + phi(w) for w in zs[:n]]
    print(f" n={n} z_n={e} e_n={e} bound={b} holds={e<=b} z_0..z_(n-1) in scope={inside} step-discrepancies={[str(d) for d in disc]}")
print("  -> as-sent wording (no containment) defeated at n=5; current wording (whenever z..S^(n-1)z in scope) claims only n<=4, where it holds")

print("== Restated unequal-start clause: d(pi S^n z, T^n y) <= L^n d(pi z,y) + eps*sum, check on 2a and random starts")
import random
random.seed(1)
S = lambda z: 2*z + eps; T = lambda y: 2*y
bad = 0
for trial in range(200):
    z0 = Fr(random.randint(-50,50),7); y0 = Fr(random.randint(-50,50),11)
    z,y = z0,y0
    for n in range(12):
        if abs(z-y) > 2**n*abs(z0-y0) + eps*geo(2,n): bad += 1
        z,y = S(z),T(y)
print(" violations:", bad)

print("== Current erratum wording, random piecewise-linear T on R (global Lipschitz = max |slope|), S arbitrary, pi=id")
def pl(knots, slopes, c0):
    # continuous piecewise-linear map with value c0 at knots[0]
    def f(x):
        v = c0; prev = knots[0]
        if x <= knots[0]: return c0 + slopes[0]*(x - knots[0])
        for i in range(1, len(knots)):
            k = knots[i]
            if x <= k: return v + slopes[i]*(x - prev)
            v += slopes[i]*(k - prev); prev = k
        return v + slopes[-1]*(x - prev)
    return f
viol = 0; tested = 0
for trial in range(400):
    knots = sorted(Fr(random.randint(-30,30),5) for _ in range(4))
    slopes = [Fr(random.randint(-25,25),10) for _ in range(5)]
    T = pl(knots, slopes, Fr(random.randint(-10,10),3))
    L = max(abs(s) for s in slopes)
    Sfun = pl(sorted(Fr(random.randint(-30,30),5) for _ in range(4)), [Fr(random.randint(-25,25),10) for _ in range(5)], Fr(random.randint(-10,10),3))
    lo_s, hi_s = sorted([Fr(random.randint(-40,0),4), Fr(random.randint(0,40),4)])
    z0 = Fr(random.randint(-20,20),9)
    # eps := max one-step discrepancy over the scope's sampled orbit points is not a valid scope bound; instead
    # take eps := sup over scope of |S(w)-T(w)|, which for PL maps is attained at knots or scope ends
    pts = [lo_s, hi_s] + [k for k in knots if lo_s <= k <= hi_s]
    # include S's knots too by dense rational grid (PL difference: max at breakpoints; grid over all breakpoints)
    grid = pts + [lo_s + (hi_s-lo_s)*Fr(i,400) for i in range(401)]
    e_ = max(abs(Sfun(w) - T(w)) for w in grid)
    z, y = z0, z0; zs = []
    for n in range(10):
        if all(lo_s <= w <= hi_s for w in zs):
            tested += 1
            if abs(z - y) > e_*geo(L, n): viol += 1
        zs.append(z); z, y = Sfun(z), T(y)
print(" instances with orbit prefix in scope:", tested, " violations:", viol)
