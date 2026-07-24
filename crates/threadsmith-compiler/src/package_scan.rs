//! PC6 Package Scan.
//!
//! Host snapshot acquisition and semantic Package Scan deliberately have
//! separate result types. The snapshot input contains only the exact optional
//! `packages` root child and its complete immutable subtree.

use crate::{DigestedSource, SourceDiagnostic, parse_blueprint_source};
use core::cmp::Ordering;
use core::fmt;
use serde_json::{Map, Value};
use std::collections::{BTreeMap, BTreeSet};
use std::sync::Arc;
use threadsmith_canonical::{canonical_bytes, canonical_sha256, sha256_digest};
use threadsmith_schema::{ArtifactKind, NativeLatticeId};
use unicode_normalization::UnicodeNormalization;

/// Stable PC6 diagnostic-code vocabulary.
pub mod package_scan_diagnostic_codes {
    pub const PACKAGES_ROOT_INVALID: &str = "PACKAGE_SCAN_PACKAGES_ROOT_INVALID";
    pub const DISCOVERY_UNREADABLE: &str = "PACKAGE_SCAN_DISCOVERY_UNREADABLE";
    pub const LAYOUT_ENTRY_INVALID: &str = "PACKAGE_SCAN_LAYOUT_ENTRY_INVALID";
    pub const DESCRIPTOR_MISSING: &str = "PACKAGE_SCAN_DESCRIPTOR_MISSING";
    pub const DESCRIPTOR_NOT_REGULAR: &str = "PACKAGE_SCAN_DESCRIPTOR_NOT_REGULAR";
    pub const DESCRIPTOR_UNREADABLE: &str = "PACKAGE_SCAN_DESCRIPTOR_UNREADABLE";
    pub const SYMLINK_FORBIDDEN: &str = "PACKAGE_SCAN_SYMLINK_FORBIDDEN";
    pub const UNSAFE_FILESYSTEM_OBJECT: &str = "PACKAGE_SCAN_UNSAFE_FILESYSTEM_OBJECT";
    pub const DECLARED_PATH_COMPONENT_NOT_DIRECTORY: &str =
        "PACKAGE_SCAN_DECLARED_PATH_COMPONENT_NOT_DIRECTORY";
    pub const DECLARED_FILE_MISSING: &str = "PACKAGE_SCAN_DECLARED_FILE_MISSING";
    pub const DECLARED_FILE_NOT_REGULAR: &str = "PACKAGE_SCAN_DECLARED_FILE_NOT_REGULAR";
    pub const DECLARED_FILE_UNREADABLE: &str = "PACKAGE_SCAN_DECLARED_FILE_UNREADABLE";
    pub const FILE_HASH_MISMATCH: &str = "PACKAGE_SCAN_FILE_HASH_MISMATCH";
    pub const DESCRIPTOR_SOURCE_INVALID: &str = "PACKAGE_SCAN_DESCRIPTOR_SOURCE_INVALID";
    pub const DESCRIPTOR_YAML_FORBIDDEN: &str = "PACKAGE_SCAN_DESCRIPTOR_YAML_FORBIDDEN";
    pub const DESCRIPTOR_SCALAR_INVALID: &str = "PACKAGE_SCAN_DESCRIPTOR_SCALAR_INVALID";
    pub const DESCRIPTOR_NON_STRING_KEY: &str = "PACKAGE_SCAN_DESCRIPTOR_NON_STRING_KEY";
    pub const DESCRIPTOR_DUPLICATE_KEY: &str = "PACKAGE_SCAN_DESCRIPTOR_DUPLICATE_KEY";
    pub const DESCRIPTOR_NFC_COLLISION: &str = "PACKAGE_SCAN_DESCRIPTOR_NFC_COLLISION";
    pub const DESCRIPTOR_ROOT_INVALID: &str = "PACKAGE_SCAN_DESCRIPTOR_ROOT_INVALID";
    pub const DESCRIPTOR_UNKNOWN_KEY: &str = "PACKAGE_SCAN_DESCRIPTOR_UNKNOWN_KEY";
    pub const DESCRIPTOR_MEMBER_MISSING: &str = "PACKAGE_SCAN_DESCRIPTOR_MEMBER_MISSING";
    pub const DESCRIPTOR_FIELD_INVALID: &str = "PACKAGE_SCAN_DESCRIPTOR_FIELD_INVALID";
    pub const PACKAGE_DIRECTORY_MISMATCH: &str = "PACKAGE_SCAN_PACKAGE_DIRECTORY_MISMATCH";
    pub const VERSION_DIRECTORY_MISMATCH: &str = "PACKAGE_SCAN_VERSION_DIRECTORY_MISMATCH";
    pub const DECLARED_PATH_DUPLICATE: &str = "PACKAGE_SCAN_DECLARED_PATH_DUPLICATE";
    pub const DECLARED_PATH_INVALID: &str = "PACKAGE_SCAN_DECLARED_PATH_INVALID";
    pub const DECLARED_PATH_PREFIX_COLLISION: &str = "PACKAGE_SCAN_DECLARED_PATH_PREFIX_COLLISION";
    pub const MODULE_FILE_UNLISTED: &str = "PACKAGE_SCAN_MODULE_FILE_UNLISTED";
    pub const DESCRIPTOR_SELF_LISTED: &str = "PACKAGE_SCAN_DESCRIPTOR_SELF_LISTED";
    pub const DIGEST_SYNTAX_INVALID: &str = "PACKAGE_SCAN_DIGEST_SYNTAX_INVALID";

