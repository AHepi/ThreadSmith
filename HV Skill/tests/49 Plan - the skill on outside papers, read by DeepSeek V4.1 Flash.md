# 49 Plan - the skill on outside papers, read by DeepSeek V4.1 Flash

Written 20 September 2026, before any run. Waiting on the owner's verification (decision 39). Nothing in it has been sent to DeepSeek.
Skill under test: file 30. The semantics document (file 10) is the theory behind the skill and is not test content and is not shown to the reader.

## What this plan covers, and what it leaves for later
The owner asked for two things now: **where the sources come from**, and **how the skill is introduced to the reader**. How replies are marked is left for a later plan, written before marking and after the owner has seen a pilot reply. That order is deliberate: the marking scheme should be fitted to what the reader's reports look like, and it must be frozen before the corpus run is read.

## The question
Where does the skill break? Earlier tests used short passages written by Claude. A paper carries everything the skill's procedure needs and a passage does not: a question the author froze, a change list the author chose, the author's own pokes, patches made over a history, rivals the author names, and parts whose origin (fitted, built, asserted) can be traced. So the corpus is made of papers, or paper-like documents, from outside this project, chosen so that every part of the skill meets at least two sources built to exercise it. The reader is DeepSeek V4.1 Flash, which has never seen the skill.

## Part 1 - Where the sources come from

### The rule for choosing a source
1. It explains something: a question it answers, named parts that do the work, and the author's own evidence or tests. An abstract alone does not qualify; a self-contained section of a long work does.
2. It is open to fetch: public domain, open access, or posted by its author. Where a canonical text is only on a mirror (Turing 1936, Bell 1964), the entry says so and the owner decides.
3. Its standing is on record: contested (critics named in print), once contested and now settled (a control), or open. Standing is recorded but never shown to the reader.
4. It fits within about 25,000 word-pieces after trimming (references, acknowledgements and appendices cut; long works cut to the section that carries the explanation).
5. Where a theory and its critique are both open, both are taken, as a pair. Pairs feed the parts of the skill that need two documents: build the best rival, testing against cases, check the patches.

### The channels, as checked from this computer on 20 September
| Channel | What it gives | Checked |
|---|---|---|
| arXiv (export API + PDF) | physics, cosmology, computing, statistics | answers; PDF text extracts cleanly |
| Project Gutenberg (plain text) | public-domain fiction, philosophy, history | answers |
| PhilSci-Archive | philosophy of science preprints | answers (search at fetch time) |
| Stanford Encyclopedia of Philosophy | definitional entries (rules and definitions) | answers |
| Cornell LII | US court opinions, public domain | answers; Justia blocks |
| NASA history, SEC, WHO, RFC Editor | government and standards documents, public domain or open | answer |
| PMC via E-utilities | open-access case reports and medical reviews | answers; 92,966 hits on the probe search |
| PLOS, OSF, archive.org | open-access journals, preprints, scanned public-domain books | answer |
| Author-posted PDFs (Bostrom, Chalmers, PERI, Liebowitz, Wolfram, Poe archive) | canonical papers posted by their authors or curators | answer |
| Nobel Foundation | Nobel lectures | answers |
| Blocked from here | AEA PDFs, AMS Notices, CERN document server (bot check) | use the HTML page, an author mirror, or drop |

Fetching is one program: a manifest (`sources.json`: id, title, author, year, where from, licence, fetch method, section to keep, standing, the parts of the skill it is chosen to exercise, and why) and `fetch.py`, which pulls each source, extracts text (PyMuPDF for PDFs, plain text or stripped HTML otherwise), trims to the named section, counts word-pieces, and writes `corpus/<id>.txt` with a provenance header. Nothing is sent to DeepSeek at this stage. Each fetched text is read once by Claude for one purpose only: to confirm it contains an explanation with parts (rule 1). Nothing is written about its weak points at this stage.

### The coverage map
The skill's parts, as the skill itself lists them, and the sources chosen to meet each. Every source appears in at least one row; every row has at least two sources. Ids are given in the candidate list below.

