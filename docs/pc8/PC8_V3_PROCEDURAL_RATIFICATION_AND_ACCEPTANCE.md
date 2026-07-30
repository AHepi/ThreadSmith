# PC8 V3 Procedural Ratification and Conditional Acceptance

## 1. Record class and non-authority boundary

Record date: `2026-07-30`.

This file is a
`procedural_ratification_and_acceptance_record`. It is non-normative,
non-dispatchable, and not self-authenticating. It creates no semantic rule,
specified criterion, fixture, relation, discriminator, preimage, diagnostic,
registry routing change, implementation behavior, qualification result, PC9
authority, or later-PC authority.

Before fresh verification, this file is only a prepared procedural candidate
that predeclares a conditional acceptance rule. It does not independently
verify the overlay or decide that its own condition is satisfied. A matching
fresh verification `PASS` is the final prepublication evidence that satisfies
the rule for the unchanged candidate. This record becomes operative only
after separately authorized publication and later consumer authentication of
the durable publication report.

Overall PC8 product acceptance remains false throughout this record's
preparation, verification, and publication projections because the executable
spine remains V2-bound and has not been qualified, verified, or independently
reviewed against V3.

## 2. Exact retained e181fa0f subject and seven-path identities

The content-addressed ratification subject is distinct from the later
five-path overlay:

```text
canonical_repository=AHepi/ThreadSmith
canonical_origin=https://github.com/AHepi/ThreadSmith.git
branch=main
remote_ref=refs/heads/main
commit=e181fa0f2892d98e149674704f185fc4efd3de77
tree=1787dadf448025d5b64d4ee53756a723b1387311
parent=ce9126b3a55660a46151bcfcfcbac75622f483d2
parent_tree=c3179302ac2399e9a22153597619989a149f93d9
parent_count=1
```

The exact parent-to-subject population is:

| Status | Path | Git blob | Bytes | LF lines | SHA-256 |
|---|---|---|---:|---:|---|
| `M` | `DECISIONS.md` | `195d99cc3189192e07e416de0d3c53541653666f` | 70,237 | 418 | `b8446febe7980716988693c1c44f75cf76636b1c7870fe464b5add13cfa3b6e1` |
| `M` | `IMPLEMENTATION_PLAN.md` | `341adc64dd879d9c09b9be99dc9950b9e3cfe07e` | 60,219 | 726 | `6202d7704edd2ec4cf0e453e0a553e887983f76f109f7d2da7de80136340a5d3` |
| `M` | `PROJECT_STATE.md` | `81a1d85936fd778b7ad23b89459d24f179f58c88` | 45,260 | 768 | `409c93c72651874227f6ebcaea0e7493ea56eb35ae0d1ac4df70898057bbdbdf` |
| `A` | `docs/pc7/PC7_IMPLEMENTATION_PUBLICATION_ATTESTATION_V2.md` | `ce853884394146a9cab2953c9a38c295d5cd94d7` | 7,989 | 171 | `33c157a5ed3f6dd3b005993381968f873a8e9bf2e7546f6e4f38eb86200ce94f` |
| `A` | `docs/pc8/PC8_AUTHORITY_REGISTRY_V3.json` | `4a26a84f278ff2b28ceba975847d598da8a181b7` | 25,591 | 600 | `63b437cae1fc8c1b3b5cd56d9ef44501178a8dcda129399c685efc8f953f9584` |
| `A` | `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V3.json` | `4e67874e5327b0252da9679b569884947e16f564` | 1,053,571 | 25,742 | `fa3c921a3e32ca9f2642813cdebd0cf8cb51c928958199851865e3f3d4660a04` |
| `A` | `docs/pc8/PC8_SPECIFIED_CONFORMANCE_CRITERIA_V3_ACCEPTANCE_AND_SUPERSESSION.md` | `d5099624b3c0b21e03057bbee7145daa6c366f0a` | 11,514 | 265 | `7b81341f3c90b5cc2a2fc87056824f464658da9d7b00bc2b3b2b68a7d6c14a08` |

