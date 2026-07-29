#![forbid(unsafe_code)]

//! Restricted Lattice source processing through Lock.
//!
//! This crate owns the PC2 boundary from UTF-8 YAML source to an NFC-normalized,
//! JSON-shaped value tree and the PC3 boundary from that tree to a validated
//! Core root shape. It also owns the PC4 boundary from validated source to a
//! non-authoritative default-expanded value, the PC5 boundary that binds that
//! exact value to its Blueprint digest, and the PC6 boundary that binds it to
//! verified local package descriptors and immutable declared-file bytes.
//! It also owns the PC7 boundary that resolves an accepted PC6 `ScannedSource`
//! against optional immutable existing-Lockfile bytes into a `ResolvedSource`,
//! and the PC8 boundary that projects that exact result into a canonical,
//! non-authoritative `LockedSource`. Declaration validation and phases after
//! Lock remain out of scope.

pub mod lock;
mod package_scan;
mod resolve;

pub use lock::{
    CreatedLockArtifact, LockAuthority, LockIdentity, LockPhaseStatus, LockedPackage, LockedSource,
    Lockfile, RequestedBy, lock_source,
};
pub use package_scan::{
    PackageDescriptorFile, PackageIdentity, PackageScanDiagnostic, PortableProjectSnapshot,
    ScannedPackage, ScannedPackageDescriptor, ScannedSource, SnapshotAcquisitionError,
    SnapshotEntry, SnapshotName, SnapshotNode, VerifiedPackageFile, acquire_project_snapshot,
    package_scan_diagnostic_codes, scan_packages,
};
pub use resolve::{
    ExistingLockfileInput, ResolveCycleEdge, ResolveDiagnostic, ResolvedSource,
    resolve_diagnostic_codes, resolve_source,
};

use core::fmt;
use saphyr_parser::{Event, Marker, Parser, ScalarStyle, Span, Tag};
use serde::Serialize;
use serde_json::{Map, Number, Value};
use std::borrow::Cow;
use std::collections::{BTreeMap, BTreeSet};
use threadsmith_canonical::canonical_sha256;
use threadsmith_schema::{ArtifactKind, NativeLatticeId};
use unicode_normalization::UnicodeNormalization;

/// Stable source diagnostic for PC2 parsing and PC3 root validation.
///
/// Upstream parser messages are never exposed through this API. PC2 freezes
/// all four fields; PC3 freezes `code` and `path` and always leaves the source
/// position fields as `None`.
#[derive(Clone, Debug, Eq, PartialEq, Serialize)]
pub struct SourceDiagnostic {
    pub code: &'static str,
    pub path: String,
    pub line: Option<usize>,
    pub column: Option<usize>,
}

impl fmt::Display for SourceDiagnostic {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(formatter, "{} at {}", self.code, self.path)
    }
}

impl std::error::Error for SourceDiagnostic {}

/// Non-authoritative PC3 output carrying an unchanged PC2 value tree.
///
/// Construction is restricted to [`validate_blueprint_source`]. This wrapper
/// proves only that the frozen Core root-shape checks passed. It is not a
/// compiled Blueprint, an identity preimage, a Manifest, or execution
/// authority.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ValidatedSource {
    value: Value,
}

impl ValidatedSource {
    /// Borrow the unchanged PC2 value tree.
    #[must_use]
    pub fn as_value(&self) -> &Value {
        &self.value
    }

    /// Consume the wrapper and return the unchanged PC2 value tree.
    #[must_use]
    pub fn into_value(self) -> Value {
        self.value
    }
}

/// Non-authoritative PC4 output carrying only the default-expanded value tree.
///
/// Construction is restricted to [`apply_blueprint_defaults`]. This wrapper
/// proves only that the frozen Standard defaults were applied. It contains no
/// default provenance, source-presence metadata, identity, Manifest, Binding,
/// or execution authority.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct DefaultedSource {
    value: Value,
}

impl DefaultedSource {
    /// Borrow the expanded JSON-shaped value used by the later Digest phase.
    #[must_use]
    pub fn as_value(&self) -> &Value {
        &self.value
    }

    /// Consume the wrapper and return the expanded JSON-shaped value.
    #[must_use]
    pub fn into_value(self) -> Value {
        self.value
    }
}

/// Opaque PC5-produced Blueprint content identity.
///
/// Construction is restricted to [`digest_source`]. A caller-created generic
/// [`NativeLatticeId`] claim is not a `BlueprintDigest` and cannot be promoted
/// into one through this API. This digest identifies source content only and
/// grants no compilation or execution authority.
#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
pub struct BlueprintDigest {
    identity: NativeLatticeId,
}

impl BlueprintDigest {
    /// Borrow the accepted native textual identity representation.
    #[must_use]
    pub const fn as_native_id(&self) -> &NativeLatticeId {
        &self.identity
    }
}

impl fmt::Display for BlueprintDigest {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Display::fmt(&self.identity, formatter)
    }
}

