# Predictions, written before looking (A3, W10 stage A)

Written 22 September 2026 by the A3 collector, before any web search was run. The
skill's trap this obeys: "Looking before writing down what would count against you.
Research done with no predictions written first can only ever agree with you."
(HV file 33, SKILL.md, Traps).

Nothing below was edited after the first search. Every line is marked *tested* or
*untested* in `evidence.md` section 8, with what happened.

## What I am looking for

W8 A6 names the check: "look in the trainer's record for an occurrence realising a
member of H that represents the survival condition at the grain of text, the sharpest
candidate being a text of the principles used as the criterion."

So three separate things, kept apart:

- **(T1) loss/optimizer text.** Does the record of a corpus state that the corpus
  contains texts that state a training loss or an optimizer?
- **(T2) preference rule or principle list.** Does it state that the corpus contains a
  written list of principles or a preference rule used as a training criterion?
- **(T3) the self-case.** Does any published corpus contain, by its own documentation,
  a document that states the loss function of a model trained on that corpus?

(T3) is the sharpest because it is the case where the same physical corpus both
supplies the history H and carries a text of the survival condition that acted on it.

## The predictions

**P-A3.1.** Every fully open corpus whose composition is published by subset will name
at least one of arXiv, GitHub, StackExchange or an academic-paper subset, and so will
state (T1) at the level of *source*, not of *document*.
*Would count against it:* an open corpus with a published subset table that names no
academic, code or Q&A source — web crawl only. **I expect C4 and FineWeb to be exactly
that, and I say so now, so that finding it is not a hit.**

**P-A3.2.** No corpus documentation will name an individual document. Composition is
published as subsets, token counts and percentages. So (T1) will be *claimed at the
source level and unstated at the document level* everywhere.
*Would count against it:* any corpus paper or datasheet that names a specific paper,
repository or file it contains.

**P-A3.3.** (T3) will not be settled by a corpus paper's own words. No corpus paper
will say "this corpus contains the paper describing the model trained on it."
*Would count against it:* such a sentence, which would settle A6's physical reading in
one quotation.

**P-A3.4.** (T3) *will* be reachable by dates: a corpus with an arXiv or academic
subset whose stated cut-off is later than the publication date of a paper stating the
loss of a model trained on that corpus. This is *worked out*, not *seen*, and it is
weaker than P-A3.3 because a stated cut-off does not entail that a particular document
passed the filters.
*Would count against it:* every open corpus's academic cut-off preceding every
relevant paper; or documentation saying the academic subset is filtered in a way that
would drop such papers.

**P-A3.5.** DeepSeek's own reports will state corpus *composition in kind* (code, math,
multilingual, token counts) and not by named source or named document, and will state
their own loss and optimizer in the report. So DeepSeek supplies the *text* of a
survival condition publicly while not stating that its corpus contains such texts.
*Would count against it:* a DeepSeek report naming arXiv or GitHub as a corpus source
(which would make (T1) *claimed* for DeepSeek too), or one publishing a document list.

**P-A3.6.** Anthropic will publish a principle list used as a training criterion (the
constitution) and will not publish corpus composition. So for Claude (T2)'s *text*
exists publicly and (T2)'s *membership in the corpus* is unstated.
*Would count against it:* Anthropic publishing a corpus composition table; or
Anthropic publishing nothing that functions as a principle list.

**P-A3.7.** At least one open corpus record will state (T1) explicitly enough to tick
W10.3 with a quoted sentence. I predict the Pile, because its composition table is the
most itemised of those I expect to find.
*Would count against it:* zero. W10.3's own falsifier: "zero falsifies the physical
reading's reach from here and the clause stays unknown."

## What would count against the whole collection

- If the only sentences I can quote are about *sources* and W8 A6's check is about
  *occurrences*, then the evidence bears on the physical reading only by a step I must
  make myself (source named → documents of that source present → a particular document
  present). I must mark that step *worked out*, and say at which link it is weakest.
- If I find myself quoting a corpus paper's *aspiration* (what it intended to include)
  rather than its *composition* (what it reports including), the quotation does not
  bear and I drop it.
- A corpus that is "open" in weights but not in data does not count; the plan says
  "fully open training corpus with published composition."
- If the reading question (i) vs (ii) is settled by file 11 itself, then the evidence
  collection was the wrong instrument and I say so instead of reporting a count.

## The one thing I expect not to settle

Whether representation in (R)'s sense holds of any such document. (R) requires a
faithful transport with selected or constructed provenance from the organization the
occurrence instantiates to the content. No corpus record speaks to that. So the most
this collection can do is settle the *presence* premise of A6's check and leave the
*representation* premise where it is. I say this before looking so that a pile of
presence-quotations is not read as more than it is.
