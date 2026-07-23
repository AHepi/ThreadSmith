Lattice Standard 0.3 Package Scan Semantics Erratum
Erratum acceptance date: 2026-07-23.
Status: accepted normative companion to Lattice Standard 0.3; PC6 semantics frozen.
This accepted erratum is derived from the independently reviewed fourth repaired candidate whose SHA-256 is d3569fc4de0c7e87fdc33c90b3fe427c7032cdd76c462c0696bfb3bd0740007d. That candidate preserves the complete prior repair history and changes fixture instantiation only by defining exact readable-directory child maps and the exact DATA_CHANGED identity input. Its independent review reported P0=0, P1=0, P2=0, and P3=0. Acceptance changes no normative Package Scan algorithm, diagnostic, fixture, golden vector, package identity, or accepted PC1 through PC5 semantic state.
The PC6 scope reconciliation remains controlling background. It establishes Package scan as the owner of local package discovery, descriptor intake, declared-file verification, package identity creation, immutable content continuity, and source-bound scanned output, while withholding Resolve, Lock, Expand, Manifest, Binding, Builder, and runtime authority.
PACKAGE_SCAN_ERRATUM_PROPOSAL_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_REVIEW_P1=6
PACKAGE_SCAN_ERRATUM_REVIEW_P2=1
PACKAGE_SCAN_ERRATUM_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P1=4
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P2=1
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P1=6
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P2=2
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P1=2
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P2=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P1=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P2=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_ACCEPTED=true
PC6_SEMANTICS_FROZEN=true
PC6_FREEZE_VERIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_STARTED=false
PC6_ACCEPTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC6 Package Scan implementation only


1. Normative relationship
The words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, and MAY are normative.
This erratum supplements Lattice Standard 0.3 only where Package scan is otherwise identity-affectingly incomplete.
Lattice Standard 0.3 remains primary normative authority.
The accepted Default Semantics Erratum remains authoritative only for its defined Default-phase transformation.
The accepted Canonical JSON Erratum remains authoritative only for converting an already selected JSON-shaped canonical value into canonical bytes and hashing those bytes.
This erratum does not alter canonical JSON encoding, SHA-256 mechanics, the native package identity prefix, or accepted PC1 through PC5 semantics.
Rules marked [S] restate Standard 0.3. Rules marked [C] clarify an existing requirement. Rules marked [N] introduce a new normative choice required to close an ambiguity. Rules marked [D] defer behavior to a later existing phase.
2. Scope
Package scan occurs immediately after Digest and immediately before Resolve.
Package scan owns local package discovery from a host-supplied immutable portable snapshot, restricted-YAML intake of every discovered package descriptor, exhaustive package-descriptor admission, descriptor and directory agreement, portable declared-path admission, verification of every declared package file, retention of exact immutable verified bytes, construction of the canonical package descriptor value, creation of the package identity, and construction of a non-authoritative source-bound scanned result.
Package scan MUST NOT collect version constraints, choose a package version, reuse a Lockfile, run a resolution fixed point, create a Lockfile, expand imports, namespace declarations, normalize declaration bodies, insert generated gates, perform static checking, create declaration identities, create a Manifest, qualify a Manifest, create a Binding, install or fetch packages, access a provider or model, execute package content, or grant authority.
3. Conceptual operation
[N] The conceptual operation is:
scan_packages(
    source: DigestedSource,
snapshot: PortableProjectSnapshot
) -> PackageScanOutcome


A semantic PackageScanOutcome is either a successful ScannedSource or one PackageScanDiagnostic.
Portable snapshot acquisition occurs before Package scan. Failure to acquire a complete valid immutable snapshot produces no semantic PackageScanOutcome.
The snapshot MUST be supplied explicitly by the host. It MUST NOT be derived from DigestedSource, an ambient current directory, an environment variable, a Blueprint declaration, a package descriptor, a package file, or a previously created identity.
The snapshot grants bounded compile-time read access only to the optional root entry named packages and, when that entry exists, its complete immutable subtree. It grants no runtime authority and is not retained as an ambient filesystem capability.
4. Portable project snapshot
4.1 Snapshot completeness
[N] PortableProjectSnapshot is a complete immutable logical view of the exact optional child named packages beneath one host-selected project root and, when present, the complete subtree rooted at that child.
It is not a materialization of the complete project root.
Snapshot acquisition MUST use exact lookup for the single root child named packages.
It MUST NOT enumerate, validate, normalize, snapshot, or otherwise inspect unrelated project-root entries.
An unrelated root entry therefore cannot affect snapshot acquisition, Package-scan diagnostics, package identity, or ScannedSource.
Snapshot acquisition either completes successfully or produces no semantic Package-scan result.
A successful snapshot MUST remain immutable for its entire semantic lifetime.
Package scan MUST operate only on the completed snapshot. It MUST NOT reopen, restat, or compare the live filesystem.
Concurrent mutation of the live filesystem during snapshot acquisition is outside Package-scan semantic completion. A host that cannot produce one complete immutable view MUST fail snapshot acquisition rather than expose a partial or temporally mixed snapshot.
The following conditions are snapshot-acquisition failures, not PC6 diagnostics, only when encountered while acquiring the exact packages entry or its included subtree:
Condition
	Required outcome
	A native name cannot be represented losslessly as Unicode scalar values
	No snapshot and no PackageScanOutcome
	A native name contains malformed UTF-16
	No snapshot and no PackageScanOutcome
	Two native names normalize to the same NFC name in one directory
	No snapshot and no PackageScanOutcome
	Host namespace aliases cannot be represented as distinct exact entries
	No snapshot and no PackageScanOutcome
	A complete immutable point-in-time view cannot be established
	No snapshot and no PackageScanOutcome
	Concurrent mutation prevents complete snapshot formation
	No snapshot and no PackageScanOutcome
	Snapshot acquisition exhausts host resources
	No snapshot and no partial package set
	The snapshot contains an internally inconsistent object reference
	Internal host failure, no semantic result
	No PC6 diagnostic code represents one of these conditions.
4.2 Portable names
Every included snapshot entry name MUST be a valid Unicode scalar sequence normalized to NFC.
The snapshot MUST expose the exact UTF-8 encoding of every name.
A snapshot name MUST NOT contain U+0000 or U+002F /.
Within one directory, every NFC name MUST identify exactly one directory entry.
Ordering of snapshot names is ascending lexicographic order over unsigned NFC UTF-8 bytes.
Locale collation, case folding, filesystem enumeration order, native code-unit order, percent-encoded diagnostic spelling, and host path normalization MUST NOT affect ordering.
4.3 Snapshot object classes
A snapshot entry is semantically one of the following classes:
Class
	Meaning
	Directory
	Immutable map from NFC names to snapshot entries
	Regular file with bytes
	Immutable exact byte sequence
	Regular file unreadable
	Entry exists and is regular, but byte content was not made available
	Directory unreadable
	Entry exists and is a directory, but its child map was not made available
	Link-like object
	An entry whose native lookup semantics can redirect traversal away from the exact stored child mapping; this class includes symbolic links, junctions, and reparse redirections
	Special object
	Device, socket, FIFO, named pipe, door, or another non-directory non-regular object
	Two different directory entries MAY refer to the same immutable regular-file content object through a hard link.
Hard-link sharing does not merge their names or paths.
Underlying inode numbers, file identifiers, object identifiers, link counts, mount origins, native absolute paths, and snapshot storage locations do not enter package identity.
4.4 Live mounts and namespace provenance
This erratum does not require PC6 to prove that a live host directory was never mounted, rebound, renamed, or subject to namespace changes before snapshot acquisition.
The completed snapshot is the semantic input boundary.
A host MAY materialize content originating across a mount boundary if that content is inside the explicitly supplied bounded snapshot.
Link-like objects represented inside the snapshot remain forbidden as specified below.
5. Diagnostic path rendering
[N] Every PC6 filesystem diagnostic path uses a canonical portable rendering.
Each NFC name is encoded as UTF-8.
Every byte in the unreserved ASCII set is emitted literally:
A-Z a-z 0-9 - . _ ~


Every other byte is emitted as % followed by two uppercase hexadecimal digits.
A literal % is therefore rendered as %25.
Directory separators are emitted as literal / between encoded name segments.
Ordering always uses original NFC UTF-8 bytes, never rendered diagnostic text.
Examples are:
café        -> caf%C3%A9
100%        -> 100%25
a b         -> a%20b
#name       -> %23name


Descriptor diagnostic paths use:
<canonical snapshot path>#<canonical RFC 6901 pointer>


The single literal # between the filesystem path and pointer is a structural delimiter. It is always emitted exactly as U+0023 and is expressly exempt from percent encoding.
The descriptor-root pointer is empty, leaving that literal trailing #.
Each descriptor pointer is rendered by this exact algorithm:
begin with the decoded NFC Unicode scalar sequence of each logical pointer token
replace every U+007E ~ in a token by the two ASCII bytes ~0
replace every U+002F / in a token by the two ASCII bytes ~1
encode the resulting token as UTF-8
emit every unreserved ASCII byte literally and every other byte as % followed by two uppercase hexadecimal digits
join encoded tokens with one literal U+002F / before each token
prepend the canonical filesystem path and exactly one literal U+0023 #


RFC 6901 escaping therefore occurs before percent encoding. Percent encoding never consumes the structural # delimiter or pointer / separators. A U+0023 contained in a filesystem component or pointer token is %23 and cannot be confused with the one literal delimiter. A root pointer has no token and renders only the trailing delimiter.
6. ScannedSource binding and semantic state
[N] A successful ScannedSource semantically binds the exact consumed DigestedSource and an ordered sequence of admitted scanned-package records.
Each scanned-package record semantically binds the admitted canonical descriptor value, the package identity, and the immutable mapping from every declared logical path to its exact verified byte sequence.
Canonical descriptor bytes are deterministic derived material.
They MAY be retained internally, cached, exposed to conformance tests, or reproduced during verification.
They are not required stored semantic state in every ScannedSource representation.
Semantic equality of successful scanned results compares the bound DigestedSource, ordered admitted canonical descriptor values, package identities, declared logical paths, and exact immutable retained bytes.
Semantic equality MUST NOT depend on the presence of a stored canonical-byte cache.
ScannedSource MUST be constructible only by successful Package scan.
A conforming public interface MUST NOT permit independent construction, caller deserialization into an accepted scanned state, replacement of the source, replacement of the package sequence, replacement of an admitted descriptor, replacement of a package identity, replacement of verified bytes, mutable access to retained bytes, or pairing one package identity with bytes not verified for that package.
ScannedSource contains no live filesystem path, snapshot mutation capability, host read capability, execution capability, or authority.
7. Package discovery universe
7.1 Packages root
[N] Package scan inspects the direct child named exactly packages of the snapshot root.
If packages is absent, Package scan succeeds with an empty local-package sequence and empty verified-content mapping.
If packages exists as a link-like object, scan fails with PACKAGE_SCAN_SYMLINK_FORBIDDEN.
If packages exists as an ordinary object other than a directory, scan fails with PACKAGE_SCAN_PACKAGES_ROOT_INVALID.
If packages exists as an unreadable directory, scan fails with PACKAGE_SCAN_DISCOVERY_UNREADABLE.
An empty readable packages directory succeeds with an empty package sequence.
7.2 Exact structural depth
[C/N] Package candidates exist only at:
packages/<package-name>/<version>/package.yaml


Package scan MUST NOT recursively discover descriptors.
The structural depth is exact:
Depth
	Meaning
	packages
	Packages root
	packages/<package-name>
	Package-name directory
	packages/<package-name>/<version>
	Version directory
	packages/<package-name>/<version>/package.yaml
	Descriptor
	A direct entry under packages is always treated as an attempted package-name slot.
A direct entry under an admitted package-name directory is always treated as an attempted version slot.
A direct package.yaml under a package-name directory is therefore an invalid version-slot entry.
A nested file named package.yaml beneath a valid version directory is not recursively discovered as another descriptor.
7.3 Structural traversal
The exact traversal is:
inspect packages root
obtain all direct package-name entries
sort package-name entries by NFC UTF-8 bytes
for each package-name entry in that order:
    classify and validate the package-name entry
    obtain all direct version entries
    sort version entries by NFC UTF-8 bytes
    for each version entry in that order:
        classify and validate the version entry
        require and classify package.yaml
        append the candidate
after structural discovery succeeds:
    sort appended candidates by package-name ASCII bytes
    then by numeric canonical version tuple
process candidates in that canonical candidate order


The nested NFC UTF-8 traversal is normative for structural diagnostic selection.
The later numeric candidate sort is normative for descriptor processing and successful ScannedSource package-record order.
For example, valid versions 2.0.0 and 10.0.0 are processed and returned in that numeric order even though the raw UTF-8 spelling 10.0.0 sorts first.
The implementation MUST NOT first validate all package-name entries globally and then make a separate global version pass.
7.4 Package-name structural slot
For each sorted package-name entry, precedence is:
Rank
	Check
	1
	Link-like object
	2
	Package-name grammar
	3
	Ordinary object type
	4
	Directory readability
	5
	Valid readable package directory
	A link-like entry produces PACKAGE_SCAN_SYMLINK_FORBIDDEN.
A non-link name that fails the package-name grammar produces PACKAGE_SCAN_LAYOUT_ENTRY_INVALID, even when its ordinary object type is also wrong.
A valid package-name entry that is not a directory produces PACKAGE_SCAN_LAYOUT_ENTRY_INVALID.
An unreadable valid package directory produces PACKAGE_SCAN_DISCOVERY_UNREADABLE.
7.5 Version structural slot
For each sorted version entry, precedence is:
Rank
	Check
	1
	Link-like object
	2
	Canonical package-version grammar
	3
	Ordinary object type
	4
	Directory readability
	5
	Valid readable version directory
	A link-like version entry produces PACKAGE_SCAN_SYMLINK_FORBIDDEN.
A non-link name that fails the canonical version grammar produces PACKAGE_SCAN_LAYOUT_ENTRY_INVALID.
A valid version entry that is not a directory produces PACKAGE_SCAN_LAYOUT_ENTRY_INVALID.
An unreadable valid version directory produces PACKAGE_SCAN_DISCOVERY_UNREADABLE.
7.6 Descriptor structural slot
Every valid version directory MUST contain a direct child named exactly package.yaml.
Descriptor classification precedence is:
Rank
	Check
	1
	Link-like object
	2
	Missing entry
	3
	Ordinary non-regular or special object
	4
	Unreadable regular bytes
	5
	Valid regular descriptor bytes
	A link-like descriptor produces PACKAGE_SCAN_SYMLINK_FORBIDDEN.
An absent descriptor produces PACKAGE_SCAN_DESCRIPTOR_MISSING.
A present non-link descriptor that is not a regular file produces PACKAGE_SCAN_DESCRIPTOR_NOT_REGULAR.
A regular descriptor whose bytes are unavailable produces PACKAGE_SCAN_DESCRIPTOR_UNREADABLE.
7.7 Additional version-directory entries
[S/C] Unlisted files have no semantic content and their bytes MUST NOT be read.
Because Standard 0.3 rejects symlinks within package trees, PC6 performs a metadata-only traversal of each admitted version-directory subtree.
The metadata traversal observes names, object classes, and readable child maps only.
It MUST NOT read bytes from an unlisted regular file.
An unlisted regular file is ignored.
An unlisted special object is ignored unless it occupies a required structural or declared-file position.
An unlisted readable directory is traversed for link-like descendants.
An unlisted unreadable directory produces PACKAGE_SCAN_DISCOVERY_UNREADABLE, because the no-link invariant cannot be established for its subtree.
A link-like object anywhere in the package version subtree produces PACKAGE_SCAN_SYMLINK_FORBIDDEN.
The metadata traversal is depth first, pre-order. Children are visited by ascending NFC UTF-8 name bytes.
8. Directory and descriptor agreement
8.1 Package names
[S/N] A package name matches:
^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$


The package-name directory component MUST match this grammar.
The descriptor package member MUST exactly equal the directory component as ASCII bytes.
No case folding, locale comparison, Unicode normalization during comparison, native path comparison, or alias comparison is applied.
A mismatch produces PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH.
8.2 Versions
[S/N] A package version has three canonical decimal components.
Each component is either 0 or begins with [1-9] followed by zero or more decimal digits.
The exact grammar is:
^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$


