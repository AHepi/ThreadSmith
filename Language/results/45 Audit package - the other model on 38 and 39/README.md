# Ledger 38/39: kingfisher, pear and wider-corpus audit

## Result and status

The explicit kingfisher pair is a control that the current language can handle. The larger audit identifies fifteen documented conflicts, interpretation/reporting gaps or bounded extension questions. They have different strengths: they are not fifteen observed program bugs. Twelve repair families were subjected to further counterexamples, rival substitutions and removal tests. Several tempting repair versions were rejected.

This is a manual audit of the supplied definition and translator instructions. No executable checker or independent witness run was performed. The proposed amendments are not a certified implementation specification.

## Read the package

[The audit report](00_Audit_report.md) gives the findings, source anchors, strongest defences and qualifications. [Worked translations](03_Worked_translations.md) show the kingfisher colour/burning pair, the isolated Hopkins image, two separately authored pear probes and a negated-belief trap, with the five requested translation sections.

[The full inherited-corpus coverage record](01_Corpus_coverage_324.md) prints all 324 inherited texts and current document-level assessments. [The new adversarial paragraphs](02_New_adversarial_paragraphs.md) add sixty original texts in thirty contrast families. Together there are 384 registered inputs. A test-input count is not a count of independent findings, completed full-ledger translations or checker executions.

[Candidate repairs and their re-audit](04_Candidate_repairs_and_reaudit.md) preserve rejected variants and objections rather than overwriting them with a success story. [Proposed amendments to 38](05_Proposed_38_amendments.md) provide the candidate clauses. [The revised translator prompt](06_Revised_39_translation_prompt.md) is conditional on the named amendments being adopted; it is not claimed to run unchanged against existing software.

[The audit's self-review](07_Self_audit_and_limits.md) records narrower findings, flawed inherited controls, corrected worked examples and remaining uncertainty. [Research and provenance](08_Research_and_provenance.md) distinguishes retrieved evidence, inherited source records and this assistant's proposals.

## Preserved evidence

The exact supplied authorities are in `sources/38_original.md` and `sources/39_original.md`. The three inherited corpus files are unchanged under `corpus/`. Their baseline hashes are in `audit/baseline_freeze.json`. The twenty literary-excerpt source records are copied as inherited metadata in `sources/inherited_literary_seeds.json`.

The structured manual receipts are in `audit/coverage_324.jsonl`, with family records alongside them. New texts are in `corpus/new_60.jsonl`; their thirty case-family records are in `audit/new_case_cards.json`. None of these JSON fields represents the output of a hidden semantic checker.

The old 36 was not supplied and the earlier possible 02 is not treated as authority. No conformance claim about either is made. “Pear” is covered with separately labelled original pear probes without assuming the user identified a particular pear poem.

## Validation

Run `python tools/validate_package.py` from this directory, or run that script by its path. It checks the baseline hashes, 384 unique input identifiers, exact receipt coverage for the inherited 324, the thirty new contrast families, the worked-table counts and the packaged-file manifest. It performs no semantic evaluation and makes no network calls.

The recorded validation result is `audit/structural_validation.json`. A successful result means those structural checks completed. It does not certify source interpretation, physics, psychological attribution, causal support, implementation conformance or completeness of the criticism.
