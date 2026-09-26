#!/usr/bin/env python3
"""s80_common.py: what the S80 tools share (round S80, does the hard-to-vary skill add anything; second version of the
plan, 23 September 2026). Paths, the design (readers, conditions, documents, repetitions), the strict tag grammar, the
method texts (skill and placebo) as sent, the answer-key slicer, the marker-output validator, atomic writes.

Nothing here sends anything anywhere. The answer key is never read from the repository: its path is given on the
command line after every reader has reported, and its SHA-256 is checked against the value recorded in log S80.

Since the process audit of 23 September 2026 (findings 1, 5, 6, 12; lessons S10, S11) this file also holds, for every
tool that calls an outside model: the thinking effort by purpose and provider (EFFORT), each provider's max_tokens
ceiling (MAX_TOKENS_CEILING), the slot lock shared by every process that calls a provider (provider_slot), the check on
a runner's pid file, and the one log lock.
"""
import contextlib, fcntl, hashlib, json, os, re, threading, time

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
# Thinking effort, set by the purpose of a call and by the provider, in this one map, which every tool reads (process
# audit of 23 September 2026, finding 5; lesson S11). A call with thinking on names its effort (s80_call refuses one
# that does not), and each request.json and receipt records the effort sent.
#   "s80":   S80's readers and markers, and the probe of their request shape: "high", the effort S80 was designed and
#            run with, so S80's method is unchanged (its request.json files record "high").
#   "audit": S81 Stage 2 and every cross-examination or audit call. Atria and Mimo "medium", from the owner's
#            instruction of 23 September 2026 (decision S17: "Use Atria and Mimo on medium thinking effort for cross
#            examination"). DeepSeek "high": S17 does not name it, and it was never piloted at medium.
# Before this map the tools sent one shared setting to every call ("high", then "medium" from decision S17); every call
# already sent keeps its effort on record in its own request.json.
EFFORT = {"s80": {"atria": "high", "mimo": "high", "deepseek": "high"},
          "audit": {"atria": "medium", "mimo": "medium", "deepseek": "high"}}
EFFORT_LEVELS = ("low", "medium", "high")
# max_tokens. Each provider's ceiling, probed 23 September 2026 (log S83): Atria refuses more than 65,536; Mimo refuses
# 200,000 and takes 131,072. Mimo at high effort spent a 64,000 budget on reasoning and wrote nothing (lessons S7, S11),
# so a provider with a probed ceiling goes at it on every rung, in every tool, S80's included (process audit finding 6);
# a tool's own ladder below is kept for a provider with no probed ceiling (DeepSeek). Calls already sent keep their
# record in their request.json.
MAX_TOKENS_CEILING = {"atria": 65536, "mimo": 131072}
READER_LADDER = [48000, 64000, 64000]   # S80's reader ladder: max_tokens per attempt that came back incomplete
MARKER_LADDER = [32000, 48000]          # S80's marker ladder
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


def effort_for(purpose, provider):
    """The thinking effort for a call of this purpose to this provider, from EFFORT; a pair not in the map raises."""
    if purpose not in EFFORT or provider not in EFFORT[purpose]:
        raise ValueError("no thinking effort set for purpose %r and provider %r in s80_common.EFFORT"
                         % (purpose, provider))
    return EFFORT[purpose][provider]


def ladder_for(provider, base):
    """The max_tokens ladder for a call to `provider` of a kind whose own ladder is `base`: the provider's probed
    ceiling on every rung where it has one, `base` itself where it has none."""
    cap = MAX_TOKENS_CEILING.get(provider)
    return [cap] * len(base) if cap else list(base)


def check_ladder(provider, ladder):
    """Raise unless `ladder` is a non-empty list of positive whole numbers, none above the provider's ceiling."""
    if (not isinstance(ladder, (list, tuple)) or not ladder
            or any(isinstance(r, bool) or not isinstance(r, int) or r <= 0 for r in ladder)):
        raise ValueError("max_tokens ladder %r is not a list of positive whole numbers" % (ladder,))
    cap = MAX_TOKENS_CEILING.get(provider)
    if cap and max(ladder) > cap:
        raise ValueError("max_tokens ladder %r goes above %s's ceiling of %d (s80_common.MAX_TOKENS_CEILING)"
                         % (list(ladder), provider, cap))


# ---------------------------------------------------------------- outside the repository: slots, pid files, the log

# The providers' slot locks and the runners' pid files live outside the repository (process audit finding 1; lesson
# S10). Every call to a provider takes one of its SLOTS_PER_PROVIDER slots first (s80_call.call, s80_probe), so the
# limit of three calls in flight to each provider (decisions S12, S17) holds across every process on this machine that
# uses these tools, not only within one pool. SEMANTICS_RUN_DIR moves the folder; every runner must then see the same
# value, or the limit no longer holds between them.
RUN_DIR = os.environ.get("SEMANTICS_RUN_DIR",
                         "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad")
