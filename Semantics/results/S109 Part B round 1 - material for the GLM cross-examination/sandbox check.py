#!/usr/bin/env python3
"""Part B round 1, the GLM cross-examination (log S109): the dry test before launch, Part B round 1's check with one change:
each job has its own manifest (its own program copy at the root), so each job's sandbox is built from its own manifest and
each runs one allowed program run. For each job: build its sandbox with the helper's own build_sandbox and a dummy key;
check the manifest's and the brief's md5s against the job list and BRIEF.md in the sandbox; hand the shell guard lines of
the form Claude Code 2.1.283 builds: one allowed program run and refused commands (a write, `python3 -c`, `cat`, `env`, a
redirect). Writes only in the scratchpad. The real key is never used, opened or read."""
import hashlib, json, os, subprocess, sys, time

sys.dont_write_bytecode = True
SEM = "/home/user/ThreadSmith/Semantics"
SP = "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad"
sys.path.insert(0, SEM + "/tools")
import glm_via_claude_code_sandboxed as H  # noqa: E402

jobs = json.load(open(os.path.join(SEM, sys.argv[1]), encoding="utf-8"))
base = os.path.join(SP, "s109x_build", "sandbox_check_%d" % int(time.time()))
dummy = "dummy-not-a-key-0000"
REFUSE = ["echo probe > probe.txt", "touch probe.txt", "python3 -c 'print(1)'", "python3 -c \"open('p','w')\"",
          "cat BRIEF.md", "env", "python3 -m model.run --claim FC23 > out.txt"]
for j in jobs["jobs"]:
    man_path = os.path.join(SEM, j["manifest"])
    print("job %d manifest md5:" % j["job"], hashlib.md5(open(man_path, "rb").read()).hexdigest(), "job list gives", j["manifest_md5"])
    man = json.load(open(man_path, encoding="utf-8"))
    brief = os.path.join(SEM, j["brief"])
    bm = hashlib.md5(open(brief, "rb").read()).hexdigest()
    root = os.path.join(base, "job%d" % j["job"])
    sandbox, tmp = os.path.join(root, "sandbox"), os.path.join(root, "tmp")
    os.makedirs(tmp)
    snap = H.build_sandbox(man, brief, sandbox, dummy)
    inbox = hashlib.md5(open(os.path.join(sandbox, "BRIEF.md"), "rb").read()).hexdigest()
    keyish = [p for p in snap if "key" in p.lower() or p.endswith(".env")]
    print("job %d (%s): brief md5 %s, job list %s, in sandbox %s; files %d, links %d, key-like paths %s"
          % (j["job"], j["tag"], bm, j["brief_md5"], inbox, len(snap), sum(1 for v in snap.values() if v == "symlink"),
             keyish or "none"))
    guard_log = os.path.join(root, "guard.jsonl")
    env = {"PATH": "/usr/bin:/bin", "GLM_SANDBOX_DIR": sandbox, "GLM_SANDBOX_TMP": tmp, "GLM_SANDBOX_GUARD_LOG": guard_log,
           "ANTHROPIC_AUTH_TOKEN": dummy}

    def line(cmd):
        return ("source %s/snapshot.sh 2>/dev/null || true && eval '%s' < /dev/null && pwd -P >| %s/claude-%s-cwd"
                % (tmp, cmd.replace("'", "'\\''"), tmp, "0a1b2c3d"))

    cmds = ["python3 -m model.run --claim FC23.new2 --claim FC22 --claim FC14"]
    for cmd in cmds + REFUSE:
        r = subprocess.run([H.GUARD, line(cmd)], cwd=sandbox, env=env, capture_output=True, text=True, timeout=900)
        out = r.stdout
        keep = [l for l in out.splitlines() if l.startswith("FC") or "refused" in l]
        print("   ---", cmd, "-> exit", r.returncode, "|", " | ".join(keep)[:400], "| dummy token in output:", dummy in out)
    after = H.snapshot(sandbox)
    print("   sandbox unchanged:", after == snap, "; __pycache__:", any("__pycache__" in k for k in after),
          "; probe files:", [k for k in after if "probe" in k or k in ("p", "out.txt")] or "none")
    print("   guard log:", [json.loads(x)["decision"] for x in open(guard_log)])
