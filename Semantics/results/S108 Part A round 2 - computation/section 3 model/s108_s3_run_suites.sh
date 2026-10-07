#!/bin/bash
# S108 Part A, section 3: the whole suite under 'none' and each variant (scale 4, cap 45, PYTHONHASHSEED=0), three at a time,
# each run under a timeout of 3000 s. Outputs: ../section 3 runs/suite/suite.<v>.json and .log.
cd "$(dirname "$0")" || exit 1
OUT="../section 3 runs/suite"
run() { v="$1"; ct="$2"; tag="$v"; [ "$ct" = "build" ] && tag="$v-ctbuild"
  S108_S3_VARIANT="$v" S108_S3_CT="$ct" PYTHONHASHSEED=0 timeout 3000 python3 -B s108_s3_suite.py "$OUT/suite.$tag.json" --scale 4 --time-cap 45 > "$OUT/suite.$tag.log" 2>&1
  echo "$tag exit $? $(date -u +%H:%M:%S)"; }
export -f run; export OUT
printf '%s\n' "none prepares" "V3.1 prepares" "V3.2 prepares" "V3.3 prepares" "V3.4 prepares" "V3.4 build" "V3.5 prepares" "V3.6 prepares" "V3.7 prepares" "V3.8 prepares" \
  | xargs -P 3 -L 1 bash -c 'run $0 $1'
echo "all suites ended $(date -u +%H:%M:%S)"
