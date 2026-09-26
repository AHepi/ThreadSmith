"""Collector D, part 4: the repairs proposed in S96 and the wordings the outside replies proposed.

(a) results/S96 Check of the repaired copy - whole text.md, section 5 (W): parsed by program
    ('Replace "…" with:\\n> …', 'After "…" add:\\n> …'); target text: the stage-1 text; status from
    replacements_stage2.json (entries' ref, and its not_applied list).
(b) results/S96 Check of the repaired copy - cases.md, 'Repairs proposed' (K).
(c) the six replies (results/S96 Cross-examination - repaired copy - returns/*.response.txt): every
    code block of a finding, and every wording given inline; target text: the repaired copy; status as
    results/S96 Reading of the replies.md ruled (FIX taken as worded or close -> applied; FIX in other
    words -> superseded; KEEP or a part not taken up -> declined; left for a later revision -> not applied).
    Where a reply gives no old wording, the replaced sentence(s) are found in the repaired copy by
    similarity near the cited line (difflib), and recorded as old/old_sentence with the ratio in the build
    report.
"""
import difflib, re
from reclib import *

WF = "results/S96 Check of the repaired copy - whole text.md"
KF = "results/S96 Check of the repaired copy - cases.md"
RD = "results/S96 Cross-examination - repaired copy - returns/"
READING = "results/S96 Reading of the replies.md"
A, S, D, N, O = "applied", "superseded", "declined", "not applied", "open for the owner"

# (item id, sub-proposal index) -> (status, stage-2 entries)
WMAP = {
    ("R-1", 0): (A, [8]), ("R-1", 1): (A, [12]), ("R-2", 0): (A, [27]), ("R-3", 0): (A, [3]),
    ("R-4", 0): (A, [18]), ("R-5", 0): (A, [14]), ("R-6", 0): (A, [1]),
    ("P-1", 0): (D, []), ("P-1", 1): (A, [10]), ("P-2", 0): (A, [4]), ("P-2", 1): (A, [6]),
    ("P-3", 0): (A, [23]), ("B-1", 0): (A, [15]), ("B-1", 1): (A, [24]), ("B-1", 2): (A, [9]),
    ("B-2", 0): (A, [12]), ("B-2", 1): (A, [25]), ("B-3", 0): (A, [19]), ("B-3", 1): (A, [20]),
    ("B-4", 0): (A, [20]), ("B-5", 0): (A, [2]), ("B-6", 0): (A, [7]), ("B-7", 0): (A, [10]),
    ("O-1", 0): (A, [5]), ("O-1", 1): (A, [5]), ("O-1", 2): (A, [22]), ("O-2", 0): (A, [16]),
    ("O-3", 0): (A, [17]), ("O-4", 0): (A, [13]), ("O-5", 0): (A, [21]), ("O-6", 0): (A, [11]),
}

