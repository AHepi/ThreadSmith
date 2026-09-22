"""W10 stage A2: fetch the corpus by address, extract the text, verify the hash.

Modelled on the plan 49 rig's fetch.py (same trim rule, same method names, the
same "written by program from the address in its header" discipline), with four
changes the W10 plan and task force:

  1. Nothing is written inside the repository. The only writing mode (--out)
     refuses a directory under the repository root, so no fetched text is kept
     here. Default mode writes nothing at all.
  2. Every source carries a hash in sources.json. Every fetch recomputes it and
     says match / DIFFERS, so a later fetch can be checked against the one that
     was frozen on 22 September 2026.
  3. --probe prints what a new candidate would score (words, hashes, the
     sentences that answer "why", the names that occur most often), which is how
     the manifest's why_passage and exchange fields were filled.
  4. --dry-run sends nothing: it prints the address it would fetch and stops.
     No key is read and no API is called anywhere in this file.

Usage
  python3 fetch.py --dry-run              # sends nothing; lists the addresses
  python3 fetch.py --check                # fetches, verifies hashes, writes nothing
  python3 fetch.py --probe W3 W7          # fetches, prints words/hash/why/names
  python3 fetch.py --out /tmp/w10corpus   # fetches and writes <id>.txt OUTSIDE the repo
  python3 fetch.py --freeze W3            # prints the hash block to paste in sources.json
  python3 fetch.py --audit                # checks the manifest against the text: band, hash,
                                          # that each why_passage quotation really occurs, and
                                          # how often each exchangeable name occurs

The text that is hashed is the text a reader would be handed: extracted,
trimmed by this file's rule, normalised (CRLF to LF, trailing spaces dropped,
runs of blank lines collapsed, NFC). The provenance header is NOT hashed.
"""
import argparse, hashlib, html as ihtml, json, os, re, subprocess, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))   # /home/user/ThreadSmith
UA = "Mozilla/5.0 (compatible; W10 corpus fetch; one fetch per source)"
CAP = 6000            # words; the band the task fixes is 1,500 to 6,000
MIN_WORDS = 1500      # below this a source is out of band, not usable
MAX_WORDS = 6000


# ---------------------------------------------------------------- fetching

