# Written by OpenAI Codex under L66.
from ledger_writer import Ledger
p=Ledger('P03')
p.fact('a',1,'unjust laws exist','exist(unjust_laws)')
p.b(1,'shall we be content to obey them, or shall we endeavor to amend them, and obey them until we have succeeded, or shall we transgress them at once?','A question proposing alternatives, not an assertion that any action or goal occurs; timing and intention also remain unrepresented.')
p.b(2,p.sentences['2'],'Attribution of thought, obligation, temporal until and majority quantification. Its content supplies no nonmodal claim suitable for a TOLD ledger; no belief is turned into an actual duty or action.')
p.b(3,p.sentences['3'],'An attributed modal conditional with a comparative evaluation. No resistance is asserted; the supposed outcome cannot be rendered without losing would/worse.')
p.b(4,p.sentences['4'],'Responsibility for a comparative worsening. The degree/evaluation worse than is excluded; substituting a binary bad-remedy proposition would change the claim.')
p.b(5,p.sentences['5'],'It resolves to government and remedy, but the causal effect remains comparative worsening. No bare MAKES action with a different effect is substituted.')
for s in range(6,11): p.b(s,p.sentences[str(s)],'Rhetorical question, retained as mentioned under 38/39. No proposition presupposed by the question is silently promoted to CLAIMED; imagery, evaluations and timing within it are likewise not checked.')
p.r(4,'a comparative moral/practical judgement or a plain state with a causal explanation','comparative judgement; retain its full wording in the bin, without asserting a different effect')
p.r(5,'it refers to government or remedy','subject government, object remedy; this resolves reference but does not create a representable degree-free causal claim')
p.r('6–10','literal information questions or rhetorical accusations','rhetorical questions; both readings remain questions and therefore go to the bin, not actual-ledger accusations')
p.finish()
