# S109 Part B round 1 (rule 7): Acc and Expl (on the hand-set Dec, Con, Sel histories) of every case the scope script builds
# (the worked cases, the owner's-case encodings, the generated worlds at scale 4, seed 109001), in one fixed order, in the
# program copy given, under the reading switches set in the environment. Used to compare a Part B candidate with a Part A
# candidate case by case: run once in the Part B copy with S109B_VARIANT set, once in the Part A copy with its switch set.
#   PYTHONHASHSEED=0 [SWITCHES] python3 -B s109b_vector.py --model-dir DIR --out OUT.json
import argparse, json, os, random, sys

ap = argparse.ArgumentParser()
ap.add_argument("--model-dir", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()
sys.argv = [sys.argv[0], "--model-dir", a.model_dir, "--section", "B1", "--out", a.out]  # s109b_scope reads its arguments at import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s109b_scope as S  # noqa: E402

cases, nw = S.worked_cases()
rows = []
for lab, c in cases:
    e = S.evaluate(c)
    rows.append([lab, e["acc"], [e["prov"][k][3] for k in ("Dec", "Con", "Sel")]])
rng = random.Random(109001)
for size in S.SMALL:
    for i in range(160):
        m = S.gen_p_cand(rng, size)
        if m is None:
            continue
        p, c = m
        e = S.evaluate(c)
        rows.append(["gen %r %d" % (size, i), e["acc"], [e["prov"][k][3] for k in ("Dec", "Con", "Sel")]])
env = {k: v for k, v in os.environ.items() if k.startswith(("S108", "S109", "S105", "S106"))}
json.dump(dict(model_dir=a.model_dir, env=env, rows=rows), open(a.out, "w", encoding="utf-8"), ensure_ascii=False)
print(len(rows), "rows;", sum(r[1] for r in rows), "Acc true")
