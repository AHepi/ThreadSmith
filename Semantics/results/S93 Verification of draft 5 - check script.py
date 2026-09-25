"""S93 verification of draft 5: checks 1 to 5, as reported in "S93 Verification of draft 5.md".

Run from anywhere: python3 "Semantics/results/S93 Verification of draft 5 - check script.py"
It reads only and writes nothing. The apply tool is imported with bytecode writing off and run in memory.

Check 1. Every ruled text of the ten S93 rulings is taken from its ruling file (fenced blocks keyed by the line
of their opening fence; quoted or backticked texts from named lines) and found in the change list: OLD and NEW
equal to the entry's block, DECLARATION equal to the field, CHECK, REASON, CASES AT RISK, GAIN and LOSS texts
contained in the field; headings and WHERE equal. X11 is entered as W61.1 with the ruling's fields, and X04's
companion W35.5 as the ruling's block, whole. Superseded texts are absent. KEEP entries keep OLD, NEW, KIND and
DECLARATION.
Check 2. The change list at 6cf57ae (draft 4) is turned into the present one by the ruled edits and by the
declared bookkeeping, op by op; what is left over is listed. The frame's hunks are classified one by one.
Check 3. Draft 5 is rebuilt in memory by tools/s89_apply_changes.py (with its self-test) and compared with the
committed theory text; draft 4 against draft 5 is diffed, and draft 4 with the changed entries' texts replaced
gives draft 5 byte for byte.
Check 4. N, M, K, CLAIM/WORDING/ORDER and the groups are recounted from the entries and compared with the frame
and the revision note; every declaration line in the note is compared with its entry; the note's map table,
its list of undeclared entries and its layer-2 column are compared with the entries and the program.
Check 5. The reading's table of eighteen items against the expected outcomes, the ruling files (md5 and last
line) and the tabulation's summary; every item's "S93 cross-examination:" line in its entry's CHECK field.
Check 6 (the grep). Word-bounded search of the draft-5 theory text and of the lines draft 5 added to the change
list for wording that could bring back a list, a count, a grade, a rank or a record.
"""
import sys
sys.dont_write_bytecode = True
import difflib, hashlib, importlib.util, pathlib, re, subprocess

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
SEM = REPO / 'Semantics'
RES = SEM / 'results'
RUL = RES / 'S93 reading rulings'
TESTS = SEM / 'tests'
CL_REL = 'Semantics/tests/Revision 2 - change list, draft of 23 September.md'
D4_COMMIT = '6cf57ae'   # draft 4 of the list, md5 b6b2ea95ea9e21ebea3316d8e9fa4b40, the text every ruling read
CL = (REPO / CL_REL).read_text(encoding='utf-8')
CL4 = subprocess.run(['git', '-C', str(REPO), 'show', f'{D4_COMMIT}:{CL_REL}'],
                     capture_output=True, check=True).stdout.decode('utf-8')
D4 = (TESTS / 'Revision 2 - file 13 draft 4, theory text.md').read_text(encoding='utf-8')
D5 = (TESTS / 'Revision 2 - file 13 draft 5, theory text.md').read_text(encoding='utf-8')
NOTE = (TESTS / 'Revision 2 - revision note, draft of 23 September.md').read_text(encoding='utf-8')
READING = (RES / 'S93 Reading of the replies.md').read_text(encoding='utf-8')
TAB = (RES / 'S93 Tabulation of the replies, before any ruling.md').read_text(encoding='utf-8')
F11 = [p for p in (SEM / 'authority').iterdir() if p.name.startswith('11 ')][0].read_text(encoding='utf-8')
md5 = lambda s: hashlib.md5(s.encode('utf-8')).hexdigest()
RULINGS = {
    'X03': 'ruling S93 X03 W19.1.md', 'X04': 'ruling S93 X04 W35.1.md', 'X05': 'ruling S93 X05 W35.2.md',
    'X06': 'ruling S93 X06 W20.1.md', 'X09': 'ruling S93 X09 W59.1 Rivals.md',
    'X10': 'ruling S93 X10 W59.1 Problems.md', 'X11': 'ruling S93 X11 proposed.md',
    'X14': 'ruling S93 X14 W60.1.md', 'X17': 'ruling S93 X17 W7.5.md', 'X18': 'ruling S93 X18 W38.1.md'}
RT = {x: (RUL / f).read_text(encoding='utf-8') for x, f in RULINGS.items()}
RL = {x: t.split('\n') for x, t in RT.items()}

results = []
def rec(ok, what, note=''):
    results.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + what + (f' -- {note}' if note else ''))


# ---------------------------------------------------------------- ruling texts
def fences(text):
    """Fenced blocks of any length (3 to 5 backticks, possibly indented), keyed by the 1-based line of the
    opening fence. An indented block is given with its indentation removed."""
    lines = text.split('\n'); out = {}; i = 0
    while i < len(lines):
        m = re.match(r'^(\s*)(`{3,})text\s*$', lines[i])
        if m:
            indent, ticks = m.group(1), m.group(2); j = i + 1
            while lines[j] != indent + ticks: j += 1
            body = [l[len(indent):] if l.startswith(indent) else l for l in lines[i + 1:j]]
            out[i + 1] = '\n'.join(body); i = j + 1; continue
        i += 1
    return out
FB = {x: fences(t) for x, t in RT.items()}
def line(x, n): return RL[x][n - 1]
def quoted(x, n, begins):
    s = line(x, n); i = s.index('"' + begins); j = s.rindex('"'); return s[i + 1:j]
def ticked(x, n):
    s = line(x, n); return s[s.index('`') + 1:s.rindex('`')]


# ---------------------------------------------------------------- the change list's entries
FIELD = re.compile(r'^- \*\*([A-Z0-9][A-Z0-9 /()-]*):\*\*(?: (.*))?$')
def split_list(cl):
    """(frame, [(entry id, chunk text)], tail) with the chunks joined back giving the entries section."""
    head, body = cl.split('\n## The entries\n', 1)
    lines = body.split('\n'); starts = []; fence = False; end = len(lines)
    for i, l in enumerate(lines):
        if not fence and l.startswith('### '): starts.append(i)
        if not fence and l.startswith('## '): end = i; break
        if l.startswith('````'): fence = not fence
    pre = '\n'.join(lines[:starts[0]])
    chunks = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else end
        chunks.append((lines[s][4:].split(' — ')[0].strip(), '\n'.join(lines[s:e])))
    tail = '\n'.join(lines[end:])
    return head, pre, chunks, tail
FRAME, PRE, CHUNKS, TAIL = split_list(CL)
FRAME4, PRE4, CHUNKS4, TAIL4 = split_list(CL4)
E = dict(CHUNKS); E4 = dict(CHUNKS4)
ORDER = [c[0] for c in CHUNKS]; ORDER4 = [c[0] for c in CHUNKS4]

def fields(chunk):
    out = {}; cur = None; fence = False
    for l in chunk.split('\n')[1:]:
        m = FIELD.match(l) if not fence else None
        if m:
            cur = m.group(1); out.setdefault(cur, []).append([m.group(2) or ''])
        elif cur is not None:
            out[cur][-1].append(l)
        if l.startswith('````'): fence = not fence
    return {k: ['\n'.join(v).rstrip('\n') for v in vs] for k, vs in out.items()}
def field(chunk, name):
    v = fields(chunk).get(name); return None if v is None else v[0]
def block(chunk, name):
    v = field(chunk, name) or ''
    m = re.search(r'````text\n(.*?)\n````', v, re.S); return m.group(1) if m else None
def s93_lines(chunk):
    c = field(chunk, 'CHECK') or ''
    return [l for l in c.split('\n') if re.match(r'^(  - )?S93 cross-examination:', l)]


print('== Check 1: the ruled texts, in the change list as the rulings give them')
def eq(what, got, want, extra=''):
    rec(got == want, what, ('byte for byte' if got == want else 'DIFFERS') + extra)
