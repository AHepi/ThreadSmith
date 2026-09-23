#!/usr/bin/env python3
"""s80_run.py: round S80, does the hard-to-vary skill add anything. Run from the repository root, in the venv, with the
keys exported:
  python Semantics/tools/s80_run.py readers [--only TAG ...]   # the 72 API reader runs
  python Semantics/tools/s80_run.py mark KEY_FILE              # both markers on every report (after the key is opened)
  python Semantics/tools/s80_run.py list                       # print the job list, send nothing

Readers: models atria, mimo, deepseek; conditions ST (skill, thinking on), NT (no skill, thinking on), SO (skill, thinking
off), NO (no skill, thinking off); documents seeded (tests/S80 Seeded authority) and clean (file 10); three repetitions.
Opus 5 readers (skill / no skill, thinking as the agent runs) are run by Claude as subagents and saved in the same folder
as opus_<cond>_<doc>_r<n>.response.txt. At most 3 calls in flight per provider (owner, 23 September 2026).
Markers: atria and mimo, thinking on, each marks every report under an anonymous id; the map from id to tag is kept in
MAP.json beside the marks and is not in any marker's input.
"""
import glob, json, os, random, sys, threading
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from s80_call import call

S = "Semantics"
OUT = f"{S}/results/S80 Skill test - outputs"
PR = f"{S}/tests/S80 Prompts"
DOCS = {"seeded": f"{S}/tests/S80 Seeded authority - file 10 with eight planted errors.md",
        "clean": f"{S}/authority/10 Claude Fable Semantics - standalone theory.md"}
SKILL_DIR = "HV Skill/authority/hard-to-vary"
SKILL_ORDER = ["SKILL.md"] + ["references/" + f for f in ["the-idea-in-depth.md", "question-bank.md", "by-domain.md",
               "building.md", "testing-against-cases.md", "reporting.md", "word-list.md"]]
CONDS = {"ST": (True, True), "NT": (False, True), "SO": (True, False), "NO": (False, False)}  # (skill, thinking)
MODELS = ["atria", "mimo", "deepseek"]
REPS = 3


def read(p):
    return open(p, encoding="utf-8").read()


def skill_text():
    return "".join("\n\n=== FILE: %s ===\n\n%s" % (f, read(os.path.join(SKILL_DIR, f))) for f in SKILL_ORDER)


def reader_jobs():
    jobs = []
    for m in MODELS:
        for c, (skill, think) in CONDS.items():
            for d in DOCS:
                for r in range(1, REPS + 1):
                    jobs.append(dict(tag=f"{m}_{c}_{d}_r{r}", model=m, skill=skill, thinking=think, doc=d))
    return jobs


def run_pool(jobs, fn):
    by_model = {}
    for j in jobs:
        by_model.setdefault(j["model"], []).append(j)
    lock = threading.Lock()
    def worker(j):
        res = fn(j)
        with lock:
            print(j["model"], j["tag"], res, flush=True)
    pools = [ThreadPoolExecutor(max_workers=3) for _ in by_model]
    futs = [pool.submit(worker, j) for pool, js in zip(pools, by_model.values()) for j in js]
    for f in futs:
        f.result()


def readers(only):
    task = read(f"{PR}/reader task.md")
    sys_skill = read(f"{PR}/reader system - with skill.md") + skill_text()
    sys_plain = read(f"{PR}/reader system - without skill.md")
    jobs = [j for j in reader_jobs() if not only or j["tag"] in only]
    run_pool(jobs, lambda j: call(j["model"], sys_skill if j["skill"] else sys_plain, task + read(DOCS[j["doc"]]),
                                  f"{OUT}/readers", j["tag"], j["thinking"]))


def mark(key_file):
    key = read(key_file)
    i = key.index("## The error file 10 already carries")
    j = key.index("## Predictions, sealed")
    key_seeded = key[:j]
    key_clean = ("# Answer key\n\nThe document is file 10 as written; the one known error is D3 below. There are no other "
                 "entries in the key.\n\n" + key[i:j])
    tags = sorted(os.path.basename(p)[:-len(".response.txt")] for p in glob.glob(f"{OUT}/readers/*.response.txt"))
    mp_path = f"{OUT}/marks/MAP.json"
    os.makedirs(f"{OUT}/marks", exist_ok=True)
    mp = json.load(open(mp_path)) if os.path.exists(mp_path) else {}
    rng = random.Random(8080)
    for t in tags:
        if t not in mp.values():
            while True:
                rid = "R%03d" % rng.randrange(1000)
                if rid not in mp:
                    break
            mp[rid] = t
    json.dump(mp, open(mp_path, "w"), indent=1, sort_keys=True)
    task = read(f"{PR}/marker task.md")
    jobs = []
    for rid, t in sorted(mp.items()):
        doc = "seeded" if "_seeded_" in t else "clean"
        for m in ["atria", "mimo"]:
            jobs.append(dict(tag=f"{rid}_by_{m}", model=m, rid=rid, doc=doc, t=t))
    def one(j):
        user = (task + "\n\n(A) ANSWER KEY\n==============\n\n" + (key_seeded if j["doc"] == "seeded" else key_clean)
                + "\n\n(B) THE DOCUMENT THE REVIEWER READ\n==================================\n\n" + read(DOCS[j["doc"]])
                + "\n\n(C) THE REPORT, id " + j["rid"] + "\n=====================\n\n"
                + read(f"{OUT}/readers/{j['t']}.response.txt"))
        return call(j["model"], None, user, f"{OUT}/marks", j["tag"], True, max_tokens=32000)
    run_pool(jobs, one)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        for j in reader_jobs():
            print(j["tag"])
    elif cmd == "readers":
        readers(sys.argv[3:] if len(sys.argv) > 2 and sys.argv[2] == "--only" else [])
    elif cmd == "mark":
        mark(sys.argv[2])
