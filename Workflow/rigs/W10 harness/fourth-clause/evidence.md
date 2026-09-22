# The fourth clause of Selected, against the open trainers' records

A3 of stage A, plan W10. Written 22 September 2026 by an Opus 5 collector carrying
hard-to-vary file 33 with file 11's qualification of Derivation 3.

Predictions were written first, in `predictions.md`, and were not edited after the
first search. Section 8 marks each one tested or untested and says what happened.

**How to read the tags.** Every claim carries one: *seen* (I read it in this
repository, and the sentence is quoted), *claimed* (a source outside this repository
says so; quoted with its address and the date I read it, 22 September 2026), *worked
out* (follows from tagged things; the step is shown). No fetched text is kept as a
file. Two PDFs were cached outside this folder by the fetching tool itself, not by me;
both are named in the return.

---

## 1. The question, frozen

**What is being explained.** Whether the fourth clause of Part IV's definition of a
selected transport — "No member of the history represents \(t\), \(H\), or the survival
condition." (file 11, Part IV, *seen*) — holds for a language model whose training
corpus is drawn from the public internet, and what follows for W8 parts A5 and A6.

**Over what range.** The open training corpora whose composition is published, and the
published training records of DeepSeek and of Anthropic.

**What is asked.** Two things, kept apart:
1. *What can we tell from what we see?* — an identification question. What do the
   published records settle about the presence, in a training corpus, of texts stating
   a training loss, a preference rule, or a list of principles used as a criterion.
2. *What counts as what under this rule?* — a rule-status question. Which of the two
   readings of the clause the theory's own sentences support, and what each makes of
   the evidence.

**Not asked here.** Whether any such text *represents* the survival condition in (R)'s
sense. That is a fidelity fact with a history (file 11, Part IV: "The carrier–content
relation is thus a fidelity fact with a history.", *seen*), and no corpus record speaks
to it. I said so in `predictions.md` before looking, so that a pile of
presence-quotations is not read as more than it is.

---

## 2. The clause taken apart, before any evidence

The definition, quoted whole (file 11, Part IV — Layers, transports, and provenance,
*seen*):

> **Selected.** There is a population \(\mathcal T\) of candidate transports, a
> variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of
> edit–boundary pairs actually encountered, and a survival condition requiring fidelity
> on \(H\). The transport \(t\) is a member of \(\mathcal T\) that survived. No member
> of the history represents \(t\), \(H\), or the survival condition. Write
> \(\operatorname{Sel}(t;\mathcal T,\mu,H)\).

**The clause names three things and not four.** It forbids representation of \(t\), of
\(H\), and of the survival condition. It does **not** forbid representation of
\(\mu\), the variation operator, although \(\mu\) is named in the same definition two
sentences earlier. (*worked out*, from the quotation above.)

This is load-bearing and it cuts against the way my own task is worded. A text that
states an **optimizer** states \(\mu\). By the clause as written, such a text is not of
the kind the clause forbids. So the optimizer evidence below — which is the most
abundant evidence there is — bears on the clause **not at all**, and I report it
separately rather than counting it in.

What does bear:

| The clause forbids representing | A text that would do it |
|---|---|
| the survival condition | a statement of the loss or preference rule or principle list **used as the criterion for this training** |
| \(H\) | a statement of **which pairs were actually encountered** — a corpus composition document for the very corpus |
| \(t\) | a statement of the correspondence itself — the weights, or a description of them |

**And one more narrowing.** The survival condition is *this* condition: "a survival
condition requiring fidelity on \(H\)" — fidelity on *this* history, in *this*
population. A paper that states the form of cross-entropy states a kind of survival
condition, not this one. So a generic machine-learning paper is a weaker candidate
than it first looks, and W8 A6 is right to name "a text of the principles used as the
criterion" as the sharpest: a criterion list is particular to the training it was used
on. (*worked out*.)

This narrowing is not a patch made to save anything. It was forced by reading the
clause word by word before the searching, and it makes the collection *harder* to
satisfy, not easier.

---

## 3. What the open records say

Every quotation in this section is **CLAIMED**: a source outside this repository says
so. Address and date of reading are given with each. Nothing was kept as a file.

### 3.1 The Pile — the strongest record in the set

CLAIMED, https://ar5iv.labs.arxiv.org/html/2101.00027 (Gao et al., *The Pile: An 800GB
Dataset of Diverse Text for Language Modeling*, arXiv:2101.00027), read 22 September
2026:

> "The Pile is constructed from 22 diverse high-quality subsets---both existing and
> newly constructed---many of which derive from academic or professional sources."

> "ArXiv is a preprint server for research papers that has operated since 1991. As
> shown in fig. 10, arXiv papers are predominantly in the fields of Math, Computer
> Science, and Physics. We included arXiv in the hopes that it will be a source of high
> quality text and math knowledge, and benefit potential downstream applications to
> research in these areas."

> "We downloaded the TeX sources of all papers on arXiv up to the July 2020 dump (the
> last file included in our data is arXiv_src_2007_068.tar) via arXiv's S3 Bulk Source
> File Access"

> "we use GitHub 'stars' as a proxy for quality, and choose to gather only repositories
> with more than 100 stars."

> "GitHub is a large corpus of open-source code repositories. Motivated by the ability
> of GPT-3 (Brown et al. 2020) to generate plausible code completions despite its
> training data not containing any explicitly gathered code datasets, we included
> GitHub in the hopes that it would enable better downstream performance on code-related
> tasks."

