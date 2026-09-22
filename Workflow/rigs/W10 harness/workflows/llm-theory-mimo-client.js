export const meta = {
  name: 'llm-theory-mimo-client',
  description: 'Addendum W12: one Opus 5 agent at xhigh researches the MiMo 2.6 Pro API on the web and writes the client with a dry run, under the hard-to-vary skill; nothing sent, no key',
  phases: [{ title: 'Client', detail: 'one Opus 5 agent at xhigh' }],
}
const ROOT = '/home/user/ThreadSmith'
const SKILL = `${ROOT}/HV Skill/authority/33/hard-to-vary/`
const W10 = `${ROOT}/Workflow/tests/W10 Plan - getting the LLM theory right; the harness, the corpus, the fourth clause, the instrument, the arms, the cross-examination.md`
const W12 = `${ROOT}/Workflow/tests/W12 Addendum to W10 - MiMo 2.6 Pro as a third examiner family in stage E (decision W8).md`
const OUT = `${ROOT}/Workflow/rigs/W10 harness/code/clients/`
const SCHEMA = {
  type: 'object',
  properties: {
    files_written: { type: 'array', items: { type: 'string' } },
    what_was_found: { type: 'string', description: 'endpoint, model id, auth, context, output ceiling, rate limits, tool calling, system message, prefill; each CLAIMED with address and date' },
    could_not_find: { type: 'array', items: { type: 'string' }, description: 'open questions for the owner' },
    dry_run: { type: 'string' },
    claims: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, evidence: { type: 'string' }, tag: { type: 'string' }, would_count_against: { type: 'string' } }, required: ['claim', 'evidence', 'tag', 'would_count_against'] } },
    dropped: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, why: { type: 'string' } }, required: ['item', 'why'] } },
    tools_used: { type: 'string', description: 'every tool; every shell command; every search and fetched address; whether any file was written outside the clients folder' },
  },
  required: ['files_written', 'what_was_found', 'could_not_find', 'dry_run', 'claims', 'dropped', 'tools_used'],
}
const PROMPT = `You are the client builder of addendum W12 to plan W10. You work under the hard-to-vary skill and will be held to it.

FIRST read the skill in full, once: ${SKILL}SKILL.md, then references/the-idea-in-depth.md, building.md, testing-against-cases.md, reporting.md, question-bank.md, word-list.md in ${SKILL}references/. One correction you carry: the skill's word list maps "fitted" to an older, unqualified Derivation 3; the authority, file 11, qualifies it: "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not." Never use the unqualified form.

THEN read ${W12} in full, W10 section 2 and stage E in ${W10}, and the two existing clients and their read-me in ${OUT} (deepseek_client.py, atria_client.py, README.md): your client has their shape and their seam.

YOUR TASK. Find out on the web what "MiMo 2.6 Pro" is and how it is called (search: "MiMo 2.6 Pro API", "Xiaomi MiMo API", "MiMo-V2.6", "mimo api key tp-", the provider's platform documentation; the owner's key begins with "tp-", which may identify the platform). Quote the documentation with addresses and today's date; everything read outside the repository is CLAIMED. Establish: the base URL and endpoint(s); the exact model id (case); authentication header; context length; the maximum output tokens; rate and concurrency limits; whether tool calling, a system message and a prefilled assistant message are supported; the price if the provider states it. Then write ${OUT}mimo_client.py: an OpenAI-compatible chat client on the two existing clients' shape (the same four-value send seam so a driver written for one holds the other), retries with backoff, the request body and the reply both returned whole, the output ceiling at the documented maximum as a parameter, at most five worker threads (the owner's limit for DeepSeek, applied here) or fewer if the provider's limit is lower, base URL and model id overridable by MIMO_BASE_URL and MIMO_MODEL, the key read from the environment as MIMO_API_KEY at call time only and written to no file (use rig.assert_no_key or the clients' own guard as they do), and a --dry flag that builds every request shape stage E needs and checks it sending nothing. Add a section to ${OUT}README.md for it, with what you found, what you could not find (questions for the owner), and the one-request live check Claude will run. If the service cannot be found at all, write the client against the most likely interface with MIMO_BASE_URL required and say so plainly.

RULES. Write only under ${OUT} (the new file and the read-me section; do not edit the two existing clients). No key exists in the environment; send nothing to any API; never write a key. Shell only for python3 dry runs of what you wrote. SELF-FALSIFICATION before you return: for every claim about the service, say what would show it wrong and whether you looked. Your final message is data, not prose: return the structured output only.`
const r = await agent(PROMPT, { label: 'client:mimo', phase: 'Client', model: 'opus', effort: 'xhigh', schema: SCHEMA })
return r
