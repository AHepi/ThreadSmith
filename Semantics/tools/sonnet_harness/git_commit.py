#!/usr/bin/env python3
"""Commit exactly the files named, and push, the way the project's agents must (other agents commit at the same time).

  python3 -B git_commit.py --message-file MSG.txt --path "Semantics/..." [--path ...] [--push] [--branch B]
         [--dry-run]

Steps, each stopping everything after it on failure:
  1. every path is inside Semantics/ and none is in authority/ or records/ unless --allow-records is given;
  2. the message file ends with the two attribution lines the orchestrator gives (Co-Authored-By, Claude-Session);
  3. the key grep (key_grep.py) over the named paths and over Semantics/: any matching file stops the commit;
  4. wait while .git/index.lock exists (10 s a time, at most 30 times);
  5. git add -- <paths>; git commit -F MSG -- <paths>  (only these paths go into the commit, whatever else is staged);
  6. every file in the commit is a named path or inside a named folder;
  7. with --push: git push -u origin B; if refused, git pull --no-rebase, then push again (once). A pull that stops
     on a conflict is NOT resolved here: the script reports it and stops (the orchestrator decides).
Prints the commit hash. --dry-run does 1 to 4 only.
"""
import argparse
import os
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402
import key_grep  # noqa: E402

TRAILER = ("Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>", "Claude-Session: ")


def git(args, timeout=300):
    return H.run(["git"] + args, cwd=H.REPO, timeout=timeout, clean_env=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--message-file", required=True)
    ap.add_argument("--path", action="append", required=True)
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--branch", default="claude/semantics-folder-work-9rtd5s")
    ap.add_argument("--allow-records", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    steps = []
    paths = []
    for p in a.path:
        full = p if os.path.isabs(p) else os.path.join(H.REPO, p)
        if not H.inside(full, H.SEM):
            H.refuse("path outside Semantics/: %s" % p)
        r = os.path.relpath(H.real(full), H.real(H.SEM)).split(os.sep)[0]
        if r in ("authority", ".git") or (r == "records" and not a.allow_records):
            H.refuse("path in Semantics/%s/ needs the orchestrator: %s" % (r, p))
        if H.KEYLIKE.search(full):
            H.refuse("a key-like path")
        paths.append(os.path.relpath(H.real(full), H.real(H.REPO)))
    msg = H.read_text(a.message_file)
    if not all(t in msg for t in TRAILER):
        H.refuse("the message lacks the attribution lines (Co-Authored-By, Claude-Session)")
    steps.append("paths and message checked")
    existing = [p for p in paths if os.path.exists(os.path.join(H.REPO, p))]
    g1 = key_grep.grep(existing, H.REPO) if existing else dict(exit=1, files=[], timed_out=False, error="")
    g2 = key_grep.grep(["Semantics/"], H.REPO)
    if g1["files"] or g2["files"] or g1["exit"] not in (0, 1) or g2["exit"] != 1:
        H.emit(dict(ok=False, job="git_commit", stopped_at="key grep", matching_files=sorted(set(g1["files"] + g2["files"])),
                    grep_exit=[g1["exit"], g2["exit"]]))
    steps.append("key grep: no file matches")
    for _ in range(30):
        if not os.path.exists(os.path.join(H.REPO, ".git", "index.lock")):
            break
        time.sleep(10)
    else:
        H.emit(dict(ok=False, job="git_commit", stopped_at="index.lock still there after 300 s", steps=steps))
    steps.append("no index.lock")
    if a.dry_run:
        H.emit(dict(ok=True, job="git_commit", dry_run=True, paths=paths, steps=steps))
    r = git(["add", "--"] + existing)
    if r["exit"] != 0:
        H.emit(dict(ok=False, job="git_commit", stopped_at="git add", stderr=r["stderr"][-500:], steps=steps))
    r = git(["commit", "-F", H.real(a.message_file), "--"] + paths)
    if r["exit"] != 0:
        H.emit(dict(ok=False, job="git_commit", stopped_at="git commit", stdout=r["stdout"][-500:], stderr=r["stderr"][-500:], steps=steps))
    head = git(["rev-parse", "HEAD"])["stdout"].strip()
    files = [l for l in git(["show", "--name-only", "--format=", "HEAD"])["stdout"].split("\n") if l.strip()]
    stray = sorted(f for f in files if not any(f == p or f.startswith(p.rstrip("/") + "/") for p in paths))
    steps.append("committed %s" % head[:7])
    out = dict(job="git_commit", commit=head, files=files, files_not_named=stray, steps=steps)
    if stray:
        H.emit(dict(ok=False, stopped_at="the commit holds files not named", **out))
    if a.push:
        r = git(["push", "-u", "origin", a.branch], timeout=300)
        if r["exit"] != 0:
            steps.append("push refused; git pull --no-rebase")
            p = git(["pull", "--no-rebase", "origin", a.branch], timeout=300)
            if p["exit"] != 0:
                H.emit(dict(ok=False, stopped_at="git pull --no-rebase (not resolved here)", stderr=p["stderr"][-800:], **out))
            r = git(["push", "-u", "origin", a.branch], timeout=300)
        out["pushed"] = r["exit"] == 0
        out["push_stderr_tail"] = r["stderr"][-300:]
        out["head_after_push"] = git(["rev-parse", "HEAD"])["stdout"].strip()
        H.emit(dict(ok=out["pushed"], **out))
    H.emit(dict(ok=True, **out))


if __name__ == "__main__":
    main()
