# L66 returned evidence

Written by OpenAI Codex, under L66, from the sealed corpus. This is the requested return package, not a project record update.

Read `DRAFT L66 - what the run showed.md` with `Gauge_OpenAI_Codex.md`. The draft links the exact reports, raw logs and consequences. A printed clean report covers only represented lines and executed questions; it does not certify the passage, its reasoning or its author.

The original eighteen translations were completed in order P01 through P18, each before opening the next passage. Their close-out hashes and times are in `evidence/translation_order.jsonl`. No answer-key content was opened. No GitHub or network operation was performed. The existing local s(CASP) runtime passed the supplied smoke fixture; the installer was not run because installation was unnecessary and its GitHub operation was excluded by the owner's instruction.

## Which files to use

| Passage | Primary semantic translation and rig-1 pair | Primary rig-2 pair |
| --- | --- | --- |
| P01 | `P01_OpenAI_Codex_translation_correction1.md`; `ledger_P01_correction1.*` | None |
| P03 | `P03_OpenAI_Codex_translation_correction1.md`; `ledger_P03_correction1.*` | `ledger_P03_correction1.*` |
| P07 | `P07_OpenAI_Codex_translation_correction1.md`; `ledger_P07_correction1.*` | None |
| P10 | `P10_OpenAI_Codex_translation_correction1.md`; `ledger_P10_correction1.*` | None |
| P13 | Original `P13_OpenAI_Codex_translation.md`; `ledger_P13.*` | `ledger_P13_correction1.*` (adapter only) |
| P14 | `P14_OpenAI_Codex_translation_correction1.md`; `ledger_P14_correction1.*` | None |
| P04, P09, P18 | Original translations and `ledger_Pxx.*` | Original `ledger_Pxx.*` |
| All others | Original translations and `ledger_Pxx.*` | None |

Translations are in `translations/`. Ledger pairs are under their named `rigs/` folders. Every original remains alongside its separate correction. Correction reasons and hashes are in `evidence/corrections_OpenAI_Codex.json`, with the separate P13 rig-2 adapter correction in `evidence/P13_rig2_adapter_correction_OpenAI_Codex.*`. The residual historical comment in P14's corrected Prolog file is clarified in `evidence/Correction_comment_erratum_OpenAI_Codex.md`; executable code, JSON and translation agree.

The pairs with most sentences shared are P01/P07 and P11/P14. `evidence/sameness/` contains original and corrected comparisons plus item-by-item human decisions. Those comparisons were made only after all original translations were closed; originals were not harmonised to improve a match.

## Evidence and attribution

`evidence/rig1/`, `evidence/rig2/` and `evidence/consequences/` retain exact stdout reports, exact stderr files, raw query logs and per-run command/hash receipts. Empty stderr is retained as an empty file. Authorship for unedited program output is recorded in its companion receipt and this package's manifest; no authorship header was inserted into raw output. The source corpus and supplied reference/tool copies remain byte-identical, with copy provenance identifying OpenAI Codex. They are not newly authored text.

The gauge counts distinct source sentences losing something to the bin. The original rig-1 printout instead uses the number of bin entries; printed reports were not rewritten to conceal that difference. Verb counts concern declared happenings; generic and intransitive uses remain separately visible in the JSON verb inventories. An absent finding is not evidence that those verbs were checked.

`tools/consequences.py` removes one ledger line at a time. Its removal operation differs from a rig-1 MAKE NOT SO what-if, which may also remove an explicitly tied result. Its DERIVED list is exactly the tool's printed classification under its fixed query list, not all semantic consequences of the passage.

## Reproducing a run

The supplied patched checker and rule files are included unchanged. They expect an installed executable at `/home/claude/sCASP/scasp`. This package neither downloads a runtime nor changes a repository. From the unpacked package root, with that runtime already installed, a new run can be written to fresh paths:

```bash
python3 'rigs/rig 1 - arguments/patched/run_check.py' 'rigs/rig 1 - arguments/ledger_P01_correction1.pl' /tmp/L66-new-P01-raw.txt > /tmp/L66-new-P01-report.txt
python3 tools/consequences.py 'rigs/rig 1 - arguments/ledger_P01_correction1.pl' /tmp/L66-new-P01-consequences-raw.txt > /tmp/L66-new-P01-consequences.txt
python3 'rigs/rig 2 - causes/patched/check2.py' 'rigs/rig 2 - causes/ledger_P13_correction1.pl' /tmp/L66-new-P13-rig2-raw.txt > /tmp/L66-new-P13-rig2-report.txt
```

Use fresh output paths because the supplied drivers append to raw logs. `authoring/` records the workspace-bound construction scripts and historical original choices; it is not needed to rerun the checkers.

`BUNDLE_MANIFEST.json` provides SHA-256 and byte size for every returned file except itself, following the supplied example's self-exclusion convention. `corpus/MANIFEST.json` is the unchanged supplied corpus manifest; its sealed-key hash is only copied metadata. KEY.enc is not included in this return. Inventory counts establish completeness only, not quality or truth.