/// Non-authoritative PC5 output binding one digest to its exact source.
///
/// Both fields are private and construction is restricted to [`digest_source`]
/// so public callers cannot pair one source with another source's digest. The
/// wrapper stores no canonical bytes, provenance, diagnostic, Manifest,
/// Binding, permission, or authority metadata.
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct DigestedSource {
    defaulted_source: DefaultedSource,
    blueprint_digest: BlueprintDigest,
}

impl DigestedSource {
    /// Borrow the exact PC4 value consumed by [`digest_source`].
    #[must_use]
    pub const fn defaulted_source(&self) -> &DefaultedSource {
        &self.defaulted_source
    }

    /// Borrow the Blueprint digest calculated from the contained source.
    #[must_use]
    pub const fn blueprint_digest(&self) -> &BlueprintDigest {
        &self.blueprint_digest
    }

    /// Consume the binding and recover its exact default-expanded source.
    #[must_use]
    pub fn into_defaulted_source(self) -> DefaultedSource {
        self.defaulted_source
    }
}

/// Canonically digest one accepted PC4 source and bind the result to it.
///
/// The complete post-default root is encoded by `threadsmith-canonical` and
/// SHA-256 is calculated there. Encoding is total for publicly constructible
/// `DefaultedSource`; failure indicates an internal invariant violation rather
/// than a user-source diagnostic.
#[must_use]
pub fn digest_source(source: DefaultedSource) -> DigestedSource {
    let digest = canonical_sha256(source.as_value())
        .expect("DefaultedSource must remain canonically encodable");
    let blueprint_digest = BlueprintDigest {
        identity: NativeLatticeId::from_canonical_digest(ArtifactKind::Blueprint, digest),
    };
    DigestedSource {
        defaulted_source: source,
        blueprint_digest,
    }
}

/// Parse one PC2 Lattice source document.
///
/// The returned value is a source projection, not a validated Blueprint or an
/// authoritative artifact. Object keys and string values are NFC-normalized
/// and arrays retain source order. No root validation or default insertion is
/// performed, so absent fields remain absent for later compiler phases.
///
/// # Errors
///
/// Returns the first deterministic diagnostic required by the frozen PC2
/// parser semantics.
pub fn parse_blueprint_source(source: &[u8]) -> Result<Value, SourceDiagnostic> {
    let source = validate_source_bytes(source)?;
    let source = source.as_ref();
    validate_directives(source)?;
    audit_yaml_features(source)?;
    let mut cursor = Cursor::new(source);

    cursor.expect_stream_start()?;
    cursor.expect_document_start()?;
    let root = cursor.parse_node(&Path::root())?;
    cursor.expect_document_end()?;
    cursor.expect_stream_end()?;

    Ok(node_to_json(root.value))
}

