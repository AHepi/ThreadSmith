#!/bin/sh
# L82_run.sh: the runner for Arm B. Written under plan L82 (frozen version named in the log); kept with the outputs.
# Usage: L82_run.sh CORPUS_DIR OUT_DIR PAIRS_FILE   (keys in the environment; run from the repository root;
#        OUT_DIR must not exist or must be empty; paths may be relative, they are made absolute at the top)
# PAIRS_FILE: one pair per line, "B03 B06" (F-side first), used for the within-pair sameness runs.
# Steps: 1 translate (four lanes per provider; the tool's per-provider lock, shared through ASK_MODEL_LOCKDIR, keeps
# the request rate under the limit); 2 both drivers on every valid ledger; 3 consequences_2 on every valid ledger;
# 4 sameness_2 within pairs per translator and across translators per text, then a COUNTS file (said, filled in,
# usual case, TOLD and SUPPOSED lines, world names) per ledger; 5 the blind reader (Atria) on every report, shuffled
# under neutral names, eight lanes: the heading line is replaced; every world name becomes world_1, world_2, ... in order
# of first appearance, substituted through NUL-delimited placeholders in two passes (so a world already named world_k
# cannot collide with another's neutral name) in the driver's quoted headings, after "world" or "case" in line texts
# (the guide's "[TOLD in world x]" and "[SUPPOSED in case x]" prefixes) and, for a name with an underscore or a digit,
# wherever it appears as a word; the leftover bin's quotations are cut from the GAUGE line; a plain-word name still
# present after the cut is listed in the key (name_still_present); the key records the map and the cut;
# 6 the prose reader (Mimo) on every new-driver report with its passage, eight lanes, world names left as written
# (its part 3 needs them); 7 a manifest. Every call leaves a receipt. Failed and skipped calls are listed in
# FAILED.txt (a non-zero exit, or an empty answer, exit 99) and SKIPPED.txt (an empty report) in the reader and prose_reader
# directories. Nothing is written outside OUT_DIR. No other caller of either provider may run while this script runs: the
# lock is shared within one run only, so the script refuses to start while another ask_model.py process is running.
# Token caps: 60000 for a translation (the pilot saw Mimo's reasoning alone reach 24000 on T11-B), 30000 for a reader
# or prose-reader call (Mimo's reasoning ran to 10800 tokens on the pilot's 12000-token prompt).
# Timings printed: translations, drivers, consequences, rig (drivers + consequences), reader, prose reader.
set -u
[ $# -eq 3 ] || { echo "usage: L82_run.sh CORPUS_DIR OUT_DIR PAIRS_FILE" >&2; exit 2; }
ROOT="$(pwd)"; T="$ROOT/Language/tools"; RIG="$ROOT/Language/rigs/rig 1 - arguments"
[ -f "$T/ask_model.py" ] && [ -d "$RIG/patched" ] || { echo "run from the repository root" >&2; exit 2; }
CORPUS="$(cd "$1" && pwd)" || { echo "no corpus dir $1" >&2; exit 2; }
[ -f "$3" ] || { echo "no pairs file $3" >&2; exit 2; }
PAIRS="$(cd "$(dirname "$3")" && pwd)/$(basename "$3")"
if [ -e "$2" ] && [ -n "$(ls -A "$2" 2>/dev/null)" ]; then echo "OUT_DIR $2 exists and is not empty; the drivers append to raw logs, so use a fresh directory" >&2; exit 2; fi
mkdir -p "$2"; OUT="$(cd "$2" && pwd)"
if pgrep -f "ask_model.py" > /dev/null 2>&1; then echo "another ask_model.py caller is running; it would share neither lock; stop it first" >&2; exit 2; fi
mkdir -p "$OUT/translations" "$OUT/ledgers" "$OUT/reports" "$OUT/consequences" "$OUT/sameness" "$OUT/reader" "$OUT/prose_reader" "$OUT/scratch"
export ASK_MODEL_LOCKDIR="$OUT"   # one lock per provider for every step of this run
TEXTS=$(ls "$CORPUS" | grep -E '^B[0-9]+\.txt$' | sed 's/\.txt$//')
echo "run started $(date -u +%Y-%m-%dT%H:%M:%SZ); corpus $CORPUS; out $OUT; texts: $(echo $TEXTS | wc -w)"
echo "step 1: translations $(date -u +%H:%M:%S)"; T1=$(date +%s)
# four lanes per provider: lane k takes every fourth text
for p in atria mimo; do for k in 0 1 2 3; do
  ( i=0; for t in $TEXTS; do if [ $((i % 4)) -eq $k ]; then python3 "$T/translate_via_api.py" $p "$t" "$CORPUS/$t.txt" "$OUT/translations"; fi; i=$((i+1)); done ) > "$OUT/translations/$p.lane$k.log" 2>&1 &
done; done
wait; echo "translations took $(( $(date +%s) - T1 )) s"
# gather valid ledgers into a scratch rig: the gate is the validation file's second line, VALID alone
cp -r "$RIG/patched" "$OUT/scratch/patched"; cp -r "$RIG/frozen" "$OUT/scratch/frozen" 2>/dev/null
for f in "$OUT/translations"/ledger_*.json; do [ -e "$f" ] || continue; b=$(basename "$f" .json); v="$OUT/translations/$(echo $b | sed 's/^ledger_//; s/_\([a-z]*\)$/.\1/').validation.txt"
  if [ -f "$v" ] && head -2 "$v" | grep -qx 'VALID'; then cp "$f" "$OUT/translations/$b.pl" "$OUT/ledgers/"; cp "$f" "$OUT/translations/$b.pl" "$OUT/scratch/"; fi; done
NV=$(ls "$OUT/ledgers" 2>/dev/null | grep -c '\.pl$'); echo "valid ledgers: $NV"
[ "$NV" -gt 0 ] || { echo "no valid ledger; stopping" >&2; exit 1; }
echo "step 2: drivers $(date -u +%H:%M:%S)"; T2=$(date +%s)
cd "$OUT/scratch" || exit 1
for f in ledger_*.pl; do b=$(basename "$f" .pl)
  python3 patched/run_check.py "$f" "$OUT/reports/$b.old.raw.txt" > "$OUT/reports/$b.old.txt" 2> "$OUT/reports/$b.old.err.txt" || echo "old driver failed on $b (see reports/$b.old.err.txt)"
  python3 patched/run_check_2.py "$f" "$OUT/reports/$b.new.raw.txt" > "$OUT/reports/$b.new.txt" 2> "$OUT/reports/$b.new.err.txt" || echo "new driver failed on $b (see reports/$b.new.err.txt)"
done; cd "$ROOT"
T2E=$(date +%s); echo "drivers took $(( T2E - T2 )) s"
echo "step 3: consequences_2 $(date -u +%H:%M:%S)"; T3=$(date +%s); mkdir -p "$OUT/scratch/tools" "$OUT/scratch/rigs/rig 1 - arguments"; cp "$T/consequences_2.py" "$OUT/scratch/tools/"; ln -sfn "$OUT/scratch/patched" "$OUT/scratch/rigs/rig 1 - arguments/patched"
for f in "$OUT/scratch"/ledger_*.pl; do b=$(basename "$f" .pl); python3 "$OUT/scratch/tools/consequences_2.py" "$f" "$OUT/consequences/$b.raw.txt" > "$OUT/consequences/$b.txt" 2> "$OUT/consequences/$b.err.txt" || echo "consequences_2 failed on $b"; done
T3E=$(date +%s); echo "consequences took $(( T3E - T3 )) s"; echo "rig (drivers and consequences) took $(( T3E - T2 )) s"
echo "step 4: sameness_2 and counts $(date -u +%H:%M:%S)"
while read -r a b; do [ -n "$a" ] || continue; for p in atria mimo; do [ -f "$OUT/ledgers/ledger_${a}_$p.json" ] && [ -f "$OUT/ledgers/ledger_${b}_$p.json" ] && python3 "$T/sameness_2.py" "$OUT/ledgers/ledger_${a}_$p.json" "$OUT/ledgers/ledger_${b}_$p.json" > "$OUT/sameness/pair_${a}_${b}_$p.txt"; done; done < "$PAIRS"
for t in $TEXTS; do [ -f "$OUT/ledgers/ledger_${t}_atria.json" ] && [ -f "$OUT/ledgers/ledger_${t}_mimo.json" ] && python3 "$T/sameness_2.py" "$OUT/ledgers/ledger_${t}_atria.json" "$OUT/ledgers/ledger_${t}_mimo.json" > "$OUT/sameness/across_${t}.txt"; done
python3 - "$OUT" <<'PY'
import os, sys, json
OUT = sys.argv[1]; rows = []
for f in sorted(os.listdir(os.path.join(OUT, "ledgers"))):
    if not f.endswith(".json"): continue
    m = json.load(open(os.path.join(OUT, "ledgers", f))); L = m["lines"].values()
    marks = [l.get("mark") for l in L]; st = [(l.get("standing") or "").upper() for l in L]
    worlds = sorted(set(l["case"] for l in L if l.get("case")))
    rows.append("%s: %d lines; said %d, filled in %d, usual case %d; TOLD %d, SUPPOSED %d; worlds: %s; bin entries %d; sentences %d" % (
        f[:-5], len(marks), marks.count("said"), marks.count("filled in"), marks.count("usual case"),
        sum(s.startswith("TOLD") for s in st), sum(s.startswith("SUPPOSED") for s in st), ", ".join(worlds) or "(none)", len(m.get("leftover", [])), len(m.get("sentences", []))))
open(os.path.join(OUT, "ledgers", "COUNTS.txt"), "w").write("\n".join(rows) + "\n"); print("\n".join(rows))
PY
echo "step 5: the blind reader $(date -u +%H:%M:%S)"; T5=$(date +%s)
python3 - "$OUT" "$T" <<'PY'
import os, sys, random, json, re, subprocess
from concurrent.futures import ThreadPoolExecutor
OUT, T = sys.argv[1], sys.argv[2]
reports = sorted(f for f in os.listdir(os.path.join(OUT, "reports")) if f.endswith(".old.txt") or f.endswith(".new.txt"))
rnd = random.Random(82); order = reports[:]; rnd.shuffle(order)
key = {"R%02d" % (i + 1): {"report": name} for i, name in enumerate(order)}
brief = open(os.path.join(os.path.dirname(T), "tests", "L82 Arm B corpus brief", "READER BRIEF for the API reader.md")).read()
skipped, jobs = [], []
for code, entry in key.items():
    name = entry["report"]; body = open(os.path.join(OUT, "reports", name)).read()
    lines = body.splitlines()
    if not lines or not body.strip(): skipped.append("%s %s: empty report" % (code, name)); entry["skipped"] = "empty report"; continue
    lines[0] = "REPORT for a passage"; text = "\n".join(lines)
    # world names: every case name the ledger uses, replaced in order of first appearance in the report
    meta = json.load(open(os.path.join(OUT, "ledgers", name.split(".")[0] + ".json")))
    cases = sorted(set(l["case"] for l in meta["lines"].values() if l.get("case")), key=lambda c: (text.find("'%s'" % c) if "'%s'" % c in text else 10**9, c))
    names = {c: "world_%d" % (i + 1) for i, c in enumerate(cases)}
    # two passes through placeholders, so a case already named world_k cannot collide with another's neutral name
    holders = {c: "\x00W%d\x00" % i for i, c in enumerate(cases)}
    for c, h in holders.items():
        text = text.replace("'%s'" % c, "'%s'" % h)                                          # the driver's quoted headings
        text = re.sub(r"(\b(?:world|case)\s+)%s\b" % re.escape(c), lambda m: m.group(1) + h, text)   # "[TOLD in world <name>]", "[SUPPOSED in case <name>]" in line texts
        if "_" in c or any(ch.isdigit() for ch in c): text = re.sub(r"\b%s\b" % re.escape(c), h, text)   # a coined name, wherever it appears
    # the leftover bin's quotations are cut from the GAUGE line
    text, cut = re.subn(r"\(not checked\): .*?\. Slowest question:", "(not checked). Slowest question:", text, flags=re.S)
    entry["bin_quotations_cut"] = bool(cut)
    entry["name_still_present"] = [c for c in cases if re.search(r"\b%s\b" % re.escape(c), text)]   # a plain-word name that also occurs in the prose, after the cut and before the neutral names go in
    for c, h in holders.items(): text = text.replace(h, names[c])
    entry["worlds"] = names
    up = os.path.join(OUT, "reader", code + ".prompt.txt"); open(up, "w").write(brief + text + "\n")
    jobs.append((code, up))
json.dump(key, open(os.path.join(OUT, "reader", "KEY_report_names.json"), "w"), indent=1)
def call(job):
    code, up = job
    r = subprocess.run([sys.executable, os.path.join(T, "ask_model.py"), "atria", "--user", up, "--out", os.path.join(OUT, "reader"), "--tag", code, "--max-tokens", "30000", "--temperature", "0.1"], capture_output=True, text=True)
    rc = r.returncode
    if rc == 0:
        resp = os.path.join(OUT, "reader", code + ".response.txt")
        if not os.path.exists(resp) or not open(resp).read().strip(): rc = 99   # an empty answer is a failure, not an answer
    return code, rc, (r.stderr or "").strip()[-300:]
with ThreadPoolExecutor(max_workers=8) as ex: results = list(ex.map(call, jobs))
failed = ["%s: exit %d %s" % (c, rc, err) for c, rc, err in results if rc != 0]
open(os.path.join(OUT, "reader", "FAILED.txt"), "w").write("\n".join(failed) + ("\n" if failed else ""))
open(os.path.join(OUT, "reader", "SKIPPED.txt"), "w").write("\n".join(skipped) + ("\n" if skipped else ""))
print("reader: %d reports, %d calls, %d failed, %d skipped" % (len(reports), len(jobs), len(failed), len(skipped)))
PY
echo "reader took $(( $(date +%s) - T5 )) s"
echo "step 6: the prose reader $(date -u +%H:%M:%S)"; T6=$(date +%s)
python3 - "$OUT" "$T" "$CORPUS" <<'PY'
import os, sys, subprocess
from concurrent.futures import ThreadPoolExecutor
OUT, T, CORPUS = sys.argv[1:4]
brief = open(os.path.join(os.path.dirname(T), "tests", "L82 Arm B corpus brief", "PROSE READER BRIEF for the API prose reader.md")).read()
skipped, jobs = [], []
for name in sorted(f for f in os.listdir(os.path.join(OUT, "reports")) if f.endswith(".new.txt")):
    text_id = name.split("_")[1]; tag = name.replace(".new.txt", "")
    passage = open(os.path.join(CORPUS, text_id + ".txt")).read()
    body = open(os.path.join(OUT, "reports", name)).read(); lines = body.splitlines()
    if not lines or not body.strip(): skipped.append("%s: empty report" % name); continue
    lines[0] = "REPORT for the passage above"; body = "\n".join(lines)
    up = os.path.join(OUT, "prose_reader", tag + ".prompt.txt")
    open(up, "w").write(brief + passage + "\n\n===== THE REPORT =====\n" + body + "\n")
    jobs.append((tag, up))
def call(job):
    tag, up = job
    r = subprocess.run([sys.executable, os.path.join(T, "ask_model.py"), "mimo", "--user", up, "--out", os.path.join(OUT, "prose_reader"), "--tag", tag, "--max-tokens", "30000", "--temperature", "0.1"], capture_output=True, text=True)
    rc = r.returncode
    if rc == 0:
        resp = os.path.join(OUT, "prose_reader", tag + ".response.txt")
        if not os.path.exists(resp) or not open(resp).read().strip(): rc = 99   # an empty answer is a failure, not an answer
    return tag, rc, (r.stderr or "").strip()[-300:]
with ThreadPoolExecutor(max_workers=8) as ex: results = list(ex.map(call, jobs))
failed = ["%s: exit %d %s" % (c, rc, err) for c, rc, err in results if rc != 0]
open(os.path.join(OUT, "prose_reader", "FAILED.txt"), "w").write("\n".join(failed) + ("\n" if failed else ""))
open(os.path.join(OUT, "prose_reader", "SKIPPED.txt"), "w").write("\n".join(skipped) + ("\n" if skipped else ""))
print("prose reader: %d calls, %d failed, %d skipped" % (len(jobs), len(failed), len(skipped)))
PY
echo "prose reader took $(( $(date +%s) - T6 )) s"
echo "step 7: manifest"; python3 - "$OUT" <<'PY'
import os, sys, hashlib, json
OUT = sys.argv[1]; man = {}
for d, _, fs in os.walk(OUT):
    if "/scratch" in d: continue
    for f in fs:
        if f.startswith(".rate_"): continue
        p = os.path.join(d, f); man[os.path.relpath(p, OUT)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
json.dump(man, open(os.path.join(OUT, "MANIFEST.json"), "w"), indent=1); print(len(man), "files hashed")
PY
echo "done $(date -u +%H:%M:%S)"
