# Part A execution index

Written by: OpenAI Codex  
Executed: 21 September 2026 (UTC)

## Scope and outcome

This index covers the twelve staged JSON/Prolog ledger pairs in `part_a/ledgers/new` and `part_a/ledgers/other`. Each pair was validated before one invocation of the unchanged patched rig-1 driver. Every invocation had its own previously nonexistent output directory, raw log, exact stdout report and stderr file. Nothing was appended to either bundled historical raw log.

All twelve JSON documents parsed. In all twelve pairs, the JSON line IDs, Prolog `line/1` declarations and Prolog `line/1` guards matched. All twelve Prolog files parsed under SWI-Prolog with exit code 0. All twelve driver processes returned 0 and had zero recorded timeouts.

Those process exits are not semantic passes. Every raw log contains eight failed optional-predicate queries. Four new-side cases also contain material `denied/1` failures. The printed reports say `NO FAULT FOUND` even when those raw runtime errors occurred. The reports are preserved exactly, but they must not be read as successful answers to the queries that failed.

## Frozen execution components

| Component | Exact path or identity | SHA-256 |
|---|---|---|
| Patched rig-1 driver | `/workspace/scratch/a549554d080c/worktree/Language_handoff/rigs/rig 1 - arguments/patched/run_check.py` | `eff1dee15bebc9771040d52e3e27a75f3b383328d119c7c6e204e0b671b7751b` |
| Patched rig-1 rules | `/workspace/scratch/a549554d080c/worktree/Language_handoff/rigs/rig 1 - arguments/patched/checker_rules.pl` | `7f10c6f40f8618d1be5bcfb2cf1e57d149160b03c6f3fd16ac936fdf71d4d16e` |
| s(CASP) executable | `/home/claude/sCASP/scasp` → `/tmp/sCASP/scasp`; s(CASP) 1.1.4 on SWI-Prolog 9.0.4 | `2110e60890a766b1a630dba595f4e9752f01662ebd5301d61af1fba685fa2ad7` |
| SWI-Prolog | `SWI-Prolog version 9.0.4 for x86_64-linux` | Not a single-file identity |
| Pair validator, written by OpenAI Codex | `part_a/runs/validate_ledger.py` | `15c50515da4fc9bfdcc9f0200b2672b4975337716f40b572210e17c8f3458ecc` |
| Isolated runner, current evidence-writing version | `part_a/runs/run_case.py` | `56bf0b214c61b534a76befacc07944d58ad32a0ef4ffbe4b98bd643b37b78754` |

The execution helper had two evidence-label versions. The six other-side runs plus new-side `L09` and `N03A` used SHA-256 `78391a69035d3d6b948eb18b1570692ed3d79e085d5b2b2c7491b21c06a016be`; the remaining four new-side runs used the current hash shown above. The only change replaced the misleading status labels `PASS_WITH_EXPECTED_OPTIONAL_QUERY_ERRORS` and `PASS` with `RUN_COMPLETED_WITH_EXPECTED_MISSING_OPTIONAL_PREDICATE_ERRORS` and `RUN_COMPLETED_NO_ERRORS`. It did not change validation, commands, error classification, execution or captured output. The generated metadata status strings were then made consistent; no report or raw log was rewritten. The driver, rules, runtime and ledgers were not patched.

## Commands and evidence convention

The exact rendered validation, SWI parse and driver commands for every case are recorded verbatim in that case's `metadata.json` under `commands.validation`, `commands.pl_parse` and `commands.driver`. They instantiate these forms with absolute paths:

```bash
/usr/local/bin/python3 /workspace/scratch/a549554d080c/deliverable/part_a/runs/validate_ledger.py LEDGER.json LEDGER.pl > CASE/validation.json 2> CASE/validation.stderr.txt
swipl -q -f none -s LEDGER.pl -t halt > CASE/pl_parse.stdout.txt 2> CASE/pl_parse.stderr.txt
cd '/workspace/scratch/a549554d080c/worktree/Language_handoff/rigs/rig 1 - arguments' && python3 patched/run_check.py LEDGER.pl CASE/raw_log.txt > CASE/report.txt 2> CASE/driver.stderr.txt
```

