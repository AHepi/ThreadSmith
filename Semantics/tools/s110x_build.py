#!/usr/bin/env python3
"""s110x_build.py: build the GLM cross-examination of log S110 (decisions S57, S58; decision S56: "Use GLM for cross
examination"). Written 29 September 2026 by the one Opus 5.5 agent of log S110, on the pattern of Part A round 2's
cross-examination build (tools/s108r2x_build.py): round 1's build (tools/s108_build.py) is imported for its helpers only,
never changed; the sandboxed helper (tools/glm_via_claude_code_sandboxed.py) and the shell guard
(tools/glm_sandbox_shell_guard.py) are used unchanged by the runner (tools/s110x_glm_loop.py).

Four GLM jobs at once (S39), each cross-examining the S110 work from one angle:
  (a) the change map against FW0 and I2;  (b) the change map against FW2, FW3 and FW4;
  (c) the change map against FW5, the present theory and the S89 audit;
  (d) files 1 and 3: internal consistency, Claude's readings passed off as the book's, the owner's decisions S20 to S58.
Each sandbox holds copies of the six frameworks, the present theory, the S89 audit and the S110 files, plus, per job, the
records its angle needs; NEVER the books or any text extracted from them (the quotations are checked by
tools/s110_quote_check.py instead). There is no program in the sandbox, so the guard refuses every command: GLM only
reads (Read, Glob, Grep) and writes nothing.

  python3 Semantics/tools/s110x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s110x_build.py --check    rebuild in memory and compare; writes nothing

Refuses unless every source is committed and unchanged from HEAD; the frame of each brief (everything but the owner's
words) holds none of the words decision S23 removes and no "model" for a candidate (S43); no sandbox path looks like a key
file; no sandbox file is one of the book extractions; each brief is at most CAP words.

Finished 29 September 2026 by a second Opus 5.5 agent after a system outage stopped the first before anything was sent:
job 3's sandbox now also holds the S96 record and the Revision 2 note on hard to vary, which the change map's "recorded"
edges e110, e119, e123 and e125 cite; nothing else changed.
"""
import json, os, re, sys
from collections import OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (round 1's build: read, never written; helpers only)

PRE = 'results/S110 - '
READING_RULE = PRE + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PRE + 'GLM cross-examination returns'
MAT = PRE + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s110x_jobs - S110, GLM cross-examination.json'
CAP = 7000
OWNER = [19, 20, 21, 23, 25, 27, 28, 31, 34, 43, 56, 57, 58]
FWDIR = 'tests/S110 Material - earlier frameworks, supplied by the owner/'
FW = ['FW0 REV from M0 - Creative revision events.md', 'I2 SPEC of FW1a - Executable inquiry.md',
      'FW2 JUMP from FW1a - Standing and capacity hierarchy.md', 'FW3 AMEND of FW2 via D1-D3 - Why-dependence.md',
      'FW4 RELATED to FW3 - Structural discharge.md', 'FW5 JUMP from FW2+FW3+FW4 - Explanatory construction.md']
F1 = "results/S110 Error correction from constructor theory's perspective.md"
F2 = 'results/S110 The change map - the earlier frameworks and the present theory.md'
F2J = 'results/S110 The change map - the earlier frameworks and the present theory.json'
F3 = 'results/S110 When something in a creative agent is knowledge - what the sources offer.md'
F4 = 'plain words/110 Error correction in constructor theory, and how the earlier attempts changed, in plain words.md'

COMMON = [('frameworks/' + f, FWDIR + f) for f in FW] + [
    ('theory/107 The semantics, standing alone, after round 4.md', 'tests/107 The semantics, standing alone, after round 4.md'),
    ('audit/S89 The theory against its sources - Deutsch and Marletto.md', 'results/S89 The theory against its sources - Deutsch and Marletto.md'),
    ('S110/1 Error correction from constructor theory\'s perspective.md', F1),
    ('S110/2 The change map.md', F2),
    ('S110/2 The change map.json', F2J),
    ('S110/3 When something in a creative agent is knowledge.md', F3),
    ('S110/4 plain words.md', F4),
    ('S110/the rule for reading this cross-examination.md', READING_RULE),
]
EXTRA = {
    3: [('records/S95 Does the semantics hold without verificationist words.md', 'results/S95 Does the semantics hold without verificationist words.md'),
        ('records/NOT-IN-BUNDLE.md', 'authority/NOT-IN-BUNDLE.md'),
        ('records/S108 Part A round 2 - what the variations found.md', 'results/S108 Part A round 2 - what the variations found.md'),
        ("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/S96 The scrubbed copy repaired.md',
         'results/S96 The scrubbed copy repaired - physical possibility, conflict by argument, premises taken as given.md'),
        ('records/Revision 2 - hard to vary restated through rivals and problems, 25 September.md',
         'tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md')],
    4: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md')],
}
JOBS = [
    dict(job=1, name='map-FW0-I2', tag='s110x_glm_a', title='the change map against FW0 and I2'),
    dict(job=2, name='map-FW2-FW4', tag='s110x_glm_b', title='the change map against FW2, FW3 and FW4'),
    dict(job=3, name='map-FW5-theory', tag='s110x_glm_c', title='the change map against FW5, the present theory and the S89 audit'),
    dict(job=4, name='files-1-3', tag='s110x_glm_d', title="files 1 and 3 for consistency, for readings passed off as the book's, and against the owner's decisions"),
]

ANGLE = {
    1: """Cross-examine **the change map against FW0 and I2** (`S110/2 The change map.md` and `.json`; `frameworks/FW0 ...`, `frameworks/I2 ...`). For every node whose id starts FW0. or I2.: is its place (section heading and locator) right, and does its one line say what the framework says there, no more? Which commitment, definition or device of FW0 or I2 that bears on information, knowledge, error correction, creativity or explanation has no node? For every edge in the steps FW0>FW2, FW0>I2 and I2>FW5: is its kind (kept, changed, added, dropped, replaced) what the two texts show; is its one line faithful to both ends; is it marked "inferred" wherever no supplied text states it, and is any edge marked "stated" that no text states? Are the map's claims about FW0 and I2 in its sections 1 (the lineage: the missing links, the same SHA-256 for FW1a in I2 and FW2, specification versions 0.1, 0.2 and 0.4), 4 (the per-theme table's FW0 and I2 rows), 5 (chains starting at FW0 or I2), 6 and 7 (the four-valued ledger; expected information gain; token counts) what the texts show? Is the list of missing links complete for what FW0 and I2 name?""",
    2: """Cross-examine **the change map against FW2, FW3 and FW4** (`S110/2 The change map.md` and `.json`; `frameworks/FW2 ...`, `frameworks/FW3 ...`, `frameworks/FW4 ...`). For every node whose id starts FW2., FW3. or FW4.: is its place right, and does its one line say what the framework says there, no more? Which commitment, definition or device that bears on information, knowledge, error correction, creativity or explanation has no node? For every edge in the steps FW2>FW3 and FW3>FW4: does the row of FW3's change register (or the text) cited in "by" say what the edge says; is each "stated" edge stated, and each "inferred" one marked; are FW3>FW4 edges marked "stated" only where FW5 or FW4 states them? Is the map's section 8 (the knowledge position of FW3 and FW4: how it arose, changed and fared) faithful to FW2, FW3 and FW4, including the quotations it gives them? Are sections 3 (items 1 to 4), 4 (the FW2, FW3 and FW4 rows), 5, 6 and 7 right about these three? Is the list of missing links complete for what they name (D1 to D3, Q2, the addenda A1 to A3, C1, C2, E1, M3)?""",
    3: """Cross-examine **the change map against FW5, the present theory and the S89 audit** (`S110/2 The change map.md` and `.json`; `frameworks/FW5 ...`; `theory/107 ...`; `audit/S89 ...`; and, for the edges marked "recorded", the records under `records/`). For every node whose id starts FW5. or PT.: is its place right, and does its one line say what the text says there, no more? Which commitment, definition or device of FW5 or of the present theory that bears on information, knowledge, error correction, creativity or explanation has no node? For every edge in the steps >FW5 and FW5>PT: is each "stated" edge stated by FW5's "Reconciliation with the supplied evolution" or text as cited; is each "recorded" edge said by the record it cites (the S89 audit's observations, the S95 record, the S96 record, the Revision 2 note on hard to vary, NOT-IN-BUNDLE.md, the S108 record, the owner's decisions), and no more; is each "inferred" edge marked? Is the present theory's text searched correctly (the map says "information" and "knowledge" occur 0 times; check)? Does the S110 work use the S89 audit faithfully, build on it and not contradict it without saying so? Check also file 1's section 6 item 5 and file 3's options O10 and O11 against the present theory's text.""",
    4: """Cross-examine **files 1 and 3** (`S110/1 ...` and `S110/3 ...`), with file 4 (`S110/4 plain words.md`) where it repeats them, for three things. (i) **Internal consistency**: does each file say the same thing in its summary, body and open questions; do files 1 and 3 agree with each other and with the change map where they meet; are counts and cross-references right? (ii) **Claude's readings passed off as the book's**: each statement is marked [book] (quoted or "paraphrase"), [implied] (a short argument) or [reading]. The book is not in your sandbox (its quotations were checked by a script against the book's text), so judge from the quotations each file gives and from the S89 audit: flag any statement marked [book] or "paraphrase" that says more than the quotations around it show, any [implied] step whose argument has a gap (name the gap), and any [reading] that is stated elsewhere as if it were the book's. (iii) **The owner's decisions S20 to S58** (section 2 below; the whole record in `records/the owner's decisions.md`): nothing settled (S28); no ranking or grading of the options, no "better than" (S20, S23); no word S23 removes in Claude's own sentences (quotations excepted); "candidate" or "explanation", never "model", for what the theory judges (S43); what hard to vary covers kept parked (S34); every option in file 3 with a concrete everyday example first; resolution and choice left to the owner (S21). Does file 3 examine the two-types result of FW3 and FW4 without settling it?""",
}

INTRO = """# A cross-examination of a mapping job: job {job} of 4, {title}

## 1. What this is

The owner of a theory of explanation and creativity (the "present theory", `theory/107 ...`) asked for two things (section 2, S57, S58): a description of error correction from the perspective of constructor theory, the physics of which transformations are possible and which impossible, as Chiara Marletto's book *The Science of Can and Can't* (2021) gives it; and a "change map" of six of the owner's earlier frameworks (`frameworks/`: FW0, I2, FW2, FW3, FW4, FW5), showing how each changed into the next and into the present theory, and how each treats information, knowledge and error correction. Behind both is the owner's question: how to tell when something in a creative agent is knowledge.

One agent did the job and wrote: file 1, error correction from constructor theory's perspective; file 2, the change map (`.md`, and its data in `.json`: 172 nodes, 132 edges, each edge with a kind and a standing: "stated" by the frameworks, "recorded" by this project's records, or "inferred" by the agent); file 3, what the sources offer for telling when something is knowledge; file 4, a plain-words version for the owner. An earlier audit of the theory against its two source books, which the job builds on, is `audit/S89 ...`. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory or the frameworks. What you find is read by one agent after every cross-examination has ended, under the rule in `S110/the rule for reading this cross-examination.md`, and each objection is settled there by argument; findings that stand are applied to corrected copies of the S110 files.

Who is who: "the owner" is the person whose theory and frameworks these are; "Claude" is the agent that did the job. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it. **No command runs here**: there is no program in this folder, and every shell command is refused. You write nothing. The books themselves are not here: their quotations in the S110 files were checked by a script as exact pieces of the books' text, at most 25 words each, so do not object that a quotation is inexact unless something in this folder shows it (the S89 audit quotes the books too).

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `frameworks/` | the owner's six earlier frameworks, as supplied (each opens with "Where this belongs": its predecessors, where it leads, and how sure the placement is) |
| `theory/107 ...` | the present theory |
| `audit/S89 ...` | the earlier audit of the theory against Deutsch's and Marletto's books |
| `S110/` | the four S110 files, the change map's data, and the rule for reading this cross-examination |
{extra_rows}"""

REPORT = """## 5. The report

Terse. No summary of the material, no praise, no restating of what holds. At most about 3,000 words.

(a) **Objections**, one table, most serious first: id (X{job}.1, X{job}.2, ...); the file and the place (section, table row, node id, edge id); the objection in one or two lines; what shows it (a quotation from a file in this folder, with its place); **the exact fix** (the sentence, the row, the node's line, the edge's kind or standing as it should read).
(b) **Checked, no objection**: one line listing what you examined and found nothing to object to (ids or sections only).
(c) **Not reached**: one line each, with why.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

S23 = [r"\bfits?\b", r"\bfitting\b", r"\bsupport(s|ed)?\b", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
       r"\bdisprov\w*", r"reason to (believe|reject)", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b",
       r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*"]


def frame_scan(b):
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The sandbox)", "", b)
    f = re.sub(r'"[^"\n]*"', ' ', f)   # quoted words are the owner's or the files', not the frame's
    f = re.sub(r'`[^`\n]*`', ' ', f)
    return sorted({m.group(0) for pat in S23 + B.MODEL_FOR_CANDIDATE for m in re.finditer(pat, f, re.I)})


def owner_block():
    dec = B.read('records/Semantics - Decisions.md')
    out = []
    for n in OWNER:
        m = re.search(r"(?m)^S%d\. \[Claude's reading[^:\]]*: .*?\] (.*)$" % n, dec)
        B.need(m, 'decision S%d not found' % n)
        out.append('**S%d.** %s' % (n, m.group(1)))
    return ("## 2. The owner's words\n\nThe owner's decisions that bind this work, in the owner's words as the project's record "
            "keeps them (each record entry also holds Claude's reading, in square brackets, left out here; the whole record "
            "is in `records/the owner's decisions.md` where your job has it). They bind as content: an objection that the "
            "work goes against one names it and quotes it.\n\n" + '\n\n'.join(out))


def build():
    files = OrderedDict()
    owner = owner_block()
    jobs_out, rows = [], []
    for j in JOBS:
        ent = list(COMMON) + EXTRA.get(j['job'], [])
        entries = []
        for dst, rel in ent:
            B.need(os.path.isfile(B.path(rel)), '%s is not there' % rel)
            B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
            B.need(not re.search(r'(\.env$|key)', dst, re.I), 'a sandbox path looks like a key file: %s' % dst)
            B.need('s110_book' not in rel and 'scratchpad' not in rel, 'a book extraction would enter the sandbox: %s' % rel)
            entries.append({'path': dst, 'src': rel, 'md5': B.md5_file(rel)})
        extra_rows = '\n'.join('| `%s` | %s |' % (d, 'a copy of the project record `%s`' % s) for d, s in EXTRA.get(j['job'], []))
        b = '\n\n'.join([INTRO.format(job=j['job'], title=j['title']), owner, TOOLS_TEXT.format(extra_rows=extra_rows),
                         '## 4. Your job: ' + j['title'] + '\n\n' + ANGLE[j['job']] +
                         "\n\nThe owner's words bind the work as content (section 2): nothing about what must happen to "
                         "an option (S21), nothing about which option to choose (S20), no word S23 removes. For what the "
                         "theory judges say \"candidate\" or \"explanation\", never \"model\" (S43).",
                         REPORT.format(job=j['job'])]) + '\n'
        hits = frame_scan(b)
        B.need(not hits, 'brief %d: the frame holds %s' % (j['job'], hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (j['job'], B.words(b), CAP))
        rel = 'tests/S110 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Log S110, the GLM cross-examination (S56), job %d: the files copied into its sandbox, each checked by "
                       "md5 at the copy; the brief is added as BRIEF.md. No book text. Written by tools/s110x_build.py." % j['job'],
               'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'log S110, the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's110x_sandboxes', 'home_root': 's110x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s110x_build.py [--check]')
    files, rows = build()
    if '--check' in a:
        for rel, text in files.items():
            B.need(os.path.exists(B.path(rel)) and B.read(rel) == text, '%s differs from the build' % rel)
        print('check: all %d files identical to the build' % len(files))
    else:
        for rel, text in files.items():
            print(('wrote   ' if B.write_checked(rel, text) else 'same    ') + rel)
    print('\n| job | angle | tag | brief | words | md5 | sandbox files |\n|---|---|---|---|---|---|---|')
    for r in rows:
        print('| %d | %s | %s | `%s` | %d | %s | %d + BRIEF.md |' % r)


if __name__ == '__main__':
    main()
