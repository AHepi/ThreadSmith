"""Collector D: checks on 'collector D.jsonl' (reads only; prints a report).

1. shape: every record has the 16 fields; rids unique; same_as points at existing rids.
2. every 'old' of an applied record is found verbatim in its target text (at target_line when given);
   term records (vocabulary cells) are reported apart: their cells are descriptions, so only their
   quoted fragments are looked for.
3. every old_sentence is verbatim in the target text; every edit's new_sentence is verbatim in the text
   the edit produced (stage texts rebuilt in memory).
4. counts by kind, status, round and source file.
"""
import collections, itertools, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edits
from lib import *

OUT = "/home/user/ThreadSmith/Semantics/results/S98 Ledger of edits and recommendations/collect/collector D.jsonl"
FIELDS = ["rid", "round", "source_file", "source_ref", "kind", "status", "applied_in", "target_text",
          "target_line", "target_part", "old", "new", "old_sentence", "new_sentence", "scope", "same_as"]


def main():
    R = [json.loads(l) for l in open(OUT, encoding="utf-8")]
    c = itertools.count(1)
    _, _, T = edits.build(lambda: "x-%d" % next(c))
    texts = {k: T[k] for k in TEXTS}
    texts[STAGE1_NAME] = T["stage1"]
    after = {"draft 5": "scrubbed copy", "scrubbed copy": None, STAGE1_NAME: "repaired copy",
             "repaired copy": "latest text"}
    rep = collections.OrderedDict()
    # 1. shape
    bad = [r["rid"] for r in R if list(r.keys()) != FIELDS]
    rids = [r["rid"] for r in R]
    dup = [k for k, v in collections.Counter(rids).items() if v > 1]
    known = set(rids)
    dangling = [(r["rid"], s) for r in R for s in r["same_as"] if s not in known]
    rep["records"] = len(R)
    rep["records with wrong field order or set"] = bad
    rep["duplicate rids"] = dup
    rep["same_as pointing nowhere"] = dangling
    rep["records with an empty target_part"] = [r["rid"] for r in R if not r["target_part"]]
    # 2. old verbatim
    misses, term_notes, checked = [], [], 0
    for r in R:
        if r["status"] != "applied" or not r["old"]:
            continue
        lines = texts.get(r["target_text"])
        if lines is None:
            misses.append((r["rid"], "unknown target text", r["target_text"]))
            continue
        if r["scope"] == "term":
            # a vocabulary cell: look for each of its words or quoted phrases in draft 5 (case and
            # the \( \) markup ignored); a cell names draft 5's words, so draft 5 is searched
            cell = re.sub(r"\((?:[^()]|\([^()]*\))*\)", " ", r["old"])
            quoted = re.findall(r"\"([^\"]{3,})\"", cell)
            bare = re.sub(r"\"[^\"]*\"", ";", cell)
            toks = [x for q in quoted for x in re.split(r"…|\.\.\.", q)]
            toks += re.split(r"[;,]| or | and |/|→", bare)
            toks = [re.sub(r"\*|\bl\.\s*[\d, –-]+|\bheading\b|\beverywhere\b|\bas mathematics\b", "", t).strip(" .:'") for t in toks]
            toks = [t for t in toks if len(t) >= 3 and not re.fullmatch(r"[\d ,–-]+", t)]
            whole = re.sub(r"\\\(|\\\)|\*", "", "\n".join(texts["draft 5"])).lower()
            miss = [t for t in toks if t.lower() not in whole]
            if miss:
                term_notes.append((r["rid"], r["source_file"].split(" - ")[-1], "not found in draft 5: " + " | ".join(m[:45] for m in miss)))
            continue
        checked += 1
        if r["target_line"]:
            ok = r["old"] in lines[r["target_line"] - 1] or r["old"] in "\n".join(
                lines[r["target_line"] - 1:r["target_line"] + 6])
        else:
            ok = r["old"] in "\n".join(lines)
        if not ok:
            misses.append((r["rid"], r["kind"], r["source_file"].split("/")[-1][:50], r["target_line"], r["old"][:90]))
    rep["applied records whose old was checked (non-term)"] = checked
    rep["applied records whose old is NOT verbatim in the target text"] = misses
    rep["applied term records: quoted fragments not found in draft 5"] = term_notes
    # 3. sentences
    s_miss, ns_miss = [], []
    for r in R:
        lines = texts.get(r["target_text"])
        if r["old_sentence"] and lines is not None:
            if r["old_sentence"] not in "\n".join(lines):
                s_miss.append((r["rid"], r["kind"], r["old_sentence"][:70]))
        if r["kind"] == "edit" and r["scope"] != "term" and r["new_sentence"]:
            a = after.get(r["target_text"])
            res = texts[a] if a else texts["scrubbed copy"]
            if r["target_text"] == "draft 5":
                res = texts["scrubbed copy"]
            if r["target_text"] == "scrubbed copy":
                res = texts[STAGE1_NAME]
            if r["new_sentence"] not in "\n".join(res):
                ns_miss.append((r["rid"], r["new_sentence"][:70]))
    rep["old_sentence not verbatim in target text"] = s_miss
    rep["edit new_sentence not verbatim in the text it produced"] = ns_miss
    # 4. counts
    rep["by kind"] = dict(collections.Counter(r["kind"] for r in R))
    rep["by status"] = dict(collections.Counter(r["status"] for r in R))
    rep["by kind and status"] = {"%s / %s" % k: v for k, v in sorted(collections.Counter((r["kind"], r["status"]) for r in R).items())}
    rep["by round"] = dict(collections.Counter(r["round"] for r in R))
    rep["by scope"] = dict(collections.Counter(r["scope"] for r in R))
    rep["by source file"] = {k: v for k, v in sorted(collections.Counter(r["source_file"] for r in R).items())}
    rep["by source file and status"] = {"%s :: %s" % k: v for k, v in sorted(collections.Counter((r["source_file"].split("/")[-1], r["status"]) for r in R).items())}
    rep["recommendations with no same_as"] = [r["rid"] for r in R if r["kind"] == "recommendation" and not r["same_as"] and r["scope"] != "term"]
    rep["records with no old_sentence (non-term)"] = len([r for r in R if r["scope"] != "term" and not r["old_sentence"]])
    rep["records with no new_sentence (non-term)"] = len([r for r in R if r["scope"] != "term" and not r["new_sentence"]])
    # stage-3 entries a reply record links to
    s3 = [r for r in R if r["source_file"].endswith("replacements_stage3.json")]
    linked = set(s for r in R if "response.txt" in r["source_file"] for s in r["same_as"])
    rep["stage-3 edits (group X, from the replies) with no reply record linked"] = [
        (r["rid"], r["source_ref"][:80]) for r in s3 if "group X" in r["source_ref"] and r["rid"] not in linked]
    s1 = [r for r in R if r["source_file"].endswith("S96 Repair - scripts/replacements.json")]
    linked95 = set(s for r in R if r["round"] == "S95" and r["kind"] == "recommendation" for s in r["same_as"])
    rep["stage-1 edits of group R with no S95 recommendation linked"] = [
        (r["rid"], r["source_ref"][:80]) for r in s1 if "group R" in r["source_ref"] and r["rid"] not in linked95]
    s2 = [r for r in R if r["source_file"].endswith("replacements_stage2.json")]
    linked96 = set(s for r in R if "S96 Check" in r["source_file"] for s in r["same_as"])
    rep["stage-2 edits of groups W/K with no check recommendation linked"] = [
        (r["rid"], r["source_ref"][:80]) for r in s2 if ("group W" in r["source_ref"] or "group K" in r["source_ref"]) and r["rid"] not in linked96]
    print(json.dumps(rep, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
