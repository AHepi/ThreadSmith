#!/usr/bin/env python3
"""s117_list_the_units_of_the_semantics.py

What it does, in plain words: for log S117, makes the list of the semantics' units that the Avida work is lined up
against: every numbered definition (D...) and worked encoding (E...) of the formal core after round 4, every formal
claim (FC...) after round 4 with its status, and the named terms of the text that the formal core does not define
(written out by hand below, each with its line in the text). For each it records the line in the file it comes from.
It reads only; it writes one JSON file into the scratch space (s117/units.json) and prints the counts.

  python3 -B Semantics/tools/s117_list_the_units_of_the_semantics.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATHS = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading')
CORE = os.path.join(MATHS, 'formal core, after round 4.md')
CLAIMS = os.path.join(MATHS, 'formal claims, after round 4.json')
CLAIMS_MD = os.path.join(MATHS, 'formal claims, after round 4.md')
TEXT = os.path.join(ROOT, 'tests', '107 The semantics, standing alone, after round 4.md')
OUT = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s117/units.json'

# Named terms of the text that the formal core quotes or relies on but does not define (line numbers in TEXT).
TERMS = [
    ('T01', 'The constitutive conjecture', 17),
    ('T02', 'Faithfulness without assessors (Part I)', 67),
    ('T03', 'Fallibility without error-as-work (Part I)', 69),
    ('T04', 'Conjecture, criticism, action (Part I)', 71),
    ('T05', 'Recursive scrutiny with operative return (Part I)', 73),
    ('T06', 'Substrate independence with physical conditions (Part I)', 75),
    ('T07', 'Two provenances, not one (Part I)', 77),
    ('T08', 'Creativity lives in construction; selection produces the raw material (opening, grievance 6)', 13),
    ('T09', 'Premises taken as given: the costly gamble (Part IX)', 397),
    ('T10', 'An inexplicit representation is not an absent one (Part X)', 407),
    ('T11', 'Closing an episode is a choice (Part X)', 429),
    ('T12', 'Explanatory barriers (Part XIII)', 495),
    ('T13', 'Error correction (the word, Part IX)', 397),
    ('T14', 'Recognized difficulty (Part X)', 429),
    ('T15', 'Complete and creative critical episodes (Part X)', 429),
]


def main():
    core = open(CORE, encoding='utf-8').read().split('\n')
    text = open(TEXT, encoding='utf-8').read().split('\n')
    units = []
    for i, line in enumerate(core, 1):
        m = re.match(r'^\*\*((D\d+\.[0-9A-Za-z]+)|(E\d+))[ .](.*?)\*\*', line)
        if m:
            uid = m.group(1)
            name = m.group(4).strip().rstrip('.')
            units.append({'id': uid, 'kind': 'definition' if uid.startswith('D') else 'encoding',
                          'name': name, 'core_line': i})
    # the text lines the formal core quotes just before each definition ("> Lnnn |")
    for u in units:
        lines = []
        j = u['core_line'] - 2
        while j >= 0 and (core[j].startswith('>') or core[j].strip() == ''):
            m = re.match(r'^> L(\d+)', core[j])
            if m:
                lines.append(int(m.group(1)))
            j -= 1
        u['text_lines'] = sorted(set(lines))
    cl = json.load(open(CLAIMS, encoding='utf-8'))['claims']
    md = open(CLAIMS_MD, encoding='utf-8').read().split('\n')
    mdline = {}
    for i, line in enumerate(md, 1):
        m = re.match(r'^\| (FC[0-9.a-z]+) \|', line)
        if m:
            mdline[m.group(1)] = i
    for c in cl:
        cid = c.get('id')
        st = (c.get('after_round4') or {}).get('status') if isinstance(c.get('after_round4'), dict) else None
        units.append({'id': cid, 'kind': 'formal claim', 'name': c.get('title', ''),
                      'status_after_round_4': st,
                      'formal_core_sections': c.get('formal_core_sections') or [],
                      'text_lines': sorted({s['line'] for s in (c.get('source') or []) if isinstance(s, dict) and 'line' in s}),
                      'claims_md_line': mdline.get(cid)})
    for tid, name, ln in TERMS:
        units.append({'id': tid, 'kind': 'named term of the text', 'name': name, 'text_lines': [ln],
                      'text_line_check': text[ln - 1][:80]})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(units, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    from collections import Counter
    print(Counter(u['kind'] for u in units), len(units))


if __name__ == '__main__':
    main()
