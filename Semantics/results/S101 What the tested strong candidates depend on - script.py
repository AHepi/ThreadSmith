#!/usr/bin/env python3
"""S101: what the seven tested strong candidates depend on, and what depends on them, by program.

Reads the latest theory text, the S98 ledger's sentence index and records, and S100's page and per-unit data
(each tested against its md5). Builds a graph of the text's defined terms, claims and end points: edges from Part
XIV's dependence order, edges read from the wording of each definition (proposed by a word scan and kept, dropped or
added by the reading tables below), and inferential edges read from the text. Joins every node's sentences to
S100's stability data, and writes two files beside this script: the analysis page and the graph as JSON. Nothing
else is written; no input is changed. A rerun gives the same bytes.

Run from results/: PYTHONDONTWRITEBYTECODE=1 python3 "S101 What the tested strong candidates depend on - script.py"
"""
import sys
sys.dont_write_bytecode = True

# ======================================================================================================
# The nodes: id, label, kind, the sentences (units of the S98 sentence index) that define it, and the words
# and symbols by which the scan finds it in other definitions
# ======================================================================================================
# kinds: 'end point: structural vocabulary', 'end point: declared index', 'end point: declared input',
#        'end point: import', 'end point read from the definition', 'defined', 'claim', 'candidate'

NODES = [
    # ---- end points the text declares
    ('O', '(O) organization: ports, components, admitted edits, boundary conditions, compatible valuations',
     'end point: structural vocabulary',
     ['L85.s1', 'L87.s1', 'L91.s1', 'L91.s2', 'L91.s3', 'L91.s4', 'L91.s5', 'L91.s6', 'L93.s1', 'L97.s1', 'L99.s1',
      'L103.s1', 'L103.s2'],
     r'\(O\)|\bSol_|\borgani[sz]ations?\b|\bdeleted component|\bfull relation|\bfootprints?\b|\badmitted edits?\b|\bports?\b|\bboundary conditions?\b|\bcomponents?\b'),
    ('Q', '(Q) the query and the answer profile Ans_p', 'end point: structural vocabulary',
     ['L141.s3', 'L141.s4', 'L143.s1'],
     r'\(Q\)|\bAns_|\bcalQ\b|\banswer profiles?\b|\bquer(y|ies)\b|\banswers?\b'),
    ('contract', 'the contract C (a declared index; the admitted edit-boundary pairs a claim ranges over)',
     'end point: declared index', ['L141.s2', 'L524.s1'], r'\bcontracts?\b'),
    ('grain', 'the grain (a declared index)', 'end point: declared index', ['L524.s1'], r'\bgrain\b|ℓ'),
    ('idx_bcont', 'boundary and continuity as declared indices', 'end point: declared index', ['L524.s1'], r'β|Ω'),
    ('in_scope', 'declared input: the scope a claim states for its contract, and why the question is answered on that restriction',
     'end point: declared input', ['L159.s1', 'L159.s5', 'L159.s7', 'L524.s4'], r'\bstated scope\b|\bscope\b'),
    ('in_aims', 'declared input: the aims O and P of a repair, with the occasions each covers',
     'end point: declared input', ['L435.s2', 'L441.s1'],
     r'claimed aims?|protected aims?|protected condition|\baims?\b|O_ex'),
    ('in_bcont', 'declared input: the system boundary and continuity of an attribution',
     'end point: declared input', ['L473.s1', 'L473.s3', 'L524.s4'],
     r'system boundary|declared boundary|boundary and continuity|declared continuity|inside the boundary|outside (that|the) boundary|resource contract'),
    ('in_assessor', 'declared input: for an assessor j, the inference forms j admits, the scope j declares, the premises j tentatively accepts and has not withdrawn',
     'end point: declared input', [], r'\bassessors?\b'),
    ('in_weight', 'declared input: a weighting of attribution among several contributions to one achievement',
     'end point: declared input', [], r'\bweighting\b'),
    ('decl_list', 'the list of declared inputs (Part XIV)', 'list', ['L522.s1', 'L522.s2'], None),
    ('theta', 'import 1: the physical module Θ, with Org_ℓ', 'end point: import', ['L517.s1'],
     r'physical module|Θ|\bOrg_|physical interpretation|physically located|physically admitted|physical history|\bthe physics\b'),
    ('N', 'import 2: the appraisal relation 𝒩', 'end point: import', ['L518.s1'], r'appraisal relation|calN'),
    ('math', 'mathematics used and not defined (sets, functions, linear maps, metrics, order)',
     'end point read from the definition', [], None),
    ('tentative', 'to tentatively accept a claim (a person\'s choice to go on with it)',
     'end point read from the definition', ['L8.s6'], r'tentatively accept'),
    ('use_task', 'the declared use task U (Deploy)', 'end point read from the definition', [], r'use task'),
    ('aims_q', 'the aims O_p of a question', 'end point read from the definition', ['L147.s1'], r'\bO_p\b'),
    # ---- defined terms
    ('question', 'a question p = (D, C, b_0, 𝒬, O_p, ρ_p) as a whole', 'defined',
     ['L135.s1', 'L137.s1', 'L141.s1', 'L147.s2'], r'\bquestions?\b'),
    ('prov_c', 'the provenance ρ_p of a contract (declared, selected, constructed)', 'defined',
     ['L155.s1', 'L155.s3', 'L155.s4', 'L155.s6'], r'ρ_p|provenance of the contract'),
    ('roles', 'roles: input, output, observation', 'defined', ['L109.s2', 'L109.s3', 'L109.s4'],
     r'\binputs? under\b|\boutputs? of component|\bobservation edits?'),
    ('K', '(K) signature; of one kind; kind', 'defined', ['L113.s1', 'L113.s2', 'L115.s1', 'L119.s1', 'L119.s2'],
     r'\(K\)|\bsig_|\bsignatures?\b|\bof one kind\b|\bkinds?\b'),
    ('sigfam', 'families of signatures: causal assignment, measurement, rule application', 'defined',
     ['L121.s1', 'L123.s1', 'L124.s1', 'L125.s1'], r'causal assignment|rule application'),
    ('occ', 'occurrence (a physically located carrier)', 'defined', ['L169.s1'], r'\boccurrences?\b|\bcarriers?\b'),
    ('content', 'content (an organization with its contract-relative commitments)', 'defined', ['L169.s2'],
     r'\bcontents?\b'),
    ('layers', 'object layer and simulation layer', 'defined', ['L175.s1', 'L177.s1'],
     r'object layer|simulation layer'),
    ('transport', 'transport t = (π, τ, σ, λ)', 'defined', ['L183.s1', 'L185.s1', 'L189.s1'],
     r'\btransports?\b|τ\(|σ\(|λ\('),
    ('fid', '(F1), (F2), (A): component, global and question fidelity; faithful on C', 'defined',
     ['L189.s2', 'L233.s1', 'L235.s1', 'L239.s1', 'L241.s1', 'L247.s1', 'L249.s1'],
     r'\(F1\)|\(F2\)|\(A\)|\bfaithful\b|\bfidelity\b|Faithful_'),
    ('cand', 'explanatory candidate (E, p, t, Γ): active commitments Γ and the named background', 'defined',
     ['L231.s1', 'L231.s2'], r'explanatory candidates?|\bcandidates?\b|Γ|active (components?|commitments?)|\bcommitments?\b|calE'),
    ('noncirc', 'non-circular dependence', 'defined', ['L255.s1', 'L255.s2', 'L255.s3', 'L255.s4'],
     r'[Nn]on-circular|NonCircular'),
    ('nonvac', 'non-vacuity', 'defined', ['L257.s1', 'L257.s2', 'L257.s3'], r'[Nn]on-vacu|NonVacuous'),
    ('E', '(E) Account', 'defined', ['L231.s3', 'L261.s1', 'L265.s1'], r'\(E\)|\bAccount\b|\baccounts?\b'),
    ('SBD', '(S), (B), (D): routes of a candidate, critical blocks, the boundary of organization edits', 'defined',
     ['L287.s2', 'L289.s1', 'L295.s1', 'L299.s2', 'L301.s1'],
     r'\((S|B|D)\)|(?<!active )\broutes?\b|\bcritical\b|CriticalBlock|\bsfS\b|Boundary_'),
    ('prov', 'three provenances of a transport: selected, constructed, declared (Sel, Con, Dec); survival on H; selection in the physical module',
     'defined', ['L193.s1', 'L195.s1', 'L195.s2', 'L195.s3', 'L195.s5', 'L197.s1', 'L197.s2', 'L199.s1', 'L199.s2',
                 'L481.s1', 'L481.s3'],
     r'\bprovenances?\b|\bSel\(|\bCon\(|\bDec\(|\bselected\b|survives? on|\bpopulation\b|selection histor|\bsurvival\b'),
    ('rep', '(R) representation', 'defined', ['L205.s1', 'L207.s1'],
     r'\(R\)|\bRep_|\brepresent(s|ed|ation|ations)?\b'),
    ('psv', 'prediction, violation, surprise; selection and construction responses', 'defined',
     ['L217.s1', 'L219.s1', 'L220.s1', 'L221.s1', 'L225.s2', 'L225.s3'],
     r'\bpredictions?\b|\bviolat(ed|ion|ions)\b|\bsurprised?\b'),
    ('hist', 'histories h', 'defined', ['L375.s1'], r'\bhistor(y|ies)\b|\bsubhistor(y|ies)\b'),
    ('aroute', 'active route', 'defined', ['L375.s2', 'L375.s3'], r'active routes?'),
    ('K1', '(K1) Bearing', 'defined', ['L377.s1', 'L377.s2', 'L379.s1'], r'\(K1\)|\b[Bb]earing\b'),
    ('K2', '(K2) Usability', 'defined', ['L387.s1', 'L389.s1'], r'\(K2\)|\bUsable_|\busable\b|\b[Uu]sability\b'),
    ('formj', 'Form_j: the inference form of a step is one j admits', 'defined', ['L393.s1'], r'\bForm_j'),
    ('scopej', 'Scope_j: the step is applied within the contract, grain and boundary j has declared', 'defined',
     ['L393.s2'], r'\bScope_j'),
    ('livej', 'Live_j: a premise is live for j', 'defined', ['L393.s2'], r'\bLive_j|\blive\b'),
    ('K3', '(K3) what a test rules out', 'defined', ['L395.s1'], r'\(K3\)'),
    ('arg', 'argument: argument tree, steps, record leaves; usable when each step is (K2)', 'defined',
     ['L8.s1', 'L8.s2', 'L397.s1', 'L397.s2', 'L397.s3', 'L397.s4'],
     r'\b[Aa]rguments?\b(?!\s*\d)|record leaf'),
    ('rules_out', 'an argument rules out a claim: the claim inconsistent with its conclusion, its denial not among its premises, read structurally', 'defined',
     ['L8.s3', 'L397.s5', 'L397.s14', 'L397.s15', 'L397.s16'], r'\brules? out\b|\bruling out\b|\bX_j'),
    ('ruled', 'ruled out, and not ruled out, for an assessor', 'defined', ['L315.s6', 'L315.s7'],
     r'\bruled out\b'),
    ('conflict', 'conflict between two candidates', 'defined', ['L315.s2', 'L315.s3'], r'\bconflicts?\b'),
    ('conflict_claim', 'conflict of a candidate with a claim', 'defined', ['L315.s10', 'L315.s11'],
     r'conflicts? with (a |the )?claim'),
    ('rivals', 'rivals', 'defined', ['L315.s1'], r'\brivals?\b'),
    ('problem', 'a problem for p', 'defined', ['L317.s1'], r'\bproblems?\b'),
    ('etv', 'easy to vary', 'defined', ['L317.s11'], r'easy to vary'),
    ('deploy', 'Deploy (deployment) and the repertoire', 'defined', ['L403.s1', 'L403.s2'],
     r'\bDeploy|\brepertoire\b|\bdeployable\b'),
    ('tasks', 'tasks, attributes and possibility in the physical module', 'defined', ['L461.s1', 'L461.s2', 'L461.s3'],
     r'\btasks?\b|\bpossibility\b|\battributes?\b'),
    ('CT1', '(CT1) retained realization', 'defined', ['L463.s1', 'L465.s1', 'L469.s1'],
     r'\(CT1\)|RetReal|retained realization'),
    ('CT2', '(CT2) retention fixed point', 'claim', ['L471.s1', 'L471.s2'], r'\(CT2\)|[Rr]etention fixed point'),
    ('own', 'Ownership', 'defined', ['L427.s1', 'L427.s2', 'L427.s3', 'L427.s4'], r'\bowned\b|\b[Oo]wnership\b'),
    ('can', 'owned capability Can', 'defined', ['L475.s1', 'L475.s2', 'L475.s3'],
     r'\bCan_|owned capability|\bcapabilit(y|ies)\b'),
    ('phys_results', 'achievement (CA) and tolerances (CT3, CT4)', 'defined', ['L477.s1', 'L479.s1', 'L479.s2', 'L479.s3'],
     r'\btolerances?\b|CanAdv|\(CA\)'),
    ('build', 'Build (construction) and the construction trace', 'defined', ['L405.s1', 'L405.s2'],
     r'\bBuild|construction trace'),
    ('N_new', '(N) newness', 'defined', ['L413.s1', 'L413.s3', 'L415.s1'], r'\(N\)|\bNew\(|\bNewness\b|≡'),
    ('G', '(G) origin', 'defined', ['L419.s1', 'L421.s1'], r'\(G\)|\bOrigin'),
    ('episode', 'episodes: complete critical episode, recognized difficulty, creative critical episode', 'defined',
     ['L429.s1', 'L429.s2', 'L429.s3'], r'\bepisodes?\b|recognized difficult|CreativeCriticalEpisode'),
    ('P', '(P) Repair, with the contribution Δ and the reading of protected conditions', 'defined',
     ['L435.s1', 'L435.s2', 'L437.s1', 'L441.s2'], r'\(P\)|\bRepair_|\brepair(s|ed)?\b'),
    ('prodby', 'ProducedBy', 'defined', ['L441.s5'], r'ProducedBy'),
    ('EX', '(EX) created explanation, with Result and ProducesVia', 'defined',
     ['L443.s2', 'L443.s3', 'L445.s1', 'L453.s1', 'L453.s2'],
     r'\(EX\)|CreateEx|[Cc]reated explanation|ProducesVia|\bResult\('),
    ('appraisal', 'Appraisal: the appraisal relation taken as an input; the aesthetic case, achievement (AR)', 'defined',
     ['L455.s1', 'L455.s2', 'L455.s3', 'L455.s4', 'L455.s5'], r'\bapprais|\baesthetic|\(AR\)'),
    ('hist_index', 'historical index', 'defined', ['L367.s1', 'L367.s2'], r'[Hh]istorical index'),
    ('RCU', 'recursion and universality: scrutinizability, (RC), barriers, (U1)-(U3); membership classes', 'defined',
     ['L487.s1', 'L491.s1', 'L495.s1', 'L495.s3', 'L497.s1', 'L499.s1', 'L502.s1', 'L505.s1',
      'L528.s1', 'L528.s2', 'L528.s3', 'L528.s4', 'L528.s5'],
     r'\(RC\)|\(U[123]\)|UECS|[Uu]niversal class|[Rr]ecursive class'),
    # ---- claims
    ('fmc', 'finite monotone claim', 'claim', ['L305.s1', 'L305.s3', 'L305.s4', 'L305.s5'],
     r'finite monotone claim|\bcontributory\b|globally indispensable'),
    ('func', 'functional transport', 'claim', ['L353.s1', 'L353.s2', 'L353.s4'], r'[Ff]unctional transport'),
    ('T2', '(T2) approximate transport', 'claim', ['L363.s1', 'L363.s2', 'L363.s3'],
     r'\(T2\)|[Aa]pproximate transport'),
    ('I2', '(I2) identification, with its setting', 'claim', ['L329.s1', 'L329.s2', 'L329.s3', 'L329.s5'],
     r'\(I2\)'),
    ('O1', '(O1) obstruction', 'claim', ['L335.s1', 'L335.s2'], r'\(O1\)'),
    ('failed', 'a failed answer stays failed', 'claim', ['L369.s1', 'L369.s2', 'L369.s3', 'L369.s4', 'L369.s5', 'L369.s6'],
     r'failed answer stays failed'),
    ('Arg1', 'Argument 1: kind preservation needs no condition of its own', 'claim',
     ['L554.s1', 'L556.s2', 'L556.s3', 'L558.s1', 'L558.s2', 'L558.s3'], None),
    ('Arg2', 'Argument 2: same counterparts, one account', 'claim',
     ['L562.s1', 'L562.s2', 'L562.s3', 'L564.s2', 'L564.s3', 'L566.s1', 'L566.s2', 'L568.s1', 'L568.s2'], None),
    ('Arg3', 'Argument 3: selected transports are underdetermined on unseen changes their population leaves open', 'claim',
     ['L572.s1', 'L572.s2', 'L572.s3', 'L574.s2', 'L574.s3', 'L574.s4', 'L574.s5', 'L576.s1', 'L576.s2', 'L576.s3', 'L576.s4'], None),
    ('Arg4', 'Argument 4: surprise requires an incomplete history', 'claim',
     ['L580.s1', 'L582.s2', 'L582.s3', 'L582.s4', 'L584.s1', 'L584.s2'], None),
    ('Arg5', 'Argument 5: question-finding is representable', 'claim',
     ['L588.s1', 'L588.s2', 'L590.s2', 'L590.s3', 'L590.s4', 'L590.s5', 'L592.s1', 'L592.s2', 'L592.s3'], None),
    ('Arg6', 'Argument 6: there are two imports', 'claim', ['L596.s1', 'L598.s2', 'L600.s1', 'L600.s2', 'L600.s3'], None),
    ('Arg7', 'Argument 7: the frozen assessment and the moving question are consistent', 'claim',
     ['L604.s1', 'L606.s2', 'L606.s3', 'L606.s4', 'L608.s1', 'L608.s2'], None),
    ('Arg8', 'Argument 8: equivariance under structure-preserving recoding', 'claim', ['L612.s1', 'L612.s3'], None),
    ('Arg9', 'Argument 9: output descriptions do not determine accounts', 'claim', ['L616.s1', 'L616.s3', 'L616.s4'], None),
    ('Arg10', 'Argument 10: a two-layer episode, in exact form', 'claim',
     ['L620.s1', 'L620.s2', 'L622.s1', 'L622.s2', 'L622.s3', 'L624.s1', 'L624.s2', 'L624.s3', 'L624.s4', 'L626.s1',
      'L626.s2', 'L626.s3', 'L626.s4', 'L626.s5', 'L626.s6', 'L626.s7', 'L626.s8', 'L628.s1', 'L628.s2', 'L630.s1',
      'L630.s2', 'L630.s3', 'L630.s4', 'L630.s5', 'L632.s1', 'L632.s2'], None),
    ('XV_frame', 'Part XV\'s opening: the claims the rest depends on, each with what would rule it out', 'claim',
     ['L534.s1', 'L534.s2'], None),
    ('XV_input_rule', 'Part XV\'s rule on a case with a missing input', 'claim', ['L534.s3'], None),
    ('suff', '(Suff) Sufficiency', 'claim', ['L536.s1', 'L536.s2', 'L536.s3'], r'\(Suff\)'),
    ('nec', '(Nec) Necessity', 'claim', ['L538.s1', 'L538.s2'], r'\(Nec\)'),
    ('elim', '(Elim) Reinstatement of kinds', 'claim', ['L540.s1', 'L540.s2'], r'\(Elim\)'),
    ('provit', '(Prov) Genesis', 'claim', ['L542.s1'], r'\(Prov\)'),
    ('qf', '(QF) Question-finding', 'claim', ['L544.s1'], r'\(QF\)'),
    # ---- the candidates that are not themselves one of the nodes above
    ('C546', 'A mathematical error (Part XV)', 'candidate', ['L546.s1'], r'mathematical error'),
    ('C441', 'Losses outside P must be exposed.', 'candidate', ['L441.s4'], r'\blosses\b'),
    ('C51', 'grievance 8: "Where is aesthetics?" In Part XI, as a declared appraisal relation.', 'candidate',
     ['L51.s1'], None),
]

