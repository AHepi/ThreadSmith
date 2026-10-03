#!/bin/bash
# S108 Part A round 2, section 3: the generated worlds (s108r2_s3_worlds.py), in two lanes, each run with a deadline. Writes only
# into ../section 3 runs/worlds/. Round 1's seeds for the candidates (108301–108304).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
O="$HERE/../section 3 runs/worlds"
mkdir -p "$O"
cd "$HERE"
export PYTHONHASHSEED=0
run() { local name="$1"; shift; echo "$(date -u +%H:%M:%S) start $name" >> "$O/runner.log"; timeout 7200 python3 -B s108r2_s3_worlds.py "$@" > "$O/$name.txt" 2>&1; echo "$(date -u +%H:%M:%S) end $name exit $?" >> "$O/runner.log"; }
( run cands.SMALL cands "$O/cands.SMALL.json" --sizes SMALL --seed 108301
  run cands.proper cands "$O/cands.proper.json" --sizes SMALL --seed 108303 --proper
  run cands.MID cands "$O/cands.MID.json" --sizes MID --seed 108304 ) &
( run chains chains "$O/chains.json" --nmax 4
  run keys keys "$O/keys.json" --nmax 4
  run args args "$O/args.json" --seed 108306
  run cands.SMALL-vm cands "$O/cands.SMALL-vm.json" --sizes SMALL --seed 108302 --valuemaps ) &
wait
echo "$(date -u +%H:%M:%S) all ended" >> "$O/runner.log"
