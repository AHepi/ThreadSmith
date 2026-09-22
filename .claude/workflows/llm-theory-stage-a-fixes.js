export const meta = {
  name: 'llm-theory-stage-a-fixes',
  description: 'Plan W10 stage A, the fix round under addendum W11: three Opus 5 fixers in the makers roles (harness, instrument, corpus), then the Opus 5 reviewer again with a dry run on a corpus document; at most three rounds',
  phases: [{ title: 'Fix', detail: 'up to three Opus 5 fixers at xhigh in parallel' }, { title: 'Re-review', detail: 'one Opus 5 reviewer at xhigh, dry run on a corpus document' }],
}

const ROOT = '/home/user/ThreadSmith'
const SKILL = `${ROOT}/HV Skill/authority/33/hard-to-vary/`
const F11 = `${ROOT}/Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`
const W8 = `${ROOT}/Workflow/authority/W8 Model - an LLM agent in the language of the semantics, file 11 (frozen).md`
const W3 = `${ROOT}/Workflow/tests/W3 Research plan - a model of LLM agents in the semantics' terms, the instrument, the arrangements, the skill map, the workflow (frozen).md`
const W10 = `${ROOT}/Workflow/tests/W10 Plan - getting the LLM theory right; the harness, the corpus, the fourth clause, the instrument, the arms, the cross-examination.md`
const W11 = `${ROOT}/Workflow/tests/W11 Addendum to W10 - the decisions stage A's reviewer forced before stages B and C; the fix round.md`
const OUT = `${ROOT}/Workflow/rigs/W10 harness/`
const RETURNS = `${OUT}stage-A returns/`
const TEXTS = (args && args.texts_dir) || '/tmp/claude-0/-home-user-ThreadSmith/00bda300-7321-5714-a655-4358c87aab9b/scratchpad/w10texts'
const MAX_ROUNDS = 3

const PREAMBLE = `You are one agent of the fix round of plan W10 stage A, under addendum W11. You work under the hard-to-vary skill and will be held to it.

FIRST read the skill in full, once: ${SKILL}SKILL.md, then references/the-idea-in-depth.md, building.md, testing-against-cases.md, reporting.md, question-bank.md, word-list.md in ${SKILL}references/. One correction you carry: the skill's word list maps "fitted" to an older, unqualified Derivation 3; the authority, file 11, qualifies it: "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not." Never use the unqualified form yourself. Addendum W11 decision D3 says this qualification is NOT sent to any reader under test; do not put it into any file a reader is handed.

THEN read: addendum W11 in full (${W11}); plan W10 in full (${W10}); the reviewer's return ${RETURNS}A5-reviewer.json in full (its "faults" are numbered 0 to 23 in array order; the addendum uses those numbers); the stage-A return of the maker whose role you take (named in your task); the harness read-me ${OUT}code/README.md; W8 (${W8}) parts your task names; W3 section 5 (${W3}); file 11 (${F11}) where a fault touches the theory.

RULES. Write only under ${OUT}. Never edit anything under ${RETURNS} nor any file under Workflow/tests, Workflow/records, Workflow/authority; the other four projects are read only. Fix only what a numbered fault or a W11 decision forces; do not improve what no fault names; if you decline a fault, say why in your return with evidence. No key exists in the environment and nothing is to be sent to any API; every program you touch must still read a key only from the environment and write it to no file. Shell is allowed to run dry runs and tests under ${OUT} (python3, sending nothing) and, for the corpus fetcher only, to fetch a document to ${TEXTS} (outside the repository; keep no fetched text under ${OUT}). Web research beyond that: none is needed; if you do read anything outside the repository, it is CLAIMED and quoted with address and date. Every change you make is listed in your return with the file, the fault number and how you verified it by running.

SELF-FALSIFICATION before you return: for every fix, write what would show it does not fix the fault, run that, and say what you saw; record anything you dropped.

Your final message is data, not prose: return the structured output only.`

