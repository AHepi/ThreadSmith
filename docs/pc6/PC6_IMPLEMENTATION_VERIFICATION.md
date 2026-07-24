# PC6 Package Scan Implementation Verification

Verification date: 2026-07-24.

Status: the bounded production implementation remains written and uncommitted.
The closed conformance-fixture interpreter now executes all 184 authoritative
rows and all 180 scan runs through the public PC6 boundary. Focused
qualification and complete frozen workspace qualification pass with the
isolated Rust 1.97.1 environment, cached dependencies, and no network access.
Implementation verification is complete. Independent implementation review
and acceptance remain incomplete.

## Fixture-interpreter repair initial gate

| Field | Verified initial value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| HEAD | `6350ee1bd3d08154b53e559ec7f8b2a30bd56322` |
| HEAD tree | `7585417326bc4706d497709f2c5c1230aa568d01` |
| Existing `origin/main` | `6350ee1bd3d08154b53e559ec7f8b2a30bd56322` |
| Existing `origin/main` tree | `7585417326bc4706d497709f2c5c1230aa568d01` |
| Index | clean |
| Worktree | intentional uncommitted PC6 implementation only |

Initial tracked changes:

```text
M  DECISIONS.md
M  IMPLEMENTATION_PLAN.md
M  PROJECT_STATE.md
M  crates/threadsmith-compiler/src/lib.rs
```

Initial untracked files:

```text
conformance/pc6/package_scan/fixture_manifest.json
crates/threadsmith-compiler/src/package_scan.rs
crates/threadsmith-compiler/tests/pc6_package_scan.rs
docs/pc6/PC6_IMPLEMENTATION_VERIFICATION.md
```

Initial tracked diff stat:

```text
DECISIONS.md                              | 17 ++++++
IMPLEMENTATION_PLAN.md                    | 34 ++++++++++++
PROJECT_STATE.md                          | 26 ++++++++--
crates/threadsmith-compiler/src/lib.rs     | 25 ++++++---
4 files changed, 86 insertions(+), 8 deletions(-)
```

The initial inventory was inspected completely and was limited to the reported
PC6 implementation, conformance, verification, and additive state work. No
unrelated change was found. No fetch or other remote operation was performed.

The controlling documents retained their accepted hashes:

```text
Package Scan erratum:
235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25

PC6 semantic freeze:
4e444eaac263b453d5d80252f28a63db919fa36efb9fef0dc98319ca0e7e0204
```

## Original implementation state and gap

The existing production work provides the immutable optional-`packages`
snapshot intake, exact Package Scan boundary, all global validation stages, the
31 diagnostics, accepted PC2 parser reuse, closed descriptor admission,
portable paths, metadata audit, raw-byte verification and retention, canonical
package identities, and private source/package/byte binding.

The existing `fixture_manifest.json` preserved all accepted rows and frozen
populations, and focused tests exercised representative public paths. It did
not interpret each row's exact operation notation. Consequently a fixture
could be counted without its source and snapshot being constructed and sent
through `acquire_project_snapshot` and `scan_packages`. Population arithmetic
did not establish executable conformance.

## Exact fixture-interpreter repair

The repair adds three narrowly scoped layers:

1. `build_executable_fixture_plan.py` translates every authoritative fixture
   row into a deterministic external plan. Each case is bound to the accepted
   row's exact input and expected-result strings by SHA-256. The generator
   constructs every base and run in an independent in-memory tree and rejects
   missing ancestors, duplicate children, non-exact replacement or deletion,
   incomplete enumeration, missing constants or records, unknown fields,
   unknown operations, unused authoritative data, duplicate IDs, and
   undispatched fixtures.
2. `executable_fixture_plan.json` is the fixed data consumed by the Rust
   harness. It contains two exact source vectors, eight exact base snapshots,
   typed acquisition or scan programs, closed node and byte-expression
   vocabularies, exact live-mutation timing, fixed diagnostic outcomes, and
   complete successful-package records. It contains no inferred directories,
   children, files, bytes, descriptor members, diagnostics, or defaults.
3. `pc6_fixture_interpreter.rs` deserializes that plan through
   unknown-field-rejecting types, reconstructs every node and byte mutation,
   performs exact optional-`packages` lookup, calls the public
   `acquire_project_snapshot` and `scan_packages` entry points, and compares
   complete outcomes. It never calls a private Package Scan validator.