def get(url, out):
    """One curl. Returns the HTTP code as a string. Nothing is sent but the GET."""
    r = subprocess.run(["curl", "-sS", "-m", "180", "-L", "-A", UA,
                        "-o", out, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    return r.stdout.strip()


def strip_html(t):
    t = re.sub(r"(?is)<(script|style|nav|footer|header|form|aside|noscript)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<!--.*?-->", " ", t)
    t = re.sub(r"(?i)<(p|br|/p|div|/div|h[1-6]|/h[1-6]|li|/tr|/dd|blockquote)[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = ihtml.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()


def pdf_text(path, pages=None):
    import pymupdf
    d = pymupdf.open(path)
    lo, hi = (pages or [1, len(d)])
    parts = [d[i].get_text() for i in range(lo - 1, min(hi, len(d)))]
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", "\n".join(parts)).strip()


def gutenberg(t):
    m = re.search(r"\*\*\* ?START OF TH[EIS]+ PROJECT GUTENBERG EBOOK.*?\*\*\*", t, re.S)
    if m:
        t = t[m.end():]
    m = re.search(r"\*\*\* ?END OF TH[EIS]+ PROJECT GUTENBERG EBOOK", t)
    if m:
        t = t[:m.start()]
    return t.strip()


def pmc(pmcid, out):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&rettype=xml"
    code = get(url, out)
    x = open(out, encoding="utf-8", errors="ignore").read()
    ti = re.search(r"<article-title>(.*?)</article-title>", x, re.S)
    title = re.sub(r"<[^>]+>", "", ti.group(1)).strip() if ti else ""
    b = re.search(r"<body>.*</body>", x, re.S)
    body = b.group(0) if b else x
    body = re.sub(r"(?is)<(table-wrap|fig|ref-list|xref)[^>]*>.*?</\1>", " ", body)
    body = re.sub(r"(?i)<(p|title|sec)[^>]*>", "\n", body)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"[ \t]+", " ", ihtml.unescape(body))
    return title, re.sub(r"\n\s*\n\s*\n+", "\n\n", body).strip(), code


def caselaw(url, out):
    """Caselaw Access Project static JSON: the case name, then each opinion with its author.
    The head matter (syllabus, counsel) is left out, so what a reader sees is the judges' own
    reasoning and nothing else."""
    code = get(url, out)
    j = json.load(open(out, encoding="utf-8"))
    body = j.get("casebody") or {}
    ops = body.get("opinions") or []
    parts = [j.get("name") or j.get("name_abbreviation", ""), j.get("decision_date", "")]
    for o in ops:
        head = (o.get("author") or o.get("type") or "").strip()
        text = (o.get("text") or "").strip()
        parts.append(f"\n\n{text}" if head and text.startswith(head) else f"\n\n{head}\n\n{text}")
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", "\n".join(p for p in parts if p)).strip(), code


def wikisource(page, out):
    """The REST html endpoint gives the article body without the site's chrome."""
    url = f"https://en.wikisource.org/api/rest_v1/page/html/{page}"
    code = get(url, out)
    body = open(out, encoding="utf-8", errors="ignore").read()
    body = re.sub(r"(?is)<(table|sup|style|script)[^>]*>.*?</\1>", " ", body)
    return strip_html(body), code


# ---------------------------------------------------------------- trimming

def trim(t, s):
    """The plan 49 rule, with the W10 band. Every cut is reported in `note`."""
    note = []
    if s.get("start"):
        ms = list(re.finditer(s["start"], t))
        if ms:
            nth = s.get("start_nth", -1)
            m = ms[nth if nth < 0 else min(nth, len(ms)) - 1]
            t = t[m.start():]
            note.append("start marker")
        else:
            note.append("START MARKER NOT FOUND")
    if s.get("end"):
        m = re.search(s["end"], t[200:])
        if m:
            t = t[:200 + m.start()]
            note.append("end marker")
        else:
            note.append("END MARKER NOT FOUND")
    m = None if s.get("no_ref_cut") else re.search(
        r"\n\s*(REFERENCES|References|Bibliography|BIBLIOGRAPHY|Acknowledg[e]?ments?|ACKNOWLEDG)\s*\n", t)
    if m and len(t[:m.start()].split()) > MIN_WORDS:
        t = t[:m.start()]
        note.append("references cut")
    cap = s.get("words_cap", CAP)
    w = t.split()
    if len(w) > cap:
        cut = " ".join(w[:cap])
        p = cut.rfind("\n\n")
        t = cut[:p] if p > len(cut) * 0.6 else cut
        note.append(f"capped at {cap} words")
    return t.strip(), note


def normalise(t):
    """What is hashed. Cosmetic differences between fetches must not break the check."""
    t = unicodedata.normalize("NFC", t.replace("\r\n", "\n").replace("\r", "\n"))
    t = "\n".join(line.rstrip() for line in t.split("\n"))
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- one source

def fetch_one(s, tmpdir):
    """Fetch, extract, trim, normalise. Returns (text, note, raw_sha, http_code)."""
    raw = os.path.join(tmpdir, f"{s['id']}.bin")
    note, code, title_seen = [], "", ""
    if s["method"] in ("arxiv", "pdf") and not s.get("is_text"):
        code = get(s["url"], raw)
        if code != "200":
            raise RuntimeError(f"HTTP {code}")
        t = pdf_text(raw, s.get("pages"))
        note.append(f"pdf pages {s.get('pages') or 'all'}")
    elif s["method"] == "pmc":
        title_seen, t, code = pmc(s["url"], raw)
    elif s["method"] == "wikisource":
        t, code = wikisource(s["url"], raw)
    elif s["method"] == "caselaw":
        t, code = caselaw(s["url"], raw)
    elif s["method"] == "gutenberg":
        code = get(s["url"], raw)
        if code != "200":
            raise RuntimeError(f"HTTP {code}")
        t = gutenberg(open(raw, encoding="utf-8", errors="ignore").read())
    else:                                    # html, or plain text
        code = get(s["url"], raw)
        if code != "200":
            raise RuntimeError(f"HTTP {code}")
        body = open(raw, encoding="utf-8", errors="ignore").read()
        t = body if s.get("is_text") else strip_html(body)
    raw_sha = sha(open(raw, "rb").read())
    pre = t
    t, tnote = trim(t, s)
    if title_seen:
        tnote.append(f"[pmc title: {title_seen[:60]}]")
    return normalise(t), note + tnote, raw_sha, code, pre


def header(s, words, note):
    return (f"# SOURCE {s['id']}\n# title: {s['title']}\n"
            f"# author: {s['author']}  year: {s['year']}\n"
            f"# from: {s['url']}\n# method: {s['method']}  trim: {'; '.join(note) or 'none'}\n"
            f"# licence: {s.get('licence','')}\n# words: {words}\n"
            f"# (provenance header; not hashed; removed before the text is sent to any reader)\n\n")


# ---------------------------------------------------------------- probing

WHY = re.compile(r"\b(because|therefore|the reason|reason why|that is why|hence|"
                 r"consequently|so that|it follows|thus|in order to|explains? why|due to)\b", re.I)


def sentences(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", t.replace("\n", " ")) if x.strip()]


def why_lines(t, n=8):
    return [x for x in sentences(t) if WHY.search(x) and 60 < len(x) < 420][:n]


STOP = set("""The This That These Those And But For With From What When Where Which While If Then There
It He She They We You I A An In On At Of To By As Or Not No So Now Thus Hence Also After Before Such
One Two Three First Second Third Chapter Part Section Figure Table Page Its His Her Their Our Your My
Mr Mrs Dr Sir Lord God But Yet Let Do Does Did Have Has Had Will Would Shall Should May Might Can Could
All Any Some Each Every Both Other Another Same Own Only Even Just Very Much More Most Less Least""".split())


def names(t, n=14):
    """Capitalised tokens that are not sentence openers, most frequent first."""
    counts = {}
    for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-zA-Z'’-]{2,})\b", t, re.M):
        w = m.group(1)
        if w in STOP:
            continue
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])[:n]


def speakers(t, n=10):
    """Lines that open with a name in a dialogue's shape (NAME: or NAME.)."""
    counts = {}
    for m in re.finditer(r"^\s*([A-Z][A-Za-z'’ -]{2,24})\s*[:.]\s", t, re.M):
        w = m.group(1).strip()
        if w.upper() in {s.upper() for s in STOP}:
            continue
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])[:n]