# The seven: candidate unit -> the node that holds it
CANDIDATES = [
    ('L546.s1', 'C546'), ('L255.s1', 'noncirc'), ('L441.s4', 'C441'), ('L51.s1', 'C51'),
    ('L517.s1', 'theta'), ('L389.s1', 'K2'), ('L437.s1', 'P'),
]

SHORT = {
    'O': '(O) organization', 'Q': '(Q) query and answers', 'contract': 'the contract', 'grain': 'the grain',
    'idx_bcont': 'boundary and continuity (indices)', 'in_scope': 'the scope of a contract (declared input)',
    'in_aims': 'the aims O and P of a repair (declared input)', 'in_bcont': 'boundary and continuity of an attribution (declared input)',
    'in_assessor': 'the assessor\'s forms, scope and premises (declared input)', 'in_weight': 'a weighting of attribution (declared input)',
    'decl_list': 'the list of declared inputs', 'theta': 'the physical module Θ (import 1)', 'N': 'the appraisal relation 𝒩 (import 2)',
    'math': 'mathematics (used, not defined)', 'tentative': 'to tentatively accept', 'use_task': 'the declared use task U',
    'aims_q': 'the aims O_p of a question', 'question': 'a question as a whole', 'prov_c': 'provenance of a contract',
    'roles': 'roles', 'K': '(K) signatures and kinds', 'sigfam': 'families of signatures', 'occ': 'occurrence',
    'content': 'content', 'layers': 'object and simulation layers', 'transport': 'transport', 'fid': '(F1), (F2), (A) fidelity',
    'cand': 'explanatory candidate', 'noncirc': 'non-circular dependence', 'nonvac': 'non-vacuity', 'E': '(E) Account',
    'SBD': '(S), (B), (D) routes', 'prov': 'provenances of a transport', 'rep': '(R) representation',
    'psv': 'prediction, violation, surprise', 'hist': 'histories', 'aroute': 'active route', 'K1': '(K1) Bearing',
    'K2': '(K2) Usability', 'formj': 'Form_j', 'scopej': 'Scope_j', 'livej': 'Live_j', 'K3': '(K3)', 'arg': 'argument',
    'ruled': 'ruled out / not ruled out', 'rules_out': 'an argument rules out a claim', 'conflict': 'conflict', 'conflict_claim': 'conflict with a claim', 'rivals': 'rivals',
    'problem': 'a problem for p', 'etv': 'easy to vary', 'deploy': 'Deploy', 'tasks': 'tasks and possibility', 'CT1': '(CT1)',
    'CT2': '(CT2)', 'own': 'Ownership', 'can': 'owned capability', 'phys_results': 'achievement and tolerances', 'build': 'Build',
    'N_new': '(N) newness', 'G': '(G) origin', 'episode': 'episodes', 'P': '(P) Repair', 'prodby': 'ProducedBy',
    'EX': '(EX) created explanation', 'appraisal': 'the Appraisal paragraph', 'hist_index': 'historical index',
    'RCU': 'recursion, universality, membership', 'fmc': 'finite monotone claim', 'func': 'functional transport', 'T2': '(T2)',
    'I2': '(I2)', 'O1': '(O1)', 'failed': 'a failed answer stays failed', 'Arg1': 'Argument 1', 'Arg2': 'Argument 2',
    'Arg3': 'Argument 3', 'Arg4': 'Argument 4', 'Arg5': 'Argument 5', 'Arg6': 'Argument 6', 'Arg7': 'Argument 7',
    'Arg8': 'Argument 8', 'Arg9': 'Argument 9', 'Arg10': 'Argument 10', 'XV_frame': 'Part XV\'s opening',
    'XV_input_rule': 'Part XV\'s missing-input rule', 'suff': '(Suff)', 'nec': '(Nec)', 'elim': '(Elim)', 'provit': '(Prov)',
    'qf': '(QF)', 'C546': 'A mathematical error', 'C441': '"Losses outside P must be exposed."', 'C51': 'grievance 8\'s answer',
}
# ======================================================================================================
# The reading tables: the Part XIV edges (entered by hand, each tested against the words of the sentence it cites),
# the proposed edges dropped on reading, and the edges read from a definition that the scan missed
# ======================================================================================================

# (from, [to...], cited sentence, the clause as the order words it)
ORDER = [
    ('K', ['O', 'contract'], 'L526.s2', '(K) depends on (O) and a contract.'),
    ('fid', ['O', 'Q', 'K'], 'L526.s3', '(F1), (F2), (A) depend on (O), (Q), (K).'),
    ('E', ['fid'], 'L526.s4', '(E) depends on those.'),
    ('SBD', ['E'], 'L526.s5', '(S), (B), (D) depend on (E).'),
    ('rep', ['fid', 'prov'], 'L526.s6', '(R) depends on (F1)–(F2) and physical provenance.'),
    ('K1', ['E'], 'L526.s7', '(K1) depends on (E).'),
    ('K2', ['in_assessor'], 'L526.s8', '(K2) depends on the assessor\'s declared inputs (Part XIV, above)'),
    ('K3', ['K2'], 'L526.s8', '(K3) on (K2).'),
    ('deploy', ['rep', 'CT1'], 'L526.s9', 'Deploy depends on (R) and (CT1).'),
    ('own', ['hist', 'in_bcont'], 'L526.s10', 'Ownership depends on histories and a declared boundary'),
    ('can', ['own', 'CT1', 'in_bcont'], 'L526.s10', 'owned capability on Ownership, (CT1) and a declared continuity (Part XII)'),
    ('build', ['hist', 'own', 'E'], 'L526.s11', 'Build depends on histories, Ownership and (E).'),
    ('N_new', ['deploy', 'build'], 'L526.s12', '(N), (G) depend on Deploy and Build.'),
    ('G', ['deploy', 'build'], 'L526.s12', '(N), (G) depend on Deploy and Build.'),
    ('P', ['G', 'E', 'deploy', 'prodby', 'in_aims'], 'L526.s13',
     '(P), (EX) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared aims with their occasions'),
    ('EX', ['G', 'E', 'deploy', 'P'], 'L526.s13', '(P), (EX) depend on (G), (E), Deploy; ... (EX) also on (P)'),
    ('prodby', ['hist', 'aroute'], 'L526.s13', 'ProducedBy on histories and their active routes.'),
    ('conflict', ['fid', 'O'], 'L526.s15', 'In Part VI, conflict depends on (F1), (F2), (A) and the target\'s ports and components (Part II)'),
    ('conflict_claim', ['fid', 'O'], 'L526.s15', 'conflict with a claim on those and on the claim'),
    ('rivals', ['conflict'], 'L526.s15', 'rivals on conflict and on the offer of one in place of the other'),
    ('ruled', ['arg', 'K2', 'E'], 'L526.s15', 'being ruled out for an assessor on usable arguments (Part IX) and (E)'),
    ('problem', ['rivals', 'ruled'], 'L526.s15', 'a problem for \\(p\\) on rivals and on neither being ruled out'),
    ('etv', ['problem'], 'L526.s15', 'easy to vary on a problem for \\(p\\)'),
    ('roles', ['O'], 'L520.s2', 'Roles, from admitted edits (Part II).'),
    ('prov', ['hist', 'theta'], 'L520.s6', 'Provenance, from physical history (Parts IV, XII).'),
]
# (RC), (U1)-(U3) "depend on all of the above" (L526.s14): edges from RCU to every node the order names before it.
ORDER_ALL_ABOVE = ('RCU', 'L526.s14', '(RC), (U1)–(U3) depend on all of the above.',
                   ['O', 'Q', 'contract', 'grain', 'idx_bcont', 'in_scope', 'in_aims', 'in_bcont', 'in_assessor',
                    'in_weight', 'K', 'fid', 'E', 'SBD', 'rep', 'prov', 'K1', 'K2', 'K3', 'CT1', 'deploy', 'own',
                    'can', 'build', 'N_new', 'G', 'P', 'EX', 'prodby', 'hist', 'aroute'])

