#!/usr/bin/env python3
"""s108r2_build.py: build Part A of decision S52, ROUND 2 (log S108): the four GLM briefs, the sandbox manifest and the
job list. Written 28 September 2026 by a Claude subagent (Opus 5.5) for the orchestrator. Round 1's build
(tools/s108_build.py) is imported, not changed: the same frozen set, the same frozen template, the same sections, the
same owner's words, the same form; round 2 adds round 1's outputs to the sandbox as background and gives each section
its share of round 1's gaps (the orchestrator's decisions on round 1's critical review, decision 4; the second
checker's list of gaps).

  python3 Semantics/tools/s108r2_build.py            build the briefs, the manifest and the job list; refuses to write
                                                     over a file whose content differs
  python3 Semantics/tools/s108r2_build.py --check    rebuild in memory and compare with the files; writes nothing

Checks before anything is written: round 1's frozen set, template, reading copy and printouts are committed and at
the md5s round 1's rule gives (the same template for round 2); every source committed and unchanged from HEAD; round
1's outputs committed and at the md5s the second checker gives; the owner's words against the record; the frame of each
brief free of the words S23 scrubs and of "model" used for a candidate (S43); each brief at most CAP words; every claim
id the guard can run; every definition id a share names is in the formal core and in the section it is given to.
"""
import json, os, re, sys
from collections import OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (round 1's build: read, never written)

SEM = B.SEM
R1 = 'results/S108 Part A - '
READING_RULE = 'results/S108 Part A round 2 - how the replies will be read, written before sending.md'
OUT = 'results/S108 Part A round 2 - returns'
JOBS_FILE = 'tools/s108r2_jobs - Part A round 2, GLM.json'
MAT = 'results/S108 Part A round 2 - material for the readers'
MANIFEST = MAT + '/sandbox manifest.json'
CAP = 7000
# Round 1's material, reused byte for byte (round 1's rule, 00adfab)
SAME = {B.TEMPLATE: '0c5ad2622fd2df95d073951d998418f3', B.BYLINE: '43142c41665438a30a3936458dd22d44',
        B.FROZEN_MD: '367c4b1f6022d5da37e1f153f2b8c05e', B.FROZEN_JSON: '30ca39e3203648a350dc97987c697765'}
# Round 1's outputs, as the second checker left them (2548f9f), as background
ROUND1 = [
    ('round 1/the dependency map.md', R1 + 'the dependency map.md', '1da37cf057ff02047fdeb1ca740eb5d8'),
    ('round 1/candidate definitions of explanation.md', R1 + 'candidate definitions of explanation.md',
     '6541dd847a158233662c895c7eb30c13'),
    ('round 1/the second checker on the critical review.md', R1 + 'the second checker on the critical review.md',
     'c757f7222e76a400ca0069f4b952017c'),
    ("round 1/the orchestrator's decisions on the critical review.md",
     R1 + "the orchestrator's decisions on the critical review.md", '23714d21b1cb260487b939124ed16142'),
    ('round 1/critical review.md', R1 + 'critical review.md', None),
    ('round 1/tabulation of the replies.md', R1 + 'tabulation of the replies, before any ruling.md', None),
] + [('round 1/section %d - variants computed.md' % n, R1 + 'section %d - variants computed.md' % n, None)
     for n in (1, 2, 3, 4)] + [
    ('round 1/replies/section %d.txt' % n, R1 + 'returns/s108_glm_section%d.response.txt' % n, None)
    for n in (1, 2, 3, 4)]
FRAME_LABELS = [r'S108-[1-4]-I\d+']     # round 1's invention ids, named in the shares: labels, not record names

INTRO = """# Part A of an experiment on a semantics, round 2: section {n} of 4, {title}

## 1. What this is

A theory, called here the semantics, is stated in a prose text ({nlines} lines, cited as L1 to L{nlines}) and in a formal core: definitions (D§.n, each with the sentences it formalizes quoted above it), encodings of the text's worked cases (E1 to E9), and formal claims (FCnn) that a program in `model/` tests on small structures. In this brief a "model" is only such a small structure, or the program's folder; what the theory judges is always called a candidate or an explanation.

The owner of the theory asked for an experiment in two parts (S52, section 2). This is Part A: freeze the parts that are hard to vary, change bits around in the middle, and see how that changes how explanation is defined. **The goal is to map dependencies.** Four agents work at the same time on the same frozen template, each on its own section of the middle. You are the agent for **section {n}: {title}** ({parts}; L{l0} to L{l1}).

**This is the second round.** In the first, four agents varied the four sections; other agents implemented and computed every variant, built a dependency map of 221 edges and a list of thirteen candidate definitions of explanation, and a review and a second check corrected both. Their files are in `round 1/` (section 3). The map has gaps: readings that round 1's candidates rest on and that were computed one way only; middle definitions no variant touched, some of them upstream of the explanation definition; and edges the computation could not settle. **Round 2 aims at these gaps.** Your section's share is in section 5. The frozen template, the frozen set and the sections are the same as in round 1.

Nothing you propose changes the theory. Part A is an experiment on copies: your variants are read, then implemented and computed by other agents in their own copies of the program; an updated map and an updated list of candidate definitions of explanation are what come out of it.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths. Who made a point decides nothing, only its reasons do."""

ROUND1_ROWS = """| `round 1/the dependency map.md` | round 1's map, as corrected: the parts of the explanation definition (its §1), how it changed with each varied item (§2), the FROZEN items the variants reached (§3), every edge with its standing, computed, contradicted or claimed only, and what would settle it (§4, §5), and the gaps (§6: §6.1 items no variant touched, §6.2 the edges claimed only, §6.3 the results that rest on one reading, §6.4 every untouched item by id) |
| `round 1/candidate definitions of explanation.md` | the thirteen candidates C1 to C13 found in round 1, what each admits and drops (computed), the reading each rests on, and the owner's decisions each does not appear to agree with |
| `round 1/section <n> - variants computed.md` | how each of round 1's variants was implemented and computed, section by section, with the inventions the computation forced (labelled like S108-1-I5) and the small cases |
| `round 1/replies/section <n>.txt` | round 1's four replies, as the agents wrote them |
| `round 1/tabulation of the replies.md`, `round 1/critical review.md`, `round 1/the second checker on the critical review.md`, `round 1/the orchestrator's decisions on the critical review.md` | how round 1's replies were read, reviewed and corrected, and what was decided for round 2 |"""

JOB = """## 5. Your job, for section {n}, in round 2

Your section: **{parts}** (L{l0} to L{l1}): {n_ms} middle sentences and {n_md} middle definitions and encodings, marked **S{n}** in the template. Its middle definitions: {mdefs}. Every item marked FROZEN, and every item of the other three sections, stays exactly as it is. Round 1's variants of your section are in `round 1/section {n} - variants computed.md`; do not repeat them: a round-2 variant either varies what they rest on, varies an item round 1 left untouched, or settles an edge round 1 left claimed only.

**Your share of round 1's gaps**, in this order:

{share}

**(i) Vary.** Change bits of **your section only**: a definition, a condition in it, a claim, a sentence, or a reading that a round-1 candidate of your section rests on (an invention; its other choices are named in the round-1 files). Propose as many distinct variants as your share needs (about six to ten), each small and exact, each written in the formal core's notation beside the item it replaces, with its id. A variant may delete a condition, weaken it, strengthen it, swap it for another, re-order conditions, or take a reading's other choice. A variant of a sentence is given as the formal statement of the new sentence.

**(ii) Trace each variant's effect on how explanation is defined** (section 4). Which candidates newly count, and which stop counting: as meeting (E), and as explanations (Account ∧ ¬Dec(t)). For a variant of a reading: which of round 1's candidates C1 to C13 change what they admit or drop, and which of their flags (the owner's decisions they do not appear to agree with) come or go. Show it with small concrete cases in the program's format where you can: a question p (target, contract, query), a candidate ℰ (organization, transport, commitments, designation), and the result before and after the variant. Use the text's own cases and the owner's where they serve (the table of observed answers, the reversed calculation, "p because p", the pole and its shadow, the student's declared formula, the weathervane, the shop sign with one part and with two, the bridge, the creative transport case). Run the existing claims to read the result before the variant; mark the result after it "not run".

**(iii) Map dependencies.** For each variant, the edges it shows: **blocks** (a FROZEN item the variant cannot stand beside), **constrains** (a FROZEN item that limits how it can be written), **changes with** (an item of another section that would have to change with it: id, section, what would change), **moves** (a part of the explanation definition that moves: a conjunct of (E), what a conjunct reads, Dec, Expl, (Suff) or (Nec), and how). For each claimed-only edge of your share: the variant or small case that would settle it, and the outcome you expect (the edge computed, or contradicted), marked "not run". An edge you cannot settle, say so, with what would settle it.

**(iv) Keep to the form** (sections 6 and 7)."""

REPORT = """## 7. The report

Terse: tables, formulas, small cases in the program's format, one-line reasons. No summary of the material. At most about 3,500 words.

Sections, in this order:
(a) **the variants**, one table: id (R2V{n}.1, R2V{n}.2, ...), item(s) or reading varied, old → new (formula), kind (delete, weaken, strengthen, swap, re-order, other choice of a reading, other), which part of your share it answers, the owner's decision it departs from, if any (or "none");
(b) **the traces**, one block per variant: which candidates newly meet (E) or newly count as explanations, which stop; for a reading, which of C1 to C13 move and which flags come or go; the small cases, before and after, each marked run (with the command and the program's result line) or "not run";
(c) **the claimed-only edges of your share**, one table: edge id, the variant or case proposed to settle it, the outcome expected (computed or contradicted), "not run";
(d) **the edges**, one table for all variants: variant, kind (blocks, constrains, changes with, moves), item (id and section, or the part of the explanation definition), why in one line, settled or not;
(e) **the items of your share you did not reach**, one line each on why not;
(f) **inventions** your variants rest on, with the other choices.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

# ------------------------------------------------------------------ the shares (the orchestrator's message for round 2)
EDGE = '`{id}` ({var}: {frm} {kind} {to}; to settle: {settle})'
SHARES = {
    1: {
        'readings': [
            "**S108-1-I5**, on which C2 (round 1's V1.5, D3.4) rests wholly: a question built with no recorded contract "
            "history counted as declared. Its other choice (ρ_p unknown, the case left out) makes V1.5 compute nothing. "
            "Vary the reading itself: ρ_p recorded as selected or as constructed on the owner's cases (the weathervane, "
            "the two-part sign), a found question with its trace (L155.s6), and the bridge's brief (S41 Q6, not computed "
            "in round 1); say which of C2's flags (S44, S41 Q15, S41 Q6) stand under each.",
            "**S108-1-I1**, on which C1 (V1.1, D1.4) partly rests: L_bv at a ≠ 1, (i) the one solution of D, or (ii) "
            "the baseline relation. Both were run; say whether any third reading the text allows changes C1's flag "
            "(S44).",
        ],
        'defs': "none: round 1 varied or reached all nine of your section. Then the untouched middle "
                "sentences of your section (round 1's map §6.4, S1 sentence middle, 132), above all those that state "
                "what an explanation is or what it reads: Part 0's statement of the claim (L11, L13, L15, L17) and of "
                "the kinds (L119), and Part III's respect, contract provenance and scope (L141, L151, L155, L159).",
        'edges': ['e1.02', 'e1.03', 'e1.14', 'e1.36', 'e1.37', 'e1.38', 'e1.39', 'e1.40'],
        'extra': "Round 1's V1.6 goes to section 2 (a condition on Acc) and V1.7 to the later part that varies the "
                 "frozen items; their edges (e1.45 to e1.51) are not yours.",
    },
    2: {
        'readings': [
            "**Edit or boundary**, on which C5 (V2.3, D6.4) rests: the owner's changes (the north wind, Tuesday) read as "
            "edits made to the vane and the sign (M13, the program's encodings) or as boundaries, circumstances "
            "(FC28.new2's D_vane; the sign with B = {mon, tue}). Read as boundaries, V2.3 drops the owner's weathervane "
            "and two-part sign (round 1's second checker's run). Vary the encoding of the owner's cases between the two, "
            "and any mixed reading the text allows (a change of the wind as an edit on one component and a boundary on "
            "another); say where C5's flags (S41 Q15, S44) stand.",
            "**D6.3's quantifier** (I136): 'every' (the program's), 'some', 'some-exempt', 'some-exempt-set'. C6 (V2.4, "
            "the written-in test back in (E)) keeps the owner's two-part sign under 'every' and drops it under the other "
            "three; C11 (section 4's V4.1) turns on it the same way. Vary Slot's quantifier as a reading of D6.3 on its "
            "own, with (E) as it is, and with V2.4 on; say for each which of the owner's cases move.",
            "**The hand-set histories** (I90; round 1's P-S2-3), on which C7 (V2.5, D12.1, Sel with H = ∅) rests: four "
            "histories set by hand (constructed, selected on {(1,b0)}, nothing tried, declared). Vary them: provenance "
            "computed from a chain (the program's prov_fixed_points, as FC30.new1 (d)); a history with pairs tried "
            "that no candidate survives; the student's copy with its source's provenance inherited (D12.3, D12.4).",
        ],
        'defs': "upstream of the explanation definition, in your section: **D6.9** "
                "(Relabeling; upstream of (E), Expl, (Suff), (Nec)), **D11.2** (Content; upstream of Dec), **D6.8** "
                "(the four conditions; upstream of Expl, (Suff), (Nec)), **D5.7** (Faithful and question fidelity; read by "
                "Dec's statement). Then the other untouched middle definitions of your section: D8.new1, D10.3, D12.7, "
                "D12.8; then its untouched middle sentences (round 1's map §6.4, S2 sentence middle).",
        'edges': ['e2.03', 'e2.06c', 'e2.07', 'e2.09', 'e2.11b', 'e2.16c', 'e2.19', 'e2.26', 'e2.33'],
        'extra': "**Round 1's V1.6, as a variant of your section.** Its formula, without the sentence it added: a "
                 "condition on Acc, **D6.7.v: Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous ∧ ¬BadTarget(p) ∧ "
                 "¬BadReq(p)**, with BadTarget and BadReq as D3.6 [S1] defines them from a description Desc the question "
                 "answers to (I76). Trace it; give the Desc you use for each worked case (round 1 left the defects not "
                 "tested for want of one, FC106); its edges e1.45 to e1.47 (constrains L161.s1–s3 and D6.6; changes "
                 "with (Suff), (Nec) and FC106; moves being an explanation) are yours to settle. Also: no claim of the "
                 "suite separates D6.4 from round 1's V2.1 or V2.2 (e2.38, e2.39): propose the claim or case that would. "
                 "e2.09 is the owner's yes or no (S45): note it only. Round 1's V2.8 is section 4's V4.4, computed; its "
                 "part on a FROZEN sentence goes to the later part that varies the frozen items.",
    },
    3: {
        'readings': [
            "**S108-3-I2 and S108-3-I5**, on which C8 (V3.4, D13.3) rests wholly: CT read as a Build subhistory, so a "
            "construction trace counts only where its output's ExplUse holds; and which ℰ's claim the trace uses. With "
            "D12.2 as written (CT reads Prepares) C8 moves nothing. Vary both: CT as written, CT as Build, and the claim "
            "used on the candidate's own question, on the widest contract, and on another question sharing t; say where "
            "C8's flag (S41 Q2) stands.",
            "**The trace's extent and the tag encoding** (and the cut K), on which C9 (V3.5, D13.8) rests: with the trace "
            "at o_t (the program's) nothing moves; with a trace spanning an unrecorded change of contract every such "
            "held output moves (round 1's second checker's run). Vary the extent (at o_t; from o_s to o_t; the whole "
            "subhistory) and the tag encoding against D13.3's tuple.",
            "**S108-3-I4 and S108-3-I3**, on which C10 (V3.6, D15.8) rests: parts(t) as E's components and the stated "
            "construction as the base member's components; the history 'Sel-parts' states all but E's last component. "
            "Vary: parts as ports, as edits; the stated construction as t's own parts; a history stating no "
            "construction left out.",
            "**The hand-set histories** (I90), on which C9 and C10 rest: their counts equal the population meeting (E) by "
            "construction of the history. Propose a history built otherwise (provenance computed from a chain).",
        ],
        'defs': "upstream of the explanation definition, in your section: **D11.3** "
                "(History; upstream of Dec, Expl, (Suff), (Nec)), **D9.1** (Claims) and **D9.2** (Argument; both "
                "upstream of Expl, (Suff), (Nec) through D16.XV's arguments). Then the other untouched middle definitions "
                "of your section: D13.7, D14.1, D15.1, D15.2, D15.5; then its untouched middle sentences (round 1's map "
                "§6.4, S3 sentence middle).",
        'edges': ['e3.30b', 'e3.34b', 'e3.37b'],
        'extra': "e3.37b is the owner's yes or no (S47 with S41 Q6): note it only.",
    },
    4: {
        'readings': [
            "**S108-4-I1**, on which C11 (V4.1, D16.XV: Account ∧ ¬Dec(t) ∧ ¬Slot_C(ℰ)) rests: Slot under 'every', and "
            "(Suff)'s antecedent kept as D16.XV writes it. Its other choices ('some', 'some-exempt', 'some-exempt-set'; "
            "(Suff) co-varied) were computed on the cases; vary the pair together and say where C11's flags (S45; S44 "
            "under the other quantifiers) stand.",
            "**S108-4-I2**, on which C12 (V4.2, the rule Acc ∧ Dec ⇒ ¬Expl deleted) rests: which of (Suff)'s shapes keep "
            "¬Dec(t) ('rule', 'L17', 'both').",
            "**S108-4-I3**, on which C13 (V4.3, Sel ∨ CT read at the holding) rests: (a) at the holding, (b) at a "
            "holding it was transferred from, (c) through inherited provenance, where it moves nothing.",
            "**The hand-set histories** (I90), on which C12 and C13 rest: their counts equal the population meeting (E) "
            "by construction of the history. Propose a history built otherwise (provenance computed from a chain).",
        ],
        'defs': "none of your section is upstream of the explanation definition; the one of your section: **E9** (the two-layer episode). Then its untouched middle sentences "
                "(round 1's map §6.4, S4 sentence middle, 112), above all Part XIV's list of declared inputs and "
                "dependence order (L520, L522, L524, L526) and Part XV's defeat conditions (L534 to L544).",
        'edges': ['e4.22', 'e4.40'],
        'extra': "",
    },
}


def edge_lines(ids, edges):
    out = []
    for i in ids:
        e = edges[i]
        settle = re.sub(r'\bas (R\d+)\b', r"as row \1 of round 1's section %s file" % i[1], e.get('what_would_settle') or '')
        out.append('- ' + EDGE.format(id=i, var=', '.join(e['variants']), frm=', '.join(e['from']), kind=e['kind'],
                                      to=(e.get('to_label') or ', '.join(e['to'])).replace('`', "'"),
                                      settle=settle or 'not stated; propose what would'))
    return out


def share_text(n, edges):
    s = SHARES[n]
    parts = ['1. **The readings round 1\'s candidates of your section rest on, under their other choices:**']
    parts += ['   - ' + r for r in s['readings']]
    parts += ['2. **The untouched middle definitions:** ' + s['defs']]
    parts += ['3. **The edges round 1 left claimed only, of your section** (round 1\'s map §4 gives each one\'s argument):']
    parts += ['   ' + l for l in edge_lines(s['edges'], edges)]
    if s['extra']:
        parts += ['4. ' + s['extra'] if n == 2 else '   ' + s['extra']]
    return '\n'.join(parts)


def sources():
    return B.sources() + ROUND1


def build():
    sec = B.section_of_part()
    for rel, h in SAME.items():
        B.need(B.md5_file(rel) == h, '%s has md5 %s, round 1 gives %s: not the same template' % (rel, B.md5_file(rel), h))
        B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
    B.check_frozen_set()
    fs = json.loads(B.read(B.FROZEN_JSON))
    text = B.read(B.TEXT[0])
    claims = B.claims_now(json.loads(B.read(B.CLAIMS_JSON[0])))
    bad = [c['id'] for c in claims if not B.GUARD_CLAIM.fullmatch(c['id'])]
    B.need(not bad, 'claim ids the sandbox guard cannot run alone: %s' % bad)
    mp = json.loads(B.read(R1 + 'the dependency map.json'))
    edges = {e['id']: e for e in mp['edges']}
    co = {e['id'] for e in mp['edges'] if e['standing'] == 'claimed only'}
    named = [i for n in SHARES for i in SHARES[n]['edges']]
    B.need(set(named) <= co, 'a share names an edge not claimed only: %s' % sorted(set(named) - co))
    left = co - set(named)
    B.need(left == {'e1.45', 'e1.46', 'e1.47', 'e1.48', 'e1.49', 'e1.50', 'e1.51', 'e2.20', 'e2.21'},
           'claimed-only edges no share names, other than the nine ruled on: %s' % sorted(left))
    D = {x['id']: x for x in fs['definitions']}
    for n, s in SHARES.items():
        for d in re.findall(r'\b(D\d+\.(?:\d+|new\d+)|E\d)\b', s['defs']):
            B.need(D[d]['status'] == 'MIDDLE' and sec[D[d]['part']] == n, '%s is not a middle item of section %d' % (d, n))
            B.need(d in mp['gaps']['untouched_middle_definitions'], '%s was touched in round 1' % d)
        for d in re.findall(r'\b(D\d+\.(?:\d+|new\d+)|E\d)\b', s['defs']):
            B.need(d in D, '%s is not in the formal core' % d)
    for dst, rel, h in sources():
        B.need(os.path.isfile(B.path(rel)), '%s is not there' % rel)
        B.need(h is None or B.md5_file(rel) == h, '%s has md5 %s, expected %s' % (rel, B.md5_file(rel), h))
        B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
    B.need(B.committed('records/Semantics - Decisions.md'), 'the decisions record differs from HEAD')
    owner, own = B.owner_words(B.read('records/Semantics - Decisions.md'))
    S, Dl = fs['sentences'], fs['definitions']
    span = B.section_spans(text, sec)
    from collections import Counter
    cc = Counter(c['status_now'] for c in claims)
    claims_counts = '%d hold on every model tried, %d have a counterexample, %d were not tested, of %d' % (
        cc['HOLDS ON ALL MODELS TRIED'], cc['COUNTEREXAMPLE FOUND'], cc['NOT TESTED'], len(claims))
    sandbox = B.SANDBOX.format(claims_counts=claims_counts)
    anchor = '| `BRIEF.md` | this brief |'
    B.need(sandbox.count(anchor) == 1, 'the sandbox table has changed')
    sandbox = sandbox.replace(anchor, ROUND1_ROWS + '\n' + anchor)
    files, rows = OrderedDict(), []
    for n, first, last, title in B.SECTIONS:
        l0, l1 = span[n]
        parts = '%s to %s' % (first, last)
        mdefs = [x['id'] for x in Dl if x['status'] == 'MIDDLE' and sec[x['part']] == n]
        n_ms = sum(1 for x in S if sec[x['part']] == n and x['status'] == 'MIDDLE')
        b = '\n\n'.join([INTRO.format(n=n, title=title, nlines=len(B.lines_of(text)), parts=parts, l0=l0, l1=l1),
                         owner, sandbox, B.EXPLANATION.format(explanation=B.EXPLANATION_NOW),
                         JOB.format(n=n, parts=parts, l0=l0, l1=l1, n_ms=n_ms, n_md=len(mdefs), mdefs=', '.join(mdefs),
                                    share=share_text(n, edges)),
                         B.FORM, REPORT.format(n=n)]) + '\n'
        frame = b
        for pat in FRAME_LABELS:
            frame = re.sub(pat, 'LABEL', frame)
        hits = B.scan(frame)
        B.need(not hits, 'brief %d: the frame holds %s' % (n, hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (n, B.words(b), CAP))
        for k in B.KEEP:
            B.need(B.OWNER_CHECK.get(k, own[k].split('"')[1]) in b, "brief %d lacks the owner's words of S%d" % (n, k))
        rel = 'tests/S108 Part A round 2 - GLM job %d, section %d, %s.md' % (n, n, title)
        files[rel] = b
        rows.append((n, title, 's108r2_glm_section%d' % n, rel, B.words(b), B.md5(b)))
    entries = []
    for dst, rel, _ in sources():
        entries.append({'path': dst, 'src': rel, 'md5': B.md5_file(rel)})
        if not dst.endswith('.py'):
            hit = B.model_for_candidate(B.read(rel))
            B.need(not hit, '%s uses "model" for a candidate: %s (decision S43)' % (rel, hit))
    for e in entries:
        B.need(not re.search(r'(\.env$|key)', e['path'], re.I), 'a sandbox path looks like a key file: %s' % e['path'])
    manifest = {'note': "Part A of decision S52, ROUND 2 (log S108): the files copied into each GLM call's sandbox, each "
                        "checked by md5 at the copy; the brief is added as BRIEF.md. Round 1's material unchanged, round "
                        "1's outputs added under round 1/. Written by tools/s108r2_build.py.",
                'text': {'path': B.TEXT[0], 'md5': B.md5_file(B.TEXT[0])},
                'frozen_set': {'path': B.FROZEN_JSON, 'md5': B.md5_file(B.FROZEN_JSON)},
                'template': {'path': B.TEMPLATE, 'md5': B.md5_file(B.TEMPLATE)},
                'sections': [{'section': n, 'parts': [p for p in B.PARTS if sec[p] == n], 'title': t}
                             for n, _, _, t in B.SECTIONS],
                'decisions_record': {'path': 'records/Semantics - Decisions.md',
                                     'md5': B.md5_file('records/Semantics - Decisions.md')},
                'files': entries}
    files[MANIFEST] = json.dumps(manifest, indent=1, ensure_ascii=False) + '\n'
    jobs = {'round': 'Part A of decision S52, round 2 (log S108)', 'rule': READING_RULE, 'out': OUT, 'max_pass': 3,
            'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'manifest': MANIFEST, 'manifest_md5': B.md5(files[MANIFEST]),
            'sandbox_root': 's108r2_sandboxes', 'home_root': 's108r2_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py',
            'jobs': [{'job': n, 'name': 'section%d' % n, 'tag': tag, 'brief': rel, 'brief_md5': h}
                     for n, title, tag, rel, w, h in rows]}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows, manifest


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s108r2_build.py [--check]')
    files, rows, manifest = build()
    if '--check' in a:
        for rel, text in files.items():
            B.need(os.path.exists(B.path(rel)) and B.read(rel) == text, '%s differs from the build' % rel)
        print('check: all %d files identical to the build' % len(files))
    else:
        for rel, text in files.items():
            print(('wrote   ' if B.write_checked(rel, text) else 'same    ') + rel)
    print('\n| section | title | tag | brief | words (build) | md5 |\n|---|---|---|---|---|---|')
    for n, title, tag, rel, w, h in rows:
        print('| %d | %s | %s | `%s` | %d | %s |' % (n, title, tag, rel, w, h))
    print('\nsandbox: %d files from the manifest + BRIEF.md; manifest md5 %s' % (len(manifest['files']),
                                                                            B.md5(files[MANIFEST])))


if __name__ == '__main__':
    main()