For diagnostic rows, the harness permits only `Err`, then compares the exact
code and complete canonical rendered path. No successful or partial package
set can satisfy that branch.

For successful rows, the harness compares the exact source binding; package
count and deterministic ordering; package, version, lattice, profiles, module
file, and descriptor file members; declared paths and digests; retained raw
bytes; exact package identity; and canonical descriptor bytes. It also checks
the applicable equivalence, distinction, hard-link, unlisted-file, immutable
snapshot, repeatability, retained-byte, and derivation relationships.

The harness records every executed fixture, source, base, operation, byte
expression, node kind, result relation, expected package record, constant,
canonical vector, and primary diagnostic code, then requires exact equality
with the closed vocabularies. The accepted expected outcomes remain external
fixed data; the harness does not calculate an expected diagnostic by
reimplementing production validation.

## Files changed by this repair

```text
conformance/pc6/package_scan/build_executable_fixture_plan.py
conformance/pc6/package_scan/executable_fixture_plan.json
crates/threadsmith-compiler/tests/support/pc6_fixture_interpreter.rs
crates/threadsmith-compiler/tests/pc6_package_scan.rs
docs/pc6/PC6_IMPLEMENTATION_VERIFICATION.md
PROJECT_STATE.md
IMPLEMENTATION_PLAN.md
```

The existing fixture manifest was read but not changed. No accepted authority,
PC6 scope/freeze document, production source file, Cargo file, dependency file,
Foundation or PC1-PC5 file, later-phase file, or Git ref was changed by this
repair.

## Deterministic mechanical evidence

`python3 conformance/pc6/package_scan/build_executable_fixture_plan.py --write`
completed successfully and wrote the deterministic plan. The independent
staleness check:

```text
python3 conformance/pc6/package_scan/build_executable_fixture_plan.py --check
```

completed successfully with:

```text
authority_sha256=235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25
fixture_ids=184 unique=184 dispatched=184
scan_cases=176 scan_runs=180 diagnostic_cases=123 success_cases=53 acquisition_cases=8
diagnostic_expectations=124 diagnostic_codes_exercised=31
byte_constants=34 canonical_vectors=6 package_identities=19
data_changed_canonical_bytes=318 data_changed_identity=lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b
all_references_resolved=true all_operations_constructible=true
```

The checker proves:

- exactly 184 unique authoritative IDs have exactly 184 executable cases;
- all 176 scan cases contain at least one public scan run, for 180 runs total;
- all eight acquisition cases contain exact node evidence or one declared
  acquisition error;
- all case operations and live operations apply successfully to exact base
  trees without implicit ancestors or children;
- all 123 primary Package Scan diagnostic expectations contain exact code and
  path, the complete 124-entry diagnostic ledger is reachable, and all 31
  diagnostic codes occur;
- all 34 constants decode, have exact lengths, and reproduce their fixed
  SHA-256 values;
- all six canonical package vectors are byte-exact and reproduce their hashes
  and identities;
- all 19 additional identities reproduce from complete descriptor records and
  fixed file bytes;
- the DATA_CHANGED descriptor canonicalizes to exactly 318 bytes and reproduces
  `lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b`;
- all two sources, eight bases, 15 operation categories, 11 byte-expression
  kinds, six node kinds, 19 success relations, complete expected records, and
  authoritative constants and vectors are reachable.

The generator passed Python bytecode compilation with its cache redirected
outside the repository. A lexical Rust delimiter scan passed for the new
support module. These checks do not substitute for Rust parsing or execution.

`git diff --check` passed. Accepted Standard/erratum/freeze paths and Cargo
paths have no repair diff. The Package Scan erratum and freeze SHA-256 values
remain exact.

## Focused repair sequence

The accepted PC2 diagnostic-precedence repair centralizes explicit scalar-tag
interpretation in the private `TaggedScalar` classifier. Incompatible explicit
core tags now fail during the forbidden-feature audit, while recognized
out-of-range integers retain `SOURCE_INVALID_SCALAR`. The focused PC2 suite
passes 18 tests with no failure. `PARSE-TAG-MISMATCH` consequently produces
`PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN` at
`packages/alpha/1.0.0/package.yaml#`.