END_POINTS = ['O', 'Q', 'contract', 'grain', 'idx_bcont', 'in_scope', 'in_aims', 'in_bcont', 'in_assessor',
              'in_weight', 'theta', 'N', 'math', 'tentative', 'use_task', 'aims_q', 'decl_list']
WHY_END = {
    'O': 'an end point: "(O) and (Q) depend on nothing" (L526.s1)',
    'Q': 'an end point: "(O) and (Q) depend on nothing" (L526.s1)',
    'contract': 'a declared index, "stated, not defined" (L526.s1, L524.s1)',
    'grain': 'a declared index (L524.s1)', 'idx_bcont': 'declared indices (L524.s1)',
    'in_scope': 'a declared input (L522.s1, L524.s4)', 'in_aims': 'a declared input (L522.s1, L441.s1)',
    'in_bcont': 'a declared input (L522.s1, L524.s4)', 'in_assessor': 'a declared input (L522.s1)',
    'in_weight': 'a declared input (L522.s1)',
    'theta': 'an import (L515.s1, L520.s1); Argument 6 follows each definition back to the imports (L598.s2)',
    'N': 'an import, "taken as an input and the semantics does not define it" (L518.s1)',
    'tentative': 'defined as "a person\'s choice to go on with it" (L8.s6); nothing further in the text',
    'use_task': 'called "declared" (L403.s1, L453.s3, L497.s1) and not in the list of declared inputs',
    'aims_q': '"the set of aims being addressed or protected" (L147.s1); not defined further',
    'math': 'used and not defined by the text',
    'decl_list': 'the list itself',
}

# Proposed by the scan and dropped on reading: (from, to) -> reason code
R_END = 'end point: its wording names this, and the text makes it an end point (no edges out)'
R_SHARED = 'stray co-mention: the two share a sentence that states both'
R_FALSE = 'stray match of the word'
R_NAMES_NOT_USES = 'named to say what it is about or what it is not; not a condition of the definition'
R_QUESTION = 'the conditions read the target, contract and query of p (Part V), not the question as a whole (its aims O_p, its provenance ρ_p)'
R_REVERSE = 'the other depends on this one (the mention points the other way)'
R_VIA = 'reached through another edge of the same definition'
R_HOW = 'says how it is found, not what it is'
R_EPISODE = 'the episode named is Build\'s subhistory with its construction trace; the complete and creative critical episodes are not required'
R_INFORMAL = 'the word used in its ordinary sense, not as the defined term'
R_IMPORT_ITEM = 'Part XII spells out items of the import; the import is the end point'

DROP = {}
for f in END_POINTS:
    DROP[f] = R_END  # every proposed edge out of an end point
DROP.update({
    ('question', 'prov'): 'the provenance of the contract (ρ_p), not of a transport',
    ('prov_c', 'question'): 'part of the question tuple; the question depends on it',
    ('prov_c', 'hist'): 'the selection history of Part IV, reached through the provenances',
    ('prov_c', 'episode'): R_EPISODE,
    ('roles', 'K'): 'a gloss after "that is"; the observation is defined by the edit it admits',
    ('content', 'cand'): R_FALSE + ' ("contract-relative commitments" of a content, not a candidate\'s active commitments)',
    ('layers', 'psv'): R_INFORMAL + ' ("whose queries are predictions")',
    ('cand', 'question'): R_QUESTION,
    ('E', 'question'): R_QUESTION,
    ('K1', 'question'): R_QUESTION,
    ('rivals', 'question'): R_QUESTION,
    ('failed', 'question'): R_QUESTION,
    ('suff', 'question'): R_QUESTION,
    ('Arg2', 'question'): R_QUESTION,
    ('nonvac', 'E'): R_REVERSE + ' ("not a contract on which an account can be claimed")',
    ('SBD', 'hist'): R_NAMES_NOT_USES + ' ("not an active route of a history, Part IX")',
    ('SBD', 'aroute'): R_NAMES_NOT_USES + ' ("not an active route of a history, Part IX")',
    ('prov', 'cand'): R_FALSE + ' ("a population of candidate transports")',
    ('prov', 'episode'): R_EPISODE,
    ('psv', 'hist'): R_VIA + ' (the selection history H, through the provenances)',
    ('aroute', 'SBD'): R_FALSE + ' (an active route is meant, not a route of a candidate)',
    ('scopej', 'tentative'): R_SHARED, ('scopej', 'K2'): R_SHARED, ('scopej', 'livej'): R_SHARED,
    ('scopej', 'arg'): R_SHARED,
    ('livej', 'contract'): R_SHARED, ('livej', 'grain'): R_SHARED, ('livej', 'scopej'): R_SHARED,
    ('conflict', 'arg'): R_HOW + ' ("it is found by argument, with no test")',
    ('conflict_claim', 'conflict'): R_NAMES_NOT_USES + ' (a parallel: "as well as with a rival")',
    ('conflict_claim', 'rivals'): R_NAMES_NOT_USES + ' (a parallel: "as well as with a rival")',
    ('etv', 'K'): R_FALSE + ' ("of the second kind")',
    ('etv', 'E'): R_NAMES_NOT_USES + ' ("the term says nothing about which of them ... is an account")',
    ('etv', 'contract'): R_NAMES_NOT_USES + ' ("on a finer contract")',
    ('deploy', 'can'): 'Part XIV places it on (CT1); "retained capability" read as (CT1)\'s retained realization',
    ('tasks', 'phys_results'): R_IMPORT_ITEM + ' (tolerances)',
    ('own', 'contract'): R_FALSE + ' ("resource contract")',
    ('own', 'question'): R_FALSE + ' ("a decisive question" supplied from outside)',
    ('own', 'content'): R_NAMES_NOT_USES + ' ("Contribution of content and ownership of a process are different attributions")',
    ('own', 'can'): R_NAMES_NOT_USES + ' ("Ownership is not defined by the capability attributed through it")',
    ('own', 'build'): R_NAMES_NOT_USES + ' ("The subhistory in Build" names what is owned; the order places Build on Ownership)',
    ('can', 'contract'): R_FALSE + ' ("resource contract")',
    ('phys_results', 'hist'): R_FALSE + ' (the history of an execution)',
    ('phys_results', 'own'): R_VIA + ' (through owned capability)',
    ('episode', 'content'): R_NAMES_NOT_USES + ' ("a content-sensitive response")',
    ('episode', 'SBD'): R_FALSE + ' ("critical episode")',
    ('prodby', 'tasks'): R_FALSE + ' ("it attributes")',
    ('arg', 'rules_out'): 'a step "rules out the case in which its premises are met and its conclusion fails"; the ruling out of a claim is built on the argument, not the reverse',
    ('deploy', 'problem'): R_FALSE + ' ("problem-directed activity")',
    ('appraisal', 'O'): R_INFORMAL + ' ("an effect organization", a relation on actions, occasions and effects)',
    ('prodby', 'P'): R_NAMES_NOT_USES + ' ("runs from Δ to the repair" names the change attributed, not the predicate (P))',
    ('appraisal', 'in_aims'): R_NAMES_NOT_USES + ' ("says nothing about how anyone appraises the aim")',
    ('appraisal', 'question'): R_NAMES_NOT_USES + ' ("or the question that led to it")',
    ('appraisal', 'P'): R_NAMES_NOT_USES + ' ("Repairing an aim repairs it and says nothing about ...")',
    ('func', 'rep'): R_INFORMAL + ' ("a represented process", the model side)',
    ('T2', 'rep'): R_INFORMAL + ' ("a represented next-step process")',
    ('T2', 'in_scope'): 'a hypothesis of the bound ("every state z of a stated scope"), not the scope of a contract',
    ('Arg2', 'SBD'): R_NAMES_NOT_USES + ' (a contrast: "Part VI, redundant routes")',
    ('Arg2', 'Arg9'): R_NAMES_NOT_USES + ' (a contrast)',
    ('Arg2', 'Arg8'): R_NAMES_NOT_USES + ' (a contrast: "A coarsening is not a recoding")',
    ('Arg3', 'layers'): R_REVERSE + ' (its Consequence: "why the object layer is fallible")',
    ('Arg3', 'psv'): R_REVERSE + ' (its Consequence: "why surprise is possible")',
    ('Arg3', 'hist'): R_VIA + ' (the selection history H, through the provenances)',
    ('Arg4', 'K'): R_INFORMAL + ' ("the signature of a selected transport")',
    ('Arg4', 'hist'): R_VIA + ' (the selection history H, through the provenances)',
    ('Arg5', 'prov'): 'the provenance given to contracts is the contract\'s (ρ_p), added as such',
    ('Arg5', 'rep'): R_INFORMAL + ' ("cannot represent this", said of a semantics)',
    ('Arg5', 'appraisal'): R_NAMES_NOT_USES + ' ("says nothing about how anyone appraises it")',
    ('Arg6', 'question'): R_NAMES_NOT_USES + ' ("when a question requires it")',
    ('Arg6', 'rep'): R_NAMES_NOT_USES + ' (named among the predicates said not to be residual)',
    ('Arg6', 'EX'): R_NAMES_NOT_USES + ' ("(EX) is defined (Part XI)")',
    ('Arg6', 'appraisal'): R_NAMES_NOT_USES + ' ("a theory of appraisal")',
    ('XV_input_rule', 'appraisal'): 'the appraisal relation named is import 2, entered as such',
    ('provit', 'hist'): R_VIA + ' (the selection history, through the provenances)',
    ('RCU', 'question'): R_FALSE + ' ("coherently posed advanceable challenges")',
    ('C546', 'CT2'): 'entered as inferential (it names the claim)', ('C546', 'fmc'): 'entered as inferential (it names the claim)',
    ('C546', 'T2'): 'entered as inferential (it names the claim)', ('C546', 'I2'): 'entered as inferential (it names the claim)',
    ('C546', 'O1'): 'entered as inferential (it names the claim)', ('C546', 'Arg1'): 'entered as inferential (it names the claim)',
    ('C546', 'Arg2'): 'entered as inferential (it names the claim)', ('C546', 'Arg3'): 'entered as inferential (it names the claim)',
    ('C51', 'appraisal'): 'entered as inferential (it points to Part XI)',
})

