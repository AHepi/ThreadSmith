#!/usr/bin/env python3
"""End-to-end stand-in test of tools/glm_via_claude_code_sandboxed.py: the decoy steps of permtest.py (both sets),
played by the scripted stand-in, through the helper itself. Dummy token; nothing leaves the machine."""
import hashlib, json, os, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import permtest as P

SEM = "/home/user/ThreadSmith/Semantics"
SP = P.SP
T = os.path.join(SP, "s105_helpertest", "run_%d" % int(time.time()))
os.makedirs(T)
MODEL = "results/S104 Round 2 - maths after the reading/model after round 2/model"
files = []
for n in sorted(os.listdir(os.path.join(SEM, MODEL))):
    if n.endswith(".py"):
        src = os.path.join(MODEL, n)
        files.append({"src": src, "path": "model/" + n, "md5": hashlib.md5(open(os.path.join(SEM, src), "rb").read()).hexdigest()})
files.append({"src": "tools/glm_sandbox_shell_guard.py", "path": "probe.txt", "md5": hashlib.md5(open(os.path.join(SEM, "tools/glm_sandbox_shell_guard.py"), "rb").read()).hexdigest()})
man = os.path.join(T, "manifest.json")
json.dump({"files": files}, open(man, "w"))
brief = os.path.join(T, "brief.md")
open(brief, "w").write("Stand-in test brief. Run the scripted steps.\n")
sroot, hroot, out = os.path.join(T, "sandboxes"), os.path.join(T, "homes"), os.path.join(T, "out")
tag = "helpertest"
sb = os.path.join(sroot, tag + ".a1")
st = P.steps(sb) + P.steps2(sb)[1:]
# probe.txt holds the guard's source here: replace the PROBE-OK grep and edit targets accordingly
script = [{"name": n, "input": i} for _, n, i in st]
sp = os.path.join(T, "script.json")
json.dump(script, open(sp, "w"))
log = os.path.join(T, "server.jsonl")
port = int(sys.argv[1]) if len(sys.argv) > 1 else 18580
srv = subprocess.Popen([sys.executable, os.path.join(P.B, "standin_tools.py"), str(port), log, sp])
time.sleep(1)
env = dict(os.environ)
for k in list(env):
    if k.endswith("_API_KEY"):
        env.pop(k)
env["GLM_API_KEY"] = "standin-dummy-token-7f3a9c"
env["SEMANTICS_RUN_DIR"] = T
try:
    r = subprocess.run([sys.executable, os.path.join(SEM, "tools/glm_via_claude_code_sandboxed.py"), "--brief", brief,
                        "--manifest", man, "--tag", tag, "--out", out, "--attempts", "1", "--max-rejects", "1",
                        "--deadline", "900", "--sandbox-root", sroot, "--home-root", hroot,
                        "--base-url", "http://127.0.0.1:%d" % port], env=env, capture_output=True, text=True, timeout=1200)
finally:
    srv.kill(); srv.wait()
print("helper exit", r.returncode)
print(r.stdout[-1500:])
print(r.stderr[-1500:])
rec = json.load(open(os.path.join(out, tag + ".receipt.json")))
h = rec["attempt_history"][0]
decoy = open(P.DECOY).read().strip()
print("accepted", rec["accepted"], "| sandbox unchanged", h["sandbox_unchanged"], h["sandbox_changes"], "| init problems", h["init_problems"])
print("guard run/refused", h["guard_commands_run"], h["guard_commands_refused"], "| calls", h["tool_calls_by_name"], "| refused or error", h["tool_calls_refused_or_error"])
allowed = []
for (label, n, _), c in zip(st, h["tool_calls"]):
    status = "refused" if c["refused_or_error"] else "ALLOWED"
    if not c["refused_or_error"]:
        allowed.append(label)
    print("%-55s %-8s %s" % (label[:55], status, (c["result_head"] or "")[:70].replace("\n", " ")))
alltext = "".join(open(os.path.join(out, f), encoding="utf-8", errors="replace").read() for f in os.listdir(out))
print("decoy string in any output file:", decoy in alltext, "| dummy token in any output file:", "standin-dummy-token-7f3a9c" in alltext)
print("ALLOWED:", allowed)
print("files in the decoy folder:", sorted(os.listdir(P.DECOY_DIR)))
print("folder:", T)
