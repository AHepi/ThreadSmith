# PC2 Parser Intake Verification Report

Verification date: 2026-07-22.

## Baseline and environment

| Field | Value |
|---|---|
| Accepted baseline commit | `f61beef39129013ae439fbef917636779d5231eb` |
| Accepted baseline tree | `798bd917d3ed6f2a3ae8136d532ab671863bd001` |
| Rust | `rustc 1.97.1 (8bab26f4f 2026-07-14)` |
| Cargo | `cargo 1.97.1 (c980f4866 2026-06-30)` |
| Workspace dependency mutation | None |
| Production/API diff | None |

## Results

| Check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass |
| `cargo check --workspace --locked --offline` | Pass |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass |
| Foundation schema regressions | Pass: 5 passed, 0 failed |
| Foundation canonical regressions | Pass: 7 passed, 0 failed |
| PC1 conformance regressions | Pass: 5 passed, 0 failed |
| Accepted immutable-file SHA-256 verification | Pass |
| Accepted production and conformance diff check | Pass: zero diff |
| Intake dependency online locked check | Pass |
| Intake dependency offline locked check | Pass |
| Selected parser event qualification | Pass: all fixtures parse as YAML; anchor and tag metadata are visible before tree construction |
| Fixture manifest validation | Pass: 4 valid and 9 invalid cases, unique IDs, all referenced files present |
| Fixture UTF-8 and NFC validation | Pass |
| Expected-tree and diagnostic-shape validation | Pass |
| Dependency checksum match | Pass: 8 resolved packages match Cargo registry checksums |
| Licence-file presence | Pass for all 8 resolved packages, including both inherited `saphyr-parser` licence sets and Unicode-3.0 |
| Build-script inventory | Pass: 3 pinned Rust scripts; only selected-`rustc` probes found; no C/C++, pkg-config, cmake, or system-library probe |
| Native/FFI check | Pass: no native FFI, system libyaml, Python parser, or native dependency in the intake graph |

The first workspace offline command reported a cache miss for existing accepted dependencies after the checkout was rehydrated. `cargo fetch --locked` populated the cache without changing repository files, and the complete workspace verification then passed offline. This was an environment prerequisite, not dependency resolution drift.

The dependency probe used a scratch-only manifest with `saphyr-parser =0.0.11` and default features disabled. It generated an isolated lock, passed online and offline checks, and was not copied into the ThreadSmith repository. The future implementation lock remains the authority once implementation is separately authorized.
