#!/usr/bin/env python3
"""Log S116, the GLM cross-examination: the dry test before launch; log S113's check (the S113 material's
`sandbox check.py`) with its names changed, and .tsv files added to the raw output looked for. Written 30 September 2026 by the one Opus 5.5 agent of log S116. For each job: build its
sandbox with the helper's own build_sandbox and a dummy key; check the manifest's and the brief's md5s against the job list
and BRIEF.md in the sandbox; check that no file in the sandbox is an Avida binary (an ELF file), a saved program population
(.spop), an Avida data file (.dat), a trace (.trace), a raw list (.jsonl) or a probe table (.tsv), larger than 400,000 bytes, or copied from outside Semantics/; hand the shell guard
lines of the form Claude Code builds: a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect, a run of one of the
S116 scripts and the program command of earlier rounds; each must be refused; the sandbox must come back unchanged. Writes
only in the scratchpad. The real key is never used, opened or read.

  python3 -B "Semantics/results/S116 Routine runs from Astra's replies - material for the GLM cross-examination/sandbox check.py" \
      "tools/s116x_jobs - S116, GLM cross-examination.json"
"""
import hashlib, json, os, subprocess, sys, time

sys.dont_write_bytecode = True
SEM = "/home/user/ThreadSmith/Semantics"
SP = "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad"
sys.path.insert(0, SEM + "/tools")
import glm_via_claude_code_sandboxed as H  # noqa: E402

jobs = json.load(open(os.path.join(SEM, sys.argv[1]), encoding="utf-8"))
base = os.path.join(SP, "s116x_build", "sandbox_check_%d" % int(time.time()))
dummy = "dummy-not-a-key-0000"
CMDS = ["echo probe > probe.txt", "touch probe.txt", "python3 -c 'print(1)'", "python3 -c \"open('p','w')\"",
        "cat BRIEF.md", "env", "python3 scripts/s116_gather_the_results.py > out.txt",
        "python3 scripts/s116_gather_the_results.py", "python3 -m model.run --claim FC23"]
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
    srcs = [e["src"] for e in man["files"]]
    outside = [s for s in srcs if "scratchpad" in s or s.startswith("/") or ".." in s]
    raw = []
    for rel in snap:
        p = os.path.join(sandbox, rel)
        with open(p, "rb") as f:
            head = f.read(4)
        if head == b"\x7fELF" or rel.endswith((".spop", ".dat", ".trace", ".jsonl", ".tsv")) or os.path.getsize(p) > 400000:
            raw.append(rel)
    print("job %d (%s): brief md5 %s, job list %s, in sandbox %s; files %d, links %d, key-like paths %s; sources from "
          "outside Semantics/ %s; binaries, raw output or large files %s; a model/ folder %s"
          % (j["job"], j["tag"], bm, j["brief_md5"], inbox, len(snap), sum(1 for v in snap.values() if v == "symlink"),
             keyish or "none", outside or "none", raw or "none", os.path.isdir(os.path.join(sandbox, "model"))))
    guard_log = os.path.join(root, "guard.jsonl")
    env = {"PATH": "/usr/bin:/bin", "GLM_SANDBOX_DIR": sandbox, "GLM_SANDBOX_TMP": tmp, "GLM_SANDBOX_GUARD_LOG": guard_log,
           "ANTHROPIC_AUTH_TOKEN": dummy}

    def line(cmd):
        return ("source %s/snapshot.sh 2>/dev/null || true && eval '%s' < /dev/null && pwd -P >| %s/claude-%s-cwd"
                % (tmp, cmd.replace("'", "'\\''"), tmp, "0a1b2c3d"))

    for cmd in CMDS:
        r = subprocess.run([H.GUARD, line(cmd)], cwd=sandbox, env=env, capture_output=True, text=True, timeout=120)
        out = r.stdout
        keep = [l for l in out.splitlines() if "refused" in l]
        print("   ---", cmd, "-> exit", r.returncode, "|", (" | ".join(keep) or out.strip())[:120],
              "| dummy token in output:", dummy in out)
    after = H.snapshot(sandbox)
    print("   sandbox unchanged:", after == snap, "; __pycache__:", any("__pycache__" in k for k in after),
          "; probe files:", [k for k in after if "probe" in k or k in ("p", "out.txt")] or "none")
    print("   guard log:", [json.loads(x)["decision"] for x in open(guard_log)])
