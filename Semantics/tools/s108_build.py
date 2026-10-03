#!/usr/bin/env python3
"""s108_build.py: build Part A of decision S52, round 1 (log S108): the frozen template, the four sections, the four
GLM briefs, the sandbox manifest and the job list. Written 28 September 2026 by a Claude subagent (Opus 5.5) for the
orchestrator, on the model of tools/s107_build.py (round 4's build), whose checks it keeps.

  python3 Semantics/tools/s108_build.py --printouts   run the program on the state after round 4 (the whole suite, the
                                                      external examples, the creative transport case, the cases of
                                                      S106) and write the printouts; about ten minutes
  python3 Semantics/tools/s108_build.py --sections    print the counts of middle items by Part and every split of the
                                                      Parts into four contiguous sections, most balanced first
  python3 Semantics/tools/s108_build.py               build the template, the briefs, the manifest and the job list;
                                                      refuses to write over a file whose content differs
  python3 Semantics/tools/s108_build.py --check       rebuild in memory and compare with the files; writes nothing

Part A (S52): "freeze all the parts that are hard to vary, changes bits around in the middle, and see how it changes how
explanation is defined. The goal in this part is to map dependencies. Use 4 GLM agents for this, each it's own section
to change and vary given the freeze. They all get the same frozen template to play with." The frozen set is
tools/s108_frozen_set.py's (Claude's reading, not approved by the owner). Nothing in the theory's text or maths is
changed by Part A: it is an experiment on copies.

Checks before anything is written: every source committed and unchanged from HEAD, with the md5s pinned below; the
owner's words against the record; the frame of each brief (everything but the owner's words) free of the words S23
scrubs and of "model" used for a candidate (S43); each brief at most CAP words; the frozen set rebuilt identical;
every claim id matches the sandbox guard's pattern.
"""
import hashlib, json, os, re, subprocess, sys
from collections import Counter, OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
REPO = os.path.dirname(SEM)
OUT_ROOT = os.environ.get('S108_OUT_ROOT') or SEM     # a test build may write elsewhere; the real one writes here

# ------------------------------------------------------------------ the state after round 4, final (ea1047a)
R4 = 'results/S107 Round 4 - maths after the reading'
TEXT = ('tests/107 The semantics, standing alone, after round 4.md', 'c7af964c329ab7959243405d394e6574')   # = tests/106
MODEL_DIR = R4 + '/model after round 4'
CORE = (R4 + '/formal core, after round 4.md', 'd6e6ec62acbc6ef763e07b7cd7b29540')
CLAIMS_MD = (R4 + '/formal claims, after round 4.md', '1bebcb5b77f51303735bc65778fc9cd8')
CLAIMS_JSON = (R4 + '/formal claims, after round 4.json', '3d9864f1be8ec8b88914dc2800af4288')
INVENTIONS = [   # (path in the sandbox, source, md5)
    ('maths/inventions I01-I102.md', 'results/S104 Round 2 - maths/inventions register.md', '397c8381ceb56a231afe154466696bb6'),
    ('maths/inventions I103-I108, external examples.md',
     'results/S104 Round 2 - maths/inventions register - addendum for the external examples.md', '1f7beaf9420340e773e76e6987b7fa06'),
    ('maths/inventions I109-I121, creative transport case.md',
     'results/S104 Round 2 - maths/inventions register - addendum for the creative transport case.md',
     '52e1400f03634ed0908ff451f0939ca4'),
    ('maths/inventions I122-I164.md', 'results/S104 Round 2 - maths after the reading/inventions register - addendum after round 2.md',
     '507a0d56a4596f93a1118eaf3677c00a'),
    ('maths/inventions I165-I183.md', 'results/S105 Round 3 - maths after the reading/inventions register - addendum after round 3.md',
     'ce8f00ae62d5b6933e899d93d7402e29'),
    ('maths/inventions I184-I191.md', 'results/S106 The written-in test taken out/inventions register - addendum after S106.md',
     '4c19472b4f097fc5698e8e4722017100'),
    ('maths/inventions I192-I197.md', R4 + '/inventions register - addendum after round 4.md', '4912096ebab724dcad7f841983b5e09d'),
]
OTHER = [
    ('maths/parked, now.md', R4 + '/parked after round 4.md', '57a0360ed51c57830388d04c7d7aa3de'),
    ('maths/parked P1-P7.md', 'results/S105 Round 3 - maths after the reading/parked after round 3.md', '6a50b6b2c96281cbeb4d7ffab33ea79c'),
    ('maths/owner questions, now.md', R4 + '/owner questions after round 4.md', '2f7425fc314e92e32e29059bf72e8b17'),
    ('maths/formal claims FC-E1 to FC-E5, external examples.md',
     'results/S104 Round 2 - maths/formal claims - addendum for the external examples.md', 'be4000fa00e47e190865c6ea52d4a2ab'),
    ('cases/creative transport case card.md', 'results/S104 Round 2 - case card, the creative transport experiment.md',
     '3bdd2fab9ed63777cca1868d57c178aa'),
    ('cases/code of the external examples (read only).py', MODEL_DIR + '/s104_external.py', None),
    ('cases/code of the creative transport case (read only).py', MODEL_DIR + '/s104_creative_transport.py', None),
    ('cases/code of the cases of the written-in step (read only).py', MODEL_DIR + '/s106_cases.py', None),
]
EXPECT_SUITE = {'H': 133, 'CEX': 2, 'NT': 7}   # round 4's second checker: 133 / 2 / 7 of 142
EXPECT_MD5 = {'s104_external.py': '86a67664a9a3584351fd4836a4140b69', 's104_creative_transport.py': 'd473944e74d2f349b1fdfb83277843cf',
              's106_cases.py': '043aeb3647a9004ae43009a7fed50b4e'}   # the outputs round 4's second checker gives
