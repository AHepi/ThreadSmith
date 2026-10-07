# S104 round 2 (maths): writes "search results.md" and "search results.json" from a run of the search.
import json
import os
import platform
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from s104_check import MD5, check_markdown  # noqa: E402

TEXT_NAME = "tests/103 The semantics, standing alone, after round 1.md"
DATE = "27 September 2026"
FOLDER = "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths"

# What each counterexample rests on, in a sentence; the full list of inventions is given with it.
CEX_NOTES = {
    "FC05": "Rests on I93 reading (ii) ('stay equal' under any footprint bijection) with I10's bijection of equal domains; under reading (i) the sentence holds on every model tried.",
    "FC18": "Rests on I94 (the counterpart read untranslated, on D's ports and domains) with I10 (bijections between equal domains) and I14 (value maps). Under D4.4's reading FC18 holds on every model tried.",
    "FC20": "Rests on I14 and I81 (value maps that need not be injective) and I21 (⊥ for several values). With κ the identity the claim holds on every model tried.",
    "FC23": "Rests on I24 (the lookup's slot) and on the claim's own wording, which allows background components that make Sol_E empty; with a satisfiable background (b) holds on every model tried.",
    "FC25": "Rests on I14 and D1.4 (a subnetwork's ports are its components' footprints) with I32 (λ(k) = the whole target). Where every port of D lies in some footprint, (a) and (b) hold on every model tried.",
    "FC63": "Rests on I66 and I99 (which relation the sum component carries) and I81 (derived ports, without which the candidate cannot be written under I14). With the sum restricted to realizable term tuples the candidate meets (E).",
    "FC77": "Rests on I18 (Hom is a condition on τ as a whole, not at a pair) and I52 (Sel with 𝒯 = {t}, μ the identity). The trivial witness exists exactly for the transports whose τ is a homomorphism.",
    "FC78": "Rests on D12.1's reading of L195 (I52: no occurrence represents t, H or the survival condition), I53 (one history), I56 (Prepares a primitive) and I90 (Θ by hand). L201's stronger sentence would exclude it; the formal core does not use L201.",
    "FC81": "(d) rests on the same history as FC78 (I52, I53, I56, I90).",
    "FC82": "Rests on the same history as FC78 (I52, I53, I56, I90).",
    "FC83": "Rests on I56 (Build's three primitives) and I90 (Θ by hand); it is the case FC83's own Look names.",
    "FC102": "Rests on I68 and I100 (six cells, occlusion of a run of interior cells, occupancy without identity as L620 has it, reflection at the ends); I52, the claim's own, plays no part in this computation.",
}


def load_claims():
    d = json.load(open(os.path.join(HERE, "formal claims.json"), encoding="utf-8"))
    return OrderedDict((c["id"], c) for c in d["claims"])


def inv_sort(xs):
    return sorted(set(xs), key=lambda s: int(s[1:]))


def reproduce_cmd(cid, S):
    extra = ""
    if S.scale != 1.0:
        extra += " --scale %g" % S.scale
    if S.time_cap != 20.0:
        extra += " --time-cap %g" % S.time_cap
    return 'cd "%s" && python3 -m model.run --claim %s%s' % (FOLDER, cid, extra)


def enrich(out, S):
    claims = load_claims()
    res = []
    for r in out:
        c = claims.get(r["id"], {})
        cinv = list(c.get("inventions", []))
        pinv = list(r["program_inventions"])
        parts = []
        # a program invention named by some part is specific to the parts that name it; the others hold
        # for every part of the claim
        specific = set(i for p in r["parts"] for i in p.get("inventions", [])) & set(pinv)
        wide = [i for i in pinv if i not in specific]
        for p in r["parts"]:
            q = OrderedDict(p)
            q["rests_on"] = inv_sort(cinv + wide + list(p.get("inventions", [])))
            parts.append(q)
        allinv = inv_sort(cinv + pinv + [i for p in r["parts"] for i in p.get("inventions", [])])
        res.append(OrderedDict([
            ("id", r["id"]), ("title", c.get("title")), ("type", c.get("type")), ("formal", c.get("formal")),
            ("status", r["status"]), ("claim_inventions", inv_sort(cinv)), ("program_inventions", inv_sort(pinv)),
            ("rests_on", allinv), ("note", CEX_NOTES.get(r["id"]) if r["status"] == "COUNTEREXAMPLE FOUND" else None),
            ("reproduce", reproduce_cmd(r["id"], S)), ("seconds", r["seconds"]), ("error", r["error"]), ("parts", parts)]))
    return res


