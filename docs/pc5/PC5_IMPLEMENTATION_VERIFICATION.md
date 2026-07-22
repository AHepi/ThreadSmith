# PC5 Digest-Phase Implementation Verification

Verification date: 2026-07-23.

Status: implementation qualification and bounded totality-repair verification
complete; a fresh independent read-only review and acceptance remain separate,
incomplete gates.

## Baseline

| Field | Value |
|---|---|
| Branch | `main` |
| Required and observed local commit | `1f6ac46647e49519add2f732fc0148dad05fe6d6` |
| Required and observed local tree | `1ac37136547c1247854558987a441fc3e4ddab96` |
| Observed remote commit | `1f6ac46647e49519add2f732fc0148dad05fe6d6` |
| Observed remote tree | `1ac37136547c1247854558987a441fc3e4ddab96` |
| Initial worktree | Clean |
| Qualification input worktree | Exact expected ten-path uncommitted PC5 implementation inventory |

## Implementation written

`threadsmith-canonical` now uses one exact canonical JSON writer for all
existing callers. It normalizes strings and keys to NFC, sorts normalized keys
by unsigned UTF-8 bytes, preserves arrays, emits minimal integers, uses the
closed lowercase escape spellings, and emits every other Unicode scalar
directly. The accepted arbitrary-precision integer representation remains
supported.

`threadsmith-compiler` now exposes opaque `BlueprintDigest` and
`DigestedSource` types plus:

```rust
pub fn digest_source(source: DefaultedSource) -> DigestedSource
```

The operation consumes the PC4 wrapper, calls `threadsmith-canonical` for both
canonical encoding and SHA-256, constructs one Blueprint-kind native identity,
and retains the exact input beside it. The output contains no canonical bytes,
provenance, diagnostic, metadata, artifact, permission, Binding, or authority
field. No public constructor, deserializer, or mutable replacement operation
can create a mismatched source/digest pair.

## Bounded totality repair

`validate_blueprint_source` now admits caller-created JSON values to the exact
frozen PC2 value domain before applying PC3 root semantics. The private
recursive admission accepts only null, booleans, signed minimal `i64`
integers, NFC strings, arrays, and objects with NFC keys and no post-NFC key
collision. It rejects input unchanged with
`SOURCE_VALUE_DOMAIN_INVALID`; it does not normalize caller input or perform
declaration validation.

Arrays are traversed by increasing index. Objects are traversed depth first by
ascending raw UTF-8 key bytes, with each object's complete key set checked
before child values. Diagnostic paths use deterministic RFC 6901 pointers;
raw values have no source line or column. The later raw-sorted key owns a
post-NFC collision path, while the first raw-sorted non-NFC key owns a
standalone key failure. This admission precedes PC3 semantic root validation,
so the accepted diagnostic precedence for genuine PC2 output is unchanged.

The repair does not change `digest_source`, the canonical writer, the digest
preimage, declaration-validation ownership, or any later phase. Domain-valid
but later-invalid declarations remain digestible.

## Focused tests executed

`pc5_canonical_json.rs` covers all eight canonical byte/hash vectors, the
complete Blueprint golden preimage, alternate-profile participation, array
order, and the accepted Foundation arbitrary-integer domain.

`pc5_digest.rs` exercises every reachable equivalence, distinction, profile,
and later-invalid fixture through the public PC2-to-PC5 path at least three
times. It checks exact digest text, Blueprint kind, native textual
representation, exact source preservation, repeatability, and array order.

The repair also tests fail-closed admission for floats, out-of-range integers,
non-NFC strings or keys, and post-NFC key collisions through the public
pipeline without a panic.

The two focused binaries pass 9 tests total: 3 canonical JSON tests and 6
compiler Digest tests.

## Qualification environment

Qualification used only the pre-existing isolated toolchain at
`/tmp/threadsmith-rustup/toolchains/1.97.1-x86_64-unknown-linux-gnu` with
`CARGO_HOME=/tmp/threadsmith-cargo`. Cargo network access was disabled with
`CARGO_NET_OFFLINE=true`, retry count zero, loopback refusal proxies, and
`--frozen` on every dependency-aware Cargo command. No installer, downloader,
Rustup command, index update, dependency update, or external connection was
used.

| Tool | Exact version |
|---|---|
| `rustc` | `rustc 1.97.1 (8bab26f4f 2026-07-14)`, commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452`, LLVM 22.1.6 |
| `cargo` | `cargo 1.97.1 (c980f4866 2026-06-30)`, commit `c980f4866141969fab6254a680546a277789d6f0` |
| `rustfmt` | `rustfmt 1.9.0-stable (8bab26f4f6 2026-07-14)` |

Before qualification, Rustfmt was run directly with edition 2024 on exactly
the two new PC5 test files. Its changes matched the previously reported
formatter diff. Hashes of the other eight implementation paths were unchanged,
the ten-path inventory was unchanged, and inspection found no change to test
data, assertions, identifiers, literals, API calls, or control flow.

## Commands and results

The original qualification used the explicit toolchain binaries. The bounded
repair qualification used the prescribed local Rustup and Cargo homes with
`cargo +1.97.1`; it selected the already-installed toolchain and remained
offline. No installer or synchronizing command was used.

```text
$RUSTFMT --edition 2024 crates/threadsmith-canonical/tests/pc5_canonical_json.rs crates/threadsmith-compiler/tests/pc5_digest.rs
PASS

