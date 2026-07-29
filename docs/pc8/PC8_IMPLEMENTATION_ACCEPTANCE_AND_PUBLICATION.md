# PC8 Lock Implementation Acceptance and Publication

Record date: 2026-07-29

Status: accepted for publication through the exact procedure in this record.
This record becomes durable publication authority only when the exact
eleven-path commit containing it is successfully published to
`refs/heads/main`.

## Acceptance scope

This record accepts the exact independently qualified PC8 Lock implementation
and executable-conformance candidate. Acceptance is limited to the frozen
portable Lock boundary. It does not repair or reinterpret accepted semantics,
change V2 specified criteria, rehabilitate superseded evidence, persist a
physical Lockfile, or begin Expand or another later phase.

The authenticated pre-acceptance repository identity is:

```text
Repository=AHepi/ThreadSmith
Branch=main
Required_HEAD=eb6f1e35d314f3c436402f122f4752e4ecc34073
Required_tree=2297b01c9ed65b6ccd4b7d54bd33e5256a4c0405
Required_remote_main=eb6f1e35d314f3c436402f122f4752e4ecc34073
Initial_index_empty=true
Initial_candidate_inventory=exact_seven_paths
```

The resulting commit, tree, local and cached refs, fresh remote, push result,
and same-tree procedural-file hashes are self-excluded from this repository
document. They are recorded only in the external operator report.

## Accepted candidate identities

The accepted implementation and executable-conformance candidate consists of
exactly these seven paths and byte sequences:

| Path | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `crates/threadsmith-compiler/src/lib.rs` | 42,769 | 1,266 | `899896e905050c8615d0a0737072bae77451d117ec58d2ca0d71ca1e2ca9e99a` |
| `crates/threadsmith-compiler/src/lock.rs` | 11,402 | 379 | `894ff6a938869d8a3161d348134ec525edee221411095f6688e8cdfa7a4b0e0e` |
| `conformance/pc8/lock/build_executable_fixture_plan.py` | 102,057 | 2,479 | `1f09749f8290eb85f09f25d35c1d51c0bf3079b9f10aa551f5b1b4aadb36ec35` |
| `conformance/pc8/lock/executable_fixture_plan.json` | 542,521 | 11,355 | `f95b8feb6d6e012b76239a974eb39f709a50f7ac98a2b6dddddac01e52d1a0f6` |
| `crates/threadsmith-compiler/tests/pc8_lock.rs` | 26,340 | 655 | `5c006a901951562d05f463d93510e09bd8539aa4b803c46438c9000c87c9c0fb` |
| `crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs` | 72,231 | 2,093 | `88e0635fb75e15a5dc1483fdd8f86ab2be59c389030c4ade16552c1f8225a71b` |
| `crates/threadsmith-compiler/tests/support/pc8_fixture_interpreter.rs` | 42,539 | 1,225 | `5cca941058bb2147bff198a50b3608b82b7eadee44f82fc0c25cca8ed4e94916` |

No acceptance step may regenerate, format, refactor, or otherwise change these
bytes.

## Controlling authority

The recovered Standard remains primary. Registry V2 routes the accepted Lock
erratum and exact V2 manifest without changing frozen normative semantics:

| Authority | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | 66,657 | 2,492 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md` | 25,595 | 442 | `bd44aa9d43c6b6abf354f0ca556a66fbab97a06b3c24f21394ffe7769e3875bc` |
| `docs/pc8/PC8_SCOPE_RECONCILIATION.md` | 34,394 | 473 | `a41990db0e2263a94356b2d87783e8f484d464e3f503200255aa0e81a3072c73` |
| `docs/pc8/PC8_SEMANTIC_FREEZE.md` | 15,024 | 267 | `c23f846c3dc7e795551f9fc2fbd0e65b2ba5bbc91eec269a5dda8490e231a0b1` |
| `docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json` | 21,344 | 525 | `b442f1acb4a7eb316ed9d61da02af3c1e5c60c34f55cf6eefefa751339d0a2c6` |
| `docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V2.json` | 1,053,112 | 25,732 | `314e1cd73f23c07067e167d37e84782c7a301b13b4c6458d62a37d0423c4482a` |
| `docs/pc8/PC8_SPECIFIED_CONFORMANCE_CRITERIA_V2_ACCEPTANCE_AND_SUPERSESSION.md` | 12,894 | 273 | `e4cfc883445a18f0efc5a4c0f2afc341b076de1915b77a3276e946d4fbcd2f58` |

Registry V2 remains procedural routing rather than normative semantics. The
V1 registry and V1 manifest remain immutable, authentic, superseded history.
There has been one post-freeze specified-criteria supersession and zero
post-freeze Lock normative supersessions.

## Governing implementation and qualification evidence

Every evidence subject below was reauthenticated before this acceptance:

| Gate | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| Task 1 resumed verification | 7,788 | 247 | `b57d5f59d1eb170a4fe490841eedfa0d6e571bdf04e9078851ba9107a74b6101` |
| Task 1 independent review | 14,044 | 365 | `8063ac2165cabcc75eb555f9868aaa160810f858c69f1f5df4796dacf5de7d7f` |
| Task 2 repair independent review | 23,653 | 655 | `b7a457cef561d3cdc95237831aa02453349486aab00eaa8be0b143f8f21881ab` |
| Task 2 acceptance | 11,058 | 285 | `30b532e042f92f27af9b4ef182b49885166dcd8c0123c85ca98be0c4171478aa` |
| Task 3 second-repair independent review | 19,477 | 532 | `cf307fff71268e436ddad98dcb4aae3a2eae0f0df98e4215f14d895d308289a7` |
| Task 3 acceptance | 14,265 | 379 | `1b2d49e2879c0c6c1f26f35a8d3909d75295e58207c5bd249971f25160f2b1dc` |
| Q17 repair independent review | 10,827 | 300 | `fa6d915ffec331746a38fefb591fca906d557efb09027697ce9fca0e2ad5cb90` |
| Task 3 Q17 acceptance amendment | 7,437 | 206 | `3689d90076f389d3137d938006104cdd900b9a833e27851d12ea0cb5e59c4ea8` |
| Complete superseding Task 4 qualification | 21,742 | 615 | `c1c845fa4414a3b1aeec940fd8aec096c304dcab79037276080635a0d3a89d49` |
| Task 4 qualification acceptance | 9,733 | 232 | `a384f10418486744b9d0e1f751b70b4934235ad9118f4e7fc810ee3bfe5d4edb` |
| Task 5 authority-preflight procedure amendment | 5,373 | 133 | `5733b59b89a3f39dbb065ede00f9ce5c156da7473c420a66f91403bacb85d17a` |
| Governing superseding Task 5 independent review | 19,485 | 458 | `90f7fa8f56c5d7df7014d13349c7a098b0566d94ee651c86d3656369ec89cbbc` |
| Task 5 procedural-repair review | 9,150 | 189 | `1edb4d84cf5e5fb3411f4d33855403e51d7ebeff7ea90569c3207f5c80ec68dc` |

The original Task 5 report remains immutable non-governing history at 19,485
bytes, 458 lines, and SHA-256
`4fe408ff266c5470478bcbe9e0229807779af2922098a82075195c115a2b38f1`.
Its Section 7 printed 13 incorrect evidence identities. The governing
superseding report changes exactly those 13 SHA-256 assignment lines:

```text
Removed_lines=13
Added_lines=13
Non_SHA_changes=0
Other_changes=0
Superseding_identity_matches=17/17
```

The separate procedural-repair review independently reproduced that boundary.
No candidate, authority, qualification, R1-R15 result, mutant result, finding,
acceptance recommendation, or terminal alias changed.

## Qualification and independent-review result

The complete third Task 4 attempt restarted at Q01 without inherited PASS and
records Q01 through Q29 as `PASS`. Its pinned offline matrix includes:

| Gate | Result |
|---|---|
| Formatting | PASS |
| Workspace all-target, all-feature check | PASS |
| Workspace all-target tests | 88 passed, 0 failed |
| Focused unfiltered `pc8_lock` | 10 passed, 0 failed |
| Workspace all-feature Clippy with warnings denied | PASS |
| Frozen dependency tree | PASS |
| PC6 and PC7 checked plans | PASS |
| V2 PC8 generator admission and self-rejection | PASS |
| Two disposable PC8 regenerations | Byte-equal to each other and the checked plan |
| Repository and no-persistence boundary | PASS |

The checked PC8 plan is 542,521 bytes and 11,355 lines at SHA-256
`f95b8feb6d6e012b76239a974eb39f709a50f7ac98a2b6dddddac01e52d1a0f6`.
It closes 20 current fixtures, 19 relations, four excluded future rows, 12
schema mutations, 235 registry spans, 1,266 schema nodes, 204 consumer
admissions, and seven named generator-rejection checks.

The strict public-boundary interpreter proves:

```text
defined_current_fixture_ids=20
generated_current_fixture_ids=20
executed_current_fixture_ids=20
defined==generated==executed=true
defined_relation_ids=19
evaluated_relation_ids=19
defined_relations==evaluated_relations=true
excluded_future_ids=4
executed_future_ids=0
```

Task 5 independently reran the baseline, recomputed R1 through R15, and killed
all 15 registered false-green mutants for their intended mechanisms:

```text
R1_R15=PASS
P0=0
P1=0
P2=0
P3=0
MUTANTS_KILLED=15
MUTANTS_SURVIVED=0
MUTANTS_WRONG_REASON=0
FINAL_DISPOSITION=PASS
```

Fixture maturity is therefore `qualified`.

## Preserved failure and supersession history

Acceptance preserves rather than rewrites:

- the failed V1-bound Task 2 generator and plan as invalid historical evidence;
- closure of `PC8-T2-SM-02` and `PC8-T2-SC-03` by the accepted Task 2 repair;
- closure of `F-PC8-T3-001` and `F-PC8-T3-002` by the accepted Task 3 repairs;
- the first Task 4 `FAIL` at Q01 caused by pre-existing repository-local
  `target`;
- recoverable quarantine of that cache outside the repository;
- the second Task 4 `FAIL` at Q17 and closure of `PC8-T4-Q17-01`;
- the blocked pre-amendment Task 5 Phase 3, which supplied no inherited PASS;
- the original non-governing Task 5 report and its exact procedural repair.

No historical failure is relabeled as PASS or included in a later PASS
population.

## Accepted implementation boundary

PC8 acceptance covers pure, deterministic Lock construction from one exact
authenticated PC7 `ResolvedSource` to one source-bound `LockedSource`,
canonical omission-preimage bytes, canonical emitted Lock bytes, and the
exact Lock identity. The output preserves the complete `ResolvedSource`.

PC8 does not write a physical Lockfile, perform atomic replacement, read live
state, call a network, install a dependency, create execution authority, emit
a Manifest or Run Binding, or authorize Builder, runtime, providers, CLI,
MCP, UI, Android, or another product surface. The future PC8 Lockfile
Persistence Adapter remains separate and unauthorized.

The normative compiler sequence remains:

```text
Resolve -> Lock -> Expand
```

## Exact repository and publication boundary

The complete prospective commit inventory is exactly:

```text
DECISIONS.md
IMPLEMENTATION_PLAN.md
PROJECT_STATE.md
docs/pc8/PC8_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md
conformance/pc8/lock/build_executable_fixture_plan.py
conformance/pc8/lock/executable_fixture_plan.json
crates/threadsmith-compiler/src/lib.rs
crates/threadsmith-compiler/src/lock.rs
crates/threadsmith-compiler/tests/pc8_lock.rs
crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs
crates/threadsmith-compiler/tests/support/pc8_fixture_interpreter.rs
```

No path outside this exact eleven-path allowlist may be staged or committed.
The seven candidate hashes must remain exact. Every V1/V2 authority,
`Cargo.toml`, `Cargo.lock`, toolchain, dependency, and earlier-phase path must
remain byte-identical to the required parent except for the reviewed
`lib.rs` and PC7 helper candidate bytes listed above.

Exactly one commit is created with:

```text
Commit_message=Implement and accept PC8 Lock
Commit_parent=eb6f1e35d314f3c436402f122f4752e4ecc34073
Commit_parent_count=1
Branch=main
Ref=refs/heads/main
Mode=normal non-force fast-forward
Commit_count=1
```

Immediately before publication, fresh remote `main` must still equal the
required parent. No merge, rebase, amend, squash, force option, tag, alternate
ref, pull request, or second commit is permitted.

Successful publication requires the published tree to equal the independently
reproduced prospective tree and local `HEAD`, local `main`, cached
`origin/main`, and fresh remote `main` to converge on the single new commit
with a clean index and worktree.

The self-excluded prospective tree, same-tree file hashes, commit, push, and
final ref identities are recorded at:

```text
/workspace/ThreadSmith/PC8/handoffs/pc8-lock-implementation-acceptance-publication/output/THREADSMITH_PC8_LOCK_IMPLEMENTATION_ACCEPTANCE_PUBLICATION_AND_DURABLE_STATE_UPDATE.txt
```

## Durable state

The following state becomes operative only through successful publication of
the exact eleven-path commit:

```text
PC8_SEMANTICS_ACCEPTED=true
PC8_SEMANTICS_FROZEN=true
PC8_SPECIFIED_CONFORMANCE_V1_CURRENT=false
PC8_SPECIFIED_CONFORMANCE_V2_REVIEWED=true
PC8_SPECIFIED_CONFORMANCE_V2_ACCEPTED=true
PC8_SPECIFIED_CONFORMANCE_V2_PUBLISHED=true
POST_FREEZE_PC8_SPECIFIED_CRITERIA_SUPERSESSIONS=1
POST_FREEZE_PC8_LOCK_NORMATIVE_SUPERSESSIONS=0
PC8_IMPLEMENTATION_STARTED=true
PC8_TASK_1_ACCEPTED=true
PC8_TASK_2_ACCEPTED=true
PC8_TASK_3_ACCEPTED=true
PC8_TASK_4_COMPLETE=true
PC8_TASK_4_ACCEPTED=true
PC8_TASK_5_ACCEPTED=true
PC8_EXECUTABLE_CONFORMANCE_COMPLETE=true
PC8_FIXTURE_INTERPRETER_COMPLETE=true
PC8_FOCUSED_QUALIFICATION_COMPLETE=true
PC8_QUALIFIED=true
PC8_IMPLEMENTATION_VERIFICATION_COMPLETE=true
PC8_IMPLEMENTATION_REVIEW_COMPLETE=true
PC8_QUALIFICATION_REVIEW_COMPLETE=true
PC8_REVIEW_P0=0
PC8_REVIEW_P1=0
PC8_REVIEW_P2=0
PC8_REVIEW_P3=0
PC8_ACCEPTED=true
FIXTURE_MATURITY=qualified
OPEN_NORMATIVE_DEFECTS=0
OPEN_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_IMPLEMENTATION_DEFECTS=0
PUSH_COMPLETE=true
PC9_STARTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC9 Expand scope reconciliation and semantic freeze only
```

Naming the next bounded task authorizes only PC9 scope reconciliation and
semantic freeze. It does not authorize Expand implementation or any Builder,
runtime, persistence, provider, installation, or product work.
