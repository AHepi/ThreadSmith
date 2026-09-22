export const meta = {
  name: 'llm-theory-stage-a',
  description: 'Plan W10 stage A: four Opus 5 builders (harness code, corpus, fourth clause, instrument) then one Opus 5 reviewer, all armed with the hard-to-vary skill',
  phases: [{ title: 'Build and collect', detail: 'four Opus 5 agents at xhigh in parallel' }, { title: 'Review', detail: 'one Opus 5 reviewer at xhigh, with a dry run' }],
}

const ROOT = '/home/user/ThreadSmith'
const SKILL = `${ROOT}/HV Skill/authority/33/hard-to-vary/`
const F11 = `${ROOT}/Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`
const W8 = `${ROOT}/Workflow/authority/W8 Model - an LLM agent in the language of the semantics, file 11 (frozen).md`
const W3 = `${ROOT}/Workflow/tests/W3 Research plan - a model of LLM agents in the semantics' terms, the instrument, the arrangements, the skill map, the workflow (frozen).md`
const W10 = `${ROOT}/Workflow/tests/W10 Plan - getting the LLM theory right; the harness, the corpus, the fourth clause, the instrument, the arms, the cross-examination.md`
const OLDRIG = `${ROOT}/HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/`
const OUT = `${ROOT}/Workflow/rigs/W10 harness/`

const PREAMBLE = `You are one agent of stage A of plan W10. You work under the hard-to-vary skill and will be held to it.

FIRST read the skill in full, once: ${SKILL}SKILL.md, then references/the-idea-in-depth.md, building.md, testing-against-cases.md, reporting.md, question-bank.md, word-list.md in ${SKILL}references/. One correction you carry: the skill's word list maps "fitted" to an older, unqualified Derivation 3; the authority, file 11, qualifies it: "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not." Never use the unqualified form.

THEN read the plan you are part of, ${W10}, in full; the model under test, ${W8} (about 34,000 words; read the parts your task names in full and the rest as needed); W3 sections 4, 5 and 7 (${W3}); and file 11 (${F11}) where your task touches the theory. The old rig you build on is at ${OLDRIG} (run.py, sonnet_agent.py, second_marker.py, repeat_check.py, fetch.py, sources.json, and the marking/ folder); read what you need of it before writing anything.

RULES. Write only under ${OUT} (create it; your task names your subfolder). Never write anywhere else; never edit any file outside that folder; the other four projects are read only. No key exists in the environment and nothing is to be sent to any API; a program you write must read any key from the environment and write it to no file. Web research is permitted (Workflow decision W4): anything read outside the repository is CLAIMED, quoted with its address and today's date; keep no fetched text as a file. You may run shell commands only to test what you wrote (python3 dry runs that send nothing) and to list files; say in your return every shell command you ran. Plain words; the skill's stance; every claim about a file quotes the file.

SELF-FALSIFICATION before you return: for every design decision or claim you keep, write what would show it wrong, look for it, and drop or restate it if found; record what you dropped.

Your final message is data, not prose: return the structured output only.`

const SCHEMA = {
  type: 'object',
  properties: {
    task: { type: 'string' },
    files_written: { type: 'array', items: { type: 'string' }, description: 'every path written, with one line on what it is' },
    what_it_does: { type: 'string', description: 'what the deliverable does, in the plan\'s terms, and how it maps to W8\'s parts' },
    dry_run: { type: 'string', description: 'what you ran to test it (commands and outcome), sending nothing' },
    predictions_bearing: { type: 'array', items: { type: 'string' }, description: 'which predictions of W10 section 5 / W3 / W8 your deliverable serves, one per line' },
    claims: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, evidence: { type: 'string' }, tag: { type: 'string', description: 'seen | claimed | worked out' }, would_count_against: { type: 'string' } }, required: ['claim', 'evidence', 'tag', 'would_count_against'] } },
    dropped: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, why: { type: 'string' } }, required: ['item', 'why'] } },
    could_not_settle: { type: 'string' },
    for_the_reviewer: { type: 'string', description: 'where you think the reviewer should press first' },
    tools_used: { type: 'string', description: 'every tool used; every shell command; every web search and fetched address; whether any file was written outside your folder' },
  },
  required: ['task', 'files_written', 'what_it_does', 'dry_run', 'predictions_bearing', 'claims', 'dropped', 'could_not_settle', 'for_the_reviewer', 'tools_used'],
}