MAT = 'results/S108 Part A - material for the readers'
FROZEN_JSON = 'results/S108 Part A - the frozen set.json'
FROZEN_MD = 'results/S108 Part A - the frozen set.md'
TEMPLATE = 'results/S108 Part A - the frozen template.md'
READING_RULE = 'results/S108 Part A - how the replies will be read, written before sending.md'
OUT = 'results/S108 Part A - returns'
JOBS_FILE = 'tools/s108_jobs - Part A, GLM.json'
MANIFEST = MAT + '/sandbox manifest.json'
BYLINE = MAT + '/the text, by line.md'
CAP = 7000
PRINTOUTS = [
    ('program printouts/whole suite now, scale 4, time cap 45.txt', MAT + '/printout - whole suite now.txt',
     ['-B', '-m', 'model.run', '--scale', '4', '--time-cap', '45', '--no-write'], 2400),
    ('program printouts/external examples FC-E1 to FC-E5 now.txt', MAT + '/printout - external examples now.txt',
     ['-B', 's104_external.py'], 900),
    ('program printouts/creative transport case CT1 to CT8 now.txt', MAT + '/printout - creative transport case now.txt',
     ['-B', 's104_creative_transport.py'], 900),
    ('program printouts/the cases of the written-in step, now.txt', MAT + '/printout - the cases of the written-in step now.txt',
     ['-B', 's106_cases.py'], 900),
]
STATUS = {'HOLDS ON ALL MODELS TRIED': 'H', 'COUNTEREXAMPLE FOUND': 'CEX', 'NOT TESTED': 'NT'}
GUARD_CLAIM = re.compile(r'FC[0-9]{1,3}(?:\.new[0-9])?')     # tools/glm_sandbox_shell_guard.py's --claim pattern
PARTS = ['Front matter', 'Part 0', 'Part I', 'Part II', 'Part III', 'Part IV', 'Part V', 'Part VI', 'Part VII',
         'Part VIII', 'Part IX', 'Part X', 'Part XI', 'Part XII', 'Part XIII', 'Part XIV', 'Part XV', 'Part XVI']
# The four sections: contiguous stretches of Parts, balanced by middle items (fixed after --sections; see the rule).
SECTIONS = [(1, 'Part 0', 'Part III', 'the opening, organizations, kinds and questions'),                 # 154 middle items
            (2, 'Part IV', 'Part VII', 'transports, provenance, account and conflict'),                   # 153
            (3, 'Part VIII', 'Part XII', 'criticism, construction, repair and the physical module'),       # 137
            (4, 'Part XIII', 'Part XVI', 'recursion, the class, what would rule it out, and the Arguments')]   # 133


def path(rel, out=False):
    return os.path.join(OUT_ROOT if out else SEM, rel)


def read(rel):
    with open(path(rel), encoding='utf-8') as f:
        return f.read()


def md5_file(rel):
    with open(path(rel), 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit('refused: ' + msg)


def words(s):
    return len(s.split())


def committed(rel):
    rel = os.path.relpath(path(rel), REPO)
    git = ['git', '-C', REPO]
    tracked = subprocess.run(git + ['ls-files', '--error-unmatch', '--', rel], capture_output=True,
                             stdin=subprocess.DEVNULL).returncode == 0
    same = subprocess.run(git + ['diff', '--quiet', 'HEAD', '--', rel], capture_output=True,
                          stdin=subprocess.DEVNULL).returncode == 0
    return tracked and same


def write_checked(rel, text):
    p = path(rel, out=True)
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            need(f.read() == text, '%s exists with other content; nothing overwritten' % rel)
        return False
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'x', encoding='utf-8') as f:
        f.write(text)
    return True


def lines_of(text):
    ls = text.split('\n')
    return ls[:-1] if ls and ls[-1] == '' else ls


def counts_of(printout):
    c = {'H': 0, 'CEX': 0, 'NT': 0}
    for m in re.finditer(r'(?m)^FC\S+\s{2}(HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)\s{2}\(', printout):
        c[STATUS[m.group(1)]] += 1
    return c


def model_files():
    return sorted(f for f in os.listdir(path(MODEL_DIR + '/model')) if f.endswith('.py'))


# ------------------------------------------------------------------ the printouts
def printouts():
    for rel in [MODEL_DIR + '/model/' + f for f in model_files()] + [s for _, s, _ in OTHER if s.startswith(MODEL_DIR)]:
        need(committed(rel), '%s is not committed, or differs from HEAD' % rel)
    before = {f: md5_file(MODEL_DIR + '/model/' + f) for f in model_files()}
    for _, rel, args, limit in PRINTOUTS:
        print('running', ' '.join(args), flush=True)
        env = {'PATH': '/usr/local/bin:/usr/bin:/bin', 'LANG': 'C.UTF-8', 'PYTHONHASHSEED': '0', 'PYTHONDONTWRITEBYTECODE': '1'}
        r = subprocess.run([sys.executable] + args, cwd=path(MODEL_DIR), env=env, capture_output=True, text=True, timeout=limit)
        need(r.returncode == 0, '%s ended with exit %d: %s' % (args, r.returncode, r.stderr[-500:]))
        if 'model.run' in args:
            need(counts_of(r.stdout) == EXPECT_SUITE, 'the whole suite gives %s, round 4\'s record %s' % (counts_of(r.stdout), EXPECT_SUITE))
        else:
            need(md5(r.stdout) == EXPECT_MD5[args[1]], '%s: output md5 %s, round 4\'s record %s' % (args[1], md5(r.stdout), EXPECT_MD5[args[1]]))
        write_checked(rel, '# command, from `%s`: PYTHONHASHSEED=0 python3 %s\n# exit 0\n\n' % (MODEL_DIR, ' '.join(args)) + r.stdout)
    after = {f: md5_file(MODEL_DIR + '/model/' + f) for f in model_files()}
    need(before == after and not os.path.exists(path(MODEL_DIR + '/model/__pycache__')), "the program's folder changed")


# ------------------------------------------------------------------ the sections
def middle_counts(fs):
    c = Counter()
    for x in fs['sentences'] + fs['definitions']:
        if x['status'] == 'MIDDLE':
            c[x['part']] += 1
    return c


def splits(c):
    """Every split of the Parts, in order, into four contiguous nonempty stretches; most balanced first."""
    ps = [p for p in PARTS if c.get(p)]
    n, tot = len(ps), sum(c.values())
    out = []
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                parts = [ps[:i], ps[i:j], ps[j:k], ps[k:]]
                sizes = [sum(c[p] for p in s) for s in parts]
                out.append((max(abs(s - tot / 4) for s in sizes), sizes, parts))
    return sorted(out, key=lambda x: (x[0], x[1]))


