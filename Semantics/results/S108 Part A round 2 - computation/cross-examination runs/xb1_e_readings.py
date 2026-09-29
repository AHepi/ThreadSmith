# Xb1 (settlement of the GLM cross-examination): R2V4.3 (e) under readings of "Sel at o". Run from the section-4 round-2 copy's
# folder (sys.path set to it); imports only; writes nothing. Same chain enumeration as s108r2_s4_cases.py r2v43_chains.
import itertools, os, sys
sys.path.insert(0, os.getcwd())
from model.claims_b import prov_fixed_points, _prov_step
READ = {
 "e as computed (held[o] and (Sel's conditions staged at o or trace))": lambda n, held, trace, direct, sc: any(held[o] and (direct[o][0] or trace[o]) for o in range(n)),
 "e1: held[o] and (Sel at o as the fixed point's value, inherited, or trace)": lambda n, held, trace, direct, sc: any(held[o] and (sc[o][0] or trace[o]) for o in range(n)),
 "e2 (the objection's): any o, Sel at o as the fixed point's value or trace": lambda n, held, trace, direct, sc: any(sc[o][0] or trace[o] for o in range(n)),
}
tot = 0; diff = {k: 0 for k in READ}; diffh = {k: 0 for k in READ}; exh = {k: None for k in READ}
for n in (1, 2, 3):
    rec_choices = [[None]] + [list(range(o)) + [None] for o in range(1, n)]
    for held in itertools.product([0, 1], repeat=n):
        for trace in itertools.product([0, 1], repeat=n):
            for selc in itertools.product([0, 1], repeat=n):
                for rec in itertools.product(*rec_choices):
                    fps = prov_fixed_points(n, list(held), list(trace), list(selc), "T'", True, rec_of=list(rec))
                    if len(fps) != 1:
                        continue
                    tot += 1
                    R, sc = fps[0]
                    last = n - 1
                    nd = bool(sc[last][0] or sc[last][1])
                    direct = _prov_step(n, list(held), list(trace), list(selc), "T'", True, R)
                    for k, f in READ.items():
                        v = bool(f(n, held, trace, direct, sc))
                        if (nd and v) != nd:
                            diff[k] += 1
                            if held[last]:
                                diffh[k] += 1
                                if exh[k] is None:
                                    exh[k] = dict(n=n, held=held, trace=trace, selc=selc, rec=rec, sc=sc)
print("chains with one fixed point under T':", tot)
for k in READ:
    print("%-100s differs from ¬Dec at %d last holdings; with t held there %d; smallest held: %s" % (k, diff[k], diffh[k], exh[k]))
