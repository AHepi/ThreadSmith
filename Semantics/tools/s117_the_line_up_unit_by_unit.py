#!/usr/bin/env python3
"""s117_the_line_up_unit_by_unit.py

What it does, in plain words: for log S117, this file holds the line-up itself, written by hand: the fifteen groups of
the semantics in plain names, the Avida things they are lined up with, and, for every one of the 284 units of the
semantics (the formal core's definitions and encodings, the formal claims after round 4, and the text's named terms),
its group, its verdict, its Avida counterpart (or none), a plain sentence on why, the evidence, and the alternatives
considered. Units that share one reason share one "profile" below; a unit can add its own note. It also holds the main
breaks (what does not work, and why) and the reverse list (what Avida shows that the semantics has no term for). It
computes nothing and writes nothing; s117_build_the_results_and_the_map.py reads it.

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""

EXACT, PART, NOT, NONE = 'LINES UP EXACTLY', 'LINES UP IN PART', 'DOES NOT LINE UP', 'NOTHING IN AVIDA'
VERDICTS = [EXACT, PART, NOT, NONE]
PLAIN_VERDICT = {
    EXACT: 'lines up exactly',
    PART: 'lines up in part',
    NOT: 'does not line up',
    NONE: 'nothing in Avida',
}

# ---- the Avida side ------------------------------------------------------------------------------------------------
AVIDA = [
    ('AV01', 'An Avida program, run alone or in the world',
     'One instruction sequence running on Avida\'s simulated computer; its observed computational behaviour (copying, tasks).'),
    ('AV02', 'Instruction ablation',
     'One instruction swapped for nop-X, an instruction that does nothing, and the program run again.'),
    ('AV03', 'Instruction changes when a program copies itself',
     'Copying mistakes, and the one-in-twenty added or removed instruction at each split.'),
    ('AV04', 'The tasks, the rewards, and the code that checks them',
     'The Avida execution environment\'s list of tasks and what each pays, written in a file in advance, and Avida\'s code that checks whether an output does a task.'),
    ('AV05', 'The numbers handed in, always in one order',
     'The three numbers a program is handed, which the world always hands out in the same order.'),
    ('AV06', 'Changes to the world\'s own rules',
     'What an instruction means changed (nand read as nor or and), the input channel removed, meanings shuffled.'),
    ('AV07', 'The program population and computational selection',
     'Many programs copying themselves into a grid of 3,600 places; the ones that copy faster spread (Avida fitness).'),
    ('AV08', 'Program ancestry',
     'The line of parent and descendant programs, thousands of generations long.'),
    ('AV09', 'The circuits read from Avida\'s records',
     'The small wiring diagrams read from Avida\'s step-by-step records: the routes from the numbers handed in to the number handed out.'),
    ('AV10', 'Required and removable instructions',
     'Which single instructions, pairs or triples had to be ablated for a task to stop while the copying went on.'),
    ('AV11', 'The six execution environments over time',
     'Which environments made the program population do more tasks, and where the count stopped.'),
    ('AV12', 'Programs alike now, unlike after a change',
     'Programs that do the same today and become different things after the same change.'),
    ('AV13', 'The giving choice',
     'Programs that give some of their running time to a neighbour or not, depending on a number the neighbour sends (S115 reply 2, S116).'),
    ('AV14', 'The people studying Avida',
     'The owner\'s questions, Claude\'s plans written before running, the runs, the checks and their corrections. Not Avida itself.'),
    ('AV00', 'Nothing in Avida',
     'Nothing in Avida, or in the Avida work, plays this part.'),
]

# ---- the semantics' side: the fifteen groups --------------------------------------------------------------------------
GROUPS = [
    ('G01', 'What the semantics takes from outside',
     'The frame: a theory of the physical world and of appraisal, taken as given, and the indices every claim is relative to.'),
    ('G02', 'Things, their parts and their changes',
     'Anything studied is a set of parts, each a constraint on some values, with a list of changes it admits.'),
    ('G03', 'Questions and the changes they ask about',
     'A question names a target, the changes it asks about, and what it asks; where the question came from is recorded.'),
    ('G04', 'Telling parts apart by how they respond',
     'Two parts are the same kind when every change the question admits affects them alike; nothing else makes a kind.'),
    ('G05', 'The test of an explanation',
     'Something counts as an account of a question when its parts match the target\'s parts, its answers match under every change, and the answers depend on its parts.'),
    ('G06', 'Which parts do the work',
     'Which parts, alone or together, an account cannot lose; and parts that do no work.'),
    ('G07', 'Rivals, problems and tests',
     'Two answers offered for one question that clash, that nobody can yet decide between, and the tests that can decide.'),
    ('G08', 'Arguments, criticism and use',
     'Reasons that rule things out for someone who can use them; criticism that has a target; premises taken as given.'),
    ('G09', 'Where a correspondence came from',
     'Every correspondence has a history: selected (variation and survival), constructed (worked out with a target in view), or only declared.'),
    ('G10', 'Standing for something; prediction and surprise',
     'A thing stands for something when a faithful correspondence with that history links them; prediction and surprise follow.'),
    ('G11', 'Making something new',
     'Building a new content inside the system, new against what it could already use, and used on a problem.'),
    ('G12', 'Repair and created explanation',
     'A repair of a stated aim, produced by a contribution; created explanation is a repair through a new account.'),
    ('G13', 'Keeping a capability; the physical side',
     'Tasks, keeping the ability to do them, owning that ability within a declared boundary, and the limits physics sets.'),
    ('G14', 'Going on without limit, and the whole structure',
     'Turning on one\'s own practice, universality, the classes, the commitments, and what would rule the semantics out.'),
    ('G15', 'The text\'s own worked examples',
     'The pole and its shadow, the balances, the tokens, the matrices, the two-layer episode and other worked cases.'),
]

# ---- profiles: one reason shared by several units -------------------------------------------------------------------
# Each: verdict, Avida counterpart id, plain why (one sentence, for every verdict but LINES UP EXACTLY it is the "why"),
# evidence (computed or argued, with the source), alternatives considered, and whether it turns on a reading.
P = {}


def prof(key, verdict, avida, why, evidence, alternatives='', reading=False, people=False):
    P[key] = dict(verdict=verdict, avida=avida, why=why, evidence=evidence, alternatives=alternatives,
                  turns_on_a_reading=reading, also_lines_up_with_the_people_studying_avida=people)


# G01
prof('frame', PART, 'AV06',
     'Every slot of the frame can be filled for Avida (its rules as the physics, the indices set in each plan), but Avida\'s "physics" is a program written by people and known exactly, not a fallible theory of the physical world.',
     'Argued: Avida\'s rules were checked line by line against its code (S114), which the semantics\' physical module never allows of physics (L53, L481).',
     'Taking the real computer\'s physics as the module: then Avida\'s programs are patterns in memory and every Avida claim is about a simulation, one grain up.')
prof('primitives', PART, 'AV05',
     'Some primitives the formal core adds have Avida counterparts (which changes actually occurred: the numbers the world handed in), others have none (an offer of one answer in place of another; a claim being used).',
     'Argued from D0.2\'s list against S111 to S116.')
prof('conjecture', NONE, 'AV00',
     'The conjecture is about explanatory creativity, and nothing in Avida creates an explanation; its one point of contact, a candidate that meets the test of an explanation and is not declared, is the hinge of group 14.',
     'Argued; see D16.XV for the computed contact (MC1).')
# G02
prof('org', EXACT, 'AV01',
     '', 'Argued, and checked by S112: every one of 23,332 programs was followed through Avida\'s step-by-step record "number by number" with no difference; a program on the simulated computer is an organization with registers, stacks and the input and output as its values and its executed instructions as its parts.')
prof('deletion', NOT, 'AV02',
     'The semantics takes a part out by leaving its values free (any value at all); Avida\'s ablation puts in a do-nothing instruction, which still does something definite, so the two give different answers.',
     'Computed (MC4): at a fine grain, the semantics\' deletion of an extra read leaves the answer undetermined where Avida\'s ablation gives a definite, different answer; at the grain of S112\'s circuits, deletion changes nothing where ablation changes the answer. S112: removing an unused read at instruction 45 of an EQU program made the later reads take other numbers.',
     'Cutting the instruction out (S112, not tested): also not deletion; it shifts every later position.')
prof('nonmonotone', NOT, 'AV02',
     'The semantics proves that taking parts out never removes a possibility; Avida\'s ablations are not like that: removing a second instruction can bring back a copying that the first removal had stopped.',
     'S112 after the cross-examination: in 85 of 89 hard cases, one ablation stopped the copying and a second ablation let it work again.')
prof('setting_unused', PART, 'AV01',
     'The definition applies to an Avida program, but the Avida work never set a value directly; it changed instructions and the numbers handed in.',
     'Argued from the S111 to S116 plans.')
prof('inputs_role', PART, 'AV05',
     'Whether the numbers handed in are an "input" in the semantics\' sense depends on whether changing them is modelled as a change made to the program or as a change of its circumstances, a choice the text leaves to whoever models it.',
     'Argued; the same choice was flagged for the owner in S108 (candidate C5).')
prof('reader_changed', NOT, 'AV02',
     'The semantics says setting one value leaves every other part as it was; Avida\'s nearest change, an ablated read, changes what every later read takes.',
     'S112: removing an unused read at instruction 45 made the reads at 47, 53 and 66 receive other numbers; MC4.')
prof('roles_exact', EXACT, 'AV01', '',
     'Argued: Avida\'s simulated computer runs in one direction, from the numbers handed in to the number handed out, and which values are outputs is fixed by the instructions\' own relations.')
prof('obs_unused', PART, 'AV01',
     'Avida programs have instructions that look at values without changing them (comparisons), which this definition could be read on, but the Avida work never looked inside the programs for them, at the owner\'s word that looking inside is the wrong direction.',
     'Argued; S116 left "which instructions do it" unexamined at the owner\'s word.')
# G03
prof('question', EXACT, 'AV04', '',
     'Argued: each task put to a program ("does it hand back NOT of a number it was handed?") is a question in the semantics\' sense: a target (the program in its world), a set of changes (the numbers, the ablations), a query that reads the output, and a recorded origin.',
     'The researchers\' measurements are questions too (AV14).', people=True)
prof('contract_provenance', EXACT, 'AV04', '',
     'Argued from S113: Avida\'s tasks come from a list written in advance, which is what the semantics calls a declared question; "in none of them did new problems come from anywhere but a list written in advance" (S113, section 7). The semantics says finding a question needs a constructed one, and Avida has none.',
     'The growing list adds tasks by a rule, but the rule was also written in advance: still declared.')
prof('two_questions', EXACT, 'AV11', '',
     'Argued from S116: counting tasks on one set of numbers and on eight sets are two questions, and gave 46 and 0 for one growing-list run; the semantics says an answer to one is not an answer to the other.', people=True)
prof('question_defect', EXACT, 'AV14', '',
     'Argued from S113 and S114: Avida\'s own count said no task was common at ten times in one run because reloading emptied each program\'s record; exposing that defect was a second question with its own contract, as the semantics says.', people=True)
# G04
prof('kinds', EXACT, 'AV12', '',
     'Computed (C2): of 318 groups of programs that do exactly the same in the unchanged test, 302 split when nand is read as nor, 285 with random numbers, 212 with the numbers reordered. S112: the commonest NOT circuit is carried by 7,959 different instruction sequences.')
prof('kinds_math', EXACT, 'AV12', '',
     'Argued: a mathematical property of the definition, which holds of any organization and so of the Avida programs written as organizations.')
prof('rule_family', EXACT, 'AV06', '',
     'Argued from S112 section 5: an instruction\'s meaning behaves as the semantics\' "rule application": the same numbers in, a different rule, a different output; with nand read as nor, 97 in 100 NAND programs did NOR, as each program\'s own circuit said beforehand.')
prof('measure_unused', PART, 'AV01',
     'The measurement family can be read on Avida\'s comparison instructions, but the Avida work never identified one.',
     'Argued.')
prof('text_only', NONE, 'AV00',
     'This claim is about the text\'s own wording or bookkeeping; nothing in Avida bears on it.',
     'Argued.')
prof('constitutive', NONE, 'AV00',
     'Avida has no constitutive statuses (no rule that makes something count as something in a practice).',
     'Argued.')
# G05
prof('transport', EXACT, 'AV09', '',
     'Computed (MC1, C1): both S112\'s circuit (read through Avida\'s trace) and the whole program (read against the task) can be written as the semantics\' transports and candidates.')
prof('condition_test', EXACT, 'AV09', '',
     'Computed: the condition can be evaluated on Avida candidates and gives a definite verdict (MC1: the program as one block meets it; C1: S112\'s circuit fails question fidelity on S112\'s own ablations in 91 in 100 program-task pairs).')
prof('F1', PART, 'AV01',
     'The whole program, as one block, matches the task part for part, but cut into its instructions it does not: the task has no parts for the instructions to match.',
     'Computed (MC1): F1 holds for the program as one block and fails for the program cut into read, copy, nand and write; F2, (A) and Dependence hold for both.')
prof('account', PART, 'AV09',
     'What the Avida work offered as "what the evolved information is", the circuit read from Avida\'s step-by-step record, fails the semantics\' test on the very ablations that study made; the whole program, as one block, passes it on the numbers the world hands in.',
     'Computed. C1: across 83,725 program-task pairs, the circuit gives the right answer at every single ablation in 8.8 in 100 (17 in 100 for NOT, 0 for XOR and EQU), though it is wrong at only 5.4 in 100 of the 7.15 million ablations. MC1: the program as one block meets all five conditions.',
     'The program cut into its instructions (fails F1, MC1); nothing (Avida holds no explanation of its own).')
prof('dependence', PART, 'AV10',
     'The first half of Dependence (a change at which the answer differs) is exactly the owner\'s "required instruction"; the second half takes parts out by the semantics\' deletion, which Avida\'s ablation is not.',
     'Computed (MC4) and from S112: 98 in 100 program-task pairs have at least one single ablation that stops the task.')
prof('deletion_in_candidate', NOT, 'AV02',
     'The semantics takes a part out by leaving its values free; Avida\'s ablation puts in a do-nothing instruction, which still acts.',
     'Computed (MC4).')
prof('nonvacuous', EXACT, 'AV14', '',
     'Argued: each S111 to S116 plan stated what was tested and what was left out, which is the stated scope the condition asks for.', people=True)
prof('relabelings', EXACT, 'AV10', '',
     'Argued from S111: 85 of the first program\'s 100 instructions change nothing when ablated; a question asked only about those changes admits no account, as the semantics says.')
prof('tables', EXACT, 'AV11', '',
     'Argued from S116: the record of which tasks a program did on the one set of test numbers is a table of observed answers; it fails as soon as the numbers change (one growing-list run: 46 common tasks on the world\'s numbers, 0 on all eight sets).')
prof('slot', EXACT, 'AV01', '',
     'Computed (MC1): the program has no part that simply writes the answer in, as expected of a part that computes it.')
prof('written_in', NONE, 'AV00',
     'These claims are about candidates with the answer written into a part (the owner\'s shop sign, generated models); no Avida program writes its answer in.',
     'Argued.')
prof('fail_elsewhere', EXACT, 'AV05', '',
     'Computed (MC2, C3): a program that meets the test on the world\'s order fails it on a wider set of changes that includes an order the world never gives; C3 found such programs in 16 of 18 populations.')
prof('arg9', EXACT, 'AV12', '',
     'Computed (C2) and from S115: two hand-built programs both copy themselves and do NOT at the same speed; after the same one-instruction change one does NAND and the other nothing (S115 reply 4, rerun to the last digit).')
prof('F1F2', EXACT, 'AV01', '',
     'Computed (MC1): the program cut into its instructions meets F2 (the whole agrees) but not F1 (the parts do not), the case the semantics names: pieces each fail to match while the assembled whole agrees.')
prof('no_assessor_E', EXACT, 'AV01', '',
     'Computed (MC1): the test of an account was evaluated on the Avida case with no history, assessor or provenance; provenance entered only afterwards.')
# G06
prof('routes_via_ablation', PART, 'AV10',
     'The structure matches (sets of instructions that must go together), but Avida finds them by ablation, not by the semantics\' deletion.',
     'S112: singles, pairs and triples of ablations.')
prof('critical_block', EXACT, 'AV10', '',
     'Computed (MC3) and from S112: in about 2 in 100 program-task pairs the task is done in two places, so no single ablation stops it and a pair does: a critical block with no critical single part, as the semantics says can happen.')
prof('boundary_family', EXACT, 'AV03', '',
     'From S111: of the 2,500 one-change neighbours of each run\'s commonest program, 69 to 79 in 100 still copy themselves; that is the semantics\' boundary over a declared family of changes, computed for the copying question.')
prof('nowork', EXACT, 'AV10', '',
     'From S111: 85 of the first program\'s 100 instructions are removable (the owner\'s term): the semantics\' "does no work by itself".')
prof('interference', EXACT, 'AV10', '',
     'From S112 after the cross-examination: in 85 of 89 hard cases an instruction\'s removal stops the copying and removing a second one restores it: a part that interferes, as the semantics allows.')
prof('monotone_assumption', EXACT, 'AV10', '',
     'Argued: the finite monotone claim applies only where its assumptions hold; the 85 restoring pairs show where they do not, which the claim itself allows.')
prof('infinite', NONE, 'AV00', 'Avida programs are finite; there are no infinitely many parts.', 'Argued.')
# G07
prof('conflict_exact', EXACT, 'AV05', '',
     'Computed (MC2, C3): two programs that agree at every order the world gives and differ at one it never gives conflict there, outside the world\'s set of changes; their answers agree inside it.')
prof('rivals_not', NOT, 'AV07',
     'In Avida programs compete for room, but nobody offers one as an answer in place of another, and the semantics says in so many words that rivals are not a selection population.',
     'Argued from L315 ("Nor are rivals a selection population").', people=True)
prof('no_assessor', NONE, 'AV00',
     'There is no one in Avida who holds premises, offers answers or rules anything out; problems, ruling out and tests between rivals need such a person.',
     'Argued from S111 section 8: no program holds a problem or criticises. The people studying Avida do all of this (AV14).', people=True)
prof('etv_not', NOT, 'AV07',
     'Avida has exactly the pattern "easy to vary" names, two programs that agree on everything the world gave and differ only where it never looked, but nobody offers them and nobody has to decide, so the term does not apply.',
     'Computed (C3): in growing-list run 2, 2,370 programs do NOT in the world\'s order; with the second and third numbers swapped, 34 of them still do and 2,336 do not.', people=True)
prof('test_part', PART, 'AV01',
     'Avida\'s test computer records what a program does at chosen numbers, which is the semantics\' test, but only the people studying Avida use it to decide between answers; in the world, checking a task is a reward rule, not a test between rivals.',
     'Argued.', people=True)
prof('no_ranking', NOT, 'AV07',
     'The semantics never ranks candidates; Avida\'s whole mechanism is a ranking (Avida fitness decides which program copies faster and spreads).',
     'Argued from L25 and S113.')
prof('claims_none', NONE, 'AV00',
     'Nothing in Avida states a claim (such as "perpetual motion is impossible") that a program could conflict with.',
     'Argued.')
# G08
prof('arguments_none', NONE, 'AV00',
     'No Avida program holds a premise, admits an inference or uses an argument; all of this happens only among the people studying Avida.',
     'Argued from S111 section 8.', people=True)
prof('criticism_not', NOT, 'AV04',
     'The nearest thing in Avida, the world withholding reward or a broken copy dying, is what the text calls an adverse signal, which "is not a criticism until an organization represents it as the premise of a criticism".',
     'Argued from L383 and S111 section 4 (the world removes broken copies).', people=True)
prof('errcorr_not', NOT, 'AV07',
     'In the semantics error correction is done by someone using premises to find an error; in Avida no instruction checks or mends anything, and errors are "corrected" only by the world removing what fails.',
     'Argued from L397 and S111 section 4.')
# G09
prof('history_exact', EXACT, 'AV08', '',
     'Argued: Avida keeps the programs\' ancestry and step-by-step records; they are histories of located occurrences with a precedence that has no cycle.')
prof('active_route', PART, 'AV09',
     'The routes read from Avida\'s step-by-step record are actual paths through executed instructions from the numbers handed in to the number handed out, but the semantics asks that the input be represented, which turns on the reading in group 9.',
     'S112 traces; see D12.1.', reading=True)
prof('occurs', EXACT, 'AV05', '',
     'Argued from S116: Avida\'s code confirms which numbers, in which order, the world actually handed in.')
prof('selected', PART, 'AV07',
     'Avida has the population, the variation and the history the semantics asks for, but its survival does not require doing the task (it only pays better), and whether the program\'s history holds something that represents the task turns on whether Avida\'s task-checking code counts as part of it.',
     'Computed (MC1): with the checking code left out of the history (reading A) the model\'s own Sel holds; counted in (reading B) it fails and the transport is declared. C3: populations persist for 50,000 updates in the environment that pays for nothing, with 11 of 3,600 programs doing NOT.',
     'Taking the checking code as part of the world\'s physics (reading A) or as an earlier occurrence that represents the task (reading B); the text\'s own reading of "member of the history" is an invention (I52).', reading=True)
prof('constructed_none', NONE, 'AV00',
     'Nothing in an Avida program\'s history works anything out with a target in view; the only construction in the Avida work is the people\'s.',
     'Argued from S111 section 8; S112\'s circuits were constructed by Claude, not by Avida.', people=True)
prof('declared', PART, 'AV04',
     'Avida\'s task list is declared in the semantics\' sense (written in by its author); whether the programs\' own correspondences are declared too turns on the reading of group 9.',
     'Computed (MC1): under reading B the model\'s Sel and Con both fail and the program\'s transport is declared.', reading=True)
prof('inherited', PART, 'AV03',
     'Copying a program is a relay that keeps its history, as the semantics says, but the rule "a binding newly built gets constructed provenance" would, read literally, give a part made by a copying mistake a constructed history, which the rest of the semantics calls selection.',
     'Argued from D12.4 and S111. Proposed for the owner, not applied: say "newly built by a construction trace".')
prof('prov_exact', EXACT, 'AV07', '',
     'Computed (MC1): under either reading the model\'s own functions give exactly one of the three histories (selected under A, declared under B), never two.')
prof('witness', EXACT, 'AV07', '',
     'Argued: Avida supplies the physical witness the claim asks for (a recorded population, the numbers actually handed in), so selection is not met trivially.')
prof('survival_fidelity', EXACT, 'AV05', '',
     'Computed (C3): what a program does at an order the world never gave is not fixed by its having lasted: in 16 of 18 populations some programs that last and do NOT in the world\'s order fail at another order and some do not.')
prof('arg3', EXACT, 'AV05', '',
     'Computed (C3, MC2): in 16 of 18 S116 populations, at some order the world never gives, the population holds programs that do NOT in the world\'s order and differ there; the other two hold no NOT programs at all. Growing-list run 2: 2,370 do NOT in the world\'s order; with the second and third numbers swapped, 34 still do and 2,336 do not.')
prof('env_enacts', EXACT, 'AV04', '',
     'Argued from S63 and S113: all the choosing in the Avida runs was done by the execution environment.')
prof('wellfounded', EXACT, 'AV08', '', 'Argued: Avida\'s histories are finite and run forward in updates.')
prof('two_prov', PART, 'AV07',
     'Avida shows only one of the two histories the semantics keeps apart: selection; nothing in it constructs.',
     'Argued from S111 section 8 and S113.')
prof('creativity_construction', PART, 'AV11',
     'Avida shows selection producing new capabilities, the "raw material" the semantics speaks of, but nothing that constructs, so by the semantics\' words nothing in Avida is creative.',
     'S113: 48 to 65 tasks commonly done in the growing-list runs, all by variation and selection.')
# G10
prof('rep', PART, 'AV01',
     'Whether an Avida program that does a task "stands for" that task flips on one reading: if its history counts as selection it represents the task on the numbers the world hands in; if the task-checking code counts as part of its history, it represents nothing.',
     'Computed (MC1, MC2): on reading A, fidelity on the world\'s order and selected history, so representation holds there and fails on a wider set of changes for programs tied to the order; on reading B, declared, so no representation. S111 had observed "nothing in them refers to where the numbers come from", which agrees with reading B and not with A.', reading=True)
prof('layers_none', NONE, 'AV00',
     'Avida programs sense only numbers: they have no lasting objects to track and make no predictions, so neither layer exists in them.',
     'Argued from S111 section 8.')
prof('surprise_not', NOT, 'AV05',
     'Avida programs fail at input orders the world never gives, which has the formal shape of surprise, but they have no layer that predicts and the world never changes its order, so nothing in Avida is ever surprised; only the tests show where it would be.',
     'Computed (C3): 16 of 18 populations; S116: Avida\'s code always hands the numbers in one order.')
prof('responses', PART, 'AV11',
     'Avida shows only one of the two responses, re-tuning within the population; and it is not a response to a failed prediction, since nothing in Avida predicts.',
     'Argued from S113.')
prof('underdet', EXACT, 'AV05', '', 'Computed (C3, MC2): as for Argument 3.')
prof('arg4', EXACT, 'AV05', '',
     'Argued: the claim gives a necessary condition; Avida programs have selected correspondences tested on less than their contract, but no layer that predicts, so the claim holds and nothing is surprised.')
prof('construction_response_none', NONE, 'AV00',
     'Nothing in Avida responds by building something new with a target in view.', 'Argued.')
prof('only_construction_origin', EXACT, 'AV11', '',
     'Argued: Avida\'s new capabilities all came by selection, and none meets the semantics\' origin (no construction), as the claim says it cannot.')
prof('theory_error_none', NONE, 'AV00', 'Nothing in Avida holds a theory, in error or not.', 'Argued.')
prof('inexplicit', PART, 'AV09',
     'An evolved circuit is exactly the kind of inexplicit thing the text means (nothing in it is stated), but whether it represents at all turns on the reading of group 9.',
     'S112; MC1.', reading=True)
# G11
prof('deploy_not', NOT, 'AV01',
     'The semantics\' "deploy" asks that a representation be put to use on a problem the system holds; an Avida program does its task, but holds no problem: tasks are set, checked and paid for by the world.',
     'Argued from S111 section 8; the retained-capability half holds (group 13).')
prof('repertoire_not', NOT, 'AV11',
     'The study of the six environments counted the tasks a population can do; the semantics\' repertoire is what a system can deploy on a problem, which in Avida is empty.',
     'Argued.')
prof('new_not', NOT, 'AV11',
     'The six-environment study\'s "new task" means a task no program in the run did before; the semantics\' "new" is measured against what the system could already deploy, which in Avida is nothing, so it holds of everything and says nothing.',
     'S113: growing-list run 1 reached 65 commonly done tasks, each "new" in S113\'s sense.')
prof('build_none', NONE, 'AV00',
     'Nothing in Avida builds a content for explanatory use inside its own boundary: new working parts arise by copying mistakes that last.',
     'Argued from S111 section 8 and D13.3.')
prof('origin_not', NOT, 'AV11',
     'The first appearance of a new capability in Avida comes from a copying mistake that lasted, not from a construction, so the semantics\' origin is not met.',
     'Argued; S113.')
prof('matching', EXACT, 'AV09', '',
     'Argued from S112: circuits written in one standard form, so that programs doing the same circuit are counted together however spelled, is the semantics\' matching of contents.')
prof('ownership', EXACT, 'AV01', '',
     'Argued from S111: "the program\'s own instructions are a part without which the thing does not happen, and the world\'s rules are the other part": ownership relative to a declared boundary, as the semantics defines it.')
prof('episode_formal', PART, 'AV11',
     'The formal episode (every change of question recorded) is met by the growing-list runs, whose reward history records each task added; the critical episode the text describes (a recognized difficulty, an objection, a response) has nothing in Avida.',
     'S113 reward history; L429.')
prof('episode_none', NONE, 'AV00',
     'Nothing in Avida recognizes a difficulty, holds an objection or closes an episode by choice.',
     'Argued from S111 section 8.', people=True)
# G12
prof('aims', EXACT, 'AV04', '',
     'Argued: aims are inputs the semantics takes as stated; for Avida they can be stated (claimed: "EQU common"; protected: "the population still copies itself").')
prof('repair_part', PART, 'AV11',
     'The first two parts of a repair hold in the six-environment study (EQU not done at the start, done later, the copying kept throughout), but "produced by" needs the path from the contributing change to the repair, which that study did not record.',
     'S113: EQU became common in all three fixed-list runs.')
prof('losses', EXACT, 'AV11', '',
     'Argued from S113: tasks once common and later lost (73 to 100 in 100 kept) were reported, as the semantics asks a repair claim to expose.')
prof('ex_none', NONE, 'AV00',
     'Explanatory aims ask that the system possess an account it can deploy; nothing in Avida does.', 'Argued.')
prof('ex_not', NOT, 'AV11',
     'The nearest Avida thing, a new capability that meets an aim, fails every part of created explanation that is about explanation (a critical episode, an origin, an account deployed).',
     'Argued from S113 and S111 section 8.')
prof('two_contrib', EXACT, 'AV10', '',
     'Argued from S112: where a task is done in two places and both ran, both are needed to stop it, and neither can be given the credit alone, as the semantics says.')
prof('appraisal_part', PART, 'AV04',
     'Avida\'s reward check is an achievement in the semantics\' sense (an action whose effect falls inside a stated purpose), but nothing in Avida appraises anything.',
     'Argued.')
# G13
prof('tasks', EXACT, 'AV04', '',
     'Argued: Avida\'s tasks are tasks in constructor theory\'s sense: a specified transformation from input to output, with its resources (running time) stated.')
prof('ct1', EXACT, 'AV01', '',
     'From S112 and S116: retained realization holds or fails exactly as the definition says, depending on which inputs count: 99 to 100 in 100 programs still do each task on numbers of the world\'s kind, 66 to 90 in 100 on random numbers; S116 counted a task only if done on all eight sets.')
prof('ct2', EXACT, 'AV01', '', 'Argued: an Avida program does not rewrite its own instructions while it runs, so it keeps its constructor state.')
prof('continuity', EXACT, 'AV08', '',
     'Argued from S111: the population and its line of descent remained to the end while not one program identical to the first did; whether "it" remained turns on the continuity declared, as the semantics says.')
prof('owned_cap', EXACT, 'AV01', '',
     'Argued from S111: the copying is owned by the program if its boundary includes the simulated computer that runs it, and not if the boundary is the instruction sequence alone ("the actual carrying out of each step belongs to the world").')
prof('canadv', EXACT, 'AV11', '',
     'From S113 and S116: from one starting program, three runs each; the growing list met "at least 48 of the list commonly done" in all three runs and failed "keep adding": the extended run stayed at exactly 41 for 25,000 updates.')
prof('tolerance_not', NOT, 'AV01',
     'The semantics says no performance is ever exact; Avida\'s simulated computer performs exactly (the same program on the same numbers always gives the same answer).',
     'Argued from D15.7 and S112 (traces matched Avida\'s own record with no difference).')
prof('population_def', EXACT, 'AV07', '',
     'Argued: the population the semantics speaks of is every program Avida\'s instruction set admits; the actual population is drawn from it.')
prof('substrate', PART, 'AV06',
     'Avida\'s programs bear organizations on a simulated carrier (one circuit written in 352 ways), as substrate independence says, but the "physical conditions" are Avida\'s rules, and nothing passes between media.',
     'S112.')
# G14
prof('scrutiny_none', NONE, 'AV00',
     'No Avida program can make its own practice a target; all the choosing is done by the execution environment.',
     'Argued.')
prof('universal_none', NONE, 'AV11',
     'Universality is about explanatory capacity; nothing in Avida has any, and every environment tried stopped at the end of a list written in advance.',
     'S113, S116; S115 reply 3: a counter of 77 tasks can never count more than 77.')
prof('classes', PART, 'AV01',
     'Avida, written as the semantics\' data, belongs to the base class and to none of the others.',
     'Argued.')
prof('suff', PART, 'AV01',
     'Whether an Avida program counts as an explanation of its task flips on one reading: if its history is selection, it passes every condition and the semantics calls it an explanation, which goes against the owner\'s reading of Avida as knowledge without the explanation kind; if the checking code counts in its history, it is declared and the semantics agrees with the owner.',
     'Computed (MC1): under reading A, the model\'s own (Suff) defeat condition is met for an assessor who takes as given that the program is no explanation; under reading B it is not, and the owner\'s rule "declared and an account, so not an explanation" (S41) holds.',
     'Not settled here: it touches what the owner left open (what knowledge is).', reading=True)
prof('bijection', EXACT, 'AV06', '',
     'Argued from S112: shuffling what the instruction letters mean stopped every program, because the programs were not recoded with the meanings; a structure-preserving recoding has to move everything together, as the semantics says.')
prof('faithful_noassessor', EXACT, 'AV05', '',
     'Computed (C3): whether a program is faithful at an order was found from the program and the task alone, with no one\'s view in it.')
prof('fallibility_none', NONE, 'AV00', 'Nothing in Avida holds a theory that could be in error.', 'Argued.')
prof('conjcrit_not', NOT, 'AV03',
     'Copying mistakes are sometimes likened to conjectures and the world\'s removal to criticism, but the semantics\' conjecture is an idea entertained and its criticism has a target; Avida\'s changes are not entertained and the world\'s removal has none.',
     'Argued from L71 and L383.')
prof('barrier_none', NONE, 'AV00',
     'A barrier is a domain no admitted condition can open; Avida\'s stopping at the end of its list is not one (the text: "a finite list of failures does not rule out a bypass").',
     'Argued from L495 and S113.')
# G15
prof('example', NONE, 'AV00',
     'This is one of the text\'s own worked examples (the pole, the balances, the tokens, the matrices, the two-layer episode); nothing in Avida plays its part.',
     'Argued.')
prof('contract_org', PART, 'AV04',
     'Avida\'s task list could be given the structure of an organization, as the text says a question can, but nothing in Avida builds or finds one.',
     'Argued.')
prof('qfinding_none', NONE, 'AV00', 'No Avida program finds a question; all of Avida\'s questions come from a list written in advance.', 'S113 section 7.')

# ---- every unit: group, profile, optional note ----------------------------------------------------------------------
U = {}


def put(group, key, ids, note=''):
    for i in ids.split():
        assert i not in U, i
        U[i] = (group, key, note)


put('G01', 'frame', 'D0.1')
put('G01', 'primitives', 'D0.2')
put('G01', 'conjecture', 'T01')
put('G02', 'org', 'D1.1 D1.2 D1.4')
put('G02', 'deletion', 'D1.3')
put('G02', 'setting_unused', 'D2.1 D2.6')
put('G02', 'inputs_role', 'D2.2')
put('G02', 'roles_exact', 'D2.3 D2.5 FC02')
put('G02', 'obs_unused', 'D2.4 FC2.new1')
put('G02', 'nonmonotone', 'FC01')
put('G02', 'reader_changed', 'FC06')
put('G02', 'kinds_math', 'FC11', 'Example: whether the numbers handed in are inputs depends on which changes are admitted (D2.2).')
put('G03', 'question', 'D3.1 D3.2 D3.3')
put('G03', 'contract_provenance', 'D3.4')
put('G03', 'nonvacuous', 'D3.5')
put('G03', 'question_defect', 'D3.6 FC106 FC107')
put('G03', 'two_questions', 'D3.7 FC34 FC36')
put('G04', 'kinds', 'D4.1 D4.2 FC04 FC05')
put('G04', 'kinds_math', 'D4.3 D4.4 D4.5 FC03 FC12 FC13 FC13.new1 FC16 FC17 FC18 FC96')
put('G04', 'rule_family', 'D4.6')
put('G04', 'measure_unused', 'FC4.new1 FC08')
put('G04', 'constitutive', 'FC09')
put('G04', 'text_only', 'FC10 FC14')
put('G05', 'transport', 'D5.1 D5.2 D5.3')
put('G05', 'F1', 'D5.4')
put('G05', 'condition_test', 'D5.5 D5.6 D5.7 D6.8')
put('G05', 'deletion_in_candidate', 'D6.1')
put('G05', 'kinds_math', 'D6.2 FC15 FC20 FC22 FC29 FC33', 'Holds of the Avida candidates by proof.')
put('G05', 'slot', 'D6.3')
put('G05', 'dependence', 'D6.4 D6.5')
put('G05', 'nonvacuous', 'D6.6')
put('G05', 'account', 'D6.7')
put('G05', 'relabelings', 'D6.9 FC21')
put('G05', 'tables', 'D6.10 FC25')
put('G05', 'F1F2', 'FC19')
put('G05', 'written_in', 'FC23 FC23.new1 FC23.new2 FC23.new3 FC23.new4 FC23.new5 FC24 FC25.new1')
put('G05', 'account', 'FC25.new2', 'Its one-component candidate has an Avida counterpart (the program as one block, MC1), which meets (E) but is not a slot.')
put('G05', 'no_assessor_E', 'FC30')
put('G05', 'text_only', 'FC31 FC104 FC104.new1 FC108 FC35')
put('G05', 'fail_elsewhere', 'FC99')
put('G05', 'arg9', 'FC101')
put('G06', 'routes_via_ablation', 'D7.1 D7.2')
put('G06', 'critical_block', 'D7.3 D7.5 FC38 FC42')
put('G06', 'boundary_family', 'D7.4')
put('G06', 'nowork', 'D7.6 FC41')
put('G06', 'monotone_assumption', 'FC37')
put('G06', 'interference', 'FC39')
put('G06', 'infinite', 'FC40')
put('G06', 'text_only', 'FC42.new1')
put('G07', 'kinds_math', 'D8.1', 'Definable on Avida targets; used only through conflict.')
put('G07', 'conflict_exact', 'D8.2 D8.new1 FC44 FC46 FC48 FC51')
put('G07', 'rivals_not', 'D8.3')
put('G07', 'claims_none', 'D8.4 D8.5 D8.6 FC52 FC53 FC54')
put('G07', 'no_assessor', 'D10.1 D10.2 D10.5 D10.6 FC47 FC47.new1 FC49 FC50')
put('G07', 'test_part', 'D10.3')
put('G07', 'etv_not', 'D10.4')
put('G07', 'kinds_math', 'FC45', 'Recoded candidates: one circuit in many spellings conflicts nowhere (S112).')
put('G07', 'conflict_exact', 'FC43', 'Symmetry of conflict holds; rivals, problems and "easy to vary" have nothing in Avida.')
put('G07', 'no_ranking', 'FC55')
put('G08', 'arguments_none', 'D9.1 D9.2 D9.3 D9.4 D9.5 D9.6 D9.7 D9.8 D9.9 D9.11 FC56 FC68 FC69 FC70 FC71 FC72 FC72.new1 FC72.new2 FC73 FC74 FC76 T09')
put('G08', 'criticism_not', 'D9.10')
put('G08', 'errcorr_not', 'T13')
put('G09', 'history_exact', 'D11.1 D11.2 D11.3')
put('G09', 'active_route', 'D11.4 FC75')
put('G09', 'occurs', 'D11.5')
put('G09', 'selected', 'D12.1')
put('G09', 'constructed_none', 'D12.2 FC12.new3')
put('G09', 'declared', 'D12.3')
put('G09', 'inherited', 'D12.4')
put('G09', 'prov_exact', 'FC12.new1 FC78')
put('G09', 'kinds_math', 'FC12.new2', 'A record of a program (S112\'s traces) carries the program\'s history.')
put('G09', 'witness', 'FC77')
put('G09', 'survival_fidelity', 'FC79')
put('G09', 'arg3', 'FC80')
put('G09', 'env_enacts', 'FC80.new1 FC97.new1')
put('G09', 'wellfounded', 'FC98.new1 FC98.new2')
put('G09', 'text_only', 'FC105')
put('G09', 'two_prov', 'T07')
put('G09', 'creativity_construction', 'T08')
put('G10', 'rep', 'D12.5')
put('G10', 'layers_none', 'D12.6')
put('G10', 'surprise_not', 'D12.7')
put('G10', 'responses', 'D12.8')
put('G10', 'underdet', 'D12.9')
put('G10', 'arg4', 'FC81')
put('G10', 'construction_response_none', 'FC82')
put('G10', 'only_construction_origin', 'FC83 FC84')
put('G10', 'theory_error_none', 'FC95')
put('G10', 'inexplicit', 'T10')
put('G11', 'deploy_not', 'D13.1')
put('G11', 'repertoire_not', 'D13.2')
put('G11', 'build_none', 'D13.3 FC84.new1')
put('G11', 'matching', 'D13.4 FC85')
put('G11', 'new_not', 'D13.5')
put('G11', 'origin_not', 'D13.6')
put('G11', 'ownership', 'D13.7')
put('G11', 'episode_formal', 'D13.8')
put('G11', 'text_only', 'FC84.new2')
put('G11', 'episode_none', 'T11 T14 T15')
put('G12', 'aims', 'D14.1')
put('G12', 'repair_part', 'D14.2 D14.3')
put('G12', 'losses', 'D14.4 FC86 FC88')
put('G12', 'ex_none', 'D14.5 D14.6')
put('G12', 'ex_not', 'D14.7')
put('G12', 'appraisal_part', 'D14.8')
put('G12', 'two_contrib', 'FC87')
put('G12', 'text_only', 'FC89 FC90.new1')
put('G13', 'tasks', 'D15.1')
put('G13', 'ct1', 'D15.2')
put('G13', 'ct2', 'D15.3 FC91 FC92')
put('G13', 'continuity', 'D15.4')
put('G13', 'owned_cap', 'D15.5')
put('G13', 'canadv', 'D15.6')
put('G13', 'tolerance_not', 'D15.7 FC93')
put('G13', 'population_def', 'D15.8')
put('G13', 'substrate', 'T06')
put('G14', 'scrutiny_none', 'D16.1 D16.2 T05')
put('G14', 'universal_none', 'D16.3 D16.4 FC94')
put('G14', 'classes', 'D16.5')
put('G14', 'suff', 'D16.XV FC30.new1')
put('G14', 'text_only', 'D18.1 FC32 FC32.new1 FC98 FC109 FC110')
put('G14', 'bijection', 'D18.2 FC67 FC100')
put('G14', 'faithful_noassessor', 'T02')
put('G14', 'fallibility_none', 'T03')
put('G14', 'conjcrit_not', 'T04')
put('G14', 'barrier_none', 'T12')
put('G15', 'example', 'E1 E2 E3 E4 E5 E6 E7 E9 FC07 FC26 FC27 FC27.new1 FC28 FC28.new1 FC28.new2 FC57 FC58 FC59 FC60 FC61 FC62 FC63 FC64 FC65 FC66 FC90 FC102 FC102.new1 FC103 FC103.new1')
put('G15', 'contract_org', 'E8')
put('G15', 'qfinding_none', 'FC97')

# ---- the main breaks: what does not work, and why (plain words first) ------------------------------------------------
BREAKS = [
    dict(id='B1', title='Whether an evolved program "stands for" its task, and counts as an explanation, flips on one unsettled reading',
         semantics='A correspondence that came about by variation and survival, with nothing in its history standing for the target, is "selected"; a selected, faithful correspondence "stands for" its target; and a candidate that passes the test of an explanation and is not merely declared is, by the semantics\' sufficiency claim, an explanation.',
         avida='An Avida program that does a task, its program population, and Avida\'s own code that checks the task and pays for it.',
         happens='Computed in a copy of the semantics\' own program: the program, taken as one block, passes all five conditions of the test of an explanation on the numbers the world hands in. If the code that checks the task is left out of the program\'s history, the program\'s correspondence is "selected", it stands for the task, and the semantics calls it an explanation. If that code counts as part of the history, the correspondence is "declared": it stands for nothing and is no explanation.',
         why='The semantics says a selected correspondence has nothing in its history that stands for the target, but in Avida the target is written down in advance, in the task list and the checking code, by people; whether that counts as "in the history" is a reading the text leaves open (the formal core marks it as invented).',
         example='The most common NOT program of run low seed 2 (110 instructions, 44 copies): it hands back nand(x, x), which is NOT x. Reading A: selected, represents NOT on the world\'s numbers, an explanation by the sufficiency claim, against the owner\'s reading of Avida as knowledge without the explanation kind. Reading B: declared, represents nothing, no explanation, which agrees with the owner and with the first Avida study.',
         units=['D12.1', 'D12.3', 'D12.5', 'D16.XV', 'FC30.new1', 'T10', 'D11.4'], groups=['G09', 'G10', 'G14'], avida_things=['AV04', 'AV07', 'AV01'],
         refs='MC1 (s117/model_cases.json); D12.1 at formal core line 454 (I52); L195, L205, L536; decisions S41, S59, S60'),
    dict(id='B2', title='Avida\'s "taking an instruction out" is not the semantics\' "taking a part out"',
         semantics='Taking a part out (deletion) leaves the values it governed completely free; "required" parts are judged by that, and the semantics proves that taking parts out never removes a possibility.',
         avida='Instruction ablation: an instruction is swapped for one that does nothing, and the program is run again (the owner\'s "required instruction").',
         happens='The do-nothing instruction still does something definite: an ablated read leaves the next read to take its number. So Avida gives a definite, different answer where the semantics\' deletion gives no answer at all, or no change; and in Avida a second ablation can bring back what a first one stopped, which deletion never can.',
         why='Ablation replaces an instruction with another instruction, a change of the program, while deletion removes all constraint; the owner\'s "required instruction" therefore lines up with the semantics\' "a change at which the answer differs", not with the semantics\' "a part the answer depends on".',
         example='In the most common EQU program of one run, ablating an unused read at instruction 45 made the reads at 47, 53 and 66 receive the third, second and first numbers instead of the first, third and second, and EQU was gone. In 85 of 89 hard cases one ablation stopped the copying and a second one restored it.',
         units=['D1.3', 'D6.1', 'D6.4', 'D6.5', 'FC01', 'FC06', 'D7.1', 'D7.2'], groups=['G02', 'G05', 'G06'], avida_things=['AV02', 'AV10'],
         refs='MC4; D1.3 line 64; L103, L255; S112 after the cross-examination, section 3'),
    dict(id='B3', title='The earlier answer to "what is it?", the circuit, fails the semantics\' test of an explanation',
         semantics='An account of a question must give the target\'s answer at every change the question asks about (question fidelity), not most of them.',
         avida='The circuits read from Avida\'s records, offered earlier as "what that evolved information actually is", and the single ablations made in the same study.',
         happens='Read as an explanation of "does the program still do the task after this one ablation?", the circuit says "it stops" exactly when the ablated instruction lies on every route. Over 83,725 program-task pairs it is wrong at only 5.4 in 100 of the 7.15 million ablations, but right at every ablation in only 8.8 in 100 pairs: 17 in 100 for NOT, 0 for XOR and EQU.',
         why='Some required instructions are not on the circuit (markers, extra reads that shift the numbers, jumps), and some instructions on the circuit are not required (another route takes over); the circuit describes the path the numbers took, not how the program responds to every change.',
         example='The NOT/EQU program of run low seed 2: for EQU, six required instructions lie off the circuit (23, 26, 27, 29, 31, 67) and four on the circuit are not required (11, 51, 74, 95).',
         units=['D6.7', 'D5.6', 'FC25.new2'], groups=['G05'], avida_things=['AV09', 'AV10'],
         refs='C1 (s117/circuit_A.json); D5.6 line 206; L250; S112 after the cross-examination, sections 3 and 4'),
    dict(id='B4', title='In Avida, lasting does not require doing the task',
         semantics='A selected correspondence "survives" by being faithful on the changes it met: the survival condition requires fidelity.',
         avida='Computational selection: programs that do a rewarded task get more running time and spread; programs that do none still copy themselves and last.',
         happens='Whole program populations last 50,000 updates doing almost no task when nothing pays, and in every environment many programs last without doing the rewarded task.',
         why='Avida\'s selection is a graded advantage (a faster rate of copying), not a pass-or-fail condition; doing the task pays better, it is not required.',
         example='The environment that pays for nothing, run 1: after 50,000 updates, 3,600 programs, of which 11 do NOT. The fixed-list environment, run 1: 3,595 programs, 2,290 do NOT.',
         units=['D12.1', 'FC55'], groups=['G09', 'G07'], avida_things=['AV07'],
         refs='C3 (s117/orders/summary.json); D12.1 line 454 (surv); L195'),
    dict(id='B5', title='Everything about explanation as an activity has nothing in Avida',
         semantics='Problems (two answers nobody can yet decide between), arguments and criticism, rivals offered one in place of another, recognized difficulties, construction, origin, deployment, created explanation, turning on one\'s own practice.',
         avida='Nothing. The nearest things are the world withholding reward (a signal, not a criticism), programs competing for room (not rivals), and copying mistakes (not conjectures).',
         happens='Of the semantics\' units about these, none has an Avida counterpart that meets its conditions; every one that has a near counterpart fails a condition.',
         why='No Avida program holds a problem, states or uses a claim, compares versions, or has anything that stands for something outside it in a way it can use; all the choosing is done by the execution environment, and all the asking, testing and criticising by the people studying Avida.',
         example='One of Astra\'s designs: programs give running time to a neighbour or not, depending on a number the neighbour sends; after 5,000 updates 76 to 88 in 100 gave to nobody. A choice about another program, carried by instructions, with no problem, no reason and no criticism behind it.',
         units=['D8.3', 'D9.10', 'D10.1', 'D13.1', 'D13.3', 'D13.6', 'D14.7', 'D16.1', 'T04', 'T13', 'T14'], groups=['G07', 'G08', 'G11', 'G12', 'G14'], avida_things=['AV00', 'AV04', 'AV07', 'AV03', 'AV13'],
         refs='L315, L383, L429; S111 section 8; decision S63'),
    dict(id='B6', title='Avida\'s "learning new things" is, in the semantics\' words, selection, not creation',
         semantics='New means not matching anything the system could already deploy on a problem; origin needs a construction inside the system; creativity lives in construction.',
         avida='The new capabilities of the six-environment study: tasks no program in the run did before, appearing over thousands of updates.',
         happens='Every new capability came by copying mistakes that lasted (the semantics\' selection response). Since nothing in Avida deploys anything on a problem, the semantics\' "repertoire" is empty and its "new" holds of everything and says nothing; its "origin" is never met.',
         why='The semantics measures newness against usable understanding and asks for construction; Avida has variation and selection only.',
         example='Growing list, run 1: 65 tasks commonly done at the end, every one "new" in the study\'s sense, none an origin in the semantics\' sense; the one run let go on stayed at 41 for 25,000 more updates.',
         units=['D13.2', 'D13.5', 'D13.6', 'T08', 'D12.8'], groups=['G11', 'G09', 'G10'], avida_things=['AV11'],
         refs='D13.5 line 518; L13, L225, L413-L422; S113 section 4; S116 section 4'),
    dict(id='B7', title='Programs fail where the world never looks, but nothing in Avida is surprised',
         semantics='Surprise is a selected correspondence failing at a change it was never shaped against, when that change occurs; it needs a layer that predicts.',
         avida='The one order in which the world hands out its numbers, and the tests in this job that handed the same numbers in the other five orders.',
         happens='In 16 of 18 saved program populations some programs that do NOT in the world\'s order fail in another order while others do not: the exact shape of surprise. But Avida programs predict nothing, and the world never changes its order, so the failure never happens to them; only the tests show it.',
         why='Surprise in the semantics needs a predicting layer and an occurring change; Avida has neither.',
         example='Growing-list run 2: 2,370 programs do NOT in the world\'s order; handed the same numbers with the second and third swapped, 34 of them still do and 2,336 do not.',
         units=['D12.7', 'D12.6', 'D10.4'], groups=['G10', 'G07'], avida_things=['AV05'],
         refs='C3; MC2; D12.7 line 488; L217-L223; S116 after the cross-examination'),
    dict(id='B8', title='Avida\'s simulated world is exact; the semantics\' physics never is',
         semantics='No performance or retention tolerance is ever exact.',
         avida='Avida\'s simulated computer: the same program on the same numbers always gives the same answer.',
         happens='The semantics\' tolerances have no counterpart in Avida\'s world: every performance there is exact.',
         why='Avida\'s "physics" is a program; the semantics\' physical module is a theory of the physical world.',
         example='23,332 programs were followed step by step against Avida\'s own record with no difference anywhere.',
         units=['D15.7', 'FC93', 'D0.1'], groups=['G13', 'G01'], avida_things=['AV01', 'AV06'],
         refs='D15.7 line 606; L479'),
]

# ---- the reverse list: what Avida shows that the semantics has no term for --------------------------------------------
REVERSE = [
    dict(id='R1', name='Copying itself', avida='AV07',
         what='A program whose own instructions make copies of it (15 of the first program\'s 100 instructions do it). The semantics speaks of copying only as something done to a content; it has no term for a content that causes its own copying, the owner\'s first property.'),
    dict(id='R2', name='Withstanding change by arrangement', avida='AV03',
         what='69 to 79 in 100 one-instruction changes leave an evolved program still copying; programs evolved with more copying mistakes lose less. The semantics can compute where a change breaks an account (its "boundary" over a family of changes) but has no term for how much of the family a thing withstands.'),
    dict(id='R3', name='Lasting by out-copying removal', avida='AV07',
         what='In Avida a program lasts only by being copied faster than the world removes programs. The semantics has continuity and retention, but no term for persistence as a balance of copying and removal.'),
    dict(id='R4', name='A graded advantage', avida='AV07',
         what='Avida fitness is a rate that decides which program spreads, not a pass-or-fail condition; the semantics has no score, rate or ordering of anything.'),
    dict(id='R5', name='How widespread a capability is', avida='AV11',
         what='The studies count tasks "present" (one program) and "common" (one in ten); the semantics has no population-level quantity.'),
    dict(id='R6', name='Pay that falls as more programs use it', avida='AV04',
         what='The "common sums pay less" environment pays from a store that runs down. The semantics has no term for an aim whose worth depends on how many already meet it.'),
    dict(id='R7', name='An order in which questions are posed', avida='AV11',
         what='The growing list added harder tasks as easier ones became common, and ended with more than the environment that offered all 77 at once. The semantics records a question\'s origin, but has no term for the order in which declared questions are presented.'),
    dict(id='R8', name='What a program can become next', avida='AV12',
         what='Two programs that do the same now become different things after the same change. The semantics separates them (two systems with the same outputs can be different organizations) but has no term for a thing\'s reach under further variation.'),
    dict(id='R9', name='A cost borne for another', avida='AV13',
         what='Programs that give running time to a neighbour at a cost to themselves. The semantics has no term for one system\'s cost for another\'s benefit.'),
]

# ---- plain sentences for the profiles that line up exactly (what matches), and plain examples ----------------------------
MATCH = {
    'org': 'A program running on Avida\'s simulated computer is, exactly, a set of parts (its executed instructions) constraining values (registers, stacks, the numbers in and out).',
    'roles_exact': 'Which values are outputs, and which way the program runs, come out of the instructions themselves, as the semantics says they should.',
    'question': 'Each task put to a program is a question in the semantics\' sense: a target, the changes asked about, and a query that reads the output.',
    'contract_provenance': 'Every question in Avida comes from a list written in advance: what the semantics calls a declared question, which can never count as a question found.',
    'two_questions': 'Counting tasks on one set of numbers and on eight sets are two different questions, and they gave different answers, as the semantics says they may.',
    'question_defect': 'When a count measured the wrong thing (a record emptied by reloading), finding that out was a second question, as the semantics says.',
    'kinds': 'Programs that behave alike under one set of changes come apart under a finer one, exactly as the semantics says kinds work.',
    'kinds_math': 'A mathematical property of the definition; it holds of the Avida programs written as the semantics\' structures.',
    'rule_family': 'Changing what an instruction means changes outputs as a rule change should, while the numbers handed in stay the same.',
    'transport': 'Both the circuit and the whole program can be written as the semantics\' candidates, with the links to the target it asks for.',
    'condition_test': 'The condition can be checked on Avida candidates and gives a clear yes or no.',
    'nonvacuous': 'The studies stated what they tested and what they left out, which is the stated scope this condition asks for.',
    'relabelings': 'Changes that alter nothing, like ablating the first program\'s 85 idle instructions, cannot by themselves support any account, as the semantics says.',
    'tables': 'A record of what a program did on one set of numbers fails as soon as the numbers change, as the semantics says of a table of observed answers.',
    'slot': 'The program has no part that simply writes the answer in.',
    'fail_elsewhere': 'A program that passes on the world\'s order of numbers fails on a wider set of changes, as the semantics says an account on one set can fail on another.',
    'arg9': 'Two programs with the same behaviour today are different organizations, shown by what the same change does to each.',
    'F1F2': 'The program cut into its instructions agrees with the task as a whole but not part for part, the very case the semantics\' two fidelity conditions are there to tell apart.',
    'no_assessor_E': 'The test of an account was computed on the Avida case without any history or anyone\'s view, as the semantics says it can be.',
    'critical_block': 'Where a program does a task in two places, only both together can be removed to stop it: a block that matters while no single part of it does.',
    'boundary_family': 'Which one-instruction changes keep a program copying and which do not is the semantics\' boundary over a family of changes.',
    'nowork': 'The owner\'s "removable instruction" is the semantics\' "does no work by itself".',
    'interference': 'A part that stops working only when another is present is the semantics\' interference.',
    'monotone_assumption': 'The claim applies only where its assumptions hold, and Avida shows where they do not, as the claim allows.',
    'conflict_exact': 'Two programs that agree on everything the world gives and differ at an order it never gives clash exactly where the semantics says they clash.',
    'history_exact': 'Avida keeps the ancestry and step-by-step record that the semantics calls a history.',
    'occurs': 'Which numbers the world actually handed in, and in which order, is recorded.',
    'prov_exact': 'Under either reading, each correspondence gets exactly one of the three histories.',
    'witness': 'Avida supplies the recorded population and inputs that keep "selected" from being true of everything.',
    'survival_fidelity': 'Having lasted does not fix what a program does at a change it never met.',
    'arg3': 'A correspondence shaped by selection is left open wherever the population holds another that also passed and differs: shown in 16 of 18 populations.',
    'env_enacts': 'The execution environment enacts the selection, as the semantics says.',
    'wellfounded': 'Avida\'s histories are finite and run forward.',
    'underdet': 'Shown in 16 of 18 populations, as for selection\'s open ends.',
    'arg4': 'Avida programs meet the necessary condition for surprise but lack the rest, and are never surprised, consistent with the claim.',
    'only_construction_origin': 'None of Avida\'s new capabilities is an origin in the semantics\' sense, as the claim says none can be without construction.',
    'matching': 'Counting programs with the same circuit together, however spelled, is the semantics\' matching of contents.',
    'ownership': 'What the program does is its own relative to a declared boundary: its instructions are inside, the world\'s rules outside.',
    'aims': 'Aims can be stated for Avida as the semantics takes them: as inputs.',
    'losses': 'Tasks once common and later lost were reported, as a repair claim must expose them.',
    'two_contrib': 'Where a task is done in two places and both ran, both get the credit.',
    'tasks': 'Avida\'s tasks are tasks in constructor theory\'s sense.',
    'ct1': 'Keeping the ability to do a task holds or fails exactly as defined, depending on which numbers count.',
    'ct2': 'A running program keeps its own instructions unchanged.',
    'continuity': 'Whether "it" remained depends on what counts as the same system: the line of descent remained, no identical program did.',
    'owned_cap': 'Whether the copying is the program\'s own depends on the boundary declared, as the semantics says.',
    'canadv': 'From one starting program, every run reached at least 48 of the growing list, and none kept going past the list.',
    'population_def': 'The population is drawn from every program Avida\'s instructions allow.',
    'bijection': 'Recoding works only if everything is recoded together, as shuffling the instruction meanings without the programs showed.',
    'faithful_noassessor': 'Whether a program is faithful was found from the program and the task alone.',
}

EXAMPLE = {
    'org': 'Every one of 23,332 evolved programs was followed step by step against Avida\'s own record with no difference.',
    'deletion': 'In one EQU program, ablating an unused read at instruction 45 made the later reads take other numbers and EQU was lost.',
    'nonmonotone': 'In 85 of 89 hard cases, one ablation stopped the copying and a second brought it back.',
    'reader_changed': 'The same unused read at instruction 45: the reads at 47, 53 and 66 received the third, second and first numbers instead of the first, third and second.',
    'kinds': 'Of 318 groups of programs that behave identically in the unchanged test, 302 split when nand is read as nor; the largest group, 5,073 programs doing the same seven tasks, came apart into several behaviours, the biggest 1,881 programs doing three tasks.',
    'contract_provenance': 'The growing list added harder tasks by a rule, but the rule and the tasks were written before the run.',
    'two_questions': 'One growing-list run: 46 tasks common on the world\'s numbers, 0 when a task had to be done on all eight sets.',
    'question_defect': 'Avida\'s own count said no task was common at ten times in one run, because reloading had emptied each program\'s record.',
    'rule_family': 'With nand read as nor, 97 in 100 programs that did NAND did NOR instead.',
    'F1': 'The NOT program of run low seed 2, as one block, matched the task; cut into read, copy, nand and write, it did not.',
    'account': 'For EQU in the program of run low seed 2: six required instructions lie off the circuit and four on it are not required.',
    'dependence': 'In 98 in 100 program-task pairs, ablating one instruction is enough to stop the task while the copying goes on.',
    'deletion_in_candidate': 'As above, the unused read at instruction 45.',
    'relabelings': 'The first program\'s 85 idle instructions.',
    'tables': 'One growing-list run: 46 tasks common on the test numbers, 0 on all eight sets.',
    'fail_elsewhere': 'Growing-list run 2: 2,370 programs do NOT in the world\'s order; with the second and third numbers swapped, 34 still do.',
    'arg9': 'Two hand-built programs both copy and do NOT at the same speed; after the same one-instruction change, one does NAND and the other nothing.',
    'F1F2': 'The NOT program cut into its instructions: the whole agrees with the task, the parts do not.',
    'critical_block': 'About 2 in 100 program-task pairs needed two instructions removed together, one from each place the task was done.',
    'boundary_family': '69 to 79 in 100 one-instruction changes left an evolved program still copying.',
    'nowork': 'The first program\'s 85 instructions whose ablation changes nothing.',
    'interference': '85 of 89 hard cases: removing a second instruction restored the copying a first removal had stopped.',
    'conflict_exact': 'Growing-list run 2: programs that agree at the world\'s order and part ways when the second and third numbers are swapped.',
    'rivals_not': 'Programs taking over each other\'s places in the grid: competition, not an offer of one answer in place of another.',
    'etv_not': 'Growing-list run 2: 34 programs still do NOT with two numbers swapped, 2,336 do not; all 2,370 do it in the world\'s order.',
    'no_ranking': 'In every rewarded environment, programs doing more tasks got more running time and spread.',
    'criticism_not': 'A copy that cannot copy itself makes no copies and dies of old age: a signal, not a criticism.',
    'errcorr_not': 'No instruction in Avida\'s set checks a copy against the original.',
    'selected': 'The environment that pays for nothing, run 1: 3,600 programs after 50,000 updates, 11 of them doing NOT.',
    'declared': 'The task list of every environment was written in a file before the run.',
    'inherited': 'A copy with one copying mistake that completes a new circuit.',
    'arg3': 'Growing-list run 2: 2,370 programs do NOT in the world\'s order; with the second and third numbers swapped, 34 still do and 2,336 do not.',
    'survival_fidelity': 'Fixed-list run 3: of 2,218 programs doing NOT in the world\'s order, 49 fail when the first two numbers are swapped.',
    'rep': 'The NOT program of run low seed 2: it hands back nand(x, x).',
    'surprise_not': 'Growing-list run 2, with the second and third numbers swapped: 2,336 programs fail at NOT; the world never hands them that order.',
    'responses': 'The growing list added tasks; the population re-tuned by copying mistakes that lasted.',
    'deploy_not': 'A program does EQU on the numbers it is handed, but holds no question about them.',
    'new_not': 'Growing-list run 1: 65 tasks commonly done at the end, each new in the study\'s sense.',
    'origin_not': 'Each of the 65 tasks first appeared through a copying mistake that lasted.',
    'episode_formal': 'The growing list\'s record of each task added.',
    'repair_part': 'Fixed list, all three runs: EQU not done at the start, common later, copying kept throughout.',
    'ex_not': 'EQU becoming common in the fixed-list runs.',
    'ct1': '99 to 100 in 100 programs still do each task on numbers of the world\'s kind; 66 to 90 in 100 on random numbers.',
    'continuity': 'At the end of every first-study run, not one program identical to the first remained; its line of descent did.',
    'owned_cap': 'The first program\'s 15 copying instructions, and the world that carries out each step.',
    'canadv': 'The all-77 run that was still rising stayed at exactly 41 common tasks for 25,000 more updates.',
    'tolerance_not': 'The same program on the same numbers always gives the same answer in the test computer.',
    'substrate': 'The commonest NOT circuit is written in 352 different ways across 7,959 instruction sequences.',
    'suff': 'The NOT program of run low seed 2, as one block, on the numbers the world hands in.',
    'bijection': 'Shuffling the meanings of all 26 instruction letters: no program copied itself or did anything.',
    'universal_none': 'A counter of 77 tasks can never count more than 77, however the rewards move.',
    'two_prov': 'Every new capability in every environment came by variation and selection.',
    'creativity_construction': 'The growing list ended with 48 to 65 tasks commonly done.',
    'conjcrit_not': 'A copying mistake that adds a random instruction, and a copy that dies because it cannot copy.',
}

# Plain names for the Avida studies, used in plain text instead of log numbers.
STUDIES = {
    'S111': 'the first Avida study (the three properties)',
    'S112': 'the study of what had to be removed',
    'S113': 'the study of the six environments',
    'S114': 'the check of Astra\'s first reply',
    'S115': 'the check of Astra\'s eight replies',
    'S116': 'the routine runs',
}
