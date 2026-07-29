use crate::ResolvedSource;
use core::fmt;
use serde_json::{Map, Number, Value};
use threadsmith_canonical::{canonical_bytes, sha256_digest};
use threadsmith_schema::{ArtifactKind, LATTICE_VERSION, NativeLatticeId};
pub use threadsmith_schema::{LockedPackage, RequestedBy};

/// Opaque PC8-produced Lock identity.
///
/// A caller-created generic native identity claim cannot be promoted into this
/// phase-produced proof:
///
/// ```compile_fail
/// use threadsmith_compiler::LockIdentity;
/// use threadsmith_schema::{ArtifactKind, NativeLatticeId, Sha256Digest};
/// let generic = NativeLatticeId::from_canonical_digest(
///     ArtifactKind::Lock,
///     Sha256Digest::from_bytes([0; 32]),
/// );
/// let _: LockIdentity = generic.into();
/// ```
#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct LockIdentity {
    identity: NativeLatticeId,
}

impl LockIdentity {
    /// Borrow the accepted native textual identity representation.
    #[must_use]
    pub const fn as_native_id(&self) -> &NativeLatticeId {
        &self.identity
    }
}

impl fmt::Display for LockIdentity {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Display::fmt(&self.identity, formatter)
    }
}

/// The complete canonical six-member PC8 Lockfile value.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct Lockfile {
    lock_version: u8,
    lattice: &'static str,
    profile: String,
    root_blueprint_digest: NativeLatticeId,
    packages: Vec<LockedPackage>,
    lock_id: LockIdentity,
}

impl Lockfile {
    #[must_use]
    pub const fn lock_version(&self) -> u8 {
        self.lock_version
    }

    #[must_use]
    pub const fn lattice(&self) -> &'static str {
        self.lattice
    }

    #[must_use]
    pub fn profile(&self) -> &str {
        &self.profile
    }

    #[must_use]
    pub const fn root_blueprint_digest(&self) -> &NativeLatticeId {
        &self.root_blueprint_digest
    }

    #[must_use]
    pub fn packages(&self) -> &[LockedPackage] {
        &self.packages
    }

    #[must_use]
    pub const fn lock_id(&self) -> &LockIdentity {
        &self.lock_id
    }
}

/// The sole canonical artifact created by one PC8 Lock operation.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct CreatedLockArtifact {
    lockfile: Lockfile,
}

impl CreatedLockArtifact {
    #[must_use]
    pub const fn lockfile(&self) -> &Lockfile {
        &self.lockfile
    }
}

/// PC8's frozen lack of authority transfer.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum LockAuthority {
    None,
}

impl LockAuthority {
    #[must_use]
    pub const fn as_str(self) -> &'static str {
        match self {
            Self::None => "none",
        }
    }
}

/// PC8's frozen non-authoritative phase observation.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum LockPhaseStatus {
    NonAuthoritativeLockedSource,
}

impl LockPhaseStatus {
    #[must_use]
    pub const fn as_str(self) -> &'static str {
        match self {
            Self::NonAuthoritativeLockedSource => "non_authoritative_locked_source",
        }
    }
}

/// Non-authoritative PC8 output bound to the exact consumed PC7 source.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct LockedSource {
    resolved_source: ResolvedSource,
    lockfile: Lockfile,
    canonical_lockfile_bytes: Vec<u8>,
    lock_id: LockIdentity,
    created_identities: Vec<LockIdentity>,
    created_artifacts: Vec<CreatedLockArtifact>,
    authority: LockAuthority,
    phase_status: LockPhaseStatus,
}

impl LockedSource {
    #[must_use]
    pub const fn resolved_source(&self) -> &ResolvedSource {
        &self.resolved_source
    }

    #[must_use]
    pub const fn lockfile(&self) -> &Lockfile {
        &self.lockfile
    }

    #[must_use]
    pub fn canonical_lockfile_bytes(&self) -> &[u8] {
        &self.canonical_lockfile_bytes
    }

    #[must_use]
    pub const fn lock_id(&self) -> &LockIdentity {
        &self.lock_id
    }

    #[must_use]
    pub fn created_identities(&self) -> &[LockIdentity] {
        &self.created_identities
    }

    #[must_use]
    pub fn created_artifacts(&self) -> &[CreatedLockArtifact] {
        &self.created_artifacts
    }

    #[must_use]
    pub const fn authority(&self) -> LockAuthority {
        self.authority
    }

    #[must_use]
    pub const fn phase_status(&self) -> LockPhaseStatus {
        self.phase_status
    }

    /// The source-bound result creates no wrapper identity.
    #[must_use]
    pub const fn wrapper_identity(&self) -> Option<&NativeLatticeId> {
        None
    }

    #[must_use]
    pub fn into_resolved_source(self) -> ResolvedSource {
        self.resolved_source
    }
}

