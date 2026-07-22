# Lattice Standard 0.3

## Unified Harness Language, Core Semantics, and Small-Model Construction Profile

**Status:** Normative draft  
**Audience:** Compiler implementers, runtime implementers, harness designers, skill authors, and LLM-builder researchers  
**Purpose:** Define a language through which an LLM can construct a modular, deterministic, permissioned harness, while ensuring that neither the constructing model nor the operating model must be trusted to enforce the machine's rules.

The words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are normative.

---

# 0. Why this is one standard

Lattice previously separated a broad language design from a narrower canonical core. That separation was useful for staging, but it created a drift risk. This document contains the architecture, the buildable Core profile, and the small-model Construction profile in one versioned standard.

The profiles remain distinct, but their relationship is explicit and normative.

| Profile | Status in this document | Purpose |
|---|---|---|
| `lattice-core-0.1` | Fully normative | Smallest buildable compiler and runtime target |
| `lattice-builder-0.1` | Fully normative | Bootstrap protocol through which bounded LLMs construct Core Blueprints |
| `lattice-extended-0.2` | Architectural target only | Future first-class adapters, stores, runtime-nested harnesses, streaming, and additional brokers |

A compiler claiming `lattice-core-0.1` MUST reject Extended-only declarations. It MUST NOT silently lower them into Core declarations.

The explicit mapping is:

| Unit kind | Core 0.1 | Extended 0.2 |
|---|---:|---:|
| `program` | Yes | Yes |
| `model` | Yes | Yes |
| `gate` | Yes | Yes |
| `controller` | Yes | Yes |
| `broker` | Yes | Yes |
| `adapter` | No | Yes |
| `store` | No | Yes |
| `subharness` | No | Yes |

A Core Blueprint may explicitly implement translation as a `program` unit. This is not the same as a first-class `adapter`, and the compiler MUST NOT invent that lowering.

A Core Blueprint may import another module at compile time. Imported declarations are flattened and namespaced. This is not runtime `subharness` nesting.

A Core runtime may maintain its own event record and materialized state. User-declared `store` units are outside Core.

---

# 1. Design objective

Lattice is a language for manufacturing purpose-specific computational harnesses.

A harness may write under a style policy, parse a database export, process documents through stages, coordinate model calls, request bounded external effects, require human approval, or combine reusable modules.

The construction language is dynamic. A compiled harness is immutable for one version. Its execution may still contain declared conditions, bounded loops, retries, holds, optional branches, classifications, and variable data.

The central rule is:

> An LLM may propose the machine. Only the compiler may define the complete machine, and only a durable Run Binding may authorize its execution.

Lattice separates six layers.

| Layer | Owns | Does not own |
|---|---|---|
| Construction | Purpose decomposition, candidate declarations, local repair, and build progress | Runtime authority |
| Source | Editable Blueprint declarations | Dependency resolution or execution |
| Compilation | Resolution, expansion, validation, canonicalization, identity, and complete topology | Live state |
| Authority | Exact immutable Manifest and Run Binding | Semantic content |
| Execution | Scheduling, budgets, model calls, effects, and controller state | Harness redesign |
| Record | Events, blobs, receipts, replay, and derived state | Mutable policy |

A rule that exists only in prompt prose is guidance. A rule becomes Lattice policy only when the compiler or runtime can enforce it.

---

# 2. Required guarantees

A conforming Core implementation MUST provide these guarantees.

| Guarantee | Required meaning |
|---|---|
| Proposal is not authority | Blueprints and builder emissions cannot execute |
| Exact execution authority | Every run is bound to one durable Manifest identity |
| Deterministic compilation | Fixed source, packages, Lockfile state, and profile produce the same machine identity |
| Bounded model calls | Every model call uses fixed inputs, route, parser, contracts, and budgets |
| Mediated effects | Models cannot directly read files, call networks, execute programs, access secrets, or mutate external systems |
| Small contracts | Every port crossing is checked against a bounded contract |
| Deterministic routing | Routing uses declared metadata and closed predicates |
| Deny by default | Missing permission never becomes permission |
| Explicit failure | Validation, policy, budget, transport, quality, incompleteness, and integrity failures remain distinct |
| Replayable record | State is a fold over append-only committed events |
| Local composition | Replacements and additions cross explicit interfaces |
| Tested constructibility | Small-model constructibility is a benchmarked profile, not an assertion inferred from schema size |

Lattice guarantees structural validity, bounded authority, explicit policy, local composition, and replayable records.

Lattice does not guarantee that a harness is useful, that a subjective output is good, that a deterministic program is correct, or that a stable model judgment is true.

---

# 3. Durable artifacts

Lattice defines these artifacts.

| Artifact | Created by | Executable | Mutable |
|---|---|---:|---:|
| Skill Package | Human, tool, or package author | No | Versioned |
| Purpose Capsule | Human or authorized planning process | No | Frozen per construction session |
| Construction Workspace | Builder runtime | No | Append-only candidate state |
| Blueprint | Human or builder | No | Editable before compilation |
| Package Set | Package installer or project owner | No | Versioned |
| Lockfile | Compiler resolver | No | Replaced atomically by a later build |
| Compiled Manifest | Compiler | No by itself | Immutable |
| Qualification Record | Qualifier | No | Immutable |
| Run Binding | Authorized operator or binding service | Yes, as authority | Immutable |
| Event Record | Runtime | Historical only | Append-only |

These meanings MUST NOT be collapsed.

A caller-supplied in-memory Manifest or Binding may be used as an expected identity. It MUST be reconciled with the durable run-root artifact and MUST NOT override it.

The runtime MUST load and validate the durable Run Binding before constructing any provider adapter, broker, scheduler, token ledger, writable event record, or live state object.

---

# 4. End-to-end lifecycle

The normative lifecycle is:

```text
Skill packages and purpose
        |
        v
Bound builder bootstrap harness
        |
        v
Construction Workspace
candidate declarations, one bounded step at a time
        |
        v
Blueprint
        |
        v
Compiler resolution and checks
        |
        +--> Lockfile
        |
        v
Compiled Manifest
        |
        v
Qualification scenarios
        |
        +--> Qualification Record
        |
        v
Durable Run Binding
        |
        v
Runtime execution
        |
        v
Append-only Event Record and content-addressed blobs
```

A later addition changes the Blueprint or its imports. It produces a new Lockfile when resolution changes, a new Manifest identity, a new qualification result, and a new Run Binding.

The active Manifest is never edited in place.

---

# 5. Conformance classes

An implementation may claim these classes.

| Class | Required behavior |
|---|---|
| `source-reader` | Parse the restricted Core source profile |
| `compiler` | Resolve, normalize, expand, check, and emit canonical Lockfiles and Manifests |
| `qualifier` | Execute declared Core scenarios |
| `runtime` | Bind and execute Core Manifests |
| `replayer` | Reconstruct canonical state from event records |
| `builder-host` | Execute the Construction profile and maintain its candidate workspace |
| `full-core` | Implement every class except Extended-only features |

Different compiler implementations may use different languages, caches, data structures, and interfaces.

Given fixed normative inputs, conforming compilers MUST produce the same dependency identities, generated topology, declaration identities, Lockfile body, Manifest body, `lock_id`, and `manifest_id`.

Vendor behavior must be declared as an extension. A Core compiler MUST NOT silently apply it.

---

# 6. Source language overview

A Blueprint exposes eight declaration forms.

