"""S90 verification of draft 3: checks 1, 2 and 4, as reported in "S90 Verification of draft 3.md".

Run from anywhere: python3 "Semantics/results/S90 Verification of draft 3 - check script.py"
It reads only; it writes nothing.

Check 1. Every fenced ruled text of the three S90 batch readings that belongs to a FIX (and, for
completeness, every KEEP line) is found in its ruling file and in the change-list entry it belongs to:
NEW and OLD byte-identical to the entry's block, DECLARATION byte-identical to the entry's field, and
REASON, CHECK and CASES AT RISK texts contained in the field. Every changed NEW is in draft 3's theory
text. Texts the readings superseded must be absent. Ruled texts the readings give inline (not fenced)
are checked by containment. Each of the 24 ruled entries has one "S90 cross-examination:" line.
Check 2. Draft 2's theory text, with the old NEW of each entry whose NEW changed replaced by the new
NEW, must equal draft 3's theory text byte for byte; the hunks are listed.
Check 4. File 11's md5.
"""
import hashlib, pathlib, re, subprocess, difflib

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
SEM = REPO / 'Semantics'
RES = SEM / 'results'
RUL = RES / 'S90 reading rulings'
CL_PATH = 'Semantics/tests/Revision 2 - change list, draft of 23 September.md'
BEFORE_COMMIT = '3deee3e'   # the change list as the rulings read it (md5 a5c92adc9f1e3806c0f9c6394cffde1e)
CL = (REPO / CL_PATH).read_text()
CL_BEFORE = subprocess.run(['git', '-C', str(REPO), 'show', f'{BEFORE_COMMIT}:{CL_PATH}'],
                           capture_output=True, text=True, check=True).stdout
D2 = (SEM / 'tests' / 'Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md').read_text()
D3 = (SEM / 'tests' / 'Revision 2 - file 13 draft 3, theory text.md').read_text()
BATCHES = {
    'b1': RES / 'S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md',
    'b2': RES / 'S90 Reading of the replies - batch 2 (Atria A2, Mimo B1).md',
    'b3': RES / 'S90 Reading of the replies - batch 3 (Mimo B2, Mimo C, Atria B2, Atria A1, Atria C).md',
}
md5 = lambda s: hashlib.md5(s.encode()).hexdigest()

def fenced_blocks(path):
    lines = path.read_text().split('\n'); out = {}; i = 0
    while i < len(lines):
        if lines[i].startswith('````'):
            j = i + 1
            while not lines[j].startswith('````'): j += 1
            out[i + 1] = '\n'.join(lines[i + 1:j]); i = j + 1; continue
        i += 1
    return out   # keyed by the 1-based line of the opening fence
BLOCKS = {b: fenced_blocks(p) for b, p in BATCHES.items()}

def norm(s):
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"')): s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()
def norm_lines(s):
    return ' '.join(re.sub(r'^\s*(- )?', '', l) for l in s.split('\n') if l.strip())

def entries(cl):
    body = cl.split('\n## The entries\n', 1)[1]; out = {}
    for ch in re.split(r'\n(?=### )', '\n' + body):
        if ch.startswith('### '): out[ch.split('\n', 1)[0][4:].split(' — ')[0].strip()] = ch
    return out
EA, EB = entries(CL), entries(CL_BEFORE)
def field(ch, name):
    buf = None
    for l in ch.split('\n'):
        m = re.match(r'- \*\*([A-Z0-9 /-]+):\*\*\s?(.*)$', l)
        if m:
            if buf is not None: break
            if m.group(1) == name: buf = [m.group(2)]; continue
        elif buf is not None: buf.append(l)
    return None if buf is None else '\n'.join(buf).rstrip('\n')
def block(ch, name):
    v = field(ch, name) or ''
    m = re.search(r'````text\n(.*?)\n````', v, re.S)
    return m.group(1) if m else None

results = []
def rec(ok, what, note=''):
    results.append(ok); print(('PASS ' if ok else 'FAIL ') + what + (f' -- {note}' if note else ''))

