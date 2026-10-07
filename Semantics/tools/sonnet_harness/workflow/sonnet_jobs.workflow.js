export const meta = {
  name: 'semantics-sonnet-jobs',
  description: 'Run narrow Sonnet jobs from task specs of the Semantics Sonnet harness; verify each by script; escalate any failure or mismatch to Opus',
  whenToUse: 'Mechanical or extraction jobs of the Semantics review rounds that have a task spec in Semantics/tools/sonnet_harness/specs/ (decisions S16, S42)',
  phases: [
    { title: 'Work', detail: 'one Sonnet agent per task spec, one job each', model: 'sonnet' },
    { title: 'Verify', detail: 'a fresh Sonnet agent re-runs the spec check by script', model: 'sonnet' },
    { title: 'Opus', detail: 'Opus reads every failed or mismatched job, and checks every extraction sheet', model: 'opus' },
    { title: 'Known answers', detail: 'optional: specs run once every job has ended (e.g. comparison with finished work)', model: 'sonnet' },
  ],
}

// args (built by the orchestrator, one brief per spec, each the JSON printed by
//   python3 -B Semantics/tools/sonnet_harness/run_task.py "<spec>" --phase brief --run <label>):
//   { jobs: [brief, ...], after: [brief, ...] (optional), opus_check_extraction: true (default) }
// Sonnet never judges a finding, writes maths or reviews (decision S16). Its prompts are short and schema-bound.
// Omitting `model` on the Opus agents would inherit the session's model; it is named so that S16 holds whatever
// the session runs on.

const A = args || {}
const JOBS = A.jobs || []
const AFTER = A.after || []
const OPUS_CHECK_EXTRACTION = A.opus_check_extraction !== false
if (!JOBS.length && !AFTER.length) throw new Error('no jobs: pass args.jobs, each the output of run_task.py --phase brief')

const RESULT = {
  type: 'object',
  required: ['ok', 'escalate', 'digest', 'checks_failed', 'trouble'],
  properties: {
    ok: { type: 'boolean', description: 'the "ok" field of the last command\'s JSON, as printed' },
    escalate: { type: 'boolean', description: 'the "escalate" field, as printed' },
    digest: { type: 'string', description: 'the "digest" field, as printed' },
    checks_failed: { type: 'array', items: { type: 'string' }, description: 'the "checks_failed" field, as printed ([] if absent)' },
    trouble: { type: 'string', description: 'one line: what went wrong running the commands; empty if nothing' },
  },
}

const OPUS_VERDICT = {
  type: 'object',
  required: ['cause', 'what_is_wrong', 'next_step'],
  properties: {
    cause: { type: 'string', enum: ['inputs or harness at fault', 'job output wrong', 'passes on reading', 'cannot tell'] },
    what_is_wrong: { type: 'string' },
    next_step: { type: 'string' },
  },
}

const SPOT = {
  type: 'object',
  required: ['rows_checked', 'rows_to_change', 'passages_missing'],
  properties: {
    rows_checked: { type: 'integer' },
    rows_to_change: {
      type: 'array',
      items: {
        type: 'object',
        required: ['item', 'reader', 'said_now', 'said_should_be', 'reply_lines', 'why'],
        properties: {
          item: { type: 'string' }, reader: { type: 'string' }, said_now: { type: 'string' },
          said_should_be: { type: 'string' }, reply_lines: { type: 'string' }, why: { type: 'string' },
        },
      },
    },
    passages_missing: {
      type: 'array',
      items: { type: 'object', required: ['reader', 'reply_lines', 'items'], properties: { reader: { type: 'string' }, reply_lines: { type: 'string' }, items: { type: 'string' } } },
    },
  },
}

const COMMON = (j) => [
  `You run ONE job of the Semantics project's Sonnet harness: ${j.id}.`,
  `What it is: ${j.purpose}`,
  `Never: ${(j.never || []).join('; ')}.`,
  `Never open a file whose name holds "key" or ".env". Never run git. Never call an outside model. Write only inside ${j.out_dir}. Run every command from /home/user/ThreadSmith with the Bash tool's timeout at 600000 ms.`,
]

