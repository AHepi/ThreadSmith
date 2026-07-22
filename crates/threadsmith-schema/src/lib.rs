#![forbid(unsafe_code)]

use core::fmt;
use core::str::FromStr;
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use unicode_normalization::UnicodeNormalization;

pub const LATTICE_VERSION: &str = "0.3";
pub const CORE_PROFILE: &str = "lattice-core-0.1";
pub const NATIVE_SCHEMA_PROFILE: &str = "threadsmith-lattice-native-0.1";
pub const MIGRATION_PROFILE: &str = "threadsmith-lattice-migration-0.1";
pub const REFERENCE_WHEEL_SHA256: &str =
    "f6643d5534d2bacb96ca20566c401bf0ffaabec4c29768d4293389052f349ef5";

pub mod error_code {
    pub const IDENTITY_FORMAT_INVALID: &str = "IDENTITY_FORMAT_INVALID";
    pub const IDENTITY_KIND_UNSUPPORTED: &str = "IDENTITY_KIND_UNSUPPORTED";
    pub const IDENTITY_PREIMAGE_UNRESOLVED: &str = "IDENTITY_PREIMAGE_UNRESOLVED";
    pub const LEGACY_ID_UNVERIFIED: &str = "LEGACY_ID_UNVERIFIED";
    pub const LEGACY_MIGRATION_REJECTED: &str = "LEGACY_MIGRATION_REJECTED";
    pub const LEGACY_AUTHORITY_FORBIDDEN: &str = "LEGACY_AUTHORITY_FORBIDDEN";
    pub const SCHEMA_INVALID: &str = "SCHEMA_INVALID";
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct SchemaError {
    code: &'static str,
    message: String,
}

impl SchemaError {
    #[must_use]
    pub fn new(code: &'static str, message: impl Into<String>) -> Self {
        Self {
            code,
            message: message.into(),
        }
    }

    #[must_use]
    pub const fn code(&self) -> &'static str {
        self.code
    }

    #[must_use]
    pub fn message(&self) -> &str {
        &self.message
    }
}

impl fmt::Display for SchemaError {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{}: {}", self.code, self.message)
    }
}

impl std::error::Error for SchemaError {}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub enum ArtifactKind {
    Blueprint,
    Package,
    Resource,
    Contract,
    Unit,
    Link,
    Policy,
    Scenario,
    Lock,
    Manifest,
    Qualification,
    Binding,
    Envelope,
    Event,
}

impl ArtifactKind {
    pub const ALL: [Self; 14] = [
        Self::Blueprint,
        Self::Package,
        Self::Resource,
        Self::Contract,
        Self::Unit,
        Self::Link,
        Self::Policy,
        Self::Scenario,
        Self::Lock,
        Self::Manifest,
        Self::Qualification,
        Self::Binding,
        Self::Envelope,
        Self::Event,
    ];

    #[must_use]
    pub const fn as_str(self) -> &'static str {
        match self {
            Self::Blueprint => "blueprint",
            Self::Package => "package",
            Self::Resource => "resource",
            Self::Contract => "contract",
            Self::Unit => "unit",
            Self::Link => "link",
            Self::Policy => "policy",
            Self::Scenario => "scenario",
            Self::Lock => "lock",
            Self::Manifest => "manifest",
            Self::Qualification => "qualification",
            Self::Binding => "binding",
            Self::Envelope => "envelope",
            Self::Event => "event",
        }
    }
}

impl fmt::Display for ArtifactKind {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str(self.as_str())
    }
}

impl FromStr for ArtifactKind {
    type Err = SchemaError;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        match value {
            "blueprint" => Ok(Self::Blueprint),
            "package" => Ok(Self::Package),
            "resource" => Ok(Self::Resource),
            "contract" => Ok(Self::Contract),
            "unit" => Ok(Self::Unit),
            "link" => Ok(Self::Link),
            "policy" => Ok(Self::Policy),
            "scenario" => Ok(Self::Scenario),
            "lock" => Ok(Self::Lock),
            "manifest" => Ok(Self::Manifest),
            "qualification" => Ok(Self::Qualification),
            "binding" => Ok(Self::Binding),
            "envelope" => Ok(Self::Envelope),
            "event" => Ok(Self::Event),
            _ => Err(SchemaError::new(
                error_code::IDENTITY_KIND_UNSUPPORTED,
                format!("unsupported native Lattice identity kind {value:?}"),
            )),
        }
    }
}

