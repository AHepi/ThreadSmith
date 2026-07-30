# PC7 Implementation Publication Attestation V2

Date: 2026-07-30  
Repository: `AHepi/ThreadSmith`  
Role: non-normative, non-dispatchable publication-provenance attestation  
Status: candidate pending independent review, acceptance, and publication

## 1. Purpose and authority boundary

This document provides durable, presently reproducible provenance for the
accepted PC7 Resolve publication subject. It supersedes the unavailable
external operator-report body only for future conformance intake. It does not
recreate that report, alter PC7 or PC8 semantics, qualify an implementation,
accept this attestation, or prove historical observations for which no
durable oracle remains.

The unavailable historical report identity remains:

| Field | Historical value |
|---|---|
| Path | `/workspace/ThreadSmith/PC7/handoffs/implementation-acceptance-publication/output/THREADSMITH_PC7_IMPLEMENTATION_ACCEPTANCE_PUBLICATION_AND_DURABLE_STATE_UPDATE.txt` |
| Bytes | `24,874` |
| Lines | `711` |
| SHA-256 | `7064a32177e39b8ee6dd5a39faca8e93c5511a03b9e7c7df8715b50e9ca79cce` |
| Exact body available | `false` |
| V3 intake dependency | `false` |

The hash above identifies missing historical evidence; it is not a source
from which the body can be reconstructed.

## 2. Reproducible PC7 publication object

The following Git facts are independently reproducible from retained
content-addressed objects:

| Field | Reproduced value |
|---|---|
| Commit | `54b8b2b380606428f0d41f33d5d32c985c18c7ea` |
| Tree | `0f578dcd1f9ac01ed01a32286020e11338f04f04` |
| Parent | `69861ccc8580b658b1365a42b1e7b45e8c0d6452` |
| Parent count | `1` |
| Subject | `Implement and accept PC7 Resolve` |
| Changed-path count | `10` |

The exact committed path inventory, in UTF-8 bytewise order, is:

| Order | Path |
|---:|---|
| 1 | `DECISIONS.md` |
| 2 | `IMPLEMENTATION_PLAN.md` |
| 3 | `PROJECT_STATE.md` |
| 4 | `conformance/pc7/resolve/build_executable_fixture_plan.py` |
| 5 | `conformance/pc7/resolve/executable_fixture_plan.json` |
| 6 | `crates/threadsmith-compiler/src/lib.rs` |
| 7 | `crates/threadsmith-compiler/src/resolve.rs` |
| 8 | `crates/threadsmith-compiler/tests/pc7_resolve.rs` |
| 9 | `crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs` |
| 10 | `docs/pc7/PC7_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md` |

## 3. Reproducible PC7 candidate identities

The six accepted candidate bodies are retained in the publication tree:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `conformance/pc7/resolve/build_executable_fixture_plan.py` | `107,538` | `02968be53c6403953fe3e7c691a3acd36eba0dc5c6c5ec6462a75e5c2201764b` |
| `conformance/pc7/resolve/executable_fixture_plan.json` | `34,460,681` | `4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d` |
| `crates/threadsmith-compiler/src/lib.rs` | `42,489` | `00e726435f9b8442da89992971ce18b382c881849401b57693c4c6554a6d9a87` |
| `crates/threadsmith-compiler/src/resolve.rs` | `84,642` | `bc9a8e8718702ffd9ef1077cf9c4da3c731f0faee27865bdb80405a535f9c2ca` |
| `crates/threadsmith-compiler/tests/pc7_resolve.rs` | `8,758` | `df7d77543102979f8fd02e991a547d9cd2e1ff339a4f753b7d475110d5e533f1` |
| `crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs` | `70,282` | `3efdbfe63ec403b737e05a0444956efe09e3d059d2a4b064a9622f65976fe326` |

These identities are observations of the accepted Git tree, not newly
promoted golden values.

## 4. Current public-main ancestry

A fresh query of `refs/heads/main` on the canonical remote returned:

```text
ce9126b3a55660a46151bcfcfcbac75622f483d2
```

The retained raw commit headers establish this exact single-parent chain:

| Order | Commit | Parent | Subject |
|---:|---|---|---|
| 1 | `54b8b2b380606428f0d41f33d5d32c985c18c7ea` | `69861ccc8580b658b1365a42b1e7b45e8c0d6452` | `Implement and accept PC7 Resolve` |
| 2 | `89fe4493a7642cffa76e731911bcabf225dacc7a` | `54b8b2b380606428f0d41f33d5d32c985c18c7ea` | `Accept and freeze PC8 Lock semantics` |
| 3 | `eb6f1e35d314f3c436402f122f4752e4ecc34073` | `89fe4493a7642cffa76e731911bcabf225dacc7a` | `Accept PC8 Lock specified-conformance criteria V2` |
| 4 | `630b664af272afaffb514b9dde8275cfc95357e9` | `eb6f1e35d314f3c436402f122f4752e4ecc34073` | `Implement and accept PC8 Lock` |
| 5 | `ce9126b3a55660a46151bcfcfcbac75622f483d2` | `630b664af272afaffb514b9dde8275cfc95357e9` | `Accept and freeze PC9 Expand semantics` |

Because Git commit identities bind their raw parent headers, the fresh public
tip and this retained chain establish that the accepted PC7 commit is in the
current public `main` ancestry. This is a present reproducible ancestry claim,
not a reconstruction of the original publication transaction.

## 5. Surviving durable-state records

The accepted publication tree contains
`docs/pc7/PC7_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md`. Current public
state retains the accepted PC7 semantic, specified-criteria,
implementation-boundary, qualification-result, and product-acceptance
records. Current `PROJECT_STATE.md` records `PC7_ACCEPTED=true` and retains
PC7 as the accepted predecessor of PC8 and PC9.

This attestation establishes that those records and their accepted Git
subject remain present. It does not use a state-file assertion as proof of an
unrecorded transport event.

## 6. Unknown historical provenance

The following observations are exactly `UNKNOWN_HISTORICAL_PROVENANCE`:

| Historical observation | Status |
|---|---|
| Exact original push stdout or transcript | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Original wall-clock ordering of the fresh-remote query and push | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Original local worktree cleanliness observation | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Original real-index cleanliness observation | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Immediate post-push local-main observation | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Immediate post-push cached `origin/main` observation | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Immediate post-push fresh-remote observation | `UNKNOWN_HISTORICAL_PROVENANCE` |
| Direct observation that no force option was supplied | `UNKNOWN_HISTORICAL_PROVENANCE` |

The surviving single-parent linear history is consistent with the accepted
normal-fast-forward procedure, but consistency is not promoted into direct
historical observation.

## 7. Conformance-intake classification

This attestation is procedural, non-normative, and non-dispatchable. Its
complete body may be authenticated as provenance before conformance
dispatch, but it controls no Resolve or Lock product observable. A missing,
substituted, size-mismatched, or hash-mismatched attestation must reject at
authority intake. The unavailable historical report must never be read or
treated as a required V3 body.

V3 changes only the retained provenance route. PC7 Resolve semantics, PC8
Lock semantics, all specified fixtures and relations, and all production
behavior remain unchanged.

## 8. Reproduction procedure

An independent reviewer can reproduce this attestation’s Git claims by
reading the raw commit object for `54b8b2b…`, enumerating its parent diff,
hashing the six candidate blobs, reading each raw header in the five-commit
chain, and freshly resolving canonical `refs/heads/main`. The reviewer must
derive the expected inventory from the commit diff and must not use this
document’s ordering as the source of truth.

Any mismatch in commit, tree, parent, subject, path inventory, candidate
identity, fresh public tip, or raw parent chain invalidates this candidate.
Any attempt to promote an unknown historical observation invalidates this
candidate.

## 9. Candidate disposition

```text
ATTESTATION_VERSION=2
NORMATIVE=false
DISPATCHABLE=false
HISTORICAL_REPORT_BODY_AVAILABLE=false
HISTORICAL_REPORT_REQUIRED_BY_V3=false
PRESENT_GIT_CLAIMS_REPRODUCIBLE=true
UNKNOWN_HISTORICAL_PROVENANCE_COUNT=8
PC7_SEMANTICS_CHANGED=false
PC8_SEMANTICS_CHANGED=false
STATUS=CANDIDATE_PENDING_INDEPENDENT_REVIEW_ACCEPTANCE_AND_PUBLICATION
```
