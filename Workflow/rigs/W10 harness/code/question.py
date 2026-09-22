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

The gauge, run on every build: no sentence of the withheld change list appears anywhere in
an arm (f) prompt. If one does, the build stops.
"""
import os, json
from rig import FIXTURES, sha256_text

FROZEN = os.path.join(FIXTURES, "frozen_question.json")


def load(path=None):
    with open(path or FROZEN, encoding="utf-8") as f:
        return json.load(f)


def for_document(row, q=None):
    """The frozen question for one document: the fixed object with its target line filled in
    from the manifest's "why" passage, and the document's own sentence quoted where the manifest
    gives one, so that every arm is handed the same target word for word."""
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
    return out


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
            "digest": sha256_text(render(q, with_change_list))[:16]}