Prerelease and build metadata are forbidden.
This canonical spelling rule applies to Package scan. It does not amend the accepted PC3 root-source grammar.
The descriptor version member MUST exactly equal the version-directory component as ASCII bytes.
A mismatch produces PACKAGE_SCAN_VERSION_DIRECTORY_MISMATCH.
Version ordering compares the major, minor, and patch components as arbitrary-size non-negative integers without machine-integer conversion. Fewer digits indicate the smaller value. Equal-length components compare by ASCII bytes.
8.3 Name aliases and hard links
Distinct logical names MUST identify distinct directory entries in the portable snapshot.
Snapshot acquisition MUST reject host alias behavior that would collapse distinct NFC logical names through case folding, trailing-dot removal, trailing-space removal, separator conversion, Unicode normalization, reserved-name mapping, or another namespace alias.
This rule concerns directory-entry names.
It does not prohibit two distinct directory entries from referring to the same immutable regular-file content object through a hard link.
Directory components do not independently enter the package identity preimage. Their admitted values must agree with the descriptor fields that do enter the preimage.
9. Descriptor source encoding
[C] package.yaml uses exactly the accepted restricted YAML 1.2 JSON-shaped source profile already frozen for PC2.
The descriptor MUST be UTF-8 and MUST NOT begin with a UTF-8 BOM.
LF, CRLF, and CR source line endings are accepted and normalized to LF for parsing.
Exactly one YAML document is accepted.
The accepted optional YAML 1.2 directive, document markers, comments, block mappings, flow mappings, block sequences, flow sequences, plain scalars, single-quoted scalars, double-quoted scalars, and literal scalar style remain governed by the accepted parser profile.
Folded scalar style, anchors, aliases, merge keys, forbidden or mismatched tags, binary-tagged values, floats, multiple documents, non-string keys, duplicate decoded keys, post-NFC key collisions, and integers outside signed i64 are rejected exactly as the accepted PC2 profile specifies.
The accepted PC2 profile does not construct a YAML date or timestamp category. A plain token such as 2026-07-23 is an NFC string. Descriptor schema validation, not descriptor parsing, therefore rejects that value when it appears in package because it does not match the package-name grammar.
Tabs used where YAML indentation forbids them are YAML syntax errors.
Every decoded string and mapping key is normalized to NFC under the accepted parser semantics.
Comments, accepted line endings, source key order, quoting, indentation, scalar presentation, document markers, and flow-versus-block presentation do not enter package identity.
10. Exhaustive descriptor grammar
10.1 Root mapping
[N] The parsed root MUST be an object.
Its permitted key set is exactly:
package
version
lattice
profiles
module_file
files


All six members are required.
Unknown members are forbidden.
No Package-scan default exists.
All six admitted members participate in the canonical descriptor value.
10.2 Package field
package MUST be a string matching the package-name grammar and exactly matching the package directory.
10.3 Version field
version MUST be a string matching the canonical Package-scan version grammar and exactly matching the version directory.
10.4 Lattice field
lattice MUST be a string exactly equal to:
0.3


10.5 Profiles field
[N] profiles MUST be a nonempty array of strings.
Each value MUST be exactly one of:
lattice-builder-0.1
lattice-core-0.1


The collection is a semantic set.
Duplicate values are forbidden.
For the canonical descriptor value, profile strings are sorted by ascending unsigned UTF-8 bytes.
Source presentation order is not semantic.
Package scan proves descriptor membership in this vocabulary only. It does not prove that later import use is compatible with an active compiler profile.
10.6 Module file field
module_file MUST be a string satisfying the portable package-relative path grammar.
It MUST occur exactly once as a path in files.
Because file paths are unique, exact-once membership follows from membership plus uniqueness.
10.7 Files field
[N] files MUST be a nonempty array.
Each element MUST be an object whose permitted and required key set is exactly:
path
sha256


path MUST be a string satisfying the portable path grammar.
sha256 MUST be a string satisfying the digest grammar.
File paths MUST be unique after accepted string decoding and NFC processing.
The exact path package.yaml MUST NOT occur in files.
A nested path such as docs/package.yaml is not the descriptor and is not forbidden solely by its final segment.
For the canonical descriptor value, file entries are sorted by ascending unsigned ASCII path bytes.
Source presentation order is not semantic.
10.8 Duplicate paths
After file-entry member types are admitted, equal path strings are grouped.
If more than one duplicated path exists, the lexicographically smallest duplicated UTF-8 path is selected.
Within that group, the diagnostic points to the second-lowest original source index.
The diagnostic is PACKAGE_SCAN_DECLARED_PATH_DUPLICATE.
10.9 Prefix collisions
After all individual file paths are admitted and sorted by ascending ASCII path bytes, PC6 identifies every pair (shorter, longer) for which:
longer starts with shorter + "/"