const FIX_SCHEMA = {
  type: 'object',
  properties: {
    role: { type: 'string' },
    fixed: { type: 'array', items: { type: 'object', properties: { fault: { type: 'integer' }, files: { type: 'array', items: { type: 'string' } }, what_changed: { type: 'string' }, verified_by_running: { type: 'string' } }, required: ['fault', 'files', 'what_changed', 'verified_by_running'] } },
    declined: { type: 'array', items: { type: 'object', properties: { fault: { type: 'integer' }, why: { type: 'string' }, evidence: { type: 'string' } }, required: ['fault', 'why', 'evidence'] } },
    decisions_applied: { type: 'array', items: { type: 'string' }, description: 'W11 decisions D1 to D4 you applied, and where' },
    dry_run: { type: 'string', description: 'every command run, and its outcome; nothing sent' },
    dropped: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, why: { type: 'string' } }, required: ['item', 'why'] } },
    for_the_reviewer: { type: 'string' },
    tools_used: { type: 'string', description: 'every tool used; every shell command; every fetched address; whether any file was written outside the harness folder' },
  },
  required: ['role', 'fixed', 'declined', 'decisions_applied', 'dry_run', 'dropped', 'for_the_reviewer', 'tools_used'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    verified_fixed: { type: 'array', items: { type: 'object', properties: { fault: { type: 'integer' }, how_checked: { type: 'string' } }, required: ['fault', 'how_checked'] } },
    faults: { type: 'array', items: { type: 'object', properties: { fault: { type: 'integer', description: 'the original number, or a new number from 24 upward for a new fault' }, deliverable: { type: 'string', description: 'A1-harness | A4-instrument | A2-corpus | A6-clients | A3-fourth-clause' }, file: { type: 'string' }, fault_text: { type: 'string' }, evidence: { type: 'string' }, forced_fix: { type: 'string' }, severity: { type: 'string', description: 'blocks stage B | blocks stage C | wording' } }, required: ['fault', 'deliverable', 'file', 'fault_text', 'evidence', 'forced_fix', 'severity'] } },
    declines_accepted: { type: 'array', items: { type: 'object', properties: { fault: { type: 'integer' }, accepted: { type: 'boolean' }, why: { type: 'string' } }, required: ['fault', 'accepted', 'why'] } },
    predictions_ticked: { type: 'array', items: { type: 'object', properties: { prediction: { type: 'string' }, verdict: { type: 'string' }, count: { type: 'string' } }, required: ['prediction', 'verdict', 'count'] } },
    dry_run: { type: 'string' },
    dropped: { type: 'array', items: { type: 'object', properties: { finding: { type: 'string' }, why_dropped: { type: 'string' } }, required: ['finding', 'why_dropped'] } },
    tools_used: { type: 'string' },
  },
  required: ['verified_fixed', 'faults', 'declines_accepted', 'predictions_ticked', 'dry_run', 'dropped', 'tools_used'],
}

const ROLES = {
  'A1-harness': { ret: 'A1-harness.json', extra: `You take the role of A1, the harness coder, over ${OUT}code/ (including code/clients/ where a fault names it). W8 parts to read: A1, A10, B4, B5, B10, B12, C4. W11's decisions D1, D2, D3 and the harness side of D4 are yours to apply (D1: no document block for the assembling step; D2: agreement.py prints both counts and reports the arm (a) half as "not reached", and the Sonnet run record says what its request count counts; D3: the field derivation3_qualification_sent: false with the reason in every run record on both transports, and the reason in the read-me; D4: the "never varies" flag in agreement.py, and P4.2 and P4.3 read over the fields the instrument's affordance table names, read from the instrument folder if A4 has written it by the time you finish, else from a path you document). Also the stage-B adapter (fault 0): the 96 record files under ${ROOT}/HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/ (find them; read three) mapped to the rig's shape. After every change: python3 skillcheck.py --check; the full dry run of every arm on both transports (run_deepseek.py --dry, sonnet_prompts.py plan --dry, wrap_sonnet.py --dry) on the fixture and, if the fetcher gives you a corpus document in ${TEXTS} (python3 ../corpus/fetch.py <id> --out ${TEXTS}), on that document; and first_marker/agreement on the adapter's output over the 96 records.` },
  'A4-instrument': { ret: 'A4-instrument.json', extra: `You take the role of A4, the instrument, over ${OUT}instrument/. W8 parts to read: A3, B4, C4. Faults 3, 4 and 5 are edits to criteria.json and marking-plan.md; a changed criterion is recorded in marking-plan.md as an addendum with the date and the fault number, never silently. D4 is yours on the instrument side: an addendum section in marking-plan.md and a machine-readable table (instrument/affordance.json: for every cross-step field, the ids of the eight arms documents that afford it, from ${OUT}corpus/coverage.md and sources.json, with one line of reason each), and the sentence that P4.2 and P4.3 are read over the fields at least one arms document affords. Verify by running: python3 -c "import json; json.load(open('criteria.json'))" and the harness's marks.py / first_marker.py --dry over your criteria (read ${OUT}code/README.md for how). Apply each fault's fix to the report the reviewer names (runs_sonnet5/F4-m2-r3.json under the old rig) and say what value the fixed criterion now gives there.` },
  'A2-corpus': { ret: 'A2-corpus.json', extra: `You take the role of A2, the corpus, over ${OUT}corpus/. Faults 21 and 22 are wording: the addendum line under split.json's what_a_freeze_means_here for the two apostrophes, with sources.json's spelling named as the one the exchange program uses; the Meno sentence in coverage.md. Nothing else in the split or the manifest changes (W11 decision D4: the split stays as frozen). Then, for the reviewer's corpus dry run: python3 fetch.py W1 --out ${TEXTS} (and one more arms document of your choice), verify the hash (--check), and report in your return the ids fetched and that ${TEXTS} is outside the repository; keep no fetched text under ${OUT}.` },
}

