# Foundation/PC1 Verification Report

Report status: reconstructed verification evidence recorded on 2026-07-22. This report qualifies the new reconstructed tree; it does not reproduce the lost historical suite or Git history.

## Environment

| Component | Verified value |
|---|---|
| rustup installer | 1.29.0 archive SHA-256 `4acc9acc76d5079515b46346a485974457b5a79893cfb01112423c89aeb5aa10` |
| rustc | `1.97.1 (8bab26f4f 2026-07-14)`; full commit `8bab26f4f68e0e26f0bb7960be334d5b520ea452` |
| Cargo | `1.97.1 (c980f4866 2026-06-30)`; full commit `c980f4866141969fab6254a680546a277789d6f0` |
| rustfmt | `1.9.0-stable (8bab26f4f6 2026-07-14)` |
| Clippy | `0.1.97 (8bab26f4f6 2026-07-14)` |
| Host | `x86_64-unknown-linux-gnu`; LLVM 22.1.6 |
| Installed components | cargo, clippy, rust-std, rustc, rustfmt |

The toolchain was restored outside the repository. No toolchain binaries are part of the provenance tree.

## Qualification matrix

| Command or check | Result |
|---|---|
| `cargo fmt --all -- --check` | Pass; no diff. |
| `cargo check --workspace --all-targets --locked --offline` | Pass; both workspace crates and all targets. |
| `cargo clippy --workspace --all-targets --locked --offline -- -D warnings` | Pass; zero warnings. |
| `cargo test --workspace --all-targets --locked --offline` | Pass after bounded review repair; 17 tests, 0 failed. |
| `cargo test -p threadsmith-schema --lib --locked --offline` | Foundation pass; 5 tests, 0 failed. |
| `cargo test -p threadsmith-canonical --lib --locked --offline` | Canonical-preimage pass; 7 tests, 0 failed. |
| `cargo test -p threadsmith-canonical --test pc1_conformance --locked --offline` | Foundation vector and PC1 schema conformance pass; 5 tests, 0 failed. |
| `cargo test --workspace --doc --locked --offline` | Pass; 0 doctests present. |
| `cargo metadata --format-version 1 --no-deps --locked --offline` | Pass; exactly two workspace members. |
| `cargo tree --workspace --locked --offline` | Pass; complete dependency closure resolves from `Cargo.lock` without network. |
| Recovered in-tree SHA-256 checks | Pass for all five recovered placements. |
| Legacy wheel SHA-256 and ZIP integrity | Pass; artifact SHA-256 matches `f6643d…49ef5`; all 24 ZIP members pass. |
| Legacy wheel RECORD verification | Pass; 23 declared member hashes and sizes match. |
| Reconstructed vector cross-check through supplied oracle | Pass; 6 valid byte/hash/typed-claim vectors and 2 invalid vectors, including arbitrary-size integers and negative-zero normalization. |

One combined checksum invocation used literal backslashes in the wheel filename and therefore failed to open that path. The wheel was immediately rechecked using its correctly quoted filename; its digest, ZIP integrity, and every RECORD hash passed. No repository file changed as a result.

## Behavioural evidence

| Required boundary | Evidence |
|---|---|
| Foundation identity mathematics | Canonical NFC JSON, sorted keys, compact UTF-8 bytes, arbitrary-size integers, SHA-256 digest, non-authoritative typed preimage claims, and claim verification exercised through public APIs. Artifact-specific preimage selection is deliberately not claimed. |
| Native/legacy separation | Recovered schema tests prove comparison without authority and reject legacy authority use. |
| Migration receipt non-authority | The recovered constructor assigns `AuthorityEffect::None` on every successful outcome path; its surviving unit test directly exercises the Equivalent path. |
| Absent preimage rejection | Canonical unit and verifier-path tests plus the recovered PC1 model return `IDENTITY_PREIMAGE_UNRESOLVED` before creating a typed claim. |
| PC1 schema vector | The complete recovered model is strictly deserialized with unknown fields denied, every categorical value constrained, every recovered field and value asserted, and unknown, missing, mistyped, and unsupported-value mutations rejected. |

## Stable source and evidence hashes

| Path | Classification | SHA-256 |
|---|---|---|
| `Cargo.toml` | recovered | `2f4bf8fdbbba2daeb9c4b067b430f95a5105cdb71129b67690b4c402ca403b6f` |
| `THREADSMITH_IMPLEMENTATION_DIRECTIVE.md` | recovered zero-byte object | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `crates/threadsmith-schema/src/lib.rs` | recovered | `8174175061eb2701a8995349c2e919eb06342942d69485e734cd722bc1eec6ef` |
| `conformance/pc1/core_model.json` | recovered | `26e810a5e7932fbcc6cc08c81e6f84030b39940dbdd2fc08bb8a1bd276f5a460` |
| `docs/adr/0001-portable-core-language.md` | recovered | `6c7608a3efa9e3a6f7db93d8ba3cfee8837fbfb87b2f2344f1ad8cc121799b08` |
| `Cargo.lock` | reconstructed | `56b705a3ce18022f8a4723f2e0839194a7a01ce6cf41b988fea6d1f03794ac93` |
| `rust-toolchain.toml` | reconstructed | `8e390d6a0838315f972690f46ef8bae8b7ecc9ee6c1ed70140ef852869c2482e` |
| `crates/threadsmith-schema/Cargo.toml` | reconstructed | `bb3852ed9f4f64bfdaf2c818997b35c9eb9b9822e80d7b8c4d04fad1596603b3` |
| `crates/threadsmith-canonical/Cargo.toml` | reconstructed | `f1f0c47e833780535da74c6077271737a6e03fab2f58462adabbba7d397ba2e8` |
| `crates/threadsmith-canonical/src/lib.rs` | reconstructed | `5ebad0226131e90c4cd9345b36fed1be021cc5d16409400ec4c4fabe179d23ac` |
| `crates/threadsmith-canonical/tests/pc1_conformance.rs` | reconstructed | `364b545f2ea0af414468b0d9652340f4e6673d71199415978c23cc42ab3216e7` |
| `conformance/foundation/canonical_vectors.json` | reconstructed | `d79edc0c54eb5f15789cb5a345249db1f9c107212a5cc564b0fcc5dd5d6c84d8` |

The complete final tree manifest is recorded in `SHA256SUMS` after the read-only review record is added.

## Qualification limits

The lost external regression suite, original vectors, original lockfile, substantive implementation directive, and Lattice Standard 0.3 were not recovered. Artifact-specific blueprint and manifest preimage selection therefore remains unresolved, exactly as recorded by the recovered PC1 model; the reconstructed public API verifies already-resolved preimage mathematics and never grants authority. The recovered migration schema also does not constrain `RequiredNextAction` by outcome, although every receipt remains non-authoritative. Passing results establish the reconstructed baseline against the supplied evidence and stated recovery criteria only. They do not establish byte identity with the lost workspace.
