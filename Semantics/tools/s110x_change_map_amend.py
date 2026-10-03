#!/usr/bin/env python3
"""s110x_change_map_amend.py: the change map of log S110 after the GLM cross-examination (rule 4 of
results/S110 - how the GLM cross-examination will be read, written before sending.md). Written 29 September 2026 by the
one Opus 5.5 agent that settled the cross-examination (decision S56).

It imports tools/s110_change_map.py for its data and its build(), never writes that file or the map as sent, applies
the amendments that stand (each marked with its objection id, Xa1 ... Xd9, as numbered in
results/S110 - the GLM cross-examination, settled.md), and writes the corrected copy:
  results/S110 The change map - the earlier frameworks and the present theory, after the cross-examination.json
Every node and edge touched carries "amended": [ids]. It prints the totals and, with --tables FILE, writes the node and
edge tables of section 10 of the corrected Markdown copy to FILE.

  python3 -B Semantics/tools/s110x_change_map_amend.py [--tables FILE] [--check]
"""
import collections, copy, importlib.util, json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
OUT = 'results/S110 The change map - the earlier frameworks and the present theory, after the cross-examination.json'

spec = importlib.util.spec_from_file_location('s110_change_map', os.path.join(HERE, 's110_change_map.py'))
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

N = [list(n) for n in cm.N]
E = [list(e) for e in cm.E]
MISSING = [list(m) for m in cm.MISSING]
MARK = collections.defaultdict(list)   # node or edge id -> objection ids


def node(i):
    return next(n for n in N if n[0] == i)


def edge(i):
    return next(e for e in E if e[0] == i)


def set_node(i, ids, **kw):
    n = node(i)
    for k, v in kw.items():
        n[['id', 'theme', 'name', 'where', 'what'].index(k)] = v
    MARK[i] += ids


def set_edge(i, ids, **kw):
    e = edge(i)
    for k, v in kw.items():
        e[['id', 'step', 'from', 'to', 'kind', 'how', 'standing', 'by'].index(k)] = v
    MARK[i] += ids


def add_node(after, row, ids):
    k = [n[0] for n in N].index(after) + 1
    N.insert(k, list(row))
    MARK[row[0]] += ids


def add_edge(after, row, ids):
    k = [e[0] for e in E].index(after) + 1
    E.insert(k, list(row))
    MARK[row[0]] += ids


# ---- job a: FW0 and I2 ----
set_edge('e98', ['Xa1', 'Xa2'], **{'from': ['I2.10', 'I2.11', 'I2.13'], 'standing': 'inferred',
         'how': 'attention learning, token allowance and daydreaming are implementation choices; FW5: "not a condition of this class" (said of specification 0.1, not of I2)',
         'by': 'FW5 "Reconciliation", "What is retained" (of specification 0.1, S7); I2 is 0.4, version gap as e96; I2 Part VIII calls daydreaming "an operational allowance"'})
add_edge('e98', ('e150', 'I2>FW5', ['I2.14'], ['FW5.20'], 'changed', 'finite resources as realisation conditions become the declared enabling conditions (resources, maintenance, disturbances) under which an owned capability is claimed', 'inferred', 'FW5 "Enabling conditions and achievement conditions"; version gap as e96'), ['Xa2'])
add_node('FW0.20', ('FW0.21', 'STA', 'GoodNow: preferred by a maximal comparison, not defeated', '§16.2 "Rival comparison, preference, defeat"', 'preference is the set of maximal CompareRivals events, "reported, not collapsed"; defeat is a reject whose criticism survives adjudication; "`GoodNow` does not entail `True`, finality, or wide reach"'), ['Xa4'])
add_edge('e24', ('e151', 'FW0>FW2', ['FW0.21'], ['FW2.18'], 'changed', 'being good now (preferred, not defeated) becomes merit preference among actual alternatives, FW2\'s "current good explanation"', 'inferred', 'the wording of both; no document joins them'), ['Xa4'])
add_node('I2.14', ('I2.15', 'ERR', 'dependency effects are scoped, not a truth cascade', 'Part II, section of that name', 'parking a necessary input stops the dependent uses under that binding, pending reconsideration; it proves no conclusion false'), ['Xa5'])
add_edge('e150', ('e152', 'I2>FW5', ['I2.15'], ['FW5.31'], 'kept', 'withdrawing an essential premise stops the uses that need it and makes no conclusion false', 'inferred', 'FW5 "Standing and actual use", (K2) and the paragraph after it; version gap as e96'), ['Xa5', 'Xc3'])
add_node('FW0.21', ('FW0.22', 'STA', 'completeness certificates: what an absence licenses', '§7.5', '"Without the certificate, absence yields OPEN"; a certificate covers its snapshot and is never promoted to "variants no one has imagined"'), ['Xa6'])
add_node('FW0.22', ('FW0.23', 'ERR', 'diversion and lapse: stopping without a verdict', '§6.4', '"Diversion proves attention elsewhere, not abandonment"; a lapse names its cause, and "`unknown` is legitimate"'), ['Xa6'])
set_node('FW0.11', ['Xa8'], what='authorship needs an origin body (channels, a provenance graph, the problem-specific organisation); the public predicate is bound to its witness (change register row 8)')
set_node('FW0.12', ['Xa8'], what='a criticism names its target, problem, background, standard and the merits to keep, fixed before the response; the system "must represent the criticism it answers"')
MISSING[0][2] = "the earlier event semantics and its audit (FW0's stated predecessors: Revision C, Revision D and its second audit)"
MARK['M0'] += ['Xa7']
MISSING.insert(1, ['CR-1.0', 'FW0 (its standing authority)', 'the first version of the class: typed schema with primitive decisive relations, its constructor dossier, theorems TH-1 to TH-17, source keys (among them CT-7)'])
MARK['CR-1.0'] += ['Xa7']

