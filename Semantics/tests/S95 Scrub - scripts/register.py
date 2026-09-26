import re, json, collections
SRC = "/home/user/ThreadSmith/Semantics/tests/Revision 2 - file 13 draft 5, theory text.md"
OUT = "/home/user/ThreadSmith/Semantics/tests/S95 Scrub - register of words in draft 5"
lines = open(SRC, encoding="utf-8").read().split("\n")

# family regex -> (category, listed_by, family label). Order matters: phrases first.
F = [
 (r"reason to believe|reason to reject", "LISTED", "owner", "reason to believe/reject"),
 (r"better than|worse than", "LISTED", "owner", "better/worse than"),
 (r"not true|more true", "LISTED", "owner", "not true / more true"),
 (r"derived from", "LISTED", "owner", "derive"),
 (r"rests? on", "TRUTH-OR-FOUNDATION", "task", "rests on"),
 (r"well[ -]founded", "TRUTH-OR-FOUNDATION", "task", "well-founded"),
 (r"less elegant|more admitted", "RANKING", "task", "more/less + adjective"),
 (r"tells? against|counts? against", "BELIEF", "extra", "tells/counts against"),
 (r"fit|fits|fitted|fitting", "LISTED", "owner", "fit"),
 (r"support\w*", "LISTED", "owner", "support"),
 (r"verif\w*", "LISTED", "owner", "verify"),
 (r"corroborat\w*", "LISTED", "owner", "corroborate"),
 (r"disprov\w*|disproof\w*", "LISTED", "owner", "disprove"),
 (r"prove|proves|proved|proven|proving|provable|proofs?", "LISTED", "owner", "prove/proof"),
 (r"true|truth\w*|truly|untrue", "LISTED", "owner", "true/truth"),
 (r"establish\w*", "LISTED", "owner", "establish"),
 (r"authorit\w*", "LISTED", "owner", "authority"),
 (r"foundation\w*", "LISTED", "owner", "foundation"),
 (r"deriv\w*", "LISTED", "owner", "derive"),
 (r"believ\w*|belief\w*", "BELIEF", "task", "belief"),
 (r"credenc\w*|confiden\w*|credib\w*", "BELIEF", "task", "credence/confidence"),
 (r"justif\w*", "BELIEF", "task", "justify"),
 (r"warrant\w*|trust\w*|certain\w*|sure|surely|doubt\w*", "BELIEF", "task", "warrant/trust/certain/sure/doubt"),
 (r"know|knows|known|knowing|knowledge", "BELIEF", "task", "know/knowledge"),
 (r"evidence\w*", "BELIEF", "task", "evidence"),
 (r"confirm\w*|validat\w*|valid|validity|invalid", "BELIEF", "task", "confirm/valid"),
 (r"epistemic\w*", "BELIEF", "extra", "epistemic"),
 (r"expect\w*", "BELIEF", "extra", "expectation"),
 (r"reliab\w*", "BELIEF", "extra", "reliable"),
 (r"certif\w*", "BELIEF", "extra", "certify"),
 (r"false\w*|falsi\w*", "TRUTH-OR-FOUNDATION", "task", "false/falsify"),
 (r"correct\w*|incorrect\w*", "TRUTH-OR-FOUNDATION", "task", "correct"),
 (r"facts?|factual", "TRUTH-OR-FOUNDATION", "task", "fact"),
 (r"real|reality|realities|really", "TRUTH-OR-FOUNDATION", "task", "real/reality"),
 (r"ground\w*|basis|basic\w*", "TRUTH-OR-FOUNDATION", "task", "ground/basis"),
 (r"primitive\w*|axiom\w*", "TRUTH-OR-FOUNDATION", "task", "primitive/axiom"),
 (r"secur\w*|guarante\w*|sound\w*", "TRUTH-OR-FOUNDATION", "task", "secure/guarantee/sound"),
 (r"refut\w*", "TRUTH-OR-FOUNDATION", "task", "refute"),
 (r"theorem\w*|lemma\w*|corollar\w*|demonstrat\w*", "TRUTH-OR-FOUNDATION", "extra", "theorem/corollary/demonstration"),
 (r"show|shows|shown|showing", "TRUTH-OR-FOUNDATION", "extra", "show (proof or evidence sense)"),
 (r"anchor\w*", "TRUTH-OR-FOUNDATION", "extra", "anchor"),
 (r"standing", "TRUTH-OR-FOUNDATION", "extra", "standing"),
 (r"licen[cs]\w*|Lic", "TRUTH-OR-FOUNDATION", "extra", "license"),
 (r"normativ\w*", "TRUTH-OR-FOUNDATION", "extra", "normative"),
 (r"obligation\w*", "TRUTH-OR-FOUNDATION", "extra", "obligation"),
 (r"settle\w*", "TRUTH-OR-FOUNDATION", "extra", "settle"),
 (r"genuine\w*|objective\w*|legitima\w*", "TRUTH-OR-FOUNDATION", "extra", "genuine/objective/legitimate"),
 (r"witness\w*", "TRUTH-OR-FOUNDATION", "extra", "witness"),
 (r"wrong\w*|right", "TRUTH-OR-FOUNDATION", "extra", "right/wrong"),
 (r"accura\w*", "TRUTH-OR-FOUNDATION", "extra", "accurate"),
 (r"better|worse|best|worst|superior\w*|inferior\w*", "RANKING", "task", "better/worse/best"),
 (r"merit\w*|worth\w*|grade\w*|rank\w*|good|bad|prefer\w*|success\w*|adequa\w*|perfect\w*", "RANKING", "extra", "merit/worth/grade/rank/success/adequate/perfection"),
 (r"progress\w*|advanc\w*|elegan\w*|appropriate\w*", "RANKING", "extra", "progress/advance/elegant/appropriate"),
 (r"accept\w*", "ACCEPT", "task", "accept"),
 (r"adopt\w*", "ACCEPT", "extra", "adopt (near-synonym of accept)"),
 (r"hold|holds|held", "BORDERLINE", "extra", "hold (satisfaction or possession)"),
 (r"entail\w*|implies|imply|follows|yields?", "BORDERLINE", "extra", "logical joint"),
]
BIG = re.compile(r"\b(" + "|".join("(?:%s)" % f[0] for f in F) + r")\b", re.I)

