You are cross-examining a test plan before it runs. The plan asks whether a "skill" (a long method document handed to a language model) makes models better at auditing a theory document, using a copy of the document with eight planted errors (four of the kind the skill targets, four ordinary) and the clean document for false alarms. You are given the plan, the prompts, and the runner code. You are not given the planted errors themselves or the skill's text.

Find everything that would make the result wrong, biased, unreadable, or not an answer to the question "does the skill add anything or should it be abandoned". Consider: confounds (prompt length, system prompt asymmetry, the task naming the error kinds), the marking design (markers marking their own model, blinding, the found-rules), the number of repetitions, the Opus arm, the runner code line by line (bugs, retries, rate, file names, resumability, the id map), and anything the plan claims it can read off that it cannot. For each point: what is wrong, why it matters, and the smallest change that fixes it. Number the points, most serious first. Close with exactly one line: RUN AS IS, RUN WITH CHANGES, or DO NOT RUN.



=== FILE: tests/S80 Plan - does the hard-to-vary skill add anything, four readers with and without it, thinking on and off.md ===

# S80 Plan - does the hard-to-vary skill add anything, four readers with and without it, thinking on and off

DRAFT until the cross-examination by Atria and Mimo returns and its points are answered; then frozen by this file's SHA-256, recorded in log S80, and not edited. Written 23 September 2026 under decision S12: "I need to know whether the hard to vary skill adds anything or should be abandoned. Rig Opus 5, Atria and Mimo with and without it. Compare with thinking on with the skill, thinking off without the skill. Use DeepSeek too."

## The question, and what would answer it
The skill (HV Skill project, file 30, `HV Skill/authority/hard-to-vary/`, 8 files, 13,648 words as sent) is used in this project as an audit aid: readers are armed with it (S78) and the other model is given file 24 in its place. So the question is asked in that use: **handed to a reader auditing a theory, does the skill make the reader find more real errors, fewer false ones, or neither?** The HV Skill project's own test (its results file 54) found that the skill changes the *form* of a reader's report (tests run, marks used) but had no answer key; it could not say whether the reports found more that was true. This round has one.

"Adds something" is read off the table as: more planted errors found (either kind) with the skill than without, at the same thinking setting, on two or more of the four readers, with false alarms not rising by more than the gain. "Should be abandoned" is read as: no reader finds more with it, or its gain is bought with as many false alarms. Anything between is reported as it stands, per reader and per error kind. The counts are never added across readers into one score.