| Declaration | Meaning |
|---|---|
| `module` | A complete harness source module |
| `unit` | A bounded computational or control component |
| `port` | A named contracted endpoint inside a unit or module boundary |
| `contract` | A small crossing agreement |
| `link` | A data delivery or controller transition |
| `policy` | A deterministic permit or deny rule |
| `resource` | A pinned program, pack, route, scope, fixture, or reference |
| `scenario` | A qualification case |

A ninth declaration form requires a language-version change.

The Core compiler may lower these declarations into a richer internal representation. That internal form is not builder input and is not portable source.

---

# 7. Core project layout

A Core project uses this layout.

```text
project/
  lattice.yaml
  lattice.lock
  lattice.profile.json
  construction/
    purpose.json
    session.json
    events.jsonl
    candidates/
  packages/
    <package-name>/
      <version>/
        package.yaml
        files...
  build/
    <manifest-id>.manifest.json
    <manifest-id>.qualification.json
  runs/
    <run-id>/
      binding.json
      events.jsonl
      blobs/
        sha256/
          <first-two-hex>/
            <remaining-hex>
```

Core package resolution is local only.

Symlinks inside source, package, construction, and run trees are rejected.

A compiler MUST NOT read undeclared package files.

A builder-host MUST NOT write outside `construction/`.

---

# 8. Core source encoding

Source is UTF-8 without a byte-order mark. Line endings normalize to LF.

Core uses a restricted YAML 1.2 mapping profile that maps exactly to the JSON data model.

| Forbidden YAML feature | Reason |
|---|---|
| Anchors, aliases, and merge keys | Hidden graph or field insertion |
| Custom tags | Implementation-dependent semantics |
| Duplicate keys | Ambiguous values |
| Non-string mapping keys | Non-portable ordering |
| Floating-point values | Canonicalization ambiguity |
| Implicit dates or timestamps | Parser-dependent typing |
| Binary scalars | Hidden decoding behavior |
| Multiple YAML documents | Ambiguous root |
| Folded block strings using `>` | Easy to misread |
| Tabs for indentation | Parser inconsistency |

Permitted scalar types are string, signed 64-bit integer, boolean, and null.

Strings normalize to Unicode NFC after parsing.

Comments do not affect semantics or identity.

---

# 9. Names and versions

A local name matches:

```text
^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$
```

Names beginning with `__` are reserved for compiler-generated declarations.

A package name matches:

```text
^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$
```

A source-level imported symbol is written:

```text
<alias>::<local-name>
```

Versions use:

```text
MAJOR.MINOR.PATCH
```

Prerelease and build metadata are outside Core.

Version requirements are exact or caret ranges.

| Requirement | Allowed interval |
|---|---|
| `^M.m.p`, where `M > 0` | `>= M.m.p` and `< (M+1).0.0` |
| `^0.m.p`, where `m > 0` | `>= 0.m.p` and `< 0.(m+1).0` |
| `^0.0.p` | Exactly `0.0.p` |

---

# 10. Root Blueprint

The root mapping permits exactly these keys:

```text
lattice
profile
module
version
purpose
imports
inputs
contracts
resources
units
links
policies
exports
scenarios
```

The required keys are:

```text
lattice
profile
module
version
purpose
units
```

A Core Blueprint begins:

```yaml
lattice: "0.3"
profile: lattice-core-0.1
module: tiny_writer
version: "1.0.0"
purpose: |
  Turn a question into one structured answer.
units: []
```

Unknown keys are compile errors.

Missing optional list fields normalize to empty lists.

Declaration names are unique inside each declaration class.

A Blueprint using `adapter`, `store`, or `subharness` under `lattice-core-0.1` produces `PROFILE_UNSUPPORTED_UNIT_KIND`.

---

# 11. Modules and imports

A module is the unit of source packaging.

```yaml
module: database_ingest
version: "1.0.0"
purpose: |
  Convert a declared export into normalized records.
```

An import is:

```yaml
use: text_tools
version: "^1.2.0"
as: text
```

Imports are compile-time composition in Core.

Imported declarations receive the namespace:

```text
text::<local-name>
```

Transitive imports receive internal chained namespaces.

Import cycles are forbidden.

Imported module inputs and exports remain explicit boundaries. The compiler does not merge same-named declarations or infer cross-module links.

---

# 12. Local package format

A package contains `package.yaml`.

```yaml
package: text_tools
version: "1.3.1"
lattice: "0.3"
profiles:
  - lattice-core-0.1
module_file: module.yaml
files:
  - path: module.yaml
    sha256: "<hex>"
  - path: validators/no_bullets.py
    sha256: "<hex>"
```

Every file path is relative, uses `/`, contains no `.` or `..` segment, and names a regular file.

Every listed file MUST match its digest.

Unlisted files have no semantic existence and MUST NOT be read.

The canonical package descriptor sorts files by path. Timestamps, ownership, permissions, directory order, and absolute paths do not affect package identity.

---

# 13. Deterministic package resolution

The resolver applies this algorithm.

| Phase | Rule |
|---|---|
| Scan | Parse and validate every local package descriptor |
| Deduplicate | Same name and version with different identities is an error |
| Collect | Gather root and transitive version requirements |
| Reuse | Reuse an existing locked version when it satisfies every requirement and still exists |
| Select | Otherwise choose the numerically greatest available satisfying version |
| Restart | Restart resolution when a selected package introduces a new requirement |
| Finish | Stop when a complete pass changes nothing |
| Bound | More than 256 passes is an error |

Core selects one version per package name.

The resolver never fetches a package.

No common version produces `RESOLVE_NO_COMMON_VERSION`.

---

# 14. Lockfile

The compiler generates the Lockfile after successful resolution.

```json
{
  "lock_version": 1,
  "lattice": "0.3",
  "profile": "lattice-core-0.1",
  "root_blueprint_digest": "lattice:blueprint:sha256:...",
  "packages": [
    {
      "name": "text_tools",
      "version": "1.3.1",
      "package_id": "lattice:package:sha256:...",
      "requested_by": [
        {
          "module": "tiny_writer",
          "requirement": "^1.2.0"
        }
      ]
    }
  ],
  "lock_id": "lattice:lock:sha256:..."
}
```

Packages sort by package name.

`requested_by` sorts by module name and requirement.

`lock_id` is calculated with the `lock_id` field omitted.

The Lockfile is written atomically.

A builder never claims that resolution succeeded. Only the compiler creates or validates a Lockfile.

---

# 15. Canonical data and identity

Canonicalization operates on the parsed JSON data model after defined defaults.

| Value | Canonical rule |
|---|---|
| String | Unicode NFC |
| Integer | Base-ten signed integer with no leading zeroes |
| Boolean | `true` or `false` |
| Null | `null` |
| Array | Preserve semantic order unless a section declares sorting |
| Object | Sort keys by ascending UTF-8 byte sequence |

Canonical JSON emits no insignificant whitespace, byte-order mark, or trailing newline.

Non-ASCII characters remain UTF-8.

SHA-256 is calculated over canonical bytes.

Identities use:

```text
lattice:<kind>:sha256:<64 lowercase hexadecimal characters>
```

| Identity | Hash input |
|---|---|
| `blueprint_digest` | Root Blueprint after source defaults, before import expansion |
| `package_id` | Canonical package descriptor |
| `resource_id` | Normalized declaration and referenced content digests |
| `contract_id` | Normalized contract |
| `unit_id` | Normalized namespaced unit |
| `link_id` | Normalized link |
| `policy_id` | Normalized policy |
| `scenario_id` | Normalized scenario |
| `lock_id` | Lockfile with identity omitted |
| `manifest_id` | Manifest with identity and compiler implementation metadata omitted |
| `qualification_id` | Qualification Record with identity omitted |
| `binding_id` | Run Binding with identity omitted |
| `envelope_id` | Envelope with identity omitted |
| `event_id` | Event with identity omitted |

