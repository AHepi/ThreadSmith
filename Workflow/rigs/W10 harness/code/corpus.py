"""The corpus, read: the manifest A2 writes, the split it freezes, and the document text.

A RULE. It fetches nothing. Plan W10 stage A gives the fetching to A2, whose fetcher
"keeps nothing in the repository", so the texts live in a folder outside the repository
and this rig is told where with --texts DIR or the environment variable W10_TEXTS.
There is no silent default: a driver with neither stops and says so.

Manifest schema. The old rig's sources.json is a list of objects with at least
id, title, author, year, domain, method, url (plan 49 rig, sources.json, entry S1:
 "id": "S1", ... "method": "arxiv", "url": "https://arxiv.org/pdf/1304.2785").
A2 extends it. This file reads only the keys it needs and names, in one closed list
each, the spellings it will accept, so that a manifest key this rig does not know
fails loudly instead of being ignored:

  the text's digest : sha256 | text_sha256 | hash        (absent -> hash_checked false, recorded)
  the two names     : exchange {a,b} | exchange {names:[a,b], exchangeable:bool}
                      | names [a,b] | speakers [a,b]   (exchangeable false -> arm (x) skips it)
  the "why" passage : why | why_passage | explanation, each either a string or an object
                      with a "quote" and, where the manifest gives one, an "explains"
  the change list   : change_list (optional; absent -> the fixed list of fixtures/frozen_question.json)

Split schema: {"arms": [ids], "reserve": [ids]} at corpus/split.json. Where that file is not
there and every row of the manifest carries a "split" of arms | reserve | spare, the split is
built from the manifest instead and the returned object says so in its "from" key, which every
driver prints. There is no third way and no silent default.
"""
import os, re, sys
from rig import SOURCES, SPLIT, read_json, sha256_text

HASH_KEYS = ["sha256", "text_sha256", "hash"]
NAME_KEYS = ["exchange", "names", "speakers"]
WHY_KEYS = ["why", "why_passage", "explanation"]


def manifest(path=None):
    rows = read_json(path or SOURCES, "the corpus manifest (A2 writes it)")
    if not isinstance(rows, list):
        raise SystemExit("sources.json must be a list of source objects, as the old rig's is. Nothing sent.")
    ids = [r["id"] for r in rows]
    if len(set(ids)) != len(ids):
        raise SystemExit(f"sources.json has repeated ids: {sorted({i for i in ids if ids.count(i) > 1})}")
    return {r["id"]: r for r in rows}


SPLIT_WORDS = {"arms": "arms", "reserve": "reserve", "spare": "reserve"}


def split(path=None, rows=None):
    p = path or SPLIT
    if not os.path.exists(p) and rows is not None:
        vals = {r.get("split") for r in rows.values()}
        if vals and vals <= set(SPLIT_WORDS):
            out = {"arms": [], "reserve": [], "from": "the manifest's per-row split field"}
            for i, r in sorted(rows.items()):
                out[SPLIT_WORDS[r["split"]]].append(i)
            return out
    d = read_json(p, "the frozen split (A2 writes it)")
    d.setdefault("from", "split.json")
    for k in ("arms", "reserve"):
        if k not in d or not isinstance(d[k], list):
            raise SystemExit(f"split.json needs the keys 'arms' and 'reserve', each a list of source ids. Got {sorted(d)}")
    both = set(d["arms"]) & set(d["reserve"])
    if both:
        raise SystemExit(f"split.json puts {sorted(both)} in both halves")
    return d


def _first(row, keys):
    for k in keys:
        if row.get(k):
            return k, row[k]
    return None, None


def names(row):
    """The two names arm (x) exchanges, as (name_a, name_b, variants_a, variants_b).
    Variants are optional lists (possessives, surnames) the manifest may give."""
    k, v = _first(row, NAME_KEYS)
    if k is None:
        return None
    if k == "exchange" and isinstance(v, dict):
        if v.get("exchangeable") is False:
            return None
        if v.get("a") and v.get("b"):
            return (v["a"], v["b"], list(v.get("a_variants") or []), list(v.get("b_variants") or []))
        ns = v.get("names")
        if isinstance(ns, (list, tuple)) and len(ns) >= 2:
            var = v.get("variants") or {}
            return (ns[0], ns[1], list(var.get(ns[0]) or []), list(var.get(ns[1]) or []))
        raise SystemExit(f"{row.get('id')}: cannot read the two names out of exchange={v!r}")
    if isinstance(v, (list, tuple)) and len(v) >= 2:
        return (v[0], v[1], [], [])
    raise SystemExit(f"{row.get('id')}: cannot read the two names out of {k}={v!r}")


def why(row):
    """The passage the document explains, as (text, quote). text is what the frozen question's
    target line is built from; quote is the document's own sentence, where the manifest gives one."""
    _, v = _first(row, WHY_KEYS)
    if v is None:
        return None, None
    if isinstance(v, dict):
        return (v.get("explains") or v.get("quote"), v.get("quote"))
    return (str(v), None)


def texts_dir(argv):
    for i, a in enumerate(argv):
        if a == "--texts" and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith("--texts="):
            return a.split("=", 1)[1]
    d = os.environ.get("W10_TEXTS", "")
    if d:
        return d
    raise SystemExit("no document folder: pass --texts DIR or set W10_TEXTS. "
                     "A2's fetcher keeps no text in the repository. Nothing sent.")


def joined(text):
    """Join line breaks inside paragraphs so one call reads the document as paragraphs
    (the old rig's sonnet_agent.py does the same); paragraph breaks are kept."""
    return "\n\n".join(re.sub(r"\s*\n\s*", " ", p).strip()
                       for p in re.split(r"\n\s*\n", text) if p.strip())


def document(doc_id, tdir, row=None, check_hash=True):
    """Return (text, meta). The provenance header the fetcher writes is stripped and never sent
    (the old fetch.py writes "# (provenance header; removed before the text is sent to any reader)")."""
    p = os.path.join(tdir, f"{doc_id}.txt")
    if not os.path.exists(p):
        raise SystemExit(f"no text for {doc_id} at {p}; run A2's fetcher into that folder. Nothing sent.")
    raw = open(p, encoding="utf-8").read()
    body = raw.split("\n\n", 1)[1].strip() if raw.startswith("#") and "\n\n" in raw else raw.strip()
    meta = {"path": p, "words": len(body.split()), "sha256": sha256_text(body), "hash_checked": False}
    if row is not None and check_hash:
        k, want = _first(row, HASH_KEYS)
        if want:
            meta["hash_checked"] = True
            meta["hash_key"] = k
            if want not in (meta["sha256"], sha256_text(raw)):
                raise SystemExit(f"{doc_id}: the text does not match the manifest {k}. Nothing sent.")
    return joined(body), meta


if __name__ == "__main__":
    src = None
    for i, a in enumerate(sys.argv):
        if a == "--sources":
            src = sys.argv[i + 1]
    m = manifest(src)
    print(f"{len(m)} sources in {src or SOURCES}")
    for i, r in m.items():
        n = names(r)
        w, q = why(r)
        print(f"  {i:6} {r.get('domain',''):12} names={'yes ' + str(n[:2]) if n else 'no'}  "
              f"why={'yes' if w else 'NO'}  quoted={'yes' if q else 'no'}")