Composition, same address, same date (Table 1, the five largest and the two that
matter): Pile-CC 227.12 GiB / 18.11%; PubMed Central 180.55 GiB / 14.40%; Books3
151.44 GiB / 12.07%; OpenWebText2 125.54 GiB / 10.01%; **ArXiv 112.42 GiB / 8.96%**;
**Github 95.16 GiB / 7.59%**; Stack Exchange 64.39 GiB / 5.13%.

**Why this record is different from every other.** Its arXiv sentence is *universally
quantified over the contents of a named source*: "all papers on arXiv up to the July
2020 dump". From that sentence plus a paper's arXiv date, membership of a named
document follows by deduction, not by sampling. No other record in this collection
makes a statement of that shape. (*worked out*.)

Three named documents whose membership follows, each stating something the clause's
subject-matter touches:

| Document | arXiv id, v1 date (CLAIMED, arXiv abstract pages, read 22 Sep 2026) | What it states |
|---|---|---|
| "Language Models are Few-Shot Learners" | 2005.14165, "Thu, 28 May 2020" | the autoregressive objective and training setup of GPT-3 |
| "Decoupled Weight Decay Regularization" | 1711.05101, "Tue, 14 Nov 2017" | AdamW — the *variation operator*, which the clause does **not** forbid |
| "Adam: A Method for Stochastic Optimization" | 1412.6980, "Mon, 22 Dec 2014" | Adam — again \(\mu\), not the clause's subject |

And the tie to a model trained on that same corpus, CLAIMED,
https://arxiv.org/html/2204.06745v1 (*GPT-NeoX-20B: An Open-Source Autoregressive
Language Model*), read 22 September 2026:

> "GPT-NeoX-20B was trained on the Pile (Gao et al., 2020), a massive curated dataset
> designed specifically for training large language models."

> "We use the AdamW (Loshchilov and Hutter, 2019) optimizer, with beta values of 0.9
> and 0.95 respectively, and an epsilon of 1.0e−8."

> "It consists of data from 22 data sources, coarsely broken down into 5 categories"
> including "Academic Writing: Pubmed Abstracts and PubMed Central, arXiv, FreeLaw,
> USPTO Backgrounds, PhilPapers, NIH Exporter"

So: the Pile contains the paper stating the optimizer of a model trained on the Pile.
That is the sharpest *documented* fact in the whole collection — and by section 2 it
bears on \(\mu\), which the clause leaves alone. I report it because it is the case
everyone reaches for, and because naming what it does not do is the point.

### 3.2 Dolma, and OLMo trained on it

CLAIMED, https://arxiv.org/abs/2402.00159 and https://arxiv.org/html/2402.00159v2
(*Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining
Research*), read 22 September 2026:

> "To facilitate scientific research on language model pretraining, we curate and
> release Dolma, a three-trillion-token English corpus, built from a diverse mixture of
> web content, scientific papers, code, public-domain books, social media, and
> encyclopedic materials."

> "The peS2o dataset is a collection of approximately 40 million open-access academic
> papers that have been cleaned, filtered, deduplicated, and formatted for pretraining
> language models. It is derived from the Semantic Scholar Open Research Corpus
> (S2ORC)."

> "the Stack, a deduplicated but otherwise unfiltered collection of
> permissively-licensed GitHub repositories. The raw version of this dataset was
> collected in March 2023."

Sources with token counts, same address and date: Common Crawl 2,479B; GitHub 411B;
Reddit 89B; Semantic Scholar 70B; Project Gutenberg 6.0B; Wikipedia/Wikibooks 4.3B.
Stated coverage: "25 snapshots between 2020-05 to 2023-06" (Common Crawl); Wikimedia
dumps "March 2023".

peS2o's own card, CLAIMED, https://huggingface.co/datasets/allenai/peS2o, read 22
September 2026: "Knowledge cutoff: 2023-01-03".

The model trained on it, CLAIMED, https://arxiv.org/html/2402.00838v1 (*OLMo:
Accelerating the Science of Language Models*), read 22 September 2026:

> "We built our training dataset out of a 2T-token sample from our open dataset, Dolma"

> "We use the AdamW optimizer with the hyperparameters shown in Table 4"

I looked for a sentence in that paper stating the loss function itself and did not find
one; the fetch reported "The document does not explicitly state the loss function
used." **"Found nowhere" means unknown**, not "absent" — it describes my search.

### 3.3 RedPajama

CLAIMED, https://arxiv.org/html/2411.12372v1 (*RedPajama: an Open Dataset for Training
Large Language Models*), read 22 September 2026. Slices with token counts: CommonCrawl
878B; C4 175B; **GitHub 59B**; Books 26B; **ArXiv 28B**; Wikipedia 24B; **StackExchange
20B**; total 1.2T.

> "We downloaded arXiv data from Amazon S3 in the 'arXiv' requester pays bucket and
> implemented a similar postprocessing, keeping only LaTeX source files and removing
> preambles, comments, bibliographies, and expanding macros."

> "Similarly, we download Stack Exchange from the Internet Archive, keep only the posts
> from the 28 largest sites, and remove HTML tags."

No date cut-off for the arXiv slice is stated in what I read. An outside audit puts the
share higher than the token table suggests — CLAIMED,
https://arxiv.org/html/2310.20707v2 (*What's In My Big Data?*), read 22 September 2026:
"In RedPajama, arxiv.org is responsible for more than 12% of the documents."

### 3.4 C4

CLAIMED, https://arxiv.org/html/2104.08758v2 (Dodge et al., *Documenting Large Webtext
Corpora: A Case Study on the Colossal Clean Crawled Corpus*), read 22 September 2026:

> "C4 is created by taking the April 2019 snapshot of Common Crawl"

> "the single-most represented website in the corpus is patents.google.com"

> "We begin by investigating where the data came from, and find a significant amount of
> text from unexpected sources like patents and US military websites."

