# S104: Round 2, the grouping of the checkers, recorded before any ruling

*Written by the orchestrator (Claude) on 28 September 2026, after the tabulation (commit 594f9a1) and before any checker was started. No ruling exists yet. The reading rule (`results/S104 Round 2 - how the replies will be read, written before sending.md`) and its two addenda are not changed. This file records how rule 5's grouping was carried out, and one departure from its letter, with the reasons. Decided under decision S13 ("You make the big decisions").*

## What rule 5 asks

Rule 5 asks for three things:
1. Items are grouped by the line or lines of the text they would change.
2. "Each group goes to one fresh Opus 5.5 checker of its own, who built nothing of this round and rules on no other group of it, so that no line of the text has two checkers."
3. Every item a reader challenges goes to a checker, and so do the twelve counterexamples.

## What the tabulation gave

The tabulation sends 349 items to checkers. Each item carries the lines of `tests/103 The semantics, standing alone, after round 1.md` that it bears on.

Grouping the items transitively (items that share a line go together, and so on) gives 55 groups:
- 53 groups of 1 to 12 items;
- one group of 92 items over 23 lines, from L57 to L574;
- one group of 109 items over 38 lines, from L13 to L604.

The two large groups form because a few lines are shared by many items. L109, L119, L255, L315 and L317 carry 14 to 18 items each, and a handful of items name lines in several Parts.

## The departure, and why

A single checker for 92 or 109 items would have to read, for each item:
- both readers' passages;
- the tabulation's rows;
- the formal statements, inventions and the second check's entries;

and then rule on 23 or 38 lines. That is more than one agent can weigh with the care rule 5 asks for, and the rule's own reason for grouping is stated in its last clause: "so that no line of the text has two checkers".

So the two large groups are split by the section of the text each line stands in. Every line still has exactly one checker, and no checker rules on a line outside its own set.