def has(what, hay, needle, times=1):
    n = (hay or '').count(needle)
    rec(n == times, what, f'found {n} time(s)' + ('' if n == times else f', expected {times}'))
def lacks(what, hay, needle):
    rec(needle not in (hay or ''), what, 'absent' if needle not in (hay or '') else 'PRESENT')
def unchanged(eid, names):
    for n in names:
        a, b = field(E[eid], n), field(E4[eid], n)
        rec(a == b and a is not None, f'{eid} {n} unchanged from draft 4')
def check_line(x, eid, text, prefix='  - '):
    n = (field(E[eid], 'CHECK') or '').split('\n').count(prefix + text)
    rec(n == 1, f'[{x}] {eid} CHECK carries the ruling\'s S93 line, byte for byte, as a line of its own', f'found {n} time(s)')

# X03 · W19.1 · FIX
x = 'X03'; w = E['W19.1']
eq('[X03 L11] W19.1 OLD = ruling OLD (unchanged)', block(w, 'OLD'), FB[x][11])
eq('[X03 L17] the NEW the ruling read = draft-4 W19.1 NEW', block(E4['W19.1'], 'NEW'), FB[x][17])
eq('[X03 L84] W19.1 NEW = the ruled NEW', block(w, 'NEW'), FB[x][84],
   f'; in draft 5 {D5.count(FB[x][84])}x, in draft 4 {D4.count(FB[x][84])}x; words {len(FB[x][84].split())}')
eq('[X03 L90] W19.1 DECLARATION = the ruled declaration', field(w, 'DECLARATION'), FB[x][90])
eq('[X03 L88] W19.1 KIND CLAIM (unchanged)', field(w, 'KIND'), 'CLAIM')
check_line(x, 'W19.1', line(x, 122)[1:-1])
lacks('[X03] the superseded NEW is absent from the list and from draft 5', CL + D5, FB[x][17])

# X04 · W35.1 · KEEP, with the companion W35.5 and the REASON edit
x = 'X04'; w = E['W35.1']
eq('[X04 L26] W35.1 OLD = ruling OLD', block(w, 'OLD'), FB[x][26])
eq('[X04 L35] W35.1 NEW = ruling NEW', block(w, 'NEW'), FB[x][35])
eq('[X04 L43] W35.1 DECLARATION = ruling DECLARATION', field(w, 'DECLARATION'), quoted(x, 43, 'Part IV'))
unchanged('W35.1', ['OLD', 'NEW', 'KIND', 'DECLARATION', 'REASON WORD', 'GAIN', 'LOSS', 'CASES AT RISK'])
has('[X04 L248] W35.1 CHECK carries the ruling\'s line, byte for byte (indent included)',
    field(w, 'CHECK'), '\n' + FB[x][248])
lacks('[X04 L305] W35.1 REASON: the old sentence on Derivations 4 and 10 is gone', field(w, 'REASON'), ticked(x, 305))
has('[X04 L306] W35.1 REASON: the ruling\'s new sentence stands', field(w, 'REASON'), ticked(x, 306))
w355 = FB[x][259]
eq('[X04 L259-283] W35.5 = the ruling\'s block, whole (heading, WHERE and every field)',
   E.get('W35.5', '').rstrip('\n'), w355)
has('[X04] the W35.5 block occurs once in the change list', CL, w355)
rec(ORDER.index('W35.5') == ORDER.index('W35.4') + 1, '[X04] W35.5 is placed after W35.4, as the ruling says')
rec(D4.count(block(E['W35.5'], 'OLD')) == 1 and D5.count(block(E['W35.5'], 'NEW')) == 1 and
    D5.count(block(E['W35.5'], 'OLD')) == 0, '[X04] W35.5 OLD once in draft 4, NEW once in draft 5, OLD not in draft 5')

# X05 · W35.2 · FIX
x = 'X05'; w = E['W35.2']
eq('[X05 L22] W35.2 OLD = ruling OLD (unchanged)', block(w, 'OLD'), FB[x][22])
eq('[X05 L28] the NEW the ruling read = draft-4 W35.2 NEW', block(E4['W35.2'], 'NEW'), FB[x][28])
eq('[X05 L135] W35.2 NEW = the ruled NEW', block(w, 'NEW'), FB[x][135], f'; in draft 5 {D5.count(FB[x][135])}x')
eq('[X05 L141] W35.2 DECLARATION = the ruled declaration', field(w, 'DECLARATION'), FB[x][141])
eq('[X05 L145] W35.2 KIND CLAIM, REASON WORD clarification (unchanged)',
   (field(w, 'KIND'), field(w, 'REASON WORD')), ('CLAIM', 'clarification'))
check_line(x, 'W35.2', FB[x][152])
rec((field(w, 'LOSS') or '').endswith(' ' + FB[x][158]), '[X05 L158] W35.2 LOSS ends with the ruling\'s optional sentence')
lacks('[X05] "fails at a pair of its contract" is gone from the list and draft 5', CL + D5, 'fails at a pair of its contract')

# X06 · W20.1 · FIX
x = 'X06'; w = E['W20.1']
eq('[X06 L250] W20.1 OLD = ruling OLD (unchanged; = L29)', (block(w, 'OLD'), FB[x][29]), (FB[x][250], FB[x][250]))
eq('[X06 L33] the NEW the ruling read = draft-4 W20.1 NEW', block(E4['W20.1'], 'NEW'), FB[x][33])
eq('[X06 L254] W20.1 NEW = the ruled NEW', block(w, 'NEW'), FB[x][254], f'; in draft 5 {D5.count(FB[x][254])}x')
eq('[X06 L259] W20.1 DECLARATION = the ruled declaration', field(w, 'DECLARATION'), FB[x][259])
eq('[X06 L257] W20.1 KIND CLAIM, REASON WORD clarification (unchanged)',
   (field(w, 'KIND'), field(w, 'REASON WORD')), ('CLAIM', 'clarification'))
unchanged('W20.1', ['GAIN', 'LOSS'])
check_line(x, 'W20.1', line(x, 264).strip()[2:])
m = re.search(r'"(puts[^"]*)" becomes "(puts[^"]*)"', line(x, 268))
lacks('[X06 L268] the finding on "active": the old words are gone', FRAME, m.group(1))
has('[X06 L268] the finding on "active": the ruled words stand', FRAME, m.group(2))
m = re.search(r'after "([^"]*)", add "([^"]*)"', line(x, 269))
has('[X06 L269] O7 in W20.1 CASES AT RISK: the ruled words follow "' + m.group(1) + '"',
    field(w, 'CASES AT RISK'), m.group(1) + ' ' + m.group(2))
fl = [l for l in FRAME.split('\n') if l.startswith('- **W20.1\'s "including any that assigns an input" has two readings.**')]
rec(len(fl) == 1 and '**Closed after the S93 cross-examination:**' in fl[0],
    '[X06 L267] the carried-forward finding on the two readings is marked closed')
rb = [l for l in (field(w, 'REASON') or '').split('\n') if '"Including any that assigns an input" has two readings' in l]
rec(len(rb) == 1 and '**Closed after the S93 cross-examination:**' in rb[0],
    '[X06 L267] REASON\'s matching bullet is marked closed')