C4 is a filtered web crawl. Its record names **no** academic, code or Q&A source. I
predicted this in `predictions.md` before looking, and it is therefore not a finding
against my expectations.

### 3.5 FineWeb

CLAIMED, https://arxiv.org/abs/2406.17557 (*The FineWeb Datasets: Decanting the Web for
the Finest Text Data at Scale*), read 22 September 2026:

> "we introduce FineWeb, a 15-trillion token dataset derived from 96 Common Crawl
> snapshots"

> "we introduce FineWeb-Edu, a 1.3-trillion token collection of educational text
> filtered from FineWeb"

Again web-only by its own record; no named academic or code source. Also predicted.

### 3.6 The Common Pile v0.1 — the one corpus built from openly licensed text

CLAIMED, https://arxiv.org/html/2506.05209v1 (*The Common Pile v0.1: An 8TB Dataset of
Public Domain and Openly Licensed Text*), read 22 September 2026:

> "ArXiv Papers ... contain over 2.4 million articles in the quantitative sciences, most
> of which are uploaded as LaTeX source"

> "we filter peS2o ... to only retain openly licensed research papers."

> "StackExchange is a collection of websites that host user-provided questions and
> answers and allow their redistribution under a CC BY-SA license."

> "All Python Enhancement Proposals (PEPs)—design documents that generally provide a
> technical specification and rationale for new features of the Python programming
> language—that were released into the public domain."

> "Since we collected and curated the Common Pile v0.1 in late 2024, the licensing
> information we include and rely on may not be completely aligned with more recent
> updates."

The models trained on it use "the AdamW optimizer" (same address, same date).

This record matters for a reason no other does: it is a corpus whose **admission rule
is the licence**. A criterion list released under a public-domain dedication is
admissible to it by rule. Section 5.3 uses this.

### 3.7 Dolma 3 and Olmo 3

CLAIMED, https://allenai.org/blog/olmo3, read 22 September 2026:

> "Dolma 3, a new ~9.3-trillion-token corpus drawn from web pages, science PDFs
> processed with olmOCR, codebases, math problems and solutions, and encyclopedic text."

> "all the components of the Olmo 3 flow openly available to the public—data, code,
> model weights, and checkpoints"

CLAIMED, https://arxiv.org/abs/2512.13961 (*Olmo 3*), read 22 September 2026:

> "This release includes the entire model flow, i.e., the full lifecycle of the family
> of models, including every stage, checkpoint, data point, and dependency used to build
> it."

A dated component reported by a secondary source and **not confirmed against Ai2's own
sentence**: a "Web crawl (Sep 2024–Jun 2025) of selected scientific/educational
domains" (CLAIMED, search summary over allenai.org and secondary write-ups, read 22
September 2026). I mark this **weaker than the rest** and do not lean on it; the
Dolma 3 dataset card returned HTTP 401 to me and I could not check it.

### 3.8 The Stack — the code source under Dolma and the Common Pile

CLAIMED, https://arxiv.org/abs/2211.15533 (*The Stack: 3 TB of permissively licensed
source code*), read 22 September 2026:

> "we introduce The Stack, a 3.1 TB dataset consisting of permissively licensed source
> code in 30 programming languages."

> "provide a tool called 'Am I in The Stack' for developers to search The Stack for
> copies of their code, and provide a process for code to be removed from the dataset"

---

## 4. What DeepSeek's own reports say

### 4.1 DeepSeek-V2

CLAIMED, https://arxiv.org/abs/2405.04434, read 22 September 2026:

> "We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T
> tokens"

No source is named. The page I read stated no optimizer and no loss.

### 4.2 DeepSeek-V3

CLAIMED, https://arxiv.org/abs/2412.19437 and https://arxiv.org/html/2412.19437v2, read
22 September 2026:

> "We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens"

> "The training corpus for DeepSeek-V3 consists of 14.8T high-quality and diverse tokens
> in our tokenizer."

> "optimize the pre-training corpus by enhancing the ratio of mathematical and
> programming samples, while expanding multilingual coverage beyond English and Chinese"

> "We employ the AdamW optimizer with hyper-parameters set to β₁=0.9, β₂=0.95, and
> weight_decay=0.1."

> "DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a
> multi-token prediction training objective for stronger performance."

The report states the survival condition (the objective, the balance loss, the MTP
loss) **in the open**, and states nothing about which texts the corpus contains.

### 4.3 DeepSeek-R1

CLAIMED, https://arxiv.org/abs/2501.12948 and https://arxiv.org/html/2501.12948v1, read
22 September 2026:

> "the reasoning abilities of LLMs can be incentivized through pure reinforcement
> learning (RL), obviating the need for human-labeled reasoning trajectories"

> "Group Relative Policy Optimization (GRPO) foregoes the critic model and estimates the
> baseline from group scores instead."

> "Accuracy rewards evaluate whether the response is correct" ... "Format rewards
> enforce the model to put its thinking process between '<think>' and '</think>' tags."

A **rule-based reward** is a preference rule stated in text. R1's record states it and
states nothing about corpus contents.

### 4.4 DeepSeek-V4

A V4 report exists. CLAIMED, https://arxiv.org/abs/2606.19348 (*DeepSeek-V4: Towards
Highly Efficient Million-Token Context Intelligence*, April 2026), read 22 September
2026:

> "We present a preview version of DeepSeek-V4 series, including two strong Mixture-of-
> Experts (MoE) language models -- DeepSeek-V4-Pro with 1.6T parameters (49B activated)
> and DeepSeek-V4-Flash with 284B parameters (13B activated) -- both supporting a context
> length of one million tokens."

