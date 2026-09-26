### W38.1 — The note of sources and departures

- **STATUS:** applied
- **GROUP:** M
- **ITEM:** W38
- **FILE-11 LINE:** 7–9
- **WHERE:** front matter, after the note. It is inserted before the rule `---` at L7 that opens Part 0. The anchor is L7–L9 (the rule, the blank line and the Part 0 heading), kept byte for byte. L7–L9 belong to no group.
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, FIX. Five statements were inaccurate: what file 00 cites, Marletto's page for interoperability, Deutsch's definition of a problem, the Derivation 6 clause, and the stated-limits line against B1's wording. Three lines follow C's fixes (physical media, a separate matter, does no work by itself). The fallback table's substrate row now cites chapter 3, pp.88 and 95. The assembler also gave the fallback for "Surprise and problems" the corrected account of Deutsch's "problem", which check 2's fix (c) implies but did not write out.
- **OLD:**
````text
---

# Part 0 — Read this first
````
- **NEW:**
````text
<!-- META:SOURCES BEGIN -->
*Sources and departures.*

**Sources.** The semantics has two sources, named as such by its owner: Chiara Marletto, *The Science of Can and Can't* (2021), and David Deutsch, *The Beginning of Infinity* (2011). Its predecessor is the FW5 construction of 8 September 2026 (file 00), whose reference list cites articles by the two authors, not these books. The task wording of the physical module (Part XII) is constructor theory's, from Deutsch's paper "Constructor Theory", *Synthese* 190 (2013), which file 00 cites. The definitions, conditions and derivations are this document's own. None is attributed to either book, and this note says nothing about what follows from them.

**Close parallels, named and not claimed as derived.** Derivation 9's last sentence, declared provenance, "relay is not" construction (Part X) and reason use (Part IX) have close parallels in Deutsch, chapter 7, pp.155–161, and chapter 16, p.406. Inexplicit representation (Part X) has one in Deutsch, chapter 16, pp.405 and 412. Part I's substrate independence, held so far as the adopted physics lets contents pass between physical media, matches the interoperability principle as Marletto states it (chapter 3, pp.87–88; its consequence for universal computers, p.95).

**Departures.** The semantics departs from the books on purpose at these places.
- *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V). Part I's fallibility commitment uses "explanation" for an account on a contract, and how hard an account is to vary is a separate matter (Part VI).
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and how hard an account is to vary grades nothing (Part VI).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the reach of an account is the set of jobs on which it is an account, fixed by the account and the world (Part VI).
- *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded and not certified: meeting the conditions of an account on a restricted contract certifies nothing about the restriction, and a verdict on a restriction whose ground the claim states is given with that ground (Part III).
- *Selection.* Deutsch calls criticism and experiment a selection (chapter 4, p.78). Here selection is blind: its history holds no represented target (Parts 0 and IV).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
- *Elimination.* Deutsch asks an eliminative explanation to explain why what it denies seems to exist (chapter 7, p.154). Here why the absent structure appears is a separate question with its own contract, which an account of the absence neither answers nor needs to (Part VII).
- *Acquisition.* Deutsch holds that grasping any idea takes conjecture (chapter 4, p.94; chapter 16, pp.403–406). Here not every acquisition is construction: reconstruction by a learner is, and relay is not (Part X).
- *Knowledge as self-preserving information.* Marletto defines knowledge as information that can keep itself instantiated in physical systems (chapter 5, p.155). The semantics leaves this out: its class is explanatory creativity, and knowledge in that sense would be an attribution of the physical module, outside the class.
- *Universality and aesthetics.* Deutsch holds that people are universal explainers (chapter 6, p.146) and that there are objective truths in aesthetics (chapter 14, p.368). The semantics abstains on both. It defines the universal class and shows no one to belong to it (Parts 0 and XIII), and it takes worth as an input and derives no aesthetics (Part XI).