Each `metadata.json` also records the side, exact ledger paths and hashes, component paths and hashes, every exit code, the exact report/raw-log/stderr hashes, query-block count, timeout count, every raw `ERROR:` line, and its classification. `validation.json` records the exact JSON, Prolog-declaration and Prolog-guard ID sets.

`RUN_COMPLETED_WITH_EXPECTED_MISSING_OPTIONAL_PREDICATE_ERRORS` means validation and parsing passed and the one driver process ended, but optional queries failed; it does not mean those queries succeeded negatively. `STOPPED_MATERIAL_ERROR` means the first driver output was preserved and no patch or rerun was attempted. The unchanged generic driver itself continued after its child s(CASP) failures and returned 0, so “stopped” describes the case disposition after that invocation, not an early halt inside the driver.

## New-side executions

| Case | Validation / PL / driver exit | Queries / timeouts | Expected optional error blocks | Material error blocks | Status | Metadata |
|---|---:|---:|---:|---:|---|---|
| `ledger_L09` | `0 / 0 / 0` | `11 / 0` | 8 | 0 | Run completed with optional-query errors | `new/ledger_L09/metadata.json` |
| `ledger_N03A` | `0 / 0 / 0` | `13 / 0` | 8 | 2 | Stopped on material error | `new/ledger_N03A/metadata.json` |
| `ledger_N03B` | `0 / 0 / 0` | `12 / 0` | 8 | 1 | Stopped on material error | `new/ledger_N03B/metadata.json` |
| `ledger_N05A` | `0 / 0 / 0` | `11 / 0` | 8 | 0 | Run completed with optional-query errors | `new/ledger_N05A/metadata.json` |
| `ledger_T02B` | `0 / 0 / 0` | `13 / 0` | 8 | 2 | Stopped on material error | `new/ledger_T02B/metadata.json` |
| `ledger_T02D` | `0 / 0 / 0` | `14 / 0` | 8 | 3 | Stopped on material error | `new/ledger_T02D/metadata.json` |

| Case | Ledger JSON SHA-256 | Ledger PL SHA-256 | Exact report SHA-256 | Raw-log SHA-256 |
|---|---|---|---|---|
| `ledger_L09` | `c1cbe1daa4736ce6775f3f0a9837e665fae0bfb5278c05a24b856f7cc1ac3cd5` | `92f0d057f794362b50273d6126bd67668859550f652764e21c83e06239a7c8b4` | `bea5824a875b1c2da10833fd141c80133ff623f762ec52e6867b0f9494bd03af` | `225b7d2c1275cbd029aeb59035c1121f892689b37c5fa2c1316975dd2a8bf7ad` |
| `ledger_N03A` | `3a9dfbdacb6468b5206393c7f3e5cd7a48b26c33094461f8175bd9d42e53447e` | `5174382e78278af5d08761fab04d09eaf7312b5a2925585fbe14c1b7790a33e4` | `a25e2e22ff25d2cdb95ce0dc4e949ffc6efe436be568a8dda02c858ae72b711b` | `444e58cf428fe60847e53a660fa7e3caf3c52386f9361d6125ec9e1a7b57ceb1` |
| `ledger_N03B` | `8273cdf94a81c5f744f1235e7a507898564cb916f796cafac9a387a6986300a1` | `30ef29f8edcd35636e8227103dd70415fc920d49a34e07948a24d9269bc9a80f` | `23d2676b98879449fd79c04b7ab623cd09df37f8e1a86b03b937bbee345d1900` | `23557e9808fc5952b79ec2825c0f2d865fdab460684d4d21479300794943e5e3` |
| `ledger_N05A` | `7fa16019d166de80438d58e007db339854f56939f60fff526e3a56aa16e11b1f` | `0d7d0ba9f798cf217c8e2c9aa0b70addc9aa840af62330cb438895ad5dd18f5e` | `0179ff0935f2482f244b94054adce7a827005567d6a6ccec00f2b148b8efdc2d` | `083c8877479082a801dc098f6cc95a7453eb8ece32cf7250ac604f45f11962cd` |
| `ledger_T02B` | `ecfa2f473ec85fc31b1d0992626fa61ac278a7dc5368bda7e37c2159f7a336d1` | `22769617066f50f50bd400c9fcc72531efdd11b582e19ea6691f2b6d738cead5` | `49d8b52f6160cd03c5b450458bb0580ffd5a6e3b0eeddfa8e953a31ab60f73d1` | `62d052bca810e7837073fa4ebfa7999e84ee1cb28e489d987cc45adb1b157f32` |
| `ledger_T02D` | `d130f72dbcc6b30c03e9ad952c7d077c201dbdb8dccb8bc80af7f5818d668658` | `133cf475c7c6a86d0d1c5de068342f1de84d6abafa148a4bd670f0d787a154a0` | `26ab0deccde5de32363149b2b0feed4fd4732ec052ddee95176b2f0d91152bcc` | `c10c7f3758a3eb7e06ff1c124d01acec8543d0018c2ffd9e116b62beae9119d1` |

