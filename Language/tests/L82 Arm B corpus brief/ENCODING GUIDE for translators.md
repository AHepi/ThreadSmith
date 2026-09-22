# Encoding guide: how the ledger you write becomes a file the checker can run

You translate under the translator's task (39) and the language definition (L80, the second version of 38), both attached. Your printed output has the five sections 39 asks for. After them, print the ledger once more as ONE JSON object inside a fenced code block that begins with the line ```json and ends with ```. Nothing else goes in that block. The checker's driver reads it; a program builds the Prolog file from it. Every field below is required unless marked optional.

```
{
 "paragraph": "<the text's id>",
 "whose": "<your name, the model you are>, under L82",
 "sentences": {"1": "<sentence 1 verbatim>", "2": "..."},
 "bin": [ {"sentence": 3, "words": "<the words binned>", "reason": "<why>"}, ... ],
 "leftover": [ "<one string per bin entry: 'Sentence 3: <words> — <reason>'>" ],
 "whatifs": [ {"whose": "<you>, sentence N line j", "text": "<the what-if in the writer's words>",
               "make_not_so": "<a fact term, e.g. exists(group_structure)>"  OR  "withdraw": "<a line id>",
               "ask": "<a query term, e.g. holds(spreads(helping))>", "claims": true|false} ],
 "lines": {
   "<id>": {"mark": "said" | "filled in" | "usual case",
            "sentence": <integer>,
            "standing": "CLAIMED" | "GIVEN" | "SUPPOSED in case <name>" | "TOLD in world <name>",
            "text": "[<standing>] <the line in the language's words>",
            "case": "<name>", "case_kind": "told" | "supposed",        <- only for TOLD and SUPPOSED lines
            "prolog_clauses": ["<one or more Prolog clauses, each ending with a full stop>"]}
 },
 "words_split": [ "<word>: <sense 1> / <sense 2>" ],
 "readings_chosen": [ "Sentence N: <the readings open>; chosen: <the one taken>" ]
}
```

## Line ids
Short lower-case letters or words with no spaces (`a`, `b`, `lamp`, `since1`). The same id is used in `lines`, in `prolog_clauses` (as `line(<id>)`), and in any line that points at another.

## Prolog clauses: the vocabulary the checker reads
Every clause of a line has `line(<id>)` as its first body goal, so the line can be taken out. Atoms are lower-case with underscores; variables are capitalised. Use only these predicates (the checker asks about exactly these):
- **A thing line**: `kind(<thing>, <kind>) :- line(id).` and `body(<thing>, not_stated) :- line(id).` (the response to a press, when not stated).
- **A fact that is claimed or given**: `holds(<fact>) :- line(id).` for example `holds(burning(lamp))`, `holds(returned(visitor))`, `holds(stayed_dry(letter))`.
- **A denied fact** (NOT [...] over a fact): `denied(<fact>) :- line(id).`
- **A general line, ALWAYS, of the MAKES kind** (a cause that produces its effect): `produced(<effect>(X)) :- line(id), kind(X, <kind>), holds(<condition>(X)).` and beside it `depends(<effect>(X), <condition>(X)) :- line(id), kind(X, <kind>).`
- **A general line, ALWAYS, of the SHOWS kind** (a rule that lets one thing be read off another, not a cause): `holds(<conclusion>(X)) :- line(id), <goals>.`
- **A general line, USUALLY**: the same as ALWAYS with `, not exception(id, X)` as the last goal of the head clause, and `exception(id, X) :- denied(<effect>(X)).` beside it.
- **An exception to a USUALLY line**: did not apply: `exempt(<usually line id>, <thing>) :- line(id).`; the opposite happened: `exception(<usually line id>, <thing>) :- line(id).` and the fact that happened as `holds(...)`.
- **A BECAUSE claim** (the text says one thing produced another): `claim_because(id, <effect fact>, <cause fact>) :- line(id).` The effect and cause are the same terms as the `holds(...)` facts of the lines it points at. Do not also write a rule that makes the cause produce the effect unless the text states such a rule.
- **A denied BECAUSE** (NOT [X because Y]): `denied_because(id, <effect>, <cause>) :- line(id).`
- **A SINCE claim** (a reason to expect, not a cause): `claim_since(id, <what is expected>, <the reason>) :- line(id).`
- **A plan** (do A so that F): `claim_plan(id, <action term>, <aim fact>) :- line(id).`; what the action changes, if the text says: `changes(<action>, <what>) :- line(id).`; what the aim depends on, if the text says: `depends(<aim>, <what>) :- line(id).`
- **A likeness** (two events alike): `claim_like(id, <event a>, <event b>) :- line(id).`
- **A what-if line** has no clause; it is the `line(id).` fact and an entry in `whatifs`.
- **A TOLD or SUPPOSED line** uses the same clauses; its `case` and `case_kind` fields tell the checker which world it belongs to. Every line of one world carries the same `case` name. A told world does not inherit the actual ledger; state inside it every fact its argument needs.

## Three complete examples
Attached as `example_T10D.json` (a report with a cause claim inside a told world), `example_P14.json` (ALWAYS SHOWS rules, a BECAUSE, a NOT, a what-if) and `example_A.json` with `example_A.pl` (an ALWAYS MAKES rule with produced/depends, a plan, a usual-case line about a kind). Match their shapes.

## Final checks before you print
1. Every line in the table has an entry in `lines` with the same id, mark, standing and sentence.
2. Every `prolog_clauses` entry ends with a full stop and has `line(<its own id>)` as its first body goal.
3. Every fact term used in a `claim_because`, `claim_since`, `denied_because` or `claim_plan` is spelled exactly as in the `holds(...)` of the line it points at (same atom names, same argument order).
4. Every sentence of the text is either the `sentence` of some line or the `sentence` of some bin entry, or both.
5. The JSON is valid: double quotes, no trailing commas, no comments.
