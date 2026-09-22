#!/bin/sh
# P17's test: the normaliser on the checker's mocks. HOLD is expected on the *_new pairs, FAIL on every other pair.
cd "$(dirname "$0")"; N=../../tools/L79_normalise.py; bad=0
expect() { got=$(python3 "$N" "$1" "$2" | head -1); if [ "$got" = "A1 $3" ]; then echo "ok   $3  $2"; else echo "WRONG $got (expected $3)  $2"; bad=$((bad+1)); fi; }
expect T10D_old.txt T10D_new.txt HOLDS; expect T07D_old.txt T07D_new.txt HOLDS; expect P14_old.txt P14_new.txt HOLDS; expect N18A_old.txt N18A_new.txt HOLDS; expect T10B_old.txt T10B_new.txt HOLDS
# the three *_nofix reports lack one D7 gauge line: A1 accepts them (a missing count is A7's business, not a regression)
expect T10B_old.txt T10B_new_nofix.txt HOLDS; expect P14_old.txt P14_new_nofix.txt HOLDS; expect N18A_old.txt N18A_new_nofix.txt HOLDS
for f in T10D_new_unlisted T10D_new_addfinding T10D_new_dropped T10D_after_gauge T10B_after_gauge T07D_new_wrongfact T07D_new_wrongline; do o=$(echo $f | cut -d_ -f1)_old.txt; expect $o $f.txt FAILS; done
for f in A_case_NOTE_not-written_deleted A_case_gauge_marks_changed A_case_head_line_id_10-77 A_case_prose_line_deleted A_case_verdict_FOLLOWS-JUMP A_dropline A_wrongline; do expect A_old.txt $f.txt FAILS; done
echo "wrong: $bad"; exit $bad