# replies: (file tag, finding label, block number or None, reading ruling id, hint line, status,
#           stage-3 ruling ids to link, inline spec or None)
# inline spec: dict(old=..., new=... or new_between=(start, end), anchor=...)
REPLIES = [
 ("atria_A", "finding 1", 1, "atria A 1, glm A 2, mimo 3 5", 329, A, ["atria A 1"], None),
 ("atria_A", "finding 2", 2, "atria A 2", 325, S, ["atria A 2"], None),
 ("atria_A", "finding 3", 3, "atria A 3", 47, S, ["atria A 3"], None),
 ("atria_A", "finding 4", 4, "atria A 4 (joined with mimo 1 4)", 61, A, ["atria A 4"], None),
 ("atria_A", "finding 4", 5, "atria A 4 at L339", 339, A, ["atria A 4"], None),
 ("atria_A", "finding 5", 6, "atria A 5", 299, D, [], None),
 ("atria_A", "finding 6", 7, "mimo 2 6 and atria A 6", 231, S, ["atria A 6"], None),
 ("glm_A", "finding 1", 1, "glm A 1", 233, A, ["glm A 1"], None),
 ("glm_A", "finding 1", 2, "glm A 1", 236, A, ["glm A 1"], None),
 ("glm_A", "finding 2", 3, "atria A 1, glm A 2, mimo 3 5", 329, A, ["glm A 2"], None),
 ("glm_A", "finding 3", 4, "glm A 3", 53, S, ["glm A 3"], None),
 ("mimo_1", "finding 1", 1, "mimo 1 1 (joined with mimo 4 F3 (ii))", 17, S, ["mimo 1 1"], None),
 ("mimo_1", "finding 2", 2, "mimo 1 2", 147, D, [], None),
 ("mimo_1", "finding 2", 3, "mimo 1 2", 155, D, [], None),
 ("mimo_1", "finding 3", 4, "mimo 1 3", 31, D, [], None),
 ("mimo_1", "finding 3", 5, "mimo 1 3", 43, A, ["mimo 1 3"], None),
 ("mimo_1", "finding 3", 6, "mimo 1 3", 159, A, ["mimo 1 3"], None),
 ("mimo_1", "finding 3 (L257)", None, "mimo 1 3", 257, A, ["mimo 1 3"],
  dict(old="", new="[no wording given] The same words stand at L257 (\"The contract \\(C\\) is a declared subset of the edits the target admits\") and must change with them.")),
 ("mimo_1", "finding 4", 7, "atria A 4, L61, L339, L536-L544; joined with mimo 1 4", 61, D, [], None),
 ("mimo_1", "finding 4 (Part XV)", None, "atria A 4; joined with mimo 1 4", 536, D, [],
  dict(old="", new="[no wording given] Part XV must carry the same labels (P1)–(P5).")),
 ("mimo_1", "finding 5", 8, "mimo 1 5", 141, D, [], None),
 ("mimo_1", "finding 5", 9, "mimo 1 5", 151, S, ["mimo 1 5"], None),
 ("mimo_1", "finding 6", 10, "mimo 1 6", 109, S, ["mimo 1 6"], None),
 ("mimo_1", "finding 7", 11, "mimo 1 7", 105, S, ["mimo 1 7"], None),
 ("mimo_1", "finding 7", 12, "mimo 1 7", 49, S, ["mimo 1 7"], None),
 ("mimo_1", "finding 8", 13, "mimo 1 8", 15, S, ["mimo 1 8"], None),
 ("mimo_1", "finding 9 (a), L11", None, "mimo 1 9 (a)", 11, D, [],
  dict(old="(Part II, Argument 1)", new_between=('Write "', '" and "(Part III'))),
 ("mimo_1", "finding 9 (a), L15", None, "mimo 1 9 (a)", 15, D, [],
  dict(old="(Part III, Argument 5)", new_between=('" and "', '"; likewise'))),
 ("mimo_1", "finding 9 (a), L315", None, "mimo 1 9 (a)", 315, D, [],
  dict(old="", new_between=('likewise "', '" at L315'))),
 ("mimo_1", "finding 9 (b), L119-L120", None, "mimo 1 9 (b)", 119, S, ["mimo 1 9 (b)"],
  dict(old="", locate="\\(t=(\\pi,\\tau,\\sigma,\\lambda)\\)", new_between=('glosses only three: write "', '" (c)'))),
 ("mimo_1", "finding 9 (c), L31, first option", None, "mimo 1 9 (c)", 31, D, [],
  dict(old="(EX) is a defined relation of an episode, not such a predicate", new_between=('either "', '" at L31'))),
 ("mimo_1", "finding 9 (c), second option (at L43, L49, L69)", None, "mimo 1 9 (c)", 43, D, [],
  dict(old="(E)", new="(EX)", noplace=True)),
 ("mimo_1", "finding 9 (d), L257", None, "mimo 1 9 (d)", 257, D, [],
  dict(old="the active commitments", new="the active components")),
 ("mimo_2", "finding 1", 1, "mimo 2 1", 255, S, ["mimo 2 1"], None),
 ("mimo_2", "finding 2", 2, "mimo 2 2", 317, S, ["mimo 2 2"], None),
 ("mimo_2", "finding 2, note on '(Part VIII)'", None, "mimo 2 remarks under Q5", 317, D, [],
  dict(old="", new_between=('(Keep "(Part VIII)"', '; it is stated'), prefix='[no wording given] Keep "(Part VIII)"')),
 ("mimo_2", "finding 3", 3, "mimo 2 3", 245, S, ["mimo 2 3"], None),
 ("mimo_2", "finding 4", 4, "mimo 2 4", 197, A, ["mimo 2 4"], None),
 ("mimo_2", "finding 4", 5, "mimo 2 4", 211, A, ["mimo 2 4"], None),
 ("mimo_2", "finding 5", 6, "mimo 2 5", 193, A, ["mimo 2 5"], None),
 ("mimo_2", "finding 5", 7, "mimo 2 5", 205, A, ["mimo 2 5"], None),
 ("mimo_2", "finding 6", 8, "mimo 2 6 and atria A 6", 287, S, ["mimo 2 6"],
  dict(old="", anchor="the commitments of \\(E|W\\) are \\(W\\).", block=8)),
 ("mimo_2", "finding 6", 9, "mimo 2 6 and atria A 6", 299, S, ["mimo 2 6"],
  dict(old="", anchor="For a declared family \\(\\mathcal V\\) of organization edits,", block=9)),
 ("mimo_2", "finding 6 (L257)", None, "mimo 2 6 and atria A 6", 257, A, ["mimo 2 6"],
  dict(old_between=('at L257 replace "', '" with "'), new_between=('" with "admits', '".\n'), new_prefix="admits")),
 ("mimo_2", "finding 7", 10, "mimo 2 7", 305, A, ["mimo 2 7"], None),
 ("mimo_2", "finding 8", 11, "mimo 2 8", 311, A, ["mimo 2 8"], None),
 ("mimo_3", "finding 1", 1, "mimo 3 1", 375, A, ["mimo 3 1"], None),
 ("mimo_3", "finding 1", 2, "mimo 3 1", 377, A, ["mimo 3 1"], None),
 ("mimo_3", "finding 1", 3, "mimo 3 1", 387, A, ["mimo 3 1"], None),
 ("mimo_3", "finding 1", 4, "mimo 3 1", 421, A, ["mimo 3 1"], None),
 ("mimo_3", "finding 1", 5, "mimo 3 1", 446, S, ["mimo 3 1"], None),
 ("mimo_3", "finding 1", 6, "mimo 3 1", 453, S, ["mimo 3 1"], None),
 ("mimo_3", "finding 2", 7, "mimo 3 2", 413, S, ["mimo 3 2"], None),
 ("mimo_3", "finding 3", 8, "mimo 3 3", 369, A, ["mimo 3 3"], None),
 ("mimo_3", "finding 4", 9, "mimo 3 4", 455, A, ["mimo 3 4"], None),
 ("mimo_3", "finding 5", 10, "atria A 1, glm A 2, mimo 3 5", 329, A, ["mimo 3 5"], None),
 ("mimo_3", "finding 6", 11, "mimo 3 6", 339, A, ["mimo 3 6"], None),
 ("mimo_3", "finding 6", 12, "mimo 3 6", 347, D, [], None),
 ("mimo_3", "finding 6, conditional alternative", None, "mimo 3 6", 339, D, [],
  dict(old="", new_between=('(If Part II prints labels for these conditions, use ', '; as printed'))),
 ("mimo_4", "F1", 1, "mimo 4 F1", 596, A, ["mimo 4 F1"], None),
 ("mimo_4", "F1 (L520)", None, "mimo 4 F1", 520, A, ["mimo 4 F1"],
  dict(old="", new_between=('(and at L520: "', '")'))),
 ("mimo_4", "F2", 2, "mimo 4 F2", 568, S, ["mimo 4 F2"], None),
 ("mimo_4", "F3 (i)", None, "mimo 4 F3", 536, S, ["mimo 4 F3"],
  dict(old="with a non-declared transport,", new="")),
 ("mimo_4", "F3 (ii)", 3, "mimo 4 F3 (with mimo 1 1)", 538, S, ["mimo 4 F3 (ii)"], None),
 ("mimo_4", "F4", 4, "mimo 4 F4", 580, D, [], None),
 ("mimo_4", "F4 (L622)", None, "mimo 4 F4", 622, A, ["mimo 4 F4"],
  dict(old="", new_between=('and at L622: "', '"\n'))),
 ("mimo_4", "F5", 5, "mimo 4 F5", 497, S, ["mimo 4 F5"], None),
 ("mimo_4", "F5 ((U3))", None, "mimo 4 F5", 506, A, ["mimo 4 F5"],
  dict(old="", new_between=('with (U3) as "', '"\n'))),
 ("mimo_4", "F6 (i)", 6, "mimo 4 F6", 626, A, ["mimo 4 F6 (i)"], None),
 ("mimo_4", "F6 (ii)", 7, "mimo 4 F6", 630, S, ["mimo 4 F6 (ii)"], None),
 ("mimo_4", "F7", 8, "mimo 4 F7", 588, S, ["mimo 4 F7"], None),
 ("mimo_4", "F8", 9, "mimo 4 F8", 612, A, ["mimo 4 F8"], None),
 ("mimo_4", "F9 (i)", None, "mimo 4 F9", 540, A, ["mimo 4 F9 (i)"],
  dict(old="the Claim of Argument 1", new="the Consequence of Argument 1")),
 ("mimo_4", "F9 (ii)", None, "mimo 4 F9", 562, A, ["mimo 4 F9 (ii)"],
  dict(old="one counterpart, the same subnetwork of \\(D\\) with port translations onto the same ports of \\(D\\)", new_between=('Replace the premise in (ii) with "', '".\n'))),
 ("mimo_4", "F10", 10, "mimo 4 F10", 526, A, ["mimo 4 F10"], None),
 ("mimo_4", "F11", 11, "mimo 4 F11", 600, A, ["mimo 4 F11"], None),
 ("mimo_4", "F12", 12, "mimo 4 F12", 608, A, ["mimo 4 F12"], None),
]