# ---- job b: FW2, FW3, FW4 ----
set_edge('e48', ['Xb1', 'Xb5'], **{'from': ['FW2.1', 'FW2.2', 'FW2.3', 'FW2.4', 'FW2.7', 'FW2.9', 'FW2.17', 'FW2.20', 'FW2.25', 'FW2.26', 'FW2.27', 'FW2.33', 'FW2.34']})
add_node('FW3.23', ('FW3.24', 'ERR', 'T11: Essential entails Work, not conversely', 'Part II T11', '"Shown to do no work" and "withdrawn as essential" are different operations: the first a criticism of quality, the second removes usability'), ['Xb1'])
add_edge('e49', ('e153', 'FW2>FW3', ['FW2.13'], ['FW3.24'], 'changed', 'Essential redefined through minimal working subsets; two operations distinguished', 'stated', 'FW3 change register, row "Part II, dependencies"'), ['Xb1'])
add_edge('e153', ('e154', 'FW2>FW3', ['FW2.28'], ['FW3.20'], 'changed', 'E1 restated as conversion from DependsOn to Deployed; escaping dependencies named', 'stated', 'FW3 change register, row "Part II, hierarchy"'), ['Xb1'])
add_edge('e154', ('e155', 'FW2>FW3', ['FW2.31'], ['FW3.6'], 'changed', 'Progress conjectured to be a gain in Account or Bearing', 'stated', 'FW3 change register, row "Part II, progress"'), ['Xb4'])
add_node('FW3.24', ('FW3.25', 'CRE', 'Contribution: authorship as Account on provenance (conjecture)', 'I.4 "Contribution"', 'an account of why the content has the organization it has that attributes it to the system\'s activity; "Mere causal involvement is not sufficient"'), ['Xb13'])
add_edge('e155', ('e156', 'FW2>FW3', ['FW2.16'], ['FW3.25'], 'changed', 'FW2\'s "an account of the contribution" read as an Account on provenance (conjecture)', 'stated', 'FW3 I.4 "Contribution"; change register, row "Part II, newness and authorship"'), ['Xb13'])
set_edge('e64', ['Xb13'], **{'from': ['FW3.5', 'FW3.6', 'FW3.25'], 'how': 'Bearing, Progress and contribution as instances of Account, still conjectures'})
set_edge('e65', ['Xb2'], **{'from': ['FW3.22'], 'how': "the repair addressed to FW2's text (the explaining-away renaming) is not in FW4, which stands alone"})
add_edge('e68', ('e157', 'FW3>FW4', ['FW3.23'], ['FW4.15'], 'kept', 'the deployed set is a record fact, the working set is not', 'inferred', 'FW4 Part VIII R15; Part XII "Record facts it may hold"'), ['Xb2'])
add_node('FW2.32', ('FW2.33', 'REC', 'the jump conjecture: EX = UED', 'Part IV "Named criticism routes and conjectures"', 'an organization that has extended itself into one independent domain by revising its own generator constraints can do so for any admitted domain; "universality arrives as a jump"'), ['Xb5'])
add_node('FW2.33', ('FW2.34', 'ERR', 'realization constraints 3 to 6', 'Part II "Physical realization and constructor-theoretic scope", constraints 3 to 6', 'retention with provenance; standing discipline; constraints as copyable contents; "Nothing first-layer crosses a boundary"'), ['Xb5'])
add_node('FW2.34', ('FW2.35', 'STA', 'refinement without semantic substitution', 'Part IV, section of that name', '"A machine-level classification may entail a semantic proposition only under an explicit bridge whose adequacy is open to criticism"'), ['Xb5'])
set_edge('e43', ['Xb5'], **{'from': ['FW2.14', 'FW2.35'], 'how': 'specification discipline S1 to S10; "knowledge" a forbidden field; it amends FW2\'s refinement section'})
set_edge('e35', ['Xb8'], by='FW3 I.5 ("This is FW2\'s "current good explanation.""); change register, row "Part II, progress"')
set_edge('e42', ['Xb9'], by='FW3 T17 (N1 §6 C5); III.3; change register, row "Part I-A, K-STANDING commentary"')
set_edge('e76', ['Xb11'], by='FW5 "Support families without a minimality assumption"; "Reconciliation", "What the structurally extended source had already repaired"')
set_edge('e56', ['Xb14'], by='FW4 "Where this belongs" ("transport"); FW4 III.5')