# X09 · W59.1 "Rivals" · FIX
x = 'X09'; w = E['W59.1']; new59 = block(w, 'NEW')
eq('[X09 L18] W59.1 OLD = ruling OLD (unchanged)', block(w, 'OLD'), FB[x][18])
rec(block(E4['W59.1'], 'NEW').startswith(FB[x][26] + '\n\n'), '[X09 L26] the Rivals paragraph the ruling read = draft-4 NEW\'s first paragraph')
eq('[X09 L32] the declaration the ruling read = draft-4 W59.1 DECLARATION', field(E4['W59.1'], 'DECLARATION'), FB[x][32])
lacks('[X09 L110] the old illustration is gone from NEW', new59, FB[x][110])
has('[X09 L116] the ruled illustration stands in NEW', new59, FB[x][116])
rec(new59.startswith(FB[x][122] + '\n\n'), '[X09 L122] W59.1 NEW opens with the ruled Rivals paragraph, whole, byte for byte')
eq('[X09 L122] draft-5 L315 = the ruled Rivals paragraph', D5.split('\n')[314], FB[x][122])
eq('[X09 L154] W59.1 DECLARATION = the ruled declaration, whole', field(w, 'DECLARATION'), FB[x][154])
lacks('[X09 L142] the old declaration sentence is gone', field(w, 'DECLARATION'), FB[x][142])
has('[X09 L148] the ruled declaration sentence stands', field(w, 'DECLARATION'), FB[x][148])
eq('[X09] W59.1 KIND CLAIM (unchanged)', field(w, 'KIND'), 'CLAIM')
check_line(x, 'W59.1', line(x, 184)[2:])
lacks('[X09] "as when two of their" is gone from W59.1 NEW and DECLARATION and from draft 5', new59 + field(w, 'DECLARATION') + D5, 'as when two of their active components')
rec([l for l in CL.split('\n') if 'as when two of their active components' in l] == ['  - ' + line(x, 184)[2:]],
    '[X09] its one other place in the list is the ruled CHECK line, which quotes it')

# X10 · W59.1 "Problems" · KEEP
x = 'X10'
has('[X10 L20] the Problems paragraph stands in W59.1 NEW, unchanged', new59, '\n\n' + FB[x][20] + '\n\n')
rec(D4.split('\n')[316] == FB[x][20] == D5.split('\n')[316], '[X10 L20] draft-4 L317 = draft-5 L317 = the Problems paragraph')
rec(block(E4['W59.1'], 'NEW').replace(FB['X09'][26], FB['X09'][122]) == new59,
    '[X09/X10] draft-4 NEW with only the Rivals paragraph replaced gives draft-5 NEW')
check_line(x, 'W59.1', quoted(x, 91, 'S93'))

# X11 · W61.1 (new) · FIX, entered as CLAIM
x = 'X11'; w = E.get('W61.1', '')
eq('[X11 L14] W61.1 OLD = the proposed OLD', block(w, 'OLD'), FB[x][14])
eq('[X11 L18] W61.1 NEW = the proposed NEW', block(w, 'NEW'), FB[x][18])
eq('[X11 L106] W61.1 DECLARATION = the ruled declaration (its list indent removed)', field(w, 'DECLARATION'), FB[x][106])
for n, name in ((99, 'STATUS'), (100, 'FILE-11 LINE'), (102, 'REASON WORD'), (103, 'KIND')):
    want = line(x, n).split(':** ', 1)[1].rstrip('.')
    eq(f'[X11 L{n}] W61.1 {name} = "{want}" (the ruling\'s list item without its closing full stop)', field(w, name), want)
eq('[X11 L101] W61.1 WHERE = the ruled WHERE', field(w, 'WHERE'), line(x, 101).split(':** ', 1)[1])
eq('[X11 L109] W61.1 CASES AT RISK = the ruled text', field(w, 'CASES AT RISK'), line(x, 109).split(':** ', 1)[1])
check_line(x, 'W61.1', quoted(x, 110, 'S93'))
rec(ORDER.index('W61.1') == ORDER.index('W59.1') + 1 and ORDER.index('W40.1') == ORDER.index('W61.1') + 1,
    '[X11 L25] W61.1 stands between W59.1 and W40.1')
rec(F11.count(FB[x][14]) == 1 and F11.split('\n')[322].count(FB[x][14]) == 1, '[X11] OLD once in file 11, on line 323')
rec(D4.count(FB[x][14]) == 1 and D5.count(FB[x][18]) == 1 and FB[x][14] not in D5, '[X11] OLD once in draft 4; NEW once in draft 5; OLD gone')

# X14 · W60.1 · KEEP
x = 'X14'; w = E['W60.1']
eq('[X14 L21] W60.1 OLD = ruling OLD', block(w, 'OLD'), FB[x][21])
eq('[X14 L27] W60.1 NEW = ruling NEW', block(w, 'NEW'), FB[x][27])
unchanged('W60.1', ['OLD', 'NEW', 'KIND', 'DECLARATION', 'REASON', 'CASES AT RISK', 'GAIN', 'LOSS'])
check_line(x, 'W60.1', quoted(x, 330, 'S93'))

# X17 · W7.5 · FIX
x = 'X17'; w = E['W7.5']
eq('[X17 L22] the OLD the ruling read = draft-4 W7.5 OLD', block(E4['W7.5'], 'OLD'), FB[x][22])
eq('[X17 L26] the NEW the ruling read = draft-4 W7.5 NEW', block(E4['W7.5'], 'NEW'), FB[x][26])
eq('[X17 L252] W7.5 OLD = the ruled OLD', block(w, 'OLD'), FB[x][252])
eq('[X17 L256] W7.5 NEW = the ruled NEW', block(w, 'NEW'), FB[x][256], f'; in draft 5 {D5.count(FB[x][256])}x')
eq('[X17 L261] W7.5 DECLARATION = the ruled declaration', field(w, 'DECLARATION'), FB[x][261])
eq('[X17 L265] W7.5 heading = the ruled heading', w.split('\n')[0], ticked(x, 265))
eq('[X17 L266] W7.5 WHERE = the ruled WHERE', '- **WHERE:** ' + field(w, 'WHERE'), ticked(x, 266))
eq('[X17 L259, L267] W7.5 KIND, REASON WORD, FILE-11 LINE unchanged (CLAIM, erratum, 518)',
   (field(w, 'KIND'), field(w, 'REASON WORD'), field(w, 'FILE-11 LINE')), ('CLAIM', 'erratum', '518'))
check_line(x, 'W7.5', quoted(x, 334, 'S93'))
has('[X17 L335] W7.5 REASON carries the ruled bullet', field(w, 'REASON'), '\n  - ' + quoted(x, 335, 'After'))
has('[X17 L336] W7.5 CASES AT RISK carries the ruled line', field(w, 'CASES AT RISK'), '\n  - ' + quoted(x, 336, 'S93'))
has('[X17 L337] W7.5 GAIN carries the ruled sentence', field(w, 'GAIN'), quoted(x, 337, 'Part VI'))
has('[X17 L338] W7.5 LOSS carries the ruled sentence', field(w, 'LOSS'), quoted(x, 338, 'The order'))
fb = [l for l in FRAME.split('\n') if l.startswith('  - *The dependence order does not place the new terms.*')]
rec(len(fb) == 1 and 'the placement is now made, in W7.5, after the (RC) sentence' in fb[0]
    and 'The candidate at the free sentence is not taken, and the free sentence stays free.' in fb[0],
    '[X17 L339] "Found in draft 4", first bullet, says the placement is made and the free sentence stays free')
added = FB[x][256][len(FB[x][26]) + 1:]
rec(FB[x][256].startswith(FB[x][26] + ' ') and added.split(' In Part VI,')[0] == '(RC), (U1)–(U3) depend on all of the above.'
    and len(('In Part VI,' + added.split(' In Part VI,')[1]).split()) == 62,
    '[X17] NEW = draft-4 NEW + the (RC) sentence + one sentence of 62 words')