function workerPrompt(j) {
  const L = COMMON(j)
  if (!j.agent) {
    if (j.long) {
      L.push('Steps:',
        `1. Run: ${j.commands.all_background}`,
        `2. Run: ${j.commands.all_wait}`,
        '   If its JSON says "running": true, run step 2 again (at most 6 times).')
    } else {
      L.push('Steps:', `1. Run: ${j.commands.all}`)
    }
    L.push('Last: return the fields the schema asks for, copied from that command\'s JSON as printed. Do not interpret or change them.')
  } else {
    L.push('Steps:',
      `1. Run: ${j.commands.run}`,
      '2. Your job:',
      ...j.agent.instructions.map((s) => '   - ' + s),
      `   Read only: ${j.agent.read.join(' | ')}`,
      `   Write only: ${j.agent.write}`,
      `3. Run: ${j.commands.check}`,
      '   If it fails on the form of your file (schema errors, missing rows), fix the file once and run step 3 again. Do not change your answers to make a check pass.',
      'Last: return the fields the schema asks for, copied from the step 3 JSON as printed.')
  }
  return L.join('\n')
}

function verifyPrompt(j) {
  return [
    `Run exactly this one command from /home/user/ThreadSmith (Bash timeout 600000 ms), and nothing else:`,
    j.commands.verify,
    'Return the fields the schema asks for, copied from its JSON as printed. Do not open, edit or rerun anything else.',
  ].join('\n')
}

function escalatePrompt(j, w, v) {
  return [
    `A job of the Semantics Sonnet harness did not pass. Job ${j.id} (${j.kind}): ${j.purpose}`,
    `Spec: ${j.spec}. Its files: ${j.out_dir} (result.*.json, and the files its checks name).`,
    `The Sonnet worker reported: ${JSON.stringify(w)}`,
    `The verifier (a second agent running the spec's check by script) reported: ${JSON.stringify(v)}`,
    'Read the result files and the files they name. Say which: the inputs or the harness are at fault; the job\'s output is wrong (say where); it passes on reading and the reports differ only in form; or you cannot tell.',
    'Write nothing outside that folder; change no file of the project; commit nothing. Never open a key file.',
  ].join('\n')
}

function spotPrompt(j) {
  return [
    `Check a tabulation sheet filled by a Sonnet agent (job ${j.id}). You rule on nothing: you check the extraction.`,
    `Sheet: ${j.agent.write}. Replies: ${j.agent.read.filter((p) => p.endsWith('.txt')).join(' | ')}.`,
    'Do not open any other file of the project (in particular no tabulation written by anyone else).',
    '1. For every row whose "said" is not "challenges", read the reply around the passages it names and say whether some point of that reader on that item does one of: says the maths says other than the sentence; says a counterexample tells against the text; says the text settles an invention (an I, H or U item) or should carry wording that settles it; gives a counterexample to a claim that held; proposes a change for a round-1 matter; proposes any change to the text, the maths or the register. List each row that should be "challenges" (or any other mark).',
    '2. Read both replies whole and list any passage about an item that no row names.',
    `Write the same JSON you return to ${j.out_dir}/opus_check.json (the only file you write). Return rows_checked (how many rows you read), rows_to_change, passages_missing.`,
  ].join('\n')
}

phase('Work')
const results = await pipeline(
  JOBS,
  (j) => agent(workerPrompt(j), { label: `sonnet: ${j.id}`, phase: 'Work', model: 'sonnet', schema: RESULT }),
  async (w, j) => {
    const v = await agent(verifyPrompt(j), { label: `verify: ${j.id}`, phase: 'Verify', model: 'sonnet', effort: 'low', schema: RESULT })
    const passed = !!(w && v && w.ok && v.ok && w.digest === v.digest)
    let escalation = null
    let spot = null
    if (!passed) {
      escalation = await agent(escalatePrompt(j, w, v), { label: `opus: ${j.id}`, phase: 'Opus', model: 'opus', schema: OPUS_VERDICT })
    }
    if (j.kind === 'extraction' && OPUS_CHECK_EXTRACTION && j.agent && j.agent.read) {
      spot = await agent(spotPrompt(j), { label: `opus check: ${j.id}`, phase: 'Opus', model: 'opus', schema: SPOT })
    }
    return { id: j.id, kind: j.kind, out_dir: j.out_dir, worker: w, verifier: v, passed, escalation, spot }
  },
)

let after = []
if (AFTER.length) {
  phase('Known answers')
  after = await parallel(AFTER.map((j) => () =>
    agent(workerPrompt(j), { label: `known answer: ${j.id}`, phase: 'Known answers', model: 'sonnet', effort: 'low', schema: RESULT })
      .then((r) => ({ id: j.id, out_dir: j.out_dir, result: r }))))
}

const done = results.filter(Boolean)
log(`${done.filter((r) => r.passed).length} of ${JOBS.length} jobs passed; ${done.filter((r) => r.escalation).length} escalated to Opus`)
return { jobs: done, after: after.filter(Boolean), missing: JOBS.length - done.length }
