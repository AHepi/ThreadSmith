"""Arm (x), the re-identification arm: exchange two names throughout a document.

A RULE and a driver (`python3 exchange.py --doc ID --texts DIR [--sources F]`), which prints
the counts and writes nothing unless --out is given.

W10 section 4: "Arm (x) is new: the same document with two named speakers' or agents' names
exchanged throughout, against the unexchanged control." The part under test is W8 A10, whose
edits are "the textual counterparts of displacement (move a passage), occlusion (withhold one)
and re-identification (exchange two labels)"; PA.3 is its prediction.

The exchange is simultaneous and whole-word: every form of name A becomes the matching form of
name B and every form of B becomes the matching form of A, in one pass, so that nothing is
swapped twice. Forms come from the manifest (A2 lists the names and may list variants) plus two
forms this program derives and records: the possessive ("Smith's") and the plural-less bare
form as given. Case is carried across: a name that appears capitalised is replaced capitalised.

The gauge: the counts per form. A document where either name was replaced zero times has not
been exchanged, and the run is void for arm (x). The driver exits non-zero on that.

What would show this design wrong: an exchanged text in which a pronoun or a role word still
points at the old name ("Smith, the defendant, said ... he" -> the arm has exchanged the label
and not the role). That is a real limit and it is not fixed here: the rig records which forms it
replaced, and the marker's arm (x) field (A4) is "which attributions moved", read against the
exchanged text as it actually is, not against an ideal one.
"""
import os, re, sys
import corpus
from rig import write_text


def forms(name, variants):
    out = []
    for n in [name] + list(variants or []):
        n = (n or "").strip()
        if not n:
            continue
        out.append(n)
        out.append(n + "'s")
        out.append(n + "’s")
    seen, uniq = set(), []
    for f in out:
        if f.lower() not in seen:
            seen.add(f.lower()); uniq.append(f)
    uniq.sort(key=len, reverse=True)
    return uniq


def _match_case(src, dst):
    if src.isupper():
        return dst.upper()
    if src[:1].isupper():
        return dst[:1].upper() + dst[1:]
    return dst


def exchange(text, a, b, a_variants=(), b_variants=()):
    """One pass, both directions. Returns (new_text, counts)."""
    fa, fb = forms(a, a_variants), forms(b, b_variants)
    if len(fa) != len(fb):
        # pair what we can, longest first, and record the leftovers
        k = min(len(fa), len(fb))
        fa, fb = fa[:k], fb[:k]
    pairs = list(zip(fa, fb))
    alts = sorted({p for pr in pairs for p in pr}, key=len, reverse=True)
    rx = re.compile(r"(?<![\w'’])(" + "|".join(re.escape(p) for p in alts) + r")(?![\w])", re.I)
    fwd = {x.lower(): y for x, y in pairs}
    rev = {y.lower(): x for x, y in pairs}
    counts = {}

    def sub(m):
        got = m.group(1)
        low = got.lower()
        to = fwd.get(low) or rev.get(low)
        if to is None:
            return got
        counts[got] = counts.get(got, 0) + 1
        return _match_case(got, to)

    return rx.sub(sub, text), counts


def totals(counts, a, b):
    ca = sum(v for k, v in counts.items() if k.lower().startswith(a.lower()))
    cb = sum(v for k, v in counts.items() if k.lower().startswith(b.lower()))
    return ca, cb


def for_document(row, text):
    n = corpus.names(row)
    if not n:
        raise SystemExit(f"{row.get('id')}: the manifest gives no two names to exchange; arm (x) cannot run on it.")
    a, b, av, bv = n
    new, counts = exchange(text, a, b, av, bv)
    ca, cb = totals(counts, a, b)
    rec = {"document": row.get("id"), "name_a": a, "name_b": b, "counts": counts,
           "replaced_a": ca, "replaced_b": cb, "void": (ca == 0 or cb == 0),
           "forms_a": forms(a, av), "forms_b": forms(b, bv)}
    return new, rec


if __name__ == "__main__":
    args = sys.argv[1:]
    def opt(name, default=None):
        for i, a in enumerate(args):
            if a == name and i + 1 < len(args):
                return args[i + 1]
        return default
    doc = opt("--doc")
    if not doc:
        print(__doc__); sys.exit(0)
    rows = corpus.manifest(opt("--sources"))
    row = rows[doc]
    text, meta = corpus.document(doc, corpus.texts_dir(args), row)
    new, rec = for_document(row, text)
    print(f"{doc}: {meta['words']} words; {rec['name_a']} <-> {rec['name_b']}; "
          f"replaced {rec['replaced_a']} and {rec['replaced_b']}; counts {rec['counts']}")
    out = opt("--out")
    if out:
        write_text(out, new)
        print("written " + out)
    sys.exit(1 if rec["void"] else 0)