Page numbers are the printed pages of the editions named. A third book, named by the owner as further reading, is not a source and is not cited.
<!-- META:SOURCES END -->

---

# Part 0 — Read this first
````
- **DECLARATION:** made by the note ("the note of sources and departures after it … not part of the theory and add nothing to it"). Not counted in N or M.
- **REASON:**
  - Worklist W38 (verify obs 1, 3 and 10; decision S19); plan 1.3.6.
  - The content is plan 1.3.6's: the sources; the constructor-theory lineage of Part XII (00:910 and 00:1416, [R2]); the FW5 predecessor; the close parallels (Deutsch, chapters 7 and 16); and the eight departures it lists.
  - Added, because other groups' entries send them here:
    - reach (C's C12 on W34.1);
    - elimination (C's C12 on W40.1);
    - the mapping of "problem" to the recognized difficulty (C's W35.3 reason);
    - interoperability, a term kept out of the theory (C's W45.1 reason);
    - blind selection (A's W37.1 reason).
  - Also added: inexplicit representation as a parallel (D pp.405, 412), since C's W41.1 restores it from file 00.
  - No book is quoted, so plan 1.3.6's 25-word limit is met trivially.
  - **Page numbers.** Each was checked against the extracted text of the named editions, by locating a phrase from the page with `sources/locate.py`: Deutsch pp.17, 19, 25, 27–28, 28, 78, 94, 146, 154, 155, 156, 160–161, 368, 405, 406 and 412, and Marletto pp.24, 95 and 155, each in the chapter named. Deutsch pp.403–406 was read (the passage on how memes are acquired, which runs across those pages). Plan 1.3.6 asks the writer to recheck at freeze.
  - **Named and not named.** The decision number (S19) is not named, because no meta block names a record file. The third book is mentioned and not named or cited, since plan 1.3.6 says it is not cited.
  - Each line that rests on another group's entry has a fallback, given below, for use if that entry is dropped under plan 1.5's cap.
- **CASES AT RISK:** none. The block is cut from every brief (D6), and "Deutsch" and "Marletto" are on the build's withheld list (plan 2.5). If it reached a tester, the departures would steer readings toward the books' judgements at exactly the guard rows: idle parts (N1, N25), stated limits (O1, O5, O8, N7), selection (O11, N11), surprise (O3, N18, N19) and elimination (N22).
- **GAIN:** Lineage, and honesty about where the semantics departs from its two sources.
- **LOSS:** Readers may hold the theory to the books (worklist W38). The authority file grows by about 720 words.
- **FALLBACKS:** if an entry a line of the sources note rests on is dropped under plan 1.5's cap, the line is replaced by the fallback, or dropped where none is given.

  | line | rests on | fallback |
  |---|---|---|
  | Inexplicit representation (parallels) | C W41.1 | drop the sentence |
  | Part I's substrate independence (parallels) | C W45.1 | Part I's substrate independence is stated without condition; Marletto treats the interoperability of carriers as a law of physics that may fail (chapter 3, pp.88 and 95). |
  | Explanation | C W36.1 | - *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V), and Part I's fallibility commitment uses "explanation" for what is not in error in the dependence alleged to do the work. |
  | Idle parts | C W33.1 (the words 'grades nothing'); the claim itself holds on file 11 | - *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here a commitment that does no work does not stop a candidate from being an account; Part VI reports it. |
  | Reach | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |
  | Stated limits | B1 W57.1 + W32(b).1 | - *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded, and what makes it appropriate is a criticizable part of the claim that the semantics does not certify (Part III). |
  | Selection | A W37.1 for 'Parts 0 and'; the claim holds on file 11's Part IV | (replace "(Parts 0 and IV)" with "(Part IV)") |
  | Surprise and problems | C W35.1-W35.3 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV), and the recognized difficulty of a critical episode (Part X) is not defined. |
  | Elimination | C W40.1 | drop the sentence |

