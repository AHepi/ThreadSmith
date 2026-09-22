"""Build an instruction pack for a fresh agent: one zip holding the instruction (paste part only),
the authority, the workflow files, the earlier rounds' instructions, and the returns.
Run from the repository root:  python3 "Semantics/tests/Instruction pack - build.py" S70 <out dir>
For a later instruction, change INSTRUCTION and add the newest return to RETURNS."""
import os, re, shutil, sys, zipfile
NUM = sys.argv[1] if len(sys.argv) > 1 else "S65"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/pack"
S = "Semantics"; T = f"{S}/tests/"; R = f"{S}/results/"
INSTRUCTION = {"S65": T + "S65 Next instruction for the other model - thirteen near cases, two attribution tests, returned as a zip.md",
               "S70": T + "S70 Next instruction for the other model - twelve near cases, the protected condition stated first, returned as a zip.md",
               "S71": T + "S71 Next instruction for the other model - the bare earlier version against every case, and three more, returned as a zip.md",
               "S72-1": T + "S72 Stage 1 testing - the bare earlier version against every case, and three more, returned as a zip.md",
               "S72-2": T + "S72 Stage 2 audit - check the testing return, then build the draft list from what survives, returned as a zip.md"}[NUM]
README = T + "Instruction pack - read me first for the agent.md"
EARLIER = [
 ("27 Next instruction for the other model - round 3, outside cases.md", "27 Round 3 - outside cases O1 to O4.md"),
 ("28 Next instruction for the other model - round 4, two change-based clauses.md", "28 Round 4 - two change-based clauses, O5 to O7.md"),
 ("41 Next instruction for the other model - finish Stage B and near cases.md", "41 Finish Stage B and near cases.md"),
 ("S62 Next instruction for the other model - Stage D, clause tests, coverage and the report, returned as a zip.md", "S62 Instruction - Stage D, clause tests, coverage and the report.md"),
 ("S64 Next instruction for the other model - ten near cases, verdicts under the earlier version, returned as a zip.md", "S64 Instruction - ten near cases under the earlier version.md"),
 ("S65 Next instruction for the other model - thirteen near cases, two attribution tests, returned as a zip.md", "S65 Instruction - thirteen near cases, two attribution tests.md"),
 ("S70 Next instruction for the other model - twelve near cases, the protected condition stated first, returned as a zip.md", "S70 Instruction - twelve near cases, the protected condition stated first.md"),
]
RETURNS = [
 ("55 Stage B return - the other model's finished table, near cases and tighter pairs.md", "55 Stage B return - table, near cases, tighter pairs.md"),
 ("57 Stage C return - the other model's seven case cards, O4 placed, phrases sorted.md", "57 Stage C return - cards O8 to O14, O4 placed, phrases sorted.md"),
 ("S62 Stage D and report - return", None), ("S64 Near cases - return", None), ("S65 Near cases - return", None), ("S70 Near cases - return", None),
]
# A later stage of a split round takes the earlier stage's return when it is in results/.
EXTRA = {"S72-2": ["S72 Stage 1 testing - return"]}
RETURNS += [(x, None) for x in EXTRA.get(NUM, []) if os.path.isdir(R + x)]
def paste(src):
    s = open(src, encoding="utf-8").read(); i = s.find("\n---\n(Below this line")
    return s if i < 0 else s[:i].rstrip("\n") + "\n"
P = os.path.join(OUT, f"{NUM} Instruction pack"); shutil.rmtree(OUT, ignore_errors=True); os.makedirs(P)
def put(src, dst, strip=False):
    d = os.path.join(P, dst); os.makedirs(os.path.dirname(d), exist_ok=True)
    open(d, "w", encoding="utf-8").write(paste(src)) if strip else shutil.copy(src, d)
put(README, "00 READ ME FIRST.md")
put(INSTRUCTION, f"01 Instruction - {NUM}.md", strip=True)
if NUM == "S72-2":
    put(T + "S72 Stage 1 testing - the bare earlier version against every case, and three more, returned as a zip.md", "earlier rounds/S72 Stage 1 instruction - testing.md", strip=True)
put(f"{S}/authority/10 Claude Fable Semantics - standalone theory.md", "authority/10 Claude Fable Semantics - standalone theory.md")
put(T + "24 Workflow - audit the semantics - give this to the other model.md", "skill/24 Workflow - audit the semantics.md")
put(T + "30 Next instruction for the other model - workflow update and re-audit.md", "skill/30 Workflow update and re-audit.md", strip=True)
for src, dst in EARLIER: put(T + src, "earlier rounds/" + dst, strip=True)
for src, dst in RETURNS:
    if dst: put(R + src, "returns/" + dst)
    else: shutil.copytree(R + src, os.path.join(P, "returns", src))
z = os.path.join(OUT, f"{NUM} Instruction pack.zip")
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for dp, _, fn in os.walk(P):
        for f in sorted(fn): zf.write(os.path.join(dp, f), os.path.relpath(os.path.join(dp, f), OUT))
print(z, sum(len(f) for _, _, f in os.walk(P)), "files")
