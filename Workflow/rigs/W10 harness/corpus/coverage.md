# Coverage - what these seventeen documents give the skill's tests purchase on, and where they leave it nothing to reach

Written 22 September 2026, stage A2 of plan W10, before any arm ran. Nothing here has been sent to any model. No key was read and no request was made to any API by any program in this folder.

Seventeen documents. 58,290 words after trimming. Every one was fetched once by `fetch.py` from the address in `sources.json`, checked for three things and nothing else: that it is the document named, that it is between 1,500 and 6,000 words after the trim, and that it contains a passage that answers "why". No weak point was looked for and none is written down. The text is kept nowhere in this repository; only the address, the trim, the licence, the "why" passage, the exchangeable names and two hashes are kept.

**Whose cases these are.** Other people's. Every one was written for its own purpose by someone with no interest in this test: a physics paper, a court's two opinions, two Greek speakers, two Scottish ones, two fables, a standards body, a lecture, a style guide, an essay, a specification. None was written by anyone on this project and none was written with the skill in view. That is the only defence this corpus has against being a corpus chosen to flatter the thing it tests, and it is not a complete one: the choosing was still done here, and the section "What this corpus cannot do" says what that leaves open.

**None of them has been read by any run in the record.** Checked document by document against `HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/sources.json` (49 sources), against HV file 50 (the same 49, with their trims), and against HV file 43 (twenty-five passages written by Claude, no outside documents at all). No address and no document here appears in any of the three. Two names do appear in the record's *replies*: "Hilbert" in the DeepSeek returns on C1, C2, C3 and "Michelson" in one return on F5. A reply that mentions a name is not a run that read the document, and W1 and W4 are new documents; but a reader may carry something about either from its weights, which is true of every famous document and is recorded here rather than left out.

---

## 0. What the harness does with this

The harness (stage A1) gets the text by running the fetcher, never by reading a file from here, because no text is here:

    python3 fetch.py --out <a directory outside the repository> --no-header --strict

`--strict` refuses to write any document whose text no longer hashes to what was frozen on 22 September 2026, so a document that changed at its address stops the run instead of quietly entering it. `--no-header` writes the text without the provenance header, which no reader is to see. `--dry-run` sends nothing and prints the addresses. The names the re-identification arm exchanges are in each entry's `exchange.names`, and the arm's own edit program is A1's, not this folder's.

## 1. The split

Eight for the arms: W1, W4, W7, W8, W9, W12, W13, W17. Four in reserve: W3, W10, W16, W19. Five held out of the split: W2, W5, W11, W14, W15. `split.json` gives the rule that chose them and what it gives up.

## 2. Which of the eleven tests each document gives purchase to

Read across: these are the skill's own tests, in its own words. A mark means the document gives that test something to bite on, not that the test will pass or fail.

| id | domain | in | remove | swap | flip | poke | reverse | starting points | add a job | rival | pull | patches | look inside |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 Michelson–Morley | science | arms | | ● | | ● | | | ● | ● | | | ● |
| W2 Ioannidis | science | held out | | | | ● | ● | ● | ● | | | ● | |
| W3 Thompson | computability | reserve | ● | | | | ● | | | | | | ● |
| W4 Hilbert | computability | arms | ● | | | | | ● | ● | | | | |
| W5 Read | economics | held out | | | | | | ● | | ● | | | |
| W7 Euthyphro | philosophy | arms | ● | ● | | | | ● | | ● | | | |
| W8 Hume | philosophy | arms | | ● | ● | | | ● | ● | ● | | | |
| W9 Kipling, trunk | fiction | arms | ● | ● | ● | | | | | | | | |
| W10 Kipling, spots | fiction | reserve | ● | ● | ● | | | ● | | | | | |
| W11 RFC 8890 | design | held out | ● | | | | | | | | ● | ● | |
| W12 Gabriel | design | arms | | ● | ● | | | | | ● | ● | | |
| W13 Palsgraf | rules | arms | ● | | | | ● | | ● | ● | ● | | |
| W14 semver | rules | held out | ● | ● | | | | | | | | ● | |
| W15 PEP 257 | instructions | held out | ● | | | | | | | | ● | | |
| W16 kernel style | instructions | reserve | ● | ● | | | | | | | ● | ● | |
| W17 Hawthorne | fiction | arms | | | ● | ● | | | | ● | | | |
| W19 Hayek | economics | reserve | | | | ● | ● | ● | | | | ● | |

The `exercises` field of each entry in `sources.json` carries the same row of this table, in the skill's words, so the manifest and this file cannot drift apart without one of them being edited on purpose.

