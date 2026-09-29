#!/bin/bash
# S108 Part A round 2, section 3: single claims (not the whole suite, which is the harness's) under each round-2 switch: the
# claims whose code reaches the switched functions (a call graph over model/, recorded in the md, §7), each set run by the
# harness's run_claims.py (--claim …) and compared with the round-4 record. Outputs in the scratchpad, summaries copied here.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SEM="$(cd "$HERE/../../.." && pwd)"
COPY="$SEM/results/S108 Part A round 2 - computation/section 3 model"
REC="$SEM/results/S107 Round 4 - maths after the reading/formal claims, after round 4.json"
SCR="/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s108r2_s3_single"
OUT="$HERE/single"
mkdir -p "$SCR" "$OUT"
PROV="FC12.new1 FC12.new2 FC12.new3 FC23.new2 FC30.new1 FC77 FC78 FC80.new1 FC81 FC82 FC83 FC84.new1 FC84.new2 FC98 FC98.new1 FC102.new1 FC104.new1"
DEPC="FC32 FC32.new1 FC98"
ARGS="FC02 FC06 FC07 FC08 FC09 FC10 FC11 FC12 FC13 FC13.new1 FC2.new1 FC23.new2 FC25 FC27.new1 FC28.new1 FC30.new1 FC36 FC4.new1 FC40 FC47 FC47.new1 FC53 FC56 FC60 FC68 FC69 FC70 FC71 FC72 FC72.new1 FC72.new2 FC73 FC85 FC91 FC92"
one() {  # name, claims, env...
  local name="$1" cl="$2"; shift 2
  local args=()
  for c in $cl; do args+=(--claim "$c"); done
  env "$@" timeout 3000 python3 -B "$SEM/tools/sonnet_harness/run_claims.py" --model-dir "$COPY" --out-dir "$SCR/$name" --scale 4 --time-cap 45 \
      --timeout 2900 --expect "$REC" --expect-key after_round4 "${args[@]}" > "$OUT/$name.json" 2>&1
  cp "$SCR/$name/raw.txt" "$OUT/$name.raw.txt" 2>/dev/null
  echo "$(date -u +%H:%M:%S) $name done" >> "$OUT/runner.log"
}
one off "$PROV FC90.new1 $DEPC" S108R2_S3_VARIANT=none
one R2V3.1 "$PROV FC90.new1 $DEPC" S108R2_S3_VARIANT=R2V3.1
one R2V3.2-contract "$PROV" S108R2_S3_RECKEY=contract
one R2V3.4-ports "$PROV" S108R2_S3_VARIANT=R2V3.4 S108R2_S3_PARTS=ports
one R2V3.4-edits "$PROV" S108R2_S3_VARIANT=R2V3.4 S108R2_S3_PARTS=edits
one R2V3.5 "$PROV" S108R2_S3_VARIANT=R2V3.5
one R2V3.6 "$PROV" S108R2_S3_VARIANT=R2V3.6
one R2V3.7 "$PROV" S108R2_S3_VARIANT=R2V3.7
one R2V3.10 "$DEPC" S108R2_S3_VARIANT=R2V3.10
one R2V3.8 "$ARGS" S108R2_S3_VARIANT=R2V3.8
one R2V3.9 "$ARGS" S108R2_S3_VARIANT=R2V3.9
one off-args "$ARGS" S108R2_S3_VARIANT=none
echo "$(date -u +%H:%M:%S) all done" >> "$OUT/runner.log"