The selected pair is the pair whose shorter path is lexicographically smallest, then whose longer path is lexicographically smallest.
The diagnostic is PACKAGE_SCAN_DECLARED_PATH_PREFIX_COLLISION.
The diagnostic pointer identifies the original source entry containing the selected longer path.
11. Portable package-relative path grammar
11.1 Exact grammar
[N] Every declared path, including module_file, consists only of lowercase ASCII.
A segment matches:
[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?


A complete path matches:
^[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?(?:/[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?)*$


The admitted path string is already its normalized logical representation.
11.2 Forbidden forms
The grammar rejects empty paths, leading /, trailing /, repeated /, empty segments, . segments, .. segments, reverse solidus, colon, NUL, controls, DEL, non-ASCII characters, uppercase letters, trailing dot, trailing space, Windows drive forms, drive-relative forms, rooted Windows forms, and UNC forms.
A forbidden form MUST NOT be normalized into an admitted path.
11.3 Reserved device basenames
For each path segment, the bytes before the first . are compared as lowercase ASCII.
The following basenames are forbidden with or without an extension:
con
prn
aux
nul
com1
com2
com3
com4
com5
com6
com7
com8
com9
lpt1
lpt2
lpt3
lpt4
lpt5
lpt6
lpt7
lpt8
lpt9


11.4 Snapshot traversal
A declared path is split only on literal /.
Each logical segment is looked up exactly in the immutable snapshot directory map.
No host convenience normalization, native separator conversion, case folding, Unicode normalization, or live-filesystem path lookup occurs.
Every admitted logical path resolves to exactly one directory-entry chain or fails.
Two declared paths may terminate in distinct directory entries sharing one hard-linked immutable content object.
12. Filesystem object semantics
12.1 Required regular files
A declared final target MUST be a regular file with available immutable bytes.
A directory at the final component produces PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR.
A non-link special object produces PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT.
A final node already established to be a regular file whose immutable bytes cannot be opened or read produces PACKAGE_SCAN_DECLARED_FILE_UNREADABLE.
12.2 Link-like objects
A link-like object is forbidden as the packages root, a package-name directory, a version directory, package.yaml, an intermediate declared-path component, a declared final target, or an unlisted descendant within a package version subtree.
A link-like object always produces PACKAGE_SCAN_SYMLINK_FORBIDDEN before an ordinary wrong-type diagnostic at the same position.
12.3 Intermediate components
For an intermediate declared-path component, an absent entry produces PACKAGE_SCAN_DECLARED_FILE_MISSING.
A link-like entry produces PACKAGE_SCAN_SYMLINK_FORBIDDEN.
A regular file where a directory is required produces PACKAGE_SCAN_DECLARED_PATH_COMPONENT_NOT_DIRECTORY.
A non-link special object produces PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT.
An unreadable directory is owned exclusively by the earlier metadata audit and produces PACKAGE_SCAN_DISCOVERY_UNREADABLE at that exact directory path.
Metadata audit attempts to enumerate every included directory in each admitted version subtree, including every directory that is an intermediate or final node of a declared path. Declared-file verification therefore begins only after every directory needed for its traversal has an available child map.
A final node established to be a directory produces PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR. If that directory cannot be enumerated, the earlier metadata-audit stage instead produces PACKAGE_SCAN_DISCOVERY_UNREADABLE, so those outcomes cannot compete.
12.4 Hard links
[N] Hard links are allowed.
Two declared logical paths MAY refer through distinct directory entries to the same immutable regular-file content object.
Each path remains a separate descriptor entry.
Each path is independently checked against its declared digest.
Each path is independently represented in the package snapshot.
The shared object identity, native file identifier, link count, and storage deduplication do not enter the package descriptor or package identity.
Hard-link sharing is not a namespace collision.
12.5 Root containment
The portable snapshot root is the semantic containment boundary.
An admitted path cannot escape through . or .., because those forms are rejected before traversal.
PC6 does not emit a live-filesystem root-containment diagnostic.
Failure to create a bounded portable snapshot is a snapshot-acquisition failure outside semantic Package scan.
13. Declared SHA-256 semantics
[N] Every sha256 value contains exactly 64 lowercase hexadecimal characters:
0 1 2 3 4 5 6 7 8 9 a b c d e f


Uppercase hexadecimal is forbidden.
Leading or trailing whitespace is forbidden.
A sha256: prefix is forbidden.
Every other prefix is forbidden.
Wrong length and non-hexadecimal characters are forbidden.
The digest is SHA-256 over the exact immutable raw file bytes retained from the portable snapshot.
No byte transformation occurs before hashing.
LF and CRLF content produce different hashes.
A content BOM participates in the hash.
An empty file is valid.
Permissions, executable bits, ownership, timestamps, native file identifiers, hard-link counts, absolute paths, and snapshot storage details do not participate.
The empty-file SHA-256 is:
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855


A digest mismatch produces PACKAGE_SCAN_FILE_HASH_MISMATCH.
The retained bytes for a declared path MUST be exactly the bytes hashed for that path.
package.yaml is not directly content-hashed into its own descriptor.
14. Immutable verified-byte continuity
[N] Successful declared-file verification follows this logical sequence:
locate the exact snapshot directory-entry chain
reject a link-like or wrong-type component
obtain the immutable regular-file bytes
calculate SHA-256 over those exact bytes
compare against the declared lowercase digest
bind that exact byte sequence to the declared logical path


PC6 MAY retain immutable byte strings, immutable content-addressed blobs, immutable snapshot-object references, or another representation that is provably byte-exact.
The logical result MUST preserve this mapping:
package identity
    -> declared logical path
    -> exact verified byte sequence


Later compiler phases MUST consume only retained immutable snapshot content.
Later phases MUST NOT reread a mutable live package path.
Mutation of the live filesystem after snapshot acquisition cannot alter an existing ScannedSource.
A later scan requires a new snapshot and independently produces the result for that new immutable input.
15. Exact canonical package descriptor value
[N] After descriptor admission and file verification, Package scan constructs exactly this JSON-shaped value:
{
  "package": "<admitted package>",
  "version": "<admitted canonical version>",
  "lattice": "0.3",
  "profiles": [
    "<unique profiles sorted by UTF-8 bytes>"
  ],
  "module_file": "<admitted path>",
  "files": [
    {
      "path": "<admitted path>",
      "sha256": "<verified lowercase digest>"
    }
  ]
}


The root contains exactly six members.
Every file entry contains exactly path and sha256.
There are no defaults.
profiles is sorted as specified.
files is sorted by ascending ASCII path bytes.
The canonical descriptor excludes directory components as additional members, YAML source bytes, comments, source key order, quoting, indentation, source line endings, document markers, project paths, package paths, timestamps, ownership, permissions, executable bits, native object identifiers, hard-link metadata, directory enumeration order, unlisted entries, snapshot provenance, and compiler metadata.
Raw declared-file bytes participate indirectly through their verified digest strings.
The value is encoded using the accepted Canonical JSON Erratum.
For the six ASCII root keys, canonical key order is:
files
lattice
module_file
package
profiles
version


No wrapper, type tag, filename, length prefix, NUL terminator, or trailing newline is added.
Canonical descriptor bytes are deterministic derived material, not mandatory stored semantic state.
16. Package identity
[S/C] The package digest is:
SHA-256(canonical package descriptor bytes)


The package identity text is exactly:
lattice:package:sha256:<64 lowercase hexadecimal>


PC6 is the sole phase-produced package-identity creator.
A caller-created generic native identity does not prove that Package scan occurred.
The admitted descriptor value, package identity, and retained immutable bytes are inseparable within the successful scanned-package record.
A failure of the accepted canonical encoder or SHA-256 core on an already admitted descriptor is an internal compiler non-conformance or operational failure.
It is not a user package-content diagnostic.
It produces no package identity, no partial package set, and no semantic PackageScanOutcome.
PACKAGE_SCAN_CANONICAL_DESCRIPTOR_INVARIANT is not a valid PC6 diagnostic code.
17. Imported module boundary
[D] PC6 treats module_file only as one required declared file.
PC6 MUST verify its raw digest, retain its exact immutable bytes, bind those bytes to the package identity, and bind the resulting package record to ScannedSource.
PC6 MUST NOT parse module_file as YAML, validate an imported root envelope, interpret imports, apply defaults, check package/profile/module compatibility, collect transitive requirements, select a version, assign namespaces, validate declaration bodies, create an imported-module digest, or create a later-phase diagnostic.
Malformed YAML, unresolved imports, unsatisfied version requirements, incompatible module metadata, and later-invalid declaration bodies do not make a package invalid at PC6 when the descriptor and declared raw bytes otherwise satisfy this erratum.
Any later phase that consumes module_file MUST use the retained immutable bytes rather than the live filesystem.
The exact ownership of imported-module parsing, root validation, compatibility, import collection, default insertion, expansion, and diagnostics is deferred to the Resolve scope reconciliation and semantic freeze.
This erratum creates no new compiler phase and does not normatively assign partial PC2 or PC3 behavior to Resolve.
18. Duplicate package candidates
[N] Under one valid portable package root, exact structural names permit at most one physical candidate for one exact package name and canonical version.
Snapshot alias collisions are rejected during snapshot acquisition rather than merged.
PC6 performs no version selection and emits no RESOLVE_DUPLICATE_VERSION.
If a later accepted composition mechanism presents Resolve with multiple scanned candidates having one package name and version, duplicate handling remains Resolve-owned.
Package candidates are ordered by package-name ASCII bytes and then numeric canonical version order.
19. PC6 diagnostic vocabulary
A semantic PackageScanDiagnostic contains exactly one stable code and one canonical diagnostic path.
Message prose and source-coordinate annotations MAY be attached but are non-normative.
19.1 Accepted-parser crosswalk
[C] Package scan parses package.yaml by invoking the exact accepted PC2 restricted-YAML semantic operation over the descriptor bytes. The function name is irrelevant; the observable input, successful JSON-shaped value, stable SourceDiagnostic code, and accepted PC2 primary-selection behavior MUST equal parse_blueprint_source on those identical bytes.
A conforming implementation MAY share the accepted parser implementation or implement it independently. It MUST NOT infer a finer Package-scan syntax category than the accepted PC2 result.
The selected accepted PC2 code maps one-to-one as follows:
Accepted PC2 code
	PC6 code
	Semantic target
	SOURCE_INVALID_UTF8
	PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID
	Descriptor root
	SOURCE_FORBIDDEN_YAML
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN
	Descriptor root
	SOURCE_INVALID_SCALAR
	PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID
	Descriptor root
	SOURCE_NON_STRING_KEY
	PACKAGE_SCAN_DESCRIPTOR_NON_STRING_KEY
	Descriptor root
	SOURCE_DUPLICATE_KEY
	PACKAGE_SCAN_DESCRIPTOR_DUPLICATE_KEY
	Descriptor root
	SOURCE_NFC_COLLISION
	PACKAGE_SCAN_DESCRIPTOR_NFC_COLLISION
	Descriptor root


For every malformed descriptor, including one containing multiple parser defects, PC6 first obtains exactly the one accepted PC2 outcome for the complete descriptor bytes and then performs this table lookup. It does not inspect a second defect or reclassify the selected result. Invalid UTF-8, a BOM, and forbidden raw source characters therefore share PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID. Directives, YAML syntax, document count, anchors, aliases, merge keys, forbidden or mismatched tags, folded scalars, and binary-tagged values share PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN. Floats and integers outside signed i64 share PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID.
All six parser-layer target paths are the complete descriptor filesystem path followed by the literal root delimiter #.
A date-looking plain scalar is not a parser rejection. It is an NFC string and continues into the descriptor schema stages.
19.2 Exhaustive code-to-target-path table
The symbols in this table are normative abbreviations:
P is packages.
N is packages/<package-name>.
V is packages/<package-name>/<version>.
D is packages/<package-name>/<version>/package.yaml.
F is V followed by the declared path's components.
i and j are original zero-based source array indices.
k is one decoded descriptor member name.
Every substituted filesystem component and pointer token is rendered by section 5.


Code
	Exact meaning
	Exact target path
	PACKAGE_SCAN_PACKAGES_ROOT_INVALID
	Present packages is a non-link object other than a directory
	P
	PACKAGE_SCAN_DISCOVERY_UNREADABLE
	An included directory cannot expose its complete immutable child map
	The exact unreadable directory
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID
	A non-link package-name or version structural slot has an invalid name or ordinary wrong type
	The exact offending structural entry
	PACKAGE_SCAN_DESCRIPTOR_MISSING
	A valid version directory lacks direct package.yaml
	The nonexistent child D
	PACKAGE_SCAN_DESCRIPTOR_NOT_REGULAR
	The descriptor is present, non-link, and not a regular file
	D
	PACKAGE_SCAN_DESCRIPTOR_UNREADABLE
	The descriptor is regular but its immutable bytes are unavailable
	D
	PACKAGE_SCAN_SYMLINK_FORBIDDEN
	A link-like object occurs at a forbidden included position
	The exact link-like node
	PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT
	A required declared-path node is a non-link special object
	The exact special node
	PACKAGE_SCAN_DECLARED_PATH_COMPONENT_NOT_DIRECTORY
	A regular file occupies an intermediate declared-path component
	The exact intermediate regular-file node
	PACKAGE_SCAN_DECLARED_FILE_MISSING
	A declared path component or final target is absent
	The shortest nonexistent prefix of F
	PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR
	A declared final node is an enumerable directory
	F
	PACKAGE_SCAN_DECLARED_FILE_UNREADABLE
	A final node established to be regular cannot supply immutable bytes
	F
	PACKAGE_SCAN_FILE_HASH_MISMATCH
	SHA-256 of retained bytes differs from the declared digest
	F, never the descriptor sha256 member
	PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID
	Accepted PC2 selected SOURCE_INVALID_UTF8
	D#
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN
	Accepted PC2 selected SOURCE_FORBIDDEN_YAML
	D#
	PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID
	Accepted PC2 selected SOURCE_INVALID_SCALAR
	D#
	PACKAGE_SCAN_DESCRIPTOR_NON_STRING_KEY
	Accepted PC2 selected SOURCE_NON_STRING_KEY
	D#
	PACKAGE_SCAN_DESCRIPTOR_DUPLICATE_KEY
	Accepted PC2 selected SOURCE_DUPLICATE_KEY
	D#
	PACKAGE_SCAN_DESCRIPTOR_NFC_COLLISION
	Accepted PC2 selected SOURCE_NFC_COLLISION
	D#
	PACKAGE_SCAN_DESCRIPTOR_ROOT_INVALID
	Parsed root is not an object
	D#
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY
	Root or file-entry object has an unknown member
	D#/<k> for a root key, or D#/files/<i>/<k> for a file-entry key
	PACKAGE_SCAN_DESCRIPTOR_MEMBER_MISSING
	A required root or file-entry member is absent
	D#/<required-member>, or D#/files/<i>/path or D#/files/<i>/sha256
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID
	A present member has the wrong type or an inadmissible non-path, non-digest value
	The exact failing member or array element: D#/<member>, D#/profiles/<i>, D#/files/<i>, D#/files/<i>/path, or D#/files/<i>/sha256 as selected by section 20
	PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH
	Descriptor package differs from its directory
	D#/package
	PACKAGE_SCAN_VERSION_DIRECTORY_MISMATCH
	Descriptor version differs from its directory
	D#/version
	PACKAGE_SCAN_DECLARED_PATH_DUPLICATE
	Two file entries decode to the same path
	D#/files/<j>/path for the selected duplicate's second-lowest source index
	PACKAGE_SCAN_DECLARED_PATH_INVALID
	module_file or a file-entry path violates the portable grammar
	D#/module_file or D#/files/<i>/path for the selected value
	PACKAGE_SCAN_DECLARED_PATH_PREFIX_COLLISION
	One declared file path is a strict directory prefix of another
	D#/files/<j>/path for the selected longer path's original source index
	PACKAGE_SCAN_MODULE_FILE_UNLISTED
	module_file does not occur in files
	D#/module_file
	PACKAGE_SCAN_DESCRIPTOR_SELF_LISTED
	Exact path package.yaml occurs in files
	D#/files/<i>/path for the selected entry
	PACKAGE_SCAN_DIGEST_SYNTAX_INVALID
	A declared digest is not exactly 64 lowercase hexadecimal characters
	D#/files/<i>/sha256 for the selected entry


This table is exhaustive. A rule or fixture that names only a code, omits the rendered path, or offers alternate targets is non-conforming.
No Resolve, Lock, Expand, declaration, Manifest, Binding, provider, or runtime diagnostic is created by PC6.
20. Deterministic primary-diagnostic precedence
Only one primary PC6 diagnostic is returned.
No partial ScannedSource is exposed.
20.1 Global traversal
After structural discovery and canonical candidate sorting succeed, PC6 performs global staged passes.
Every pass visits candidates in canonical candidate order.
PC6 completes one pass for every candidate before beginning the next pass.
Global precedence is:
Rank
	Stage
	1
	Packages-root classification
	2
	Nested structural discovery using section 7.3
	3
	Restricted-YAML descriptor parsing for every candidate
	4
	Descriptor shallow schema, scalar admission, and directory agreement for every candidate
	5
	Profile, module_file, and files collection validation for every candidate
	6
	Metadata-only link audit for every candidate
	7
	Declared-file verification for every candidate
	8
	Canonical derivation and package identity for every candidate, whose internal failure is non-semantic
Thus, a descriptor parse failure in a later candidate precedes a file-hash mismatch in an earlier candidate.
	20.2 Descriptor-schema precedence
For one parsed descriptor, precedence is:
Rank
	Check
	1
	Root object type
	2
	Unknown root keys, selected by ascending UTF-8 key bytes
	3
	Missing root keys in fixed order
	4
	Shallow root-member type checks in fixed order
	5
	package value grammar
	6
	version value grammar
	7
	lattice exact value
	8
	Package-directory agreement
	9
	Version-directory agreement
	The fixed root-member order is:
package
version
lattice
profiles
module_file
files


Shallow type checks prove only:
package is a string
version is a string
lattice is a string
profiles is an array
module_file is a string
files is an array


They do not validate collection contents or the module_file path.
Collection contents and module_file path admission occur only in the following global collection pass.
20.3 Profiles precedence
Profiles validation occurs before module_file and files validation for the same candidate.
Profiles precedence is:
Rank
	Check
	1
	Nonempty requirement
	2
	Element string types by increasing source index
	3
	Invalid values, selected by ascending UTF-8 value then source index
	4
	Duplicates, selected by ascending UTF-8 value and pointing to the second-lowest source index
	20.4 Files precedence
After profiles succeed, module_file is admitted against the portable path grammar.
A module_file path failure produces PACKAGE_SCAN_DECLARED_PATH_INVALID at D#/module_file under the section 19.2 abbreviation before any deep files validation.
After module_file succeeds, files precedence is:
Rank
	Check
	1
	Nonempty requirement
	2
	Element object types by increasing source index
	3
	Unknown file-entry keys by source index, then UTF-8 key bytes
	4
	Missing path, then missing sha256, by source index
	5
	Member types by increasing source index, checking path before sha256 within one entry
	6
	Duplicate path selection under section 10.8
	7
	File-entry path grammar, selected by UTF-8 path then source index
	8
	Digest syntax, selected by admitted path order
	9
	Exact package.yaml self-listing, selected by admitted path order
	10
	Prefix-collision selection under section 10.9
	11
	module_file membership
20.5 Metadata audit precedence
Metadata audit occurs after complete descriptor admission.
Traversal is depth first, pre-order.
Children are ordered by NFC UTF-8 bytes.
At each node, a link-like object is reported immediately.
An unreadable directory is reported as PACKAGE_SCAN_DISCOVERY_UNREADABLE at that exact directory when its traversal turn begins.
Regular and special unlisted objects are not opened.
The audit includes all readable directory nodes in the admitted version subtree, regardless of whether a directory is unlisted, is an intermediate declared-path component, or is itself a declared final target.
Because this global stage completes for every candidate before declared-file verification begins, no unreadable-directory condition is owned by declared-file verification.
20.6 Declared-file traversal precedence
Declared files are verified by ascending ASCII logical path bytes.
For one path, each component is processed left to right.
At an intermediate component, precedence is:
Rank
	Check
	1
	Missing entry
	2
	Link-like object
	3
	Regular file where directory is required
	4
	Special object
	5
	Readable directory, whose readability was already established by metadata audit
	At the final component, precedence is:
Rank
	Check
	1
	Missing entry
	2
	Link-like object
	3
	Special object
	4
	Enumerable directory, whose readability was already established by metadata audit
	5
	Unreadable regular bytes
	6
	Regular immutable bytes
	7
	Digest comparison
	The canonical filesystem diagnostic path is the shortest project-relative prefix at which the failure is established.
A final missing target therefore reports the complete declared path.
An intermediate failure reports the path prefix ending at the failing component.
21. Resource limits
[N] This erratum defines no semantic maximum for package count, files per package, descriptor bytes, path bytes, individual file bytes, total snapshot bytes, package-tree depth below a version directory, or aggregate directory entries.
An implementation may fail operationally because the host cannot supply sufficient memory, storage, address space, time, or another resource.
Operational exhaustion is not a PC6 semantic diagnostic.
It produces no partial package set, no package identity from a partial scan, no ScannedSource, and no conforming completed compilation result.
Conformance comparison assumes resources sufficient to complete the fixture.
22. Non-authority
Successful Package scan proves the admitted canonical package descriptor, the declared raw-file digests, equality of retained bytes to those digests, and binding of the resulting package records to the exact DigestedSource.
It does not prove imported declaration validity, import reachability, profile compatibility, version resolution, fixed-point completion, import-cycle absence, Lockfile existence, namespace expansion, declaration normalization, static validity, declaration identity, Manifest existence, qualification, Binding, resource execution permission, filesystem access permission, network access permission, provider or model access, secret access, package installation authority, or runtime authority.
Package scan MUST NOT execute, dynamically load, or runtime-import any declared file.
23. Reference pseudocode
function scan_packages(source, snapshot):
    packages = snapshot.root.child("packages")
    if packages is absent:
        return private_scanned_source(source, [])
    require_packages_root(packages)
    candidate_records = []
    package_entries = sort_by_nfc_utf8(packages.children)
    for package_entry in package_entries:
        require_structural_package_entry(package_entry)
        version_entries = sort_by_nfc_utf8(package_entry.children)
        for version_entry in version_entries:
            require_structural_version_entry(version_entry)
            descriptor_entry = version_entry.child("package.yaml")
            require_descriptor_entry(descriptor_entry)
            candidate_records.append(
                package_entry.name,
                version_entry.name,
                version_entry,
                descriptor_entry
            )
    candidate_records = sort_by_package_ascii_then_numeric_version(
        candidate_records
    )
    parsed_records = []
    for candidate in candidate_records:
        parser_result = accepted_pc2_restricted_yaml(
            candidate.descriptor.bytes
        )
        if parser_result is SourceDiagnostic:
            return PackageScanDiagnostic(
                map_exact_pc2_code(parser_result.code),
                render(candidate.descriptor.path) + "#"
            )
        parsed = parser_result.value
        parsed_records.append(candidate, parsed)
    admitted_records = []
    for candidate, parsed in parsed_records:
        admitted = admit_shallow_descriptor_and_scalars(parsed)
        require_directory_agreement(admitted, candidate)
        admitted_records.append(candidate, admitted)
    normalized_records = []
    for candidate, admitted in admitted_records:
        normalized = validate_profiles_files_and_paths(admitted)
        normalized_records.append(candidate, normalized)
    for candidate, normalized in normalized_records:
        metadata_audit(candidate.version_directory)
    verified_records = []
    for candidate, normalized in normalized_records:
        verified_snapshot = {}
        for file in normalized.files_sorted_by_path:
            bytes = traverse_snapshot_and_require_regular_bytes(
                candidate.version_directory,
                split(file.path, "/")
            )
            require_sha256(bytes, file.sha256)
            verified_snapshot[file.path] = immutable(bytes)
        verified_records.append(
            candidate,
            normalized,
            immutable(verified_snapshot)
        )
    scanned_packages = []
    for candidate, normalized, verified_snapshot in verified_records:
        canonical_value = exact_canonical_descriptor_value(normalized)
        canonical_bytes = accepted_canonical_json(canonical_value)
        package_hash = accepted_sha256(canonical_bytes)
        package_id = "lattice:package:sha256:" + lowercase_hex(package_hash)
        scanned_packages.append(
            private_scanned_package(
                canonical_value,
                package_id,
                verified_snapshot
            )
        )
    return private_scanned_source(
        source,
        ordered(scanned_packages)
    )


function map_exact_pc2_code(code):
    SOURCE_INVALID_UTF8     -> PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID
    SOURCE_FORBIDDEN_YAML   -> PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN
    SOURCE_INVALID_SCALAR   -> PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID
    SOURCE_NON_STRING_KEY   -> PACKAGE_SCAN_DESCRIPTOR_NON_STRING_KEY
    SOURCE_DUPLICATE_KEY    -> PACKAGE_SCAN_DESCRIPTOR_DUPLICATE_KEY
    SOURCE_NFC_COLLISION    -> PACKAGE_SCAN_DESCRIPTOR_NFC_COLLISION


function metadata_audit(directory):
    if directory.child_map is unavailable:
        fail PACKAGE_SCAN_DISCOVERY_UNREADABLE at directory.path
    for child in sort_by_nfc_utf8(directory.children):
        if child is link-like:
            fail PACKAGE_SCAN_SYMLINK_FORBIDDEN at child.path
        if child is directory:
            metadata_audit(child)


function traverse_snapshot_and_require_regular_bytes(version_directory, segments):
    node = version_directory
    for each non-final segment in left-to-right order:
        child = node.child(segment)
        if child is absent:
            fail PACKAGE_SCAN_DECLARED_FILE_MISSING at child.path
        if child is link-like:
            fail PACKAGE_SCAN_SYMLINK_FORBIDDEN at child.path
        if child is regular:
            fail PACKAGE_SCAN_DECLARED_PATH_COMPONENT_NOT_DIRECTORY at child.path
        if child is special:
            fail PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT at child.path
        assert child is a directory with an available child map
        node = child
    final = node.child(final_segment)
    if final is absent:
        fail PACKAGE_SCAN_DECLARED_FILE_MISSING at final.path
    if final is link-like:
        fail PACKAGE_SCAN_SYMLINK_FORBIDDEN at final.path
    if final is special:
        fail PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT at final.path
    if final is directory:
        fail PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR at final.path
    if final is regular with unavailable bytes:
        fail PACKAGE_SCAN_DECLARED_FILE_UNREADABLE at final.path
    return final.immutable_bytes


A canonical encoder or hashing failure after descriptor admission is an internal non-semantic failure and does not return a PackageScanDiagnostic.
Exact PC6 Fixture Proposal
24. Fixture model
The fixture-manifest version is:
pc6-package-scan-fourth-repaired-candidate-5


A fixture contains an exact DigestedSource, an exact immutable portable snapshot or an exact snapshot-acquisition failure, and one expected semantic result.
A semantic fixture that does not state a different source and base begins with exact DS-A and an exact fresh copy of T-MINIMAL.
Every fixture is independent. Its operations are applied in written order only to that fresh copy.
USE_SOURCE(source) replaces DS-A for the complete fixture.
USE_BASE(snapshot) replaces T-MINIMAL before any mutation.
An operation never inherits state from another fixture.
Snapshot-acquisition fixtures replace the semantic source-and-snapshot default with their exact pre-snapshot condition and produce no PortableProjectSnapshot.
A portable snapshot node is represented as:
directory(children)
directory_unreadable
regular(hex_bytes, optional hardlink_group)
regular_unreadable
link(target_text)
special(kind)


directory(children) is a readable directory whose child map is exactly children; no child outside that map exists.
directory({}) is a readable directory with an exact empty child map.
The bare constructor token directory, if encountered in imported fixture notation, is exact shorthand for directory({}). No executable fixture in this candidate uses that shorthand.
All names are exact NFC Unicode strings unless the fixture explicitly describes a pre-snapshot native-name failure.
Every directory(children) node is readable. directory_unreadable is the only unreadable-directory constructor.
Every regular(hex_bytes, optional hardlink_group) node has immutable available bytes. regular_unreadable is the only unavailable-byte regular-file constructor.
No directory, regular file, or child is implied by omission.
The following exact mutation operations are used:
USE_SOURCE(source)
USE_BASE(snapshot)
ADD(path, node)
REMOVE(path)
REPLACE_NODE(path, node)
REPLACE_HEX(path, exact_hex)
REPLACE_UTF8(path, exact_utf8)
INSERT_UTF8_AFTER(path, exact_anchor, exact_text)
DELETE_UTF8_EXACT(path, exact_text)
SET_DESCRIPTOR(path, exact_descriptor_bytes)
RENAME(old_path, new_final_component)
SET_CHILD_ENUMERATION(path, exact_name_sequence)
SHARE_HARDLINK(path_a, path_b, group_id)
SNAPSHOT_ACQUISITION_FAILURE(reason, exact_native_name_evidence)


ADD(path, directory({})) creates a readable directory with no children at that exact path.
ADD of a descendant beneath that directory requires every non-final ancestor to exist as a readable directory and adds only the explicitly named descendant. Separately written ADD operations add only their own explicitly named descendants. No unlisted or unspecified child exists.
REPLACE_NODE(path, directory({})) replaces the complete node and its complete child map with an empty readable directory.
Each section 28 base snapshot contains only the children explicitly defined by that base. Its rows are applied in written order: a directory({}) row creates an empty readable directory, and later rows naming descendants add only those exact descendants. After the final row, every child map contains exactly the children explicitly listed beneath it.
Fixture mutations cannot create an implicit ancestor, child, or descendant.
Every text replacement requires exactly one matching occurrence.
Within fixture-operation and constructor notation, a double-quoted meta-string uses exactly these escapes: \n is byte 0A, \\ is byte 5C, and \" is byte 22. Every other displayed ASCII character is its single ASCII byte. A source-token hex declaration overrides rendered meta-string text and is authoritative.
When a descriptor constant rather than a snapshot path is the first argument to REPLACE_UTF8, INSERT_UTF8_AFTER, or DELETE_UTF8_EXACT, the operation transforms that exact descriptor byte sequence and replaces the fixture's package.yaml bytes with the result.
SET_DESCRIPTOR replaces the complete regular-file byte sequence at the named package.yaml path.
RENAME changes only the named directory entry's final NFC name and retains its entire immutable node.
For fixtures that require a descriptor not separately named in section 27, BD constructs exact descriptor bytes by ASCII concatenation:
BD(package, version, profiles, module_file, files) =
"package: " + package + "\n" +
"version: \"" + version + "\"\n" +
"lattice: \"0.3\"\n" +
"profiles:\n" +
for each profile in supplied source order:
    "  - " + profile + "\n" +
"module_file: " + module_file + "\n" +
"files:\n" +
for each (path, sha256) in supplied source order:
    "  - path: " + path + "\n" +
    "    sha256: " + sha256 + "\n"


BD has no implicit member, whitespace, comment, or trailing byte beyond the stated concatenation.
For exact YAML scalar-source spelling in path fixtures, BDP constructs:
BDP(path_scalar_source) =
"package: alpha\n" +
"version: \"1.0.0\"\n" +
"lattice: \"0.3\"\n" +
"profiles:\n" +
"  - lattice-core-0.1\n" +
"module_file: " + path_scalar_source + "\n" +
"files:\n" +
"  - path: " + path_scalar_source + "\n" +
"    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n"


path_scalar_source is the complete exact YAML scalar token without a line ending. BDP adds no other byte. Each BDP fixture states both the exact scalar-source bytes and the exact decoded NFC string value. Because module_file is validated before files, an inadmissible decoded path targets D#/module_file.
For multi-entry path fixtures, BDF(module_file_scalar_source, entries) uses the same fixed package, version, lattice, and profile prefix as BDP, then emits:
"module_file: " + module_file_scalar_source + "\n" +
"files:\n" +
for each (path_scalar_source, sha256_scalar_source) in supplied source order:
    "  - path: " + path_scalar_source + "\n" +
    "    sha256: " + sha256_scalar_source + "\n"


BDF adds no implicit entry or byte. Every BDF fixture supplies all entries and every scalar source token exactly.
25. DigestedSource vectors
25.1 DS-A
Canonical bytes:
{"contracts":[],"exports":[],"imports":[],"inputs":[],"lattice":"0.3","links":[],"module":"root","policies":[],"profile":"lattice-core-0.1","purpose":"fixture root","resources":[],"scenarios":[],"units":[],"version":"1.0.0"}


Length:
224


Hex:
7b22636f6e747261637473223a5b5d2c226578706f727473223a5b5d2c22696d706f727473223a5b5d2c22696e70757473223a5b5d2c226c617474696365223a22302e33222c226c696e6b73223a5b5d2c226d6f64756c65223a22726f6f74222c22706f6c6963696573223a5b5d2c2270726f66696c65223a226c6174746963652d636f72652d302e31222c22707572706f7365223a226669787475726520726f6f74222c227265736f7572636573223a5b5d2c227363656e6172696f73223a5b5d2c22756e697473223a5b5d2c2276657273696f6e223a22312e302e30227d


SHA-256:
196ff00d07966e5e60f787fc91fd4e9d1a7b52c8b7bb8ced93cc2d86443fe4b5


Identity:
lattice:blueprint:sha256:196ff00d07966e5e60f787fc91fd4e9d1a7b52c8b7bb8ced93cc2d86443fe4b5


25.2 DS-B
Canonical bytes:
{"contracts":[],"exports":[],"imports":[],"inputs":[],"lattice":"0.3","links":[],"module":"root","policies":[],"profile":"lattice-core-0.1","purpose":"fixture root b","resources":[],"scenarios":[],"units":[],"version":"1.0.0"}


Length:
226


Hex:
7b22636f6e747261637473223a5b5d2c226578706f727473223a5b5d2c22696d706f727473223a5b5d2c22696e70757473223a5b5d2c226c617474696365223a22302e33222c226c696e6b73223a5b5d2c226d6f64756c65223a22726f6f74222c22706f6c6963696573223a5b5d2c2270726f66696c65223a226c6174746963652d636f72652d302e31222c22707572706f7365223a226669787475726520726f6f742062222c227265736f7572636573223a5b5d2c227363656e6172696f73223a5b5d2c22756e697473223a5b5d2c2276657273696f6e223a22312e302e30227d


SHA-256:
4e0ca3af498ac0d0aa54c1fc302e0a6e8688761f6875375f2120e9f44005f3a4


Identity:
lattice:blueprint:sha256:4e0ca3af498ac0d0aa54c1fc302e0a6e8688761f6875375f2120e9f44005f3a4


26. Authoritative byte constants
In every constant below, hexadecimal is authoritative. Length and SHA-256 are recalculated from that hex. Any rendered text is explanatory only.
26.1 M_ALPHA_100
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e302e30220a707572706f73653a20616c706861207061636b6167650a756e6974733a205b5d0a


Length and SHA-256:
105
900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55


26.2 M_ALPHA_110
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e312e30220a707572706f73653a20616c706861207061636b6167650a756e6974733a205b5d0a


Length and SHA-256:
105
bcf3b8591ddedb2f578fb75ec773abea499b82b6baaaee9f4a5fcb0e60efe551


26.3 M_BETA_200
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20626574610a76657273696f6e3a2022322e302e30220a707572706f73653a2062657461207061636b6167650a756e6974733a205b5d0a


Length and SHA-256:
103
80d80984355a2fce54a4b9c03c75ff4f880e155bd0c668efbf7404183f353e85


26.4 M_TEXT_TOOLS
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20746578745f746f6f6c730a76657273696f6e3a2022312e332e31220a707572706f73653a207465787420746f6f6c73207061636b6167650a756e6974733a205b5d0a


Length and SHA-256:
115
bfeaac869e4dffdda7420438e2ee780adcd958d0c67acda9a717c78e0d177a6d


26.5 V_NO_BULLETS
Authoritative hex:
646566206e6f5f62756c6c6574732874657874293a0a2020202072657475726e20222d2022206e6f7420696e20746578740a


Length and SHA-256:
50
94a10cbfdc1bf4260ba3ef1ce611b45bd8243d3b362b116ee7dc819b34565060


Exact escaped UTF-8 rendering:
def no_bullets(text):\n\x20\x20\x20\x20return "- " not in text\n


The second line begins with exactly four U+0020 bytes.
26.6 EMPTY
Authoritative hex:




Length and SHA-256:
0
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855


26.7 DATA
Authoritative hex:
616c70686120646174610a


Length and SHA-256:
11
c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73


26.8 DATA_CHANGED
Authoritative hex:
616c7068612064617461206368616e6765640a


Length and SHA-256:
19
792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2


26.9 M_ALPHA_CHANGED
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e302e30220a707572706f73653a20616c706861207061636b616765206368616e6765640a756e6974733a205b5d0a


Length and SHA-256:
113
9b9f2b1e36beaad57c6436ad62b9bef6e01db6203d5567ac3afd0b1a0785acff


26.10 M_INVALID_YAML
Authoritative hex:
756e6974733a205b0a


Length and SHA-256:
9
7b8412cfb68dc835e7ccbdba401b79052a99f8f9e6dd3c955e47358506232945


26.11 M_UNRESOLVED_IMPORT
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e302e30220a707572706f73653a20756e7265736f6c76656420696d706f72740a696d706f7274733a0a20202d207573653a206d697373696e675f706b670a2020202076657273696f6e3a20225e312e302e30220a2020202061733a206d697373696e670a756e6974733a205b5d0a


Length and SHA-256:
177
43332c30f07a88388a60f93b9f76b21ed16f8d40ed130af788474d9017184916


Exact escaped UTF-8 rendering:
lattice: "0.3"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: "1.0.0"\npurpose: unresolved import\nimports:\n\x20\x20- use: missing_pkg\n\x20\x20\x20\x20version: "^1.0.0"\n\x20\x20\x20\x20as: missing\nunits: []\n


The list marker line begins with two U+0020 bytes. The version and as lines begin with four U+0020 bytes.
26.12 M_UNSATISFIED_VERSION
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e302e30220a707572706f73653a20756e7361746973666965642076657273696f6e0a696d706f7274733a0a20202d207573653a20626574610a2020202076657273696f6e3a20225e392e302e30220a2020202061733a2062657461390a756e6974733a205b5d0a


Length and SHA-256:
170
25628abdc47ca14733a318bf3007e15689efa276e8a60fc55a459080fde165e2


Exact escaped UTF-8 rendering:
lattice: "0.3"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: "1.0.0"\npurpose: unsatisfied version\nimports:\n\x20\x20- use: beta\n\x20\x20\x20\x20version: "^9.0.0"\n\x20\x20\x20\x20as: beta9\nunits: []\n


26.13 M_LATER_INVALID_BODY
Authoritative hex:
6c6174746963653a2022302e33220a70726f66696c653a206c6174746963652d636f72652d302e310a6d6f64756c653a20616c7068610a76657273696f6e3a2022312e302e30220a707572706f73653a206c6174657220696e76616c69640a756e6974733a0a20202d206e616d653a2062726f6b656e0a202020206b696e643a206e6f745f615f636f72655f6b696e640a


Length and SHA-256:
145
87d252d0ef0f72f94eecbd7bb30ab17a8d24940e4bd1ca227f77ac1871c502e4


Exact escaped UTF-8 rendering:
lattice: "0.3"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: "1.0.0"\npurpose: later invalid\nunits:\n\x20\x20- name: broken\n\x20\x20\x20\x20kind: not_a_core_kind\n


26.14 M_OPAQUE
M_OPAQUE is an exact binary module payload. It is not descriptor YAML and PC6 never parses it.
Authoritative hex:
00ff804c4154544943450a


Length and SHA-256:
11
7d92f51ef5701e0e78e1bb5ded05de427c6818dd6cbc9822fd95a949a0e8e10d


27. Descriptor source constants
27.1 D_MIN
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
209
3c05bc67312c14a02ad9bb20862346510926ca56fd1911f07b8c8de97810eec8


27.2 D_MULTI
Authoritative hex:
66696c65733a0a20202d207368613235363a20393461313063626664633162663432363062613365663163653631316234356264383234336433623336326231313665653764633831396233343536353036300a20202020706174683a2076616c696461746f72732f6e6f5f62756c6c6574732e70790a20202d207368613235363a20626665616163383639653464666664646137343230343338653265653738306164636439353864306336376163646139613731376337386530643137376136640a20202020706174683a206d6f64756c652e79616d6c0a20202d207368613235363a20653362306334343239386663316331343961666266346338393936666239323432376165343165343634396239333463613439353939316237383532623835350a20202020706174683a20656d7074792e7478740a6d6f64756c655f66696c653a20226d6f64756c652e79616d6c220a70726f66696c65733a205b6c6174746963652d636f72652d302e312c206c6174746963652d6275696c6465722d302e315d0a6c6174746963653a2022302e33220a76657273696f6e3a2022312e332e31220a7061636b6167653a20746578745f746f6f6c730a


Length and SHA-256:
444
44792eae6572ad36f5288067306bf7181e3fe21f9cd6128675c75b25f1c0c961


27.3 D_ALPHA_110
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e312e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20626366336238353931646465646232663537386662373565633737336162656134393962383262366261616165653966346135666362306536306566653535310a


Length and SHA-256:
209
3bf1d883ff9571c62712b0f49830e472c889bfa538479afc8ad89f13fe8ba1dc


27.4 D_BETA_200
Authoritative hex:
7061636b6167653a20626574610a76657273696f6e3a2022322e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20383064383039383433353561326663653534613462396330336337356666346638383065313535626430633636386566626637343034313833663335336538350a


Length and SHA-256:
208
4486f30a679b920f093b0560ecebe16a4a23ec98aa286bcd5c365deba7ce7f1f


27.5 D_HARDLINK
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a20612e7478740a202020207368613235363a20633065663238616130346663306531326535376561323935616539663335366230393237316364313961366237393936616233613336356132643838656537330a20202d20706174683a20622e7478740a202020207368613235363a20633065663238616130346663306531326535376561323935616539663335366230393237316364313961366237393936616233613336356132643838656537330a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
395
88dc9fa0b217977a62f4836ee86a1731ac936a075c4662e0ddceedfea87fd640


27.6 D_ALPHA_2_0_0
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022322e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
209
86b42b0660fcf2b2e2db0eb46472253abc0996cf196f70261f1f699113d3eb8d


27.7 D_ALPHA_10_0_0
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a202231302e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
210
6ee0d8cbc29faa40730af59414530b965b4d3cfff2a77a9dd2bb17b06b8220a9


27.8 D_MIN_REVERSED
Authoritative hex:
66696c65733a0a20202d207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a20202020706174683a206d6f64756c652e79616d6c0a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6c6174746963653a2022302e33220a76657273696f6e3a2022312e302e30220a7061636b6167653a20616c7068610a


Length and SHA-256:
209
36265bc6c10de3fa5222168cce055f13f45bbe59aa97d0b539e60ea3a39405e5


27.9 D_MIN_COMMENTED
Authoritative hex:
23207061636b61676520666978747572650a7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
227
46c3d438fed6ad7988ba03df449a8ab5b4c520dda934f60566c4beb88509e7c8


27.10 D_MIN_INDENT4
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a202020202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a202020202d20706174683a206d6f64756c652e79616d6c0a2020202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350a


Length and SHA-256:
215
9705c25fa5fd8b95300ac1376dee0f15acc135221e41b73faeac4ad5ee8d7d2c


27.11 D_MIN_QUOTED
Authoritative hex:
227061636b616765223a2022616c706861220a2276657273696f6e223a2022312e302e30220a226c617474696365223a2022302e33220a2270726f66696c6573223a0a20202d20226c6174746963652d636f72652d302e31220a226d6f64756c655f66696c65223a20226d6f64756c652e79616d6c220a2266696c6573223a0a20202d202270617468223a20226d6f64756c652e79616d6c220a2020202022736861323536223a202239303064643338393361373139656337656131636235616366663865633739393232336436623864336633633664656133656230396632643036623637623535220a


Length and SHA-256:
235
0cfc3fa97eb2433d089f443e62c264a33873c48c9de0164c068c310ec75d86dc


27.12 D_MIN_CRLF and D_MIN_CR
D_MIN_CRLF is obtained only by replacing every 0A byte in D_MIN by 0D0A.
Its authoritative hex is:
7061636b6167653a20616c7068610d0a76657273696f6e3a2022312e302e30220d0a6c6174746963653a2022302e33220d0a70726f66696c65733a0d0a20202d206c6174746963652d636f72652d302e310d0a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0d0a66696c65733a0d0a20202d20706174683a206d6f64756c652e79616d6c0d0a202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350d0a


Its authoritative length and SHA-256 are:
218
4b406f628c0b7386153e54663d9a9de824d90a5a1e3b6589907a799d75044281


D_MIN_CR is obtained only by replacing every 0A byte in D_MIN by 0D.
Its authoritative hex is:
7061636b6167653a20616c7068610d76657273696f6e3a2022312e302e30220d6c6174746963653a2022302e33220d70726f66696c65733a0d20202d206c6174746963652d636f72652d302e310d6d6f64756c655f66696c653a206d6f64756c652e79616d6c0d66696c65733a0d20202d20706174683a206d6f64756c652e79616d6c0d202020207368613235363a20393030646433383933613731396563376561316362356163666638656337393932323364366238643366336336646561336562303966326430366236376235350d


Its authoritative length and SHA-256 are:
209
eb93759af8a948e2a78be9f18a34e51039e3a382099104aeffede7410f02b635


27.13 D_MULTI_FILES_ALT and D_MULTI_PROFILES_ALT
D_MULTI_FILES_ALT authoritative hex:
66696c65733a0a20202d207368613235363a20626665616163383639653464666664646137343230343338653265653738306164636439353864306336376163646139613731376337386530643137376136640a20202020706174683a206d6f64756c652e79616d6c0a20202d207368613235363a20653362306334343239386663316331343961666266346338393936666239323432376165343165343634396239333463613439353939316237383532623835350a20202020706174683a20656d7074792e7478740a20202d207368613235363a20393461313063626664633162663432363062613365663163653631316234356264383234336433623336326231313665653764633831396233343536353036300a20202020706174683a2076616c696461746f72732f6e6f5f62756c6c6574732e70790a6d6f64756c655f66696c653a20226d6f64756c652e79616d6c220a70726f66696c65733a205b6c6174746963652d636f72652d302e312c206c6174746963652d6275696c6465722d302e315d0a6c6174746963653a2022302e33220a76657273696f6e3a2022312e332e31220a7061636b6167653a20746578745f746f6f6c730a


Length and SHA-256:
444
369904d67d8b97823e1df1b6a6963999fe2033a41dbd38ba4fc0b4eb94db02ab


D_MULTI_PROFILES_ALT authoritative hex:
66696c65733a0a20202d207368613235363a20393461313063626664633162663432363062613365663163653631316234356264383234336433623336326231313665653764633831396233343536353036300a20202020706174683a2076616c696461746f72732f6e6f5f62756c6c6574732e70790a20202d207368613235363a20626665616163383639653464666664646137343230343338653265653738306164636439353864306336376163646139613731376337386530643137376136640a20202020706174683a206d6f64756c652e79616d6c0a20202d207368613235363a20653362306334343239386663316331343961666266346338393936666239323432376165343165343634396239333463613439353939316237383532623835350a20202020706174683a20656d7074792e7478740a6d6f64756c655f66696c653a20226d6f64756c652e79616d6c220a70726f66696c65733a205b6c6174746963652d6275696c6465722d302e312c206c6174746963652d636f72652d302e315d0a6c6174746963653a2022302e33220a76657273696f6e3a2022312e332e31220a7061636b6167653a20746578745f746f6f6c730a


Length and SHA-256:
444
6a5e485c17ec5a5f1395cb7b55ac86a3d306eed5d1c9223867f4283d9a60a722


27.14 D_DIGEST_F63
D_DIGEST_F63 is D_MIN with its declared digest replaced by exactly 63 lowercase ASCII f characters. The plain scalar is a string under accepted PC2 semantics.
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a206666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666660a


Length and SHA-256:
208
7fb80cc9809bcff098f2adbb71764edcafc57ae4ee5ac524a436aa035f12fcc4


27.15 D_DIGEST_F64
D_DIGEST_F64 is D_MIN with its declared digest replaced by exactly 64 lowercase ASCII f characters. It is syntactically valid digest text and intentionally differs from M_ALPHA_100.
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666660a


Length and SHA-256:
209
33729846e931436932be0c406caf59a285990fca92781fd1e587a6689e7ee6d7


27.16 D_OPAQUE
D_OPAQUE is the exact BD output for alpha 1.0.0, the Core profile, module_file module.yaml, and sole file module.yaml with the M_OPAQUE digest.
Authoritative hex:
7061636b6167653a20616c7068610a76657273696f6e3a2022312e302e30220a6c6174746963653a2022302e33220a70726f66696c65733a0a20202d206c6174746963652d636f72652d302e310a6d6f64756c655f66696c653a206d6f64756c652e79616d6c0a66696c65733a0a20202d20706174683a206d6f64756c652e79616d6c0a202020207368613235363a20376439326635316566353730316530653738653162623564656430356465343237633638313864643663626339383232666439356139343961306538653130640a


Length and SHA-256:
209
e017ddd1889e0098920992862911724a76ee28109f5e717b51956589972e5d81


28. Exact base snapshots
28.1 T-ABSENT
The root contains no entry named packages.
28.2 T-EMPTY
packages/    directory({})


28.3 T-MINIMAL
packages/                              directory({})
packages/alpha/                        directory({})
packages/alpha/1.0.0/                  directory({})
packages/alpha/1.0.0/package.yaml      regular(D_MIN)
packages/alpha/1.0.0/module.yaml       regular(M_ALPHA_100)


28.4 T-MULTIPLE-PACKAGES
T-MINIMAL plus:
packages/beta/                         directory({})
packages/beta/2.0.0/                   directory({})
packages/beta/2.0.0/package.yaml       regular(D_BETA_200)
packages/beta/2.0.0/module.yaml        regular(M_BETA_200)


28.5 T-MULTIPLE-VERSIONS
T-MINIMAL plus:
packages/alpha/1.1.0/                  directory({})
packages/alpha/1.1.0/package.yaml      regular(D_ALPHA_110)
packages/alpha/1.1.0/module.yaml       regular(M_ALPHA_110)


28.6 T-MULTI-FILE
packages/                                              directory({})
packages/text_tools/                                   directory({})
packages/text_tools/1.3.1/                             directory({})
packages/text_tools/1.3.1/package.yaml                 regular(D_MULTI)
packages/text_tools/1.3.1/module.yaml                  regular(M_TEXT_TOOLS)
packages/text_tools/1.3.1/empty.txt                    regular(EMPTY)
packages/text_tools/1.3.1/validators/                  directory({})
packages/text_tools/1.3.1/validators/no_bullets.py     regular(V_NO_BULLETS)


28.7 T-HARDLINK
T-HARDLINK is:
packages/                              directory({})
packages/alpha/                        directory({})
packages/alpha/1.0.0/                  directory({})
packages/alpha/1.0.0/package.yaml      regular(D_HARDLINK)
packages/alpha/1.0.0/module.yaml       regular(M_ALPHA_100)
packages/alpha/1.0.0/a.txt             regular(DATA, hardlink_group=h1)
packages/alpha/1.0.0/b.txt             regular(DATA, hardlink_group=h1)


The two declared paths are distinct directory entries sharing one immutable content object.
28.8 T-VERSION-ORDER
T-VERSION-ORDER is:
packages/                              directory({})
packages/alpha/                        directory({})
packages/alpha/2.0.0/                  directory({})
packages/alpha/2.0.0/package.yaml      regular(D_ALPHA_2_0_0)
packages/alpha/2.0.0/module.yaml       regular(M_ALPHA_100)
packages/alpha/10.0.0/                 directory({})
packages/alpha/10.0.0/package.yaml     regular(D_ALPHA_10_0_0)
packages/alpha/10.0.0/module.yaml      regular(M_ALPHA_100)


Structural version-name traversal examines 10.0.0 before 2.0.0 because diagnostic traversal uses NFC UTF-8 bytes.
After structural success, canonical candidate processing and successful record order are 2.0.0 then 10.0.0 because candidate order uses numeric version tuples.
29. Golden canonical package vectors
29.1 Minimal package
Canonical bytes:
{"files":[{"path":"module.yaml","sha256":"900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"1.0.0"}


Length:
222


Hex:
7b2266696c6573223a5b7b2270617468223a226d6f64756c652e79616d6c222c22736861323536223a2239303064643338393361373139656337656131636235616366663865633739393232336436623864336633633664656133656230396632643036623637623535227d5d2c226c617474696365223a22302e33222c226d6f64756c655f66696c65223a226d6f64756c652e79616d6c222c227061636b616765223a22616c706861222c2270726f66696c6573223a5b226c6174746963652d636f72652d302e31225d2c2276657273696f6e223a22312e302e30227d


SHA-256:
bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b


Identity:
lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b


29.2 Multi-file package
Canonical bytes:
{"files":[{"path":"empty.txt","sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"path":"module.yaml","sha256":"bfeaac869e4dffdda7420438e2ee780adcd958d0c67acda9a717c78e0d177a6d"},{"path":"validators/no_bullets.py","sha256":"94a10cbfdc1bf4260ba3ef1ce611b45bd8243d3b362b116ee7dc819b34565060"}],"lattice":"0.3","module_file":"module.yaml","package":"text_tools","profiles":["lattice-builder-0.1","lattice-core-0.1"],"version":"1.3.1"}


Length:
458


Hex:
7b2266696c6573223a5b7b2270617468223a22656d7074792e747874222c22736861323536223a2265336230633434323938666331633134396166626634633839393666623932343237616534316534363439623933346361343935393931623738353262383535227d2c7b2270617468223a226d6f64756c652e79616d6c222c22736861323536223a2262666561616338363965346466666464613734323034333865326565373830616463643935386430633637616364613961373137633738653064313737613664227d2c7b2270617468223a2276616c696461746f72732f6e6f5f62756c6c6574732e7079222c22736861323536223a2239346131306362666463316266343236306261336566316365363131623435626438323433643362333632623131366565376463383139623334353635303630227d5d2c226c617474696365223a22302e33222c226d6f64756c655f66696c65223a226d6f64756c652e79616d6c222c227061636b616765223a22746578745f746f6f6c73222c2270726f66696c6573223a5b226c6174746963652d6275696c6465722d302e31222c226c6174746963652d636f72652d302e31225d2c2276657273696f6e223a22312e332e31227d


SHA-256:
ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8


Identity:
lattice:package:sha256:ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8


The source profile order is Core then Builder. Canonical order is Builder then Core.
The source file order is validators/no_bullets.py, module.yaml, empty.txt. Canonical order is empty.txt, module.yaml, validators/no_bullets.py.
29.3 Hard-link package
Canonical bytes:
{"files":[{"path":"a.txt","sha256":"c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73"},{"path":"b.txt","sha256":"c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73"},{"path":"module.yaml","sha256":"900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"1.0.0"}


SHA-256:
403906116513b9c432a9f9558d7af747286b5539ee95563fba019d38584a1dc7


Identity:
lattice:package:sha256:403906116513b9c432a9f9558d7af747286b5539ee95563fba019d38584a1dc7


Hard-link metadata does not appear in the preimage.
29.4 Numeric-version-order packages
Alpha 2.0.0 canonical bytes:
{"files":[{"path":"module.yaml","sha256":"900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"2.0.0"}


Length, hex, SHA-256, and identity:
222
7b2266696c6573223a5b7b2270617468223a226d6f64756c652e79616d6c222c22736861323536223a2239303064643338393361373139656337656131636235616366663865633739393232336436623864336633633664656133656230396632643036623637623535227d5d2c226c617474696365223a22302e33222c226d6f64756c655f66696c65223a226d6f64756c652e79616d6c222c227061636b616765223a22616c706861222c2270726f66696c6573223a5b226c6174746963652d636f72652d302e31225d2c2276657273696f6e223a22322e302e30227d
0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752
lattice:package:sha256:0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752


Alpha 10.0.0 canonical bytes:
{"files":[{"path":"module.yaml","sha256":"900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"10.0.0"}


Length, hex, SHA-256, and identity:
223
7b2266696c6573223a5b7b2270617468223a226d6f64756c652e79616d6c222c22736861323536223a2239303064643338393361373139656337656131636235616366663865633739393232336436623864336633633664656133656230396632643036623637623535227d5d2c226c617474696365223a22302e33222c226d6f64756c655f66696c65223a226d6f64756c652e79616d6c222c227061636b616765223a22616c706861222c2270726f66696c6573223a5b226c6174746963652d636f72652d302e31225d2c2276657273696f6e223a2231302e302e30227d
842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407
lattice:package:sha256:842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407
29.5 Opaque-binary module package
Canonical bytes:
{"files":[{"path":"module.yaml","sha256":"7d92f51ef5701e0e78e1bb5ded05de427c6818dd6cbc9822fd95a949a0e8e10d"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"1.0.0"}


Length:
222


Hex:
7b2266696c6573223a5b7b2270617468223a226d6f64756c652e79616d6c222c22736861323536223a2237643932663531656635373031653065373865316262356465643035646534323763363831386464366362633938323266643935613934396130653865313064227d5d2c226c617474696365223a22302e33222c226d6f64756c655f66696c65223a226d6f64756c652e79616d6c222c227061636b616765223a22616c706861222c2270726f66696c6573223a5b226c6174746963652d636f72652d302e31225d2c2276657273696f6e223a22312e302e30227d


SHA-256:
981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a


Identity:
lattice:package:sha256:981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a
30. Additional exact package identities
Fixture record
	Package SHA-256
	Complete identity
	Alpha 1.1.0
	10cb5b7f8f6d9074d1bb625770af63fa84573dce7f356db9f1a51829e0e9f399
	lattice:package:sha256:10cb5b7f8f6d9074d1bb625770af63fa84573dce7f356db9f1a51829e0e9f399
	Alpha 2.0.0 using M_ALPHA_100
	0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752
	lattice:package:sha256:0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752
	Alpha 10.0.0 using M_ALPHA_100
	842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407
	lattice:package:sha256:842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407
	Beta 2.0.0
	9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4
	lattice:package:sha256:9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4
	Beta with minimal Alpha bytes
	b6705fd7774024451a41bccd82dae7f7ead5c998341a10afbff2c77a6dac20e1
	lattice:package:sha256:b6705fd7774024451a41bccd82dae7f7ead5c998341a10afbff2c77a6dac20e1
	Alpha version 1.0.1
	9f305028f064ace9b8d839ad48f8dcd62281e3bc5ba081177d85e143232a098e
	lattice:package:sha256:9f305028f064ace9b8d839ad48f8dcd62281e3bc5ba081177d85e143232a098e
	Alpha with both profiles
	934a9bc2921a91d1d1145956389a4b3a0dcc887756e33f909d00cf3e00287576
	lattice:package:sha256:934a9bc2921a91d1d1145956389a4b3a0dcc887756e33f909d00cf3e00287576
	Two modules, module.yaml selected
	6e7bc9698250aaa255189f5a8d8e74b91b52547deb7e66a9e602393bd5d8c476
	lattice:package:sha256:6e7bc9698250aaa255189f5a8d8e74b91b52547deb7e66a9e602393bd5d8c476
	Two modules, entry.yaml selected
	9031644cb03fe56a568c6635f88cda9130ca89e97f91723a710215e27da8f37b
	lattice:package:sha256:9031644cb03fe56a568c6635f88cda9130ca89e97f91723a710215e27da8f37b
	Add data.txt
	51b4317223471152bf1e81041a58edb10507a6be370317b49b3cf5c7f93aa80a
	lattice:package:sha256:51b4317223471152bf1e81041a58edb10507a6be370317b49b3cf5c7f93aa80a
	Move same data to docs/data.txt
	676636785015758fc969e33b6f153f7787e507742547509d84b9f6c9e83bc495
	lattice:package:sha256:676636785015758fc969e33b6f153f7787e507742547509d84b9f6c9e83bc495
	Change data.txt bytes and digest
	b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b
	lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b
	The exact construction for this same identity record uses the normal DS-A and a fresh T-MINIMAL, followed only by:
ADD(
    packages/alpha/1.0.0/data.txt,
    regular(DATA_CHANGED)
)
SET_DESCRIPTOR(
    packages/alpha/1.0.0/package.yaml,
    BD(
        alpha,
        1.0.0,
        [lattice-core-0.1],
        module.yaml,
        [
            (
                module.yaml,
                900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55
            ),
            (
                data.txt,
                792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2
            )
        ]
    )
)
	The complete verified file set is module.yaml from T-MINIMAL plus data.txt containing DATA_CHANGED. For this record, DATA_CHANGED is exact hex 616c7068612064617461206368616e6765640a, length 19, and SHA-256 792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2.
	The resulting canonical six-member descriptor contains exactly:
lattice = "0.3"
package = "alpha"
version = "1.0.0"
profiles = ["lattice-core-0.1"]
module_file = "module.yaml"
files = [(data.txt, 792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2), (module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]
	The canonical files collection is sorted by path, placing data.txt before module.yaml.
	Applying the accepted canonical JSON rules to that exact six-member object independently reproduces package SHA-256 b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b and identity lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b.
	This exact construction expands the existing identity record. It creates no new fixture ID and no additional golden canonical package vector.
	Add empty file
	5acd1d6ab712dd052ad942bff1f7f840e7215d44fc479fba29492d0b75097778
	lattice:package:sha256:5acd1d6ab712dd052ad942bff1f7f840e7215d44fc479fba29492d0b75097778
	Change module bytes and digest
	c100d984afe465b06fd525f42a519651e094ff63a15a29f315a4ca3ff1047ef6
	lattice:package:sha256:c100d984afe465b06fd525f42a519651e094ff63a15a29f315a4ca3ff1047ef6
	Invalid-YAML module bytes
	67615ce7c1071eb92ade638f888c1bd0fa866716849e72813635eb7c1b9c3d4b
	lattice:package:sha256:67615ce7c1071eb92ade638f888c1bd0fa866716849e72813635eb7c1b9c3d4b
	Unresolved-import module bytes
	b7a30c594bc90b58cc0127d350ae942d657415c1a234fdfc418bd0954f13b16e
	lattice:package:sha256:b7a30c594bc90b58cc0127d350ae942d657415c1a234fdfc418bd0954f13b16e
	Unsatisfied-version module bytes
	037b2e0b64dccd3f890923d393b73c0dc56807d0149468791412bd98d20accfb
	lattice:package:sha256:037b2e0b64dccd3f890923d393b73c0dc56807d0149468791412bd98d20accfb
	Later-invalid declaration bytes
	ede26ac500571dae4a6d00717d04ced75c2fdd070de95e620dda8731256e5f9f
	lattice:package:sha256:ede26ac500571dae4a6d00717d04ced75c2fdd070de95e620dda8731256e5f9f
	Opaque binary module bytes
	981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a
	lattice:package:sha256:981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a
	The third repair adds the opaque-module vector. It changes no pre-existing calculated hash or package identity in this table.
31. Valid fixtures
Fixture ID
	Exact input
	Expected result
	VAL-ROOT-ABSENT
	DS-A, T-ABSENT
	Success with exact DS-A, empty ordered package sequence, empty byte mapping
	VAL-ROOT-EMPTY
	DS-A, T-EMPTY
	Success with exact DS-A, empty ordered package sequence, empty byte mapping
	VAL-MINIMAL
	DS-A, T-MINIMAL
	Exact identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b with module.yaml mapped to exact M_ALPHA_100
	VAL-MULTIPLE-PACKAGES
	DS-A, T-MULTIPLE-PACKAGES
	Ordered identities lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b then lattice:package:sha256:9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4
	VAL-MULTIPLE-VERSIONS
	DS-A, T-MULTIPLE-VERSIONS
	Ordered identities lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b then lattice:package:sha256:10cb5b7f8f6d9074d1bb625770af63fa84573dce7f356db9f1a51829e0e9f399
	VAL-NUMERIC-VERSION-ORDER
	DS-A, T-VERSION-ORDER
	Structural traversal examines 10.0.0 first; successful records are ordered lattice:package:sha256:0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752 then lattice:package:sha256:842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407
	VAL-MULTIPLE-FILES
	DS-A, T-MULTI-FILE
	Identity lattice:package:sha256:ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8 with exact M_TEXT_TOOLS, EMPTY, and V_NO_BULLETS mapping
	VAL-EMPTY-FILE
	DS-A, T-MULTI-FILE
	empty.txt retains zero bytes and the exact empty digest
	VAL-DISCOVERY-ORDER
	USE_BASE(T-MULTIPLE-PACKAGES); SET_CHILD_ENUMERATION(packages, [beta, alpha]); SET_CHILD_ENUMERATION(packages/alpha, [1.0.0]); SET_CHILD_ENUMERATION(packages/alpha/1.0.0, [module.yaml, package.yaml]); SET_CHILD_ENUMERATION(packages/beta, [2.0.0]); SET_CHILD_ENUMERATION(packages/beta/2.0.0, [module.yaml, package.yaml])
	Ordered identities lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b then lattice:package:sha256:9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4
	VAL-HARDLINK
	DS-A, T-HARDLINK
	Identity lattice:package:sha256:403906116513b9c432a9f9558d7af747286b5539ee95563fba019d38584a1dc7 with a.txt and b.txt separately bound to exact DATA
	VAL-UNLISTED-REGULAR
	ADD(packages/alpha/1.0.0/ignored.bin, regular(EMPTY))
	Exact minimal identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b; ignored.bin bytes are not read or retained
	VAL-UNLISTED-SPECIAL
	ADD(packages/alpha/1.0.0/ignored.sock, special(socket))
	Exact minimal identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	VAL-UNICODE-UNLISTED
	ADD(packages/alpha/1.0.0/café.txt, regular(EMPTY)), with the name encoded as NFC UTF-8 hex 636166c3a92e747874
	Exact minimal identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b; name is ordered by NFC UTF-8 and bytes remain unread
	VAL-PERCENT-UNLISTED
	ADD(packages/alpha/1.0.0/100%.txt, regular(EMPTY))
	Exact minimal identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	32. Snapshot-acquisition boundary fixtures
Fixture ID
	Exact pre-snapshot condition
	Expected
	SNAP-NONUTF8-UNIX-NAME
	SNAPSHOT_ACQUISITION_FAILURE(unrepresentable native name, exact native filename bytes ff inside the included packages subtree)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-MALFORMED-UTF16-NAME
	SNAPSHOT_ACQUISITION_FAILURE(malformed UTF-16 name, exact unpaired high surrogate D800 inside the included packages subtree)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-NFC-COLLISION
	SNAPSHOT_ACQUISITION_FAILURE(post-NFC name collision, one included native directory contains exact names U+00E9 and U+0065 U+0301)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-HOST-CASE-ALIAS
	SNAPSHOT_ACQUISITION_FAILURE(host namespace alias, included entries exact a and A cannot be represented as distinct)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-TRAILING-DOT-ALIAS
	SNAPSHOT_ACQUISITION_FAILURE(host namespace alias, included entries exact name and name. cannot be represented as distinct)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-CONCURRENT-MUTATION
	SNAPSHOT_ACQUISITION_FAILURE(concurrent mutation, host cannot produce one immutable point-in-time view of exact packages subtree)
	Snapshot-acquisition failure; no partial package set
	SNAP-ABA-MUTATION
	SNAPSHOT_ACQUISITION_FAILURE(ABA mutation, included directory state changes exact A to B to A and host cannot establish one point)
	Snapshot-acquisition failure; no PC6 diagnostic
	SNAP-RESOURCE-EXHAUSTION
	SNAPSHOT_ACQUISITION_FAILURE(resource exhaustion, storage fails while acquiring the exact packages subtree)
	Operational failure; no semantic result
	SNAP-UNRELATED-ROOT-NAME
	Host root has unrelated native entry bytes ff; exact lookup of the one child packages independently yields exact T-MINIMAL
	Snapshot acquisition MUST NOT enumerate the unrelated entry; PC6 receives T-MINIMAL and succeeds with the minimal identity
	33. Portable-name and diagnostic-rendering fixtures
Fixture ID
	Exact snapshot input
	Expected
	NAME-UNICODE-STRUCTURAL
	ADD(packages/café, directory({})), with exact NFC component hex 636166c3a9
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/caf%C3%A9
	NAME-PERCENT-STRUCTURAL
	ADD(packages/100%, directory({}))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/100%25
	NAME-SPACE-STRUCTURAL
	ADD(packages/a b, directory({}))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/a%20b
	NAME-UTF8-ORDER
	ADD(packages/z!, directory({})); ADD(packages/é, directory({})), with exact NFC é component hex c3a9
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/z%21, because 7A 21 precedes C3 A9
	NAME-PERCENT-ORDER
	ADD(packages/%, directory({})); ADD(packages/a, directory({}))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/%25, because byte 25 precedes 61
	NAME-UNICODE-UNLISTED-SYMLINK
	ADD(packages/alpha/1.0.0/café, link("target")), with exact NFC component hex 636166c3a9
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0/caf%C3%A9
	34. Presentation-equivalence fixtures
Fixture ID
	Exact descriptor presentation
	Expected
	EQ-KEY-ORDER
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_REVERSED)
	Canonical bytes and identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-COMMENTS
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_COMMENTED)
	Canonical bytes and identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-INDENTATION
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_INDENT4)
	Canonical bytes and identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-QUOTING
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_QUOTED)
	Canonical bytes and identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-LINE-ENDINGS-LF
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN)
	Identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-LINE-ENDINGS-CRLF
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_CRLF)
	Identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-LINE-ENDINGS-CR
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN_CR)
	Identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b
	EQ-FILES-ORDER
	USE_BASE(T-MULTI-FILE); SET_DESCRIPTOR(packages/text_tools/1.3.1/package.yaml, D_MULTI_FILES_ALT)
	Identity lattice:package:sha256:ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8
	EQ-PROFILES-ORDER
	USE_BASE(T-MULTI-FILE); SET_DESCRIPTOR(packages/text_tools/1.3.1/package.yaml, D_MULTI_PROFILES_ALT)
	Identity lattice:package:sha256:ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8
	EQ-PHYSICAL-ENUMERATION
	USE_BASE(T-MULTIPLE-PACKAGES); SET_CHILD_ENUMERATION(packages, [beta, alpha]); SET_CHILD_ENUMERATION(packages/alpha, [1.0.0]); SET_CHILD_ENUMERATION(packages/alpha/1.0.0, [module.yaml, package.yaml]); SET_CHILD_ENUMERATION(packages/beta, [2.0.0]); SET_CHILD_ENUMERATION(packages/beta/2.0.0, [module.yaml, package.yaml])
	Ordered identities lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b then lattice:package:sha256:9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4
	35. Identity-distinction fixtures
Fixture ID
	Exact change
	Expected
	ID-PACKAGE
	RENAME(packages/alpha, beta); SET_DESCRIPTOR(packages/beta/1.0.0/package.yaml, BD(beta, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	Identity lattice:package:sha256:b6705fd7774024451a41bccd82dae7f7ead5c998341a10afbff2c77a6dac20e1
	ID-VERSION
	RENAME(packages/alpha/1.0.0, 1.0.1); SET_DESCRIPTOR(packages/alpha/1.0.1/package.yaml, BD(alpha, 1.0.1, [lattice-core-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	Identity lattice:package:sha256:9f305028f064ace9b8d839ad48f8dcd62281e3bc5ba081177d85e143232a098e
	ID-LATTICE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "lattice: \"0.3\"\n", "lattice: \"0.4\"\n"))
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/lattice; no identity
	ID-PROFILES-MEMBERSHIP
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1, lattice-builder-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	Identity lattice:package:sha256:934a9bc2921a91d1d1145956389a4b3a0dcc887756e33f909d00cf3e00287576
	ID-MODULE-FILE
	Scan A: ADD(packages/alpha/1.0.0/entry.yaml, regular(M_ALPHA_100)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(entry.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)])). Scan B independently repeats both operations but supplies entry.yaml as the BD module_file argument.
	Distinct identities lattice:package:sha256:6e7bc9698250aaa255189f5a8d8e74b91b52547deb7e66a9e602393bd5d8c476 and lattice:package:sha256:9031644cb03fe56a568c6635f88cda9130ca89e97f91723a710215e27da8f37b
	ID-DECLARED-PATH
	Scan A: ADD(packages/alpha/1.0.0/data.txt, regular(DATA)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (data.txt, c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73)])). Scan B: ADD(packages/alpha/1.0.0/docs, directory({})); ADD(packages/alpha/1.0.0/docs/data.txt, regular(DATA)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (docs/data.txt, c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73)])).
	Distinct identities lattice:package:sha256:51b4317223471152bf1e81041a58edb10507a6be370317b49b3cf5c7f93aa80a and lattice:package:sha256:676636785015758fc969e33b6f153f7787e507742547509d84b9f6c9e83bc495
	In Scan B, docs begins with an exact empty child map; the subsequent ADD leaves its complete child map containing exactly data.txt and no unspecified metadata-audit competitor.
	ID-DECLARED-HASH-REJECTED
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_DIGEST_F64)
	PACKAGE_SCAN_FILE_HASH_MISMATCH at packages/alpha/1.0.0/module.yaml; no package identity
	ID-DECLARED-FILE-SET
	ADD(packages/alpha/1.0.0/empty.txt, regular(EMPTY)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (empty.txt, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855)]))
	Identity lattice:package:sha256:5acd1d6ab712dd052ad942bff1f7f840e7215d44fc479fba29492d0b75097778
	ID-RAW-BYTES-AND-DIGEST
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_ALPHA_CHANGED)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 9b9f2b1e36beaad57c6436ad62b9bef6e01db6203d5567ac3afd0b1a0785acff)]))
	Identity lattice:package:sha256:c100d984afe465b06fd525f42a519651e094ff63a15a29f315a4ca3ff1047ef6
36. Descriptor parser-crosswalk fixtures
Every operation below replaces packages/alpha/1.0.0/package.yaml in the default snapshot. Every expected parser target is the complete descriptor path followed by the literal root delimiter.
Fixture ID
	Exact source condition
	Expected diagnostic
	PARSE-INVALID-UTF8
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, hex(ff))
	PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID at packages/alpha/1.0.0/package.yaml#
	PARSE-BOM
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, hex(efbbbf) + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID at packages/alpha/1.0.0/package.yaml#
	PARSE-RAW-CONTROL
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, hex(00) + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID at packages/alpha/1.0.0/package.yaml#
	PARSE-DIRECTIVE-YAML
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, exact UTF-8 "%YAML 1.1\n---\n" + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-DIRECTIVE-TAG
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, exact UTF-8 "%TAG !e! tag:example.com,2026:\n---\n" + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-SYNTAX
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, hex(756e6974733a205b0a))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-MULTIPLE-DOCUMENTS
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_MIN + exact UTF-8 "---\n" + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-ANCHOR
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: &p alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-ALIAS
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: *p\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-MERGE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, exact UTF-8 "<<: {package: alpha}\n" + D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-TAG
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: !custom alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-TAG-MISMATCH
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: !!int alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-FOLDED
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: >\n  alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-BINARY
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: !!binary YQ==\n"))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	PARSE-FLOAT
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: 1.5\n"))
	PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID at packages/alpha/1.0.0/package.yaml#
	PARSE-I64-RANGE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: 9223372036854775808\n"))
	PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID at packages/alpha/1.0.0/package.yaml#
	PARSE-DATE-LIKE-STRING
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: 2026-07-23\n"))
	Parsing succeeds with package equal to string 2026-07-23; PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/package
	PARSE-NONSTRING-KEY
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "1: alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_NON_STRING_KEY at packages/alpha/1.0.0/package.yaml#
	PARSE-DUPLICATE-KEY
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, INSERT_UTF8_AFTER(D_MIN, "package: alpha\n", "package: alpha\n"))
	PACKAGE_SCAN_DESCRIPTOR_DUPLICATE_KEY at packages/alpha/1.0.0/package.yaml#
	PARSE-NFC-COLLISION
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, exact hex c3a93a20747275650a65cc813a2066616c73650a followed by D_MIN)
	PACKAGE_SCAN_DESCRIPTOR_NFC_COLLISION at packages/alpha/1.0.0/package.yaml#
	PARSE-MULTI-DEFECT
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, exact UTF-8 "%YAML 1.1\n---\npackage: 1.5\n")
	The accepted PC2 operation selects SOURCE_FORBIDDEN_YAML before scalar projection; PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/alpha/1.0.0/package.yaml#
	37. Descriptor-schema failure fixtures