## The material
- **Seeded document:** `tests/S80 Seeded authority - file 10 with eight planted errors.md` (md5 73354050aeaffd331b0ac0fdb9b0d66c): file 10 (md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e) with eight edits made by program, each old string matched once. Four are of the kind the skill is written to find (HV: a condition made vacuous, a distinction collapsed, an idle condition claimed independent, a patch that shields the theory), four are ordinary (GEN: a swapped theorem, an arithmetic slip, a biconditional wider than its proof, an invalid refutation step). Where each is and what counts as finding it is in the sealed list, kept outside the repository until every reader has reported; its SHA-256 (b8e2a5868f33550d80720c128a042b7b9013b34928226fbabfef3076d73f3e76) is recorded in log S80 now. The sealed list travels to no reader.
- **Clean document:** file 10 as it is. It carries one known real error, D3 (Derivation 3's claim wider than its proof, logs S70 to S75), which is also in the seeded document. The clean document measures false alarms: what a reader reports when nothing is planted.
- Readers see the document under its own title, "Claude Fable Semantics", with no mention of seeding.

## The readers and the conditions
- **Atria** (Atria-Dawn-Preview), **Mimo** (mimo-v2.6-pro), **DeepSeek** (deepseek-v4-pro), by API, each in four conditions: ST skill with thinking on; NT no skill with thinking on; SO skill with thinking off; NO no skill with thinking off. Thinking is set by `thinking: {type: enabled|disabled}` (all three honour it: probe of 23 September, zero reasoning tokens when disabled); with thinking on, `reasoning_effort: high`. The owner's named comparison is ST against NO; the four cells also separate the skill's effect from thinking's.
- **Opus 5.5** as a subagent, in two conditions: S with the skill (the agent is told to read the skill's directory first), N without. Thinking cannot be switched for a subagent; it runs as the agent runs. The agent is given a working folder holding only the document (and the skill, for S), and told to read nothing else; it has the repository in reach, and the seeded file sits in `tests/` under its S80 name. That leak is named here and checked afterwards: each Opus report is searched for "S80", "seeded" and "planted".
- **Three repetitions** of every cell and both documents: 3 × 4 × 2 × 3 = 72 API reports and 2 × 2 × 3 = 12 Opus reports.
- **The same task for every reader** (`tests/S80 Prompts/reader task.md`): find the defects (false statements, failed proofs, claims wider than support, contradictions, idle conditions, shields from criticism), each with place, quotation, what is wrong, and how sure. The task names the HV kinds and the GEN kinds alike, so a reader without the skill is not left to guess that idle parts or shields count. The skill condition adds a system prompt with the skill whole (main file, then the seven modules, each headed by its name); the no-skill condition has a one-line system prompt.
- `max_tokens` 48,000; provider-default temperature; at most 3 calls in flight per provider (decision S12). The runner is `tools/s80_run.py` with `tools/s80_call.py`; every call is kept with request, response, reasoning and receipt in `results/S80 Skill test - outputs/readers/`.
- One pilot call (DeepSeek, NO, seeded) was made before this plan to test the pipe; it is in the scratch area, not in the outputs, and does not count.

## Marking
- **Markers: Atria and Mimo** (decision S12), thinking on, each marking every one of the 84 reports once (168 calls), with `tests/S80 Prompts/marker task.md`: the key (the sealed list without its predictions, for a seeded report; the D3 entry only, for a clean report), the document the reader saw, and the report under an anonymous id. The map from id to condition is in `marks/MAP.json` and is in no marker's input. A report's wording can still show the skill (its words "held", "loose", "idle"): marking is blind to the label, not to the style, and the per-error rules are written so that style cannot pass for finding.
- A marker returns, per key error, FOUND or NOT with the report's words as evidence, and for every other item GENUINE, MISTAKEN or UNCLEAR. Each marker marks its own model's reports among the rest; the table is given per marker and for agreement (an error counts as found when both markers say FOUND; a false alarm when both say MISTAKEN), and every disagreement is listed.
- **Claude's check:** after both markings and before the map is opened, an Opus 5.5 subagent re-marks every disagreement against the key, from the report's own words, and its call stands for the agreed table's disputed cells, recorded as such.

## The table
Per reader and condition, over three repetitions: HV errors found (of 12), GEN errors found (of 12), D3 found (of 6, both documents), false alarms on the clean document (both markers MISTAKEN), items listed, and tokens and seconds. Read as: the skill's effect at thinking on (ST against NT), at thinking off (SO against NO), the owner's comparison (ST against NO), and thinking's effect with and without the skill. With three repetitions a difference of one error in twelve is noise; the results say so for every difference they report, and a difference is called a finding only when it holds in the same direction on at least two readers.

## Predictions
Sealed in the sealed list (Q1 to Q5), made before any counted run; opened with it.

## Not tested
The skill's other uses: building a theory, testing against cases, questioning a person. Other documents than file 10; errors of other kinds; the skill handed over in other ways (router only, or as file 24). Opus with thinking switched. Temperature. Long-run stability beyond three repetitions.


=== FILE: tests/S80 Prompts/reader task.md ===

Below is a theory document, "Claude Fable Semantics". Audit it.

Your job is to find its defects: statements that are false, proofs that do not prove what they claim, claims wider than their support, parts that contradict other parts, conditions or clauses that do no work, and anything that shields the theory from criticism it should face. Read the whole document before you report.

For each defect give:
1. Where it is: the Part and the heading or label.
2. The exact sentence or formula, quoted.
3. What is wrong, in two to five sentences, with a counterexample or the step that fails where you can give one.
4. How sure you are: sure, likely, or possible.

List the defects most serious first. Report only defects you can state this way. End your report with the line END OF REPORT.

THE DOCUMENT
============



=== FILE: tests/S80 Prompts/reader system - with skill.md ===

You are reviewing a document. You have the skill below, a method for testing explanations, and you should use it for this audit. The skill is given in full: its main file first, then every reference module it names, each headed by its file name.



=== FILE: tests/S80 Prompts/reader system - without skill.md ===

You are reviewing a document.


=== FILE: tests/S80 Prompts/marker task.md ===

You are marking one report written by a reviewer who was asked to audit a theory document and list its defects. You are given: (A) the answer key, which lists errors known to be in the document the reviewer read, with what counts as finding each; (B) the document the reviewer read; (C) the report. The reviewer did not see the answer key.

Mark strictly by the key's "Found when" rules. An error is FOUND only if the report locates it (the right Part, sentence or formula) AND says what is wrong with it in a way the key's rule accepts. Mentioning the location while praising it, or objecting to it for an unrelated reason, is NOT FOUND. Quote the report's own words as evidence for every FOUND.

Then take every other defect the report lists (every item that does not count as finding a key error) and judge it against the document: GENUINE (the document really has this problem as stated), MISTAKEN (the document does not have this problem: the report misreads, misquotes, or its argument fails), or UNCLEAR (a matter of judgement or presentation you cannot settle). Give one sentence of reason each.

Answer with a single JSON object and nothing else, in this form:
{"key": {"<error id>": {"found": true|false, "evidence": "<the report's words, or empty>"}, ...},
 "others": [{"item": "<the report's heading or first words>", "verdict": "GENUINE"|"MISTAKEN"|"UNCLEAR", "reason": "<one sentence>"}, ...],
 "report_items_total": <number of defects the report lists>}

Include every error id in the key, in its order.


=== FILE: tools/s80_run.py ===

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


=== FILE: tools/s80_call.py ===

#!/usr/bin/env python3
"""s80_call.py: one streamed call to an outside model, with a receipt. Written for round S80 (does the hard-to-vary
skill add anything), 23 September 2026, from the pattern of Language/tools/ask_model_2.py (read, not copied across
projects' records: this file is the Semantics project's own).

Providers (keys from the environment only, never from a file in the repository):
  atria     https://api.atria-asi.ai/v1/chat/completions             Atria-Dawn-Preview  ATRIA_API_KEY
  mimo      https://token-plan-sgp.xiaomimimo.com/v1/chat/completions mimo-v2.6-pro       MIMO_API_KEY
  deepseek  https://api.deepseek.com/chat/completions                 deepseek-v4-pro     DEEPSEEK_API_KEY
Thinking is switched with the body field `thinking: {"type": "enabled"|"disabled"}`, which all three accept
(probe of 23 September: reasoning tokens 0 with it disabled on each).

call(provider, system, user, out_dir, tag, thinking, max_tokens) writes <tag>.response.txt, <tag>.reasoning.txt,
<tag>.request.json and <tag>.receipt.json in out_dir; on failure <tag>.error.txt and a receipt with "failed": true.
Retries on 429, 5xx, disconnects, silence and empty answers, at most 5 attempts; 400/401/403/404/413/422 not retried.
"""
import hashlib, json, os, time
import requests

PROVIDERS = {
    "atria": ("https://api.atria-asi.ai/v1/chat/completions", "Atria-Dawn-Preview", "ATRIA_API_KEY"),
    "mimo": ("https://token-plan-sgp.xiaomimimo.com/v1/chat/completions", "mimo-v2.6-pro", "MIMO_API_KEY"),
    "deepseek": ("https://api.deepseek.com/chat/completions", "deepseek-v4-pro", "DEEPSEEK_API_KEY"),
}
FINAL = {400, 401, 403, 404, 413, 422}


def _stream(url, key, body, idle):
    content, reasoning, finish, last, chunks = "", "", None, None, 0
    with requests.post(url, json=body, stream=True, timeout=(30, idle),
                       headers={"Authorization": "Bearer " + key, "Accept": "text/event-stream"}) as r:
        if r.status_code != 200:
            return r.status_code, r.text[:4000], None
        for line in r.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            try:
                d = json.loads(data)
            except Exception:
                continue
            chunks += 1; last = d
            for ch in d.get("choices") or []:
                delta = ch.get("delta") or {}
                content += delta.get("content") or ""
                reasoning += delta.get("reasoning_content") or ""
                if ch.get("finish_reason"):
                    finish = ch["finish_reason"]
    return 200, "", dict(content=content, reasoning=reasoning, finish=finish, last=last, chunks=chunks)


def call(provider, system, user, out_dir, tag, thinking, max_tokens=48000, idle=900, attempts=5):
    url, model, keyname = PROVIDERS[provider]
    key = os.environ[keyname]
    os.makedirs(out_dir, exist_ok=True)
    p = lambda ext: os.path.join(out_dir, tag + ext)
    if os.path.exists(p(".response.txt")):
        return "skipped"
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = {"model": model, "messages": messages, "max_tokens": max_tokens, "stream": True,
            "stream_options": {"include_usage": True},
            "thinking": {"type": "enabled" if thinking else "disabled"}}
    if thinking:
        body["reasoning_effort"] = "high"
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
    open(p(".request.json"), "w").write(raw)
    started, history = time.time(), []
    for n in range(1, attempts + 1):
        t0 = time.time()
        try:
            status, text, res = _stream(url, key, body, idle)
        except Exception as e:
            status, text, res = 0, repr(e), None
        if status == 200 and not (res["content"] or "").strip():
            status, text = (-4 if res["finish"] == "length" else -2), "empty content, finish %s" % res["finish"]
        history.append({"attempt": n, "status": status, "seconds": round(time.time() - t0, 1),
                        "finish": res and res["finish"]})
        if status == 200:
            break
        if status in FINAL or n == attempts:
            open(p(".error.txt"), "w").write("status %s after %d attempts\n%s" % (status, n, text))
            open(p(".receipt.json"), "w").write(json.dumps({"provider": provider, "model": model, "tag": tag,
                "failed": True, "attempt_history": history, "thinking": thinking}, indent=1))
            return "failed"
        time.sleep(min(120, 10 * 2 ** n))
    open(p(".reasoning.txt"), "w").write(res["reasoning"])
    open(p(".response.txt"), "w").write(res["content"])
    last = res["last"] or {}
    open(p(".receipt.json"), "w").write(json.dumps({
        "provider": provider, "model": last.get("model", model), "tag": tag, "thinking": thinking,
        "response_id": last.get("id"), "finish_reason": res["finish"], "chunks": res["chunks"],
        "usage": last.get("usage"), "request_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "response_sha256": hashlib.sha256(res["content"].encode()).hexdigest(),
        "reasoning_chars": len(res["reasoning"]), "attempt_history": history,
        "total_seconds": round(time.time() - started, 1), "asked_at_unix": int(started)}, indent=1))
    return "ok"
