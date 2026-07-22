# PC3 Source-Validation Implementation Verification

Verification date: 2026-07-22.

Source baseline commit: `94c3978aa92d27064e8f25cf40681f8ce67b379d`

Source baseline tree: `ea1951221ea49e7caedf7687c7fe231918f6c1da`

## Implementation boundary

The public implementation is `validate_blueprint_source(Value) -> Result<ValidatedSource, SourceDiagnostic>` in `threadsmith-compiler`. `ValidatedSource` has a private value field and exposes immutable borrowing or consuming extraction only. No new crate, feature, dependency, build script, native code, or FFI surface was added.

## Qualification results

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass |
| `cargo check --workspace --all-targets --locked --offline` | Pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass |
| `cargo test --workspace --all-targets --locked --offline` | Pass: 39 passed, 0 failed |
| Foundation canonical regressions | Pass: 7 |
| Foundation schema/authority regressions | Pass: 5 |
| PC1 conformance regressions | Pass: 5 |
| PC2 parser regressions | Pass: 15 |
| PC3 focused integration tests | Pass: 7; all 19 frozen fixture cases are each replayed three times; all required and categorized root fields are independently exercised |
| Frozen fixture JSON integrity | Pass |
| Accepted Foundation/PC1/PC2/Standard/ADR diff | Pass: none |
| Cargo manifest and lock diff | Pass: none |
| `git diff --check` | Pass |

## Focused behavior proven

- non-object roots fail with `SOURCE_ROOT_TYPE`;
- unknown keys are selected by ascending UTF-8 bytes and use escaped RFC 6901 paths;
- missing required keys follow frozen required-key order;
- invalid values follow frozen permitted-key order;
- Core lattice/profile selectors, module-name grammar, and three-component version form are enforced;
- every declaration root field is an array when present;
- declaration elements remain opaque, including later-invalid names, kinds, references, contracts, routes, policies, controls, budgets, and secrets;
- absent optional fields, explicit empty fields, arbitrary declaration-array order, and the complete PC2 value are preserved without default insertion; and
- repeated validation returns identical success or diagnostic results.

## Dependency and provenance result

`Cargo.toml` and `Cargo.lock` are unchanged. PC3 uses existing `serde_json::Value` plus standard Rust operations, so parser dependency provenance, licences, offline availability, native/FFI exposure, and reproducibility implications are unchanged.

The historical PC3-intake checksum ledger continues to describe the accepted freeze tree. Its durable state entries change during implementation acceptance; the freeze documents and fixture remain unchanged. The implementation checksum ledger records the completed PC3 tree separately.

## Not proven

This tranche does not prove declaration validity, default expansion, package resolution, Lockfile generation, Blueprint or declaration identity, normalization, gate insertion, static checking, Manifest generation, qualification, Binding, runtime, replay, builder behavior, cross-platform binary reproducibility, or release readiness.
