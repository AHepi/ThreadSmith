# PC8 Erratum Acceptance and Semantic-Freeze Verification

Verification date: 2026-07-28.

Status: exact PC8 Lock semantic and specified-conformance candidate accepted,
frozen, and documentation-only published. PC8 implementation has not started
and overall PC8 product acceptance remains false.

This repository record becomes operative only as part of the exact one-commit
publication described below. Commit, staged-tree, push, and final remote
identities are self-excluded from that same commit and are recorded in the
external operator report.

## 1. Authorized gate

This gate records acceptance of already reviewed semantics and specified
criteria. It does not repeat review, repair semantic content, construct
executable conformance, implement Lock, persist a physical Lockfile, qualify
code, accept PC8 overall, or begin Expand, PC9, Builder, runtime, providers,
installation, CLI, MCP, UI, Android, or any product surface.

The exact repository envelope is:

```text
DECISIONS.md
IMPLEMENTATION_PLAN.md
PROJECT_STATE.md
docs/pc8/PC8_AUTHORITY_REGISTRY_V1.json
docs/pc8/PC8_ERRATUM_ACCEPTANCE_AND_FREEZE_VERIFICATION.md
docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST.json
docs/pc8/PC8_SCOPE_RECONCILIATION.md
docs/pc8/PC8_SEMANTIC_FREEZE.md
docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md
```

No other repository path may differ from the accepted PC7 baseline.

## 2. Initial repository authentication

| Field | Verified value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| Initial commit | `54b8b2b380606428f0d41f33d5d32c985c18c7ea` |
| Initial tree | `0f578dcd1f9ac01ed01a32286020e11338f04f04` |
| Initial subject | `Implement and accept PC7 Resolve` |
| Initial local `main` | Required initial commit |
| Initial cached `origin/main` | Required initial commit |
| Initial fresh remote `main` | Required initial commit |
| Initial index | Empty |
| Initial tracked differences | Absent |
| Initial untracked inventory | Exactly the four reviewed PC8 candidate paths |

No fetch, merge, rebase, amend, reset, stash, tag, branch creation, pull
request, force option, or destructive cleanup is part of this gate.

## 3. Reviewed subject authentication

| Candidate path | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST.json` | 1040963 | 25487 | `72a680a44a6d49388f1e26bac46e7e59862a1e502a74a72c239a8c908bf03399` |
| `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | 34097 | 463 | `7468db3f8cf2a6ec4990fb2c0bf254309598552fc1dd99759f2c72c0dc5dc52f` |
| `docs/pc8/PC8_SEMANTIC_FREEZE.md` | 14757 | 257 | `14d71ab9f32d1cc52c68ce268462fe81c2c6952951491db4543a6fc380cae9b9` |
| `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | 25127 | 431 | `26b85cfae2b9b5fb9cbe2f1afcbc98949087b031a65209681ac8ac3da7774ae3` |

All four candidate files are UTF-8 without BOM, LF-only, have exactly one
final LF, contain no NUL, and have no trailing horizontal whitespace. The
standalone manifest strict-parses with duplicate-key rejection and is exactly
its deterministic two-space JSON serialization.

## 4. Governing independent evidence

The acceptance decision consumes the completed review; it does not repeat or
reinterpret it.

| Evidence | Bytes | Lines | SHA-256 | Role |
|---|---:|---:|---|---|
| Governing superseding independent review | 37745 | 975 | `87a5b71c241310ea6011201035f55493ee624c116a226fbb708f343b2d9a21ce` | Governing non-dispatchable evidence |
| Unchanged historical source review | 37749 | 975 | `3faa73b090ae377399a18cd6798e7f76c4ce037fa21edec1740888de260358c0` | Preserved historical evidence |
| Author-side remaining-finding repair report | 44192 | 1130 | `2414aab3998091c0821b1d52e628e4385805eb0c4eb386f4c3164b1f10782362` | Non-authoritative repair evidence |

The governing report path is:

```text
/workspace/ThreadSmith/PC8/handoffs/scope-reconciliation-semantic-freeze-re-review-repair-review/output/THREADSMITH_PC8_LOCK_SEMANTIC_REREVIEW_P2_01_REPAIR_INDEPENDENT_REVIEW_SUPERSEDING.txt
```

Machine comparison proves exactly four line replacements and no other change:

```text
line 603: PUBLIC_PC7_SOURCE_CONSTRUCTION=20/20 -> PUBLIC_PC7_SOURCE_CONSTRUCTION=PASS
line 651: EXACT_RESOLVED_SOURCE_PRESERVATION=20/20 -> EXACT_RESOLVED_SOURCE_PRESERVATION=PASS
line 952: PUBLIC_PC7_SOURCE_CONSTRUCTION=20/20 -> PUBLIC_PC7_SOURCE_CONSTRUCTION=PASS
line 954: EXACT_RESOLVED_SOURCE_PRESERVATION=20/20 -> EXACT_RESOLVED_SOURCE_PRESERVATION=PASS
```

The original report remains byte-identical. The correction is procedural
claim serialization only and changes no review computation, candidate byte,
finding, semantic conclusion, or evidence identity other than the superseding
report itself.

The governing disposition is:

```text
REREVIEW_P0=0
REREVIEW_P1=0
REREVIEW_P2=0
REREVIEW_P3=0
REFUTED=0
UNDERDETERMINED=0
UNVERIFIED=0
PC8_RR_P2_01_CLOSED=true
PUBLIC_PC7_SOURCE_CONSTRUCTION=PASS
EXACT_RESOLVED_SOURCE_PRESERVATION=PASS
FINAL_DISPOSITION=PASS
```

## 5. Accepted documents and immutable regions

| Accepted path | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST.json` | 1040963 | 25487 | `72a680a44a6d49388f1e26bac46e7e59862a1e502a74a72c239a8c908bf03399` |
| `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | 34394 | 473 | `a41990db0e2263a94356b2d87783e8f484d464e3f503200255aa0e81a3072c73` |
| `docs/pc8/PC8_SEMANTIC_FREEZE.md` | 15024 | 267 | `c23f846c3dc7e795551f9fc2fbd0e65b2ba5bbc91eec269a5dda8490e231a0b1` |
| `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | 25595 | 442 | `bd44aa9d43c6b6abf354f0ca556a66fbab97a06b3c24f21394ffe7769e3875bc` |