> "We pre-train both models on more than 32T diverse and high-quality tokens"

> "the Muon optimizer for faster convergence and greater training stability."

Same shape: token count, no sources, optimizer named. **DeepSeek-V4-Flash is the reader
under test in W10 stage C** and this is its own record.

### 4.5 DeepSeek-Coder — the one DeepSeek report that names its sources

CLAIMED, https://arxiv.org/html/2401.14196v1 (*DeepSeek-Coder: When the Large Language
Model Meets Programming*), read 22 September 2026:

> "We collect public repositories created before February 2023 on GitHub and retain only
> 87 programming languages"

> "The training dataset of DeepSeek-Coder is composed of 87% source code, 10% English
> code-related natural language corpus, and 3% code-unrelated Chinese natural language
> corpus."

The English portion is said to include "materials from GitHub's Markdown and
StackExchange".

This **falsifies the strong form of my P-A3.5**, which said DeepSeek reports name no
sources. One does. I record the failure rather than narrowing the prediction.

---

## 5. What Anthropic's records say

### 5.1 The corpus

Anthropic publishes no composition by subset. Its system cards give one sentence of the
same shape across releases. CLAIMED, search over anthropic.com and www-cdn.anthropic.com
for the phrase "trained on a proprietary mix of publicly available information on the
Internet", read 22 September 2026 — the sentences returned, attributed to the system
cards named:

> Claude Opus 4 and Claude Sonnet 4 "were trained on a proprietary mix of publicly
> available information on the Internet as of March 2025, as well as non-public data
> from third parties, data provided by data-labeling services and paid contractors, data
> from Claude users who have opted in to have their data used for training, and data
> generated internally at Anthropic."

> Claude Opus 5 "was trained on a proprietary mix of publicly available information from
> the internet, public and private datasets, and synthetic data generated by other
> models."

I mark these **weaker than the arXiv quotations**: they reached me through a search
summary of PDF system cards, not from a page I read whole. The system cards are PDFs;
I did not fetch them, to avoid the tool writing more cached files.

Cut-offs, from a page I did read whole. CLAIMED,
https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data,
read 22 September 2026:

> "Claude Opus 5 was trained on data up until May 2026."

> "Claude Fable 5.1 was trained on data up until June 2026."

> "Claude Sonnet 5 was trained on data up until January 2026."

That page states cut-offs and **no sources at all**.

### 5.2 The criterion, published

CLAIMED, https://arxiv.org/abs/2212.08073 (*Constitutional AI: Harmlessness from AI
Feedback*), read 22 September 2026:

> "The only human oversight is provided through a list of rules or principles, and so we
> refer to the method as 'Constitutional AI'."

> "In the RL phase, we sample from the finetuned model, use a model to evaluate which of
> the two samples is better, and then train a preference model from this dataset of AI
> preferences. We then train with RL using the preference model as the reward signal,
> i.e. we use 'RL from AI Feedback' (RLAIF)."

CLAIMED, https://arxiv.org/html/2212.08073v1, read 22 September 2026, on the appendix
that carries the list itself:

> "Here we show the constitutional principles and instructions we used for SL-CAI and
> RL-CAI. These were selected in a fairly ad hoc manner for research purposes."

with, as one of them:

> "Identify specific ways in which the assistant's last response is harmful, unethical,
> racist, sexist, toxic, dangerous, or illegal"

CLAIMED, https://www.anthropic.com/news/claudes-constitution, read 22 September 2026:

> "We use the constitution in two places during the training process. During the first
> phase, the model is trained to critique and revise its own responses using the set of
> principles and a few examples of the process. During the second phase, a model is
> trained via reinforcement learning, but rather than using human feedback, it uses
> AI-generated feedback based on the set of principles to choose the more harmless
> output."

> "Please choose the assistant response that is as harmless and ethical as possible. Do
> NOT choose responses that are toxic, racist, or sexist, or that encourage or support
> illegal, violent, or unethical behavior."

CLAIMED, https://www.anthropic.com/news/claude-new-constitution, read 22 September 2026:

> "Jan 22, 2026"

> "released under a Creative Commons CC0 1.0 Deed, meaning it can be freely used by
> anyone for any purpose"

> "Claude itself also uses the constitution to construct many kinds of synthetic training
> data" — including "rankings of possible responses"

> "Our previous Constitution was composed of a list of standalone principles. We've come
> to believe that a different approach is necessary"

### 5.3 What those two records make, put together

*worked out*, from 5.1 and 5.2, with every step shown:

1. The constitution is a text of the principles used as the criterion. (5.2, quoted.)
2. It was published on the public internet on 22 January 2026 and dedicated to the
   public domain. (5.2, quoted.)
3. Claude Opus 5 was trained on data up until May 2026, and its record says the data
   includes "publicly available information from the internet". (5.1, quoted.)
4. So the criterion text was publicly available on the internet, in the clear, for four
   months inside the window of a model trained under that criterion.

**What step 4 does not give.** Membership. Anthropic states no composition, so nothing
in the record says the constitution was in the corpus, and nothing says it was not. And
even membership would not give representation in (R)'s sense. So the Claude case is the
**sharpest particular candidate in the record and the least checkable one**. Its
sharpness and its unreachability come from the same fact: the corpus is not open.

Step 2 also plants a flag for the open corpora. A CC0 text is admissible by rule to a
corpus built from openly licensed sources (3.6). The Common Pile v0.1 was collected in
late 2024, before January 2026, so not that one — but the rule is now in place for any
later openly licensed corpus.

---

## 6. The two readings of the clause

### 6.1 Reading (i), the strict reading

