#!/usr/bin/env bash
# run_suite.sh - runs the prove-it-wrong test suite on one model, with one skill, in a clean folder.
#
# What this file does: makes a fresh working folder holding only a copy of the skill and the
# case files, then asks a headless Claude Code agent (on the model you name) to apply the skill
# to every case and write one answer per case. Nothing else on the computer is shown to it.
# The marking lists are NOT copied in. Afterwards, give the answers and the marking list to a
# separate grader (see README.md), never to the agent that wrote them.
#
# Usage: run_suite.sh SKILL_FOLDER CASES_FOLDER WORK_FOLDER [MODEL] [WORD_LIMIT]
#   MODEL defaults to claude-sonnet-5. Use a full model name, not an alias, so the run is repeatable.
#   WORD_LIMIT defaults to 700 (rounds 1 to 3 used 700; round 4 used 1000).
set -euo pipefail
skill_folder="$1"; cases_folder="$2"; work_folder="$3"; model="${4:-claude-sonnet-5}"; word_limit="${5:-700}"
mkdir -p "$work_folder/answers"
cp -r "$skill_folder" "$work_folder/skill"
find "$work_folder/skill" -type d -name evals -prune -exec rm -rf {} +   # the marking lists must never reach the agent under test
cp -r "$cases_folder" "$work_folder/cases"
cd "$work_folder"
prompt="You are an agent asked to review claims before they are accepted or acted on. A skill for this job is installed at ./skill/. Read ./skill/SKILL.md first and follow it, opening its reference files when it directs you to. For each case file in ./cases/, apply the skill and write your answer to ./answers/ with the same file name. If the skill has a checking script, run it on each answer and fix the answer until it passes. You cannot run the experiments described in the cases; treat anything you cannot run as the skill directs. Keep each answer under ${word_limit} words. Use only the files in this folder. When every answer is written, reply with one line per case: the file name and, if you ran a checker, its last line."
# The prompt goes in on standard input: --allowedTools takes several names and would swallow it.
printf '%s' "$prompt" | claude -p --model "$model" --safe-mode --output-format json \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash" > run_result.json
python3 - <<'PY'
import json
d = json.load(open("run_result.json"))
print("models used:", list((d.get("modelUsage") or {}).keys()))
print("cost (USD):", d.get("total_cost_usd"))
print(d.get("result", "")[-2000:])
PY
