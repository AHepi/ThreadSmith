# S81 determination: Claude's readings written before the returns were opened

23 September 2026

**What these files are.** These are Claude's own rulings for round S81, written from the texts alone:

- **01** gives Claude's ruling on each of the 52 cases (O1 to O52). For every case it gives the mark under file 10 and the mark under file 11, and says whether the verdict and the passage stay the same or change.
- **02** is Claude's reading of how file 11 differs from file 10.
- **raw readings/** holds the six readings the two files above were reconciled from, unedited.

**How they were written.** Two independent Claude readers each read the texts and wrote their own reading. A third Claude, the reconciler, then compared the two readings. Where they differed, it ruled from the texts and kept both readings on the record. The readers and the reconciler used only these sources: file 10, file 11, the S81 case book and the instruction sections of the Stage 1 briefs. None of them opened any Stage 1 or Stage 2 return, the samples or the S81 table. This follows lesson S2: "a second reader writes its reading before it opens the first reader's." Here Claude is the second reader and the returns are the first reader's. Each file states what its writer opened and what it saw by name only.

**Why this is committed now.** This commit comes before the S81 table is built. The git history therefore proves that these rulings were written before the returns were read.

**What they are for.** These readings are Claude's evidence for the determination. They do not replace it. The determination still reads the returns as the plan requires. If Claude changes a ruling after reading the returns, the determination records the change and the reason for it.

**Names used inside the files.** The files were written in a working folder and refer to one another by their working names:

| Working name | File here |
|---|---|
| `reader1_O1-O26.md` | `raw readings/01a reader 1, cases O1-O26.md` |
| `reader1_O27-O52.md` | `raw readings/01b reader 1, cases O27-O52.md` |
| `reader2_O1-O26.md` | `raw readings/01c reader 2, cases O1-O26.md` |
| `reader2_O27-O52.md` | `raw readings/01d reader 2, cases O27-O52.md` |
| `diffreader1.md` | `raw readings/02a difference reader 1.md` |
| `diffreader2.md` | `raw readings/02b difference reader 2.md` |

A mechanical word diff that one difference reader used (`wdiff.txt`) was a working aid and is not copied here. Any reader can regenerate it from files 10 and 11.
