# PC2 Parser Dependency Intake

Status: frozen for PC2 implementation intake on 2026-07-22.

This record is preparation for PC2. It does not add a dependency, create a parser, create `threadsmith-compiler`, or begin PC2 implementation. The accepted Foundation/PC1 baseline remains commit `f61beef39129013ae439fbef917636779d5231eb`, tree `798bd917d3ed6f2a3ae8136d532ab671863bd001`.

## Selected path

PC2 implementation is to use the low-level event interface from `saphyr-parser` version `0.0.11`, fetched from crates.io with default features disabled. The future dependency declaration is frozen as:

```toml
saphyr-parser = { version = "=0.0.11", default-features = false }
```

The dependency belongs only to the future `threadsmith-compiler` crate. It must not be added to `threadsmith-schema` or `threadsmith-canonical`.

The selection is an event parser, not the higher-level `saphyr` value loader and not a Serde YAML deserializer. Events preserve the evidence needed to reject anchors, aliases, tags, complex keys, duplicate keys, and NFC key collisions before constructing a JSON-shaped tree. ThreadSmith, not the dependency, owns scalar interpretation, normalization, subset enforcement, diagnostics, and root validation.

| Property | Frozen intake result |
|---|---|
| Crate | `saphyr-parser` |
| Version | `0.0.11` exactly |
| Registry checksum | `ebfd783fcf1b3f6bafd557be0e1427ec54f826f513c3cdd749f9844484df2a13` |
| Upstream | `https://github.com/saphyr-rs/saphyr` |
| Release tag | `v0.0.11`; tag target commit `f606ac7ae9e222513dfb04f831bd8cabe87e870f` |
| Registry publication | 2026-07-11T08:42:26Z |
| Rust boundary | Pure Rust parser; MSRV 1.85.0; accepted workspace toolchain 1.97.1 |
| Normal direct dependencies | `arraydeque ^0.5.1`, `thiserror ^2.0.17` |
| Native/system dependencies | None |
| Build scripts | No direct parser build script; transitive Rust-only scripts in `thiserror`, `proc-macro2`, and `quote` invoke the pinned `rustc` for cfg/version probes; no C/C++ compiler or system-library probe found |
| Default features | Disabled; the crate currently declares no default feature |
| Licence | `MIT OR Apache-2.0`, with both inherited contributor licence sets required in redistributions |
| Workspace mutation in this tranche | None; `Cargo.toml` and `Cargo.lock` are unchanged |

## Candidate evaluation

| Candidate | Result | Reason |
|---|---|---|
| `saphyr-parser 0.0.11` | Selected | Active, narrowly scoped, pure Rust YAML 1.2 event parser. The event stream preserves syntax evidence before value-tree construction and has a small normal dependency graph. |
| `yaml-rust2 0.11.0` | Rejected | Pure Rust and stable, but it is in basic-maintenance mode and its high-level loader and broader dependency surface are unnecessary. Its low-level ancestry remains the fallback if the selected API fails qualification. |
| `saphyr 0.0.11` | Rejected | High-level YAML object loading performs work ThreadSmith must control itself and adds dependencies not needed for the parser boundary. |
| `granit-parser 1.0.0-rc.1` | Rejected | Technically promising pure-Rust event parser with spans, but only a release candidate and too new for the production boundary at this gate. |
| `serde-saphyr 1.0.0-rc.1` | Rejected | Release candidate and Serde-first. Direct deserialization would obscure the pre-tree checks required for duplicate keys, forbidden features, and ThreadSmith-owned scalar rules. |
| `serde_yaml 0.9.34+deprecated` | Rejected | Archived and explicitly unmaintained; depends on `unsafe-libyaml` and does not provide the desired controlled YAML 1.2 event boundary. |
| libyaml bindings | Rejected | C/native FFI and system-library provenance conflict with the portable Rust production boundary. |
| Python YAML parsers | Rejected | A Python parser dependency is explicitly forbidden and would violate the ordinary-application boundary. |

## Reproducibility and offline rule

The implementation tranche must add the exact direct pin above and commit the resulting `Cargo.lock`. Resolution must be performed with Rust/Cargo 1.97.1. CI and release checks must use `--locked`; after one authenticated fetch or vendoring step, all build and test checks must pass with `--locked --offline`. A release or source bundle must either carry a Cargo vendor directory with source replacement configuration or document the pre-populated Cargo cache procedure. No Git dependency, branch dependency, path override, system package, Python environment, or native compiler may enter the parser graph.

The intake probe resolved the following graph. These transitive versions are evidence from the 2026-07-22 probe, not a second hand-maintained lockfile; the future committed `Cargo.lock` is authoritative.

| Package | Probe version | crates.io checksum | Licence |
|---|---:|---|---|
| `saphyr-parser` | 0.0.11 | `ebfd783fcf1b3f6bafd557be0e1427ec54f826f513c3cdd749f9844484df2a13` | MIT OR Apache-2.0; two inherited notice sets |
| `arraydeque` | 0.5.1 | `7d902e3d592a523def97af8f317b08ce16b7ab854c1985a0c671e6f15cebc236` | MIT |
| `thiserror` | 2.0.19 | `09a43598840e33d5b0331f38c5e30d13bb11c11210a4b58f0d9b18a5a5eefcd9` | MIT OR Apache-2.0 |
| `thiserror-impl` | 2.0.19 | `43cbfe0cf76104d42a574802844187e84a305e531ed54455f11fbde0f10541cd` | MIT OR Apache-2.0 |
| `proc-macro2` | 1.0.107 | `985e7ec9bb745e6ce6535b544d84d6cd6f7ad8bd711c398938ae983b91a766d9` | MIT OR Apache-2.0 |
| `quote` | 1.0.47 | `1fbf4db142a473a8d80c26bbf18454ed458bf8d26c8219c331daecfdbd079001` | MIT OR Apache-2.0 |
| `syn` | 3.0.3 | `53e9bae58849f64dfa4f5d5ae372c8341f7305f82a3868709269343628b659a3` | MIT OR Apache-2.0 |
| `unicode-ident` | 1.0.24 | `e6e4313cd5fcd3dad5cafa179702e2b244f760991f45397d14d4ebf38247da75` | (MIT OR Apache-2.0) AND Unicode-3.0 |

## Safety and licence disposition

No selected package introduces native FFI or a system libyaml dependency. `arraydeque 0.5.1` contains internal Rust `unsafe` memory operations. The resolved derive graph also runs Rust build scripts from `thiserror`, `proc-macro2`, and `quote`; their sources and checksums are locked, and they invoke the selected `rustc` for cfg/version probes. The probe found no C/C++ compiler, pkg-config, cmake, or system-library invocation. These are pinned third-party implementation facts, not unpinned native FFI and not ThreadSmith source. They must remain visible in dependency review; any change in versions, features, sources, scripts, or graph reopens intake.

The selected and resolved licences are permissive. Distribution must reproduce both licence sets named by `saphyr-parser`, the MIT notice for `arraydeque`, the chosen MIT/Apache notices for the derive graph, and the Unicode-3.0 notice for `unicode-ident`. This does not choose or change the missing ThreadSmith project licence. If the future ThreadSmith licence makes any of these incompatible, dependency intake must reopen before implementation is accepted.

## Provenance sources

The controlling sources are the crates.io sparse-index entries and downloaded crate checksums, the released crate manifests and licence files, and the upstream release tag. Repository default-branch state was considered only for maintenance and API context; it is not a substitute for the pinned release.
