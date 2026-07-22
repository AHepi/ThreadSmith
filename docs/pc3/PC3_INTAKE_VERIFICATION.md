# PC3 Scope and Semantic-Freeze Verification

Verification date: 2026-07-22.

Baseline commit: `94c3978aa92d27064e8f25cf40681f8ce67b379d`

Baseline tree: `ea1951221ea49e7caedf7687c7fe231918f6c1da`

## Environment

| Component | Result |
|---|---|
| Rust | `rustc 1.97.1 (8bab26f4f 2026-07-14)` |
| Cargo | `cargo 1.97.1 (c980f4866 2026-06-30)` |
| Dependency mode | `--locked --offline` |
| Baseline | local `main` and `origin/main` matched the recorded commit and tree before edits |

## Regression results

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | pass |
| `cargo check --workspace --all-targets --locked --offline` | pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | pass |
| `cargo test --workspace --all-targets --locked --offline` | pass: 32 tests, 0 failed |
| Foundation canonical unit suite | pass: 7 |
| PC1 conformance suite | pass: 5 |
| Schema/native-legacy and migration suite | pass: 5 |
| PC2 parser regression suite | pass: 15 |

## PC3 documentation and fixture results

| Check | Result |
|---|---|
| JSON syntax and unique fixture identifiers | pass: 19 cases |
| Independent root-validator oracle against exact expected outcomes | pass: 19 cases |
| Requested valid/invalid/deferred semantic categories explicit | pass |
| Standard root allowlist and required-key extraction | pass; exact match |
| Standard lifecycle adjacency (`Parse`, `Source validate`, `Default`) | pass |
| Documentation references and state consistency | pass |
| `git diff --check` | pass |

The oracle is verification code executed from the shell; it is not product code and was not added to the repository. It independently implements the frozen root-only decision order and compares every manifest case with its exact expected code/path or unchanged-success result.

## Provenance and boundary checks

| Evidence | Result |
|---|---|
| Standard SHA-256 | unchanged: `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| PC2 implementation SHA-256 | unchanged: `b4a62deedcbffd8599066acd3c4906199cb43c079dd2cb22849ff460da59bf16` |
| PC2 regression SHA-256 | unchanged: `dec443cd12b7d4be1c73497e76793aa4ef58620c6d57ab93c591d5105ab7d824` |
| `Cargo.toml` SHA-256 | unchanged: `4a75e00ce7a60fc7033a473b63a8509e3695b4dadfe60581a70f30dcb9798d67` |
| `Cargo.lock` SHA-256 | unchanged: `03b0244635c458583108edc56c6fcb33eeeae060e1ed6e7d29943c8c5b2b0b5a` |
| Cargo/dependency diff | none |
| Foundation, PC1, PC2, Standard, and ADR diff | none |
| Rust product-code diff | none |

## Dependency and licence findings

PC3 requires no new dependency for the frozen boundary. No dependency was added, removed, updated, or re-featured, so accepted provenance, offline behavior, licences, build scripts, native/FFI exposure, and reproducibility implications are unchanged. Any implementation proposal that requires a new dependency must stop and reopen dependency intake.

## What this verification proves

It proves that the documentation and fixtures consistently describe a deterministic, root-only PC3 `Source validate` boundary; accepted Foundation, PC1, and PC2 behavior still passes; and no implementation or dependency mutation entered the tranche.

It does not prove PC3 implementation behavior, declaration validity, default expansion, identity, resolution, Lockfile or Manifest generation, static checking, qualification, Binding, runtime behavior, or release readiness.