def is_cex(p):
    return p["status"] in ("counterexample found", "computed: not as claimed", "fails by construction")


def space_line(p):
    bits = []
    sp = p.get("space") or {}
    if p.get("exhaustive"):
        bits.append("exhaustive: %s" % sp.get("note"))
    else:
        if sp.get("sizes_from"):
            bits.append("sizes %s … %s (%d sizes, %d draws each)" % (sp["sizes_from"], sp["sizes_to"], sp["n_sizes"], sp["per_size"]))
        if sp.get("families"):
            bits.append("families: %s" % ", ".join(sp["families"]))
        if sp.get("note"):
            bits.append(sp["note"])
    if p.get("seed") is not None:
        bits.append("seed %d" % p["seed"])
    if p.get("models_tried") is not None:
        bits.append("%d models tried" % p["models_tried"])
    if p.get("hypothesis_met") is not None and p.get("hypothesis_met") != p.get("models_tried"):
        bits.append("%d of them meeting the claim's hypothesis" % p["hypothesis_met"])
    if p.get("smallest_size"):
        bits.append("first found at size %s" % p["smallest_size"])
    if p.get("stopped"):
        bits.append(p["stopped"])
    return "; ".join(bits)


def fence(txt):
    return "```\n" + txt.rstrip() + "\n```"