A permission, route, budget, validator, generated gate, contract, or policy change changes the relevant identity.

---

# 16. Compiler profile and source defaults

The Core profile contains:

```json
{
  "profile": "lattice-core-0.1",
  "contract_max_bytes": 4096,
  "declaration_max_bytes": 8192,
  "untrusted_payload_max_bytes": 1048576,
  "model_repair_max": 2,
  "control_loop_max_default": 3,
  "policy_default": "deny",
  "model_fallback_default": false,
  "commit_order": "activation_id_then_local_sequence"
}
```

Defaults are:

| Field | Default |
|---|---|
| Missing root list | Empty list |
| Input `required` | `true` |
| Input `cardinality` | `one` |
| Input `on_absence` | `block` |
| Output `cardinality` | `one` |
| Unit mode for `program`, `model`, and `gate` | `stateless` |
| Unit mode for `controller` | `event_sourced` |
| Unit mode for `broker` | `external` |
| Model `repair_attempts` | `0` |
| Link `mode` | `data` |
| Link `delivery` | `multicast` |
| Missing predicate | Constant `true` |
| Model fallback | `false` |
| Scenario `required` | `true` |

No other defaults exist.

Default expansion occurs before declaration hashing.

---

# 17. Contracts

A contract is a bounded crossing agreement.

```yaml
contract: answer
version: "1.0.0"
codec: json
shape:
  type: object
  properties:
    text:
      type: string
      min_length: 1
      max_length: 4000
  required:
    - text
  additional_properties: false
max_bytes: 8192
labels:
  integrity_at_least: syntactic
  instructionality: data
validators: []
assurance:
  - shape_validation
on_failure: ANSWER_INVALID
```

A canonical contract MUST NOT exceed `contract_max_bytes`.

Core codecs are:

```text
json
utf8
bytes
```

A JSON contract uses the Core shape language.

Supported shape keywords are:

```text
type
properties
required
additional_properties
items
min_items
max_items
min_length
max_length
minimum
maximum
enum
const
```

Supported JSON types are:

```text
object
array
string
integer
boolean
null
```

Unknown shape keywords are compile errors.

Validation reports the first failure in depth-first order. Object properties visit in UTF-8 key order. Array items visit by increasing index.

---

# 18. Labels and assurance

Lattice separates origin, integrity, confidentiality, and instructionality.

| Dimension | Closed values |
|---|---|
| Origin | `program`, `model`, `human`, `user`, `import`, `derived` |
| Integrity | `unverified`, `syntactic`, `validated`, `corroborated`, `deterministic` |
| Confidentiality | `public`, `internal`, `restricted`, `secret` |
| Instructionality | `instruction`, `reference`, `data` |

Integrity and confidentiality are ordered. Origin and instructionality are categories.

External text defaults to `data`.

Passing validation does not convert data into instruction.

A stronger integrity label may be emitted only by a unit whose contract names the assurance that justifies it.

Core assurance kinds are:

| Assurance | Meaning |
|---|---|
| `shape_validation` | Payload matches the declared shape |
| `deterministic_validator` | A pinned deterministic validator accepted it |
| `same_impl_recompute` | The same implementation reproduced it |
| `fixture_test` | A named test accepted it |
| `perturbation_consistency` | A model judgment remained stable under a named variation |
| `human_approval` | An authorized human approved the exact payload |

`same_impl_recompute` proves repeatability under the same implementation, not correctness.

`perturbation_consistency` proves stability under the named variation, not truth.

---

# 19. Resources

Core resource kinds are:

```text
program
validator
pack
model_route
filesystem_scope
fixture
reference
```

A resource declaration pins a path and digest.

```yaml
resource: writer_pack
kind: pack
path: packs/writer.json
sha256: "<hex>"
```

A resource file must be listed in the root project or a selected package and must match its digest.

A Core compiler does not execute resources during ordinary compilation.

Qualification and runtime may execute permitted resources through the runtime boundary.

---

# 20. Units and ports

Core unit kinds are `program`, `model`, `gate`, `controller`, and `broker`.

The only legal kind and mode pairs are:

| Kind | Mode |
|---|---|
| `program` | `stateless` |
| `model` | `stateless` |
| `gate` | `stateless` |
| `controller` | `event_sourced` |
| `broker` | `external` |

A unit performs one bounded responsibility.

```yaml
unit: writer
kind: model
inputs:
  - port: question
    contract: question
outputs:
  - port: answer
    contract: answer
role: draft
pack: writer_pack
response_contract: answer
repair_attempts: 1
limits:
  model_calls: 1
  input_tokens: 2000
  output_tokens: 1000
```

Input cardinalities are:

```text
one
optional
many
```

Absence policies are:

```text
block
fail
explicit_none
literal_default
```

A required `one` input has exactly one producer.

A `many` input orders values by producer identity and envelope identity.

The runtime does not fabricate semantic substitutes for missing upstream values.

---

# 21. Program, model, gate, controller, and broker boundaries

A `program` is deterministic and effect-free. It receives declared envelopes and emits declared payloads.

A `model` receives one deterministic rendered pack and returns one structured response. It has no direct tools or ambient memory.

A `gate` validates data or makes a policy-controlled crossing.

A `controller` schedules declared workflow states. It cannot alter contracts, permissions, budgets, policies, or the Run Binding.

A `broker` is the only Core unit permitted to perform an external effect.

The required tool pattern is:

```text
model output request
        |
        v
request contract
        |
        v
gate and policy
        |
        v
broker
        |
        v
recorded result envelope
```

A model unit declaring filesystem, network, process, environment, database, or secret authority is a compile error.

---

# 22. Pack rendering

A pack resource is provider-neutral JSON.

```json
{
  "instruction": "Answer the supplied question. Return JSON only.",
  "fields": [
    {
      "name": "question",
      "from": "input.question",
      "render": "json"
    }
  ]
}
```

Fields render in listed order.

The runtime produces:

```json
{
  "instruction": "<compiler-pinned instruction>",
  "fields": [
    {
      "name": "<name>",
      "instructionality": "data",
      "content": "<rendered value>"
    }
  ]
}
```

Data and reference content remain structurally separate from instruction content.

The model receives no undeclared conversation history, hidden files, ambient memory, or unrecorded system prompt.

The exact provider-neutral pack and exact provider request bytes are stored before provider invocation.

---

# 23. Model-call transaction

Every model attempt follows this lifecycle.

```text
Eligible
Prepared
Authorized
Reserved
Issued
Exposed
Attempted
Terminated
Parsed
Validated
Admitted
```

A failure replaces the remaining suffix with one terminal outcome.

```text
Rejected
Denied
Exhausted
TransportFailed
Cancelled
IntegrityFailed
```

| Event | Meaning |
|---|---|
| `Eligible` | Inputs and controller state permit activation |
| `Prepared` | Exact inputs, pack, parser, role, and limits are fixed |
| `Authorized` | Manifest, route, and policy checks pass |
| `Reserved` | Budgets are durably reserved |
| `Issued` | Durable work identity is committed |
| `Exposed` | Exact rendered context and provider request identities are committed |
| `Attempted` | Provider invocation began |
| `Terminated` | Provider invocation ended and raw bytes or transport failure were recorded |
| `Parsed` | Raw bytes were parsed or parse failure recorded |
| `Validated` | Contract validation completed |
| `Admitted` | A valid output envelope was committed |

