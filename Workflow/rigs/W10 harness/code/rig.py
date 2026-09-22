"""W10 harness, shared rules: paths, run naming, JSON writing, the key-safety check.

A RULE, not a driver. Importing this file sends nothing and writes nothing.
Plan W10 section 2: "Keys: the owner supplies them; read from the environment, written to no file."
Nothing here reads a key except to check that a key never reaches a saved file.
"""
import os, json, re, hashlib, time

HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, ".."))                 # ".../W10 harness"
REPO = os.path.normpath(os.path.join(RIG, "..", "..", ".."))     # ".../ThreadSmith"

AUTHORITY_SKILL = os.path.join(REPO, "HV Skill", "authority", "33", "hard-to-vary")
SKILL_COPY = os.path.join(RIG, "skill", "hard-to-vary")          # the copy sent to the reader
CORPUS_DIR = os.path.join(RIG, "corpus")                         # A2 writes here
SOURCES = os.path.join(CORPUS_DIR, "sources.json")
SPLIT = os.path.join(CORPUS_DIR, "split.json")
CRITERIA = os.path.join(RIG, "instrument", "criteria.json")      # A4 writes here
RUNS = os.path.join(RIG, "runs")
CALLS = os.path.join(RIG, "calls")
MARKING = os.path.join(RIG, "marking")
FIXTURES = os.path.join(HERE, "fixtures")

SKILL_FILE = "33"
MODULES = ["the-idea-in-depth", "question-bank", "by-domain", "building",
           "testing-against-cases", "reporting", "word-list"]
SKILL_FILES = ["SKILL.md"] + [f"references/{m}.md" for m in MODULES]

# The eight marks of file 33, in the file's own order (SKILL.md, "Stop"). The closed list arm (e) prefills.
MARKS = ["held", "held if", "two routes", "loose", "idle", "borrowed", "fixed", "unknown"]

KEY_ENV = ["DEEPSEEK_API_KEY", "ATRIA_API_KEY"]


def assert_no_key(text, where):
    """Refuse to write anything that contains a key that is in the environment.
    The body of a request never carries the key (it goes in the Authorization header);
    this is the check that keeps it so, so that saving every request as sent (PA.1) is safe."""
    for name in KEY_ENV:
        v = os.environ.get(name, "")
        if len(v) >= 12 and v in text:
            raise SystemExit(f"REFUSED: {where} contains the value of {name}. Nothing written, nothing sent.")
    return True


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(obj, indent=1, ensure_ascii=False)
    assert_no_key(text, path)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)
    return path


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    assert_no_key(text, path)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)
    return path


def read_json(path, what=""):
    if not os.path.exists(path):
        raise SystemExit(f"missing {what or 'file'}: {path}. Nothing sent.")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def run_id(doc, arm, repeat):
    """Runs are named <document>-<arm>-r<repeat>, one folder of calls per run.
    Arm ids: a b c cctl cprime d e f r x k  (cctl is arm (c)'s equal-length control,
    cprime is arm (c')). The reader is named in the run record, never in the run id,
    because the two readers are never summed (W10 section 4)."""
    return f"{doc}-{arm}-r{int(repeat)}"


def parse_run_id(rid):
    """<document>-<arm>-r<repeat> -> (document, arm, repeat). The document id may carry hyphens;
    the arm and the repeat never do."""
    head, arm, rep = rid.rsplit("-", 2)
    if not rep.startswith("r"):
        raise SystemExit(f"{rid!r} is not a run id of the form <document>-<arm>-r<repeat>")
    return head, arm, int(rep[1:])


def run_path(reader, rid):
    return os.path.join(RUNS, reader, rid + ".json")


def call_dir(reader, rid):
    return os.path.join(CALLS, reader, rid)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
