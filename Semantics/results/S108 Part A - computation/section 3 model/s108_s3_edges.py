# S108 Part A, section 3: the edges (rule 5), the reply's marked and those the computation adds, as data.
#   python3 -B s108_s3_edges.py JSON_OUT MD_OUT
# Writes the JSON beside the md ("S108 Part A - section 3 - variants computed.json") and the md table of §8 to MD_OUT.
# Standing: computed (the computation shows it), contradicted (it shows otherwise), not settled by computation (with what would
# settle it), added (shown by the computation, not named by the reply). Marks are the frozen template's. Evidence names the
# run: cases = section 3 runs/cases/cases.txt; suite.<v> = section 3 runs/suite/; worlds.<kind> = section 3 runs/worlds/.
import json
import sys

E = []


def cls_of(standing, named):
    if not named:
        return "added"
    if standing.startswith("contradicted"):
        return "contradicted"
    if standing.startswith("not settled"):
        return "not settled by computation"
    if "in part" in standing or "not settled" in standing:
        return "computed in part"
    return "computed"


def e(variant, kind, item, mark, why, standing, evidence, settle=None, named=True):
    E.append(dict(variant=variant, kind=kind, item=item, mark=mark, reply_why=why if named else None, named_by_reply=named,
                  standing=standing, standing_class=cls_of(standing, named), evidence=evidence, what_would_settle=settle))


# ---- V3.1 D9.7 RO(α, φ) :⟺ Incons(φ, concl(α)) ----------------------------------------------------------------------------
e("V3.1", "constrains", "L397.s5", "FROZEN", "X_j(ψ) = usable ∧ RO must stay a reading of the frozen words; the variant lives inside RO",
  "computed", "X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)} is still 'the set of arguments usable by j that rule out ψ' under V3.1 (the frozen words name no block); its extension grows: worlds.args 1,677 of 9,600 (model, φ) Out_j F → T, 175 more X_j moves; usability 0 moves")
e("V3.1", "changes with", "L8.s3", "S1", "'the claim's denial is not among its premises' states the block in Part 0; must change with the variant",
  "computed", "L8.s3's clause is false of D9.7 under V3.1: ¬PM alone rules out PM (FC72 (e) as claimed → not as claimed; cases §C); p alone rules out ¬p for j who accepts p")
e("V3.1", "moves", "(Suff) and (Nec) defeat sets (D16.XV)", "S4", "ruling out by bare acceptance enters them; being an explanation (Acc ∧ ¬Dec) unmoved",
  "computed", "j accepting ¬Expl(ℰ) alone: an argument not using (E) rules out Expl(ℰ) F → T; the pole's forward candidate (Acc T, constructed) in Def(L536) F → T; j accepting Expl(ℰ) alone rules out ¬Expl(ℰ) ((Nec), L61) F → T (cases §C). Acc, Dec, Account ∧ ¬Dec(t): 0 moves on 27 worked cases, FC-E1–E5, CT1–CT8, 61,900 generated candidates (§3, §5, §6.1)")
e("V3.1", "changes with", "L397.n14, L397.s16", "S3", None, "added",
  "the two sentences varied with D9.7 (new form not given by the reply) are false of it under V3.1: 'p because p' (L397.s16) rules ¬p out for j who accepts p; a record made from ψ rules out ¬ψ (FC72 (b)); FC72.new1 (b) (O4, O5: 'the block alone tells it from the denial'): as claimed → not as claimed", named=False)
e("V3.1", "changes with", "D9.9 (K3), FC71 (i), (i′)", "S3", None, "added",
  "D9.9's clause 'no leaf of α with ¬(T∧B∧I) as a conjunct' and its record-leaf clause (L395) no longer block: FC71 (i), (ii) holds → counterexample (α⁺ ∈ X_j(T∧B∧I) with the block present); FC71 (i′) as claimed → not as claimed (suite.V3.1)", named=False)
e("V3.1", "changes with", "FC60 (b) (E3, the two balances: a bias set from the favoured mass)", "–", None, "added",
  "the record made from x = m* now rules out x ≠ m*: FC60 (b) as claimed → not as claimed (suite.V3.1)", named=False)
e("V3.1", "changes with", "FC72.new2 (c), K1 (the myth about winter, L397, S28)", "–", None, "added",
  "j2, who holds 'Slot ∧ ¬Acc(ℰ_myth1)' as one premise (the finding with the denial in it), rules the myth out under V3.1 (blocked under none): FC72.new2 (c) as claimed → not as claimed; the myth's Acc and being an explanation unmoved (S44, S45 untouched: ruled out for j is not 'not an explanation')", named=False)
e("V3.1", "moves", "who has ruled what out (D9.8), problems (D10.1)", "S2; FROZEN", None, "added",
  "worlds.args: 1,677 new Out_j(φ), smallest: ¬q accepted rules out q; no usability moves (V3.1 reads RO only)", named=False)

