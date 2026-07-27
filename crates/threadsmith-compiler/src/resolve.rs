use crate::{ScannedPackage, ScannedSource, SourceDiagnostic, parse_blueprint_source};
use core::cmp::Ordering;
use core::fmt;
use serde::Serialize;
use serde_json::{Map, Number, Value};
use std::collections::{BTreeMap, BTreeSet};
use std::sync::Arc;
use threadsmith_canonical::{canonical_bytes, canonical_sha256, sha256_digest};
use unicode_normalization::UnicodeNormalization;

/// Stable PC7 Resolve diagnostic codes.
pub mod resolve_diagnostic_codes {
    pub const DUPLICATE_VERSION: &str = "RESOLVE_DUPLICATE_VERSION";
    pub const IMPORT_INVALID: &str = "RESOLVE_IMPORT_INVALID";
    pub const CONSTRAINT_INVALID: &str = "RESOLVE_CONSTRAINT_INVALID";
    pub const IMPORT_ALIAS_CONFLICT: &str = "RESOLVE_IMPORT_ALIAS_CONFLICT";
    pub const LOCK_SOURCE_INVALID: &str = "RESOLVE_LOCK_SOURCE_INVALID";
    pub const LOCK_SCHEMA_INVALID: &str = "RESOLVE_LOCK_SCHEMA_INVALID";
    pub const LOCK_ID_MISMATCH: &str = "RESOLVE_LOCK_ID_MISMATCH";
    pub const LOCK_CONTEXT_MISMATCH: &str = "RESOLVE_LOCK_CONTEXT_MISMATCH";
    pub const PACKAGE_NOT_FOUND: &str = "RESOLVE_PACKAGE_NOT_FOUND";
    pub const PROFILE_INCOMPATIBLE: &str = "RESOLVE_PROFILE_INCOMPATIBLE";
    pub const NO_COMMON_VERSION: &str = "RESOLVE_NO_COMMON_VERSION";
    pub const MODULE_SOURCE_INVALID: &str = "RESOLVE_MODULE_SOURCE_INVALID";
    pub const MODULE_YAML_FORBIDDEN: &str = "RESOLVE_MODULE_YAML_FORBIDDEN";
    pub const MODULE_SCALAR_INVALID: &str = "RESOLVE_MODULE_SCALAR_INVALID";
    pub const MODULE_NON_STRING_KEY: &str = "RESOLVE_MODULE_NON_STRING_KEY";
    pub const MODULE_DUPLICATE_KEY: &str = "RESOLVE_MODULE_DUPLICATE_KEY";
    pub const MODULE_NFC_COLLISION: &str = "RESOLVE_MODULE_NFC_COLLISION";
    pub const MODULE_ENVELOPE_INVALID: &str = "RESOLVE_MODULE_ENVELOPE_INVALID";
    pub const MODULE_METADATA_MISMATCH: &str = "RESOLVE_MODULE_METADATA_MISMATCH";
    pub const PASS_LIMIT: &str = "RESOLVE_PASS_LIMIT";
    pub const IMPORT_CYCLE: &str = "RESOLVE_IMPORT_CYCLE";
}

const DIAGNOSTIC_CODES: [&str; 21] = [
    resolve_diagnostic_codes::DUPLICATE_VERSION,
    resolve_diagnostic_codes::IMPORT_INVALID,
    resolve_diagnostic_codes::CONSTRAINT_INVALID,
    resolve_diagnostic_codes::IMPORT_ALIAS_CONFLICT,
    resolve_diagnostic_codes::LOCK_SOURCE_INVALID,
    resolve_diagnostic_codes::LOCK_SCHEMA_INVALID,
    resolve_diagnostic_codes::LOCK_ID_MISMATCH,
    resolve_diagnostic_codes::LOCK_CONTEXT_MISMATCH,
    resolve_diagnostic_codes::PACKAGE_NOT_FOUND,
    resolve_diagnostic_codes::PROFILE_INCOMPATIBLE,
    resolve_diagnostic_codes::NO_COMMON_VERSION,
    resolve_diagnostic_codes::MODULE_SOURCE_INVALID,
    resolve_diagnostic_codes::MODULE_YAML_FORBIDDEN,
    resolve_diagnostic_codes::MODULE_SCALAR_INVALID,
    resolve_diagnostic_codes::MODULE_NON_STRING_KEY,
    resolve_diagnostic_codes::MODULE_DUPLICATE_KEY,
    resolve_diagnostic_codes::MODULE_NFC_COLLISION,
    resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
    resolve_diagnostic_codes::MODULE_METADATA_MISMATCH,
    resolve_diagnostic_codes::PASS_LIMIT,
    resolve_diagnostic_codes::IMPORT_CYCLE,
];

#[must_use]
pub const fn resolve_diagnostic_codes() -> &'static [&'static str] {
    &DIAGNOSTIC_CODES
}

/// Optional immutable existing-Lockfile input. It is bytes, never a path.
#[derive(Clone, Debug, Eq, PartialEq)]
pub enum ExistingLockfileInput {
    Absent,
    Bytes(Arc<[u8]>),
}

impl ExistingLockfileInput {
    #[must_use]
    pub const fn absent() -> Self {
        Self::Absent
    }

    #[must_use]
    pub fn from_bytes(bytes: impl Into<Arc<[u8]>>) -> Self {
        Self::Bytes(bytes.into())
    }

    #[must_use]
    pub fn bytes(&self) -> Option<&[u8]> {
        match self {
            Self::Absent => None,
            Self::Bytes(bytes) => Some(bytes.as_ref()),
        }
    }
}

/// The optional structured detail carried only by `RESOLVE_IMPORT_CYCLE`.
#[derive(Clone, Debug, Eq, PartialEq, Serialize)]
pub struct ResolveCycleEdge {
    alias: String,
    from: String,
    source_path: String,
    to: String,
}

impl ResolveCycleEdge {
    #[must_use]
    pub fn alias(&self) -> &str {
        &self.alias
    }

    #[must_use]
    pub fn from(&self) -> &str {
        &self.from
    }

    #[must_use]
    pub fn source_path(&self) -> &str {
        &self.source_path
    }

    #[must_use]
    pub fn to(&self) -> &str {
        &self.to
    }
}

/// One deterministic PC7 primary diagnostic.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ResolveDiagnostic {
    code: &'static str,
    path: String,
    canonical_cycle: Option<Vec<ResolveCycleEdge>>,
}

impl ResolveDiagnostic {
    #[must_use]
    pub const fn code(&self) -> &'static str {
        self.code
    }

    #[must_use]
    pub fn path(&self) -> &str {
        &self.path
    }

    #[must_use]
    pub fn canonical_cycle(&self) -> Option<&[ResolveCycleEdge]> {
        self.canonical_cycle.as_deref()
    }
}

impl fmt::Display for ResolveDiagnostic {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{} at {}", self.code, self.path)
    }
}

impl std::error::Error for ResolveDiagnostic {}

/// Non-authoritative PC7 output bound to the exact consumed PC6 source.
///
/// The semantic projection is provided for deterministic later-phase intake
/// and conformance comparison. It creates no identity or authority.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ResolvedSource {
    scanned_source: ScannedSource,
    semantic_projection: Value,
}

impl ResolvedSource {
    #[must_use]
    pub const fn scanned_source(&self) -> &ScannedSource {
        &self.scanned_source
    }

    #[must_use]
    pub fn active_profile(&self) -> &str {
        self.semantic_projection
            .get("active_profile")
            .and_then(Value::as_str)
            .expect("ResolvedSource always retains active_profile")
    }

    /// Borrow the complete immutable non-authoritative PC7 representation.
    #[must_use]
    pub const fn semantic_projection(&self) -> &Value {
        &self.semantic_projection
    }

    #[must_use]
    pub fn into_scanned_source(self) -> ScannedSource {
        self.scanned_source
    }
}

#[derive(Clone, Debug)]
struct DiagnosticCandidate {
    rank: u8,
    code: &'static str,
    path: String,
    canonical_cycle: Option<Vec<ResolveCycleEdge>>,
}

impl DiagnosticCandidate {
    fn plain(rank: u8, code: &'static str, path: String) -> Self {
        Self {
            rank,
            code,
            path,
            canonical_cycle: None,
        }
    }

    fn finish(self) -> ResolveDiagnostic {
        ResolveDiagnostic {
            code: self.code,
            path: self.path,
            canonical_cycle: self.canonical_cycle,
        }
    }
}

