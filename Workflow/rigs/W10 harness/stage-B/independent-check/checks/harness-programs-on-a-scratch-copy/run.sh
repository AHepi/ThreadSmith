#!/usr/bin/env bash
# How the files in this folder were made, 23 September 2026, by the comparison worker of stage B.
#
# The harness's own collection stopped at its command 1 in place, because <rig>/runs/record96/ is
# gitignored and was not in this checkout (see ../../../collection/01-first-collect.txt). Nothing in
# the repository was changed to get past that. Instead the harness's programs, unchanged, were run
# on a copy of the rig in scratch space outside the repository:
#   - code/, instrument/, marking/ and stage-B/w10/ copied, and `diff -r` shown identical;
#   - record_adapter.py (unchanged) run from the copy, reading the real record and writing the 96
#     run records into the COPY's runs/record96/ (rig.py computes every path from its own file);
#   - the six commands of the handover's step 2, run unchanged, in order, from the copy's code/.
# The logs 00 to 06 and the two count files beside this script are what those runs wrote.
# This is NOT the canonical collection: <rig>/marking/ in the repository still holds only the
# closed mapping. Running the adapter in place is the orchestrator's decision (harness worker's return).
#
# Usage: bash run.sh <scratch dir outside the repository>
set -u
S="${1:?give a scratch directory outside the repository}"
RIG="/home/user/ThreadSmith/Workflow/rigs/W10 harness"
PY=/home/user/.venvs/threadsmith/bin/python
export PYTHONDONTWRITEBYTECODE=1
rm -rf "$S" && mkdir -p "$S/W10 harness/stage-B"
cd "$RIG" && cp -r code instrument marking "$S/W10 harness/" && cp -r stage-B/w10 "$S/W10 harness/stage-B/"
rm -rf "$S/W10 harness/code/__pycache__"
diff -r code "$S/W10 harness/code" -x __pycache__ && diff -r instrument "$S/W10 harness/instrument" \
  && diff -r marking "$S/W10 harness/marking" && diff -r stage-B/w10 "$S/W10 harness/stage-B/w10" && echo "copy identical"
cd "$S/W10 harness/code"
$PY record_adapter.py --record "/home/user/ThreadSmith/HV Skill/rigs/plan 49 rig - DeepSeek on outside papers" > "$S/00-adapter.txt" 2>&1
run(){ n=$1; shift; echo "command: $*" > "$S/$n.txt"; "$@" >>"$S/$n.txt" 2>&1; echo "exit code: $?" >> "$S/$n.txt"; }
run 01-first-collect  $PY first_marker.py collect --scratch "../stage-B" --reader record96 --tag first
run 02-second-collect $PY second_marker.py collect --scratch "../stage-B" --reader record96
run 03-validate-first  $PY first_marker.py validate --marks ../marking/marks_first_record96.json
run 04-validate-second $PY first_marker.py validate --marks ../marking/marks_second_record96.json
run 05-compare $PY second_marker.py compare --scratch "../stage-B" --reader record96
run 06-stage-b $PY stage_b.py --reader record96
echo "outputs: $S/W10 harness/marking/ and $S/0*.txt"
