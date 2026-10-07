#!/bin/bash
# S108 Part A round 1, the second checker: the runs behind O1, O2 and O3. Each runs inside a section copy (read-only imports,
# python3 -B, no file of the copy written) and writes its output here. Usage: bash runs.sh [o3]  (o3: also the n ≤ 4 chains, ~5 min)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
C="$HERE/.."
export PYTHONHASHSEED=0
enc='import sys; sys.path.insert(0, sys.argv[1]); import owner_cases as o
from model.claims_a import table_candidate
from model.core import account
for n, f in o.CASES:
    c = f(); e = table_candidate(c.p, set(c.p.D.ports), encode=True)
    print(o.row(n, c)[:400]); print("%-34s E_enc on its question: Acc %s" % ("", account(e)))'
{
  cd "$C/section 1 model"
  for v in none V1.1 V1.5; do echo "== section 1, $v"; S108_S1_VARIANT=$v timeout 120 python3 -B -c "$enc" "$HERE"; done
  cd "$C/section 2 model"
  for v in off V2.1 V2.2 V2.3 V2.4; do echo "== section 2, $v"; S108_S2_VARIANT=$v timeout 120 python3 -B -c "$enc" "$HERE"; done
  cd "$C/section 4 model"
  for q in every some some-exempt some-exempt-set; do echo "== section 4, V4.1, quantifier $q (Dec F)"
    S108_S4_VARIANT=V4.1 S108_S4_V41_Q=$q timeout 120 python3 -B -c 'import sys; sys.path.insert(0, sys.argv[1]); import owner_cases as o
from model import s108_s4 as s4
from model.core import account
for n, f in o.CASES:
    c = f(); a = account(c); sl = s4.has_slot(c)
    print("%-34s Acc %-5s Slot %-5s being an explanation: V4.1 %-5s none %s" % (n, a, sl, s4.expl(a, False, slot=sl), s4.expl(a, False, variant="none")))' "$HERE"; done
} > "$HERE/owner cases - output.txt" 2>&1
cd "$C/section 3 model"
timeout 600 python3 -B "$HERE/o3_trace_extent.py" 3 > "$HERE/o3 trace extent - n le 3 - output.txt" 2>&1
if [ "${1:-}" = "o3" ]; then timeout 900 python3 -B "$HERE/o3_trace_extent.py" 4 "T'" T > "$HERE/o3 trace extent - n le 4 - output.txt" 2>&1; fi
