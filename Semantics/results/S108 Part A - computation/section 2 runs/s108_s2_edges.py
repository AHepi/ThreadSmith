# Builds the section 2 edges JSON and the md table (scratch tool; the JSON is the deliverable).
import json
import sys

OUT_JSON = "/home/user/ThreadSmith/Semantics/results/S108 Part A - section 2 - variants computed.json"

C, X, N = "computed", "contradicted", "not settled by computation"

E = []


def e(eid, variant, kind, item, mark, named, standing, shows, settle="", note=""):
    E.append(dict(id=eid, variant=variant, kind=kind, item=item, template_mark=mark, named_by_reply=named,
                  standing=standing, what_shows_it=shows, what_would_settle_it=settle, note=note))


# ---- edges the reply names (tabulation §4, rows for V2.1-V2.8, and its prose edge) ----
e("R1", "V2.1", "moves", "Dependence (D6.5), a conjunct of (E)", "S2", True, C,
  "Dep F→T on 57 / 74 / 8 generated candidates (single / value maps / MID proper), none T→F; the reply's case ¬Acc → Acc",
  note="the reply's gloss 'commitments that do no work (L313) become accounts' holds of 49 of the 57; 8 keep a commitment doing work for (F1)/(F2) while no block carries the contrast (§5)")
e("R2", "V2.1", "changes with", "D7.2 routes (S), L289", "FROZEN", True, C,
  "∅ ∈ S for 63 generated candidates under V2.1, 0 off; L299.s1 realized by 20 off and 20 under V2.1; L307's S by 17 and 17; L309's finite realization S = {{a}} under both")
e("R3", "V2.1", "constrains", "L275.n1", "S2", True, "SUITE_R3",
  "")
e("R4", "V2.2", "blocks", "L311.s2 ('(B) records the collective contribution')", "FROZEN", True, N,
  "finite part computed: under V2.2 every route has a critical singleton (0 of 1,297 routes without one); so an infinitary Γ in which no singleton is critical in any route has S = ∅ and (B) records nothing (argument, two lines, §5)",
  settle="a computation of S over an infinite Γ (the program enumerates a finite powerset); or the owner reading L311 as a claim about its finite truncations")
e("R5", "V2.2", "constrains", "L299.s1 ('a block may be critical while no singleton in it is')", "FROZEN", True, X,
  "'constrains' computed (realizations 20 → 1); 'such a candidate now fails (E)' contradicted: under V2.2 one generated candidate has S = {{k0,k1},{k0,k2},{k0,k1,k2}}, Γ meets (E), block {k1,k2} critical in Γ, no singleton of it critical (the critical singleton k0 lies outside the block)")
e("R6", "V2.2", "changes with", "D10.4 / D10.6 (problems; easy to vary; solved)", "FROZEN / S2", True, X,
  "V2.2 moves no pair's conflict pairs, rivals or kind (0 of 3,835); Prob_j (D10.1) reads Riv and NotOut, not the value of Acc; so no problem is added or removed")
e("R7", "V2.3", "blocks", "L329.s3 (identification, (I1)) and E2; L331.s2", "FROZEN (L329.s3); S2 (E2, L331.s2)", True, "SUITE_R7",
  "'no candidate meets (E) on a contract {1}×B' computed: 168 → 0 of 1,953 generated; E_rev and E_fwd on C_id T→F",
  settle="for L331.s2: the two balances built as a question on {1}×B with a candidate (the program computes their kernel, FC59, FC60, not (E)), or a reading of 'account' there")
e("R8", "V2.3", "changes with", "D3.3 (S1: Ident, identification contracts)", "S1", True, N,
  "V2.3 leaves Ident(p) as it was (D3.3 reads no Dependence; FC28's Ident part under V2.3, §6); the reply's 'would need contracts that vary only the boundary re-read' is a proposal for D3.3",
  settle="section 1's computation of V1.4 (Ident with a ≠ 1) read together with V2.3 (tabulation §7, same axis)")
e("R9", "V2.3", "constrains", "L253.s1 (the query held fixed)", "FROZEN", True, C,
  "the switch reads only the pair's edit in NC2's pair loop; no query changes in any run")
e("R10", "V2.4", "blocks", "— (the owner's decision S45, with S44)", "—", True, N,
  "an owner's decision, not an item; V2.4 = round 3's (E) exactly (§2: the S106 printout's 10 MOVED cases move back)",
  settle="the owner's yes or no in the later step (S52)")
