# Language - index

Every research state of the ledger language, in order, with links. Numbers are log entries in the [project story](<records/Checked reasoning language - project story.md>), which is the full account. "Not in bundle" means the file is described in the log but was left out of both zips as superseded; it is not here.

## 1. The first theory and its research (logs 01 to 05)
| | |
| --- | --- |
| Story | Decisions 1 to 4: purpose; theory first, by the skill; honest attempt over correctness; no research yet. |
| Authority | `01 Theory - twelve properties.html` - **not in bundle**. Summarised in [ORIGIN.md](ORIGIN.md). |
| Test | `03 Research plan - what would count against each property.md` - **not in bundle**; frozen before searching. |
| Result | `04 Research - existing languages against the twelve properties.html` - **not in bundle**. Most predictions right; one half wrong (GUARD marks filled-in lines); three properties changed; one finding fits no part (argument mapping aids reasoning with no checker). |
| Lessons | Lessons 1 to 6 (pictures; the validator; "claimed" because desk research only reaches what makers say). |

## 2. The first rig, s(CASP) (logs 06 to 10)
| | |
| --- | --- |
| Story | Decision 9: run the real checker on more than the tomato paragraph. |
| Test | `06 Test plan - what I expect the checker to do.md` (five paragraphs A to E, frozen before any rule existed) - **not in bundle**. `09 Test plan - your ball and coin paragraph.md` - **not in bundle**. |
| Raw result | Rig 1 developed on paragraph A, then frozen with fingerprints. Ledgers A, A2, B, C, D, E and F (ball and coin) are in [rigs/rig 1 - arguments/](<rigs/rig 1 - arguments/>) as they stand now. |
| Interpretation | Log 07: every planted fault in A found; page 01 corrected (softened tomato is "follows on an unstated assumption", not a jump); three patches. Log 10: first result "seen, on someone else's case": NO FAULT FOUND, a predicted miss; patches 4 and 5, each fitted to this one paragraph. |
| Lessons | Lessons 7, 8 (installing s(CASP); a run that hung waiting for keyboard input). Decision 10: the owner confirms the finding ("It violates basic laws of physics"). |

## 3. The second theory: causes as pressing patterns (logs 11 to 17)
| | |
| --- | --- |
| Story | Decision 11: the language "does not appear to adequately capture causal relations". Decisions 12 to 16: requirements; research through the connectors; counterfactuals and abstractions. |
| Authority | `15 Theory - merged - the one theory the build will test.html` - **not in bundle**. Merges pages 11 and 12. |
| Test | `12 Research plan` and `16 Test plan - the build of the merged theory.md` (cases A to G) - **not in bundle**. |
| Raw result | Rig 2 in [rigs/rig 2 - causes/](<rigs/rig 2 - causes/>): a shape book, response classes, three strength levels, general laws, a driver that finds which slot failed. Ledgers A to G, plus X1 and X2 added after the plan to break the rig. |
| Interpretation | Log 17: the owner's paragraph comes out right from general laws alone; a clean sweep on Claude's cases; both hostile cases broke the frozen rig. |
| Lessons | Lesson on the connectors asking for permission (log 12). |

## 4. One language for both rigs (logs 18 to 23)
| | |
| --- | --- |
| Story | The owner asked what meanings the system captures (18) and whether two sentences differ (19). |
| Authority | `18 Reference - what meanings the system captures.md`, `20 Rulebook - what counts as a legal line.md`, `23 Rulebook ...` - all **not in bundle**, superseded by 38. |
| Tests | [21 Test plan - your Markus paragraph](<tests/21 Test plan - your Markus paragraph.md>); [22 Test plan - your Mondays paragraph](<tests/22 Test plan - your Mondays paragraph.md>). |
| Raw result | Ledgers G (Markus) and H (Mondays) in rig 1; G in rig 2. `raw_log.txt`. |
| Interpretation | [21 Test results](<results/21 Test results - your Markus paragraph.html>): the predicted JUMP false alarm; patch 6 (SINCE). [22 Test results](<results/22 Test results - your Mondays paragraph.html>): 2 of 7 steps hold; the supposition undoes itself; patch 7 (chains). |
| Lessons | "What each patch gave up", patches 6 and 7. |