# Read from a definition, not caught by the scan: (from, to, cited sentence, note)
ADD = [
    ('question', 'O', 'L141.s1', '"\\(D\\) is the target", an organization'),
    ('roles', 'sigfam', None, None),  # placeholder removed below
    ('fid', 'contract', 'L233.s1', '"every \\((a,b)\\in C\\)"; "faithful on \\(C\\)"'),
    ('noncirc', 'contract', 'L255.s4', '"There exist \\((a,b)\\in C\\)"'),
    ('E', 'contract', 'L265.s1', '"under the changes in \\(C\\)"'),
    ('SBD', 'O', 'L299.s3', '"a declared family \\(\\mathcal V\\) of organization edits"'),
    ('prov', 'contract', 'L195.s1', '"a finite history \\(H\\subseteq C\\)"'),
    ('aroute', 'contract', 'L375.s2', '"under the declared contrasts"'),
    ('formj', 'in_assessor', 'L393.s1', '"the inference form of \\(u\\) is one \\(j\\) admits"'),
    ('scopej', 'idx_bcont', 'L393.s2', '"within the contract, grain and boundary \\(j\\) has declared"'),
    ('scopej', 'in_assessor', 'L393.s2', '"the scope \\(j\\) declares" (L522.s1)'),
    ('livej', 'in_assessor', 'L393.s2', '"a premise \\(j\\) tentatively accepts ... and not withdrawn"'),
    ('conflict', 'contract', 'L315.s1', '"in \\(C\\) or outside it"'),
    ('CT2', 'CT1', 'L471.s1', '"states whose executions all complete and return into \\(C\\)"'),
    ('CT2', 'math', 'L471.s2', '"monotone", "greatest fixed point"'),
    ('deploy', 'CT1', 'L403.s1', '"as a retained capability (Part XII)", read as (CT1)\'s retained realization'),
    ('N_new', 'deploy', 'L413.s3', '"\\(R_{<e}(s,h)=\\bigcup_{\\xi\\text{ before }e}R_{\\beta,\\ell}(s,\\xi)\\)": the repertoire of Deploy'),
    ('N_new', 'content', 'L413.s1', '"transports from \\(d\\) to \\(c\\)", contents of a repertoire'),
    ('G', 'question', 'L419.s1', '"\\(c\\) is actually used to address \\(p\\)"'),
    ('G', 'content', 'L425.s1', '"The content \\(c\\) may be an organization, a transport, or a contract"'),
    ('EX', 'hist', 'L445.s1', '"\\(e_c\\preceq_h e\\)"'),
    ('EX', 'use_task', 'L453.s3', '"\\(U_c\\) is the declared use task for \\(c\\)"'),
    ('EX', 'question', 'L445.s1', '"\\(\\operatorname{Origin}_{\\beta,\\ell}(s,c,p_c,h,e_c)\\)": the question \\(p_c\\) of an origin'),
    ('EX', 'transport', 'L453.s3', '"\\(t_c\\) and \\(\\Gamma_c\\) are the transport and the identified commitments"'),
    ('appraisal', 'math', 'L455.s3', 'the sets \\(\\mathit{Act}\\), \\(\\mathit{Occ}\\), \\(\\mathit{Eff}\\) and the relation (AR)'),
    ('fmc', 'math', 'L305.s1', '"finite", "upward closed", minimal members'),
    ('func', 'math', 'L353.s2', 'composition of maps; induction'),
    ('T2', 'math', 'L363.s2', 'a metric, a Lipschitz constant, a sum'),
    ('I2', 'math', 'L329.s5', 'linear maps and kernels'),
    ('O1', 'math', 'L335.s1', 'relations, invariants, paths'),
    ('Arg3', 'contract', 'L572.s1', '"a finite history \\(H\\subsetneq C\\)"'),
    ('Arg5', 'prov_c', 'L592.s2', '"by giving contracts provenance"'),
    ('Arg5', 'N_new', 'L590.s5', '"Deploy, Build, and New apply"'),
    ('Arg6', 'contract', 'L596.s1', '"declared indices and declared inputs"'),
    ('Arg6', 'idx_bcont', 'L596.s1', '"declared indices"'),
    ('Arg6', 'in_scope', 'L596.s1', '"declared inputs"'), ('Arg6', 'in_aims', 'L596.s1', '"declared inputs"'),
    ('Arg6', 'in_bcont', 'L596.s1', '"declared inputs"'), ('Arg6', 'in_assessor', 'L596.s1', '"declared inputs"'),
    ('Arg6', 'in_weight', 'L596.s1', '"declared inputs"'),
    ('XV_input_rule', 'decl_list', 'L534.s3', '"one of the declared inputs Part XIV lists"'),
    ('qf', 'N_new', 'L544.s1', '"be new"'), ('qf', 'G', 'L544.s1', '"the originative contribution of an episode"'),
    ('C441', 'in_aims', 'L441.s1', '"a protected condition is lost exactly when it fails on an occasion it covers"'),
    ('C51', 'N', 'L51.s1', '"a declared appraisal relation"'),
]
ADD = [a for a in ADD if a[2] is not None]
ADD.append(('sigfam', 'roles', 'L123.s1', '"intervention on its output port"'))

# Inferential edges, read from the text: (from, to, cited sentence, how)
INFER = [
    ('C546', 'fmc', 'L546.s1', 'names the claim: a counterexample to it would rule the class out'),
    ('C546', 'I2', 'L546.s1', 'names the claim'), ('C546', 'O1', 'L546.s1', 'names the claim'),
    ('C546', 'T2', 'L546.s1', 'names the claim'), ('C546', 'CT2', 'L546.s1', 'names the claim'),
    ('C546', 'Arg1', 'L546.s1', 'names the argument'), ('C546', 'Arg2', 'L546.s1', 'names the argument'),
    ('C546', 'Arg3', 'L546.s1', 'names the argument'),
    ('C546', 'XV_frame', 'L534.s1', 'an item of the list Part XV opens with'),
    ('C51', 'appraisal', 'L51.s1', 'points to Part XI ("In Part XI") and restates it in short'),
    ('C441', 'P', 'L441.s4', 'a requirement placed in the paragraph on the aims of (P); what it asks of a repair claim is not said further'),
    ('in_scope', 'decl_list', 'L522.s1', 'named a declared input by the list'),
    ('in_aims', 'decl_list', 'L522.s1', 'named a declared input by the list'),
    ('in_bcont', 'decl_list', 'L522.s1', 'named a declared input by the list'),
    ('in_assessor', 'decl_list', 'L522.s1', 'named a declared input by the list'),
    ('in_weight', 'decl_list', 'L522.s1', 'named a declared input by the list'),
]

# Reverse mentions: patterns on the bare text of every unit, and the readings of stray matches.
REVERSE_PAT = {
    'C546': r'mathematical error|Part XV\b',
    'noncirc': r'[Nn]on-circular|NonCircular|assumes its own answer|its conclusion among its premises|\bp because p\b',
    'C441': r'\blosses\b|\bexpos',
    'C51': r'grievance 8|Where is aesthetics',
    'theta': r'physical module|Θ|\bOrg_',
    'K2': r'\(K2\)|\bUsable_|\busable\b|\b[Uu]sability\b|can use it|whoever can use',
    'P': r'\(P\)|\bRepair_|\brepair(s|ed|ing)?\b',
}
REVERSE_FALSE = {
    ('C441', 'L538.s2'): 'the exposed case of (Nec), not a loss',
    ('C441', 'L161.s3'): 'exposing the defect of a question, not a loss',
    ('P', 'L273.s2'): R_INFORMAL + ' ("does not repair this")',
    ('P', 'L309.s2'): R_INFORMAL + ' ("to repair this")',
    ('P', 'L405.s5'): R_FALSE, ('P', 'L159.s6'): R_FALSE,
}

# ======================================================================================================
# The program: inputs, the scan, the graph, the joins, the page and the JSON
# ======================================================================================================
import os, re, json, csv, hashlib
from collections import defaultdict, Counter

SEM = '/home/user/ThreadSmith/Semantics'
LED = SEM + '/results/S98 Ledger of edits and recommendations'
S100 = SEM + '/results/S100 Strong candidates and the most altered sections'
LATEST = SEM + '/tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md'
HERE = os.path.dirname(os.path.abspath(__file__))
NAME = 'S101 What the tested strong candidates depend on'
OUT_MD = os.path.join(HERE, NAME + '.md')
OUT_JSON = os.path.join(HERE, NAME + ' - graph.json')

INPUTS = {
    LATEST: 'ebca15a047f686b15d5f5766b69825c9',
    LED + '/group/sentence index of the latest text.jsonl': 'fdaf069a0c1d71be4e17b38d2f6bce82',
    LED + '/line-up/data/records.jsonl': '591a7cc8d07cc376dc324dd725a11579',
    S100 + '.md': 'db26b70bd5bc8985b8d93a9aa8b6ea19',
    S100 + ' - data.csv': 'aafca7e15b1515e58161da95227ac354',
}


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


for p, h in INPUTS.items():
    assert md5(p) == h, 'input changed: ' + p

UNITS = {}
ORDERED = []
for line in open(LED + '/group/sentence index of the latest text.jsonl', encoding='utf-8'):
    u = json.loads(line)
    UNITS[u['id']] = u
    ORDERED.append(u['id'])
DATA = {r['unit_id']: r for r in csv.DictReader(open(S100 + ' - data.csv', encoding='utf-8'))}
RECORDS = {}
for line in open(LED + '/line-up/data/records.jsonl', encoding='utf-8'):
    r = json.loads(line)
    RECORDS[r['rid']] = r
S100MD = open(S100 + '.md', encoding='utf-8').read()
# the latest text holds each unit's words where the index says
TEXT = open(LATEST, encoding='utf-8').read().split('\n')
for uid, u in UNITS.items():
    assert u['text'] in '\n'.join(TEXT[u['line'] - 1:u['line_end']]), uid

GREEK = {r'\ell': 'ℓ', r'\Theta': 'Θ', r'\Gamma': 'Γ', r'\rho': 'ρ', r'\tau': 'τ', r'\sigma': 'σ',
         r'\lambda': 'λ', r'\pi': 'π', r'\beta': 'β', r'\Omega': 'Ω', r'\xi': 'ξ', r'\Delta': 'Δ',
         r'\equiv': '≡', r'\mu': 'μ', r'\chi': 'χ', r'\delta': 'δ'}


def bare(t):
    """The unit's words with markup set aside, for the pattern scan."""
    t = t.replace('**', '')
    t = re.sub(r'\\tag\{([^}]*)\}', r'(\1)', t)
    t = re.sub(r'\\operatorname\{([^}]*)\}', r' \1', t)
    t = re.sub(r'\\mathcal\s*\{?([A-Za-z])\}?', r'cal\1', t)
    t = re.sub(r'\\mathsf\{([A-Za-z]+)\}', r'sf\1', t)
    t = re.sub(r'\\mathrm\{([A-Za-z]+)\}', r'\1', t)
    for k, v in sorted(GREEK.items(), key=lambda kv: -len(kv[0])):
        t = t.replace(k, v)
    t = re.sub(r'\\[()\[\]]', ' ', t)
    t = re.sub(r'\\[A-Za-z]+', ' ', t)
    return t.replace('*', '')


NODE = {}
for nid, label, kind, units, pat in NODES:
    for u in units:
        assert u in UNITS, (nid, u)
    NODE[nid] = {'id': nid, 'label': label, 'kind': kind, 'units': units,
                 'pat': re.compile(pat) if pat else None}
CAND_NODE = dict(CANDIDATES)
for u, n in CANDIDATES:
    assert u in NODE[n]['units']

# ---- 1. the scan: in each node's defining sentences, every other node's words
PROPOSED = []
MATCHED_IN = {}
for nid, n in NODE.items():
    for u in n['units']:
        txt = bare(UNITS[u]['text'])
        hits = [m for m, o in NODE.items() if m != nid and o['pat'] and o['pat'].search(txt)]
        for a, b in re.findall(r'Arguments? (\d+)(?:\s*[–-]\s*(\d+))?', txt):
            for k in range(int(a), int(b or a) + 1):
                if 'Arg%d' % k != nid:
                    hits.append('Arg%d' % k)
        for m in hits:
            if (nid, m) not in MATCHED_IN:
                MATCHED_IN[(nid, m)] = u
                PROPOSED.append((nid, m))

# ---- 2. the edges
EDGES = []  # dicts: from, to, kind, source, cite, note


def add_edge(f, t, kind, source, cite, note):
    for e in EDGES:
        if e['from'] == f and e['to'] == t and e['kind'] == kind:
            if source == 'Part XIV order' and e['source'] != 'Part XIV order':
                e['note'] = (e['note'] + '; ' if e['note'] else '') + 'also in the wording of the definition'
                e['source'], e['cite'] = source, cite
            return
    EDGES.append({'from': f, 'to': t, 'kind': kind, 'source': source, 'cite': cite, 'note': note})


for f, tos, cite, clause in ORDER:
    assert all(part.strip(' .') in UNITS[cite]['text'] for part in clause.split('...')), (cite, clause)
    for t in tos:
        add_edge(f, t, 'definitional', 'Part XIV order', cite, 'the order: "%s"' % clause)
rcu, rcite, rclause, rtos = ORDER_ALL_ABOVE
assert rclause in UNITS[rcite]['text']
for t in rtos:
    add_edge(rcu, t, 'definitional', 'Part XIV order', rcite, 'the order: "%s"' % rclause)

DROPPED = []
KEPT_READ = []
for f, t in PROPOSED:
    if f in END_POINTS:
        DROPPED.append((f, t, R_END))
        continue
    if (f, t) in DROP:
        DROPPED.append((f, t, DROP[(f, t)]))
        continue
    KEPT_READ.append((f, t))
    add_edge(f, t, 'definitional', 'read from the definition', MATCHED_IN[(f, t)],
             'the wording of its defining sentence uses it')
for f, t, cite, note in ADD:
    assert cite in UNITS, cite
    add_edge(f, t, 'definitional', 'read from the definition', cite, 'added on reading: ' + note)
for f, t, cite, how in INFER:
    assert cite in UNITS, cite
    add_edge(f, t, 'inferential', 'read from the text', cite, how)
for k in DROP:
    assert isinstance(k, str) or k in PROPOSED, ('a drop that the scan never proposed', k)
for e in EDGES:
    assert e['from'] in NODE and e['to'] in NODE, e
    assert not (e['from'] in END_POINTS and e['kind'] == 'definitional'), e

OUT = defaultdict(list)
INN = defaultdict(list)
for e in EDGES:
    OUT[e['from']].append(e)
    INN[e['to']].append(e)


def closure(start, kinds=('definitional', 'inferential'), direction='out'):
    seen, stack = set(), [start]
    while stack:
        x = stack.pop()
        for e in (OUT[x] if direction == 'out' else INN[x]):
            if e['kind'] in kinds:
                y = e['to'] if direction == 'out' else e['from']
                if y not in seen and y != start:
                    seen.add(y)
                    stack.append(y)
    return seen


def depth_paths(start, kinds=('definitional', 'inferential')):
    """Shortest path from start to every node it reaches (breadth first), for the tables."""
    prev, order, frontier = {start: None}, [], [start]
    while frontier:
        nxt = []
        for x in frontier:
            for e in sorted(OUT[x], key=lambda e: e['to']):
                if e['kind'] in kinds and e['to'] not in prev:
                    prev[e['to']] = x
                    order.append(e['to'])
                    nxt.append(e['to'])
        frontier = nxt
    return prev, order


