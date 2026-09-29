#!/usr/bin/env python3
"""Log S110, the GLM cross-examination: the dry test before launch, on Part B round 1's check (the S109 material's
`sandbox check.py`) with one change: the S110 sandboxes hold no program, so every command handed to the guard must be
refused, the program run included. For each job: build its sandbox with the helper's own build_sandbox and a dummy key;
check the manifest's and the brief's md5s against the job list and BRIEF.md in the sandbox; check that no file in the
sandbox comes from the scratchpad's book extraction (by name, and by searching every sandbox file for three long
stretches of the book's text that are quoted nowhere in the S110 files); hand the shell guard lines of the form Claude
Code 2.1.283 builds: a write, `python3 -c`, `cat`, `env`, a redirect and the one program command; each must be refused;
the sandbox must come back unchanged. Writes only in the scratchpad. The real key is never used, opened or read.

  python3 -B "Semantics/results/S110 - material for the GLM cross-examination/sandbox check.py" \
      "tools/s110x_jobs - S110, GLM cross-examination.json" BOOKDIR
"""
import hashlib, json, os, re, subprocess, sys, time

sys.dont_write_bytecode = True
SEM = "/home/user/ThreadSmith/Semantics"
SP = "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad"
sys.path.insert(0, SEM + "/tools")
import glm_via_claude_code_sandboxed as H  # noqa: E402

jobs = json.load(open(os.path.join(SEM, sys.argv[1]), encoding="utf-8"))
bookdir = sys.argv[2]
# three probes of the book's text, taken at fixed offsets of chapters 3 and 5 and of Deutsch's chapter 6, each 12 words;
# they are read from the scratchpad at run time and printed only as their md5s
probes = []
for name, off in (("full/13_3_Information.txt", 20000), ("full/17_5_Knowledge.txt", 15000), ("deutsch.txt", 400000)):
    txt = re.sub(r"\s+", " ", open(os.path.join(bookdir, name), encoding="utf-8").read())
    w = txt[off:off + 400].split(" ")[1:13]
    probes.append(" ".join(w))
base = os.path.join(SP, "s110x_build", "sandbox_check_%d" % int(time.time()))
dummy = "dummy-not-a-key-0000"
CMDS = ["echo probe > probe.txt", "touch probe.txt", "python3 -c 'print(1)'", "python3 -c \"open('p','w')\"",
        "cat BRIEF.md", "env", "python3 -m model.run --claim FC23 > out.txt", "python3 -m model.run --claim FC23"]
print("book probes (md5 only):", [hashlib.md5(p.encode()).hexdigest()[:8] for p in probes])
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
    from_scratch = [s for s in srcs if "s110_book" in s or "scratchpad" in s or s.startswith("/")]
    hits = []
    for rel in snap:
        data = re.sub(r"\s+", " ", open(os.path.join(sandbox, rel), encoding="utf-8", errors="replace").read())
        hits += [(rel, i) for i, p in enumerate(probes) if p in data]
    print("job %d (%s): brief md5 %s, job list %s, in sandbox %s; files %d, links %d, key-like paths %s; sources from the "
          "scratchpad %s; book probes found %s"
          % (j["job"], j["tag"], bm, j["brief_md5"], inbox, len(snap), sum(1 for v in snap.values() if v == "symlink"),
             keyish or "none", from_scratch or "none", hits or "none"))
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
        print("   ---", cmd, "-> exit", r.returncode, "|", (" | ".join(keep) or out.strip())[:160],
              "| dummy token in output:", dummy in out)
    after = H.snapshot(sandbox)
    print("   sandbox unchanged:", after == snap, "; __pycache__:", any("__pycache__" in k for k in after),
          "; probe files:", [k for k in after if "probe" in k or k in ("p", "out.txt")] or "none")
    print("   guard log:", [json.loads(x)["decision"] for x in open(guard_log)])
