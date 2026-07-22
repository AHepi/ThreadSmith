# Lattice Standard 0.3 Canonical JSON Erratum

Erratum date: 2026-07-22.

Status: normative companion to Lattice Standard 0.3.

## Authority and scope

This erratum resolves only byte-encoding ambiguity in sections 8, 15, 31,
35, 37, and 69 of Lattice Standard 0.3 wherever the Standard requires
canonical JSON. The recovered bytes of `LATTICE_STANDARD_0.3.md` remain
unchanged. Where this erratum defines an exact canonical JSON byte, escape, or
ordering rule, it is controlling for Lattice Standard 0.3. Every unaffected
Standard rule and every artifact-specific preimage rule remains unchanged.

This erratum does not select a new identity preimage, add an identity, alter a
compiler phase, validate source, apply a default, normalize a declaration,
sort a semantic collection, resolve a package, create an artifact, or grant
authority. It closes only the one-to-one encoding from an already selected
JSON-shaped canonical value to bytes.

## Canonical value domain

Canonical JSON is defined over exactly these values:

```text
object
array
Unicode string
integer admitted by the owning Standard schema
boolean
null
```

This erratum does not add or narrow an artifact's integer range. The source
profile and each artifact schema continue to decide which integer values are
representable. In particular, PC5 `DefaultedSource` contains only signed
64-bit integers because PC2 established that boundary, while the accepted
Foundation generic canonical machinery may continue to represent a wider
already-resolved integer preimage where its owning schema permits one.

Strings and object keys are Unicode scalar-value sequences normalized to NFC.
An unpaired UTF-16 surrogate is not a Unicode scalar value and has no canonical
encoding. A conforming internal string representation therefore makes such a
value impossible or rejects it as an internal invariant violation before an
artifact identity is created.

If two distinct object keys normalize to the same NFC string, the value has no
canonical object representation. A compiler must reject that state as an
internal invariant violation. This is not an additional source diagnostic for
phases whose accepted input already guarantees normalized, collision-free
keys.

## Byte stream

The canonical output is exactly one UTF-8 byte sequence with:

```text
no byte-order mark
no insignificant whitespace
no leading or trailing whitespace
no trailing newline
```

Punctuation is the ASCII JSON punctuation required by the value structure.
Objects use `{`, `}`, `:`, and `,`; arrays use `[`, `]`, and `,`. Empty objects
and arrays are exactly `{}` and `[]`.

## Object and array encoding

Object keys are first normalized to NFC, then sorted lexicographically by
their unsigned UTF-8 byte sequences. Comparison occurs on the normalized key
bytes before JSON string escaping. When one byte sequence is a proper prefix
of another, the shorter sequence sorts first.

Each object member is encoded as its canonical key string, one colon, and its
canonical value. Members are separated by one comma. No other byte occurs
between members.

Array elements remain in their existing semantic order unless another
Standard section explicitly normalized that collection before canonical JSON
encoding. Canonical JSON itself never sorts an array. Elements are separated
by one comma with no other intervening byte.

## String encoding

Each string and object key is normalized to NFC and enclosed by ASCII quotation
mark bytes. Inside those quotation marks, every Unicode scalar is encoded by
exactly one of these rules:

| Unicode scalar | Exact output bytes |
|---|---|
| quotation mark `U+0022` | `\"` |
| reverse solidus `U+005C` | `\\` |
| backspace `U+0008` | `\b` |
| tab `U+0009` | `\t` |
| line feed `U+000A` | `\n` |
| form feed `U+000C` | `\f` |
| carriage return `U+000D` | `\r` |
| every other `U+0000` through `U+001F` | `\u00xx`, using two lowercase hexadecimal digits |
| solidus `U+002F` | `/` |
| every other Unicode scalar | its direct NFC UTF-8 encoding |

Optional escaping does not exist. In particular:

```text
line feed is always \n and never \u000a
solidus is always / and never \/
non-ASCII scalars are direct UTF-8 and never \uXXXX or surrogate-pair escapes
```

The direct-UTF-8 rule includes `U+007F`, C1 controls such as `U+0085`,
`U+2028`, `U+2029`, non-ASCII Basic Multilingual Plane scalars, and
supplementary-plane scalars.

## Scalar encoding

Integers use ASCII base ten. Zero is exactly `0`. A negative integer
uses one leading `-` followed by its magnitude. A positive integer has no
leading `+`. No integer has a leading zero except the value zero. The complete
signed `i64` range used by PC5 is encodable, including
`-9223372036854775808` and `9223372036854775807`. An owning schema that admits
a wider integer uses the same minimal base-ten rule; this erratum does not
truncate, coerce, or reject it merely for exceeding `i64`.

The boolean values are exactly `true` and `false`. Null is exactly `null`.

## Hash boundary

Where the Standard assigns an identity to canonical JSON, SHA-256 consumes
exactly the byte stream defined above. No wrapper, path, filename, media type,
length prefix, terminating NUL, newline, diagnostic, implementation metadata,
or compiler-stage marker is added unless the artifact-specific Standard
preimage explicitly contains that data as a value.

The textual identity remains:

```text
lattice:<kind>:sha256:<64 lowercase hexadecimal characters>
```

## Required conformance coverage

Any implementation claiming canonical JSON conformance under Lattice Standard
0.3 must bind exact golden bytes and SHA-256 values for quotation mark, reverse
solidus, every short control escape, other C0 controls, solidus, `U+007F`,
`U+0085`, non-ASCII BMP scalars, supplementary scalars, NFC normalization,
UTF-8 object-key ordering, empty containers, the signed `i64` boundaries,
booleans, null, and absence of a trailing newline.

These vectors establish encoding only. They do not by themselves prove that an
implementation selected the correct artifact-specific preimage or that the
identified content is valid, compiled, qualified, bound, executable, or
authoritative.