| Part of the skill | Sources chosen to exercise it |
|---|---|
| Step 1, freeze the question: *what produces it* | S11 ulcers, S16 Wegener, S5 Bullet Cluster |
| *what can we tell from what we see* | F2 Speckled Band, F6 Blue Cross, S17 case reports, S10 Clever Hans |
| *why can it not happen* | C1 Turing, C6 Bell, C2 Aaronson, P4 Chalmers |
| *why is there none of it* | S9 Fermi dissolved, S4 dark matter history (why no visible mass) |
| *what counts as what under this rule* | R1 Nix v Hedden, R2 Toy Biz, C3 Church-Turing entry |
| *does it achieve its purpose* | D1 RFC 1958, D2 slow start, I1 WHO checklist, P6 Modest Proposal |
| Remove, swap, two routes | F1 Poe, F4 Time Machine, D1, D2, I1, I2 |
| Flip the outcome | C4 Wolfram, F3 Tolstoy, E4 colonial origins, S7 lightsail |
| Poke, and measure against producer | S13 integrated information, S14 ego depletion, S15 learning styles |
| Reverse | E2 debt threshold, S12 Feynman, P2 Hume |
| Hunt the answer in the starting points | P1 Anselm, E1 efficient markets, F5 Lucretius, P7 Meno |
| Add a job | S5 Bullet Cluster, S11, S16 |
| Build the best rival, and test your test | S1/S2 inflation pair, S3/S4 gravity pair, S7/S8 'Oumuamua pair, E3 QWERTY pair |
| Pull | D1 RFC 1958, I1, P6 |
| Check the patches: catch-all and gauge, narrowed range, a fix | S1/S2, S3, S12, S18 Knight Capital, S14 |
| Look inside | S10 Clever Hans, C7 four colours, S12 |
| Where parts came from: fitted, built, asserted | E2, E4, C4, S3 |
| The eight marks, especially borrowed and free | E3 QWERTY (a convention), R1, D1 |
| Domain: diagnoses (jobs that did not show) | S12, S17, S18 |
| Domain: designs and plans | D1, D2, P6 |
| Domain: arguments | P1, P2, P3, P4, C2 |
| Domain: history and comparisons | E4, F3, E3, S16 |
| Domain: stories and creative choices | F1, F2, F4, F6 |
| Domain: proofs | C1, C6, C7 |
| Domain: rules and definitions | R1, R2, C3 |
| Domain: written instructions | I1, I2 |
| Module: building (owner as critic) | S6 Where's the flux, S8 (given the phenomenon, asked to build) |
| Module: testing against cases | S14 pair, S15 pair, E2 pair |
| Module: question bank, dodges and follow-ups | only in conversation mode (Part 2, mode 3) |
| The quick version (a small claim) | short pieces: R1, P1, D2 |
| Controls (should be left standing) | S11, S16, S5, C6, R1, D2 |

### The candidate list
Fetched and confirmed to exist unless marked *find*. Standing: C contested, S settled after contest, O open.

**Science.** S1 Ijjas, Steinhardt, Loeb 2013, *Inflationary paradigm in trouble after Planck2013*, arXiv:1304.2785 (C). S2 Guth, Kaiser, Nomura 2013, *Inflationary paradigm after Planck 2013*, arXiv:1312.7619 (C, the reply). S3 Famaey and McGaugh 2012, *Modified Newtonian dynamics*, arXiv:1112.3960, sections 1 to 4 (C). S4 Bertone and Hooper 2016, *A history of dark matter*, arXiv:1605.04909 (C). S5 Clowe et al. 2006, *A direct empirical proof of the existence of dark matter*, arXiv:astro-ph/0608407 (S). S6 Boyajian et al. 2015, *Where's the flux?*, arXiv:1509.03622 (O; the phenomenon with candidate explanations). S7 Bialy and Loeb 2018, *Could solar radiation pressure explain 'Oumuamua's peculiar acceleration?*, arXiv:1810.11490 (C). S8 'Oumuamua ISSI team 2019, *The natural history of 'Oumuamua*, arXiv:1907.01910 (C, the rival). S9 Sandberg, Drexler, Ord 2018, *Dissolving the Fermi paradox*, arXiv:1806.02404 (O). S10 Lapuschkin et al. 2019, *Unmasking Clever Hans predictors*, arXiv:1902.10178 (S). S11 Marshall 2005, Nobel lecture on Helicobacter (S). S12 Feynman 1986, *Personal observations on the reliability of the Shuttle*, Rogers Commission appendix F, public domain (S). S13 Oizumi, Albantakis, Tononi 2014, *Integrated information theory 3.0*, PLOS Computational Biology (C). S14 Hagger et al. 2016, ego depletion registered replication, with a proponent reply, both *find* on OSF or PsyArXiv (C). S15 Pashler et al. 2008, *Learning styles: concepts and evidence*, *find* open mirror, with the VARK proponent paper (C). S16 Wegener 1924, *The Origin of Continents and Oceans*, English translation, archive.org, chapters 1 and 2 (S). S17 two open-access case reports from PMC chosen at fetch time by the search "diagnostic reasoning" AND "case report", read for rule 1 only (O). S18 SEC 2013 order in the matter of Knight Capital, sec.gov (S).