def norm(s):
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def blocks_of(text):
    fin = re.split(r"\n#+ Answers", text)[0]
    return re.findall(r"\n```[a-z]*\n(.*?)\n```", fin, flags=re.S)


def best_match(lines, hint, block, span=4):
    """Best window of whole sentences (one line) or of consecutive lines near `hint`."""
    b = norm(block)
    best = (0.0, None, "")
    rng = range(max(1, hint - span), min(len(lines), hint + span) + 1)
    if "\n" in block.strip():
        k = block.strip().count("\n") + 1
        for n in rng:
            for w in range(1, k + 3):
                if n + w - 1 > len(lines):
                    break
                win = lines[n - 1:n - 1 + w]
                if not win[0].strip() or not win[-1].strip():
                    continue
                cand = "\n".join(win)
                sm = difflib.SequenceMatcher(None, norm(cand), b, autojunk=False)
                if sm.quick_ratio() < best[0]:
                    continue
                r = sm.ratio()
                if r > best[0]:
                    best = (r, n, cand)
        return best
    for n in rng:
        L = lines[n - 1]
        if not L.strip():
            continue
        sents = sentences_of(L)
        for i in range(len(sents)):
            for j in range(i + 1, len(sents) + 1):
                cand = " ".join(sents[i:j])
                if len(cand) > 3 * len(b) + 200:
                    break
                sm = difflib.SequenceMatcher(None, norm(cand), b, autojunk=False)
                if sm.quick_ratio() < best[0]:
                    continue
                r = sm.ratio()
                if r > best[0]:
                    best = (r, n, cand)
    return best


