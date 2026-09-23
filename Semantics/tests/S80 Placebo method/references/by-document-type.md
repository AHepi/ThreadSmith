# By document type

This file shows what the checks look like in different kinds of document. The method is the same everywhere. What changes is what the reader needs, where errors tend to hide, and which checks find the most. Each section gives those three and a small example.

Contents: 1 Research papers. 2 Reports and proposals. 3 Specifications and requirements. 4 Proofs and mathematical notes. 5 Manuals and instructions. 6 Policies, rules and contracts. 7 Essays and arguments. 8 Theories and technical frameworks. 9 Traps.

---

## 1. Research papers

- **Reader needs:** to know what was found, how, and how far to trust it.
- **Where errors hide:** between the abstract and the results; between the methods and what was actually done; in tables that were updated after the text was written.
- **Checks that find the most:** figures repeated across abstract, text and tables; sample sizes through every stage; citations for background claims; whether the conclusion says more than the results show.

**Example.** An abstract says 120 people took part. The methods say 128 were recruited and 8 withdrew. The results table has 118 rows. The discussion says "all 120". The reviewer lists all four places together, asks which is right, and notes that the percentages in the table, computed on 118, will each shift slightly if 120 is correct.

Also check that each figure and table is referred to in the text, that statistical tests are named, and that the claims in the discussion stay within what the results support. Where a claim goes further, say so, and suggest wording that matches the evidence.

---

## 2. Reports and proposals

- **Reader needs:** a clear recommendation or finding, the reasons for it, and the costs.
- **Where errors hide:** in totals, in the summary, and in figures copied from other documents.
- **Checks that find the most:** add every table; check each summary figure against the body; check dates and deadlines against each other; check that every option listed is actually discussed.

**Example.** A proposal gives a start date of 1 March and a twelve-month project "ending 31 January". The budget table covers March to February. The reviewer notes the conflict, points out that one of the three is wrong, and asks which.

Also check that the recommendation is stated in the summary, not only in the body, and that the report answers the question it was commissioned to answer.

---

## 3. Specifications and requirements

- **Reader needs:** to know exactly what must be built or done, and how it will be checked.
- **Where errors hide:** in terms defined strictly and then used casually (see section 4 of `principles-in-depth.md`); in "should" and "must" used interchangeably; in numbered requirements that refer to each other.
- **Checks that find the most:** terms against definitions; each requirement's wording for a single clear meaning; cross-references between requirements; numeric limits and their units.

**Example.** Requirement 4.2 says the page "must load in under 2 seconds". Requirement 7.1 says "response times shall not exceed 2,000 ms under normal load". A tester cannot tell whether these are the same requirement, whether "normal load" applies to 4.2, or which wins if they conflict. The reviewer asks for one requirement or a stated relationship between the two.

Also check that each requirement can be tested as written, that modal words (must, shall, should, may) follow a stated convention, and that every requirement has a unique number.

---

## 4. Proofs and mathematical notes

- **Reader needs:** to follow each step, and to know exactly what has been proved.
- **Where errors hide:** in steps marked "clearly" or "it is easy to see"; in the base case; in division by quantities that might be zero; in the gap between the statement and the last line.
- **Checks that find the most:** a licence for each step; statement against conclusion; order of quantifiers; every case covered; small concrete instances worked by hand.

**Example.** A note states: "For all positive integers *n*, the sum 1 + 3 + 5 + ... + (2*n* − 1) equals *n*²." The proof checks *n* = 1, assumes the result for *n*, and adds the next term, 2*n* + 1, to get *n*² + 2*n* + 1 = (*n* + 1)². Each step can be named: base case by arithmetic, inductive step by algebra. The reviewer confirms it and moves on. In a second lemma, the proof writes "clearly the maximum is attained". The set is open, so the maximum need not exist. The reviewer asks for an argument or a change to "supremum".

