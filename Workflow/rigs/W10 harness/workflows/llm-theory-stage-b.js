export const meta = {
  name: 'llm-theory-stage-b',
  description: 'Plan W10 stage B (plan W14): every marking prompt under the harness stage-B folder marked by one Sonnet 5 subagent at effort high, armed with the hard-to-vary skill, five at a time; each writes one JSON of marks',
  phases: [{ title: 'Mark', detail: 'one Sonnet 5 marker per prompt, five at a time' }],
}
const ROOT = '/home/user/ThreadSmith'
const SKILL = `${ROOT}/HV Skill/authority/33/hard-to-vary/`
const jobs = (args && args.prompts) || []
const POOL = (args && args.pool) || 5
const SCHEMA = {
  type: 'object',
  properties: {
    prompt_file: { type: 'string' },
    output_path: { type: 'string', description: 'the path the prompt named, where you wrote the JSON' },
    keys_written: { type: 'integer' },
    nulls: { type: 'array', items: { type: 'string' }, description: 'fields you left null, with nothing else' },
    files_read: { type: 'array', items: { type: 'string' }, description: 'every file you read, by path' },
  },
  required: ['prompt_file', 'output_path', 'keys_written', 'nulls', 'files_read'],
}
function prompt(p) {
  return `You are one marker of stage B of plan W10 (Workflow project, plan W14). You are armed with the hard-to-vary skill and held to it.

FIRST read the skill in full, once: ${SKILL}SKILL.md, then references/the-idea-in-depth.md, building.md, testing-against-cases.md, reporting.md, question-bank.md, word-list.md in ${SKILL}references/. One correction you carry: the skill's word list maps "fitted" to an older, unqualified Derivation 3; the authority qualifies it: "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not." Never use the unqualified form.

THEN read exactly one more file, your marking prompt: ${p}
Do what it says: mark the one report it contains, field by field, by the criterion given for each field and nothing else, and write one JSON object with one key per field, once, with the Write tool, to the output path the prompt names at its end. Where a field's values are a closed list, use one of them exactly; where you cannot tell, use null. Never guess. Never read any other file, folder, mapping, index or report: the marking is blind, and a Read of anything but the skill files and this prompt strikes your mark. Do not run shell commands. Do not edit anything.

Your final message is data, not prose: return the structured output only (the prompt file, the output path, the number of keys, the fields left null, every file you read).`
}
const results = []
const queue = jobs.map((p, i) => ({ p, i }))
async function worker(w) {
  while (queue.length) {
    const { p, i } = queue.shift()
    const name = p.split('/').pop().replace('.txt', '')
    const r = await agent(prompt(p), { label: `mark:${name}`, phase: 'Mark', model: 'sonnet', effort: 'high', schema: SCHEMA })
    results.push({ i, prompt: p, result: r })
    if (results.length % 10 === 0) log(`${results.length} of ${jobs.length} marked`)
  }
}
await Promise.all(Array.from({ length: POOL }, (_, w) => worker(w)))
results.sort((a, b) => a.i - b.i)
return { marked: results.length, results }
