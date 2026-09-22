# L79 Arm A -- RUN SUMMARY

Written by the runner. It records what was run, how long it took, on what
machine, which files the A1 instrument failed, and what went to standard
error. It marks nothing: A1 to A8 are the marker's business, not the
runner's.

Plan: `Language/tests/L79 Test plan - Arm A, the ledgers in hand on the old rig
and the new, third version.md` (SHA-256 begins 2e97300690dc39f7).

## Counts

| | |
| --- | --- |
| Ledgers run | 76 |
| &nbsp;&nbsp;of which `rig1` -- `Language/rigs/rig 1 - arguments/` (top level) | 36 |
| &nbsp;&nbsp;of which `r45` -- `Language/results/45 Reruns by the orchestrator/` | 8 |
| &nbsp;&nbsp;of which `l69` -- `Language/results/L69 Return - L66 run by OpenAI Codex/rigs/rig 1 - arguments/` | 23 |
| &nbsp;&nbsp;of which `l72` -- `Language/results/L72 Return - Astra Ultra/rigs/rig 1 - arguments/` | 9 |
| Old-driver reports written | 76 |
| New-driver reports written | 76 |
| Normaliser comparisons run | 76 |
| `A1 HOLDS` | 76 |
| `A1 FAILS` | 0 |
| `consequences_2.py` runs | 4 |
| `consequences.py` (old) runs | 0 -- its baseline exists (plan P5, P15) |
| Non-empty stderr files | 0 |

## Timings

Wall clock for a whole pass over all 76 ledgers, one ledger at a time, one
process at a time.

| Pass | Seconds |
| --- | --- |
| OLD driver, `patched/run_check.py`, all 76 | 97.0 |
| NEW driver, `patched/run_check_2.py`, all 76 | 110.0 |
| Both passes together | 207.0 |

## The machine

This session's container.

- `swipl --version`: `SWI-Prolog version 9.0.4 for x86_64-linux`
- `/home/claude/sCASP/scasp --version`: `% s(CASP): version 1.1.4 on SWI-Prolog 9.0.4`
- `uname -srm`: `Linux 6.18.44-fc-v37 x86_64`
- `python3 --version`: `Python 3.11.15`

## A1 FAILS

None. The normaliser printed `A1 HOLDS` on all 76 ledgers.

## Standard error

Every `.err.txt` file in this folder is empty: no run wrote to standard error.