## Other-side executions

| Case | Validation / PL / driver exit | Queries / timeouts | Expected optional error blocks | Material error blocks | Status | Metadata |
|---|---:|---:|---:|---:|---|---|
| `ledger_L09_other` | `0 / 0 / 0` | `11 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_L09_other/metadata.json` |
| `ledger_N03A_other` | `0 / 0 / 0` | `12 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_N03A_other/metadata.json` |
| `ledger_N03B_other` | `0 / 0 / 0` | `12 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_N03B_other/metadata.json` |
| `ledger_N05A_other` | `0 / 0 / 0` | `11 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_N05A_other/metadata.json` |
| `ledger_T02B_other` | `0 / 0 / 0` | `12 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_T02B_other/metadata.json` |
| `ledger_T02D_other` | `0 / 0 / 0` | `12 / 0` | 8 | 0 | Run completed with optional-query errors | `other/ledger_T02D_other/metadata.json` |

| Case | Ledger JSON SHA-256 | Ledger PL SHA-256 | Exact report SHA-256 | Raw-log SHA-256 |
|---|---|---|---|---|
| `ledger_L09_other` | `78ec42fa403f338ae4bfc7cdec45a6a3db3c7048b04b019b9acf71a984709e9c` | `a13444931f8425025f8c530e80ca41c857243b8f8a214714f1d404ae97d426b2` | `3dd3b236fdba4febafa5d8ee1aa3d4ce7f8451cb31a288c99c6f5bd5a9a86236` | `584d88f9109068a5c5a690cf5f8ad7bbc48c7345dc225e9cce50b3f234d65c7a` |
| `ledger_N03A_other` | `f9cc006467e25e9d3eb237bafb86b6a763c90959a298707d8d0c846b6706a7c7` | `815bd22afb5b859819bf63b9409efb5e3cf9122a34b4a2aed17e6f093eeb9bb7` | `d45d1a39e62200317ec65041ad2a661341fdc08d2606d787cc76a177043e489d` | `a66650c541ec01ff20493d8de3008e310fba622a0fb643b70fa01b42ca63a26d` |
| `ledger_N03B_other` | `6521bda9b9fc6316a47c190b12d6fd037fe8debd2db9da2fce49e11fc301e9d7` | `d7da0b470acd9deb0909a33437d0491165379fbdbd59121080760c39a6b35b2f` | `b51737db99bd9fbefdfd8bcdc28e0da5ec7763645f36012fbb196c0d7a2f2720` | `7d1e94a5a9ed1dfaf23fbb3f57d49a56d6d7e0b3748b5047ba5bb5a37044dac0` |
| `ledger_N05A_other` | `fa623c38869c8ad37efeae840e34bbae5969f8c8c22135b5b241400df9cb7266` | `a13444931f8425025f8c530e80ca41c857243b8f8a214714f1d404ae97d426b2` | `b9cd9c7c72389fe96d4c92031cbacf058199a61c04fb0adc713f7a94af55fbbd` | `84653e0479779111ea12d000a9cc7b32ebb46db7a39d0256855621381412974c` |
| `ledger_T02B_other` | `677fd08fb2d268f4dfdb43dd70849c5f0c6f1cc10a80900e638e8697cf7735cc` | `c4d93281bf57cec92320d638db310a57e2b42e71f3fa3ae844aa315dfeada1c1` | `fe5b049f398b12eba375edfb5a8631eb4a6c44be9b5e31ce4a60ed4515f1a334` | `60c5a40237922b2e29798b62a3896d196e1c5f8ea5b72f6f12b454dab5c2a077` |
| `ledger_T02D_other` | `d26f63e5126562c8683ac9c23e24222724d2df6ca777b4314f824303e1dd223d` | `6a7d7a07d148012371a800dd1c4fdc9ae1a4041bac4575ab06ae5210ace686e5` | `96d3b8ea0ba159c2f06cf1bd03dc15385b781c712d98d22901b5dd00b16482a4` | `2de93a0578a6408862e779586997df41a3bdad9f12c0157c28e95fa569985927` |

