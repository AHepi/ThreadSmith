#!/usr/bin/env python3
"""s87_run.py: send prepared texts to Atria, Mimo or DeepSeek through tools/s80_call.py, from a JSON job list, never
overwriting a file. Written 23 September 2026 for the work of log S87 (the S81 determination), after the process
audit's findings 1, 5, 6 and 12: every call takes a provider slot shared across processes, names its thinking effort
from the one map in s80_common, and keeps each provider's max_tokens ceiling.

  python Semantics/tools/s87_run.py JOBS.json --dry-run   what would be sent, and every file each pass may write;
                                                          sends nothing, writes nothing, needs no keys
  python Semantics/tools/s87_run.py JOBS.json             send (the keys from the environment only)

JOBS.json is {"purpose": "audit", "about": "...", "jobs": [...]} or a bare list of jobs. Each job:
  tag         the stem of the call's files, letters, digits, and . _ - only
  provider    atria, mimo or deepseek
  brief       the text sent as the one user message (a path, relative to the job list's folder or absolute)
  out         the folder the call's files go to (the same)
  effort      the thinking effort sent; it must equal s80_common.effort_for(purpose, provider) unless the job gives
              "effort_differs_because", which is then recorded in the receipt
  ladder      max_tokens per rung; none above s80_common.MAX_TOKENS_CEILING for the provider
  attempts    attempts per pass (s80_call.call); "max_rejects" (answers that come back and fail, default 3)
  max_pass    the highest pass the job may go as: 1 means one pass and never a rerun
  optional:   "system" (a path; none by default), "purpose" (overrides the list's), "note" (kept in the receipt)
Every call has thinking on, temperature s80_common.TEMPERATURE, and is accepted only when it finishes "stop" with
END OF REPORT on its last line (s80_call.accept_reader). Both the brief and the out folder must be inside Semantics/.

Before anything is sent, every job is checked (fields, paths, effort, ladder, the pass it would go as, no tag twice in
one folder), and a real run refuses to start while s80_common.S81_RUN_PIDFILE names a live process (that runner takes
no slot). A tag whose .response.txt exists is skipped; an earlier pass's files are kept under their pass number
(s80_call.pass_plan); a second sender of the same tag is refused (s80_common.tag_lock).
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C
from s80_call import call, pass_plan, PROVIDERS, accept_reader
from s80_run import run_pool

NEED = ("tag", "provider", "brief", "out", "effort", "ladder", "attempts", "max_pass")
MAY = ("max_rejects", "system", "purpose", "note", "effort_differs_because")
TAG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
ROOTS = [C.S]            # every brief and out folder lies under one of these


def _need(ok, msg):
    if not ok:
        raise SystemExit(msg)


def _whole(x, least):
    return isinstance(x, int) and not isinstance(x, bool) and x >= least


def load(path):
    """(list-level purpose, checked jobs, sha256 of the job list). Raises SystemExit on the first fault; sends
    nothing."""
    raw = C.read(path)
    data = json.loads(raw)
    if isinstance(data, dict):
        _need(set(data) <= {"purpose", "jobs", "about"}, "%s: unknown fields %s" % (path, sorted(set(data) - {
            "purpose", "jobs", "about"})))
    purpose, jobs = (data.get("purpose", "audit"), data.get("jobs")) if isinstance(data, dict) else ("audit", data)
    _need(isinstance(jobs, list) and jobs, "%s: no jobs" % path)
    base = os.path.dirname(os.path.abspath(path))
    at = lambda p: os.path.normpath(p if os.path.isabs(p) else os.path.join(base, p))
    out, seen = [], set()
    for i, j in enumerate(jobs, 1):
        _need(isinstance(j, dict), "job %d is not an object" % i)
        _need(not [k for k in NEED if k not in j], "job %d lacks %s" % (i, [k for k in NEED if k not in j]))
        _need(not [k for k in j if k not in NEED + MAY], "job %d has unknown fields %s" % (i, [k for k in j
                                                                                             if k not in NEED + MAY]))
        tag, prov = j["tag"], j["provider"]
        _need(isinstance(tag, str) and TAG.match(tag), "job %d: tag %r" % (i, tag))
        _need(prov in PROVIDERS, "%s: provider %r is not one of %s" % (tag, prov, sorted(PROVIDERS)))
        brief, od = at(j["brief"]), at(j["out"])
        system = at(j["system"]) if j.get("system") else None
        for p in [brief, od] + ([system] if system else []):
            _need(any(C._inside(p, r) for r in ROOTS), "%s: %s lies outside %s" % (tag, p, ROOTS))
        _need(os.path.isfile(brief), "%s: the brief %s is not there" % (tag, brief))
        _need(system is None or os.path.isfile(system), "%s: the system text %s is not there" % (tag, system))
        _need((od, tag) not in seen, "%s appears twice for one folder" % tag)
        seen.add((od, tag))
        pur = j.get("purpose", purpose)
        want = C.effort_for(pur, prov)
        _need(j["effort"] in C.EFFORT_LEVELS, "%s: effort %r is not one of %s" % (tag, j["effort"], C.EFFORT_LEVELS))
        _need(j["effort"] == want or j.get("effort_differs_because"),
              "%s: effort %r, but s80_common.effort_for(%r, %r) is %r; give effort_differs_because to send it"
              % (tag, j["effort"], pur, prov, want))
        try:
            C.check_ladder(prov, j["ladder"])
        except ValueError as e:
            raise SystemExit("%s: %s" % (tag, e))
        _need(_whole(j["attempts"], 1), "%s: attempts must be a whole number of at least 1" % tag)
        _need(_whole(j.get("max_rejects", 3), 1), "%s: max_rejects must be a whole number of at least 1" % tag)
        _need(_whole(j["max_pass"], 1), "%s: max_pass must be a whole number of at least 1" % tag)
        out.append(dict(tag=tag, model=prov, brief=brief, out=od, system=system, user=C.read(brief),
                        system_text=C.read(system) if system else None, effort=j["effort"], purpose=pur,
                        mapped_effort=want, ladder=list(j["ladder"]), attempts=j["attempts"],
                        max_rejects=j.get("max_rejects", 3), max_pass=j["max_pass"], note=j.get("note"),
                        effort_differs_because=j.get("effort_differs_because")))
    return purpose, out, C.sha256(raw)


def plan(jobs):
    """For each job: skip (its response is there) or the pass it would go as; SystemExit if any would go above its
    max_pass, before anything is sent."""
    rows = []
    for j in jobs:
        if os.path.exists(os.path.join(j["out"], j["tag"] + ".response.txt")):
            rows.append((j, None, []))
            continue
        renames, k = pass_plan(j["out"], j["tag"])
        _need(k <= j["max_pass"], "%s would go as pass %d, above its max_pass %d; nothing sent"
              % (j["tag"], k, j["max_pass"]))
        rows.append((j, k, renames))
    return rows


def dry_run(path, jobs, sha):
    pid = C.live_pid(C.S81_RUN_PIDFILE)
    print("job list %s (sha256 %s): %d jobs" % (path, sha[:12], len(jobs)))
    if pid:
        print("NOTE: %s names live pid %d; a real run refuses to start until it ends" % (C.S81_RUN_PIDFILE, pid))
    send = []
    for j, k, renames in plan(jobs):
        t, d = j["tag"], j["out"]
        if k is None:
            print("%s skip: %s.response.txt is there" % (t, t))
            continue
        send.append(j)
        names = set(os.listdir(d)) if os.path.isdir(d) else set()
        freed = {old for old, _ in renames}
        may = [t + e for e in (".request.json", ".response.txt", ".reasoning.txt", ".receipt.json", ".error.txt")]
        may += ["%s.pass%d.a%d.%s.txt" % (t, k, n, w) for n in range(1, j["attempts"] + 1)
                for w in ("truncated", "reasoning")]
        clash = sorted(f for f in may if f in names and f not in freed)
        print("%s SEND to %s (%s): pass %d of at most %d; max_tokens %s; thinking on, reasoning_effort %s (the map's "
              "%r for %s: %s); temperature %s; system %s; text %s, sha256 %s, %d words"
              % (t, j["model"], PROVIDERS[j["model"]][1], k, j["max_pass"], j["ladder"], j["effort"], j["purpose"],
                 j["model"], j["mapped_effort"], C.TEMPERATURE, os.path.relpath(j["system"], C.REPO) if j["system"]
                 else "none", os.path.relpath(j["brief"], C.REPO), C.sha256(j["user"])[:12], len(j["user"].split())))
        print("    into %s; renamed first: %s" % (os.path.relpath(d, C.REPO),
                                                  ", ".join("%s -> %s" % r for r in renames) or "none"))
        print("    may write: %s.pass%d.a<1..%d>.truncated.txt / .reasoning.txt (attempts that come back and fail), "
              "%s.request.json, then on success .reasoning.txt, .receipt.json and last .response.txt, or on failure "
              ".error.txt and .receipt.json; up to %d attempts, at most %d that come back and fail; already there: %s"
              % (t, k, j["attempts"], t, j["attempts"], j["max_rejects"], ", ".join(clash) or "none"))
        _need(not clash, "%s: a file this pass may write is already there: %s" % (t, clash))
    per = {}
    for j in send:
        per[j["model"]] = per.get(j["model"], 0) + 1
    print("to send: %d calls (%s); at most %d in flight per provider across every process (slot locks in %s)"
          % (len(send), ", ".join("%s %d" % kv for kv in sorted(per.items())) or "none", C.SLOTS_PER_PROVIDER,
             C.LOCK_DIR))


def run(path, jobs, sha):
    C.refuse_if_runner_alive()
    rows = plan(jobs)
    for j, k, _ in rows:
        if k is not None and PROVIDERS[j["model"]][2] not in os.environ:
            raise SystemExit("%s: %s is not set in the environment; nothing sent"
                             % (j["tag"], PROVIDERS[j["model"]][2]))
    rel = os.path.relpath(os.path.abspath(path), C.REPO)

    def one(j):
        extra = {"runner": "tools/s87_run.py", "job_list": rel, "job_list_sha256": sha, "purpose": j["purpose"],
                 "effort_from_map": j["mapped_effort"], "max_pass": j["max_pass"]}
        if j["note"]:
            extra["note"] = j["note"]
        if j["effort_differs_because"]:
            extra["effort_differs_because"] = j["effort_differs_because"]
        if not os.path.exists(os.path.join(j["out"], j["tag"] + ".response.txt")):
            C.log("start", j["model"], j["tag"], "effort", j["effort"], "max_tokens", j["ladder"])
        return call(j["model"], j["system_text"], j["user"], j["out"], j["tag"], True, j["ladder"], accept_reader,
                    extra=extra, attempts=j["attempts"], max_rejects=j["max_rejects"], effort=j["effort"])
    run_pool(jobs, one)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or not os.path.isfile(a[0]) or set(a[1:]) - {"--dry-run"}:
        raise SystemExit(__doc__)
    purpose, jobs, sha = load(a[0])
    (dry_run if "--dry-run" in a[1:] else run)(a[0], jobs, sha)
