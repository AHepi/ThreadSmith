"""Collector D, part 3: the repairs proposed in S95 (results file sections 7-9 and the two range checks),
each with its status as S96 stage 1 ruled (replacements.json entries[k].ref, and its not_applied list).
The wording is copied from the source by anchors (verbatim); target text: the scrubbed copy."""
from reclib import *

RF = "results/S95 Does the semantics hold without verificationist words.md"
R1F = "results/S95 Scrub - check of the opening note, the note of sources and departures, and Parts 0 to VIII.md"
R2F = "results/S95 Scrub - check of Parts IX to XV and every derivation, proof or argument after them.md"

A, S, O, N = "applied", "superseded", "open for the owner", "not applied"

# (src, ref, line, old-spec, new-spec, status, stage-1 entries, group, anchor-for-insertion, scope)
# spec: ("b", start, end, after[, after2]) | ("lit", text) | ("link",) | ("last2",) | ("first",) | ("toend", anchor) | None
ITEMS = [
 # ---------------- results file, section 7 ----------------
 ("RF", "section 7, B1, first repair (l. 397 add)", 397, None, ("b", 'At l. 397 add: "', '"\n- At l. 8', None), A, [25], "b1-397", "", "sentence"),
 ("RF", "section 7, B1, second repair (l. 8, R1)", 8, ("link",), ("b", 'replace the step sentence with R1: "', '"\n- Rename', None), A, [27], "R1", None, "sentence"),
 ("RF", "section 7, B1, third repair (rename)", 397, ("lit", "R_j(ψ)"), ("lit", "X_j(ψ)"), A, [25], "rename-X", None, "term"),
 ("RF", "section 7, B2, R13 (l. 315)", 315, ("link",), ("b", '- R13 (l. 315): "', '"\n- R18', None), A, [45], "R13", None, "sentence"),
 ("RF", "section 7, B2, R18 (l. 369)", 369, ("link",), ("b", '- R18 (l. 369): "', '"\n\n**B3.', None), A, [51], "R18", None, "sentence"),
 ("RF", "section 7, B3, R14 (i)", 317, ("link",), ("b", '*Repair, R14:* "', '" In (ii)', None), A, [46], "R14i", None, "span"),
 ("RF", "section 7, B3, R14 (ii)", 317, ("link",), ("b", 'In (ii): "', '"\n\n**B4.', '*Repair, R14:*'), A, [47], "R14ii", None, "span"),
 ("RF", "section 7, B4, R15 (l. 317)", 317, ("link",), ("b", '*Repair, R15:* "', '"\n\n**B5.', None), A, [22], "R15", None, "sentence"),
 ("RF", "section 7, B5, R11 (l. 277)", 277, ("first",), ("b", '*Repair, R11:* "', '"\n\n**B6.', None), A, [40], "R11", None, "sentence"),
 ("RF", "section 7, B6, l. 17", 17, ("last2",), ("b", '- l. 17: "', '"\n- l. 536 (A)', None), A, [28], "b6-17", None, "sentence"),
 ("RF", "section 7, B6, l. 536 (A)", 536, ("link",), ("b", '- l. 536 (A): "', '" (A) ends:', None), A, [17], "b6-536", None, "sentence"),
 ("RF", "section 7, B6, end of (A)", 536, ("link",), ("b", '(A) ends: "', '"\n- l. 538 (B)', None), A, [66], "b6-536end", None, "span"),
 ("RF", "section 7, B6, l. 538 (B)", 538, ("link",), ("b", '- l. 538 (B): "', '"\n\nThis l. 17', None), A, [18], "b6-538", None, "sentence"),
 ("RF", "section 7, B7, l. 522", 522, None, ("b", '- l. 522, after "(Part XII);": "', '" (with "admits"', None), A, [61], "b7-522", "(Part XII);", "span"),
 ("RF", "section 7, B7, l. 526", 526, None, ("b", '- l. 526, after "(K1) depends on (E).": "', '";\n- l. 598', None), A, [62], "b7-526", "(K1) depends on (E).", "sentence"),
 ("RF", "section 7, B7, l. 598", 598, ("link",), ("b", '- l. 598: "', '";\n- optionally', None), A, [72], "b7-598", None, "span"),
 ("RF", "section 7, B7, optional (l. 391)", 393, None, ("b", '- optionally, at l. 391: "', '"\n\n**B8.', None), A, [26], "b7-391", "does not define it].", "sentence"),
 ("RF", "section 7, B8, R12 (l. 299)", 299, ("link",), ("b", '*Repair, R12:* "', '". At l. 307', None), A, [41], "R12-299", None, "span"),
 ("RF", "section 7, B8, R12 (l. 307)", 307, ("b", 'At l. 307, "', '" then becomes', '**B8.'), ("b", 'then becomes "', '".\n\n**B9.', '**B8.'), A, [43], "R12-307", None, "span"),
 ("RF", "section 7, B9, R8 (l. 151)", 151, ("link",), ("b", '- R8 (l. 151): "', '"\n- R16', None), A, [33], "R8", None, "span"),
 ("RF", "section 7, B9, R16 (l. 331)", 331, ("link",), ("b", '- R16 (l. 331): "', '"\n\n**B10.', None), A, [49], "R16", None, "span"),
 ("RF", "section 7, B10, R9 (l. 159)", 159, ("link",), ("b", '*Repair, R9:* "', '"\n\n**B11.', None), A, [34], "R9", None, "sentence"),
 ("RF", "section 7, B11, l. 526 with l. 31", 526, ("link",), ("b", '- l. 526, with l. 31 to match: "', '"\n- l. 600, if the name stays', None), A, [63, 30], "b11-526", None, "sentence"),
 ("RF", "section 7, B11, l. 600", 600, ("link",), ("b", '- l. 600, if the name stays: "', '"\n\n**B12.', None), A, [73], "b11-600", None, "span"),
 ("RF", "section 7, B12, first repair (range 2 reader, l. 397)", 397, ("last1",), ("b", 'the last sentence of l. 397 becomes "', '"\n- (this answer)', None), S, [], "b12-397", None, "sentence"),
 ("RF", "section 7, B12, second repair (marker)", 397, None, ("b", '- (this answer) add: "', '"\n\nNo reader has read', None), S, [], "b12-marker", None, "sentence"),
 ("RF", "section 7, B13 (l. 441)", 441, ("link",), ("b", '*Repair:* "', '"\n\n**B14.', '**B13.'), A, [54], "b13", None, "span"),
 ("RF", "section 7, B14 (l. 479)", 479, ("link",), ("b", '*Repair:* "', '"\n\n**B15.', '**B14.'), A, [58], "b14", None, "sentence"),
 ("RF", "section 7, B15, l. 620", 620, ("link",), ("b", '- l. 620: "', '".\n- l. 630', '**B15.'), A, [75], "b15-620", None, "span"),
 ("RF", "section 7, B15, l. 630", 630, ("link",), ("b", 'since a contract contains changes: "', '"\n- l. 540', None), A, [76], "b15-630", None, "sentence"),
 ("RF", "section 7, B15, l. 540", 540, ("link",), ("b", 'since claims are ruled out and arguments are not: "', '"\n- l. 600', None), A, [67], "b15-540", None, "sentence"),
 ("RF", "section 7, B15, l. 600", 600, ("link",), ("b", '- l. 600: "', '"\n- l. 453', '- l. 540, since'), A, [74], "b15-600", None, "sentence"),
 ("RF", "section 7, B15, l. 453", 453, ("link",), ("b", '- l. 453: "', '".\n\n## 8.', None), A, [56], "b15-453", None, "span"),
 # ---------------- results file, section 8 ----------------
 ("RF", "section 8, residue, l. 47 (R3)", 47, ("link",), ("b", '*Repair, R3:* "', '"\n- l. 61.', '## 8.'), A, [31], "R3-47", None, "sentence"),
 ("RF", "section 8, residue, l. 61 (R3)", 61, ("link",), ("b", '- l. 61. *Repair, R3:* "', '"\n- l. 317', None), A, [32], "R3-61", None, "span"),
 ("RF", "section 8, residue, l. 335 (R17)", 335, ("link",), ("b", '*Repair, R17:* "', '"\n- l. 495.', None), A, [50], "R17", None, "span"),
 ("RF", "section 8, residue, l. 495", 495, ("link",), ("b", '- l. 495. *Repair:* "', '"\n\n**Authority words.**', None), A, [59], "l495", None, "sentence"),
 ("RF", "section 8, authority words, l. 161 (R4)", 161, ("link",), ("b", '*Repair, R4:* "', '"\n- l. 461', None), A, [35], "R4", None, "sentence"),
 ("RF", "section 8, authority words, l. 461", 461, ("link",), ("b", '*Repair:* "', '" The range 2 reader notes', '- l. 461, a task'), A, [57], "l461", None, "span"),
 ("RF", "section 8, authority words, l. 532", 532, ("link",), ("b", '*Repair:* "', '".\n\n**"An argument that X"', '- l. 532, the heading'), A, [65], "l532", None, "sentence"),
 ("RF", "section 8, reasons-FOR form, l. 542", 542, ("toend", "; an argument that every construction trace"), ("b", '- l. 542: "', '"\n- l. 544: "', None), A, [68], "l542", None, "span"),
 ("RF", "section 8, reasons-FOR form, l. 544", 544, ("link",), ("b", '- l. 544: "', '"\n- l. 538, "argued', None), A, [69], "l544", None, "paragraph"),
 ("RF", "section 8, reasons-FOR form, l. 526", 526, ("link",), ("b", '*Repair:* "', '"\n\n**Foundational residue.**', '- l. 526, "a separate argument'), A, [64], "l526def", None, "span"),
 ("RF", "section 8, foundational residue, l. 518", 518, ("link",), ("b", '*Repair:* "', '"\n\n**Corroboration', '**Foundational residue.**'), A, [60], "l518", None, "sentence"),
 ("RF", "section 8, corroboration residue, l. 211 (R5)", 211, ("link",), ("b", '*Repair, R5:* "', '"\n\n**Belief', None), A, [37], "R5", None, "sentence"),
 ("RF", "section 8, belief words, R6 option A, l. 221", 221, ("lit", "- **surprise** is a violation of a selected transport at \\((a,b)\\notin H\\)."), ("b", '- l. 221: "', '";\n- at l. 223', None), O, [], "R6A-221", None, "paragraph"),
 ("RF", "section 8, belief words, R6 option A, l. 223", 223, ("b", '- at l. 223, ', ' become ', '*Repair, R6, two options.*'), ("b", ' become ', ';\n- the heading', '- at l. 223, '), O, [], "R6A-223", None, "term"),
 ("RF", "section 8, belief words, R6 option A, heading l. 215", 215, ("lit", "## Prediction, surprise, violation"), ("b", '- the heading at l. 215 becomes "', '";\n- "recognized', None), O, [], "R6A-215", None, "sentence"),
 ("RF", "section 8, belief words, R6 option A, 'recognized difficulty' (l. 223, 317, 429, Part X)", 223, ("lit", "recognized difficulty"), ("lit", "registered difficulty"), O, [], "R6A-rec", None, "term"),
 ("RF", "section 8, belief words, R6 option B, l. 221", 221, None, ("b", 'Option B: add "', '" at l. 221', '*Repair, R6, two options.*'), A, [38], "R6B-221", "\\((a,b)\\notin H\\).", "span"),
 ("RF", "section 8, belief words, R6 option B, the same pointer for 'recognized difficulty' at l. 223", 223, None, ("b", 'Option B: add "', '" at l. 221', '*Repair, R6, two options.*'), A, [39, 55], "R6B-223", None, "span"),
 ("RF", "section 8, borderline, l. 43 (R7), first sentence", 43, ("lit", "The physical theory fixes which changes are possible at all."), ("b", '*Repair, R7:* "', '" and "What', None), S, [], "R7a", None, "sentence"),
 ("RF", "section 8, borderline, l. 43 (R7), last sentence", 43, None, ("b", ' and "', '"\n- l. 201', '*Repair, R7:*'), S, [], "R7b", None, "sentence"),
 ("RF", "section 8, borderline, l. 201 (R10)", 201, ("link",), ("b", '*Repair, R10:* "', '"\n- l. 8:', None), A, [36], "R10", None, "span"),
 ("RF", "section 8, borderline, optional l. 403", 403, None, ("b", 'Optional: l. 403 "', '"\n\n## 9.', None), N, [], "opt403", None, "sentence"),
 # ---------------- results file, section 9 ----------------
 ("RF", "section 9, MORE, l. 385", 385, ("link",), ("b", '*Repair:* "', '"\n- l. 390', '- l. 385:'), A, [52], "l385", None, "sentence"),
 ("RF", "section 9, MORE, l. 429", 429, ("link",), ("b", '*Repair:* "', '"\n- l. 441', '- l. 429:'), A, [53], "l429", None, "sentence"),
 ("RF", "section 9, MORE, l. 455 (optional)", 455, None, ("b", '*Optional repair:* "', '"\n- l. 479', '- l. 455:'), O, [], "l455", None, "sentence"),
 ("RF", "section 9, MORE, l. 592", 592, ("link",), ("b", '*Repair:* l. 592, "', '"\n- l. 568', None), A, [71], "l592", None, "sentence"),
 ("RF", "section 9, MORE, l. 568 (and l. 317)", 568, ("link",), ("b", '*Repair:* "', '"\n- l. 630', '- l. 568, and l. 317'), A, [70, 48], "l568", None, "span"),
 ("RF", "section 9, INTENDED, l. 25 (R19)", 25, ("link",), ("b", '*Repair, R19:* "', '"\n- l. 27', None), A, [29], "R19", None, "sentence"),
 # ---------------- range 1 check ----------------
 ("R1F", "Repairs, R1 (l. 8)", 8, ("b", 'Replace "', '" with:', '**R1 ('), ("b", '> ', '\n\n**R2', '**R1 ('), A, [27], "R1", None, "sentence"),
 ("R1F", "Repairs, R2 (l. 17)", 17, ("last2",), ("b", '> ', '\n\n**R3', '**R2 ('), S, [], "R2", None, "sentence"),
 ("R1F", "Repairs, R3 (l. 47)", 47, ("link",), ("b", 'l. 47: "', '" l. 61:', '**R3 ('), A, [31], "R3-47", None, "sentence"),
 ("R1F", "Repairs, R3 (l. 61)", 61, ("link",), ("b", 'l. 61: "', '"\n\n**R4', '**R3 ('), A, [32], "R3-61", None, "span"),
 ("R1F", "Repairs, R4 (l. 161)", 161, ("b", 'Replace "', '" with:', '**R4 ('), ("b", '> ', '\n\n**R5', '**R4 ('), A, [35], "R4", None, "sentence"),
 ("R1F", "Repairs, R5 (l. 211)", 211, ("link",), ("b", '"', '"\n\n**R6', '**R5 (l. 211; residue 6).** '), A, [37], "R5", None, "sentence"),
 ("R1F", "Repairs, R6 option A (l. 221)", 221, ("lit", "- **surprise** is a violation of a selected transport at \\((a,b)\\notin H\\)."), ("b", 'at l. 221, "', '" At l. 223:', '**R6 ('), O, [], "R6A-221", None, "paragraph"),
 ("R1F", "Repairs, R6 option A (l. 223)", 223, None, ("b", 'At l. 223: "', '" The heading at l. 215', '**R6 ('), O, [], "R6A-223", None, "paragraph"),
 ("R1F", "Repairs, R6 option A (heading l. 215)", 215, ("lit", "## Prediction, surprise, violation"), ("b", 'The heading at l. 215 becomes "', '", and "recognized', '**R6 ('), O, [], "R6A-215", None, "sentence"),
 ("R1F", "Repairs, R6 option A ('recognized difficulty' at l. 317 and in Part X)", 317, ("lit", "recognized difficulty"), ("lit", "registered difficulty"), O, [], "R6A-rec", None, "term"),
 ("R1F", "Repairs, R6 option B (end of l. 221)", 221, None, ("b", 'at the end of l. 221 add "', '", and give', '**R6 ('), A, [38], "R6B-221", "\\((a,b)\\notin H\\).", "span"),
 ("R1F", "Repairs, R6 option B (the same pointer for 'recognized difficulty' at its first use, l. 223)", 223, None, ("b", 'at the end of l. 221 add "', '", and give', '**R6 ('), A, [39, 55], "R6B-223", None, "span"),
 ("R1F", "Repairs, R7 (l. 43), first sentence", 43, ("lit", "The physical theory fixes which changes are possible at all."), ("b", '**R7 (l. 43; residue 8).** "', '" Last sentence:', None), S, [], "R7a", None, "sentence"),
 ("R1F", "Repairs, R7 (l. 43), last sentence", 43, None, ("b", 'Last sentence: "', '"\n\n**R8', None), S, [], "R7b", None, "sentence"),
 ("R1F", "Repairs, R8 (l. 151)", 151, ("link",), ("b", '**R8 (l. 151; broken 8).** "', '"\n\n**R9', None), A, [33], "R8", None, "span"),
 ("R1F", "Repairs, R9 (l. 159)", 159, ("b", 'Replace "', '" with:', '**R9 ('), ("b", '> ', '\n\n**R10', '**R9 ('), A, [34], "R9", None, "sentence"),
 ("R1F", "Repairs, R10 (l. 201)", 201, ("link",), ("b", '**R10 (l. 201; residue 10).** "', '"\n\n**R11', None), A, [36], "R10", None, "span"),
 ("R1F", "Repairs, R11 (l. 277)", 277, ("first",), ("b", '> ', '\n\n**R12', '**R11 ('), A, [40], "R11", None, "sentence"),
 ("R1F", "Repairs, R12 (l. 299)", 299, ("link",), ("b", '**R12 (l. 299; broken 7).** "', '" At l. 307', None), A, [41], "R12-299", None, "span"),
 ("R1F", "Repairs, R12 (l. 307)", 307, ("b", 'At l. 307, "', '" can then become', '**R12 ('), ("b", 'can then become "', '".\n\n**R13', '**R12 ('), A, [43], "R12-307", None, "span"),
 ("R1F", "Repairs, R13 (l. 315)", 315, ("b", 'Replace "', '" with:', '**R13 ('), ("b", '> ', '\n\n**R14', '**R13 ('), A, [45], "R13", None, "sentence"),
 ("R1F", "Repairs, R14 (l. 317), (i)", 317, ("link",), ("b", 'In (i): "', '" In (ii):', '**R14 ('), A, [46], "R14i", None, "span"),
 ("R1F", "Repairs, R14 (l. 317), (ii)", 317, ("link",), ("b", 'In (ii): "', '"\n\n**R15', '**R14 ('), A, [47], "R14ii", None, "span"),
 ("R1F", "Repairs, R15 (l. 317)", 317, ("link",), ("b", '**R15 (l. 317; broken 4).** "', '"\n\n**R16', None), A, [22], "R15", None, "sentence"),
 ("R1F", "Repairs, R16 (l. 331)", 331, ("link",), ("b", '**R16 (l. 331; broken 8).** "', '"\n\n**R17', None), A, [49], "R16", None, "span"),
 ("R1F", "Repairs, R17 (l. 335)", 335, ("link",), ("b", '**R17 (l. 335; residue 3).** "', '"\n\n**R18', None), A, [50], "R17", None, "span"),
 ("R1F", "Repairs, R18 (l. 369)", 369, ("link",), ("b", '**R18 (l. 369; broken 2).** "', '"\n\n**R19', None), A, [51], "R18", None, "sentence"),
 ("R1F", "Repairs, R19 (l. 25)", 25, ("link",), ("b", '**R19 (l. 25; changed claim 4).** "', '"\n\nOptional clarity', None), A, [29], "R19", None, "sentence"),
 ("R1F", "Repairs, optional clarity, l. 305", 305, ("link",), ("b", 'l. 305 "', '" l. 311', 'Optional clarity'), A, [42], "opt305", None, "sentence"),
 ("R1F", "Repairs, optional clarity, l. 311", 311, ("link",), ("b", 'l. 311 "', '"\n\n**For the Part IX', 'Optional clarity'), A, [44], "opt311", None, "span"),
 # ---------------- range 2 check ----------------
 ("R2F", "section 6, repair 1 (l. 495)", 495, ("link",), ("b", '1. **l. 495.** "', '"\n2.', '## 6. Repairs'), A, [59], "l495", None, "sentence"),
 ("R2F", "section 6, repair 2 (l. 542)", 542, ("toend", "; an argument that every construction trace"), ("b", 'to the end of the item with: "', '"\n3.', '## 6. Repairs'), A, [68], "l542", None, "span"),
 ("R2F", "section 6, repair 3 (l. 544)", 544, ("link",), ("b", '3. **l. 544.** "', '"\n4.', '## 6. Repairs'), A, [69], "l544", None, "paragraph"),
 ("R2F", "section 6, repair 4 (l. 391, Form_j)", 393, ("first",), ("b", '4. **l. 391.** "', '" Optionally also:', '## 6. Repairs'), S, [], "r2-4", None, "sentence"),
 ("R2F", "section 6, repair 4, optional (Scope_j, Live_j)", 393, None, ("b", 'Optionally also: "', '"\n5.', '## 6. Repairs'), A, [26], "b7-391", "does not define it].", "sentence"),
 ("R2F", "section 6, repair 5 (l. 518)", 518, ("link",), ("b", '5. **l. 518.** "', '"\n6.', '## 6. Repairs'), A, [60], "l518", None, "sentence"),
 ("R2F", "section 6, repair 6 (l. 532)", 532, ("link",), ("b", '6. **l. 532.** "', '"\n7.', '## 6. Repairs'), A, [65], "l532", None, "sentence"),
 ("R2F", "section 6, repair 7 (l. 461)", 461, ("link",), ("b", '7. **l. 461.** "', '" With this,', '## 6. Repairs'), A, [57], "l461", None, "span"),
 ("R2F", "section 6, repair 8, (A) (l. 536)", 536, ("link",), ("b", '   - (A): "', '"\n   - End of (A)', '## 6. Repairs'), A, [17], "b6-536", None, "sentence"),
 ("R2F", "section 6, repair 8, end of (A)", 536, ("link",), ("b", '   - End of (A): "', '"\n   - (B)', '## 6. Repairs'), A, [66], "b6-536end", None, "span"),
 ("R2F", "section 6, repair 8, (B) (l. 538)", 538, ("link",), ("b", '   - (B): "', '"\n9.', '## 6. Repairs'), A, [18], "b6-538", None, "sentence"),
 ("R2F", "section 6, repair 9 (l. 526)", 526, ("link",), ("b", '9. **l. 526.** "', '"\n10.', '## 6. Repairs'), A, [64], "l526def", None, "span"),
 ("R2F", "section 6, repair 10 (l. 526, and l. 31)", 526, ("link",), ("b", '(and the same at l. 31): "', '" If the owner keeps', '## 6. Repairs'), A, [63, 30], "b11-526", None, "sentence"),
 ("R2F", "section 6, repair 10, l. 600", 600, ("link",), ("b", 'l. 600 should read "', '"\n11.', '## 6. Repairs'), A, [73], "b11-600", None, "span"),
 ("R2F", "section 6, repair 11 (l. 441)", 441, ("link",), ("b", '11. **l. 441.** "', '"\n12.', '## 6. Repairs'), A, [54], "b13", None, "span"),
 ("R2F", "section 6, repair 12 (l. 397 add)", 397, None, ("b", 'Add after the first two sentences: "', '" Rename', '## 6. Repairs'), A, [25], "b1-397", ("second",), "sentence"),
 ("R2F", "section 6, repair 12 (rename)", 397, ("lit", "\\(R_j(\\psi)\\)"), ("lit", "\\(X_j(\\psi)\\)"), A, [25], "rename-X", None, "term"),
 ("R2F", "section 6, repair 13 (l. 397)", 397, ("last1",), ("b", 'Replace the last sentence with: "', '"\n14.', '## 6. Repairs'), S, [], "b12-397", None, "sentence"),
 ("R2F", "section 6, repair 14 (l. 522)", 522, None, ("b", 'After "(Part XII);" insert: "', '".\n    - **l. 526**', '## 6. Repairs'), S, [61], "b7-522", "(Part XII);", "span"),
 ("R2F", "section 6, repair 14 (l. 526)", 526, None, ("b", 'after "(K1) depends on (E)." insert "', '"\n    - **l. 598**', '## 6. Repairs'), A, [62], "b7-526", "(K1) depends on (E).", "sentence"),
 ("R2F", "section 6, repair 14 (l. 598)", 598, ("link",), ("b", '    - **l. 598**: "', '"\n15.', '## 6. Repairs'), A, [72], "b7-598", None, "span"),
 ("R2F", "section 6, repair 15 (l. 479)", 479, ("link",), ("b", '15. **l. 479.** "', '"\n16.', '## 6. Repairs'), A, [58], "b14", None, "sentence"),
 ("R2F", "section 6, repair 16 (l. 620)", 620, ("link",), ("b", '16. **l. 620.** "', '". **l. 630:**', '## 6. Repairs'), A, [75], "b15-620", None, "span"),
 ("R2F", "section 6, repair 16 (l. 630)", 630, ("link",), ("b", '**l. 630:** "', '"\n17.', '## 6. Repairs'), A, [76], "b15-630", None, "sentence"),
 ("R2F", "section 6, repair 17 (l. 540)", 540, ("link",), ("b", '17. **l. 540.** "', '" **l. 600:**', '## 6. Repairs'), A, [67], "b15-540", None, "sentence"),
 ("R2F", "section 6, repair 17 (l. 600)", 600, ("link",), ("b", '**l. 600:** "', '" **l. 453:**', '## 6. Repairs'), A, [74], "b15-600", None, "sentence"),
 ("R2F", "section 6, repair 17 (l. 453)", 453, ("link",), ("b", '**l. 453:** "', '".\n18.', '## 6. Repairs'), A, [56], "b15-453", None, "span"),
 ("R2F", "section 6, repair 18, optional (l. 403)", 403, None, ("b", '18. **Optional, l. 403.** "', '"\n19.', '## 6. Repairs'), N, [], "opt403", None, "sentence"),
 ("R2F", "section 6, repair 19 (l. 385)", 385, ("link",), ("b", '19. **l. 385.** "', '"\n20.', '## 6. Repairs'), A, [52], "l385", None, "sentence"),
 ("R2F", "section 6, repair 20 (l. 429)", 429, ("link",), ("b", '20. **l. 429.** "', '"\n21.', '## 6. Repairs'), A, [53], "l429", None, "sentence"),
 ("R2F", "section 6, repair 21 (l. 592)", 592, ("link",), ("b", '21. **l. 592.** "', '"\n22.', '## 6. Repairs'), A, [71], "l592", None, "sentence"),
 ("R2F", "section 6, repair 22 (l. 568, and l. 317)", 568, ("link",), ("b", 'outside the range): "', '"\n23.', '## 6. Repairs'), A, [70, 48], "l568", None, "span"),
 ("R2F", "section 6, repair 23, optional (l. 455)", 455, None, ("b", 'kept open.** "', '"', '## 6. Repairs'), O, [], "l455", None, "sentence"),
]