**What it says.** The members of \(H\) are formal edit–boundary pairs, and
representation is undefined on them, so the clause excludes nothing.

**What holds it, in the theory's own words** (all *seen*):

- file 11, Part III: "The **contract** \(C\subseteq A\times B\) is the set of admitted
  edit–boundary pairs the claim ranges over".
- file 11, Part II: "\(A\) is a set of admitted edits, closed under a partial
  associative composition with identity \(1\). \(B\) is a set of boundary conditions."
  So a member of \(C\), and hence of \(H\subseteq C\), is a pair drawn from two sets of
  an organization's formal furniture.
- file 11, Part IV: "An **occurrence** is a physically located carrier." And (R):
  "An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when ...". The
  relation Rep takes an occurrence on the left.
- A pair \((a,b)\in A\times B\) is not a physically located carrier. So Rep is not
  defined on it.

**What the evidence makes of it.** Nothing. Not one quotation of section 3, 4 or 5
bears on reading (i). The reading is settled or not settled inside file 11, and the
corpus records are the wrong instrument for it. I said in `predictions.md` that this
was the outcome that would show the collection was the wrong instrument, and for
reading (i) it is.

**Consequence if (i) wins.** The clause does no work. W8 A6's own falsifier applies:
"a showing that the strict reading is right, in which case the clause does no work
anywhere in the theory and the finding is an ask for the Semantics project, never a
change made from here" (W8 part A6, *seen*). A6 goes from *unknown* to *idle*. W8 A5's
holder loses one of its two conditions — A5 reads "Held if the fourth clause of the
same definition holds (A6), and held if the independence premise of Derivation 3's
proof is read as file 11 now reads it" (W8 part A5, *seen*) — and becomes held if the
independence premise alone. That is a strictly better position for A5, bought by
throwing a clause of the theory away.

### 6.2 Reading (ii), the physical reading

**What it says.** A selected provenance is a claim about a physical history, so the
clause reaches the occurrences that realised the pairs.

**What holds it, in the theory's own words** (all *seen*):

- file 11, Part XII: "A selected provenance \(\operatorname{Sel}(t;\mathcal T,\mu,H)\)
  is a claim about a physical history: a population of realized transports, a
  physically admitted variation operator, and a survival condition enacted by the
  environment. It is fallible and checkable as any physical claim is."
- file 11, Part IV, inside the definition itself: "a finite history \(H\subseteq C\) of
  edit–boundary pairs **actually encountered**".

**Where reading (ii) is weaker than it is usually stated — and how far that survived my
own check.** Part XII's sentence lists three things as physical — the population, the
operator, the survival condition — and **does not list \(H\)**. So the sentence W8 A6
leans on does not itself carry \(H\) into the physical. That was my first finding, and
I went looking for what would show it wrong. I found it, in file 11, Part 0, grievance
9 (*seen*):

> "Selection is a physical history: a population, a variation operator, a survival
> condition and a sequence of events (Parts IV, XII)."

"a sequence of events" is the physical counterpart of \(H\), stated by the theory in its
own voice. So the restated finding, weaker than the one I first wrote: **Part XII's
sentence alone does not carry \(H\) into the physical, but file 11 elsewhere does.** The
physical reading rests on three places, not one — Part IV's "actually encountered",
Part XII's "a claim about a physical history", and Part 0's "a sequence of events" — and
an attack has to reach all three. That is a stronger position for reading (ii) than I
credited it with an hour earlier, and I record the correction rather than the first
draft.

**What the evidence makes of it.** Under (ii) the evidence bears, and here is exactly
how far.

| Step | Status |
|---|---|
| A corpus record names a source whose documents state losses, preference rules or principle lists | **claimed**, six records, section 9 |
| From a named source to a named document being present | **worked out** for the Pile alone, whose sentence is universally quantified ("all papers on arXiv up to the July 2020 dump"); **unknown** for every other record, whose sentences name a source without quantifying its contents |
| From a document being present to an occurrence realising a member of \(H\) | **unknown**: presence in a corpus is not presence in the finite history actually encountered; deduplication, filtering, sampling and epoch scheduling all sit between |
| From that occurrence to representation under (R) | **unknown**: (R) needs a faithful transport with selected or constructed provenance, and no record speaks to it |
| From representation of a *generic* loss to representation of *the* survival condition | **unknown and probably false**: section 2's narrowing |

So: under reading (ii) the evidence settles the **first** link, makes the second link
deductive for one corpus, and leaves the last three where they were. A6 stays
*unknown*, but it is now unknown for a **named** reason at a **named** link rather than
for want of looking.

**Consequence if (ii) wins and the clause then fails.** W8 A6, *seen*: "If the clause
fails, the provenance is neither selected nor constructed, so by the trichotomy it is
declared, and a declared transport makes no occurrence represent anything." And file
11, Part IV, *seen*: "A declared transport does not make an occurrence represent
anything; it makes a modeller assert that it does."

One thing to record about that step, found by taking it apart: **A6's move from "not
Selected" to "Declared" is held jointly with A9.** The trichotomy has three limbs, and
failing the fourth clause is precisely the shape that would push a transport toward
*Constructed* — Part IV, *seen*: "**Constructed.** There is an episode (Part X) whose
construction witness prepares \(t\), and in which \(t\), or the organization it targets,
is available as a represented target." What rules Constructed out is W8 A9's finding
that no construction witness is produced. So A6's consequence is not A6's alone. It
should be marked *held, jointly with A9*.

The cost if it lands: W8 A5 loses its subject; B6, whose heading reads "A target may
come from the weights, and a rival may be built from the problem in the context"
(*seen*), loses the word *fitted*, which is selected provenance under another name
(file 33 word list: "fitted | selected provenance | Part IV"); and the model's whole use
of the qualified Derivation 3 goes, since Derivation 3 is a theorem about selected
transports. That is a large bill, and it
is the reason the clause is worth this much work.

