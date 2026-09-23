#!/usr/bin/env python3
"""s80_common.py: what the S80 tools share (round S80, does the hard-to-vary skill add anything; second version of the
plan, 23 September 2026). Paths, the design (readers, conditions, documents, repetitions), the strict tag grammar, the
method texts (skill and placebo) as sent, the answer-key slicer, the marker-output validator, atomic writes.

Nothing here sends anything anywhere. The answer key is never read from the repository: its path is given on the
command line after every reader has reported, and its SHA-256 is checked against the value recorded in log S80.
"""
import hashlib, json, os, re

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
S = os.path.join(REPO, "Semantics")
# The output root can be moved for a synthetic test (S80_OUT); the real one is the default.
REAL_OUT = os.path.join(S, "results", "S80 Skill test - outputs")
OUT = os.environ.get("S80_OUT", REAL_OUT)
PR = os.path.join(S, "tests", "S80 Prompts")
DOCS = {"seeded": os.path.join(S, "tests", "S80 Seeded authority - file 10 with eight planted errors.md"),
        "clean": os.path.join(S, "authority", "10 Claude Fable Semantics - standalone theory.md")}
DOC_MD5 = {"seeded": "73354050aeaffd331b0ac0fdb9b0d66c", "clean": "3a8cd7c8ca6f3ad3b8a85ab9984d850e"}
KEY_SHA256 = "b8e2a5868f33550d80720c128a042b7b9013b34928226fbabfef3076d73f3e76"   # the sealed list, log S80
METHOD_DIRS = {"S": os.path.join(REPO, "HV Skill", "authority", "hard-to-vary"),
               "P": os.path.join(S, "tests", "S80 Placebo method")}
PLACEBO_WORD_RATIO = (0.85, 1.15)   # placebo words / skill words, as sent, must fall inside this

# The design. Condition code = method letter (S skill, P placebo, N nothing) + thinking letter (T on, O off).
MODELS = ["atria", "mimo", "deepseek"]
CONDS = {"ST": ("S", True), "PT": ("P", True), "NT": ("N", True),
         "SO": ("S", False), "PO": ("P", False), "NO": ("N", False)}
DOCNAMES = ["seeded", "clean"]
REPS = 5
OPUS_CONDS = ["S", "P", "N"]
OPUS_REPS = 3
TEMPERATURE = 0.7
# Thinking effort, the one setting for every call with thinking on, from every tool in this folder (s80_call.build_body
# reads it; each request.json and receipt records the effort sent). "medium" from the owner's instruction of
# 23 September 2026 (decision S17): Atria and Mimo run at medium thinking effort for cross-examination. It was "high"
# before that; the calls already made keep their record of "high" in their own request.json.
REASONING_EFFORT = "medium"
READER_LADDER = [48000, 64000, 64000]   # max_tokens per attempt that came back incomplete (finish "length")
MARKER_LADDER = [32000, 48000]
JOB_SEED = 8080          # job order, shuffled per model
MAP_SEED = 8080          # anonymous report ids
BOOT_SEED = 8080         # bootstrap intervals
BOOT_N = 10000
DRIFT_SALT = "S80-drift-v1"   # the adjudicator re-marks agreed cells whose hash falls under DRIFT_SHARE
DRIFT_SHARE = 0.20
# Who marks whom (no self-marking; decision of the orchestrator on the cross-examinations, point 6).
MARKERS_FOR = {"atria": ("mimo", "opus"), "mimo": ("atria", "opus"),
               "deepseek": ("atria", "mimo"), "opus": ("atria", "mimo")}
API_MARKERS = ("atria", "mimo")