`Attempted` MUST NOT occur before durable `Issued` and `Exposed`.

`Admitted` MUST NOT occur before successful `Validated`.

A planned pack does not prove exposure.

An in-memory work ticket does not prove issuance.

A provider response that fails parsing or validation is not semantic output.

---

# 24. Model response and repair

Core model responses contain exactly one UTF-8 JSON value.

Markdown fences, leading prose, trailing prose, comments, and heuristic extraction are forbidden.

A parse or contract failure may trigger bounded repair.

The repair pack is:

```json
{
  "original_pack_ref": "blob:...",
  "error": {
    "code": "<diagnostic-code>",
    "path": "<canonical-path>",
    "message": "<bounded-message>"
  },
  "attempt": 1
}
```

The error message is limited to 512 Unicode scalar values.

Each retry receives a new attempt identity under the same work identity.

Fallback is disabled unless the Run Binding explicitly pins an ordered fallback list.

---

# 25. Policies

Policies are deterministic expressions over canonical metadata.

```yaml
policy: deny_secret_write
scope: broker_request
when:
  all:
    - eq: [request.effect, "fs.write"]
    - in: [request.payload.confidentiality, [restricted, secret]]
decision: deny
code: SECRET_WRITE_DENIED
```

Core operators are:

```text
all
any
not
eq
neq
in
glob
lt
lte
gt
gte
has
```

Missing paths produce `MISSING`.

Every comparison involving `MISSING` is false except `has`.

`all` over an empty list is true.

`any` over an empty list is false.

Policies evaluate in ascending `policy_id` order.

Decision semantics are deny-overrides:

```text
any matching deny        -> deny
no matching deny and
at least one permit      -> permit
otherwise                -> deny
```

Declaration order never changes policy meaning.

---

# 26. Links and routing

A link connects one output port to one input port.

```yaml
link: writer_to_checker
from: writer.answer
to: checker.answer
mode: data
delivery: multicast
```

Core link modes are:

```text
data
transition
```

Delivery modes are:

```text
multicast
exclusive
```

Exclusive links belong to a named group.

Exactly one exclusive route must match.

Zero matches produce `ROUTE_NO_MATCH`.

Multiple matches produce `ROUTE_AMBIGUOUS`.

A route predicate may inspect:

```text
envelope.header
controller.state
run.mode
```

It may not inspect arbitrary payload text.

Semantic routing uses a model or program unit to emit a closed label. The router then reads that label from declared metadata.

---

# 27. Controllers and bounded loops

A controller is a finite-state machine.

```yaml
unit: writing_flow
kind: controller
states:
  - start
  - draft
  - review
  - complete
  - incomplete
initial: start
terminal:
  - complete
  - incomplete
transitions:
  - from: start
    to: draft
    on: envelope:question
  - from: draft
    to: review
    on: activation_admitted:writer
  - from: review
    to: draft
    on: envelope:revise
    max_visits: 2
  - from: review
    to: complete
    on: envelope:accept
```

For a state and trigger, exactly one matching transition is taken.

Zero matches leaves the controller waiting.

Multiple matches produce `CONTROL_AMBIGUOUS` and an integrity failure.

Every directed cycle must contain a bounded transition.

Crossing beyond `max_visits` produces `incomplete` when that terminal state exists, otherwise `CONTROL_BOUND_EXHAUSTED`.

Controller state is derived from transition events.

---

# 28. Filesystem broker

Core supports:

```text
fs.read
fs.write
```

A filesystem scope declares read and write globs and safety policy.

Before every effect, the broker:

```text
normalizes separators
rejects empty, dot, and parent segments
resolves without following symlinks
verifies the target remains inside the run root
rejects device files
checks the declared scope
checks broker policy
checks budgets
```

Inspection failure is denial, not proof of absence.

Read bytes are recorded by content identity.

A write request includes an idempotency key and expected prior state.

Atomic write uses temporary file plus rename. If the platform cannot provide required atomicity, the runtime returns `FS_ATOMICITY_UNAVAILABLE`.

---

# 29. Budgets

Budgets are finite integers.

Core budget keys are:

```text
logical_steps
model_calls
input_tokens
output_tokens
effect_calls
payload_bytes
wall_time_safety_ms
```

The Run Binding declares global maxima.

A unit activation reserves no more than the minimum of its declared limit and the remaining global budget.

Reservations are atomic and durable.

Unused reservation is released through an event.

Logical budgets determine deterministic stopping.

Wall time is a safety control and does not establish deterministic replay.

Budget exhaustion is an explicit terminal outcome, not record corruption.

---

# 30. Scheduling

An activation is one execution of one unit against one complete input set in one controller epoch.

Its identity includes:

```text
manifest identity
unit identity
controller epoch
ordered input envelope identities
```

A unit becomes eligible when its controller state permits it, required inputs are satisfied, the same activation has not terminated, and its budget can potentially be reserved.

The reference scheduler is sequential and chooses the lexicographically smallest eligible activation identity.

A concurrent runtime may compute speculatively, but event commits MUST be equivalent to the reference order.

---

# 31. Envelopes and events

An envelope is immutable.

```json
{
  "envelope_id": "lattice:envelope:sha256:...",
  "header": {
    "contract_id": "lattice:contract:sha256:...",
    "kind": "answer",
    "producer": "lattice:unit:sha256:...",
    "activation_id": "lattice:activation:sha256:...",
    "sequence": 18,
    "labels": {
      "origin": "model",
      "integrity": "validated",
      "confidentiality": "internal",
      "instructionality": "data"
    }
  },
  "payload_ref": "blob:sha256:...",
  "codec": "json"
}
```

Events are canonical JSON objects, one per line.

```json
{
  "sequence": 42,
  "event_id": "lattice:event:sha256:...",
  "event_type": "Admitted",
  "run_id": "run-001",
  "manifest_id": "lattice:manifest:sha256:...",
  "binding_id": "lattice:binding:sha256:...",
  "unit_id": "lattice:unit:sha256:...",
  "activation_id": "lattice:activation:sha256:...",
  "parents": ["lattice:event:sha256:..."],
  "inputs": [],
  "outputs": ["lattice:envelope:sha256:..."],
  "receipt_ref": "blob:sha256:..."
}
```

Sequence starts at zero and increases by one.

Every event after zero includes the immediately preceding event identity as a parent.

The runtime treats authority-bearing events as committed only after durable persistence.

A truncated final line may be ignored only when it contains no complete JSON value. Any other malformed event is `RECORD_CORRUPT`.

---

# 32. Replay

The event record is authoritative.

Materialized state is a pure fold over known event types.

Core distinguishes:

| Mode | Meaning |
|---|---|
| Record replay | Rebuild state from committed events and blobs |
| Deterministic reexecution | Re-run pinned deterministic units and compare outputs |
| Live rerun | Start a new run against current providers or external state |

Record replay is required.

Deterministic reexecution is required for units claiming deterministic integrity.

A live rerun is not replay.

Model raws, file-read bytes, provider requests, operator inputs, and other external observations are recorded when they influence committed state.

A model call is never reissued during record replay.

---

# 33. Qualification

Compilation proves structural conformance.

Qualification executes scenarios.

Core scenario kinds are:

```text
fixture
adversarial
replay
budget
compatibility
construction
```

Scenarios run in ascending `scenario_id` order.

A required scenario failure prevents qualification.

A Qualification Record binds results to one exact Manifest and profile.

A Run Binding may require one exact Qualification Record.

The source cannot declare itself qualified.

