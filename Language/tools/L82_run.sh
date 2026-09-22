#!/bin/sh
# L82_run.sh: the runner for Arm B. Written under plan L82 (frozen version named in the log); kept with the outputs.
# Usage: L82_run.sh CORPUS_DIR OUT_DIR PAIRS_FILE   (keys in the environment; run from the repository root)
# PAIRS_FILE: one pair per line, "B03 B06" (F-side first), used for the within-pair sameness runs.
# Steps: 1 translate (Atria and Mimo in parallel, texts sequential per provider); 2 both drivers on every ledger;
# (translations run in four lanes per provider; the tool's per-provider lock keeps the request rate under the limit)
# 3 consequences_2 on every ledger; 4 sameness_2 within pairs per translator and across translators per text;
# 5 the blind reader (Atria) on every report, shuffled under neutral names; 6 the prose reader (Mimo) on every new report
# with its passage; 7 a manifest. Every call leaves a receipt. Nothing is written outside OUT_DIR.
set -u
CORPUS="$1"; OUT="$2"; PAIRS="$3"; ROOT="$(pwd)"; T="$ROOT/Language/tools"; RIG="$ROOT/Language/rigs/rig 1 - arguments"
mkdir -p "$OUT/translations" "$OUT/ledgers" "$OUT/reports" "$OUT/consequences" "$OUT/sameness" "$OUT/reader" "$OUT/prose_reader" "$OUT/scratch"
TEXTS=$(ls "$CORPUS" | grep -E '^B[0-9]+\.txt$' | sed 's/\.txt$//')
echo "step 1: translations $(date -u +%H:%M:%S)"; T1=$(date +%s)
# four lanes per provider: lane k takes every fourth text; the tool's per-provider lock keeps the request rate under the limit
for p in atria mimo; do for k in 0 1 2 3; do
  ( i=0; for t in $TEXTS; do if [ $((i % 4)) -eq $k ]; then python3 "$T/translate_via_api.py" $p "$t" "$CORPUS/$t.txt" "$OUT/translations"; fi; i=$((i+1)); done ) > "$OUT/translations/$p.lane$k.log" 2>&1 &
