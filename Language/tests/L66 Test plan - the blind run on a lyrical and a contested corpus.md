# L66 Test plan - the blind run on a lyrical and a contested corpus

Written before any translation or run. Not edited afterwards.
Authority: file 10. Language: 38 with 39. Scope: L64 (accepted, decision L7). Rigs as they stand. Steps three and four of the five approved at L63, folded into one run on new data (decision L8).

## The corpus, sealed
Eighteen passages, 151 sentences, at "results/L66 Corpus - lyrical argument and group selection": twelve of lyrical prose that argues (Lucretius four, Thoreau four, Pope two, Emerson two; public domain, verbatim, verse set as prose), two public-domain group-selection passages (Darwin's tribe, Kropotkin's sociability), two modern group-selection passages in the corpus maker's words (the case for, the case against), and two more, each of those with one sentence flipped between MAKES and SHOWS at the group level. Six of the twelve lyrical passages carry one sentence altered by a program (seed 45), each alteration a negation or a reversed connective. The passages are shuffled as P01 to P18. The key (which passage is which; the six alterations; the two flips) is `KEY.json`, SHA-256 `d3d02b645573de42098bfa39e05d2f61034b4f5b9641d0c5cc3041d12fd1d7eb`, held encrypted as `KEY.enc`; the orchestrator holds the passphrase and opens the key after the worker's return and after the reader's answers are in. `SOURCES.md` says where the words come from. `MANIFEST.json` hashes every passage file.

## Who is blind to what
- **The worker** (a new agent, not Claude, not the other model): translates all eighteen under 38 and 39, writes the ledgers, runs both rigs and the consequences program, and returns everything. It sees the texts and nothing about plants, flips or sources beyond SOURCES.md.
- **The reader** (a fresh agent, and the owner if willing): sees only the printed reports, never a ledger or a text, and must say for each finding what it is and which sentence it points at.
- **The orchestrator** (Claude): made the corpus and the plants and knows them; opens the key last; marks.
- What is not blind: the corpus maker also wrote the two modern passages and this plan. The predictions below were written knowing the plants.

## The questions, frozen
1. **Plants.** Does the checker, on the worker's translation, report a fault on the planted sentence of a planted passage, and stay silent on the unplanted ones?
2. **Consistency.** On the twelve unaltered passages (six lyrical, four group-selection sources, two modern), does the checker report no contradiction, as their reputation says it should?
3. **The dispute.** On the modern for and against passages, does the sameness test show the same facts with a different point (the group-level general line MAKES on one side, SHOWS on the other), and does the consequences program diverge between them under the change "withdraw the group-structure line"? On the flipped pair, does the checker or the sameness test see the flip?
4. **Scope.** Where does the bin gauge of L64 read on lyrical prose and on contested science?
5. **Read-back.** Given the reports alone, can a reader name each finding and the sentence it points at?

## What I expect
| | Expectation | Would count against |
| --- | --- | --- |
| E1 plants | The program's alterations are crude; two are ungrammatical. A negation inserted into an argument that does not state the opposite claim yields no contradiction; it yields a reason that does not connect, or nothing. Expected: a fault reported on the planted sentence in **2 of 6** planted passages (a NO CONNECTION or JUMP in a SINCE chain); the other four pass silent, and at least one is binned by the translator as a slip of the text, which 39 rule 16 asks it to record | 5 or 6 found: the plants were too easy; 0: the checker cannot see a broken step in lyrical argument at all |
| E2 false alarms | **1 of 6** unplanted lyrical passages gets a contradiction, and it is Emerson's consistency passage, whose "though it contradict everything you said to-day" and "no man can violate his nature" invite one; Pope and the rest pass silent | 3 or more: the language misreads lyrical argument as contradiction |
| E3 consistency of sources | Darwin, Kropotkin and both modern passages: no contradiction. Kropotkin's "under any circumstances sociability is the greatest advantage" against his own "the fittest under certain circumstances" is a USUALLY against an ALWAYS that a careful translator keeps apart | A contradiction in Darwin or Kropotkin |
| E4 the dispute | The sameness test on for against against: **3 to 5** facts both say (within a group the helper does worse; helping spreads when helpers are clustered; social insects and the cell are cases), and the general line about the group differs in kind, MAKES against SHOWS. No contradiction inside either. Consequences: withdrawing the group-structure line removes "helping spreads" from the for ledger and changes nothing in the against ledger | Fewer than 2 shared facts (the translator wrote them in unrelated words), or a contradiction inside one side |
| E5 the flips | The checker finds **neither** flip: 38 has no rule that MAKES and SHOWS on the same content clash. The sameness test between each original and its flip shows one line differing in kind and nothing else | The checker reports the flip as a fault: then 38 has a rule I did not know it had |
| E6 scope | The bin gauge (sentences losing something to the bin) reads: Lucretius and Thoreau under a third; Pope and Emerson over a third; both modern group-selection passages over a third, on likelihood, more, most and numbers; Darwin and Kropotkin near a third. The count of unshaped verbs is highest on Lucretius (Leonard's verbs: seep, stream, plenish) | Lucretius over a third: the laws of pressing do not reach even the poem of pressing |
| E7 read-back | The reader names the finding and the sentence for **at least 4 of 5** contradictions, **at least half** of the jumps and no-connections, and **fewer than half** of the derived consequences, because "never said; follows from lines N, M" points at lines, and lines at sentences, one step too many | Contradictions traced under half: the report wording fails its one job |
| E8 size | 18 ledgers of 6 to 15 lines; the worker's whole run, rigs and consequences, under an hour; consequences never over 40 derived facts on one ledger | A consequences run over 100 on any ledger: the pull of L64 section 7 is real at this size |

## What would count as failure
- Of the language: E2 or E3 against it, or E6 with Lucretius over a third.
- Of the plants as a method: E1 at 0 or at 6.
- Of the read-back: E7's contradictions under half.
- Of the design: any passage the worker cannot translate at all under 38 and 39.

## Order of work
1. The worker translates, runs, returns (brief L66).
2. The reader answers from the reports alone (brief L66-reader).
3. The orchestrator checks the return as before (manifest, identity, reruns), then opens the key, marks E1 to E8, and writes the results file.
4. Then the source check of the two modern passages against the works named in SOURCES.md, before any conclusion about the dispute is kept.

## Not tested
A second translator on the same texts (the sameness test across translators waits for one). WITHDRAW and MAKE NOT SO beyond the one change named in E4. Texts longer than fifteen sentences. Any reader's reading of a passage itself.

## Traps
- Opening the key before the reader has answered.
- Marking the plants by whether the translator noticed them. The question is whether the checker reports a fault on the sentence.
- Reading Pope's high bin count as failure. Modality is out of scope by L64, openly.
- Taking the two modern passages as the dispute. They are the corpus maker's words until the source check.
