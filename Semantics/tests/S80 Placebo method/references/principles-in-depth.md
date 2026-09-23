# Principles in depth

This file says what a careful review involves in full, and gives the reason behind each step of the procedure. Each section starts with a concrete example and then gives the general point.

Contents: 1 What a review is for. 2 Reading at two speeds. 3 Why keep an inventory. 4 Terms. 5 Cross-references and numbering. 6 Arithmetic and worked examples. 7 Proofs and derivations. 8 Quotations and citations. 9 Clarity and structure. 10 Audience. 11 Notation. 12 Severity and proportion. 13 What a review is not. 14 Traps.

---

## 1. What a review is for

**Example.** A user manual for a dishwasher tells the reader to "press START, then select the programme". On the machine, pressing START with no programme selected does nothing, and the manual's own diagram shows the programme dial being turned first. Nobody who wrote the manual was wrong about the machine. The sentence was simply written in the wrong order, and every reader who follows it will stand in front of a machine that does not start.

**Point.** A document exists to be used by readers who will not be able to ask the author what was meant. The reviewer stands in for those readers, but with more patience: the reviewer checks what a reader would take on trust. A review is therefore measured by one thing: how many of the problems that would cost a reader something have been found, located and explained in a way the author can act on.

This has three consequences.

- **Findings are about the text.** The question is always what the document says, not what the author meant. If the author meant something else, the text needs to change.
- **Findings carry their costs.** Each finding should make clear what would go wrong for a reader if it stayed. That is how the author, and you, decide what to fix first.
- **Coverage matters as much as findings.** A review that found five problems in the first half and never read the second half is worse than useless if it does not say so: it gives false confidence about the half nobody checked.

---

## 2. Reading at two speeds

**Example.** A reviewer starts a forty-page technical report at page one and reads slowly. By page twelve they have written ten notes asking what "the adjusted index" is. On page thirty the report defines it, in a box headed "Methods note". Nine of the ten notes were wasted, and the tenth, that the term is used long before it is defined, is the only finding.

**Point.** Read twice, at two speeds.

- **The skim** builds a map: purpose, main claim, structure, where the definitions are, where the evidence is, where the conclusions are. It takes a small fraction of the time of the close read and saves more than it costs. Its output is a sentence or two stating the document's main claim or purpose, in your own words, and a rough outline.
- **The close read** goes sentence by sentence, with the map in hand. Now a term used before its definition is a finding about order, not a mystery. A conclusion that goes beyond the evidence is visible, because you know where the evidence was.

A third, quicker pass at the end, with your notes, removes notes answered elsewhere and confirms the rest. Many first impressions are wrong; the second pass is where you find out which.

For a long document, the close read can be split across sessions, but keep the order. Reading sections out of order loses exactly the thing a reader will experience: meeting ideas in sequence.

---

## 3. Why keep an inventory

**Example.** A specification defines "user" in section 2 as "any person with a login". In section 7 it says "users may not see admin pages", and in section 9 "users with admin rights can edit settings". Read one at a time, each sentence is clear. Read against section 2, section 7 and section 9 cannot both hold for a person with a login and admin rights.

**Point.** Most inconsistencies are between places far apart. Memory does not hold the exact wording of a definition from twenty pages back; it holds a rough sense of it, which is exactly the level at which the inconsistency is invisible. An inventory is a written list of the things you will need to compare: defined terms and their definitions, symbols and their meanings, numbered items and their numbers, key figures and each place they appear, main claims and where they are supported, and sources and what they are cited for.

With an inventory, every consistency check becomes a lookup. Without one, it becomes a feat of memory, and memory tends to confirm what it expects.

Build the inventory during the skim and complete it during the close read. For a document of a few pages, it can be a handful of lines. For a long document, it is the most useful thing you will write.

---

## 4. Terms

**Example.** A policy document says in its opening that "staff" means "employees on permanent contracts". Later it says "all staff, including contractors, must complete the training". A contractor reading the first definition concludes the training does not apply to them; a manager reading the later sentence concludes it does.

**Point.** A technical term makes an implicit promise: every time it appears, it means the same thing. Check that promise in three ways.

- **Defined before use, or safely assumed.** Either the term is defined at or before its first appearance, or the intended reader can be expected to know it. If the definition comes later, note the first use.
- **Used in one sense.** Check each use against the definition. Watch especially for a term that starts precise and becomes casual: "significant" defined statistically in the methods, then used to mean "large" in the discussion.
- **One word for one thing.** If the document uses "client", "customer" and "account holder", the reader will wonder whether these are three groups or one. If they are one, say so and suggest picking one word. If they are three, check that each is defined.

Also check the definitions themselves. A definition should be clear about what it includes and excludes, should not depend on a term defined only later, and should agree with any other definition of the same term elsewhere in the document, including glossaries, footnotes and appendices.

---

## 5. Cross-references and numbering

**Example.** A paper says "as shown in Figure 3, the effect is largest at low temperature". Figure 3 shows a map of sampling sites. The temperature plot is Figure 4. A figure was added to an earlier draft, the numbering moved, and the text was not updated.

