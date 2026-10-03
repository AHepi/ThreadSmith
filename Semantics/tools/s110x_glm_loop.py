#!/usr/bin/env python3
"""s110x_glm_loop.py: the GLM cross-examination of log S110 (decisions S57, S58; decision S56, "Use GLM for cross
examination"): four GLM jobs at once (S39), each in its own sandbox. Written 29 September 2026 by the one Opus 5.5 agent
of log S110: Part A round 2's cross-examination runner (tools/s108r2x_glm_loop.py) with its names changed and nothing
else: the same sandboxed helper and shell guard (unchanged), the same checks before sending, the same rounds of passes.
Each job names its own sandbox manifest and md5; the sandboxes hold no program, so the guard refuses every command and
GLM only reads.

  python3 Semantics/tools/s110x_glm_loop.py "Semantics/tools/s110x_jobs - S110, GLM cross-examination.json" [--dry-run]

For each job of the list (built by tools/s110x_build.py) whose reply has not been accepted, one call through
tools/glm_via_claude_code_sandboxed.py (glm-5.3 through Claude Code, effort medium, the 1,000,000-token window, tools
Read, Glob, Grep and one command, inside a fresh sandbox holding the manifest's files and the brief), up to max_pass
passes (3). The jobs of a round go at once, one thread each; each call takes a "glm" provider slot per attempt
(s80_common.provider_slot, four slots from decision S39), so four calls are in flight together. Pass 1 of a job goes
under its tag (s110x_glm_a to s110x_glm_d), pass k > 1 under <tag>_pass<k>. A job's pass k+1 goes only after pass k of
every job has ended, in rounds: in round r, every job not yet accepted whose next pass is at most r goes as that pass. A
job is accepted when <tag>.response.txt or <tag>_pass<k>.response.txt is in the returns folder (the caller writes it
last, after the receipt, only for a reply whose last non-blank line carries END OF REPORT). Within a call: 6 attempts,
at most 3 answers without the sentinel; connection failures, timeouts, 429 and 5xx are tried again and are not answers
(the caller's rules). A rerun after an interruption continues from the passes whose files are already there.

Before anything is sent (lesson S12): the reading rule the job list names is tracked by git and unchanged from HEAD
(the caller checks it again at every call, --rule); the tools this round runs are tracked and unchanged from HEAD; every
brief and the manifest have the md5s the job list gives (checked again at every call); there are no more jobs than GLM
slots; GLM_API_KEY is in the environment. This script never reads, prints or writes the key. Progress lines go to
standard output; they hold no reply text. With --dry-run nothing is sent and no key is needed.
"""
import datetime, json, os, subprocess, sys, threading

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
REPO = os.path.dirname(SEM)
CALLER = os.path.join(HERE, "glm_via_claude_code_sandboxed.py")
TOOLS = ["glm_via_claude_code_sandboxed.py", "glm_sandbox_shell_guard.py", "glm_via_claude_code.py", "s80_common.py",
         "s96_glm_call.py", "s110x_glm_loop.py", "s110x_build.py"]
sys.path.insert(0, HERE)
import s80_common as C  # noqa: E402

SAY = threading.Lock()


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def say(*parts):
    with SAY:
        print(now(), *parts, flush=True)


def need(ok, msg):
    if not ok:
        say("refused:", msg)
        raise SystemExit(1)


def committed(rel):
    git = ["git", "-C", REPO]
    tracked = subprocess.run(git + ["ls-files", "--error-unmatch", "--", rel], capture_output=True,
                             stdin=subprocess.DEVNULL).returncode == 0
    same = subprocess.run(git + ["diff", "--quiet", "HEAD", "--", rel], capture_output=True,
                          stdin=subprocess.DEVNULL).returncode == 0
    return tracked and same


def tag_for(job, k):
    return job["tag"] if k == 1 else "%s_pass%d" % (job["tag"], k)


def accepted(job, out, max_pass):
    return [k for k in range(1, max_pass + 1) if os.path.exists(os.path.join(out, tag_for(job, k) + ".response.txt"))]


def next_pass(job, out, max_pass):
    """One above the highest pass that left any file of its tag in the returns folder."""
    names = os.listdir(out) if os.path.isdir(out) else []
    used = [k for k in range(1, max_pass + 1) if any(n.startswith(tag_for(job, k) + ".") for n in names)]
    return max(used or [0]) + 1


