# PC2 Standard Reconciliation Verification

Verification date: 2026-07-22.

## Baseline and environment

| Field | Value |
|---|---|
| Baseline commit | `d49017e319d5472007f0062c4574d099510f5b05` |
| Baseline tree | `834a8ca2caf18e8301268b1f80e4ceb47dd2cdca` |
| Branch | `main` |
| Initial worktree | Clean |
| Rust | `rustc 1.97.1 (8bab26f4f 2026-07-14)` |
| Cargo | `cargo 1.97.1 (c980f4866 2026-06-30)` |
| Toolchain location | Disposable `/tmp/threadsmith-rustup`; no repository or user installation |
| Parser dependency | Unchanged `saphyr-parser =0.0.11`, default features disabled |
| Lockfile SHA-256 | Unchanged `03b0244635c458583108edc56c6fcb33eeeae060e1ed6e7d29943c8c5b2b0b5a` |

## Results

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass |
| `cargo check --workspace --all-targets --locked --offline` | Pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass |
| `cargo test --workspace --all-targets --locked --offline` | Pass: 32 passed, 0 failed |
| Foundation canonical unit regressions | Pass: 7 passed, 0 failed |
| Foundation schema regressions | Pass: 5 passed, 0 failed |
| PC1 conformance regressions | Pass: 5 passed, 0 failed |
| PC2 parser regressions | Pass: 15 passed, 0 failed |
| Standard conformance fixtures | Pass: 7 valid and 8 invalid fixtures through the public API |
| Fixture manifest paths/count and expected-JSON syntax | Pass |
| Standard recovered/tracked hash comparison | Pass: exact SHA-256 match |
| Cargo manifests, lock, Foundation/PC1 crates and conformance diff from baseline | Pass: zero diff |
| Locked/offline dependency tree and metadata | Pass |
| Parser graph licence-file presence | Pass |
| `git diff --check` | Pass |

The online step was limited to installing the repository-pinned Rust toolchain in `/tmp` and populating its disposable Cargo cache. All qualification commands were subsequently run with both `--locked` and `--offline` where supported.

## Focused implementation repairs before review

The first focused fixture run passed 13 of 14 tests. The folded-block diagnostic initially pointed to the dependency's content marker instead of the forbidden `>` token; the parser now reports the indicator position and the focused suite passed 14 of 14.

The first Clippy pass found one iterator-style warning under `-D warnings`; it was repaired without semantic change. The complete formatting/check/Clippy/test sequence was then rerun successfully.

Read-only review repair cycle 1 added correct handling for Standard YAML core tags and made object sorting explicit before `serde_json::Map` insertion. The focused suite then passed 15 of 15 and the complete qualification sequence passed 32 of 32.

## Proven

- PC2 accepts the Standard root vocabulary without interpreting it.
- Missing required fields, unknown fields, explicit values, and absent fields survive for PC3.
- PC2 performs no default insertion or unit/profile gate.
- literal blocks, matching YAML core JSON-category tags, YAML 1.2 Core non-float scalars, signed `i64` bounds, line-ending normalization, and single-document presentation forms behave deterministically;
- forbidden YAML, floats, non-string keys, duplicate keys, and NFC collisions fail closed;
- arrays preserve order and JSON objects serialize in deterministic key order;
- Foundation/PC1 code, identity boundaries, migration behavior, Cargo dependency graph, and lockfile are unchanged.

## Not proven or not implemented

PC3 Source validation, later compiler phases, Blueprint or Manifest identity, resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, provider behavior, cross-platform qualification, byte-reproducible binaries, and arbitrary-depth resource bounds are not proven or implemented by this tranche.