impl Serialize for ArtifactKind {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_str(self.as_str())
    }
}

impl<'de> Deserialize<'de> for ArtifactKind {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        let value = String::deserialize(deserializer)?;
        value.parse().map_err(serde::de::Error::custom)
    }
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct Sha256Digest([u8; 32]);

impl Sha256Digest {
    #[must_use]
    pub const fn from_bytes(bytes: [u8; 32]) -> Self {
        Self(bytes)
    }

    #[must_use]
    pub const fn as_bytes(&self) -> &[u8; 32] {
        &self.0
    }

    #[must_use]
    pub fn to_hex(self) -> String {
        const HEX: &[u8; 16] = b"0123456789abcdef";
        let mut output = String::with_capacity(64);
        for byte in self.0 {
            output.push(char::from(HEX[usize::from(byte >> 4)]));
            output.push(char::from(HEX[usize::from(byte & 0x0f)]));
        }
        output
    }
}

impl FromStr for Sha256Digest {
    type Err = SchemaError;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        if value.len() != 64 || !value.bytes().all(|byte| byte.is_ascii_hexdigit()) {
            return Err(SchemaError::new(
                error_code::IDENTITY_FORMAT_INVALID,
                "SHA-256 digest must contain exactly 64 hexadecimal characters",
            ));
        }
        if value.bytes().any(|byte| byte.is_ascii_uppercase()) {
            return Err(SchemaError::new(
                error_code::IDENTITY_FORMAT_INVALID,
                "SHA-256 digest must use lowercase hexadecimal",
            ));
        }
        let mut bytes = [0_u8; 32];
        for (index, chunk) in value.as_bytes().chunks_exact(2).enumerate() {
            let high = hex_value(chunk[0]).ok_or_else(|| {
                SchemaError::new(
                    error_code::IDENTITY_FORMAT_INVALID,
                    "invalid SHA-256 digest",
                )
            })?;
            let low = hex_value(chunk[1]).ok_or_else(|| {
                SchemaError::new(
                    error_code::IDENTITY_FORMAT_INVALID,
                    "invalid SHA-256 digest",
                )
            })?;
            bytes[index] = (high << 4) | low;
        }
        Ok(Self(bytes))
    }
}

impl fmt::Display for Sha256Digest {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str(&self.to_hex())
    }
}

impl Serialize for Sha256Digest {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_str(&self.to_hex())
    }
}

impl<'de> Deserialize<'de> for Sha256Digest {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        let value = String::deserialize(deserializer)?;
        value.parse().map_err(serde::de::Error::custom)
    }
}

#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct LegacyKind(String);

impl LegacyKind {
    pub fn parse(value: impl Into<String>) -> Result<Self, SchemaError> {
        let value = value.into();
        let mut bytes = value.bytes();
        if !bytes.next().is_some_and(|byte| byte.is_ascii_lowercase())
            || !bytes.all(|byte| {
                byte.is_ascii_lowercase() || byte.is_ascii_digit() || byte == b'-' || byte == b'_'
            })
        {
            return Err(SchemaError::new(
                error_code::IDENTITY_FORMAT_INVALID,
                format!("invalid legacy identity kind {value:?}"),
            ));
        }
        Ok(Self(value))
    }

    #[must_use]
    pub fn as_str(&self) -> &str {
        &self.0
    }

    #[must_use]
    pub fn standard_kind(&self) -> Option<ArtifactKind> {
        self.0.parse().ok()
    }
}

#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct LegacyLatticeId {
    kind: LegacyKind,
    digest: Sha256Digest,
}