Fixture ID
	Exact mutation
	Expected
	DESC-NONOBJECT
	Exact descriptor hex 5b5d0a
	PACKAGE_SCAN_DESCRIPTOR_ROOT_INVALID at packages/alpha/1.0.0/package.yaml#
	DESC-UNKNOWN-FIELD
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", "extra: true\n")
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/extra
	DESC-MISSING-FIELD
	DELETE_UTF8_EXACT(D_MIN, "lattice: \"0.3\"\n")
	PACKAGE_SCAN_DESCRIPTOR_MEMBER_MISSING at packages/alpha/1.0.0/package.yaml#/lattice
	DESC-WRONG-TYPE
	REPLACE_UTF8(D_MIN, "package: alpha\n", "package: [alpha]\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/package
	DESC-INVALID-PACKAGE
	REPLACE_UTF8(D_MIN, "package: alpha\n", "package: Alpha\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/package
	DESC-INVALID-VERSION
	REPLACE_UTF8(D_MIN, "version: \"1.0.0\"\n", "version: \"01.0.0\"\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/version
	DESC-INVALID-LATTICE
	REPLACE_UTF8(D_MIN, "lattice: \"0.3\"\n", "lattice: \"0.4\"\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/lattice
	DESC-INVALID-PROFILE
	REPLACE_UTF8(D_MIN, "  - lattice-core-0.1\n", "  - lattice-extended-0.2\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/profiles/0
	DESC-PROFILE-WRONG-TYPE
	REPLACE_UTF8(D_MIN, "  - lattice-core-0.1\n", "  - true\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/profiles/0
	DESC-DUPLICATE-PROFILE
	INSERT_UTF8_AFTER(D_MIN, "  - lattice-core-0.1\n", "  - lattice-core-0.1\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/profiles/1
	DESC-EMPTY-PROFILES
	REPLACE_UTF8(D_MIN, "profiles:\n  - lattice-core-0.1\n", "profiles: []\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/profiles
	DESC-FILES-WRONG-TYPE
	REPLACE_UTF8(D_MIN, "files:\n  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "files: {}\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/files
	DESC-FILE-NONOBJECT
	REPLACE_UTF8(D_MIN, "  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "  - module.yaml\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/files/0
	DESC-FILE-UNKNOWN
	INSERT_UTF8_AFTER(D_MIN, "    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "    size: 105\n")
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/files/0/size
	DESC-FILE-MISSING-SHA
	DELETE_UTF8_EXACT(D_MIN, "    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n")
	PACKAGE_SCAN_DESCRIPTOR_MEMBER_MISSING at packages/alpha/1.0.0/package.yaml#/files/0/sha256
	DESC-DUPLICATE-FILE
	INSERT_UTF8_AFTER(D_MIN, "    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n")
	PACKAGE_SCAN_DECLARED_PATH_DUPLICATE at packages/alpha/1.0.0/package.yaml#/files/1/path
	DESC-EMPTY-FILES
	REPLACE_UTF8(D_MIN, "files:\n  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "files: []\n")
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/files
	DESC-MODULE-UNLISTED
	REPLACE_UTF8(D_MIN, "module_file: module.yaml\n", "module_file: entry.yaml\n")
	PACKAGE_SCAN_MODULE_FILE_UNLISTED at packages/alpha/1.0.0/package.yaml#/module_file
	DESC-PACKAGE-YAML-LISTED
	INSERT_UTF8_AFTER(D_MIN, "    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n", "  - path: package.yaml\n    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n")
	PACKAGE_SCAN_DESCRIPTOR_SELF_LISTED at packages/alpha/1.0.0/package.yaml#/files/1/path
37.1 Descriptor-pointer rendering fixtures
Each exact inserted root key is accepted by PC2 as one NFC string and is then rejected by the closed descriptor schema as the only unknown key. The fixture therefore reaches a legitimate unknown-key target.
Fixture ID
	Exact descriptor mutation and decoded unknown key
	Expected diagnostic
	PTR-SOLIDUS
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact UTF-8 "\"a/b\": true\n"); decoded key a/b
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/a~1b
	PTR-TILDE
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact UTF-8 "\"a~b\": true\n"); decoded key a~b
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/a~0b
	PTR-PERCENT
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact UTF-8 "\"a%b\": true\n"); decoded key a%b
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/a%25b
	PTR-NUMBER-SIGN
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact UTF-8 "\"a#b\": true\n"); decoded key a#b
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/a%23b
	PTR-C0
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact source-fragment hex 22615c78303162223a20747275650a); accepted YAML escape decodes key bytes 610162
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/a%01b
	PTR-NONASCII
	INSERT_UTF8_AFTER(D_MIN, "lattice: \"0.3\"\n", exact source-fragment hex 22636166c3a9223a20747275650a); decoded NFC key café
	PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY at packages/alpha/1.0.0/package.yaml#/caf%C3%A9
In every expected path, the only literal # is the separator after package.yaml. The # inside PTR-NUMBER-SIGN's token is %23.
	38. Layout and precedence fixtures
Fixture ID
	Exact snapshot mutation
	Expected
	LAYOUT-PACKAGES-FILE
	REPLACE_NODE(packages, regular(EMPTY))
	PACKAGE_SCAN_PACKAGES_ROOT_INVALID at packages
	LAYOUT-PACKAGES-SYMLINK
	REPLACE_NODE(packages, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages
	LAYOUT-PACKAGES-UNREADABLE
	REPLACE_NODE(packages, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages
	LAYOUT-PACKAGE-DIRECTORY-UNREADABLE
	REPLACE_NODE(packages/alpha, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages/alpha
	LAYOUT-VERSION-DIRECTORY-UNREADABLE
	REPLACE_NODE(packages/alpha/1.0.0, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages/alpha/1.0.0
	LAYOUT-PACKAGE-NAME-MISMATCH
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: beta\n"))
	PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH at packages/alpha/1.0.0/package.yaml#/package
	LAYOUT-VERSION-MISMATCH
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "version: \"1.0.0\"\n", "version: \"1.0.1\"\n"))
	PACKAGE_SCAN_VERSION_DIRECTORY_MISMATCH at packages/alpha/1.0.0/package.yaml#/version
	LAYOUT-STRAY-PACKAGE-FILE
	ADD(packages/notes.txt, regular(EMPTY))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/notes.txt
	LAYOUT-STRAY-VERSION-FILE
	ADD(packages/alpha/readme.txt, regular(EMPTY))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/alpha/readme.txt
	LAYOUT-MISSING-DESCRIPTOR
	REMOVE(packages/alpha/1.0.0/package.yaml)
	PACKAGE_SCAN_DESCRIPTOR_MISSING at packages/alpha/1.0.0/package.yaml
	LAYOUT-WRONG-DEPTH-DESCRIPTOR
	ADD(packages/alpha/package.yaml, regular(D_MIN))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/alpha/package.yaml
	LAYOUT-PACKAGE-SYMLINK
	REPLACE_NODE(packages/alpha, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha
	LAYOUT-VERSION-SYMLINK
	REPLACE_NODE(packages/alpha/1.0.0, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0
	PREC-INVALID-NAME-SYMLINK
	ADD(packages/Bad, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/Bad
	PREC-INVALID-NAME-REGULAR
	ADD(packages/Bad, regular(EMPTY))
	PACKAGE_SCAN_LAYOUT_ENTRY_INVALID at packages/Bad
	PREC-DESCRIPTOR-SYMLINK
	REPLACE_NODE(packages/alpha/1.0.0/package.yaml, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0/package.yaml
	PREC-DESCRIPTOR-DIRECTORY
	REPLACE_NODE(packages/alpha/1.0.0/package.yaml, directory({}))
	PACKAGE_SCAN_DESCRIPTOR_NOT_REGULAR at packages/alpha/1.0.0/package.yaml
	PREC-DESCRIPTOR-UNREADABLE
	REPLACE_NODE(packages/alpha/1.0.0/package.yaml, regular_unreadable)
	PACKAGE_SCAN_DESCRIPTOR_UNREADABLE at packages/alpha/1.0.0/package.yaml
	PREC-NESTED-TRAVERSAL
	REMOVE(packages/alpha/1.0.0/package.yaml); ADD(packages/bad!, directory({}))
	PACKAGE_SCAN_DESCRIPTOR_MISSING at packages/alpha/1.0.0/package.yaml because nested traversal completes alpha before reaching later package entry bad!
	PREC-STRUCTURAL-VERSION-UTF8
	USE_BASE(T-VERSION-ORDER); REMOVE(packages/alpha/10.0.0/package.yaml); REMOVE(packages/alpha/2.0.0/package.yaml)
	PACKAGE_SCAN_DESCRIPTOR_MISSING at packages/alpha/10.0.0/package.yaml, proving structural NFC UTF-8 order examines 10.0.0 before 2.0.0
	PREC-GLOBAL-DESCRIPTOR-PASS
	USE_BASE(T-MULTIPLE-PACKAGES); REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(DATA)); REPLACE_NODE(packages/beta/2.0.0/package.yaml, regular(M_INVALID_YAML))
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/beta/2.0.0/package.yaml# wins before the earlier Alpha file-hash mismatch
	PREC-GLOBAL-PARSER-BEFORE-SHALLOW
	USE_BASE(T-MULTIPLE-PACKAGES); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "package: alpha\n", "package: [alpha]\n")); SET_DESCRIPTOR(packages/beta/2.0.0/package.yaml, M_INVALID_YAML)
	PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN at packages/beta/2.0.0/package.yaml#; later-candidate parser failure defeats earlier-candidate shallow-schema failure
	PREC-GLOBAL-SHALLOW-BEFORE-COLLECTION
	USE_BASE(T-MULTIPLE-PACKAGES); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "  - lattice-core-0.1\n", "  - lattice-extended-0.2\n")); SET_DESCRIPTOR(packages/beta/2.0.0/package.yaml, REPLACE_UTF8(D_BETA_200, "package: beta\n", "package: [beta]\n"))
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/beta/2.0.0/package.yaml#/package; later-candidate shallow-schema failure defeats earlier-candidate collection failure
	PREC-GLOBAL-COLLECTION-BEFORE-METADATA
	USE_BASE(T-MULTIPLE-PACKAGES); ADD(packages/alpha/1.0.0/ignored-link, link("target")); SET_DESCRIPTOR(packages/beta/2.0.0/package.yaml, REPLACE_UTF8(D_BETA_200, "  - lattice-core-0.1\n", "  - lattice-extended-0.2\n"))
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/beta/2.0.0/package.yaml#/profiles/0; later-candidate collection failure defeats earlier-candidate metadata failure
	PREC-GLOBAL-METADATA-BEFORE-DECLARED
	USE_BASE(T-MULTIPLE-PACKAGES); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_DIGEST_F64); ADD(packages/beta/2.0.0/ignored-link, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/beta/2.0.0/ignored-link; later-candidate metadata failure defeats earlier-candidate declared-file hash mismatch
	PREC-SHALLOW-BEFORE-AGREEMENT
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(REPLACE_UTF8(D_MIN, "package: alpha\n", "package: beta\n"), "profiles:\n  - lattice-core-0.1\n", "profiles: {}\n"))
	PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID at packages/alpha/1.0.0/package.yaml#/profiles wins before the otherwise applicable PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH at packages/alpha/1.0.0/package.yaml#/package
	PREC-AGREEMENT-BEFORE-PROFILE-CONTENT
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(REPLACE_UTF8(D_MIN, "package: alpha\n", "package: beta\n"), "  - lattice-core-0.1\n", "  - lattice-extended-0.2\n"))
	PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH at packages/alpha/1.0.0/package.yaml#/package wins before the deep profile-value failure
39. Path failure fixtures
Each single-path fixture replaces the default descriptor with BDP(exact_scalar_source). The exact decoded value follows the source token. Every single-path result is PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file.
Fixture ID
	Exact scalar-source token and decoded NFC value
	Expected diagnostic
	PATH-EMPTY
	BDP("\"\""); decoded hex is empty
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-LEADING-SLASH
	BDP("\"/module.yaml\""); decoded hex 2f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-TRAILING-SLASH
	BDP("\"module.yaml/\""); decoded hex 6d6f64756c652e79616d6c2f
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-REPEATED-SLASH
	BDP("\"sub//module.yaml\""); decoded hex 7375622f2f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-DOT
	BDP("\"./module.yaml\""); decoded hex 2e2f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-PARENT
	BDP("\"../module.yaml\""); decoded hex 2e2e2f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-BACKSLASH
	BDP(source-token hex 227375625c5c6d6f64756c652e79616d6c22); decoded hex 7375625c6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-DRIVE
	BDP("\"c:/module.yaml\""); decoded hex 633a2f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-UNC
	BDP("\"//server/share/module.yaml\""); decoded hex 2f2f7365727665722f73686172652f6d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-COLON
	BDP("\"a:b\""); decoded hex 613a62
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-NUL
	BDP(source-token hex 225c3022); accepted YAML escape decodes hex 00
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-CONTROL
	BDP(source-token hex 225c78303122); accepted YAML escape decodes hex 01
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-UNICODE
	BDP(source-token hex 22636166c3a92e74787422); decoded NFC hex 636166c3a92e747874
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-NON-NFC
	BDP(source-token hex 2263616665cc812e74787422); accepted parsing normalizes decoded hex 63616665cc812e747874 to NFC hex 636166c3a92e747874
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-UPPERCASE
	BDP("\"Module.yaml\""); decoded hex 4d6f64756c652e79616d6c
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-RESERVED
	BDP("\"con.txt\""); decoded hex 636f6e2e747874
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-TRAILING-DOT
	BDP("\"module.\""); decoded hex 6d6f64756c652e
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-TRAILING-SPACE
	BDP(source-token hex 226d6f64756c652e79616d6c2022); decoded hex 6d6f64756c652e79616d6c20
	PACKAGE_SCAN_DECLARED_PATH_INVALID at packages/alpha/1.0.0/package.yaml#/module_file
	PATH-DUPLICATE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BDF(module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	PACKAGE_SCAN_DECLARED_PATH_DUPLICATE at packages/alpha/1.0.0/package.yaml#/files/1/path
	PATH-NFC-DUPLICATE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BDF(module.yaml, [(module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55), (source-token hex 22c3a922, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (source-token hex 2265cc8122, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855)])); the last two source strings normalize to the same parsed value
	PACKAGE_SCAN_DECLARED_PATH_DUPLICATE at packages/alpha/1.0.0/package.yaml#/files/2/path before path grammar
	PATH-PREFIX-COLLISION
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BDF(module.yaml, [(a, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (a/b, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (b, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (b/c, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	PACKAGE_SCAN_DECLARED_PATH_PREFIX_COLLISION at packages/alpha/1.0.0/package.yaml#/files/1/path
	PATH-PREFIX-SELECTION
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BDF(module.yaml, [(b, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (b/c, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (a, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (a/z, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (a/y, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855), (module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	PACKAGE_SCAN_DECLARED_PATH_PREFIX_COLLISION at packages/alpha/1.0.0/package.yaml#/files/4/path; selected pair is a and a/y
	40. Declared-file failure fixtures
Every fixture in this section starts from T-MINIMAL unless it explicitly names another base.
When a declared path changes, package.yaml is replaced by the exact BD output using the stated path, the unchanged Core profile and package/version fields, and the stated digest.
Fixture ID
	Exact snapshot mutation
	Expected diagnostic
	FILE-MISSING
	REMOVE(packages/alpha/1.0.0/module.yaml)
	PACKAGE_SCAN_DECLARED_FILE_MISSING at packages/alpha/1.0.0/module.yaml
	FILE-DIRECTORY
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, directory({}))
	PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR at packages/alpha/1.0.0/module.yaml
	The exact empty child map completes metadata audit without a competing descendant, so declared-file verification necessarily selects this diagnostic.
	FILE-DIRECTORY-UNREADABLE
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages/alpha/1.0.0/module.yaml during metadata audit
	FILE-FINAL-SYMLINK
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0/module.yaml
	FILE-INTERMEDIATE-MISSING
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], sub/module.yaml, [(sub/module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)]))
	PACKAGE_SCAN_DECLARED_FILE_MISSING at packages/alpha/1.0.0/sub
	FILE-INTERMEDIATE-SYMLINK
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], sub/module.yaml, [(sub/module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)])); ADD(packages/alpha/1.0.0/sub, link("target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0/sub
	FILE-INTERMEDIATE-REGULAR
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], sub/module.yaml, [(sub/module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)])); ADD(packages/alpha/1.0.0/sub, regular(EMPTY))
	PACKAGE_SCAN_DECLARED_PATH_COMPONENT_NOT_DIRECTORY at packages/alpha/1.0.0/sub
	FILE-INTERMEDIATE-SPECIAL
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], sub/module.yaml, [(sub/module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)])); ADD(packages/alpha/1.0.0/sub, special(FIFO))
	PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT at packages/alpha/1.0.0/sub
	FILE-INTERMEDIATE-UNREADABLE-DIRECTORY
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], sub/module.yaml, [(sub/module.yaml, 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55)])); ADD(packages/alpha/1.0.0/sub, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages/alpha/1.0.0/sub during metadata audit
	FILE-SPECIAL
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, special(FIFO))
	PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT at packages/alpha/1.0.0/module.yaml
	FILE-UNREADABLE
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular_unreadable)
	PACKAGE_SCAN_DECLARED_FILE_UNREADABLE at packages/alpha/1.0.0/module.yaml
	FILE-DIGEST-SHORT
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_DIGEST_F63)
	PACKAGE_SCAN_DIGEST_SYNTAX_INVALID at packages/alpha/1.0.0/package.yaml#/files/0/sha256
	FILE-DIGEST-UPPERCASE
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55", "900DD3893A719EC7EA1CB5ACFF8EC799223D6B8D3F3C6DEA3EB09F2D06B67B55"))
	PACKAGE_SCAN_DIGEST_SYNTAX_INVALID at packages/alpha/1.0.0/package.yaml#/files/0/sha256
	FILE-DIGEST-PREFIXED
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, REPLACE_UTF8(D_MIN, "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55", "sha256:900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"))
	PACKAGE_SCAN_DIGEST_SYNTAX_INVALID at packages/alpha/1.0.0/package.yaml#/files/0/sha256
	FILE-HASH-MISMATCH
	SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_DIGEST_F64)
	PACKAGE_SCAN_FILE_HASH_MISMATCH at packages/alpha/1.0.0/module.yaml
	FILE-LINE-ENDINGS
	REPLACE_HEX(packages/alpha/1.0.0/module.yaml, exact bytes obtained from M_ALPHA_100 by replacing every 0A byte by 0D0A); descriptor remains exact D_MIN
	PACKAGE_SCAN_FILE_HASH_MISMATCH at packages/alpha/1.0.0/module.yaml
	FILE-BOM
	REPLACE_HEX(packages/alpha/1.0.0/module.yaml, efbbbf followed by the complete M_ALPHA_100 hex); descriptor remains exact D_MIN
	PACKAGE_SCAN_FILE_HASH_MISMATCH at packages/alpha/1.0.0/module.yaml
	FILE-UNLISTED-SYMLINK
	ADD(packages/alpha/1.0.0/ignored-link, link("ignored-target"))
	PACKAGE_SCAN_SYMLINK_FORBIDDEN at packages/alpha/1.0.0/ignored-link
	FILE-UNLISTED-UNREADABLE-DIR
	ADD(packages/alpha/1.0.0/ignored, directory_unreadable)
	PACKAGE_SCAN_DISCOVERY_UNREADABLE at packages/alpha/1.0.0/ignored
	No disappearing-file, changing-file, ABA, or live-mount diagnostic fixture exists. Those conditions belong to snapshot acquisition and produce no semantic PC6 result.
41. Imported-module boundary fixtures
Each fixture begins from the exact fixture default. A row that replaces module bytes also replaces package.yaml with the stated complete deterministic descriptor so the declared digest matches.
Fixture ID
	Exact operations
	Expected PC6 result
	PHASE-MALFORMED-MODULE-YAML
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_INVALID_YAML)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 7b8412cfb68dc835e7ccbdba401b79052a99f8f9e6dd3c955e47358506232945)]))
	PC6 succeeds with identity lattice:package:sha256:67615ce7c1071eb92ade638f888c1bd0fa866716849e72813635eb7c1b9c3d4b
	PHASE-UNRESOLVED-IMPORT
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_UNRESOLVED_IMPORT)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 43332c30f07a88388a60f93b9f76b21ed16f8d40ed130af788474d9017184916)]))
	PC6 succeeds with identity lattice:package:sha256:b7a30c594bc90b58cc0127d350ae942d657415c1a234fdfc418bd0954f13b16e
	PHASE-UNSATISFIED-VERSION
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_UNSATISFIED_VERSION)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 25628abdc47ca14733a318bf3007e15689efa276e8a60fc55a459080fde165e2)]))
	PC6 succeeds with identity lattice:package:sha256:037b2e0b64dccd3f890923d393b73c0dc56807d0149468791412bd98d20accfb
	PHASE-LATER-INVALID-BODY
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_LATER_INVALID_BODY)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 87d252d0ef0f72f94eecbd7bb30ab17a8d24940e4bd1ca227f77ac1871c502e4)]))
	PC6 succeeds with identity lattice:package:sha256:ede26ac500571dae4a6d00717d04ced75c2fdd070de95e620dda8731256e5f9f
	PHASE-NO-MODULE-PARSE
	REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_OPAQUE)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, D_OPAQUE)
	PC6 retains exact M_OPAQUE bytes without interpreting them and succeeds with identity lattice:package:sha256:981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a
	PHASE-NO-LOCKFILE
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; no Lockfile is produced
	PHASE-NO-EXPANSION
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; no namespace or flattened declaration set is produced
	PHASE-NO-DECLARATION-ID
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; only package identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b is created
	PHASE-NO-MANIFEST
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; no Manifest is produced
	PHASE-NO-BINDING
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; no Binding is produced
	PHASE-NO-AUTHORITY
	No mutation; exact input is DS-A and T-MINIMAL
	Minimal package succeeds; no execution or access authority is produced
	This fixture document does not assign a later phase result, later diagnostic, or later precise owner to malformed or semantically incompatible module content.