print('== Check 1: ruled texts')
# (batch, fence line, entry, field, mode, ruling file)
MAP = [
 ('b1', 75, 'W19.1', 'NEW', 'block', 'ruling s90_xexam_mimo_A1 R08.md'),
 ('b1', 114, 'W20.1', 'NEW', 'block', 'ruling s90_xexam_mimo_A1 R15.md'),
 ('b1', 121, 'W20.1', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_A1 R15.md'),
 ('b1', 150, 'W37.1', 'NEW', 'block', 'ruling s90_xexam_mimo_A1 R01.md'),
 ('b1', 209, 'W22.1', 'NEW', 'block', 'ruling s90_xexam_mimo_A2 R28.md'),
 ('b1', 216, 'W22.1', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_A2 R28.md'),
 ('b1', 292, 'W24.1', 'NEW', 'block', 'ruling s90_xexam_mimo_A2 R26.md'),
 ('b1', 344, 'W6.3', 'DECLARATION', 'eq', 'ruling s90_xexam_atria_B1 R39.md'),
 ('b2', 232, 'W6.3', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_B1 item 2 R39.md'),
 ('b2', 238, 'W6.3', 'REASON', 'in', 'ruling s90_xexam_mimo_B1 item 2 R39.md'),
 ('b2', 244, 'W6.3', 'CHECK', 'in_check1', 'ruling s90_xexam_mimo_B1 item 2 R39.md'),
 ('b2', 286, 'W7.5', 'OLD', 'block', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b2', 292, 'W7.5', 'NEW', 'block', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b2', 299, 'W7.5', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b2', 305, 'W7.5', 'REASON', 'in', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b2', 311, 'W7.5', 'REASON', 'in', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b2', 317, 'W7.5', 'CHECK', 'in', 'ruling s90_xexam_mimo_B1 item 3 R48.md'),
 ('b3', 168, 'W35.1', 'NEW', 'block', 'ruling s90_xexam_mimo_C item 1 R12.md'),
 ('b3', 179, 'W35.1', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_C item 1 R12.md'),
 ('b3', 185, 'W35.1', 'CHECK', 'in', 'ruling s90_xexam_mimo_C item 1 R12.md'),
 ('b3', 257, 'W35.2', 'NEW', 'block', 'ruling s90_xexam_mimo_C item 4 R13.md'),
 ('b3', 264, 'W35.2', 'DECLARATION', 'eq', 'ruling s90_xexam_mimo_C item 4 R13.md'),
 ('b3', 270, 'W35.2', 'CHECK', 'in', 'ruling s90_xexam_mimo_C item 4 R13.md'),
 ('b3', 426, 'W37.1', 'NEW', 'block', 'ruling s90_xexam_atria_A1 item 1 R01.md'),
 ('b3', 434, 'W37.1', 'REASON', 'inl', 'ruling s90_xexam_atria_A1 item 1 R01.md'),
 ('b3', 443, 'W37.1', 'CHECK', 'in', 'ruling s90_xexam_atria_A1 item 1 R01.md'),
 ('b3', 514, 'W35.2', 'REASON', 'in', 'ruling s90_xexam_atria_C item 1 R13.md'),
 ('b3', 595, 'W40.1', 'DECLARATION', 'eq', 'ruling s90_xexam_atria_C item 5 R25.md'),
 ('b3', 601, 'W40.1', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 5 R25.md'),
 # KEEP lines
 ('b1', 244, 'W19.2', 'CHECK', 'in', 'ruling s90_xexam_mimo_A2 R51.md'),
 ('b2', 125, 'W19.2', 'CHECK', 'in', 'ruling s90_xexam_atria_A2 item 1 R51.md'),
 ('b2', 131, 'W19.2', 'CASES AT RISK', 'in', 'ruling s90_xexam_atria_A2 item 1 R51.md'),
 ('b2', 197, 'W58(ii).1', 'CHECK', 'in', 'ruling s90_xexam_mimo_B1 item 1 R04.md'),
 ('b3', 137, 'W17.3', 'CHECK', 'in', 'ruling s90_xexam_mimo_B2 item 2 R52.md'),
 ('b3', 208, 'W45.1', 'CHECK', 'in', 'ruling s90_xexam_mimo_C item 2 R07.md'),
 ('b3', 322, 'W17.2', 'CHECK', 'in', 'ruling s90_xexam_atria_B2 item 1 R42.md'),
 ('b3', 343, 'W21.1', 'CHECK', 'inl', 'ruling s90_xexam_atria_B2 item 2 R31.md'),
 ('b3', 379, 'W13.1', 'CHECK', 'in', 'ruling s90_xexam_atria_B2 item 3 R32-R33.md'),
 ('b3', 385, 'W13.2 + W12.2', 'CHECK', 'in', 'ruling s90_xexam_atria_B2 item 3 R32-R33.md'),
 ('b3', 465, 'W20.2', 'CHECK', 'in', 'ruling s90_xexam_atria_A1 item 2 R17.md'),
 ('b3', 535, 'W36.1', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 2 R06.md'),
 ('b3', 556, 'W58(i).1', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 3 R21.md'),
 ('b3', 574, 'W33.1', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 4 R24.md'),
 ('b3', 622, 'W41.1', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 6 R30.md'),
 ('b3', 646, 'W35.3', 'CHECK', 'in', 'ruling s90_xexam_atria_C item 7 R34.md'),
]
for b, line, eid, name, mode, rf in MAP:
    t = BLOCKS[b][line]; rt = (RUL / rf).read_text(); tag = f'[{b} L{line}] {eid} {name}'
    if t in rt: rr, rok = 'ruling file byte for byte', True
    elif norm(t) in norm(rt): rr, rok = 'ruling file after whitespace/quote normalization', True
    elif norm(norm_lines(t)) in norm(norm_lines(rt)): rr, rok = 'ruling file after bullet/indent normalization', True
    else: rr, rok = 'NOT in ruling file', False
    got = field(EA[eid], name) or ''
    if mode == 'block':
        cok = block(EA[eid], name) == t; cr = 'entry block byte-identical' if cok else 'entry block DIFFERS'
        if name == 'NEW': cok = cok and t in D3; cr += f'; in draft 3: {t in D3}; in draft 2: {t in D2}'
    elif mode == 'eq': cok = got == t; cr = 'field byte-identical' if cok else 'field DIFFERS'
    elif mode == 'in_check1':
        core = t[len('check 1, SOUND. '):]; cok = got.startswith('check 1, SOUND') and core in got
        cr = 'field keeps "check 1, SOUND" and holds the rest byte for byte' if cok else 'NOT in field'
    elif mode == 'in': cok = t in got; cr = 'in field byte for byte' if cok else 'NOT in field'
    else:
        cok = norm_lines(t) in norm_lines(got)
        cr = 'in field byte for byte' if t in got else ('in field, indentation differs only' if cok else 'NOT in field')
    rec(rok and cok, tag, f'{rr}; {cr}')
for b, line, eid, name in [('b1', 350, 'W6.3', 'REASON'), ('b1', 356, 'W6.3', 'CHECK'), ('b3', 502, 'W35.2', 'NEW'),
                           ('b3', 508, 'W35.2', 'DECLARATION'), ('b3', 235, 'W41.1', 'CHECK'), ('b3', 289, 'W40.1', 'CHECK')]:
    present = BLOCKS[b][line] in (field(EA[eid], name) or '')
    rec(not present, f'[{b} L{line}] superseded text absent from {eid} {name}', 'absent' if not present else 'PRESENT')
INLINE = [
 ('W37.1', 'REASON WORD', 'clarification', 'eq'), ('W37.1', 'KIND', 'ORDER', 'eq'),
 ('W37.1', 'DECLARATION', 'If a checker rules CLAIM: "Part 0 now says that a selection history holds no represented target, as Part IV states."', 'in'),
 ('W37.1', 'GAIN / LOSS', 'Part 0 no longer uses file 10', 'in'),
 ('W19.1', 'WHERE', 'Three sentences are inserted', 'in'),
 ('W19.1', 'LOSS', 'Part II grows by three sentences, and it uses the notation of Parts IV and V before those Parts, typed inline with pointers to them.', 'in'),
 ('W20.1', 'CHECK', "ettled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined)", 'in'),
 ('W20.1', 'REASON', "settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined)", 'in'),
 ('W20.1', 'CASES AT RISK', 'O45: holds AGREE, on firmer text (W20.1 now states that membership does not wait on a description; L309 s3, W28.1 and W58(i).1 agree)', 'in'),
 ('W24.1', 'REASON', "The condition carries 00:518's 'admitted generator' as well, so the two quantifiers match (S90, Mimo A2, R26).", 'in'),
 ('W24.1', 'KIND', 'WORDING', 'eq'),
 ('W22.1', 'CHECK', "S90, Mimo part A2, R28 FALLS; fresh checker FIX after the cross-examination: \\(\\mathcal E_c\\) is 'the criticism's connection from \\(g\\) to \\(\\delta\\), interpreted as an explanatory candidate (Part V) for \\(p_\\delta\\)', not the candidate 'the criticism offers'; the declaration says 'says what its terms are', not 'defines its terms'.", 'in'),
 ('W6.3', 'KIND', 'CLAIM', 'eq'),
 ('W6.3', 'REASON', 'This entry goes one sentence past that scope, for the same reason. It cannot be dropped:', 'in'),
 ('W7.5', 'GAIN', '(EK) reaches the declared obligations through (P).', 'in'),
 ('W35.2', 'CHECK', "Atria C (item 1) ruled FIX to the same effect with 'into the simulation layer' and 'a constructed transport'; the batch-3 reading takes this wording, which R12's fix shares.", 'in'),
 ('W40.1', 'CHECK', "A second checker (Mimo C, item 5) ruled KEEP on the same replies, finding the drafted declaration exact; the batch-3 reading takes the FIX, whose declaration quotes NEW's clause word for word and so is exact on both rulings' tests.", 'in'),
 ('W40.1', 'CASES AT RISK', 'Atria C (point 3) reads the same move toward; with the clause declared, both halves are accounted for.', 'in'),
 ('W19.2', 'CASES AT RISK', 'Mimo (S90, part A2, task (d)) reads it as a move toward', 'in'),
]
for eid, name, t, mode in INLINE:
    got = field(EA[eid], name) or ''
    rec(got.strip() == t if mode == 'eq' else t in got, f'{eid} {name} (ruled inline)', repr(t[:70]))
w201 = field(EA['W20.1'], 'CHECK')
rec(True, 'W20.1 CHECK: the ruled line opens a sentence there, so its first letter is capitalized',
    'note only: "Settled wording" in CHECK, "settled wording" in REASON' if 'Settled wording (F3' in w201 else '')
RULED = ['W37.1', 'W19.1', 'W35.1', 'W35.2', 'W20.1', 'W40.1', 'W24.1', 'W22.1', 'W6.3', 'W7.5',
         'W58(ii).1', 'W36.1', 'W45.1', 'W20.2', 'W58(i).1', 'W33.1', 'W41.1', 'W21.1', 'W13.1', 'W13.2 + W12.2',
         'W35.3', 'W17.2', 'W19.2', 'W17.3']
for i, eid in enumerate(RULED):
    c = field(EA[eid], 'CHECK') or ''; kind = 'FIX' if i < 10 else 'KEEP'
    m = re.search(r'S90 cross-examination: [^\n]*? — ([^,(]*)', c)
    rec(c.count('S90 cross-examination:') == 1 and m and m.group(1).strip().startswith(kind),
        f'{eid}: one "S90 cross-examination:" line, {kind}')
changed_entries = [e for e in EB if EB[e] != EA[e]]
rec(sorted(changed_entries) == sorted(RULED), 'the entries whose text changed are exactly the 24 ruled ones', str(len(changed_entries)))

print('== Check 2: draft 2 against draft 3')
new_changed = [e for e in EB if block(EB[e], 'NEW') != block(EA[e], 'NEW')]
print('entries whose NEW changed:', new_changed)
x = D2
for e in new_changed:
    o, n = block(EB[e], 'NEW'), block(EA[e], 'NEW')
    rec(D2.count(o) == 1 and D3.count(n) == 1, f'{e}: old NEW once in draft 2, new NEW once in draft 3')
    x = x.replace(o, n, 1)
rec(x == D3, 'draft 2 with those NEWs replaced equals draft 3 byte for byte', f'md5 draft 2 {md5(D2)}, draft 3 {md5(D3)}')
for h in [l for l in difflib.unified_diff(D2.split('\n'), D3.split('\n'), lineterm='', n=0) if l.startswith('@@')]:
    print('  hunk', h)

print('== Check 4: file 11')
f11 = [p for p in (SEM / 'authority').iterdir() if p.name.startswith('11 ')][0]
rec(hashlib.md5(f11.read_bytes()).hexdigest() == '5e494c1095d920d128b9a79de378f923', 'file 11 md5 5e494c1095d920d128b9a79de378f923')
print(f'\nPASS {sum(results)} FAIL {len(results) - sum(results)}')
