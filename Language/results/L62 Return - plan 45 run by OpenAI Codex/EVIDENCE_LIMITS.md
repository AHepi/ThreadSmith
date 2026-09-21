# Evidence-tool limits

Written by: OpenAI Codex

The exact reports and raw solver streams are primary evidence. The assistant-written wrappers improve isolation and receipts but do not certify the historical drivers.

`run_pair.py` passes the exact driver path, ledger path and fresh raw-log path to Python. Its `--rules` argument is recorded and hashed but is not injected into the historical driver. The four driver sources themselves load a fixed colocated file: each rig-1 driver opens `checker_rules.pl` beside itself and each rig-2 driver opens `laws.pl` beside itself. The driver path and hash are therefore the binding evidence; the recorded rules hash is a checked companion identity, not proof created by the wrapper. Likewise, `case_id`, `rig`, `version` and `role` are descriptive labels. Exact command paths and hashes take precedence over them.

`run_pair.py` has no child timeout. Every returned invocation did finish, and its exit file, stdout, stderr and raw log are present, but the helper should not be reused as an unattended hang-safe runner. Its JSON/Prolog line check is structural and its SWI load is a syntax/load check, not a semantic validation. The returned ledgers contain no load-time directive lines.

`run_direct_query.py` records the rules and ledger paths and hashes, query text, removed line identifiers, runtime hash, solver outputs, exit and timeout state. It deletes the temporary composed program and does not record that temporary file's own hash. The program can be reconstructed from the preserved helper version and receipt, but this is weaker than retaining the exact runtime file. Its line-removal expression is textual rather than a Prolog parser. The only removal used for adjudication was N23-A's `s1`; in that ledger the first and only declaration text `line(s1).` precedes the guarded clause, and the helper required exactly one substitution.

Both helpers hash component files after execution rather than atomically binding an immutable snapshot. The source-identity report shows that every supplied bundle file remained byte-identical through packaging, and each run used a new isolated output directory, but that does not turn the wrappers into a cryptographic execution sandbox.

The helpers count answers and errors heuristically. In particular, `run_pair.py` does not recognise s(CASP)'s wording `scasp_predicate ... does not exist` as a missing-predicate error. The per-slice execution summaries therefore reclassify errors from the raw text predicate by predicate. No answer count, wrapper exit, `NO FAULT FOUND`, `Fine`, or `JUMP` is treated as a clean semantic result when its bearing query errored.