const PERMITTED_ROOT_KEYS: [&str; 14] = [
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

const REQUIRED_ROOT_KEYS: [&str; 6] = [
    "lattice", "profile", "module", "version", "purpose", "units",
];

const OPTIONAL_ROOT_LISTS: [&str; 8] = [
    "imports",
    "inputs",
    "contracts",
    "resources",
    "links",
    "policies",
    "exports",
    "scenarios",
];

const SOURCE_VALUE_DOMAIN_INVALID: &str = "SOURCE_VALUE_DOMAIN_INVALID";

fn admit_pc2_value_domain(value: &Value, path: &Path) -> Result<(), SourceDiagnostic> {
    match value {
        Value::Null | Value::Bool(_) => Ok(()),
        Value::Number(number) => {
            let Some(integer) = number.as_i64() else {
                return Err(source_validation_diagnostic(
                    SOURCE_VALUE_DOMAIN_INVALID,
                    &path.0,
                ));
            };
            if number.as_str() != integer.to_string() {
                return Err(source_validation_diagnostic(
                    SOURCE_VALUE_DOMAIN_INVALID,
                    &path.0,
                ));
            }
            Ok(())
        }
        Value::String(text) => {
            if !text.nfc().eq(text.chars()) {
                return Err(source_validation_diagnostic(
                    SOURCE_VALUE_DOMAIN_INVALID,
                    &path.0,
                ));
            }
            Ok(())
        }
        Value::Array(values) => {
            for (index, value) in values.iter().enumerate() {
                admit_pc2_value_domain(value, &path.index(index))?;
            }
            Ok(())
        }
        Value::Object(values) => {
            let mut entries = values
                .iter()
                .map(|(key, value)| (key.as_str(), value))
                .collect::<Vec<_>>();
            entries.sort_by(|left, right| left.0.as_bytes().cmp(right.0.as_bytes()));

            let mut normalized_keys = BTreeMap::new();
            let mut first_non_nfc = None;
            for (key, _) in &entries {
                let normalized: String = key.nfc().collect();
                if normalized_keys.insert(normalized.clone(), *key).is_some() {
                    return Err(source_validation_diagnostic(
                        SOURCE_VALUE_DOMAIN_INVALID,
                        &path.key(key).0,
                    ));
                }
                if normalized != *key && first_non_nfc.is_none() {
                    first_non_nfc = Some(path.key(key));
                }
            }
            if let Some(path) = first_non_nfc {
                return Err(source_validation_diagnostic(
                    SOURCE_VALUE_DOMAIN_INVALID,
                    &path.0,
                ));
            }

            for (key, value) in entries {
                admit_pc2_value_domain(value, &path.key(key))?;
            }
            Ok(())
        }
    }
}

/// Validate the frozen PC3 Core root shape without changing the value tree.
///
/// Validation is limited to the root object, its exact key set, required keys,
/// Core selectors, module metadata, and root collection categories. Array
/// elements are deliberately opaque to PC3. No defaults are inserted and no
/// identity, resolution, compilation, Manifest, Binding, or authority is
/// created.
///
/// # Errors
///
/// Returns the first diagnostic in the precedence frozen by PC3: root type,
/// UTF-8-ordered unknown key, required-key order, then permitted-key value
/// order. PC3 diagnostics have no source line or column because the PC2 value
/// boundary does not retain source locations.
pub fn validate_blueprint_source(value: Value) -> Result<ValidatedSource, SourceDiagnostic> {
    admit_pc2_value_domain(&value, &Path::root())?;

    let Some(root) = value.as_object() else {
        return Err(source_validation_diagnostic("SOURCE_ROOT_TYPE", ""));
    };

    if let Some(key) = root
        .keys()
        .filter(|key| !PERMITTED_ROOT_KEYS.contains(&key.as_str()))
        .min_by(|left, right| left.as_bytes().cmp(right.as_bytes()))
    {
        return Err(source_validation_diagnostic(
            "SOURCE_UNKNOWN_KEY",
            &json_pointer_key(key),
        ));
    }

    for key in REQUIRED_ROOT_KEYS {
        if !root.contains_key(key) {
            return Err(source_validation_diagnostic(
                "SOURCE_REQUIRED_KEY_MISSING",
                &json_pointer_key(key),
            ));
        }
    }

    for key in PERMITTED_ROOT_KEYS {
        let Some(root_value) = root.get(key) else {
            continue;
        };
        let valid = match key {
            "lattice" => root_value.as_str() == Some("0.3"),
            "profile" => root_value.as_str() == Some("lattice-core-0.1"),
            "module" => root_value.as_str().is_some_and(is_local_name),
            "version" => root_value.as_str().is_some_and(is_core_version),
            "purpose" => root_value.is_string(),
            "imports" | "inputs" | "contracts" | "resources" | "units" | "links" | "policies"
            | "exports" | "scenarios" => root_value.is_array(),
            _ => unreachable!("permitted root keys are exhaustively matched"),
        };
        if !valid {
            return Err(source_validation_diagnostic(
                "SOURCE_INVALID_ROOT_VALUE",
                &json_pointer_key(key),
            ));
        }
    }

    Ok(ValidatedSource { value })
}

/// Apply the frozen PC4 source defaults without validating declaration bodies.
///
/// Explicit members always take precedence, including empty, null, malformed,
/// and later-invalid values. Non-object elements and invalid nested containers
/// remain unchanged. The transformation is deterministic and idempotent and
/// creates no diagnostic, canonical bytes, identity, authority, or executable
/// artifact.
#[must_use]
pub fn apply_blueprint_defaults(source: ValidatedSource) -> DefaultedSource {
    let mut value = source.into_value();
    let root = value
        .as_object_mut()
        .expect("ValidatedSource always contains a root object");

    for key in OPTIONAL_ROOT_LISTS {
        root.entry(key).or_insert_with(|| Value::Array(Vec::new()));
    }

    apply_to_object_elements(root.get_mut("inputs"), apply_input_defaults);
    apply_to_object_elements(root.get_mut("exports"), apply_output_defaults);

    apply_to_object_elements(root.get_mut("units"), |unit| {
        let kind_defaults = match unit.get("kind").and_then(Value::as_str) {
            Some("program" | "gate") => Some(("stateless", false)),
            Some("model") => Some(("stateless", true)),
            Some("controller") => Some(("event_sourced", false)),
            Some("broker") => Some(("external", false)),
            _ => None,
        };

        if let Some((mode, is_model)) = kind_defaults {
            unit.entry("mode")
                .or_insert_with(|| Value::String(mode.to_owned()));
            if is_model {
                unit.entry("repair_attempts")
                    .or_insert_with(|| Value::Number(Number::from(0)));
                unit.entry("fallback").or_insert_with(|| Value::Bool(false));
            }
        }

        apply_to_object_elements(unit.get_mut("inputs"), apply_input_defaults);
        apply_to_object_elements(unit.get_mut("outputs"), apply_output_defaults);
    });

    apply_to_object_elements(root.get_mut("links"), |link| {
        link.entry("mode")
            .or_insert_with(|| Value::String("data".to_owned()));
        link.entry("delivery")
            .or_insert_with(|| Value::String("multicast".to_owned()));
        link.entry("when").or_insert_with(constant_true_predicate);
    });
    apply_to_object_elements(root.get_mut("policies"), |policy| {
        policy.entry("when").or_insert_with(constant_true_predicate);
    });
    apply_to_object_elements(root.get_mut("scenarios"), |scenario| {
        scenario
            .entry("required")
            .or_insert_with(|| Value::Bool(true));
    });

    DefaultedSource { value }
}

fn apply_to_object_elements(
    value: Option<&mut Value>,
    mut apply: impl FnMut(&mut Map<String, Value>),
) {
    let Some(Value::Array(elements)) = value else {
        return;
    };
    for element in elements {
        if let Value::Object(object) = element {
            apply(object);
        }
    }
}

fn apply_input_defaults(input: &mut Map<String, Value>) {
    input.entry("required").or_insert_with(|| Value::Bool(true));
    input
        .entry("cardinality")
        .or_insert_with(|| Value::String("one".to_owned()));
    input
        .entry("on_absence")
        .or_insert_with(|| Value::String("block".to_owned()));
}

fn apply_output_defaults(output: &mut Map<String, Value>) {
    output
        .entry("cardinality")
        .or_insert_with(|| Value::String("one".to_owned()));
}

fn constant_true_predicate() -> Value {
    let mut predicate = Map::new();
    predicate.insert("all".to_owned(), Value::Array(Vec::new()));
    Value::Object(predicate)
}

fn is_local_name(value: &str) -> bool {
    let mut segments = value.split('_');
    let Some(first) = segments.next() else {
        return false;
    };
    let mut characters = first.chars();
    characters
        .next()
        .is_some_and(|character| character.is_ascii_lowercase())
        && characters.all(|character| character.is_ascii_lowercase() || character.is_ascii_digit())
        && segments.all(|segment| {
            !segment.is_empty()
                && segment
                    .chars()
                    .all(|character| character.is_ascii_lowercase() || character.is_ascii_digit())
        })
}

fn is_core_version(value: &str) -> bool {
    let mut components = value.split('.');
    let valid_component = |component: &str| {
        !component.is_empty() && component.bytes().all(|byte| byte.is_ascii_digit())
    };
    components.next().is_some_and(valid_component)
        && components.next().is_some_and(valid_component)
        && components.next().is_some_and(valid_component)
        && components.next().is_none()
}

fn json_pointer_key(key: &str) -> String {
    format!("/{}", key.replace('~', "~0").replace('/', "~1"))
}

fn source_validation_diagnostic(code: &'static str, path: &str) -> SourceDiagnostic {
    SourceDiagnostic {
        code,
        path: path.to_owned(),
        line: None,
        column: None,
    }
}

fn audit_yaml_features(source: &str) -> Result<(), SourceDiagnostic> {
    let mut cursor = Cursor::new(source);
    cursor.expect_stream_start()?;
    cursor.expect_document_start()?;
    cursor.audit_node(&Path::root())?;
    cursor.expect_document_end()?;
    cursor.expect_stream_end()?;
    cursor.reject_unquoted_non_c0_source_characters()
}

#[derive(Clone, Debug)]
struct LocatedNode {
    value: Node,
}

#[derive(Clone, Debug)]
enum Node {
    Null,
    Bool(bool),
    Number(Number),
    String(String),
    Sequence(Vec<LocatedNode>),
    Mapping(Vec<Entry>),
}

#[derive(Clone, Debug)]
struct Entry {
    key: String,
    value: LocatedNode,
}

#[derive(Clone, Debug)]
struct Path(String);

impl Path {
    fn root() -> Self {
        Self(String::new())
    }

    fn key(&self, key: &str) -> Self {
        let escaped = key.replace('~', "~0").replace('/', "~1");
        Self(format!("{}/{}", self.0, escaped))
    }

    fn index(&self, index: usize) -> Self {
        Self(format!("{}/{}", self.0, index))
    }
}

struct Cursor<'source> {
    parser: Parser<'source, saphyr_parser::StrInput<'source>>,
    source: &'source str,
    unquoted_non_c0_source_characters: Vec<Marker>,
}