The standalone manifest retains its complete reviewed byte sequence:

```text
MANIFEST_REVIEWED_BYTES=1040963
MANIFEST_ACCEPTED_BYTES=1040963
MANIFEST_SHA256=72a680a44a6d49388f1e26bac46e7e59862a1e502a74a72c239a8c908bf03399
MANIFEST_WHOLE_FILE_BYTE_EQUAL=true
```

Its `candidate_status` and related self-validation status fields remain the
immutable historical state of the reviewed candidate. Procedural acceptance
is recorded by this verification, the authority registry, durable project
state, the publication commit, and external publication evidence.

The three Markdown documents change only pre-region procedural metadata and
post-region acceptance/status envelopes. Their reviewed substantive regions
are exactly preserved:

| Path | Reviewed start offset | Accepted start offset | Region bytes | Region SHA-256 | Byte equal |
|---|---:|---:|---:|---|---|
| `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | 436 | 498 | 32651 | `5e884174e982fcd4a5bfc15ef31458948d30941e99c95c41c0cf245e6a15d21c` | true |
| `docs/pc8/PC8_SEMANTIC_FREEZE.md` | 379 | 414 | 13633 | `71a46c1dd55c462bf580f095ef9bfc11664f594a22f85e21e6d34e4687eb3973` | true |
| `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | 299 | 394 | 23788 | `9b1b47824f4c4c0b69ab9a25349bf9b7266c1c36fd75f78bd10fee7fa8894f47` | true |

The boundaries are respectively:

```text
scope: [## 1. Authenticated baseline and authoring boundary,
        ## 16. Accepted reconciliation disposition)
freeze: [## 1. Bound baseline and authority,
         ## 13. Accepted freeze status)
erratum: [## Normative Section 1 — Authority, scope, and provenance,
          ## Normative Section 18 — Accepted disposition)
```

No Lock projection, canonical ordering, occurrence multiplicity, preimage
construction, emitted-byte construction, identity algorithm, source
construction, source preservation, schema, fixture, relation, discriminator,
registry, diagnostic, persistence boundary, non-authority boundary, or
future-only allocation changes.

## 6. Accepted specified-conformance closure

The accepted maturity is `specified`. It is not yet dispatchable, executable,
qualified, implementation-verified, or implementation-reviewed.

| Population | Accepted value |
|---|---:|
| Authority rows | 10 |
| Rule-provenance rows | 40 |
| `[S]` rules | 10 |
| `[C]` rules | 10 |
| `[N]` rules | 14 |
| `[D]` rules | 6 |
| Normative choices | 14 |
| Schemas | 16 |
| Resolved sources | 20 |
| Fixtures | 20 |
| Relations | 19 |
| Discriminators | 41 |
| Preimage registries | 4 |
| Preimage byte spans | 235 |
| Future-only rows | 4 |
| Schema mutations | 12 |

