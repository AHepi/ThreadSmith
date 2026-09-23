You are marking one report written by a reviewer who was asked to audit a theory document and list its defects. You are given: (A) the answer key, which lists errors known to be in the document the reviewer read, with what counts as finding each; (B) the document the reviewer read; (C) the report. The reviewer did not see the answer key.

Mark strictly by the key's "Found when" rules. An error is FOUND only if the report locates it (the right Part, sentence or formula) AND says what is wrong with it in a way the key's rule accepts. Mentioning the location while praising it, or objecting to it for an unrelated reason, is NOT FOUND. Quote the report's own words as evidence for every FOUND.

Then take every other defect the report lists (every item that does not count as finding a key error) and judge it against the document: GENUINE (the document really has this problem as stated), MISTAKEN (the document does not have this problem: the report misreads, misquotes, or its argument fails), or UNCLEAR (a matter of judgement or presentation you cannot settle). Give one sentence of reason each.

Answer with a single JSON object and nothing else, in this form:
{"key": {"<error id>": {"found": true|false, "evidence": "<the report's words, or empty>"}, ...},
 "others": [{"item": "<the report's heading or first words>", "verdict": "GENUINE"|"MISTAKEN"|"UNCLEAR", "reason": "<one sentence>"}, ...],
 "report_items_total": <number of defects the report lists>}

Include every error id in the key, in its order.
