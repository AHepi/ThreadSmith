#!/bin/sh
# L86_run.sh OUT_DIR: runs the driver's third version on the four L86 mocks, the 32 Arm B ledgers and the 76 Arm A ledgers
# (plan L86), in a scratch copy of the rig, and leaves per set: the reports (<name>.third.txt, .raw.txt, .err.txt), the
# comparison with the second version's stored report (<name>.compare.txt, from L86_compare.py), and RUN SUMMARY.md with
# the seconds each set took and the counts E3 and E4 read (JUMP. heads, NO CONNECTION. heads, block headings). Run from
# the repository root. Written 23 September 2026 for plan L86.
set -u
ROOT="$(pwd)"; T="$ROOT/Language/tools"; RIG="$ROOT/Language/rigs/rig 1 - arguments"; OUT="$(mkdir -p "$1" && cd "$1" && pwd)"
mkdir -p "$OUT/scratch" "$OUT/mocks" "$OUT/armB" "$OUT/armA"; cp -r "$RIG/patched" "$OUT/scratch/patched"
run_set() { # $1 set name, $2 dir of ledgers (json+pl), $3 dir of old reports or "", $4 old report pattern
  set_name="$1"; src="$2"; old="$3"; pat="$4"; T0=$(date +%s); n=0
  for pl in "$src"/*.pl; do [ -e "$pl" ] || continue; b=$(basename "$pl" .pl); cp "$pl" "${pl%.pl}.json" "$OUT/scratch/" 2>/dev/null || { echo "$b: no json" >> "$OUT/$set_name/SKIPPED.txt"; continue; }
    ( cd "$OUT/scratch" && python3 patched/run_check_3.py "$b.pl" "$OUT/$set_name/$b.raw.txt" > "$OUT/$set_name/$b.third.txt" 2> "$OUT/$set_name/$b.err.txt" ) || echo "$b: driver exit non-zero" >> "$OUT/$set_name/FAILED.txt"
    n=$((n+1))
    if [ -n "$old" ]; then o=$(printf "$pat" "$b"); [ -f "$old/$o" ] && python3 "$T/L86_compare.py" "$old/$o" "$OUT/$set_name/$b.third.txt" > "$OUT/$set_name/$b.compare.txt" 2>&1 || echo "$b: no old report $old/$o" >> "$OUT/$set_name/NO_OLD.txt"; fi
  done
  echo "$set_name: $n ledgers, $(( $(date +%s) - T0 )) s" >> "$OUT/RUN SUMMARY.md"
}
: > "$OUT/RUN SUMMARY.md"; echo "run started $(date -u +%Y-%m-%dT%H:%M:%SZ); run_check_3.py $(sha256sum "$RIG/patched/run_check_3.py" | cut -c1-16)" >> "$OUT/RUN SUMMARY.md"
run_set mocks "$ROOT/Language/tests/L86 Mocks" "" ""
run_set armB "$ROOT/Language/results/L82 Arm B outputs/ledgers" "$ROOT/Language/results/L82 Arm B outputs/reports" "%s.new.txt"
# Arm A: the 76 ledgers of plan L79's P14, in their four places, against the L79 outputs
mkdir -p "$OUT/armA_src"; i=0
for d in "rig1:$RIG" "r45:$ROOT/Language/results/45 Reruns by the orchestrator" "l69:$ROOT/Language/results/L69 Return - L66 run by OpenAI Codex/rigs/rig 1 - arguments" "l72:$ROOT/Language/results/L72 Return - Astra Ultra/rigs/rig 1 - arguments"; do
  tag=${d%%:*}; dir=${d#*:}; mkdir -p "$OUT/armA/$tag" "$OUT/armA_src/$tag"
  for pl in "$dir"/ledger_*.pl; do [ -e "$pl" ] || continue; cp "$pl" "${pl%.pl}.json" "$OUT/armA_src/$tag/" 2>/dev/null; done
  run_set "armA/$tag" "$OUT/armA_src/$tag" "$ROOT/Language/results/L79 Arm A outputs/$tag" "%s.new.txt"
done
python3 - "$OUT" <<'PY'
import os, sys, re
OUT = sys.argv[1]; rows = []
for root, _, files in os.walk(OUT):
    if "/scratch" in root or "armA_src" in root: continue
    for f in sorted(files):
        if not f.endswith(".third.txt"): continue
        t = open(os.path.join(root, f)).read()
        jumps = len(re.findall(r"(?m)^\s*JUMP\.", t)); nocs = len(re.findall(r"(?m)^\s*NO CONNECTION\.", t))
        blocks = len(re.findall(r"(?m)^\s*General lines that could", t)); reached = len(re.findall(r"(?m)^\s*Reached without the reason:", t))
        cmp = os.path.join(root, f.replace(".third.txt", ".compare.txt")); c = open(cmp).read().split("\n")[0] if os.path.exists(cmp) else "-"
        rows.append((os.path.relpath(os.path.join(root, f), OUT), jumps, nocs, blocks, reached, c))
same = sum(1 for r in rows if r[5] == "SAME"); diff = [r[0] for r in rows if r[5].startswith("DIFFERENT")]; nocmp = sum(1 for r in rows if r[5] == "-")
bad = [r[0] for r in rows if r[3] != r[1] + r[2] or r[4] != r[2]]
with open(os.path.join(OUT, "RUN SUMMARY.md"), "a") as s:
    s.write("reports: %d; compared SAME: %d; DIFFERENT: %d (%s); not compared: %d\n" % (len(rows), same, len(diff), ", ".join(diff) or "-", nocmp))
    s.write("block counts off (blocks != JUMP + NO CONNECTION heads, or Reached != NO CONNECTION): %d (%s)\n" % (len(bad), ", ".join(bad) or "-"))
    s.write("\n| report | JUMP. | NO CONNECTION. | General lines blocks | Reached blocks | compare |\n| --- | --- | --- | --- | --- | --- |\n")
    for r in rows: s.write("| %s | %d | %d | %d | %d | %s |\n" % r)
print(open(os.path.join(OUT, "RUN SUMMARY.md")).read()[:1500])
PY