    pub const ALL: [&str; 31] = [
        PACKAGES_ROOT_INVALID,
        DISCOVERY_UNREADABLE,
        LAYOUT_ENTRY_INVALID,
        DESCRIPTOR_MISSING,
        DESCRIPTOR_NOT_REGULAR,
        DESCRIPTOR_UNREADABLE,
        SYMLINK_FORBIDDEN,
        UNSAFE_FILESYSTEM_OBJECT,
        DECLARED_PATH_COMPONENT_NOT_DIRECTORY,
        DECLARED_FILE_MISSING,
        DECLARED_FILE_NOT_REGULAR,
        DECLARED_FILE_UNREADABLE,
        FILE_HASH_MISMATCH,
        DESCRIPTOR_SOURCE_INVALID,
        DESCRIPTOR_YAML_FORBIDDEN,
        DESCRIPTOR_SCALAR_INVALID,
        DESCRIPTOR_NON_STRING_KEY,
        DESCRIPTOR_DUPLICATE_KEY,
        DESCRIPTOR_NFC_COLLISION,
        DESCRIPTOR_ROOT_INVALID,
        DESCRIPTOR_UNKNOWN_KEY,
        DESCRIPTOR_MEMBER_MISSING,
        DESCRIPTOR_FIELD_INVALID,
        PACKAGE_DIRECTORY_MISMATCH,
        VERSION_DIRECTORY_MISMATCH,
        DECLARED_PATH_DUPLICATE,
        DECLARED_PATH_INVALID,
        DECLARED_PATH_PREFIX_COLLISION,
        MODULE_FILE_UNLISTED,
        DESCRIPTOR_SELF_LISTED,
        DIGEST_SYNTAX_INVALID,
    ];
}

/// One deterministic semantic Package Scan failure.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct PackageScanDiagnostic {
    code: &'static str,
    path: String,
}

impl PackageScanDiagnostic {
    #[must_use]
    pub const fn code(&self) -> &'static str {
        self.code
    }

    #[must_use]
    pub fn path(&self) -> &str {
        &self.path
    }
}

impl fmt::Display for PackageScanDiagnostic {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{} at {}", self.code, self.path)
    }
}

impl std::error::Error for PackageScanDiagnostic {}

fn diagnostic(code: &'static str, path: impl Into<String>) -> PackageScanDiagnostic {
    PackageScanDiagnostic {
        code,
        path: path.into(),
    }
}

/// A native name presented to portable snapshot acquisition.
///
/// The non-Unicode variants let a host report names that cannot cross the
/// portable boundary without manufacturing a lossy Unicode spelling.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct SnapshotName {
    representation: SnapshotNameRepresentation,
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum SnapshotNameRepresentation {
    Unicode(String),
    UnixBytes(Vec<u8>),
    WindowsUtf16(Vec<u16>),
}

impl SnapshotName {
    #[must_use]
    pub fn unicode(value: impl Into<String>) -> Self {
        Self {
            representation: SnapshotNameRepresentation::Unicode(value.into()),
        }
    }

    #[must_use]
    pub fn unix_bytes(value: impl Into<Vec<u8>>) -> Self {
        Self {
            representation: SnapshotNameRepresentation::UnixBytes(value.into()),
        }
    }

    #[must_use]
    pub fn windows_utf16(value: impl Into<Vec<u16>>) -> Self {
        Self {
            representation: SnapshotNameRepresentation::WindowsUtf16(value.into()),
        }
    }
}

/// One immutable raw snapshot entry supplied to acquisition.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct SnapshotEntry {
    name: SnapshotName,
    node: SnapshotNode,
}

impl SnapshotEntry {
    #[must_use]
    pub fn new(name: SnapshotName, node: SnapshotNode) -> Self {
        Self { name, node }
    }
}

/// Raw immutable object classes accepted by snapshot acquisition.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct SnapshotNode {
    kind: SnapshotNodeKind,
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum SnapshotNodeKind {
    Directory(Vec<SnapshotEntry>),
    DirectoryUnreadable,
    Regular(Arc<[u8]>),
    RegularUnreadable,
    LinkLike,
    Special,
}

impl SnapshotNode {
    #[must_use]
    pub fn directory(children: Vec<SnapshotEntry>) -> Self {
        Self {
            kind: SnapshotNodeKind::Directory(children),
        }
    }

    #[must_use]
    pub fn directory_unreadable() -> Self {
        Self {
            kind: SnapshotNodeKind::DirectoryUnreadable,
        }
    }

    #[must_use]
    pub fn regular(bytes: Vec<u8>) -> Self {
        Self {
            kind: SnapshotNodeKind::Regular(Arc::from(bytes)),
        }
    }

    /// Construct a second logical entry sharing an immutable hard-link payload.
    #[must_use]
    pub fn regular_shared(bytes: Arc<[u8]>) -> Self {
        Self {
            kind: SnapshotNodeKind::Regular(bytes),
        }
    }

    #[must_use]
    pub fn regular_unreadable() -> Self {
        Self {
            kind: SnapshotNodeKind::RegularUnreadable,
        }
    }

    #[must_use]
    pub fn link_like() -> Self {
        Self {
            kind: SnapshotNodeKind::LinkLike,
        }
    }

    #[must_use]
    pub fn special() -> Self {
        Self {
            kind: SnapshotNodeKind::Special,
        }
    }
}

/// Snapshot acquisition failure outside semantic Package Scan.
#[derive(Clone, Debug, Eq, PartialEq)]
pub enum SnapshotAcquisitionError {
    UnrepresentableNativeName,
    MalformedUtf16Name,
    InvalidPortableName,
    NfcNameCollision,
    NamespaceAlias,
    IncompleteImmutableView,
    ConcurrentMutation,
    ResourceExhaustion,
    InconsistentObjectReference,
}

