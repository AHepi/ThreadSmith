# S108 Part A, section 1: compare a whole-suite JSON under a variant with the one under 'none' (s108_s1_suite.py outputs).
#   python3 -B s108_s1_compare.py NONE.json VARIANT.json
# Prints every claim whose status moves, and every part whose status, or whose counterexample/witness/result text, moves
# (model counts and timings are not compared). Writes nothing.
import json
import sys


def key(p):
    return p["label"]


def main():
    a, b = (json.load(open(x, encoding="utf-8")) for x in sys.argv[1:3])
    A = {c["id"]: c for c in a["claims"]}
    B = {c["id"]: c for c in b["claims"]}
    st_moves, text_moves, stops = [], [], []
    for cid in A:
        ca, cb = A[cid], B.get(cid)
        if cb is None:
            continue
        if ca["status"] != cb["status"]:
            st_moves.append((cid, ca["status"], cb["status"]))
        pa = {key(p): p for p in ca["parts"]}
        pb = {key(p): p for p in cb["parts"]}
        for lab in pa:
            x, y = pa[lab], pb.get(lab)
            if y is None:
                text_moves.append((cid, lab, "part missing under the variant", ""))
                continue
            if y.get("stopped") or x.get("stopped"):
                stops.append((cid, lab, x.get("stopped"), y.get("stopped")))
            if x["status"] != y["status"]:
                text_moves.append((cid, lab, "status %s → %s" % (x["status"], y["status"]), ""))
            else:
                for k in ("counterexample", "witness", "result"):
                    if (x.get(k) or "") != (y.get(k) or ""):
                        text_moves.append((cid, lab, "same status (%s), %s text differs" % (x["status"], k), ""))
                        break
        if (ca["error"] or "") != (cb["error"] or ""):
            text_moves.append((cid, "-", "error: %s" % ((cb["error"] or "")[-300:]), ""))
    print("variant %s vs %s: claims %d; claim status moves %d; part moves %d; time-cap stops %d" % (b["variant"], a["variant"], len(A), len(st_moves), len(text_moves), len(stops)))
    for cid, s0, s1 in st_moves:
        print("CLAIM %s: %s → %s" % (cid, s0, s1))
    for cid, lab, what, _ in text_moves:
        print("  part %s | %s | %s" % (cid, lab[:110], what))
    for s in stops:
        print("  STOP %s | %s | %s → %s" % s)
    tally = {}
    for c in b["claims"]:
        tally[c["status"]] = tally.get(c["status"], 0) + 1
    print("statuses under the variant: %s" % tally)


if __name__ == "__main__":
    main()