done; done
wait; echo "translations took $(( $(date +%s) - T1 )) s"
# gather valid ledgers into a scratch rig
cp -r "$RIG/patched" "$OUT/scratch/patched"; cp -r "$RIG/frozen" "$OUT/scratch/frozen" 2>/dev/null
for f in "$OUT/translations"/ledger_*.json; do b=$(basename "$f" .json); if grep -q '^VALID' "$OUT/translations/$(echo $b | sed 's/^ledger_//; s/_\([a-z]*\)$/.\1/').validation.txt" 2>/dev/null; then cp "$f" "$OUT/translations/$b.pl" "$OUT/ledgers/"; cp "$f" "$OUT/translations/$b.pl" "$OUT/scratch/"; fi; done
echo "valid ledgers: $(ls "$OUT/ledgers" | grep -c '\.pl$')"
echo "step 2: drivers $(date -u +%H:%M:%S)"; T2=$(date +%s)
cd "$OUT/scratch"; for f in ledger_*.pl; do b=$(basename "$f" .pl); python3 patched/run_check.py "$f" "$OUT/reports/$b.old.raw.txt" > "$OUT/reports/$b.old.txt" 2> "$OUT/reports/$b.old.err.txt"; python3 patched/run_check_2.py "$f" "$OUT/reports/$b.new.raw.txt" > "$OUT/reports/$b.new.txt" 2> "$OUT/reports/$b.new.err.txt"; done; cd "$ROOT"
echo "drivers took $(( $(date +%s) - T2 )) s"
echo "step 3: consequences_2"; mkdir -p "$OUT/scratch/tools" "$OUT/scratch/rigs/rig 1 - arguments"; cp "$T/consequences_2.py" "$OUT/scratch/tools/"; ln -sfn "$OUT/scratch/patched" "$OUT/scratch/rigs/rig 1 - arguments/patched"
for f in "$OUT/scratch"/ledger_*.pl; do b=$(basename "$f" .pl); python3 "$OUT/scratch/tools/consequences_2.py" "$f" "$OUT/consequences/$b.raw.txt" > "$OUT/consequences/$b.txt" 2> "$OUT/consequences/$b.err.txt"; done
echo "step 4: sameness_2"
while read -r a b; do for p in atria mimo; do [ -f "$OUT/ledgers/ledger_${a}_$p.json" ] && [ -f "$OUT/ledgers/ledger_${b}_$p.json" ] && python3 "$T/sameness_2.py" "$OUT/ledgers/ledger_${a}_$p.json" "$OUT/ledgers/ledger_${b}_$p.json" > "$OUT/sameness/pair_${a}_${b}_$p.txt"; done; done < "$PAIRS"
for t in $TEXTS; do [ -f "$OUT/ledgers/ledger_${t}_atria.json" ] && [ -f "$OUT/ledgers/ledger_${t}_mimo.json" ] && python3 "$T/sameness_2.py" "$OUT/ledgers/ledger_${t}_atria.json" "$OUT/ledgers/ledger_${t}_mimo.json" > "$OUT/sameness/across_${t}.txt"; done
echo "step 5: the blind reader $(date -u +%H:%M:%S)"; T5=$(date +%s)
python3 - "$OUT" "$T" <<'PY'
import os, sys, random, json, subprocess
OUT, T = sys.argv[1], sys.argv[2]
reports = sorted(f for f in os.listdir(os.path.join(OUT, "reports")) if f.endswith(".old.txt") or f.endswith(".new.txt"))
rnd = random.Random(82); order = reports[:]; rnd.shuffle(order)
key = {"R%02d" % (i + 1): name for i, name in enumerate(order)}
json.dump(key, open(os.path.join(OUT, "reader", "KEY_report_names.json"), "w"), indent=1)
brief = open(os.path.join(os.path.dirname(T), "tests", "L82 Arm B corpus brief", "READER BRIEF for the API reader.md")).read()
for code, name in key.items():
    body = open(os.path.join(OUT, "reports", name)).read().replace("REPORT for paragraph", "REPORT for passage")
    # neutral names: strip the ledger id and translator from the heading line
    lines = body.splitlines(); lines[0] = "REPORT for a passage"; body = "\n".join(lines)
    up = os.path.join(OUT, "reader", code + ".prompt.txt"); open(up, "w").write(brief + body + "\n")
    subprocess.run([sys.executable, os.path.join(T, "ask_model.py"), "atria", "--user", up, "--out", os.path.join(OUT, "reader"), "--tag", code, "--max-tokens", "4000", "--temperature", "0.1"])
PY
echo "reader took $(( $(date +%s) - T5 )) s"
echo "step 6: the prose reader $(date -u +%H:%M:%S)"; T6=$(date +%s)
python3 - "$OUT" "$T" "$CORPUS" <<'PY'
import os, sys, subprocess
OUT, T, CORPUS = sys.argv[1:4]
brief = open(os.path.join(os.path.dirname(T), "tests", "L82 Arm B corpus brief", "PROSE READER BRIEF for the API prose reader.md")).read()
for name in sorted(f for f in os.listdir(os.path.join(OUT, "reports")) if f.endswith(".new.txt")):
    text_id = name.split("_")[1]
    passage = open(os.path.join(CORPUS, text_id + ".txt")).read()
    body = open(os.path.join(OUT, "reports", name)).read(); lines = body.splitlines(); lines[0] = "REPORT for the passage above"; body = "\n".join(lines)
    up = os.path.join(OUT, "prose_reader", name.replace(".new.txt", "") + ".prompt.txt")
    open(up, "w").write(brief + passage + "\n\n===== THE REPORT =====\n" + body + "\n")
    subprocess.run([sys.executable, os.path.join(T, "ask_model.py"), "mimo", "--user", up, "--out", os.path.join(OUT, "prose_reader"), "--tag", name.replace(".new.txt", ""), "--max-tokens", "4000", "--temperature", "0.1"])
PY
echo "prose reader took $(( $(date +%s) - T6 )) s"
echo "step 7: manifest"; python3 - "$OUT" <<'PY'
import os, sys, hashlib, json
OUT = sys.argv[1]; man = {}
for d, _, fs in os.walk(OUT):
    if "/scratch" in d: continue
    for f in fs:
        p = os.path.join(d, f); man[os.path.relpath(p, OUT)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
json.dump(man, open(os.path.join(OUT, "MANIFEST.json"), "w"), indent=1); print(len(man), "files hashed")
PY
echo "done $(date -u +%H:%M:%S)"