Every `driver.stderr.txt` was empty, with SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## ERROR classification

Every invocation produced the same eight expected missing-optional-predicate error blocks: `claim_because/3` twice, `claim_since/3` twice, and `claim_plan/3`, `claim_like/3`, `exempt/2` and `denied_because/3` once each. Their full `ERROR:` lines and query headers are retained under `expected_missing_optional_predicate_errors` in each metadata file. They are errors from generic questions whose input-specific predicate is absent; they are not successful “no answer” results.

The material errors were all failed `denied/1` queries:

| Side and case | Exact failed query |
|---|---|
| new, `ledger_N03A` | `denied(has_red_colouring(pear))` |
| new, `ledger_N03A` | `denied(has_yellow_skin(pear))` |
| new, `ledger_N03B` | `denied(red_stained(finger))` |
| new, `ledger_T02B` | `denied(belong_to(feathers,kingfisher))` |
| new, `ledger_T02B` | `denied(unharmed(feathers))` |
| new, `ledger_T02D` | `denied(belong_to(feathers,kingfisher))` |
| new, `ledger_T02D` | `denied(burned(feathers))` |
| new, `ledger_T02D` | `denied(caught_fire(kingfisher))` |

These are material because `denied/1` is part of the core rule vocabulary and the driver issued each query while checking facts it had actually enumerated. In each block s(CASP) reported `scasp_predicate 'denied/1' does not exist`. The driver did not inspect the s(CASP) return code; its parser found no `% Answer` blocks and treated the failed query as an empty answer set. The later `NO FAULT FOUND` line therefore cannot certify those checks.

No other-side raw log contains a `denied(...)` query header. Those ledgers place their lines inside TOLD cases, which the driver removes from the actual-world `holds(F)` enumeration before this check. Consequently, zero other-side `denied/1` errors does not show that the denial route worked there; it was not exercised.

## Parse warnings

SWI-Prolog emitted only discontiguous-clause warnings, with parse exit 0, for `N03A`, `N03B`, `T02B` and `T02D` on both sides. The exact warnings are preserved in each affected `pl_parse.stderr.txt`. `L09` and `N05A` on both sides had empty parse stderr. No warning was changed or suppressed.

## What the run establishes

Seen: all staged JSON files parse, their line IDs and guards match their paired Prolog files, all Prolog files parse, the installed runtime is callable, twelve isolated driver processes completed, and no query timed out.

Seen: the raw logs contain the optional-query failures above, and four new-side logs additionally contain material core-query failures, while every printed report says `NO FAULT FOUND`.

Worked out from the unchanged driver and the raw output: the printed reports are incomplete whenever a queried predicate was absent, because a failed s(CASP) subprocess and a successful query with no model both become an empty answer list at the report layer.

This does not establish that any ledger is fault-free. It also does not compare the translations, decide sameness, repair the adapter, or patch the rig. The first outputs remain the evidence.
