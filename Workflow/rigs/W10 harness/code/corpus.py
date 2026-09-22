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
                      where the value is a block (A2 writes one), the digest of the text is
                      read from text_sha256 | sha256 inside it and the digest of the fetched
                      bytes from raw_sha256. A spelling inside the block that looks like a
                      digest and is not in those closed lists fails loudly; the block's
                      bookkeeping keys (words, chars, fetched, hash_of, extractor) are ignored.
                      A2's raw_sha256 is the digest of the bytes the fetcher downloaded, which
                      no reader of the saved text can recompute, so it is recorded and not
                      compared; the comparison is on the text digest. (fault 6)
  the two names     : exchange {a,b} | exchange {names:[a,b], exchangeable:bool}
                      | names [a,b] | speakers [a,b]   (exchangeable false -> arm (x) skips it)
  the "why" passage : why | why_passage | explanation, each either a string or an object
                      with a "quote" and, where the manifest gives one, an "explains"
  the change list   : change_list (optional; absent -> the fixed list of fixtures/frozen_question.json)

Split schema: three lists at corpus/split.json, the arms, the reserve and the held out. Each
list holds either an id string or an object with an "id" (A2 writes objects). The held-out list
is read from not_in_the_split | held_out | out_of_the_split. Where that file is not there and
every row of the manifest carries a "split" of arms | reserve | spare, the split is built from
the manifest instead, "spare" meaning held out, and the returned object says so in its "from"
key, which every driver prints. There is no third way and no silent default.