impl LegacyLatticeId {
    #[must_use]
    pub fn kind(&self) -> &LegacyKind {
        &self.kind
    }

    #[must_use]
    pub const fn digest(&self) -> Sha256Digest {
        self.digest
    }

    #[must_use]
    pub fn standard_kind(&self) -> Option<ArtifactKind> {
        self.kind.standard_kind()
    }

    pub fn reject_as_authority(&self) -> SchemaError {
        SchemaError::new(
            error_code::LEGACY_AUTHORITY_FORBIDDEN,
            format!("legacy identity {self} cannot grant execution authority"),
        )
    }
}

impl FromStr for LegacyLatticeId {
    type Err = SchemaError;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        let mut parts = value.split(':');
        let lattice = parts.next();
        let kind = parts.next();
        let algorithm = parts.next();
        let digest = parts.next();
        if lattice != Some("lattice")
            || algorithm != Some("sha256")
            || parts.next().is_some()
            || kind.is_none()
            || digest.is_none()
        {
            return Err(SchemaError::new(
                error_code::IDENTITY_FORMAT_INVALID,
                "identity must be lattice:<kind>:sha256:<64 lowercase hex>",
            ));
        }
        Ok(Self {
            kind: LegacyKind::parse(kind.unwrap_or_default())?,
            digest: digest.unwrap_or_default().parse()?,
        })
    }
}

impl fmt::Display for LegacyLatticeId {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            formatter,
            "lattice:{}:sha256:{}",
            self.kind.as_str(),
            self.digest
        )
    }
}

impl Serialize for LegacyLatticeId {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_str(&self.to_string())
    }
}

impl<'de> Deserialize<'de> for LegacyLatticeId {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        let value = String::deserialize(deserializer)?;
        value.parse().map_err(serde::de::Error::custom)
    }
}

#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct NativeLatticeId {
    kind: ArtifactKind,
    digest: Sha256Digest,
}

impl NativeLatticeId {
    /// Constructs a typed native-profile identity claim from a canonical digest.
    ///
    /// This constructor does not validate an artifact or grant authority. Callers
    /// that calculate or verify identities must use the artifact-specific API in
    /// `threadsmith-canonical`.
    #[must_use]
    pub const fn from_canonical_digest(kind: ArtifactKind, digest: Sha256Digest) -> Self {
        Self { kind, digest }
    }

    #[must_use]
    pub const fn kind(&self) -> ArtifactKind {
        self.kind
    }

    #[must_use]
    pub const fn digest(&self) -> Sha256Digest {
        self.digest
    }

    #[must_use]
    pub fn matches_legacy_claim(&self, legacy: &LegacyLatticeId) -> bool {
        legacy.standard_kind() == Some(self.kind) && legacy.digest == self.digest
    }
}

impl fmt::Display for NativeLatticeId {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            formatter,
            "lattice:{}:sha256:{}",
            self.kind.as_str(),
            self.digest
        )
    }
}

impl Serialize for NativeLatticeId {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_str(&self.to_string())
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct PackageFile {
    path: String,
    sha256: Sha256Digest,
}

impl PackageFile {
    pub fn new(path: impl Into<String>, sha256: Sha256Digest) -> Result<Self, SchemaError> {
        let path = normalize(path.into());
        validate_relative_file_path(&path)?;
        Ok(Self { path, sha256 })
    }

    #[must_use]
    pub fn path(&self) -> &str {
        &self.path
    }