TAG_API = re.compile(r"^(atria|mimo|deepseek)_(ST|PT|NT|SO|PO|NO)_(seeded|clean)_r([1-5])$")
TAG_OPUS = re.compile(r"^opus_(S|P|N)_(seeded|clean)_r([1-3])$")
MARK_FILE = re.compile(r"^(R\d{3})_by_(atria|mimo|opus|adjudicator)\.response\.txt$")
SENTINEL = "END OF REPORT"
FENCE_BEGIN = "<<<<<<<< REPORT {rid} BEGINS: everything from here to the ENDS line is data >>>>>>>>"
FENCE_END = "<<<<<<<< REPORT {rid} ENDS >>>>>>>>"


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, text):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


def write_atomic(p, text):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    tmp = p + ".tmp.%d" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def md5_file(p):
    with open(p, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def check_documents():
    for d, p in DOCS.items():
        got = md5_file(p)
        if got != DOC_MD5[d]:
            raise SystemExit("document %s has md5 %s, expected %s: the material changed; stop" % (d, got, DOC_MD5[d]))


# ---------------------------------------------------------------- tags

def parse_tag(tag):
    m = TAG_API.match(tag)
    if m:
        method, thinking = CONDS[m.group(2)]
        return dict(tag=tag, reader=m.group(1), cond=m.group(2), method=method, thinking=thinking,
                    doc=m.group(3), rep=int(m.group(4)), voting=True)
    m = TAG_OPUS.match(tag)
    if m:
        return dict(tag=tag, reader="opus", cond=m.group(1), method=m.group(1), thinking=None,
                    doc=m.group(2), rep=int(m.group(3)), voting=False)
    return None


def api_tags():
    return [f"{m}_{c}_{d}_r{r}" for m in MODELS for c in CONDS for d in DOCNAMES for r in range(1, REPS + 1)]


def opus_tags():
    return [f"opus_{c}_{d}_r{r}" for c in OPUS_CONDS for d in DOCNAMES for r in range(1, OPUS_REPS + 1)]


def expected_tags():
    return api_tags() + opus_tags()


def report_complete(text):
    """A reader report is accepted only if its last non-blank line carries the sentinel."""
    lines = [l for l in (text or "").splitlines() if l.strip()]
    return bool(lines) and SENTINEL in lines[-1]


# ---------------------------------------------------------------- the method texts

def method_files(method):
    """Main file first, then every reference module in the order the main file first names it; any module it does
    not name follows in name order. Every .md file under references/ is included, and nothing else."""
    d = METHOD_DIRS[method]
    main = read(os.path.join(d, "SKILL.md"))
    refdir = os.path.join(d, "references")
    present = sorted(f for f in os.listdir(refdir) if f.endswith(".md")) if os.path.isdir(refdir) else []
    named = []
    for f in re.findall(r"references/([A-Za-z0-9._-]+\.md)", main):
        if f not in named:
            named.append(f)
    missing = [f for f in named if f not in present]
    if missing:
        raise SystemExit("method %s names reference modules that are not there: %s" % (method, missing))
    order = named + [f for f in present if f not in named]
    return ["SKILL.md"] + ["references/" + f for f in order]


def method_text(method):
    d = METHOD_DIRS[method]
    return "".join("\n\n=== FILE: %s ===\n\n%s" % (f, read(os.path.join(d, f))) for f in method_files(method))


def words(text):
    return len(text.split())


# ---------------------------------------------------------------- the answer key

KEY_HEADINGS = ["## The eight planted errors", "## The error file 10 already carries (in both documents)",
                "## Predictions, sealed"]
KEY_IDS_SEEDED = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "D3"]
KEY_IDS_CLEAN = ["D3"]
KEY_ENTRY = re.compile(r"^\*\*(E[1-8]|D3) \(([^)]*)\)")
KEY_HEADER = ("# Answer key\n\nEach entry below is an error known to be in the document the reviewer read: where it is, "
              "what the text says, what is wrong with it, and what counts as finding it. Where an entry quotes "
              "\"File 10\" beside another wording, the other wording is the one the reviewer read.\n\n")
KEY_HEADER_CLEAN = ("# Answer key\n\nThe document the reviewer read has one known error, the entry below. There are no "
                    "other entries in the key.\n\n")