impl fmt::Display for SnapshotAcquisitionError {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str(match self {
            Self::UnrepresentableNativeName => "native name is not losslessly representable",
            Self::MalformedUtf16Name => "native name contains malformed UTF-16",
            Self::InvalidPortableName => "native name is not a portable snapshot component",
            Self::NfcNameCollision => "native names collide after NFC normalization",
            Self::NamespaceAlias => "host namespace aliases distinct exact entries",
            Self::IncompleteImmutableView => "complete immutable view could not be established",
            Self::ConcurrentMutation => "concurrent mutation prevented immutable acquisition",
            Self::ResourceExhaustion => "snapshot acquisition exhausted host resources",
            Self::InconsistentObjectReference => {
                "snapshot contains an inconsistent object reference"
            }
        })
    }
}

impl std::error::Error for SnapshotAcquisitionError {}

/// Completed immutable view of only the optional `packages` child.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct PortableProjectSnapshot {
    packages: Option<PortableNode>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct PortableEntry {
    name: String,
    node: PortableNode,
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum PortableNode {
    Directory(Vec<PortableEntry>),
    DirectoryUnreadable,
    Regular(Arc<[u8]>),
    RegularUnreadable,
    LinkLike,
    Special,
}

/// Acquire one portable immutable snapshot from an exact optional
/// `packages`-child result.
///
/// The caller must perform only the host root's exact `packages` lookup before
/// calling this function. Unrelated project-root entries are not represented
/// by this API and therefore cannot be enumerated by Package Scan.
pub fn acquire_project_snapshot(
    packages_lookup: Result<Option<SnapshotNode>, SnapshotAcquisitionError>,
) -> Result<PortableProjectSnapshot, SnapshotAcquisitionError> {
    let packages = packages_lookup?;
    Ok(PortableProjectSnapshot {
        packages: packages.map(acquire_node).transpose()?,
    })
}

fn acquire_node(node: SnapshotNode) -> Result<PortableNode, SnapshotAcquisitionError> {
    Ok(match node.kind {
        SnapshotNodeKind::Directory(children) => {
            let mut acquired = Vec::with_capacity(children.len());
            let mut names = BTreeSet::new();
            for child in children {
                let name = acquire_name(child.name)?;
                if !names.insert(name.clone()) {
                    return Err(SnapshotAcquisitionError::NfcNameCollision);
                }
                acquired.push(PortableEntry {
                    name,
                    node: acquire_node(child.node)?,
                });
            }
            acquired.sort_by(|left, right| left.name.as_bytes().cmp(right.name.as_bytes()));
            PortableNode::Directory(acquired)
        }
        SnapshotNodeKind::DirectoryUnreadable => PortableNode::DirectoryUnreadable,
        SnapshotNodeKind::Regular(bytes) => PortableNode::Regular(bytes),
        SnapshotNodeKind::RegularUnreadable => PortableNode::RegularUnreadable,
        SnapshotNodeKind::LinkLike => PortableNode::LinkLike,
        SnapshotNodeKind::Special => PortableNode::Special,
    })
}

fn acquire_name(name: SnapshotName) -> Result<String, SnapshotAcquisitionError> {
    let name = match name.representation {
        SnapshotNameRepresentation::Unicode(name) => name,
        SnapshotNameRepresentation::UnixBytes(bytes) => String::from_utf8(bytes)
            .map_err(|_| SnapshotAcquisitionError::UnrepresentableNativeName)?,
        SnapshotNameRepresentation::WindowsUtf16(units) => {
            String::from_utf16(&units).map_err(|_| SnapshotAcquisitionError::MalformedUtf16Name)?
        }
    };
    if name
        .chars()
        .any(|character| matches!(character, '\0' | '/'))
        || !name.nfc().eq(name.chars())
    {
        return Err(SnapshotAcquisitionError::InvalidPortableName);
    }
    Ok(name)
}

impl PortableNode {
    fn children(&self) -> Option<&[PortableEntry]> {
        match self {
            Self::Directory(children) => Some(children),
            _ => None,
        }
    }

    fn child(&self, name: &str) -> Option<&PortableNode> {
        let children = self.children()?;
        children
            .binary_search_by(|entry| entry.name.as_bytes().cmp(name.as_bytes()))
            .ok()
            .map(|index| &children[index].node)
    }
}

/// Opaque PC6-produced package identity.
///
/// A generic PC1 identity claim cannot be promoted into this phase-produced
/// proof:
///
/// ```compile_fail
/// use threadsmith_compiler::PackageIdentity;
/// use threadsmith_schema::{ArtifactKind, NativeLatticeId, Sha256Digest};
/// let generic = NativeLatticeId::from_canonical_digest(
///     ArtifactKind::Package,
///     Sha256Digest::from_bytes([0; 32]),
/// );
/// let _: PackageIdentity = generic.into();
/// ```
#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct PackageIdentity {
    identity: NativeLatticeId,
}

impl PackageIdentity {
    #[must_use]
    pub const fn as_native_id(&self) -> &NativeLatticeId {
        &self.identity
    }
}

impl fmt::Display for PackageIdentity {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Display::fmt(&self.identity, formatter)
    }
}

/// One admitted canonical descriptor file member.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct PackageDescriptorFile {
    path: String,
    sha256: String,
}

impl PackageDescriptorFile {
    #[must_use]
    pub fn path(&self) -> &str {
        &self.path
    }

    #[must_use]
    pub fn sha256(&self) -> &str {
        &self.sha256
    }
}

/// Exact admitted six-member canonical descriptor value.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ScannedPackageDescriptor {
    package: String,
    version: String,
    lattice: String,
    profiles: Vec<String>,
    module_file: String,
    files: Vec<PackageDescriptorFile>,
}