# ---- job c: FW5, the present theory, S89 ----
set_edge('e125', ['Xc1'], how='physical possibility enters where a content is instantiated in a carrier or transformed, and also as the content of claims a candidate can conflict with (no list closed)')
set_edge('e122', ['Xc2'], standing='recorded', by='tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md, W60.1 (inserted after "Historical index"); it matches the owner\'s S20, "the mistake shouldn\'t be able to creep back in"')
add_node('FW5.30', ('FW5.31', 'ERR', 'Usable_j (K2): licence, scope, live premises', '"Standing and actual use"', 'withdrawing an essential premise makes an application unusable; another argument for the same conclusion can stay usable; the conclusion is not thereby false'), ['Xc3'])
add_node('FW5.31', ('FW5.32', 'EXP', 'the question contract', '"Mathematical foundations", "Questions and their contracts"', 'target, scope, baseline, respect, contrast contract, query operator and obligations; a question is an indexed structure'), ['Xc3'])
add_node('PT.33', ('PT.34', 'ERR', 'conflict with a claim; rivals given a claim', 'Part VI "Rivals"', 'a candidate can conflict with a claim as well as with a rival; ruling a candidate out by a claim taken as given is the assessor\'s choice'), ['Xc3'])
add_node('PT.34', ('PT.35', 'CRE', 'contracts have provenance; a question can be found', 'Part III "Contracts have provenance"; Part XVI, 5', 'a contract is declared, selected or constructed; question-finding is representable (claim QF)'), ['Xc3'])
set_edge('e110', ['Xc3'], **{'from': ['FW5.8', 'FW5.31'], 'how': 'K3 kept; K2 kept, with usability tied to premises live for the person and a premise taken as given allowed'})
add_edge('e142', ('e158', 'FW5>PT', [], ['PT.34'], 'added', 'conflict with a claim, and rivals given a claim taken as given', 'recorded', 'decisions S25 to S27; results/S96 (conflict by argument)'), ['Xc3'])
add_edge('e158', ('e159', 'FW5>PT', ['FW5.32'], ['PT.35'], 'changed', 'the question contract kept; contracts given a provenance, and question-finding made representable', 'inferred', 'tests/107 Part III against FW5 "Questions and their contracts"'), ['Xc3'])
set_edge('e113', ['Xc4'], **{'to': ['PT.8'], 'kind': 'changed', 'how': 'the paragraph on representational fidelity against content correction is gone; the two defects survive as (R)\'s two transports: from carrier to content, and from the content\'s target to the content', 'by': 'tests/107 Part IV ("A system can represent a theory in error") against FW5 "Physical realization of semantic organization"; "inscription" occurs 0 times in tests/107'})
set_edge('e103', ['Xc5'], how='tasks and possibility kept; information variables dropped (information 0 times from file 10 on); copying kept as a transformation [read in tests/107 Part I and Part XII, not in S89]')
set_edge('e105', ['Xc6'], by='results/S89, observation 8 ("CT1 and CT2 retention" in file 10); tests/107 Part XII')
set_edge('e101', ['Xc7'], by='results/S89, observations 9 and 10 (file 10, line 216; declared provenance); where between FW5 and file 10 it came in is not documented')
set_edge('e73', ['Xc10'], by='FW5 "Reconciliation", "What is retained" ("criticism as itself conjectural"); the reason-bearing half is inferred, from FW5 "Criticism, evidence, and operative decisions"')
set_node('PT.3', ['Xc11'], where='Part 0 "What this document claims"; Part I "Fallibility without error-as-work"; Part V (Account); Part IV "Three provenances" (Dec)')