**Economics and social science.** E1 Malkiel 2003, *The efficient market hypothesis and its critics*, Journal of Economic Perspectives, HTML page answers, PDF blocked (C). E2 Herndon, Ash, Pollin 2013, PERI working paper 322, with Reinhart and Rogoff 2010, *find* NBER (C). E3 Liebowitz and Margolis 1990, *The fable of the keys*, author-posted, with David 1985 *Clio and the economics of QWERTY*, *find* (C). E4 Acemoglu, Johnson, Robinson 2001, *The colonial origins of comparative development*, *find* NBER or MIT (C).

**Philosophy.** P1 Anselm, *Proslogion* chapters 2 to 4, Gutenberg or CCEL (C). P2 Hume, *Enquiry*, section VII, Gutenberg 9662 (C). P3 Bostrom 2003, *Are you living in a computer simulation?*, author-posted (C). P4 Chalmers 1995, *Facing up to the problem of consciousness*, author-posted (C). P5 Norton, *Waiting for Landauer*, PhilSci-Archive, *find* id (C). P6 Swift 1729, *A Modest Proposal*, Gutenberg 1080 (a plan; irony tests freezing the question). P7 Plato, *Meno*, Gutenberg 1643, the slave-boy passage (C).

**Computability.** C1 Turing 1936, *On computable numbers*, mirror at Virginia, 36 pages, text extracts cleanly; copyright uncertain, owner to decide (S). C2 Aaronson 2011, *Why philosophers should care about computational complexity*, arXiv:1108.1791, sections 1 to 5 (O). C3 Stanford Encyclopedia entry *The Church-Turing thesis* (a definition; C on hypercomputation). C4 Wolfram 2002, *A New Kind of Science*, chapter 12, the principle of computational equivalence, wolframscience.com (C). C5 Deutsch 1985, *Quantum theory, the Church-Turing principle and the universal quantum computer*, *find* author site (C). C6 Bell 1964, *On the Einstein Podolsky Rosen paradox*, CERN server blocks; *find* another open mirror (S). C7 Gonthier 2008, *Formal proof, the four-colour theorem*, AMS blocks; *find* Microsoft Research mirror (S).

**Fiction and creative choices.** F1 Poe 1846, *The Philosophy of Composition*, eapoe.org (C: an author explaining why every detail of a poem is there, long suspected to be a story told afterwards). F2 Conan Doyle, *The Adventure of the Speckled Band*, Gutenberg 1661 (a chain of identification). F3 Tolstoy, *War and Peace*, second epilogue, Gutenberg 2600, chapters 1 to 4 (a theory of history). F4 Wells, *The Time Machine*, chapter 1, Gutenberg 35 (a theory told in a story). F5 Lucretius, *On the Nature of Things*, book I, Gutenberg 785 (an ancient theory). F6 Chesterton, *The Blue Cross*, Gutenberg 204 (two routes to one job).

**Designs, rules, instructions.** D1 RFC 1958, *Architectural principles of the Internet* (design; free and inherited choices). D2 RFC 2001, *TCP slow start, congestion avoidance* (design with a reason for each rule). R1 *Nix v. Hedden*, 149 U.S. 304 (1893), Cornell LII (is a tomato a vegetable under the tariff; short). R2 *Toy Biz v. United States* (2003), *find* on LII or CourtListener (are the X-Men dolls). I1 WHO 2009, *Surgical Safety Checklist implementation manual*, who.int (instructions with reasons). I2 one protocols.io protocol that states a reason for each step, *find*.

Forty-six sources, of which about twelve need a mirror or an id found at fetch time. The owner strikes any and adds any.

## Part 2 - How the skill is introduced to DeepSeek V4.1 Flash

### What was checked
The service accepts the key and offers `deepseek-flash` (V4.1 Flash) and `deepseek-v4-pro`. Context is one million word-pieces, so skill and paper fit with room. Thinking is on by default; effort levels are low, high and max, and "high" is the middle one. The service supports tool calls in thinking mode, with the model's reasoning passed back between calls. Input that repeats across runs is served from a cache at a fiftieth of the price, so the skill goes first in every prompt, unchanged.

### Three modes, each a way of handing over the skill
**Mode 0, no skill (the fair rival).** System message: a bare instruction to judge whether the paper's explanation holds up, saying what does the work, what is loose, and what would test it, in under 1,200 words. Then the paper as the user message.

**Mode 1, the skill pasted whole.** System message: the framing (below), then all eight files of the skill, each under a line naming it. User message: the paper. The router has nothing to do because every module is already open.