def family(w):
    for rx, cat, by, lab in F:
        if re.fullmatch(rx, w, re.I): return cat, by, lab
    raise ValueError(w)

POSSESS = {201, 315, 369, 429, 580}
PROOFBLOCK = re.compile(r"^\*?Proof\*?$")
def classify(n, w, pre, post, raw):
    wl = w.lower(); cat, by, lab = family(w); tech = ""; note = ""
    if lab == "derive":
        if w.startswith("Derivation") and (re.match(r"\s*\d", post) or n in (546, 550)):
            tech = "Derivation 1–10, the Part XVI labels"
        elif n == 397: tech = "receipt (Part IX): 'a derivation tree over leaves'"
        if n in (21, 455, 518, 526): note = "definitional dependence ('derive'/'derived')"
        if n in (29, 31, 520): note = "Part 0/XIV: 'everything else is derived from the two primitives'"
        if n in (107, 203): note = "section title"
        if n == 211: note = "causal: a record copied from the carrier"
    if lab == "prove/proof":
        if w == "Proof": tech = "proof block of a claim (Part VI, VIII, XVI)"
        elif n in (49, 105, 277, 343, 429, 495): note = "mathematical proof as subject matter"
        if n == 105: cat = "BORDERLINE"; note = "a kind of port (mathematical object)"
    if lab == "support":
        if 285 <= n <= 313: tech = "support (Part VI): a member W of S_{E,p}, a subset whose restriction is an account"
        elif n == 403: note = "ordinary: assists a use task"
    if lab == "establish":
        if n in (315, 369, 395, 526) or (n == 317 and wl == "established"):
            tech = "established (Part VI): the assessor holds a usable receipt"
        elif n == 317: note = "ordinary, inside the definition of 'test' (Part VI)"
    if lab == "fit" and n in (315, 317, 526): tech = "fits (Part VI): no established result shows it failing (E)"
    if wl.startswith("receipt"): tech = "receipt (Part IX)"
    if lab == "evidence" and n == 397: tech = "evidence leaf (Part IX)"
    if lab == "refute":
        if n == 395: tech = "(K3), 'What a test refutes'"
        elif n == 317: note = "inside the definition of 'test' (Part VI)"
        elif n in (47, 61, 534, 542): note = "Part XV defeat list"
    if lab == "primitive/axiom" and wl.startswith("primitive"):
        if n in (47, 171, 175, 201, 542, 576, 620): tech = "primitive layer P (Part IV)"
        else: tech = "the two primitives, Θ and N (Parts 0, XIV; Derivation 6)"
    if lab == "primitive/axiom" and wl.startswith("axiom"): note = "mathematics as subject matter"
    if lab == "anchor": tech = "anchor λ(k) (Parts II, V; Derivations 1, 2)" if n not in (279, 281) else "the refused 'anchoring condition' (Part V)"
    if lab == "normative": tech = "normative relation N, primitive 2 (Parts XI, XIV)"
    if lab == "standing": tech = "Standing, (K2) (Part IX)"
    if lab == "license":
        if n == 608: note = "ordinary: 'a licensed operation of the semantics'"
        else: tech = "(K2) Lic_j(u)"
    if lab == "ground/basis":
        if n in (377, 383): tech = "(K1) grounds g of a criticism (Part IX)"
    if lab == "confirm/valid" and n == 385: note = "in 'Reason use', between (K1) and (K2)"
    if lab == "know/knowledge":
        if n in (433, 443, 520, 528): tech = "created explanatory knowledge (EK) (Part XI); knowledge-creation class (Part XIV)"
        elif n in (31, 526, 600): note = "quoted, in the list of predicates the theory refuses as primitive"
    if lab == "epistemic": tech = "epistemic obligation O_ep in (EK) (Part XI)"
    if lab == "expectation":
        if n == 201: note = "ordinary: 'the expected arrangement'"
        else: tech = "expectation (Part IV; Derivation 4)"
    if lab == "accurate" and n in (479, 517): tech = "accuracy grades Q_Θ of the physical module (Parts XII, XIV)"
    if lab.startswith("merit") and wl.startswith("grade") and n in (479, 517): tech = "accuracy grades Q_Θ (Parts XII, XIV)"
    if lab == "obligation": tech = "claimed and protected obligations O, P; epistemic obligations (Part XI, (P), (EK))"
    if lab == "witness":
        if n in (47, 155, 197, 225, 405, 409, 411, 542, 584, 604): tech = "construction witness (Parts IV, X)"
        elif n == 632: note = "logic: a relative-consistency witness"
        elif n in (311, 343): note = "mathematical witness (an instance of an existential claim)"
        elif n == 211: note = "testimony sense: 'independent witness to its history'"
    if lab.startswith("theorem"):
        if wl.startswith("theorem") and n in (305, 546): tech = "Finite monotone theorem (Part VI)"
        if n == 542: tech = "Derivation 3's qualification"
        if n == 552: tech = "title of Derivation 1"
        if wl.startswith("corollar"): tech = "Corollary of Derivation 1"
    if lab == "real/reality":
        if n == 343: cat = "BORDERLINE"; note = "real numbers"
        elif wl == "really": note = "in scare quotes: the claim the theory refuses"
    if lab == "true/truth":
        if n in (31, 524): cat = "BORDERLINE"; note = "logic: a predicate is 'true or false' of a case, as against an index"
        if n == 151: cat = "BORDERLINE"; note = "mathematics: a reachability truth value"
        if n == 255: cat = "BORDERLINE"; note = "mathematics: logically equivalent mathematical truths"
        if n == 606: cat = "BORDERLINE"; note = "satisfaction at an index (Derivation 7)"
    if lab == "correct":
        if wl == "correction": cat = "BORDERLINE"; note = "the owner's 'error correction'"
        if n == 628: note = "inside a quoted obligation, 'predict displacements correctly'"
        if n in (441, 443): note = "'correct account' in the prose of Part XI"
    if lab.startswith("show"):
        if n == 624: cat = "BORDERLINE"; note = "display sense: 'the occupancy field shows nothing'"
        elif n == 315: note = "inside the definition of 'fits'"
    if lab.startswith("hold"):
        if re.match(r"\s*(a|an|selected|usable)\b", post) or n == 429:
            note = "possession sense (holds a receipt, a transport)"
        elif n == 317: note = "idiom: 'holds one of them to account'"
        else: note = "satisfaction sense ('the condition holds')"
    if lab == "logical joint": note = "joint of an argument"
    if lab == "more/less + adjective":
        if wl == "more admitted": cat = "BORDERLINE"; note = "a count, not merit"
        else: note = "inside a denial: (E) does not prefer the elegant account"
    if lab.startswith("merit") and n in (25, 317, 522): note = (note + "; " if note else "") + "inside a denial"
    if lab.startswith("genuine") and n == 610: note = "title of Derivation 8, 'genuine recoding'"
    if lab.startswith("progress") and n == 433: tech = "title of Part XI"
    if lab.startswith("progress") and n == 497: note = "Part XIII: advanceable challenges"
    if lab.startswith("progress") and "appropriate" in w.lower(): note = "near-synonym of 'fits'"
    if lab == "tells/counts against" and n in (315, 369): tech = "(K3), as used in Part VI and Part VIII"
    if lab.startswith("adopt") and n in (75, 315, 461, 526): note = "'the adopted physics' (Part I) or the physical module"
    if lab == "settle" and n == 317: tech = "inside the definition of 'problem' (Part VI)"
    return cat, by, lab, tech, note