$CARGO fmt --all -- --check
PASS

$CARGO check --workspace --all-targets --frozen
PASS

$CARGO test --workspace --all-targets --frozen
PASS: 50 passed, 0 failed, 0 ignored

$CARGO clippy --workspace --all-targets --all-features --frozen -- -D warnings
PASS: no warnings

$CARGO tree --workspace --frozen
PASS: complete frozen dependency tree resolved from local resources

git diff --check
PASS
```

Post-repair focused commands:

```text
cargo +1.97.1 test -p threadsmith-compiler --test pc5_digest --frozen
PASS: 6 passed, 0 failed

cargo +1.97.1 test -p threadsmith-compiler --test pc2_parser --test pc3_source_validate --test pc4_default --frozen
PASS: 26 passed, 0 failed (PC2 16, PC3 7, PC4 3)
```

Post-repair full qualification restarted from formatting:

```text
cargo +1.97.1 fmt --all -- --check
PASS

cargo +1.97.1 check --workspace --all-targets --frozen
PASS

cargo +1.97.1 test --workspace --all-targets --frozen
PASS: 52 passed, 0 failed, 0 ignored

cargo +1.97.1 clippy --workspace --all-targets --all-features --frozen -- -D warnings
PASS: no warnings

cargo +1.97.1 tree --workspace --frozen
PASS: complete frozen dependency tree resolved from local resources

git diff --check
PASS
```

The post-repair 52 tests comprise:

| Suite | Passed |
|---|---:|
| Foundation canonical unit tests | 7 |
| Foundation schema unit tests | 5 |
| PC1 conformance | 5 |
| PC2 parser | 16 |
| PC3 source validation | 7 |
| PC4 defaults | 3 |
| PC5 canonical JSON | 3 |
| PC5 Digest | 6 |
| **Total** | **52** |

Foundation and PC1-PC4 regressions account for 43 passing tests; focused PC5
coverage adds 9 passing tests.

## Checks completed

| Check | Result |
|---|---|
| Required baseline and local/remote equality | Pass |
| Initial worktree cleanliness | Pass |
| PC5 fixture JSON integrity | Pass |
| Fixture category counts | Pass: 8 canonical, 5 equivalent source presentations, 8 distinctions, 6 later-invalid cases |
| Golden byte-hex SHA-256 cross-check | Pass: all 8, using the existing Python standard library only |
| Compiler dependency shape | Pass: two existing workspace path dependencies only |
| External package inventory | Pass: no package added |
| Original Standard hash | Pass: `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| Default Semantics Erratum hash | Pass: `ed5d32095abe2f834f19cef20d27f20d60469ecf0ac1367ed75e4725e2527766` |
| Canonical JSON Erratum hash | Pass: `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` |
| Frozen PC5 documents and fixture diff | Pass: unchanged |
| Prior Foundation and PC1-PC4 conformance diff | Pass: unchanged |
| Formatting | Pass: direct repair and workspace check |
| Workspace all-target check | Pass: frozen |
| Full test suite | Pass: 52/52; 43 prior-phase and 9 PC5 |
| Clippy | Pass: all targets, all features, warnings denied |
| Frozen dependency tree | Pass: 31 packages; inventory unchanged |
| Edit allowlist | Pass |
| `git diff --check` | Pass |

The lockfile package inventory is identical to the baseline: no external
package was added. Its only dependency-graph change is the two existing
workspace path edges from `threadsmith-compiler` to `threadsmith-canonical`
and `threadsmith-schema`.

## Proof boundary

This qualification proves that the current uncommitted, repaired PC5
implementation formats, compiles, lints, and passes every workspace test under
the pinned Rust 1.97.1 toolchain with frozen, network-silent dependency
resolution. It proves that public caller-created inputs outside the frozen PC2
domain fail before construction of `ValidatedSource`, while genuine PC2 paths
and later-invalid domain-valid declarations remain operational. It also proves
the fixture counts, eight golden canonical encodings and hashes, controlling-
document hashes, frozen PC5 artifacts, prior conformance artifacts, dependency
inventory, and edit boundary checked here.

It does not constitute the independent implementation review, PC5 acceptance,
publication, a proof against SHA-256 collisions, or authority for Package scan
or any later compiler/runtime phase.

## Boundary retained

No package scan, resolution, Lockfile behavior, import expansion, declaration
validation, duplicate-name validation, static check, later identity, Manifest,
qualification, Binding, runtime, replay, Builder, provider, model-management,
CLI, MCP, Android, SDK, UI, commit, or push work was performed.

```text
PC5_IMPLEMENTATION_STARTED=true
PC5_IMPLEMENTATION_VERIFICATION_COMPLETE=true
PC5_IMPLEMENTATION_REVIEW_COMPLETE=false
PC5_REPAIR_COMPLETE=true
PC5_REPAIR_REVIEW_COMPLETE=false
PC5_ACCEPTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC5 repaired implementation independent read-only review
```
