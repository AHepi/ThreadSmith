"""Phase 0 of plan 49: fetch every source, extract text, trim, write corpus/<id>.txt.
No DeepSeek call is made here. Nothing is sent anywhere; this only downloads and trims.
Resumable: a source whose corpus file exists is skipped unless --force."""
import json, os, re, sys, subprocess, html as ihtml
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (compatible; hard-to-vary corpus fetch)"
CAP = 18000            # words; about 24,000 word-pieces
MIN_WORDS = 700        # below this the fetch is called failed

def get(url, out):
    r = subprocess.run(["curl","-sS","-m","180","-L","-A",UA,"-o",out,"-w","%{http_code}",url],
                       capture_output=True, text=True)
    return r.stdout.strip()

def strip_html(t):
    t = re.sub(r"(?is)<(script|style|nav|footer|header|form)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<!--.*?-->", " ", t)
    t = re.sub(r"(?i)<(p|br|/p|div|/div|h[1-6]|/h[1-6]|li|/tr)[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = ihtml.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()

def pdf_text(path, pages=None):
    import pymupdf
    d = pymupdf.open(path)
    lo, hi = (pages or [1, len(d)])
    parts = [d[i].get_text() for i in range(lo-1, min(hi, len(d)))]
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", "\n".join(parts)).strip()

def gutenberg(t):
    m = re.search(r"\*\*\* ?START OF TH[EIS]+ PROJECT GUTENBERG EBOOK.*?\*\*\*", t, re.S)
    if m: t = t[m.end():]
    m = re.search(r"\*\*\* ?END OF TH[EIS]+ PROJECT GUTENBERG EBOOK", t)
    if m: t = t[:m.start()]
    return t.strip()

def pmc(pmcid, out):
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&rettype=xml")
    code = get(url, out)
    x = open(out, encoding="utf-8", errors="ignore").read()
    ti = re.search(r"<article-title>(.*?)</article-title>", x, re.S)
    title = re.sub(r"<[^>]+>", "", ti.group(1)).strip() if ti else ""
    b = re.search(r"<body>.*</body>", x, re.S)
    body = b.group(0) if b else x
    body = re.sub(r"(?is)<(table-wrap|fig|ref-list|xref)[^>]*>.*?</\1>", " ", body)
    body = re.sub(r"(?i)<(p|title|sec)[^>]*>", "\n", body)
    return title, re.sub(r"\n\s*\n\s*\n+", "\n\n", re.sub(r"[ \t]+"," ", ihtml.unescape(re.sub(r"<[^>]+>"," ",body)))).strip(), code

def trim(t, s):
    note = []
    if s.get("start"):
        ms = list(re.finditer(s["start"], t))
        if ms:
            nth = s.get("start_nth", -1)
            m = ms[nth if nth < 0 else min(nth, len(ms)) - 1]
            t = t[m.start():]
        else: note.append("start marker not found")
    if s.get("end"):
        m = re.search(s["end"], t[200:])
        if m: t = t[:200 + m.start()]
        else: note.append("end marker not found")
    # cut reference lists and acknowledgements where they clearly begin
    m = None if s.get("no_ref_cut") else re.search(r"\n\s*(REFERENCES|References|Bibliography|BIBLIOGRAPHY|Acknowledg[e]?ments?|ACKNOWLEDG)\s*\n", t)
    if m and len(t[:m.start()].split()) > MIN_WORDS:
        t = t[:m.start()]; note.append("references cut")
    cap = s.get("words_cap", CAP)
    w = t.split()
    if len(w) > cap:
        cut = " ".join(w[:cap])
        p = cut.rfind("\n\n")
        t = cut[:p] if p > len(cut)*0.6 else cut
        note.append(f"capped at {cap} words")
    return t.strip(), note

def main():
    force = "--force" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    srcs = json.load(open(f"{HERE}/sources.json"))
    if only: srcs = [s for s in srcs if s["id"] in only]
    os.makedirs(f"{HERE}/corpus", exist_ok=True); os.makedirs(f"{HERE}/raw", exist_ok=True)
    rows = []
    for s in srcs:
        out = f"{HERE}/corpus/{s['id']}.txt"
        if os.path.exists(out) and not force:
            w = len(open(out,encoding='utf-8').read().split()); rows.append((s['id'],"skip",w,"")); continue
        raw = f"{HERE}/raw/{s['id']}.bin"
        title_seen = ""; note = []
        try:
            if s["method"] in ("arxiv","pdf") and not s.get("is_text"):
                code = get(s["url"], raw)
                if code != "200": raise RuntimeError(f"HTTP {code}")
                t = pdf_text(raw, s.get("pages"))
            elif s["method"] == "pmc":
                title_seen, t, code = pmc(s["url"], raw)
            elif s["method"] == "gutenberg":
                code = get(s["url"], raw); t = gutenberg(open(raw,encoding="utf-8",errors="ignore").read())
            else:  # html or plain text
                code = get(s["url"], raw)
                body = open(raw, encoding="utf-8", errors="ignore").read()
                t = body if s.get("is_text") else strip_html(body)
            t, note = trim(t, s)
            words = len(t.split())
            status = "ok" if words >= s.get("min_words", MIN_WORDS) else "TOO SHORT"
            hdr = (f"# SOURCE {s['id']}\n# title: {s['title']}\n# author: {s['author']}  year: {s['year']}\n"
                   f"# from: {s['url']}\n# method: {s['method']}  trim: {'; '.join(note) or 'none'}\n"
                   f"# words: {words}\n# (provenance header; removed before the text is sent to any reader)\n\n")
            open(out,"w",encoding="utf-8").write(hdr + t)
            rows.append((s['id'], status, words, "; ".join(note) + (f" [pmc title: {title_seen[:60]}]" if title_seen else "")))
        except Exception as e:
            rows.append((s['id'], "FAIL", 0, repr(e)[:90]))
    print(f"{'id':6} {'status':9} {'words':>7}  note")
    for r in rows: print(f"{r[0]:6} {r[1]:9} {r[2]:>7}  {r[3][:88]}")
    ok=[r for r in rows if r[1] in ("ok","skip")]
    print(f"\n{len(ok)}/{len(rows)} usable; total words {sum(r[2] for r in ok)}; "
          f"est. word-pieces {int(sum(r[2] for r in ok)*1.35)}")
if __name__ == "__main__": main()