impl ScannedPackageDescriptor {
    #[must_use]
    pub fn package(&self) -> &str {
        &self.package
    }

    #[must_use]
    pub fn version(&self) -> &str {
        &self.version
    }

    #[must_use]
    pub fn lattice(&self) -> &str {
        &self.lattice
    }

    #[must_use]
    pub fn profiles(&self) -> &[String] {
        &self.profiles
    }

    #[must_use]
    pub fn module_file(&self) -> &str {
        &self.module_file
    }

    #[must_use]
    pub fn files(&self) -> &[PackageDescriptorFile] {
        &self.files
    }

    fn canonical_value(&self) -> Value {
        let files = self
            .files
            .iter()
            .map(|file| {
                let mut value = Map::new();
                value.insert("path".to_owned(), Value::String(file.path.clone()));
                value.insert("sha256".to_owned(), Value::String(file.sha256.clone()));
                Value::Object(value)
            })
            .collect();
        let mut value = Map::new();
        value.insert("package".to_owned(), Value::String(self.package.clone()));
        value.insert("version".to_owned(), Value::String(self.version.clone()));
        value.insert("lattice".to_owned(), Value::String(self.lattice.clone()));
        value.insert(
            "profiles".to_owned(),
            Value::Array(self.profiles.iter().cloned().map(Value::String).collect()),
        );
        value.insert(
            "module_file".to_owned(),
            Value::String(self.module_file.clone()),
        );
        value.insert("files".to_owned(), Value::Array(files));
        Value::Object(value)
    }
}

/// One declared logical path bound to its exact verified immutable bytes.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct VerifiedPackageFile {
    path: String,
    bytes: Arc<[u8]>,
}

impl VerifiedPackageFile {
    #[must_use]
    pub fn path(&self) -> &str {
        &self.path
    }

    #[must_use]
    pub fn bytes(&self) -> &[u8] {
        self.bytes.as_ref()
    }
}

/// One inseparable PC6 package record.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ScannedPackage {
    descriptor: ScannedPackageDescriptor,
    identity: PackageIdentity,
    verified_files: Vec<VerifiedPackageFile>,
}

impl ScannedPackage {
    #[must_use]
    pub const fn descriptor(&self) -> &ScannedPackageDescriptor {
        &self.descriptor
    }

    #[must_use]
    pub const fn identity(&self) -> &PackageIdentity {
        &self.identity
    }

    #[must_use]
    pub fn verified_files(&self) -> &[VerifiedPackageFile] {
        &self.verified_files
    }

    /// Reproduce the exact derived canonical descriptor bytes.
    #[must_use]
    pub fn canonical_descriptor_bytes(&self) -> Vec<u8> {
        canonical_bytes(&self.descriptor.canonical_value())
            .expect("admitted package descriptors must be canonically encodable")
    }
}

/// Non-authoritative PC6 output bound to one exact PC5 source.
///
/// External callers cannot independently pair a source with a package list:
///
/// ```compile_fail
/// use threadsmith_compiler::{DigestedSource, ScannedSource};
/// fn forge(source: DigestedSource) -> ScannedSource {
///     ScannedSource { digested_source: source, packages: Vec::new() }
/// }
/// ```
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ScannedSource {
    digested_source: DigestedSource,
    packages: Vec<ScannedPackage>,
}

impl ScannedSource {
    #[must_use]
    pub const fn digested_source(&self) -> &DigestedSource {
        &self.digested_source
    }

    #[must_use]
    pub fn packages(&self) -> &[ScannedPackage] {
        &self.packages
    }
}

struct Candidate<'snapshot> {
    package: &'snapshot str,
    version: &'snapshot str,
    version_node: &'snapshot PortableNode,
    descriptor_node: &'snapshot PortableNode,
    version_path: String,
    descriptor_path: String,
}

struct ParsedCandidate<'snapshot> {
    candidate: Candidate<'snapshot>,
    value: Value,
}

struct ShallowCandidate<'snapshot> {
    candidate: Candidate<'snapshot>,
    root: Map<String, Value>,
    package: String,
    version: String,
    lattice: String,
}

struct AdmittedCandidate<'snapshot> {
    candidate: Candidate<'snapshot>,
    descriptor: ScannedPackageDescriptor,
}

struct VerifiedCandidate {
    descriptor: ScannedPackageDescriptor,
    verified_files: Vec<VerifiedPackageFile>,
}

/// Perform semantic PC6 Package Scan over one exact source and snapshot.
pub fn scan_packages(
    source: DigestedSource,
    snapshot: PortableProjectSnapshot,
) -> Result<ScannedSource, PackageScanDiagnostic> {
    let Some(packages_node) = snapshot.packages.as_ref() else {
        return Ok(ScannedSource {
            digested_source: source,
            packages: Vec::new(),
        });
    };
    let packages = require_packages_root(packages_node)?;
    let candidates = discover_candidates(packages)?;

    let mut parsed = Vec::with_capacity(candidates.len());
    for candidate in candidates {
        let PortableNode::Regular(bytes) = candidate.descriptor_node else {
            unreachable!("structural discovery admitted descriptor bytes");
        };
        let value = parse_blueprint_source(bytes)
            .map_err(|error| map_parser_diagnostic(error, &candidate.descriptor_path))?;
        parsed.push(ParsedCandidate { candidate, value });
    }

    let mut shallow = Vec::with_capacity(parsed.len());
    for parsed in parsed {
        shallow.push(admit_shallow(parsed)?);
    }

    let mut admitted = Vec::with_capacity(shallow.len());
    for shallow in shallow {
        admitted.push(admit_collections(shallow)?);
    }

    for record in &admitted {
        metadata_audit(
            record.candidate.version_node,
            &record.candidate.version_path,
        )?;
    }

    let mut verified = Vec::with_capacity(admitted.len());
    for record in admitted {
        let verified_files = verify_declared_files(&record)?;
        verified.push(VerifiedCandidate {
            descriptor: record.descriptor,
            verified_files,
        });
    }

    let mut scanned_packages = Vec::with_capacity(verified.len());
    for record in verified {
        let digest = canonical_sha256(&record.descriptor.canonical_value())
            .expect("admitted package descriptors must be canonically encodable");
        scanned_packages.push(ScannedPackage {
            descriptor: record.descriptor,
            identity: PackageIdentity {
                identity: NativeLatticeId::from_canonical_digest(ArtifactKind::Package, digest),
            },
            verified_files: record.verified_files,
        });
    }

    Ok(ScannedSource {
        digested_source: source,
        packages: scanned_packages,
    })
}