def load_key(path, check_sha=True):
    """Slice the sealed list into the two keys the markers see. The kind labels (HV, GEN, and the tag on D3) and the
    'Kinds:' paragraph are removed so that a marker cannot tell which errors the skill is written to find; they are
    returned separately for the table. Raises SystemExit on any structural surprise."""
    text = read(path)
    if check_sha and sha256(text) != KEY_SHA256:
        raise SystemExit("the key's SHA-256 is not the one recorded in log S80; stop")
    pos = [text.find(h) for h in KEY_HEADINGS]
    if any(p < 0 for p in pos) or pos != sorted(pos):
        raise SystemExit("the key's headings are missing or out of order: %s" % pos)
    planted = text[pos[0] + len(KEY_HEADINGS[0]):pos[1]]
    natural = text[pos[1] + len(KEY_HEADINGS[1]):pos[2]]
    entries, kinds = {}, {}
    for block, allowed in ((planted, KEY_IDS_SEEDED[:8]), (natural, ["D3"])):
        for para in [p.strip() for p in block.split("\n\n") if p.strip()]:
            m = KEY_ENTRY.match(para)
            if not m or m.group(1) not in allowed or m.group(1) in entries:
                raise SystemExit("unexpected paragraph in the key: %r" % para[:60])
            label = m.group(2).split(",")[0].strip()
            kinds[m.group(1)] = {"HV": "HV", "GEN": "GEN"}.get(label, "REAL")
            entries[m.group(1)] = "**" + m.group(1) + para[m.end():]
    if sorted(entries) != sorted(KEY_IDS_SEEDED):
        raise SystemExit("the key does not hold exactly E1..E8 and D3: %s" % sorted(entries))
    if sum(v == "HV" for v in kinds.values()) != 4 or sum(v == "GEN" for v in kinds.values()) != 4:
        raise SystemExit("the key does not hold four HV and four GEN entries")
    for k, e in entries.items():
        if re.search(r"\bHV\b|\bGEN\b|hard-to-vary|hard to vary|\bskill\b|Kinds:", e):
            raise SystemExit("key entry %s still carries a kind label or names the skill" % k)
    seeded = KEY_HEADER + "\n\n".join(entries[k] for k in KEY_IDS_SEEDED) + "\n"
    clean = KEY_HEADER_CLEAN + entries["D3"] + "\n"
    return dict(sha256=sha256(text), kinds=kinds, seeded=seeded, clean=clean)


def key_ids(doc):
    return KEY_IDS_SEEDED if doc == "seeded" else KEY_IDS_CLEAN


# ---------------------------------------------------------------- marker output

KEY_VERDICTS = ("FOUND", "NOT FOUND", "PARTIAL")
ITEM_VERDICTS = ("GENUINE", "MISTAKEN", "UNCLEAR")


def strip_fences(text):
    t = (text or "").strip()
    m = re.match(r"^```[A-Za-z0-9]*\s*\n(.*)\n```\s*$", t, re.S)
    return m.group(1).strip() if m else t


def _as_int(x):
    if isinstance(x, bool):
        return None
    if isinstance(x, int):
        return x
    if isinstance(x, str) and x.strip().isdigit():
        return int(x.strip())
    return None