Fresh physical presence of this commit on remote `main` is a current
observation. It does not reconstruct or authenticate the original acceptance
or push transaction.

## 3. Binding top decision and authenticated input identities

The binding decision is:

```text
TOP_DECISION=RETAIN_EXACT_E181FA0F_SUBJECT_AND_PROSPECTIVELY_RATIFY
QUARANTINE_ROUTE=RETAIN
RATIFICATION_AUTHORIZED=true
NORMATIVE_REOPENING_AUTHORIZED=false
V3_CRITERIA_REPAIR_AUTHORIZED=false
V2_QUALIFICATION_INHERITANCE=false
PUBLICATION_AUTHORIZED=false
PC9_MUTATION_AUTHORITY=false
PC10_OR_LATER_AUTHORITY=false
```

The complete controlling-input set has cardinality five:

| Input | Bytes | LF lines | SHA-256 | Role |
|---|---:|---:|---|---|
| `/workspace/scratch/3f06e5c3b586/control-inputs/THREADSMITH_TOP_ORCHESTRATOR_HANDOVER.md` | 32,008 | 614 | `9a74e07b51eed5ebdfa71c4ebff3e5000e97d8364c22a7d4072b6331e43c4369` | lifecycle and publication controls |
| `/workspace/ThreadSmith/evidence/pc8/PC8_V3_QUARANTINE_INDEPENDENT_REVIEW.md` | 33,438 | 563 | `7dc53b1d4fd5b1c7d9b162505e3d47eb030a3320b1f5aba29dc9db87839db1cd` | governing exact-subject independent review |
| `/workspace/ThreadSmith/PC9/handoffs/entry-authentication/output/THREADSMITH_PC9_ENTRY_AUTHENTICATION_AND_PC8_CLOSURE_REPORT.txt` | 21,008 | 420 | `fada97d04d4ab4c4e91e53b1de4188bf6d92fe3834eea4d7ab13cc64f4103ec3` | authenticated PC9 stop and PC8-closure gap |
| `/workspace/ThreadSmith/PC8/handoffs/v3-ratification-scope/output/THREADSMITH_PC8_V3_RATIFICATION_SCOPE_REPORT.md` | 56,239 | 1,077 | `dca04b40ac07cb9035cb3785c30254d4db84f8cec1cc193ed05b9e4d72b30ed5` | exact five-path substantive and procedural envelope |
| `/workspace/ThreadSmith/PC8/handoffs/v3-ratification-scope-correction/output/THREADSMITH_PC8_V3_RATIFICATION_SCOPE_PROCEDURAL_CORRECTION.md` | 42,188 | 783 | `a13376562231623f91d20c3f5b41ffc53f24f93dcbb1bae314f7424ce7ea12c9` | exact three-stage procedural substitution |

The correction prospectively supersedes only the original scope's four-stage
worker/report envelope. All original substantive, path, immutable,
historical-evidence, whitespace, structural-proof, candidate-manifest,
prospective-tree, verification, and publication obligations remain
controlling except for an exact corrected substitution.

## 4. Governing quarantine-review result and direct substantive-preservation basis

The governing quarantine review returns `PASS` for exact-subject review and
the route `SUBSTANTIVELY_VALID_PROCEDURALLY_RATIFIABLE`, with P0=0, P1=0,
P2=4, P3=2, `REFUTED=4`, `UNDERDETERMINED=0`, and `UNVERIFIED=10`. It does not
authenticate the missing historical chain and does not accept or publish this
overlay.

The controlling substantive proof is a direct deterministic structural
comparison of immutable V2 and V3 manifest bytes. Its operation rule is:

- recurse through common dictionary members;
- count each added or removed dictionary member as one structural operation;
- compare list members by common index and count each excess member as one
  addition or removal; and