impl<'source> Cursor<'source> {
    fn new(source: &'source str) -> Self {
        Self {
            parser: Parser::new_from_str(source),
            source,
            unquoted_non_c0_source_characters: non_c0_source_character_markers(source),
        }
    }

    fn permit_quoted_source_characters(&mut self, style: ScalarStyle, span: Span) {
        if matches!(style, ScalarStyle::SingleQuoted | ScalarStyle::DoubleQuoted) {
            self.unquoted_non_c0_source_characters.retain(|marker| {
                marker.index() < span.start.index() || marker.index() >= span.end.index()
            });
        }
    }

    fn reject_unquoted_non_c0_source_characters(&self) -> Result<(), SourceDiagnostic> {
        self.unquoted_non_c0_source_characters
            .first()
            .map_or(Ok(()), |marker| {
                Err(diagnostic_at(
                    "SOURCE_FORBIDDEN_YAML",
                    &Path::root(),
                    *marker,
                ))
            })
    }

    fn next(&mut self, path: &Path) -> Result<(Event<'source>, Span), SourceDiagnostic> {
        match self.parser.next_event() {
            Some(Ok(event)) => Ok(event),
            Some(Err(error)) => Err(diagnostic_at_marker(
                "SOURCE_FORBIDDEN_YAML",
                path,
                *error.marker(),
            )),
            None => Err(diagnostic_without_position("SOURCE_FORBIDDEN_YAML", path)),
        }
    }