def path_to(prev, x):
    p = [x]
    while prev[p[-1]] is not None:
        p.append(prev[p[-1]])
    return list(reversed(p))


# strongly connected components of the definitional edges (Tarjan)
def sccs(kinds=('definitional',)):
    index, low, onstack, stack, out, counter = {}, {}, set(), [], [], [0]

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        onstack.add(v)
        for e in OUT[v]:
            if e['kind'] not in kinds:
                continue
            w = e['to']
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.discard(w)
                comp.append(w)
                if w == v:
                    break
            out.append(comp)
    import sys
    sys.setrecursionlimit(10000)
    for v in NODE:
        if v not in index:
            strong(v)
    return [sorted(c) for c in out if len(c) > 1]


LOOPS = sccs()

# ---- 3. stability, from S100's per-unit data
sec_rows = re.search(r'### 4\.1 .*?\n\n(\|.*?)\n\n', S100MD, re.S).group(1).split('\n')[2:]
MOST_ALTERED_SECTIONS = []
for row in sec_rows[:10]:
    cells = [c.strip() for c in row.strip('|').split('|')]
    m = re.search(r'\((?:line|lines) (\d+)(?:–(\d+))?\)$', cells[1])
    MOST_ALTERED_SECTIONS.append(('sec-L%s-%s' % (m.group(1), m.group(2) or m.group(1)), cells[1], cells[4]))
unit_rows = re.search(r'### 4\.4 .*?\n\n(\|.*?)\n\n', S100MD, re.S).group(1).split('\n')[2:]
TOP15 = [[c.strip() for c in r.strip('|').split('|')][1] for r in unit_rows]
MA_SEC = {s for s, _, _ in MOST_ALTERED_SECTIONS}
for s in MA_SEC:
    assert any(r['section_id'] == s for r in DATA.values()), s
ELIG = [r for r in DATA.values() if r['kind'] != 'heading' and r['is_dated_note'] == 'no']
SUBST_DIST = Counter(int(r['substantive_changes']) for r in ELIG)
MOVED_AT = 3
SHARE_MOVED_UNITS = sum(v for k, v in SUBST_DIST.items() if k >= MOVED_AT) / len(ELIG)


def unit_info(u):
    d = DATA[u]
    return {'id': u, 'text': UNITS[u]['text'], 'section': d['section'], 'section_id': d['section_id'],
            'first_version': d['first_version'], 'versions_carried': int(d['versions_carried']),
            'criticism_driven': int(d['criticism_driven_changes']), 'owner_directed': int(d['owner_directed_changes']),
            'vocabulary_only': int(d['vocabulary_only_changes']), 'replaced_wordings': int(d['replaced_wordings']),
            'substantive': int(d['substantive_changes']), 'wordings_held': int(d['wordings_held']),
            'untouched_in_substance': d['untouched_in_substance'] == 'yes',
            'strong_candidate_list': d['strong_candidate_list'],
            'in_most_altered_section': d['section_id'] in MA_SEC, 'among_15_most_changed': u in TOP15}


def node_stability(nid, skip=()):
    us = [unit_info(u) for u in NODE[nid]['units'] if u not in skip]
    if not us:
        return {'class': 'no sentence of its own', 'units': [], 'max_subst': -1, 'crit': 0, 'strong': [],
                'most_altered_section': False, 'untouched': 0, 'n': 0, 'subst': 0, 'max_unit': None, 'max_wordings': 0}
    mx = max(us, key=lambda x: (x['substantive'], x['criticism_driven']))
    moved = mx['substantive'] >= MOVED_AT or any(x['in_most_altered_section'] for x in us)
    held = all(x['substantive'] == 0 for x in us)
    cls = 'held' if held else ('moved a lot' if moved else 'changed a little')
    if held and min(x['versions_carried'] for x in us) < 10:
        cls = 'held (younger than file 10)'
    return {'class': cls, 'units': us, 'max_subst': mx['substantive'], 'max_unit': mx['id'],
            'max_wordings': mx['wordings_held'], 'crit': sum(x['criticism_driven'] for x in us),
            'subst': sum(x['substantive'] for x in us),
            'untouched': sum(1 for x in us if x['untouched_in_substance']), 'n': len(us),
            'min_versions': min(x['versions_carried'] for x in us),
            'most_altered_section': any(x['in_most_altered_section'] for x in us),
            'strong': [x['id'] for x in us if x['strong_candidate_list']]}


STAB = {n: node_stability(n) for n in NODE}
CAND_UNITS = {u for u, _ in CANDIDATES}

# ---- 4. per candidate
RESULT = {}
for u, n in CANDIDATES:
    fwd_def = closure(n, ('definitional',))
    fwd_all = closure(n)
    rev_def = closure(n, ('definitional',), 'in')
    rev_all = closure(n, ('definitional', 'inferential'), 'in')
    prev, order = depth_paths(n)
    own_rest = node_stability(n, skip=(u,))
    on_path = sorted(fwd_all, key=lambda x: (-STAB[x]['max_subst'], -STAB[x]['crit'], x))
    ranked = [x for x in on_path if STAB[x]['units']]
    most = ranked[0] if ranked else None
    most_def = next((x for x in ranked if x != 'decl_list'), None)
    RESULT[u] = {'node': n, 'fwd_def': fwd_def, 'fwd_all': fwd_all, 'rev_def': rev_def, 'rev_all': rev_all,
                 'prev': prev, 'order': order, 'own_rest': own_rest, 'most': most, 'most_def': most_def}

# reverse mentions
MENTIONS = {}
for u, n in CANDIDATES:
    key = n if n in REVERSE_PAT else u
    rx = re.compile(REVERSE_PAT[n])
    rows = []
    for uid in ORDERED:
        if uid in NODE[n]['units'] or UNITS[uid]['kind'] == 'heading' or DATA[uid]['is_dated_note'] == 'yes':
            continue
        if rx.search(bare(UNITS[uid]['text'])):
            if (n, uid) in REVERSE_FALSE:
                rows.append((uid, 'stray match', REVERSE_FALSE[(n, uid)]))
                continue
            holders = [m for m, o in NODE.items() if uid in o['units']]
            through = [m for m in holders if m in RESULT[u]['rev_all']]
            if n == 'C546' and not re.search(r'mathematical error', UNITS[uid]['text']):
                rows.append((uid, 'points to Part XV, of which it is an item', ''))
            elif through:
                rows.append((uid, 'inside a definition that depends on it', ', '.join(SHORT[x] for x in through)))
            else:
                rows.append((uid, 'uses it by name', ('in ' + ', '.join(SHORT[x] for x in holders)) if holders else ''))
    MENTIONS[u] = rows

# ---- 5. shared core
COUNT = Counter()
for u, n in CANDIDATES:
    for x in RESULT[u]['fwd_all'] | {n}:
        COUNT[x] += 1
CORE = sorted([x for x, c in COUNT.items() if c >= 4], key=lambda x: (-COUNT[x], x))

# ---- 6. values
VAL_SETS = {
    'the appraisal relation (import 2)': {'N'},
    'the Appraisal paragraph of Part XI': {'appraisal'},
    'Part XI\'s repair definitions': {'P', 'prodby', 'C441'},
    'Part XI\'s created-explanation definition': {'EX'},
    'the part of Part XV that names the appraisal relation': {'XV_input_rule'},
}
AIMS = {'in_aims', 'aims_q'}


def values_of(nodeset):
    return {k: sorted(v & nodeset) for k, v in VAL_SETS.items() if v & nodeset}


# ---- 7. the order against the wording
ORDER_PAIRS = {(e['from'], e['to']) for e in EDGES if e['source'] == 'Part XIV order'}
READ_PAIRS = {(e['from'], e['to']) for e in EDGES if e['source'] == 'read from the definition'}
WORDED = set(KEPT_READ) | {(f, t) for f, t, _, _ in ADD}
ORDER_NOT_WORDED = sorted(p for p in ORDER_PAIRS if p not in WORDED and p[0] != 'RCU')
ORDER_NAMED = {f for f, _, _, _ in ORDER} | {t for _, ts, _, _ in ORDER for t in ts} | set(ORDER_ALL_ABOVE[3]) | {'RCU'}
UNPLACED = [x for x in NODE if NODE[x]['kind'] == 'defined' and x not in ORDER_NAMED]
ORDER_OUT = defaultdict(set)
for f, t in ORDER_PAIRS:
    ORDER_OUT[f].add(t)


def order_reach(f, t):
    seen, stack = set(), [f]
    while stack:
        x = stack.pop()
        for y in ORDER_OUT[x]:
            if y == t:
                return True
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return False


# wording-only paths: edges read from definitions and inferential edges, the order's edges left out
WORD_OUT = defaultdict(set)
for e in EDGES:
    if e['source'] != 'Part XIV order' or (e['from'], e['to']) in WORDED:
        WORD_OUT[e['from']].add(e['to'])


def word_closure(start):
    seen, stack = set(), [start]
    while stack:
        x = stack.pop()
        for y in WORD_OUT[x]:
            if y not in seen and y != start:
                seen.add(y)
                stack.append(y)
    return seen


for u, n in CANDIDATES:
    RESULT[u]['fwd_word'] = word_closure(n)
    wr = sorted([x for x in RESULT[u]['fwd_word'] if STAB[x]['units'] and x != 'decl_list'],
                key=lambda x: (-STAB[x]['max_subst'], -STAB[x]['crit'], x))
    RESULT[u]['most_def_word'] = wr[0] if wr else None
COUNT_WORD = Counter()
for u, n in CANDIDATES:
    for x in RESULT[u]['fwd_word'] | {n}:
        COUNT_WORD[x] += 1
CORE_WORD = sorted([x for x, c in COUNT_WORD.items() if c >= 4], key=lambda x: (-COUNT_WORD[x], x))

# ---- 8. what S100 says each candidate came through
def s100_block(u):
    m = re.search(r'\n\*\*%s\*\* · (.*?)\n(.*?)(?=\n\*\*L\d+\.s\d+\*\* · |\n### 3\.2)' % re.escape(u), S100MD, re.S)
    head, body = m.group(1), m.group(2)
    since = re.search(r'\n- (In the text since [^\n]*)', body).group(1).rstrip('.')
    changes = re.search(r'\n- ((?:Allowed changes|Changes): [^\n]*)', body).group(1).split('; the ledger')[0].rstrip('.') + '.'
    props = re.findall(r'\n  - ([A-Z]+-\d+) · ([^·]+) · (\w+) · ([^·]+) ·[^\n]*\n((?:    > [^\n]*\n?)+)', body)
    out = []
    for rid, rnd, kind, outcome, wording in props:
        assert rid in RECORDS
        out.append({'rid': rid, 'round': rnd.strip(), 'kind': kind, 'outcome': outcome.strip(),
                    'wording': '\n'.join(l[4:] for l in wording.rstrip('\n').split('\n'))})
    return head, since, changes, out


# ---- 9. when each declared input entered the list (from S100's run of wordings of L522.s1)
blk = re.search(r'#### 3\. L522\.s1 .*?(?=\n#### 4\.)', S100MD, re.S).group(0)
blk = blk.split('- Proposed and replaced')[0]
L522_WORDINGS = re.findall(r'\n- ([^\n]+):\n  > ([^\n]+)', blk)
ITEM_KEY = {'in_aims': 'of a repair, with the occasions each covers', 'in_scope': 'the scope of a contract',
            'in_bcont': 'the system boundary and continuity of an attribution', 'in_assessor': 'for an assessor',
            'in_weight': 'a weighting of'}
ITEM_SINCE = {}
for k, key in ITEM_KEY.items():
    ITEM_SINCE[k] = next(lbl for lbl, txt in L522_WORDINGS if key in txt)

# ---- 10. the order against the wording, edge by edge
READ_ONLY_OUT = defaultdict(set)
for f, t in WORDED:
    READ_ONLY_OUT[f].add(t)


def read_reach(f, t):
    seen, stack = set(), [f]
    while stack:
        x = stack.pop()
        for y in READ_ONLY_OUT[x]:
            if y == t:
                return True
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return False


ORDER_CHECK = []
for f, tos, cite, clause in ORDER:
    for t in tos:
        if (f, t) in WORDED:
            st = 'in the wording'
        elif read_reach(f, t):
            st = 'reached through the wording of other definitions'
        else:
            st = 'not in the wording'
        ORDER_CHECK.append((f, t, cite, st))
READ_NOT_ORDER = sorted((f, t) for f, t in WORDED if (f, t) not in ORDER_PAIRS
                        and NODE[f]['kind'] in ('defined',) and (f, t) not in {(a, b) for a, b, _, _ in INFER})
# of those, the ones whose target the order places, but not after the source
READ_AGAINST_ORDER = [(f, t) for f, t in READ_NOT_ORDER if f in ORDER_NAMED and t in ORDER_NAMED
                      and NODE[t]['kind'] == 'defined' and not order_reach(f, t)]


# ======================================================================================================
# The notes read by hand from the paths (numbers taken from the computation above)
# ======================================================================================================
N_USERS = sorted({e['from'] for e in INN['N']})


def _n(u):
    return len(RESULT[u]['fwd_all'])


def _r(u):
    return len(RESULT[u]['rev_all'])


def _names(u):
    return sum(1 for m in MENTIONS[u] if m[1] != 'stray match')