# ---- V3.2 D9.4 Live_j(d; u) :⟺ d ∈ Accepted_j(ξ) ------------------------------------------------------------------------
e("V3.2", "constrains", "L389.s1", "FROZEN", "Live must remain a predicate of (d;u) read by K2's ∀d",
  "computed", "under V3.2 Live_j(d; u) is still a predicate of (d; u), constant in u; (K2) as displayed is read unchanged; every suite run under V3.2 computes (K2) through it")
e("V3.2", "moves", "X_j and everything downstream (D9.8; D10.1)", "S2; FROZEN", "fewer usable arguments; fewer ruled out; fewer problems and fewer solved; no conjunct of (E) moves",
  "computed, in part; 'fewer problems' contradicted", "fewer usable: worlds.args 8,983 argument usabilities T → F, 26 Out_j T → F; FC47 (b), FC53 (a), FC68 (b)–(c), FC70, FC71 (i), (i′) move. Fewer solved, more problems: FC47.new1 (the pole, forward against reversed): solved at ξ and ξ″ under none (|X_j(Acc(ℰ_rev))| = 4, Prob_j F) → unsolved at all three (|X_j| = 0, Prob_j T): with fewer ruled out, D10.1's NotOut holds of more rivals, so problems grow. (E): 0 moves")
e("V3.2", "changes with", "L393.n2", "S3", None, "added",
  "L393.n2 defines Live 'd = concl(u′) for some u′ ∈ Below(u) with Usable_j(u′) (D9.4), or a premise j tentatively accepts': false of D9.4 under V3.2 (FC70: a premise live twice over is no longer live after withdrawal)", named=False)
e("V3.2", "changes with", "L369.s3 (FC68 (b), (c))", "S3", None, "added",
  "'every such candidate alike is ruled out … from the candidate's own answer there': the two-step argument from (A) and each candidate's own answer is not usable: FC68 (b)–(c) as claimed → not as claimed; FC68 (a) ('a failed answer stays failed', L369.s1–s2 FROZEN) holds under V3.2", named=False)
e("V3.2", "changes with", "D9.9 (K3) (FC71 (i))", "S3", None, "added",
  "K3's u⁺ from a failed prediction is a step above the step concluding ¬O; with Live through no step it is unusable unless j accepts ¬O itself (cases §C: T → F; with ¬O accepted T): FC71 (i), (i′) move", named=False)
e("V3.2", "changes with", "D18.1's loop K2 → Live → K2; I40 (FC69)", "S4; S3", None, "added",
  "DEP's Live loses its staged (K2) edge: the loop S101 read closes trivially; FC69's alternative reading has one fixed point (0 usable steps) where it had two (0 and 2): FC69 (I40's alternative) as claimed → not as claimed; FC32.new1 (b)'s cycle text changes", named=False)
e("V3.2", "changes with", "FC47 (b), FC53 (a) (arguments from a test's record; ConfCl with Applies)", "–", None, "added",
  "each is a two-step argument whose intermediate conclusion j does not accept: usable T → F (suite.V3.2)", named=False)

# ---- V3.3 D9.6 without the premise-alone clause -------------------------------------------------------------------------
e("V3.3", "constrains", "L397.s5", "FROZEN", "as V3.1",
  "computed", "X_j(ψ) is still the set of arguments usable by j that rule out ψ, but for a premise alone 'usable by j' reads nothing of j: X_j0(design ∧ PM) = X_j(design ∧ PM) for j0 who accepts nothing and j who accepts ¬PM (cases §C)")
e("V3.3", "changes with", "L393.n2", "S3", "'a claim j has never taken up is not live for j'; the varied D9.6 contradicts it",
  "computed", "FC72.new1 (a) as claimed → not as claimed: j0 never took ¬PM up and ¬PM alone is usable by j0 and rules out design ∧ PM")
e("V3.3", "moves", "(Suff)/(Nec) defeat sets; Prob_j assessor-independent", "S4; FROZEN", "bare claims rule out with no chooser, against S28",
  "computed", "FC72 (f): usable F → T, |X_j0| 0 → 1; ψ = r ∧ (r → ¬Expl(ℰ)) alone, j0 accepts nothing: an argument not using (E) rules out Expl(ℰ) F → T (a bare ¬Expl(ℰ) stays blocked by D9.7); worlds.args 2,621 usabilities F → T, 703 Out_j F → T. What rules out is then the same for every assessor, so D10.1's problems and D16.XV's defeat sets no longer depend on j for premises alone")
e("V3.3", "changes with", "FC72.new1 (c) (S27 with S28 and Q23)", "–", None, "added",
  "'for j0 (accepts nothing)': ruled out F → T; the conflict and the ruling out coincide with no chooser: FC72.new1 (c) as claimed → not as claimed (suite.V3.3)", named=False)

# ---- V3.4 D13.3 ExplUse :⟺ UsesClaim ∧ Acc(ℰ) ----------------------------------------------------------------------------
e("V3.4", "blocks", "L403.s3", "FROZEN", "'A system may understand a theory in error': a use in error can no longer prepare explanatory use",
  "computed", "FC90.new1 (a) as claimed → not as claimed (both CT readings): Build for the reversed calculation used in error T → F; worked cases: Build T → F exactly on the 5 with Acc F; worlds.cands: Build moves on 16,267 of 17,280 (every Acc-F candidate)")