# X18 · W38.1 · FIX
x = 'X18'; w = E['W38.1']
lacks('[X18 L74] the old Surprise-and-problems line is gone from W38.1 NEW', block(w, 'NEW'), FB[x][74])
has('[X18 L80] the ruled Surprise-and-problems line stands in W38.1 NEW', block(w, 'NEW'), FB[x][80])
unchanged('W38.1', ['OLD', 'KIND', 'DECLARATION'])
check_line(x, 'W38.1', quoted(x, 88, 'S93'))
clause = 'a conflict in which what the system holds meets a claimed obligation only by failing a protected one (Part XI), when the system represents it'
rec(clause in FB[x][80] and clause in D5.split('\n')[428], '[X18 L84] the new clause equals draft-5 L429\'s clause')
rec(block(E4['W38.1'], 'NEW').replace(FB[x][74], FB[x][80]) == block(w, 'NEW'), '[X18] draft-4 NEW with only that line replaced gives draft-5 NEW')

rulings_last = {x: [l for l in RL[x] if l.strip()][-1] for x in RULINGS}
rec(sorted(x for x, l in rulings_last.items() if l.endswith('FIX')) == ['X03', 'X05', 'X06', 'X09', 'X11', 'X17', 'X18'] and
    sorted(x for x, l in rulings_last.items() if l.endswith('KEEP')) == ['X04', 'X10', 'X14'],
    'the ten ruling files end: FIX X03 X05 X06 X09 X11 X17 X18; KEEP X04 X10 X14')


print('== Check 2: draft 4 of the list turned into draft 5 by the ruled edits and the declared bookkeeping')
UPHELD = {'W37.1': 'F', 'W36.1': 'D', 'W34.1': 'D', 'W33.1': 'D', 'W40.1': 'I', 'W24.1': 'J', 'W22.1': 'J', 'W6.3': 'K'}
N7_NOTE = ('(Corrected on 25 September 2026, after the S93 cross-examination, from "N7 (O59)": under D8 N7 is O58 '
           'and O59 is N8. Bookkeeping; no verdict or reading changes.)')
CLOSED_W201_REASON = (' **Closed after the S93 cross-examination:** NEW reads "including any of them that assigns an input", '
                      'which leaves only the second reading (ruling S93 X06 W20.1, ruling 1).')
def repl(chunk, old, new, what):
    assert chunk.count(old) == 1, (what, chunk.count(old)); return chunk.replace(old, new, 1)
def append_to_field(chunk, name, text):
    lines = chunk.split('\n'); fence = False; start = None; end = None
    for i, l in enumerate(lines):
        m = FIELD.match(l) if not fence else None
        if m and start is not None and end is None: end = i
        if m and m.group(1) == name and start is None: start = i
        if l.startswith('````'): fence = not fence
    if end is None: end = len(lines)
    while end > start + 1 and lines[end - 1] == '': end -= 1
    return '\n'.join(lines[:end] + [text] + lines[end:])
OPS = []   # (entry, description, source)
def op(eid, desc, src, fn):
    OPS.append((eid, desc, src)); R[eid] = fn(R[eid])
R = dict(CHUNKS4)
up = lambda p: f'  - S93 cross-examination: upheld by both readers (s93_xexam_atria_{p}, s93_xexam_mimo_{p}); not thereby confirmed.'
op('W19.1', 'NEW replaced by the ruled NEW', 'X03 L84', lambda c: repl(c, FB['X03'][17], FB['X03'][84], 'W19.1 NEW'))
op('W19.1', 'DECLARATION replaced', 'X03 L90', lambda c: repl(c, '- **DECLARATION:** ' + field(c, 'DECLARATION'), '- **DECLARATION:** ' + FB['X03'][90], 'x'))
op('W19.1', 'S93 CHECK line', 'X03 L122', lambda c: append_to_field(c, 'CHECK', '  - ' + line('X03', 122)[1:-1]))
op('W35.1', 'REASON sentence on Derivations 4 and 10 replaced', 'X04 L305-306', lambda c: repl(c, ticked('X04', 305), ticked('X04', 306), 'x'))
op('W35.1', 'S93 CHECK line', 'X04 L248', lambda c: append_to_field(c, 'CHECK', FB['X04'][248]))
op('W35.2', 'NEW replaced', 'X05 L135', lambda c: repl(c, FB['X05'][28], FB['X05'][135], 'x'))
op('W35.2', 'DECLARATION replaced', 'X05 L141', lambda c: repl(c, '- **DECLARATION:** ' + field(c, 'DECLARATION'), '- **DECLARATION:** ' + FB['X05'][141], 'x'))
op('W35.2', 'S93 CHECK line', 'X05 L152', lambda c: append_to_field(c, 'CHECK', '  - ' + FB['X05'][152]))
op('W35.2', 'the optional LOSS sentence appended', 'X05 L158', lambda c: repl(c, '- **LOSS:** ' + field(c, 'LOSS'), '- **LOSS:** ' + field(c, 'LOSS') + ' ' + FB['X05'][158], 'x'))
op('W20.1', 'NEW replaced', 'X06 L254', lambda c: repl(c, FB['X06'][33], FB['X06'][254], 'x'))
op('W20.1', 'DECLARATION replaced', 'X06 L259', lambda c: repl(c, '- **DECLARATION:** ' + field(c, 'DECLARATION'), '- **DECLARATION:** ' + FB['X06'][259], 'x'))
op('W20.1', 'S93 CHECK line', 'X06 L264', lambda c: append_to_field(c, 'CHECK', '  - ' + line('X06', 264).strip()[2:]))
m6 = re.search(r'after "([^"]*)", add "([^"]*)"', line('X06', 269))
op('W20.1', 'O7 line: the ruled words added', 'X06 L269', lambda c: repl(c, m6.group(1) + ',', m6.group(1) + ' ' + m6.group(2) + ',', 'x'))
op('W20.1', 'REASON bullet on the two readings marked closed (applier\'s words)', 'X06 L267 (bookkeeping)',
   lambda c: repl(c, 'The named verdicts are the same on both (models 1a and 1b). Carried forward below.',
                  'The named verdicts are the same on both (models 1a and 1b). Carried forward below.' + CLOSED_W201_REASON, 'x'))
op('W59.1', 'NEW: the illustration of conflict', 'X09 L110-116', lambda c: repl(c, FB['X09'][110], FB['X09'][116], 'x'))
op('W59.1', 'DECLARATION: the third sentence', 'X09 L142-148', lambda c: repl(c, FB['X09'][142], FB['X09'][148], 'x'))
op('W59.1', 'S93 CHECK line (X09)', 'X09 L184', lambda c: append_to_field(c, 'CHECK', '  - ' + line('X09', 184)[2:]))
op('W59.1', 'S93 CHECK line (X10)', 'X10 L91', lambda c: append_to_field(c, 'CHECK', '  - ' + quoted('X10', 91, 'S93')))
op('W59.1', '"N7 (O59)" corrected to "N7 (O58)", with a dated note', 'bookkeeping (the reading rule\'s slip)',
   lambda c: repl(c, '  - **N7 (O59): holds; the watch is narrowed.**', '  - **N7 (O58): holds; the watch is narrowed.** ' + N7_NOTE, 'x'))
op('W34.1', '"N7 (O59)" corrected to "N7 (O58)", with a dated note', 'bookkeeping',
   lambda c: repl(c, '  - **N7 (O59).**', '  - **N7 (O58).** ' + N7_NOTE, 'x'))