fn primary(mut candidates: Vec<DiagnosticCandidate>) -> Option<ResolveDiagnostic> {
    candidates.sort_by(|left, right| {
        left.rank
            .cmp(&right.rank)
            .then_with(|| left.path.as_bytes().cmp(right.path.as_bytes()))
    });
    candidates
        .into_iter()
        .next()
        .map(DiagnosticCandidate::finish)
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Version {
    text: String,
    components: [String; 3],
}

impl Version {
    fn parse(text: &str) -> Option<Self> {
        let mut parts = text.split('.');
        let major = parts.next()?;
        let minor = parts.next()?;
        let patch = parts.next()?;
        if parts.next().is_some()
            || !canonical_decimal(major)
            || !canonical_decimal(minor)
            || !canonical_decimal(patch)
        {
            return None;
        }
        Some(Self {
            text: text.to_owned(),
            components: [major.to_owned(), minor.to_owned(), patch.to_owned()],
        })
    }

    fn numeric_cmp(&self, other: &Self) -> Ordering {
        for (left, right) in self.components.iter().zip(&other.components) {
            let order = decimal_cmp(left, right);
            if order != Ordering::Equal {
                return order;
            }
        }
        Ordering::Equal
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
enum IntervalKind {
    Exact,
    Caret,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Interval {
    kind: IntervalKind,
    lower: Version,
    upper: Option<Version>,
}

impl Interval {
    fn admits(&self, version: &Version) -> bool {
        if self.kind == IntervalKind::Exact {
            return version.numeric_cmp(&self.lower) == Ordering::Equal;
        }
        version.numeric_cmp(&self.lower) != Ordering::Less
            && self
                .upper
                .as_ref()
                .is_none_or(|upper| version.numeric_cmp(upper) == Ordering::Less)
    }

    fn to_value(&self) -> Value {
        object([
            (
                "kind",
                Value::String(
                    match self.kind {
                        IntervalKind::Exact => "exact",
                        IntervalKind::Caret => "caret",
                    }
                    .to_owned(),
                ),
            ),
            ("lower_inclusive", Value::String(self.lower.text.clone())),
            (
                "upper_exclusive",
                self.upper
                    .as_ref()
                    .map_or(Value::Null, |version| Value::String(version.text.clone())),
            ),
        ])
    }
}

fn parse_constraint(text: &str) -> Option<Interval> {
    if let Some(version_text) = text.strip_prefix('^') {
        let lower = Version::parse(version_text)?;
        let mut upper_components = lower.components.clone();
        if upper_components[0] != "0" {
            upper_components[0] = increment_decimal(&upper_components[0]);
            upper_components[1] = "0".to_owned();
            upper_components[2] = "0".to_owned();
        } else if upper_components[1] != "0" {
            upper_components[1] = increment_decimal(&upper_components[1]);
            upper_components[2] = "0".to_owned();
        } else {
            upper_components[2] = increment_decimal(&upper_components[2]);
        }
        let upper_text = upper_components.join(".");
        Some(Interval {
            kind: IntervalKind::Caret,
            lower,
            upper: Version::parse(&upper_text),
        })
    } else {
        let lower = Version::parse(text)?;
        Some(Interval {
            kind: IntervalKind::Exact,
            lower,
            upper: None,
        })
    }
}

fn canonical_decimal(value: &str) -> bool {
    value == "0"
        || (value
            .as_bytes()
            .first()
            .is_some_and(|byte| matches!(byte, b'1'..=b'9'))
            && value.as_bytes().iter().all(u8::is_ascii_digit))
}

fn decimal_cmp(left: &str, right: &str) -> Ordering {
    left.len()
        .cmp(&right.len())
        .then_with(|| left.as_bytes().cmp(right.as_bytes()))
}

fn increment_decimal(value: &str) -> String {
    let mut bytes = value.as_bytes().to_vec();
    let mut carry = true;
    for byte in bytes.iter_mut().rev() {
        if !carry {
            break;
        }
        if *byte == b'9' {
            *byte = b'0';
        } else {
            *byte += 1;
            carry = false;
        }
    }
    if carry {
        bytes.insert(0, b'1');
    }
    String::from_utf8(bytes).expect("decimal increment remains ASCII")
}

#[derive(Clone, Debug)]
struct Import {
    package: String,
    constraint: String,
    alias: String,
    interval: Interval,
    source_path: String,
}

#[derive(Clone, Debug)]
enum Contributor {
    Root {
        module: String,
    },
    Package {
        package: String,
        version: Version,
        package_id: String,
    },
}

#[derive(Clone, Debug)]
struct Requirement {
    package: String,
    constraint: String,
    alias: String,
    interval: Interval,
    source_path: String,
    contributor: Contributor,
}

impl Requirement {
    fn to_value(&self) -> Value {
        let contributor = match &self.contributor {
            Contributor::Root { module } => object([
                ("kind", Value::String("root".to_owned())),
                ("module", Value::String(module.clone())),
            ]),
            Contributor::Package {
                package,
                version,
                package_id,
            } => object([
                ("kind", Value::String("package".to_owned())),
                ("package", Value::String(package.clone())),
                ("package_id", Value::String(package_id.clone())),
                ("version", Value::String(version.text.clone())),
            ]),
        };
        object([
            ("alias", Value::String(self.alias.clone())),
            ("constraint", Value::String(self.constraint.clone())),
            ("contributor", contributor),
            ("interval", self.interval.to_value()),
            ("package", Value::String(self.package.clone())),
            ("source_path", Value::String(self.source_path.clone())),
        ])
    }
}

#[derive(Clone, Debug)]
struct ParsedModule {
    package_index: usize,
    value: Value,
    imports: Vec<Import>,
    module_file: String,
    retained_bytes: Arc<[u8]>,
    retained_sha256: String,
    node: String,
}

#[derive(Clone, Debug)]
struct LockEntry {
    name: String,
    version: String,
    package_id: String,
}

#[derive(Clone, Debug)]
struct ParsedLock {
    bytes: Arc<[u8]>,
    input_sha256: String,
    entries: Vec<LockEntry>,
}

#[derive(Clone, Debug)]
struct SelectionDecision {
    package: String,
    status: &'static str,
    selected_by: &'static str,
    selected_version: String,
    selected_package_id: String,
    lock_entry: Option<(String, String)>,
}

impl SelectionDecision {
    fn to_value(&self) -> Value {
        object([
            (
                "lock_entry",
                self.lock_entry
                    .as_ref()
                    .map_or(Value::Null, |(version, id)| {
                        object([
                            ("package_id", Value::String(id.clone())),
                            ("version", Value::String(version.clone())),
                        ])
                    }),
            ),
            ("package", Value::String(self.package.clone())),
            ("selected_by", Value::String(self.selected_by.to_owned())),
            (
                "selected_package_id",
                Value::String(self.selected_package_id.clone()),
            ),
            (
                "selected_version",
                Value::String(self.selected_version.clone()),
            ),
            ("status", Value::String(self.status.to_owned())),
        ])
    }
}

type SelectionState = BTreeMap<String, usize>;

/// Resolve one exact PC6 source without filesystem, network, clock, locale, or
/// host capability access.
pub fn resolve_source(
    scanned_source: ScannedSource,
    existing_lockfile: ExistingLockfileInput,
) -> Result<ResolvedSource, ResolveDiagnostic> {
    let root = scanned_source
        .digested_source()
        .defaulted_source()
        .as_value();
    let root_object = root
        .as_object()
        .expect("PC6 retains a PC3-validated root object");
    let active_profile = root_object
        .get("profile")
        .and_then(Value::as_str)
        .expect("PC3 admitted a profile string")
        .to_owned();
    let root_module = root_object
        .get("module")
        .and_then(Value::as_str)
        .expect("PC3 admitted a module string")
        .to_owned();
    let blueprint_digest = scanned_source
        .digested_source()
        .blueprint_digest()
        .to_string();

    let candidate_groups = group_candidates(&scanned_source)?;

    let root_import_value = root_object
        .get("imports")
        .expect("PC4 inserts the root imports array");
    let root_imports = admit_imports(root_import_value, "root#")?;

    let parsed_lock = admit_lock(&existing_lockfile, &active_profile, &blueprint_digest)?;

    let mut parsed_modules: BTreeMap<String, ParsedModule> = BTreeMap::new();
    let mut state = SelectionState::new();
    let mut pass_values = Vec::new();
    let mut converged_requirements = Vec::new();
    let mut final_decisions = Vec::new();

    for pass in 1_u16..=256 {
        let requirements = collect_requirements(
            &root_imports,
            &root_module,
            &state,
            &parsed_modules,
            &scanned_source,
        );

        let (next_state, decisions) = select_next_state(
            &requirements,
            &candidate_groups,
            &scanned_source,
            parsed_lock.as_ref(),
            &active_profile,
        )?;

        let newly_required = next_state
            .values()
            .filter(|index| {
                let id = scanned_source.packages()[**index].identity().to_string();
                !parsed_modules.contains_key(&id)
            })
            .copied()
            .collect::<Vec<_>>();
        if !newly_required.is_empty() {
            let mut admitted = Vec::new();
            let mut candidates = Vec::new();
            for package_index in newly_required {
                match admit_selected_module(package_index, &scanned_source, &active_profile) {
                    Ok(module) => admitted.push(module),
                    Err(mut errors) => candidates.append(&mut errors),
                }
            }
            if let Some(diagnostic) = primary(candidates) {
                return Err(diagnostic);
            }
            for module in admitted {
                let id = scanned_source.packages()[module.package_index]
                    .identity()
                    .to_string();
                parsed_modules.insert(id, module);
            }
        }

        let unchanged = state_equal(&state, &next_state, &scanned_source);
        let changes = changes_value(&state, &next_state, &scanned_source);
        pass_values.push(object([
            (
                "active_requirements",
                Value::Array(requirements.iter().map(Requirement::to_value).collect()),
            ),
            ("changes", changes),
            ("input_selection", selection_value(&state, &scanned_source)),
            (
                "output_selection",
                selection_value(&next_state, &scanned_source),
            ),
            ("pass", Value::Number(Number::from(u64::from(pass)))),
            (
                "selection_decisions",
                Value::Array(decisions.iter().map(SelectionDecision::to_value).collect()),
            ),
            ("unchanged", Value::Bool(unchanged)),
        ]));

        if unchanged {
            state = next_state;
            converged_requirements = requirements;
            final_decisions = decisions;
            break;
        }

        if pass == 256 {
            return Err(ResolveDiagnostic {
                code: resolve_diagnostic_codes::PASS_LIMIT,
                path: "resolve#/passes/257".to_owned(),
                canonical_cycle: None,
            });
        }
        state = next_state;
    }

    let graph = build_graph(
        &root_module,
        &state,
        &converged_requirements,
        &scanned_source,
    );
    if let Some(cycle) = canonical_cycle(&converged_requirements) {
        let path = cycle[0].source_path.clone();
        return Err(ResolveDiagnostic {
            code: resolve_diagnostic_codes::IMPORT_CYCLE,
            path,
            canonical_cycle: Some(cycle),
        });
    }

    let semantic_projection = build_success_value(SuccessValueInputs {
        scanned: &scanned_source,
        active_profile: &active_profile,
        lock: parsed_lock.as_ref(),
        pass_values: &pass_values,
        state: &state,
        parsed_modules: &parsed_modules,
        requirements: &converged_requirements,
        graph: &graph,
        final_decisions: &final_decisions,
    });

    Ok(ResolvedSource {
        scanned_source,
        semantic_projection,
    })
}

fn group_candidates(
    scanned: &ScannedSource,
) -> Result<BTreeMap<String, Vec<usize>>, ResolveDiagnostic> {
    let mut exact_groups: BTreeMap<(String, String), Vec<usize>> = BTreeMap::new();
    for (index, package) in scanned.packages().iter().enumerate() {
        exact_groups
            .entry((
                package.descriptor().package().to_owned(),
                package.descriptor().version().to_owned(),
            ))
            .or_default()
            .push(index);
    }

    let mut duplicate_candidates = Vec::new();
    let mut collapsed = Vec::new();
    for ((name, version), indexes) in exact_groups {
        let first = indexes[0];
        if indexes
            .iter()
            .skip(1)
            .any(|index| scanned.packages()[*index] != scanned.packages()[first])
        {
            duplicate_candidates.push(DiagnosticCandidate::plain(
                1,
                resolve_diagnostic_codes::DUPLICATE_VERSION,
                format!(
                    "packages/{}/{}",
                    encode_component(&name),
                    encode_component(&version)
                ),
            ));
        } else {
            collapsed.push(first);
        }
    }
    if let Some(diagnostic) = primary(duplicate_candidates) {
        return Err(diagnostic);
    }

    let mut groups: BTreeMap<String, Vec<usize>> = BTreeMap::new();
    for index in collapsed {
        groups
            .entry(scanned.packages()[index].descriptor().package().to_owned())
            .or_default()
            .push(index);
    }
    for indexes in groups.values_mut() {
        indexes.sort_by(|left, right| {
            compare_version_text(
                scanned.packages()[*left].descriptor().version(),
                scanned.packages()[*right].descriptor().version(),
            )
        });
    }
    Ok(groups)
}

fn admit_imports(value: &Value, anchor: &str) -> Result<Vec<Import>, ResolveDiagnostic> {
    let Some(entries) = value.as_array() else {
        return Err(ResolveDiagnostic {
            code: resolve_diagnostic_codes::IMPORT_INVALID,
            path: anchor.to_owned(),
            canonical_cycle: None,
        });
    };
    let mut candidates = Vec::new();
    let mut admitted = Vec::new();
    let mut aliases = BTreeMap::<String, usize>::new();
    for (index, entry) in entries.iter().enumerate() {
        let base = format!("{anchor}/imports/{index}");
        let Some(object) = entry.as_object() else {
            candidates.push(DiagnosticCandidate::plain(
                2,
                resolve_diagnostic_codes::IMPORT_INVALID,
                base,
            ));
            continue;
        };

        for key in object
            .keys()
            .filter(|key| !matches!(key.as_str(), "use" | "version" | "as"))
        {
            candidates.push(DiagnosticCandidate::plain(
                2,
                resolve_diagnostic_codes::IMPORT_INVALID,
                format!("{base}/{}", encode_pointer_token(key)),
            ));
        }
        for field in ["use", "version", "as"] {
            if !object.contains_key(field) {
                candidates.push(DiagnosticCandidate::plain(
                    2,
                    resolve_diagnostic_codes::IMPORT_INVALID,
                    format!("{base}/{field}"),
                ));
            }
        }
        for field in ["use", "version", "as"] {
            if object.get(field).is_some_and(|value| !value.is_string()) {
                candidates.push(DiagnosticCandidate::plain(
                    2,
                    resolve_diagnostic_codes::IMPORT_INVALID,
                    format!("{base}/{field}"),
                ));
            }
        }

        let package = object.get("use").and_then(Value::as_str);
        let constraint = object.get("version").and_then(Value::as_str);
        let alias = object.get("as").and_then(Value::as_str);
        if package.is_some_and(|text| !package_name(text)) {
            candidates.push(DiagnosticCandidate::plain(
                2,
                resolve_diagnostic_codes::IMPORT_INVALID,
                format!("{base}/use"),
            ));
        }
        let interval = constraint.and_then(parse_constraint);
        if constraint.is_some() && interval.is_none() {
            candidates.push(DiagnosticCandidate::plain(
                3,
                resolve_diagnostic_codes::CONSTRAINT_INVALID,
                format!("{base}/version"),
            ));
        }
        let alias_valid = alias.is_some_and(local_name);
        if alias.is_some() && !alias_valid {
            candidates.push(DiagnosticCandidate::plain(
                2,
                resolve_diagnostic_codes::IMPORT_INVALID,
                format!("{base}/as"),
            ));
        }
        if let Some(alias) = alias.filter(|_| alias_valid)
            && aliases.insert(alias.to_owned(), index).is_some()
        {
            candidates.push(DiagnosticCandidate::plain(
                4,
                resolve_diagnostic_codes::IMPORT_ALIAS_CONFLICT,
                format!("{base}/as"),
            ));
        }

        if let (Some(package), Some(constraint), Some(alias), Some(interval)) =
            (package, constraint, alias, interval)
            && package_name(package)
            && alias_valid
        {
            admitted.push(Import {
                package: package.to_owned(),
                constraint: constraint.to_owned(),
                alias: alias.to_owned(),
                interval,
                source_path: base,
            });
        }
    }
    if let Some(diagnostic) = primary(candidates) {
        Err(diagnostic)
    } else {
        Ok(admitted)
    }
}

fn collect_requirements(
    root_imports: &[Import],
    root_module: &str,
    state: &SelectionState,
    parsed_modules: &BTreeMap<String, ParsedModule>,
    scanned: &ScannedSource,
) -> Vec<Requirement> {
    let mut requirements = root_imports
        .iter()
        .map(|import| Requirement {
            package: import.package.clone(),
            constraint: import.constraint.clone(),
            alias: import.alias.clone(),
            interval: import.interval.clone(),
            source_path: import.source_path.clone(),
            contributor: Contributor::Root {
                module: root_module.to_owned(),
            },
        })
        .collect::<Vec<_>>();

    let mut pending = root_imports
        .iter()
        .map(|import| import.package.clone())
        .collect::<BTreeSet<_>>();
    let mut visited = BTreeSet::new();
    while let Some(package_name) = pending.pop_first() {
        if !visited.insert(package_name.clone()) {
            continue;
        }
        let Some(index) = state.get(&package_name).copied() else {
            continue;
        };
        let package = &scanned.packages()[index];
        let package_id = package.identity().to_string();
        let Some(module) = parsed_modules.get(&package_id) else {
            continue;
        };
        let contributor = Contributor::Package {
            package: package_name,
            version: Version::parse(package.descriptor().version())
                .expect("PC6 admitted canonical versions"),
            package_id,
        };
        for import in &module.imports {
            pending.insert(import.package.clone());
            requirements.push(Requirement {
                package: import.package.clone(),
                constraint: import.constraint.clone(),
                alias: import.alias.clone(),
                interval: import.interval.clone(),
                source_path: import.source_path.clone(),
                contributor: contributor.clone(),
            });
        }
    }
    requirements.sort_by(requirement_cmp);
    requirements
}

fn requirement_cmp(left: &Requirement, right: &Requirement) -> Ordering {
    left.package
        .as_bytes()
        .cmp(right.package.as_bytes())
        .then_with(|| contributor_cmp(&left.contributor, &right.contributor))
        .then_with(|| left.interval.lower.numeric_cmp(&right.interval.lower))
        .then_with(|| match (&left.interval.upper, &right.interval.upper) {
            (None, None) => Ordering::Equal,
            (None, Some(_)) => Ordering::Less,
            (Some(_), None) => Ordering::Greater,
            (Some(left), Some(right)) => left.numeric_cmp(right),
        })
        .then_with(|| left.constraint.as_bytes().cmp(right.constraint.as_bytes()))
        .then_with(|| left.alias.as_bytes().cmp(right.alias.as_bytes()))
        .then_with(|| {
            left.source_path
                .as_bytes()
                .cmp(right.source_path.as_bytes())
        })
}

fn contributor_cmp(left: &Contributor, right: &Contributor) -> Ordering {
    match (left, right) {
        (Contributor::Root { module: left }, Contributor::Root { module: right }) => {
            left.as_bytes().cmp(right.as_bytes())
        }
        (Contributor::Root { .. }, Contributor::Package { .. }) => Ordering::Less,
        (Contributor::Package { .. }, Contributor::Root { .. }) => Ordering::Greater,
        (
            Contributor::Package {
                package: left_name,
                version: left_version,
                package_id: left_id,
            },
            Contributor::Package {
                package: right_name,
                version: right_version,
                package_id: right_id,
            },
        ) => left_name
            .as_bytes()
            .cmp(right_name.as_bytes())
            .then_with(|| left_version.numeric_cmp(right_version))
            .then_with(|| left_id.as_bytes().cmp(right_id.as_bytes())),
    }
}

fn select_next_state(
    requirements: &[Requirement],
    groups: &BTreeMap<String, Vec<usize>>,
    scanned: &ScannedSource,
    lock: Option<&ParsedLock>,
    active_profile: &str,
) -> Result<(SelectionState, Vec<SelectionDecision>), ResolveDiagnostic> {
    let mut by_package: BTreeMap<&str, Vec<&Requirement>> = BTreeMap::new();
    for requirement in requirements {
        by_package
            .entry(&requirement.package)
            .or_default()
            .push(requirement);
    }

    let mut diagnostics = Vec::new();
    let mut state = SelectionState::new();
    let mut decisions = Vec::new();
    for (name, package_requirements) in by_package {
        let path = format!("packages/{}", encode_component(name));
        let Some(group) = groups.get(name) else {
            diagnostics.push(DiagnosticCandidate::plain(
                9,
                resolve_diagnostic_codes::PACKAGE_NOT_FOUND,
                path,
            ));
            continue;
        };
        let eligible = group
            .iter()
            .copied()
            .filter(|index| {
                scanned.packages()[*index]
                    .descriptor()
                    .profiles()
                    .iter()
                    .any(|profile| profile == active_profile)
            })
            .collect::<Vec<_>>();
        if eligible.is_empty() {
            diagnostics.push(DiagnosticCandidate::plain(
                10,
                resolve_diagnostic_codes::PROFILE_INCOMPATIBLE,
                path,
            ));
            continue;
        }
        let satisfying = eligible
            .iter()
            .copied()
            .filter(|index| {
                let version = Version::parse(scanned.packages()[*index].descriptor().version())
                    .expect("PC6 admitted a canonical version");
                package_requirements
                    .iter()
                    .all(|requirement| requirement.interval.admits(&version))
            })
            .collect::<Vec<_>>();
        if satisfying.is_empty() {
            diagnostics.push(DiagnosticCandidate::plain(
                11,
                resolve_diagnostic_codes::NO_COMMON_VERSION,
                path,
            ));
            continue;
        }

        let lock_entry = lock.and_then(|lock| lock.entries.iter().find(|entry| entry.name == name));
        let (selected, status, selected_by) = if let Some(entry) = lock_entry {
            let same_version = group
                .iter()
                .copied()
                .find(|index| scanned.packages()[*index].descriptor().version() == entry.version);
            match same_version {
                None => (
                    *satisfying.last().expect("nonempty satisfying group"),
                    "stale_version",
                    "greatest",
                ),
                Some(index)
                    if scanned.packages()[index].identity().to_string() != entry.package_id =>
                {
                    (
                        *satisfying.last().expect("nonempty satisfying group"),
                        "stale_identity",
                        "greatest",
                    )
                }
                Some(index)
                    if !scanned.packages()[index]
                        .descriptor()
                        .profiles()
                        .iter()
                        .any(|profile| profile == active_profile) =>
                {
                    (
                        *satisfying.last().expect("nonempty satisfying group"),
                        "profile_ineligible",
                        "greatest",
                    )
                }
                Some(index)
                    if !package_requirements.iter().all(|requirement| {
                        requirement.interval.admits(
                            &Version::parse(scanned.packages()[index].descriptor().version())
                                .expect("PC6 admitted version"),
                        )
                    }) =>
                {
                    (
                        *satisfying.last().expect("nonempty satisfying group"),
                        "constraint_incompatible",
                        "greatest",
                    )
                }
                Some(index) => (index, "reused", "lock"),
            }
        } else {
            (
                *satisfying.last().expect("nonempty satisfying group"),
                if lock.is_some() {
                    "entry_missing"
                } else {
                    "no_lock_input"
                },
                "greatest",
            )
        };
        let package = &scanned.packages()[selected];
        state.insert(name.to_owned(), selected);
        decisions.push(SelectionDecision {
            package: name.to_owned(),
            status,
            selected_by,
            selected_version: package.descriptor().version().to_owned(),
            selected_package_id: package.identity().to_string(),
            lock_entry: lock_entry.map(|entry| (entry.version.clone(), entry.package_id.clone())),
        });
    }
    if let Some(diagnostic) = primary(diagnostics) {
        Err(diagnostic)
    } else {
        Ok((state, decisions))
    }
}

fn admit_selected_module(
    package_index: usize,
    scanned: &ScannedSource,
    active_profile: &str,
) -> Result<ParsedModule, Vec<DiagnosticCandidate>> {
    let package = &scanned.packages()[package_index];
    let descriptor = package.descriptor();
    let module_file = descriptor.module_file();
    let verified = package
        .verified_files()
        .iter()
        .find(|file| file.path() == module_file)
        .expect("PC6 guarantees module_file is a verified declared file");
    let declared_digest = descriptor
        .files()
        .iter()
        .find(|file| file.path() == module_file)
        .expect("PC6 binds module_file metadata")
        .sha256()
        .to_owned();
    let anchor = format!(
        "packages/{}/{}/{}#",
        encode_component(descriptor.package()),
        encode_component(descriptor.version()),
        encode_component(module_file)
    );

    let value = match parse_blueprint_source(verified.bytes()) {
        Ok(value) => value,
        Err(error) => {
            return Err(vec![module_parser_diagnostic(error, &anchor)]);
        }
    };
    let Some(root) = value.as_object() else {
        return Err(vec![DiagnosticCandidate::plain(
            18,
            resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
            anchor,
        )]);
    };

    const PERMITTED: [&str; 14] = [
        "lattice",
        "profile",
        "module",
        "version",
        "purpose",
        "imports",
        "inputs",
        "contracts",
        "resources",
        "units",
        "links",
        "policies",
        "exports",
        "scenarios",
    ];
    const REQUIRED: [&str; 6] = [
        "lattice", "profile", "module", "version", "purpose", "units",
    ];
    let mut candidates = Vec::new();
    for key in root.keys().filter(|key| !PERMITTED.contains(&key.as_str())) {
        candidates.push(DiagnosticCandidate::plain(
            18,
            resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
            format!("{anchor}/{}", encode_pointer_token(key)),
        ));
    }
    for key in REQUIRED {
        if !root.contains_key(key) {
            candidates.push(DiagnosticCandidate::plain(
                18,
                resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
                format!("{anchor}/{key}"),
            ));
        }
    }
    for key in PERMITTED {
        let Some(field) = root.get(key) else {
            continue;
        };
        let valid_type = match key {
            "lattice" | "profile" | "module" | "version" | "purpose" => field.is_string(),
            _ => field.is_array(),
        };
        if !valid_type {
            candidates.push(DiagnosticCandidate::plain(
                18,
                resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
                format!("{anchor}/{key}"),
            ));
        }
    }
    if root
        .get("module")
        .and_then(Value::as_str)
        .is_some_and(|value| !local_name(value))
    {
        candidates.push(DiagnosticCandidate::plain(
            18,
            resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
            format!("{anchor}/module"),
        ));
    }
    if root
        .get("version")
        .and_then(Value::as_str)
        .is_some_and(|value| Version::parse(value).is_none())
    {
        candidates.push(DiagnosticCandidate::plain(
            18,
            resolve_diagnostic_codes::MODULE_ENVELOPE_INVALID,
            format!("{anchor}/version"),
        ));
    }

    let imports = if let Some(imports) = root.get("imports").and_then(Value::as_array) {
        match admit_imports(&Value::Array(imports.clone()), &anchor) {
            Ok(imports) => imports,
            Err(error) => {
                candidates.push(DiagnosticCandidate {
                    rank: rank_for_code(error.code()),
                    code: error.code(),
                    path: error.path().to_owned(),
                    canonical_cycle: None,
                });
                Vec::new()
            }
        }
    } else {
        Vec::new()
    };

    for (key, expected) in [
        ("lattice", "0.3"),
        ("profile", active_profile),
        ("module", descriptor.package()),
        ("version", descriptor.version()),
    ] {
        if let Some(actual) = root.get(key).and_then(Value::as_str)
            && actual != expected
        {
            candidates.push(DiagnosticCandidate::plain(
                19,
                resolve_diagnostic_codes::MODULE_METADATA_MISMATCH,
                format!("{anchor}/{key}"),
            ));
        }
    }
    if !candidates.is_empty() {
        return Err(candidates);
    }

    Ok(ParsedModule {
        package_index,
        value,
        imports,
        module_file: module_file.to_owned(),
        retained_bytes: Arc::from(verified.bytes()),
        retained_sha256: declared_digest,
        node: package_node(package),
    })
}

fn module_parser_diagnostic(error: SourceDiagnostic, anchor: &str) -> DiagnosticCandidate {
    let (rank, code) = match error.code {
        "SOURCE_INVALID_UTF8" => (12, resolve_diagnostic_codes::MODULE_SOURCE_INVALID),
        "SOURCE_FORBIDDEN_YAML" => (13, resolve_diagnostic_codes::MODULE_YAML_FORBIDDEN),
        "SOURCE_INVALID_SCALAR" => (14, resolve_diagnostic_codes::MODULE_SCALAR_INVALID),
        "SOURCE_NON_STRING_KEY" => (15, resolve_diagnostic_codes::MODULE_NON_STRING_KEY),
        "SOURCE_DUPLICATE_KEY" => (16, resolve_diagnostic_codes::MODULE_DUPLICATE_KEY),
        "SOURCE_NFC_COLLISION" => (17, resolve_diagnostic_codes::MODULE_NFC_COLLISION),
        _ => unreachable!("PC2 exposes only the six frozen parser codes at this boundary"),
    };
    DiagnosticCandidate::plain(rank, code, append_pointer(anchor, &error.path))
}

fn rank_for_code(code: &str) -> u8 {
    DIAGNOSTIC_CODES
        .iter()
        .position(|candidate| *candidate == code)
        .map(|index| u8::try_from(index + 1).expect("21 ranks fit u8"))
        .expect("known Resolve diagnostic")
}

fn state_equal(left: &SelectionState, right: &SelectionState, scanned: &ScannedSource) -> bool {
    left.len() == right.len()
        && left.iter().all(|(name, left_index)| {
            right.get(name).is_some_and(|right_index| {
                scanned.packages()[*left_index].identity()
                    == scanned.packages()[*right_index].identity()
            })
        })
}

fn changes_value(
    before: &SelectionState,
    after: &SelectionState,
    scanned: &ScannedSource,
) -> Value {
    let names = before
        .keys()
        .chain(after.keys())
        .cloned()
        .collect::<BTreeSet<_>>();
    let mut changes = Map::new();
    for name in names {
        let from = before
            .get(&name)
            .map(|index| scanned.packages()[*index].identity().to_string());
        let to = after
            .get(&name)
            .map(|index| scanned.packages()[*index].identity().to_string());
        if from != to {
            changes.insert(
                name,
                object([
                    ("from", from.map_or(Value::Null, Value::String)),
                    ("to", to.map_or(Value::Null, Value::String)),
                ]),
            );
        }
    }
    Value::Object(changes)
}

fn selection_value(state: &SelectionState, scanned: &ScannedSource) -> Value {
    Value::Array(
        state
            .iter()
            .map(|(name, index)| {
                let package = &scanned.packages()[*index];
                object([
                    ("name", Value::String(name.clone())),
                    ("package_id", Value::String(package.identity().to_string())),
                    ("record", package_record_value(package)),
                    (
                        "version",
                        Value::String(package.descriptor().version().to_owned()),
                    ),
                ])
            })
            .collect(),
    )
}

fn build_graph(
    root_module: &str,
    state: &SelectionState,
    requirements: &[Requirement],
    scanned: &ScannedSource,
) -> Value {
    let mut nodes = vec![object([
        ("kind", Value::String("root".to_owned())),
        ("module", Value::String(root_module.to_owned())),
        ("node", Value::String("root".to_owned())),
    ])];
    for (name, index) in state {
        let package = &scanned.packages()[*index];
        nodes.push(object([
            ("kind", Value::String("package".to_owned())),
            ("name", Value::String(name.clone())),
            ("node", Value::String(package_node(package))),
            ("package_id", Value::String(package.identity().to_string())),
            (
                "version",
                Value::String(package.descriptor().version().to_owned()),
            ),
        ]));
    }
    let mut edges = requirements
        .iter()
        .map(|requirement| {
            let from = match &requirement.contributor {
                Contributor::Root { .. } => "root".to_owned(),
                Contributor::Package {
                    package,
                    version,
                    package_id,
                } => format!("package:{package}@{}#{package_id}", version.text),
            };
            let target_index = state
                .get(&requirement.package)
                .expect("converged requirement target is selected");
            object([
                ("alias", Value::String(requirement.alias.clone())),
                ("constraint", Value::String(requirement.constraint.clone())),
                ("from", Value::String(from)),
                (
                    "source_path",
                    Value::String(requirement.source_path.clone()),
                ),
                (
                    "to",
                    Value::String(package_node(&scanned.packages()[*target_index])),
                ),
            ])
        })
        .collect::<Vec<_>>();
    edges.sort_by(graph_edge_value_cmp);
    object([
        ("edges", Value::Array(edges)),
        ("nodes", Value::Array(nodes)),
    ])
}

fn graph_edge_value_cmp(left: &Value, right: &Value) -> Ordering {
    for key in ["from", "alias", "to", "constraint", "source_path"] {
        let order = left[key]
            .as_str()
            .expect("graph edge strings")
            .as_bytes()
            .cmp(right[key].as_str().expect("graph edge strings").as_bytes());
        if order != Ordering::Equal {
            return order;
        }
    }
    Ordering::Equal
}

#[derive(Clone)]
struct CycleInputEdge {
    from: String,
    to: String,
    alias: String,
    constraint: String,
    source_path: String,
}

fn canonical_cycle(requirements: &[Requirement]) -> Option<Vec<ResolveCycleEdge>> {
    let mut adjacency: BTreeMap<String, Vec<CycleInputEdge>> = BTreeMap::new();
    for requirement in requirements {
        let Contributor::Package { package, .. } = &requirement.contributor else {
            continue;
        };
        adjacency
            .entry(package.clone())
            .or_default()
            .push(CycleInputEdge {
                from: package.clone(),
                to: requirement.package.clone(),
                alias: requirement.alias.clone(),
                constraint: requirement.constraint.clone(),
                source_path: requirement.source_path.clone(),
            });
    }
    for edges in adjacency.values_mut() {
        edges.sort_by(cycle_edge_cmp);
    }

    let mut best: Option<(Vec<Vec<u8>>, Vec<CycleInputEdge>)> = None;
    for start in adjacency.keys() {
        let mut visited = BTreeSet::new();
        visited.insert(start.clone());
        let mut path = Vec::new();
        enumerate_cycles(start, start, &adjacency, &mut visited, &mut path, &mut best);
    }
    best.map(|(_, edges)| {
        edges
            .into_iter()
            .map(|edge| ResolveCycleEdge {
                alias: edge.alias,
                from: edge.from,
                source_path: format!("{}/use", edge.source_path),
                to: edge.to,
            })
            .collect()
    })
}

fn enumerate_cycles(
    start: &str,
    current: &str,
    adjacency: &BTreeMap<String, Vec<CycleInputEdge>>,
    visited: &mut BTreeSet<String>,
    path: &mut Vec<CycleInputEdge>,
    best: &mut Option<(Vec<Vec<u8>>, Vec<CycleInputEdge>)>,
) {
    let Some(edges) = adjacency.get(current) else {
        return;
    };
    for edge in edges {
        if edge.to == start {
            path.push(edge.clone());
            consider_cycle(path, best);
            path.pop();
        } else if visited.insert(edge.to.clone()) {
            path.push(edge.clone());
            enumerate_cycles(start, &edge.to, adjacency, visited, path, best);
            path.pop();
            visited.remove(&edge.to);
        }
    }
}

fn consider_cycle(
    cycle: &[CycleInputEdge],
    best: &mut Option<(Vec<Vec<u8>>, Vec<CycleInputEdge>)>,
) {
    let mut best_rotation: Option<(Vec<Vec<u8>>, Vec<CycleInputEdge>)> = None;
    for offset in 0..cycle.len() {
        let rotated = cycle[offset..]
            .iter()
            .chain(cycle[..offset].iter())
            .cloned()
            .collect::<Vec<_>>();
        let tokens = rotated.iter().map(cycle_token).collect::<Vec<_>>();
        if best_rotation
            .as_ref()
            .is_none_or(|(current, _)| tokens < *current)
        {
            best_rotation = Some((tokens, rotated));
        }
    }
    let rotation = best_rotation.expect("a cycle contains at least one edge");
    if best
        .as_ref()
        .is_none_or(|(current, _)| rotation.0 < *current)
    {
        *best = Some(rotation);
    }
}

fn cycle_token(edge: &CycleInputEdge) -> Vec<u8> {
    let mut token = Vec::new();
    for (index, field) in [
        edge.from.as_str(),
        edge.alias.as_str(),
        edge.to.as_str(),
        edge.constraint.as_str(),
        edge.source_path.as_str(),
    ]
    .into_iter()
    .enumerate()
    {
        if index != 0 {
            token.push(0);
        }
        token.extend_from_slice(field.as_bytes());
    }
    token
}

fn cycle_edge_cmp(left: &CycleInputEdge, right: &CycleInputEdge) -> Ordering {
    cycle_token(left).cmp(&cycle_token(right))
}

struct SuccessValueInputs<'a> {
    scanned: &'a ScannedSource,
    active_profile: &'a str,
    lock: Option<&'a ParsedLock>,
    pass_values: &'a [Value],
    state: &'a SelectionState,
    parsed_modules: &'a BTreeMap<String, ParsedModule>,
    requirements: &'a [Requirement],
    graph: &'a Value,
    final_decisions: &'a [SelectionDecision],
}

fn build_success_value(inputs: SuccessValueInputs<'_>) -> Value {
    let SuccessValueInputs {
        scanned,
        active_profile,
        lock,
        pass_values,
        state,
        parsed_modules,
        requirements,
        graph,
        final_decisions,
    } = inputs;
    let selected_packages = selection_value(state, scanned);
    let selected_modules = Value::Array(
        state
            .values()
            .map(|index| {
                let package = &scanned.packages()[*index];
                let id = package.identity().to_string();
                let module = parsed_modules
                    .get(&id)
                    .expect("every converged selection has an admitted module");
                object([
                    (
                        "imports",
                        Value::Array(module.imports.iter().map(import_projection_value).collect()),
                    ),
                    ("module_file", Value::String(module.module_file.clone())),
                    ("node", Value::String(module.node.clone())),
                    ("package_id", Value::String(id)),
                    ("parsed_module", module.value.clone()),
                    ("record", package_record_value(package)),
                    (
                        "retained_bytes",
                        bytes_value(module.retained_bytes.as_ref()),
                    ),
                    (
                        "retained_bytes_sha256",
                        Value::String(module.retained_sha256.clone()),
                    ),
                ])
            })
            .collect(),
    );
    let selected_names = state.keys().cloned().collect::<BTreeSet<_>>();
    let unreferenced = lock.map_or_else(Vec::new, |lock| {
        lock.entries
            .iter()
            .filter(|entry| !selected_names.contains(&entry.name))
            .map(|entry| Value::String(entry.name.clone()))
            .collect()
    });
    let existing_lock = object([
        (
            "input",
            lock.map_or(Value::Null, |lock| bytes_value(lock.bytes.as_ref())),
        ),
        (
            "input_sha256",
            lock.map_or(Value::Null, |lock| Value::String(lock.input_sha256.clone())),
        ),
        (
            "package_decisions",
            Value::Array(
                final_decisions
                    .iter()
                    .map(SelectionDecision::to_value)
                    .collect(),
            ),
        ),
        ("unreferenced_entries", Value::Array(unreferenced)),
    ]);
    object([
        ("active_profile", Value::String(active_profile.to_owned())),
        (
            "applicable_requirements",
            Value::Array(requirements.iter().map(Requirement::to_value).collect()),
        ),
        ("authority", Value::String("none".to_owned())),
        ("created_artifacts", Value::Array(Vec::new())),
        ("created_identities", Value::Array(Vec::new())),
        ("existing_lock", existing_lock),
        ("import_graph", graph.clone()),
        (
            "phase_status",
            Value::String("non_authoritative_resolved_source".to_owned()),
        ),
        ("resolution_passes", Value::Array(pass_values.to_vec())),
        ("scanned_source", scanned_source_value(scanned)),
        ("selected_modules", selected_modules),
        ("selected_packages", selected_packages),
    ])
}

fn import_projection_value(import: &Import) -> Value {
    object([
        ("as", Value::String(import.alias.clone())),
        ("use", Value::String(import.package.clone())),
        ("version", Value::String(import.constraint.clone())),
    ])
}

fn scanned_source_value(scanned: &ScannedSource) -> Value {
    let root = scanned
        .digested_source()
        .defaulted_source()
        .as_value()
        .clone();
    let active_profile = root["profile"].as_str().expect("PC3 profile").to_owned();
    object([
        ("active_profile", Value::String(active_profile)),
        (
            "blueprint_digest",
            Value::String(scanned.digested_source().blueprint_digest().to_string()),
        ),
        ("defaulted_root", root),
        (
            "packages",
            Value::Array(
                scanned
                    .packages()
                    .iter()
                    .map(package_record_value)
                    .collect(),
            ),
        ),
    ])
}

fn package_record_value(package: &ScannedPackage) -> Value {
    let descriptor = package.descriptor();
    let files = descriptor
        .files()
        .iter()
        .map(|file| {
            object([
                ("path", Value::String(file.path().to_owned())),
                ("sha256", Value::String(file.sha256().to_owned())),
            ])
        })
        .collect();
    let descriptor_value = object([
        ("files", Value::Array(files)),
        ("lattice", Value::String(descriptor.lattice().to_owned())),
        (
            "module_file",
            Value::String(descriptor.module_file().to_owned()),
        ),
        ("package", Value::String(descriptor.package().to_owned())),
        (
            "profiles",
            Value::Array(
                descriptor
                    .profiles()
                    .iter()
                    .cloned()
                    .map(Value::String)
                    .collect(),
            ),
        ),
        ("version", Value::String(descriptor.version().to_owned())),
    ]);
    let verified_files = package
        .verified_files()
        .iter()
        .map(|file| {
            let digest = descriptor
                .files()
                .iter()
                .find(|descriptor_file| descriptor_file.path() == file.path())
                .expect("PC6 descriptor and retained files agree")
                .sha256();
            object([
                ("bytes", bytes_value(file.bytes())),
                ("path", Value::String(file.path().to_owned())),
                ("sha256", Value::String(digest.to_owned())),
            ])
        })
        .collect();
    object([
        ("descriptor", descriptor_value),
        ("package_id", Value::String(package.identity().to_string())),
        ("verified_files", Value::Array(verified_files)),
    ])
}

fn bytes_value(bytes: &[u8]) -> Value {
    object([
        ("encoding", Value::String("lowercase_hex".to_owned())),
        ("hex", Value::String(lower_hex(bytes))),
    ])
}

fn package_node(package: &ScannedPackage) -> String {
    format!(
        "package:{}@{}#{}",
        package.descriptor().package(),
        package.descriptor().version(),
        package.identity()
    )
}

fn compare_version_text(left: &str, right: &str) -> Ordering {
    Version::parse(left)
        .expect("PC6 admitted version")
        .numeric_cmp(&Version::parse(right).expect("PC6 admitted version"))
}

fn package_name(value: &str) -> bool {
    let bytes = value.as_bytes();
    if !bytes.first().is_some_and(|byte| byte.is_ascii_lowercase()) {
        return false;
    }
    let mut previous_separator = false;
    for byte in &bytes[1..] {
        match byte {
            b'a'..=b'z' | b'0'..=b'9' => previous_separator = false,
            b'.' | b'_' | b'-' if !previous_separator => previous_separator = true,
            _ => return false,
        }
    }
    !previous_separator
}

fn local_name(value: &str) -> bool {
    let bytes = value.as_bytes();
    if !bytes.first().is_some_and(|byte| byte.is_ascii_lowercase()) {
        return false;
    }
    let mut previous_separator = false;
    for byte in &bytes[1..] {
        match byte {
            b'a'..=b'z' | b'0'..=b'9' => previous_separator = false,
            b'_' if !previous_separator => previous_separator = true,
            _ => return false,
        }
    }
    !previous_separator
}

fn object<const N: usize>(entries: [(&str, Value); N]) -> Value {
    Value::Object(
        entries
            .into_iter()
            .map(|(key, value)| (key.to_owned(), value))
            .collect(),
    )
}

fn lower_hex(bytes: &[u8]) -> String {
    const HEX: &[u8; 16] = b"0123456789abcdef";
    let mut output = String::with_capacity(bytes.len() * 2);
    for byte in bytes {
        output.push(char::from(HEX[usize::from(byte >> 4)]));
        output.push(char::from(HEX[usize::from(byte & 0x0f)]));
    }
    output
}

fn encode_component(value: &str) -> String {
    percent_encode(value.as_bytes())
}

fn encode_pointer_token(value: &str) -> String {
    let mut escaped = String::new();
    for character in value.chars() {
        match character {
            '~' => escaped.push_str("~0"),
            '/' => escaped.push_str("~1"),
            _ => escaped.push(character),
        }
    }
    percent_encode(escaped.as_bytes())
}

fn append_pointer(anchor: &str, pointer: &str) -> String {
    if pointer.is_empty() {
        return anchor.to_owned();
    }
    let mut output = anchor.to_owned();
    for token in pointer.split('/').skip(1) {
        output.push('/');
        output.push_str(&percent_encode(token.as_bytes()));
    }
    output
}

fn percent_encode(bytes: &[u8]) -> String {
    const HEX: &[u8; 16] = b"0123456789ABCDEF";
    let mut output = String::new();
    for byte in bytes {
        if byte.is_ascii_alphanumeric() || matches!(byte, b'-' | b'.' | b'_' | b'~') {
            output.push(char::from(*byte));
        } else {
            output.push('%');
            output.push(char::from(HEX[usize::from(byte >> 4)]));
            output.push(char::from(HEX[usize::from(byte & 0x0f)]));
        }
    }
    output
}

fn admit_lock(
    input: &ExistingLockfileInput,
    active_profile: &str,
    blueprint_digest: &str,
) -> Result<Option<ParsedLock>, ResolveDiagnostic> {
    let ExistingLockfileInput::Bytes(bytes) = input else {
        return Ok(None);
    };
    if bytes.starts_with(&[0xef, 0xbb, 0xbf]) {
        return Err(lock_diagnostic(
            resolve_diagnostic_codes::LOCK_SOURCE_INVALID,
            "lock#",
        ));
    }
    let text = std::str::from_utf8(bytes)
        .map_err(|_| lock_diagnostic(resolve_diagnostic_codes::LOCK_SOURCE_INVALID, "lock#"))?;
    let mut parser = StrictJsonParser::new(text);
    let (value, integer_lexemes) = parser.parse().map_err(|issue| {
        lock_diagnostic(
            resolve_diagnostic_codes::LOCK_SOURCE_INVALID,
            &format!("lock#{}", issue.diagnostic_pointer()),
        )
    })?;
    let canonical = canonical_lock_bytes(&value, &integer_lexemes, "")
        .map_err(|()| lock_diagnostic(resolve_diagnostic_codes::LOCK_SOURCE_INVALID, "lock#"))?;
    if canonical.as_slice() != bytes.as_ref() {
        return Err(lock_diagnostic(
            resolve_diagnostic_codes::LOCK_SOURCE_INVALID,
            "lock#",
        ));
    }

    let root = value
        .as_object()
        .ok_or_else(|| lock_diagnostic(resolve_diagnostic_codes::LOCK_SOURCE_INVALID, "lock#"))?;
    let permitted = [
        "lock_version",
        "lattice",
        "profile",
        "root_blueprint_digest",
        "packages",
        "lock_id",
    ];
    if let Some(key) = root
        .keys()
        .filter(|key| !permitted.contains(&key.as_str()))
        .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
    {
        return Err(lock_schema(&format!("/{}", encode_pointer_token(key))));
    }
    for field in permitted {
        if !root.contains_key(field) {
            return Err(lock_schema(&format!("/{field}")));
        }
    }
    for (field, valid) in [
        (
            "lock_version",
            integer_lexemes.contains_key("/lock_version"),
        ),
        ("lattice", root["lattice"].is_string()),
        ("profile", root["profile"].is_string()),
        (
            "root_blueprint_digest",
            root["root_blueprint_digest"].is_string(),
        ),
        ("packages", root["packages"].is_array()),
        ("lock_id", root["lock_id"].is_string()),
    ] {
        if !valid {
            return Err(lock_schema(&format!("/{field}")));
        }
    }
    if integer_lexemes
        .get("/lock_version")
        .is_none_or(|value| value != "1")
    {
        return Err(lock_schema("/lock_version"));
    }
    if !blueprint_id(
        root["root_blueprint_digest"]
            .as_str()
            .expect("type checked"),
    ) {
        return Err(lock_schema("/root_blueprint_digest"));
    }
    if !native_id(root["lock_id"].as_str().expect("type checked"), "lock") {
        return Err(lock_schema("/lock_id"));
    }

    let package_values = root["packages"].as_array().expect("type checked");
    for (index, package) in package_values.iter().enumerate() {
        if !package.is_object() {
            return Err(lock_schema(&format!("/packages/{index}")));
        }
    }
    let package_fields = ["name", "version", "package_id", "requested_by"];
    for (index, package) in package_values.iter().enumerate() {
        let package = package.as_object().expect("object checked");
        if let Some(key) = package
            .keys()
            .filter(|key| !package_fields.contains(&key.as_str()))
            .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
        {
            return Err(lock_schema(&format!(
                "/packages/{index}/{}",
                encode_pointer_token(key)
            )));
        }
    }
    for field in package_fields {
        for (index, package) in package_values.iter().enumerate() {
            if !package
                .as_object()
                .expect("object checked")
                .contains_key(field)
            {
                return Err(lock_schema(&format!("/packages/{index}/{field}")));
            }
        }
    }
    for field in package_fields {
        for (index, package) in package_values.iter().enumerate() {
            let value = &package.as_object().expect("object checked")[field];
            let valid = if field == "requested_by" {
                value.is_array()
            } else {
                value.is_string()
            };
            if !valid {
                return Err(lock_schema(&format!("/packages/{index}/{field}")));
            }
        }
    }
    for field in ["name", "version", "package_id"] {
        for (index, package) in package_values.iter().enumerate() {
            let value = package[field].as_str().expect("type checked");
            let valid = match field {
                "name" => package_name(value),
                "version" => Version::parse(value).is_some(),
                "package_id" => native_id(value, "package"),
                _ => unreachable!("closed package scalar grammar fields"),
            };
            if !valid {
                return Err(lock_schema(&format!("/packages/{index}/{field}")));
            }
        }
    }

    for (package_index, package) in package_values.iter().enumerate() {
        for (request_index, request) in package["requested_by"]
            .as_array()
            .expect("type checked")
            .iter()
            .enumerate()
        {
            if !request.is_object() {
                return Err(lock_schema(&format!(
                    "/packages/{package_index}/requested_by/{request_index}"
                )));
            }
        }
    }
    let request_fields = ["module", "requirement"];
    for (package_index, package) in package_values.iter().enumerate() {
        for (request_index, request) in package["requested_by"]
            .as_array()
            .expect("type checked")
            .iter()
            .enumerate()
        {
            let request = request.as_object().expect("object checked");
            if let Some(key) = request
                .keys()
                .filter(|key| !request_fields.contains(&key.as_str()))
                .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
            {
                return Err(lock_schema(&format!(
                    "/packages/{package_index}/requested_by/{request_index}/{}",
                    encode_pointer_token(key)
                )));
            }
        }
    }
    for field in request_fields {
        for (package_index, package) in package_values.iter().enumerate() {
            for (request_index, request) in package["requested_by"]
                .as_array()
                .expect("type checked")
                .iter()
                .enumerate()
            {
                let request = request.as_object().expect("object checked");
                if !request.contains_key(field) {
                    return Err(lock_schema(&format!(
                        "/packages/{package_index}/requested_by/{request_index}/{field}"
                    )));
                }
            }
        }
    }
    for field in request_fields {
        for (package_index, package) in package_values.iter().enumerate() {
            for (request_index, request) in package["requested_by"]
                .as_array()
                .expect("type checked")
                .iter()
                .enumerate()
            {
                let request = request.as_object().expect("object checked");
                let value = request[field].as_str().ok_or_else(|| {
                    lock_schema(&format!(
                        "/packages/{package_index}/requested_by/{request_index}/{field}"
                    ))
                })?;
                let valid = if field == "module" {
                    local_name(value)
                } else {
                    parse_constraint(value).is_some()
                };
                if !valid {
                    return Err(lock_schema(&format!(
                        "/packages/{package_index}/requested_by/{request_index}/{field}"
                    )));
                }
            }
        }
    }

    let mut package_names = Vec::new();
    for (index, package) in package_values.iter().enumerate() {
        let name = package["name"].as_str().expect("validated").to_owned();
        if let Some(previous) = package_names.last().map(String::as_str)
            && previous.as_bytes() >= name.as_bytes()
        {
            return Err(lock_schema(&format!("/packages/{index}/name")));
        }
        package_names.push(name);
    }

    let mut entries = Vec::new();
    for (index, package) in package_values.iter().enumerate() {
        let mut requested_by = Vec::new();
        for (request_index, request) in package["requested_by"]
            .as_array()
            .expect("validated")
            .iter()
            .enumerate()
        {
            let pair = (
                request["module"].as_str().expect("validated").to_owned(),
                request["requirement"]
                    .as_str()
                    .expect("validated")
                    .to_owned(),
            );
            if requested_by
                .last()
                .is_some_and(|previous: &(String, String)| {
                    previous
                        .0
                        .as_bytes()
                        .cmp(pair.0.as_bytes())
                        .then_with(|| previous.1.as_bytes().cmp(pair.1.as_bytes()))
                        == Ordering::Greater
                })
            {
                let offending = if requested_by
                    .last()
                    .is_some_and(|previous| previous.0 != pair.0)
                {
                    "module"
                } else {
                    "requirement"
                };
                return Err(lock_schema(&format!(
                    "/packages/{index}/requested_by/{request_index}/{offending}"
                )));
            }
            requested_by.push(pair);
        }
        entries.push(LockEntry {
            name: package_names[index].clone(),
            version: package["version"].as_str().expect("validated").to_owned(),
            package_id: package["package_id"]
                .as_str()
                .expect("validated")
                .to_owned(),
        });
    }

    let mut body = root.clone();
    let supplied_id = body
        .remove("lock_id")
        .and_then(|value| value.as_str().map(str::to_owned))
        .expect("validated lock_id");
    body.insert("lock_version".to_owned(), Value::Number(Number::from(1)));
    let expected_digest =
        canonical_sha256(&Value::Object(body)).expect("validated Lockfile body is canonicalizable");
    let expected_id = format!("lattice:lock:sha256:{expected_digest}");
    if supplied_id != expected_id {
        return Err(lock_diagnostic(
            resolve_diagnostic_codes::LOCK_ID_MISMATCH,
            "lock#/lock_id",
        ));
    }
    for (field, expected) in [
        ("lattice", "0.3"),
        ("profile", active_profile),
        ("root_blueprint_digest", blueprint_digest),
    ] {
        if root[field].as_str().expect("validated") != expected {
            return Err(lock_diagnostic(
                resolve_diagnostic_codes::LOCK_CONTEXT_MISMATCH,
                &format!("lock#/{field}"),
            ));
        }
    }
    Ok(Some(ParsedLock {
        bytes: bytes.clone(),
        input_sha256: sha256_digest(bytes).to_string(),
        entries,
    }))
}

fn lock_diagnostic(code: &'static str, path: &str) -> ResolveDiagnostic {
    ResolveDiagnostic {
        code,
        path: path.to_owned(),
        canonical_cycle: None,
    }
}

fn lock_schema(pointer: &str) -> ResolveDiagnostic {
    lock_diagnostic(
        resolve_diagnostic_codes::LOCK_SCHEMA_INVALID,
        &format!("lock#{pointer}"),
    )
}

fn blueprint_id(value: &str) -> bool {
    native_id(value, "blueprint")
}

fn native_id(value: &str, kind: &str) -> bool {
    value
        .strip_prefix(&format!("lattice:{kind}:sha256:"))
        .is_some_and(|digest| {
            digest.len() == 64
                && digest
                    .as_bytes()
                    .iter()
                    .all(|byte| byte.is_ascii_digit() || matches!(byte, b'a'..=b'f'))
        })
}

fn canonical_lock_bytes(
    value: &Value,
    integer_lexemes: &BTreeMap<String, String>,
    pointer: &str,
) -> Result<Vec<u8>, ()> {
    match value {
        Value::Null | Value::Bool(_) | Value::String(_) => canonical_bytes(value).map_err(|_| ()),
        Value::Number(_) => integer_lexemes
            .get(pointer)
            .map(|text| text.as_bytes().to_vec())
            .ok_or(()),
        Value::Array(values) => {
            let mut output = vec![b'['];
            for (index, child) in values.iter().enumerate() {
                if index != 0 {
                    output.push(b',');
                }
                output.extend(canonical_lock_bytes(
                    child,
                    integer_lexemes,
                    &format!("{pointer}/{index}"),
                )?);
            }
            output.push(b']');
            Ok(output)
        }
        Value::Object(values) => {
            let mut output = vec![b'{'];
            let mut entries = values.iter().collect::<Vec<_>>();
            entries.sort_by(|(left, _), (right, _)| left.as_bytes().cmp(right.as_bytes()));
            for (index, (key, child)) in entries.into_iter().enumerate() {
                if index != 0 {
                    output.push(b',');
                }
                output.extend(canonical_bytes(&Value::String(key.clone())).map_err(|_| ())?);
                output.push(b':');
                output.extend(canonical_lock_bytes(
                    child,
                    integer_lexemes,
                    &format!("{pointer}/{}", encode_pointer_token(key)),
                )?);
            }
            output.push(b'}');
            Ok(output)
        }
    }
}

#[derive(Debug)]
struct JsonIssue {
    pointer: String,
}

impl JsonIssue {
    fn key_collision(pointer: String) -> Self {
        Self {
            pointer: format!("key-collision:{pointer}"),
        }
    }

    fn numeric(pointer: &str) -> Self {
        Self {
            pointer: format!("numeric:{pointer}"),
        }
    }

    fn diagnostic_pointer(&self) -> &str {
        self.pointer
            .strip_prefix("key-collision:")
            .or_else(|| self.pointer.strip_prefix("numeric:"))
            .unwrap_or("")
    }
}

struct StrictJsonParser<'a> {
    bytes: &'a [u8],
    position: usize,
    integer_lexemes: BTreeMap<String, String>,
}

impl<'a> StrictJsonParser<'a> {
    fn new(text: &'a str) -> Self {
        Self {
            bytes: text.as_bytes(),
            position: 0,
            integer_lexemes: BTreeMap::new(),
        }
    }

    fn parse(&mut self) -> Result<(Value, BTreeMap<String, String>), JsonIssue> {
        self.whitespace();
        let value = self.value("")?;
        self.whitespace();
        if self.position != self.bytes.len() {
            return Err(JsonIssue {
                pointer: String::new(),
            });
        }
        Ok((value, std::mem::take(&mut self.integer_lexemes)))
    }

    fn value(&mut self, pointer: &str) -> Result<Value, JsonIssue> {
        match self.bytes.get(self.position).copied() {
            Some(b'{') => self.object(pointer),
            Some(b'[') => self.array(pointer),
            Some(b'"') => self.string().map(Value::String),
            Some(b't') if self.literal(b"true") => Ok(Value::Bool(true)),
            Some(b'f') if self.literal(b"false") => Ok(Value::Bool(false)),
            Some(b'n') if self.literal(b"null") => Ok(Value::Null),
            Some(b'-' | b'0'..=b'9') => self.number(pointer),
            Some(b'+') => Err(JsonIssue::numeric(pointer)),
            _ => Err(JsonIssue {
                pointer: pointer.to_owned(),
            }),
        }
    }

    fn object(&mut self, pointer: &str) -> Result<Value, JsonIssue> {
        self.position += 1;
        self.whitespace();
        let mut output = Map::new();
        let mut normalized_keys = BTreeSet::new();
        if self.take(b'}') {
            return Ok(Value::Object(output));
        }
        loop {
            if self.bytes.get(self.position) != Some(&b'"') {
                return Err(JsonIssue {
                    pointer: pointer.to_owned(),
                });
            }
            let key = self.string()?;
            let normalized = key.nfc().collect::<String>();
            let key_pointer = format!("{pointer}/{}", encode_pointer_token(&key));
            if !normalized_keys.insert(normalized) {
                return Err(JsonIssue::key_collision(key_pointer));
            }
            self.whitespace();
            if !self.take(b':') {
                return Err(JsonIssue {
                    pointer: key_pointer,
                });
            }
            self.whitespace();
            let value = self.value(&key_pointer)?;
            output.insert(key, value);
            self.whitespace();
            if self.take(b'}') {
                break;
            }
            if !self.take(b',') {
                return Err(JsonIssue {
                    pointer: pointer.to_owned(),
                });
            }
            self.whitespace();
        }
        Ok(Value::Object(output))
    }

    fn array(&mut self, pointer: &str) -> Result<Value, JsonIssue> {
        self.position += 1;
        self.whitespace();
        let mut output = Vec::new();
        if self.take(b']') {
            return Ok(Value::Array(output));
        }
        loop {
            let item_pointer = format!("{pointer}/{}", output.len());
            output.push(self.value(&item_pointer)?);
            self.whitespace();
            if self.take(b']') {
                break;
            }
            if !self.take(b',') {
                return Err(JsonIssue {
                    pointer: pointer.to_owned(),
                });
            }
            self.whitespace();
        }
        Ok(Value::Array(output))
    }

    fn string(&mut self) -> Result<String, JsonIssue> {
        if !self.take(b'"') {
            return Err(JsonIssue {
                pointer: String::new(),
            });
        }
        let mut output = String::new();
        let mut segment_start = self.position;
        loop {
            let Some(byte) = self.bytes.get(self.position).copied() else {
                return Err(JsonIssue {
                    pointer: String::new(),
                });
            };
            match byte {
                b'"' => {
                    output.push_str(
                        std::str::from_utf8(&self.bytes[segment_start..self.position]).map_err(
                            |_| JsonIssue {
                                pointer: String::new(),
                            },
                        )?,
                    );
                    self.position += 1;
                    return Ok(output);
                }
                b'\\' => {
                    output.push_str(
                        std::str::from_utf8(&self.bytes[segment_start..self.position]).map_err(
                            |_| JsonIssue {
                                pointer: String::new(),
                            },
                        )?,
                    );
                    self.position += 1;
                    let escape = *self.bytes.get(self.position).ok_or_else(|| JsonIssue {
                        pointer: String::new(),
                    })?;
                    self.position += 1;
                    match escape {
                        b'"' => output.push('"'),
                        b'\\' => output.push('\\'),
                        b'/' => output.push('/'),
                        b'b' => output.push('\u{0008}'),
                        b'f' => output.push('\u{000c}'),
                        b'n' => output.push('\n'),
                        b'r' => output.push('\r'),
                        b't' => output.push('\t'),
                        b'u' => {
                            let first = self.hex_quad()?;
                            let scalar = if (0xd800..=0xdbff).contains(&first) {
                                if !self.take(b'\\') || !self.take(b'u') {
                                    return Err(JsonIssue {
                                        pointer: String::new(),
                                    });
                                }
                                let second = self.hex_quad()?;
                                if !(0xdc00..=0xdfff).contains(&second) {
                                    return Err(JsonIssue {
                                        pointer: String::new(),
                                    });
                                }
                                0x10000
                                    + ((u32::from(first) - 0xd800) << 10)
                                    + (u32::from(second) - 0xdc00)
                            } else if (0xdc00..=0xdfff).contains(&first) {
                                return Err(JsonIssue {
                                    pointer: String::new(),
                                });
                            } else {
                                u32::from(first)
                            };
                            output.push(char::from_u32(scalar).ok_or_else(|| JsonIssue {
                                pointer: String::new(),
                            })?);
                        }
                        _ => {
                            return Err(JsonIssue {
                                pointer: String::new(),
                            });
                        }
                    }
                    segment_start = self.position;
                }
                0x00..=0x1f => {
                    return Err(JsonIssue {
                        pointer: String::new(),
                    });
                }
                _ => self.position += 1,
            }
        }
    }

    fn hex_quad(&mut self) -> Result<u16, JsonIssue> {
        let end = self.position.checked_add(4).ok_or_else(|| JsonIssue {
            pointer: String::new(),
        })?;
        let bytes = self
            .bytes
            .get(self.position..end)
            .ok_or_else(|| JsonIssue {
                pointer: String::new(),
            })?;
        let mut value = 0_u16;
        for byte in bytes {
            value = value
                .checked_mul(16)
                .and_then(|value| value.checked_add(u16::from(hex_digit(*byte)?)))
                .ok_or_else(|| JsonIssue {
                    pointer: String::new(),
                })?;
        }
        self.position = end;
        Ok(value)
    }

    fn number(&mut self, pointer: &str) -> Result<Value, JsonIssue> {
        let start = self.position;
        let negative = self.take(b'-');
        if self.take(b'0') {
            if negative
                || self
                    .bytes
                    .get(self.position)
                    .is_some_and(u8::is_ascii_digit)
            {
                return Err(JsonIssue::numeric(pointer));
            }
        } else {
            let first = self.bytes.get(self.position).copied();
            if !first.is_some_and(|byte| matches!(byte, b'1'..=b'9')) {
                return Err(JsonIssue::numeric(pointer));
            }
            self.position += 1;
            while self
                .bytes
                .get(self.position)
                .is_some_and(u8::is_ascii_digit)
            {
                self.position += 1;
            }
        }
        if self
            .bytes
            .get(self.position)
            .is_some_and(|byte| matches!(byte, b'.' | b'e' | b'E'))
        {
            return Err(JsonIssue::numeric(pointer));
        }
        let text = std::str::from_utf8(&self.bytes[start..self.position])
            .map_err(|_| JsonIssue::numeric(pointer))?;
        self.integer_lexemes
            .insert(pointer.to_owned(), text.to_owned());
        Ok(Value::Number(Number::from(0)))
    }

    fn literal(&mut self, literal: &[u8]) -> bool {
        if self.bytes.get(self.position..self.position + literal.len()) == Some(literal) {
            self.position += literal.len();
            true
        } else {
            false
        }
    }

    fn whitespace(&mut self) {
        while self
            .bytes
            .get(self.position)
            .is_some_and(|byte| matches!(byte, b' ' | b'\n' | b'\r' | b'\t'))
        {
            self.position += 1;
        }
    }

    fn take(&mut self, expected: u8) -> bool {
        if self.bytes.get(self.position) == Some(&expected) {
            self.position += 1;
            true
        } else {
            false
        }
    }
}

fn hex_digit(byte: u8) -> Option<u8> {
    match byte {
        b'0'..=b'9' => Some(byte - b'0'),
        b'a'..=b'f' => Some(byte - b'a' + 10),
        b'A'..=b'F' => Some(byte - b'A' + 10),
        _ => None,
    }
}
