#!/usr/bin/env python3
"""S98 line-up checks (specification section 11). Python 3 standard library only.
Run from the line-up folder after scripts/build.py:
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/check.py
Reads the inputs and the outputs; the rerun check runs scripts/build.py once more and compares md5s.
Writes nothing of its own. Exit status 0 when every check passes.
"""
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import build  # noqa: E402

LINEUP = build.LINEUP
GROUPDIR = build.GROUPDIR

# spec section 3: units per group
UNITS_EXPECTED = {"G01": 46, "G02": 66, "G03": 56, "G04": 98, "G05": 68, "G06": 67, "G07": 48, "G08": 27,
                  "G09": 51, "G10": 80, "G11": 27, "G12": 35, "G13": 14, "G14": 55, "G15": 18}
# spec section 4.1: changes per group
CHANGES_EXPECTED = {"G01": 86, "G02": 52, "G03": 74, "G04": 118, "G05": 153, "G06": 143, "G07": 42, "G08": 37,
                    "G09": 65, "G10": 105, "G11": 77, "G12": 50, "G13": 22, "G14": 116, "G15": 89, "G16": 46}
# spec section 4.2: units touched, full, pointer lines, vocabulary lines, records in blocks
TABLE_42 = {
    "G01": (29, 62, 2, 37, 52), "G02": (27, 51, 28, 24, 7), "G03": (39, 80, 1, 50, 25),
    "G04": (68, 139, 17, 85, 34), "G05": (52, 130, 15, 81, 42), "G06": (61, 157, 107, 157, 23),
    "G07": (32, 55, 4, 25, 2), "G08": (21, 44, 9, 37, 4), "G09": (40, 70, 9, 48, 1),
    "G10": (49, 119, 9, 59, 34), "G11": (26, 81, 6, 46, 29), "G12": (23, 49, 6, 16, 12),
    "G13": (7, 16, 0, 11, 22), "G14": (50, 141, 24, 144, 19), "G15": (16, 115, 12, 43, 3),
}
G16_EXPECTED = {"full": 88, "pointer": 1, "full_vocab_with_sentences": 80, "full_no_sentence": 8}
TOTALS = {"full": 1309, "pointer": 249, "term_lines": 863, "term_records": 224, "blocks": 309,
          "section_blocks": 96, "rest_blocks": 213}

# spec section 10: the word list (quoted data, for this check only)
WORDS = ["fits", "supports", "supported", "verifies", "verified", "corroborates", "corroborated", "proves",
         "proved", "disproves", "disproved", "reason to believe", "reason to reject", "better than",
         "worse than", "true", "not true", "more true", "established", "authority", "foundation",
         "foundational", "derived", "derived from", "prove", "proven", "proving"]
STEMS = ["belie", "justif", "verif", "confirm", "corroborat", "rank", "authorit", "foundation", "better", "worse",
         "best", "proof", "support"]

FAILS = []


def fail(msg):
    FAILS.append(msg)
    print("FAIL: " + msg)


def ok(msg):
    print("ok: " + msg)