The splitting works like this:
- **Each line goes to the sub-group of its section** (the nearest heading above it).
- **Sections with no item of their own are merged.** A section whose lines are the home of no item is merged into the sub-group where most of its items have their home. This is how L13 goes with L193–L201, L77 with L47–L55, L219 with L151, L568 with L315–L317, and L604 with L161.
- **Each item has one primary checker:** the checker holding most of its lines, or, where two tie, the one whose section comes first. The primary checker rules on what the item comes to (rule 5's second paragraph), and on the item's lines in its own set.
- **An item whose lines fall in more than one sub-group is also a shared item** for each other checker holding one of its lines. That checker weighs the item's points as they bear on its own lines, rules only those lines, and does not rule on what the item comes to.
- **Context items.** The context items (E- and C-items that challenge no line) go to every checker whose lines they name, as the addenda say.
- **The critical review** (rule 13) reads the rulings of every shared item side by side and names any conflict between them. It is told that this grouping was made.

The 53 small groups are unchanged: one checker each, as rule 5 says.

**In all:** 78 checkers, 140 lines, each line with one checker, and each of the 349 items with one primary checker. The program that made the split checked all three.

## What each checker is given

Rule 5 lists what each checker is given: the part briefs, the text, both readers' passages whole, the tabulation's rows, the maths files and both checks whole (including the check of the formalization's sections 2 and 3), and the rule.

All of these are named to each checker and left open to it whole. Each checker reads in them what bears on its items, not every file from end to end. For each of its items it must read:
- the passages of the replies;
- the rows of the tabulation;
- the entries of the maths files and of the two checks.

This is a reading of "is given" and not a narrowing of what the checker may use.

**Concurrency.** The checkers run at most four at a time, in two runs of two each. That is within the rule's limit of five.

## The checkers

The same list, with every item's lines, is in `results/S104 Round 2 - the grouping of the checkers, recorded before any ruling.json`.

| checker (ruling file name) | its lines | primary items | shared items (lines here) | context |
|---|---|---|---|---|
| L3-L538 | L3, L17, L43, L67, L277, L363, L536, L538 | FC30, FC66, NF01, NF02, NF03, E06, E15, E22 | — | E18 |
| L13-L201 | L13, L193, L195, L197, L199, L201 | D12.1, D12.2, D12.3, FC77, FC78, FC81, FC82, I52, I53, H05, H13, NF07, E03, C01, C02, C04, C11 | E14 (here L201), C03 (here L195), C07 (here L197) | E11, C13 |
| L27 | L27 | matter 14 | — | — |
| L41 | L41 | FC79 | — | — |
| L47-L77 | L47, L55, L77 | FC84, H06, E14, C07 | — | — |
| L57 | L57 | FC10, I09 | — | — |
| L91-L103 | L91, L103 | D1.1, D1.3, D2.1, I01, I02, I03, I04, H03, H18, E04 | — | — |
| L109 | L109 | D2.2, D2.3, D2.4, D2.5, FC02, FC11, I05, I06, I80, H04, matter 5, L123 | D2.1 (here L109), I04 (here L109), E04 (here L109) | — |
| L113-L127 | L113, L119, L121, L123, L124, L125, L127 | D4.2, D4.3, D4.4, D4.5, D4.6, FC05, FC06, FC07, FC08, FC09, FC12, FC13, FC14, I07, I08, I10, I11, I12, I93, I94, I102, U4, U5, H01, H02, matter 4, E05 | D2.1 (here L119), FC18 (here L119), I09 (here L119), matter 5 (here L113), L123 (here L123), E04 (here L119) | E07 |
| L138-L141 | L138, L141 | D3.1, D3.2, I21, I82 | I20 (here L138) | — |
| L151-L219 | L151, L219 | D3.3, D3.7, FC34, FC35, FC36, I51, I72, I73, matter 6 | — | E07, C08 |
| L155 | L155 | D3.4 | — | H20 |
| L159-L522 | L159, L473, L522 | D15.4, E13 | — | E01, E07, C09, C10 |
| L161-L604 | L161, L604 | D3.6, FC105, FC106, FC107, I76 | — | — |
| L169 | L169 | D11.1, D11.2, I45, I48, matter 2 | FC105 (here L169) | — |
| L189 | L189 | D5.1, D5.2, FC20, I14, I16, I17, I81 | — | — |
| L205-L211 | L205, L211 | D12.5, FC95, C03 | I48 (here L205) | E01 |
| L217-L225 | L217, L220, L221, L225 | D11.5, D12.7, D12.8, FC83, I50, I56, H07, H08, C05 | D5.7 (here L220), FC20 (here L220), FC82 (here L225), FC104 (here L220), I49 (here L220), H13 (here L217), matter 12 (here L220) | E08, E11, C08 |
| L231-L253 | L231, L233, L245, L247, L250, L253 | D5.3, D5.4, D5.6, D5.7, FC17, FC19, FC104, I15, I20, I49, U1, matter 12 | D3.1 (here L253), D3.2 (here L253), D5.1 (here L231), D5.2 (here L233), I14 (here L233), I21 (here L250) | E01, C12 |
| L242 | L242 | D5.5, I18, I84 | — | — |
| L255-L257 | L255, L257 | D3.5, D6.3, D6.4, D6.5, D6.6, D6.9, FC01, FC21, FC23, FC26, I22, I24, I25, I26, I27, I28, I79, I83, U6, E19 | FC34 (here L255), I03 (here L255) | — |
| L265 | L265 | FC33 | — | — |
| L269 | L269 | D6.10, FC25, I32 | — | E18 |
| L271 | L271 | FC27 | — | — |
| L273 | L273 | FC24, matter 7 | — | — |
| L275 | L275 | FC29 | — | — |
| L287-L313 | L287, L296, L299, L305, L313 | D7.1, D7.3, D7.5, D7.6, FC41, I29, E02 | — | E21 |
| L302 | L302 | D7.4 | — | — |
| L307 | L307 | I30 | — | — |
| L311 | L311 | FC40, I31, matter 8, matter 13 | — | — |
| L315-L568 | L315, L317, L568 | D8.1, D8.2, D8.3, D8.5, D10.1, D10.2, D10.3, D10.4, D10.5, D10.6, FC43, FC44, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC53, I19, I33, I34, I35, I36, I37, I86, H10 | D5.1 (here L315), I17 (here L315) | H20 |
| L325 | L325 | FC28, I65, I92 | FC02 (here L325), FC27 (here L325), I79 (here L325) | — |
| L329 | L329 | FC57, FC58, I63, I64 | — | — |
| L331 | L331 | FC60 | — | — |
| L339 | L339 | FC62 | D1.3 (here L339), I03 (here L339) | — |
| L343 | L343 | FC63, I66, I99 | — | — |
| L353 | L353 | FC64 | — | — |
| L361 | L361 | FC65 | — | — |
| L365 | L365 | FC67 | — | — |
| L369 | L369 | FC68 | — | — |
| L375-L385 | L375, L385 | D9.11, D11.3, D11.4, FC75, FC76, I44, I46, I47, I95, H11, H19, matter 11 | — | — |
| L377 | L377 | D9.10, H12 | — | — |
| L383 | L383 | FC74 | — | — |
| L387-L393 | L387, L393 | D9.4, D9.5, D9.6, FC56, FC69, FC70, I40, I41, I42, I89, matter 9 | — | E16 |
| L395 | L395 | D9.9, FC71, I43 | — | — |
| L397 | L397 | D9.1, D9.7, FC72, I38, I39, I87, I88 | — | E16 |
| L403 | L403 | D13.1, I55 | — | — |
| L405-L429 | L405, L409, L411, L429 | D12.4, D13.3, D13.8, I54, H15, C06 | I53 (here L409), I56 (here L405), H05 (here L411), H06 (here L429), E03 (here L405), C02 (here L411) | E01, E09, E16, C10 |
| L413 | L413 | D13.4, FC85 | — | C09 |
| L425-L590 | L425, L590 | E8, FC97, I67, E20 | — | — |
| L427 | L427 | H14 | — | C14 |
| L441 | L441 | D14.1, D14.3, FC86, FC87, FC88, I57, I58 | — | C10, C14 |
| L443-L628 | L443, L453, L628 | D14.5, D14.6, FC89, FC90, I59, I60, L443 | — | C10 |
| L447-L449 | L447, L448, L449 | D14.7 | — | — |
| L455 | L455 | D14.8 | — | — |
| L461 | L461 | D15.1 | — | — |
| L466-L495 | L466, L479, L495 | D15.2, D15.7, D16.3, FC93, I62, NF11, E17 | — | C12 |
| L469-L471 | L469, L471 | FC91, FC92, I61, matter 10, L471 | — | — |
| L475 | L475 | D15.5 | — | H20 |
| L477 | L477 | D15.6 | — | — |
| L481 | L481 | D15.8, H09 | — | C13 |
| L487 | L487 | D16.1, H16 | — | — |
| L492 | L492 | D16.2, I74 | — | — |
| L497 | L497 | I75 | — | — |
| L509 | L509 | FC94 | — | — |
| L520-L526 | L520, L526 | D6.7, D6.8, D18.1, FC31, FC32, FC98, L520 | D5.7 (here L520), FC104 (here L520), I49 (here L520), matter 12 (here L520), E03 (here L526) | — |
| L528 | L528 | D16.4, D16.5 | — | H20 |
| L542 | L542 | NF05 | E14 (here L542) | — |
| L554-L558 | L554, L556, L558 | FC15, FC18, I13, matter 1 | D4.4 (here L556), I12 (here L554) | — |
| L562 | L562 | FC96 | — | — |
| L572-L574 | L572, L574 | D12.9, FC80, I71 | I02 (here L574) | C13 |
| L584 | L584 | matter 3 | — | E08, E11 |
| L596 | L596 | D13.6 | FC98 (here L596) | — |
| L606 | L606 | FC99 | — | E07 |
| L612 | L612 | FC100, I70 | — | — |
| L616 | L616 | FC101 | — | — |
| L620-L626 | L620, L622, L624, L626 | E9, FC102, I68, I100, H17, E10 | — | — |
| L630 | L630 | FC103, I69 | — | — |