def write_results(out, S, total_seconds):
    res = enrich(out, S)
    counts = OrderedDict()
    for r in res:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    pcounts = OrderedDict()
    for r in res:
        for p in r["parts"]:
            pcounts[p["status"]] = pcounts.get(p["status"], 0) + 1
    # invention -> results that depend on it
    inv_res = OrderedDict()
    for r in res:
        for i in r["rests_on"]:
            inv_res.setdefault(i, []).append(OrderedDict([("claim", r["id"]), ("status", r["status"]),
                                                          ("counterexample_parts", [p["label"] for p in r["parts"] if is_cex(p) and i in p["rests_on"]])]))
    inv_res = OrderedDict(sorted(inv_res.items(), key=lambda kv: int(kv[0][1:])))
    J = OrderedDict()
    J["about"] = OrderedDict([
        ("log", "S104"), ("round", "review round 2 (maths): the counterexample search"), ("date", DATE), ("decision", "S36"),
        ("text_under_review", TEXT_NAME), ("md5", MD5),
        ("program", "model/ (standard library only); run from the folder: python3 -m model.run"),
        ("scale", S.scale), ("time_cap_per_part_seconds", S.time_cap), ("total_seconds", total_seconds),
        ("python", platform.python_version()),
        ("statuses", {"HOLDS ON ALL MODELS TRIED": "no part found a counterexample; every part searched says what it searched",
                      "COUNTEREXAMPLE FOUND": "some part found one; the smallest found is written out",
                      "NOT TESTED": "no part could be put to the models; each says why"}),
        ("claim_counts", counts), ("part_counts", pcounts),
        ("note", "A result on a claim depends on every invention in its rests_on list: the claim's own (formal claims.json) and the program's (inventions register, I77 onward). A counterexample that rests on an invention is a counterexample to this formalization, not to the text."),
    ])
    J["results"] = res
    for r in res:
        r["counterexample_rests_on"] = inv_sort([i for p in r["parts"] if is_cex(p) for i in p["rests_on"]]) if r["status"] == "COUNTEREXAMPLE FOUND" else []
    J["counterexamples"] = [OrderedDict([("claim", r["id"]), ("title", r["title"]), ("parts", [p["label"] for p in r["parts"] if is_cex(p)]),
                                         ("rests_on", r["counterexample_rests_on"]), ("note", r["note"]), ("reproduce", r["reproduce"])]) for r in res if r["status"] == "COUNTEREXAMPLE FOUND"]
    J["not_tested"] = [OrderedDict([("claim", r["id"]), ("part", p["label"]), ("why", p.get("why"))]) for r in res for p in r["parts"] if p["status"] == "not tested"]
    J["inventions_results"] = inv_res
    json.dump(J, open(os.path.join(HERE, "search results.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    M = []
    M.append("# S104 Round 2 — search results")
    M.append("")
    M.append("*Log S104, review round 2 (the maths round), %s, under decision S36 (\"maybe exploring the math a bit more might help instead of words. Since words are vague\"; \"if implementation forces invention, that needs to be recorded\"). The text under review is `%s`, md5 %s (checked before every run; not written to). The claims are those of `formal claims.md` (FC01–FC110); the program is the package `model/` in this folder, standard library only. Written by `model/report.py` from one run of `python3 -m model.run --scale %g --time-cap %g` (%.0f s of computing).*" % (DATE, TEXT_NAME, MD5, S.scale, S.time_cap, total_seconds))
    M.append("")
    M.append("**What this is.** For each formal claim, the program built small finite models of the formal core and looked for a counterexample: through every model of a small space where the space is small, otherwise through seeded random draws in ascending order of size, so that the first counterexample found is the smallest found. Existence claims were searched for a witness. Claims about the text's worked cases were computed on the encodings of `formal core.md` §17. Every choice the program made that the formal core leaves open is an invention, recorded in `inventions register.md` as I77–I102 and tagged in the code; every result names the inventions it rests on, the claim's own and the program's. A result that rests on an invention is a result about this formalization, not about the text. Nothing is settled (S28): 'holds on all models tried' reports a search that found nothing within its bounds (I77), and a counterexample is one model, open to being read another way.")
    M.append("")
    M.append("**Statuses.** A claim is *COUNTEREXAMPLE FOUND* when some part found one (or a computation on a worked case came out otherwise than the claim says); *HOLDS ON ALL MODELS TRIED* when no part did and at least one part was put to models; *NOT TESTED* when no part could be, with the reason. Parts are: *for all* (searched for a counterexample), *there is* (searched for a witness), *computation* (a worked case computed), *by construction* (true of the program as written, reported, not searched), *look* (a claim's Look, a first reading of where a counterexample might lie, computed; its outcome never makes the claim's status), and *not tested*.")
    M.append("")
    M.append("**Counts.** %d claims: %s. Parts: %s." % (len(res), "; ".join("%d %s" % (v, k) for k, v in counts.items()),
                                                     "; ".join("%d %s" % (v, k) for k, v in pcounts.items())))
    M.append("")
    M.append("**Reproducing.** Every result, counterexamples included, is reproduced by one command, given with it: `cd \"%s\" && python3 -m model.run --claim FCnn%s%s`. The whole run: the same command without `--claim`." % (
        FOLDER, (" --scale %g" % S.scale) if S.scale != 1.0 else "", (" --time-cap %g" % S.time_cap) if S.time_cap != 20.0 else ""))
    M.append("")
    M.append("## Counterexamples")
    M.append("")
    for r in res:
        if r["status"] != "COUNTEREXAMPLE FOUND":
            continue
        M.append("### %s · %s" % (r["id"], r["title"]))
        M.append("")
        M.append("**The claim.** %s" % r["formal"])
        M.append("")
        if r["note"]:
            M.append("**What it rests on.** %s Every invention the counterexample depends on: %s." % (r["note"], ", ".join(r["counterexample_rests_on"])))
        else:
            M.append("**Inventions the counterexample depends on.** %s." % ", ".join(r["counterexample_rests_on"]))
        M.append("")
        M.append("**Reproduce.** `%s`" % r["reproduce"])
        M.append("")
        for p in r["parts"]:
            if not is_cex(p):
                continue
            M.append("**Part: %s** (%s). %s" % (p["label"], p["status"], p["statement"]))
            M.append("")
            sl = space_line(p)
            if sl:
                M.append("Searched: %s." % sl)
                M.append("")
            M.append(fence(p.get("counterexample") or p.get("result") or ""))
            M.append("")
            if p.get("note"):
                M.append("*%s*" % p["note"])
                M.append("")
    M.append("## Every claim")
    M.append("")
    M.append("| claim | status | parts | rests on |")
    M.append("| --- | --- | --- | --- |")
    for r in res:
        pc = OrderedDict()
        for p in r["parts"]:
            pc[p["status"]] = pc.get(p["status"], 0) + 1
        M.append("| %s | %s | %s | %s |" % (r["id"], r["status"], "; ".join("%d %s" % (v, k) for k, v in pc.items()), ", ".join(r["rests_on"]) or "—"))
    M.append("")
    M.append("## Details, claim by claim")
    for r in res:
        M.append("")
        M.append("### %s · %s — %s" % (r["id"], r["title"], r["status"]))
        M.append("")
        M.append("**The claim.** %s" % r["formal"])
        M.append("")
        M.append("**Rests on.** Claim's inventions: %s. Program's: %s. **Reproduce.** `%s`" % (", ".join(r["claim_inventions"]) or "none", ", ".join(r["program_inventions"]) or "none", r["reproduce"]))
        if r["error"]:
            M.append("")
            M.append("**Error.**")
            M.append(fence(r["error"]))
        for p in r["parts"]:
            M.append("")
            M.append("- **%s** [%s] — *%s*. %s" % (p["label"], p["kind"], p["status"], p["statement"]))
            sl = space_line(p)
            if sl:
                M.append("  - Searched: %s." % sl)
            if p.get("why"):
                M.append("  - Why not: %s" % p["why"])
            if p.get("note"):
                M.append("  - Note: %s" % p["note"])
            body = p.get("witness") or p.get("result")
            if body and not is_cex(p):
                txt = body if len(body) < 1500 else body[:1500] + "\n… (the full text is in search results.json and is printed by the reproduce command)"
                M.append("")
                for line in fence(txt).split("\n"):
                    M.append("  " + line)
            if is_cex(p):
                M.append("  - The counterexample is written out above, under Counterexamples.")
    M.append("")
    M.append("## Not tested, and why")
    M.append("")
    for x in J["not_tested"]:
        M.append("- %s, %s: %s" % (x["claim"], x["part"], x["why"]))
    M.append("")
    M.append("## Results by invention")
    M.append("")
    M.append("Each invention, with the claims whose results depend on it; a claim with a counterexample names the parts whose counterexample depends on it. The same list is written into each entry of `inventions register.md`.")
    M.append("")
    M.append("| invention | results that depend on it |")
    M.append("| --- | --- |")
    for i, rows in inv_res.items():
        M.append("| %s | %s |" % (i, "; ".join("%s %s%s" % (x["claim"], "(counterexample: %s)" % ", ".join(x["counterexample_parts"]) if x["counterexample_parts"] else
                                                          ("(counterexample elsewhere)" if x["status"] == "COUNTEREXAMPLE FOUND" else "(" + x["status"].lower() + ")"), "")
                                             for x in rows)))
    M.append("")
    M.append("*Written %s. Not committed.*" % DATE)
    open(os.path.join(HERE, "search results.md"), "w", encoding="utf-8").write("\n".join(M) + "\n")
    n, bad = check_markdown(os.path.join(HERE, "search results.md"))
    print("search results written; quotations in search results.md: %d, not found: %d" % (n, len(bad)))
