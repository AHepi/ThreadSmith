#!/usr/bin/env python3
"""s103_glm_loop.py: GLM's side of round 1 of the review rounds of decision S35 (log S103). Written 27 September 2026
by a Claude subagent for the orchestrator.

  python3 Semantics/tools/s103_glm_loop.py "Semantics/tools/s103_jobs - round 1, GLM.json" [--dry-run]

For each part of the GLM job list (built by tools/s103_build.py) whose reply has not been accepted, one call through
tools/glm_via_claude_code.py (glm-5.3 through Claude Code, effort medium, the brief whole as the one prompt), the parts
one after another; up to max_pass passes (3). Pass 1 of a part goes under its tag (s103_vary_glm_<n>), pass k > 1
under <tag>_pass<k>, because the caller never writes into a tag that already has a file. A part's pass k+1 goes only
after pass k of every part has ended, in rounds: in round r, every part not yet accepted whose next pass is at most r
goes as that pass. A part is accepted when <tag>.response.txt or <tag>_pass<k>.response.txt is in the returns folder
(the caller writes it last, after the receipt, only for a reply whose last line carries END OF REPORT). A rerun of this
script after an interruption continues from the passes whose files are already there, and never goes above max_pass.

Before anything is sent (lesson S12): the reading rule the job list names is tracked by git and unchanged from HEAD
(the caller checks it again at every call, --rule), every brief has the md5 the job list gives (--brief-md5 at every
call), and GLM_API_KEY is in the environment. This script never reads, prints or writes the key: the caller takes it
from the environment it inherits from here. Progress lines (the caller's start, attempt, done lines; this script's
round and pass lines) go to standard output; they hold no reply text. With --dry-run nothing is sent and no key is
needed.
"""
import datetime, json, os, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
REPO = os.path.dirname(SEM)
CALLER = os.path.join(HERE, "glm_via_claude_code.py")
sys.path.insert(0, HERE)
import s80_common as C  # noqa: E402


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def say(*parts):
    print(now(), *parts, flush=True)


def need(ok, msg):
    if not ok:
        say("refused:", msg)
        raise SystemExit(1)


def rule_committed(rel):
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
    need(a and os.path.isfile(a[0]) and set(a[1:]) <= {"--dry-run"}, "usage: s103_glm_loop.py JOBS.json [--dry-run]")
    dry = "--dry-run" in a[1:]
    data = json.loads(C.read(a[0]))
    rule = os.path.join(SEM, data["rule"])
    rule_rel = os.path.relpath(rule, REPO)
    out = os.path.join(SEM, data["out"])
    max_pass, effort, jobs = data["max_pass"], data["effort"], data["jobs"]
    need(effort == "medium", "effort %r; the owner's rule for outside readers is medium (decision S17)" % effort)
    need(isinstance(max_pass, int) and 1 <= max_pass <= 3, "max_pass %r" % max_pass)
    need(C._inside(out, SEM), "the returns folder %s lies outside Semantics/" % out)
    if dry and not rule_committed(rule_rel):
        say("note: the reading rule %s is not committed, or differs from HEAD; a real run refuses" % rule_rel)
    else:
        need(rule_committed(rule_rel), "the reading rule %s is not committed, or differs from HEAD; nothing sent"
             % rule_rel)
    for j in jobs:
        brief = os.path.join(SEM, j["brief"])
        need(C._inside(brief, SEM) and os.path.isfile(brief), "%s: brief %s" % (j["tag"], brief))
        need(C.md5_file(brief) == j["brief_md5"], "%s: the brief's md5 is %s, the job list gives %s; nothing sent"
             % (j["tag"], C.md5_file(brief), j["brief_md5"]))
    need(len({j["tag"] for j in jobs}) == len(jobs), "two jobs share a tag")
    need(dry or os.environ.get("GLM_API_KEY"), "GLM_API_KEY is not set in the environment; nothing sent")
    say("s103_glm_loop: %d parts, up to %d passes, effort %s, rule %s, returns %s%s"
        % (len(jobs), max_pass, effort, rule_rel, os.path.relpath(out, REPO),
           " [dry run: nothing sent; round 1 only]" if dry else ""))
    if not dry:
        os.makedirs(out, exist_ok=True)
    for r in range(1, (1 if dry else max_pass) + 1):
        say("round %d" % r)
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
            tag = tag_for(j, k)
            argv = [sys.executable, CALLER, "--brief", os.path.join(SEM, j["brief"]), "--tag", tag, "--out", out,
                    "--effort", effort, "--rule", rule, "--brief-md5", j["brief_md5"]]
            say("%s: part %s, pass %d of at most %d, as tag %s" % (j["tag"], j["part"], k, max_pass, tag))
            if dry:
                continue
            rc = subprocess.run(argv, cwd=REPO, stdin=subprocess.DEVNULL).returncode
            say("%s: pass %d ended, exit %d" % (j["tag"], k, rc))
    left = [j["tag"] for j in jobs if not accepted(j, out, max_pass)]
    say("s103_glm_loop: every pass ended; accepted %d of %d parts%s" % (
        len(jobs) - len(left), len(jobs), ("; not accepted: " + ", ".join(left)) if left else ""))


if __name__ == "__main__":
    main()