**Point.** Cross-references break silently. Every edit that adds, removes or moves a section, figure, table, equation or theorem can break every pointer after it. The only reliable check is to follow each one.

For each pointer check three things: the target exists, it carries that number, and it shows or says what the pointer claims. "See section 4" when section 4 exists but is about something else is as bad as a pointer to nothing.

Check numbering itself: sections, figures, tables, equations and footnotes run in sequence, with no gaps or repeats, and numbering styles match (not "Table 2" in one place and "Tab. II" in another). Check vague pointers ("above", "earlier", "as discussed") as well: they point to something, and a reader should be able to find it. If "as discussed above" refers to something thirty pages back, suggest a precise reference.

Check the contents list, list of figures and index, if any, against the actual headings and page numbers.

---

## 6. Arithmetic and worked examples

**Example.** A budget proposal lists five items adding to "Total: £52,300". The items are £12,000, £8,500, £15,200, £9,800 and £6,300, which add to £51,800. The £500 difference turns out to be a line removed from an earlier draft. A reader who checks will lose confidence in every other figure in the proposal.

**Point.** Redo every calculation you can. This is tedious and it is where many of the most damaging errors are found, precisely because readers and authors both assume the numbers are right.

- **Totals and subtotals.** Add them up.
- **Percentages.** Check the numerator, the denominator, and which base is being used. "An increase of 50% then a decrease of 50%" does not return to the start. "Percentage points" and "percent" are different.
- **Averages.** Check whether mean or median is meant, and whether the average is over the right group.
- **Units and conversions.** Check that units are stated, that they match across the document, and that conversions are correct. A factor of 1,000 is a common slip.
- **Rounding.** Check that rounded figures are consistent with each other and with any stated precision. A breakdown whose parts add to 101% is normal with rounding; one that adds to 110% is not.
- **Repeated figures.** Each number that appears more than once should agree everywhere it appears: summary, body, tables, figures, abstract, slides.
- **Order of magnitude.** Before checking the detail, ask whether each number is roughly the size it should be. A town of 10,000 people does not have 40,000 households.

**Worked examples** deserve special care, because readers copy them. Work each one yourself from the stated inputs, without looking at the author's answer first. Then compare. If you get a different answer, check your own work before reporting, then report both answers and where they part. Also check that the example actually illustrates the method it is attached to: an example that uses a shortcut the method does not describe teaches the wrong method.

---

## 7. Proofs and derivations

**Example.** A proof by induction shows that if the statement holds for n, it holds for n + 1. It never checks the starting case. The statement turns out to fail for n = 1. The step from n to n + 1 was sound, but the chain had nothing to start from, so the proof shows nothing at all.

**Point.** A proof is a chain of steps, each of which must follow from what came before by a stated or standard rule. Check it one step at a time.

- **Name the licence for each step.** For each line, say to yourself what justifies it: a definition, an earlier lemma, an assumption, a standard result, algebra. If you cannot name it, either the step is wrong or it needs more explanation. Both are findings, of different severity.
- **Check the statement and the conclusion match.** The proof should end with exactly what the theorem states: the same objects, the same quantifiers, the same cases. A proof of "every A is a B" that ends by showing "some A is a B", or a proof of the converse, is a common slip.
- **Watch the order of quantifiers.** "For every x there is a y" is not "there is a y for every x". Proofs often slide between them.
- **Check every case is covered.** If the proof splits into cases, check the cases together cover everything. Watch for the case of equality, the empty set, zero, the single element, and the boundary.
- **Check divisions and inverses.** Dividing by a quantity needs it to be non-zero. Taking a square root, a logarithm, an inverse, needs its own condition. Check each is secured.
- **Check that what is used is available.** Every assumption the proof leans on should appear in the statement, in an earlier result, or in a clearly stated standing assumption. An assumption that appears only in the middle of the proof is a gap in the statement.
- **Check cited results.** If a step cites "Lemma 2" or "a standard result", check that the result says what is needed and that its conditions are met here.
- **Try a small case.** Pick a small, concrete instance of the statement and check it by hand. This does not prove anything, but it catches statements that are simply false, and it helps you follow the proof.

Derivations in applied work follow the same rules: check each algebraic step, check that approximations are stated and justified where they are made, and check that the final formula has consistent units on both sides.

---

## 8. Quotations and citations

**Example.** An essay quotes a historian as saying the treaty "made war inevitable". The historian's actual sentence is that the treaty "made war more likely than it had been, though not inevitable". The quotation marks surround words that appear in the source, in a different order and with the opposite sense.

**Point.** Quotations and citations are claims about other documents, and they can be checked only by looking at those documents.

- **Quotations** must match the source word for word, with any omission marked by an ellipsis and any insertion by square brackets, and must not change the sense by what they leave out. Check the page or location given.
- **Citations** must support what they are cited for. A citation attached to a specific claim should contain that claim, or evidence for it. A citation to a whole book for a specific figure is not enough; ask for a page.
- **Reference details** must be correct and consistent: authors, year, title, venue, pages, and the same form throughout. Each in-text citation should appear in the reference list, and each entry in the list should be cited.