# ---- section 5's chains (Xa3, Xb7): links the chains use that the map lacked, each a reading ----
add_edge('e134', ('e160', '>FW5', ['FW4.9'], ['FW5.7'], 'changed', 'Bearing as an instance of Account (a conjecture) becomes criticism with its bearing, reason use as causal organization', 'inferred', 'FW4 Part V against FW5 "Criticism, evidence, and operative decisions"'), ['Xa3'])
add_edge('e160', ('e162', '>FW5', ['FW4.8'], ['FW5.4'], 'changed', 'Account A1 to A3 becomes the structural answer (E); non-circular dependence returns into it', 'inferred', 'FW4 Part IV against FW5 "Explanatory adequacy without a Because primitive"'), ['Xa3'])
add_edge('e151', ('e161', 'FW0>FW2', ['FW0.7'], ['FW2.11'], 'changed', '"prediction is not explanation", a cross-sort bridge, becomes a clause of Account', 'inferred', 'the wording of both; no document joins them'), ['Xa3'])


def build():
    cm.N, cm.E, cm.MISSING = [tuple(n) for n in N], [tuple(e) for e in E], [tuple(m) for m in MISSING]
    _, nodes, edges = cm.build()
    data = json.loads(cm.build()[0], object_pairs_hook=collections.OrderedDict)
    data['title'] = 'S110 The change map - the earlier frameworks and the present theory, after the cross-examination'
    data['written'] = ('29 September 2026, by the one Opus 5.5 agent of log S110 (decision S56); corrected the same day after '
                       'the GLM cross-examination by tools/s110x_change_map_amend.py (each amendment marked by its objection id)')
    for x in data['nodes'] + data['edges']:
        if x['id'] in MARK:
            x['amended'] = MARK[x['id']]
    for x in data['missing']:
        if x['id'] in MARK:
            x['amended'] = MARK[x['id']]
    return json.dumps(data, indent=1, ensure_ascii=False) + '\n', data


def tables(data):
    themes = collections.OrderedDict(cm.THEMES)
    out = []
    for t, name in themes.items():
        ns = [n for n in data['nodes'] if n['theme'] == t]
        out += ['### Nodes: %s (%s, %d)' % (name, t, len(ns)), '', '| id | name | where |', '|---|---|---|']
        for n in ns:
            mk = ' [%s]' % ', '.join(n['amended']) if 'amended' in n else ''
            out.append('| %s%s | %s | %s |' % (n['id'], mk, n['name'], n['where']))
        out.append('')
    for s in data['steps']:
        es = [e for e in data['edges'] if e['step'] == s['id']]
        out += ['### Edges: %s (%d)' % (s['name'], len(es)), '', '| id | from | to | kind | how | standing |',
                '|---|---|---|---|---|---|']
        for e in es:
            mk = ' [%s]' % ', '.join(e['amended']) if 'amended' in e else ''
            st = e['standing'] + (': ' + e['by'] if e['by'] else '')
            out.append('| %s%s | %s | %s | %s | %s | %s |' % (e['id'], mk, ', '.join(e['from']) or '(none)',
                       ', '.join(e['to']) or '(none)', e['kind'], e['how'], st))
        out.append('')
    return '\n'.join(out)


def main():
    text, data = build()
    p = os.path.join(SEM, OUT)
    if '--check' in sys.argv[1:]:
        same = os.path.exists(p) and open(p, encoding='utf-8').read() == text
        print('check: %s' % ('identical to the build' if same else 'DIFFERS from the build'))
        sys.exit(0 if same else 1)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)
    if '--tables' in sys.argv[1:]:
        with open(sys.argv[sys.argv.index('--tables') + 1], 'w', encoding='utf-8') as f:
            f.write(tables(data))
    nodes, edges = data['nodes'], data['edges']
    c = collections.Counter
    print('nodes %d; by version %s' % (len(nodes), dict(c(n['version'] for n in nodes))))
    print('by theme %s' % dict(c(n['theme'] for n in nodes)))
    print('edges %d; by kind %s; by standing %s' % (len(edges), dict(c(e['kind'] for e in edges)), dict(c(e['standing'] for e in edges))))
    for s in data['steps']:
        es = [e for e in edges if e['step'] == s['id']]
        print('  step %-8s %3d edges; kinds %s; standing %s' % (s['id'], len(es), dict(c(e['kind'] for e in es)), dict(c(e['standing'] for e in es))))
    touched = {x for e in edges for x in e['from'] + e['to']}
    print('nodes on no edge: %s' % sorted(set(n['id'] for n in nodes) - touched))
    print('missing rows: %d' % len(data['missing']))
    print('amended ids: %d' % len(MARK))


if __name__ == '__main__':
    main()