def section_of_part():
    need(SECTIONS, 'the four sections are not fixed yet: run --sections and fix SECTIONS')
    out = {'Front matter': 1}    # the title lines before Part 0 hold headings only
    for n, first, last, _ in SECTIONS:
        on = False
        for p in PARTS:
            if p == first:
                on = True
            if on:
                out[p] = n
            if p == last:
                on = False
    need(set(out) == set(PARTS), 'the sections do not cover every Part')
    return out


# ------------------------------------------------------------------ the owner's words (as s107_build.py, S52 added)
KEEP = [20, 21, 23, 25, 26, 27, 28, 33, 34, 36, 40, 41, 43, 44, 45, 47, 52]
REPLACE = [
    (21, "Answering file 93's choices (log S93): ", "Answering choices the drafters had put to the owner: "),
    (23, "Next step after log S94, in three paragraphs: ", "Next step, in three paragraphs: "),
    (25, "Claude's report that draft 5 ties", "Claude's report that an earlier draft ties"),
    (25, " (log S95): ", ": "),
    (26, " (log S95): ", ": "),
    (33, "After reading log S101 (file 101, what the tested strong candidates depend on), in three paragraphs: ",
     "After reading a study of what seven sentences of the text depend on, in three paragraphs: "),
    (34, "Then, after log S102 (file 102, every way hard to vary has been defined and used), in two paragraphs: ",
     "Then, after reading a summary of every way hard to vary had been defined and used, in two paragraphs: "),
    (36, "During the reading of round 1 (log S103): ", "During the reading of the first review round: "),
    (40, "During the round-2 checking (log S104), ", "During the checking of the second review round, "),
    (43, "Answering Claude's question \"When should a model count as \"cheating\", meaning it just has the answer "
         "written into it instead of explaining it? …\": ",
     "Answering Claude's question on when a candidate explanation counts as cheating, meaning it just has the "
     "answer written into it instead of explaining it: "),
    (44, "Answering Claude's question asked again without the word \"model\" (", "Answering Claude's question ("),
    (47, "Quoting from the plain file 105 ", "Quoting a passage Claude wrote in a plain-words summary of the third review round, "),
    (52, "Said while round 4's reading was running: ", "Said while the fourth review round was being read: "),
]
REPLACE_WITH_QUOTES = {43, 44}
DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 23: "25 September 2026", 25: "26 September 2026",
         26: "26 September 2026", 27: "26 September 2026", 28: "26 September 2026", 33: "27 September 2026",
         34: "27 September 2026", 36: "27 September 2026", 40: "28 September 2026", 41: "28 September 2026",
         43: "28 September 2026", 44: "28 September 2026", 45: "28 September 2026", 47: "28 September 2026",
         52: "28 September 2026"}
OWNER_CHECK = {43: "LLMs are not part of the semantics", 44: "Neither. It's an explanation when the agent",
               45: "Yes, take the test out", 47: "I think I misunderstood this question. The math doesn't ask for anything.",
               52: "freeze all the parts that are hard to vary, changes bits around in the middle"}


def owner_words(dec):
    own = {}
    for n in KEEP:
        m = re.search(r"(?m)^S%d\. \[Claude's reading[^:\]]*: .*?\] (.*)$" % n, dec)
        need(m, 'decision S%d not found' % n)
        own[n] = m.group(1)
    text = dict(own)
    for n, old, new in REPLACE:
        s = text[n]
        need(s.count(old) == 1, 'S%d: %r occurs %d times' % (n, old, s.count(old)))
        i = s.index(old)
        need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0, 'S%d: %r lies inside a quotation' % (n, old))
        need(n in REPLACE_WITH_QUOTES or '"' not in old, 'S%d: the span replaced holds a quotation' % n)
        text[n] = s.replace(old, new)
    for n in own:
        b = text[n]
        for _, old, new in [r for r in REPLACE if r[0] == n]:
            b = b.replace(new, old, 1)
        need(own[n] == b, "S%d: the owner's words changed" % n)
        need(not re.search(r"\blog S\d|\bfile \d{2,3}\b|\bdraft \d|round-2|round 1\b", text[n]), 'S%d names an internal record' % n)
        need(not re.search(r"\bmodel", text[n], re.I) or n not in (43, 44), 'S%d still says "model"' % n)
    body = ["## 2. The owner's words",
            "The theory's owner took the decisions below, in this order; they bind every variant as content. Each is "
            "quoted from the project's record of decisions. Words inside quotation marks are the owner's, word for "
            "word, typos included, except where the connecting words say that a quoted passage is Claude's (in S26, "
            "S28, S41, S44, S45 and S47). The few connecting words outside the quotation marks are the recorder's; "
            "where the record names internal files or logs there, a plain description stands in their place, and in "
            "S43 Claude's question is described, not quoted. In these words \"Claude\" is the drafters of the text and "
            "of the maths; \"your agents\" and \"your explanation\" in S27 are addressed to them. S52 is the instruction "
            "for this part: you are one of the four agents it names."]
    for n in KEEP:
        body.append('**S%d** (%s). %s' % (n, DATES[n], text[n]))
        if n == 26:
            body.append("*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked "
                        "for: holding an explanation in a carrier (ink, a brain, a file); copying or teaching it; testing "
                        "between two rival explanations, where the test changes the thing explained; building from an "
                        "explanation (a perpetual-motion machine, a bridge); and performing music. The examples are the "
                        "drafters' words, not the owner's, and are not a decision. S27 is the owner's reply to them.")
        if n == 41:
            body.append("*What S41 is.* The four questions in S41 are the drafters' words; the owner's words are the four "
                        "answers. Each answer is the owner's choice between two sides the drafters offered. S47 says how "
                        "the answer on the bridge was meant.")
        if n == 45:
            body.append("*What S44 and S45 are.* The question in S44 and the proposal in S45 are the drafters' words; "
                        "the owner's words are the answers, and in S45 the owner chose the proposal with its description.")
        if n == 47:
            body.append("*What S47 is.* The passage the owner quotes is the drafters' own words; the owner's words follow it.")
        if n == 52:
            body.append("*What S52 is.* This part is the first of the two S52 names (Part A). \"The parts that are hard to "
                        "vary\" are, in the drafters' working reading, the sentences and definitions that readers tried to "
                        "vary across the review rounds and that came through unchanged while the parts around them kept "
                        "changing; the owner has not been asked to approve that reading. What hard to vary covers in "
                        "general stays parked (S33, S34).")
    return '\n\n'.join(body), own


