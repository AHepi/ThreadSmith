"""Arm (c)'s fixed summariser, and arm (c)'s control.

A RULE and a small driver (`python3 summariser.py --demo`). It calls no model: W3 section 5
says arm (c) hands each call "a summary of the transcript written by a fixed program", so the
program must be the same program every time and must decide nothing by taste.

The control. W8 section 4 records builder B's seam: "Arm (c) confounds length with content
(builder B): an equal-length summary omitting the parts list is proposed as the arm's control."
So there are two summarisers here, arm id `c` and arm id `cctl`:
  c    - the summary, with the parts list in it.
  cctl - the same program with the parts list removed and the words it would have used given
         to the other sections, so the two are the same length in words.
The control is never longer than the full summary; where the transcript has too little other
material to reach the length, the gap is written into the summary record as `shortfall_words`.
That number is the gauge: a control that is much shorter than the summary is not a control,
and the run says so instead of being quietly read as one.

What would show this design wrong: a pair of runs where cctl's summary differs from c's in
anything but the parts list and the depth of the other sections. The record keeps both
summaries in full, so the reviewer can diff them.
"""
import re, sys
import carryover

SECTIONS = [
    ("QUESTION",    "S12", r"(?i)\b(question|what is being explained|kind of question|frozen)\b"),
    ("JOBS",        "S12", r"(?i)\b(job|jobs|given|fixed|added|and not)\b"),
    ("PARTS",       "S3",  r".*"),
    ("CHANGE LIST", "S4",  r".*"),
    ("TESTS SO FAR","S5",  r".*"),
]
BUDGET = 400          # words for the whole summary; the same number for both summarisers


def _lines(text):
    """The lines a summary may keep, in the order they appear: headings, list items,
    and the first sentence of each other paragraph."""
    out = []
    for para in re.split(r"\n\s*\n", text or ""):
        for raw in para.split("\n"):
            s = raw.strip()
            if not s:
                continue
            if s.startswith("#") or re.match(r"^\s*([-*+]|\d+[.)])\s+", s) or s.endswith(":"):
                out.append(s)
            else:
                first = re.split(r"(?<=[.!?])\s+", s)[0]
                out.append(first)
    return [re.sub(r"\s+", " ", x).strip() for x in out if x.strip()]


def _pick(text, pattern):
    ls = _lines(text)
    if pattern == r".*":
        return ls
    keep = [l for l in ls if re.search(pattern, l)]
    return keep or ls


def _sections(replies):
    """replies: {step_id: reply_text} for the steps done so far. A carry-over note, if the reply
    carries one, is cut off first: it is a message to the next reader, not part of the step's answer,
    and leaving it in would make arm (c)'s summary depend on which arm wrote the transcript."""
    out = []
    for name, step, pat in SECTIONS:
        if replies.get(step):
            out.append((name, _pick(carryover.strip_note(replies[step]), pat)))
    return out


def _render(kept):
    parts = []
    for name, ls in kept:
        if ls:
            parts.append(name + "\n" + "\n".join(ls))
    return "\n\n".join(parts)


def _words(kept):
    return sum(len(l.split()) for _, ls in kept for l in ls)


def _grow(sections, budget, skip=()):
    """Take lines round-robin from each section, deepest-last, until the budget is reached."""
    kept = [(n, []) for n, _ in sections if n not in skip]
    idx = {n: 0 for n, _ in sections}
    pool = {n: ls for n, ls in sections}
    total, moved = 0, True
    while moved:
        moved = False
        for i, (n, got) in enumerate(kept):
            ls = pool[n]
            if idx[n] < len(ls):
                w = len(ls[idx[n]].split())
                if total + w <= budget:
                    got.append(ls[idx[n]]); idx[n] += 1; total += w; moved = True
    return kept, total


def summarise(replies, budget=BUDGET, omit_parts=False, match_words=None):
    """Return (text, record). omit_parts=True is the control (arm cctl)."""
    secs = _sections(replies)
    skip = ("PARTS",) if omit_parts else ()
    target = match_words if (omit_parts and match_words) else budget
    kept, total = _grow(secs, target, skip=skip)
    text = _render(kept)
    rec = {"budget_words": budget, "words": total, "omit_parts": omit_parts,
           "sections": [n for n, ls in kept if ls],
           "steps_in": sorted(replies.keys())}
    if omit_parts and match_words:
        rec["match_words"] = match_words
        rec["shortfall_words"] = max(0, match_words - total)
    return text, rec


def pair(replies, budget=BUDGET):
    """The summary and its equal-length control, built from the same transcript."""
    full, rfull = summarise(replies, budget=budget, omit_parts=False)
    ctl, rctl = summarise(replies, budget=budget, omit_parts=True, match_words=rfull["words"])
    return (full, rfull), (ctl, rctl)


if __name__ == "__main__":
    if "--demo" not in sys.argv:
        print(__doc__); sys.exit(0)
    demo = {
        "S12": "## Step 1\nWhat is being explained: why the bread failed to rise.\nThe kind: what produces it.\n"
               "## Step 2 jobs\n1. It rises in a warm kitchen and not in a cold one.\n2. It rises with fresh yeast and not with old.",
        "S3":  "## Parts\n1. The yeast is alive.\n2. The dough was warm enough.\n3. There was sugar for the yeast.",
        "S4":  "## Change list\n- Cool the kitchen by ten degrees.\n- Use yeast a year past its date.\n- Leave the sugar out.",
    }
    (f, rf), (c, rc) = pair(demo, budget=60)
    print("=== SUMMARY (arm c) ===\n" + f)
    print(f"\n[{rf}]")
    print("\n=== CONTROL (arm cctl), parts list omitted ===\n" + c)
    print(f"\n[{rc}]")
