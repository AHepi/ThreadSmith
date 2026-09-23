#!/usr/bin/env python3
"""s81_sonnet_collect.py: bring the Stage 1 returns of round S81, second version (Sonnet subagent testers A and B,
plan `tests/S81 Plan - second version, Sonnet testers and API auditors.md`), into the S81 outputs, with the
contamination check of that plan.

  python Semantics/tools/s81_sonnet_collect.py --transcripts DIR   # DIR/<folder tag>.jsonl: each agent's transcript
  python Semantics/tools/s81_sonnet_collect.py --no-transcripts    # records that no transcript was checked
  python Semantics/tools/s81_sonnet_collect.py --clear A2 "REASON" # the orchestrator's ruling on a word-only void

For each agent (A1 to B3, s81_sonnet_prep.py), the latest prepared attempt is read from its folder:
- return.md missing: nothing is done (not yet run).
- The return is VOID if it carries any of: S81, S76, S75, R2 J (as written), or "prediction", "O48 change" (any case).
  A double-quoted span of the return that stands word for word in the agent's own brief.md is left out of this scan:
  the theory itself uses the word "prediction", and a sentence copied from the text the agent was given is no sign of
  contamination. The lines of every remaining hit are recorded.
- The run is VOID if its tool-call extract touches any path outside its folder. The extract is made here with
  tools/s80_transcript_extract.py from the transcript the orchestrator supplies, and kept as stage1/<tag>.tools.txt.
  Read, Write, Edit: the file path must lie in the folder. Glob, Grep: a path must be given and lie in the folder (a
  missing path means the working directory, which is the repository). Bash: every absolute path must lie in the folder,
  at least one must name it, and "~" or ".." as a path voids; the body of a heredoc is content and is not scanned. TodoWrite and ToolSearch pass. Any other tool voids.
- brief.md changed voids the attempt. The return's last non-blank line lacking END OF REPORT, or a 1C or 1K return
  lacking a record with a MARK line for any of O1 to O52 (a 1D return lacking its Counts section), makes it incomplete.
- A void or incomplete attempt is kept as returns/<s81 tag>.pass<k>.void.txt or .truncated.txt with a receipt
  .pass<k>.receipt.json ("failed": true); it is rerun once (s81_sonnet_prep.py --attempt 2 TAG).
- A clean, complete return is copied to returns/<s81 tag>.response.txt, the name s81_build.py reads for a Stage 1
  return; the prompt to <s81 tag>.request.md; a receipt to <s81 tag>.receipt.json.
- --clear: a void whose only hits are the word "prediction" outside a quotation may be read by the orchestrator (the
  authority, decision S13) and cleared with a reason; the reason and the hits stay in the receipt. Nothing else clears.
Every run rewrites stage1/contamination.md, the table of every attempt judged so far.
"""
import hashlib, json, os, re, shutil, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s81_build as B
from s81_sonnet_prep import AGENTS, MAP, SENTINEL

S1 = os.path.join(B.OUT, "stage1")
VOID_IDS = ["S81", "S76", "S75", "R2 J"]          # matched as written
VOID_WORDS = ["prediction", "O48 change"]          # matched in any case
CLEARABLE = {"prediction"}
PATH_RE = re.compile(r"(/(?:tmp|home|root|etc|usr|var|opt|proc|mnt|srv|dev|sys|bin|lib|run|workspace|Users)"
                     r"(?:/[^\s\"'`<>|;,)\]}]*)?)")
QUOTE_RE = re.compile(r'"([^"\n]{8,}?)"|“([^”\n]{8,}?)”')
PASS_TOOLS = {"TodoWrite", "ToolSearch"}
HEREDOC_RE = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?\n\s*\2\s*(?=\n|$)", re.S)


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def inside(p, folder):
    p = os.path.normpath(p)
    return p == folder or p.startswith(folder + "/")


