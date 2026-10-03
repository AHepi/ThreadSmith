#!/usr/bin/env python3
"""s80_run.py: round S80, does the hard-to-vary skill add anything (plan S80, second version). Run from anywhere, in the
venv, with the keys exported (never written to a file):
  python Semantics/tools/s80_run.py list                        # the job order per model; sends nothing
  python Semantics/tools/s80_run.py manifest                    # write or check the run MANIFEST; sends nothing
  python Semantics/tools/s80_run.py readers [--only TAG ...]    # the 180 API reader runs
  python Semantics/tools/s80_run.py mark KEY_FILE [--accept-missing] [--dry-run]
        # after every reader (API and Opus) has reported: the anonymous map, the API marker calls, and the input files
        # for the Opus-marked reports (marks/opus_inputs/<rid>.md)

Readers: atria, mimo, deepseek; conditions ST PT NT (skill, placebo, nothing; thinking on) and SO PO NO (thinking off);
documents seeded and clean; five repetitions; job order shuffled per model with a fixed seed; at most 3 calls in flight
per provider (decision S12). The Opus arm (S, P, N; three repetitions) is run by the orchestrator as subagents, prepared
by s80_opus_prep.py and collected by s80_opus_collect.py into the same readers folder.
The limit of 3 per provider holds across processes too (s80_common.provider_slot). Thinking effort and max_tokens per
provider come from s80_common: effort_for("s80", provider) ("high", S80's design) and ladder_for(provider,
READER_LADDER or MARKER_LADDER) (the probed ceiling on every rung: Atria 65,536, Mimo 131,072; DeepSeek the ladder).
Markers: no self-marking. atria's reports: mimo + an Opus subagent; mimo's: atria + an Opus subagent; deepseek's and
opus's: atria + mimo. Thinking on. The map from anonymous id to tag is marks/MAP.json and is in no marker's input.

Guards: the two documents' md5s are asserted at start; the MANIFEST (document md5s, method texts' SHA-256, system and
task texts' SHA-256, temperature, ladders, seeds, job order) is written on the first run and every later run must match
it; readers refuse to run once anything exists in marks/; marking refuses to start unless every expected report is
present and complete (or, with --accept-missing, has a failed receipt from at least two passes).
"""
import difflib, json, os, random, shutil, sys, time, traceback
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C
from s80_call import call, PROVIDERS, accept_reader

READERS_DIR = os.path.join(C.OUT, "readers")
MARKS_DIR = os.path.join(C.OUT, "marks")
MANIFEST = os.path.join(C.OUT, "MANIFEST.json")


# ---------------------------------------------------------------- texts

def system_text(method):
    if method == "N":
        return C.read(os.path.join(C.PR, "reader system - without skill.md"))
    return C.read(os.path.join(C.PR, "reader system - with method.md")).rstrip("\n") + C.method_text(method)


def reader_user_text(doc):
    return C.read(os.path.join(C.PR, "reader task.md")) + C.read(C.DOCS[doc])


def check_methods():
    sk, pl = C.method_text("S"), C.method_text("P")
    ratio = C.words(pl) / C.words(sk)
    lo, hi = C.PLACEBO_WORD_RATIO
    if not lo <= ratio <= hi:
        raise SystemExit("placebo is %d words against the skill's %d (ratio %.2f, outside %s); stop"
                         % (C.words(pl), C.words(sk), ratio, C.PLACEBO_WORD_RATIO))
    return sk, pl


# ---------------------------------------------------------------- jobs

def reader_jobs():
    jobs = []
    for i, m in enumerate(C.MODELS):
        js = []
        for c, (method, think) in C.CONDS.items():
            for d in C.DOCNAMES:
                for r in range(1, C.REPS + 1):
                    js.append(dict(tag=f"{m}_{c}_{d}_r{r}", model=m, method=method, thinking=think, doc=d,
                                   out=READERS_DIR))
        random.Random(C.JOB_SEED + i).shuffle(js)
        jobs += js
    return jobs


def run_pool(jobs, fn):
    by_model = {}
    for j in jobs:
        by_model.setdefault(j["model"], []).append(j)

    def worker(j):
        try:
            res = fn(j)
        except Exception:
            res = "worker-exception"
            p = os.path.join(j["out"], j["tag"] + ".error.txt")
            if os.path.exists(p):      # never over an earlier pass's error file: this one goes beside it
                p = os.path.join(j["out"], "%s.worker-exception.%d.txt" % (j["tag"], int(time.time())))
            C.write(p, "worker exception\n" + traceback.format_exc())
        C.log(j["model"], j["tag"], res)   # under the one log lock, shared with every other progress line
        return res

    pools = {m: ThreadPoolExecutor(max_workers=3) for m in by_model}
    futs = [pools[m].submit(worker, j) for m, js in by_model.items() for j in js]
    results = [f.result() for f in futs]
    for p in pools.values():
        p.shutdown()
    print("done:", {r: results.count(r) for r in set(results)})


# ---------------------------------------------------------------- manifest

