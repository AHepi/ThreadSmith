"""The frozen question, and the one arm that is handed less of it.

A RULE. W10 section 4: "The same frozen question is handed to every arm; the
question-identity field is recorded on every run." The question object is frozen in
fixtures/frozen_question.json; only the target line varies between documents, and it is
built by program from the manifest's "why" passage so that no arm can be handed a
different question by accident.

Arm (f) is "arm (a) with the change list withheld from the context" (W3 section 5).
Here that means exactly one thing: the change list and the list of what it leaves out are
removed from the frozen question, and nothing is put in their place. The method (file 33)
is sent whole in every arm, so its Step 4 still tells the reader to write a change list;
what arm (f) withholds is the one the owner handed in. B5 is the part under test: "At each
call the context must carry the frozen question - its target, the change list it ranges
over and what is asked - and the parts under test."

The gauge: no sentence of the withheld change list appears anywhere in an arm (f) prompt. If
one does, the build stops. It is run over the thing the reader is actually handed, on both
transports: on Sonnet over the whole prompt body, and on DeepSeek over the assembled messages
of every call (fault 20 of the stage-A review, which found it running once, at construction, on
the system message and the document alone, never on the user turn where the question block
sits, while two docstrings said otherwise).

Arm (x) (fault 8 of the stage-A review). The question block quotes the document's own sentence.
On three of the eight arms documents (W1, W9, W12) that sentence names one of the two names the
re-identification arm exchanges, so an unexchanged quotation would put one name in its old role
beside the exchanged document, by the rig's hand and not the reader's. for_document(row,
exchanged=True) runs the same exchange over the quotation, and a second gauge stops the build if
either name still stands anywhere in the question block of an exchanged run.
"""
import os, json
from rig import FIXTURES, sha256_text

FROZEN = os.path.join(FIXTURES, "frozen_question.json")


def load(path=None):
    with open(path or FROZEN, encoding="utf-8") as f:
        return json.load(f)


def for_document(row, q=None, exchanged=False):
    """The frozen question for one document: the fixed object with its target line filled in
    from the manifest's "why" passage, and the document's own sentence quoted where the manifest
    gives one, so that every arm is handed the same target word for word.

    exchanged=True is arm (x): the quotation is put through the same name exchange as the
    document, so the question quotes the document the reader was handed."""
    import corpus
    q = q or load()
    why, quote = corpus.why(row)
    if why:
        why = str(why).strip().rstrip(".")
        if not why.lower().startswith("why"):
            why = "why " + why
    target = q["target_template"].format(why=why) if why else q["target_fallback"]
    out = dict(q)
    out["document"] = row.get("id")
    out["target"] = target
    out["why_from_manifest"] = bool(why)
    out["quote"] = quote if isinstance(quote, str) else None
    out["exchanged"] = bool(exchanged)
    out["quote_exchange"] = None
    if exchanged:
        import exchange as X
        n = corpus.names(row)
        if n is None:
            raise SystemExit(f"{row.get('id')}: arm (x) asked for an exchanged question and the "
                             f"manifest gives no two names. Nothing sent.")
        a, b, av, bv = n
        before, counts = out["quote"] or "", {}
        if out["quote"]:
            out["quote"], counts = X.exchange(out["quote"], a, b, av, bv)
        out["quote_exchange"] = {"name_a": a, "name_b": b, "counts": counts,
                                 "replaced": sum(counts.values()),
                                 "occurrences_in_the_quote": occurrences(before, a, b, av, bv)}
        check_exchanged(out, a, b, av, bv, row.get("id"))
    return out


def occurrences(text, a, b, av=(), bv=()):
    """How many whole-word occurrences of either name's forms stand in a text."""
    import re
    import exchange as X
    alts = sorted(set(X.forms(a, av) + X.forms(b, bv)), key=len, reverse=True)
    if not alts or not text:
        return 0
    rx = re.compile(r"(?<![\w'’])(" + "|".join(re.escape(p) for p in alts) + r")(?![\w])", re.I)
    return len(rx.findall(text))


def check_exchanged(q, a, b, av=(), bv=(), doc_id=""):
    """The gauge for arm (x)'s question block, in two halves.

    1. Every occurrence of either name in the quotation was exchanged: the number of
       substitutions equals the number of occurrences that stood there before.
    2. No other line of the block names either name. Those lines are not exchanged, so a name
       in one of them is a name the rig would put in its old role beside an exchanged
       document, which is what fault 8 was."""
    e = q.get("quote_exchange") or {}
    if e.get("replaced") != e.get("occurrences_in_the_quote"):
        raise SystemExit(f"{doc_id}: arm (x) exchanged {e.get('replaced')} of "
                         f"{e.get('occurrences_in_the_quote')} name occurrences in the frozen "
                         f"question's quotation. Nothing sent.")
    rest = dict(q)
    rest["quote"] = None
    for with_cl in (True, False):
        n = occurrences(render(rest, with_cl), a, b, av, bv)
        if n:
            raise SystemExit(f"{doc_id}: arm (x)'s frozen question names one of the two exchanged "
                             f"names outside the quotation ({n} occurrence(s)); that line is not "
                             f"exchanged and would show a name in its old role. Nothing sent.")
    return True


def render(q, with_change_list=True):
    """The block that goes into the context. Arm (f) gets with_change_list=False."""
    lines = ["=== THE FROZEN QUESTION (it is not yours to change; if you find a better one,",
             "    say so in your answer and answer this one anyway) ===",
             f"Question id: {q['id']}   (frozen {q['frozen']})",
             f"What is being explained: {q['target']}"]
    if q.get("quote"):
        lines.append(f"The passage it turns on, in the document's own words: \"{q['quote']}\"")
    lines += [
             f"What is asked: {q['query']}",
             f"Which kind of question: {q['kind']}"]
    if with_change_list:
        lines.append("Over what range - the change list this question covers:")
        for c in q["change_list"]:
            lines.append(f"  - {c}")
        lines.append("What the change list leaves out, said before any run:")
        for c in q["left_out"]:
            lines.append(f"  - {c}")
    lines.append("=== END OF THE FROZEN QUESTION ===")
    return "\n".join(lines)


def withheld_strings(q):
    return list(q["change_list"]) + list(q["left_out"])


def check_withheld(prompt_text, q):
    """The gauge for arm (f)."""
    bad = [s for s in withheld_strings(q) if s and s in prompt_text]
    if bad:
        raise SystemExit(f"arm (f) build leaked the withheld change list: {bad[:1]}. Nothing sent.")
    return True


def identity(q, with_change_list=True):
    """What the question-identity field is compared against: a digest of the block as sent."""
    return {"question_id": q["id"], "target": q["target"],
            "change_list_sent": with_change_list,
            "quote_exchanged": bool(q.get("exchanged")),
            "quote_exchange": q.get("quote_exchange"),
            "digest": sha256_text(render(q, with_change_list))[:16]}