The governing review independently established 204 of 204 schema-consumer
admissions, 12 of 12 source admissions, exact mutation rejections, isolated
mechanisms, locators and reasons, 20 of 20 public-PC7 source constructions,
69 of 69 retained byte bindings, 20 of 20 fixture recomputations, complete
preimage and emitted stream equality, 20 of 20 PC7 structural round trips,
19 of 19 relation recomputations, and four gap-free, overlap-free preimage
registries covering all 235 byte spans.

The four future-only rows remain non-dispatchable at their declared activation
conditions: a current non-ASCII package name, a literal selected-name
proper-prefix pair, an accepted non-Core successful PC7 source, and the
physical PC8 Lockfile Persistence Adapter.

## 7. Authority registry

`docs/pc8/PC8_AUTHORITY_REGISTRY_V1.json` is 8,632 bytes, 228 lines, SHA-256
`969ce520453014ffd7a5d2cd997dd12a36948b7bfaafeb864cbd327e647e136b`.
It is strict duplicate-free JSON and exactly its deterministic two-space
serialization with one final LF.

The registry binds the accepted PC1-PC7 authority closure, reviewed and
accepted PC8 document identities, the exact standalone manifest, governing
superseding review, this exact acceptance-verification path, required commit
parent and subject, publication ref and mode, and the external publication
evidence path. External reports and procedural records are explicitly
non-dispatchable and do not become normative semantic authority.

## 8. Durable project-state transition

`DECISIONS.md`, `IMPLEMENTATION_PLAN.md`, and `PROJECT_STATE.md` record only
the accepted PC8 semantic/specification boundary and its next task. They do
not claim implementation, executable fixture dispatch, qualification,
physical persistence, or overall PC8 product acceptance.

The accepted transition is:

```text
PC8_RR_P2_01_CLOSED=true
PC8_SEMANTICS_ACCEPTED=true
PC8_SPECIFIED_CONFORMANCE_ACCEPTED=true
PC8_SEMANTIC_FREEZE_COMPLETE=true
PC8_SEMANTICS_FROZEN=true
PC8_DOCUMENTATION_PUBLISHED=true
PC8_IMPLEMENTATION_STARTED=false
PC8_ACCEPTED=false
FIXTURE_MATURITY=specified
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
PUSH_COMPLETE=true
FINAL_DISPOSITION=PASS
```

## 9. Staged-tree and publication evidence

Before commit, the operator must reauthenticate all source identities, verify
the exact nine-path diff allowlist, prove no unstaged difference remains,
strict-validate both JSON files, re-run every immutable-region equality
check, and write exactly those nine paths to a temporary index.

The staged tree must be computed independently from that temporary index and
then reproduced by the real index after staging the same nine paths. The
published commit must have exactly:

```text
Parent=54b8b2b380606428f0d41f33d5d32c985c18c7ea
Branch=main
Ref=refs/heads/main
Subject=Accept and freeze PC8 Lock semantics
Mode=normal non-force fast-forward
```

The exact staged-tree SHA-1, commit SHA-1, final tree SHA-1, push result,
local `main`, cached `origin/main`, fresh remote `main`, clean index and
worktree, and external report identity cannot be embedded self-referentially
in this same commit. They are recorded at:

```text
/workspace/ThreadSmith/PC8/handoffs/scope-reconciliation-semantic-freeze-acceptance/output/THREADSMITH_PC8_LOCK_SEMANTIC_AND_SPECIFIED_CONFORMANCE_ACCEPTANCE_FREEZE_AND_PUBLICATION.txt
```

Publication is valid only if that record proves the published tree is exactly
the independently verified staged tree and all three final `main` identities
converge.

## 10. Result and next bounded task

This acceptance freezes the exact reviewed PC8 Lock semantics and retains the
standalone manifest as durable specified criteria. It does not establish
dispatchable, executable, or qualified conformance and it does not accept PC8
implementation or product behavior.

```text
PC8_RR_P2_01_CLOSED=true
PC8_SEMANTICS_ACCEPTED=true
PC8_SPECIFIED_CONFORMANCE_ACCEPTED=true
PC8_SEMANTIC_FREEZE_COMPLETE=true
PC8_SEMANTICS_FROZEN=true
PC8_DOCUMENTATION_PUBLISHED=true
PC8_IMPLEMENTATION_STARTED=false
PC8_ACCEPTED=false
FIXTURE_MATURITY=specified
PUSH_COMPLETE=true
FINAL_DISPOSITION=PASS
NEXT_BOUNDED_TASK=separate read-only PC8 implementation and executable-conformance impact assessment against the newly frozen authority
```