The executable-plan repair derives `M_ALPHA_100` mechanically from the
authoritative fixture manifest and materializes both `REPLACE_HEX` cases before
serialization. `FILE-LINE-ENDINGS` now contains one direct 111-byte lowercase
hex expression with SHA-256
`3c30f12e8929018fe49106632840db81d938772a08782b754e920d8d391e3f19`.
`FILE-BOM` contains one direct 108-byte lowercase hex expression with SHA-256
`43a8b648df7dbcba5a4d792083cfb041fdfc9d9f4457b7b8dd4beaebdcb4ff99`.
The Python validator and Rust interpreter both require direct exact hex for
`REPLACE_HEX`; the unreachable serialized `lf_to_crlf` vocabulary was removed,
while `concat` remains reachable for descriptor construction.

The final bounded Clippy repair changed only:

```text
crates/threadsmith-compiler/tests/support/pc6_fixture_interpreter.rs
crates/threadsmith-compiler/tests/pc6_package_scan.rs
```

The two manual remainder checks now use `usize::is_multiple_of`. The
`compare_scanned_source` helper now receives one private borrowed structure
containing the existing plan, authoritative constants, and canonical vectors.
No assertion, fixture, expected record, byte, digest, ordering rule, source
binding, package binding, operation, diagnostic, or public API changed.

## Isolated toolchain and dependency state

All commands used these isolated paths and settings:

```text
RUSTUP_HOME=/tmp/threadsmith-rustup
CARGO_HOME=/tmp/threadsmith-cargo
CARGO_NET_OFFLINE=true
PATH=/tmp/threadsmith-rustup/toolchains/1.97.1-x86_64-unknown-linux-gnu/bin:/usr/bin:/bin
```

The verified binaries are:

```text
rustc 1.97.1
rustc commit 8bab26f4f68e0e26f0bb7960be334d5b520ea452
cargo 1.97.1
cargo commit c980f4866141969fab6254a680546a277789d6f0
rustfmt 1.9.0-stable
clippy 0.1.97
```

Dependencies were already present in the isolated Cargo cache. No rustup,
installation, download, fetch, update, registry synchronization, dependency
resolution, telemetry, or other network operation occurred. Every Cargo
qualification command used `--frozen --offline`; formatting ran with
`CARGO_NET_OFFLINE=true`.

## Focused qualification evidence

The exact focused sequence passed:

```text
cargo fmt --all -- --check
git diff --check
cargo test -p threadsmith-compiler --test pc2_parser --frozen --offline
cargo check -p threadsmith-compiler --all-targets --frozen --offline
cargo test -p threadsmith-compiler --test pc6_package_scan --frozen --offline
cargo clippy -p threadsmith-compiler --all-targets --all-features --frozen --offline -- -D warnings
python3 conformance/pc6/package_scan/build_executable_fixture_plan.py --check
git diff --check
```

PC2 passed 18 tests with zero failures. PC6 passed 13 tests with zero failures.
The Rust fixture interpreter executed 184 unique fixture IDs with none skipped
or left over, 180 public scan runs, 123 diagnostic cases, 53 successful cases,
eight acquisition cases, 124 diagnostic expectations, and all 31 diagnostic
codes. Complete successful package records, retained bytes, canonical
identities, package ordering, source binding, and absence of partial success
were compared. `PARSE-TAG-MISMATCH`, `FILE-LINE-ENDINGS`, and `FILE-BOM` all
passed through the public PC6 API.

Formatting, frozen all-target compilation, all-feature Clippy with warnings
denied, the deterministic executable-plan checker, golden population checks,
and textual-diff checks all passed. The accepted fixture manifest, production
PC6 source, completed PC2 repair, Cargo manifests, lockfile, accepted
authorities, prior-phase files, and unrelated paths remained byte-identical
during the final Clippy repair.

## Full frozen workspace qualification

The full qualification reused the same direct isolated binaries and cached
dependencies. The exact ordered commands were:

```text
cargo fmt --all -- --check
cargo check --workspace --all-targets --frozen --offline
cargo test --workspace --all-targets --frozen --offline
cargo clippy --workspace --all-targets --all-features --frozen --offline -- -D warnings
cargo tree --workspace --frozen --offline
python3 conformance/pc6/package_scan/build_executable_fixture_plan.py --check
git diff --check
```