    fn expect_stream_start(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::StreamStart, _) => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_document_start(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::DocumentStart(_), _) => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_document_end(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::DocumentEnd, _) => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn expect_stream_end(&mut self) -> Result<(), SourceDiagnostic> {
        match self.next(&Path::root())? {
            (Event::StreamEnd, _) if self.parser.next_event().is_none() => Ok(()),
            (_, span) => Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &Path::root(),
                span.start,
            )),
        }
    }

    fn parse_node(&mut self, path: &Path) -> Result<LocatedNode, SourceDiagnostic> {
        let (event, span) = self.next(path)?;
        self.parse_event(event, span, path)
    }

    fn audit_node(&mut self, path: &Path) -> Result<(), SourceDiagnostic> {
        let (event, span) = self.next(path)?;
        self.audit_event(event, span, path)
    }

    fn audit_event(
        &mut self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<(), SourceDiagnostic> {
        match event {
            Event::Alias(_) => Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
            Event::Scalar(value, style, anchor, tag) => {
                self.permit_quoted_source_characters(style, span);
                let marker = scalar_error_marker(
                    self.source,
                    span.start,
                    style,
                    anchor != 0 || tag.is_some(),
                );
                reject_scalar_surface(value.as_ref(), style, anchor, tag.as_deref(), path, marker)
            }
            Event::SequenceStart(anchor, tag) => {
                if anchor != 0 || !collection_tag_is(tag.as_deref(), "seq") {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                let mut index = 0;
                loop {
                    let (event, span) = self.next(path)?;
                    if matches!(event, Event::SequenceEnd) {
                        return Ok(());
                    }
                    self.audit_event(event, span, &path.index(index))?;
                    index += 1;
                }
            }
            Event::MappingStart(anchor, tag) => {
                if anchor != 0 || !collection_tag_is(tag.as_deref(), "map") {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                self.audit_mapping(path)
            }
            _ => Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
        }
    }

    fn audit_mapping(&mut self, path: &Path) -> Result<(), SourceDiagnostic> {
        loop {
            let (event, span) = self.next(path)?;
            if matches!(event, Event::MappingEnd) {
                return Ok(());
            }

            let value_path = match event {
                Event::Scalar(value, style, anchor, tag) => {
                    self.permit_quoted_source_characters(style, span);
                    let marker = scalar_error_marker(
                        self.source,
                        span.start,
                        style,
                        anchor != 0 || tag.is_some(),
                    );
                    reject_scalar_surface(
                        value.as_ref(),
                        style,
                        anchor,
                        tag.as_deref(),
                        path,
                        marker,
                    )?;
                    let key: String = value.nfc().collect();
                    if style == ScalarStyle::Plain && key == "<<" {
                        return Err(diagnostic_at(
                            "SOURCE_FORBIDDEN_YAML",
                            &path.key("<<"),
                            span.start,
                        ));
                    }
                    path.key(&key)
                }
                Event::Alias(_) => {
                    return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
                }
                other => {
                    self.audit_event(other, span, path)?;
                    path.clone()
                }
            };
            self.audit_node(&value_path)?;
        }
    }

    fn parse_event(
        &mut self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<LocatedNode, SourceDiagnostic> {
        let value = match event {
            Event::Alias(_) => {
                return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
            }
            Event::Scalar(value, style, anchor, tag) => {
                let metadata_marker = scalar_error_marker(
                    self.source,
                    span.start,
                    style,
                    anchor != 0 || tag.is_some(),
                );
                reject_scalar_surface(
                    value.as_ref(),
                    style,
                    anchor,
                    tag.as_deref(),
                    path,
                    metadata_marker,
                )?;
                parse_scalar(value.as_ref(), style, tag.as_deref(), path, span.start)?
            }
            Event::SequenceStart(anchor, tag) => {
                if anchor != 0 || !collection_tag_is(tag.as_deref(), "seq") {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                let mut values = Vec::new();
                loop {
                    let (event, span) = self.next(path)?;
                    if matches!(event, Event::SequenceEnd) {
                        break;
                    }
                    let item_path = path.index(values.len());
                    values.push(self.parse_event(event, span, &item_path)?);
                }
                Node::Sequence(values)
            }
            Event::MappingStart(anchor, tag) => {
                if anchor != 0 || !collection_tag_is(tag.as_deref(), "map") {
                    return Err(diagnostic_at(
                        "SOURCE_FORBIDDEN_YAML",
                        path,
                        node_metadata_marker(self.source, span.start, true),
                    ));
                }
                Node::Mapping(self.parse_mapping(path)?)
            }
            _ => return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start)),
        };
        Ok(LocatedNode { value })
    }

    fn parse_mapping(&mut self, path: &Path) -> Result<Vec<Entry>, SourceDiagnostic> {
        let mut entries = Vec::new();
        let mut decoded_keys = BTreeSet::new();
        let mut normalized_keys = BTreeMap::<String, String>::new();

        loop {
            let (event, span) = self.next(path)?;
            if matches!(event, Event::MappingEnd) {
                return Ok(entries);
            }

            let (raw_key, key) = self.parse_key(event, span, path)?;
            let key_path = path.key(&key);
            if decoded_keys.contains(&raw_key) {
                return Err(diagnostic_at("SOURCE_DUPLICATE_KEY", &key_path, span.start));
            }
            if normalized_keys.contains_key(&key) {
                return Err(diagnostic_at("SOURCE_NFC_COLLISION", &key_path, span.start));
            }
            decoded_keys.insert(raw_key.clone());
            normalized_keys.insert(key.clone(), raw_key.clone());

            let value = self.parse_node(&key_path)?;
            entries.push(Entry { key, value });
        }
    }

    fn parse_key(
        &self,
        event: Event<'source>,
        span: Span,
        path: &Path,
    ) -> Result<(String, String), SourceDiagnostic> {
        let Event::Scalar(value, style, anchor, tag) = event else {
            if matches!(event, Event::Alias(_)) {
                return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
            }
            return Err(diagnostic_at("SOURCE_NON_STRING_KEY", path, span.start));
        };

        let metadata_marker =
            scalar_error_marker(self.source, span.start, style, anchor != 0 || tag.is_some());
        reject_scalar_surface(
            value.as_ref(),
            style,
            anchor,
            tag.as_deref(),
            path,
            metadata_marker,
        )?;
        if style == ScalarStyle::Folded {
            return Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, span.start));
        }

        let raw = parse_key_scalar(value.as_ref(), style, tag.as_deref(), path, span.start)?;
        if style == ScalarStyle::Plain && raw == "<<" {
            return Err(diagnostic_at(
                "SOURCE_FORBIDDEN_YAML",
                &path.key("<<"),
                span.start,
            ));
        }
        let normalized = raw.nfc().collect();
        Ok((raw, normalized))
    }
}