---

# 34. Run Binding

A Run Binding authorizes one exact run configuration.

```json
{
  "run_id": "run-001",
  "manifest_id": "lattice:manifest:sha256:...",
  "qualification_id": "lattice:qualification:sha256:...",
  "profile": "lattice-core-0.1",
  "runtime_abi": "lattice-core-runtime-0.1",
  "routes": {
    "draft": "lattice:resource:sha256:..."
  },
  "budgets": {
    "logical_steps": 100,
    "model_calls": 4,
    "input_tokens": 12000,
    "output_tokens": 4000,
    "effect_calls": 8,
    "payload_bytes": 10485760
  },
  "run_root": "root:...",
  "fallback": false,
  "binding_id": "lattice:binding:sha256:..."
}
```

Every used role must resolve to an exact route resource.

The binding cannot weaken a non-overridable policy or exceed Manifest maxima.

---

# 35. Compilation pipeline

A Core compiler executes these phases.

| Phase | Output |
|---:|---|
| Read | Source bytes |
| Parse | Restricted YAML data |
| Source validate | Valid root shape |
| Default | Expanded source defaults |
| Digest | Blueprint identity |
| Package scan | Valid local package set |
| Resolve | Exact versions |
| Lock | Canonical Lockfile |
| Expand | Namespaced imports |
| Normalize | Resolved declaration forms |
| Insert | Exact external intake gates |
| Static check | Cross-declaration validity |
| Identify | Declaration identities |
| Sort | Canonical collections |
| Manifest | Complete canonical machine |
| Persist | Atomic Manifest file |

For each external module input, Core inserts exactly one intake gate and its explicit links.

The gate applies payload-size, codec, shape, validator, and label-flow checks.

Generated declarations appear in the Manifest before hashing.

Core inserts no other unit or adapter automatically.

A compile failure produces no partial Manifest.

---

# 36. Core static errors

A compiler MUST use stable error codes for at least these conditions.

| Code | Meaning |
|---|---|
| `SOURCE_UNKNOWN_KEY` | Unknown source field |
| `SOURCE_FORBIDDEN_YAML` | Forbidden YAML feature |
| `SOURCE_DUPLICATE_NAME` | Duplicate declaration name |
| `PROFILE_UNSUPPORTED_UNIT_KIND` | Extended-only unit used under Core |
| `RESOLVE_DUPLICATE_VERSION` | Same package version, different identity |
| `RESOLVE_NO_COMMON_VERSION` | No version satisfies all requirements |
| `RESOLVE_IMPORT_CYCLE` | Import cycle |
| `NAMESPACE_COLLISION` | Expanded declaration collision |
| `CONTRACT_TOO_LARGE` | Contract exceeds cap |
| `CONTRACT_INVALID_SHAPE` | Invalid shape |
| `PORT_UNBOUND_REQUIRED` | Required port has no producer |
| `PORT_TOO_MANY_PRODUCERS` | Non-many port has multiple producers |
| `LINK_CONTRACT_INCOMPATIBLE` | Producer and consumer contracts conflict |
| `LINK_LABEL_FLOW_DENIED` | Label flow is not permitted |
| `ROUTE_AMBIGUOUS` | Multiple exclusive routes may match |
| `CONTROL_UNBOUNDED_CYCLE` | Controller cycle lacks a bound |
| `POLICY_UNKNOWN_OPERATOR` | Unsupported policy operator |
| `MODEL_DIRECT_EFFECT` | Model declares ambient authority |
| `BROKER_UNSUPPORTED_EFFECT` | Broker effect outside profile |
| `RESOURCE_HASH_MISMATCH` | Resource bytes do not match |
| `BUDGET_INVALID` | Budget is invalid or exceeds parent |
| `SECRET_IN_SOURCE` | Secret value appears where only a handle is permitted |
| `ABI_INCOMPATIBLE` | Runtime or profile mismatch |

Additional diagnostics are permitted. Core error meanings may not be changed.

---

# 37. Compiled Manifest identity

The Manifest contains:

```text
manifest_version
lattice
profile
module
module_version
blueprint_digest
lock_id
profile_values
contracts
resources
units
links
policies
inputs
exports
scenarios
compiler
manifest_id
```

Collections sort by item identity.

The compiler field records implementation name and version.

Compiler implementation metadata does not affect `manifest_id`.

This permits independent compiler implementations to emit the same machine identity.

---

# 38. Construction Profile overview

`lattice-builder-0.1` is a first-class normative profile.

Its purpose is not merely to allow small declarations. Its purpose is to define the process through which a bounded model can construct a complete Core harness without reading or holding the entire standard.

The builder itself is a hand-authored, pre-qualified Core harness.

That bootstrap harness is the trusted seed. It may be approximately small, but its size is not a semantic guarantee. Its exact Manifest identity MUST be published with the builder implementation.

The builder model never receives runtime authority over the harness being built.

It may write only candidate declarations into the Construction Workspace.

Only the ordinary Core compiler can turn the resulting Blueprint into a Manifest.

---

# 39. Builder bootstrap boundary

The bootstrap builder contains these fixed components.

| Component | Responsibility |
|---|---|
| Purpose intake gate | Validate and freeze the Purpose Capsule |
| Pass controller | Enforce construction order |
| Inventory renderer | Produce a compact view of accepted candidates |
| Gap selector | Choose one compiler-grounded missing item |
| Pack renderer | Build one bounded builder pack |
| Builder model unit | Emit one candidate action |
| Candidate parser | Parse exact structured output |
| Candidate validator | Validate the emitted declaration against its target schema |
| Candidate registrar | Append accepted candidates idempotently |
| Diagnostic selector | Return one canonical primary error |
| Replan gate | Permit local replanning after retry exhaustion |
| Blueprint assembler | Render accepted candidate state into source |
| Compiler bridge | Invoke the ordinary compiler as a program boundary |
| Qualification bridge | Invoke required scenarios |
| Completion gate | Declare construction complete only after compiler and qualification success |

The builder model cannot select its own target schema, active pass, compiler diagnostic, budget, or candidate registration result.

---

# 40. Purpose Capsule

Construction starts with a frozen Purpose Capsule.

```json
{
  "goal": "Produce clear explanatory prose from one question and supplied references.",
  "non_goals": [
    "Do not browse the network.",
    "Do not invent citations."
  ],
  "inputs": [
    {
      "name": "question",
      "description": "A user question."
    },
    {
      "name": "references",
      "description": "Optional supplied reference documents."
    }
  ],
  "outputs": [
    {
      "name": "answer",
      "description": "Structured explanatory prose."
    }
  ],
  "permitted_effects": [],
  "required_properties": [
    "No direct model tools.",
    "No unsupported citation."
  ],
  "required_scenarios": [
    "valid question",
    "malformed model output",
    "instruction embedded in reference data"
  ],
  "construction_profile": "lattice-builder-0.1"
}
```

The Purpose Capsule is content-addressed and frozen at session start.

A purpose change creates a new construction session.

The builder cannot remove non-goals, permitted-effect restrictions, or required scenarios.

---

# 41. Construction Workspace

The workspace is append-only candidate state.

```text
construction/
  purpose.json
  session.json
  events.jsonl
  candidates/
    <candidate-id>.json
  rejected/
    <attempt-id>.json
  rendered/
    lattice.yaml
```

An accepted candidate is not runtime authority.

The workspace state is a fold over construction events.

The required construction events are:

```text
SessionStarted
PassEntered
GapSelected
PackRendered
BuilderAttempted
CandidateParsed
CandidateRejected
CandidateAccepted
CandidateNoOp
RepairRequested
StepExhausted
ReplanSelected
PassCompleted
BlueprintRendered
CompileAttempted
CompileFailed
CompilePassed
QualificationAttempted
QualificationFailed
QualificationPassed
ConstructionCompleted
ConstructionIncomplete
```

A builder-host must recover the same candidate state after interruption.

---

# 42. Construction passes

The pass sequence is fixed.

| Pass | Permitted emission |
|---|---|
| `scope` | Module boundary, module inputs, module exports |
| `skeleton` | One controller outline or one bounded unit placeholder |
| `contracts` | One contract |
| `resources` | One resource declaration |
| `units` | One complete unit |
| `links` | One link or one related link set |
| `policies` | One policy |
| `scenarios` | One scenario |
| `compile_repair` | One local declaration replacement required by a compiler error |
| `qualification_repair` | One local declaration replacement required by a failed scenario |

The builder MUST NOT emit a complete harness in one response.

The builder MUST NOT emit more than one unit per response.

A link set may contain no more than eight links and must share one declared purpose, such as wiring one unit's outputs.

The pass controller, not the model, determines when a pass is complete.

A later pass may reference accepted earlier declarations.

A later pass may replace an earlier declaration only through an explicit repair action.

---

# 43. Atomic construction step

One builder call fills one locally defined gap.

The step lifecycle is:

```text
select one gap
render one pack
call builder model
parse one action
validate one candidate
accept, no-op, or reject
return one error when rejected
retry within bound
replan locally after exhaustion
continue
```

No conversation history is supplied.

The builder pack is the model's complete world for that step.

---

# 44. Builder pack

The provider-neutral builder pack is:

```json
{
  "protocol": "lattice-builder-0.1",
  "session_id": "lattice:construction-session:sha256:...",
  "purpose_ref": "blob:sha256:...",
  "pass": "contracts",
  "inventory": {
    "module": "clear_explainer",
    "inputs": ["question", "references"],
    "exports": ["answer"],
    "contracts": [
      {
        "name": "question",
        "id": "lattice:contract:sha256:...",
        "summary": "JSON object containing one nonempty text field."
      }
    ],
    "resources": [],
    "units": [],
    "links": [],
    "policies": [],
    "scenarios": []
  },
  "gap": {
    "code": "MISSING_OUTPUT_CONTRACT",
    "description": "Define the structured answer contract.",
    "acceptance": [
      "The contract must use the Core JSON shape subset.",
      "The canonical declaration must fit the contract byte cap."
    ]
  },
  "target": {
    "declaration_kind": "contract",
    "schema_ref": "lattice:schema:sha256:..."
  },
  "active_constraints": {
    "declaration_max_bytes": 8192,
    "contract_max_bytes": 4096,
    "allowed_unit_kinds": [
      "program",
      "model",
      "gate",
      "controller",
      "broker"
    ],
    "forbidden_effects": [
      "net.request",
      "process.exec"
    ]
  },
  "previous_error": null
}
```

The pack token limit defaults to 3000 tokens under the route's pinned tokenizer.

The pack renderer MUST fail rather than silently truncate required fields.

The inventory is a compact machine-generated projection, not a prose summary written by another model.

---

# 45. Inventory compression

The builder never receives the whole Blueprint unless the target declaration requires it and the pack remains within budget.

The inventory includes:

| Item | Included form |
|---|---|
| Module | Name and purpose code |
| Input and export | Name and contract reference |
| Contract | Name, identity, one-sentence machine-generated shape summary |
| Resource | Name, kind, identity |
| Unit | Name, kind, input port names, output port names |
| Link | Source, destination, mode |
| Policy | Name, scope, decision |
| Scenario | Name, kind, required flag |

A summary is generated from normalized structure using fixed templates.

The summary is not model-authored.

Items sort by declaration kind, then local name, then identity.

When inventory exceeds the pack budget, the renderer includes all declarations directly referenced by the gap, then their one-hop dependencies, then remaining declarations in canonical order until the limit. It emits `inventory_complete: false` and a digest of the omitted inventory.

A gap selector MUST NOT choose a task whose required dependencies would be omitted.

---

# 46. Builder output

The builder model returns exactly one JSON object.

Permitted actions are:

```text
emit
replace
replan
abstain
```

An emission is:

```json
{
  "action": "emit",
  "declaration_kind": "contract",
  "declaration": {
    "contract": "answer",
    "version": "1.0.0",
    "codec": "json",
    "shape": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "min_length": 1,
          "max_length": 4000
        }
      },
      "required": ["text"],
      "additional_properties": false
    },
    "max_bytes": 8192,
    "on_failure": "ANSWER_INVALID"
  }
}
```

A replacement additionally names the exact candidate identity being replaced.

A replan provides one closed replan label from the pack's permitted set.

An abstention states one closed reason code.

Markdown, commentary, multiple JSON values, and undeclared fields are invalid.

No rationale is required. The candidate declaration is the relevant output.

---

# 47. Bounded emissions

The default Construction limits are:

| Limit | Default |
|---|---:|
| Builder pack tokens | 3000 |
| Builder output tokens | 1800 |
| Candidate declaration bytes | 8192 |
| Contract bytes | 4096 |
| Units per call | 1 |
| Contracts per call | 1 |
| Policies per call | 1 |
| Scenarios per call | 1 |
| Related links per call | 8 |
| Repair attempts per step | 2 |
| Replans per gap | 2 |
| Total construction steps | Purpose-bound and finite |

A candidate exceeding a limit is rejected before registration.

Limits are pinned in the construction session.

A model cannot request larger limits.

---

# 48. Candidate validation and registration

Candidate processing occurs in this order.

```text
exact JSON parse
builder action schema
target declaration schema
profile support
source semantic checks local to the declaration
reference checks against accepted inventory
authority and purpose checks
canonicalization
candidate identity
idempotent registration
```

If the exact candidate identity already exists, the registrar emits `CandidateNoOp`.

If the same local name exists with different content and the action is not an authorized replacement, the candidate is rejected.

Accepted candidates are appended to the workspace and never silently mutated.

A replacement preserves the old candidate and appends a new active candidate relation.

The candidate registrar does not write a Manifest or Run Binding.

---

# 49. One-error feedback

A rejected builder attempt receives exactly one primary diagnostic.

Primary-error selection is deterministic.

Diagnostics sort by:

```text
phase priority
canonical source path
diagnostic code
canonical message hash
```

The phase priority is:

| Priority | Phase |
|---:|---|
| 1 | JSON parse |
| 2 | Builder action schema |
| 3 | Target declaration schema |
| 4 | Profile support |
| 5 | Forbidden authority or purpose violation |
| 6 | Name and reference validity |
| 7 | Contract and port compatibility |
| 8 | Policy and routing validity |
| 9 | Budget and boundedness |
| 10 | Other local semantic checks |

Only the first diagnostic is rendered into the next repair pack.

The full diagnostic set remains in the construction event record for audit, but it is not shown to the builder model during that repair step.

Two conforming compiler bridges MUST select the same primary error from the same diagnostic set.

---

# 50. Repair

A repair pack is the original builder pack plus:

```json
{
  "previous_error": {
    "code": "CONTRACT_INVALID_SHAPE",
    "path": "declaration.shape.required[0]",
    "message": "Required property 'text' is absent from properties.",
    "attempt": 1
  }
}
```

Only the first error is supplied.

The model receives at most two repair attempts by default.

A repair must address the same gap.

It may not widen authority, remove a required scenario, weaken a non-goal, or change the Purpose Capsule.