e("R11", "V2.4", "moves", "(E) itself; what Bearing reads (D9.10, S3)", "S2 / S3", True, "SUITE_R11",
  "(E): 11 worked cases, 972 / 776 / 301 generated accounts T→F")
e("R12", "V2.4", "changes with", "D16.XV (S4), (Suff) / (Nec) at L536 / L538", "S4", True, "SUITE_R12",
  "Expl shrinks: 22 (case, history) T→F; 1,944 generated")
e("R13", "V2.5", "constrains", "L195.s1 ('a finite history H ⊆ C of edit–boundary pairs actually encountered')", "FROZEN", True, C,
  "under V2.5 Sel accepts H = ∅: 'its pairs having occurred' vacuous, fidelity on ∅ is Hom(τ) (I18); FC77 part 3's 'other choice' is the variant's reading")
e("R14", "V2.5", "blocks (in effect)", "L211.s3 ('A declared transport does not make an occurrence represent anything')", "S2", True, C,
  "FC30.new1 (e) under V2.5: the link nobody tried and nobody worked out is Sel, its fixed point {o1: Sel}, so its holding represents (D12.5); as an effect: the transport is no longer declared, so L211.s3 still holds formally")
e("R15", "V2.5", "moves", "Dec (D12.3), hence Expl := Acc ∧ ¬Dec and (Suff) L536", "S2 / S4", True, C,
  "Account ∧ ¬Dec(t) F→T on the history 'nothing tried' for every account: 28 of 28 worked cases, 1,027 / 847 / 310 generated; no other history moves")
e("R16", "V2.6", "blocks", "L315.s1 (rivals: conflict 'in C or outside it'), L317.s6 (kind ii)", "FROZEN", True, C,
  "310 of 310 kind-ii pairs lose every conflict pair, rivalry and kind; FC72.new2 (b): tilt and myth on the Greeks' C not rivals (§7)")
e("R17", "V2.6", "moves", "nothing in (E); problems, ETV (D10.4) and the (Nec) attack route through easy-to-vary change", "—", True, "SUITE_R17",
  "0 Acc changes in every population; no kind ii remains, so ETV_j holds of no candidate")
e("R18", "V2.7", "blocks (in effect)", "L315.s12 ('the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion')", "S2", True, C,
  "the reply's case: ConfCl T→F; 410 of 1,822 generated (candidate, pair) lose ConfCl, all by the second disjunct alone",
  note="where the candidate's answer is itself the motion χ excludes (FC53 (b), L315.s16's pendulum) the conflict stays under V2.7 (suite, §6); S27's words are about what the explanation describes, not only its answer")
e("R19", "V2.7", "constrains", "D8.4 (Allow_χ, Applies)", "FROZEN", True, C,
  "the switch touches only D8.5's second disjunct; Allow_χ and Applies are read as before in every run")
e("R20", "V2.7", "changes with", "D8.6 (ConfG_χ)", "FROZEN", True, "SUITE_R20",
  "'no longer feeds any ruling out of a single candidate': the program builds no argument from ConfCl or ConfG_χ",
  settle="an encoding of L315.s13–s14's argument whose premise is a computed ConfCl")
e("R21", "V2.8", "constrains", "D16.XV (S4): 'Acc ∉ Uses(α)'", "S4", True, N,
  "V2.8 not implemented: out of scope as written (tabulation §6). The committed printout's FC30.new1 (h) already computes both readings on one case: 'symbol False, instance True'",
  settle="section 4's computation of V4.4 (the same reading)")
e("R22", "V2.8", "moves", "(Suff)'s defeat set (L536)", "S4", True, N,
  "as R21", settle="section 4's computation of V4.4")
e("P1", "V2.1", "keeps", "L309.s1 (interference: the full candidate fails (E) although a subset meets it)", "FROZEN", True, C,
  "built (Γ = {a,b}, a: y = x, b: y = 0): S = {{a}}, full candidate (E) F under off and V2.1 (F1, F2, A fail); the reply left it unsettled")

# ---- edges the computation shows that the reply did not name ----
e("N1", "V2.1", "changes with", "D7.3 (B) critical block; L293 (B)'s definition", "FROZEN (D7.3)", False, C,
  "off: every route has a critical block (0 of 1,322 without; argument §5: the Lost witness is critical); V2.1: 120 of 1,450 routes have none (63 of them ∅)")
e("N2", "V2.1", "changes with", "L313.s2 (NoWork)", "S2", False, C,
  "V2.1 admits more than L313's case: 8 of 57 new accounts have a commitment that does work for (F1)/(F2) while none carries the contrast (smallest: Γ = {k0} on p0, the answer on p1 set by the background)")
