# S108 Part A, Sonnet 5.5 trial, section 2: the worked cases of the text and the student's declared formula, each computed
# with no variant on and with each of V2.1 to V2.7 on (core.S2_ON): Acc (E), its conjuncts, routes S, and Acc and not Dec
# in three provenance scenarios (Theta by hand, I90; claims_s41.provenance_of): (i) a transport with a construction trace
# (Con), (ii) a transport declared, no pair tried, no trace (H = empty; Sel's conditions computed by claims_b.sel),
# (iii) a transport declared with one pair tried (H = {(1, b0)}; Sel computed by sel).
# Run from the folder "section 2 model":  PYTHONHASHSEED=0 python3 -B s108_section2_cases.py [json path]
# Standard library only; imports the package model/ and s106_cases.py of this folder; writes nothing but the printout
# (and the json when a path is given). Nothing here changes the theory (S40).
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model import claims_b  # noqa: E402
from model.core import ONE, account, routes, minimal, NC2  # noqa: E402
from model.claims_b import fwd_pole_cand, e6_parts  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
import s106_cases  # noqa: E402

VARIANTS = ["V2.1", "V2.2", "V2.3", "V2.3b", "V2.4", "V2.5", "V2.6", "V2.7"]


def set_on(v):
    core.S2_ON.clear()
    if v:
        core.S2_ON.add(v)
    claims_b.SEL_H_NONEMPTY = "V2.5" not in core.S2_ON


def collect():
    got = []
    orig = s106_cases.case

    def grab(label, where, c, note=""):
        got.append((label, where, c))
    s106_cases.case = grab
    buf = io.StringIO()
    with redirect_stdout(buf):
        s106_cases.main()
    s106_cases.case = orig
    return got


def tf(x):
    return "T" if x else "F"


def evaluate(c):
    out = {}
    v, d = account(c, detail=True)
    out["acc"] = bool(v)
    out["conj"] = {k: bool(d[k]) for k in ("F1", "F2", "A", "NC1", "Dep", "NonVacuous") if k in d}
    w = None
    try:
        w = NC2(c, witness=True)
    except Exception as e:  # noqa: BLE001
        w = "error: %s" % e
    out["nc2_witness"] = repr(w) if w else None
    if len(c.Gamma) <= 8:
        S = routes(c)
        out["routes"] = sorted(["{" + ",".join(sorted(W)) + "}" for W in S])
        out["min_routes"] = sorted(["{" + ",".join(sorted(W)) + "}" for W in minimal(S)])
    else:
        out["routes"] = "skipped (%d commitments)" % len(c.Gamma)
        out["min_routes"] = "skipped"
    prov = {}
    b0 = c.p.b0
    for lab, kind, H in (("con", "Con", [(ONE, b0)]), ("decl_H0", "Sel", []), ("decl_H1", "Sel", [(ONE, b0)])):
        s, k, dec = provenance_of(c, kind, H)
        prov[lab] = {"Sel": bool(s), "Con": bool(k), "Dec": bool(dec), "AccNotDec": bool(v and not dec)}
    out["prov"] = prov
    return out


def main():
    cases = collect()
    cases.append(("Student's declared formula (FC30.new1 (a); the pole's forward candidate, the identity pair)", "S41 Q2", fwd_pole_cand()[1]))
    # (evaluate once per config)
    table = {}
    for v in [""] + VARIANTS:
        set_on(v)
        for label, where, c in cases:
            table.setdefault(label, {})[v or "off"] = evaluate(c)
    e6 = {}
    for v in [""] + VARIANTS:
        set_on(v)
        e6[v or "off"] = [(p["label"][:40], p["status"]) for p in e6_parts()]
    set_on("")
    # printout
    print("S108 section 2, worked cases: Acc (E) with no variant on (off) and with each variant on; T = holds, F = fails")
    print("scenarios for 'Acc and not Dec': (i) constructed (Con), (ii) declared, no pair tried (H = empty), (iii) declared, one pair tried")
    print("=" * 140)
    for label, where, c in cases:
        row = table[label]
        off = row["off"]
        print("%s   [%s]   |Gamma| = %d" % (label, where, len(c.Gamma)))
        print("   off: Acc %s  conj %s  witness %s  routes(min) %s" % (tf(off["acc"]), off["conj"], off["nc2_witness"], off["min_routes"]))
        print("        Acc&notDec: (i) %s (ii) %s (iii) %s" % tuple(tf(off["prov"][k]["AccNotDec"]) for k in ("con", "decl_H0", "decl_H1")))
        for v in VARIANTS:
            on = row[v]
            mv = []
            if on["acc"] != off["acc"]:
                mv.append("Acc %s->%s" % (tf(off["acc"]), tf(on["acc"])))
            for k, nm in (("con", "(i)"), ("decl_H0", "(ii)"), ("decl_H1", "(iii)")):
                if on["prov"][k]["AccNotDec"] != off["prov"][k]["AccNotDec"]:
                    mv.append("Acc&notDec %s %s->%s" % (nm, tf(off["prov"][k]["AccNotDec"]), tf(on["prov"][k]["AccNotDec"])))
            if on["routes"] != off["routes"]:
                mv.append("routes %s -> %s" % (off["min_routes"], on["min_routes"]))
            if on["nc2_witness"] != off["nc2_witness"]:
                mv.append("witness %s -> %s" % (off["nc2_witness"], on["nc2_witness"]))
            print("   %-5s %s   (Acc %s; conj %s)" % (v, ("MOVES: " + "; ".join(mv)) if mv else "no move", tf(on["acc"]), on["conj"]))
    print("=" * 140)
    print("E6 skew-symmetric (FC63 (c-i), (c-ii)) statuses:")
    for k in ["off"] + VARIANTS:
        print("   %-5s %s" % (k, e6[k]))
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            json.dump({"table": table, "e6": e6}, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
