# Local checker setup and smoke verification

Author: OpenAI Codex. Knowledge labels: **seen** for command outputs and files; **worked out** for the report comparison.

The required runtime already existed locally. SWI-Prolog is `/usr/bin/swipl` (version 9.0.4). The supplied drivers’ expected path `/home/claude/sCASP/scasp` resolves to the existing executable `/tmp/sCASP/scasp` (s(CASP) 1.1.4). No installer, package installation, git command, repository read, network request, or GitHub action was performed. The installer was inspected as supplied text, but not run: it would clone from GitHub, contrary to the owner’s instruction, and the required runtime was already available.

The exact supplied rig-1 smoke command was run on the existing T05B ledger, with only its output-log path redirected to this return folder. It exited 0. Its report matches `tools/smoke_expected_report_T05B.txt` after omitting the GAUGE line, as `rigs/READ ME FIRST.md` requires for timing comparisons. The actual GAUGE also matches all expected substantive fields: 2 said lines, 0 filled-in lines, 0 usual-case lines, 1 of 3 sentences with bin material, and the same quoted-command explanation. Only the recorded timing differs (0.04 rather than 0.05 seconds).

The raw log is nonempty (9,094 bytes), contains an actual s(CASP) answer for `holds(F)` with `F = folded(ada,note)` and line 1, and has no timed-out questions. Missing-predicate errors for unsupported query categories remain in the raw log exactly as printed; the handoff explicitly describes these as expected for absent line kinds. Raw outputs have not been altered to insert author text; this note and `setup_receipt_OpenAI_Codex.json` identify their collector and commands.

Supplied checker files, source passages, and ledgers were not edited. No corpus passage or sealed key was read during setup. The joined script’s hard-coded rig-2 path was noticed, but no joined execution is required by this handoff and no modification was made.
