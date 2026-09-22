# Correction to the original P11 / P14 hand-decision commentary

Written by OpenAI Codex. This new file corrects an interpretive error in `P11_P14_original_hand_decisions_OpenAI_Codex.md`, which is preserved unchanged. It changes no source, ledger, report, raw log, only-list decision or near-list decision.

The original commentary's section “Same wording, different standing and implementation” and its final paragraph incorrectly characterize P14 g's unconditional actual-world encoding as a translation defect that keeps spread true under MAKE NOT SO. That interpretation failed to inspect the driver's dependency-based removal. It is withdrawn. The section's observation that both `.pl` files have `holds(spreads(helping)) :- line(g)` is accurate but does not establish behavior under that operation.

Seen in `../rig1/P14_OpenAI_Codex.report.txt` and its raw log: P14's MAKE NOT SO operation sets aside g because the ledger's h says the effect came from f. The raw query `holds(spreads(helping))` with `removed: ['f', 'g']` returns “No models.” Seen in `../rig1/P11_OpenAI_Codex.raw.txt`: P11's corresponding query removes only f and returns a model justified by g. Both reports print HOLDS because their expected answers are opposite. P14 correction1 has the same behavior, as recorded in `../rig1/P14_correction1_OpenAI_Codex.report.txt` and `.raw.txt`.

Seen in `../consequences/P14_OpenAI_Codex.report.txt`: taking out line f alone removes `holds(exists(group_structure))` and leaves spread. That tool performs simple one-line removal; it is not the dependency-based MAKE NOT SO operation. Conflating them caused the withdrawn interpretation.

Worked out: g records the source's actual outcome, alongside the separate causal claim h. It does not add a second production premise or prove that causal claim. The causal check still reports JUMP at h, because no executable production route is supplied. HOLDS on the negative what-if is failed derivability of the positive query after the driver removed the declared dependent effect, not a derivation of an explicit negative fact and not validation of a production mechanism.

The original only/near item decisions, the g standing difference, and the bin-retention asymmetry remain as recorded. For the primary comparison and its operational qualifications, read `P11_P14_correction1_primary_hand_decisions_OpenAI_Codex.md`.