assert {'T2', 'Arg2', 'Arg3'} <= {x for x in RESULT['L546.s1']['fwd_all'] if STAB[x]['class'] == 'moved a lot'}
assert {'O1', 'CT2'} <= {x for x in RESULT['L546.s1']['fwd_all'] if STAB[x]['class'] == 'held'}
assert 'E' not in RESULT['L437.s1']['fwd_word'] and 'E' in RESULT['L437.s1']['fwd_all']
assert not any(values_of(closure(x)) for x in CORE)
assert set(N_USERS) == {'Arg6', 'C51', 'XV_input_rule', 'appraisal'}
assert not any('EX' in RESULT[u]['fwd_all'] for u, _ in CANDIDATES) and 'EX' in RESULT['L437.s1']['rev_all']
assert {'suff', 'nec', 'elim', 'provit'} <= RESULT['L389.s1']['rev_all']
assert ITEM_SINCE['in_assessor'].startswith('the S96 stage-1')
O_P_USES = [u for u in ORDERED if 'O_p' in UNITS[u]['text']]
assert O_P_USES == ['L137.s1', 'L147.s1'], O_P_USES

NOTES = [
    '- **L546.s1, A mathematical error.** Its own wording depends on nothing but the eight claims it names, so its path is theirs. Three of the eight moved a lot: (T2) (L363.s2, 5 substantive changes), Argument 2 (L568.s1, 3) and Argument 3 (L572.s2, 4). Log S88 records why: "(F1) Derivation 2\'s claim that two faithful candidates\' "components are pairwise of one kind on \\(C\\)" is false under its stated assumptions, shown by two counter-instances, so Part XV\'s own defeat entry ("A mathematical error ... under their stated assumptions") is triggered, in both files word for word"; S88 found the like of file 10\'s Derivation 3 (its F4) and hypotheses left out of (T2) (its F2). The claims were rewritten; this sentence was not. Two of the eight held, (O1) and (CT2), whose second sentence (L471.s2) is itself a never-challenged strong candidate. No node depends on it. Four sentences point to Part XV as a whole (L17.s4, L47.s3, L61.s1, L339.s4); the short list in "Where to attack this" names the five other items and not this one, and ends "Anything else is a detail." (L61.s2–s3).',
    '- **L255.s1, non-circular dependence.** The sentence heads a definition whose later sentences moved: L255.s3 (since draft 1, 3 substantive changes) and L255.s4 (since draft 2, 5), after S88\'s third finding, "(F3) The set \\(\\Gamma\\) of active commitments in non-circular dependence is never typed" (log S88); the explanatory candidate\'s definition moved with it (L231.s2, since draft 2). Its path is short (%d nodes) and ends in (O), (Q), the contract and the grain; the scope of a contract and the list of declared inputs come onto it only through transport\'s "on the stated scope" (L189.s1). It has the most dependants of the seven, %d nodes, because (E) depends on it and most of the theory depends on (E); %d sentences use it by name, among them "\\"\\(p\\) because \\(p\\)\\" fails non-circular dependence." (L273.s1), (Suff) (L536.s2) and the paragraph "A premise that is the denial" (L397.s14–s16), which reads a premise "structurally as non-circular dependence reads identity".' % (
        _n('L255.s1'), _r('L255.s1'), _names('L255.s1')),
    '- **L441.s4, "Losses outside \\(P\\) must be exposed."** No other sentence of the text uses it or its words, and "exposed" is defined nowhere: the text does not say who exposes the losses or to whom. The declined proposal E-16 would have said "A repair claim exposes its losses outside \\(P\\)." Its own terms are the protected aims \\(P\\), a declared input, and "losses", read from L441.s1 ("a protected condition is lost exactly when it fails on an occasion it covers"). The rest of its path is that of (P), beside which it stands: %d nodes by the order, %d by the wording alone.' % (
        _n('L441.s4'), len(RESULT['L441.s4']['fwd_word'])),
    '- **L51.s1, grievance 8\'s answer.** A pointer. It depends on the Appraisal paragraph (L455) and on import 2 (L518.s1), and both moved: import 2 grew from file 10\'s "The **normative relation** \\(\\mathcal N\\), when a question invokes one." (quoted in S100) to add "It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance." Its word "declared" is not Part XIV\'s word for \\(\\mathcal N\\), which is an import "taken as an input" (L518.s1) and is named apart from the declared inputs (L522.s2); the proposal it came through, C-143 (S90, not applied), said so: "L51 still calls the normative relation "declared"; no entry changes it". The sentence held while what it points to changed. No node depends on it; the front matter "states nothing the body does not state more exactly" (L35.s1).',
    '- **L517.s1, the physical module.** An end point: the text takes it from outside (import 1) and defines nothing it holds. %d nodes depend on it, through occurrences ("a physically located carrier", L169.s1), histories ("a physical interpretation", L375.s1), the provenances ("Provenance, from physical history", L520.s6), (R) (\\(\\operatorname{Org}_\\ell\\), L207.s1, and "The one thing (R) takes from outside", L213.s1), tasks and (CT1), owned capability and Deploy. Three other candidates reach it: A mathematical error through Argument 3 ("a transport the physics and the stated construction admit", L572.s3), and (P) and "Losses outside \\(P\\)" through histories and the provenances. The declined proposal E-26 would have added "It is the physics adopted, and is itself conjectural: a verdict that turns on what it admits is given with it." Part XII spells out what the module holds; its "Tasks" sentences changed a little or came in with the repaired copy (L461.s4–s6).' % _r('L517.s1'),
    '- **L389.s1, (K2).** The formula has been in the text since file 10 (one word swapped, \\(\\operatorname{Lic}_j\\) to \\(\\operatorname{Form}_j\\)), and its three predicates were defined only in the last three versions, each marked as Claude\'s reading: "\\(\\operatorname{Form}_j(u)\\): the inference form of \\(u\\) is one \\(j\\) admits [Claude\'s reading; draft 5 names this predicate and does not define it]." (L393.s1, since the scrubbed copy), and Scope_j and Live_j (L393.s2, since the repaired copy). The proposal it came through, C-181 (S93, not applied), asked to "define (K2)\'s Lic_j, Scope_j and Live_j". The assessor\'s inputs entered the list of declared inputs in %s, and the order\'s sentence that places (K2) (L526.s8) is as young (since the repaired copy). So its end points are the newest part of its path. %d nodes depend on it (%s), among them four of Part XV\'s items, each stated as what "an argument ... rules out"; %d sentences use it by name or by "whoever can use it".' % (
        'the S96 repair (26 September; first in its stage-1 text)', _r('L389.s1'), ', '.join(SHORT[x] for x in sorted(RESULT['L389.s1']['rev_all'])), _names('L389.s1')),
    '- **L437.s1, (P).** The formula held; the sentences that say what its letters are moved: the aims as declared inputs (L441.s1, since file 11, 3 criticism-driven changes), the contribution \\(\\Delta\\) (L435.s1, since draft 1), ProducedBy (L441.s5, since file 11) and the reading of \\(r(\\xi\')\\) (L441.s2, since draft 1). Its path has %d nodes by the order and %d by its wording alone: the order places (P) after (G), (E) and Deploy (L526.s13), while (P)\'s words use only the aims, the contribution \\(\\Delta\\) (a subhistory) and ProducedBy. By its words alone it does not reach (E), and the text says "An account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions." (L441.s6). %d nodes depend on it: %s.' % (
        _n('L437.s1'), len(RESULT['L437.s1']['fwd_word']), _r('L437.s1'), ', '.join(SHORT[x] for x in sorted(RESULT['L437.s1']['rev_all']))),
]

CORE_NOTES = [
    'The core falls in two. The structural end points held or changed once: (O) (all 13 sentences untouched), transport (3 of 3), the physical module (untouched), and the contract, the grain, boundary and continuity, and the query, each with one change (L524.s1, L141.s3). The definitions in the core moved a lot: the explanatory candidate (L231.s1, one wording and 6 substantive changes from proposals written against it; L231.s2, since draft 2), non-circular dependence (L255.s3–s4), the scope of a contract (L159.s1, 4 wordings), and the list of declared inputs (L522.s1, 5 wordings, from 57 to 111 words by S100\'s count).',
    '',
    'Two of the seven stand apart from the core\'s main line: grievance 8\'s answer reaches only the appraisal relation and the Appraisal paragraph, and (K2) reaches the contract, the grain and boundary and continuity through Scope_j, and the list of declared inputs through the assessor\'s inputs, and nothing of Part V. The physical module is itself in the core, as an end point three others reach.',
]

VALUE_NOTES = [
    'What the definitions and the order show, and no more:',
    '',
    '1. **The appraisal relation is used by four nodes of the graph:** %s. No definition of Parts II–XIII other than the Appraisal paragraph uses it. The dependence order (L526) does not name it; the list of imports does, "when a question invokes an appraisal" (L518.s1), and Argument 6\'s claim has "and, where invoked, \\(\\mathcal N\\)" (L596.s1).' % ', '.join(SHORT[x] for x in N_USERS),
    '2. **One of the seven depends on it directly:** grievance 8\'s answer, which points to where the text takes it as an input. None reaches it through a path.',
    '3. **Two of the seven are Part XI\'s repair sentences:** (P) and "Losses outside \\(P\\) must be exposed." Their paths reach the declared aims \\(O\\) and \\(P\\) and, through (G) and the question, the aims \\(O_p\\) of a question; they do not reach the appraisal relation. The text says of the aims: "Their declaration makes no appraisal of the aims, and (P) puts no order on alternatives." (L441.s3); and of a repair: "Repairing an aim repairs it and says nothing about how anyone appraises the aim, or the question that led to it." (L455.s1). Created explanation (EX) is on no candidate\'s path; it depends on (P) and is among what depends on it.',
    '4. **The aims \\(O_p\\) of a question** stand in the question itself, \\(p=(D,\\ C,\\ b_0,\\ \\mathcal Q,\\ O_p,\\ \\rho_p)\\), glossed "\\(O_p\\) is the set of aims being addressed or protected." (L147.s1); no other sentence of the text uses \\(O_p\\).',
    '5. **Four of the seven reach no values node and no aims:** A mathematical error, non-circular dependence, the physical module and (K2). No node of the shared core has a values node or an aim on its path.',
    '6. **Part XV\'s opening names the appraisal relation beside the declared inputs:** "A case whose assessment turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the appraisal relation, is a case with a missing input, not an argument that rules a claim out." (L534.s3). The rule governs how a case against any item is read; the claims that "A mathematical error" names use no appraisal.',
    '7. **The text on its two imports:** "The two imports are a theory of matter and, when a question requires it, a theory of appraisal." and "Neither is a predicate about explanation." (L600.s2–s3).',
    '',
    'This bears on the owner\'s question whether values belong inside the theory or beside it. It does not answer it.',
]

ORDER_NOTES = [
    '- **Placed by the order, not in the wording** (%d of the order\'s %d edges; %d more reached only through other definitions). (P) after (G), (E) and Deploy (L526.s13): (P)\'s formula uses the aims, \\(\\Delta\\) and ProducedBy. (N) after Build (L526.s12): its formula uses the repertoire of Deploy and \\(\\equiv_\\ell\\), and reaches Build only through other definitions. (F1), (F2), (A) after (K) (L526.s3): their wording uses no signature, and the text\'s own link runs from (F1) to signatures ("By (K), no component of \\(E\\) whose signature on \\(C\\) differs from its counterpart\'s meets (F1)", L245.s4; Argument 1). Build after (E) (L526.s11): the nearest wording is "prepares a represented organization for explanatory use of \\(c\\)" (L405.s1).' % (sum(1 for x in ORDER_CHECK if x[3] == 'not in the wording'), len(ORDER_CHECK), sum(1 for x in ORDER_CHECK if x[3].startswith('reached'))),
    '- **Loops read from the wording.** {Build, provenances, (R)}: (R) depends on the provenances (the order); a constructed transport needs an episode "whose construction trace prepares \\(t\\), and in which \\(t\\), or the organization it carries to, is available as a represented target" (L197.s1), and Build asks for "a represented organization" (L405.s1). Whether this is a loop or a recursion that ends in selected transports, the text does not say; the order says "The order has no cycle and no endless descent." (L526.s17), and "A representation defined only by its own construction ... has not supplied its place in the order" (L526.s18). {(K2), argument, Live_j}: a premise is live for \\(j\\) when it is "the conclusion of a step of the same argument as \\(u\\) that is usable by \\(j\\)" (L393.s2), and an argument is usable "when each of its steps is (K2)" (L397.s4): a recursion over the steps of one argument tree, whose leaves are premises (L397.s2). Of the seven, (K2) is in the second loop; (P), "Losses outside \\(P\\)" and A mathematical error reach the first, and none is in it.',
    '- **Called declared, not in the list of declared inputs.** The declared use task \\(U\\) (L403.s1, L453.s3, L497.s1), on the paths of (P) and "Losses outside \\(P\\)" through Deploy; "the declared contrasts" of an active route (L375.s2); "a declared restriction operation" (L287.s1) and "a declared family \\(\\mathcal V\\) of organization edits" (L299.s3); and "a declared appraisal" (L25.s1) and "a declared appraisal relation" (L51.s1), for what Part XIV makes an import.',
]