def manifest_now():
    C.check_documents()
    sk, pl = check_methods()
    systems = {m: system_text(m) for m in "SPN"}
    import platform, requests
    return {
        "round": "S80, second version of the plan",
        "documents_md5": {d: C.md5_file(p) for d, p in C.DOCS.items()},
        "seeded_vs_clean_diff_sha256": C.sha256("".join(difflib.unified_diff(
            C.read(C.DOCS["clean"]).splitlines(True), C.read(C.DOCS["seeded"]).splitlines(True)))),
        "skill": {"files": C.method_files("S"), "words_as_sent": C.words(sk), "sha256": C.sha256(sk)},
        "placebo": {"files": C.method_files("P"), "words_as_sent": C.words(pl), "sha256": C.sha256(pl)},
        "system_sha256": {m: C.sha256(t) for m, t in systems.items()},
        "framing_identical_for_skill_and_placebo":
            systems["S"][:len(systems["S"]) - len(sk)] == systems["P"][:len(systems["P"]) - len(pl)],
        "reader_user_sha256": {d: C.sha256(reader_user_text(d)) for d in C.DOCNAMES},
        "reader_task_sha256": C.sha256(C.read(os.path.join(C.PR, "reader task.md"))),
        "models": {m: PROVIDERS[m][1] for m in C.MODELS},
        "temperature": C.TEMPERATURE, "top_p": "provider default (unset)",
        "reasoning_effort_when_thinking": {m: C.effort_for("s80", m) for m in C.MODELS},
        "reader_max_tokens_ladder": {m: C.ladder_for(m, C.READER_LADDER) for m in C.MODELS},
        "marker_max_tokens_ladder": {m: C.ladder_for(m, C.MARKER_LADDER) for m in C.API_MARKERS},
        "reps": C.REPS, "opus_reps": C.OPUS_REPS, "job_seed": C.JOB_SEED, "map_seed": C.MAP_SEED,
        "boot_seed": C.BOOT_SEED, "drift_salt": C.DRIFT_SALT, "drift_share": C.DRIFT_SHARE,
        "job_order": [j["tag"] for j in reader_jobs()],
        "python": platform.python_version(), "requests": requests.__version__,
    }


def manifest_check(write=True):
    now = manifest_now()
    if not now["framing_identical_for_skill_and_placebo"]:
        raise SystemExit("the system prompt framing differs between skill and placebo; stop")
    if os.path.exists(MANIFEST):
        old = json.loads(C.read(MANIFEST))
        diff = [k for k in now if k not in ("python", "requests") and old.get(k) != now[k]]
        if diff:
            raise SystemExit("MANIFEST differs from the material now in these fields: %s; stop" % diff)
        return old
    if write:
        now["written_at_unix"] = int(time.time())
        C.write_atomic(MANIFEST, json.dumps(now, indent=1, ensure_ascii=False))
    return now


def marks_exist():
    return os.path.isdir(MARKS_DIR) and any(os.scandir(MARKS_DIR))


# ---------------------------------------------------------------- readers

def readers(only):
    if marks_exist():
        raise SystemExit("marks/ is not empty: the answer key may be in the repository; readers refuse to run")
    manifest_check()
    systems = {m: system_text(m) for m in "SPN"}
    users = {d: reader_user_text(d) for d in C.DOCNAMES}
    jobs = [j for j in reader_jobs() if not only or j["tag"] in only]
    if only and len(jobs) != len(set(only)):
        raise SystemExit("unknown tags in --only: %s" % sorted(set(only) - {j["tag"] for j in jobs}))
    run_pool(jobs, lambda j: call(j["model"], systems[j["method"]], users[j["doc"]], READERS_DIR, j["tag"],
                                  j["thinking"], C.ladder_for(j["model"], C.READER_LADDER), accept_reader,
                                  extra={"doc": j["doc"]}, effort=C.effort_for("s80", j["model"])))


# ---------------------------------------------------------------- marking

def marker_user_text(task, key, doc, rid, report):
    b, e = C.FENCE_BEGIN.format(rid=rid), C.FENCE_END.format(rid=rid)
    if b in report or e in report:
        raise SystemExit("report %s contains the fence line" % rid)
    return (task + "\n\n(A) THE ANSWER KEY\n==================\n\n" + (key["seeded"] if doc == "seeded" else key["clean"])
            + "\n\n(B) THE DOCUMENT THE REVIEWER READ\n==================================\n\n" + C.read(C.DOCS[doc])
            + "\n\n(C) THE REPORT, id " + rid + "\n=====================\n\n" + b + "\n" + report.rstrip("\n")
            + "\n" + e + "\n")