- count each unequal scalar or type as one replacement.

That comparison closes exactly:

```text
STRUCTURAL_OPERATIONS_TOTAL=69
EVIDENCE_IDENTITY_MIRRORS=9
VERSION_MIRRORS=4
SUPERSESSION_METADATA_MIRRORS=56
CLASSIFICATION_CLOSED=true
REVERSE_OPERATIONS_RECREATE_V2=true
```

The V2 and V3 values are exactly equal for `candidate_status`,
`semantic_contract`, `rule_provenance`, `normative_choices`,
`resolved_sources`, `fixtures`, `relations`, `preimage_registry`,
`future_only`, `populations`, and `self_validation`. Registry V2 and V3 are
exactly equal for `normative_authority`, `authority_classification`, and
`procedural_alias_correction`. The proof reaches no Lock semantic, fixture,
relation, preimage, diagnostic, implementation, or PC9 authority.

## 5. Prospective historical-evidence supersession table

No unavailable body is reconstructed, approximated, or impersonated:

| Unavailable historical item | Preserved identity or locator | Prospective replacement | Exact effect |
|---|---|---|---|
| V3 author report | 17,977 bytes; SHA-256 `e9dc31bed5e5a0d92ef8538aa8f171d8e39456050098dc5889bec2dbfa52a0bb`; body and path unavailable | combined preparation report | `PROSPECTIVELY_REPLACED_NOT_RECONSTRUCTED`; the old body supplies no claim and the new report authenticates only the new overlay |
| Prior V3 independent review | 27,664 bytes; SHA-256 `86fc913dca7c2d196efe31cf9c736cab49401ccf7ed299ba97de65d7d5e77981`; body unavailable | governing quarantine review for the retained subject plus fresh overlay verification | `PROSPECTIVELY_REPLACED_NOT_RECONSTRUCTED`; the original review claim stays refuted and neither new report pretends to be it |
| V3 adjudication | 32,792 bytes; SHA-256 `39b9f4f3597a24ae947fcf8ef270e2e93d2990a76de296343c3ba8daa544e289`; named body unavailable | top retain/ratify decision, governing recomputation, original scope as corrected | `PROSPECTIVELY_REPLACED_NOT_RECONSTRUCTED`; no old rationale or body is supplied |
| Original V3 acceptance/publication operator report | obsolete locator preserved only in immutable historical criteria; body unavailable | new ratification publication report | `PROSPECTIVELY_REPLACED_NOT_RECONSTRUCTED`; the new report proves only the later five-path transaction and leaves the original push historically unproved |

The unavailable old PC7 publication report remains
`UNKNOWN_HISTORICAL_PROVENANCE`. The committed PC7 attestation retains its
already established future-intake role. If any unavailable exact historical
body appears before publication, this fixed evidence classification no longer
applies and the current gate must stop at `PC_BLOCKED`.

## 6. Immutable semantic, criteria, manifest, attestation, implementation, PC9, and unspecified-path boundary

The following authority identities are immutable:

| Path | Required SHA-256 |
|---|---|
| `docs/pc7/PC7_IMPLEMENTATION_PUBLICATION_ATTESTATION_V2.md` | `33c157a5ed3f6dd3b005993381968f873a8e9bf2e7546f6e4f38eb86200ce94f` |
| `docs/pc8/PC8_AUTHORITY_REGISTRY_V3.json` | `63b437cae1fc8c1b3b5cd56d9ef44501178a8dcda129399c685efc8f953f9584` |
| `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V3.json` | `fa3c921a3e32ca9f2642813cdebd0cf8cb51c928958199851865e3f3d4660a04` |
| `docs/pc8/PC8_SPECIFIED_CONFORMANCE_CRITERIA_V3_ACCEPTANCE_AND_SUPERSESSION.md` | `7b81341f3c90b5cc2a2fc87056824f464658da9d7b00bc2b3b2b68a7d6c14a08` |
| `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | `bd44aa9d43c6b6abf354f0ca556a66fbab97a06b3c24f21394ffe7769e3875bc` |
| `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | `a41990db0e2263a94356b2d87783e8f484d464e3f503200255aa0e81a3072c73` |
| `docs/pc8/PC8_SEMANTIC_FREEZE.md` | `c23f846c3dc7e795551f9fc2fbd0e65b2ba5bbc91eec269a5dda8490e231a0b1` |
| `docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json` | `b442f1acb4a7eb316ed9d61da02af3c1e5c60c34f55cf6eefefa751339d0a2c6` |
| `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V2.json` | `314e1cd73f23c07067e167d37e84782c7a301b13b4c6458d62a37d0423c4482a` |