## 5. The other model's rulebook audit and three piles of fixes (logs 32 to 36)
| | |
| --- | --- |
| Story | Log 32: the other model audited rulebook 23 (byte-identical copy) and found 25 real faults. Sorted into three piles by running five of its cases through the rigs (log 33). |
| Test | [35 Test plan - the third pile](<tests/35 Test plan - the third pile.md>) - the features and their forcing cases, frozen before building. Piles 1 and 2 have no separate plan; each change was run first on the case that forced it (log 34). |
| Raw result | Ledgers `K..` in rig 1 (named after the audit's findings F04, F06, ...) and K01 in rig 2; `..._before_pile2` and `..._before_pile3` copies of the drivers and rules. |
| Interpretation | Log 33: rig 1 was right where the page was wrong (F04, F13). Log 34: patches 8 to 11, all earlier ledgers unchanged. Log 35: patches 12 to 14, the rigs joined (`joined/`), one known limit (two causes, one withdrawn: K22b). |
| Authority | `33 Rulebook`, `34 Rulebook`, `36 The ledger language - complete definition.md` - **not in bundle**, superseded by 38. The other model's "Rulebook Audit and Repaired V3" - **not in bundle**. |

## 6. The blind sample and the clean language (logs 37 to 39)
| | |
| --- | --- |
| Story | The other model's literary stress test: 324 inputs, keys held apart, never run by it. The owner chose the literary corpus on purpose (log 39). |
| Test | [37 Test plan - blind sample from the literary stress test](<tests/37 Test plan - blind sample from the literary stress test.md>) - four families, eight texts, chosen by text and question only, keys opened after. |
| Raw result | Ledgers T05B, T05D, T07B, T07D, T10B, T10D, T11B, T11D in rig 1; `raw_log.txt`. |
| Interpretation | [37 Test results](<results/37 Test results - blind sample from the literary stress test.md>): seven of eight matched; the miss (T07B, a told story) was predicted, then fixed by patch 15 (a told world stands alone). Patch 16: "cannot tell" for a plan the ledger knows nothing about. |
| Authority | [38 The ledger language - complete definition](<authority/38 The ledger language - complete definition.md>) - TOLD as a fourth standing; "cannot tell" under SO THAT. [39 Prompt - translate a text into the ledger language](<authority/39 Prompt - translate a text into the ledger language.md>) - the translator's task, in positive wording. |
| Rig | [rigs/](rigs/) as of these two patches ("38 Checker rigs - both, current"). |
| Next | Give 38 and 39 to the other model with one of its own texts; compare ledgers line by line. |

## 7. The other model's audit of 38 and 39 (log 45) - plan frozen, not run
| | |
| --- | --- |
| Story | Decision 35. The next step at log 39 was to give the other model 38 and 39 and compare ledgers line by line; its return is an audit of both files instead, with six translations of its own texts and none of Claude's. |
| Raw result | [45 Audit package - the other model on 38 and 39](<results/45 Audit package - the other model on 38 and 39/>) - kept unchanged; its `README.md` is the way in and `tools/validate_package.py` checks its hashes and counts. Includes the 324-input literary corpus of log 37, which was not in the earlier bundles. |
| Interpretation | Log 45: what it holds, what it does not, four findings confirmed against the text of 38 and 39 (F01, F02, F04, F15), two references the record cannot place ("02"; the skill read from a GitHub repository). |
| Test | [45 Test plan - the 38 and 39 audit package, ledgers compared and findings sorted](<tests/45 Test plan - the 38 and 39 audit package, ledgers compared and findings sorted.md>) - Part A: six ledgers compared by the sameness test; Part B: fifteen findings sorted into the three piles of log 33 by running each forcing case on the rig as it stands. |
| Instruction | [46 Next instruction for the other model - translate the eight texts of plan 37](<tests/46 Next instruction for the other model - translate the eight texts of plan 37.md>) - the live one: the eight texts of plan 37 under 38 and 39, one family per stage, then three short answers (why its six are TOLD; what "02" is; which skill it read). Not yet sent. |
| Execution attempt | [58 Execution attempt - the other model on plan 45](<results/58 Execution attempt - the other model on plan 45/>) - the other model was handed plan 45; blocked before Part A with no s(CASP) on its machine. Kept unchanged. It exported its six tables as `.json`/`.pl` pairs (unparsed, not run), registered the fifteen Part B rows with every observed pile null, and recorded three discrepancies against the plan's predictions (N17, N22, N03-B), which stand beside the plan; the plan is unchanged. |
| Next | Run plan 45 here: the runtime is installed and the driver reproduces the recorded T05-B run (log 58). Paste 46. Two decisions for the owner: fixture as actual ledger or TOLD world (46 chooses the actual ledger; changeable before sending); what "02" is. |

## Files in this project, by folder
- `authority/`: 38, 39.
- `tests/`: 21, 22, 35, 37, 45, 46.
- `results/`: 21 (html), 22 (html), 37; the folder 45 (the other model's package, 25 files); the folder 58 (its execution attempt on plan 45, 67 files, of which 25 are a second copy of 45).
- `rigs/`: `READ ME FIRST.md`; `rig 1 - arguments/` (frozen, patched, joined, 36 ledgers as .json/.pl pairs, raw_log.txt); `rig 2 - causes/` (frozen, patched, 14 ledgers, raw_log.txt).
