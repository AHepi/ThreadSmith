# ThreadSmith Foundation/PC1 Restoration Inventory

Inventory status: reconstructed from a read-only inspection completed on 2026-07-22 before repository edits.

## Recovered artifacts placed in the tree

| Supplied filename | Repository path | Status | SHA-256 | Notes |
|---|---|---|---|---|
| `Cargo.toml` | `Cargo.toml` | recovered | `2f4bf8fdbbba2daeb9c4b067b430f95a5105cdb71129b67690b4c402ca403b6f` | Exact path and bytes are directly evidenced. |
| `lib.rs` | `crates/threadsmith-schema/src/lib.rs` | recovered | `8174175061eb2701a8995349c2e919eb06342942d69485e734cd722bc1eec6ef` | Exact bytes; repository path is a high-confidence reconstruction. |
| `core_model.json` | `conformance/pc1/core_model.json` | recovered | `26e810a5e7932fbcc6cc08c81e6f84030b39940dbdd2fc08bb8a1bd276f5a460` | Exact bytes; repository path is reconstructed. |
| `0001-portable-core-language(1).md` | `docs/adr/0001-portable-core-language.md` | recovered | `6c7608a3efa9e3a6f7db93d8ba3cfee8837fbfb87b2f2344f1ad8cc121799b08` | Exact bytes; attachment suffix removed and directory reconstructed. |
| `THREADSMITH_IMPLEMENTATION_DIRECTIVE.md` | `THREADSMITH_IMPLEMENTATION_DIRECTIVE.md` | recovered | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Exact zero-byte object; substantive content remains missing. |

## Recovered artifact retained outside the tree

| Supplied filename | Status | SHA-256 | Notes |
|---|---|---|---|
| `lattice_reference-0.1.0-py3-none-any(3)(1).whl` | recovered reference only | `f6643d5534d2bacb96ca20566c401bf0ffaabec4c29768d4293389052f349ef5` | Archive and RECORD verified. Excluded from the public tree because original path, licence, and redistribution provenance are unresolved. |

## Reconstructed files

| Repository path | Status | Reason |
|---|---|---|
| `.gitignore` | reconstructed | Keeps Cargo build output outside the baseline. |
| `Cargo.lock` | reconstructed | Required by the recovered ADR for locked and offline verification. |
| `rust-toolchain.toml` | reconstructed | Exact pin values are stated by the recovered ADR. |
| `crates/threadsmith-schema/Cargo.toml` | reconstructed | Required to load the recovered schema source as the evidenced workspace member. |
| `crates/threadsmith-canonical/Cargo.toml` | reconstructed | Required to load the evidenced canonical workspace member. |
| `crates/threadsmith-canonical/src/lib.rs` | reconstructed | Minimum canonical bytes, digest, non-authoritative typed preimage claim, claim verification, and absent-preimage boundary. It does not select artifact-specific preimages. |
| `crates/threadsmith-canonical/tests/pc1_conformance.rs` | reconstructed | Executes the reconstructed vectors and recovered PC1 model through public APIs. |
| `conformance/foundation/canonical_vectors.json` | reconstructed | Replaces missing canonical-preimage vector evidence with explicitly labelled oracle-cross-checked fixtures. |
| `DECISIONS.md` | reconstructed | Preserves recovery decisions and boundaries. |
| `IMPLEMENTATION_PLAN.md` | reconstructed | Preserves the bounded gate sequence and PC2 exclusion. |
| `PROJECT_STATE.md` | reconstructed | Preserves restoration state between sessions. |
| `RESTORATION_INVENTORY.md` | reconstructed | Separates recovered, reconstructed, and missing material. |
| `docs/VERIFICATION_REPORT.md` | reconstructed | Records executed command and result evidence. |
| `docs/ACCEPTANCE_REVIEW.md` | reconstructed | Records the separate read-only review, bounded repair, and fresh acceptance. |
| `SHA256SUMS` | reconstructed | Complete committed-tree checksum manifest, excluding itself to avoid self-reference. |

Stable source hashes are recorded in `docs/VERIFICATION_REPORT.md`; every final tree file except the checksum manifest itself is recorded in `SHA256SUMS`.

## Missing and unresolved evidence

| Missing item | Status | Consequence |
|---|---|---|
| Lost Git history and original baseline commit | missing | The new commit is a provenance anchor, not recovered history. |
| Lattice Standard 0.3 normative document | missing | No replacement is fabricated; reconstruction is bounded to converging supplied evidence. |
| Substantive implementation directive | missing | The supplied zero-byte object supplies no semantic or scope authority. |
| Original canonical crate bytes and manifests | missing | Their replacements are explicitly reconstructed. |
| Original `Cargo.lock`, tests, and conformance vectors | missing | Exact historical dependency resolution and suite breadth cannot be claimed. |
| Original paths for the ADR, model, schema source, and wheel | missing | Every inferred placement is labelled reconstructed. |
| ThreadSmith licence and legacy-wheel redistribution provenance | missing | No licence is invented and the wheel is not committed. |
| Artifact-specific canonical preimage rules and original identity vectors | missing | Generic canonical preimage mathematics is requalified, but blueprint and manifest artifact identities remain unresolved as the recovered PC1 model requires. |
| Migration outcome-to-next-action constraint | unresolved recovered behavior | The exact recovered schema permits combinations not constrained by outcome; receipts remain non-authoritative. |

Byte-exact restoration of the repository is false. PC2 has not started.
