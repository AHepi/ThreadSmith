#!/bin/bash
# S108 Part A, section 3: the claims with a part stopped by the 45 s cap in any suite run, re-run under 'none' and every reading
# at cap 300 (scale 4, PYTHONHASHSEED=0), two at a time, each run under a timeout of 3000 s. Usage: ./s108_s3_rerun_capped.sh FC23.new1 FC43 ...
cd "$(dirname "$0")" || exit 1
OUT="../section 3 runs/suite"
CL=""; for c in "$@"; do CL="$CL --claim $c"; done
run() { v="$1"; ct="$2"; tag="$v"; [ "$ct" = "build" ] && tag="$v-ctbuild"
  S108_S3_VARIANT="$v" S108_S3_CT="$ct" PYTHONHASHSEED=0 timeout 3000 python3 -B s108_s3_suite.py "$OUT/capped300.$tag.json" --scale 4 --time-cap 300 $CL > "$OUT/capped300.$tag.log" 2>&1
  echo "$tag exit $? $(date -u +%H:%M:%S)"; }
export -f run; export OUT CL
printf '%s\n' "none prepares" "V3.1 prepares" "V3.2 prepares" "V3.3 prepares" "V3.4 prepares" "V3.4 build" "V3.5 prepares" "V3.6 prepares" "V3.7 prepares" "V3.8 prepares" \
  | xargs -P 2 -L 1 bash -c 'run $0 $1'
echo "capped reruns ended $(date -u +%H:%M:%S)"