**How I know this.** For every document I read the passage quoted in `sources.json` and the lines around it, the opening and the closing 180 characters, and the sentences the fetcher's probe pulled out for carrying "because", "therefore", "the reason" and their kin. That much is *seen*. The marks in the table are *worked out* from those passages and from what kind of document it is; they are not a reading of the whole document, and a reader who reads the whole may find a test bites where this table says nothing, or nothing where it says it bites. Where a mark rests on a search result rather than the text, it is not in the table.

## 3. The eleven tests, the other way round

| Test | Documents | Of those, in the arms |
|---|---|---|
| Remove | W3, W4, W7, W9, W10, W11, W13, W14, W15, W16 | W4, W7, W9, W13 |
| Swap | W1, W7, W8, W9, W10, W12, W14, W16 | W1, W7, W8, W9, W12 |
| Flip the outcome | W8, W9, W10, W12, W17 | W8, W9, W12, W17 |
| Poke | W1, W2, W17, W19 | W1, W17 |
| Reverse | W2, W3, W13, W19 | W13 |
| Hunt the answer in the starting points | W2, W4, W5, W7, W8, W10, W19 | W4, W7, W8 |
| Add a job | W1, W2, W4, W8, W13 | W1, W4, W8, W13 |
| Build the best rival | W1, W5, W7, W8, W12, W13, W17 | W1, W7, W8, W12, W13, W17 |
| Pull | W11, W12, W13, W15, W16 | W12, W13 |
| Check the patches | W2, W11, W14, W16, W19 | none |
| Look inside | W1, W3 | W1 |

## 4. The six kinds of question

| Kind | Documents |
|---|---|
| What produces it | W2, W5, W9, W10, W12, W19 |
| What can we tell from what we see | W8, W17, W2 |
| Why can it not happen | W3, W4 |
| Why is there none of it | W1 |
| What counts as what under this rule | W7, W13, W14 |
| Does it achieve its purpose | W11, W14, W15, W16 |

## 5. The eight domains of HV file 50

science W1, W2 · computability W3, W4 · economics W5, W19 · philosophy W7, W8 · fiction W9, W10, W17 · design W11, W12 · rules W13, W14 · instructions W15, W16.

Every domain has at least two. The arms eight carry six of the eight: science, computability, philosophy (two), fiction (two), design, rules. Economics and instructions are in the reserve and not in the arms, for the reason `split.json` gives.

## 6. The re-identification arm

Nine documents have two named speakers or agents whose names can be exchanged, and in each the exchange changes what the document attributes to whom. All eight arms documents are among them.

| id | the two names | how often each occurs | what the exchange changes |
|---|---|---|---|
| W1 | Fresnel, Stokes | 4, 2 | each is credited with the other's account of aberration, and the result refutes the other one |
| W4 | Fermat, Bernoulli | 4, 3 | each is credited with the other's problem, and Kummer's ideal numbers are traced to the wrong one |
| W7 | SOCRATES, EUTHYPHRO | 103, 103 | the prosecutor becomes the questioner; every definition offered and every refutation change hands |
| W8 | CLEANTHES, PHILO | 22, 9 | the argument from design and the attack on it change speakers |
| W9 | Elephant's Child, Crocodile | 38, 26 | the Crocodile's nose is the one stretched, so the story explains crocodiles' trunks |
| W10 | the Leopard, the Ethiopian | 26, 24 | the Ethiopian gets the spots and the Leopard the changed skin |
| W12 | MIT, New Jersey | 13, 11 | every property of the two design philosophies changes hands, and the prediction about which spreads reverses |
| W13 | Cardozo, Andrews | 2, 2 | the holding and the dissent change authors, and the judgment follows from the wrong opinion |
| W17 | Dr. Heidegger, the widow Wycherly | 25, 7 | the widow runs the experiment and the doctor is one of the four who grow young |

The counts are from `fetch.py --audit`, which fetches each document and counts the name in the trimmed text. They matter: an edit that touches four tokens is a smaller change to the world than one that touches two hundred, and three of the nine are thin. W13 is the thinnest, and it is thin for a reason worth keeping: the two names occur as the author lines of the two opinions and in the line recording who concurred, which is exactly where the document attributes each opinion. Exchanging them changes the attribution completely while changing almost no other word. W1 and W4 are thin without that excuse: there the exchange reaches one contrast each. If arm (x) moves nothing on W1, W4 and W13 but moves on the other five, the honest reading is that the edit was small, not that the reader has no counterpart to the primitive layer.

The edit the arm makes is a change to the world of the text (the second of the three things that can change), not a change to the explanation under test. The unexchanged document is the control, because the record already holds attribution errors with no exchange at all.

