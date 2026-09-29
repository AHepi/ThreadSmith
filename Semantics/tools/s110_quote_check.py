#!/usr/bin/env python3
"""s110_quote_check.py: check every book quotation in the S110 files (log S110; decisions S19, S58; lesson S29).
Written 29 September 2026 by the one Opus 5.5 agent of log S110. It holds no book text: it reads the extracted text of
the two books from a folder in the session's scratchpad, which is never put in the repository.

A book quotation in the S110 files is a passage in curly quotation marks followed, within 200 characters, by its
citation "(Marletto, ch. N)", "(Marletto, Prelude)" or "(Deutsch, ch. N)" (or a longer parenthesis ending so). For each
the script checks:
  1. the passage is an exact piece of the cited chapter's extracted text (runs of white space made single);
  2. it has at most 25 words (runs of non-space characters);
  3. it is not chained: between it and the quotation before it in the same file stand at least five words of the
     file's own (citations and punctuation not counted), or a line break.
It also flags any passage in straight quotation marks of six words or more that is an exact piece of either book
(a book quotation not marked as one), and any curly passage with no citation.

  python3 Semantics/tools/s110_quote_check.py BOOKDIR FILE.md [FILE.md ...]

BOOKDIR holds full/<NN>_*.txt for Marletto's chapters (the extraction's file names) and deutsch.txt (with its
=====PART n xhtml/chapterNNN.html===== markers). Exit 0 when every check passes, 1 otherwise.
"""
import glob, os, re, sys

M_FILES = {'Foreword': '06_', 'Prelude': '08_', '1': '09_', '2': '11_', '3': '13_', '4': '15_', '5': '17_',
           '6': '19_', '7': '21_'}
CITE = re.compile(r'\b(Marletto|Deutsch),\s*(?:ch\.\s*(\d+)|(Prelude|Foreword))\)')
CURLY = re.compile(r'“(.+?)”', re.S)
STRAIGHT = re.compile(r'(?<![\w`])"([^"\n]{20,400}?)"(?![\w`])')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def load(bookdir):
    m = {}
    for k, pre in M_FILES.items():
        fs = glob.glob(os.path.join(bookdir, 'full', pre + '*.txt'))
        m[k] = norm(open(fs[0], encoding='utf-8').read()) if fs else ''
    d = {}
    raw = open(os.path.join(bookdir, 'deutsch.txt'), encoding='utf-8').read()
    parts = re.split(r'=====PART \d+ xhtml/([\w-]+)\.html=====', raw)
    for i in range(1, len(parts) - 1, 2):
        mm = re.fullmatch(r'chapter0*(\d+)', parts[i])
        if mm:
            d[mm.group(1)] = norm(parts[i + 1])
    return m, d


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        raise SystemExit(__doc__)
    m, d = load(a[0])
    whole = ' '.join(list(m.values()) + list(d.values()))
    heads = [v[:160] for v in m.values()]   # a chapter's title, cited by name, is not a quotation
    bad = 0
    for f in a[1:]:
        text = open(f, encoding='utf-8').read()
        rows, prev_end = [], None
        for q in CURLY.finditer(text):
            quote = norm(q.group(1))
            c = CITE.search(text, q.end(), q.end() + 200)
            if not c:
                rows.append((quote, '-', 'NO CITATION'))
                bad += 1
                prev_end = q.end()
                continue
            book, ch = c.group(1), c.group(2) or c.group(3)
            src = (m if book == 'Marletto' else d).get(ch, '')
            probs = []
            if quote not in src:
                probs.append('not in the cited chapter' + (' (it is elsewhere in the books)' if quote in whole else ''))
            if len(quote.split()) > 25:
                probs.append('%d words' % len(quote.split()))
            if prev_end is not None:
                gap = text[prev_end:q.start()]
                own = CITE.sub(' ', gap)
                own = re.sub(r'\((?:the sentence|from|paraphrase)[^)]*', ' ', own)
                nwords = len(re.findall(r"[A-Za-z][A-Za-z'’-]*", own))
                if '\n' not in gap and nwords < 5:
                    probs.append('chained: %d own words since the previous quotation' % nwords)
            prev_end = q.end()
            rows.append((quote, '%s %s' % (book, ch), '; '.join(probs) or 'ok'))
            bad += bool(probs)
        for s in STRAIGHT.finditer(text):
            t = norm(s.group(1))
            if len(t.split()) >= 6 and t in whole and not any(t in h for h in heads):
                rows.append((t, '-', 'A BOOK QUOTATION IN STRAIGHT QUOTATION MARKS'))
                bad += 1
        print('## %s: %d book quotations' % (os.path.basename(f), sum(1 for r in rows if r[1] != '-')))
        for i, (qt, src, res) in enumerate(rows, 1):
            print('%3d. [%s] %d words: %s | %s' % (i, src, len(qt.split()), (qt[:60] + '...') if len(qt) > 63 else qt, res))
    print('RESULT: %s' % ('every check passes' if not bad else '%d problem(s)' % bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