42. Snapshot and source-binding fixtures
Fixture ID
	Exact operation
	Expected
	BIND-EXACT-SOURCE
	Scan exact T-MINIMAL once with DS-A and independently once with DS-B
	Package records equal, complete ScannedSource values differ
	BIND-SOURCE-SWAP
	After exact DS-A and T-MINIMAL scan, attempt to replace the bound source by exact DS-B
	No public operation exists
	BIND-ID-CONTENT-SWAP
	Attempt to pair identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b with exact M_ALPHA_CHANGED bytes
	No public operation exists
	BIND-REPEAT-SCAN
	Scan exact DS-A and exact T-MINIMAL twice
	Semantically identical results
	BIND-LIVE-MUTATION-AFTER-SNAPSHOT
	Acquire exact T-MINIMAL; after acquisition replace only the live host module.yaml by DATA without changing the immutable snapshot
	Existing result retains exact M_ALPHA_100 and the minimal identity
	BIND-NEW-SNAPSHOT-UNUPDATED-DIGEST
	Fresh T-MINIMAL copy; REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_ALPHA_CHANGED)); descriptor remains exact D_MIN
	PACKAGE_SCAN_FILE_HASH_MISMATCH at packages/alpha/1.0.0/module.yaml
	BIND-NEW-SNAPSHOT-UPDATED-DIGEST
	Fresh T-MINIMAL copy; REPLACE_NODE(packages/alpha/1.0.0/module.yaml, regular(M_ALPHA_CHANGED)); SET_DESCRIPTOR(packages/alpha/1.0.0/package.yaml, BD(alpha, 1.0.0, [lattice-core-0.1], module.yaml, [(module.yaml, 9b9f2b1e36beaad57c6436ad62b9bef6e01db6203d5567ac3afd0b1a0785acff)]))
	Identity lattice:package:sha256:c100d984afe465b06fd525f42a519651e094ff63a15a29f315a4ca3ff1047ef6
	BIND-LATER-CONSUMPTION
	Scan exact DS-A and T-MINIMAL, then replace only the live host module.yaml by DATA before a later phase requests module.yaml
	Later consumer receives exact retained M_ALPHA_100 bytes only
	BIND-CANONICAL-BYTES-DERIVED
	Scan exact DS-A and T-MINIMAL, then reproduce canonical bytes from its admitted descriptor value
	Exact 222-byte minimal canonical vector from section 29.1, regardless of whether it was cached
	BIND-NO-CANONICAL-CACHE
	Scan exact DS-A and T-MINIMAL and discard only derived canonical-byte cache after creating the minimal identity
	Semantic result still binds exact DS-A, the admitted descriptor, identity lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b, and M_ALPHA_100
	BIND-NO-MUTABLE-BYTES
	After exact DS-A and T-MINIMAL scan, attempt to mutate returned module.yaml bytes
	Operation is unavailable
	43. Golden verification ledger
