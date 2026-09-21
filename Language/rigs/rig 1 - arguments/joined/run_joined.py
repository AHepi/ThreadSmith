# run_joined.py
# What this file does: runs rig 1's driver with rig 2's laws and the bridge added, so one ledger can hold arguments and pressing patterns together.
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "patched"))
import run_check as rig_one
laws = open("/home/claude/rig2/patched/laws.pl").read()
laws = re.sub(r"#pred line\(N\)[^\n]*\n", "", laws)          # rig 1 already gives the wording for line(N)
bridge = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bridge.pl")).read()
rig_one.RULES = rig_one.RULES + "\n" + laws + "\n" + bridge
with open(sys.argv[2], "a") as log: print(rig_one.check(sys.argv[1], log))
