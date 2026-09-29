#!/usr/bin/env python3
"""s109_build.py: build Part B of decision S52, round 1 (log S109): the free set and the frozen template, the four GLM
briefs, the sandbox manifest and the job list. Written 29 September 2026 by the one Opus 5.5 agent of decision S56 that
does Part B's launch. Part A's round-1 build (tools/s108_build.py) is imported, not changed, as Part A round 2's build
was: the same text, formal core, claims, program, printouts and owner's words; Part B inverts Part A's marks.

  python3 Semantics/tools/s109_build.py            build; refuses to write over a file whose content differs
  python3 Semantics/tools/s109_build.py --check    rebuild in memory and compare with the files; writes nothing

Part B (S52): "The next bit, Freeze everything except the hard to vary bits to see how explanation changes in meaning
and scope." The hard-to-vary items are Part A's frozen set (tools/s108_frozen_set.py; Claude's working reading, not
approved by the owner): 238 items, 169 sentences and 69 definitions and encodings. In Part B they are the FREE set, in
four sections B1 to B4; everything else (Part A's middle, 577 items) is FROZEN.

The four sections follow the explanation definition's own structure, being an explanation = Account(E) and not Dec(t),
with (Suff) and (Nec) the claims about it, in the dependence order the text itself gives (L526): B1 what an account is
of (organizations, kinds, the question and its contract: Parts 0 to III); B2 the account itself (transports, fidelity,
(E)'s conjuncts, routes, the exact constructions and the transport results: Part IV's "Transports", Parts V, VI up to
L313, VII, VIII); B3 the provenance clause (occurrences and contents, layers, the three provenances, representation,
prediction, construction, repair, the physical module: the rest of Part IV, Parts X to XII); B4 what rules candidates
out and what the class claims (rivals, conflict, problems from L315, criticism and arguments, recursion, the class,
what would rule it out, the Arguments: Parts VI from L315, IX, XIII to XVI).

Checks before anything is written: Part A's frozen set, template and reading copy committed and at the md5s Part A's
rounds give; the frozen set rebuilt identical; Part A's end state (the map and the list after the cross-examination,
the settled file, what the variations found) committed and at pinned md5s; every source committed and unchanged from
HEAD; the owner's words against the record; the frame of each brief free of the words S23 scrubs and of "model" for a
candidate (S43); each brief at most CAP words; every claim id runnable by the guard; every carry-over's free item in the
free set and in the section it is given to; the four sections cover the 238 free items exactly once.
"""
import json, os, re, sys
from collections import Counter, OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (Part A round 1's build: read, never written)

SEM = B.SEM
PA = 'results/S108 Part A - '
PA2 = 'results/S108 Part A round 2 - '
FREE_MD = 'results/S109 Part B - the free set and the frozen template.md'
FREE_JSON = 'results/S109 Part B - the free set and the frozen template.json'
READING_RULE = 'results/S109 Part B round 1 - how the replies will be read, written before sending.md'
OUT = 'results/S109 Part B round 1 - returns'
JOBS_FILE = 'tools/s109_jobs - Part B round 1, GLM.json'
MAT = 'results/S109 Part B round 1 - material for the readers'
MANIFEST = MAT + '/sandbox manifest.json'
CAP = 7000
# Part A's material, reused byte for byte (Part A round 2's build pins the same md5s)
SAME = {B.TEMPLATE: '0c5ad2622fd2df95d073951d998418f3', B.BYLINE: '43142c41665438a30a3936458dd22d44',
        B.FROZEN_MD: '367c4b1f6022d5da37e1f153f2b8c05e', B.FROZEN_JSON: '30ca39e3203648a350dc97987c697765'}
MAP_JSON = PA2 + 'the dependency map, after the cross-examination.json'
# Part A's end state, as the settlement left it (0f71693 and after), as background
PART_A = [
    ('part A/the dependency map, after the cross-examination.md', PA2 + 'the dependency map, after the cross-examination.md'),
    ('part A/candidate definitions of explanation, after the cross-examination.md',
     PA2 + 'candidate definitions of explanation, after the cross-examination.md'),
    ('part A/the cross-examination of round 2, settled.md', PA2 + 'the GLM cross-examination, settled.md'),
    ('part A/what round 2 found.md', PA2 + 'what the variations found.md'),
    ('part A/what round 1 found.md', 'results/S108 Part A round 1 - what the variations found.md'),
]
PARTS_OF = {'(E)': 'X:(E)', 'Dec': 'X:Dec', 'Expl': 'X:Expl', '(Suff)': 'X:(Suff)', '(Nec)': 'X:(Nec)'}
TAG = {'(E)': 'E', 'Dec': 'Dec', 'Expl': 'Expl', '(Suff)': 'Suff', '(Nec)': 'Nec'}
SECTIONS = [
    (1, 'organizations, kinds, questions and contracts', 'Part 0 to Part III',
     'what an account is of: the target organization, its components and admitted edits, roles and kinds, and the '
     'question with its contract, query and stated scope; (E) reads all of it'),
    (2, 'transports, fidelity, the account, routes and the exact constructions', "Part IV's Transports, Part V, "
     'Part VI to L313, Part VII, Part VIII',
     "the account itself: the transport, (E)'s conjuncts (F1), (F2), (A), Dependence and NonVacuous, what (E) excludes, "
     'work and routes over the commitments, the exact constructions that exercise it, and the transport results'),
    (3, 'provenance, histories, representation, construction, repair and the physical module',
     "the rest of Part IV, Parts X to XII",
     'the provenance clause: occurrences and contents, the two layers, selected, constructed and declared, '
     'representation, prediction and violation, construction and origin, repair and created explanation, the physical '
     'module; Dec reads these'),
    (4, 'rivals, problems, criticism, the class, what would rule it out, and the Arguments',
     'Part VI from L315, Part IX, Parts XIII to XVI',
     'what rules candidates out and what the class claims: rivals, conflict with a claim, problems, criticism and '
     'arguments, recursion, the class collected, the defeat conditions and the Arguments; (Suff) and (Nec) read these'),
]
# Part A's items that belong to Part B: (a) ruled to Part B by Part A's records; (b) flagged by Part A round 2's
# tabulation as changing a FROZEN item in effect or as written, and not implemented. Formulas as the tabulations give them.
CARRY = [
    {'id': 'V1.7', 'class': 'a', 'free': ['D3.5'], 'from': "Part A round 1, section 1 (D0.2)",
     'where': "ruled to Part B by the orchestrator's decision 3 on round 1's critical review; edges e1.48 to e1.51, "
              "claimed only",
     'old': "Excl(Σ) a primitive (I27); D3.5: Σ is a declared input naming Excl(Σ) ⊆ A×B; Stated(C,Σ) :⟺ (A×B)∖C ⊆ Excl(Σ)",
     'new': "Excl(Σ) := (A×B) ∖ C, defined; so Stated(C,Σ) always holds (D0.2's primitive changes with it)",
     'note': "the silent narrowing L43.s4 says is caught would no longer be caught; on every question the program "
             "builds I85's default scope already equals the formula, so only a question stating a smaller exclusion "
             "moves (Acc F → T there); blocks D3.5, L43.s4, L159.s1; constrains D6.6 (NonVacuous's second conjunct "
             "becomes vacuous); moves NonVacuous"},
    {'id': "V2.8, its part on L315.s7", 'class': 'a', 'free': ['L315.s7'], 'from': 'Part A round 1, section 2 (D9.8)',
     'where': "its part on L315.s7 ruled to Part B by the orchestrator's decision 3; its D16.XV part is round 1's V4.4, "
              "computed; edges e2.20, e2.21, claimed only",
     'old': "L315.s7: a candidate is not ruled out for j when no argument usable by j rules it out; X_j(φ) := {α : "
            "Usable_j(α) ∧ RO(α,φ)}; ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅",
     'new': "ℰ ruled out for j :⟺ ∃α ∈ X_j('Acc(ℰ)') with Acc(ℰ) ∈ Uses(α) (the instance reading, I196)",
     'note': "changes which arguments rule a candidate out; (Suff)'s defeat set grows by arguments reaching ℰ only "
             "through another candidate's Acc"},
    {'id': 'R2V2.7', 'class': 'a', 'free': ['L189.s2'], 'from': 'Part A round 2, section 2 (D5.7)',
     'where': "D5.7's one variant; it rewrites L189.s2, so Part A's settlement gave it to Part B; edge r2e2.14, "
              "claimed only",
     'old': "L189.s2: a transport is faithful on C when it meets the component and global fidelity conditions of "
            "Part V; D5.7: Faithful_C(t) := F1_C ∧ F2_C; QFid_C := A_C; Viol narrow (D12.7)",
     'new': "Faithful_C(t) := F1_C ∧ F2_C ∧ A_C (question fidelity inside 'faithful'); Viol := Viol⁺",
     'note': "a selected transport wrong in its answers on its own H is no longer Sel, so Dec (FC104.new1 (a)); Rep "
             "harder, so Sel easier where earlier representations exist; (Nec) reads Faithful"},
    {'id': 'R2V1.2', 'class': 'b', 'free': ['L155.s6'], 'from': 'Part A round 2, section 1 (D3.4)',
     'where': 'flagged by the round-2 tabulation (possible, in effect: L155.s6); not implemented',
     'old': "D3.4: constructed :⟺ C results from an episode with a construction trace; Found(p) requires ρ_p = "
            "constructed", 'new': "constructed :⟺ ∃h′ [Rec_h′(C→C′) = constructed ∧ Prepares(h′, C′ as a content)]; "
                                  "Found(p′) :⟺ ρ_p′ = constructed", 'note': 'settles e1.37 in the reply\'s reading'},
    {'id': 'R2V1.4', 'class': 'b', 'free': ['L155.s6'], 'from': 'Part A round 2, section 1 (L15.s2 through D3.4)',
     'where': 'flagged by the round-2 tabulation (in effect: L155.s6); not implemented; edge r2e1.30, claimed only',
     'old': 'Found(p) requires ρ_p = constructed (D3.4; L155.s6)', 'new': 'Found(p) :⟺ ρ_p ∈ {selected, constructed}',
     'note': 'a question found by selection counts as found'},
    {'id': 'R2V1.7', 'class': 'b', 'free': ['D4.2'], 'from': 'Part A round 2, section 1 (L119.s1)',
     'where': 'flagged by the round-2 tabulation (in effect: D4.2); not implemented; edge r2e1.34, claimed only',
     'old': "D4.2: j ~_C j′ :⟺ a bijection β: V_j → V_j′ with X_v = X_β(v) and L_j′(a,b) = β_*(L_j(a,b)) ∀(a,b) ∈ C (I10)",
     'new': "j ~_C j′ :⟺ V_j = V_j′ ∧ sig_C(j) = sig_C(j′) (footprints as ordered tuples; β dropped)",
     'note': 'kinds read through the ports themselves, not up to a relabeling'},
    {'id': 'R2V1.8', 'class': 'b', 'free': ['D3.2'], 'from': 'Part A round 2, section 1 (L141.n3)',
     'where': 'flagged by the round-2 tabulation (possible, in effect: D3.2; E4); not implemented; edge r2e1.37',
     'old': 'Q(O,a,b;δ_O) ∈ Y_p ∪ {⊥}, Y_p free (D3.2)', 'new': 'Y_p := X_δD (⊥ as D3.2)',
     'note': 'the query answers with values of the designated port only; E4 [B2] would carry no question'},
    {'id': 'R2V1.9', 'class': 'b', 'free': ['D3.1'], 'from': 'Part A round 2, section 1 (L159.s3)',
     'where': 'flagged by the round-2 tabulation (as written: D3.1); not implemented; edge r2e1.40',
     'old': 'D3.1: C ⊆ A×B, (1,b0) ∈ C; L159.s3: admitting a change is not a claim that it can be carried out',
     'new': 'Question(p) ⇒ ∀(a,b) ∈ C: Θ_admits(a); a C holding an unadmitted pair names no question',
     'note': 'departs from S25 to S27 (the reply names them): physical possibility would enter what a question is'},
    {'id': 'R2V2.4', 'class': 'b', 'free': ['D12.4'], 'from': 'Part A round 2, section 2 (D12.3)',
     'where': 'flagged by the round-2 tabulation (possible, in effect: D12.4); not implemented',
     'old': 'D12.4: a holding reached by content-preserving transfers inherits prov part by part (parts = each '
            'component with its counterpart binding; a binding newly built gets Con)',
     'new': 'a holding reached by a copy of the carrier\'s whole content inherits prov(t,o) whole: parts := {t}',
     'note': 'the student\'s copy would inherit its source\'s provenance and count as an explanation: departs from '
             'S41 Q2 (the reply names it)'},
]
FRAME_LABELS = [r'S108-[1-4]-I\d+', r'S108r2-[1-4]-I\d+']


def heading_of_lines(text):
    """For each line, the nearest '## ' heading inside its Part, or the Part's own heading."""
    out, cur = {}, None
    for n, l in enumerate(B.lines_of(text), 1):
        if l.startswith('# Part'):
            cur = l[2:].strip()
        elif l.startswith('## '):
            cur = l[3:].strip()
        out[n] = cur
    return out


def section_of_free(x, head):
    p = x['part']
    line = x['line'] if x['kind'] == 'sentence' else (x['lines'][0] if x.get('lines') else None)
    if p in ('Front matter', 'Part 0', 'Part I', 'Part II', 'Part III'):
        return 1
    if p == 'Part IV':
        return 2 if line is not None and head.get(line) == 'Transports' else 3
    if p in ('Part V', 'Part VII', 'Part VIII'):
        return 2
    if p == 'Part VI':
        return 2 if line is not None and line < 315 else 4
    if p in ('Part X', 'Part XI', 'Part XII'):
        return 3
    if p in ('Part IX', 'Part XIII', 'Part XIV', 'Part XV', 'Part XVI'):
        return 4
    raise SystemExit('refused: no section for %s (%s)' % (x['id'], p))


def bearing_sets(mp):
    """Every definition each part of the explanation definition rests on, from Part A's map: the part's defining
    definitions, what it reads, and the ancestors in the program's dependency graph (D18.1), through the X: nodes."""
    nodes = {n['id']: n for n in mp['nodes'] if n['id'].startswith('X:')}
    out = {}
    for name, xid in PARTS_OF.items():
        seen, todo, defs = set(), [xid], set()
        while todo:
            k = todo.pop()
            if k in seen:
                continue
            seen.add(k)
            n = nodes[k]
            defs |= set(n.get('defined_by') or []) | set(n.get('d18_ancestor_definitions') or [])
            for r in n.get('reads') or []:
                (todo.append(r) if r.startswith('X:') else defs.add(r))
        out[name] = defs
    return out


def free_set(fs, text, mp):
    head = heading_of_lines(text)
    bear = bearing_sets(mp)
    mnodes = {n['id']: n for n in mp['nodes']}
    S, D = fs['sentences'], fs['definitions']
    sc_ids = {x['id'] for x in S if x.get('s100_list')}
    sc_defs = set()
    for x in S:
        if x.get('s100_list'):
            sc_defs |= set(x.get('defs') or [])
    items = []
    for x in S + D:
        if x['status'] != 'FROZEN':
            continue
        kind = 'sentence' if x in S else 'definition'
        n = section_of_free(dict(x, kind=kind), head)
        if kind == 'definition':
            on = [p for p in PARTS_OF if x['id'] in bear[p]]
            via = []
        else:
            on, via = [], []
            for p in PARTS_OF:
                hit = [d for d in (x.get('defs') or []) if d in bear[p]]
                if hit:
                    on.append(p)
                    via += [d for d in hit if d not in via]
        m = mnodes.get(x['id'], {})
        edges = [{'edge': e['edge'], 'kind': e['kind'], 'standing': e['standing'], 'variants': e.get('variants', [])}
                 for e in m.get('edges_in') or []]
        items.append(OrderedDict([
            ('id', x['id']), ('kind', kind), ('part', x['part']),
            ('line', x.get('line')) if kind == 'sentence' else ('lines', x.get('lines')),
            ('section', n), ('bears_on', on), ('through', via),
            ('strong_candidate', x['id'] in sc_ids), ('formalizes_a_strong_candidate', x['id'] in sc_defs),
            ('text', x['text'] if kind == 'sentence' else None),
            ('formalized_by', x.get('defs') or []) if kind == 'sentence' else ('formalizes', x.get('units') or []),
            ('why_hard_to_vary', x['reason']), ('part_A_edges_in', edges)]))
    by = {i['id']: i for i in items}
    for c in CARRY:
        for f in c['free']:
            B.need(f in by, 'carry-over %s: %s is not in the free set' % (c['id'], f))
        c['section'] = by[c['free'][0]]['section']
    # Part A variants a free item blocked (blocks edges ending at a free item)
    blocked = []
    for e in mp['edges']:
        if e['kind'] != 'blocks':
            continue
        hit = [t for t in e.get('to') or [] if t in by]
        if hit:
            blocked.append({'edge': e['id'], 'variants': e['variants'], 'free_items': hit, 'standing': e['standing'],
                            'sections': sorted({by[t]['section'] for t in hit})})
    return items, bear, blocked


def tag_of(i):
    t = [TAG[p] for p in i['bears_on']]
    if i['strong_candidate']:
        t.append('SC')
    elif i['formalizes_a_strong_candidate']:
        t.append('SCdef')
    return ' '.join(t)


def mark(i):
    if i is None:
        return 'FROZEN'
    t = tag_of(i)
    return 'B%d' % i['section'] + (' ⟨%s⟩' % t if t else '')


def ids(xs):
    return ', '.join(xs) or 'none'


def template_md(fs, text, core_text, claims, items, bear, blocked):
    by = {i['id']: i for i in items}
    S, D = fs['sentences'], fs['definitions']
    L = ['# S109 Part B: the free set and the frozen template', '',
         "*The same template for the four agents of Part B round 1 (decision S52: \"Freeze everything except the hard to "
         "vary bits to see how explanation changes in meaning and scope.\"). Built by `tools/s109_build.py` from the text, "
         "the formal core and the claims after the fourth review round, from Part A's frozen set (`tools/s108_frozen_set.py`) "
         "and from Part A's dependency map after its cross-examination. Part A's frozen set is the drafters' working "
         "reading of \"the parts that are hard to vary\"; the owner has not been asked to approve it. Nothing here changes "
         "the text or the maths: Part B varies copies. \"Model\" here means only a small structure the program builds, "
         "never a candidate (S43).*", '',
         '## 1. How to read it', '',
         '- Part B is Part A inverted. Every sentence of the text and every definition and encoding of the formal core '
         'carries one mark:',
         "  - **B1**, **B2**, **B3**, **B4**: the **free set**, Part A's frozen set (the parts that are hard to vary, in "
         "the working reading: put to the readers or checkers at least once, and changed by no round or step), in four "
         "sections. Each agent varies its own section only.",
         "  - **FROZEN**: everything else, which is Part A's middle. It stays exactly as it is in every variant.",
         '- After a free mark, ⟨…⟩ says what the item bears on, from Part A\'s map (section 3): **E** (E), Account; '
         '**Dec** the provenance clause; **Expl** being an explanation, Account ∧ ¬Dec(t) (D16.XV); **Suff** and **Nec** '
         'the claims (Suff) (L536, L17) and (Nec) (L538); **SC** a strong candidate (a sentence the review rounds tried '
         'to vary and left unchanged, on the list of S100, S101); **SCdef** a definition that formalizes a strong candidate.',
         '- A definition bears on a part when it is among the definitions the part is defined by, reads, or has upstream '
         "in the program's dependency graph (D18.1), through the parts' nodes in Part A's map. A sentence bears on a part "
         'through the definitions that formalize it; which ones is listed in section 3 (and in the `.json`).',
         '- A free sentence formalized by a FROZEN definition: a variant of the sentence may carry the matching change of '
         'that definition, marked "changes with (its formalization)"; no other FROZEN item changes. A FROZEN item that '
         'cannot stand beside a variant is an edge (blocks), recorded; the variant is still computed. A variant that '
         'changes a FROZEN item beyond the formalization of the free words it varies is out of Part B.',
         '- Ids as in Part A: `L<line>.s<k>` (a sentence unchanged since the oldest text the record follows) or '
         '`L<line>.n<k>` (newer words); definitions `D§.n`, encodings `En`, as in the formal core.', '']
    cnt = Counter((i['section'], i['kind']) for i in items)
    L += ['## 2. The four sections of the free set, and why this split', '',
          '| section | what it holds | stretch of the text | free sentences | free definitions | all | bear on (E) | on Dec | '
          'on Expl, (Suff) or (Nec) | strong candidates |', '|---|---|---|---|---|---|---|---|---|---|']
    for n, title, stretch, what in SECTIONS:
        its = [i for i in items if i['section'] == n]
        L.append('| B%d, %s | %s | %s | %d | %d | %d | %d | %d | %d | %d |' % (
            n, title, what, stretch, cnt[(n, 'sentence')], cnt[(n, 'definition')], len(its),
            sum(1 for i in its if '(E)' in i['bears_on']), sum(1 for i in its if 'Dec' in i['bears_on']),
            sum(1 for i in its if set(i['bears_on']) & {'Expl', '(Suff)', '(Nec)'}),
            sum(1 for i in its if i['strong_candidate'])))
    L += ['', "**Why this split.** Part A's sections were stretches of Parts balanced by middle items; cut the same way, "
          "the free set would fall 57 / 95 / 49 / 37. Part B splits it by the explanation definition's own structure: "
          "being an explanation is Account(ℰ) ∧ ¬Dec(t), with (Suff) and (Nec) the claims about it, and the text gives "
          "the order in which its parts depend on each other (L526: (K) on (O) and a contract; (F1), (F2), (A) on (O), "
          "(Q), (K); representation on fidelity and provenance; …). So B1 holds what an account is of (the target and "
          "the question), B2 the account itself, B3 the provenance clause Dec reads, and B4 what rules candidates out "
          "and what the class claims, which (Suff) and (Nec) read. Two Parts are cut at their own seams: Part IV at its "
          "heading \"Transports\" (the transport goes with the account; occurrences, layers, provenances, representation "
          "and prediction with provenance), and Part VI at L315, where work and routes (L287 to L313) end and rivals, "
          "conflict and problems begin. A definition goes where the first line it formalizes lies; one that quotes no "
          "line goes by its Part. The weights come out 57 / 57 / 57 / 67.", '',
          "**What the explanation definition rests on, among the free items** (Part A's map after its cross-examination, "
          "`part A/the dependency map, after the cross-examination.md`, its §1 and nodes `X:`). In Part B the "
          "definitions that compose the parts are FROZEN, since they were Part A's middle: (E)'s D6.7, Dec's D12.3, "
          "D16.XV, and Dependence's D6.4, D6.5. What is free is much of what they are built from:", '']
    for p in PARTS_OF:
        fr = [i['id'] for i in items if i['kind'] == 'definition' and p in i['bears_on']]
        L.append('- **%s** rests on %d free definitions: %s.' % (p, len(fr), ids(fr)))
    L += ['', '## 3. The free set, by section', '',
          'Per section: the free items (id, kind, what each bears on, and, for a sentence, the definitions it bears '
          'through); the carry-overs from Part A; the Part A variants a free item of the section blocked. Why each item '
          "is hard to vary: `template/why each free item is hard to vary.md` (Part A's frozen set). Part A's edges into "
          "each free item are in the `.json` (`part_A_edges_in`).", '']
    for n, title, stretch, what in SECTIONS:
        its = [i for i in items if i['section'] == n]
        L += ['### 3.%d Section B%d: %s (%s)' % (n, n, title, stretch), '',
              '| id | kind | bears on | through | strong candidate |', '|---|---|---|---|---|']
        for i in its:
            L.append('| `%s` | %s | %s | %s | %s |' % (
                i['id'], i['kind'], ', '.join(i['bears_on']) or '–', ', '.join(i['through']) or '–',
                'yes' if i['strong_candidate'] else ('formalizes one' if i['formalizes_a_strong_candidate'] else '–')))
        cs = [c for c in CARRY if c['section'] == n]
        L += ['', '**Carry-overs from Part A** (class a: ruled to Part B by Part A\'s records; class b: flagged by Part A '
              'round 2\'s tabulation as changing a FROZEN item, and not implemented; a class-b item may be taken up as a '
              'variant of the free item it rewrites):', '']
        if not cs:
            L.append('- none')
        for c in cs:
            L.append('- **%s** (class %s; %s) on %s. %s. Old: %s. New: %s. %s.' % (
                c['id'], c['class'], c['from'], ', '.join('`%s`' % f for f in c['free']), c['where'][0].upper() +
                c['where'][1:], c['old'], c['new'], c['note'][0].upper() + c['note'][1:]))
        bl = [b for b in blocked if n in b['sections']]
        L += ['', "**Part A variants a free item of this section blocked** (a blocks edge of Part A's map ending at it; "
              'a variant of the free item would lift the block):', '']
        if not bl:
            L.append('- none')
        for b in bl:
            L.append('- %s: %s blocks %s (%s)' % (b['edge'], ', '.join(b['variants']), ', '.join(
                '`%s`' % t for t in b['free_items']), b['standing']))
        L.append('')
    # the text, sentence by sentence
    tl = B.lines_of(text)
    by_line = {}
    for x in S:
        by_line.setdefault(x['line'], []).append(x)
    L += ['## 4. The text, sentence by sentence', '',
          'Each line: `id | mark | the sentence`, in the order of the text; headings as they stand. A sentence longer '
          'than 1,500 characters is cut at a space, the later pieces marked `(cont.)`.', '']
    for k, l in enumerate(tl, 1):
        if l.startswith('#'):
            L += ['', l, '']
            continue
        for x in by_line.get(k, []):
            pieces = B.split_long(x['text'].replace('\n', ' '))
            L.append('`%s` | %s | %s' % (x['id'], mark(by.get(x['id'])), pieces[0]))
            L += ['`%s` (cont.) | %s' % (x['id'], pc) for pc in pieces[1:]]
    L += ['', '## 5. The formal core, definition by definition', '',
          'The formal core after the fourth review round, from its section 0 on, with a mark line `⟦B<n> ⟨…⟩⟧` or '
          '`⟦FROZEN⟧` before each definition and encoding. Quotations of the text (`> Lnnn | …`) are as the core has '
          'them, of the text as the maths round read it; where a line changed since, section 4 above has its words now. '
          'Lines longer than 1,500 characters are cut at a space, the later pieces marked `(cont.)`.', '']
    dids = {x['id'] for x in D}
    started = False
    for l in B.lines_of(core_text):
        if l.startswith('## §0'):
            started = True
        if not started:
            continue
        m = re.match(r'^\*\*((?:D\d+\.(?:\d+|new\d+|XV))|(?:E\d+))\b', l)
        if m:
            B.need(m.group(1) in dids, '%s has no entry in the frozen set' % m.group(1))
            L += ['⟦%s⟧ %s' % (mark(by.get(m.group(1))), m.group(1))]
        pieces = B.split_long(l)
        L.append(pieces[0])
        L += ['(cont.) ' + pc for pc in pieces[1:]]
    L += ['', '## 6. The claims, by section', '',
          'Each claim with the lines its statement cites, and the free sections of the free sentences among them. A '
          "claim is a consequence the program tests; a variant that changes a definition may change a claim's result.", '',
          '| claim | title | lines | free sentences cited, by section | result now |', '|---|---|---|---|---|']
    for c in claims:
        lines = sorted({s['line'] for s in c.get('source') or []})
        fr = sorted({'B%d' % by[x['id']]['section'] for x in S if x['line'] in lines and x['id'] in by})
        L.append('| %s | %s | %s | %s | %s |' % (c['id'], c['title'].replace('|', '\\|')[:110],
                                                ', '.join('L%d' % k for k in lines), ', '.join(fr) or '—',
                                                c.get('status_now') or ''))
    return '\n'.join(L) + '\n'


# ------------------------------------------------------------------ the briefs
INTRO = """# Part B of an experiment on a semantics, round 1: section B{n} of 4, {title}

## 1. What this is

A theory, called here the semantics, is stated in a prose text ({nlines} lines, cited as L1 to L{nlines}) and in a formal core: definitions (D§.n, each with the sentences it formalizes quoted above it), encodings of the text's worked cases (E1 to E9), and formal claims (FCnn) that a program in `model/` tests on small structures. In this brief a "model" is only such a small structure, or the program's folder; what the theory judges is always called a candidate or an explanation.

The owner of the theory asked for an experiment in parts (S52, section 2). Part A froze the parts that are hard to vary and varied the middle, to map dependencies; it has ended, and its map and its list of candidate definitions of explanation are in `part A/` (section 3). **This is Part B, its inverse: the middle and everything else is now frozen, and the parts that are hard to vary are the free set; they are what is varied, to see how explanation changes in meaning and scope.** Four agents work at the same time on the same template, each on its own section of the free set. You are the agent for **section B{n}: {title}** ({stretch}).

Nothing you propose changes the theory. Part B is an experiment on copies: your variants are read, then implemented and computed by another agent in copies of the program; what comes out is a record of how the meaning and the scope of explanation move with each variant, and a list of candidate definitions of explanation.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths. Who made a point decides nothing, only its reasons do."""

TEMPLATE_ROWS_OLD = """| `template/the frozen template.md` | **the frozen template**, the same for the four agents: every sentence of the text, one per line, and every definition and encoding of the formal core, each marked FROZEN or S1 to S4 (its section); the four sections; the claims by section. Start here |
| `template/the frozen set.md` | why each item is frozen or in the middle, item by item, with the criterion as applied |"""
TEMPLATE_ROWS_NEW = """| `template/the free set and the frozen template.md` | **the template**, the same for the four agents. Start here: its §1 says how to read it; §2 the four sections of the free set, why the split, and the free definitions each part of the explanation definition rests on; §3 the free items of each section, what each bears on, the carry-overs from Part A and the Part A variants a free item blocked; §4 the text, one sentence per line, and §5 the formal core, every item marked FROZEN or B1 to B4 (its section), with ⟨E Dec Expl Suff Nec SC⟩ for what it bears on; §6 the claims |
| `template/why each free item is hard to vary.md` | Part A's frozen set: the criterion, and why each free item was judged hard to vary, item by item |"""
PART_A_ROWS = """| `part A/the dependency map, after the cross-examination.md` | Part A's map: the parts of the explanation definition (§1), how it moved with each of Part A's variants (§2), the edges and their standing, the gaps, and the items it left to Part B |
| `part A/candidate definitions of explanation, after the cross-examination.md` | Part A's list, C1 to C21: what each admits and drops (computed), the reading it rests on, and the owner's decisions each does not appear to agree with |
| `part A/what round 1 found.md`, `part A/what round 2 found.md`, `part A/the cross-examination of round 2, settled.md` | Part A's two rounds in short, and the objections to round 2 as settled |"""

MEANING_SCOPE = """## 5. What "meaning" and "scope" are here

Both are measured against section 4, before and after the variant.

- **Meaning** is what the definition of explanation says: which conditions, on what (the question, its contract, the transport, the commitments, the designation, the stated scope, the history), with what provenance clause. A variant's effect on meaning is stated as the changed formal statement of the part that moves, beside the old one: (E) and its conjuncts, Dec, being an explanation (Account ∧ ¬Dec(t)), (Suff), (Nec). A variant can change meaning while no case computed moves; say so.
- **Scope** is which things count as explanations: which candidates enter and which leave, as meeting (E) and as explanations. Read on (1) the text's worked cases (the table of observed answers, the reversed calculation, "p because p", the pole and its shadow, the swap, the skew-symmetric matrices, the constitutive rules, the two-layer episode); (2) **the owner's own cases**: the two-part sign (FC23.new2), the weathervane (FC22, the program's vane), the bridge (FC84.new1) and the student's copy of the formula (FC30.new1 (d)); (3) made-up candidates: the external examples, the creative transport case, and the generated worlds at scale 4 (say which kind of small case you expect to enter or leave, with one written out); and (4) which claims' results move.
- Where an owner's case turns on a reading the owner has not settled (the change as an edit or as a boundary; D6.3's quantifier; whether a question's history is recorded; which history the bridge has), give the result "on that reading" only, with the reading."""

JOB = """## 6. Your job, for section B{n}

Your section: **{title}** ({stretch}): {n_s} free sentences and {n_d} free definitions and encodings, marked **B{n}** in the template (its §3.{n} lists them). Every item marked FROZEN, and every free item of the other three sections, stays exactly as it is.

Of your section's free items, these bear on the explanation definition (Part A's map; the template's §2 and §3.{n}):
- **(E)**: {b_e}
- **Dec**, not (E): {b_dec}
- **being an explanation, (Suff) or (Nec) only**: {b_rest}
- **strong candidates** (sentences the review rounds tried to vary and left unchanged): {sc}

{carry}

{blocked}

**(i) Vary** your section's free items only: first your carry-overs, as variants of the free item each rewrites; then the items that bear on (E) or Dec; then the strong candidates; then the rest as they bear on explanation. About six to ten variants, each small and exact. A variant may **replace** an item, **weaken** it, **strengthen** it, **drop** it, or **re-order a dependence** (make a part read an item it did not read, or stop reading one it did). Give each: (1) the changed formal statement beside the old one, in the formal core's notation, with the id it changes (new ids `D§.n.b<k>`, `En.b<k>`, `L<line>.s<k>.b<k>`); (2) the changed sentence: the free sentence as the variant would have it, old beside new (for a definition, the free sentence that formalizes it, or "none"). Where a free sentence is formalized by a FROZEN definition, the variant may state the matching change of that definition, marked "changes with (its formalization)"; no other FROZEN item changes.

**(ii) Predict what each variant does to explanation** (section 5): its **meaning**, as the changed formal statement of the part that moves, old beside new; its **scope**, the candidates expected to enter and to leave, the owner's four cases each named (enters, leaves, stays, or "on that reading"), the made-up candidates, and the claims expected to move; name the case you expect to move first. Run the existing claims to read the result before the variant; mark every result after it "not run". Small cases in the program's format: a question p (target, contract, query), a candidate ℰ (organization, transport, commitments, designation), the result before and after.

**(iii) Map the edges** for each variant: **blocks** (a FROZEN item the variant cannot stand beside: which, and why in one line); **constrains** (a FROZEN item that limits how it can be written); **changes with** (a FROZEN definition that formalizes the varied words, or an item of another section: id, section, what would change); **moves** (a part of the explanation definition: a conjunct of (E), what a conjunct reads, Dec, Expl, (Suff) or (Nec), and how). An edge you cannot settle, say so, with what would settle it.

**(iv) Keep to the form** (sections 7 and 8)."""

REPORT = """## 8. The report

Terse: tables, formulas, small cases in the program's format, one-line reasons. No summary of the material. At most about 3,500 words.

Sections, in this order:
(a) **the variants**, one table: id (PB{n}.1, PB{n}.2, ...), free item(s) varied [id], kind (replace, weaken, strengthen, drop, re-order a dependence), the carry-over it takes up (or "–"), old → new formal statement, old → new sentence, the owner's decisions it departs from (or "none");
(b) **meaning**, one block per variant: the part(s) of the explanation definition that move, old and new formal statement side by side; or "no part moves", with why;
(c) **scope**, one block per variant: the candidates expected to enter and to leave; the owner's four cases, each named with enters, leaves, stays or "on that reading" (and the reading); the made-up candidates; the claims expected to move; the small cases, before and after, each marked run (with the command and the program's result line) or "not run";
(d) **the edges**, one table for all variants: variant, kind (blocks, constrains, changes with, moves), item (id and mark, or the part of the explanation definition), why in one line, settled or not;
(e) **the free items of your section that bear on explanation and that you did not vary**, one line each on why not;
(f) **inventions** your variants rest on, with the other choices.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""


def form_b():
    f = B.FORM.replace('## 6. The form of every variant', '## 7. The form of every variant')
    old = 'with the id it changes (new ids as `D§.n.v<k>` or `FCnn.v<k>`);'
    B.need(f.count(old) == 1, "Part A's form changed")
    f = f.replace(old, 'with the id it changes (new ids as in section 6 (i), or `FCnn.b<k>`);')
    old = 'Never new prose: a variant of a sentence is its formal statement, not a rewording.'
    B.need(f.count(old) == 1, "Part A's form changed")
    f = f.replace(old, 'Nothing is added to the text. The changed sentence you give beside a variant records which words '
                       'of the free sentence the formal change alters, as few as the change needs, beside the old words; '
                       'it is not new text for the theory, and every word section 2 forbids (S23) stays out of it.')
    old = 'When a variant does, say so plainly, in its row, and name the decision'
    B.need(f.count(old) == 1, "Part A's form changed")
    f = f.replace(old, 'Such a variant is computed like any other; the decision it departs from is kept for the owner, '
                       'who answers yes or no later. When a variant does, say so plainly, in its row, and name the decision')
    return f


def carry_text(n):
    cs = [c for c in CARRY if c['section'] == n]
    if not cs:
        return '**Carry-overs from Part A**: none in your section.'
    out = ['**Carry-overs from Part A** (the template\'s §3.%d gives each with its edges): class a, ruled to Part B by '
           'Part A\'s records; class b, varied in Part A in a way that changed a free item, and so not computed there:' % n]
    for c in cs:
        out.append('- **%s** (class %s) on %s: old %s; new %s.' % (c['id'], c['class'], ', '.join(
            '`%s`' % f for f in c['free']), c['old'], c['new']))
    return '\n'.join(out)


def blocked_text(n, blocked):
    bl = [b for b in blocked if n in b['sections']]
    if not bl:
        return '**Part A variants a free item of your section blocked**: none.'
    return ('**Part A variants a free item of your section blocked** (a variant of that item would lift the block; '
            'Part A\'s map §4 gives each edge): ' + '; '.join(
                '%s by %s' % (', '.join(b['free_items']), ', '.join(b['variants'])) for b in bl) + '.')


def sources(free_md_body):
    s = []
    for dst, rel, h in B.sources():
        if rel == B.TEMPLATE:
            continue
        if rel == B.FROZEN_MD:
            s.append(('template/why each free item is hard to vary.md', rel, h))
            continue
        s.append((dst, rel, h))
    s.insert(0, ('template/the free set and the frozen template.md', FREE_MD, None))
    s += [(dst, rel, None) for dst, rel in PART_A]
    return s


def build():
    for rel, h in SAME.items():
        B.need(B.md5_file(rel) == h, '%s has md5 %s, Part A gives %s' % (rel, B.md5_file(rel), h))
        B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
    B.check_frozen_set()
    for _, rel in PART_A + [(None, MAP_JSON)]:
        B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
    fs = json.loads(B.read(B.FROZEN_JSON))
    text, core_text = B.read(B.TEXT[0]), B.read(B.CORE[0])
    claims = B.claims_now(json.loads(B.read(B.CLAIMS_JSON[0])))
    bad = [c['id'] for c in claims if not B.GUARD_CLAIM.fullmatch(c['id'])]
    B.need(not bad, 'claim ids the sandbox guard cannot run alone: %s' % bad)
    mp = json.loads(B.read(MAP_JSON))
    items, bear, blocked = free_set(fs, text, mp)
    B.need(len(items) == 238 and Counter(i['kind'] for i in items) == Counter({'sentence': 169, 'definition': 69}),
           'the free set is not 169 sentences and 69 definitions')
    B.need(len({i['id'] for i in items}) == 238, 'a free item twice')
    cnt = Counter(i['section'] for i in items)
    B.need(set(cnt) == {1, 2, 3, 4}, 'a section is empty')
    files = OrderedDict()
    body = template_md(fs, text, core_text, claims, items, bear, blocked)
    files[FREE_MD] = body
    B.need(not B.model_for_candidate(body), 'the template uses "model" for a candidate')
    for dst, rel, h in sources(body):
        if rel == FREE_MD:
            continue
        B.need(os.path.isfile(B.path(rel)), '%s is not there' % rel)
        B.need(h is None or B.md5_file(rel) == h, '%s has md5 %s, expected %s' % (rel, B.md5_file(rel), h))
        B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
    B.need(B.committed('records/Semantics - Decisions.md'), 'the decisions record differs from HEAD')
    owner, own = B.owner_words(B.read('records/Semantics - Decisions.md'))
    for old, new in [
        ('S52 is the instruction for this part: you are one of the four agents it names.',
         'S52 is the instruction for this part: its second part ("The next bit") is this one, Part B.'),
        ('*What S52 is.* This part is the first of the two S52 names (Part A).',
         '*What S52 is.* This part is the second of the two S52 names (Part B); the first, Part A, has ended.')]:
        B.need(owner.count(old) == 1, "the owner's words frame changed: %r" % old)
        owner = owner.replace(old, new)
    cc = Counter(c['status_now'] for c in claims)
    claims_counts = '%d hold on every model tried, %d have a counterexample, %d were not tested, of %d' % (
        cc['HOLDS ON ALL MODELS TRIED'], cc['COUNTEREXAMPLE FOUND'], cc['NOT TESTED'], len(claims))
    sandbox = B.SANDBOX.format(claims_counts=claims_counts)
    for old, new in [(TEMPLATE_ROWS_OLD, TEMPLATE_ROWS_NEW),
                     ('| `BRIEF.md` | this brief |', PART_A_ROWS + '\n| `BRIEF.md` | this brief |'),
                     ('Other agents implement and compute it.', 'Another agent implements and computes it.')]:
        B.need(sandbox.count(old) == 1, 'the sandbox table has changed: %r' % old[:60])
        sandbox = sandbox.replace(old, new)
    explanation = B.EXPLANATION.format(explanation=B.EXPLANATION_NOW)
    explanation += ("\n\nIn Part B the definitions that compose these parts are FROZEN (they were Part A's middle): "
                    "(E)'s D6.7, Dec's D12.3, D16.XV, and Dependence's D6.4 and D6.5. Free are the conjuncts' own "
                    "definitions, (F1) D5.4, (F2) D5.5, (A) D5.6, NonVacuous D6.6 and D6.1, D6.2, and what all of "
                    "them are built from (the template's §2).")
    form = form_b()
    rows = []
    for n, title, stretch, what in SECTIONS:
        its = [i for i in items if i['section'] == n]
        b_e = [i['id'] for i in its if '(E)' in i['bears_on']]
        b_dec = [i['id'] for i in its if 'Dec' in i['bears_on'] and '(E)' not in i['bears_on']]
        b_rest = [i['id'] for i in its if i['bears_on'] and not set(i['bears_on']) & {'(E)', 'Dec'}]
        sc = [i['id'] for i in its if i['strong_candidate']]
        b = '\n\n'.join([
            INTRO.format(n=n, title=title, stretch=stretch, nlines=len(B.lines_of(text))), owner, sandbox, explanation,
            MEANING_SCOPE,
            JOB.format(n=n, title=title, stretch=stretch, n_s=sum(1 for i in its if i['kind'] == 'sentence'),
                       n_d=sum(1 for i in its if i['kind'] == 'definition'), b_e=ids(b_e), b_dec=ids(b_dec),
                       b_rest=ids(b_rest), sc=ids(sc), carry=carry_text(n), blocked=blocked_text(n, blocked)),
            form, REPORT.format(n=n)]) + '\n'
        frame = b
        for pat in FRAME_LABELS:
            frame = re.sub(pat, 'LABEL', frame)
        hits = B.scan(frame)
        B.need(not hits, 'brief %d: the frame holds %s' % (n, hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (n, B.words(b), CAP))
        for k in B.KEEP:
            B.need(B.OWNER_CHECK.get(k, own[k].split('"')[1]) in b, "brief %d lacks the owner's words of S%d" % (n, k))
        rel = 'tests/S109 Part B round 1 - GLM job %d, section B%d, %s.md' % (n, n, title)
        files[rel] = b
        rows.append((n, title, 's109_glm_section%d' % n, rel, B.words(b), B.md5(b)))
    entries = []
    for dst, rel, _ in sources(body):
        t = files.get(rel)
        entries.append({'path': dst, 'src': rel, 'md5': B.md5(t) if t is not None else B.md5_file(rel)})
        if not dst.endswith('.py'):
            hit = B.model_for_candidate(t if t is not None else B.read(rel))
            B.need(not hit, '%s uses "model" for a candidate: %s (decision S43)' % (rel, hit))
    for e in entries:
        B.need(not re.search(r'(\.env$|key)', e['path'], re.I), 'a sandbox path looks like a key file: %s' % e['path'])
    fj = OrderedDict([
        ('about', "S109 Part B of decision S52, round 1: the free set (Part A's frozen set, the parts that are hard to "
                  "vary in Claude's working reading, not approved by the owner) in four sections, and what each free "
                  "item bears on in the explanation definition, from Part A's map after its cross-examination. Built by "
                  "tools/s109_build.py; the template is the .md beside this file."),
        ('inputs', {rel: B.md5_file(rel) for rel in [B.FROZEN_JSON, B.FROZEN_MD, MAP_JSON, B.TEXT[0], B.CORE[0],
                                                     B.CLAIMS_JSON[0]]}),
        ('sections', [{'section': 'B%d' % n, 'title': t, 'stretch': s, 'holds': w,
                       'items': sum(1 for i in items if i['section'] == n)} for n, t, s, w in SECTIONS]),
        ('split_rule', "Parts 0-III -> B1; Part IV under the heading 'Transports' -> B2, the rest of Part IV -> B3; "
                       "Parts V, VII, VIII -> B2; Part VI before L315 -> B2, from L315 -> B4; Parts X-XII -> B3; Parts "
                       "IX, XIII-XVI -> B4; a definition by the first line it formalizes, else by its Part"),
        ('bearing_sets', {p: sorted(v) for p, v in bear.items()}),
        ('carry_overs', CARRY), ('part_A_variants_blocked_by_a_free_item', blocked), ('items', items)])
    files[FREE_JSON] = json.dumps(fj, indent=1, ensure_ascii=False) + '\n'
    manifest = {'note': "Part B of decision S52, round 1 (log S109): the files copied into each GLM call's sandbox, each "
                        "checked by md5 at the copy; the brief is added as BRIEF.md. Part A's material, with the Part B "
                        "template in place of Part A's and Part A's end state under part A/. Written by tools/s109_build.py.",
                'text': {'path': B.TEXT[0], 'md5': B.md5_file(B.TEXT[0])},
                'free_set': {'path': FREE_JSON, 'md5': B.md5(files[FREE_JSON])},
                'template': {'path': FREE_MD, 'md5': B.md5(body)},
                'sections': [{'section': 'B%d' % n, 'title': t, 'stretch': s} for n, t, s, _ in SECTIONS],
                'decisions_record': {'path': 'records/Semantics - Decisions.md',
                                     'md5': B.md5_file('records/Semantics - Decisions.md')},
                'files': entries}
    files[MANIFEST] = json.dumps(manifest, indent=1, ensure_ascii=False) + '\n'
    jobs = {'round': 'Part B of decision S52, round 1 (log S109)', 'rule': READING_RULE, 'out': OUT, 'max_pass': 3,
            'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'manifest': MANIFEST, 'manifest_md5': B.md5(files[MANIFEST]),
            'sandbox_root': 's109_sandboxes', 'home_root': 's109_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py',
            'jobs': [{'job': n, 'name': 'section%d' % n, 'tag': tag, 'brief': rel, 'brief_md5': h}
                     for n, title, tag, rel, w, h in rows]}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows, manifest, items


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s109_build.py [--check]')
    files, rows, manifest, items = build()
    if '--check' in a:
        for rel, text in files.items():
            B.need(os.path.exists(B.path(rel)) and B.read(rel) == text, '%s differs from the build' % rel)
        print('check: all %d files identical to the build' % len(files))
    else:
        for rel, text in files.items():
            print(('wrote   ' if B.write_checked(rel, text) else 'same    ') + rel)
    c = Counter((i['section'], i['kind']) for i in items)
    print('\nsections:', '; '.join('B%d %d sentences + %d definitions' % (n, c[(n, 'sentence')], c[(n, 'definition')])
                                  for n in (1, 2, 3, 4)))
    print('\n| section | title | tag | brief | words (build) | md5 |\n|---|---|---|---|---|---|')
    for n, title, tag, rel, w, h in rows:
        print('| B%d | %s | %s | `%s` | %d | %s |' % (n, title, tag, rel, w, h))
    print('\nsandbox: %d files from the manifest + BRIEF.md; manifest md5 %s' % (len(manifest['files']),
                                                                            B.md5(files[MANIFEST])))


if __name__ == '__main__':
    main()