op('W60.1', 'S93 CHECK line', 'X14 L330', lambda c: append_to_field(c, 'CHECK', '  - ' + quoted('X14', 330, 'S93')))
op('W7.5', 'heading', 'X17 L265', lambda c: repl(c, c.split('\n')[0], ticked('X17', 265), 'x'))
op('W7.5', 'WHERE', 'X17 L266', lambda c: repl(c, '- **WHERE:** ' + field(c, 'WHERE'), ticked('X17', 266), 'x'))
op('W7.5', 'OLD replaced', 'X17 L252', lambda c: repl(c, FB['X17'][22], FB['X17'][252], 'x'))
op('W7.5', 'NEW replaced', 'X17 L256', lambda c: repl(c, '````text\n' + FB['X17'][26] + '\n````', '````text\n' + FB['X17'][256] + '\n````', 'x'))
op('W7.5', 'DECLARATION replaced', 'X17 L261', lambda c: repl(c, '- **DECLARATION:** ' + field(c, 'DECLARATION'), '- **DECLARATION:** ' + FB['X17'][261], 'x'))
op('W7.5', 'S93 CHECK line', 'X17 L334', lambda c: append_to_field(c, 'CHECK', '  - ' + quoted('X17', 334, 'S93')))
op('W7.5', 'REASON bullet', 'X17 L335', lambda c: append_to_field(c, 'REASON', '  - ' + quoted('X17', 335, 'After')))
op('W7.5', 'CASES AT RISK line', 'X17 L336', lambda c: append_to_field(c, 'CASES AT RISK', '  - ' + quoted('X17', 336, 'S93')))
op('W7.5', 'GAIN sentence, after "After the S93 cross-examination: "', 'X17 L337',
   lambda c: repl(c, '- **GAIN:** ' + field(c, 'GAIN'), '- **GAIN:** ' + field(c, 'GAIN') + ' After the S93 cross-examination: ' + quoted('X17', 337, 'Part VI'), 'x'))
op('W7.5', 'LOSS sentence, after "After the S93 cross-examination: "', 'X17 L338',
   lambda c: repl(c, '- **LOSS:** ' + field(c, 'LOSS'), '- **LOSS:** ' + field(c, 'LOSS') + ' After the S93 cross-examination: ' + quoted('X17', 338, 'The order'), 'x'))
op('W38.1', 'NEW: the Surprise-and-problems line', 'X18 L74-80', lambda c: repl(c, FB['X18'][74], FB['X18'][80], 'x'))
op('W38.1', 'S93 CHECK line', 'X18 L88', lambda c: append_to_field(c, 'CHECK', '  - ' + quoted('X18', 88, 'S93')))
for eid, p in UPHELD.items():
    op(eid, f'S93 CHECK line: upheld by both readers (part {p})', 'the reading, section 6', lambda c, p=p: append_to_field(c, 'CHECK', up(p)))
order_r = list(ORDER4)
order_r.insert(order_r.index('W35.4') + 1, 'W35.5'); R['W35.5'] = FB['X04'][259] + '\n'
order_r.insert(order_r.index('W59.1') + 1, 'W61.1'); R['W61.1'] = E['W61.1']   # compared field by field in check 1 and below
OPS.append(('W35.5', 'new entry, the X04 ruling\'s block whole', 'X04 L259-283'))
OPS.append(('W61.1', 'new entry (ruled fields: check 1; the rest listed as bookkeeping)', 'X11 ruling 5'))
rebuilt = PRE + '\n' + '\n'.join(R[e] for e in order_r)
actual = PRE + '\n' + '\n'.join(E[e] for e in ORDER)
rec(order_r == ORDER, 'entry order: draft 4\'s, with W35.5 after W35.4 and W61.1 after W59.1', f'{len(ORDER4)} -> {len(ORDER)} entries')
rec(rebuilt == actual, f'the entries section: draft 4 + {len(OPS)} listed ops = draft 5, byte for byte')
if rebuilt != actual:
    for l in difflib.unified_diff(rebuilt.split('\n'), actual.split('\n'), 'rebuilt', 'actual', lineterm='', n=0): print('   ', l[:200])
rec(TAIL == TAIL4 and PRE == PRE4, 'the list after the entries, and the lines before the first entry, are unchanged')
changed_entries = sorted(e for e in ORDER if E.get(e) != E4.get(e))
print('  entries changed or added:', ', '.join(changed_entries))
for eid, desc, src in OPS: print(f'    op {eid}: {desc} [{src}]')
claim_fields = sorted(e for e in ORDER4 if any(field(E[e], n) != field(E4[e], n) for n in ('OLD', 'NEW', 'KIND', 'DECLARATION')))
rec(claim_fields == sorted(['W19.1', 'W20.1', 'W35.2', 'W38.1', 'W59.1', 'W7.5']),
    'OLD, NEW, KIND or DECLARATION changed only in W19.1, W35.2, W20.1, W59.1, W7.5 and W38.1 (with W61.1 and W35.5 added)', ', '.join(claim_fields))
rec(len(changed_entries) == 18, 'in all, 16 entries changed and 2 added: the 6 above, and W35.1, W34.1, W60.1 and the 7 other upheld items for CHECK lines or bookkeeping')
w61 = fields(E['W61.1'])
rec(sorted(w61) == sorted(['STATUS', 'GROUP', 'ITEM', 'FILE-11 LINE', 'WHERE', 'REASON WORD', 'KIND', 'CHECK', 'OLD', 'NEW',
                           'DECLARATION', 'REASON', 'CASES AT RISK', 'GAIN / LOSS']), 'W61.1 has the list\'s usual fields and no others')
print('    W61.1 bookkeeping (not in the ruling): heading ' + repr(E['W61.1'].split('\n')[0]))
for n in ('GROUP', 'ITEM', 'REASON', 'GAIN / LOSS'): print(f'    W61.1 {n}: {w61[n][0][:160]}' + (' …' if len(w61[n][0]) > 160 else ''))
print('    W61.1 CHECK, first line: ' + w61['CHECK'][0].split('\n')[0][:200])
rec('file 11 L105' in w61['REASON'][0] and 'An edit that sets a port replaces the component assigning that port' in F11.split('\n')[104]
    and 'intervening on the upstream port changes the target\'s downstream value but not the calculation\'s' in F11.split('\n')[272],
    'W61.1 REASON\'s file-11 pointers hold (L105: an edit replaces the component; L273: the reversed calculation)')

# the frame
fa, fb_ = FRAME4.split('\n'), FRAME.split('\n')
S93_SECTION_HEAD = '**After the cross-examination (S93): 7 rulings FIX, 3 KEEP, none DROP; 8 items upheld by both readers; 2 entries added.**'
def classify(o, n):
    nn = [l for l in n if l.strip()]
    if o == ['**DRAFT 4 — hard to vary restated through rivals and problems; correction-sticks result added; not frozen**'] and len(n) == 1 and n[0].startswith('**DRAFT 5'):
        return 'frame: the header'
    if len(o) == len(n) == 1 and o[0].startswith('Made from file 11') and n[0].startswith(o[0].rsplit(' No outside reader', 1)[0]):
        return 'frame: the opening paragraph (the draft-5 sentence added; its last sentence brought up to date)'
    if len(o) == len(n) == 1 and o[0].startswith('*Written on 23 September') and n[0].startswith(o[0][:-1]) and n[0].endswith('*'):
        return 'frame: the italic record, one pass appended'
    if not o and len(nn) == 1 and nn[0].startswith('Draft 5 applies the rulings of the S93'):
        return 'frame: What this is, a paragraph on draft 5 added'
    if len(o) == len(n) == 1 and o[0].startswith('- **Entries that change the theory text: 57.**') and n[0].startswith('- **Entries that change the theory text: 59.**'):
        return 'count update: Counts, the theory entries (recounted in check 4)'
    if len(o) == len(n) == 1 and o[0].startswith('- **The checks.**') and n[0].startswith(
            o[0].replace('None has been cross-examined.', 'None had been cross-examined when draft 4 was made.')):
        return 'frame: Counts, "The checks": the S93 sentence appended; "None has been cross-examined." put in the past'
    if len(o) == len(n) == 1 and o[0].startswith('**After the cross-examination (S90)') and n[0].startswith(o[0] + ' (After S93:'):
        return 'frame: the S90 paragraph, a parenthesis appended'
    if not o and nn and nn[0].startswith(S93_SECTION_HEAD):
        return 'frame: the section "After the cross-examination (S93)" added (its table is checked in check 4)'
    if len(o) == len(n) == 1 and o[0].startswith('- **No outside reader has seen these wordings in their final form.**') and \
            re.sub(r' \(After S93:[^)]*\)', '', n[0]) == o[0]:
        return 'frame: the held items, a parenthesis inserted'
    if len(o) == len(n) == 2 and o[0].startswith('- **"Active" is still undefined**'):
        mm = re.search(r'"(puts[^"]*)" becomes "(puts[^"]*)"', line('X06', 268))
        if n[0] == o[0].replace(mm.group(1), mm.group(2)) and n[1].startswith(o[1] + ' **Closed after the S93 cross-examination:**'):
            return 'X06 record edits: the finding on "active" (ruled words) and the finding on the two readings (closed)'
    if len(o) == len(n) == 1 and o[0].startswith('  - *The dependence order does not place the new terms.*') and n[0].startswith(o[0] + ' **After the S93 cross-examination:**'):
        return 'X17: "Found in draft 4", first bullet, the ruling\'s two sentences appended'
    if not o and nn and nn[0] == '## Carried forward after S93':
        return 'frame: the section "Carried forward after S93" added'
    return None