Ellipses in this ledger are display abbreviations only. The complete authoritative values in sections 25 through 30 control.
Constant or record
	Byte length
	Recalculated SHA-256
	Dependent package hash
	Review repair result
	DS-A
	224
	196ff00d...e4b5
	Not applicable
	Unchanged and independently matched
	DS-B
	226
	4e0ca3af...f3a4
	Not applicable
	Authoritative hex added and independently matched
	D_MIN
	209
	3c05bc67...eec8
	bc7d7188...053b
	Unchanged and independently matched
	DATA_CHANGED
	19
	792ef13d...e9b2
	b84865cb...101b
	Fourth-repair exact ADD and BD identity inputs independently matched
	D_DIGEST_F63
	208
	7fb80cc9...fcc4
	None; descriptor fails digest syntax
	Third-repair exact nonnumeric short-digest fixture
	D_DIGEST_F64
	209
	33729846...e6d7
	None; retained file fails hash comparison
	Third-repair exact syntactically valid mismatch fixture
	Minimal canonical bytes
	222
	bc7d7188...053b
	Same
	Unchanged
	D_MULTI
	444
	44792eae...c961
	ba06b608...92b8
	Unchanged
	D_ALPHA_110
	209
	3bf1d883...a1dc
	10cb5b7f...f399
	Authoritative descriptor hex added and independently matched
	D_BETA_200
	208
	4486f30a...7f1f
	96218039...9ef4
	Authoritative descriptor hex added and independently matched
	D_HARDLINK
	395
	88dc9fa0...d640
	40390611...1dc7
	Authoritative descriptor hex added and independently matched
	Multi-file canonical bytes
	458
	ba06b608...92b8
	Same
	Unchanged and independently matched
	V_NO_BULLETS
	50
	94a10cbf...5060
	ba06b608...92b8
	Rendered indentation repaired; hash unchanged
	M_UNRESOLVED_IMPORT
	177
	43332c30...4916
	b7a30c59...b16e
	Rendered indentation repaired; hash and identity unchanged
	M_UNSATISFIED_VERSION
	170
	25628abd...65e2
	037b2e0b...ccfb
	Rendered indentation repaired; hash and identity unchanged
	M_LATER_INVALID_BODY
	145
	87d252d0...02e4
	ede26ac5...5f9f
	Rendered indentation repaired; hash and identity unchanged
	M_OPAQUE
	11
	7d92f51e...e10d
	981b422e...970a
	Third-repair exact no-module-parse vector
	D_OPAQUE
	209
	e017ddd1...5d81
	981b422e...970a
	Third-repair exact matching descriptor
	Opaque-module canonical bytes
	222
	981b422e...970a
	Same
	Third-repair exact canonical package vector
	Hard-link canonical record
	408
	40390611...1dc7
	Same
	New repaired fixture
	Alpha 2.0.0 canonical record
	222
	0a31f832...9752
	Same
	Numeric-order fixture independently matched
	Alpha 10.0.0 canonical record
	223
	842fa7fd...f407
	Same
	Numeric-order fixture independently matched
	Empty file
	0
	e3b0c442...b855
	Multi-file and add-empty identities
	Unchanged
	No pre-existing candidate golden digest changed as a consequence of the third documentation repair.
