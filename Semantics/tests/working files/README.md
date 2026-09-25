# Working files

These are working files made in the session scratchpad and cited by committed records. They were copied here on 25 September 2026 so that they are not lost when the temporary machine is cleared (lesson S23). Every file is unchanged, byte for byte. A file the records call `scratchpad/rivals/01 entries.md` is `rivals/01 entries.md` here. A file already in the repository with the same content was not copied again; each section below says where it is. All of them were made by Claude subagents or by the orchestrator.

Left out everywhere: Python's compiled caches (`__pycache__/`), and three files that hold longer runs of text from the source books than the project allows (more than 25 words in a row). They are named below.

## rivals/ - the making of revision 2 draft 4 (25 September, 01:30 to 03:48 UTC)

The pass that restated hard to vary through rivals and problems. The drafted change entries (`01 entries.md`), the models (`02 models.md`), the text attack (`03a text attack.md`) and the model attack (`03b model attack.md`). The entry blocks before and after (`orig_W33.1.md`, `orig_W34.1.md`, `orig_W38.1.md`, `block_W38.1.md`, `final/blocks/`). The scripts that spliced the entries into copies of the change list and built the draft (`splice.py`, `make_w38.py`, `attack3a/splice_fixed.py`, `final/make_blocks.py`, `final/frame_edits.py`, `final/regen_note.py`) and the copies they made: change lists (`cl_spliced.md`, `attack3a/cl_fixed.md`, `final/cl_final.md`), whole file 13 builds (`base_full.md`, `new_full.md`, `attack3a/fixed_full.md`, `file13_draft4.md`, which `check_cl4.md` and `final/try_full.md` repeat), and theory-text builds (`new_theory.md`, `attack3a/fixed_theory.md`, `blocks_theory.md`).

- Cited by: the note on rivals and problems (`tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md`, for 01, 02, 03a and 03b); `plain words/92 working record/plan.md` (`file13_draft4.md`, `01 entries.md`) and `review expert.md` (`file13_draft4.md`); the project story, log S91.
- Already in the repository, so not here: every script and output under `attack/`, `attack3a/`, `final/` and `models/` that is in `tests/Revision 2 - rivals and problems - scripts/`; `base_theory.md` (draft 3's theory text); `file13_draft4_theory.md` and `final/try_theory.md` (draft 4's theory text); `final/cl_draft4.md` and `final/note_draft4.md` (the change list and the revision note, in `tests/`); `f1_repo_run.txt` (the scripts folder's `final/f1_output.txt`).

## plain/ - the making of the plain-words document, file 92 (25 September, 04:13 to 08:33 UTC)

The section drafts 00 to 13 (`section 00.md` to `section 13.md`, and `.s00_before_review.md`, section 0 before its review). The first and second whole drafts (`whole v1.md`, `whole v2.md`). The parts each whole was joined from: `whole_parts/` and `body.tmp` for v1; `v2parts/` for v2, with `index.py`, which listed the sections each example appears in; `v3parts/` for the final document.

- Cited by: the project story, log S92; `plain words/92 working record/` (the expert review and the first cold read read `whole v1.md`, the second cold read read `whole v2.md`, and the two revision logs go from v1 to v2 and from v2 to the final).
- Already in the repository, so not here: the plan, the word sheet, the expert review, the two cold reads and the two revision logs (in `plain words/92 working record/`); `whole v3.md`, which is file 92.

## ratchet/ - the check "does correction stick" (24 September, 21:37 to 22:42 UTC)

The models (`02 models.md`), the proposal (`03 proposal.md`), the text attack and the model attack (`04a text attack.md`, `04b model attack.md`), the checked result (`05 checked result.md`), the answer sent back (`final_plain.txt`), and `check/quote_len.py`, which flags long book quotations.

- Cited by: `tests/Revision 2 - does correction stick, the hard-to-vary lemma and its limit, analysis of 24 September.md`, which is built from these files, and the scripts beside it.
- Already in the repository, so not here: `note.md`, which is that analysis; every script and output under `attack/`, `check/` and `models/`, and the `rerun_*` and `repo_*` outputs, which are the same as the outputs in `tests/Revision 2 - does correction stick - model scripts/`.
- Left out: `01 text.md` and `check/assemble_note.py`, which quote the book in one run of 31 words. `01 text.md` is in the analysis as its Appendix A, with that quotation shortened.

## errcorr/ - the error-correction analysis (24 September, 11:32 to 12:25 UTC)

The theory map (`01 theory map.md`), the synthesis before its check (`03 synthesis.md`) and the checked answer (`04 checked answer.md`). The scripts that searched the book text by word or page (`kw.py`, `pages.py`) and checked each quotation against its page and its length (`checkquotes.py`, `check2.py`); they print book text when run but hold none. The draft commit message (`commitmsg.txt`).

- Cited by: `tests/Revision 2 - error correction and grading, analysis of 24 September.md`: its body is 04, its Appendix A is 01, and it names 03 as not included.
- Already in the repository, so not here: `note.md`, which is that analysis.
- Left out: `02 sources.md`. Each quotation in it is 25 words or fewer, but in twelve places two to four quotations stand side by side, with only a page number between them, and give back up to about 50 words of the book in a row. Its text is in the analysis as Appendix B.