function fixerPrompt(role, faults, round, prior) {
  const r = ROLES[role]
  return `${PREAMBLE}

YOUR TASK (round ${round}): ${r.extra}

The maker's own return to read: ${RETURNS}${r.ret}. The faults assigned to you this round, by the reviewer's numbering: ${faults.join(', ')}.${prior ? `

This is not the first round. The reviewer's latest return, verbatim, follows; the faults listed for you above are the ones it still holds against your deliverable (original numbers, or 24 and up for faults it found new). Read its evidence and forced_fix for each before touching anything:
${prior}` : ''}`
}

function reviewerPrompt(round, fixes) {
  return `${PREAMBLE}

YOUR TASK (round ${round}): you are A5, the reviewer, again. Read your own stage-A return (${RETURNS}A5-reviewer.json) as the list of faults you returned; read addendum W11's four decisions as taken (you do not re-open them; you check they are applied as written). The fixers' returns for this round, verbatim, follow at the end. For every fault the fixers say they fixed: check it by RUNNING the thing (the same command that showed the fault, or a sharper one), never by reading the fixer's word; a fault whose fix you cannot show by running stays open. For every fault a fixer declined: say whether you accept the decline, with why. Then the dry run again: python3 skillcheck.py --check; run_deepseek.py --dry, sonnet_prompts.py plan --dry and wrap_sonnet.py --dry over ALL arms on (i) the fixture and (ii) a corpus document of the frozen split in ${TEXTS} (the corpus fixer should have fetched W1 there; if not, python3 ../corpus/fetch.py W1 --out ${TEXTS} yourself; keep nothing under the harness folder); read the saved request bodies for the things your first review checked (partition, exchange, withheld change list, the edited skill, the prefix call, the assembler's context, the run-record fields, the derivation3 field, MAX_TOKENS); the stage-B adapter on the 96 records with first_marker --dry and agreement over them. Delete and regenerate ${OUT}dry/ first so what you read is yours. Tick W10.9 and W10.10 (addendum W11 section 4) with counts; re-tick W10.1 on the corpus document. Return every fault that remains or is new with its severity (blocks stage B | blocks stage C | wording), using the original number where it is the same fault and 24 upward for a new one. Rules as before: write nothing except ${OUT}dry/ and files a wording fix of yours needs (say which); no key, nothing sent.

THE FIXERS' RETURNS THIS ROUND:
${fixes}`
}

const ASSIGN = { 'A1-harness': [0, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20], 'A4-instrument': [3, 4, 5, 18], 'A2-corpus': [21, 22] }
const roleOf = (d) => d.startsWith('A1') ? 'A1-harness' : d.startsWith('A4') ? 'A4-instrument' : d.startsWith('A2') ? 'A2-corpus' : d.startsWith('A6') ? 'A1-harness' : 'A1-harness'

let assign = ASSIGN
let prior = null
const rounds = []
for (let round = 1; round <= MAX_ROUNDS; round++) {
  const roles = Object.keys(assign).filter(k => assign[k].length)
  log(`round ${round}: fixers ${roles.join(', ')}`)
  const fixes = await parallel(roles.map(role => () =>
    agent(fixerPrompt(role, assign[role], round, prior), { label: `fix:${role}:r${round}`, phase: 'Fix', model: 'opus', effort: 'xhigh', schema: FIX_SCHEMA })))
  const fixMap = {}
  roles.forEach((role, i) => { fixMap[role] = fixes[i] })
  const review = await agent(reviewerPrompt(round, JSON.stringify(fixMap, null, 1)), { label: `review:r${round}`, phase: 'Re-review', model: 'opus', effort: 'xhigh', schema: REVIEW_SCHEMA })
  rounds.push({ round, fixes: fixMap, review })
  if (!review) { log(`round ${round}: reviewer returned nothing`); break }
  const blocking = (review.faults || []).filter(f => (f.severity || '').startsWith('blocks'))
  log(`round ${round}: ${review.faults.length} faults returned, ${blocking.length} blocking`)
  if (!blocking.length) break
  const next = { 'A1-harness': [], 'A4-instrument': [], 'A2-corpus': [] }
  for (const f of blocking) next[roleOf(f.deliverable || '')].push(f.fault)
  assign = next
  prior = JSON.stringify(review, null, 1)
}
return { rounds }