### 6.3 The rival reading, built because the skill requires one

Neither W8 A6 nor my task names it, and it is the best rival I can build.

**Reading (iii), the exclusivity reading.** The clause is what keeps Selected and
Constructed apart: it says the criterion was not available as a represented target
**to the process that did the selecting**.

What holds it (file 11, Part IV, *seen*): "Neither provenance is reducible to the other:
a selected transport has no represented target and no criticism in its history; a
constructed one has both." That sentence restates the clause in plain words, puts
"represented target" where the clause puts "represents", and says "in its history" —
not "in its corpus".

**What tells (iii) apart from (ii).** Under (ii) the question is settled by corpus
membership. Under (iii) it is settled by the **declared boundary**: whether the
engineers who wrote the loss are inside the system. file 11, Part XII, *seen*: "A
capability is attributed to a system under a declared boundary (which processes and
resources are the system's) ... Both are declared before the attribution, not chosen
after it." W8 part B1 declares a boundary at which "the record, the corpus and the owner
are outside it" (W8 section 1, *seen*).

So a change that separates them: **move the boundary to enclose the training run's
engineers, holding the corpus fixed.** Under (ii) nothing changes — the same documents
are in the same corpus. Under (iii) the clause flips, because the criterion becomes
represented inside the system. That is a poke a judge can run on paper, and it is the
one I would put to the DeepSeek examiners first.

If (iii) is right, the evidence of sections 3 to 5 is **beside the point**, and A6's
named check — look in the trainer's record for an occurrence — is looking in the wrong
place. I report this as the finding most likely to overturn my own collection.

---

## 7. The sharpest test an open corpus allows, as a procedure

W8 A6 says of its two checks: "Neither check is a run this repository can make."
(*seen*). That is true of this repository. It is **not** true of a public corpus index,
and this section names the run.

### 7.1 What the test has to be

From section 2: the clause bites only on a text that states **the survival condition of
the training that used that corpus**, or **\(H\)**, or **\(t\)**. From section 6.2: what
an index can settle is membership, and membership alone. So the sharpest available test
is:

> **Is there a named document, in a named open corpus, that states the loss function of
> a model trained on that corpus?**

That is the question my task names, and it is the right one, because it is the only
link in the chain that a search can close.

### 7.2 The instruments, with addresses

CLAIMED, https://infini-gram.io/, read 22 September 2026:

> Infini-gram is "an engine that efficiently processes n-gram queries with **unbounded
> n** and **trillion-token massive corpora**."

> the index is built on "the union of several open text corpora: {Dolma,
> RedPajama-Data-1T, Pile, and C4}."

Its query types, same address and date, include "Document search using individual n-gram
terms, multiple terms, or combined Boolean expressions", and its web interface is given
as https://hf.co/spaces/liujch1998/infini-gram with a documented API.

CLAIMED, https://arxiv.org/abs/2303.03919 (*Data Portraits: Recording Foundation Model
Training Data*), read 22 September 2026:

> "Using our tools, we document a popular language modeling corpus (The Pile) and a
> recently released code modeling dataset (The Stack)."

> "We release a live interface of our tools at https://dataportraits.org/"

CLAIMED, https://arxiv.org/abs/2211.15533, read 22 September 2026: the "Am I in The
Stack" tool, "for developers to search The Stack for copies of their code".

Three independent indices over four of the five open corpora this task names. Note
that none of them indexes FineWeb or Dolma 3, and the examiner should say so.

### 7.3 The procedure, written so a stranger could run it

**Name the corpus and the model.** Corpus: the Pile. Model trained on it: GPT-NeoX-20B
(section 3.1, quoted). Second pair: Dolma, and OLMo (section 3.2, quoted).

**Step 1 — fix the target documents before searching.** Three, fixed now:

| Target | Why it is the target | What it would settle |
|---|---|---|
| `torch/nn/functional.py` from pytorch/pytorch, the definition of `cross_entropy` | the Pile's GitHub rule is "only repositories with more than 100 stars"; PyTorch clears it by orders of magnitude; the function is the one that computes GPT-NeoX-20B's loss | a text in the corpus that **states the loss function of a model trained on that corpus** — the sharpest case, in code |
| arXiv:2005.14165, "Language Models are Few-Shot Learners" | arXiv v1 28 May 2020, inside "all papers on arXiv up to the July 2020 dump" | a text stating the objective of a model of the same family; weaker, because the objective is another model's |
| arXiv:1711.05101, "Decoupled Weight Decay Regularization" | v1 14 Nov 2017, inside the same window; named by GPT-NeoX-20B as its optimizer | **does not bear on the clause** (section 2): it states \(\mu\). It is included as the *nearest innocent neighbour*, the thing the test must **not** fire on |

The third row is there on purpose. The skill's rule: "run it on the very thing it is
meant to catch, and on that thing's nearest innocent neighbour. A test that both pass is
measuring something else." An examiner who reports "found, therefore the clause fails"
for row three has shown the test measures presence, not the clause.

**What I went looking for that would sink row one, and found.** Two things, both kept.
(a) The Pile's record gives one GitHub admission rule — "more than 100 stars" — and
says nothing about the other filters (size, extension, licence) that a real pipeline
carries; so membership is genuinely open, which is why this is a test and not a claim.
(b) Large-model training does not always call `torch.nn.functional.cross_entropy`;
Megatron-style stacks use a fused vocabulary-parallel cross-entropy of their own. So
row one, if found, gives a text stating **the loss function that was minimised**, and
not necessarily the exact code path that ran. That distinction does not matter to the
clause — the clause is about the survival condition, not about which implementation
computed it — but it matters to anyone who reports row one as "the file that trained
the model", and the examiner must not say that.

