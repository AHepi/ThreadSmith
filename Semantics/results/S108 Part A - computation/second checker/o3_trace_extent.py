"""Second checker, O3: V3.5 (D13.8's record clause deleted) with a construction trace that spans occurrences.
The program (claims_b._con_at) reads a trace as a label at one occurrence: Prepares(h', o, .) holds for h' = {o} alone,
so the record clause is never read for a held output. Here the output's trace has an extent o_s .. o_t (D13.3, L405:
a trace is (h', the controlled processes, the incoming carriers, the bindings constructed, the resulting representation)),
and Prepares(h', o_t, .) asks h' to hold o_s .. o_t. Every other occurrence keeps the program's one-occurrence trace.
extent s = t gives the program's encoding back (the control). Run with cwd = the section 3 copy; imports only; writes nothing.
usage: python3 -B o3_trace_extent.py NMAX [cuts...]"""
import itertools
import sys
import time

sys.path.insert(0, ".")
from model import s108s3  # noqa: E402
from model.claims_b import chain_eps  # noqa: E402


def con_at(o, held, trace, start, rd, R, eps):
    if not trace[o]:
        return False
    for i in range(start[o] + 1):          # h' = o_i .. o_o must hold the trace's occurrences o_start .. o_o
        if not eps(i, o):
            continue
        if rd == "U":
            ok = any(x in R for x in range(i, o + 1))
        elif rd == "K":
            ok = any(x in R for x in range(i, o))
        else:
            ok = any(held[x] for x in range(i, o + 1))
        if ok:
            return True
    return False


def prov_step(n, held, trace, start, selc, rd, R, eps):
    out = {}
    for o in range(n):
        before, upto = range(o), range(o + 1)
        c_ = con_at(o, held, trace, start, rd, R, eps)
        if rd == "U":
            s_ = selc[o] and not any(x in R for x in upto)
        elif rd == "K":
            s_ = selc[o] and not any(x in R for x in before)
        elif rd == "T":
            s_ = selc[o] and not any(held[x] for x in before)
        else:
            s_ = selc[o] and not any(x in R for x in before)
        s_ = s_ and not trace[o]            # I161, as the program
        out[o] = (bool(s_), bool(c_))
    return out


def fixed_points(n, held, trace, start, selc, rd, eps):
    fps = []
    for bits in itertools.product([0, 1], repeat=n):
        R = frozenset(o for o in range(n) if bits[o])
        sc = prov_step(n, held, trace, start, selc, rd, R, eps)
        if frozenset(o for o in range(n) if held[o] and (sc[o][0] or sc[o][1])) == R:
            fps.append((R, sc))
    return fps


def out_dec(n, held, trace, start, selc, qs, rs, rd):
    fps = fixed_points(n, held, trace, start, selc, rd, chain_eps(qs, rs))
    return tuple(sorted(set(not s and not k for R, sc in fps for (s, k) in [sc[n - 1]])))


def chains(nmax):
    for n in range(1, nmax + 1):
        for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n):
            held, trace, selc = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]
            for steps in itertools.product(("same", "rec", "unrec"), repeat=n - 1):
                qs, rs = ["C"], [False]
                for st in steps:
                    if st == "same":
                        qs.append(qs[-1]); rs.append(False)
                    else:
                        qs.append("C'" if qs[-1] == "C" else "C"); rs.append(st == "rec")
                for s_out in range(n):       # the output's trace starts at o_{s_out}; the others at their own occurrence
                    start = list(range(n))
                    start[n - 1] = s_out
                    yield n, held, trace, selc, qs, rs, start


def main():
    nmax = int(sys.argv[1])
    cuts = sys.argv[2:] or ["T'", "T", "K", "U"]
    t0 = time.time()
    res = {}
    for m in chains(nmax):
        n, held, trace, selc, qs, rs, start = m
        spans_unrec = any(qs[i] != qs[i - 1] and not rs[i] for i in range(start[n - 1] + 1, n))
        enc = "program (trace at o_t)" if start[n - 1] == n - 1 else ("trace spans an unrecorded change" if spans_unrec else "trace spans occurrences, no unrecorded change")
        for rd in cuts:
            s108s3.set_variant("none")
            off = out_dec(n, held, trace, start, selc, qs, rs, rd)
            s108s3.set_variant("V3.5")
            on = out_dec(n, held, trace, start, selc, qs, rs, rd)
            s108s3.set_variant("none")
            key = (rd, enc, "held at output" if held[-1] else "not held at output")
            r = res.setdefault(key, {"chains": 0, "moves": 0, "dirs": {}, "witness": None})
            r["chains"] += 1
            if off != on:
                r["moves"] += 1
                d = "Dec %s → %s" % (off, on)
                r["dirs"][d] = r["dirs"].get(d, 0) + 1
                if r["witness"] is None:
                    r["witness"] = dict(n=n, held=held, trace=trace, selc=selc, contracts=qs, records=rs, output_trace_from="o%d" % (start[-1] + 1))
    print("chains n ≤ %d, cuts %s, %.1f s" % (nmax, cuts, time.time() - t0))
    for k in sorted(res):
        r = res[k]
        print("%-4s | %-46s | %-19s | chains %6d | Dec moves (none → V3.5) %5d %s" % (k[0], k[1], k[2], r["chains"], r["moves"], r["dirs"]))
        if r["witness"] and k[2] == "held at output":
            print("       smallest: %s" % r["witness"])


if __name__ == "__main__":
    main()