The third repair adds exact nonnumeric digest-failure descriptor sources and the authoritative opaque-module vector without changing earlier canonical package results.
The fourth repair makes the previously implicit DATA_CHANGED identity construction and every readable-directory fixture child map exact. It changes fixture instantiation only and makes no normative Package Scan algorithm change.
The exact DATA_CHANGED construction independently reproduces the existing b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b package hash. No golden digest, package identity, fixture membership, diagnostic expectation, or vector population changes.
Hex is the source of truth for every named byte constant.
44. Conformance requirements
A conforming implementation MUST demonstrate that absent and empty package roots produce equal empty semantic package sets, unrelated project-root entries are outside snapshot acquisition, structural diagnostics use exact nested NFC UTF-8 traversal, successful candidates use numeric version order, every global validation pass completes for all candidates before the next pass, invalid snapshot names are diagnosed through canonical percent-encoded paths, unrepresentable included native names fail before semantic PC6, accepted YAML presentation variants converge, profile and file source order do not affect identity, every identity-participating descriptor change alters or invalidates the expected result, every rejected path category selects the required diagnostic, link-like objects are never followed, unlisted bytes are never read, hard-linked distinct paths remain separately declared and verified, raw file bytes are hashed without transformation, later phases consume retained immutable bytes, canonical bytes can be reproduced as derived material, package identities cannot be paired with different bytes, scanned results cannot be paired with different DigestedSource values, and PC6 creates no Lockfile, Manifest, Binding, or authority.
A conforming implementation MUST also replay the six exact accepted-PC2 parser mappings without finer reclassification, preserve date-looking plain scalars as strings until descriptor schema validation, render every primary diagnostic through the exhaustive section 19.2 target rule, assign all unavailable directory child maps to metadata audit, limit PACKAGE_SCAN_DECLARED_FILE_UNREADABLE to a final regular file's unavailable bytes, distinguish every adjacent global stage with the section 38 cross-candidate fixtures, and reproduce every section 37.1 pointer vector with one literal # delimiter.
45. Residual review risks
Risk
	Classification after repair
	Strict lowercase ASCII paths reject existing mixed-case or Unicode package content
	Deliberate accepted Core trade-off
	Canonical package versions differ from broader PC3 source-version admission
	Accepted compatibility concern
	Both normative profiles differ from the recovered singleton-Core schema
	Accepted compatibility concern
	Required lattice differs from the recovered schema
	Accepted compatibility concern
	Complete immutable package-scoped snapshot acquisition may require platform-specific host machinery
	Review concern, but no longer an impossible PC6 live-filesystem proof
	Metadata-only traversal of unlisted directories observes names and object classes
	Deliberate security trade-off required for no-link enforcement
	Large immutable snapshots may exhaust resources
	Explicit deferred operational risk
	Exact imported-module intake remains unresolved
	Deliberately deferred to Resolve reconciliation without affecting PC6 identity bytes
	The recovered PackageDescriptor requires migration rather than silent reuse
	Compatibility concern
	Host snapshot acquisition failure is outside PackageScanOutcome
	Review concern requiring confirmation of compiler-level failure reporting, not a package-identity ambiguity