If you cannot open a source, say so plainly and list the citation as unchecked. Do not mark it as correct because it looks plausible or because you remember it. See `checking-sources.md` for the full method.

---

## 9. Clarity and structure

**Example.** A report's key recommendation appears in the second half of paragraph six of section four, after a long discussion of alternatives, and nowhere else. The executive summary lists the alternatives but not the recommendation.

**Point.** A document can be correct in every line and still fail its reader. Check the structure at three scales.

- **The whole.** Does the order let the reader meet each idea before it is needed? Is the main point stated early and restated where the reader will look for it: summary, introduction, conclusion? Does each section's heading describe what is in it?
- **The paragraph.** Does each paragraph have one job, and does its first sentence tell the reader what that job is? A paragraph that starts with a method, turns into a result and ends with a caveat is three paragraphs.
- **The sentence.** Can each sentence be read once and understood? Watch for long sentences with nested clauses, pronouns whose reference is unclear ("this", "it", "they"), strings of nouns ("user access control policy review process"), negatives stacked on negatives, and passive sentences that hide who does what when it matters.

A structural finding is worth making when it would cost a reader something: time, understanding, or the main point. It is not worth making because you would have organised it differently.

---

## 10. Audience

**Example.** A guide "for new volunteers" at a food bank explains the charity's governance structure over three pages, and then says "follow the standard FIFO procedure in the stockroom" without saying what FIFO is.

**Point.** Every document has an intended reader, stated or implied. Check the document against that reader.

- **What they already know.** Terms the reader knows can be used freely. Terms they do not know must be explained. The same term can be basic for one audience and obscure for another.
- **What they need.** A reader who has to act needs steps, in order. A reader who has to decide needs options, costs and a recommendation. A reader who has to check needs the evidence and the method.
- **What they will read.** Many readers read only the title, summary and headings. Check that those alone give a true picture.

If the intended audience is not stated, infer it from the document's purpose and say which audience you assumed.

---

## 11. Notation

**Example.** In a set of lecture notes, *n* is the sample size in chapter 1, the number of groups in chapter 3, and an index of summation in chapter 4. A student reading chapter 4 with chapter 1 in mind will misread the key formula.

**Point.** Notation is a vocabulary, and the same rules apply as for terms, with extra force, because symbols carry no hints of meaning.

- **One meaning per symbol,** at least within any stretch the reader will hold in mind at once. If a symbol must be reused, say so at the point of reuse.
- **One symbol per meaning.** Do not write the same quantity as *x* in one place and *X* in another, unless the difference is intended and explained.
- **Introduce near first use.** Define each symbol where it first appears, and consider a table of notation for a long document.
- **Consistent conventions.** Bold for vectors, capitals for sets, hats for estimates: whatever the convention, keep it throughout. Check subscripts and superscripts are not interchanged.
- **No more notation than needed.** A symbol used once can often be replaced with words.
- **Displayed formulas are part of the sentence.** Check they are punctuated and that the text around them reads grammatically.

---

## 12. Severity and proportion

**Example.** A review lists forty-two comments in page order. Comment 31 notes that the main table's totals are wrong, which changes the conclusion. The author, working down the list, fixes thirty typos, runs out of time, and resubmits with the wrong table.

**Point.** Grade every finding, and order the report by grade. A usable scale has three or four levels:

- **Critical:** changes a main conclusion, makes the document unsafe or unusable, or would mislead a reader on something that matters.
- **Major:** a clear error or inconsistency that a careful reader would notice and that damages trust, but that does not change the main conclusion.
- **Minor:** a small error or unclear passage that costs the reader a little time or confidence.
- **Mechanical:** typos, formatting, spelling, punctuation.

When in doubt between two grades, pick the higher and say why. Keep the review in proportion to the document and to the brief: a proofread of a final draft does not need a critique of the structure, and a structural review of a first draft does not need every comma.

---

## 13. What a review is not

- **Not agreement or disagreement.** You can think the author's position is wrong and still report only the document's errors, or think it is right and still find many errors. If you are asked for your view on the position, give it separately and label it.
- **Not a rewrite.** Suggest corrections where something is wrong or unclear. Do not replace the author's voice with yours.
- **Not a proof of correctness.** A review that finds nothing shows that you did not find anything, in the parts you checked, with the checks you ran. Say what you checked.
- **Not a line edit.** Unless the brief asks for it, do not mark every sentence you would tighten. Mark the ones a reader would stumble on.
- **Not about taste.** Preferences of style are worth a comment only if a house style or a stated standard requires them.

---

## 14. Traps

- Starting the close read before the skim, and wasting notes on things explained later.
- Checking consistency from memory instead of from an inventory.
- Trusting a number because it is round, familiar, or in a summary.
- Reading a worked example instead of working it.
- Accepting "it is well known that" in a proof without checking what is claimed to be known.
- Leaving a finding without its location or its grade.
- Reporting a style preference as an error.