Two cautions on this list. First, an exchange that is only a change of label is not what W8 part A10 asks about: what it asks is whether the emission moves, and a reader that never names either party will move nothing whatever the edit. That would show the edit reached no port at this grain, which is exactly what PA.3 is written to be able to show. Second, W12's pair (MIT, New Jersey) are places, not persons. If that is judged not to be "two named agents", the arms fall to seven exchangeable and arm (x)'s denominator with them; the judgment should be made before stage C and written down, not after a count.

## 7. The gaps

- **No pairs.** HV file 50 had five: a claim and its published critique, which *build the best rival*, *check the patches* and *testing against cases* need and which one document cannot supply. This corpus has none. I looked for one, the published critique of W2, at two addresses (PubMed Central id 1855693 and the PLoS Medicine article page for 10.1371/journal.pmed.0040168) and found it 528 and 695 words, under the band. That is a fact about my search and not a showing that no pair exists in band. What stands in for it: W13 carries a rule and its best rival in one document, W8 carries an argument and its attacker, W12 carries two design schools. A rival the document itself builds is a weaker test than two documents written apart, because the author chose how strong to make it.
- **Check the patches has nothing in the arms.** Five documents give it purchase and all five are in the reserve or held out. A history of being caught out and rescued is what that test needs, and none of the eight arms documents carries one. The arms cannot bear on that test this round, and any report that claims to have run it on them should be read with that in mind.
- **Look inside has one document, W3, and it is in the reserve.** W1 gives it a little (the apparatus is described so that its workings can be poked). This is not only a gap in the corpus: HV file 54 already records that *look inside* has almost no purchase on a single document, and file 33 answers with a reporting rule rather than a way to reach inside. A reader that leaves parts *unknown* and names *look inside* as the test that cannot bite is doing what the skill asks, not failing.
- **Reverse is thin**, and the one document in the arms that carries it (W13) carries it as a question of law, not of cause.
- **No diagnosis of a failure.** File 50 had three (the shuttle appendix, a case report, an SEC order). Nothing here is a root-cause account of something that went wrong, so the *diagnoses* row of `by-domain.md` has nothing in this corpus.
- **Economics and instructions are absent from the arms.**
- **One document is truncated**: W7, capped at 6,000 words, stops before the dialogue's close. Its header says so and the reader is handed the header-stripped text.
- **Nothing here is in a language other than English, and nothing is a spoken or conversational explanation** — the same two gaps file 50 recorded, unclosed.
- **Two documents are served under someone's copyright rather than an open licence** (W3, a Turing lecture carrying ACM's copyright served from a university course page; W12, on the author's own site). They are openly fetchable pages, which is what the task permits, but they are not open licences and `sources.json` says so for each. W3 is in the reserve and W12 is in the arms; if the owner reads "openly fetchable" more strictly than I have, W12 must be replaced and the split with it.

## 8. What this corpus cannot do

- It cannot show the model is right. It can show where the arms' differences fail to appear, and where the skill's words fail to reach a document.
- It was chosen here, by the project that will read the results. Every document is someone else's and the standings and licences come from the documents and their publishers, not from this project; but which seventeen were fetched, and which passage was called the "why" passage, was decided here, and a corpus chosen to suit an arm would flatter it. The guard against that is that the eight arms documents were chosen by one stated rule (they admit the name exchange), fixed before any run, and that the passages quoted are the documents' own words at addresses anyone can refetch and hash.
- A hash is not a guarantee that a later fetch gives the same text; it is a way of finding out that it did not. Two hashes are kept for each document: one of the bytes as downloaded and one of the trimmed text a reader would be handed. A change in the first with no change in the second is a cosmetic change at the server; a change in the second is a different document and a new claim.
- The word band (1,500 to 6,000) was set by the task, not by anything about explanation. It keeps out long papers, and with them most claim-and-critique pairs and most technical arguments carried over many pages. The corpus is therefore made of short documents, and what a reader does with a long one is not tested here.

## 9. How these were found

Web search on 22 September 2026, then one fetch per candidate by `fetch.py`. Every search and every address, including the ones that failed, is listed in the return of this stage and in `sources.json`'s addresses. Candidates were kept only if the fetch returned the document named, in band, with a "why" passage; the ones dropped were dropped for a stated reason (out of band, truncated, the wrong page, or the server refused), not because of what they said.

## 10. Traps

- Sending a document with its provenance header. The header names the source, the trim and the licence; `fetch.py --no-header` writes the text without it, and no reader is to see it.
- Showing a reader this file, `split.json`, a document's standing, or the names the exchange will use.
- Reading these documents for their weak points before the marking plan of A4 is frozen.
- Writing the corpus text inside the repository. `fetch.py` refuses it; the refusal is the rule, not a convenience.
- Reading a document's place in the split as a judgement about the document.
