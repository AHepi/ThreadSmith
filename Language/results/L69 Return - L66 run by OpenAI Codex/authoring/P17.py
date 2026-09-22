# Written by OpenAI Codex under L66.
from ledger_writer import Ledger
p=Ledger('P17')
p.b(1,p.sentences['1'],'Admonition must not forget plus slight-or-no versus immense advantage, increases in numbers and standards, and joint contributors. Dropping these quantitative contrasts would change the argument; no unqualified individual or tribal advantage is asserted.')
p.b(2,p.sentences['2'],'Hypothetical tribe qualified by many members/high degree, their readiness and purposes, and victory over most tribes. No actual tribe or victory is instantiated; the what-if contains no single admitted change from an actual ledger and its quantified outcome is outside scope. The conditional identification as natural selection remains visible here.')
p.thing('a',3,'tribes','tribes')
p.thing('b',3,'other_tribes','tribes')
p.add('c',3,'c: tribes SUPPLANTED other_tribes',['did(c, tribes, supplanted, other_tribes, none) :- $.','holds(supplanted(tribes,other_tribes)) :- $.'])
p.fact('d',3,'morality is an element in tribal success','element_of(morality,tribal_success)',standing='GIVEN')
p.b(3,'At all times throughout the world; important; standard of morality and number of well-endowed men will thus everywhere tend to rise and increase','Unbounded time/place, importance, degree and population-count increases, and the inference to them. d does not assert that morality alone is sufficient to produce success or increasing numbers.')
p.r(2,'an actual reported tribe or a hypothetical class described through a quantified conditional','hypothetical conditional only; its full qualifications stay in the bin rather than become an actual specimen')
p.r(3,'a particular historical replacement or a collective historical assertion','collective assertion using the writer\'s supplanted, no chosen tribe/date or physical press')
p.v('supplanted',3,'unshaped happening; no push/hit substitute')
p.finish()