# ------------------------------------------------------------------ the template
def split_long(line, cap=1500):
    pieces, rest = [], line
    while len(rest) > cap:
        cut = rest.rfind(' ', 0, cap)
        cut = cut if cut > 0 else cap
        pieces.append(rest[:cut])
        rest = rest[cut:].lstrip(' ')
    pieces.append(rest)
    return pieces


def mark_of(x, sec):
    return 'FROZEN' if x['status'] == 'FROZEN' else 'S%d' % sec[x['part']]


def template(fs, text, core_text, claims, sec):
    tl = lines_of(text)
    by_line = {}
    for x in fs['sentences']:
        by_line.setdefault(x['line'], []).append(x)
    S, D = fs['sentences'], fs['definitions']
    L = ['# S108 Part A: the frozen template', '',
         "*The same template for the four agents of Part A (decision S52). Built by `tools/s108_build.py` from the text "
         "and the formal core after the fourth review round and from the frozen set (`tools/s108_frozen_set.py`). The "
         "frozen set is the drafters' working reading of \"the parts that are hard to vary\"; the owner has not been "
         "asked to approve it. Nothing here changes the text or the maths: Part A varies copies.*", '',
         '## 1. How to read it', '',
         '- Every sentence of the text and every definition and encoding of the formal core carries one mark:',
         '  - **FROZEN**: a part that is hard to vary, in the working reading: it was put to the readers or checkers at '
         'least once (challenged or tested), and no round or step changed it. It stays exactly as it is in every '
         'variant. Why each item is frozen: `the frozen set.md` beside this file.',
         '  - **S1**, **S2**, **S3**, **S4**: the middle, in four sections. Each agent varies its own section only.',
         '- Ids: a sentence unchanged since the oldest text the record follows sentence by sentence is `L<line>.s<k>`; a '
         'sentence whose words are newer is `L<line>.n<k>`; a display formula carries the line of its `\\[`. '
         'Definitions are `D§.n`, encodings `En`, as in the formal core.',
         '- A frozen sentence whose definition is in the middle constrains that definition: a variant of the definition '
         'must still be a reading of the frozen words. A frozen definition whose sentence is in the middle is the maths '
         'those words now point to.', '']
    L += ['## 2. The four sections', '',
          '| section | Parts | lines | middle sentences | middle definitions | frozen items in its stretch |',
          '|---|---|---|---|---|---|']
    span = section_spans(text, sec)
    for n, first, last, title in SECTIONS:
        ps = [p for p in PARTS if sec[p] == n]
        L.append('| S%d, %s | %s to %s | L%d–L%d | %d | %d | %d |' % (
            n, title, first, last, span[n][0], span[n][1],
            sum(1 for x in S if x['part'] in ps and x['status'] == 'MIDDLE'),
            sum(1 for x in D if x['part'] in ps and x['status'] == 'MIDDLE'),
            sum(1 for x in S + D if x['part'] in ps and x['status'] == 'FROZEN')))
    L += ['', 'A definition belongs to the section of the Part whose lines it formalizes (the lines it quotes); one '
          'that quotes none belongs by its section of the core. The middle definitions of each section:', '']
    for n, first, last, title in SECTIONS:
        ids = [x['id'] for x in D if x['status'] == 'MIDDLE' and sec[x['part']] == n]
        L.append('- **S%d**: %s' % (n, ', '.join(ids) or 'none'))
    L += ['', '## 3. The text, sentence by sentence', '',
          'Each line: `id | mark | the sentence`, in the order of the text; headings as they stand. A sentence longer '
          'than 1,500 characters is cut at a space, the later pieces marked `(cont.)`.', '']
    for n, l in enumerate(tl, 1):
        if l.startswith('#'):
            L += ['', l, '']
            continue
        for x in by_line.get(n, []):
            t = x['text'].replace('\n', ' ')
            pieces = split_long(t)
            L.append('`%s` | %s | %s' % (x['id'], mark_of(x, sec), pieces[0]))
            L += ['`%s` (cont.) | %s' % (x['id'], pc) for pc in pieces[1:]]
    L += ['', '## 4. The formal core, definition by definition', '',
          'The formal core after the fourth review round, from its section 0 on, with a mark line `⟦FROZEN⟧` or '
          '`⟦S<n>⟧` before each definition and encoding. Quotations of the text (`> Lnnn | …`) are as the core has them, '
          'of the text as the maths round read it; where a line changed since, section 3 above has its words now. '
          'Lines longer than 1,500 characters are cut at a space, the later pieces marked `(cont.)`.', '']
    dmark = {x['id']: mark_of(x, sec) for x in D}
    started = False
    for l in lines_of(core_text):
        if l.startswith('## §0'):
            started = True
        if not started:
            continue
        m = re.match(r'^\*\*((?:D\d+\.(?:\d+|new\d+|XV))|(?:E\d+))\b', l)
        if m:
            need(m.group(1) in dmark, '%s has no mark' % m.group(1))
            L += ['⟦%s⟧ %s' % (dmark[m.group(1)], m.group(1))]
        pieces = split_long(l)
        L.append(pieces[0])
        L += ['(cont.) ' + pc for pc in pieces[1:]]
    L += ['', '## 5. The claims, by section', '',
          'Each claim with the lines its statement cites; the section is that of the Parts of those lines. A claim is '
          'a consequence the program tests; a variant that changes a definition may change a claim\'s result.', '',
          '| claim | title | lines | section | result now |', '|---|---|---|---|---|']
    part_of_line = {x['line']: x['part'] for x in S}
    for c in claims:
        lines = sorted({s['line'] for s in c.get('source') or []})
        secs = sorted({sec[part_of_line[n]] for n in lines if n in part_of_line})
        res = c.get('status_now') or ''
        L.append('| %s | %s | %s | %s | %s |' % (c['id'], c['title'].replace('|', '\\|')[:110], ', '.join('L%d' % n for n in lines),
                                              ', '.join('S%d' % s for s in secs) or '—', res))
    return '\n'.join(L) + '\n'