SRCS = {"RF": RF, "R1F": R1F, "R2F": R2F}


def full_sentence(t):
    t = t.strip()
    return bool(t) and not t.startswith("\u2026") and (t[0].isupper() or t[0] in "*#\\(") and t[-1] in ".)]"


def build(next_rid, prior, texts):
    src = {k: Src(v) for k, v in SRCS.items()}
    sc = texts["scrubbed copy"]
    H = headings(sc)
    s1 = {r["_key"][1]: r for r in prior if r.get("_key", ("",))[0] == "S96-1"}
    out = []
    groups = {}
    for (sk, ref, line, ospec, nspec, status, links, group, anchor, scope) in ITEMS:
        S_ = src[sk]
        new = S_.between(*nspec[1:]) if nspec[0] == "b" else nspec[1]
        L = sc[line - 1]
        old = ""
        if ospec:
            if ospec[0] == "b":
                old = S_.between(*ospec[1:])
            elif ospec[0] == "lit":
                old = ospec[1]
            elif ospec[0] == "link":
                old = s1[links[0]]["old"] if s1[links[0]]["target_line"] == line else ""
            elif ospec[0] == "last1":
                old = sentences_of(L)[-1]
            elif ospec[0] == "line":
                old = L
            elif ospec[0] == "last2":
                old = " ".join(sentences_of(L)[-2:])
            elif ospec[0] == "first":
                old = sentences_of(L)[0]
            elif ospec[0] == "toend":
                old = L[L.index(ospec[1]):]
        if anchor == ("second",):
            anchor = sentences_of(L)[1]
        os_, ns_, found = place(texts, "scrubbed copy", line, old, new, anchor)
        if ospec and ospec[0] == "link":
            o, n_ = old.strip(), new.strip()
            similar = (o and n_ and not n_.startswith("\u2026") and o[0].isupper() == n_[0].isupper()
                       and o[-1] == n_[-1])
            if not similar:
                ns_ = new if full_sentence(new) else ""
        if not os_ and not old:
            os_ = ""
        applied_in = "repaired copy" if status == "applied" else "none"
        extra = ""
        if anchor and len(anchor) > 80:
            extra = "; to be inserted after the sentence beginning: %s" % anchor[:60]
        elif anchor:
            extra = "; to be inserted after: %s" % anchor
        r = rec(next_rid(), "S95", SRCS[sk], ref + extra, "recommendation", status, applied_in,
                "scrubbed copy", line, H, old, new, os_, ns_, scope)
        r["same_as"] = [s1[k]["rid"] for k in links]
        r["_key"] = ("S95rec", sk, ref)
        r["_old_from"] = ospec[0] if ospec else "none"
        groups.setdefault(group, []).append(r)
        out.append(r)
    for g, rs in groups.items():
        for r in rs:
            r["same_as"] += [o["rid"] for o in rs if o is not r]
    return out