fn require_packages_root(node: &PortableNode) -> Result<&[PortableEntry], PackageScanDiagnostic> {
    match node {
        PortableNode::LinkLike => Err(diagnostic(
            package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
            "packages",
        )),
        PortableNode::Directory(children) => Ok(children),
        PortableNode::DirectoryUnreadable => Err(diagnostic(
            package_scan_diagnostic_codes::DISCOVERY_UNREADABLE,
            "packages",
        )),
        _ => Err(diagnostic(
            package_scan_diagnostic_codes::PACKAGES_ROOT_INVALID,
            "packages",
        )),
    }
}

fn discover_candidates(
    packages: &[PortableEntry],
) -> Result<Vec<Candidate<'_>>, PackageScanDiagnostic> {
    let mut candidates = Vec::new();
    for package_entry in packages {
        let package_path = join_path("packages", &package_entry.name);
        let versions = match &package_entry.node {
            PortableNode::LinkLike => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                    render_path(&["packages", &package_entry.name]),
                ));
            }
            _ if !is_package_name(&package_entry.name) => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::LAYOUT_ENTRY_INVALID,
                    render_path(&["packages", &package_entry.name]),
                ));
            }
            PortableNode::Directory(children) => children,
            PortableNode::DirectoryUnreadable => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::DISCOVERY_UNREADABLE,
                    render_path(&["packages", &package_entry.name]),
                ));
            }
            _ => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::LAYOUT_ENTRY_INVALID,
                    render_path(&["packages", &package_entry.name]),
                ));
            }
        };

        for version_entry in versions {
            let version_path = join_path(&package_path, &version_entry.name);
            let version_children = match &version_entry.node {
                PortableNode::LinkLike => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                        render_path(&["packages", &package_entry.name, &version_entry.name]),
                    ));
                }
                _ if !is_package_version(&version_entry.name) => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::LAYOUT_ENTRY_INVALID,
                        render_path(&["packages", &package_entry.name, &version_entry.name]),
                    ));
                }
                PortableNode::Directory(children) => children,
                PortableNode::DirectoryUnreadable => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::DISCOVERY_UNREADABLE,
                        render_path(&["packages", &package_entry.name, &version_entry.name]),
                    ));
                }
                _ => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::LAYOUT_ENTRY_INVALID,
                        render_path(&["packages", &package_entry.name, &version_entry.name]),
                    ));
                }
            };
            let descriptor_path = format!("{version_path}/package.yaml");
            let descriptor_node = version_children
                .binary_search_by(|entry| entry.name.as_bytes().cmp(b"package.yaml"))
                .ok()
                .map(|index| &version_children[index].node);
            let Some(descriptor_node) = descriptor_node else {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::DESCRIPTOR_MISSING,
                    render_path(&[
                        "packages",
                        &package_entry.name,
                        &version_entry.name,
                        "package.yaml",
                    ]),
                ));
            };
            match descriptor_node {
                PortableNode::LinkLike => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                        render_path(&[
                            "packages",
                            &package_entry.name,
                            &version_entry.name,
                            "package.yaml",
                        ]),
                    ));
                }
                PortableNode::Regular(_) => {}
                PortableNode::RegularUnreadable => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::DESCRIPTOR_UNREADABLE,
                        render_path(&[
                            "packages",
                            &package_entry.name,
                            &version_entry.name,
                            "package.yaml",
                        ]),
                    ));
                }
                _ => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::DESCRIPTOR_NOT_REGULAR,
                        render_path(&[
                            "packages",
                            &package_entry.name,
                            &version_entry.name,
                            "package.yaml",
                        ]),
                    ));
                }
            }
            candidates.push(Candidate {
                package: &package_entry.name,
                version: &version_entry.name,
                version_node: &version_entry.node,
                descriptor_node,
                version_path,
                descriptor_path,
            });
        }
    }
    candidates.sort_by(|left, right| {
        left.package
            .as_bytes()
            .cmp(right.package.as_bytes())
            .then_with(|| compare_versions(left.version, right.version))
    });
    Ok(candidates)
}

fn map_parser_diagnostic(error: SourceDiagnostic, descriptor_path: &str) -> PackageScanDiagnostic {
    let code = match error.code {
        "SOURCE_INVALID_UTF8" => package_scan_diagnostic_codes::DESCRIPTOR_SOURCE_INVALID,
        "SOURCE_FORBIDDEN_YAML" => package_scan_diagnostic_codes::DESCRIPTOR_YAML_FORBIDDEN,
        "SOURCE_INVALID_SCALAR" => package_scan_diagnostic_codes::DESCRIPTOR_SCALAR_INVALID,
        "SOURCE_NON_STRING_KEY" => package_scan_diagnostic_codes::DESCRIPTOR_NON_STRING_KEY,
        "SOURCE_DUPLICATE_KEY" => package_scan_diagnostic_codes::DESCRIPTOR_DUPLICATE_KEY,
        "SOURCE_NFC_COLLISION" => package_scan_diagnostic_codes::DESCRIPTOR_NFC_COLLISION,
        _ => unreachable!("accepted PC2 parser has exactly six outcomes"),
    };
    diagnostic(code, format!("{descriptor_path}#"))
}

