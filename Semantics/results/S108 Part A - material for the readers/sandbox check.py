#!/usr/bin/env python3
"""Part A build (log S108): build one sandbox from Part A's manifest with the helper's own code and a dummy key,
then hand the guard two shell lines of the form Claude Code 2.1.283 builds: one allowed program run and one refused
command. Writes only in the scratchpad. The real key is never used."""
import json, os, subprocess, sys, time

sys.dont_write_bytecode = True
SEM = "/home/user/ThreadSmith/Semantics"
SP = "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad"
sys.path.insert(0, SEM + "/tools")
import glm_via_claude_code_sandboxed as H  # noqa: E402

manifest_rel, brief_rel = sys.argv[1], sys.argv[2]
man = json.load(open(os.path.join(SEM, manifest_rel), encoding="utf-8"))
root = os.path.join(SP, "s108_build", "sandbox_check_%d" % int(time.time()))
os.makedirs(root)
sandbox, tmp = os.path.join(root, "sandbox"), os.path.join(root, "tmp")
os.makedirs(tmp)
dummy = "dummy-not-a-key-0000"
snap = H.build_sandbox(man, os.path.join(SEM, brief_rel), sandbox, dummy)
print("sandbox files:", len(snap), "links:", sum(1 for v in snap.values() if v == "symlink"))
guard_log = os.path.join(root, "guard.jsonl")
env = {"PATH": "/usr/bin:/bin", "GLM_SANDBOX_DIR": sandbox, "GLM_SANDBOX_TMP": tmp, "GLM_SANDBOX_GUARD_LOG": guard_log,
       "ANTHROPIC_AUTH_TOKEN": dummy}


def line(cmd):
    return ("source %s/snapshot.sh 2>/dev/null || true && eval '%s' < /dev/null && pwd -P >| %s/claude-%s-cwd"
            % (tmp, cmd, tmp, "0a1b2c3d"))


for cmd in ["python3 -m model.run --claim FC23 --claim FC30.new1 --claim FC14", "cat BRIEF.md", "env"]:
    r = subprocess.run([H.GUARD, line(cmd)], cwd=sandbox, env=env, capture_output=True, text=True, timeout=600)
    out = r.stdout
    print("---", cmd, "-> exit", r.returncode)
    print("   ", " | ".join(l for l in out.splitlines() if l.startswith("FC") or "refused" in l or "formal core" in l)[:900])
    print("    dummy token in output:", dummy in out, "; stderr:", r.stderr.strip()[:200])
after = H.snapshot(sandbox)
print("sandbox unchanged:", after == snap, "; __pycache__:", any("__pycache__" in k for k in after))
print("guard log:", [json.loads(x)["decision"] for x in open(guard_log)])