fn validate_source_bytes(source: &[u8]) -> Result<Cow<'_, str>, SourceDiagnostic> {
    let source = std::str::from_utf8(source).map_err(|error| {
        let (line, column) = byte_position(source, error.valid_up_to());
        SourceDiagnostic {
            code: "SOURCE_INVALID_UTF8",
            path: String::new(),
            line: Some(line),
            column: Some(column),
        }
    })?;
    let source = if source.contains('\r') {
        Cow::Owned(source.replace("\r\n", "\n").replace('\r', "\n"))
    } else {
        Cow::Borrowed(source)
    };

    let mut line = 1;
    let mut column = 1;
    for (index, character) in source.char_indices() {
        let forbidden = (index == 0 && character == '\u{feff}')
            || character == '\0'
            || matches!(character, '\u{0001}'..='\u{0008}' | '\u{000b}' | '\u{000c}' | '\u{000e}'..='\u{001f}');
        if forbidden {
            return Err(SourceDiagnostic {
                code: "SOURCE_INVALID_UTF8",
                path: String::new(),
                line: Some(line),
                column: Some(column),
            });
        }
        if character == '\n' {
            line += 1;
            column = 1;
        } else {
            column += 1;
        }
    }
    Ok(source)
}

fn validate_directives(source: &str) -> Result<(), SourceDiagnostic> {
    let mut yaml_directive_seen = false;
    let mut char_index = 0;
    for (line_index, line) in source.lines().enumerate() {
        if line.starts_with('%') {
            let suffix = line.strip_prefix("%YAML 1.2");
            let valid_yaml_12 = suffix.is_some_and(|suffix| {
                let suffix = suffix.trim_start();
                suffix.is_empty() || suffix.starts_with('#')
            });
            if valid_yaml_12 && !yaml_directive_seen {
                yaml_directive_seen = true;
            } else {
                return Err(diagnostic_at(
                    "SOURCE_FORBIDDEN_YAML",
                    &Path::root(),
                    Marker::new(char_index, line_index + 1, 0),
                ));
            }
        } else if !line.trim_start().is_empty() && !line.trim_start().starts_with('#') {
            break;
        }
        char_index += line.chars().count() + 1;
    }
    Ok(())
}

fn byte_position(source: &[u8], offset: usize) -> (usize, usize) {
    let prefix = String::from_utf8_lossy(&source[..offset]);
    let line = prefix.bytes().filter(|byte| *byte == b'\n').count() + 1;
    let column = prefix
        .rsplit('\n')
        .next()
        .map_or(1, |tail| tail.chars().count() + 1);
    (line, column)
}