rows = []
for n, raw in enumerate(lines, 1):
    for m in BIG.finditer(raw):
        w = m.group(1)
        if w.lower() == "right" and re.match(r"-hand", raw[m.end():]): continue
        if w == "Lic" and not raw[m.start()-1:m.start()] in ("{", "\\", " "): pass
        pre = raw[:m.start()].split()[-6:]
        post = raw[m.end():]
        ctx = " ".join(pre + ["[" + w + "]"] + post.split()[:5])
        cat, by, lab, tech, note = classify(n, w, pre, post, raw)
        rows.append({"line": n, "word": w, "context": ctx, "category": cat, "listed_by": by,
                     "family": lab, "technical_term": bool(tech), "term": tech, "note": note})
for i, r in enumerate(rows, 1): r["n"] = i
json.dump({"source": "tests/Revision 2 - file 13 draft 5, theory text.md",
           "source_md5": "7f1d8ad02adf96e27622593bd263252e",
           "made_for": "log S95, decision S23", "rows": rows}, open(OUT + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
c = collections.Counter(r["category"] for r in rows)
print(len(rows), dict(c), "technical:", sum(r["technical_term"] for r in rows))

def esc(x): return x.replace("|", "\\|").replace("\n", " ")
md = ["# S95 Scrub — register of words in draft 5", "",
 "*Log S95, under decision S23 (the owner, 25 September 2026). Made by program (`S95 Scrub - scripts/register.py`) from `tests/Revision 2 - file 13 draft 5, theory text.md` (md5 7f1d8ad02adf96e27622593bd263252e), which is read and not edited. The same rows are in the JSON file beside this one.*", "",
 "**What is scanned.** Every occurrence, whole word and inflection, case-insensitive, LaTeX included, of: the owner's list (fit, support, verify, corroborate, prove/proof, disprove, reason to believe, reason to reject, better than, worse than, true/truth, not true, more true, establish, authority, foundation, derive/derived from); belief words (believe, belief, credence, confidence, credible, justify, warrant, trust, certain, know/knowledge, evidence, confirm, valid, sure, doubt); truth and foundation words (false, falsify, correct, fact, real/reality, ground, basis, basic, rests on, primitive, axiom, secure, guarantee, sound, refute); ranking words (better, worse, best, worst, superior, inferior, more/less with an adjective of merit); and accept. Words the task did not list but that carry one of the forbidden ideas back in are added and marked *extra* in the column *from*: epistemic, expectation, reliable, certify, theorem/corollary/demonstration, show (proof sense), anchor, standing, license, normative, obligation, settle, genuine/objective/legitimate, witness, right/wrong, accurate, merit/worth/grade/rank/success/adequate/perfection/prefer/bad, progress/advance/elegant/appropriate, tells/counts against, adopt, well-founded, hold (satisfaction sense) and the logical joints entail/imply/follows/yields.",
 "",
 "**Words the scan looked for and did not find in draft 5:** verify, corroborate, disprove, reason to believe, reason to reject, better than, worse than, not true, more true, authority, foundation, believe, belief, credence, confidence, credible, warrant, trust, certain, sure, doubt, confirm, validate, basis, basic, secure, sound, falsify, better, worse, best, worst, superior, inferior, good.",
 "",
 "**Categories.** LISTED: the family is on the owner's list. BELIEF, TRUTH-OR-FOUNDATION, RANKING, ACCEPT: the task's groups. BORDERLINE: an ordinary mathematical, logical or physical use (real numbers, a truth value, a predicate true of a case, 'holds' of a condition, a logical joint, the owner's 'error correction'). *Technical term* names the defined term of the theory the occurrence belongs to; blank means the word is used in its ordinary sense.",
 "",
 "TOTALS",
 "",
 "| # | line | word | context (12 words) | category | from | technical term | note |",
 "|---|---|---|---|---|---|---|---|"]
cc = collections.Counter(r["category"] for r in rows); cb = collections.Counter(r["listed_by"] for r in rows)
md[md.index("TOTALS")] = ("**Totals.** " + str(len(rows)) + " occurrences on " + str(len({r['line'] for r in rows})) + " lines. By category: " +
    ", ".join(f"{k} {cc[k]}" for k in ["LISTED","BELIEF","TRUTH-OR-FOUNDATION","RANKING","ACCEPT","BORDERLINE"]) +
    ". From the owner's list " + str(cb['owner']) + ", the task's lists " + str(cb['task']) + ", extra " + str(cb['extra']) +
    ". In a defined technical term of the theory: " + str(sum(r['technical_term'] for r in rows)) + ".")
for r in rows:
    md.append(f"| {r['n']} | {r['line']} | {esc(r['word'])} | {esc(r['context'])} | {r['category']} | {r['listed_by']} | {esc(r['term'])} | {esc(r['note'])} |")
open(OUT + ".md", "w", encoding="utf-8").write("\n".join(md) + "\n")
fam = collections.Counter((r["category"], r["family"]) for r in rows)
for k, v in sorted(fam.items()): print(v, k)