Formatting and the workspace all-target check passed. The workspace test run
passed exactly 67 tests with zero failed, zero ignored, zero measured, and zero
filtered:

```text
threadsmith-canonical unit tests                         7 passed
PC1 conformance                                         5 passed
PC5 canonical JSON                                      3 passed
threadsmith-compiler unit tests                         0 passed
PC2 parser                                             18 passed
PC3 source validation                                   7 passed
PC4 default                                             3 passed
PC5 digest                                              6 passed
PC6 package scan                                       13 passed
threadsmith-schema unit tests                           5 passed
aggregate                                              67 passed
```

The PC6 suite again executed all 184 unique fixture IDs and all 180 public scan
runs: 123 diagnostic cases, 53 successful cases, eight acquisition cases, 124
diagnostic expectations, and all 31 diagnostic codes. No fixture was skipped
or left over. `PARSE-TAG-MISMATCH`, `FILE-LINE-ENDINGS`, and `FILE-BOM`
continued to pass through the real public Package Scan API.

The all-workspace, all-target, all-feature Clippy gate passed with warnings
denied. The first invocation exited successfully but replayed three obsolete
diagnostic messages from the pre-repair Cargo build cache; direct inspection
proved that every cited expression and signature was absent from the current
files. Repeating the identical Clippy gate with
`CARGO_TARGET_DIR=/tmp/threadsmith-pc6-workspace-clippy-target` forced a fresh
offline rebuild and passed with no diagnostic output. No repository cleanup or
source change was used.

The frozen dependency tree resolved entirely from `Cargo.lock` and the
isolated cache. PC6 added no external dependency. Every `Cargo.toml` and
`Cargo.lock` remained byte-identical and had no worktree diff. The executable
plan checker passed and independently reproduced:

```text
fixture_ids=184 unique=184 dispatched=184
scan_cases=176 scan_runs=180 diagnostic_cases=123 success_cases=53 acquisition_cases=8
diagnostic_expectations=124 diagnostic_codes_exercised=31
byte_constants=34 canonical_vectors=6 package_identities=19
data_changed_canonical_bytes=318 data_changed_identity=lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b
all_references_resolved=true all_operations_constructible=true
```

Independent manifest accounting also matched the frozen 18 descriptor
presentations, 18 path-scalar vectors, and six pointer vectors. The accepted
Package Scan erratum retained SHA-256
`235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25`,
and the PC6 semantic freeze retained SHA-256
`4e444eaac263b453d5d80252f28a63db919fa36efb9fef0dc98319ca0e7e0204`.
The accepted Standard, every accepted erratum, PC6 reconciliation/freeze
evidence, PC1-PC5 conformance material, and prior implementation evidence
remained unchanged except for the three authorized current-status documents.

Before the success-only documentation update, independently sorted SHA-256
inventories covered all 114 repository files outside Git metadata and build
output. The pre- and post-qualification manifests were byte-identical, with
manifest SHA-256
`71791b201e32034abac130c3e85a19776d3805822e9a441a98d94c6ae3faec88`.
Qualification changed no source, test, fixture, generator, executable plan,
Cargo file, lockfile, accepted authority, prior-phase evidence, or unrelated
path.

The combined candidate boundary remains the accepted PC2 precedence repair in
`crates/threadsmith-compiler/src/lib.rs` and
`crates/threadsmith-compiler/tests/pc2_parser.rs`; the PC6 production,
integration, interpreter, generator, executable-plan, and fixture-authority
paths already present in the authorized worktree; and the three current
verification/status documents. No dependency, later compiler phase, Builder,
runtime, provider, or product-surface change is part of this boundary.

## Proven and remaining state

Focused PC6 qualification and full frozen workspace qualification are complete,
so PC6 implementation verification is complete. The implementation and fixture
interpreter remain uncommitted, and PC6 remains unaccepted. No independent
implementation review was performed or claimed. Builder and runtime remain
unauthorized.

## Exact next gate

Perform a separate independent read-only PC6 implementation review. PC6
acceptance, commit, push, Builder, runtime, and every later phase remain
separate and unauthorized.