def build(next_rid, prior, texts):
    out = []
    report = []
    st1 = texts["stage1"]
    H1 = headings(st1)
    texts2 = dict(texts)
    texts2[STAGE1_NAME] = st1
    s2 = {r["_key"][1]: r for r in prior if r.get("_key", ("",))[0] == "S96-2"}
    s3 = [r for r in prior if r.get("_key", ("",))[0] == "S96-3"]
    # ---------------- (a) whole-text check ----------------
    W = Src(WF)
    sec = W.text[W.text.index("## 5. Repairs, exact wordings"):W.text.index("## 6. Not done here")]
    items = re.split(r"\n(?=\*\*[A-Z]-\d \()", sec)
    for it in items[1:]:
        m = re.match(r"\*\*([A-Z]-\d) \(l\. (\d+)", it)
        iid, line0 = m.group(1), int(m.group(2))
        subs = list(re.finditer(
            r"(?:(?:At|at) (?:the end of )?l\. (\d+),? )?(?:[Rr]eplace \"(.*?)\" with:|(?:[Aa]fter|add:?) \"(.*?)\"(?: \([^)]*\))?,? add:|after \"(.*?)\"(?: \([^)]*\))?,? add:)\n> (.*)", it))
        for k, sm in enumerate(subs):
            line = int(sm.group(1)) if sm.group(1) else line0
            old = sm.group(2) or ""
            anchor = sm.group(3) or sm.group(4)
            new = sm.group(5)
            status, links = WMAP[(iid, k)]
            os_, ns_, found = place(texts2, STAGE1_NAME, line, old, new, anchor if not old else None)
            ref = "section 5, %s, proposal %d%s" % (iid, k + 1, ("; to be inserted after: %s" % anchor) if anchor else "")
            r = rec(next_rid(), "S96", WF, ref, "recommendation", status,
                    "repaired copy" if status == A else "none", STAGE1_NAME, line, H1, old, new, os_, ns_,
                    "sentence" if old and os_ and old.strip() == os_.strip() else "span")
            r["same_as"] = [s2[x]["rid"] for x in links]
            r["_key"] = ("W", iid, k)
            out.append(r)
        if iid == "B-4":
            new = W.between("After the B-3 sentence add:\n> ", "\n", "**B-4 (l. 397).**")
            r = rec(next_rid(), "S96", WF, "section 5, B-4, proposal 1; to be inserted after the sentence B-3 proposes",
                    "recommendation", A, "repaired copy", STAGE1_NAME, 397, H1, "", new, "", "", "sentence")
            r["same_as"] = [s2[20]["rid"]]
            r["_key"] = ("W", iid, 0)
            out.append(r)
        if iid == "O-6":
            new = W.between("sentence add:\n> ", "\n", "**O-6 (l. 315; optional).**")
            L = st1[315 - 1]
            k0 = L.index("Nor is the conflict enough to do anything about it")
            anchor_sent = locate_sentence(L, L[k0:k0 + 60])
            os_, ns_, found = place(texts2, STAGE1_NAME, 315, "", new, anchor_sent)
            r = rec(next_rid(), "S96", WF, "section 5, O-6 (optional), proposal 1; to be inserted after the sentence beginning: Nor is the conflict enough to do anything about it",
                    "recommendation", A, "repaired copy", STAGE1_NAME, 315, H1, "", new, os_, ns_, "sentence")
            r["same_as"] = [s2[11]["rid"]]
            r["_key"] = ("W", iid, 0)
            out.append(r)
            r = rec(next_rid(), "S96", WF, "section 5, O-7", "recommendation", O, "none", STAGE1_NAME, 317, H1,
                    "", "[no wording given] " + W.between("**O-7.** ", "\n", "## 5. Repairs"), "", "", "sentence")
            r["_key"] = ("W", "O-7", 0)
            out.append(r)
    # ---------------- (b) cases check ----------------
    K = Src(KF)
    old = K.between('Replace "', '" with "', "1. **l. 526, for O37.**")
    new = K.between('" with "', '."\n', "1. **l. 526, for O37.**")
    os_, ns_, found = place(texts2, STAGE1_NAME, 526, old, new)
    r = rec(next_rid(), "S96", KF, "Repairs proposed, 1 (l. 526, for O37)", "recommendation", A, "repaired copy",
            STAGE1_NAME, 526, H1, old, new, os_, ns_, "span")
    r["same_as"] = [s2[26]["rid"]]
    out.append(r)
    desc = K.between("2. **l. 317, for N5 and O24** (for the owner, not a repair on its own). ", " A problem solved")
    r = rec(next_rid(), "S96", KF, "Repairs proposed, 2 (l. 317, for N5 and O24)", "recommendation", O, "none",
            STAGE1_NAME, 317, H1, "", "[no wording given] " + desc, "", "", "sentence")
    out.append(r)
    # ---------------- (c) the replies ----------------
    rp = texts["repaired copy"]
    Hr = headings(rp)
    cache = {}
    for tag, flabel, bno, ruling, hint, status, links, inline in REPLIES:
        f = RD + "s96_xexam_%s.response.txt" % tag
        if f not in cache:
            cache[f] = Src(f)
        src = cache[f]
        blocks = blocks_of(src.text)
        old = ""
        anchor = None
        ratio = None
        line = hint
        os_ = ns_ = ""
        if inline and "block" not in inline:
            if "new" in inline:
                new = inline["new"]
            else:
                st, en = inline["new_between"]
                new = inline.get("new_prefix", "") + src.between(st, en)
                if "prefix" in inline:
                    new = inline["prefix"] + src.between(st, en)
            if "old_between" in inline:
                old = src.between(*inline["old_between"])
            else:
                old = inline.get("old", "")
            if inline.get("noplace"):
                pass
            elif inline.get("locate"):
                os_ = locate_sentence(rp[line - 1], inline["locate"])
            elif old and rp[line - 1].count(old) == 1:
                os_, ns_, _ = place(texts, "repaired copy", line, old, new)
            elif old:
                # the quoted words are not on the hinted line: search nearby
                for n in range(max(1, hint - 3), min(632, hint + 3) + 1):
                    if rp[n - 1].count(old) == 1:
                        line = n
                        os_, ns_, _ = place(texts, "repaired copy", line, old, new)
                        break
            elif not new.startswith("[no wording given]"):
                ratio, n, cand = best_match(rp, hint, new, span=3)
                if n and ratio >= 0.5:
                    line, os_ = n, cand
                    old = cand
                    ns_ = new if new.strip()[-1:] in ".)]" else ""
        else:
            new = blocks[bno - 1]
            if inline and "anchor" in inline:
                anchor = inline["anchor"]
                os_, ns_, _ = place(texts, "repaired copy", line, "", new.strip() if not new.startswith(",") else new, anchor)
                if new.startswith(","):
                    L = rp[line - 1]
                    if L.count(anchor) == 1:
                        nl = L.replace(anchor, anchor.rstrip(".") + new.rstrip() + ("." if anchor.endswith(".") and not new.rstrip().endswith(".") else ""), 1)
                        ns_ = locate_sentence(nl, anchor.rstrip(".")) if anchor.rstrip(".") in nl else ""
            else:
                ratio, n, cand = best_match(rp, hint, new)
                if n and ratio >= 0.4:
                    line = n
                    old = cand
                    os_ = cand
                    ns_ = new
        stage3 = [r["rid"] for r in s3 if any(
            x in [y.strip() for y in re.split(r"[;,]", r["_ruling"])] for x in links)]
        if not stage3:
            stage3 = [r["rid"] for r in s3 if any(
                any(y.strip().startswith(x + " (") for y in re.split(r";", r["_ruling"])) for x in links)]
        ref = "%s%s; ruling '%s' in %s, section 3" % (
            flabel, (", proposed wording (code block %d)" % bno) if bno else ", wording given inline",
            ruling, READING)
        if anchor:
            ref += "; to be inserted after: %s" % anchor
        r = rec(next_rid(), "S96", RD + "s96_xexam_%s.response.txt" % tag, ref, "recommendation", status,
                "latest text" if status == A else "none", "repaired copy", line, Hr, old, new, os_, ns_,
                "paragraph" if "\n" in new.strip() else ("sentence" if old and os_ == old else "span"))
        r["same_as"] = stage3
        r["_key"] = ("reply", tag, flabel, bno)
        report.append((r["rid"], tag, flabel, bno, ratio, line))
        out.append(r)
    # replies about the same place, joined by the reading: link them
    groups = {}
    for r in out:
        k = r.get("_key", ("",))
        if k[0] == "reply":
            ref = r["source_ref"]
            m = re.search(r"ruling '([^']*)'", ref)
            groups.setdefault((m.group(1), r["target_line"]), []).append(r)
    for g, rs in groups.items():
        for r in rs:
            r["same_as"] += [o["rid"] for o in rs if o is not r]
    build.report = report
    return out
