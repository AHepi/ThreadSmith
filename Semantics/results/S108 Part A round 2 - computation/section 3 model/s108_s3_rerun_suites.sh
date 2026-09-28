#!/bin/bash
# S108 Part A, section 3: re-run of the whole suite under V3.1, V3.2, V3.3 and V3.5 after two fixes to the copy (FC90.new1's
# note printed only under V3.4; FC84.new2's own encodings of D13.8's record clause switched with V3.5), two at a time,
# the same settings as s108_s3_run_suites.sh. Outputs replace ../section 3 runs/suite/suite.<v>.json and .log.
cd "$(dirname "$0")" || exit 1
OUT="../section 3 runs/suite"
run() { v="$1"
  S108_S3_VARIANT="$v" S108_S3_CT=prepares PYTHONHASHSEED=0 timeout 3000 python3 -B s108_s3_suite.py "$OUT/suite.$v.json" --scale 4 --time-cap 45 > "$OUT/suite.$v.log" 2>&1
  echo "$v rerun exit $? $(date -u +%H:%M:%S)"; }
export -f run; export OUT
printf '%s\n' V3.5 V3.1 V3.2 V3.3 | xargs -P 2 -L 1 bash -c 'run $0'
echo "reruns ended $(date -u +%H:%M:%S)"
