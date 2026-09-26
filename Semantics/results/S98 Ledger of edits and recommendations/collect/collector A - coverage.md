# Collector A - coverage

Collector A's stretch is every edit made to the theory, and every change proposed to it, before file 11 (revision 1, log S76) was written. The ledger beside this file, `collector A.jsonl`, holds 321 records, one JSON object per line, in the order of the rounds. It was built by program (`collector A - scripts/build.py` with `lib.py`); a rerun gives the same bytes (md5 of the ledger: 7701ffbae274a17ea51836f8575f59f7). The checks below come from `collector A - scripts/check.py`. The repository was read at commit 81e7ac0d98a8b0d8f278155d3833f50fe9272506. Nothing was committed.

Most records are written against file 10. The R2 family was written against file 20, the other model's revision of file 10, which is not in the repository; from log S69 the rounds read R2 as amendments to file 10.

## The groups

| Records | round | Source | What each record holds | kind and status |
|---|---|---|---|---|
| A-1 to A-26 | file 20 (before log 25) | `results/S62 Stage D and report - return/07 Quotations.md`, earlier and revised passages side by side; the anchoring block from `04 Two anchoring passages.md` | Each place where the other model's quotation of file 20 differs from its quotation of file 10. old is file 10's own sentence at its line; new is the quoted file 20 wording. A one-sentence replacement is cut to the changed span, and both whole sentences are kept. A passage file 20 adds has an empty old and the nearest file 10 line as target_line. | edit; declined (file 20 set aside, decision S4) |
| A-27 to A-163 | R2 (log 25) | `results/S64 Near cases - return/05 Quotations.md`, rows S64-R2-A01 to J02, cut into sentences; `results/S62 .../07 Quotations.md`, rows R2-A-1 to R2-H-41 and R2-extra-C | Every recovered sentence of the R2 amendments, A to J, in amendment order. old is empty: the file 20 wording each one replaces was never quoted. target_part names the Parts the sentence (or the sentence before it) names, with file 10's Part titles. | recommendation; 134 not applied; 3 applied in other wording in file 11 (J on Part VI, file 11 line 301; J on Part XVI.3, two sentences) |
| A-164 to A-237 | Stage B (logs 41, 55) | `results/55 Stage B return ...`, table rows 33 to 112 (row number = file line + 18) | The phrase cell of each row as printed, underline tags kept. new_sentence holds the R2 sentence or sentences the phrases sit in, and same_as points at those records. | recommendation, span; status taken from the R2 sentence (4 applied, 70 not applied) |
| A-238 to A-245 | round 4 (log 28) | `tests/28 ...`, lines 8 and 11 | Clauses A-prime (4 sentences) and C-prime (4), Claude's own | recommendation; superseded by A-second and C-second |
| A-246 to A-258 | round 5 and Stage C (logs 29, 30) | `tests/30 ...`, lines 21 and 23 | Clauses A-second (7) and C-second (6). A-second recurs verbatim in the S62 A fix card, listed in source_ref. | recommendation; superseded |
| A-259 to A-271 | S62 (log S63) | `results/S62 .../01 Fix cards.md` | The sentences the other model tagged [yours] in the four boxed clauses: A (1), C (8, the local replacement for C-second), G (2), H (2). The [R2] sentences in the same boxes are the R2 records; the [an outside author's] sentences are A-second. | recommendation; A, C and H superseded (11); G not applied (2) |
| A-272 to A-280 | S64 (log S65), S65 (log S70) | `results/S64 .../02 Tighter pairs and fix cards.md`, `results/S65 .../02 ...` | Clauses H64, I64 and H65, three sentences each, kept verbatim through S70 and S72 | recommendation; superseded |
| A-281 to A-301 | S70 (log S71) | `results/S70 .../06 Report addendum.md`, heading (11) | The 21 lines of the clarifying-draft list (20 marked WORDING, 1 CLAIM) | recommendation; superseded (S72 Stage 2 rebuilt the list) |
| A-302 to A-315 | S72 (log S75) | `results/S72 Stage 2 audit - return/05 Report addendum.md`, heading (11); the box in `04 Fix card for Derivation 3.md` | D3-1 and D3-2 (Derivation 3 restated) and W01 to W12 | recommendation; applied in other wording in file 11 (logs S75, S76) |
| A-316 to A-320 | S75 | `results/S75 Results ...`, point 4 and "Proposed change to file 10" | The restated claim, the consequence, grievance 3, attack (D) and the Part XV entry | recommendation; applied in other wording in file 11 |
| A-321 | S76 | `records/Semantics - project story.md`, log S76 | The four-sentence patch made first and not kept | edit; superseded; no wording given |

## Status words as used here

- **applied**: a later text carries the change; applied_in names the text and says "in other wording" (no record in this stretch is carried word for word; checked by program).
- **not applied**: no later text carries it, and no later proposal in this stretch names it as a source.
- **superseded**: a later proposal took its place; same_as names the later records where the link is known.
- **declined**: set aside by the owner (file 20, decision S4).

## same_as as used here

Links run both ways. A sentence that recurs word for word in several sources is one record, and the other places are listed in its source_ref. same_as joins records of three kinds:

1. A Stage B phrase row and the R2 sentence records its phrases sit in.
2. A later restatement and a proposal the later source names as its source: A-second and the S62 A sentence to S70 line 3 and W01 (W01 cites "A-S62A"); C-second and the S62 C sentences to S70 lines 2 and 4, and the S62 C sentences to W02; the S62 H sentences to S70 line 13; H64 to S70 line 14 and W07; I64 to S70 line 17 and W12; H65 to S70 line 15 and W08 (W08 cites T-C03, which is H65); the S70 CLAIM line, R2 J's two Part XVI.3 sentences, D3-1, D3-2 and the S75 restated claim; the S76 patch to the S75 records. A-prime and C-prime link to the A-second or C-second sentence nearest in wording, and C-second to the nearest S62 C sentence (similarity by program, threshold 0.45).
3. S70 lines and S72 W lines on the same cases, matched by Claude from the case numbers each row cites, not named by either source: S70 lines 2, 3, 5, 6, 9, 10, 14, 15, 16 and 17 to W02, W01, W03, W06, W10, W09, W07, W08, W11 and W12.

## Checks by program

| Check | Result | Misses |
|---|---|---|
| Every old recorded against file 10 is found verbatim in file 10 | 26 of 26 | none |
| The same, for the records with status applied | 7 of 7 | none |
| Each such old is on its target_line of file 10 | 26 of 26 | none |
| old inside old_sentence | 26 of 26 | none |
| new inside new_sentence | 241 of 241 | none |
| new found byte for byte in its source_file (the 3 records with no wording left out) | 318 of 318 | none |
| Stage B: every underlined phrase of the row is inside its new_sentence | 66 of 74 | A-164, A-177, A-180, A-188, A-191, A-205, A-210, A-214: each holds one or two phrases from R2's "Expected benefit ... Risk" paragraphs, which are not recorded (see below) |
| Applied in file 11 "in other wording": new is not verbatim in file 11 | 25 of 25 not verbatim | none |
| Field names and order, allowed values, unique rids, every same_as target present | all | none |

For later collectors: of the 19 declined file 20 edits that have an old, 7 have that old still verbatim in file 11, which was written from file 10.

## Counts

| kind | status | records |
|---|---|---|
| edit | declined | 26 |
| edit | superseded | 1 |
| recommendation | not applied | 206 |
| recommendation | superseded | 62 |
| recommendation | applied | 26 |
| all | | 321 |

By scope: sentence 233, span 83, paragraph 5. Records with at least one same_as link: 212.

## Sources read

"read" means parts were read by eye; "parsed" or "scanned" means read by program only.

| Source | md5 | How it was used |
|---|---|---|
| `records/Semantics - project story.md` | eb3779a3415a4bbec9f056b0194afb28 | read: log entries 24 to 31, 41, 55 to 57 and S60 to S79, printed by search |
| `records/Semantics - Decisions.md` | d3a6b746b7c15c2527bd2cea65122c07 | read: S20 to S29 only, for the rules of this task |
| `authority/10 Claude Fable Semantics - standalone theory.md` | 3a8cd7c8ca6f3ad3b8a85ab9984d850e | target text; indexed by program (lines, Parts, sentences); every old checked against it |
| `authority/11 Claude Fable Semantics - standalone theory, revision 1.md` | 5e494c1095d920d128b9a79de378f923 | searched only (lines 43, 301, 560 to 566) to place the applied records; checked by program that no applied new is verbatim in it |
| `authority/00 FW5 JUMP from FW2+FW3+FW4 - Explanatory construction (predecessor, 8 September 2026).md` | f27e14ce636844152fc9d92a0e72958f | headings listed only; no record gives its change to file 10 sentence by sentence |
| `results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md` | 48ef9384fb787163a0a2644a4007e322 | table rows 33 to 112 parsed by program; opening read |
| `results/57 Stage C return - the other model's seven case cards, O4 placed, phrases sorted.md` | ae4b8000d198f88ae7de027649afe486 | scanned: headings and a search for proposed wording (none new; its quoted passages recur in S62/07) |
| `results/S65 Saved page - the other model's chat, S62 and S64 manifests and timings.md` | 6ca5a77244378c1e6bbefa51038be001 | scanned: no Stage B rows and no proposal lines |
| `results/S75 Results - the bare version test, audited: what a new version of the theory is built from.md` | c395b96374063a0550b4a09a05b35443 | read in full |
| `results/S78 Results - the two-stage pattern reviewed by five readers, what stands, what is corrected, what to repair before S76.md` | e43241e0da99509d9dd665a09b655207 | scanned: headings and search; it proposes no theory wording (point 6 on W08 and point 10 on R2 J's Part VIII sentence used for status) |
| `results/S62 Stage D and report - return/01 Fix cards.md` | 7e08d8c964a5aeef0e1d92b824bc1117 | read: the four boxed clauses and the fields around them |
| `results/S62 Stage D and report - return/02 Clause tests on the fourteen cases.md` | 050664949c6ace4d14e231a7283ea9b4 | scanned by program (no proposed wording) |
| `results/S62 Stage D and report - return/03 The finding at its size.md` | 2040a46397e8f4e288fcfb0f17e43076 | read |
| `results/S62 Stage D and report - return/04 Two anchoring passages.md` | be52fe21997fe83850be438e2ae4f6e0 | read; source of the file 20 anchoring block (A-26) |
| `results/S62 Stage D and report - return/05 Near-case coverage of the table.md` | 5c5c5fa0f332568cea4a510b067e5727 | scanned by program (no proposed wording) |
| `results/S62 Stage D and report - return/06 Attack points and refutation entries.md` | e6d118fb039879f504dd196138d63141 | scanned by program (no proposed wording) |
| `results/S62 Stage D and report - return/07 Quotations.md` | b2af03d07e6df557339b114e8031bf54 | parsed by program in full (earlier, revised and R2 rows) |
| `results/S62 Stage D and report - return/08 Report.md` | 0e2ea43b2ddfecf0d01da9a46828cf42 | headings and section (7) read; boxed clauses scanned (repeats of 01) |
| `results/S62 Stage D and report - return/MANIFEST.md` | b98e58fdfe4ce1c7711084e0bf7137d9 | scanned by program for tagged proposal lines (none) |
| `results/S62 Stage D and report - return/PARKED.md` | 1fbe6befb5aed362bf5fdf6d2788459f | scanned by program for tagged proposal lines (none) |
| `results/S64 Near cases - return/01 Ten case cards.md` | cb1bad37866023bdf2e8ddf6cdc3a0b7 | scanned by program (no proposed wording) |
| `results/S64 Near cases - return/02 Tighter pairs and fix cards.md` | 71b0617f1ffdc54eef99dca2880329d6 | read: boxed clauses H64 and I64 |
| `results/S64 Near cases - return/03 Clause tests on all cases.md` | 452a2fe84738c0e1645ef47f839513ad | scanned by program (no proposed wording) |
| `results/S64 Near cases - return/04 Coverage after this round.md` | 1472b30a4c0dbb7e141062fe6afd7923 | scanned by program (no proposed wording) |
| `results/S64 Near cases - return/05 Quotations.md` | 7c8b7b034e980e5ad81596bc84224cae | parsed by program (rows S64-R2-A01 to J03) |
| `results/S64 Near cases - return/06 Report addendum.md` | 238e452eac04e332ab12a97fc8476d01 | sections (7) and (8) read |
| `results/S64 Near cases - return/MANIFEST.md` | cb4fc0713d8b3e2d4016c1e3f16bfd20 | scanned by program for tagged proposal lines (none) |
| `results/S64 Near cases - return/PARKED.md` | 8d1ce410485e7e6e017190cdf82e3c3f | scanned by program for tagged proposal lines (none) |
| `results/S65 Near cases - return/01 Thirteen case cards.md` | 9e7ba391deff5f89e6907c06fb14bcc5 | scanned by program (no proposed wording) |
| `results/S65 Near cases - return/02 Tighter pairs and fix cards.md` | 20643175bf8e5714da469a2dcf9969cf | read: boxed clause H65 and the repeats of H64 and I64 |
| `results/S65 Near cases - return/03 Clause tests on all cases.md` | 84d1952292db3233f6e49d29a5d50838 | scanned by program (no proposed wording) |
| `results/S65 Near cases - return/04 Coverage after this round.md` | d4f29e1a43c5cf292b6778d3f9b7d71b | scanned by program (no proposed wording) |
| `results/S65 Near cases - return/05 Quotations.md` | 1232e6b49da52fbebb25ad2b044817c7 | structure scanned; registers repeat S62 and S64 identifiers |
| `results/S65 Near cases - return/06 Report addendum.md` | 784f6900330f07af95a762b88c24df1f | sections (7) and (9) read |
| `results/S65 Near cases - return/MANIFEST.md` | e64eb5cec5e59a579b2f0a68ca9223e3 | scanned by program for tagged proposal lines (none) |
| `results/S65 Near cases - return/PARKED.md` | 8d1ce410485e7e6e017190cdf82e3c3f | scanned by program for tagged proposal lines (none) |
| `results/S70 Near cases - return/01 Twelve case cards.md` | c18ddc1d242012272cc6997e6fcb5da8 | scanned by program (no proposed wording) |
| `results/S70 Near cases - return/02 Tighter pairs and fix cards.md` | f38ae8ac980e3fbc9ffee66edc57d09e | boxed clauses scanned (verbatim repeats) |
| `results/S70 Near cases - return/03 Clause tests on all cases.md` | a586d07ddd12c252bdb4253c6a6b64b0 | scanned by program (no proposed wording) |
| `results/S70 Near cases - return/04 Coverage after this round.md` | 840aa851d27e992ed696004d7c40b6b3 | scanned by program (no proposed wording) |
| `results/S70 Near cases - return/05 Quotations.md` | 9c920216d84d5322a18b41249a6bcfeb | structure scanned |
| `results/S70 Near cases - return/06 Report addendum.md` | 9981ee371cb897310ec9d79e4ad8c886 | sections (7), (10) and (11) read; heading (11) parsed by program |
| `results/S70 Near cases - return/MANIFEST.md` | 3e18222c6f2dd14119ef5ad0a72580c2 | scanned by program for tagged proposal lines (none) |
| `results/S70 Near cases - return/PARKED.md` | 8d1ce410485e7e6e017190cdf82e3c3f | scanned by program for tagged proposal lines (none) |
| `results/S72 Stage 1 testing - return/01 The bare earlier version against every case.md` | b9907caeca696350cf78509404a91dbd | scanned by program (no proposed wording) |
| `results/S72 Stage 1 testing - return/02 Three case cards.md` | 8d130ef0ad9f425459f4daea745171b3 | scanned by program (no proposed wording) |
| `results/S72 Stage 1 testing - return/03 Tighter pairs and fix cards.md` | 02363657f962e101e5f2c395cd00ba3a | boxed clauses scanned (verbatim repeats) |
| `results/S72 Stage 1 testing - return/04 Coverage after this round.md` | bf4316271338b9aee8721d4821ab1488 | scanned by program (no proposed wording) |
| `results/S72 Stage 1 testing - return/05 Quotations.md` | cacdc8e1adbe7fe941985bff8a6d329d | parsed by program (T-R and T-C entries; all repeat S62 and S64 wording) |
| `results/S72 Stage 1 testing - return/MANIFEST.md` | c0154b471dd94d522db21473e18a1def | scanned by program for tagged proposal lines (none) |
| `results/S72 Stage 1 testing - return/PARKED.md` | 8d1ce410485e7e6e017190cdf82e3c3f | scanned by program for tagged proposal lines (none) |
| `results/S72 Stage 2 audit - return/01 Audit of the bare version table.md` | b6f08e7693aa4536581fcbbd9b152e37 | scanned by program (no proposed wording) |
| `results/S72 Stage 2 audit - return/02 Audit of the three cards and pairs.md` | c8272acb20b617b548c628423484af15 | scanned (verbatim repeats of H64, I64, H65) |
| `results/S72 Stage 2 audit - return/03 Audit of the quotations.md` | 292df2ce6484d3bf5be90d594f716520 | scanned (verbatim repeats of R2 and clause wording) |
| `results/S72 Stage 2 audit - return/04 Fix card for Derivation 3.md` | 5a87a44b21526731a2b0b017fe848d9c | read in full |
| `results/S72 Stage 2 audit - return/05 Report addendum.md` | dcf981d9f6fa781b306694407dfc1a3b | sections (7), (11) and (12) read; heading (11) parsed by program |
| `results/S72 Stage 2 audit - return/MANIFEST.md` | b21f3e29c9511075517529c5b337aed6 | scanned by program for tagged proposal lines (none) |
| `results/S72 Stage 2 audit - return/PARKED.md` | 8d1ce410485e7e6e017190cdf82e3c3f | scanned by program for tagged proposal lines (none) |
| `tests/24 Workflow - audit the semantics - give this to the other model.md` | f6fb285a58f1021b65dfc60facae815a | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/27 Next instruction for the other model - round 3, outside cases.md` | f5092fb6ffa92e85956cdae79a2c254a | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/28 Next instruction for the other model - round 4, two change-based clauses.md` | d0cb302388254a39072f6f2b888e1031 | read: lines 1 to 14 (clauses A-prime and C-prime) |
| `tests/30 Next instruction for the other model - workflow update and re-audit.md` | 611de04a42ba4569209a83b5a45fdd0d | read: lines 17 to 24 (clauses A-second and C-second); rest searched |
| `tests/41 Next instruction for the other model - finish Stage B and near cases.md` | f5fe20064f192812e5bd38d1deb70cef | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/55 Next instruction for the other model - Stage C, the outside cases.md` | a37b4f8fd81265dd7c6870aa712f5a39 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/57 Next instruction for the other model - Stage D fix cards and the report.md` | 325e2d6515218d2b422d12d788ea7cb5 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S62 Next instruction for the other model - Stage D, clause tests, coverage and the report, returned as a zip.md` | 2778420e2f38aba2e999def9b6903aa8 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S63 Next instruction for the other model - ten near cases by an outside author, returned as a zip.md` | 8faf109e32ca760e64898591067351e7 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S64 Next instruction for the other model - ten near cases, verdicts under the earlier version, returned as a zip.md` | d190772114c423aef21d4214ccab3188 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S65 Next instruction for the other model - thirteen near cases, two attribution tests, returned as a zip.md` | a37e19a7b09d85a594921372c1647431 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S70 Next instruction for the other model - twelve near cases, the protected condition stated first, returned as a zip.md` | 932b043aab285549fddd0c70712fd701 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S71 Next instruction for the other model - the bare earlier version against every case, and three more, returned as a zip.md` | 52957c1ea5af2cca6dd56f9f2c05dbe1 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S72 Stage 1 testing - the bare earlier version against every case, and three more, returned as a zip.md` | d2309c683a98c0ef295bb42526ad9a16 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S72 Stage 2 audit - check the testing return, then build the draft list from what survives, returned as a zip.md` | 40d060d18de001388fa4e5b95102eeca | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S76 Stage 1 testing - file 11 against every case, returned as a zip.md` | a95af191d20992babd161e4c8dce2e45 | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |
| `tests/S76 Stage 2 audit - check the file 11 test, returned as a zip.md` | 9dfe1523c98f883e8b75db4105e68ffd | searched by program for proposed theory wording; lines with hits read (none beyond 28 and 30) |

## Sources skipped, and why

- `tests/24 Owner's guide - running the audit workflow.md`, `tests/Instruction pack - ...` (three files): instructions about running the rounds; no theory wording.
- `tests/S79 Seeded ...` (two files): written after file 11; the planted errors are test material, not proposed wording.
- `results/S78 Two-stage pattern review - return/` (five reports and the raw returns): reviews of the testing process; `S78 Results` was searched instead and proposes no theory wording.
- Everything from S79 on (S80 to S97, the revision 2 drafts and change list): later than file 11, in the other collectors' stretches.
- `authority/12 Claude Fable Semantics - causality, standalone theory.md`: a separate causality text written after file 11.
- R2's "Expected benefit ... Risk" paragraphs, S64-R2-A02, B04, C06, D04, E04, F03, G01, H01, I04 and J03: they say why each amendment was proposed, not what it says.
- Stage B rows whose phrases all come from those paragraphs: row 66 (F), 90 (H), 100 (I), 101 (I), 111 (J) and 112 (J). Eight more rows mix such a phrase with R2 wording; they are recorded, with the reason paragraph named in source_ref.
- Tighter pairs, case cards, clause-test tables, coverage tables and near-case fields in the returns: pairs of changes to cases and verdicts, not wording for the theory.
- Quoted passages that are the same in both versions: S62 Q05/Q06, Q11/Q12, Q19/Q20.
- The "Whether the earlier theory already said this" quotations in the fix cards and the T-E and A-E quotations of the S72 returns: file 10's own text, unchanged.
- MANIFEST and PARKED files: scanned only; nothing in them proposes wording.

## What could not be recovered

- **Stage B rows 1 to 32** (amendments A, B, C and the first rows of D). They were pasted into the chat of log 41 and never reached the repository (S62 coverage file 05, log S63, S75).
- **R2 as a whole.** The file "Claude Fable Proposed Amendments R2" (log 25) was never in the repository. The records hold the sentences the returns quote: A (A01 and R2-A-1 to 13), B01 to B03, C01 to C05 and R2-extra-C, D01 to D03, E01 to E03, F01 and F02, G (R2-G-14 to 30), H (R2-H-31 to 41), I01 to I03, J01 and J02. Whether R2 held more is not known.
- **The old wording for R2.** The file 20 passages each R2 sentence replaces were never quoted, so old is empty for all R2 and Stage B records.
- **File 20.** Not held. Only the 25 revised passages of S62/07 and the block in S62/04 are quoted in full; its other differences from file 10 are unknown. For passages file 20 adds, target_line is the nearest file 10 line (after attack (E) for attack (F); after "Construction reduced to selection" for the two added Part XV entries).
- **The S76 patch.** Made first on the word "Revision time" and not kept; A-321 has a description only.
- **FW5 (file 00) to file 10.** No record gives this change sentence by sentence; the two texts differ as wholes (1,502 lines and 19,273 words against 629 lines and 7,880 words), so no record was made for it.
- **Three S75 items are partial.** Grievance 3 (A-318): new_sentence is left empty, since putting S75's words in place of "*always* underdetermined" would leave "on unseen changes" twice. Attack (D) (A-319): S75 gives a description, not wording. Part XV (A-320): the bullet's own words, with the added part in italics; new_sentence is left empty.
- **target_part** for the R2 and Stage B records uses file 10's Part titles for the Parts that R2 names; file 20's headings may differ. For the S70 lines, target_part was named by Claude from the cases, rows and clauses each line cites; for W01 to W12 it is the Parts the row itself names.
