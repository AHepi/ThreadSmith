# PC4 Default-Phase Implementation Read-Only Review

Review date: 2026-07-22.

Review boundary: the public PC4 API in `threadsmith-compiler`, its focused
integration tests, all nine frozen fixtures, the accepted Standard and Default
Semantics Erratum, implementation evidence, and additive durable-state entries.
The review was performed as a separate read-only adversarial pass in the
primary workspace; no independent agent context was used.

## Review criteria

- the public result can be constructed only by consuming `ValidatedSource`;
- every insertion target and exact value matches the accepted freeze;
- object-member presence has absolute precedence over defaults;
- malformed and ambiguous data is preserved for later validation;
- traversal is bounded, deterministic, order-preserving, and idempotent;
- no provenance or source-presence data enters the identity-bearing value;
- no diagnostic, later-phase validation, canonicalization, identity, artifact,
  or authority enters PC4;
- tests exercise production code through public PC3-to-PC4 and
  PC2-to-PC3-to-PC4 paths; and
- accepted Foundation through PC3, Standard, erratum, dependency, and
  authority boundaries remain unchanged.

## Findings

| Severity | Finding | Resolution |
|---|---|---|
| P0 | None. | — |
| P1 | None. | — |
| P2 | None. | — |
| P3 | None. | — |

No repair cycle was required.

## Closure review

The read-only pass confirmed:

- `DefaultedSource.value` is private and its production constructor path is
  `apply_blueprint_defaults`;
- the implementation returns `DefaultedSource` directly and owns no semantic
  diagnostic;
- its target paths, inserted values, recognized unit kinds, and traversal
  order exactly match the frozen semantics;
- use of object-map entry presence preserves explicit empty, null, invalid,
  contradictory, and non-default values without interpretation;
- non-object elements and invalid nested containers are retained without
  recursive or convenience defaulting;
- all nine frozen fixtures use the public PC3-to-PC4 boundary with exact output,
  deterministic replay, and idempotence checks;
- a source-text test exercises the public PC2-to-PC3-to-PC4 pipeline;
- no dependency, Cargo, Foundation, PC1, PC2, PC3, Standard, erratum, ADR,
  canonicalization, digest, identity, Manifest, Binding, or runtime change
  exists; and
- formatting, workspace checks, Clippy, 43 tests, locked/offline dependency
  checks, fixture integrity, hash checks, and diff checks pass.

There are no open P0, P1, P2, or P3 findings. PC4 implementation is accepted
within the frozen `ValidatedSource -> DefaultedSource` boundary. This acceptance
does not authorize PC5 or any later compiler/runtime phase.