const TASKS = [
  { key: 'A1-harness', prompt: `${PREAMBLE}

YOUR TASK: A1, the harness coder. Write, under ${OUT}code/, a Python rig that runs every arm of W10 section 4 (W3 section 5's arms (a) to (r) as W8 amends them, plus (x)) on DeepSeek V4.1 Flash through its chat-completions API (model "deepseek-flash", as ${OLDRIG}run.py uses; effort high; the beta prefix-completion endpoint for arm (e), where the assistant message is prefilled with a report skeleton whose mark column is a closed list; five worker threads; resumable; the skill copy diffed against ${ROOT}/HV Skill/authority/33/hard-to-vary before every call; the request body as sent and the reply as returned both saved per call, which is prediction PA.1; the number of requests per run recorded; every module the tool loop served recorded by the rig, not by the reader). The same rig writes the prompt files for the Sonnet subagent transport: one prompt file per call, with the step decomposition of file 33's procedure (steps 1-2, 3, 4, 5, 6-7 for arms (b), (c), (c'); one call per test of Step 5 plus an assembler for arm (d), with the parts under test split across calls as W8 part B12 requires) and a JSON "next step" interface so a workflow script can feed the previous call's output into the next prompt. Write the fixed summariser for arm (c) as a deterministic program with an equal-length control that omits the parts list (W8 section 4); the carry-over-note extraction for (c'); the partition assembler; the name-exchange program for arm (x) over a document marked with two names; the change-list-withheld variant (f); the router-criticism insertion (r). Write the marker programs: a first-marker template that takes the frozen criteria file the instrument agent (A4) will write at ${OUT}instrument/criteria.json (design to that path and a reasonable schema, and say so), the blind second marker (shuffle, closed mapping, as second_marker.py), and an agreement-by-field program computing run-to-run and marker-to-marker agreement per field and document, with the P4.1 baseline rule of W3 section 5 (all three (a)-to-(a) pairs; a document counts as disagreeing when any pair disagrees). Write a read-me that says which program is a driver and which a rule, how runs are named, and what a dry run checks. Test with dry runs that send nothing (a --dry flag on every driver). Do not fetch any document; the corpus agent supplies the manifest at ${OUT}corpus/sources.json (design to that path and to the schema of the old sources.json).` },

  { key: 'A2-corpus', prompt: `${PREAMBLE}

YOUR TASK: A2, the corpus collector. Under ${OUT}corpus/, write sources.json (the schema of ${OLDRIG}sources.json, extended with: the address, the licence or open standing, the domain, the passage that answers "why", whether the document has two named speakers or agents whose names the re-identification arm can exchange and which names, and a hash of the fetched text so a later fetch can be checked), a fetcher (fetch.py, modelled on the old one: fetch by address, extract text, verify the hash, keep nothing in the repository), and a coverage map (coverage.md) in the skill's own words: which of the eleven tests each document gives purchase to, and the gaps. Requirements: at least twelve documents no run in the record has read (check every candidate against ${OLDRIG}sources.json and against HV file 50, ${ROOT}/HV Skill/tests/50 Corpus - outside sources for the skill test.md, and against HV file 43); across the domains of file 50 (science, computability, economics, philosophy, fiction, design, rules, instructions); openly fetchable (public domain, open licence, or an open-access page), each 1,500 to 6,000 words; at least six with two named speakers or agents whose exchange changes what the document attributes to whom (dialogues, debates, case reports, histories with two actors, stories with two characters); each with a passage that gives an explanation of why something happened, works, or should be done. Freeze the split in split.json: eight for the arms, four in reserve. Fetch each candidate once to check it exists and to compute the hash; keep no text. Say whose cases they are (other people's) and how you found them (web search; every search and address listed).` },

  { key: 'A3-fourth-clause', prompt: `${PREAMBLE}

YOUR TASK: A3, the fourth-clause collector. Read W8 parts A5 and A6 in full and file 11's Part IV (Three provenances, Selected) and Part XII (Selection in the physical module). The clause: "No member of the history represents \\(t\\), \\(H\\), or the survival condition." Under ${OUT}fourth-clause/, write evidence.md and evidence.json. For every fully open training corpus with published composition you can reach (at least: the Pile; Dolma and OLMo; RedPajama; FineWeb; C4; and any other you find) and for DeepSeek's own published technical reports (DeepSeek-V2, V3, R1 and any V4 report) and for the published descriptions of Claude's training (Anthropic's documentation and papers, including Constitutional AI): does the record state that the corpus contains texts stating a training loss, an optimizer, a preference rule, or a list of principles used as a criterion; does it name the sources (arXiv, GitHub, documentation) from which such texts come; does any published corpus contain, by its own documentation, a document that states the loss function of a model trained on that corpus (the sharpest case: a corpus that includes the paper describing its own model's training)? Quote every claim with its address and today's date; nothing kept as a file; every quotation marked CLAIMED. Then the two readings of the clause, in the theory's words: (i) the strict reading, on which members of \\(H\\) are formal edit-boundary pairs and representation (R) is undefined on them; (ii) the physical reading, which Part XII's "A selected provenance ... is a claim about a physical history" favours, on which the clause reaches the occurrences that realised the pairs; for each, what the evidence makes of it and what the consequence is (W8 A6: if the clause fails, the provenance is declared and "A declared transport does not make an occurrence represent anything"). Then: the sharpest test an open corpus allows, named as a procedure a DeepSeek examiner could run (a search of a corpus index for a named document), and what result would settle A6 either way. Tick W10.3 with the count of open records that state the presence of such texts, quoting each.` },

  { key: 'A4-instrument', prompt: `${PREAMBLE}

YOUR TASK: A4, the instrument. Read HV plan 52 (${ROOT}/HV Skill/tests/52 Marking plan - frozen before the corpus is read.md), plan H63 and results H64 (${ROOT}/HV Skill/tests/H63 Plan - blind second marking by Sonnet 5 of the 96 marked reports.md; ${ROOT}/HV Skill/results/H64 Results - blind second marking by Sonnet 5, agreement with the first marker.md), the old marker programs (${OLDRIG}second_marker.py; the marking/ folder's JSON files for their shape), W3 section 5 (phase 3 and phase 4) and W8 parts B4, C4 and A3. Under ${OUT}instrument/, write the marking plan for this round, frozen before any report is read: criteria.json (machine-readable, one entry per field with its name, its allowed values, its criterion in words a stranger could apply, its layer (the document, the thing under test, the reader), whether it is within-step or cross-step per W8 part B4, and the example that fixes its boundary) and marking-plan.md (the same in prose, with the reasons). Fields required: the eleven tests as RAN / NAME ONLY / ABSENT / CANNOT with plan 52's criteria kept where H64 found them reliable; the three fields H64 struck, each reworded with a written rule (shape's PART boundary; "turned own test"; the same-explanation verdict, now as presence per document with the sentence quoted, never as a count); the three new fields (the eight marks per part, read by document; pairs that pull, named; rivals built, named); the question-identity field (the question the run froze against the one handed in: SAME / MOVED, with the quoted question); the modules-opened field taken from the transport's record and the reader's own list kept apart (W8 part C4, P4.9); the request-as-sent fields (requests per run; PA.1); the arm (e) fields (which ports the skeleton set; marks outside the closed list); the arm (x) fields (which attributions moved under the name exchange). Then the rule for agreement by field and document, the P4.1 baseline rule as W3 fixes it, the marker's conflicts named, the layer named on every report, the three-layer rule (plan 52), and what is struck if a field does not agree in stage B. Every criterion tested against two reports from the record (quote them, ${ROOT}/HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/runs_sonnet5/ or runs_repeat/) to show a stranger could apply it; those two reports are then fitting for that criterion and are named so.` },
]