**Mode 2, the router live.** System message: the framing, then `SKILL.md` alone. A tool is offered, `open_module(name)`, which returns the text of one reference file; the skill's own table and map say when to open which. The run records which modules the reader opened and in what order. This is the only mode that tests the router, and the only one in which the reader can fail to open a module the case needed.

**Mode 3, conversation (a later phase, on a subset).** The reader has the skill (as mode 2) and is told to question the author. A second DeepSeek session plays the author: it holds the paper and is instructed to defend it as its author would, honestly and without the skill. Six exchanges, then the reader writes its report. This is the only mode in which the skill's *How to ask* and the question bank's dodges and follow-ups meet anything. The owner's earlier finding that a model reinterprets negative instructions is watched for here: the skill's wording is full of "never" and "do not", and this is where it would show.

### The framing text (modes 1 and 2), positive wording, given word for word
"Below is a method for judging whether an explanation holds up. It is the tool. The document that follows in the next message is the thing to judge. Work through the method's procedure on that document: freeze the question the document answers (where it answers several, take the one its title or opening makes central, and say so); list the jobs and the parts; write the change list; run the tests; say where each part came from; then write the report in the form the method gives, with one of the method's marks on every part. Use everyday words and concrete changes. Keep the report under 1,200 words. Where the method refers to a source theory that is not supplied, work from the method's own words."

That last sentence exists because the skill's word-list points to the semantics document, which the reader does not get. Any reply that asks for that document is recorded as a finding.

### Settings, the same for every run
Model `deepseek-flash`; thinking on at effort high; no temperature set (it has no effect in thinking mode); a ceiling of 24,000 word-pieces per reply, thinking included; one system message and one user message; every run a fresh conversation. Mode 2 allows up to twelve tool calls per run, with reasoning passed back as the service requires. Ten runs at a time, as the owner's limit; retries with backoff on a rate-limit reply; every run saved as it comes (prompt, reply, reasoning, tool calls, usage, time) so the run can stop and resume.

### Cost, worked out
About 46 sources x 3 single-shot modes = 138 runs, plus a pilot of 9. Skill prefix cached after the first run of each mode; paper 5,000 to 25,000 word-pieces uncached; reply and thinking 4,000 to 10,000. Under five dollars for everything in this plan, conversation mode included. Not yet seen.

### What could go wrong in the introduction, and what is watched
- The reader judges the skill instead of the paper. Caught by the framing's first two sentences; watched in the pilot.
- The reader ignores the modules and gives a generic critique. Mode 2's tool log shows whether modules were opened; mode 1's reports show whether the domain file's "parts, jobs, changes" appear.
- The reader treats the paper's own pokes as its own tests. Watched: a report that repeats the author's tests without adding one.
- The reader asks for the missing theory. Recorded.
- Long papers push the reply past the ceiling. The ceiling is generous and the reply length is capped by instruction.
- The "never" wording (the owner's finding on the other model). Watched in mode 3.

## The phases, each waiting on the owner
| Phase | What happens | DeepSeek calls | Waits on |
|---|---|---|---|
| 0 | Manifest written; every source fetched and trimmed; each read once for rule 1; the twelve *find* items found or struck | none | this plan being verified |
| 1 | Pilot: three sources (one paper, one story, one rule) x three modes | 9 | phase 0 shown to the owner |
| 2 | The corpus: every source x modes 0, 1, 2, ten at a time | about 138 | the pilot replies shown to the owner, and the marking plan written and frozen |
| 3 | Conversation mode on twelve sources | about 12 dialogues of 7 calls | phase 2 read |
| 4 | Marking, table, results file | none | the frozen marking plan |

## What this plan does not decide
- How replies are marked. A separate plan, written after the pilot and frozen before phase 2 is read.
- Whether V4-Pro is run beside Flash. Same rig, one setting; the owner's call on cost.
- The licence line for mirrored texts (Turing, Bell, Gonthier, Pashler, David). Sending a text to a service for private analysis is not publishing it, but the owner decides.

## The key
Used only in the shell's environment at run time. Written into no file in this set and no file in the rig. Deleted at DeepSeek's site by the owner when the runs are done.

## Traps
- Showing the reader any source's standing, any pair's other half (except where the mode calls for two documents), or any note from this plan.
- Reading the fetched texts for their weak points before the marking plan is frozen. Phase 0 reads them for rule 1 only.
- Letting the skill drift between modes. One copy, checked by hash, for modes 1, 2 and 3.
- Treating a mode 0 miss as the skill's success. The comparison is box by box, later.
- Starting any phase without the owner's word.
