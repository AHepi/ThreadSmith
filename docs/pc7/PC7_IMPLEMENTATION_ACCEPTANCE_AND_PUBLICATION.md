# PC7 Resolve Implementation Acceptance and Publication

Record date: 2026-07-28

Status: accepted for publication through the exact procedure in this record.
This record becomes durable publication authority only when the exact
ten-path commit containing it is successfully published to `refs/heads/main`.

## Acceptance scope

This record accepts the exact independently qualified PC7 Resolve
implementation and executable-conformance candidate. Acceptance is limited to
the frozen Resolve boundary. It does not repair or reinterpret accepted
semantics, modify accepted authority, reopen a finding, change a reviewed
candidate byte, or begin a later phase.

The authenticated pre-acceptance repository identity is:

```text
Branch=main
Required_HEAD=69861ccc8580b658b1365a42b1e7b45e8c0d6452
Required_tree=e22cd53a128957f07416433d0c77c05337f8bef0
Required_remote_main=69861ccc8580b658b1365a42b1e7b45e8c0d6452
Initial_index_empty=true
Initial_candidate_inventory=exact_six_paths
```

The resulting commit, tree, cached remote, fresh remote, and push identities
are self-excluded from this repository document and are recorded only in the
external operator report.

## Accepted candidate identities

The accepted implementation and executable-conformance candidate consists of
exactly these six paths and bytes:

| Path | SHA-256 |
|---|---|
| `conformance/pc7/resolve/build_executable_fixture_plan.py` | `02968be53c6403953fe3e7c691a3acd36eba0dc5c6c5ec6462a75e5c2201764b` |
| `conformance/pc7/resolve/executable_fixture_plan.json` | `4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d` |
| `crates/threadsmith-compiler/src/lib.rs` | `00e726435f9b8442da89992971ce18b382c881849401b57693c4c6554a6d9a87` |
| `crates/threadsmith-compiler/src/resolve.rs` | `bc9a8e8718702ffd9ef1077cf9c4da3c731f0faee27865bdb80405a535f9c2ca` |
| `crates/threadsmith-compiler/tests/pc7_resolve.rs` | `df7d77543102979f8fd02e991a547d9cd2e1ff339a4f753b7d475110d5e533f1` |
| `crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs` | `3efdbfe63ec403b737e05a0444956efe09e3d059d2a4b064a9622f65976fe326` |

The six hashes were authenticated before regression execution, after the
regression spine, after durable-state authoring, and before staging. No
accepted candidate path is regenerated or formatted into different bytes by
this acceptance gate.

## Controlling semantic authority

The recovered Lattice Standard remains primary. The accepted Resolve erratum,
standalone fixture manifest, semantic freeze, and V1 authority registry bind
the exact PC7 semantics and criteria used by the generator, interpreter,
qualification, and review:

