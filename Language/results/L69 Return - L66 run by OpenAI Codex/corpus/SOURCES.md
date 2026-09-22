# Sources and provenance of the corpus

Eighteen passages, P01 to P18, in a shuffled order. Every sentence is numbered. The mapping from P-number to source is sealed in KEY.enc (its SHA-256 is in MANIFEST.json) and is opened by the orchestrator only after the run returns. This file says where the words come from without saying which passage is which.

## Public-domain texts, verbatim
Fetched from Project Gutenberg on 21 September 2026. Verse is set as prose: line breaks removed, sentences kept whole, wording unchanged. Typographic marks normalised (curly quotes to straight, em-dashes to commas where the dash separated clauses). One passage of Emerson's *Self-Reliance* leaves out a five-sentence anecdote (the adviser and the Devil's child) from the middle of the paragraph; the sentences kept are in their original order.

- Lucretius, *On the Nature of Things*, translated by William Ellery Leonard (1916), Gutenberg #785: Book I (nothing from nothing; the void; nothing returns to nothing) and Book II (the swerve). Four passages.
- Henry David Thoreau, *On the Duty of Civil Disobedience* (1849), Gutenberg #71. Four passages.
- Alexander Pope, *An Essay on Man* (1734), Epistle I, Gutenberg #2428. Two passages.
- Ralph Waldo Emerson, *Self-Reliance* (1841), in *Essays*, Gutenberg #16643. Two passages.
- Charles Darwin, *The Descent of Man* (1871), chapter V, Gutenberg #2300. One passage.
- Peter Kropotkin, *Mutual Aid: A Factor of Evolution* (1902), chapter I, Gutenberg #4341. One passage.

## Passages in the corpus maker's words
Two passages state the modern case for and the modern case against group selection, each in a supporter's voice, written by the orchestrator (Claude) on 21 September 2026 from memory of the sources below, **not looked up in this session**. A source check against these works is a named step before the marks are read. They are arguments, not quotations, and no sentence is attributed to any author.

The case for (multilevel selection): D. S. Wilson and E. Sober, "Reintroducing group selection to the human behavioral sciences", *Behavioral and Brain Sciences* 17 (1994); D. S. Wilson and E. O. Wilson, "Rethinking the theoretical foundation of sociobiology", *Quarterly Review of Biology* 82 (2007); M. A. Nowak, C. E. Tarnita and E. O. Wilson, "The evolution of eusociality", *Nature* 466 (2010); Darwin's tribe passage above.

The case against (gene and kin selection): G. C. Williams, *Adaptation and Natural Selection* (1966); W. D. Hamilton, "The genetical evolution of social behaviour", *Journal of Theoretical Biology* 7 (1964); R. Dawkins, *The Selfish Gene* (1976); S. A. West, A. S. Griffin and A. Gardner, "Social semantics", *Journal of Evolutionary Biology* 20 (2007); P. Abbot and 136 others, "Inclusive fitness theory and eusociality", *Nature* 471 (2011). The claim that group and kin accounting are the same arithmetic: the Price equation as used by Hamilton (1975) and by Marshall, "Group selection and kin selection: formally equivalent approaches", *Trends in Ecology and Evolution* 26 (2011).

Two further passages are these two with one sentence each changed by the corpus maker. Which, and how, is in the sealed key.

## What else is in the sealed key
Some of the public-domain passages carry one sentence altered by a program (seed recorded), which, and how, is in the key. Nothing else in any passage was altered.