A valid repaired declaration enters normal registration.

---

# 51. Replanning after exhaustion

After repair attempts are exhausted, the builder does not continue repeating the same prompt.

The gap selector provides a closed set of local replan choices.

Example:

```json
{
  "permitted_replans": [
    "split_contract",
    "replace_unit_shape",
    "add_program_validator",
    "mark_requirement_advisory",
    "declare_incomplete"
  ]
}
```

A replan changes the local construction strategy, not the purpose.

The following replans are forbidden unless an authorized Purpose Capsule delta exists:

```text
add a new external effect
remove a required scenario
weaken a deny policy
increase global budgets
permit model tools
change an external output contract
discard accepted evidence of failure
```

After the replan bound is exhausted, the session records `ConstructionIncomplete`.

Incomplete construction is a valid, visible outcome.

---

# 52. Pass completion

A pass completes only when its machine-checkable completion predicate is true.

| Pass | Completion predicate |
|---|---|
| `scope` | Every declared input and export has a name and contract gap |
| `skeleton` | Every required responsibility maps to a unit or controller gap |
| `contracts` | Every port and module boundary resolves to a contract |
| `resources` | Every implementation, pack, fixture, and scope reference resolves |
| `units` | Every skeleton unit is complete and profile-valid |
| `links` | Every required input is connected or has explicit absence behavior |
| `policies` | Every effect and authority crossing has a decision path |
| `scenarios` | Every Purpose Capsule required scenario has a source declaration |
| `compile_repair` | The ordinary Core compiler succeeds |
| `qualification_repair` | Every required scenario passes |

The model cannot emit `pass_complete`.

The pass controller derives completion from candidate state and compiler results.

---

# 53. Blueprint rendering

The Blueprint assembler renders active accepted candidates into canonical source order.

The source order is:

```text
root metadata
imports
inputs
contracts
resources
units
links
policies
exports
scenarios
```

Within a declaration class, items sort by local name and then candidate identity.

Rendering is deterministic.

The rendered Blueprint is ordinary non-authoritative Core source.

A human may inspect or edit it. A human edit creates a new candidate event or a new construction session according to builder-host policy. It is never silently merged.

---

# 54. Compiler and qualification bridge

After source rendering, the builder-host invokes the ordinary Core compiler.

The builder model does not receive authority to declare compilation success.

A compile failure returns one canonical primary compiler error into `compile_repair`.

A successful compile produces an ordinary Lockfile and Manifest.

Qualification then runs required scenarios.

A scenario failure returns one bounded machine-readable failure into `qualification_repair`.

The builder may propose a local source replacement.

It may not edit the qualification result or delete the failing required scenario.

Construction completes only when:

```text
the Blueprint compiles
the exact Manifest is persisted
every required construction and runtime scenario passes
a Qualification Record is persisted
the Completion gate records ConstructionCompleted
```

Creating a Run Binding is outside the builder's authority unless a separate authorized binding service is invoked.

---

# 55. Skill compilation

A skill package may contain:

```text
machine-readable schemas
programs and validators
pack templates
fixtures
reference material
conventions
```

The builder classifies each skill item.

| Skill content | Candidate Lattice form |
|---|---|
| Executable with declared interface | Program or validator resource |
| Machine-checkable rule | Contract validator or policy |
| Input-output example | Scenario |
| Reference document | Reference resource |
| Prompt template | Pack resource |
| Subjective convention | Advisory reference or quality scenario |
| Secret value | Rejected |
| Unbounded permission request | Rejected |

The builder does not decide that a subjective convention became enforceable merely because it appeared in `SKILL.md`.

Checkable content becomes executable only after normal compilation and qualification.

Uncheckable content remains visibly advisory.

A skill is not followed by the runtime model as an authority document.

---

# 56. Builder authority restrictions

The builder model has:

```text
no filesystem broker
no network broker
no process broker
no secret access
no Run Binding access
no Manifest mutation
no direct package installation
no compiler result authority
no qualification result authority
```

The builder-host may expose read-only pinned skill references through the pack renderer.

The builder model may propose resource declarations only for resources already present in the allowed package set or explicitly supplied project files.

A requested undeclared resource is rejected.

---

# 57. Construction replay and recovery

The Construction Workspace is event-sourced.

On restart, the builder-host:

```text
loads the frozen Purpose Capsule
validates the session profile and seed Manifest identity
replays construction events
reconstructs active candidates
reconstructs pass and gap state
resumes from the first uncommitted step
```

A model call is not reissued when its accepted or rejected result is already committed.

Re-emitting the same candidate is a no-op.

A crash after candidate bytes are written but before `CandidateAccepted` is committed leaves no accepted candidate. Recovery may safely retry.

---

# 58. Small-model constructibility benchmark

A project MUST NOT claim that Lattice is small-model constructible merely because declarations and packs are bounded.

The claim requires an executed benchmark using the actual Construction profile.

The benchmark release is versioned separately from language semantics:

```text
lattice-builder-benchmark-0.1
```

The benchmark contains at least 24 construction tasks across these domains.

| Domain | Minimum tasks |
|---|---:|
| Style-constrained writing | 4 |
| Structured document parsing | 4 |
| Data normalization | 4 |
| Staged pipeline processing | 4 |
| Governed tool requests | 4 |
| Module addition and compatibility repair | 4 |

Tasks include positive construction, malformed outputs, contradictory constraints, missing resources, bounded-loop design, and attempted authority widening.

Each task runs under at least four fixed random seeds or deterministic sampling variants when the route supports them.

The exact model, parameter count, active parameter count for mixture models, quantization, tokenizer, provider, sampling parameters, and context limit MUST be published.

---

# 59. Construction metrics

Every benchmark report includes:

| Metric | Meaning |
|---|---|
| Exact-response rate | Builder returned exactly one permitted JSON object |
| First-pass schema rate | First attempt passed the builder action and target schema |
| First-pass acceptance rate | First attempt was registered |
| Repair-survival rate | Rejected first attempts that became accepted within the repair bound |
| Replan-survival rate | Exhausted steps that succeeded through a permitted local replan |
| Declaration efficiency | Accepted declarations per builder call |
| Compiler-completion rate | Sessions producing a valid Core Manifest |
| Qualification-completion rate | Sessions passing every required scenario |
| Authority-widening attempt rate | Raw attempts to exceed Purpose or profile authority |
| Authority-widening admission count | Such attempts admitted by the builder-host |
| Median and tail pack tokens | Pack size distribution |
| Median and tail output tokens | Builder response size distribution |
| Construction calls | Total model calls per completed harness |
| Incomplete rate | Sessions ending visibly incomplete |
| Hidden intervention count | Human or frontier-model repairs not represented in the protocol |

Authority-widening admission count MUST be zero for a conforming builder-host. This measures enforcement, not model quality.

Failed sessions and traces MUST be preserved.

Cherry-picked successful runs are not a valid benchmark report.

---

# 60. Small-model qualification claims

A model-specific claim uses one of these labels.

| Claim | Requirement |
|---|---|
| `builder-protocol-conformant` | Builder-host passes protocol conformance with a deterministic mock builder |
| `builder-model-evaluated` | All benchmark metrics are published for the named model |
| `small-model-qualified` | The named model has no more than 8 billion active parameters and meets the benchmark release threshold |
| `4b-class-qualified` | The named model has no more than 4.5 billion active parameters and meets the benchmark release threshold |

The provisional benchmark-0.1 thresholds are:

| Metric | Threshold |
|---|---:|
| Exact-response rate | At least 90 percent |
| First-pass schema rate | At least 80 percent |
| Repair-survival rate | At least 80 percent |
| Compiler-completion rate | At least 75 percent |
| Qualification-completion rate | At least 65 percent |
| Authority-widening admission count | Zero |
| Hidden intervention count | Zero |
| Median builder pack | No more than 3000 route-tokenizer tokens |
| Ninety-ninth percentile builder pack | No more than 4000 route-tokenizer tokens |

These thresholds belong to the benchmark release and may be tuned from evidence without changing Core compilation meaning.

A claim made for one model, quantization, or context limit does not transfer automatically to another.

---

# 61. Construction conformance tests

A conforming builder-host must pass these cases.

| Test | Required result |
|---|---|
| Whole-harness output | Rejected because one atomic step was requested |
| Two units in one response | Rejected |
| Identical candidate re-emitted | CandidateNoOp |
| Same name, different content without replacement | Rejected |
| Multiple diagnostics | One canonical primary error returned |
| Compiler implementations with same diagnostics | Same primary error selected |
| Repair succeeds within bound | Candidate accepted |
| Repair bound exhausted | Local replan or visible incomplete result |
| Replan adds forbidden network access | Rejected |
| Required scenario deletion | Rejected |
| Crash before CandidateAccepted | No accepted candidate after recovery |
| Crash after CandidateAccepted | Candidate present exactly once after replay |
| Builder claims compile success | Ignored; compiler result governs |
| Builder claims qualification success | Ignored; qualifier result governs |
| Inventory truncation omits required dependency | Gap selection blocked |
| Skill subjective rule | Preserved as advisory, not silently enforced |
| Small model emits invalid JSON | One parse error returned, bounded retry |
| Completed construction without required scenarios | Impossible by completion predicate |

---

# 62. Adding modules after initial construction

A later addition is a new construction session with:

```text
the previous Blueprint or Manifest inventory
the original Purpose Capsule
an authorized Delta Capsule
the same or a compatible Construction profile
```

A Delta Capsule states what may change.

```json
{
  "base_manifest_id": "lattice:manifest:sha256:...",
  "goal": "Add supplied-reference fact checking before final formatting.",
  "allowed_changes": [
    "new contracts",
    "new resources",
    "new units",
    "new links",
    "new scenarios"
  ],
  "forbidden_changes": [
    "network access",
    "removal of citation validation",
    "increase of model fallback authority"
  ]
}
```

The builder emits new declarations and explicit replacements.

Existing declarations are not edited invisibly.

The compiler produces a new Manifest.

Old runs retain the old identity and record.

---

# 63. Composition under Core and Extended profiles

Core supports compile-time module imports.

This is enough for many reusable packages and modular additions.

Core does not provide independently running nested harnesses.

Extended 0.2 is intended to add:

| Extended kind | Intended responsibility |
|---|---|
| `adapter` | First-class contract translation with explicit loss declarations |
| `store` | User-declared event-sourced or transactional durable state |
| `subharness` | Runtime composition of independently compiled and bound harnesses |

Until canonical Extended semantics are published, these forms are architectural reservations only.

A Core compiler encountering them returns an unsupported-profile error.

This prevents two compilers from inventing different lowerings while claiming the same semantic target.

---

# 64. Standard examples

## 64.1 Clear-writing skill

A skill says:

```text
Use concise sentences.
Do not use bullet points.
Do not invent citations.
Explain unfamiliar terms.
Write clearly.
```

The builder may classify it as:

| Skill statement | Candidate machine form |
|---|---|
| No bullet points | Deterministic validator |
| Citation must exist in supplied references | Referential validator |
| Output must expose uncertainty | Contract field |
| Explain unfamiliar terms | Review scenario or advisory reference |
| Write clearly | Advisory reference and measurable proxies |

The builder constructs one contract, resource, unit, link, policy, or scenario per step.

The compiler checks the complete Blueprint.

The runtime model writes content but cannot disable validation, add network access, or certify its own output.

## 64.2 Database parser

A builder constructs:

```text
external upload intake
        |
        v
deterministic decoder
        |
        v
normalizer program
        |
        v
integrity gate
        |
        +--> rejection report
        |
        v
filesystem write broker
```

A model may propose mappings as data.

It never receives write authority.

Every rejected row remains recorded.

## 64.3 Later fact-check module

The existing harness exports a draft contract.

A Delta Capsule permits a new fact-check unit, decision contract, bounded revision transition, and scenarios.

The builder adds them incrementally.

The old Manifest remains unchanged.

The new Blueprint compiles to a new identity.

---

# 65. Required command-line surface

A full-core reference implementation exposes:

```text
lattice check <project>
lattice build <project>
lattice qualify <manifest>
lattice construct <project> --purpose <file>
lattice resume-construction <project>
lattice bind <manifest> --run-root <path>
lattice run <run-root>
lattice replay <run-root>
lattice benchmark-builder <benchmark> --route <route>
```

Required exit codes are:

| Code | Meaning |
|---:|---|
| 0 | Success |
| 2 | Source or compile error |
| 3 | Qualification failure |
| 4 | Binding failure |
| 5 | Runtime operational failure |
| 6 | Runtime integrity failure |
| 7 | Replay mismatch |
| 8 | Unsupported profile or extension |
| 9 | Construction incomplete |
| 10 | Builder benchmark threshold not met |

Machine-readable diagnostics use JSON Lines when requested.

---

# 66. Security boundary

Lattice describes and records authority. The operating system must enforce the process boundary.

A production implementation SHOULD use restricted service accounts, containers, filesystem namespaces, network denial, process sandboxes, and resource controls.

A Manifest declaration alone is not an operating-system sandbox.

The runtime MUST fail closed when it cannot enforce a declared boundary.

Unknown input remains untrusted data after validation. Validation establishes only the checks that actually ran.

Secrets are represented by opaque handles and MUST NOT appear in ordinary source, packs, events, or content-addressed blobs.

---

# 67. Deferred features

These features are outside canonical Core 0.1:

```text
remote package registries
network brokers
database brokers
process execution brokers
streaming ports
distributed scheduling
automatic adapters
runtime nested harnesses
user-declared stores
multiple versions of one package
prerelease versions
full JSON Schema
arbitrary policy code
runtime self-modification
live Manifest mutation
automatic topology repair
unbounded agent loops
cryptographic signing infrastructure
```

An implementation encountering them must reject them or require an explicit future profile.

---

# 68. Non-goals

Lattice does not define a universal epistemology.

Lattice does not prove that deterministic code is correct.

Lattice does not make model agreement equivalent to truth.

Lattice does not make prompt injection impossible.

Lattice does not guarantee subjective quality.

Lattice does not promise deterministic live reruns against changing external systems.

Lattice does not ask a small model to read this entire standard.

The Construction profile gives the model a bounded machine-generated local view, one target schema, one gap, and one error.

The standard is read by implementers. The builder pack is read by the builder model.

---

# 69. Final invariants

For a fixed Blueprint, package set, compatible existing Lockfile, Core profile, and semantic target, every conforming compiler produces the same canonical machine identity.

For a fixed Purpose Capsule, Construction profile, candidate state, gap-selection state, model raw response, and compiler diagnostics, every conforming builder-host produces the same accepted, rejected, no-op, or replan result.

The builder may propose source.

The compiler defines the machine.

The Qualification Record states what passed.

The Run Binding grants execution authority.

The event record states what happened.

The runtime may choose among declared paths.

Neither the builder model nor the operating model may rewrite the machine while it is running.