UNSURE = [
    '- **Edges read from definitions are a reading.** The scan proposes; a reading keeps, drops or adds (Appendix B). Another reader could drop or add some. One rule of reading changes the graph most: that a definition naming "question \\(p\\)" reads its target, contract and query and not the whole question (§1.2). Without it, every such definition would reach the provenance of contracts, and through Build nearly the whole text.',
    '- **The order and the wording disagree in places** (§5). Both kinds of edge are in the graph; a path through an edge of the order that is not in the wording (such as (P) to (E)) is the order\'s placement, not what the definition\'s words use. The counts "by the wording alone" show the difference.',
    '- **"Moved a lot" is S100\'s measure.** It counts on a sentence the proposals and replaced wordings written against it: the explanatory candidate\'s first sentence (L231.s1) and "A kind is an equivalence class of components under this relation." (L119.s2) have one wording each and six substantive changes. The tables give the wordings held beside the count.',
    '- **Seven is a small number.** The shared core, "on the paths of at least four", is a stated line; at three, %d more nodes come in.' % len([x for x, c in COUNT.items() if c == 3]),
    '- **Untouched may mean unexamined.** Nodes with no changes, such as (O) and transport, may never have been read closely; the 29 never-challenged strong candidates are not traced here.',
    '- **Words the paths pass through that the text leaves undefined** are not nodes: "exposed" (L441.s4), "counterexample" and "stated assumptions" (L546.s1), the states \\(\\xi,\\xi\'\\) of (P), "problem-directed activity" (Deploy), "event" (a record leaf), "the offer of one in place of the other" (rivals).',
    '- **The sentences that name a candidate are found by words.** A sentence that uses a candidate\'s idea without its words is missed; one that names it without depending on it is listed as naming it.',
    '- **The ledger\'s tree** (`line-up/data/tree.json`) was not needed: sections come from S100\'s per-unit data, and the proposal ids S100 lists were matched to the ledger\'s records.',
]
# ======================================================================================================
# 11. The page
# ======================================================================================================
L = []
w = L.append


def short(n):
    return SHORT[n]


def cls_cell(n):
    s = STAB[n]
    if not s['units']:
        return 'no sentence of its own'
    bits = [s['class']]
    if s['max_subst'] > 0:
        bits.append('most in %s (%d substantive, %d wording%s)' % (s['max_unit'], s['max_subst'], s['max_wordings'],
                                                                  '' if s['max_wordings'] == 1 else 's'))
    return '; '.join(bits)


def flags(n):
    f = []
    k = NODE[n]['kind']
    if k.startswith('end point'):
        f.append(k.replace('end point: ', 'end point, ').replace('end point read from the definition', 'end point read from the definition'))
    if k == 'list':
        f.append('the list of declared inputs')
    if STAB[n]['strong']:
        f.append('holds strong candidate%s %s' % ('s' if len(STAB[n]['strong']) > 1 else '', ', '.join(STAB[n]['strong'])))
    if STAB[n]['most_altered_section']:
        f.append('in one of the ten most-altered sections')
    for kk, v in VAL_SETS.items():
        if n in v:
            f.append('values: ' + kk)
    if n in AIMS:
        f.append('aims')
    return '; '.join(f)


def quote(u):
    t = UNITS[u]['text']
    return '\n'.join('> ' + l for l in t.split('\n'))


def unit_line(u):
    i = unit_info(u)
    return '%s (%s; since %s, %d of 10 versions; criticism-driven %d, substantive %d, wordings %d%s%s)' % (
        u, i['section'], i['first_version'], i['versions_carried'], i['criticism_driven'], i['substantive'],
        i['wordings_held'], '; strong candidate, ' + i['strong_candidate_list'] if i['strong_candidate_list'] else '',
        '; in a most-altered section' if i['in_most_altered_section'] else '')


n_nodes = len(NODE)
n_def_edges = sum(1 for e in EDGES if e['kind'] == 'definitional')
n_order = sum(1 for e in EDGES if e['source'] == 'Part XIV order')
n_read = sum(1 for e in EDGES if e['source'] == 'read from the definition')
n_inf = sum(1 for e in EDGES if e['kind'] == 'inferential')
n_prop, n_drop = len(PROPOSED), len(DROPPED)
n_prop_nonend = sum(1 for f, t in PROPOSED if f not in END_POINTS)
n_reentered = sum(1 for f, t, r in DROPPED if r.startswith('entered as inferential'))
n_drop_nonend = sum(1 for f, t, r in DROPPED if f not in END_POINTS) - n_reentered
n_add = len(ADD)
core_vals = {x: values_of(closure(x)) for x in CORE}

w('# S101 — What the tested strong candidates depend on')
w('')
w('*Log S101, 27 September 2026, under decision S32. Made by program (`%s - script.py`) from the latest text (`tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md`), the S98 ledger\'s sentence index and records, and S100\'s page and per-unit data; nothing in them was changed. One agent (decision S22). Sentences are quoted byte for byte. The graph is beside this page as JSON (`%s - graph.json`).*' % (NAME, NAME))
w('')
w('## What was asked')
w('')
w('The owner, 27 September 2026, answering Claude\'s proposal "trace what the 7 tested strong candidates depend on, the other ideas each one relies on. That\'s your \'see what else they depend on\', and it\'s the firmest place to start": "Do it". Earlier (decision S31) the aim: to "isolate the strong candidates, See what else they depend on and maybe even figure out, for example, whether values should be part of the theory, or separate."')
w('')
w('The seven are S100\'s strong candidates that were challenged and kept: each has been in all ten versions with no change in substance, its neighbours changed more than those of three sentences in four, and a proposal was made against it and not taken.')
w('')

# ---------------- In short
w('## In short')
w('')
w('- **The graph:** %d nodes (the defined terms and symbols of the latest text, the claims and Arguments the seven name or that name them, and the end points the text declares) and %d edges: %d definitional edges placed by Part XIV\'s dependence order, %d read from the wording of a definition, and %d inferential edges read from the text. A program proposed %d edges from the words of each definition; on reading, %d of the %d proposed out of sentences that are not end points were dropped (stray matches, words named to say what a definition is not, mentions that point the other way; Appendix B), %d were entered as inferential edges instead, and %d edges the program missed were added, each with the sentence it is read from.' % (
    n_nodes, len(EDGES), n_order, n_read, n_inf, n_prop, n_drop_nonend, n_prop_nonend, n_reentered, n_add))
for u, n in CANDIDATES:
    R = RESULT[u]
    s = STAB
    nodes_path = [x for x in sorted(R["fwd_all"]) if STAB[x]["units"]]
    held = sum(1 for x in nodes_path if STAB[x]['class'].startswith('held'))
    moved = [x for x in nodes_path if STAB[x]['class'] == 'moved a lot']
    most = R['most']
    if not R['fwd_all']:
        w('- **%s** (%s): an end point of the text, an import; it depends on nothing, and %d nodes depend on it.' % (u, short(n), len(R['rev_all'])))
        continue
    md = R['most_def']
    w(('- **%s** (%s): depends on %d nodes (%d end points; %d by the wording alone, the order\'s edges left out); of the %d with sentences of their own, %d held, %d moved a lot. Most altered on its path: %s (%s, %d substantive changes)%s. %d nodes depend on it.' % (
        u, short(n), len(R['fwd_all']),
        sum(1 for x in R['fwd_all'] if NODE[x]['kind'].startswith('end point')), len(R['fwd_word']), len(nodes_path), held, len(moved),
        short(most), STAB[most]['max_unit'], STAB[most]['max_subst'],
        ('' if md == most else '; the most altered definition: %s (%s, %d)' % (short(md), STAB[md]['max_unit'], STAB[md]['max_subst'])),
        len(R['rev_all']))).replace('. 0 nodes depend on it.', '. No node depends on it.'))
w('- **The shared core** (nodes on the paths of at least four of the seven, the candidate\'s own node counted): %s.' % '; '.join('%s (%d of 7)' % (short(x), COUNT[x]) for x in CORE))
w('- **Values:** %s. No node of the shared core depends on the appraisal relation, on the Appraisal paragraph, or on Part XI\'s repair or created-explanation definitions. In the whole graph the appraisal relation is used by %s only.' % (
    '; '.join('%s: %s' % (u, ', '.join('%s (%s)' % (k, ', '.join(short(x) for x in v)) for k, v in values_of(RESULT[u]['fwd_all'] | {RESULT[u]['node']}).items()) or 'none') for u, _ in CANDIDATES),
    ', '.join(short(x) for x in N_USERS)))
w('- **Loops read from the wording** (not from the order): %s. Part XIV says "The order has no cycle and no endless descent." (L526.s17)' % '; '.join('{' + ', '.join(short(x) for x in c) + '}' for c in LOOPS))
w('')

# ---------------- 1. Method
w('## 1. How the graph was made')
w('')
w('### 1.1 Nodes')
w('')
w('A node is a defined term or symbol of the latest text, with the sentences that define it (units of the S98 sentence index; a displayed formula is one unit), or a claim or Argument, or an end point. The end points are those the text declares: (O) and (Q), which "depend on nothing"; the declared indices (grain, boundary, continuity, the contract), and the declared inputs, "which are stated, not defined" (L526.s1); and the two imports (L515.s1–L518.s1). Four more end points are read from the definitions, because the text defines them no further: mathematics used and not defined; "to tentatively accept" (L8.s6, "a person\'s choice to go on with it"); the declared use task \\(U\\) of Deploy, which the text calls declared (L403.s1, L453.s3, L497.s1) and does not list among the declared inputs; and the aims \\(O_p\\) of a question (L147.s1). The list of declared inputs (L522.s1–s2) is a node of its own: each declared input is joined to it by an inferential edge ("named a declared input by the list"), so that the list\'s changes show on a path without being counted as changes of the input it names.')
w('')
w('Where a candidate is one sentence of a longer definition (non-circular dependence, (K2), (P), import 1), the candidate is that definition\'s node, and the other sentences of the definition are reported apart as "the rest of its own definition".')
w('')
w('### 1.2 Edges')
w('')
w('- **Part XIV order:** every clause of the dependence order (L526.s2–s15) and of "Everything else is defined in terms of ..." (L520.s2, L520.s6), entered by hand as (from, to) pairs, each tested by the program against the words of the sentence it cites. "(RC), (U1)–(U3) depend on all of the above" (L526.s14) gives an edge from that node to every node the order names before it.')
w('- **Read from the definition:** the program looks, in each node\'s defining sentences (markup set aside), for the words and symbols of every other node, and proposes an edge for each match. Every proposal was then read: proposals out of an end point are dropped, as the text makes end points depend on nothing; the others are kept unless the reading table drops them with a reason (a stray match of the word; a word named to say what a definition is about or is not; the mention points the other way; reached through another edge). Edges the scan missed were added, each with its sentence. Appendix B lists every dropped proposal and every added edge.')
w('- **One rule of reading, stated because it changes the graph:** a candidate is "for question \\(p\\)", and \\(p=(D,C,b_0,\\mathcal Q,O_p,\\rho_p)\\) carries aims and a provenance. The conditions of (E) read the target, the contract (with its baseline) and the query of \\(p\\), and never its aims \\(O_p\\) or its provenance \\(\\rho_p\\); so an edge goes to the question as a whole only where a definition turns on it as a whole (the provenance of a contract, (G)\'s "used to address \\(p\\)", (EX)\'s \\(p_c\\), question-finding). Read the other way, every definition that names a question would reach the provenances, and through them nearly everything.')
w('- **Inferential:** read from the text: the claims and Arguments a candidate names or restates, the Part it points to, the list it is an item of. For what depends on each candidate, the program also lists every sentence whose words name it (§2), and marks those inside a definition that depends on it through the graph.')
w('')
w('### 1.3 Stability')
w('')
w('Each node\'s sentences are joined to S100\'s per-unit data (`S100 ... - data.csv`): versions carried (of ten), criticism-driven changes, substantive changes (criticism-driven + owner-directed + replaced wordings other than vocabulary), and wordings held. A node **held** when every sentence of it has no substantive change; it **moved a lot** when one of its sentences has %d or more substantive changes (%.0f%% of the 694 units S100 counts; the upper tenth begins there) or stands in one of S100\'s ten most-altered sections (its §4.1); otherwise it **changed a little**. S100 counts on a sentence the proposals and replaced wordings that were written against it, so a sentence can carry many substantive changes and one wording throughout (L231.s1 and L119.s2 do); the tables give the wordings held beside the count. "Most altered on the path" orders the nodes on a path by the largest substantive count of any one sentence, then by criticism-driven changes.' % (MOVED_AT, 100 * SHARE_MOVED_UNITS))
w('')
w('The ten most-altered sections (S100 §4.1): %s.' % '; '.join('%s (%s per unit)' % (nm, r) for _, nm, r in MOST_ALTERED_SECTIONS))
w('')