unexplained = []
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, fa, fb_, autojunk=False).get_opcodes():
    if tag == 'equal': continue
    label = classify(fa[i1:i2], fb_[j1:j2])
    print(f'    frame hunk -{i1 + 1},{i2 - i1} +{j1 + 1},{j2 - j1}: {label or "UNEXPLAINED"}')
    if label is None: unexplained.append((i1, j1))
rec(not unexplained, 'every hunk of the frame is a frame or count update or a ruled record edit', f'{len(unexplained)} unexplained')
cf = FRAME.split('## Carried forward after S93\n', 1)[1] if '## Carried forward after S93\n' in FRAME else ''
rec(cf and 'None is an edit in this draft.' in cf, '"Carried forward after S93" says that none of it is an edit')


print('== Check 3: the theory text of draft 5, rebuilt, and draft 4 against it')
spec = importlib.util.spec_from_file_location('s89_apply_changes', SEM / 'tools' / 's89_apply_changes.py')
tool = importlib.util.module_from_spec(spec); spec.loader.exec_module(tool)
built = tool.build(str(REPO / CL_REL), 'draft of 25 September 2026, not frozen')
st = tool.self_test(built)
rec(st == ['an unlisted edit was refused', 'an edit inside a new text was refused'], 'the tool builds with no refusal, and its self-test refuses both planted edits')
eq('the rebuilt theory text = the committed draft 5', built['theory_text'], D5,
   f'; md5 {md5(built["theory_text"])}; words {len(built["theory_text"].split())} (runner), hunks {built["hunks"]}')
rec(md5(D5) == '7f1d8ad02adf96e27622593bd263252e', 'draft 5 md5 7f1d8ad02adf96e27622593bd263252e')
rec(md5(built['result_text']) == '40cefd9b586f43762e0a58c54e843cb0' and len(built['result_text'].split()) == 30426,
    'the full draft 5, dated "draft of 25 September 2026, not frozen": md5 40cefd9b586f43762e0a58c54e843cb0, 30,426 words (runner)')
rec(md5(D4) == 'fc55b470c63cd4b3c27d6aa64d8d8c17', 'draft 4 md5 fc55b470c63cd4b3c27d6aa64d8d8c17')
import os
def build_text(text, date='draft of 25 September 2026, not frozen'):
    """Build from a change-list text held in memory (an anonymous memory file; nothing is written to disk)."""
    fd = os.memfd_create('change-list'); os.write(fd, text.encode('utf-8'))
    try: return tool.build(f'/proc/self/fd/{fd}', date)
    finally: os.close(fd)
b4 = build_text(CL4)
rec(b4['theory_text'] == D4 and md5(b4['result_text']) == '57c94ab5f0bada4e9443904253dc2db3' and len(b4['result_text'].split()) == 29864
    and (len(b4['entries']), len(b4['applied']), len(b4['theory_entries']), b4['hunks'], b4['summary']['N'], b4['summary']['M']) == (65, 60, 57, 55, 51, 57),
    'draft 4 of the list, built in memory: its theory text = draft 4; full md5 57c94ab5f0bada4e9443904253dc2db3, 29,864 words; 65 parsed, 60 applied, 57 theory, 55 hunks, N 51 of M 57',
    'the reading\'s draft-4 column')
v = CL4.replace('\n' + E4['W20.1'], '\n' + FB['X04'][259] + '\n\n' + E4['W20.1'], 1)
bv = build_text(v)
rec(md5(bv['theory_text']) == '5f7888dba8be366f5caed39672bdd096' and bv['hunks'] == 56,
    'draft 4 + W35.5 alone gives theory md5 5f7888dba8be366f5caed39672bdd096 and 56 hunks, as the X04 checker found in memory')
c75 = E4['W7.5'].replace(E4['W7.5'].split('\n')[0], ticked('X17', 265)).replace('- **WHERE:** ' + field(E4['W7.5'], 'WHERE'), ticked('X17', 266))
c75 = c75.replace(FB['X17'][22] + '\n````', FB['X17'][252] + '\n````').replace('````text\n' + FB['X17'][26] + '\n````', '````text\n' + FB['X17'][256] + '\n````')
c75 = c75.replace('- **DECLARATION:** ' + field(E4['W7.5'], 'DECLARATION'), '- **DECLARATION:** ' + FB['X17'][261])
bv = build_text(CL4.replace(E4['W7.5'], c75, 1))
rec(md5(bv['theory_text']) == 'f7fb94d3ad26c089c6abbf60b83baf67' and len(bv['theory_text'].split()) == 12639,
    'draft 4 + the X17 fix alone gives theory md5 f7fb94d3ad26c089c6abbf60b83baf67, 12,639 words, as the X17 checker found')
import os as _os
CENV = dict(_os.environ, LC_ALL='C')
wc = subprocess.run(['wc', '-w'], input=D5.encode('utf-8'), capture_output=True, env=CENV).stdout.split()[0].decode()
wcf = subprocess.run(['wc', '-w'], input=built['result_text'].encode('utf-8'), capture_output=True, env=CENV).stdout.split()[0].decode()
rec((wc, wcf) == ('12622', '30382'), 'wc -w in the C locale: draft 5 theory text 12,622, full draft 30,382, as the frame states (a UTF-8 locale counts as the runner does)', f'{wc}, {wcf}')
l4, l5 = D4.split('\n'), D5.split('\n')
changed = [i + 1 for i in range(max(len(l4), len(l5))) if (l4[i:i + 1] or [None]) != (l5[i:i + 1] or [None])]
rec(len(l4) == len(l5) and changed == [119, 223, 231, 315, 325, 526, 582], 'draft 4 against draft 5: exactly seven changed lines',
    ', '.join(f'L{c}' for c in changed))
TRACE = [  # (entry, ruling, text in draft 4, text in draft 5)
    ('W19.1', 'X03', FB['X03'][17], FB['X03'][84]),
    ('W35.2', 'X05', FB['X05'][28], FB['X05'][135]),
    ('W20.1', 'X06', FB['X06'][33], FB['X06'][254]),
    ('W59.1', 'X09', FB['X09'][26], FB['X09'][122]),
    ('W61.1', 'X11', FB['X11'][14], FB['X11'][18]),
    ('W7.5', 'X17', FB['X17'][26] + ' (RC), (U1)–(U3) depend on all of the above.', FB['X17'][256]),
    ('W35.5', 'X04', block(E['W35.5'], 'OLD'), block(E['W35.5'], 'NEW'))]
x4 = D4
for eid, x, a, b in TRACE:
    ln = [i + 1 for i, l in enumerate(l4) if a in l]
    rec(D4.count(a) == 1 and D5.count(b) == 1 and len(ln) == 1, f'L{ln[0] if ln else "?"}: {eid} ({x}): its draft-4 text once in draft 4, its draft-5 text once in draft 5')
    x4 = x4.replace(a, b, 1)