**Step 2 — pick a query string per target that no other document would carry.** For
row one, a distinctive line from the function's body or docstring, not the function name
(the name occurs in thousands of files). For rows two and three, a sentence from the
abstract: "We introduce Adam, an algorithm for first-order gradient-based optimization
of stochastic objective functions" is such a string for the Adam paper, and the analogue
is chosen from each target.

**Step 3 — run the search.** infini-gram document search, restricted to the `Pile`
index, then to the `Dolma` index; independently, dataportraits.org for the Pile and The
Stack; independently, "Am I in The Stack" for `pytorch/pytorch`.

**Step 4 — record the raw return as it came**, count of matching documents per index per
string, and the index version string, since the indices are of particular corpus
versions and the Pile has known variants.

**Step 5 — read the result.**

| Result | What it settles |
|---|---|
| Row one **found** in the Pile or Dolma index | Under reading (ii): the corpus contains a text stating the loss function computed in the training of a model trained on that corpus. The first link of section 6.2's chain closes **deductively** rather than by the Pile's quantified sentence, and the second link ("present in the corpus") closes too. A6 moves from *unknown* to *held if the physical reading is right* — exactly the move W10 section 7 names. Three links remain open and the report must say so. |
| Row one **not found** | The clause's sharpest open case is not available. W8 A6's own falsifier bites: "a trainer's record showing the corpus contains no such occurrence, in which case A6 collapses into A5". Not found in an index is weaker than that — "found nowhere means unknown" — so the honest report is that the sharpest test ran and returned nothing, and A6 stays *unknown* with one fewer route. |
| Row three found **and** row one not found | The test is measuring presence of machine-learning text in general, not the clause's subject. Redesign before anything follows. |
| Rows one and three both found | Consistent, and the examiner must not add them. Row three is reported as \(\mu\) and set aside. |

**Step 6 — the reading question, which no search settles.** Run section 6.3's poke on
paper: hold the corpus fixed, move the declared boundary to enclose the training run's
engineers. If the answer to "does the clause hold" changes, reading (iii) is live and
the search of steps 1 to 5 was answering a different question.

### 7.4 What would settle A6 either way

**Would settle it against the clause (the clause fails).** A document found in a named
open corpus index that states the **particular** survival condition of a model trained
on that corpus — its loss with its own hyperparameters, or its own criterion list — plus
a showing that the document's organization admits a faithful transport to that content
with selected or constructed provenance. The first half is a search; the second half is
an argument about (R) that a judge makes, and it is where the case will actually be won
or lost.

**Would settle it for the clause (the clause holds).** Either the strict reading shown
right from file 11's own sentences, in which case the clause is vacuous and idle; or
reading (iii) shown right plus the declared boundary of W8 B1 held to, in which case the
criterion is represented only outside the system and the clause holds by the boundary,
not by the corpus.

**What would settle nothing.** Any number of optimizer papers. Any number of generic
cross-entropy statements. Any count of corpora that name arXiv. Repeats add nothing:
weighing the same thing on the same scale does not settle what the bag weighs.

---

## 8. My predictions, marked

| Prediction | Tested? | What happened |
|---|---|---|
| P-A3.1 every itemised open corpus names arXiv/GitHub/StackExchange/academic source | tested | **held** for the Pile, Dolma, RedPajama, Common Pile, Dolma 3. C4 and FineWeb name none, as I said in advance they would. |
| P-A3.2 no corpus documentation names an individual document | tested | **held for documents, failed for sources.** Dodge et al. name `patents.google.com` as C4's most represented site and WIMBD names `arxiv.org` as >12% of RedPajama's documents; the Common Pile names the PEPs as a whole set. No record names an individual document. The Pile's quantified sentence is the interesting middle case and I had not foreseen it. |
| P-A3.3 no corpus paper says it contains the paper describing its own model | tested | **held.** I found no such sentence in any record read. |
| P-A3.4 the self-case is reachable by dates | tested | **held, and narrower than I wrote it.** Reachable for the *optimizer* (the Pile contains the AdamW paper; GPT-NeoX-20B uses AdamW) — and section 2 then shows the optimizer does not bear on the clause. Reachable for the *loss* only through code (PyTorch in the Pile's and Dolma's code subsets), which is why section 7 makes that the target. |
| P-A3.5 DeepSeek reports state composition in kind, never by source | tested | **failed.** DeepSeek-Coder names GitHub, GitHub Markdown and StackExchange, with a date ("created before February 2023"). The prediction was too strong and I let it stand as written rather than narrow it. |
| P-A3.6 Anthropic publishes a principle list and no composition | tested | **held**, and sharper than I expected: the constitution is CC0 since 22 January 2026 and Opus 5's cut-off is May 2026. |
| P-A3.7 at least one record ticks W10.3, and it will be the Pile | tested | **held**, and for the reason I did not predict — not the itemisation but the universal quantifier over arXiv's contents. |

**The prediction I did not write and should have.** That the clause names three things
and not four, so that optimizer evidence falls outside it. Section 2 was forced by
reading, not predicted, and everything downstream of it was shaped by it. A reader
should treat section 2 as the place where my collection could most easily have gone the
other way.

---

## 9. W10.3, ticked

W10's own wording: "at least one open trainer's record states that its corpus contains
texts of the kind the fourth clause forbids, with the sentence quoted; zero falsifies
the physical reading's reach from here and the clause stays unknown."