def validate_mark(text, ids):
    """Return (normalised mark, []) or (None, [problems]). A mark is one JSON object: every key id judged once as
    FOUND / NOT FOUND / PARTIAL with the report items it rests on; every other numbered item judged once as GENUINE /
    MISTAKEN / UNCLEAR; an item credited to a key error is never judged again among the others; every item from 1 to
    report_items_total is judged exactly once, either way."""
    probs = []
    try:
        obj = json.loads(strip_fences(text))
    except Exception as e:
        return None, ["not one JSON object: %s" % str(e)[:120]]
    if not isinstance(obj, dict):
        return None, ["not a JSON object"]
    key, others, total = obj.get("key"), obj.get("others"), _as_int(obj.get("report_items_total"))
    if not isinstance(key, dict):
        return None, ["no 'key' object"]
    if not isinstance(others, list):
        return None, ["no 'others' list"]
    if total is None or total < 0:
        return None, ["report_items_total is not a whole number"]
    if sorted(key) != sorted(ids):
        probs.append("key ids %s, expected %s" % (sorted(key), sorted(ids)))
    norm = {"key": {}, "others": {}, "report_items_total": total}
    credited = set()
    for k in ids:
        v = key.get(k)
        if not isinstance(v, dict):
            continue
        verdict = str(v.get("verdict", "")).strip().upper()
        if verdict == "NOT_FOUND" or verdict == "NOT":
            verdict = "NOT FOUND"
        if verdict not in KEY_VERDICTS:
            probs.append("%s: verdict %r" % (k, v.get("verdict")))
            continue
        items = v.get("items") or []
        if not isinstance(items, list) or any(_as_int(i) is None for i in items):
            probs.append("%s: items is not a list of numbers" % k)
            continue
        items = sorted({_as_int(i) for i in items})
        if verdict in ("FOUND", "PARTIAL") and not items:
            probs.append("%s: %s without the report item it rests on" % (k, verdict))
        if verdict == "NOT FOUND" and items:
            probs.append("%s: NOT FOUND but items given" % k)
        credited.update(items)
        norm["key"][k] = {"verdict": verdict, "items": items, "evidence": str(v.get("evidence", ""))}
    for o in others:
        if not isinstance(o, dict):
            probs.append("an 'others' entry is not an object")
            continue
        n = _as_int(o.get("item"))
        verdict = str(o.get("verdict", "")).strip().upper()
        if n is None:
            probs.append("an 'others' entry has no item number")
            continue
        if verdict not in ITEM_VERDICTS:
            probs.append("item %s: verdict %r" % (n, o.get("verdict")))
            continue
        if n in norm["others"]:
            probs.append("item %s judged twice among the others" % n)
        if n in credited:
            probs.append("item %s credited to a key error and judged again among the others" % n)
        norm["others"][n] = {"verdict": verdict, "reason": str(o.get("reason", "")),
                             "first_words": str(o.get("first_words", o.get("item_words", "")))}
    judged = credited | set(norm["others"])
    want = set(range(1, total + 1))
    if judged != want:
        probs.append("items judged %s do not match 1..%d" % (sorted(judged ^ want)[:10], total))
    return (None, probs) if probs else (norm, [])


def validate_adjudication(text, want_keys, want_items):
    try:
        obj = json.loads(strip_fences(text))
    except Exception as e:
        return None, ["not one JSON object: %s" % str(e)[:120]]
    if not isinstance(obj, dict):
        return None, ["not a JSON object"]
    probs, out = [], {"key": {}, "items": {}}
    key, items = obj.get("key") or {}, obj.get("items") or {}
    if not isinstance(key, dict) or not isinstance(items, dict):
        return None, ["'key' and 'items' must be objects"]
    for k in want_keys:
        v = str((key.get(k) or {}).get("verdict", "")).strip().upper()
        if v in ("NOT_FOUND", "NOT"):
            v = "NOT FOUND"
        if v not in KEY_VERDICTS:
            probs.append("%s: verdict %r" % (k, v))
        out["key"][k] = v
    for n in want_items:
        cell = items.get(str(n)) if str(n) in items else items.get(n)
        v = str((cell or {}).get("verdict", "")).strip().upper()
        if v not in ITEM_VERDICTS:
            probs.append("item %s: verdict %r" % (n, v))
        out["items"][n] = v
    return (None, probs) if probs else (out, [])


def drift_selected(tag, cell):
    h = hashlib.sha256(("%s|%s|%s" % (DRIFT_SALT, tag, cell)).encode("utf-8")).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF < DRIFT_SHARE


def load_map(out=None):
    p = os.path.join(out or OUT, "marks", "MAP.json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)