fn non_c0_source_character_markers(source: &str) -> Vec<Marker> {
    let mut markers = Vec::new();
    let mut line = 1;
    let mut column = 0;
    for (index, character) in source.chars().enumerate() {
        if matches!(character, '\u{007f}'..='\u{0084}' | '\u{0086}'..='\u{009f}' | '\u{fffe}' | '\u{ffff}')
        {
            markers.push(Marker::new(index, line, column));
        }
        if character == '\n' {
            line += 1;
            column = 0;
        } else {
            column += 1;
        }
    }
    markers
}

fn reject_scalar_surface(
    value: &str,
    style: ScalarStyle,
    anchor: usize,
    tag: Option<&Tag>,
    path: &Path,
    marker: Marker,
) -> Result<(), SourceDiagnostic> {
    if anchor != 0
        || style == ScalarStyle::Folded
        || tag
            .is_some_and(|tag| matches!(classify_tagged_scalar(value, tag), TaggedScalar::Mismatch))
    {
        Err(diagnostic_at("SOURCE_FORBIDDEN_YAML", path, marker))
    } else {
        Ok(())
    }
}

fn collection_tag_is(tag: Option<&Tag>, expected: &str) -> bool {
    tag.is_none_or(|tag| tag.is_yaml_core_schema() && tag.suffix == expected)
}

fn parse_scalar(
    source: &str,
    style: ScalarStyle,
    tag: Option<&Tag>,
    path: &Path,
    marker: Marker,
) -> Result<Node, SourceDiagnostic> {
    match classify_scalar(source, style, tag) {
        Ok(PlainScalar::Null) => Ok(Node::Null),
        Ok(PlainScalar::Bool(value)) => Ok(Node::Bool(value)),
        Ok(PlainScalar::Integer(value)) => Ok(Node::Number(Number::from(value))),
        Ok(PlainScalar::String) => Ok(Node::String(source.nfc().collect())),
        Err(()) => Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker)),
    }
}

fn parse_key_scalar(
    source: &str,
    style: ScalarStyle,
    tag: Option<&Tag>,
    path: &Path,
    marker: Marker,
) -> Result<String, SourceDiagnostic> {
    match classify_scalar(source, style, tag) {
        Ok(PlainScalar::String) => Ok(source.to_owned()),
        Ok(_) => Err(diagnostic_at("SOURCE_NON_STRING_KEY", path, marker)),
        Err(()) => Err(diagnostic_at("SOURCE_INVALID_SCALAR", path, marker)),
    }
}

enum PlainScalar {
    Null,
    Bool(bool),
    Integer(i64),
    String,
}

enum TaggedScalar {
    Value(PlainScalar),
    OutOfRange,
    Mismatch,
}

fn classify_scalar(value: &str, style: ScalarStyle, tag: Option<&Tag>) -> Result<PlainScalar, ()> {
    let Some(tag) = tag else {
        return if style == ScalarStyle::Plain {
            classify_plain_scalar(value)
        } else {
            Ok(PlainScalar::String)
        };
    };

    match classify_tagged_scalar(value, tag) {
        TaggedScalar::Value(value) => Ok(value),
        TaggedScalar::OutOfRange | TaggedScalar::Mismatch => Err(()),
    }
}

fn classify_tagged_scalar(value: &str, tag: &Tag) -> TaggedScalar {
    if !tag.is_yaml_core_schema() {
        return TaggedScalar::Mismatch;
    }

    match tag.suffix.as_str() {
        "str" => TaggedScalar::Value(PlainScalar::String),
        "null" if is_core_null(value) => TaggedScalar::Value(PlainScalar::Null),
        "bool" => parse_core_bool(value)
            .map(PlainScalar::Bool)
            .map_or(TaggedScalar::Mismatch, TaggedScalar::Value),
        "int" => match parse_core_integer(value) {
            Some(Ok(value)) => TaggedScalar::Value(PlainScalar::Integer(value)),
            Some(Err(())) => TaggedScalar::OutOfRange,
            None => TaggedScalar::Mismatch,
        },
        _ => TaggedScalar::Mismatch,
    }
}

fn classify_plain_scalar(value: &str) -> Result<PlainScalar, ()> {
    if is_core_null(value) {
        return Ok(PlainScalar::Null);
    }
    if let Some(value) = parse_core_bool(value) {
        return Ok(PlainScalar::Bool(value));
    }

    if let Some(integer) = parse_core_integer(value) {
        return integer.map(PlainScalar::Integer);
    }
    if is_core_float(value) {
        return Err(());
    }
    Ok(PlainScalar::String)
}

fn is_core_null(value: &str) -> bool {
    matches!(value, "" | "null" | "Null" | "NULL" | "~")
}

fn parse_core_bool(value: &str) -> Option<bool> {
    match value {
        "true" | "True" | "TRUE" => Some(true),
        "false" | "False" | "FALSE" => Some(false),
        _ => None,
    }
}