phase('Build and collect')
const built = await parallel(TASKS.map(t => () =>
  agent(t.prompt, { label: `A:${t.key}`, phase: 'Build and collect', model: 'opus', effort: 'xhigh', schema: SCHEMA })
    .then(r => ({ key: t.key, result: r }))
))
const out = {}
for (const r of built.filter(Boolean)) out[r.key] = r.result
log(`stage A builders returned: ${Object.keys(out).join(', ')}`)

phase('Review')
const summary = Object.entries(out).map(([k, v]) => `## ${k}\nfiles: ${(v.files_written || []).join('; ')}\nwhat it does: ${v.what_it_does}\ndry run: ${v.dry_run}\ncould not settle: ${v.could_not_settle}\nfor the reviewer: ${v.for_the_reviewer}`).join('\n\n')
const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    faults: { type: 'array', items: { type: 'object', properties: { deliverable: { type: 'string' }, file: { type: 'string' }, fault: { type: 'string' }, evidence: { type: 'string' }, forced_fix: { type: 'string' }, severity: { type: 'string', description: 'blocks stage B | blocks stage C | wording' } }, required: ['deliverable', 'file', 'fault', 'evidence', 'forced_fix', 'severity'] } },
    dry_run: { type: 'string', description: 'the dry run you made of the harness on one document for every arm and both transports, sending nothing: commands and outcome' },
    predictions_ticked: { type: 'array', items: { type: 'object', properties: { prediction: { type: 'string' }, verdict: { type: 'string' }, count: { type: 'string' } }, required: ['prediction', 'verdict', 'count'] }, description: 'W10.1 to W10.4' },
    dropped: { type: 'array', items: { type: 'object', properties: { finding: { type: 'string' }, why_dropped: { type: 'string' } }, required: ['finding', 'why_dropped'] } },
    verdict: { type: 'string', description: 'the report in the skill\'s headings' },
    tools_used: { type: 'string' },
  },
  required: ['faults', 'dry_run', 'predictions_ticked', 'dropped', 'verdict', 'tools_used'],
}
const review = await agent(`${PREAMBLE}

YOUR TASK: A5, the reviewer. Four builders have returned; their summaries follow. Read every file they wrote under ${OUT} against plan W10 (sections 3, 4, 5) and against W8's parts they serve (A3, A6, A10, B4, B10, B12, C4 and the predictions). Run the skill's procedure on each deliverable as an explanation of why it does what the plan asks. Then make the dry run yourself: for one document of the corpus (do not fetch it; use the harness's --dry mode, which sends nothing), every arm, both transports, and read what the request as sent would have been; check the skill copy diff; check that no key is read from any file and none is written; check the corpus split and that no source repeats one in the old sources.json or HV file 50; check every criterion of the instrument against the two reports the instrument agent quoted and against one more report of your choosing from the record. Tick W10.1 to W10.4 with counts. Return every fault with the file and the fix it forces, ranked by what it blocks. You may fix a wording fault yourself in the file and say so; anything larger is returned as a fault, not fixed.

THE BUILDERS' SUMMARIES:
${summary}`, { label: 'A:A5-reviewer', phase: 'Review', model: 'opus', effort: 'xhigh', schema: REVIEW_SCHEMA })
out['A5-reviewer'] = review
return out
