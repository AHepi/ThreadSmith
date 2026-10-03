# S108 Part A round 2, section 1: compare one whole-suite run (run_claims.py's claims.json and raw.txt) with the round-4
# record and with what the computing agent expects to move. A reader only: prints one JSON object, writes nothing.
#   python3 -B s108r2_s1_suite_check.py --claims RUN/claims.json --record "formal claims, after round 4.json" --key after_round4
#          --expected "suite - expected moves.json" --run NAME [--off-raw OFF/raw.txt --on-raw RUN/raw.txt]
# moved = the claims whose status, or whose parts' (label, kind, status), differ from the record. ok = moved equals the
# expected set for NAME exactly. text_moved (a look, never part of ok): the claims whose printed block differs between the
# run with every variant off and this run (counts of models tried and timings removed).
import argparse
import json
import re
import sys

sys.dont_write_bytecode = True


def blocks(raw):
    """claim id -> its printed block, with timings and model counts removed."""
    out, cur = {}, None
    lines = raw.split("\n")
    head = re.compile(r"^(\S+)  (HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)  \(([\d.]+) s\)$")
    for i, ln in enumerate(lines):
        m = head.match(ln)
        if m and i > 0 and lines[i - 1].startswith("=" * 20):
            cur = m.group(1)
            out[cur] = [m.group(2)]
            continue
        if cur is None or ln.startswith("=" * 20):
            continue
        ln = re.sub(r"\([\d.]+ s\)", "", ln)
        ln = re.sub(r"\b\d+ models? tried\b", "N models tried", ln)
        ln = re.sub(r"models_tried[=: ]+\d+", "models_tried N", ln)
        out[cur].append(ln)
    return {k: "\n".join(v) for k, v in out.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", required=True)
    ap.add_argument("--record", required=True)
    ap.add_argument("--key", default="after_round4")
    ap.add_argument("--expected", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--off-raw")
    ap.add_argument("--on-raw")
    a = ap.parse_args()
    rec = json.load(open(a.record, encoding="utf-8"))
    want = {c["id"]: c[a.key] for c in rec["claims"]}
    got = {c["id"]: c for c in json.load(open(a.claims, encoding="utf-8"))["claims"]}
    exp = json.load(open(a.expected, encoding="utf-8"))["runs"][a.run]
    status_moved, parts_moved, missing_in_run = [], [], []
    for cid, w in want.items():
        g = got.get(cid)
        if g is None:
            missing_in_run.append(cid)
            continue
        if w["status"] != g["status"]:
            status_moved.append(dict(id=cid, recorded=w["status"], got=g["status"]))
        wp = [(p["label"], p["kind"], p["status"]) for p in w.get("parts", [])]
        gp = [(p["label"], p["kind"], p["status"]) for p in g["parts"]]
        if wp != gp:
            parts_moved.append(dict(id=cid, parts=[dict(label=x[0], recorded=x[2], got=y[2]) for x, y in zip(wp, gp) if x != y]
                                    + ([dict(count_recorded=len(wp), count_got=len(gp))] if len(wp) != len(gp) else [])))
    moved = sorted(set(x["id"] for x in status_moved) | set(x["id"] for x in parts_moved))
    exp_moved = sorted(exp["moved"])
    out = dict(run=a.run, expected_moved=exp_moved, moved=moved, status_moved=status_moved, parts_moved=parts_moved,
               unexpected=sorted(set(moved) - set(exp_moved)), missing=sorted(set(exp_moved) - set(moved)),
               claims_missing_in_run=missing_in_run, extra_claims_in_run=sorted(set(got) - set(want)))
    if a.off_raw and a.on_raw:
        off, on = blocks(open(a.off_raw, encoding="utf-8").read()), blocks(open(a.on_raw, encoding="utf-8").read())
        out["text_moved"] = sorted(k for k in set(off) | set(on) if off.get(k) != on.get(k))
        out["text_moved_status_kept"] = sorted(set(out["text_moved"]) - set(moved))
    out["ok"] = not out["unexpected"] and not out["missing"] and not missing_in_run and not out["extra_claims_in_run"]
    print(json.dumps(out, ensure_ascii=False))
    sys.exit(0 if out["ok"] else 1)


if __name__ == "__main__":
    main()