# ------------------------------------------------------------------ the briefs
INTRO = """# Part A of an experiment on a semantics: section {n} of 4, {title}

## 1. What this is

A theory, called here the semantics, is stated in a prose text ({nlines} lines, cited as L1 to L{nlines}) and in a formal core: definitions (D§.n, each with the sentences it formalizes quoted above it), encodings of the text's worked cases (E1 to E9), and formal claims (FCnn) that a program in `model/` tests on small structures. In this brief a "model" is only such a small structure, or the program's folder; what the theory judges is always called a candidate or an explanation.

The owner of the theory asked for an experiment in two parts (S52, section 2). This is Part A: freeze the parts that are hard to vary, change bits around in the middle, and see how that changes how explanation is defined. **The goal is to map dependencies.** Four agents work at the same time on the same frozen template, each on its own section of the middle. You are the agent for **section {n}: {title}** ({parts}; L{l0} to L{l1}).

Nothing you propose changes the theory. Part A is an experiment on copies: your variants are read, then implemented and computed by other agents in their own copies of the program; the map and a list of candidate definitions of explanation are what come out of it.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths. Who made a point decides nothing, only its reasons do."""

SANDBOX = """## 3. The sandbox and your tools

| file or folder | what it is |
|---|---|
| `template/the frozen template.md` | **the frozen template**, the same for the four agents: every sentence of the text, one per line, and every definition and encoding of the formal core, each marked FROZEN or S1 to S4 (its section); the four sections; the claims by section. Start here |
| `template/the frozen set.md` | why each item is frozen or in the middle, item by item, with the criterion as applied |
| `text/the text.md` | the text exactly as it stands |
| `text/the text, by line.md` | the same text, one line per text line as `L<n> \\| ...`, long lines cut into pieces of at most 1,500 characters |
| `maths/formal core, now.md` | the formal core as it stands, unmarked |
| `maths/formal claims, now.md` and `.json` | the claims and their results now: {claims_counts} |
| `maths/inventions ....md` | the inventions (Inn): every choice the maths made that the text leaves open, with the other choices |
| `maths/parked, now.md`, `maths/parked P1-P7.md` | points parked (not to be argued) |
| `maths/owner questions, now.md` | questions put to the owner and their status |
| `maths/formal claims FC-E1 to FC-E5, external examples.md` | five claims from an outside cross-examination |
| `cases/creative transport case card.md`; `cases/code of ... (read only).py` | a worked case supplied by the owner, and the code that reads it, the external examples and the cases of the written-in step (you can read it; it does not run here) |
| `program printouts/` | the program's printouts as the theory now stands: the whole suite at scale 4 (every claim, in full), the external examples, the creative transport case, the cases of the written-in step |
| `model/` | the program, standard-library Python: `core.py` (organizations, questions, candidates, the account), the claims files (one function per claim), `args.py`, `phys.py`, `gen.py` (the generators), `cases.py`, `e9.py`, `inventions_model.py` |
| `BRIEF.md` | this brief |

Your tools. **Read** (read a long file in pieces with offset and limit), **Glob** and **Grep**, inside this folder only. **Bash** runs one command only, typed plainly from this folder: `python3 -m model.run` with `--claim FCnn` (repeatable, for example `--claim FC23 --claim FC30.new1`), `--scale N` (at most 4), `--time-cap N` (at most 60), `--brief`, `--help`. Anything else is refused, and nothing can be written. Run a claim to read how the theory as it stands behaves on its small cases; that is your baseline. You cannot change the program or run new code: a variant is written in the formal core's notation, and a small case as Python in the program's notation (as in `model/core.py`) or in the printouts' format, with the result you expect, marked "not run". Other agents implement and compute it. Work economically: read what your section needs, search with Grep.

**Only your final message is kept.** Write the whole report in your last message, after your last tool call."""

EXPLANATION = """## 4. How explanation is defined now: what every variant is traced against

This is the target of your job (ii). Each item carries its mark in the template; the lines and definitions are the places to read.

{explanation}

What counts as "how explanation is defined" here: (E) with its conjuncts and what each reads (the question, the contract, the transport, the commitments, the designation, the scope statement); being an explanation, Account ∧ ¬Dec(t); the provenance of a transport (selected, constructed, declared) as far as Dec reads it; and what the text says (E) excludes and does not exclude. A change elsewhere matters to it exactly when it changes which candidates meet these, or what meeting them says."""

JOB = """## 5. Your job, for section {n}

Your section: **{parts}** (L{l0} to L{l1}): {n_ms} middle sentences and {n_md} middle definitions and encodings, marked **S{n}** in the template. Its middle definitions: {mdefs}. Every item marked FROZEN, and every item of the other three sections, stays exactly as it is.

**(i) Vary.** Change bits of **your section only**: a definition, a condition in it, a claim, a sentence. Propose several distinct variants (about five to eight), each small and exact, each written in the formal core's notation beside the item it replaces, with its id. A variant may delete a condition, weaken it, strengthen it, swap it for another, or re-order conditions. A variant of a sentence is given as the formal statement of the new sentence. Choose variants that bear on how explanation is defined, directly or through what it reads; say in one line why each was chosen.

**(ii) Trace each variant's effect on how explanation is defined** (section 4). Which candidates newly count, and which stop counting: as meeting (E), and as explanations (Account ∧ ¬Dec(t)). Show it with small concrete cases, in the program's format where you can: a question p (target, contract, query), a candidate ℰ (organization, transport, commitments, designation), and the result before and after the variant. Use the text's own cases where they serve (the table of observed answers, the reversed calculation, "p because p", the pole and its shadow, the swap, the skew-symmetric matrices, the student's declared formula, the weathervane, the shop sign, the bridge, the creative transport case). Run the existing claims to read the result before the variant; mark the result after it "not run".

**(iii) Map dependencies.** For each variant, the edges it shows:
- **blocks**: a FROZEN item the variant cannot stand beside (they contradict, or a frozen sentence can no longer be read by the varied definition): the item, and why in one line;
- **constrains**: a FROZEN item that limits how the variant can be written, without ruling it out;
- **changes with**: an item of another section that would have to change with the variant for the theory to hang together (its id, its section, and what would change);
- **moves**: a part of the explanation definition that moves (a conjunct of (E), what a conjunct reads, Dec, Expl, (Suff) or (Nec)), and how.
These edges are the goal (S52). An edge you cannot settle, say so, with what would settle it.

**(iv) Keep to the form** (sections 6 and 7)."""