fn admit_shallow<'snapshot>(
    parsed: ParsedCandidate<'snapshot>,
) -> Result<ShallowCandidate<'snapshot>, PackageScanDiagnostic> {
    let descriptor_path = &parsed.candidate.descriptor_path;
    let Value::Object(root) = parsed.value else {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_ROOT_INVALID,
            descriptor_path,
            &[],
        ));
    };
    const KEYS: [&str; 6] = [
        "package",
        "version",
        "lattice",
        "profiles",
        "module_file",
        "files",
    ];
    if let Some(key) = root
        .keys()
        .filter(|key| !KEYS.contains(&key.as_str()))
        .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
    {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_UNKNOWN_KEY,
            descriptor_path,
            &[key],
        ));
    }
    for key in KEYS {
        if !root.contains_key(key) {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DESCRIPTOR_MEMBER_MISSING,
                descriptor_path,
                &[key],
            ));
        }
    }
    for key in KEYS {
        let value = &root[key];
        let valid = match key {
            "package" | "version" | "lattice" | "module_file" => value.is_string(),
            "profiles" | "files" => value.is_array(),
            _ => unreachable!(),
        };
        if !valid {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
                descriptor_path,
                &[key],
            ));
        }
    }
    let package = root["package"].as_str().unwrap().to_owned();
    let version = root["version"].as_str().unwrap().to_owned();
    let lattice = root["lattice"].as_str().unwrap().to_owned();
    if !is_package_name(&package) {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["package"],
        ));
    }
    if !is_package_version(&version) {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["version"],
        ));
    }
    if lattice != "0.3" {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["lattice"],
        ));
    }
    if package != parsed.candidate.package {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::PACKAGE_DIRECTORY_MISMATCH,
            descriptor_path,
            &["package"],
        ));
    }
    if version != parsed.candidate.version {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::VERSION_DIRECTORY_MISMATCH,
            descriptor_path,
            &["version"],
        ));
    }
    Ok(ShallowCandidate {
        candidate: parsed.candidate,
        root,
        package,
        version,
        lattice,
    })
}