def complete(text):
    lines = [l for l in (text or "").splitlines() if l.strip()]
    return bool(lines) and SENTINEL in lines[-1]


def form_missing(s81tag, text):
    """What the brief's form requires and the return lacks: a 1C or 1K return needs a record with a MARK for each of
    O1 to O52 (a Write that overwrote an earlier part leaves the sentinel and loses records); a 1D return needs its
    Counts section."""
    if "_1D_" in s81tag:
        return [] if re.search(r"^## Counts", text, re.M) else ["the Counts section"]
    recs = B.records(text)
    return [c for c in B.CASES if not (recs.get(c, {}).get("MARK"))]


def return_hits(ret, brief):
    """[(word, line)] for every void string, after removing quoted spans that stand in the brief word for word."""
    nb = B.norm(brief)
    kept = QUOTE_RE.sub(lambda m: " " if B.norm(m.group(1) or m.group(2)) in nb else m.group(0), ret)
    hits = []
    for line in kept.split("\n"):
        for w in VOID_IDS:
            if w in line:
                hits.append((w, line.strip()[:300]))
        for w in VOID_WORDS:
            if w.lower() in line.lower():
                hits.append((w, line.strip()[:300]))
    return hits


def tool_hits(extract, folder):
    """[reason] for every tool call in the extract that touches a path outside the folder."""
    hits = []
    for n, line in enumerate(l for l in extract.split("\n") if l.strip()):
        name, _, raw = line.partition(" ")
        try:
            inp = json.loads(raw) if raw.strip() else {}
        except Exception:
            hits.append("call %d %s: input unreadable" % (n + 1, name))
            continue
        where = "call %d %s" % (n + 1, name)
        if name in PASS_TOOLS:
            continue
        if name in ("Read", "Write", "Edit", "MultiEdit", "NotebookEdit", "NotebookRead"):
            p = inp.get("file_path") or inp.get("notebook_path") or ""
            if not (os.path.isabs(p) and inside(p, folder)):
                hits.append("%s: path outside the folder: %s" % (where, p[:200]))
        elif name in ("Glob", "Grep"):
            p = inp.get("path") or ""
            if not (os.path.isabs(p) and inside(p, folder)):
                hits.append("%s: search outside the folder: %s" % (where, p[:200] or "(no path: the working directory)"))
            for q in PATH_RE.findall(inp.get("pattern", "") + " " + inp.get("glob", "")):
                if not inside(q.rstrip(".:"), folder):
                    hits.append("%s: pattern names a path outside the folder: %s" % (where, q[:200]))
        elif name == "Bash":
            cmd = HEREDOC_RE.sub("<<HEREDOC", inp.get("command", ""))   # text written through a heredoc is content
            ps = [q.rstrip(".:") for q in PATH_RE.findall(cmd)]
            bad = [q for q in ps if not inside(q, folder)]
            for q in bad:
                hits.append("%s: path outside the folder: %s" % (where, q[:200]))
            if not any(inside(q, folder) for q in ps):
                hits.append("%s: names no path in the folder (runs in the working directory): %s" % (where, cmd[:200]))
            if re.search(r"(^|[\s=:\"'])~[\w-]*(/|$|\s*[;&|])|(^|[\s=:\"'/])\.\.(/|\s|$)", cmd):
                hits.append("%s: relative escape (~ or ..): %s" % (where, cmd[:200]))
        else:
            hits.append("%s: a tool outside the folder's task" % where)
    return hits


def served_models(transcript_path):
    ms = set()
    for line in open(transcript_path, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        m = (d.get("message") or {}).get("model") if isinstance(d.get("message"), dict) else None
        if m:
            ms.add(m)
    return sorted(ms)


def extract(tdir, ft):
    tp = None
    for ext in (".jsonl", ".json", ".txt"):
        if os.path.exists(os.path.join(tdir, ft + ext)):
            tp = os.path.join(tdir, ft + ext)
            break
    if not tp:
        return None, None, None
    out = os.path.join(S1, ft + ".tools.txt")
    os.makedirs(S1, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(HERE, "s80_transcript_extract.py"), tp, out], check=True,
                   stdout=subprocess.DEVNULL)
    return B.read(out), served_models(tp), tp


