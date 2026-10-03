#!/bin/bash
# S109 Part B round 1: the scope runs of sections B1-B3, one at a time, after the whole-suite queue (at most 3 heavy runs).
C="/home/user/ThreadSmith/Semantics/results/S109 Part B round 1 - computation"
QP=$(cat /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s109b_queue.pid)
while kill -0 "$QP" 2>/dev/null && [ "$(grep -c '^.* end ' "$C/whole suite/queue log.txt")" -lt 30 ]; do sleep 20; done
for s in B1 B2 B3; do
  echo "$(date -u +%H:%M:%S) start scope $s"
  cd "$C" && PYTHONHASHSEED=0 timeout 3600 python3 -B scripts/s109b_scope.py --model-dir "section $s model" --section $s --out "section $s runs/scope.json" > "section $s runs/scope.stdout.txt" 2>&1
  echo "$(date -u +%H:%M:%S) end scope $s exit $?"
done