LOCK_DIR = os.path.join(RUN_DIR, "locks")
SLOTS_PER_PROVIDER = 3
# The S81 Stage 2 runner of 23 September 2026 (pass 2 and the effort controls) ran from the code before the slot lock,
# so it takes no slot: nothing that sends may start while its pid file names a live process.
S81_RUN_PIDFILE = os.path.join(RUN_DIR, "s81_run2.pid")
LOG_LOCK = threading.Lock()
_held = threading.local()


def log(*parts):
    """One line with the time, printed whole: every runner's progress line goes through this one lock."""
    with LOG_LOCK:
        print(time.strftime("%H:%M:%S"), *parts, flush=True)


def _inside(path, root):
    path, root = os.path.realpath(path), os.path.realpath(root)
    return path == root or path.startswith(root + os.sep)


def holds_slot(provider):
    """Whether this thread holds one of the provider's slots now (s80_call.stream refuses to send otherwise)."""
    return getattr(_held, "count", {}).get(provider, 0) > 0


def _hold(provider, step):
    if not hasattr(_held, "count"):
        _held.count = {}
    _held.count[provider] = _held.count.get(provider, 0) + step


@contextlib.contextmanager
def provider_slot(provider, label="", poll=5.0):
    """Hold one of the provider's SLOTS_PER_PROVIDER slots for the length of the block: an exclusive flock on
    LOCK_DIR/<provider>.slot<N>, waiting until one is free (said once, through log). The kernel drops a flock when the
    process holding it ends, however it ends, so a dead holder leaves no stale slot and nothing needs cleaning up; the
    pid, label and time written into the file are for a person reading it. Threads of one process each open the file
    afresh, so they exclude one another too. Yields {"slot": N, "waited_seconds": s}."""
    if _inside(LOCK_DIR, REPO):
        raise SystemExit("the lock folder %s is inside the repository; set SEMANTICS_RUN_DIR outside it" % LOCK_DIR)
    os.makedirs(LOCK_DIR, mode=0o700, exist_ok=True)
    t0, said = time.time(), False
    while True:
        for n in range(SLOTS_PER_PROVIDER):
            fd = os.open(os.path.join(LOCK_DIR, "%s.slot%d" % (provider, n)), os.O_RDWR | os.O_CREAT, 0o600)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os.close(fd)
                continue
            try:
                os.ftruncate(fd, 0)
                os.write(fd, ("pid %d, %s, since %s\n" % (os.getpid(), label or "-",
                                                         time.strftime("%Y-%m-%d %H:%M:%S"))).encode("utf-8"))
                _hold(provider, 1)
                yield {"slot": n, "waited_seconds": round(time.time() - t0, 1)}
            finally:
                _hold(provider, -1)
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)
            return
        if not said:
            log("waiting for a free %s slot (all %d held)%s" % (provider, SLOTS_PER_PROVIDER,
                                                                 (" for " + label) if label else ""))
            said = True
        time.sleep(poll)


@contextlib.contextmanager
def tag_lock(out_dir, tag):
    """An exclusive, non-waiting lock on one call's outputs (out_dir + tag), held by s80_call.call for the whole call,
    so two processes (or threads) never send the same tag into the same folder at once and overwrite each other's
    files. Yields True when taken, False when another holder has it."""
    if _inside(LOCK_DIR, REPO):
        raise SystemExit("the lock folder %s is inside the repository; set SEMANTICS_RUN_DIR outside it" % LOCK_DIR)
    os.makedirs(LOCK_DIR, mode=0o700, exist_ok=True)
    key = hashlib.sha256((os.path.realpath(out_dir) + "\0" + tag).encode("utf-8")).hexdigest()[:24]
    fd = os.open(os.path.join(LOCK_DIR, "tag-%s.lock" % key), os.O_RDWR | os.O_CREAT, 0o600)
    got = True
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        got = False
    try:
        yield got
    finally:
        if got:
            fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def live_pid(pidfile):
    """The pid named in `pidfile` if that process is alive (not ended, not a zombie, not this process), else None."""
    try:
        with open(pidfile, encoding="utf-8") as f:
            pid = int(f.read().strip() or "0")
    except (OSError, ValueError):
        return None
    if pid <= 0 or pid == os.getpid():
        return None
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return None
    except PermissionError:
        return pid
    try:
        with open("/proc/%d/stat" % pid, encoding="utf-8") as f:
            if f.read().rsplit(")", 1)[1].split()[0] == "Z":
                return None
    except (OSError, IndexError):
        pass
    return pid


def refuse_if_runner_alive(pidfiles=None):
    """Raise SystemExit, before anything is sent, while a pid file names a live runner that takes no slot."""
    for p in pidfiles or [S81_RUN_PIDFILE]:
        pid = live_pid(p)
        if pid:
            raise SystemExit("%s names pid %d, which is alive: that runner takes no provider slot, so the limit of %d "
                             "per provider cannot hold; nothing sent" % (p, pid, SLOTS_PER_PROVIDER))


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
