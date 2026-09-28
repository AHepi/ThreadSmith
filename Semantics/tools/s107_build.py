#!/usr/bin/env python3
"""s107_build.py: build round 4 of the review rounds (decision S35; log S107): four GLM jobs at once (decision S39),
each a slightly different attack, in maths and code (decisions S36, S40), on the state after step S106 (the written-in
test taken out of what makes something an explanation, decisions S44 and S45; "and criticism" put back into the
opening and the bridge re-encoded, decision S47). Written 28 September 2026 by a Claude subagent (Opus 5.5) for the
orchestrator, on the model of tools/s105_build.py (round 3's build), whose parts it keeps.

  python3 Semantics/tools/s107_build.py --printouts   run the program three times (the whole suite, the external
                                                      examples, the creative transport case) on the model after S106
                                                      and write the printouts; about ten minutes
  python3 Semantics/tools/s107_build.py               build the reading copy of the text, the four briefs, the sandbox
                                                      manifest and the job list; refuses to write over a file whose
                                                      content differs; prints the table for the reading rule
  python3 Semantics/tools/s107_build.py --check       rebuild in memory and compare with the files; writes nothing

What differs from round 3's build:
- the material: the text after S106 (tests/106), the maths after S106, the records of S106 (report, critical review,
  the orchestrator's decisions, the second checker) and of round 3 (moves, integration, areas 1 and 3, critical review,
  the orchestrator's decisions, the second checker, the text changes); the text as round 3 left it (tests/105) and as
  round 3 found it (tests/104 with the owner's answers), for comparison;
- two files of round 3 are left out of the sandbox because they use the word "model" for a candidate explanation
  (decision S43; lesson S42): `S105 Round 3 - area 2 - verdicts and formal fixes.md` (its L72) and `owner questions
  after round 3.md` (its L7). Area 2 made no move; its one finding that held became the owner question R3-Q1, which
  decisions S44 and S45 answered. Every file of the sandbox is scanned for that use (MODEL_FOR_CANDIDATE) and the build
  refuses on a hit;
- the reading copy marks the lines round 3 changed (*) and the lines S106 changed (+);
- the owner's words add S43, S44, S45 and S47; the connecting words of S43, S44 and S47 that quote Claude's question
  with the word "model", or name an internal file, are replaced by plain descriptions, checked against the record;
- each brief says what "model" means in it (only a small structure the program builds, or the program's folder), and
  the frame is scanned for "model" used for a candidate as well as for the words decision S23 scrubs;
- the jobs point at what changed since round 3 (the orchestrator's brief for log S107).
Checks before anything is written: every source committed and unchanged from HEAD, with the md5s pinned below; the
owner's words against the record; the frame of each brief (everything but the owner's words); each brief at most CAP
words; round 3's 9 changed lines; the counts of S106's changed lines against its record.
"""
import hashlib, json, os, re, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
REPO = os.path.dirname(SEM)
STEP = "results/S106 The written-in test taken out"
R3 = "results/S105 Round 3 - maths after the reading"
R3R = "results/S105 Round 3 - "
R2 = "results/S104 Round 2 - maths after the reading"
R2M = "results/S104 Round 2 - maths"
MODEL_DIR = STEP + "/model after S106"
MAT = "results/S107 Round 4 - material for the readers"
READING_RULE = "results/S107 Round 4 - how the replies will be read, written before sending.md"
OUT = "results/S107 Round 4 - returns"
JOBS_FILE = "tools/s107_jobs - round 4, GLM.json"
MANIFEST = MAT + "/sandbox manifest.json"
BYLINE = MAT + "/the text under review, by line.md"
CAP = 7000