A held-out document is never handed to a driver: split() returns the three lists apart and
held_out_ids() is what a driver checks --docs against. W10 section 12 names "spending the 33
held-out sources" as a trap, and split.json says of the five: "They are not spares to be swapped
in silently: using one is a change to the split and a new claim." (faults 7 and 19)
"""
import os, re, sys
from rig import SOURCES, SPLIT, read_json, sha256_text

HASH_KEYS = ["sha256", "text_sha256", "hash"]
# Inside a digest block (row["hash"] = {...}): the closed lists, and the keys that are
# bookkeeping and not a digest.
HASH_BLOCK_TEXT = ["text_sha256", "sha256"]
HASH_BLOCK_RAW = ["raw_sha256"]
HASH_BLOCK_NOT_A_DIGEST = ["words", "chars", "fetched", "hash_of", "extractor"]
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


SPLIT_WORDS = {"arms": "arms", "reserve": "reserve", "spare": "held_out"}
HELD_OUT_KEYS = ["held_out", "not_in_the_split", "out_of_the_split"]


def _ids(v, where):
    """A split list is ids or objects carrying an "id". A2 writes objects."""
    if not isinstance(v, list):
        raise SystemExit(f"{where} must be a list of source ids or of objects with an 'id'. Got {type(v).__name__}")
    out = []
    for r in v:
        if isinstance(r, str):
            out.append(r)
        elif isinstance(r, dict) and isinstance(r.get("id"), str):
            out.append(r["id"])
        else:
            raise SystemExit(f"{where}: cannot read a source id out of {r!r}")
    return out


def split(path=None, rows=None):
    """The three lists, kept apart. held_out is recorded and never handed to a driver."""
    p = path or SPLIT
    if not os.path.exists(p) and rows is not None:
        vals = {r.get("split") for r in rows.values()}
        if vals and vals <= set(SPLIT_WORDS):
            out = {"arms": [], "reserve": [], "held_out": [],
                   "from": "the manifest's per-row split field"}
            for i, r in sorted(rows.items()):
                out[SPLIT_WORDS[r["split"]]].append(i)
            _no_overlap(out, "the manifest's per-row split field")
            return out
    d = read_json(p, "the frozen split (A2 writes it)")
    out = {"from": d.get("from", "split.json")}
    for k in ("arms", "reserve"):
        if k not in d:
            raise SystemExit(f"split.json needs the keys 'arms' and 'reserve', each a list of "
                             f"source ids or of objects with an 'id'. Got {sorted(d)}")
        out[k] = _ids(d[k], f"split.json's {k!r}")
    k, v = _first(d, HELD_OUT_KEYS)
    out["held_out"] = _ids(v, f"split.json's {k!r}") if v else []
    out["held_out_key"] = k
    _no_overlap(out, p)
    return out


def _no_overlap(d, where):
    names = ("arms", "reserve", "held_out")
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            both = set(d.get(a) or []) & set(d.get(b) or [])
            if both:
                raise SystemExit(f"{where} puts {sorted(both)} in both {a} and {b}")
    return True


def held_out_ids(path=None, rows=None):
    """What a driver refuses to run on. Using one is a change to the split and a new claim
    (split.json, what_a_freeze_means_here); W10 section 12 names spending them as a trap."""
    return list(split(path, rows).get("held_out") or [])


def _first(row, keys):
    for k in keys:
        if row.get(k):
            return k, row[k]
    return None, None


def digest(row):
    """(key, text_digest, raw_digest) out of the manifest row, or (None, None, None).

    A2 writes a block: "hash": {"text_sha256": ..., "raw_sha256": ..., "words": ...}. The
    closed-list rule is kept where it bites: a key inside the block that looks like a digest
    (sha256, a *_sha256, a digest or hash) and is not one this rig knows stops the run rather
    than being ignored."""
    k, v = _first(row, HASH_KEYS)
    if v is None:
        return None, None, None
    if isinstance(v, str):
        return k, v, None
    if not isinstance(v, dict):
        raise SystemExit(f"{row.get('id')}: cannot read a digest out of {k}={v!r}")
    known = set(HASH_BLOCK_TEXT) | set(HASH_BLOCK_RAW) | set(HASH_BLOCK_NOT_A_DIGEST)
    unknown = [kk for kk in v
               if kk not in known and (kk.endswith("sha256") or "digest" in kk or "hash" in kk)]
    if unknown:
        raise SystemExit(f"{row.get('id')}: the manifest's {k!r} block carries digest key(s) "
                         f"{sorted(unknown)} this rig does not know. Nothing sent.")
    t = next((v[x] for x in HASH_BLOCK_TEXT if v.get(x)), None)
    r = next((v[x] for x in HASH_BLOCK_RAW if v.get(x)), None)
    if not t and not r:
        raise SystemExit(f"{row.get('id')}: the manifest's {k!r} block carries no digest this "
                         f"rig knows ({HASH_BLOCK_TEXT + HASH_BLOCK_RAW}). Nothing sent.")
    return k, t, r


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
        k, want_text, want_raw = digest(row)
        if want_text:
            meta["hash_checked"] = True
            meta["hash_key"] = k
            meta["hash_compared"] = "the manifest's text digest against the text with the "
            meta["hash_compared"] += "fetcher's provenance header removed"
            if want_text not in (meta["sha256"], sha256_text(raw)):
                raise SystemExit(f"{doc_id}: the text does not match the manifest {k}. Nothing sent.")
        elif want_raw:
            # A2's raw_sha256 is the digest of the bytes the fetcher downloaded. Nothing that
            # reads the saved text can recompute it, so it is recorded and not compared.
            meta["hash_key"] = k
            meta["raw_sha256_in_manifest"] = want_raw
            meta["hash_not_checked_because"] = ("the manifest gives only the digest of the fetched "
                                                "bytes, which the saved text cannot reproduce")
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
        _, td, rd = digest(r)
        print(f"  {i:6} {r.get('domain',''):12} names={'yes ' + str(n[:2]) if n else 'no'}  "
              f"why={'yes' if w else 'NO'}  quoted={'yes' if q else 'no'}  "
              f"digest={'text' if td else ('raw only' if rd else 'NO')}")
    try:
        sp = split(rows=m)
        print(f"  split from {sp['from']}: arms {len(sp['arms'])}, reserve {len(sp['reserve'])}, "
              f"held out {len(sp['held_out'])} (never handed to a driver)")
    except SystemExit as e:
        print(f"  split: {e}")