FORM = """## 6. The form of every variant, and the owner's words

Every variant is exactly one of:
1. **maths**: a changed definition, condition or claim, in the formal core's notation, beside the one it replaces, with the id it changes (new ids as `D§.n.v<k>` or `FCnn.v<k>`);
2. **code**: the same change as Python in the program's notation, with the small case and the result you expect, marked "not run".

Never new prose: a variant of a sentence is its formal statement, not a rewording.

The owner's words bind every variant as content. A variant may explore a definition the owner's decisions would reject: that is how later candidates are found. When a variant does, say so plainly, in its row, and name the decision (for example: rejected by S41, Q2, "No, not if just declared"; by S45, a written-in answer never stops a candidate being an explanation; by S25 to S27, physical possibility only where information or knowledge is instantiated or transformed; by S47, the maths asks for nothing). Beyond that: do not list, count, grade or rank rivals, and do not argue from how many (S20); nothing about what must happen to a candidate (S21); every word S23 forbids stays out of every name, gloss and variant, "argument" is reasons why this and not that, and every accepting is tentative (S23); nothing is settled (S28); nothing about what hard to vary covers in general, or about what makes an explanation a bad one (S33, S34; parked); every choice the text leaves open that you make is named as an invention, with the other choices (S36); AI programs are not part of the semantics (S43). Where values are placed is the owner's question: vary nothing that moves them. Never call a candidate a "model"."""

REPORT = """## 7. The report

Terse: tables, formulas, small cases in the program's format, one-line reasons. No summary of the material. At most about 3,000 words.

Sections, in this order:
(a) **the variants**, one table: id (V{n}.1, V{n}.2, ...), item(s) varied, old → new (formula), kind (delete, weaken, strengthen, swap, re-order, other), why chosen (one line), the owner's decision it departs from, if any (or "none");
(b) **the traces**, one block per variant: which candidates newly meet (E) or newly count as explanations, which stop; the small cases, before and after, each marked run (with the command and the program's result line) or "not run";
(c) **the edges**, one table for all variants: variant, kind (blocks, constrains, changes with, moves), item (id and section, or the part of the explanation definition), why in one line, settled or not;
(d) **the items of your section you did not vary** that you judge bear most on how explanation is defined, one line each on why not;
(e) **inventions** your variants rest on, with the other choices.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bfalse\b",
         r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*",
         r"\bvalid\w*", r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*",
         r"\bgrade[sd]?\b", r"\bwrong\b", r"\bprefer\w*",
         r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bFable\b", r"\bOpus\b", r"\bSonnet\b", r"\bDeutsch\b",
         r"\bMarletto\b", r"\bPinker\b", r"\blog S\d", r"\bS(?:9\d|1\d\d)\b", r"\bCONFIRMED\b"]
MODEL_FOR_CANDIDATE = [r"\bmodels? counts? as (cheat|simply|just|an? explanation|explain)", r"\bwhen does a model\b",
                       r"\b(candidate|explanatory) models?\b", r"\bmodels? (that|which) explains?\b",
                       r"\ba model (is|as) an explanation\b"]
FRAME_MODEL = MODEL_FOR_CANDIDATE + [r"\bmodell?(ed|ing)\b"]
ALLOWED_IN_FRAME = ["do not list, count, grade or rank rivals"]


def frame_of(text):
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The sandbox)", "", text)
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    hits = sorted({m.group(0) for pat in SCRUB + FRAME_MODEL for m in re.finditer(pat, f, re.I)})
    for m in re.finditer(r"\bS(\d\d)\b", f):
        if int(m.group(1)) not in KEEP:
            hits.append(m.group(0))
    return hits


def model_for_candidate(text):
    return sorted({m.group(0) for pat in MODEL_FOR_CANDIDATE for m in re.finditer(pat, text, re.I)})

# How explanation is defined now: written from the text and the formal core after round 4 (checked by the build
# against both: every id named must be in the core, every line cited must hold the words quoted).
EXPLANATION_NOW = """- **Account (E)**, D6.7, L262: Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous, for a candidate ℰ = (E, p, t, Γ, δ_E) (D5.3, L231) of a question p = (D, C, b0, Q, δ_D, O_p, ρ_p) (D3.1, L137). Its conjuncts: (F1), component fidelity, D5.4, L233–L237; (F2), global fidelity with Hom(τ), D5.5, L239–L243; (A), question fidelity, D5.6, L247–L253; Dependence := NC0 ∧ NC2, some contrast of E's answers at a pair of C (in Y_p ∪ {⊥}) lost when a nonempty block of Γ is deleted, D6.2, D6.4, D6.5, L255; NonVacuous, Sol_D(1,b0) ≠ ∅ ∧ Stated(C, Σ), D6.6, D3.5, L257. Acc takes no assessor, no history, no provenance and no grain (FC30).
- **Being an explanation**: Account(ℰ) ∧ ¬Dec(t) (L17, L49, L61, L69); D16.XV: Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ), the owner's answer Q2 in S41 ("No, not if just declared"). Dec(t), the provenance "declared", is neither selected (Sel, D12.1, L193–L195) nor constructed (CT, D12.2, L197), read per holding (D12.3, D12.4, L199–L211).
- **What (E) excludes, and what it does not** (L267–L277): a table of observed answers fails (F1) (E_tab, D6.10, FC25); a table that encodes the response to every admitted change meets (F1), and (E) where it meets the rest (E_enc, FC25.new2); a reversed calculation fails (F2) under the production contract (L271, FC27), and under τ′, which sets the calculation's relation, it is another candidate, which meets every conjunct (FC27.new1 (d)); a contrast no admitted edit realizes fails Dependence (L275). A written-in answer never stops a candidate being an explanation (S44, S45): the slot test NC1 and the pin (D6.3) stay defined, and are not conjuncts of (E).
- **The claims about it**: (Suff) and (Nec), L536 and L538, with their formal shapes in D16.XV; the owner's four answers as encoded: Q2 FC30.new1, Q6 FC84.new1 (with S47), Q15 FC22 (b), Q23 FC72 and FC72.new1.
- **In the program**: `core.account` (in `model/core.py`) computes Acc; `core.NC2` its Dependence; `core.slot` and `core.NC1` the written-in test, read by no conjunct of Acc. The claims FC21 to FC31, FC23.new1 to FC23.new3, FC25.new2 and FC30.new1 read it, and the printouts give their results now."""
SECTION_TITLES = {}      # n -> title, from SECTIONS


def sources():
    """(path in the sandbox, source under Semantics/, md5 or None)."""
    s = [('template/the frozen template.md', TEMPLATE, None), ('template/the frozen set.md', FROZEN_MD, None),
         ('text/the text.md', TEXT[0], TEXT[1]), ('text/the text, by line.md', BYLINE, None),
         ('maths/formal core, now.md', CORE[0], CORE[1]), ('maths/formal claims, now.md', CLAIMS_MD[0], CLAIMS_MD[1]),
         ('maths/formal claims, now.json', CLAIMS_JSON[0], CLAIMS_JSON[1])]
    s += INVENTIONS + OTHER
    s += [(dst, rel, None) for dst, rel, _, _ in PRINTOUTS]
    s += [('model/' + f, MODEL_DIR + '/model/' + f, None) for f in model_files()]
    return s


def by_line(text, text_md5):
    out = ['# The text, by line', '',
           'A reading copy of `text/the text.md` (md5 %s), made so that no line is longer than 1,500 characters. Each '
           'line of the text is given as `L<n> | <line>`; a line longer than 1,500 characters is cut at a space into '
           'pieces, the second and later written `L<n> (cont.) | <piece>`. Empty lines are given as `L<n> |`. Nothing '
           'else differs from the text.' % text_md5, '']
    for n, l in enumerate(lines_of(text), 1):
        pieces = split_long(l)
        out.append(('L%d | %s' % (n, pieces[0])).rstrip())
        out += ['L%d (cont.) | %s' % (n, pc) for pc in pieces[1:]]
    return '\n'.join(out) + '\n'


def claims_now(cj):
    """The claims with their result now (the last result the claims file records)."""
    out = []
    for c in cj['claims']:
        st = None
        for k in ('after_round4', 'after_r4', 'after_s106', 'after_round3', 'after_s41', 'after_round2'):
            v = c.get(k)
            if v:
                st = v.get('status') if isinstance(v, dict) else re.search(r"'status': '([^']+)'", str(v)).group(1)
                break
        out.append(dict(c, status_now=st or ''))
    return out


def section_spans(text, sec):
    """The lines of each section: from the heading of its first Part (or line 1) to the line before the next section's."""
    starts = {}
    for n, l in enumerate(lines_of(text), 1):
        m = re.match(r'^# (Part [0IVX]+) — ', l)
        if m:
            starts.setdefault(sec[m.group(1)], n)
    starts[1] = 1
    N = len(lines_of(text))
    order = sorted(starts)
    return {k: (starts[k], (starts[order[i + 1]] - 1) if i + 1 < len(order) else N) for i, k in enumerate(order)}