e("V3.4", "moves", "Dec(t), via CT (D12.2) and Build", "S2", "transports constructed only through uses-in-error become Dec; Expl = Acc ∧ ¬Dec shrinks on that class",
  "contradicted under D12.2 as written; computed only under S108-3-I2",
  "D12.2's CT reads Prepares (t held at an output of a trace), not ExplUse (the program's DEP: CT → h, Prepares, BindingConstruction): on the reply's case (ℰ_rev claimed on C1, judged on C_id) Con T, Dec F, Account ∧ ¬Dec(t) on C_id T both ways; 0 Dec moves on the worked cases, the scripts, the generated candidates. With CT reading ExplUse (S108-3-I2): the reply's case T → F; worked cases 'Con-explu' Dec moves 5 (Acc F; Account ∧ ¬Dec(t) unmoved, since with its own claim Con ⇔ Acc); worlds.cands 'Con-explu (widest)': Account ∧ ¬Dec(t) T → F on 122 (Acc on C, not on the widest contract); worlds.chains under T′: Dec F → T 546 held, and T → F 92 (below)",
  settle="whether 'the construction trace' of D12.2 (L197) is Build's subhistory with all Build's conjuncts (S108-3-I2) or t held at an output of a trace (D12.2 as written): a reading of L197 and D18.1's sentence 'Con asks for a construction trace, which is what Build's subhistory is'")
e("V3.4", "constrains", "L526.s11 ('Build depends on histories, Ownership and (E)')", "S4", "ExplUse must keep reading the claim 'Acc(ℰ)'; it does, conjoined with Acc",
  "computed", "DEP unchanged by V3.4 (ExplUse → UsesClaim, (E), Cand); FC32.new1 (d) (L526's dependences as paths) unmoved; under V3.4 Build depends on (E)'s value, not only on the claim's content (FC90.new1 (a))")
e("V3.4", "moves", "Origin (G), created explanation (EX)", "S3", None, "added",
  "Build is a conjunct of (G) (D13.6) and (G) of (EX): Build F wherever the claim used fails (E); (EX)'s own Account conjunct (L449) then repeats what Origin already asks where the claim used is (c, p_c, t_c, Γ_c)'s (FC90.new1 (a)'s statement)", named=False)
e("V3.4", "moves", "Sel via D12.1's exclusion (under S108-3-I2)", "S2", None, "added",
  "worlds.chains, T′: 92 chains with Dec T → F at a held output: an earlier trace whose output uses a claim failing (E) no longer constructs, its occurrence is no longer represented, and D12.1's exclusion of a later selection lifts (n = 2: held [1, 1], trace [1, 0], Sel's conditions [0, 1], ExplUse [0, 0]); under U, 124 chains left with no fixed point", named=False)

# ---- V3.5–V3.8: filled below after the suites (s108_s3_edges_rest) ----------------------------------------------------------
try:
    from s108_s3_edges_rest import add_rest
    add_rest(e)
except ImportError:
    pass


def md_table(rows):
    out = []
    cur = None
    for r in rows:
        if r["variant"] != cur:
            cur = r["variant"]
            out.append("\n### %s\n\n| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |\n|---|---|---|---|---|" % cur)
        why = (r["reply_why"] or "–")
        why = why if len(why) <= 110 else why[:107] + "…"
        ev = r["evidence"] + ((" — settle: " + r["what_would_settle"]) if r["what_would_settle"] else "")
        st = "**%s**" % r["standing"] if r["standing_class"] in ("added", "contradicted") else r["standing"]
        out.append("| %s | %s [%s] | %s | %s | %s |" % (r["kind"], r["item"], r["mark"], why.replace("|", "\\|"), st, ev.replace("|", "\\|")))
    return "\n".join(out)


def main():
    jout, mout = sys.argv[1:3]
    counts = {}
    for r in E:
        counts[r["standing_class"]] = counts.get(r["standing_class"], 0) + 1
    with open(jout, "w", encoding="utf-8") as f:
        json.dump(dict(section=3, status="complete", note="rule 5 of the reading rule; standing per edge; nothing ruled; nothing changes the theory (rule 11)",
                       counts=counts, edges=E), f, ensure_ascii=False, indent=1)
    with open(mout, "w", encoding="utf-8") as f:
        f.write(md_table(E) + "\n\n### Edge counts\n\n%d rows in the JSON, %d named by the reply (all 22 of the tabulation's rows for section 3) and %d added: "
                "computed %d, computed in part (a part contradicted or not settled, named in the row) %d, contradicted %d, not settled by computation %d, added %d.\n"
                % (len(E), sum(r["named_by_reply"] for r in E), counts.get("added", 0), counts.get("computed", 0), counts.get("computed in part", 0),
                   counts.get("contradicted", 0), counts.get("not settled by computation", 0), counts.get("added", 0)))
    print(counts, len(E))


if __name__ == "__main__":
    main()