# ---------------------------------------------------------------- main

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guard(out):
    """Nothing is written inside the repository. This is the task's rule, in code."""
    out = os.path.abspath(out)
    if os.path.commonpath([out, REPO]) == REPO:
        sys.exit(f"refusing to write inside the repository: {out}\n"
                 f"(the corpus text is never kept here; pass --out with a path outside {REPO})")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--sources", default=os.path.join(HERE, "sources.json"))
    ap.add_argument("--dry-run", action="store_true", help="send nothing; print the addresses")
    ap.add_argument("--check", action="store_true", help="fetch and verify hashes; write nothing")
    ap.add_argument("--probe", action="store_true", help="fetch and print words, hash, why, names")
    ap.add_argument("--freeze", action="store_true", help="print the hash block for sources.json")
    ap.add_argument("--write-hashes", action="store_true",
                    help="fill a MISSING hash in sources.json from this fetch; an existing hash is "
                         "never overwritten (that is what freezing means) unless --force-hash")
    ap.add_argument("--force-hash", action="store_true",
                    help="overwrite an existing hash: this unfreezes a source and is a new claim")
    ap.add_argument("--grep", help="print the lines of the TRIMMED text that match this pattern "
                                   "(how the why_passage quotations were taken); writes nothing")
    ap.add_argument("--grep-raw", help="the same over the UNTRIMMED text (how the start and end "
                                       "markers were found); writes nothing")
    ap.add_argument("--out", help="directory OUTSIDE the repository to write <id>.txt into")
    ap.add_argument("--no-header", action="store_true", help="write the text without the provenance header")
    ap.add_argument("--strict", action="store_true", help="with --out, refuse to write a source whose hash differs")
    ap.add_argument("--audit", action="store_true",
                    help="fetch and check the manifest against the text: the band, the hash, that the "
                         "why_passage quotation really occurs in the text, and that each exchangeable "
                         "name really occurs; writes nothing")
    a = ap.parse_args()

    srcs = load(a.sources)
    if a.ids:
        srcs = [s for s in srcs if s["id"] in a.ids]
    if not srcs:
        sys.exit("no sources selected")

    if a.dry_run:
        print(f"{'id':6} {'method':10} {'band':13} address")
        for s in srcs:
            b = f"{s.get('hash',{}).get('words','?')} w"
            print(f"{s['id']:6} {s['method']:10} {b:13} {s['url']}")
        print(f"\n{len(srcs)} sources. Nothing was fetched and nothing was sent.")
        return

    import tempfile, shutil
    tmp = tempfile.mkdtemp(prefix="w10fetch.")          # outside the repository, deleted below
    out = guard(a.out) if a.out else None
    if out:
        os.makedirs(out, exist_ok=True)
    rows, changed = [], False
    try:
        for s in srcs:
            try:
                t, note, raw_sha, code, pre = fetch_one(s, tmp)
                for pat, which, body in ((a.grep, "trimmed", t), (a.grep_raw, "untrimmed", pre)):
                    if not pat:
                        continue
                    print(f"===== {s['id']}  lines of the {which} text matching {pat!r} "
                          f"({len(body.split())} words)")
                    lines = body.split("\n")
                    for i, line in enumerate(lines):
                        if re.search(pat, line):
                            print(f"  {i:6} {line[:300]}")
                            for j in (i + 1, i + 2):          # two lines of context
                                if j < len(lines) and lines[j].strip():
                                    print(f"  {'':6} {lines[j][:300]}")
                words = len(t.split())
                h = s.get("hash") or {}
                text_sha = sha(t)
                verdict = ("no hash yet" if not h.get("text_sha256")
                           else "match" if h["text_sha256"] == text_sha
                           else "raw match, text DIFFERS" if h.get("raw_sha256") == raw_sha
                           else "DIFFERS")
                band = "in band" if MIN_WORDS <= words <= MAX_WORDS else "OUT OF BAND"
                rows.append((s["id"], code, words, band, verdict, "; ".join(note)))
                if a.probe:
                    print(f"\n===== {s['id']}  {s['title'][:70]}")
                    print(f"  http {code}  words {words}  {band}  trim: {'; '.join(note) or 'none'}")
                    print(f"  text_sha256 {text_sha}")
                    print(f"  raw_sha256  {raw_sha}")
                    print(f"  opens: {t[:180]!r}")
                    print(f"  ends:  {t[-180:]!r}")
                    print("  names:", ", ".join(f"{w}({c})" for w, c in names(t)))
                    sp = speakers(t)
                    if sp:
                        print("  speaker lines:", ", ".join(f"{w}({c})" for w, c in sp))
                    print("  why:")
                    for x in why_lines(t):
                        print("   -", x[:300])
                block = {"text_sha256": text_sha, "raw_sha256": raw_sha,
                         "words": words, "chars": len(t), "fetched": "2026-09-22",
                         "hash_of": "the trimmed, normalised text; the header is not hashed",
                         "extractor": ("pymupdf " + __import__("pymupdf").VersionBind
                                       if s["method"] in ("pdf", "arxiv") and not s.get("is_text")
                                       else "this file's strip_html/regex extraction")}
                if a.freeze:
                    print(json.dumps({"id": s["id"], "hash": block}, indent=1))
                if a.audit:
                    flat = re.sub(r"\s+", " ", t)
                    faults, counts = [], []
                    if band != "in band":
                        faults.append(f"{words} words is outside 1,500 to 6,000")
                    if verdict not in ("match", "no hash yet"):
                        faults.append("hash " + verdict)
                    for field in ("licence", "licence_how_i_know", "split"):
                        if not s.get(field):
                            faults.append(f"no {field}")
                    q = re.sub(r"\s+", " ", (s.get("why_passage") or {}).get("quote", "")).strip()
                    if not q:
                        faults.append("no why_passage quotation")
                    elif q not in flat:
                        faults.append("the why_passage quotation is NOT in the text")
                    ex = s.get("exchange") or {}
                    if ex.get("exchangeable"):
                        for n in ex.get("names", []):
                            c = len(re.findall(re.escape(n), flat))
                            counts.append(f"{n}×{c}")
                            if c == 0:
                                faults.append(f"the exchangeable name {n!r} does not occur")
                    print(f"{s['id']:6} {'OK' if not faults else 'FAULT'}  "
                          f"{'; '.join(faults)}{'  [' + ', '.join(counts) + ']' if counts else ''}")
                if a.write_hashes:
                    if h.get("text_sha256") and not a.force_hash:
                        rows[-1] = rows[-1][:5] + ("hash already frozen; not touched",)
                    else:
                        s["hash"] = block
                        changed = True
                if out:
                    if a.strict and verdict.endswith("DIFFERS"):
                        rows[-1] = rows[-1][:4] + ("REFUSED: " + verdict, rows[-1][5])
                        continue
                    p = os.path.join(out, f"{s['id']}.txt")
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(("" if a.no_header else header(s, words, note)) + t)
            except Exception as e:
                rows.append((s["id"], "-", 0, "FAIL", repr(e)[:60], ""))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)          # the fetched bytes are not kept
    if a.write_hashes and changed:
        all_srcs = load(a.sources)
        by_id = {x["id"]: x for x in srcs}
        for x in all_srcs:
            if x["id"] in by_id and by_id[x["id"]].get("hash"):
                x["hash"] = by_id[x["id"]]["hash"]
        with open(a.sources, "w", encoding="utf-8") as f:
            json.dump(all_srcs, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"hashes written into {a.sources}")

    print(f"\n{'id':6} {'code':5} {'words':>6} {'band':12} {'hash':24} note")
    for r in rows:
        print(f"{r[0]:6} {r[1]:5} {r[2]:>6} {r[3]:12} {r[4]:24} {r[5][:40]}")
    ok = [r for r in rows if r[3] == "in band" and r[4] in ("match", "no hash yet")]
    print(f"\n{len(ok)}/{len(rows)} in band and hash-clean; total words {sum(r[2] for r in ok)}")
    if out:
        print(f"written to {out} (outside the repository; delete it when the round ends)")
    else:
        print("nothing was written; no text is kept in the repository")


if __name__ == "__main__":
    main()