def main():
    a = sys.argv[1:]
    need(a and os.path.isfile(a[0]) and set(a[1:]) <= {"--dry-run"}, "usage: s110x_glm_loop.py JOBS.json [--dry-run]")
    dry = "--dry-run" in a[1:]
    data = json.loads(C.read(a[0]))
    rule = os.path.join(SEM, data["rule"])
    rule_rel = os.path.relpath(rule, REPO)
    out = os.path.join(SEM, data["out"])
    max_pass, effort, jobs = data["max_pass"], data["effort"], data["jobs"]
    need(effort == "medium", "effort %r; the owner's rule for outside readers is medium (decision S17)" % effort)
    need(isinstance(max_pass, int) and 1 <= max_pass <= 3, "max_pass %r" % max_pass)
    need(C._inside(out, SEM), "the returns folder %s lies outside Semantics/" % out)
    need(len({j["tag"] for j in jobs}) == len(jobs), "two jobs share a tag")
    need(len(jobs) <= C.slots_for("glm"), "%d jobs but %d GLM slots; they would not all go at once"
         % (len(jobs), C.slots_for("glm")))
    for j in jobs:
        manifest = os.path.join(SEM, j["manifest"])
        need(C._inside(manifest, SEM) and os.path.isfile(manifest), "%s: manifest %s" % (j["tag"], manifest))
        need(C.md5_file(manifest) == j["manifest_md5"], "%s: the manifest's md5 is %s, the job list gives %s; nothing sent"
             % (j["tag"], C.md5_file(manifest), j["manifest_md5"]))
        brief = os.path.join(SEM, j["brief"])
        need(C._inside(brief, SEM) and os.path.isfile(brief), "%s: brief %s" % (j["tag"], brief))
        need(C.md5_file(brief) == j["brief_md5"], "%s: the brief's md5 is %s, the job list gives %s; nothing sent"
             % (j["tag"], C.md5_file(brief), j["brief_md5"]))
    unchecked = [rule_rel] + [os.path.relpath(os.path.join(HERE, t), REPO) for t in TOOLS] + \
        [os.path.relpath(os.path.abspath(a[0]), REPO)]
    bad = [r for r in unchecked if not committed(r)]
    if dry and bad:
        say("note: not committed, or differing from HEAD (a real run refuses): %s" % ", ".join(bad))
    else:
        need(not bad, "not committed, or differing from HEAD: %s; nothing sent" % ", ".join(bad))
    need(dry or os.environ.get("GLM_API_KEY"), "GLM_API_KEY is not set in the environment; nothing sent")
    sroot = os.path.join(C.RUN_DIR, data["sandbox_root"])
    hroot = os.path.join(C.RUN_DIR, data["home_root"])
    say("s110x_glm_loop: %d jobs at once, up to %d passes, effort %s%s, rule %s, returns %s, sandboxes %s, GLM slots %d%s"
        % (len(jobs), max_pass, effort, ", 1M context" if data.get("context_1m") else "", rule_rel,
           os.path.relpath(out, REPO), sroot, C.slots_for("glm"), " [dry run: nothing sent; round 1 only]" if dry else ""))
    if not dry:
        os.makedirs(out, exist_ok=True)

    def one(j, k, tag, results):
        argv = [sys.executable, CALLER, "--brief", os.path.join(SEM, j["brief"]), "--manifest", os.path.join(SEM, j["manifest"]),
                "--manifest-md5", j["manifest_md5"], "--tag", tag, "--out", out, "--effort", effort,
                "--rule", rule, "--brief-md5", j["brief_md5"], "--attempts", str(data["attempts"]),
                "--max-rejects", str(data["max_rejects"]), "--deadline", str(data["deadline"]),
                "--sandbox-root", sroot, "--home-root", hroot] + (["--context-1m"] if data.get("context_1m") else [])
        rc = subprocess.run(argv, cwd=REPO, stdin=subprocess.DEVNULL).returncode
        results[tag] = rc
        say("%s: pass %d ended, exit %d" % (j["tag"], k, rc))

    for r in range(1, (1 if dry else max_pass) + 1):
        say("round %d" % r)
        todo = []
        for j in jobs:
            got = accepted(j, out, max_pass)
            if got:
                say("%s: accepted on pass %d; skipped" % (j["tag"], got[0]))
                continue
            k = next_pass(j, out, max_pass)
            if k > max_pass:
                say("%s: no pass left (%d used)" % (j["tag"], max_pass))
                continue
            if k > r:
                continue
            todo.append((j, k, tag_for(j, k)))
        results, threads = {}, []
        for j, k, tag in todo:
            say("%s: job %d (%s), pass %d of at most %d, as tag %s%s"
                % (j["tag"], j["job"], j["name"], k, max_pass, tag, " [dry run: not sent]" if dry else ""))
            if not dry:
                t = threading.Thread(target=one, args=(j, k, tag, results), daemon=False)
                t.start()
                threads.append(t)
        for t in threads:
            t.join()
    left = [j["tag"] for j in jobs if not accepted(j, out, max_pass)]
    say("s110x_glm_loop: every pass ended; accepted %d of %d jobs%s" % (
        len(jobs) - len(left), len(jobs), ("; not accepted: " + ", ".join(left)) if left else ""))


if __name__ == "__main__":
    main()