def summary_table():
    rows = []
    if os.path.isdir(B.RET):
        for f in sorted(os.listdir(B.RET)):
            if f.startswith(("s81_1C_", "s81_1K_", "s81_1D_")) and f.endswith("receipt.json"):
                r = json.loads(B.read(os.path.join(B.RET, f)))
                if r.get("reader") != "sonnet subagent":
                    continue
                c = r["contamination"]
                res = ("cleared by the orchestrator" if r.get("cleared") else
                       "VOID" if r.get("void") else "INCOMPLETE" if r.get("failed") else "collected")
                rows.append("| %s | %s | %d | %s | %s | %s | %s | %s |" % (
                    r["s81_tag"], r["folder_tag"], r["attempt"], res,
                    "; ".join("%s: %s" % (w, l[:80]) for w, l in c["return_hits"]) or "none",
                    "yes" if c["transcript_checked"] else "NO",
                    "; ".join(c["transcript_hits"])[:300] or "none", ", ".join(r.get("served_models") or []) or "-"))
    head = ("# S81 Stage 1 - contamination check of the Sonnet testers' returns\n\n"
            "Written by `tools/s81_sonnet_collect.py`; one row per attempt judged. Void strings in a return: S81, S76, "
            "S75, R2 J (as written), prediction, O48 change (any case), quoted sentences of the agent's own brief "
            "left out. A run is also void if its tool-call extract touches any path outside its folder.\n\n"
            "| Call | Folder | Attempt | Result | Hits in the return | Transcript checked | Hits in the tool calls "
            "| Model as served |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    B.write(os.path.join(S1, "contamination.md"), head + "\n".join(rows) + "\n")


def clear(ft, reason):
    tag = ft.split("-")[0]
    s81tag = AGENTS[tag]
    k = 2 if ft.endswith("-2") else 1
    rp = os.path.join(B.RET, "%s.pass%d.receipt.json" % (s81tag, k))
    if not os.path.exists(rp):
        raise SystemExit("no failed receipt for %s attempt %d" % (s81tag, k))
    r = json.loads(B.read(rp))
    c = r["contamination"]
    if not r.get("void") or c["transcript_hits"] or not c["transcript_checked"] or not r["sentinel_present"] \
            or r["form_missing"] \
            or not r["brief_unchanged"] or any(w not in CLEARABLE for w, _ in c["return_hits"]):
        raise SystemExit("only a void whose sole hits are the word 'prediction', with a clean checked transcript and a "
                         "complete return, can be cleared")
    if os.path.exists(os.path.join(B.RET, s81tag + ".response.txt")):
        raise SystemExit(s81tag + " already has a collected return")
    mp = json.loads(B.read(MAP))
    at = mp[tag][str(k)]
    r.update(failed=False, void=False, cleared={"by": "orchestrator (decision S13)", "reason": reason,
                                                "at_unix": int(time.time())})
    shutil.copyfile(os.path.join(at["folder"], "return.md"), os.path.join(B.RET, s81tag + ".response.txt"))
    B.write(os.path.join(B.RET, s81tag + ".request.md"), B.read(at["prompt"]))
    B.write(os.path.join(B.RET, s81tag + ".receipt.json"), json.dumps(r, indent=1))
    os.replace(rp, rp.replace(".receipt.json", ".cleared.receipt.json"))
    print(s81tag, "cleared and collected (attempt %d)" % k)
    summary_table()


def main(a):
    if a[:1] == ["--clear"] and len(a) == 3:
        return clear(a[1], a[2])
    if "--transcripts" not in a and "--no-transcripts" not in a:
        raise SystemExit(__doc__)
    tdir = a[a.index("--transcripts") + 1] if "--transcripts" in a else None
    mp = json.loads(B.read(MAP))
    os.makedirs(B.RET, exist_ok=True)
    for tag, s81tag in AGENTS.items():
        p = lambda ext: os.path.join(B.RET, s81tag + ext)
        if os.path.exists(p(".response.txt")):
            print(tag, s81tag, "already collected")
            continue
        attempts = mp.get(tag, {})
        if not attempts:
            print(tag, s81tag, "not prepared")
            continue
        k = max(int(x) for x in attempts)
        at = attempts[str(k)]
        folder, ft = at["folder"], at["folder_tag"]
        rpath = os.path.join(folder, "return.md")
        if not os.path.exists(rpath):
            print(tag, s81tag, "attempt %d not yet run" % k)
            continue
        if os.path.exists(p(".pass%d.receipt.json" % k)) or os.path.exists(p(".pass%d.cleared.receipt.json" % k)):
            print(tag, s81tag, "attempt %d already judged" % k)
            continue
        ret = B.read(rpath)
        brief = B.read(os.path.join(folder, "brief.md"))
        brief_ok = sha(brief) == at["brief_sha256"]
        extra = sorted(set(os.listdir(folder)) - {"brief.md", "return.md"})
        rh = return_hits(ret, brief)
        th, tchecked, models, tpath = [], False, None, None
        if tdir:
            ex, models, tpath = extract(tdir, ft)
            if ex is None:
                print(tag, s81tag, "attempt %d: no transcript %s/%s.jsonl; not collected" % (k, tdir, ft))
                continue
            th, tchecked = tool_hits(ex, os.path.normpath(folder)), True
        missing = form_missing(s81tag, ret)
        done = complete(ret) and not missing
        void = bool(rh or th or not brief_ok)
        receipt = {"reader": "sonnet subagent", "s81_tag": s81tag, "agent": tag, "folder_tag": ft, "attempt": k,
                   "folder": folder, "prompt_sha256": at["prompt_sha256"], "brief_sha256": at["brief_sha256"],
                   "brief_unchanged": brief_ok, "other_files_in_folder": extra,
                   "response_sha256": sha(ret), "response_chars": len(ret), "sentinel_present": complete(ret),
                   "form_missing": missing,
                   "contamination": {"return_hits": rh, "transcript_checked": tchecked, "transcript_hits": th,
                                     "transcript": tpath},
                   "served_models": models, "served_model_is_sonnet": (any("sonnet" in m.lower() for m in models)
                                                                       if models else None),
                   "thinking": "as the agent runs (not switchable)", "temperature": "not settable",
                   "collected_at_unix": int(time.time())}
        if void or not done:
            receipt.update(failed=True, void=void)
            B.write(p(".pass%d.%s.txt" % (k, "void" if void else "truncated")), ret)
            B.write(p(".pass%d.receipt.json" % k), json.dumps(receipt, indent=1))
            why = ("void (%s)" % "; ".join([w for w, _ in rh] + th + ([] if brief_ok else ["brief.md changed"]))
                   if void else "incomplete (%s)" % ("no " + SENTINEL if not complete(ret) else
                                                   "form lacks " + ", ".join(missing[:8])))
            print(tag, s81tag, "attempt %d %s%s" % (k, why[:400], "; rerun once: s81_sonnet_prep.py --attempt 2 " + tag
                                                    if k == 1 else "; failed twice"))
            continue
        receipt["failed"] = False
        B.write(p(".request.md"), B.read(at["prompt"]))
        shutil.copyfile(rpath, p(".response.txt"))
        B.write(p(".receipt.json"), json.dumps(receipt, indent=1))
        print(tag, s81tag, "collected (attempt %d)%s%s" % (k, "" if tchecked else ", transcript NOT checked",
                                                           (", other files in folder: %s" % extra) if extra else ""))
    summary_table()


if __name__ == "__main__":
    main(sys.argv[1:])