    #[must_use]
    pub const fn sha256(&self) -> Sha256Digest {
        self.sha256
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct PackageDescriptor {
    package: String,
    version: String,
    profiles: Vec<String>,
    module_file: String,
    files: Vec<PackageFile>,
}

impl PackageDescriptor {
    pub fn new(
        package: impl Into<String>,
        version: impl Into<String>,
        profiles: Vec<String>,
        module_file: impl Into<String>,
        mut files: Vec<PackageFile>,
    ) -> Result<Self, SchemaError> {
        let package = normalize(package.into());
        validate_package_name(&package)?;
        let version = version.into();
        validate_version(&version)?;
        let normalized_profiles = profiles.into_iter().map(normalize).collect::<Vec<_>>();
        if normalized_profiles != [CORE_PROFILE] {
            return Err(schema_invalid(format!(
                "unsupported package profiles {normalized_profiles:?}; Foundation F2 supports only {CORE_PROFILE:?}"
            )));
        }
        let module_file = normalize(module_file.into());
        validate_relative_file_path(&module_file)?;
        files.sort_by(|left, right| left.path.as_bytes().cmp(right.path.as_bytes()));
        for pair in files.windows(2) {
            if pair[0].path == pair[1].path {
                return Err(schema_invalid(
                    "package file paths must be unique after NFC",
                ));
            }
        }
        if !files.iter().any(|file| file.path == module_file) {
            return Err(schema_invalid(
                "module_file must appear in the package file list",
            ));
        }
        Ok(Self {
            package,
            version,
            profiles: normalized_profiles,
            module_file,
            files,
        })
    }

    #[must_use]
    pub fn package(&self) -> &str {
        &self.package
    }

    #[must_use]
    pub fn version(&self) -> &str {
        &self.version
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
    pub fn files(&self) -> &[PackageFile] {
        &self.files
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct RequestedBy {
    module: String,
    requirement: String,
}

impl RequestedBy {
    pub fn new(
        module: impl Into<String>,
        requirement: impl Into<String>,
    ) -> Result<Self, SchemaError> {
        let module = normalize(module.into());
        validate_local_name(&module)?;
        let requirement = requirement.into();
        validate_version_requirement(&requirement)?;
        Ok(Self {
            module,
            requirement,
        })
    }

    #[must_use]
    pub fn module(&self) -> &str {
        &self.module
    }

    #[must_use]
    pub fn requirement(&self) -> &str {
        &self.requirement
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct LockedPackage {
    name: String,
    version: String,
    package_id: NativeLatticeId,
    requested_by: Vec<RequestedBy>,
}

impl LockedPackage {
    pub fn new(
        name: impl Into<String>,
        version: impl Into<String>,
        package_id: NativeLatticeId,
        mut requested_by: Vec<RequestedBy>,
    ) -> Result<Self, SchemaError> {
        let name = normalize(name.into());
        validate_package_name(&name)?;
        let version = version.into();
        validate_version(&version)?;
        if package_id.kind != ArtifactKind::Package {
            return Err(schema_invalid("locked package_id must have package kind"));
        }
        requested_by.sort_by(|left, right| {
            left.module
                .as_bytes()
                .cmp(right.module.as_bytes())
                .then_with(|| {
                    left.requirement
                        .as_bytes()
                        .cmp(right.requirement.as_bytes())
                })
        });
        Ok(Self {
            name,
            version,
            package_id,
            requested_by,
        })
    }

    #[must_use]
    pub fn name(&self) -> &str {
        &self.name
    }

    #[must_use]
    pub fn version(&self) -> &str {
        &self.version
    }

    #[must_use]
    pub fn package_id(&self) -> &NativeLatticeId {
        &self.package_id
    }

    #[must_use]
    pub fn requested_by(&self) -> &[RequestedBy] {
        &self.requested_by
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct LockfileBody {
    root_blueprint_digest: NativeLatticeId,
    packages: Vec<LockedPackage>,
}

impl LockfileBody {
    pub fn new(
        root_blueprint_digest: NativeLatticeId,
        mut packages: Vec<LockedPackage>,
    ) -> Result<Self, SchemaError> {
        if root_blueprint_digest.kind != ArtifactKind::Blueprint {
            return Err(schema_invalid(
                "root_blueprint_digest must have blueprint kind",
            ));
        }
        packages.sort_by(|left, right| left.name.as_bytes().cmp(right.name.as_bytes()));
        for pair in packages.windows(2) {
            if pair[0].name == pair[1].name {
                return Err(schema_invalid("Lockfile package names must be unique"));
            }
        }
        Ok(Self {
            root_blueprint_digest,
            packages,
        })
    }

    #[must_use]
    pub const fn lock_version(&self) -> u8 {
        1
    }

    #[must_use]
    pub const fn lattice(&self) -> &'static str {
        LATTICE_VERSION
    }

    #[must_use]
    pub const fn profile(&self) -> &'static str {
        CORE_PROFILE
    }

    #[must_use]
    pub fn root_blueprint_digest(&self) -> &NativeLatticeId {
        &self.root_blueprint_digest
    }

    #[must_use]
    pub fn packages(&self) -> &[LockedPackage] {
        &self.packages
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum DiagnosticPhase {
    Parse,
    Schema,
    Identity,
    Semantic,
    Migration,
}

impl DiagnosticPhase {
    const fn priority(self) -> u8 {
        match self {
            Self::Parse => 0,
            Self::Schema => 1,
            Self::Identity => 2,
            Self::Semantic => 3,
            Self::Migration => 4,
        }
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct MigrationDiagnostic {
    phase: DiagnosticPhase,
    code: String,
    path: String,
    message_digest: Sha256Digest,
}

impl MigrationDiagnostic {
    pub fn new(
        phase: DiagnosticPhase,
        code: impl Into<String>,
        path: impl Into<String>,
        message_digest: Sha256Digest,
    ) -> Result<Self, SchemaError> {
        let code = normalize(code.into());
        let path = normalize(path.into());
        if code.is_empty() || path.is_empty() {
            return Err(schema_invalid(
                "migration diagnostic code and path are required",
            ));
        }
        Ok(Self {
            phase,
            code,
            path,
            message_digest,
        })
    }

    #[must_use]
    pub fn code(&self) -> &str {
        &self.code
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum MigrationOutcome {
    Equivalent,
    Converted,
    Rejected,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum RequiredNextAction {
    NativeValidation,
    NativeCompilation,
    NativeQualification,
    NativeBinding,
    ManualResolution,
    None,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum AuthorityEffect {
    None,
}

/// Inputs to the F2 logical migration-receipt schema.
///
/// This type does not import or verify legacy bytes. The F3 migration seam must
/// establish that evidence before constructing a receipt.
#[derive(Clone, Debug)]
pub struct MigrationReceiptInput {
    pub source_artifact_kind: ArtifactKind,
    pub source_artifact_bytes_sha256: Sha256Digest,
    pub claimed_legacy_id: Option<LegacyLatticeId>,
    pub native_id: Option<NativeLatticeId>,
    pub native_canonical_sha256: Option<Sha256Digest>,
    pub outcome: MigrationOutcome,
    pub diagnostics: Vec<MigrationDiagnostic>,
    pub required_next_action: RequiredNextAction,
}

/// A deterministic, non-authoritative relationship record between legacy and
/// native identity claims.
///
/// F2 validates the logical field relationships only. The serialized receipt
/// is not a ThreadSmith identity, and F3 remains responsible for import,
/// recomputation, native validation, and evidence provenance.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct MigrationReceipt {
    receipt_version: u8,
    conversion_profile: &'static str,
    source_format: &'static str,
    source_wheel_sha256: Sha256Digest,
    source_artifact_kind: ArtifactKind,
    source_artifact_bytes_sha256: Sha256Digest,
    claimed_legacy_id: Option<LegacyLatticeId>,
    lattice_version: &'static str,
    semantic_profile: &'static str,
    native_schema_profile: &'static str,
    native_id: Option<NativeLatticeId>,
    native_canonical_sha256: Option<Sha256Digest>,
    outcome: MigrationOutcome,
    diagnostics: Vec<MigrationDiagnostic>,
    authority_effect: AuthorityEffect,
    required_next_action: RequiredNextAction,
}

impl MigrationReceipt {
    pub fn new(mut input: MigrationReceiptInput) -> Result<Self, SchemaError> {
        if let Some(claimed) = &input.claimed_legacy_id
            && claimed.standard_kind() != Some(input.source_artifact_kind)
            && input.outcome != MigrationOutcome::Rejected
        {
            return Err(migration_rejected(
                "legacy identity kind does not match source_artifact_kind",
            ));
        }
        match input.outcome {
            MigrationOutcome::Equivalent => {
                let claimed = input.claimed_legacy_id.as_ref().ok_or_else(|| {
                    migration_rejected("equivalent receipt requires a claimed legacy identity")
                })?;
                let native = input.native_id.as_ref().ok_or_else(|| {
                    migration_rejected("equivalent receipt requires a native identity")
                })?;
                let canonical_digest = input.native_canonical_sha256.ok_or_else(|| {
                    migration_rejected("equivalent receipt requires native canonical digest")
                })?;
                if !native.matches_legacy_claim(claimed) || native.digest != canonical_digest {
                    return Err(migration_rejected(
                        "equivalent receipt requires identical verified legacy/native identity",
                    ));
                }
            }
            MigrationOutcome::Converted => {
                let native = input.native_id.as_ref().ok_or_else(|| {
                    migration_rejected("converted receipt requires a native identity")
                })?;
                let canonical_digest = input.native_canonical_sha256.ok_or_else(|| {
                    migration_rejected("converted receipt requires native canonical digest")
                })?;
                if native.digest != canonical_digest {
                    return Err(migration_rejected(
                        "native identity must match native canonical digest",
                    ));
                }
                if native.kind != input.source_artifact_kind {
                    return Err(migration_rejected(
                        "native identity kind must match source_artifact_kind",
                    ));
                }
                if input
                    .claimed_legacy_id
                    .as_ref()
                    .is_some_and(|legacy| native.matches_legacy_claim(legacy))
                {
                    return Err(migration_rejected(
                        "converted receipt must not alias an equivalent identity",
                    ));
                }
                if input.diagnostics.is_empty() {
                    return Err(migration_rejected(
                        "converted receipt must record at least one diagnostic",
                    ));
                }
            }
            MigrationOutcome::Rejected => {
                if input.native_id.is_some() || input.native_canonical_sha256.is_some() {
                    return Err(migration_rejected(
                        "rejected receipt cannot admit a native identity",
                    ));
                }
                if input.diagnostics.is_empty() {
                    return Err(migration_rejected(
                        "rejected receipt must record at least one diagnostic",
                    ));
                }
            }
        }
        input.diagnostics.sort_by(|left, right| {
            left.phase
                .priority()
                .cmp(&right.phase.priority())
                .then_with(|| left.path.as_bytes().cmp(right.path.as_bytes()))
                .then_with(|| left.code.as_bytes().cmp(right.code.as_bytes()))
                .then_with(|| left.message_digest.cmp(&right.message_digest))
        });
        Ok(Self {
            receipt_version: 1,
            conversion_profile: MIGRATION_PROFILE,
            source_format: "lattice-reference-0.1.0",
            source_wheel_sha256: REFERENCE_WHEEL_SHA256.parse()?,
            source_artifact_kind: input.source_artifact_kind,
            source_artifact_bytes_sha256: input.source_artifact_bytes_sha256,
            claimed_legacy_id: input.claimed_legacy_id,
            lattice_version: LATTICE_VERSION,
            semantic_profile: CORE_PROFILE,
            native_schema_profile: NATIVE_SCHEMA_PROFILE,
            native_id: input.native_id,
            native_canonical_sha256: input.native_canonical_sha256,
            outcome: input.outcome,
            diagnostics: input.diagnostics,
            authority_effect: AuthorityEffect::None,
            required_next_action: input.required_next_action,
        })
    }

    #[must_use]
    pub const fn outcome(&self) -> MigrationOutcome {
        self.outcome
    }

    #[must_use]
    pub const fn authority_effect(&self) -> AuthorityEffect {
        self.authority_effect
    }

    #[must_use]
    pub fn native_id(&self) -> Option<&NativeLatticeId> {
        self.native_id.as_ref()
    }

    #[must_use]
    pub fn claimed_legacy_id(&self) -> Option<&LegacyLatticeId> {
        self.claimed_legacy_id.as_ref()
    }

    #[must_use]
    pub fn diagnostics(&self) -> &[MigrationDiagnostic] {
        &self.diagnostics
    }
}

fn normalize(value: String) -> String {
    value.nfc().collect()
}

fn schema_invalid(message: impl Into<String>) -> SchemaError {
    SchemaError::new(error_code::SCHEMA_INVALID, message)
}

fn migration_rejected(message: impl Into<String>) -> SchemaError {
    SchemaError::new(error_code::LEGACY_MIGRATION_REJECTED, message)
}

fn validate_package_name(value: &str) -> Result<(), SchemaError> {
    let mut previous_separator = false;
    for (index, byte) in value.bytes().enumerate() {
        let separator = matches!(byte, b'.' | b'_' | b'-');
        let valid = if index == 0 {
            byte.is_ascii_lowercase()
        } else {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || separator
        };
        if !valid || (separator && previous_separator) {
            return Err(schema_invalid(format!("invalid package name {value:?}")));
        }
        previous_separator = separator;
    }
    if value.is_empty() || previous_separator {
        return Err(schema_invalid(format!("invalid package name {value:?}")));
    }
    Ok(())
}

fn validate_local_name(value: &str) -> Result<(), SchemaError> {
    let mut previous_separator = false;
    for (index, byte) in value.bytes().enumerate() {
        let separator = byte == b'_';
        let valid = if index == 0 {
            byte.is_ascii_lowercase()
        } else {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || separator
        };
        if !valid || (separator && previous_separator) {
            return Err(schema_invalid(format!("invalid local name {value:?}")));
        }
        previous_separator = separator;
    }
    if value.is_empty() || previous_separator {
        return Err(schema_invalid(format!("invalid local name {value:?}")));
    }
    Ok(())
}

fn validate_version(value: &str) -> Result<(), SchemaError> {
    let parts: Vec<&str> = value.split('.').collect();
    if parts.len() != 3 || parts.iter().any(|part| !valid_version_component(part)) {
        return Err(schema_invalid(format!("invalid Core version {value:?}")));
    }
    Ok(())
}

fn validate_version_requirement(value: &str) -> Result<(), SchemaError> {
    let version = value.strip_prefix('^').unwrap_or(value);
    validate_version(version)
}

fn valid_version_component(value: &str) -> bool {
    !value.is_empty()
        && value.bytes().all(|byte| byte.is_ascii_digit())
        && (value == "0" || !value.starts_with('0'))
}

fn validate_relative_file_path(value: &str) -> Result<(), SchemaError> {
    if value.is_empty()
        || value.starts_with('/')
        || value.ends_with('/')
        || value.contains('\\')
        || value
            .split('/')
            .any(|part| part.is_empty() || part == "." || part == "..")
    {
        return Err(schema_invalid(format!(
            "invalid package file path {value:?}"
        )));
    }
    Ok(())
}

const fn hex_value(byte: u8) -> Option<u8> {
    match byte {
        b'0'..=b'9' => Some(byte - b'0'),
        b'a'..=b'f' => Some(byte - b'a' + 10),
        _ => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn digest(value: u8) -> Sha256Digest {
        Sha256Digest::from_bytes([value; 32])
    }

    #[test]
    fn native_and_legacy_ids_are_distinct_but_receipt_comparable() {
        let native = NativeLatticeId::from_canonical_digest(ArtifactKind::Package, digest(1));
        let legacy: LegacyLatticeId = native.to_string().parse().unwrap();
        assert!(native.matches_legacy_claim(&legacy));
        assert_eq!(
            legacy.reject_as_authority().code(),
            error_code::LEGACY_AUTHORITY_FORBIDDEN
        );
    }

    #[test]
    fn unknown_legacy_kind_is_representable_but_not_native() {
        let legacy: LegacyLatticeId = format!("lattice:profile:sha256:{}", digest(2))
            .parse()
            .unwrap();
        assert_eq!(legacy.standard_kind(), None);
        assert_eq!(
            "profile".parse::<ArtifactKind>().unwrap_err().code(),
            error_code::IDENTITY_KIND_UNSUPPORTED
        );
    }

    #[test]
    fn package_and_lock_collections_are_normalized() {
        let file_b = PackageFile::new("z.txt", digest(3)).unwrap();
        let file_a = PackageFile::new("module.yaml", digest(4)).unwrap();
        let descriptor = PackageDescriptor::new(
            "text_tools",
            "1.3.1",
            vec![CORE_PROFILE.to_owned()],
            "module.yaml",
            vec![file_b, file_a],
        )
        .unwrap();
        assert_eq!(descriptor.files()[0].path(), "module.yaml");
        assert_eq!(descriptor.files()[1].path(), "z.txt");

        let package_id = NativeLatticeId::from_canonical_digest(ArtifactKind::Package, digest(5));
        let requested = vec![
            RequestedBy::new("zeta", "^1.0.0").unwrap(),
            RequestedBy::new("alpha", "1.0.0").unwrap(),
        ];
        let locked = LockedPackage::new("text_tools", "1.3.1", package_id, requested).unwrap();
        assert_eq!(locked.requested_by()[0].module(), "alpha");
        let blueprint = NativeLatticeId::from_canonical_digest(ArtifactKind::Blueprint, digest(6));
        assert!(LockfileBody::new(blueprint, vec![locked]).is_ok());

        let module = PackageFile::new("module.yaml", digest(9)).unwrap();
        assert_eq!(
            PackageDescriptor::new(
                "text_tools",
                "1.3.1",
                vec!["lattice-extended-0.1".to_owned()],
                "module.yaml",
                vec![module],
            )
            .unwrap_err()
            .code(),
            error_code::SCHEMA_INVALID
        );
    }

    #[test]
    fn receipt_outcomes_do_not_alias_legacy_authority() {
        let native = NativeLatticeId::from_canonical_digest(ArtifactKind::Package, digest(7));
        let legacy: LegacyLatticeId = native.to_string().parse().unwrap();
        let receipt = MigrationReceipt::new(MigrationReceiptInput {
            source_artifact_kind: ArtifactKind::Package,
            source_artifact_bytes_sha256: digest(8),
            claimed_legacy_id: Some(legacy),
            native_id: Some(native),
            native_canonical_sha256: Some(digest(7)),
            outcome: MigrationOutcome::Equivalent,
            diagnostics: vec![],
            required_next_action: RequiredNextAction::NativeQualification,
        })
        .unwrap();
        assert_eq!(receipt.authority_effect(), AuthorityEffect::None);
        assert_eq!(receipt.outcome(), MigrationOutcome::Equivalent);
    }

    #[test]
    fn converted_and_rejected_receipts_require_diagnostics() {
        let native = NativeLatticeId::from_canonical_digest(ArtifactKind::Package, digest(10));
        let converted = MigrationReceipt::new(MigrationReceiptInput {
            source_artifact_kind: ArtifactKind::Package,
            source_artifact_bytes_sha256: digest(11),
            claimed_legacy_id: None,
            native_id: Some(native),
            native_canonical_sha256: Some(digest(10)),
            outcome: MigrationOutcome::Converted,
            diagnostics: vec![],
            required_next_action: RequiredNextAction::NativeValidation,
        });
        assert_eq!(
            converted.unwrap_err().code(),
            error_code::LEGACY_MIGRATION_REJECTED
        );

        let rejected = MigrationReceipt::new(MigrationReceiptInput {
            source_artifact_kind: ArtifactKind::Package,
            source_artifact_bytes_sha256: digest(12),
            claimed_legacy_id: None,
            native_id: None,
            native_canonical_sha256: None,
            outcome: MigrationOutcome::Rejected,
            diagnostics: vec![],
            required_next_action: RequiredNextAction::ManualResolution,
        });
        assert_eq!(
            rejected.unwrap_err().code(),
            error_code::LEGACY_MIGRATION_REJECTED
        );
    }
}