46. Review disposition
The third repaired candidate preserved the original and first-repair history and addressed all findings supplied by the independent review of the second repaired candidate.
This fourth repaired candidate preserves all earlier history and addresses only the two P1 fixture-construction findings supplied by the completed independent review of the third repaired candidate. That review reported P0=0, P1=2, P2=0, and P3=0.
The accepted PC2 parser operation is now reused at its six observable stable outcomes. Date-looking plain scalars remain strings and descriptor package-name grammar owns their later rejection.
Directory enumeration failure belongs only to metadata audit, final regular-byte unreadability belongs only to declared-file verification, and every diagnostic code has one exact target-path rule.
The formerly numeric all-zero digest fixtures are replaced by authoritative nonnumeric descriptor sources that reach digest syntax and raw-byte hash comparison as intended.
Every semantic fixture has DS-A plus a fresh T-MINIMAL as an explicit default, every exception names its base, and deterministic constructors and operations supply complete descriptor and snapshot bytes.
Cross-candidate fixtures now permanently distinguish parser, shallow-schema, collection, metadata, and declared-file global stages, while dual invalid versions distinguish raw structural ordering from successful numeric ordering.
Reachable unknown-key fixtures cover /, ~, %, #, an escaped C0 scalar, and non-ASCII Unicode through the complete RFC 6901 and percent-encoding pipeline.
Portable names now have one NFC UTF-8 representation, one ordering, and one diagnostic rendering.
Live-filesystem mutation and ABA proof obligations have been replaced by a complete immutable portable snapshot boundary.
That snapshot is now explicitly limited to exact lookup of packages and its included subtree, so unrelated project-root entries cannot affect PC6.
Hard-link content sharing is separated from namespace aliasing.
Diagnostic traversal, the accepted-parser crosswalk, object precedence, prefix-collision selection, and canonical-core failure ownership are closed within this candidate.
Structural version-name diagnostics use NFC UTF-8 order, while successful candidates and outputs use numeric canonical version order.
Global staged validation and the reference pseudocode now agree.
Shallow schema checks, directory agreement, profile validation, module_file admission, and file validation have non-overlapping precedence.
Imported-module parsing and compatibility have been removed from PC6 and deferred without assigning incomplete Resolve semantics.
Every named byte constant is authoritative by hexadecimal, newly affected descriptor constants are complete, whitespace-sensitive paths are executable through exact constructors, and expected identities are complete outside the expressly non-authoritative verification ledger.
Canonical descriptor bytes remain exact identity inputs and golden conformance outputs but are no longer mandatory stored semantic state.
The fourth repair changes fixture instantiation only and makes no normative Package Scan algorithm change.
Every executable readable-directory node now has an exact child map. directory({}) begins empty, descendant additions are explicit, base snapshots contain only listed children, and REPLACE_NODE with directory({}) replaces the complete prior child map.
The existing DATA_CHANGED identity record now gives its exact DS-A and T-MINIMAL defaults, ADD operation, complete BD operation, two-file verified set, package fields, canonical path order, and independently reproduced package identity.
The fixture-manifest version is pc6-package-scan-fourth-repaired-candidate-5. Fixture membership is unchanged.
The verified populations remain 34 authoritative byte constants, six canonical package vectors, 19 package identities, 18 descriptor presentations, 18 path-scalar vectors, six pointer vectors, 184 unique fixture IDs, 124 diagnostic expectations, and a 31-code diagnostic vocabulary.
The completed independent read-only review of the exact fourth repaired candidate verified all 2613 lines, every normative and fixture population, all golden arithmetic, and the DATA_CHANGED identity, and reported P0=0, P1=0, P2=0, and P3=0. This acceptance records that supplied independent-review result and does not claim to perform another independent review.
The fourth repaired candidate is accepted as this normative companion and closes the PC6 Package Scan semantic ambiguities without authorizing implementation or any later compiler, Builder, runtime, provider, or product work.
FOUNDATION_ACCEPTED=true
PC1_ACCEPTED=true
PC2_ACCEPTED=true
PC3_ACCEPTED=true
DEFAULT_ERRATUM_COMPLETE=true
CANONICAL_JSON_ERRATUM_COMPLETE=true
PC4_ACCEPTED=true
PC5_ACCEPTED=true
PUSH_COMPLETE=true
PC6_SCOPE_RECONCILED=true
PACKAGE_SCAN_ERRATUM_PROPOSAL_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_REVIEW_P1=6
PACKAGE_SCAN_ERRATUM_REVIEW_P2=1
PACKAGE_SCAN_ERRATUM_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P1=4
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P2=1
PACKAGE_SCAN_ERRATUM_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P1=6
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P2=2
PACKAGE_SCAN_ERRATUM_SECOND_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P1=2
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P2=0
PACKAGE_SCAN_ERRATUM_THIRD_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_COMPLETE=true
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_COMPLETE=true
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P0=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P1=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P2=0
PACKAGE_SCAN_ERRATUM_FOURTH_REPAIR_REVIEW_P3=0
PACKAGE_SCAN_ERRATUM_ACCEPTED=true
PC6_SEMANTICS_FROZEN=true
PC6_FREEZE_VERIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_STARTED=false
PC6_ACCEPTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC6 Package Scan implementation only