# ---------------- 2. The seven
w('## 2. The seven, one by one')
w('')
for i, (u, n) in enumerate(CANDIDATES, 1):
    R = RESULT[u]
    head, since, changes, props = s100_block(u)
    w('### 2.%d %s' % (i, u))
    w('')
    w(quote(u))
    w('')
    w('- **Where:** %s.' % head)
    w('- **What it came through (S100):** %s. %s' % (since.replace('In the text since', 'in the text since'), changes))
    for p in props:
        w('  - %s · %s · %s · %s, proposing:' % (p['rid'], p['round'], p['kind'], p['outcome']))
        w('\n'.join('    > ' + l[2:] if l.startswith('> ') else '    > ' + l for l in p['wording'].split('\n')))
    own = R['own_rest']
    if own['units']:
        w('- **The rest of its own definition:** %s.' % '; '.join(unit_line(x['id']) for x in own['units']))
    w('')
    # definitional table
    if R['fwd_all']:
        w('**What it depends on** (%d nodes; the path shown is one shortest path; D = definitional, I = inferential):' % len(R['fwd_all']))
        w('')
    if R['fwd_all']:
        w('| node | how it is reached | last edge | stability | sentences held / all | criticism-driven | marks |')
        w('| --- | --- | --- | --- | ---: | ---: | --- |')
        for x in R['order']:
            p = path_to(R['prev'], x)
            last = [e for e in OUT[p[-2]] if e['to'] == x]
            le = sorted(last, key=lambda e: e['kind'])[0]
            s = STAB[x]
            w('| %s | %s | %s, %s (%s) | %s | %s | %s | %s |' % (
                short(x), ' → '.join(p), 'D' if le['kind'] == 'definitional' else 'I', le['source'], le['cite'],
                cls_cell(x), ('%d / %d' % (s['untouched'], s['n'])) if s['units'] else '–',
                s['crit'] if s['units'] else '–', flags(x)))
        w('')
    else:
        w('Nothing: it is an end point of the text, an import (L515.s1, L520.s1).')
        w('')
    nodes_path = [x for x in sorted(R["fwd_all"]) if STAB[x]["units"]]
    moved = sorted([x for x in nodes_path if STAB[x]['class'] == 'moved a lot'], key=lambda x: (-STAB[x]['max_subst'], x))
    held = [x for x in nodes_path if STAB[x]['class'].startswith('held')]
    most = R['most']
    most_def = R['most_def']
    if nodes_path:
        w('**Stability of the path:** of %d nodes with sentences of their own, %d held, %d changed a little, %d moved a lot%s. Most altered on the path: **%s** (%s, %d substantive changes, %d wordings). Most altered definition on the path, the list of declared inputs left aside: **%s** (%s, %d substantive changes, %d wording%s).' % (
            len(nodes_path), len(held), len(nodes_path) - len(held) - len(moved), len(moved),
            (' (' + ', '.join(short(x) for x in moved) + ')') if moved else '',
            short(most), STAB[most]['max_unit'], STAB[most]['max_subst'], STAB[most]['max_wordings'],
            short(most_def), STAB[most_def]['max_unit'], STAB[most_def]['max_subst'], STAB[most_def]['max_wordings'],
            '' if STAB[most_def]['max_wordings'] == 1 else 's'))
        mw = R['most_def_word']
        if mw != most_def:
            w('')
            w('By the wording alone (%d nodes, the order\'s edges left out), the most altered definition on the path is **%s** (%s, %d substantive changes); %s is reached only through the order.' % (
                len(R['fwd_word']), short(mw), STAB[mw]['max_unit'], STAB[mw]['max_subst'], short(most_def)))
        w('')
    # reverse
    rev = sorted(R['rev_all'], key=lambda x: (NODE[x]['kind'], x))
    if rev:
        w('**What depends on it** (%d nodes: what would be exposed if it were ruled out):' % len(rev))
        w('')
        w(', '.join('%s%s' % (short(x), ' [moved a lot]' if STAB[x]['class'] == 'moved a lot' else '') for x in rev) + '.')
    else:
        w('**What depends on it:** no node of the graph.')
    w('')
    ms = MENTIONS[u]
    real = [m for m in ms if m[1] != 'stray match']
    w('**Sentences whose words name it** (%d, %d of them stray matches set aside): %s' % (
        len(ms), len(ms) - len(real),
        '; '.join('%s (%s%s)' % (uid, kind, (': ' + via) if via and kind != 'stray match' else '') for uid, kind, via in real) if real else 'none.'))
    w('')
    vals = values_of(R['fwd_all'] | {n})
    aims = sorted(AIMS & (R['fwd_all'] | {n}))
    w('**Values:** %s%s' % (
        ('; '.join('%s: %s' % (k, ', '.join(short(x) for x in v)) for k, v in vals.items()) if vals else 'no path reaches the appraisal relation, the Appraisal paragraph, or Part XI\'s repair or created-explanation definitions'),
        ('. Aims on its path: %s.' % ', '.join(short(x) for x in aims)) if aims else '.'))
    w('')

# per-candidate notes read by hand
w('### 2.8 Read from the paths, candidate by candidate')
w('')
for line in NOTES:
    w(line)
w('')

# ---------------- 3. Shared core
w('## 3. The shared core')
w('')
w('How many of the seven have each node on their path (the candidate\'s own node counted). Nodes on the paths of at least four:')
w('')
w('| node | of 7 | which | stability | sentences held / all | marks |')
w('| --- | ---: | --- | --- | ---: | --- |')
for x in CORE:
    which = [u for u, n in CANDIDATES if x in RESULT[u]['fwd_all'] or x == n]
    s = STAB[x]
    w('| %s | %d | %s | %s | %s | %s |' % (short(x), COUNT[x], ', '.join(which), cls_cell(x),
                                           ('%d / %d' % (s['untouched'], s['n'])) if s['units'] else '–', flags(x)))
w('')
three = sorted([x for x, c in COUNT.items() if c == 3], key=lambda x: x)
w('On the paths of three: %s.' % ', '.join(short(x) for x in three))
w('')
w('By the wording alone (the order\'s edges left out), the nodes on the paths of at least four are: %s.' % '; '.join('%s (%d of 7)' % (short(x), COUNT_WORD[x]) for x in CORE_WORD))
w('')
w('The core as one graph (edges among core nodes only; D definitional, I inferential):')
w('')
w('```mermaid')
w('graph TD')
ALIAS = {x: x for x in CORE}
for x in CORE:
    lab = short(x).replace('"', "'")
    if len(lab) > 60:
        lab = lab[:57] + '...'
    w('  %s["%s — %d of 7"]' % (x, lab, COUNT[x]))
for e in EDGES:
    if e['from'] in CORE and e['to'] in CORE:
        w('  %s -->|%s| %s' % (e['from'], 'D' if e['kind'] == 'definitional' else 'I', e['to']))
w('```')
w('')
w('Values in the core: %s' % ('none of the core nodes has the appraisal relation, the Appraisal paragraph, or a repair or created-explanation definition on its own path.' if not any(core_vals.values()) else str(core_vals)))
w('')
for line in CORE_NOTES:
    w(line)
w('')

# ---------------- 4. Values
w('## 4. Values: what the definitions and the order show')
w('')
w('| candidate | appraisal relation (import 2) | Appraisal paragraph (Part XI) | repair definitions (Part XI) | created explanation (Part XI) | aims on the path |')
w('| --- | --- | --- | --- | --- | --- |')
for u, n in CANDIDATES:
    R = RESULT[u]
    reach = R['fwd_all'] | {n}
    direct = {e['to'] for e in OUT[n]} | {n}

    def cell(ids):
        hit = ids & reach
        if not hit:
            return 'no'
        return ', '.join(('%s (%s)' % (short(h), 'itself' if h == n else ('direct' if h in direct else 'through its path'))) for h in sorted(hit))
    w('| %s | %s | %s | %s | %s | %s |' % (u, cell({'N'}), cell({'appraisal'}), cell({'P', 'prodby', 'C441'}), cell({'EX'}),
                                            ', '.join(short(a) for a in sorted(AIMS & reach)) or 'none'))
w('')
for line in VALUE_NOTES:
    w(line)
w('')

# ---------------- 5. Order and wording
w('## 5. The order and the wording')
w('')
w('Each edge of Part XIV\'s order, against the wording of the definition it starts from:')
w('')
w('| from | to | cited | against the wording |')
w('| --- | --- | --- | --- |')
for f, t, cite, st in ORDER_CHECK:
    w('| %s | %s | %s | %s |' % (short(f), short(t), cite, st))
w('')
w('Edges read from the wording of a definition that the order does not state: %d. Most of them go to nodes the order does not place at all (%d defined nodes: %s). Of those whose two ends the order does place, these go to a defined node the order does not put before the one that uses it (%d): %s.' % (
    len(READ_NOT_ORDER), len(UNPLACED), ', '.join(short(x) for x in UNPLACED), len(READ_AGAINST_ORDER),
    '; '.join('%s → %s' % (short(f), short(t)) for f, t in READ_AGAINST_ORDER)))
w('')
for line in ORDER_NOTES:
    w(line)
w('')
w('When each item entered the list of declared inputs (L522.s1), from S100\'s run of its wordings:')
w('')
for k in ['in_aims', 'in_scope', 'in_bcont', 'in_weight', 'in_assessor']:
    w('- %s: first in "%s".' % (short(k), ITEM_SINCE[k]))
w('')

# ---------------- 6. Unsure
w('## 6. What is unsure')
w('')
for line in UNSURE:
    w(line)
w('')
w('## 7. Files and rerun')
w('')
w('- This page; the graph, `%s - graph.json` (nodes with their sentences, kinds, marks and S100 data; edges with kind, source and the sentence cited; the proposals dropped; the sentences that name each candidate); the script, `%s - script.py`.' % (NAME, NAME))
w('- Inputs, read only, each tested against its md5 by the script: %s.' % '; '.join('`%s` (%s)' % (os.path.relpath(p, SEM), h) for p, h in INPUTS.items()))
w('- Rerun from `results/`: `PYTHONDONTWRITEBYTECODE=1 python3 "%s - script.py"` (a few seconds); a rerun gives the same bytes.' % NAME)
w('')

# ---------------- Appendix A: nodes
w('## Appendix A. Every node, with its sentences')
w('')
for nid in NODE:
    n = NODE[nid]
    w('- **%s** `%s` · %s · %s%s' % (n['label'], nid, n['kind'], cls_cell(nid),
                                     (' · ' + WHY_END[nid]) if nid in WHY_END else ''))
    for u in n['units']:
        w('  - ' + unit_line(u))
w('')
w('## Appendix B. The reading table')
w('')
w('Proposals dropped or re-entered (%d: %d out of end points, which the text makes depend on nothing; %d entered as inferential edges; %d dropped on reading):' % (n_drop, n_drop - n_drop_nonend - n_reentered, n_reentered, n_drop_nonend))
w('')
w('| from | to | matched in | why dropped |')
w('| --- | --- | --- | --- |')
for f, t, r in DROPPED:
    if f in END_POINTS:
        continue
    w('| %s | %s | %s | %s |' % (f, t, MATCHED_IN[(f, t)], r))
w('')
w('Out of end points: %s.' % '; '.join('%s → %s' % (f, t) for f, t, r in DROPPED if f in END_POINTS))
w('')
w('Edges added on reading (%d):' % len(ADD))
w('')
w('| from | to | sentence | what is read |')
w('| --- | --- | --- | --- |')
for f, t, cite, note in ADD:
    w('| %s | %s | %s | %s |' % (f, t, cite, note))
w('')

page = '\n'.join(L).rstrip('\n') + '\n'
open(OUT_MD, 'w', encoding='utf-8').write(page)

# ---------------- JSON
J = {'about': {'log': 'S101', 'date': '2026-09-27', 'decision': 'S32',
               'inputs': {os.path.relpath(p, SEM): h for p, h in INPUTS.items()},
               'stability_rule': {'held': 'every sentence has 0 substantive changes',
                                  'moved a lot': 'a sentence with %d or more substantive changes, or in one of S100\'s ten most-altered sections' % MOVED_AT,
                                  'changed a little': 'otherwise'},
               'most_altered_sections': [s for s, _, _ in MOST_ALTERED_SECTIONS]},
     'candidates': [], 'nodes': [], 'edges': EDGES, 'dropped_proposals': [
         {'from': f, 'to': t, 'why': r} for f, t, r in DROPPED], 'loops_read_from_the_wording': LOOPS,
     'shared_core': [{'node': x, 'of_7': COUNT[x]} for x in CORE]}
for u, n in CANDIDATES:
    R = RESULT[u]
    J['candidates'].append({'unit': u, 'node': n, 'text': UNITS[u]['text'], 'depends_on': sorted(R['fwd_all']),
                            'depends_on_definitional_only': sorted(R['fwd_def']),
                            'depended_on_by': sorted(R['rev_all']),
                            'most_altered_on_path': R['most'], 'most_altered_definition_on_path': R['most_def'],
                            'values_on_path': values_of(R['fwd_all'] | {n}),
                            'aims_on_path': sorted(AIMS & (R['fwd_all'] | {n})),
                            'sentences_naming_it': [{'unit': a, 'reading': b, 'via': c} for a, b, c in MENTIONS[u]]})
for nid, n in NODE.items():
    s = STAB[nid]
    J['nodes'].append({'id': nid, 'short': SHORT[nid], 'label': n['label'], 'kind': n['kind'],
                       'end_point': n['kind'].startswith('end point'), 'declared_input': n['kind'] == 'end point: declared input',
                       'declared_index': n['kind'] == 'end point: declared index', 'import': n['kind'] == 'end point: import',
                       'strong_candidate_sentences': s['strong'], 'in_most_altered_section': s['most_altered_section'],
                       'values_node': any(nid in v for v in VAL_SETS.values()),
                       'candidate_unit': next((u for u, m in CANDIDATES if m == nid), None),
                       'stability': s['class'], 'marks': flags(nid), 'on_paths_of': COUNT.get(nid, 0),
                       'sentences': s['units']})
open(OUT_JSON, 'w', encoding='utf-8').write(json.dumps(J, ensure_ascii=False, indent=1) + '\n')
print('written', OUT_MD, OUT_JSON)