fn admit_collections<'snapshot>(
    shallow: ShallowCandidate<'snapshot>,
) -> Result<AdmittedCandidate<'snapshot>, PackageScanDiagnostic> {
    let descriptor_path = &shallow.candidate.descriptor_path;
    let profiles = shallow.root["profiles"].as_array().unwrap();
    if profiles.is_empty() {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["profiles"],
        ));
    }
    for (index, profile) in profiles.iter().enumerate() {
        if !profile.is_string() {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
                descriptor_path,
                &["profiles", &index.to_string()],
            ));
        }
    }
    let profile_strings = profiles
        .iter()
        .enumerate()
        .map(|(index, value)| (value.as_str().unwrap(), index))
        .collect::<Vec<_>>();
    if let Some((_value, index)) = profile_strings
        .iter()
        .filter(|(value, _)| !matches!(*value, "lattice-builder-0.1" | "lattice-core-0.1"))
        .min_by(|left, right| {
            left.0
                .as_bytes()
                .cmp(right.0.as_bytes())
                .then(left.1.cmp(&right.1))
        })
    {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["profiles", &index.to_string()],
        ));
    }
    let mut profile_indices = BTreeMap::<&str, Vec<usize>>::new();
    for (value, index) in &profile_strings {
        profile_indices.entry(*value).or_default().push(*index);
    }
    if let Some((_value, indices)) = profile_indices
        .iter()
        .find(|(_, indices)| indices.len() > 1)
    {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["profiles", &indices[1].to_string()],
        ));
    }
    let mut admitted_profiles = profile_strings
        .into_iter()
        .map(|(value, _)| value.to_owned())
        .collect::<Vec<_>>();
    admitted_profiles.sort_by(|left, right| left.as_bytes().cmp(right.as_bytes()));

    let module_file = shallow.root["module_file"].as_str().unwrap().to_owned();
    if !is_portable_path(&module_file) {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DECLARED_PATH_INVALID,
            descriptor_path,
            &["module_file"],
        ));
    }

    let files = shallow.root["files"].as_array().unwrap();
    if files.is_empty() {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
            descriptor_path,
            &["files"],
        ));
    }
    for (index, file) in files.iter().enumerate() {
        if !file.is_object() {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
                descriptor_path,
                &["files", &index.to_string()],
            ));
        }
    }
    for (index, file) in files.iter().enumerate() {
        let object = file.as_object().unwrap();
        if let Some(key) = object
            .keys()
            .filter(|key| !matches!(key.as_str(), "path" | "sha256"))
            .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
        {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DESCRIPTOR_UNKNOWN_KEY,
                descriptor_path,
                &["files", &index.to_string(), key],
            ));
        }
    }
    for key in ["path", "sha256"] {
        for (index, file) in files.iter().enumerate() {
            let object = file.as_object().unwrap();
            if !object.contains_key(key) {
                return Err(descriptor_diagnostic(
                    package_scan_diagnostic_codes::DESCRIPTOR_MEMBER_MISSING,
                    descriptor_path,
                    &["files", &index.to_string(), key],
                ));
            }
        }
    }
    for (index, file) in files.iter().enumerate() {
        let object = file.as_object().unwrap();
        for key in ["path", "sha256"] {
            if !object[key].is_string() {
                return Err(descriptor_diagnostic(
                    package_scan_diagnostic_codes::DESCRIPTOR_FIELD_INVALID,
                    descriptor_path,
                    &["files", &index.to_string(), key],
                ));
            }
        }
    }

    struct IndexedFile {
        original_index: usize,
        path: String,
        sha256: String,
    }
    let mut indexed = files
        .iter()
        .enumerate()
        .map(|(original_index, value)| {
            let value = value.as_object().unwrap();
            IndexedFile {
                original_index,
                path: value["path"].as_str().unwrap().to_owned(),
                sha256: value["sha256"].as_str().unwrap().to_owned(),
            }
        })
        .collect::<Vec<_>>();

    let mut duplicates = BTreeMap::<&str, Vec<usize>>::new();
    for file in &indexed {
        duplicates
            .entry(file.path.as_str())
            .or_default()
            .push(file.original_index);
    }
    if let Some((_path, indices)) = duplicates.iter().find(|(_, indices)| indices.len() > 1) {
        let mut indices = indices.to_vec();
        indices.sort_unstable();
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DECLARED_PATH_DUPLICATE,
            descriptor_path,
            &["files", &indices[1].to_string(), "path"],
        ));
    }

    if let Some(file) = indexed
        .iter()
        .filter(|file| !is_portable_path(&file.path))
        .min_by(|left, right| {
            left.path
                .as_bytes()
                .cmp(right.path.as_bytes())
                .then(left.original_index.cmp(&right.original_index))
        })
    {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DECLARED_PATH_INVALID,
            descriptor_path,
            &["files", &file.original_index.to_string(), "path"],
        ));
    }

    indexed.sort_by(|left, right| left.path.as_bytes().cmp(right.path.as_bytes()));
    if let Some(file) = indexed.iter().find(|file| !is_digest(&file.sha256)) {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DIGEST_SYNTAX_INVALID,
            descriptor_path,
            &["files", &file.original_index.to_string(), "sha256"],
        ));
    }
    if let Some(file) = indexed.iter().find(|file| file.path == "package.yaml") {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::DESCRIPTOR_SELF_LISTED,
            descriptor_path,
            &["files", &file.original_index.to_string(), "path"],
        ));
    }
    for (short_index, shorter) in indexed.iter().enumerate() {
        let prefix = format!("{}/", shorter.path);
        if let Some(longer) = indexed[short_index + 1..]
            .iter()
            .filter(|file| file.path.starts_with(&prefix))
            .min_by(|left, right| left.path.as_bytes().cmp(right.path.as_bytes()))
        {
            return Err(descriptor_diagnostic(
                package_scan_diagnostic_codes::DECLARED_PATH_PREFIX_COLLISION,
                descriptor_path,
                &["files", &longer.original_index.to_string(), "path"],
            ));
        }
    }
    if !indexed.iter().any(|file| file.path == module_file) {
        return Err(descriptor_diagnostic(
            package_scan_diagnostic_codes::MODULE_FILE_UNLISTED,
            descriptor_path,
            &["module_file"],
        ));
    }

    let files = indexed
        .into_iter()
        .map(|file| PackageDescriptorFile {
            path: file.path,
            sha256: file.sha256,
        })
        .collect();
    Ok(AdmittedCandidate {
        candidate: shallow.candidate,
        descriptor: ScannedPackageDescriptor {
            package: shallow.package,
            version: shallow.version,
            lattice: shallow.lattice,
            profiles: admitted_profiles,
            module_file,
            files,
        },
    })
}

fn metadata_audit(node: &PortableNode, path: &str) -> Result<(), PackageScanDiagnostic> {
    match node {
        PortableNode::Directory(children) => {
            for child in children {
                let child_path = join_path(path, &child.name);
                match &child.node {
                    PortableNode::LinkLike => {
                        return Err(diagnostic(
                            package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                            child_path,
                        ));
                    }
                    PortableNode::Directory(_) | PortableNode::DirectoryUnreadable => {
                        metadata_audit(&child.node, &child_path)?;
                    }
                    _ => {}
                }
            }
            Ok(())
        }
        PortableNode::DirectoryUnreadable => Err(diagnostic(
            package_scan_diagnostic_codes::DISCOVERY_UNREADABLE,
            path,
        )),
        _ => unreachable!("metadata audit starts at an admitted directory"),
    }
}