| Authority | Bytes | SHA-256 |
|---|---:|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | 66,657 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md` | 1,413,209 | `a0ab4b4eaa0e06d0105fd43b06e684c7581e7b359d6a89cc76eb44b9057fc72e` |
| `docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json` | 1,306,575 | `da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c` |
| `docs/pc7/PC7_SEMANTIC_FREEZE.md` | 30,129 | `47f2b65f3807e0fe4940c7c6c15475fa472f0a578dba2bccaaba670e43654169` |
| `docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json` | 2,041 | `7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161` |

The controlling semantic-publication procedure is:

```text
Report=THREADSMITH_PC7_SEMANTIC_AND_CRITERIA_REPAIR_ACCEPTANCE_FREEZE_AND_PUBLICATION.txt
Bytes=26830
Lines=681
SHA256=48a9cb9b90e83397ede415515574ece94a64d78f05585d48aaf074f5ae2710e8
```

That report binds the exact fifth-repair acceptance, refrozen semantic
authority, standalone manifest, authority registry, and preserved dormant
future-only P3. This implementation acceptance changes none of those bytes.

## Governing implementation and qualification evidence

Every governing report was authenticated before any live repository write as
valid UTF-8 without BOM, LF-only, exactly one final LF, no trailing horizontal
whitespace, and no NUL byte.

| Evidence | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `THREADSMITH_PC7_IMPLEMENTATION_AND_EXECUTABLE_CONFORMANCE_SECOND_REPAIR.txt` | 33,112 | 917 | `c4e26cd22737a2e807a5d23b2ca8323e5fcc7460d0a494439c47d70bb2c12600` |
| `THREADSMITH_PC7_IMPLEMENTATION_AND_EXECUTABLE_CONFORMANCE_SECOND_REPAIR_INDEPENDENT_RE_REVIEW.txt` | 37,273 | 962 | `710fec8d3b48aeeee57da272bf2d5f0062840fb809b01aa2e34f0e150517668e` |
| `THREADSMITH_PC7_REFRESHED_FOCUSED_QUALIFICATION.txt` | 37,145 | 1,067 | `1c4ecf8ec5ea238ca4b833d28b3f575592c547decd511434fc7253c26768be27` |
| `THREADSMITH_PC7_REFRESHED_FOCUSED_QUALIFICATION_INDEPENDENT_REVIEW.txt` | 55,500 | 1,039 | `8bc60be961f2a81fdf7ac82ae1ecaf2d7dd2bb05e7c39d555f23e1e73b69605d` |

The final independent qualification review records:

```text
RECOMPUTED=168
DERIVED=0
REFUTED=0
UNDERDETERMINED=0
UNVERIFIED=0
REVIEW_P0=0
REVIEW_P1=0
REVIEW_P2=0
REVIEW_P3=0
QUALIFICATION_REVIEW_DISPOSITION=PASS
```

These results are acceptance evidence bound to the exact candidate,
authorities, plan, toolchain, and baseline recorded here. They are not
substitutes for the retained executable criteria.

## Toolchain and isolation

The acceptance regression used only the already available local toolchain and
cached dependencies:

```text
rustc=1.97.1 (8bab26f4f 2026-07-14)
rustc_commit=8bab26f4f68e0e26f0bb7960be334d5b520ea452
cargo=1.97.1 (c980f4866 2026-06-30)
rustfmt=1.9.0-stable
clippy=0.1.97
host=x86_64-unknown-linux-gnu
RUSTUP_HOME=/tmp/threadsmith-rustup
CARGO_HOME=/tmp/threadsmith-cargo
CARGO_NET_OFFLINE=true
Rust_or_dependency_install=false
Rust_network_use=false
Cargo_targets_inside_repository=false
Python_caches_inside_repository=false
```

All Cargo targets and Python caches were redirected beneath an isolated
acceptance directory in `/tmp`. Cargo ran frozen or locked and offline.

## Acceptance regression results

The exact regression categories and outcomes are:

| Gate | Command class | Result |
|---|---|---|
| Formatting | `cargo fmt --all -- --check` | PASS |
| Workspace check | `cargo check --workspace --all-targets --frozen --offline` | PASS |
| Complete workspace tests | `cargo test --workspace --all-targets --frozen --offline` | PASS |
| Clippy | `cargo clippy --workspace --all-targets --all-features --frozen --offline -- -D warnings` | PASS |
| Dependency tree | `cargo tree --workspace --frozen --offline` | PASS |
| Unfiltered PC7 binary | `cargo test --locked --offline -p threadsmith-compiler --test pc7_resolve -- --nocapture` | PASS |
| Generator admission and rejection self-tests | generator with explicit authority root and registry, `--check --print-summary` | PASS |
| Checked-plan verification | generator `--check` against the retained plan | PASS |
| Python syntax | external-cache `python3 -m py_compile` | PASS |
| Disposable regeneration A | authenticated copy with plan removed, then explicit generation | PASS |
| Disposable regeneration B | authenticated copy with plan removed, then explicit generation | PASS |
| Regeneration comparisons | A equals B; A and B equal checked plan | PASS |
| Textual diffs | `git diff --check` and `git diff --cached --check` | PASS |

The complete workspace result is:

```text
Workspace_tests_discovered=78
Workspace_tests_passed=78
Workspace_tests_failed=0
Workspace_tests_ignored=0
Workspace_tests_filtered_out=0
```

The 78 tests comprise seven canonical-core unit tests, five PC1 tests, three
PC5 canonical-JSON tests, zero compiler unit tests, 18 PC2 tests, seven PC3
tests, three PC4 tests, six PC5 Digest tests, 13 PC6 tests, 11 PC7 tests, and
five schema-core unit tests.

The separately invoked unfiltered PC7 test binary result is:

```text
Tests_discovered=11
Tests_passed=11
Tests_failed=0
Tests_ignored=0
Tests_filtered_out=0
```

The public-boundary PC7 interpreter dispatches every current case through
`resolve_source`, rejects duplicate execution, compares complete success or
exact diagnostic outcomes, and asserts defined/generated equality before
dispatch and defined/executed equality afterward.

## Fixture equality, plan identity, and determinism

The fixture population and set relationship are:

```text
Defined_fixture_ids=118
Generated_fixture_ids=118
Executed_fixture_ids=118
defined_fixture_ids==generated_fixture_ids==executed_fixture_ids=true
Excluded_future_vectors=4
Excluded_future_vectors_dispatched=0
```

The newline-delimited, byte-sorted current fixture-ID preimage has exactly one
final LF:

```text
Fixture_ID_preimage_bytes=2576
Fixture_ID_preimage_SHA256=ab7b72bdb33a255d2539a204cd880fa7aedab61b8672cfa3f02d8342d510f221
```

The checked and independently regenerated plan identity is:

```text
Plan_bytes=34460681
Plan_SHA256=4e1e5ef85dadeea5c1d0d3cd0ef9231dae887237b5860e89c8925db9420b9d9d
Regeneration_A_equals_B=true
Regeneration_A_equals_checked_plan=true
Regeneration_B_equals_checked_plan=true
Generator_rejection_self_tests=PASS
Checked_plan_verification=PASS
```

All 118 current rows are therefore specified, dispatchable, executable
through the public boundary, and qualified for the exact PC7 claim. Fixture
maturity is `qualified`. The four future vectors remain outside the current
population and receive no dispatch or qualification claim.

## Unchanged-boundary proof

Before durable-state authoring, the worktree differed from the required
baseline at exactly the six reviewed candidate paths and the index was empty.
Regression outputs and Python caches remained outside the repository.

After durable-state authoring and before staging, the complete prospective
inventory is exactly:

```text
PROJECT_STATE.md
IMPLEMENTATION_PLAN.md
DECISIONS.md
docs/pc7/PC7_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md
conformance/pc7/resolve/build_executable_fixture_plan.py
conformance/pc7/resolve/executable_fixture_plan.json
crates/threadsmith-compiler/src/lib.rs
crates/threadsmith-compiler/src/resolve.rs
crates/threadsmith-compiler/tests/pc7_resolve.rs
crates/threadsmith-compiler/tests/support/pc7_fixture_interpreter.rs
```

The six candidate hashes remain exactly those recorded above. Every accepted
authority hash remains exact. Every Cargo manifest and `Cargo.lock` remains
byte-identical to the required baseline. All PC1-PC6 implementation,
conformance, fixture, and acceptance paths remain byte-identical except that
the reviewed `lib.rs` candidate adds the PC7 module and public exports without
altering the earlier phase implementations. The complete workspace regression
proves earlier supported behavior remains passing.

No path outside the exact ten-path allowlist is staged or committed. Paths are
staged explicitly; no broad `git add` pathspec is permitted. Both unstaged and
staged textual-diff checks must pass before commit.

## Acceptance boundary and retained limitations

PC7 acceptance covers only the following boundary:

| Included surface | Limit |
|---|---|
| Input | Frozen opaque `ScannedSource` and optional immutable existing-Lockfile bytes used only by Resolve |
| Lock intake | Exact existing-Lockfile validation needed by Resolve |
| Resolution | Profile eligibility, requirement intersection, version selection, compatible lock reuse, and deterministic fixed-point resolution |
| Module intake | Selected-module parsing from PC6-retained bytes |
| Failure | Total diagnostic precedence and exact logical paths |
| Success | Converged graph and source-bound non-authoritative `ResolvedSource` |
| Conformance | Strict generator, checked plan, public-boundary interpreter, and qualified current fixture set recorded here |

PC7 acceptance does not create or authorize a new Lockfile, `lock_id`,
Manifest, Binding, identity, authority, persistence, installation, provider,
model, network operation, Builder, runtime, CLI, MCP, UI, Android behavior, or
other product surface.

The historical semantic-review value remains:

```text
RESOLVE_ERRATUM_REVIEW_P3=1
```

That finding is dormant, future-only, non-dispatchable, excluded from current
populations, and non-blocking. It is not the PC7 implementation-review or
qualification-review result. This acceptance does not close, reclassify,
dispatch, erase, or otherwise alter it.

## Publication procedure

The complete candidate and durable-state inventory is staged explicitly.
Exactly one commit is created with:

```text
Commit_message=Implement and accept PC7 Resolve
Commit_parent=69861ccc8580b658b1365a42b1e7b45e8c0d6452
Commit_parent_count=1
```

Immediately before publication, a fresh remote query must still identify
`refs/heads/main` at
`69861ccc8580b658b1365a42b1e7b45e8c0d6452`. Only then may the exact new
commit be sent by a normal non-force fast-forward push to
`refs/heads/main`. No other ref, tag, branch, pull request, merge, amend,
rebase, squash, force option, or alternate publication topology is permitted.

Successful publication requires local `HEAD`, local `main`, cached
`origin/main`, and fresh remote `main` to equal the new commit, the new commit
to have the required single parent, the published inventory to equal the ten
paths above, and both index and worktree to be clean. Those resulting
identities and the push result are recorded externally because embedding them
here would be self-referential.

## Durable state

```text
PC7_IMPLEMENTATION_STARTED=true
PC7_FIXTURE_INTERPRETER_COMPLETE=true
PC7_FOCUSED_QUALIFICATION_COMPLETE=true
PC7_IMPLEMENTATION_VERIFICATION_COMPLETE=true
PC7_IMPLEMENTATION_REVIEW_COMPLETE=true
PC7_QUALIFICATION_REVIEW_COMPLETE=true
PC7_REVIEW_P0=0
PC7_REVIEW_P1=0
PC7_REVIEW_P2=0
PC7_REVIEW_P3=0
PC7_ACCEPTED=true
FIXTURE_MATURITY=qualified
PUSH_COMPLETE=true
PC8_STARTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC8 Lock scope reconciliation and semantic freeze only
```