The V2-bound executable-spine identities remain:

| Path | Required SHA-256 |
|---|---|
| `conformance/pc8/lock/build_executable_fixture_plan.py` | `1f09749f8290eb85f09f25d35c1d51c0bf3079b9f10aa551f5b1b4aadb36ec35` |
| `conformance/pc8/lock/executable_fixture_plan.json` | `f95b8feb6d6e012b76239a974eb39f709a50f7ac98a2b6dddddac01e52d1a0f6` |
| `crates/threadsmith-compiler/tests/support/pc8_fixture_interpreter.rs` | `5cca941058bb2147bff198a50b3608b82b7eadee44f82fc0c25cca8ed4e94916` |
| `crates/threadsmith-compiler/tests/pc8_lock.rs` | `5c006a901951562d05f463d93510e09bd8539aa4b803c46438c9000c87c9c0fb` |

Critical PC9 identities remain:

| Path | Required SHA-256 |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3_EXPAND_SEMANTICS_ERRATUM.md` | `565b2e6ae07637a3c973881ca0da94b3086bb7b1e23219e4e25d994efcf48765` |
| `docs/pc9/PC9_SCOPE_RECONCILIATION.md` | `b8e809958b43e932b7c53fb039f672ac0d29bb4eaa61785b06a31c36e3d70e7e` |
| `docs/pc9/PC9_SEMANTIC_FREEZE.md` | `9c6f5a631e92c5c3fbc6711a516c9e297df5a20b9a33f71cf71c7c1072892ecc` |
| `docs/pc9/PC9_EXPAND_SPECIFIED_CONFORMANCE_MANIFEST.json` | `256af0a46b035b0054a09e518db2d674a97c809b183901a5c8173ee0f98cef88` |
| `docs/pc9/PC9_AUTHORITY_REGISTRY_V1.json` | `d2e96358d49d97e40ab20c2783750af1115b205900529e5c22f167f080f526c7` |
| `docs/pc9/PC9_ERRATUM_ACCEPTANCE_AND_FREEZE_VERIFICATION.md` | `a640170ba4c185a7a02338696b2202536dc8fabfa72723f8588f49d3291c268b` |

All other existing files, all pre-existing bytes in the three append-only
files, every production/conformance/test/Cargo path, every PC9
implementation/conformance/test path, and every unspecified path are
immutable. Set equality of the candidate diff with the five-path overlay is
the global unspecified-path proof.

## 7. PC8-V3-IR-005 whitespace treatment

The three two-space Markdown hard-break suffixes at lines 3, 4, and 5 of the
PC7 attestation are historical bytes in blob
`ce853884394146a9cab2953c9a38c295d5cd94d7` and SHA-256
`33c157a5ed3f6dd3b005993381968f873a8e9bf2e7546f6e4f38eb86200ce94f`.
They remain byte-identical. This overlay does not clean, normalize, or copy
them.

Quality is measured only on the new five-path delta:

```text
git diff --check e181fa0f2892d98e149674704f185fc4efd3de77 -- DECISIONS.md IMPLEMENTATION_PLAN.md PROJECT_STATE.md docs/pc8/PC8_V3_PROCEDURAL_RATIFICATION_AND_ACCEPTANCE.md docs/pc8/PC8_V3_PROCEDURAL_RATIFICATION_REGISTRY_SUPPLEMENT_V1.json
```

The required result is exit zero and no output.

## 8. PC8-V3-IR-006 normalization treatment

The historical normalized SHA-256
`646c8d9c41f8ed88f1f63ce1e8534a23659188614fc1e0865cef520bf1c222e9`
has no committed projection or serialization recipe. It remains
`UNVERIFIED`, non-controlling history. This record does not invent, infer, or
search for a normalization preimage.

Only the direct `69 = 9 + 4 + 56` structural proof in Section 4 controls
substantive preservation. That proof is independently reproducible from the
immutable V2/V3 JSON bytes and is sufficient without the historical
normalization assertion.

## 9. Exact five-path overlay and per-path obligations

The ordered overlay has cardinality five and no sixth path:

| Status | Repository path | Obligation |
|---|---|---|
| `M` | `DECISIONS.md` | `PC8-V3-OVERLAY-001`: exact baseline blob plus the twelve `PC8-V3-RAT-001..012` procedural decisions |
| `M` | `IMPLEMENTATION_PLAN.md` | `PC8-V3-OVERLAY-002`: exact baseline blob plus the corrected three-stage tranche, restart vocabulary, full projection, predicates, and sole successor gate |
| `M` | `PROJECT_STATE.md` | `PC8-V3-OVERLAY-003`: exact baseline blob plus the current preparation state, conditional projection, and six finding dispositions |
| `A` | `docs/pc8/PC8_V3_PROCEDURAL_RATIFICATION_AND_ACCEPTANCE.md` | `PC8-V3-OVERLAY-004`: this twelve-section human-auditable record |
| `A` | `docs/pc8/PC8_V3_PROCEDURAL_RATIFICATION_REGISTRY_SUPPLEMENT_V1.json` | `PC8-V3-OVERLAY-005`: strict machine-readable procedural supplement |

The JSON supplement does not become a dispatch input, add normative
authority, change registry V3 routing, change the V3 manifest, increment a
supersession ordinal, assign qualification, or retroactively satisfy the
missing original operator condition. The three durable-state files are
projections of the supplement. A mismatch among representations is a blocking
candidate defect.

## 10. Preparation, verification, and publication state transitions

The only stages are `PREPARATION`, `INDEPENDENT_VERIFICATION`, and
`AUTHORIZED_PUBLICATION`; `AUTONOMOUS_RETRY=false` for each.

| Field | After combined preparation | After independent verification `PASS` / publication ready | After authorized ratification publication |
|---|---|---|---|
| `PC8_V3_SUBJECT_RETAINED` | `true` | `true` | `true` |
| `PC8_V3_SUBJECT_BYTES_ALREADY_ON_REMOTE_MAIN` | `true` | `true` | `true` |
| `PC8_V3_RATIFICATION_PREPARED` | `true` | `true` | `true` |
| `PC8_V3_RATIFICATION_INDEPENDENTLY_VERIFIED` | `false` | `true` | `true` |
| `PC8_V3_RATIFICATION_ACCEPTED` | `false` | `true` | `true` |
| `PC8_V3_RATIFICATION_PUBLISHED` | `false` | `false` | `true` |
| `PC8_V3_RATIFICATION_OPERATIVE` | `false` | `false` | `true` |
| `PC8_SPECIFIED_CONFORMANCE_V2_CURRENT` | `true` | `true` | `false` |
| `PC8_SPECIFIED_CONFORMANCE_V3_REVIEWED` | `true` | `true` | `true` |
| `PC8_SPECIFIED_CONFORMANCE_V3_ACCEPTED` | `false` | `true` | `true` |
| `PC8_SPECIFIED_CONFORMANCE_V3_PUBLISHED` | `false` | `false` | `true` |
| `PC8_SPECIFIED_CONFORMANCE_V3_CURRENT` | `false` | `false` | `true` |
| `POST_FREEZE_PC8_SPECIFIED_CRITERIA_SUPERSESSIONS` | `2` | `2` | `2` |
| `POST_FREEZE_PC8_LOCK_NORMATIVE_SUPERSESSIONS` | `0` | `0` | `0` |
| `PC8_V2_PRODUCT_ACCEPTANCE_HISTORICAL` | `true` | `true` | `true` |
| `PC8_ACCEPTED` | `false` | `false` | `false` |
| `PC8_EXECUTABLE_SPINE_BOUND_TO_V3` | `false` | `false` | `false` |
| `PC8_REQUALIFIED_AGAINST_V3` | `false` | `false` | `false` |
| `PC8_IMPLEMENTATION_VERIFIED_AGAINST_V3` | `false` | `false` | `false` |
| `PC8_EXECUTABLE_SPINE_INDEPENDENTLY_REVIEWED_AGAINST_V3` | `false` | `false` | `false` |
| `V2_QUALIFICATION_INHERITED_BY_V3` | `false` | `false` | `false` |
| `OPEN_PC8_V3_RATIFICATION_FINDINGS` | `6` | `6` with prospective dispositions not yet operative | `0` with all six historical dispositions retained |
| `PC9_SEMANTICS_ACCEPTED` | `true` | `true` | `true` |
| `PC9_ACCEPTED` | `false` | `false` | `false` |
| `PC9_MUTATION_AUTHORIZED` | `false` | `false` | `false` |
| `PC10_OR_LATER_AUTHORIZED` | `false` | `false` | `false` |
| `PUBLICATION_AUTHORIZED` | `false` | `false` | `false` after the one-shot token is consumed |
| `NEXT_BOUNDED_TASK` | fresh independent verification of the exact five-path overlay | mandatory top checkpoint and request one-shot publication authorization for the exact verified tree | `PC8-V3-EXECUTABLE-SPINE-IMPACT-SCOPE-001` |

Only the preparation column is current. All six quarantine findings remain
open with prospective dispositions only. The post-publication dispositions
are, in finding order:

```text
PC8-V3-IR-001=CLOSED_BY_PROSPECTIVE_REPLACEMENT
PC8-V3-IR-002=CLOSED_BY_PROSPECTIVE_REPLACEMENT
PC8-V3-IR-003=CLOSED_BY_PROSPECTIVE_PROCEDURAL_SUPERSESSION
PC8-V3-IR-004=CLOSED_BY_NEW_PUBLICATION_EVIDENCE
PC8-V3-IR-005=DISPOSED_AS_PRESERVED_NONBLOCKING_HISTORY
PC8-V3-IR-006=DISPOSED_AS_UNVERIFIED_NONCONTROLLING_HISTORY
```

## 11. External evidence and restart envelope

The candidate closure locations are:

| Artifact | Exact path |
|---|---|
| Candidate root | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-and-acceptance/candidate` |
| Overlay root | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-and-acceptance/candidate/overlay` |
| Manifest | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-and-acceptance/candidate/THREADSMITH_PC8_V3_PROCEDURAL_RATIFICATION_AND_ACCEPTANCE_CANDIDATE_MANIFEST.json` |
| Checksum closure | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-and-acceptance/candidate/THREADSMITH_PC8_V3_PROCEDURAL_RATIFICATION_AND_ACCEPTANCE_CANDIDATE_SHA256SUMS.txt` |

The external report population has cardinality three:

| Stage | Exact report path |
|---|---|
| Combined preparation | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-and-acceptance/output/THREADSMITH_PC8_V3_PROCEDURAL_RATIFICATION_AND_ACCEPTANCE_REPORT.md` |
| Independent verification | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-verification/output/THREADSMITH_PC8_V3_PROCEDURAL_RATIFICATION_VERIFICATION_REPORT.md` |
| Authorized publication | `/workspace/ThreadSmith/PC8/handoffs/v3-procedural-ratification-publication/output/THREADSMITH_PC8_V3_PROCEDURAL_RATIFICATION_PUBLICATION_REPORT.md` |

The preparation report binds the five inputs, manifest, checksum closure,
five bundled files, and tuple `C`. The verification report additionally
rehashes the preparation report and independently rebinds `C`. The publication
report additionally rehashes the verification report and exact one-shot
token. No report embeds or guesses its own SHA-256.

The complete restart vocabulary is:

```text
AUTHOR_OVERLAY
INDEPENDENT_VERIFICATION
TOP_PUBLICATION_AUTHORIZATION
PUBLICATION_PREFLIGHT
REMOTE_FAST_FORWARD
PUBLICATION_REPORT_FINALIZATION
NONE
```

Preparation `PASS` stops at `INDEPENDENT_VERIFICATION`. Verification `PASS`
stops at `TOP_PUBLICATION_AUTHORIZATION`. Publication records `NONE` only
after one-commit, normal non-force remote convergence, repository closure, and
durable report finalization. No stage retries automatically.

## 12. Conditional acceptance result and sole post-publication gate

Tuple `C` is the exact preparation tuple consisting of the baseline commit and
tree; ordered statuses `M,M,M,A,A`; each candidate file's SHA-256, Git blob,
bytes, LF count, and bundle identity; manifest bytes and SHA-256; checksum
closure bytes and SHA-256; and the one prospective tree yielded equally by
two separately initialized preparation indexes. Those same-tree identities
and the prospective tree are self-excluded from repository files and are
bound only after all candidate bytes exist by external closure evidence.

`CONDITIONAL_PROCEDURAL_ACCEPTANCE(C)` is satisfied if and only if:

1. the fresh independent verification report exists at its exact required
   path;
2. that report rehashes all five controlling inputs and the combined
   preparation report;
3. it records `DISPOSITION=PASS`;
4. it independently recomputes every identity in `C`;
5. it proves the overlay, manifest, checksum closure, and bundle are unchanged
   from `C`;
6. it independently constructs the same prospective tree bound by `C`;
7. every substantive, immutable-boundary, quality, structural-proof, state,
   and no-unresolved-choice verification predicate passes; and
8. it records
   `FIRST_UNFINISHED_OPERATION=TOP_PUBLICATION_AUTHORIZATION`.

The current preparation result is:

```text
CONDITIONAL_PROCEDURAL_ACCEPTANCE_STATUS=PENDING
PC8_V3_RATIFICATION_PREPARED=true
PC8_V3_RATIFICATION_INDEPENDENTLY_VERIFIED=false
PC8_V3_RATIFICATION_ACCEPTED=false
PC8_V3_RATIFICATION_PUBLISHED=false
PC8_V3_RATIFICATION_OPERATIVE=false
PC8_ACCEPTED=false
PUBLICATION_AUTHORIZED=false
FIRST_UNFINISHED_OPERATION=INDEPENDENT_VERIFICATION
```

A matching verification `PASS` satisfies the predeclared condition by
operation of this record; the verifier supplies evidence rather than
acceptance authorship. A mismatch or non-PASS result leaves the condition
unsatisfied. Even after ratification publication, overall
`PC8_ACCEPTED=false`.

After operative publication, the sole next gate is:

```text
GATE_ID=PC8-V3-EXECUTABLE-SPINE-IMPACT-SCOPE-001
ROLE=fresh read-only PC8 V3 executable-spine impact and exact-scope worker
MUTATION_ALLOWLIST=NONE
```

That gate may scope only the V3 executable-spine impact. It may not repair,
build, qualify, review, accept, publish, open PC9, or begin PC10.