rec(x4 == D5, 'draft 4 with those seven texts replaced = draft 5, byte for byte')
for h in [l for l in difflib.unified_diff(l4, l5, lineterm='', n=0) if l.startswith('@@')]: print('   hunk', h)


print('== Check 4: counts and declarations')
theory = []
for eid in ORDER:
    f = fields(E[eid])
    status, kind = f.get('STATUS', [''])[0].strip(), (f.get('KIND', [''])[0].split() or [''])[0].strip('.')
    if status == 'applied' and kind != 'META':
        old = block(E[eid], 'OLD'); start = F11.index(old)
        theory.append(dict(id=eid, kind=kind, group=re.match(r'[A-Z0-9]+', f['GROUP'][0]).group(0), start=start, line=F11.count('\n', 0, start) + 1,
                           decl=(f.get('DECLARATION') or [''])[0].strip(), reason=f['REASON WORD'][0].strip(), f11=f['FILE-11 LINE'][0].strip()))
theory.sort(key=lambda t: t['start'])
kinds = {k: sum(t['kind'] == k for t in theory) for k in ('CLAIM', 'WORDING', 'ORDER')}
N, M = kinds['CLAIM'], len(theory)
status_counts = {}
for eid in ORDER:
    s = (field(E[eid], 'STATUS') or '').strip(); status_counts[s] = status_counts.get(s, 0) + 1
meta = [e for e in ORDER if (field(E[e], 'KIND') or '').strip() == 'META' and (field(E[e], 'STATUS') or '').strip() == 'applied']
loc_entries = [e for e in ORDER if block(E[e], 'LAYER-2 LOCATORS') is not None]
K = len([l for l in block(E[loc_entries[0]], 'LAYER-2 LOCATORS').split('\n') if l.strip()]) if len(loc_entries) == 1 else -1
groups = {}
for t in theory:
    g = groups.setdefault(t['group'], [0, 0]); g[1] += 1; g[0] += t['kind'] == 'CLAIM'
gtext = ', '.join(f'{g} {groups[g][0]} of {groups[g][1]}' for g in ['A', 'B1', 'B2', 'C', 'H', 'S93'])
print(f'  recount: {len(ORDER)} entries; status {status_counts}; meta {meta}; CLAIM {kinds["CLAIM"]}, WORDING {kinds["WORDING"]}, '
      f'ORDER {kinds["ORDER"]}; N = {N} of M = {M}; K = {K}; groups {gtext}')
rec((kinds['CLAIM'], kinds['WORDING'], kinds['ORDER'], N, M, K) == (52, 5, 2, 52, 59, 42), 'CLAIM 52, WORDING 5, ORDER 2; N 52 of M 59; K 42')
rec(len(ORDER) == 67 and status_counts == {'applied': 62, 'record-only': 5} and len(meta) == 3, '67 entries: 62 applied (59 theory, 3 meta), 5 record-only, none held')
rec((built['summary']['N'], built['summary']['M'], built['summary']['K']) == (N, M, K), 'the program\'s N, M and K agree with the recount')
cl_counts = [l for l in FRAME.split('\n') if l.startswith('- **Entries that change the theory text:')][0]
rec(cl_counts.startswith(f'- **Entries that change the theory text: {M}.** Expected ruling CLAIM {N}, WORDING {kinds["WORDING"]}, '
                         f'ORDER {kinds["ORDER"]}. By group: {gtext}. The note reads "{N} of the {M} changes".'), 'the frame\'s Counts line agrees')
rec('- **Layer 2 of the record: 42 places.**' in FRAME and '67 entries parsed, 62 applied (59 theory, 3 meta), 5 record-only, none held; '
    'CLAIM 52, WORDING 5, ORDER 2; N = 52 of M = 59, K = 42; 57 diff hunks' in FRAME, 'the frame\'s layer-2 line and "The build (draft 5)" agree')
rec(f'N = {N} of M = {M} changes; K = {K} places.' in NOTE and f': {N} of the {M} changes.' in NOTE and f'did not declare: {K} places.' in NOTE,
    'the revision note\'s section 1 gives N 52 of M 59 and K 42, in its own line and in the note')
note_groups = '; '.join(f'{g} {groups[g][0]} of {groups[g][1]}' for g in ['A', 'B1', 'C', 'B2', 'H', 'S93'])
rec(f'**Counts.** N = {N} of M = {M}. By drafting group: {note_groups}. K = {K}.' in NOTE, 'the revision note\'s section 5 Counts agree', note_groups)
want = [f'- File 11, line {t["line"]}: {t["decl"]}' for t in theory if t['kind'] == 'CLAIM']
sec1 = NOTE.split('## 1. The note, as the program writes it', 1)[1].split('\n## 2.', 1)[0]
got = [l for l in sec1.split('\n') if l.startswith('- File 11, line ')]
rec(got == want, f'the note\'s {len(got)} declaration lines = the {len(want)} CLAIM entries\' declarations, in file-11 order, byte for byte')
nb = built['result_text'].split(tool.MARKERS['NOTE'][0] + '\n', 1)[1].split('\n' + tool.MARKERS['NOTE'][1], 1)[0]
rec(nb in NOTE, 'the program\'s NOTE block occurs whole in the revision note\'s section 1')
for eid in ['W19.1', 'W35.2', 'W20.1', 'W59.1', 'W61.1', 'W7.5']:
    t = [t for t in theory if t['id'] == eid][0]
    has(f'the note carries {eid}\'s declaration (file 11, line {t["line"]}) as its entry now gives it', NOTE, f'- File 11, line {t["line"]}: {t["decl"]}\n')
rec(all(t['decl'] for t in theory if t['kind'] == 'CLAIM'), 'every CLAIM entry carries a declaration')
number = {t['id']: i for i, t in enumerate(theory, 1)}
rows = re.findall(r'(?m)^\| (R2-\d\d) \| ([^|]+?) \| [^|]*\| [^|]*\| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| (yes|no) \|', NOTE)
bad = [r for r in rows if not (number.get(r[1]) == int(r[0][3:]) and [t for t in theory if t['id'] == r[1]][0]['f11'] == r[2]
                               and [t for t in theory if t['id'] == r[1]][0]['reason'] == r[3]
                               and [t for t in theory if t['id'] == r[1]][0]['kind'] == r[4]
                               and (r[5] == 'yes') == ([t for t in theory if t['id'] == r[1]][0]['kind'] == 'CLAIM'))]
rec(len(rows) == M and not bad, f'the note\'s map (section 5): {len(rows)} rows, each R2 number, file-11 line, reason, expected ruling and "declared" as the entries give', str(bad))
und = re.findall(r'(?m)^  - (W[^ ]+(?: \+ W[^ ]+)?) \(file 11, line (\d+)\): expected ([A-Z]+)', NOTE)
rec(sorted((u[0], u[2]) for u in und) == sorted((t['id'], t['kind']) for t in theory if t['kind'] != 'CLAIM'),
    f'the note\'s list of undeclared entries = the {M - N} non-CLAIM theory entries, with their kinds', ', '.join(u[0] for u in und))
col = built['summary']['column']
nrows = {m_.group(1): m_.group(2) for m_ in re.finditer(r'(?m)^\| (L2-\d\d) \|.*\| ([^|]*) \|[^|]*\|$', NOTE)}
rec(len(nrows) == K and all(nrows[r].strip() == col[r] for r in col), f'the note\'s layer-2 column (section 2) = the program\'s, {len(nrows)} rows')
OUTC = {'X03': 'FIX', 'X04': 'KEEP', 'X05': 'FIX', 'X06': 'FIX', 'X09': 'FIX', 'X10': 'KEEP', 'X11': 'FIX', 'X14': 'KEEP', 'X17': 'FIX',
        'X01': 'upheld by both', 'X02': 'upheld by both', 'X07': 'upheld by both', 'X08': 'upheld by both', 'X12': 'upheld by both',
        'X13': 'upheld by both', 'X15': 'upheld by both', 'X16': 'upheld by both'}