e("N3", "V2.2", "blocks", "L307.s1 (redundant routes S = {{a},{b},{a,b}})", "FROZEN", False, C,
  "no candidate realizes that S under V2.2 (17 → 0; all 17 become {{a},{b}}); argument: every route has a critical singleton, and in {a,b} neither is")
e("N4", "V2.2", "blocks", "L313.n3 ('When Γ is infinite, a block of such commitments can still be critical')", "S2", False, N,
  "by the argument of R4: L311's candidate has S = ∅ under V2.2, so its example goes",
  settle="as R4")
e("N5", "V2.2", "changes with", "D7.3 (B): every route has a critical singleton", "FROZEN (D7.3)", False, C,
  "0 of 1,297 routes under V2.2 without a critical singleton (21 of 1,322 off)")
e("N6", "V2.3", "moves", "(E) on every contract whose contrasts all sit at pairs (1,b), not only on {1}×B", "S2 (D6.4)", False, C,
  "253 generated accounts T→F, of which 168 on contracts {1}×B′; the other 85 on contracts that hold an edit but carry their contrast only at boundary pairs")
e("N7", "V2.4", "moves", "E8 p_δ's identity candidate (K1's criticism question, FC107); R3-Q1's hand-turned vane; E_rev under τ′ (H only)", "S2 / S3", False, C,
  "all three T→F under V2.4 (§2); the reply named the myth's bearing, not these")
e("N8", "V2.4", "changes with", "D6.10 (tables) and the generators' E_enc", "S2", False, C,
  "972 of 1,027 generated accounts fail (E) under V2.4 (E_enc 864, lookup 102, random 6), each by a slot: after S106 most generated accounts have a component that pins the answer")
e("N9", "V2.5", "changes with", "D5.5 Hom(τ) (I18) and D6.7 (F2)", "S2", False, C,
  "Acc ⇒ (F2) ⇒ Hom(τ); with H = ∅ allowed, Hom(τ) ∧ Θ admits t ⇒ Sel(t;{t},id,∅); so on a holding with nothing tried Account ∧ ¬Dec(t) ⟺ Acc ∧ Θ admits t: ¬Dec(t) adds only Θ's admission (1,027 of 1,027)")
e("N10", "V2.6", "changes with", "D8.3 Riv (its ∃ over A_D × B_D)", "S2", False, C,
  "492 kind-i pairs keep kind i and lose their conflict pairs outside C; rivals then need a conflict in C")
e("N11", "V2.7", "changes with", "L317 'solved with no test' by an argument from a claim (D10.6)", "S2", False, N,
  "23 generated (candidate, pair) where the candidate meets (E) lose ConfCl (20 at a pair of C): the ground for that route to solving goes there",
  settle="an encoding of the argument from ConfCl (as R20); the program computes ConfCl, not the solving")
e("N12", "V2.1–V2.4", "independent of", "D8.2 Conf, D8.3 Riv, D10.2 kinds", "S2 / FROZEN", False, C,
  "0 of 3,835 pairs change conflict pairs, rivals or kind under each of V2.1–V2.4")
e("N13", "V2.5, V2.6, V2.7", "independent of", "(E) (D6.7)", "S2", False, C,
  "0 Acc changes in every population and case")


def main():
    suite = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
    for x in E:
        if x["standing"].startswith("SUITE_"):
            k = x["standing"][6:]
            st, add = suite.get(k, (None, None))
            if st is None:
                raise SystemExit("suite result missing for " + k)
            x["standing"] = st
            x["what_shows_it"] = (x["what_shows_it"] + "; " + add) if x["what_shows_it"] else add
    for x in suite.get("_new", []):
        E.append(x)
    counts = {}
    for x in E:
        key = ("named" if x["named_by_reply"] else "added") + " / " + x["standing"]
        counts[key] = counts.get(key, 0) + 1
    out = dict(section=2, source="results/S108 Part A - section 2 - variants computed.md",
               standings=("computed", "contradicted", "not settled by computation"), counts=counts, edges=E)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps(counts, ensure_ascii=False))
    for x in E:
        print("| %s | %s | %s | %s | %s | %s | %s |" % (x["id"], x["variant"], x["kind"], x["item"] + (" [%s]" % x["template_mark"] if x["template_mark"] not in ("—", "") else ""),
                                                      x["standing"], x["what_shows_it"] + ((" — note: " + x["note"]) if x["note"] else ""),
                                                      x["what_would_settle_it"] or "—"))


if __name__ == "__main__":
    main()