fn parse_core_integer(value: &str) -> Option<Result<i64, ()>> {
    if let Some(digits) = value.strip_prefix("0o") {
        return (!digits.is_empty() && digits.bytes().all(|byte| matches!(byte, b'0'..=b'7')))
            .then(|| i64::from_str_radix(digits, 8).map_err(|_| ()));
    }
    if let Some(digits) = value.strip_prefix("0x") {
        return (!digits.is_empty() && digits.bytes().all(|byte| byte.is_ascii_hexdigit()))
            .then(|| i64::from_str_radix(digits, 16).map_err(|_| ()));
    }

    let unsigned = value.strip_prefix(['+', '-']).unwrap_or(value);
    if unsigned.is_empty() || !unsigned.bytes().all(|byte| byte.is_ascii_digit()) {
        return None;
    }
    Some(value.parse::<i64>().map_err(|_| ()))
}

fn is_core_float(value: &str) -> bool {
    let lower = value.to_ascii_lowercase();
    if matches!(lower.as_str(), ".inf" | "+.inf" | "-.inf" | ".nan") {
        return true;
    }

    let unsigned = value.strip_prefix(['+', '-']).unwrap_or(value);
    let (mantissa, exponent) = match unsigned.find(['e', 'E']) {
        Some(index) => {
            if unsigned[index + 1..].contains(['e', 'E']) {
                return false;
            }
            (&unsigned[..index], Some(&unsigned[index + 1..]))
        }
        None => (unsigned, None),
    };
    let exponent_is_valid = exponent.is_none_or(|exponent| {
        let digits = exponent.strip_prefix(['+', '-']).unwrap_or(exponent);
        !digits.is_empty() && digits.bytes().all(|byte| byte.is_ascii_digit())
    });
    if !exponent_is_valid {
        return false;
    }

    let mantissa_is_valid = if let Some(fraction) = mantissa.strip_prefix('.') {
        !fraction.is_empty() && fraction.bytes().all(|byte| byte.is_ascii_digit())
    } else if let Some((whole, fraction)) = mantissa.split_once('.') {
        !whole.is_empty()
            && whole.bytes().all(|byte| byte.is_ascii_digit())
            && fraction.bytes().all(|byte| byte.is_ascii_digit())
    } else {
        !mantissa.is_empty() && mantissa.bytes().all(|byte| byte.is_ascii_digit())
    };
    mantissa_is_valid && (mantissa.contains('.') || exponent.is_some())
}

fn node_to_json(node: Node) -> Value {
    match node {
        Node::Null => Value::Null,
        Node::Bool(value) => Value::Bool(value),
        Node::Number(value) => Value::Number(value),
        Node::String(value) => Value::String(value),
        Node::Sequence(values) => Value::Array(
            values
                .into_iter()
                .map(|value| node_to_json(value.value))
                .collect(),
        ),
        Node::Mapping(mut entries) => {
            entries.sort_by(|left, right| left.key.as_bytes().cmp(right.key.as_bytes()));
            let mut object = Map::new();
            for entry in entries {
                object.insert(entry.key, node_to_json(entry.value.value));
            }
            Value::Object(object)
        }
    }
}

fn diagnostic_at(code: &'static str, path: &Path, marker: Marker) -> SourceDiagnostic {
    SourceDiagnostic {
        code,
        path: path.0.clone(),
        line: Some(marker.line()),
        column: Some(marker.col() + 1),
    }
}

fn diagnostic_at_marker(code: &'static str, path: &Path, marker: Marker) -> SourceDiagnostic {
    diagnostic_at(code, path, marker)
}

fn diagnostic_without_position(code: &'static str, path: &Path) -> SourceDiagnostic {
    SourceDiagnostic {
        code,
        path: path.0.clone(),
        line: None,
        column: None,
    }
}

fn node_metadata_marker(source: &str, marker: Marker, has_metadata: bool) -> Marker {
    if !has_metadata {
        return marker;
    }
    let line = source
        .lines()
        .nth(marker.line().saturating_sub(1))
        .unwrap_or_default();
    let prefix: String = line.chars().take(marker.col()).collect();
    let column = prefix
        .chars()
        .enumerate()
        .filter_map(|(index, character)| matches!(character, '&' | '!').then_some(index))
        .last();
    column.map_or(marker, |column| {
        Marker::new(
            marker.index().saturating_sub(marker.col() - column),
            marker.line(),
            column,
        )
    })
}

fn scalar_error_marker(
    source: &str,
    marker: Marker,
    style: ScalarStyle,
    has_metadata: bool,
) -> Marker {
    if style == ScalarStyle::Folded && marker.line() > 1 {
        let indicator_line = marker.line() - 1;
        if let Some(line) = source.lines().nth(indicator_line - 1)
            && let Some(column) = line.chars().position(|character| character == '>')
        {
            return Marker::new(0, indicator_line, column);
        }
    }
    node_metadata_marker(source, marker, has_metadata)
}
