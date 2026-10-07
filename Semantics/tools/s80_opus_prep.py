#!/usr/bin/env python3
"""s80_opus_prep.py: build the working folders and prompts for the Opus 5.5 reader arm of round S80 (plan S80, second
version). The arm is separate and does not vote: conditions S (skill), P (placebo), N (nothing); documents seeded and
clean; three repetitions; 18 subagents, run by the orchestrator at most five at a time.

  python Semantics/tools/s80_opus_prep.py                      # attempt 1 for all 18 tags
  python Semantics/tools/s80_opus_prep.py --attempt 2 TAG ...  # the one rerun of a voided repetition

Each folder is OUTSIDE the repository, under <root>/opus/<code>/, where <code> is a neutral name that says nothing of
condition or document. It holds only document.md and, for S and P, method/SKILL.md and method/references/*.md. The
prompt for each tag is written to <root>/opus_admin/prompts/<tag>.a<k>.md, and the map from tag to folder to
<root>/opus_admin/MAP.json; neither is inside any agent's folder. <root> defaults to the session scratchpad's s80/
folder and can be set with S80_OPUS_ROOT.

The prompt is the API arm's framing and task: the same first sentence, the same method framing (reworded only where the
method is a folder rather than text below), the same task text with its first line saying where the document is, and a
closing line saying where to write the report. Nothing is sent anywhere by this script.
"""
import hashlib, json, os, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C

ROOT = os.environ.get("S80_OPUS_ROOT",
                      "/tmp/claude-0/-home-user-ThreadSmith/b7f93a41-2fef-58bf-8052-3a6eefa05845/scratchpad/rr")
WORK = os.path.join(ROOT, "opus")
ADMIN = os.path.join(ROOT, "opus_admin")
API_FIRST = 'Below is a theory document, "Claude Fable Semantics". Audit it.'
OPUS_FIRST = 'The file document.md in your working folder is a theory document, "Claude Fable Semantics". Audit it.'
API_TAIL = "THE DOCUMENT\n============"


def opus_task():
    t = C.read(os.path.join(C.PR, "reader task.md"))
    if not t.startswith(API_FIRST) or API_TAIL not in t:
        raise SystemExit("reader task.md does not have the expected first line and document heading")
    body = t[len(API_FIRST):t.index(API_TAIL)].rstrip()
    return OPUS_FIRST + body


def prompt_for(cond, folder):
    framing = ("You are reviewing a document." if cond == "N"
               else C.read(os.path.join(C.PR, "reader framing - with method - Opus arm.md")).strip())
    w = C.read(os.path.join(C.PR, "reader wrapper - Opus arm.md"))
    return w.replace("{FRAMING}", framing).replace("{FOLDER}", folder).replace("{TASK}", opus_task())


def code_for(tag, attempt):
    return "w" + hashlib.sha256(("S80-opus-folder|%s|%d" % (tag, attempt)).encode()).hexdigest()[:8]


def build(tag, attempt, mp):
    info = C.parse_tag(tag)
    code = code_for(tag, attempt)
    folder = os.path.join(WORK, code)
    if os.path.exists(os.path.join(folder, "report.md")):
        print(tag, "attempt", attempt, "already has a report; left as it is")
        return
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
    shutil.copyfile(C.DOCS[info["doc"]], os.path.join(folder, "document.md"))
    if C.md5_file(os.path.join(folder, "document.md")) != C.DOC_MD5[info["doc"]]:
        raise SystemExit("copied document does not match its md5")
    method_sha = None
    if info["method"] in ("S", "P"):
        src = C.METHOD_DIRS[info["method"]]
        for f in C.method_files(info["method"]):
            dst = os.path.join(folder, "method", f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(os.path.join(src, f), dst)
        method_sha = C.sha256(C.method_text(info["method"]))
    prompt = prompt_for(info["method"], folder)
    ppath = os.path.join(ADMIN, "prompts", "%s.a%d.md" % (tag, attempt))
    C.write(ppath, prompt)
    mp.setdefault(tag, {})[str(attempt)] = {"code": code, "folder": folder, "prompt": ppath,
                                            "prompt_sha256": C.sha256(prompt), "method_text_sha256": method_sha,
                                            "document_md5": C.DOC_MD5[info["doc"]],
                                            "files": sorted(os.path.relpath(os.path.join(dp, f), folder)
                                                            for dp, _, fs in os.walk(folder) for f in fs)}
    print(tag, "attempt", attempt, "->", folder)


def main(a):
    C.check_documents()
    if os.path.abspath(ROOT).startswith(C.REPO + os.sep):
        raise SystemExit("the Opus folders must be outside the repository")
    mpath = os.path.join(ADMIN, "MAP.json")
    mp = json.loads(C.read(mpath)) if os.path.exists(mpath) else {}
    if a and a[0] == "--attempt":
        attempt, tags = int(a[1]), a[2:]
        if attempt != 2 or not tags:
            raise SystemExit("usage: --attempt 2 TAG ...  (one rerun only, for a voided repetition)")
    else:
        attempt, tags = 1, C.opus_tags()
    for t in tags:
        if not C.TAG_OPUS.match(t):
            raise SystemExit("not an Opus tag: %s" % t)
        if attempt == 2 and "1" not in mp.get(t, {}):
            raise SystemExit("%s has no first attempt" % t)
        build(t, attempt, mp)
    C.write_atomic(mpath, json.dumps(mp, indent=1, sort_keys=True))
    print("map:", mpath)


if __name__ == "__main__":
    main(sys.argv[1:])