fn verify_declared_files(
    record: &AdmittedCandidate<'_>,
) -> Result<Vec<VerifiedPackageFile>, PackageScanDiagnostic> {
    let mut verified = Vec::with_capacity(record.descriptor.files.len());
    for file in &record.descriptor.files {
        let mut node = record.candidate.version_node;
        let mut path = record.candidate.version_path.clone();
        let segments = file.path.split('/').collect::<Vec<_>>();
        for segment in &segments[..segments.len() - 1] {
            path = join_path(&path, segment);
            let Some(child) = node.child(segment) else {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::DECLARED_FILE_MISSING,
                    path,
                ));
            };
            match child {
                PortableNode::LinkLike => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                        path,
                    ));
                }
                PortableNode::Regular(_) | PortableNode::RegularUnreadable => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::DECLARED_PATH_COMPONENT_NOT_DIRECTORY,
                        path,
                    ));
                }
                PortableNode::Special => {
                    return Err(diagnostic(
                        package_scan_diagnostic_codes::UNSAFE_FILESYSTEM_OBJECT,
                        path,
                    ));
                }
                PortableNode::Directory(_) => node = child,
                PortableNode::DirectoryUnreadable => {
                    unreachable!("metadata audit owns unreadable directories")
                }
            }
        }
        let final_segment = segments.last().unwrap();
        path = join_path(&path, final_segment);
        let Some(final_node) = node.child(final_segment) else {
            return Err(diagnostic(
                package_scan_diagnostic_codes::DECLARED_FILE_MISSING,
                path,
            ));
        };
        let bytes = match final_node {
            PortableNode::LinkLike => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::SYMLINK_FORBIDDEN,
                    path,
                ));
            }
            PortableNode::Special => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::UNSAFE_FILESYSTEM_OBJECT,
                    path,
                ));
            }
            PortableNode::Directory(_) => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::DECLARED_FILE_NOT_REGULAR,
                    path,
                ));
            }
            PortableNode::DirectoryUnreadable => {
                unreachable!("metadata audit owns unreadable directories")
            }
            PortableNode::RegularUnreadable => {
                return Err(diagnostic(
                    package_scan_diagnostic_codes::DECLARED_FILE_UNREADABLE,
                    path,
                ));
            }
            PortableNode::Regular(bytes) => bytes,
        };
        if sha256_digest(bytes).to_hex() != file.sha256 {
            return Err(diagnostic(
                package_scan_diagnostic_codes::FILE_HASH_MISMATCH,
                path,
            ));
        }
        verified.push(VerifiedPackageFile {
            path: file.path.clone(),
            bytes: Arc::clone(bytes),
        });
    }
    Ok(verified)
}

fn descriptor_diagnostic(
    code: &'static str,
    descriptor_path: &str,
    pointer: &[&str],
) -> PackageScanDiagnostic {
    diagnostic(code, render_descriptor_path(descriptor_path, pointer))
}

fn render_descriptor_path(descriptor_path: &str, pointer: &[&str]) -> String {
    let mut output = String::with_capacity(descriptor_path.len() + 16);
    output.push_str(descriptor_path);
    output.push('#');
    for token in pointer {
        output.push('/');
        let escaped = token.replace('~', "~0").replace('/', "~1");
        output.push_str(&percent_encode(escaped.as_bytes()));
    }
    output
}

fn render_path(components: &[&str]) -> String {
    components
        .iter()
        .map(|component| percent_encode(component.as_bytes()))
        .collect::<Vec<_>>()
        .join("/")
}

fn join_path(prefix: &str, component: &str) -> String {
    format!("{prefix}/{}", percent_encode(component.as_bytes()))
}

fn percent_encode(bytes: &[u8]) -> String {
    const HEX: &[u8; 16] = b"0123456789ABCDEF";
    let mut output = String::with_capacity(bytes.len());
    for byte in bytes {
        if byte.is_ascii_alphanumeric() || matches!(*byte, b'-' | b'.' | b'_' | b'~') {
            output.push(char::from(*byte));
        } else {
            output.push('%');
            output.push(char::from(HEX[usize::from(byte >> 4)]));
            output.push(char::from(HEX[usize::from(byte & 0x0f)]));
        }
    }
    output
}

fn is_package_name(value: &str) -> bool {
    let bytes = value.as_bytes();
    if !bytes.first().is_some_and(u8::is_ascii_lowercase) {
        return false;
    }
    let mut after_separator = false;
    for byte in &bytes[1..] {
        if matches!(*byte, b'.' | b'_' | b'-') {
            if after_separator {
                return false;
            }
            after_separator = true;
        } else if byte.is_ascii_lowercase() || byte.is_ascii_digit() {
            after_separator = false;
        } else {
            return false;
        }
    }
    !after_separator
}

fn is_package_version(value: &str) -> bool {
    let mut components = value.split('.');
    (0..3).all(|_| components.next().is_some_and(is_canonical_decimal))
        && components.next().is_none()
}

fn is_canonical_decimal(value: &str) -> bool {
    value == "0"
        || (value
            .as_bytes()
            .first()
            .is_some_and(|byte| matches!(byte, b'1'..=b'9'))
            && value.bytes().all(|byte| byte.is_ascii_digit()))
}

fn compare_versions(left: &str, right: &str) -> Ordering {
    for (left, right) in left.split('.').zip(right.split('.')) {
        let order = left
            .len()
            .cmp(&right.len())
            .then_with(|| left.as_bytes().cmp(right.as_bytes()));
        if order != Ordering::Equal {
            return order;
        }
    }
    Ordering::Equal
}

fn is_portable_path(value: &str) -> bool {
    if value.is_empty() || !value.is_ascii() {
        return false;
    }
    value.split('/').all(|segment| {
        if segment.is_empty() || is_reserved_basename(segment) {
            return false;
        }
        let bytes = segment.as_bytes();
        bytes
            .first()
            .is_some_and(|byte| byte.is_ascii_lowercase() || byte.is_ascii_digit())
            && bytes
                .last()
                .is_some_and(|byte| byte.is_ascii_lowercase() || byte.is_ascii_digit())
            && bytes.iter().all(|byte| {
                byte.is_ascii_lowercase()
                    || byte.is_ascii_digit()
                    || matches!(*byte, b'.' | b'_' | b'-')
            })
    })
}

fn is_reserved_basename(segment: &str) -> bool {
    let basename = segment.split('.').next().unwrap_or(segment);
    matches!(basename, "con" | "prn" | "aux" | "nul")
        || basename.strip_prefix("com").is_some_and(|suffix| {
            matches!(suffix, "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9")
        })
        || basename.strip_prefix("lpt").is_some_and(|suffix| {
            matches!(suffix, "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9")
        })
}

fn is_digest(value: &str) -> bool {
    value.len() == 64
        && value
            .bytes()
            .all(|byte| byte.is_ascii_digit() || matches!(byte, b'a'..=b'f'))
}