def build_map(tags_sha):
    """tags_sha: {tag: response sha256}. Keeps existing ids; a report whose bytes changed keeps its id, its marks are
    moved to marks/stale/<time>/ and must be made again."""
    mp = C.load_map()
    by_tag = {v["tag"]: k for k, v in mp.items()}
    rng = random.Random(C.MAP_SEED)
    stale = []
    for t in sorted(tags_sha):
        if t in by_tag:
            rid = by_tag[t]
            if mp[rid]["response_sha256"] != tags_sha[t]:
                stale.append(rid)
                mp[rid]["response_sha256"] = tags_sha[t]
            continue
        while True:
            rid = "R%03d" % rng.randrange(1000)
            if rid not in mp:
                break
        mp[rid] = {"tag": t, "response_sha256": tags_sha[t]}
    if stale:
        dest = os.path.join(MARKS_DIR, "stale", time.strftime("%Y%m%dT%H%M%S"))
        os.makedirs(dest, exist_ok=True)
        for rid in stale:
            for sub in ("", "opus_inputs", "adjudication_inputs"):
                d = os.path.join(MARKS_DIR, sub)
                if os.path.isdir(d):
                    for f in os.listdir(d):
                        if f.startswith(rid + "_by_") or f.startswith(rid + "."):
                            shutil.move(os.path.join(d, f), os.path.join(dest, (sub + "__" if sub else "") + f))
        print("reports changed since they were mapped; their marks moved to", dest, ":", stale)
    C.write_atomic(os.path.join(MARKS_DIR, "MAP.json"), json.dumps(mp, indent=1, sort_keys=True))
    return mp


def mark(key_file, accept_missing=False, dry_run=False, test_key=False):
    import s80_table
    if test_key and os.path.abspath(C.OUT) == os.path.abspath(C.REAL_OUT):
        raise SystemExit("--test-key is for a synthetic output root only")
    C.check_documents()
    key = C.load_key(key_file, check_sha=not test_key)
    status = s80_table.completeness(READERS_DIR)
    bad = {t: s for t, s in status["tags"].items() if s != "ok"}
    if status["unexpected"]:
        raise SystemExit("unexpected files in readers/: %s" % status["unexpected"][:10])
    if bad:
        s80_table.print_failures(status)
        if not accept_missing:
            raise SystemExit("%d expected reports are not present and complete; marking does not start" % len(bad))
        not_ok = [t for t, s in bad.items() if s != "failed-twice"]
        if not_ok:
            raise SystemExit("--accept-missing needs a failed receipt from two passes for each; not so for %s" % not_ok)
    tags_sha = {t: C.sha256(C.read(os.path.join(READERS_DIR, t + ".response.txt")))
                for t, s in status["tags"].items() if s == "ok"}
    os.makedirs(MARKS_DIR, exist_ok=True)
    mp = build_map(tags_sha)
    C.write_atomic(os.path.join(MARKS_DIR, "MISSING.json"), json.dumps(sorted(bad), indent=1))
    task = C.read(os.path.join(C.PR, "marker task.md"))
    jobs, n_opus = [], 0
    for rid, v in sorted(mp.items()):
        t = v["tag"]
        info = C.parse_tag(t)
        report = C.read(os.path.join(READERS_DIR, t + ".response.txt"))
        user = marker_user_text(task, key, info["doc"], rid, report)
        extra = {"rid": rid, "report_sha256": v["response_sha256"], "key_sha256": key["sha256"], "doc": info["doc"],
                 "key_ids": C.key_ids(info["doc"])}
        for m in C.MARKERS_FOR[info["reader"]]:
            if m == "opus":
                d = os.path.join(MARKS_DIR, "opus_inputs")
                if not os.path.exists(os.path.join(d, rid + ".md")):
                    C.write(os.path.join(d, rid + ".md"), user)
                    C.write(os.path.join(d, rid + ".meta.json"),
                            json.dumps(dict(extra, input_sha256=C.sha256(user)), indent=1))
                n_opus += 1
            else:
                jobs.append(dict(tag=f"{rid}_by_{m}", model=m, user=user, extra=extra, out=MARKS_DIR))
    print("API marker calls:", len(jobs), " Opus marker inputs:", n_opus, " missing reports:", len(bad))
    if dry_run:
        return

    def accept_mark_for(ids):
        def acc(res):
            if res["finish"] != "stop":
                return False, "finish %s" % res["finish"]
            obj, probs = C.validate_mark(res["content"], ids)
            return (True, "") if obj else (False, "; ".join(probs)[:500])
        return acc

    run_pool(jobs, lambda j: call(j["model"], None, j["user"], MARKS_DIR, j["tag"], True,
                                  C.ladder_for(j["model"], C.MARKER_LADDER), accept_mark_for(j["extra"]["key_ids"]),
                                  extra=j["extra"], max_rejects=2, effort=C.effort_for("s80", j["model"])))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "list":
        js = reader_jobs()
        for j in js:
            print(j["tag"])
        print(len(js), "API reader jobs;", len(C.opus_tags()), "Opus reader tags run by the orchestrator")
    elif a[0] == "manifest":
        print(json.dumps({k: v for k, v in manifest_check().items() if k != "job_order"}, indent=1))
    elif a[0] == "readers":
        readers(a[2:] if len(a) > 1 and a[1] == "--only" else [])
    elif a[0] == "mark":
        mark(a[1], accept_missing="--accept-missing" in a, dry_run="--dry-run" in a, test_key="--test-key" in a)
    else:
        raise SystemExit(__doc__)