def md5_file(p):
    with open(p, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def outputs():
    out = []
    for root, dirs, files in os.walk(LINEUP):
        dirs.sort()
        rel = os.path.relpath(root, LINEUP)
        if rel.split(os.sep)[0] == "scripts":
            continue
        for fn in sorted(files):
            out.append(os.path.normpath(os.path.join(rel, fn)))
    return sorted(out)


def read(rel):
    with open(os.path.join(LINEUP, rel), encoding="utf-8") as f:
        return f.read()


def word_hits(text):
    hits = []
    low = text.lower()
    for w in WORDS:
        for m in re.finditer(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
            hits.append(w)
    for s in STEMS:
        for m in re.finditer(r"(?<![a-z])" + re.escape(s), low):
            hits.append(s)
    return hits


def blockquote_lines(text):
    return "\n".join(("> " + l) if l != "" else ">" for l in text.split("\n"))


def main():
    # 1. md5s
    for name, m in build.INPUTS:
        got = md5_file(os.path.join(GROUPDIR, name))
        if got != m:
            fail("md5 of {} is {}".format(name, got))
    ok("1. md5s of the five inputs checked")

    # 2. records.jsonl
    with open(os.path.join(GROUPDIR, "anchored.jsonl"), encoding="utf-8") as f:
        a_lines = f.read().split("\n")[:-1]
    r_lines = read("data/records.jsonl").split("\n")
    if r_lines[-1] != "":
        fail("records.jsonl does not end with a newline")
    r_lines = r_lines[:-1]
    if len(r_lines) != 1850:
        fail("records.jsonl has {} lines".format(len(r_lines)))
    recs = [json.loads(l) for l in r_lines]
    anch = [json.loads(l) for l in a_lines]
    if len({r["rid"] for r in recs}) != 1850:
        fail("records.jsonl rids not distinct")
    for al, rl, a, r in zip(a_lines, r_lines, anch, recs):
        if list(r.items())[:len(a)] != list(a.items()):
            fail("fields differ for " + a["rid"])
        if not rl.startswith(al[:-1] + ", "):
            fail("bytes of the first fields differ for " + a["rid"])
    ok("2. records.jsonl: {} lines, distinct rids, first fields equal anchored.jsonl".format(len(recs)))
    R = {r["rid"]: r for r in recs}

    # 3. units once
    tree = json.loads(read("data/tree.json"))
    with open(os.path.join(GROUPDIR, "sentence index of the latest text.jsonl"), encoding="utf-8") as f:
        units = [json.loads(l) for l in f if l.strip()]
    uids = [u["id"] for u in units]
    seen = {}
    unit_group = {}
    for g in tree["groups"]:
        if g["id"] == "G16":
            continue
        n = 0
        for s in g["sections"]:
            for u in s["units"]:
                seen[u["id"]] = seen.get(u["id"], 0) + 1
                unit_group[u["id"]] = g["id"]
                n += 1
        if n != UNITS_EXPECTED[g["id"]]:
            fail("{} has {} units, expected {}".format(g["id"], n, UNITS_EXPECTED[g["id"]]))
    if set(seen) != set(uids) or any(v != 1 for v in seen.values()):
        fail("units not each shown once")
    ukey = {u["id"]: (u["line"], u["n"]) for u in units}
    utext = {u["id"]: u["text"] for u in units}
    for g in tree["groups"]:
        for s in g.get("sections", []):
            for u in s["units"]:
                if u["text"] != utext[u["id"]]:
                    fail("unit text differs " + u["id"])
            ids = [u["id"] for u in s["units"]]
            if ids != sorted(ids, key=lambda x: ukey[x]):
                fail("units out of text order in " + s["id"])
    anchors_units = 0
    for g in build.GROUP_IDS[:-1]:
        t = read(build.GROUP_FILE[g])
        anchors_units += len(re.findall(r'<a id="L\d+-s\d+"></a>', t))
    if anchors_units != 756:
        fail("unit anchors in group files: {}".format(anchors_units))
    ok("3. every one of the {} units appears once over G01–G15; per-group counts equal section 3".format(len(uids)))

    # 4. showings
    show = {rid: {"full": [], "pointer": [], "term line": [], "block": 0, "g16 full": 0, "g16 pointer": 0,
                  "block_where": None} for rid in R}
    per = {g: {"touched": 0, "full": 0, "pointer": 0, "term": 0, "blocks": 0} for g in build.GROUP_IDS}
    sec_blocks = rest_blocks = 0
    for g in tree["groups"]:
        gid = g["id"]
        if gid == "G16":
            for c in g["changes"]:
                for x in c["records"]:
                    show[x["rid"]]["g16 " + x["display"]] += 1
            continue
        for s in g["sections"]:
            for u in s["units"]:
                if u["entries"]:
                    per[gid]["touched"] += 1
                for e in u["entries"]:
                    for x in e["records"]:
                        if R[x["rid"]]["change_id"] != e["change_id"]:
                            fail("record {} under change {}".format(x["rid"], e["change_id"]))
                        show[x["rid"]][x["display"]].append(u["id"])
                        per[gid]["full" if x["display"] == "full" else ("pointer" if x["display"] == "pointer" else "term")] += 1
            for e in s["block"]:
                for x in e["records"]:
                    show[x]["block"] += 1
                    show[x]["block_where"] = s["id"]
                    per[gid]["blocks"] += 1
                    sec_blocks += 1
        for rb in g["rest"]:
            for e in rb["changes"]:
                for x in e["records"]:
                    show[x]["block"] += 1
                    show[x]["block_where"] = "rest-" + rb["part_key"]
                    per[gid]["blocks"] += 1
                    rest_blocks += 1
    place = {}
    with open(os.path.join(GROUPDIR, "proposal by place - scripts/assignment.jsonl"), encoding="utf-8") as f:
        for l in f:
            if l.strip():
                p = json.loads(l)
                place[p["change_id"]] = p
    with open(os.path.join(GROUPDIR, "proposal by place - scripts/sections.json"), encoding="utf-8") as f:
        sections = json.load(f)
    secpair = {tuple(s["section"]): s for s in sections}

    def sec_of_unit(uid):
        line = ukey[uid][0]
        hits = [s for s in sections if s["first_line"] <= line <= s["last_line"]]
        return tuple(hits[0]["section"])

    n_err = 0
    counts = {"full": 0, "pointer": 0, "term_lines": 0, "term_records": 0, "g16_full_vs": 0, "g16_full_ns": 0,
              "g16_pointer": 0}
    for rid, r in R.items():
        sh = show[rid]
        sents = r["latest_sentences"]
        vocab = r["scope"] in ("term", "whole text")
        p = place[r["change_id"]]
        in16 = p["group"][0] == "ALL"
        bad = False
        if sents and not vocab:
            if len(sh["full"]) != 1 or sorted(sh["full"] + sh["pointer"]) != sorted(sents) or sh["term line"] or sh["block"]:
                bad = True
            else:
                home = sh["full"][0]
                insec = [x for x in sorted(sents, key=lambda x: ukey[x]) if sec_of_unit(x) == tuple(p["section"])]
                want = insec[0] if insec else sorted(sents, key=lambda x: ukey[x])[0]
                if home != want or r["lineup_home_sentence"] != home:
                    bad = True
            if sh["g16 pointer"] != (1 if in16 else 0) or sh["g16 full"]:
                bad = True
            counts["full"] += 1
            counts["pointer"] += len(sh["pointer"])
            counts["g16_pointer"] += sh["g16 pointer"]
        elif sents and vocab:
            if sorted(sh["term line"]) != sorted(sents) or sh["full"] or sh["pointer"] or sh["block"]:
                bad = True
            if sh["g16 full"] != (1 if in16 else 0) or sh["g16 pointer"]:
                bad = True
            counts["term_lines"] += len(sh["term line"])
            counts["term_records"] += 1
            counts["g16_full_vs"] += sh["g16 full"]
        else:
            if in16:
                if sh["g16 full"] != 1 or sh["block"] or sh["g16 pointer"]:
                    bad = True
                counts["g16_full_ns"] += 1
            else:
                if sh["block"] != 1 or sh["g16 full"] or sh["g16 pointer"]:
                    bad = True
                want = ("sec-L{}-{}".format(secpair[tuple(p["section"])]["first_line"], secpair[tuple(p["section"])]["last_line"])
                        if tuple(p["section"]) in secpair else "rest-" + p["section"][0])
                if sh["block_where"] != want:
                    bad = True
            if sh["full"] or sh["pointer"] or sh["term line"]:
                bad = True
        if bad:
            n_err += 1
            if n_err <= 10:
                fail("showings of {} do not follow section 4.2".format(rid))
    for g, (t, fu, po, te, bl) in TABLE_42.items():
        got = per[g]
        if (got["touched"], got["full"], got["pointer"], got["term"], got["blocks"]) != (t, fu, po, te, bl):
            fail("{} figures {} differ from the section 4.2 table {}".format(
                g, (got["touched"], got["full"], got["pointer"], got["term"], got["blocks"]), (t, fu, po, te, bl)))
    chg = {}
    for r in recs:
        chg[r["change_id"]] = r["lineup_change_group"]
    for g, n in CHANGES_EXPECTED.items():
        got = sum(1 for v in chg.values() if v == g)
        if got != n:
            fail("{} has {} changes, expected {}".format(g, got, n))
    g16full = sum(show[x]["g16 full"] for x in R)
    if (g16full, counts["g16_pointer"], counts["g16_full_vs"], counts["g16_full_ns"]) != (
            G16_EXPECTED["full"], G16_EXPECTED["pointer"], G16_EXPECTED["full_vocab_with_sentences"], G16_EXPECTED["full_no_sentence"]):
        fail("G16 figures differ")
    tot = (counts["full"], counts["pointer"], counts["term_lines"], counts["term_records"], sec_blocks + rest_blocks, sec_blocks, rest_blocks)
    want = tuple(TOTALS[k] for k in ("full", "pointer", "term_lines", "term_records", "blocks", "section_blocks", "rest_blocks"))
    if tot != want:
        fail("totals {} differ from {}".format(tot, want))
    if counts["full"] + counts["term_records"] + sec_blocks + rest_blocks + counts["g16_full_ns"] != 1850:
        fail("records do not add up to 1850")
    # the same showings, counted in the markdown group files
    exp_md = {}
    for g in tree["groups"]:
        f = g["file"]
        if g["id"] == "G16":
            for c in g["changes"]:
                for x in c["records"]:
                    exp_md[(f, x["rid"], x["display"] == "pointer")] = exp_md.get((f, x["rid"], x["display"] == "pointer"), 0) + 1
            continue
        for s in g["sections"]:
            for u in s["units"]:
                for e in u["entries"]:
                    for x in e["records"]:
                        k = (f, x["rid"], x["display"] == "pointer")
                        exp_md[k] = exp_md.get(k, 0) + 1
            for e in s["block"]:
                for x in e["records"]:
                    exp_md[(f, x, False)] = exp_md.get((f, x, False), 0) + 1
        for rb in g["rest"]:
            for e in rb["changes"]:
                for x in e["records"]:
                    exp_md[(f, x, False)] = exp_md.get((f, x, False), 0) + 1
    got_md = {}
    pat = re.compile(r"^\s*- \*\*([A-E]-\d+)\*\* · ")
    for g in build.GROUP_IDS:
        f = build.GROUP_FILE[g]
        for line in read(f).split("\n"):
            m = pat.match(line)
            if not m:
                continue
            r = R[m.group(1)]
            ptr_prefix = "**{}** · {} · {} · {} · shown in full under [".format(r["rid"], r["round"], r["kind"], r["status"])
            is_ptr = line.lstrip()[2:].startswith(ptr_prefix)
            k = (f, r["rid"], is_ptr)
            got_md[k] = got_md.get(k, 0) + 1
    if got_md != exp_md:
        diff = [k for k in set(got_md) | set(exp_md) if got_md.get(k) != exp_md.get(k)]
        fail("record lines in the group files differ from tree.json at {} places, e.g. {}".format(len(diff), sorted(diff)[:3]))
    csv_rows = list(csv.reader(open(os.path.join(LINEUP, "data/by sentence.csv"), encoding="utf-8", newline="")))
    if csv_rows[0] != build.CSV_COLUMNS or len(csv_rows[0]) != 29:
        fail("csv header")
    if len(csv_rows) - 1 != sum(exp_md.values()):
        fail("csv rows {} differ from showings {}".format(len(csv_rows) - 1, sum(exp_md.values())))
    for row in csv_rows[1:]:
        r = R[row[10]]
        if row[8] != "pointer" and (row[21], row[22], row[23], row[24]) != (r["old"], r["new"], r["old_sentence"], r["new_sentence"]):
            fail("csv wording differs for " + row[10])
            break
    ok("4. every record's showings follow section 4.2; per-group figures equal the table; "
       "full {}, pointer {} (+{} in G16), vocabulary lines {} ({} records), blocks {} ({} + {}), G16 in full {}; "
       "markdown record lines and {} csv rows agree".format(
           counts["full"], counts["pointer"], counts["g16_pointer"], counts["term_lines"], counts["term_records"],
           sec_blocks + rest_blocks, sec_blocks, rest_blocks, g16full, len(csv_rows) - 1))

    # 5. wording shown byte for byte
    stripped = {}
    for g in build.GROUP_IDS:
        f = build.GROUP_FILE[g]
        stripped[f] = "\n".join(l.lstrip(" ") for l in read(f).split("\n"))
    A = {a["rid"]: a for a in anch}
    nchk = 0
    for (f, rid, is_ptr), n in exp_md.items():
        if is_ptr:
            continue
        a = A[rid]
        before = a["old_sentence"] if a["old_sentence"] != "" else a["old"]
        after = a["new_sentence"] if a["new_sentence"] != "" else a["new"]
        texts = [before, after]
        if a["old_sentence"] != "" and a["old"] != "" and a["old_sentence"] != a["old"]:
            texts.append(a["old"])
        if a["new_sentence"] != "" and a["new_sentence"] != a["new"]:
            texts.append(a["new"])
        for t in texts:
            if t == "":
                continue
            nchk += 1
            if blockquote_lines(t) not in stripped[f]:
                fail("wording of {} not found in {}".format(rid, f))
    ok("5. {} wording texts found byte for byte, as blockquotes, in the files where they are shown".format(nchk))

    # 6. links and anchors
    md_files = [o for o in outputs() if o.endswith(".md")]
    anchors = {}
    for f in md_files:
        ids = re.findall(r'<a id="([^"]+)"></a>', read(f))
        if len(ids) != len(set(ids)):
            fail("duplicate anchors in " + f)
        anchors[f] = set(ids)
    nlinks = 0
    for f in md_files:
        for m in re.finditer(r"\]\(([^)\s]+)\)", read(f)):
            tgt = m.group(1)
            if re.match(r"^[a-z]+:", tgt):
                continue
            path, _, anc = tgt.partition("#")
            path = urllib.parse.unquote(path)
            dest = f if path == "" else os.path.normpath(os.path.join(os.path.dirname(f), path))
            nlinks += 1
            if dest not in anchors and not os.path.exists(os.path.join(LINEUP, dest)):
                fail("link to missing file {} in {}".format(tgt, f))
                continue
            if anc and anc not in anchors.get(dest, set()):
                fail("link to missing anchor {} in {}".format(tgt, f))
    ok("6. {} relative links resolve, with their anchors; anchors unique in each file".format(nlinks))

    # 7. word scan of the builder's own words and the index prose
    fixed = []
    for v in build.TEXT.values():
        fixed.extend(v if isinstance(v, list) else [v])
    hits = []
    for s in fixed:
        hits += word_hits(s)
    prose = [l for l in read("index.md").split("\n") if not l.startswith("|")]
    for l in prose:
        hits += word_hits(l)
    if hits:
        fail("word scan: " + ", ".join(sorted(set(hits))))
    ok("7. word scan of {} fixed strings and {} index prose lines: nothing found".format(len(fixed), len(prose)))

    # 8. rerun gives the same bytes
    before = {o: md5_file(os.path.join(LINEUP, o)) for o in outputs()}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    subprocess.run([sys.executable, os.path.join(HERE, "build.py")], check=True, env=env,
                   stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    after = {o: md5_file(os.path.join(LINEUP, o)) for o in outputs()}
    if before != after:
        fail("rerun changed: " + ", ".join(o for o in sorted(set(before) | set(after)) if before.get(o) != after.get(o)))
    ok("8. a second run gives the same bytes for all {} outputs".format(len(after)))

    if FAILS:
        print("{} check(s) failed".format(len(FAILS)))
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