/// Project one exact accepted PC7 source into its deterministic PC8 Lock
/// artifact without filesystem, environment, network, clock, randomness, or
/// persistence access.
#[must_use]
pub fn lock_source(resolved_source: ResolvedSource) -> LockedSource {
    let profile = resolved_source.active_profile().to_owned();
    let root_blueprint_digest = resolved_source
        .scanned_source()
        .digested_source()
        .blueprint_digest()
        .as_native_id()
        .clone();
    let projection = resolved_source.semantic_projection();
    let selected_packages = projection
        .get("selected_packages")
        .and_then(Value::as_array)
        .expect("ResolvedSource always retains selected_packages");
    let applicable_requirements = projection
        .get("applicable_requirements")
        .and_then(Value::as_array)
        .expect("ResolvedSource always retains applicable_requirements");

    let mut packages = Vec::with_capacity(selected_packages.len());
    for selected in selected_packages {
        let name = member_string(selected, "name");
        let version = member_string(selected, "version");
        let selected_package_id = member_string(selected, "package_id");
        let selected_record = resolved_source
            .scanned_source()
            .packages()
            .iter()
            .find(|package| package.identity().to_string() == selected_package_id)
            .expect("each selected package is an exact retained PC6 record");
        assert_eq!(
            selected_record.descriptor().package(),
            name,
            "selected package name must match its retained PC6 record"
        );
        assert_eq!(
            selected_record.descriptor().version(),
            version,
            "selected package version must match its retained PC6 record"
        );

        let requested_by = applicable_requirements
            .iter()
            .filter(|requirement| member_string(requirement, "package") == name)
            .map(|requirement| {
                let contributor = requirement
                    .get("contributor")
                    .expect("applicable requirement retains contributor");
                let module = match member_string(contributor, "kind") {
                    "root" => member_string(contributor, "module"),
                    "package" => member_string(contributor, "package"),
                    _ => unreachable!("ResolvedSource contributor kind is closed"),
                };
                RequestedBy::new(module, member_string(requirement, "constraint"))
                    .expect("ResolvedSource requested_by projection remains schema-valid")
            })
            .collect();
        packages.push(
            LockedPackage::new(
                name,
                version,
                selected_record.identity().as_native_id().clone(),
                requested_by,
            )
            .expect("ResolvedSource package projection remains schema-valid"),
        );
    }
    packages.sort_by(|left, right| left.name().as_bytes().cmp(right.name().as_bytes()));

    let preimage = lockfile_value(
        1,
        LATTICE_VERSION,
        &profile,
        &root_blueprint_digest,
        &packages,
        None,
    );
    let preimage_bytes =
        canonical_bytes(&preimage).expect("ResolvedSource Lock preimage is canonicalizable");
    let lock_id = LockIdentity {
        identity: NativeLatticeId::from_canonical_digest(
            ArtifactKind::Lock,
            sha256_digest(&preimage_bytes),
        ),
    };
    let lockfile = Lockfile {
        lock_version: 1,
        lattice: LATTICE_VERSION,
        profile,
        root_blueprint_digest,
        packages,
        lock_id: lock_id.clone(),
    };
    let emitted_value = lockfile_value(
        lockfile.lock_version,
        lockfile.lattice,
        &lockfile.profile,
        &lockfile.root_blueprint_digest,
        &lockfile.packages,
        Some(&lock_id),
    );
    let canonical_lockfile_bytes =
        canonical_bytes(&emitted_value).expect("complete Lockfile is canonicalizable");

    LockedSource {
        resolved_source,
        lockfile: lockfile.clone(),
        canonical_lockfile_bytes,
        lock_id: lock_id.clone(),
        created_identities: vec![lock_id],
        created_artifacts: vec![CreatedLockArtifact { lockfile }],
        authority: LockAuthority::None,
        phase_status: LockPhaseStatus::NonAuthoritativeLockedSource,
    }
}

fn member_string<'a>(value: &'a Value, member: &str) -> &'a str {
    value
        .get(member)
        .and_then(Value::as_str)
        .expect("ResolvedSource semantic member is a string")
}

fn lockfile_value(
    lock_version: u8,
    lattice: &str,
    profile: &str,
    root_blueprint_digest: &NativeLatticeId,
    packages: &[LockedPackage],
    lock_id: Option<&LockIdentity>,
) -> Value {
    let package_values = packages
        .iter()
        .map(|package| {
            let requested_by = package
                .requested_by()
                .iter()
                .map(|request| {
                    object([
                        ("module", Value::String(request.module().to_owned())),
                        (
                            "requirement",
                            Value::String(request.requirement().to_owned()),
                        ),
                    ])
                })
                .collect();
            object([
                ("name", Value::String(package.name().to_owned())),
                ("version", Value::String(package.version().to_owned())),
                (
                    "package_id",
                    Value::String(package.package_id().to_string()),
                ),
                ("requested_by", Value::Array(requested_by)),
            ])
        })
        .collect();
    let mut value = Map::new();
    value.insert(
        "lock_version".to_owned(),
        Value::Number(Number::from(lock_version)),
    );
    value.insert("lattice".to_owned(), Value::String(lattice.to_owned()));
    value.insert("profile".to_owned(), Value::String(profile.to_owned()));
    value.insert(
        "root_blueprint_digest".to_owned(),
        Value::String(root_blueprint_digest.to_string()),
    );
    value.insert("packages".to_owned(), Value::Array(package_values));
    if let Some(lock_id) = lock_id {
        value.insert("lock_id".to_owned(), Value::String(lock_id.to_string()));
    }
    Value::Object(value)
}

fn object<const N: usize>(entries: [(&str, Value); N]) -> Value {
    Value::Object(
        entries
            .into_iter()
            .map(|(key, value)| (key.to_owned(), value))
            .collect(),
    )
}