IE = {'X01': 'W37.1', 'X02': 'W36.1', 'X03': 'W19.1', 'X04': 'W35.1', 'X05': 'W35.2', 'X06': 'W20.1', 'X07': 'W34.1', 'X08': 'W33.1',
      'X09': 'W59.1', 'X10': 'W59.1', 'X11': 'W61.1', 'X12': 'W40.1', 'X13': 'W24.1', 'X14': 'W60.1', 'X15': 'W22.1', 'X16': 'W6.3', 'X17': 'W7.5'}
maprow = {m_.group(1): m_.group(2) for m_ in re.finditer(r'(?m)^\| R2-\d\d \| ([^|]+?) \|.*\| ([^|]*) \|$', NOTE)}
rec(all(f'{x}: {o}' in maprow[IE[x]] for x, o in OUTC.items()) and
    sum(1 for e, v_ in maprow.items() if re.search(r'X\d\d:', v_)) == 16,
    'the note\'s map, column "S93": each of the seventeen items with an R2 number carries its outcome; no other row names an item',
    'W35.5: ' + maprow['W35.5'])
S93T = FRAME.split(S93_SECTION_HEAD, 1)[1]
trow = re.findall(r'(?m)^\| (X\d\d) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|', S93T)
okt = all((r[3] == 'meta' and r[1] == 'W38.1') or (number[r[1].split(',')[0].split(' (')[0]] == int(r[3][3:])
          and field(E[r[1].split(',')[0].split(' (')[0]], 'FILE-11 LINE').strip() == r[2]) for r in trow)
okt = okt and all(r[4].startswith({'X04': 'KEEP', 'X10': 'KEEP', 'X14': 'KEEP'}.get(r[0], 'FIX')) for r in trow)
rec(len(trow) == 10 and okt, 'the frame\'s S93 table: ten rows, each R2 number, file-11 line and ruling as the entries and rulings give', ', '.join(f'{r[0]} {r[3]}' for r in trow))


print('== Check 5: the reading of the replies, and the CHECK lines')
EXPECT = {'FIX': ['X03', 'X05', 'X06', 'X09', 'X11', 'X17', 'X18'], 'KEEP': ['X04', 'X10', 'X14'],
          'UPHELD': ['X01', 'X02', 'X07', 'X08', 'X12', 'X13', 'X15', 'X16']}
ITEM_ENTRY = {'X01': 'W37.1', 'X02': 'W36.1', 'X03': 'W19.1', 'X04': 'W35.1', 'X05': 'W35.2', 'X06': 'W20.1', 'X07': 'W34.1',
              'X08': 'W33.1', 'X09': 'W59.1', 'X10': 'W59.1', 'X11': 'W61.1', 'X12': 'W40.1', 'X13': 'W24.1', 'X14': 'W60.1',
              'X15': 'W22.1', 'X16': 'W6.3', 'X17': 'W7.5', 'X18': 'W38.1'}
rrows = re.findall(r'(?m)^\| (X\d\d) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([A-K]) \| ([A-Z]+) / ([A-Z]+) \| ([^|]+?) \| ([^|]+?) \|$', READING)
rec(len(rrows) == 18 and [r[0] for r in rrows] == [f'X{i:02d}' for i in range(1, 19)], 'the reading\'s table has the eighteen items, X01 to X18')
out = {}
for r in rrows:
    o = r[7]
    out[r[0]] = 'UPHELD' if o == 'upheld by both readers; not thereby confirmed' else ('FIX' if o.startswith('**FIX') else ('KEEP' if o.startswith('**KEEP') else o))
rec(all(out.get(x) == k for k, xs in EXPECT.items() for x in xs), 'each item\'s outcome as expected (FIX 7, KEEP 3, upheld by both 8)')
rec('**7 FIX** (X03, X05, X06, X09, X11, X17, X18), **3 KEEP** (X04, X10, X14), **no DROP**, and **8 upheld by both readers** '
    '(X01, X02, X07, X08, X12, X13, X15, X16)' in READING, 'the reading\'s "In all" sentence agrees')
for r in rrows:
    x = r[0]
    if x in RULINGS:
        mm = re.match(r'`([^`]+)` \(([0-9a-f]{32})\)', r[8])
        ok = mm and mm.group(1) == RULINGS[x] and hashlib.md5((RUL / RULINGS[x]).read_bytes()).hexdigest() == mm.group(2) \
            and rulings_last[x] == f'{x}: {out[x]}'
        rec(ok, f'{x}: ruling file {RULINGS[x]!r} named, its md5 as given, last line "{rulings_last[x]}"')
    else:
        rec(r[8] == 'none', f'{x}: no ruling file (upheld by both)')
tabrows = {m_.group(1): (m_.group(2), m_.group(3), m_.group(4), m_.group(5)) for m_ in
           re.finditer(r'(?m)^\| (X\d\d) \| ([^|]+?) \| ([A-K]) \| ([A-Z]+) \| ([A-Z]+) \|', TAB.split('### 2.1 Summary', 1)[1].split('### 2.2', 1)[0])}
rec(all(tabrows[r[0]][1:] == (r[4], r[5], r[6]) and tabrows[r[0]][0].replace('"', '') == r[1].replace('"', '').replace(',', '')
        for r in rrows), 'the reading\'s entry, part and closing lines agree with the tabulation\'s section 2.1 for all eighteen')
for x, eid in ITEM_ENTRY.items():
    ls = s93_lines(E[eid])
    if x in EXPECT['UPHELD']:
        p = [r[4] for r in rrows if r[0] == x][0]
        rec(ls == [up(p)], f'{x} ({eid}): one S93 line, "upheld by both readers", part {p}')
    else:
        rec(len(ls) == (2 if eid == 'W59.1' else 1), f'{x} ({eid}): its S93 line is in the CHECK field',
            'W59.1 carries two, X09\'s and X10\'s' if eid == 'W59.1' else '')
others = [e for e in ORDER if s93_lines(E[e]) and e not in ITEM_ENTRY.values()]
rec(others == ['W35.5'], 'no other entry carries an S93 line but W35.5, whose CHECK is the X04 ruling\'s', str(others))


print('== Check 6: the grep for a list, count, grade, rank or record')
PAT = re.compile(r'\b(counts?|counted|counting|number of|list of|grade[sd]?|grading|rank(?:s|ed|ing)?|records? of|enumerat\w*)\b', re.I)
for i, l in enumerate(l5, 1):
    for m_ in PAT.finditer(l):
        print(f'  theory L{i}{" (changed)" if i in changed else ""}: …{l[max(0, m_.start() - 70):m_.end() + 70]}…')
added_lines = [l[1:] for l in difflib.unified_diff(CL4.split('\n'), CL.split('\n'), lineterm='', n=0)
               if l.startswith('+') and not l.startswith('+++')]
for l in added_lines:
    for m_ in PAT.finditer(l):
        print(f'  change list, added line: …{l[max(0, m_.start() - 70):m_.end() + 70]}…')
new_sentence = FB['X17'][256].split(' In Part VI,')[1]
rec(not PAT.search('In Part VI,' + new_sentence) and not PAT.search(FB['X09'][116]) and not PAT.search(FB['X03'][84])
    and not PAT.search(FB['X05'][135]) and not PAT.search(FB['X06'][254]) and not PAT.search(FB['X11'][18])
    and not PAT.search(block(E['W35.5'], 'NEW')) and not PAT.search(FB['X18'][80]),
    'none of the words the S93 fixes wrote into the text or the sources note is a hit')

print(f'\nPASS {sum(results)} FAIL {len(results) - sum(results)}')
