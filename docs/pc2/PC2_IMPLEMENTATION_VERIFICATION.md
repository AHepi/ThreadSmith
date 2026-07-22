# PC2 Parser Implementation Verification

Verification date: 2026-07-22.

## Environment and scope

| Field | Value |
|---|---|
| Source baseline commit | `84238ee404c752b65d047fad2469cfc253b593d6` |
| Source baseline tree | `bef9d75bda5091b69319f9bf00934eaeea3baaef` |
| Rust | `rustc 1.97.1 (8bab26f4f 2026-07-14)` |
| Cargo | `cargo 1.97.1 (c980f4866 2026-06-30)` |
| Parser dependency | `saphyr-parser =0.0.11`, default features disabled |
| Native/system parser dependency | None |
| Python parser dependency | None |

## Qualification results

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass |
| `cargo check --workspace --all-targets --locked --offline` | Pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass |
| `cargo test --workspace --all-targets --locked --offline` | Pass: 28 passed, 0 failed |
| Foundation schema regressions | Pass: 5 passed, 0 failed |
| Foundation canonical regressions | Pass: 7 passed, 0 failed |
| PC1 conformance regressions | Pass: 5 passed, 0 failed |
| PC2 focused parser tests | Pass: 11 passed, 0 failed; includes 4 valid and 9 invalid frozen fixtures |
| Locked/offline metadata and dependency tree | Pass |
| Dependency version/checksum comparison with intake | Pass; four newly locked packages match exactly |
| Licence-file presence and hashes | Pass for parser and resolved graph records |
| Native/FFI boundary | Pass: no system libyaml, Python, Git/path override, C/C++ build, or unpinned native FFI |
| Foundation/PC1 immutable-file diff | Pass: zero diff |
| Historical Foundation hash ledger, immutable entries | Pass |
| Historical PC2-intake hash ledger, immutable entries | Pass |
| PC2 implementation changed-file ledger | Pass |

The historical `SHA256SUMS` ledger intentionally continues to describe the reconstructed Foundation/PC1 tree. Its `Cargo.toml`, `Cargo.lock`, and three durable-state entries differ because later accepted tranches changed those files; all other entries verify. Likewise, the PC2 intake ledger's three durable-state entries differ after implementation acceptance, while every intake document and fixture verifies. Neither historical ledger was rewritten.

The committed `Cargo.lock` SHA-256 before this report was `03b0244635c458583108edc56c6fcb33eeeae060e1ed6e7d29943c8c5b2b0b5a`. The resolved parser graph is the exact graph accepted during intake. Offline verification used the pre-populated Cargo registry cache; a release/source bundle still requires the vendoring or cache procedure specified by the intake.

## Proven and unproven

Proven: the public parser implements the frozen source boundary and deterministic diagnostics for the accepted fixtures and tested edge cases; Foundation/PC1 bytes and regression behavior are preserved; the selected dependency graph is pinned, cached, and buildable offline in the accepted environment.

Not proven: arbitrary-input termination under unbounded size or depth; byte-reproducible binaries across hosts; cross-platform qualification; any Blueprint or Manifest identity; compiler semantics, resolution, execution, runtime, builder, or release behavior.