Also check notation against a notation table if there is one, that every cited lemma is stated before use, and that numbered equations referred to later have the right numbers. See section 7 of `principles-in-depth.md`.

---

## 5. Manuals and instructions

- **Reader needs:** to carry out a task, in order, without help.
- **Where errors hide:** in the order of steps; in names of buttons, menus and parts that no longer match the product; in steps that assume a state the reader may not be in.
- **Checks that find the most:** do the task following only the text, if you can; check every named control exists with that name; check each step says what the reader should see afterwards.

**Example.** Step 3 says "Click Save". The current version of the software labels the button "Apply". Step 5 says "Return to the main screen" but no step says how. The reviewer lists both, and suggests adding what the reader should see after step 4 so they can tell whether they are on track.

Also check warnings come before the step they apply to, not after, and that each step contains one action.

---

## 6. Policies, rules and contracts

- **Reader needs:** to know what applies to them, what they must do, and what happens if they do not.
- **Where errors hide:** in definitions at the start that the body forgets; in lists of who is covered; in exceptions stated in one section and forgotten in another; in dates, amounts and notice periods.
- **Checks that find the most:** each defined term against every use; each cross-reference to a clause; every amount, date and period against every other mention; the list of who is covered against every "all" and "any" in the body.

**Example.** Clause 2 defines "Notice Period" as 30 days. Clause 9 says the agreement may be ended "on 60 days' notice". Clause 12 refers to "the Notice Period set out in clause 8", and clause 8 is about payment. The reviewer lists all three and asks which period is intended, and where the reference in clause 12 should point.

Also check that capitalised defined terms are capitalised every time they are used in the defined sense, and not when they are not.

---

## 7. Essays and arguments

- **Reader needs:** to follow the argument and to see what supports each step.
- **Where errors hide:** in quotations; in claims presented as facts without a source; in the gap between the introduction's promise and the conclusion's delivery.
- **Checks that find the most:** quotations against sources; each factual claim for a source or a reason; the thesis stated in the introduction against the conclusion; each paragraph's link to the thesis.

**Example.** The introduction promises to show three causes of a decline. The body discusses two. The conclusion says "these three causes". The reviewer points out the missing third, and asks whether it was cut or is to be added.

Also check that the argument addresses the obvious objections a reader would raise, and that counter-evidence the author cites is described fairly.

---

## 8. Theories and technical frameworks

*Documents that set out definitions, axioms or principles, and build results on them.*

- **Reader needs:** to understand each definition exactly, to follow each derived result, and to apply the framework to cases of their own.
- **Where errors hide:** in definitions that are stated once formally and then paraphrased informally in ways that differ; in results that cite definitions by number after renumbering; in worked examples that apply a definition differently from how it is stated; in claims in the summary that the body does not establish.
- **Checks that find the most:** a full inventory of definitions, with each use checked against its definition; every numbered cross-reference followed; every worked example redone from the definitions alone; each stated result checked against its proof or derivation; the summary and the list of claims checked against the body.

**Example.** A framework defines, in its second part, a "stable" arrangement as one in which every element has at least three neighbours. A later section calls an arrangement stable because "each element has more than three neighbours", and a worked example in an appendix counts an element with exactly three neighbours as not stable. The reviewer notes that the later section and the appendix both depart from the definition, in the same direction, asks whether the definition or the two uses should change, and checks whether any result that relies on the definition is affected.

Also check that informal glosses match the formal definitions they gloss, that every symbol in a formal statement is defined, that each result's proof proves the statement as given, and that the document's statements about its own scope match what it actually covers.

---

## 9. Traps

- Treating every document the same, and missing where this kind tends to go wrong.
- Reviewing a manual without trying to follow it.
- Reviewing a contract clause by clause without checking the defined terms against every use.
- Accepting a theory's informal summary as a faithful statement of its formal content.
- Forgetting that the summary, abstract or introduction is also part of the document, and often the part with the most errors.
