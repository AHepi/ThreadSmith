#!/bin/bash
# S108 Part A round 2, section 3: the external examples (FC-E1–FC-E5), the creative transport case (CT1–CT8) and the written-in
# step's case script, each under every round-2 switch, compared line by line with the run with every switch off (whose md5s
# are the committed printouts'). Run from anywhere; writes only into ../section 3 runs/scripts/.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../section 3 runs/scripts"
mkdir -p "$OUT"
cd "$HERE"
export PYTHONHASHSEED=0
declare -A ENVS=(
  [none]=""
  [R2V3.1]="S108R2_S3_VARIANT=R2V3.1"
  [R2V3.2-contract]="S108R2_S3_RECKEY=contract"
  [R2V3.4-ports]="S108R2_S3_VARIANT=R2V3.4 S108R2_S3_PARTS=ports"
  [R2V3.4-edits]="S108R2_S3_VARIANT=R2V3.4 S108R2_S3_PARTS=edits"
  [R2V3.5]="S108R2_S3_VARIANT=R2V3.5"
  [R2V3.6]="S108R2_S3_VARIANT=R2V3.6"
  [R2V3.7]="S108R2_S3_VARIANT=R2V3.7"
  [R2V3.8]="S108R2_S3_VARIANT=R2V3.8"
  [R2V3.9]="S108R2_S3_VARIANT=R2V3.9"
  [R2V3.10]="S108R2_S3_VARIANT=R2V3.10"
)
ORDER="none R2V3.1 R2V3.2-contract R2V3.4-ports R2V3.4-edits R2V3.5 R2V3.6 R2V3.7 R2V3.8 R2V3.9 R2V3.10"
for s in s104_external s104_creative_transport s106_cases; do
  for v in $ORDER; do
    env ${ENVS[$v]} timeout 900 python3 -B "$s.py" > "$OUT/$s.$v.txt" 2>&1
  done
done
{
  for s in s104_external s104_creative_transport s106_cases; do
    echo "== $s: 'none' md5 $(md5sum < "$OUT/$s.none.txt" | cut -d' ' -f1)"
    for v in $ORDER; do
      [ "$v" = none ] && continue
      n=$(diff "$OUT/$s.none.txt" "$OUT/$s.$v.txt" | grep -c '^[<>]')
      echo "   $v: $n lines differ"
      diff "$OUT/$s.none.txt" "$OUT/$s.$v.txt" | grep '^[<>]' | head -20 | sed 's/^/      /'
    done
  done
} > "$OUT/compare.txt"
cat "$OUT/compare.txt"