The count is the plan's instrument and is not a mark. It is reported at three levels,
never summed, because the levels do different work.

**Level A — records stating contents by universal quantification over a named source
(membership of a named document follows deductively): 1.**

1. **The Pile.** "We downloaded the TeX sources of all papers on arXiv up to the July
   2020 dump (the last file included in our data is arXiv_src_2007_068.tar) via arXiv's
   S3 Bulk Source File Access" — and — "we use GitHub 'stars' as a proxy for quality,
   and choose to gather only repositories with more than 100 stars." (CLAIMED,
   https://ar5iv.labs.arxiv.org/html/2101.00027, 22 September 2026.)

**Level B — records naming a source whose documents state a loss, a preference rule or
a principle list, without quantifying its contents: 5.**

2. **Dolma.** "The peS2o dataset is a collection of approximately 40 million open-access
   academic papers ... derived from the Semantic Scholar Open Research Corpus (S2ORC)."
   and "the Stack, a deduplicated but otherwise unfiltered collection of
   permissively-licensed GitHub repositories. The raw version of this dataset was
   collected in March 2023." (CLAIMED, https://arxiv.org/html/2402.00159v2, 22 September
   2026.)
3. **RedPajama-V1.** "We downloaded arXiv data from Amazon S3 in the 'arXiv' requester
   pays bucket and implemented a similar postprocessing, keeping only LaTeX source files
   ..." with slices ArXiv 28B, GitHub 59B, StackExchange 20B tokens. (CLAIMED,
   https://arxiv.org/html/2411.12372v1, 22 September 2026.)
4. **The Common Pile v0.1.** "ArXiv Papers ... contain over 2.4 million articles in the
   quantitative sciences, most of which are uploaded as LaTeX source" and "we filter
   peS2o ... to only retain openly licensed research papers." (CLAIMED,
   https://arxiv.org/html/2506.05209v1, 22 September 2026.)
5. **Dolma 3 / Olmo 3.** "Dolma 3, a new ~9.3-trillion-token corpus drawn from web
   pages, science PDFs processed with olmOCR, codebases, math problems and solutions,
   and encyclopedic text." (CLAIMED, https://allenai.org/blog/olmo3, 22 September 2026.)
6. **DeepSeek-Coder** — a trainer's record whose corpus is not open. "We collect public
   repositories created before February 2023 on GitHub and retain only 87 programming
   languages" and "The training dataset of DeepSeek-Coder is composed of 87% source
   code, 10% English code-related natural language corpus ..." (CLAIMED,
   https://arxiv.org/html/2401.14196v1, 22 September 2026.)

**What Level A is, and what it is not.** Level A is about the *shape* of a sentence —
whether it quantifies universally over a named source's contents — and relevance is a
separate filter. The Common Pile has a universally quantified sentence too ("All Python
Enhancement Proposals (PEPs) ... that were released into the public domain"), and it
does not reach Level A here only because PEPs are not texts of the kind the clause
touches. I looked for this because it is what would have shown my A/B split to be a
dressed-up ranking, and it half did: the split is real, but it is two tests, not one.

**A record kept out of the count, named.** The Stack (R8) is a corpus in its own right
with its own trained model, so it could be counted as a seventh record. It is kept out
because it *is* Dolma's code subset and the Common Pile's, and counting it again would
weigh one body of text twice. In or out, the threshold is already met; the reviewer can
put it back and nothing downstream moves.

**Level C — records stating that the corpus contains a *named document* of the kind the
clause forbids: 0.**

No record read states this. The Pile's quantified sentence entails it for named
documents but does not state it, and entailment by the reader is *worked out*, not
*claimed*.

**The tick.** W10.3 holds at Level A and Level B: the threshold is "at least one", and
six records qualify at the level of source, one of them by a sentence from which named
membership follows. It fails at Level C, and the physical reading's reach from here
therefore stops at the first of the five links in section 6.2. **A6 stays *unknown*.**
The tick moves nothing on its own; what would move it is section 7's run.

---

## 10. Where the parts of this collection came from, and what it does not show

**Provenance of the pieces.** The clause's decomposition in section 2 is *built* —
forced by reading the definition word by word. The two readings in 6.1 and 6.2 are W8's
and are *asserted* there; the sentences that hold each are *seen* in file 11. Reading
(iii) in 6.3 is *built*, by me, from one sentence of Part IV. The corpus facts are all
*claimed*. The chain in 6.2 and the dates in 3.1 are *worked out*.

**Findings that fit no part, kept rather than absorbed.**
- Part XII's selection sentence does not list \(H\) among the physical things, which
  weakens the reading W8 A6 favours at exactly the place A6 leans hardest.
- A6's step from "not Selected" to "Declared" needs A9 and does not say so.
- DeepSeek-Coder names its sources; the other DeepSeek reports do not. Whatever explains
  the difference is not in this collection.

**What this does not show.** Nothing here shows the clause holds or fails. It shows
which link in the chain the record reaches, which it does not, and what run would reach
the next one. Hard to vary is not the same as true, and a count of corpora is not a
mark.

**What was not looked at.** Non-English corpora; Nemotron-CC, Zyda, MAP-Neo, Matrix and
other open corpora I did not reach; the Pile's Pile-CC snapshot date; whether
`pytorch/pytorch` actually survives the Pile's and The Stack's filters, which is
precisely what section 7 is for; the licence status of any particular arXiv paper under
peS2o's open-access filter; and Anthropic's system-card PDFs, which I did not fetch.

**One next step.** Hand section 7.3 to a DeepSeek examiner in stage E with the three
target rows fixed as written here, and require the row-three result to be reported
beside the row-one result. If the examiner reports only row one, the run was not the
test.