def check_frozen_set():
    for rel in (FROZEN_JSON, FROZEN_MD):
        need(committed(rel), '%s is not committed, or differs from HEAD' % rel)
    r = subprocess.run([sys.executable, '-B', os.path.join(HERE, 's108_frozen_set.py'), '--state', 'r4', '--check'],
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    need(r.returncode == 0, 'the frozen set does not rebuild identical: %s' % (r.stdout + r.stderr)[-400:])


def build():
    sec = section_of_part()
    for n, first, last, title in SECTIONS:
        SECTION_TITLES[n] = title
    need(EXPLANATION_NOW, 'the summary of how explanation is defined now is not written yet')
    core_ids = set(re.findall(r'(?m)^\*\*((?:D\d+\.(?:\d+|new\d+|XV))|(?:E\d+))\b', read(CORE[0])))
    claim_ids = {c['id'] for c in json.loads(read(CLAIMS_JSON[0]))['claims']}
    for d in re.findall(r'\b(D\d+\.(?:\d+|new\d+|XV)|E\d)\b', EXPLANATION_NOW):
        need(d in core_ids, 'the summary names %s, which the core does not hold' % d)
    for c in re.findall(r'\b(FC\d+(?:\.new\d+)?)\b', EXPLANATION_NOW):
        need(c in claim_ids, 'the summary names %s, which the claims do not hold' % c)
    # the frozen set must be the committed one, and rebuilt identical
    check_frozen_set()
    fs = json.loads(read(FROZEN_JSON))
    text, core_text = read(TEXT[0]), read(CORE[0])
    cj = json.loads(read(CLAIMS_JSON[0]))
    claims = claims_now(cj)
    bad = [c['id'] for c in claims if not GUARD_CLAIM.fullmatch(c['id'])]
    need(not bad, 'claim ids the sandbox guard cannot run alone: %s' % bad)
    files = OrderedDict()
    files[BYLINE] = by_line(text, md5_file(TEXT[0]))
    files[TEMPLATE] = template(fs, text, core_text, claims, sec)
    # every source other than the ones this build writes is committed and unchanged
    written = {TEMPLATE, BYLINE}
    for dst, rel, h in sources():
        if rel in written:
            continue
        need(os.path.isfile(path(rel)), '%s is not there' % rel)
        need(h is None or md5_file(rel) == h, '%s has md5 %s, expected %s' % (rel, md5_file(rel), h))
        need(committed(rel), '%s is not committed, or differs from HEAD: the material must be fixed first' % rel)
    need(committed('records/Semantics - Decisions.md'), 'the decisions record differs from HEAD')
    owner, own = owner_words(read('records/Semantics - Decisions.md'))
    S, D = fs['sentences'], fs['definitions']
    span = section_spans(text, sec)
    cc = Counter(c['status_now'] for c in claims)
    need(set(cc) <= set(STATUS), 'a claim with no result now: %s' % cc)
    claims_counts = '%d hold on every model tried, %d have a counterexample, %d were not tested, of %d' % (
        cc['HOLDS ON ALL MODELS TRIED'], cc['COUNTEREXAMPLE FOUND'], cc['NOT TESTED'], len(claims))
    rows = []
    for n, first, last, title in SECTIONS:
        ps = [p for p in PARTS if sec[p] == n]
        l0, l1 = span[n]
        parts = '%s to %s' % (first, last) if first != last else first
        mdefs = [x['id'] for x in D if x['status'] == 'MIDDLE' and sec[x['part']] == n]
        n_ms = sum(1 for x in S if x['part'] in ps and x['status'] == 'MIDDLE')
        b = '\n\n'.join([INTRO.format(n=n, title=title, nlines=len(lines_of(text)), parts=parts, l0=l0, l1=l1),
                         owner, SANDBOX.format(claims_counts=claims_counts), EXPLANATION.format(explanation=EXPLANATION_NOW),
                         JOB.format(n=n, parts=parts, l0=l0, l1=l1, n_ms=n_ms, n_md=len(mdefs), mdefs=', '.join(mdefs) or 'none'),
                         FORM, REPORT.format(n=n)]) + '\n'
        hits = scan(b)
        need(not hits, 'brief %d: the frame holds %s' % (n, hits))
        need(words(b) <= CAP, 'brief %d has %d words, above %d' % (n, words(b), CAP))
        for k in KEEP:
            need(OWNER_CHECK.get(k, own[k].split('"')[1]) in b, "brief %d lacks the owner's words of S%d" % (n, k))
        rel = 'tests/S108 Part A - GLM section %d, %s.md' % (n, title)
        files[rel] = b
        rows.append((n, title, 's108_glm_section%d' % n, rel, words(b), md5(b)))
    # the manifest: every file of the sandbox, checked by md5 at the copy; the brief is added as BRIEF.md
    entries = []
    for dst, rel, _ in sources():
        body = files.get(rel)
        entries.append({'path': dst, 'src': rel, 'md5': md5(body) if body is not None else md5_file(rel)})
        if not dst.endswith('.py'):
            t = body if body is not None else read(rel)
            hit = model_for_candidate(t)
            need(not hit, '%s uses "model" for a candidate: %s (decision S43)' % (rel, hit))
    for e in entries:
        need(not re.search(r'(\.env$|key)', e['path'], re.I), 'a sandbox path looks like a key file: %s' % e['path'])
    manifest = {'note': "Part A of decision S52, round 1 (log S108): the files copied into each GLM call's sandbox, each "
                        "checked by md5 at the copy; the brief is added as BRIEF.md. Written by tools/s108_build.py.",
                'text': {'path': TEXT[0], 'md5': md5_file(TEXT[0]), 'lines': len(lines_of(text))},
                'frozen_set': {'path': FROZEN_JSON, 'md5': md5_file(FROZEN_JSON)},
                'sections': [{'section': n, 'parts': [p for p in PARTS if sec[p] == n], 'title': t} for n, _, _, t in SECTIONS],
                'decisions_record': {'path': 'records/Semantics - Decisions.md', 'md5': md5_file('records/Semantics - Decisions.md')},
                'printout_commands': {dst: 'PYTHONHASHSEED=0 python3 ' + ' '.join(a) + '  (from ' + MODEL_DIR + ')'
                                      for dst, _, a, _ in PRINTOUTS},
                'files': entries}
    files[MANIFEST] = json.dumps(manifest, indent=1, ensure_ascii=False) + '\n'
    jobs = {'round': 'Part A of decision S52, round 1 (log S108)', 'rule': READING_RULE, 'out': OUT, 'max_pass': 3,
            'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'manifest': MANIFEST, 'manifest_md5': md5(files[MANIFEST]),
            'sandbox_root': 's108_sandboxes', 'home_root': 's108_homes', 'helper': 'tools/glm_via_claude_code_sandboxed.py',
            'jobs': [{'job': n, 'name': 'section%d' % n, 'tag': tag, 'brief': rel, 'brief_md5': h}
                     for n, title, tag, rel, w, h in rows]}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows, manifest


def main():
    a = sys.argv[1:]
    need(set(a) <= {'--check', '--printouts', '--sections'}, 'usage: s108_build.py [--printouts | --sections | --check]')
    if '--printouts' in a:
        printouts()
        return
    if '--sections' in a:
        fs = json.loads(read(FROZEN_JSON))
        c = middle_counts(fs)
        print('middle items by Part:', ', '.join('%s %d' % (p, c[p]) for p in PARTS if c.get(p)), '; all', sum(c.values()))
        for dev, sizes, parts in splits(c)[:12]:
            print('%5.1f  %s' % (dev, ' | '.join('%s–%s (%d)' % (s[0], s[-1], z) for s, z in zip(parts, sizes))))
        return
    files, rows, manifest = build()
    if '--check' in a:
        for rel, text in files.items():
            need(os.path.exists(path(rel, out=True)) and open(path(rel, out=True), encoding='utf-8').read() == text,
                 '%s differs from the build' % rel)
        print('check: all %d files identical to the build' % len(files))
    else:
        for rel, text in files.items():
            print(('wrote   ' if write_checked(rel, text) else 'same    ') + rel)
    print('\n| section | title | tag | brief | words (build) | md5 |\n|---|---|---|---|---|---|')
    for n, title, tag, rel, w, h in rows:
        print('| %d | %s | %s | `%s` | %d | %s |' % (n, title, tag, rel, w, h))
    print('\nsandbox: %d files from the manifest + BRIEF.md; manifest md5 %s' % (len(manifest['files']), md5(files[MANIFEST])))


if __name__ == '__main__':
    main()
