#!/usr/bin/env python3
"""Strict PC7 specified-manifest admission and deterministic plan generation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
import sys
import tempfile
import unicodedata
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = ROOT / "conformance/pc7/resolve/executable_fixture_plan.json"

EXPECTED_MANIFEST_SHA256 = (
    "da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c"
)
REGISTRY_PATH = Path("docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json")
REGISTRY_SHA256 = "7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161"
REGISTRY_BYTES = 2041
BASELINE_COMMIT = "ded743ea3577ffc2b955565dee9159287ec98e05"
BASELINE_TREE = "e26180101c53c5cf44e4f270a9e868a4582be392"
REGISTRY_FORMAT = "threadsmith-pc7-authority-registry-1"
AUTHORITY_DOCUMENTS = (
    ("lattice_standard", "docs/standard/LATTICE_STANDARD_0.3.md"),
    (
        "default_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md",
    ),
    (
        "canonical_json_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md",
    ),
    (
        "package_scan_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md",
    ),
    (
        "resolve_semantics_erratum",
        "docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md",
    ),
    ("pc7_scope_reconciliation", "docs/pc7/PC7_SCOPE_RECONCILIATION.md"),
    ("pc7_semantic_freeze", "docs/pc7/PC7_SEMANTIC_FREEZE.md"),
    (
        "pc7_specified_conformance_manifest",
        "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json",
    ),
)
EXPECTED_POPULATIONS = {
    "current_fixtures": 118,
    "non_dispatchable_future_vectors": 4,
    "diagnostic_codes": 21,
    "diagnostic_fixtures": 81,
    "ordinary_success_fixtures": 31,
    "success_relation_fixtures": 6,
    "new_normative_choices": 45,
    "schema_categories": 127,
    "reachable_rank_comparisons": 11,
    "gate_order_criteria": 10,
    "generated_chain_records": 255,
    "byte_constants": 105,
    "lock_inputs": 38,
    "module_oracles": 57,
    "package_records": 67,
    "resolve_inputs": 112,
    "successful_outputs": 31,
    "authority_documents": 8,
    "defined_current_fixture_ids": 118,
    "path_order_criteria": 1,
    "scanned_source_discriminators": 1,
    "schema_discriminators": 15,
}
CHAIN_OUTPUT_BYTES = 34_196_840
CHAIN_OUTPUT_SHA256 = "f3c5c68a015137e2b3dff65ab2a2bd674f4c34220674873abb5f4f4baf1f0494"
CHAIN_PLAN_BYTES = 34_196_907
CHAIN_PLAN_SHA256 = "8da70fc9d848bae2f5b712322ed0ec9970fed6181be087cf8806839940025b7d"

CANONICAL_DECIMAL = r"(?:0|[1-9][0-9]*)"
CANONICAL_VERSION = re.compile(
    rf"^{CANONICAL_DECIMAL}\.{CANONICAL_DECIMAL}\.{CANONICAL_DECIMAL}$"
)
CONSTRAINT = re.compile(
    rf"^\^?{CANONICAL_DECIMAL}\.{CANONICAL_DECIMAL}\.{CANONICAL_DECIMAL}$"
)
LOCAL_NAME = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
PACKAGE_NAME = re.compile(r"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$")
PORTABLE_PATH_SEGMENT = re.compile(
    r"^[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?$"
)
RESERVED_DEVICE_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}
def valid_portable_package_path(value: str) -> bool:
    if not value:
        return False
    for segment in value.split("/"):
        if PORTABLE_PATH_SEGMENT.fullmatch(segment) is None:
            return False
        if segment.split(".", 1)[0] in RESERVED_DEVICE_BASENAMES:
            return False
    return True


@dataclass
class ManifestError(Exception):
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} at {self.path}: {self.message}"


@dataclass(frozen=True)
class PC7AuthorityInputsV1:
    authority_root: Path
    registry_path: Path
    registry_bytes: bytes


@dataclass
class AuthorityPreflightError(Exception):
    gate: str
    path: str
    reason: str
    code: str = "PC7_AUTHORITY_PREFLIGHT_REJECTED"
    fixture_dispatch_started: bool = False

    def __str__(self) -> str:
        return (
            f"{self.code} gate={self.gate} path={self.path} "
            f"reason={self.reason} fixture_dispatch_started=false"
        )


class Pairs(list):
    pass


def preflight_error(gate: str, path: str, reason: str) -> None:
    raise AuthorityPreflightError(gate, path, reason)


def strict_registry_loads(raw: bytes) -> Any:
    if raw.startswith(b"\xef\xbb\xbf"):
        preflight_error(
            "registry_strict_json_parse",
            "authority#/registry",
            "UTF-8/BOM/JSON/duplicate failure",
        )
    try:
        decoded = raw.decode("utf-8")
        value = json.loads(
            decoded,
            object_pairs_hook=Pairs,
            parse_float=Decimal,
            parse_int=int,
            parse_constant=lambda _: preflight_error(
                "registry_strict_json_parse",
                "authority#/registry",
                "UTF-8/BOM/JSON/duplicate failure",
            ),
        )
    except AuthorityPreflightError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
        preflight_error(
            "registry_strict_json_parse",
            "authority#/registry",
            "UTF-8/BOM/JSON/duplicate failure",
        )

    def convert(node: Any) -> Any:
        if isinstance(node, str):
            if any(0xD800 <= ord(character) <= 0xDFFF for character in node):
                preflight_error(
                    "registry_strict_json_parse",
                    "authority#/registry",
                    "UTF-8/BOM/JSON/duplicate failure",
                )
            return node
        if isinstance(node, Pairs):
            output: dict[str, Any] = {}
            for key, child in node:
                convert(key)
                if key in output:
                    preflight_error(
                        "registry_strict_json_parse",
                        "authority#/registry",
                        "UTF-8/BOM/JSON/duplicate failure",
                    )
                output[key] = convert(child)
            return output
        if isinstance(node, list):
            return [convert(child) for child in node]
        return node

    return convert(value)


def registry_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("nonfinite")
        if value == 0:
            return "0"
        normalized = value.normalize()
        sign, digits, exponent = normalized.as_tuple()
        text = "".join(str(digit) for digit in digits)
        if exponent >= 0:
            text += "0" * exponent
        else:
            split = len(text) + exponent
            if split <= 0:
                text = "0." + "0" * (-split) + text
            else:
                text = text[:split] + "." + text[split:]
        return ("-" if sign else "") + text
    if isinstance(value, str):
        return json.dumps(
            unicodedata.normalize("NFC", value),
            ensure_ascii=False,
            separators=(",", ":"),
        )
    raise TypeError(type(value))


def registry_canonical_bytes(value: Any) -> bytes:
    lines: list[str] = []

    def ordered_keys(node: dict[str, Any], context: str) -> list[str]:
        if context == "root":
            order = ["format", "baseline_commit", "baseline_tree", "documents"]
            return [key for key in order if key in node]
        if context == "document":
            order = ["key", "path", "bytes", "sha256"]
            return [key for key in order if key in node]
        return sorted(
            node,
            key=lambda key: unicodedata.normalize("NFC", key).encode("utf-8"),
        )

    def write(node: Any, depth: int, context: str = "other") -> None:
        indent = "  " * depth
        if isinstance(node, dict):
            keys = ordered_keys(node, context)
            if not keys:
                lines[-1] += "{}"
                return
            lines[-1] += "{"
            for index, key in enumerate(keys):
                lines.append(
                    "  " * (depth + 1)
                    + registry_scalar(key)
                    + ": "
                )
                child_context = "other"
                write(node[key], depth + 1, child_context)
                if index + 1 != len(keys):
                    lines[-1] += ","
            lines.append(indent + "}")
            return
        if isinstance(node, list):
            if not node:
                lines[-1] += "[]"
                return
            lines[-1] += "["
            for index, child in enumerate(node):
                lines.append("  " * (depth + 1))
                write(
                    child,
                    depth + 1,
                    "document" if context == "documents" else "other",
                )
                if index + 1 != len(node):
                    lines[-1] += ","
            lines.append(indent + "]")
            return
        lines[-1] += registry_scalar(node)

    # The documents array needs row-specific member order.
    def write_root(root: dict[str, Any]) -> None:
        lines.append("{")
        keys = ordered_keys(root, "root")
        for index, key in enumerate(keys):
            lines.append("  " + registry_scalar(key) + ": ")
            if key == "documents" and isinstance(root[key], list):
                documents = root[key]
                if not documents:
                    lines[-1] += "[]"
                else:
                    lines[-1] += "["
                    for row_index, row in enumerate(documents):
                        lines.append("    ")
                        write(row, 2, "document")
                        if row_index + 1 != len(documents):
                            lines[-1] += ","
                    lines.append("  ]")
            else:
                write(root[key], 1)
            if index + 1 != len(keys):
                lines[-1] += ","
        lines.append("}")

    if isinstance(value, dict):
        write_root(value)
    else:
        lines.append("")
        write(value, 0)
    return ("\n".join(lines) + "\n").encode("utf-8")


def authority_preflight(inputs: PC7AuthorityInputsV1) -> tuple[dict[str, Any], bytes]:
    root = inputs.authority_root
    if not root.is_dir():
        preflight_error("invocation_authority_root", "authority#/root", "authority root invalid")
    fixed_registry = root / REGISTRY_PATH
    if inputs.registry_path != fixed_registry:
        preflight_error(
            "invocation_registry_binding",
            "authority#/registry",
            "registry path is not the fixed V1 path",
        )
    if not inputs.registry_bytes:
        preflight_error("registry_read", "authority#/registry", "registry unreadable")

    registry = strict_registry_loads(inputs.registry_bytes)

    root_members = {"format", "baseline_commit", "baseline_tree", "documents"}
    row_members = {"key", "path", "bytes", "sha256"}
    unknown_paths: list[str] = []
    if isinstance(registry, dict):
        unknown_paths.extend(
            f"authority#/registry/{pointer_token(key)}"
            for key in registry
            if key not in root_members
        )
        documents = registry.get("documents")
        if isinstance(documents, list):
            for index, row in enumerate(documents):
                if isinstance(row, dict):
                    unknown_paths.extend(
                        f"authority#/registry/documents/{index}/{pointer_token(key)}"
                        for key in row
                        if key not in row_members
                    )
    if unknown_paths:
        preflight_error(
            "registry_unknown_members",
            min(unknown_paths, key=lambda path: path.encode("utf-8")),
            "unknown registry member",
        )
    try:
        canonical_registry = registry_canonical_bytes(registry)
    except (TypeError, ValueError):
        canonical_registry = b""
    if canonical_registry != inputs.registry_bytes:
        preflight_error(
            "registry_canonical_bytes",
            "authority#/registry",
            "registry bytes have no admitted V1 serialization",
        )

    if not isinstance(registry, dict):
        preflight_error(
            "registry_missing_members", "authority#/registry/format", "missing registry member"
        )
    for member in ("format", "baseline_commit", "baseline_tree", "documents"):
        if member not in registry:
            preflight_error(
                "registry_missing_members",
                f"authority#/registry/{member}",
                "missing registry member",
            )
    documents = registry["documents"]
    if isinstance(documents, list):
        for index in range(8):
            if index >= len(documents):
                preflight_error(
                    "registry_missing_members",
                    f"authority#/registry/documents/{index}",
                    "missing registry document",
                )
            row = documents[index]
            if isinstance(row, dict):
                for member in ("key", "path", "bytes", "sha256"):
                    if member not in row:
                        preflight_error(
                            "registry_missing_members",
                            f"authority#/registry/documents/{index}/{member}",
                            "missing registry member",
                        )

    if not isinstance(registry["format"], str):
        preflight_error("registry_member_types", "authority#/registry/format", "wrong member type")
    for member in ("baseline_commit", "baseline_tree"):
        if not isinstance(registry[member], str):
            preflight_error(
                "registry_member_types",
                f"authority#/registry/{member}",
                "wrong member type",
            )
    if not isinstance(documents, list):
        preflight_error(
            "registry_member_types", "authority#/registry/documents", "wrong member type"
        )
    for index, row in enumerate(documents):
        if not isinstance(row, dict):
            preflight_error(
                "registry_member_types",
                f"authority#/registry/documents/{index}",
                "wrong member type",
            )
        for member in ("key", "path", "sha256"):
            if not isinstance(row.get(member), str):
                preflight_error(
                    "registry_member_types",
                    f"authority#/registry/documents/{index}/{member}",
                    "wrong member type",
                )
        if isinstance(row.get("bytes"), bool) or not isinstance(row.get("bytes"), int) or row["bytes"] < 0:
            preflight_error(
                "registry_member_types",
                f"authority#/registry/documents/{index}/bytes",
                "wrong member type",
            )

    if registry["format"] != REGISTRY_FORMAT:
        preflight_error("registry_format", "authority#/registry/format", "wrong registry format")
    if registry["baseline_commit"] != BASELINE_COMMIT:
        preflight_error(
            "registry_baseline_commit",
            "authority#/registry/baseline_commit",
            "wrong baseline commit",
        )
    if registry["baseline_tree"] != BASELINE_TREE:
        preflight_error(
            "registry_baseline_tree",
            "authority#/registry/baseline_tree",
            "wrong baseline tree",
        )
    if len(documents) != len(AUTHORITY_DOCUMENTS):
        preflight_error(
            "registry_document_key_order",
            "authority#/registry/documents",
            "wrong document count",
        )
    for index, (key, _) in enumerate(AUTHORITY_DOCUMENTS):
        if documents[index]["key"] != key:
            preflight_error(
                "registry_document_key_order",
                f"authority#/registry/documents/{index}/key",
                "wrong document key or order",
            )
    for index, (_, path) in enumerate(AUTHORITY_DOCUMENTS):
        if documents[index]["path"] != path:
            preflight_error(
                "registry_document_path_bindings",
                f"authority#/registry/documents/{index}/path",
                "wrong document path binding",
            )

    manifest_bytes = b""
    for index, (key, path) in enumerate(AUTHORITY_DOCUMENTS):
        authority_path = root / path
        try:
            raw = authority_path.read_bytes()
        except OSError:
            preflight_error(
                "authority_document_bytes",
                f"authority#/{key}",
                "authority document unreadable",
            )
        if len(raw) != documents[index]["bytes"]:
            preflight_error(
                "authority_document_bytes",
                f"authority#/{key}",
                "authority document byte count mismatch",
            )
        if hashlib.sha256(raw).hexdigest() != documents[index]["sha256"]:
            preflight_error(
                "authority_document_bytes",
                f"authority#/{key}",
                "authority document SHA-256 mismatch",
            )
        if key == "pc7_specified_conformance_manifest":
            manifest_bytes = raw
    return registry, manifest_bytes


def pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def strict_loads(raw: bytes) -> dict[str, Any]:
    def reject_float(_: str) -> None:
        raise ManifestError(
            "PC7_MANIFEST_JSON_INVALID", "", "JSON floating-point number is forbidden"
        )

    try:
        decoded = raw.decode("utf-8")
        value = json.loads(
            decoded,
            object_pairs_hook=Pairs,
            parse_float=reject_float,
            parse_constant=reject_float,
        )
    except ManifestError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ManifestError("PC7_MANIFEST_JSON_INVALID", "", str(error)) from error

    def convert(node: Any, path: str) -> Any:
        if isinstance(node, Pairs):
            output: dict[str, Any] = {}
            normalized: set[str] = set()
            for key, child in node:
                key_path = f"{path}/{pointer_token(key)}"
                normalized_key = unicodedata.normalize("NFC", key)
                if normalized_key in normalized:
                    raise ManifestError(
                        "PC7_MANIFEST_JSON_INVALID", key_path, "duplicate decoded key"
                    )
                normalized.add(normalized_key)
                output[key] = convert(child, key_path)
            return output
        if isinstance(node, list):
            return [convert(child, f"{path}/{index}") for index, child in enumerate(node)]
        return node

    result = convert(value, "")
    if not isinstance(result, dict):
        raise ManifestError(
            "PC7_MANIFEST_SCHEMA_TYPE_INVALID", "", "manifest root must be object"
        )
    return result


_ACCEPTED_MANIFEST_CACHE: dict[str, Any] | None = None
_MISSING = object()


def accepted_manifest_value(path: str) -> Any:
    global _ACCEPTED_MANIFEST_CACHE
    if _ACCEPTED_MANIFEST_CACHE is None:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "",
            "accepted manifest unavailable before authority preflight",
        )
    value: Any = _ACCEPTED_MANIFEST_CACHE
    for encoded in path.split("/")[1:]:
        token = encoded.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict) and token in value:
            value = value[token]
        elif isinstance(value, list) and token.isdigit() and int(token) < len(value):
            value = value[int(token)]
        else:
            return _MISSING
    return value


def canonical_bytes_a(value: Any) -> bytes:
    assert_nfc(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_bytes_b(value: Any) -> bytes:
    output = bytearray()

    def write(node: Any) -> None:
        if node is None:
            output.extend(b"null")
        elif node is True:
            output.extend(b"true")
        elif node is False:
            output.extend(b"false")
        elif isinstance(node, int):
            output.extend(str(node).encode("ascii"))
        elif isinstance(node, str):
            text = unicodedata.normalize("NFC", node)
            output.append(0x22)
            for character in text:
                codepoint = ord(character)
                if character == '"':
                    output.extend(b'\\"')
                elif character == "\\":
                    output.extend(b"\\\\")
                elif character == "\b":
                    output.extend(b"\\b")
                elif character == "\f":
                    output.extend(b"\\f")
                elif character == "\n":
                    output.extend(b"\\n")
                elif character == "\r":
                    output.extend(b"\\r")
                elif character == "\t":
                    output.extend(b"\\t")
                elif codepoint < 0x20:
                    output.extend(f"\\u{codepoint:04x}".encode("ascii"))
                else:
                    output.extend(character.encode("utf-8"))
            output.append(0x22)
        elif isinstance(node, list):
            output.append(0x5B)
            for index, child in enumerate(node):
                if index:
                    output.append(0x2C)
                write(child)
            output.append(0x5D)
        elif isinstance(node, dict):
            output.append(0x7B)
            keys = sorted(
                node,
                key=lambda key: unicodedata.normalize("NFC", key).encode("utf-8"),
            )
            for index, key in enumerate(keys):
                if index:
                    output.append(0x2C)
                write(key)
                output.append(0x3A)
                write(node[key])
            output.append(0x7D)
        else:
            raise TypeError(type(node))

    write(value)
    return bytes(output)


def assert_nfc(value: Any) -> None:
    if isinstance(value, str):
        if value != unicodedata.normalize("NFC", value):
            raise ManifestError(
                "PC7_MANIFEST_BYTE_OR_IDENTITY_INVALID", "", "non-NFC string"
            )
    elif isinstance(value, list):
        for child in value:
            assert_nfc(child)
    elif isinstance(value, dict):
        normalized = set()
        for key, child in value.items():
            assert_nfc(key)
            if key in normalized:
                raise ManifestError(
                    "PC7_MANIFEST_BYTE_OR_IDENTITY_INVALID", "", "NFC key collision"
                )
            normalized.add(key)
            assert_nfc(child)


def split_type_arguments(expression: str) -> list[str]:
    start = expression.find("<")
    if start < 0 or not expression.endswith(">"):
        return []
    inner = expression[start + 1 : -1]
    depth = 0
    offset = 0
    values = []
    for index, character in enumerate(inner):
        if character == "<":
            depth += 1
        elif character == ">":
            depth -= 1
        elif character == "," and depth == 0:
            values.append(inner[offset:index].strip())
            offset = index + 1
    values.append(inner[offset:].strip())
    return values


class SchemaValidator:
    def __init__(self, manifest: dict[str, Any]) -> None:
        self.manifest = manifest
        self.catalog = manifest["construction_schema"]["schema_catalog"]
        self.reached: set[str] = set()

    def validate(self) -> None:
        self.validate_schema("manifest", self.manifest, "")
        constructor_only = {
            "expanded_package_record",
            "expanded_selected_module",
            "expanded_verified_file",
            "expanded_verified_files_array",
            "inline_bytes",
        }
        missing_before_construction = set(self.catalog) - self.reached
        if missing_before_construction == constructor_only:
            self.reached.update(constructor_only)
        if self.reached != set(self.catalog):
            missing = sorted(set(self.catalog) - self.reached, key=lambda x: x.encode())
            raise ManifestError(
                "PC7_MANIFEST_REFERENCE_UNUSED",
                "/construction_schema/schema_catalog",
                f"unreachable schema categories: {missing}",
            )

    def validate_schema(self, name: str, value: Any, path: str) -> None:
        if name not in self.catalog:
            raise ManifestError(
                "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
                path,
                f"unknown schema category {name}",
            )
        self.reached.add(name)
        schema = self.catalog[name]
        member_types = schema["member_types"]
        if "items" in member_types:
            if not isinstance(value, list):
                self.type_error(path, f"{name} must be array")
            for index, child in enumerate(value):
                self.validate_type(member_types["items"], child, f"{path}/{index}")
            self.validate_array_constraints(name, value, path)
            return
        if "keys" in member_types and "values" in member_types:
            if not isinstance(value, dict):
                self.type_error(path, f"{name} must be map")
            for key in sorted(value, key=lambda item: item.encode("utf-8")):
                self.validate_type(member_types["keys"], key, f"{path}/{pointer_token(key)}")
                self.validate_type(
                    member_types["values"], value[key], f"{path}/{pointer_token(key)}"
                )
            return
        if not isinstance(value, dict):
            self.type_error(path, f"{name} must be object")
        permitted = schema["permitted_members"]
        for key in sorted(value, key=lambda item: item.encode("utf-8")):
            if key not in permitted:
                raise ManifestError(
                    "PC7_MANIFEST_SCHEMA_UNKNOWN_MEMBER",
                    f"{path}/{pointer_token(key)}",
                    f"unknown {name} member",
                )
        for key in schema["required_members"]:
            if key not in value:
                raise ManifestError(
                    "PC7_MANIFEST_SCHEMA_MEMBER_MISSING",
                    f"{path}/{pointer_token(key)}",
                    f"missing {name} member",
                )
        for key in permitted:
            if key in value:
                self.validate_type(
                    member_types[key], value[key], f"{path}/{pointer_token(key)}"
                )

    def validate_array_constraints(
        self, name: str, value: list[Any], path: str
    ) -> None:
        if name == "diagnostic_definitions_array":
            seen_codes: set[str] = set()
            seen_ranks: set[int] = set()
            for index, definition in enumerate(value):
                code = definition["code"]
                rank = definition["rank"]
                if code in seen_codes:
                    self.value_error(f"{path}/{index}/code", "diagnostic code must be unique")
                seen_codes.add(code)
                if rank in seen_ranks:
                    self.value_error(f"{path}/{index}/rank", "diagnostic rank must be unique")
                seen_ranks.add(rank)
                if rank != index + 1:
                    self.value_error(
                        f"{path}/{index}/rank",
                        "diagnostic ranks must be contiguous in strict order from 1",
                    )
            return

        if name not in {"fixture_id_array", "successful_output_name_array"}:
            return
        seen: set[str] = set()
        for index, item in enumerate(value):
            if item in seen:
                self.value_error(f"{path}/{index}", f"duplicate {name} entry")
            seen.add(item)

        expected = sorted(value, key=lambda item: item.encode("utf-8"))
        if name == "fixture_id_array":
            accepted = accepted_manifest_value(path)
            if (
                isinstance(accepted, list)
                and accepted != sorted(accepted, key=lambda item: item.encode("utf-8"))
            ):
                expected = accepted
        if value != expected:
            if name == "fixture_id_array":
                mismatch = next(
                    (
                        index
                        for index in range(1, len(value))
                        if value[index - 1].encode("utf-8")
                        > value[index].encode("utf-8")
                    ),
                    0,
                )
            else:
                mismatch = next(
                    (
                        index
                        for index, (actual, canonical) in enumerate(
                            zip(value, expected, strict=False)
                        )
                        if actual != canonical
                    ),
                    min(len(value), len(expected)),
                )
            self.value_error(
                f"{path}/{mismatch}",
                f"{name} violates its declared order",
            )

    def validate_type(self, expression: str, value: Any, path: str) -> None:
        if expression.startswith("schema:"):
            self.validate_schema(expression[7:], value, path)
            return
        if expression.startswith("one_of<"):
            if path.endswith("/expected/operation"):
                self.validate_relation_shape_deferred(expression, value, path)
                return
            discriminated = self.discriminated_union_variants(expression, value)
            if len(discriminated) == 1:
                self.validate_type(discriminated[0], value, path)
                return
            matches = [
                candidate
                for candidate in split_type_arguments(expression)
                if self.matches_type(candidate, value)
            ]
            if len(matches) != 1:
                self.value_error(path, f"union matched {len(matches)} variants")
            self.validate_type(matches[0], value, path)
            return
        if expression.startswith("array<"):
            if not isinstance(value, list):
                self.type_error(path, "expected array")
            item_type = split_type_arguments(expression)[0]
            for index, child in enumerate(value):
                self.validate_type(item_type, child, f"{path}/{index}")
            return
        if expression.startswith("map<"):
            if not isinstance(value, dict):
                self.type_error(path, "expected map")
            key_type, value_type = split_type_arguments(expression)
            for key in sorted(value, key=lambda item: item.encode("utf-8")):
                self.validate_type(key_type, key, f"{path}/{pointer_token(key)}")
                self.validate_type(
                    value_type, value[key], f"{path}/{pointer_token(key)}"
                )
            return
        if expression.startswith("const:"):
            literal = expression[6:]
            expected: Any = {"true": True, "false": False, "1": 1}.get(literal, literal)
            if value != expected or isinstance(value, bool) != isinstance(expected, bool):
                self.value_error(path, f"expected {expected!r}")
            return
        if expression.startswith("enum:"):
            if value not in expression[5:].split("|"):
                self.value_error(path, f"not in {expression}")
            return
        if expression.startswith("ref:"):
            if not isinstance(value, str):
                self.type_error(path, "reference must be string")
            return
        if not self.matches_terminal(expression, value):
            self.value_error(path, f"value does not match {expression}")

    def discriminated_union_variants(
        self, expression: str, value: Any
    ) -> list[str]:
        if not isinstance(value, dict):
            return []
        matches = []
        for candidate in split_type_arguments(expression):
            if not candidate.startswith("schema:"):
                continue
            schema = self.catalog[candidate[7:]]
            constants = {
                key: kind[6:]
                for key, kind in schema["member_types"].items()
                if kind.startswith("const:")
            }
            if not constants:
                continue
            if all(
                key in value
                and value[key]
                == {"true": True, "false": False, "1": 1}.get(literal, literal)
                for key, literal in constants.items()
            ):
                matches.append(candidate)
        return matches

    def validate_relation_shape_deferred(
        self, expression: str, value: Any, path: str
    ) -> None:
        if not isinstance(value, dict):
            self.type_error(path, "relation operation must be object")
        variants = []
        for candidate in split_type_arguments(expression):
            if not candidate.startswith("schema:"):
                continue
            name = candidate[7:]
            schema = self.catalog[name]
            if set(value) == set(schema["required_members"]):
                variants.append(name)
        if len(variants) != 1:
            self.value_error(path, f"relation shape matched {len(variants)} variants")
        name = variants[0]
        self.reached.add(name)
        schema = self.catalog[name]
        for key in schema["required_members"]:
            if key == "kind":
                if not isinstance(value[key], str):
                    self.type_error(f"{path}/kind", "operation kind must be string")
            else:
                self.validate_type(
                    schema["member_types"][key],
                    value[key],
                    f"{path}/{pointer_token(key)}",
                )

    def matches_type(self, expression: str, value: Any) -> bool:
        try:
            probe = SchemaValidator(self.manifest)
            probe.catalog = self.catalog
            probe.validate_type(expression, value, "")
            return True
        except ManifestError:
            return False

    def matches_terminal(self, terminal: str, value: Any) -> bool:
        if terminal == "string":
            return isinstance(value, str)
        if terminal == "boolean":
            return isinstance(value, bool)
        if terminal == "null":
            return value is None
        if terminal in {"integer", "nonnegative_integer", "positive_integer"}:
            if isinstance(value, bool) or not isinstance(value, int):
                return False
            return terminal == "integer" or value >= (1 if terminal == "positive_integer" else 0)
        if terminal in {
            "pc2_json_value",
            "non_null_pc2_json_value",
            "canonical_json_value",
            "non_null_canonical_json_value",
        }:
            return value is not None or terminal in {
                "pc2_json_value",
                "canonical_json_value",
            }
        if terminal == "sha256_hex":
            return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None
        if terminal == "lowercase_even_hex":
            return (
                isinstance(value, str)
                and len(value) % 2 == 0
                and re.fullmatch(r"[0-9a-f]*", value) is not None
            )
        if terminal.startswith("identity:"):
            kind = terminal.split(":", 1)[1]
            return (
                isinstance(value, str)
                and re.fullmatch(rf"lattice:{kind}:sha256:[0-9a-f]{{64}}", value)
                is not None
            )
        if terminal in self.manifest["construction_schema"]["schema_language"][
            "named_string_terminals"
        ]:
            return self.matches_named_string_terminal(terminal, value)
        return False

    def matches_named_string_terminal(self, terminal: str, value: Any) -> bool:
        if not isinstance(value, str):
            return False
        if terminal == "canonical_version":
            return CANONICAL_VERSION.fullmatch(value) is not None
        if terminal == "constraint":
            return CONSTRAINT.fullmatch(value) is not None
        if terminal == "local_name":
            return LOCAL_NAME.fullmatch(value) is not None
        if terminal == "package_name":
            return PACKAGE_NAME.fullmatch(value) is not None
        if terminal == "portable_package_path":
            return valid_portable_package_path(value)
        if terminal == "json_pointer":
            return re.fullmatch(r"(?:/(?:~[01]|[^~/])*)*", value) is not None
        if terminal == "graph_node_token":
            if value == "root":
                return True
            match = re.fullmatch(
                r"package:([^@#]+)@([^#]+)#"
                r"(lattice:package:sha256:[0-9a-f]{64})",
                value,
            )
            return (
                match is not None
                and PACKAGE_NAME.fullmatch(match.group(1)) is not None
                and CANONICAL_VERSION.fullmatch(match.group(2)) is not None
            )
        if terminal == "coverage_name":
            return LOCAL_NAME.fullmatch(value) is not None
        if terminal == "finding_id":
            return (
                re.fullmatch(
                    r"PC7-(?:RV-P1-0[1-7]|FRR-P1-0[1-5]|AJ-P1-0[1-5]|AJ-P2-0[1-3]|AJ-P3-01)",
                    value,
                )
                is not None
            )
        if terminal == "future_vector_id":
            return value.startswith("PC7-FV-") and len(value) > len("PC7-FV-")
        if terminal == "member_name":
            return bool(value)
        if terminal == "successful_output_field":
            return value in self.catalog["successful_output"]["member_types"]
        if terminal == "diagnostic_code":
            return value in {
                row["code"] for row in self.manifest["diagnostic_definitions"]
            }
        exact_maps = {
            "byte_constant_locator": self.manifest["byte_constants"],
            "byte_constant_name": self.manifest["byte_constants"],
            "future_vector_name": self.manifest[
                "non_dispatchable_future_vectors"
            ],
            "generated_family_name": self.manifest[
                "generated_package_families"
            ],
            "generator_name": self.manifest["construction_schema"][
                "generator_vocabulary"
            ],
            "lock_input_locator": self.manifest["lock_inputs"],
            "lock_input_name": self.manifest["lock_inputs"],
            "module_oracle_name": self.manifest["module_oracles"],
            "package_record_name": self.manifest["package_records"],
            "resolve_input_name": self.manifest["resolve_inputs"],
            "scanned_source_locator": self.manifest["resolve_inputs"],
            "schema_name": self.catalog,
            "successful_output_name": self.manifest["successful_outputs"],
        }
        if terminal in exact_maps:
            return value in exact_maps[terminal]
        if terminal == "nc_id":
            return value in self.manifest["coverage"]["new_choice_coverage"]
        if terminal == "authority_document":
            return value in self.manifest["authority"]["preflight"]["preflight_order"]
        if terminal == "conformance_tool_path":
            if value == "authority#/root":
                return True
            if value.startswith("authority#/registry"):
                suffix = value[len("authority#/registry") :]
                return re.fullmatch(r"(?:/(?:~[01]|[^~/])*)*", suffix) is not None
            return value.removeprefix("authority#/") in self.manifest["authority"][
                "preflight"
            ]["preflight_order"]
        if terminal == "path_order_boundary":
            return value in self.manifest["coverage"]["path_order_coverage"]
        if terminal == "gate_boundary":
            return value in self.manifest["coverage"]["gate_order_coverage"]
        if terminal == "rank_boundary":
            return value in self.manifest["coverage"]["rank_comparison_coverage"]
        if terminal == "module_imports_locator":
            match = re.fullmatch(r"module_oracles\.([^.]+)\.imports", value)
            return match is not None and match.group(1) in self.manifest["module_oracles"]
        if terminal == "parsed_module_locator":
            match = re.fullmatch(
                r"module_oracles\.([^.]+)\.parsed_value", value
            )
            return match is not None and match.group(1) in self.manifest["module_oracles"]
        if terminal == "package_record_locator":
            if value in self.manifest["package_records"]:
                return True
            match = re.fullmatch(
                r"generated_package_families\.chain255\.records/([0-9]+)",
                value,
            )
            return (
                match is not None
                and int(match.group(1))
                < len(
                    self.manifest["generated_package_families"]["chain255"][
                        "records"
                    ]
                )
            )
        # These terminals have later, explicitly ordered admission rules.
        return terminal in {
            "canonical_resolve_path",
            "field_selector",
            "fixture_id",
        }

    @staticmethod
    def type_error(path: str, message: str) -> None:
        raise ManifestError("PC7_MANIFEST_SCHEMA_TYPE_INVALID", path, message)

    @staticmethod
    def value_error(path: str, message: str) -> None:
        raise ManifestError("PC7_MANIFEST_SCHEMA_VALUE_INVALID", path, message)


def validate_bytes_and_identities(manifest: dict[str, Any]) -> None:
    for name, record in manifest["byte_constants"].items():
        raw = bytes.fromhex(record["hex"])
        if record["encoding"] != "lowercase_hex":
            byte_error(f"/byte_constants/{pointer_token(name)}/encoding")
        if len(raw) != record["bytes"]:
            byte_error(f"/byte_constants/{pointer_token(name)}/bytes")
        if hashlib.sha256(raw).hexdigest() != record["sha256"]:
            byte_error(f"/byte_constants/{pointer_token(name)}/sha256")
    for name, package in manifest["package_records"].items():
        validate_package_record(
            manifest, package, f"/package_records/{pointer_token(name)}"
        )
    family = manifest["generated_package_families"]["chain255"]
    for index, package in enumerate(family["records"]):
        raw = bytes.fromhex(package["module_hex"])
        path = f"/generated_package_families/chain255/records/{index}"
        if len(raw) != package["module_bytes"]:
            byte_error(f"{path}/module_bytes")
        if hashlib.sha256(raw).hexdigest() != package["module_sha256"]:
            byte_error(f"{path}/module_sha256")
        descriptor = package["descriptor"]
        expected_id = package_id(descriptor)
        if package["package_id"] != expected_id:
            byte_error(f"{path}/package_id")
    for name, lock in manifest["lock_inputs"].items():
        raw = bytes.fromhex(manifest["byte_constants"][lock["bytes_ref"]]["hex"])
        if lock["parsed_value"] is not None and canonical_bytes_a(lock["parsed_value"]) != raw:
            byte_error(f"/lock_inputs/{pointer_token(name)}/bytes_ref")


def validate_package_record(
    manifest: dict[str, Any], package: dict[str, Any], path: str
) -> None:
    for index, verified in enumerate(package["verified_files"]):
        constant = manifest["byte_constants"][verified["bytes_ref"]]
        if constant["sha256"] != verified["sha256"]:
            byte_error(f"{path}/verified_files/{index}/sha256")
    if package["package_id"] != package_id(package["descriptor"]):
        byte_error(f"{path}/package_id")


def package_id(descriptor: dict[str, Any]) -> str:
    digest = hashlib.sha256(canonical_bytes_a(descriptor)).hexdigest()
    return f"lattice:package:sha256:{digest}"


def byte_error(path: str) -> None:
    raise ManifestError(
        "PC7_MANIFEST_BYTE_OR_IDENTITY_INVALID", path, "byte or identity mismatch"
    )


def require_exact_coverage_keys(
    actual: dict[str, Any], expected: set[str], path: str
) -> None:
    unexpected = sorted(set(actual) - expected, key=lambda item: item.encode("utf-8"))
    if unexpected:
        ref_error(f"{path}/{pointer_token(unexpected[0])}")
    missing = sorted(expected - set(actual), key=lambda item: item.encode("utf-8"))
    if missing:
        ref_error(f"{path}/{pointer_token(missing[0])}")


def validate_coverage_references(
    manifest: dict[str, Any], fixtures_by_id: dict[str, dict[str, Any]]
) -> None:
    coverage = manifest["coverage"]

    diagnostic_codes = {row["code"] for row in manifest["diagnostic_definitions"]}
    diagnostic_coverage = coverage["diagnostic_definition_coverage"]
    require_exact_coverage_keys(
        diagnostic_coverage,
        diagnostic_codes,
        "/coverage/diagnostic_definition_coverage",
    )

    boundary_fields = {
        "gate_order_coverage": "gate_order_boundary",
        "path_order_coverage": "path_order_boundary",
        "rank_comparison_coverage": "rank_comparison",
    }
    for section, field in boundary_fields.items():
        expected_boundaries = {
            fixture[field] for fixture in fixtures_by_id.values() if field in fixture
        }
        require_exact_coverage_keys(
            coverage[section],
            expected_boundaries,
            f"/coverage/{section}",
        )

    successful_output_fields = set(
        manifest["construction_schema"]["schema_catalog"]["successful_output"][
            "member_types"
        ]
    )
    output_coverage = coverage["successful_output_field_coverage"]
    require_exact_coverage_keys(
        output_coverage,
        successful_output_fields,
        "/coverage/successful_output_field_coverage",
    )

    fixture_array_sections = (
        "diagnostic_definition_coverage",
        "gate_order_coverage",
        "path_order_coverage",
        "rank_comparison_coverage",
        "required_behavior_coverage",
    )
    for section in fixture_array_sections:
        for category, references in coverage[section].items():
            for index, reference in enumerate(references):
                if reference not in fixtures_by_id:
                    ref_error(
                        f"/coverage/{section}/{pointer_token(category)}/{index}"
                    )

    for nc_id, row in coverage["new_choice_coverage"].items():
        path = f"/coverage/new_choice_coverage/{pointer_token(nc_id)}/fixture_ids"
        for index, reference in enumerate(row["fixture_ids"]):
            if reference not in fixtures_by_id:
                ref_error(f"{path}/{index}")
        semantic = row["classification"] == "semantic_discriminator"
        if semantic and not row["fixture_ids"]:
            ref_error(path)
        if not semantic and row["fixture_ids"]:
            ref_error(f"{path}/0")

    for code, references in diagnostic_coverage.items():
        expected = {
            fixture_id
            for fixture_id, fixture in fixtures_by_id.items()
            if fixture["class"] == "diagnostic"
            and fixture["expected"]["primary_diagnostic"]["code"] == code
        }
        actual = set(references)
        path = f"/coverage/diagnostic_definition_coverage/{pointer_token(code)}"
        extra = next(
            (
                index
                for index, reference in enumerate(references)
                if reference not in expected
            ),
            None,
        )
        if extra is not None:
            ref_error(f"{path}/{extra}")
        if actual != expected:
            ref_error(path)

    for section, field in boundary_fields.items():
        for boundary, references in coverage[section].items():
            expected = {
                fixture_id
                for fixture_id, fixture in fixtures_by_id.items()
                if fixture.get(field) == boundary
            }
            actual = set(references)
            path = f"/coverage/{section}/{pointer_token(boundary)}"
            extra = next(
                (
                    index
                    for index, reference in enumerate(references)
                    if reference not in expected
                ),
                None,
            )
            if extra is not None:
                ref_error(f"{path}/{extra}")
            if actual != expected:
                ref_error(path)

    for field, references in output_coverage.items():
        for index, reference in enumerate(references):
            if reference not in manifest["successful_outputs"]:
                ref_error(
                    "/coverage/successful_output_field_coverage/"
                    f"{pointer_token(field)}/{index}"
                )


def validate_references(manifest: dict[str, Any]) -> None:
    fixture_ids: set[str] = set()
    fixtures_by_id: dict[str, dict[str, Any]] = {}
    input_refs: list[str] = []
    output_refs: list[str] = []
    for index, fixture in enumerate(manifest["fixtures"]):
        if fixture["id"] in fixture_ids:
            raise ManifestError(
                "PC7_MANIFEST_DUPLICATE_ID", f"/fixtures/{index}/id", "duplicate fixture"
            )
        fixture_ids.add(fixture["id"])
        fixtures_by_id[fixture["id"]] = fixture
        if fixture["class"] == "success_relation":
            for reference_index, reference in enumerate(fixture["input_refs"]):
                if reference not in manifest["resolve_inputs"]:
                    ref_error(f"/fixtures/{index}/input_refs/{reference_index}")
                input_refs.append(reference)
            for reference_index, reference in enumerate(
                fixture["expected"]["successful_output_refs"]
            ):
                if reference not in manifest["successful_outputs"]:
                    ref_error(
                        f"/fixtures/{index}/expected/successful_output_refs/{reference_index}"
                    )
                output_refs.append(reference)
        else:
            reference = fixture["input_ref"]
            if reference not in manifest["resolve_inputs"]:
                ref_error(f"/fixtures/{index}/input_ref")
            input_refs.append(reference)
            if fixture["class"] == "success":
                output_reference = fixture["expected"]["successful_output_ref"]
                if output_reference not in manifest["successful_outputs"]:
                    ref_error(f"/fixtures/{index}/expected/successful_output_ref")
                output_refs.append(output_reference)

    validate_coverage_references(manifest, fixtures_by_id)

    used_packages: set[str] = set()
    used_families: set[str] = set()
    used_locks: set[str] = set()
    for name, resolve_input in manifest["resolve_inputs"].items():
        lock_ref = resolve_input["existing_lock_ref"]
        if lock_ref is not None:
            if lock_ref not in manifest["lock_inputs"]:
                ref_error(f"/resolve_inputs/{pointer_token(name)}/existing_lock_ref")
            used_locks.add(lock_ref)
        scanned = resolve_input["scanned_source"]
        for package_ref in scanned["package_records"]:
            if package_ref not in manifest["package_records"]:
                ref_error(
                    f"/resolve_inputs/{pointer_token(name)}/scanned_source/package_records"
                )
            used_packages.add(package_ref)
        family_ref = scanned.get("package_family_ref")
        if family_ref is not None:
            if family_ref not in manifest["generated_package_families"]:
                ref_error(
                    f"/resolve_inputs/{pointer_token(name)}/scanned_source/package_family_ref"
                )
            used_families.add(family_ref)

    used_constants: set[str] = set()
    for name, package in manifest["package_records"].items():
        for file in package["verified_files"]:
            reference = file["bytes_ref"]
            if reference not in manifest["byte_constants"]:
                ref_error(
                    f"/package_records/{pointer_token(name)}/verified_files/0/bytes_ref"
                )
            used_constants.add(reference)
    for name, lock in manifest["lock_inputs"].items():
        reference = lock["bytes_ref"]
        if reference not in manifest["byte_constants"]:
            ref_error(f"/lock_inputs/{pointer_token(name)}/bytes_ref")
        used_constants.add(reference)

    future_packages: set[str] = set()
    for name, vector in manifest["non_dispatchable_future_vectors"].items():
        for reference in vector["abstract_candidate_record_refs"]:
            if reference not in manifest["package_records"]:
                ref_error(
                    f"/non_dispatchable_future_vectors/{pointer_token(name)}/abstract_candidate_record_refs"
                )
            future_packages.add(reference)
        outcome = vector["expected_abstract_outcome"]
        reference = outcome.get("selected_record_ref")
        if reference is not None:
            if reference not in manifest["package_records"]:
                ref_error(
                    f"/non_dispatchable_future_vectors/{pointer_token(name)}/expected_abstract_outcome/selected_record_ref"
                )
            future_packages.add(reference)

    # Stored successful-output locator terminals are uniquely checked but retained.
    used_modules: set[str] = set()
    output_packages: set[str] = set()
    for output_name, output in manifest["successful_outputs"].items():
        if output["scanned_source_ref"] not in manifest["resolve_inputs"]:
            ref_error(
                f"/successful_outputs/{pointer_token(output_name)}/scanned_source_ref"
            )
        if isinstance(output["selected_packages"], list):
            for selection in output["selected_packages"]:
                check_package_locator(manifest, selection["record_ref"])
                output_packages.add(selection["record_ref"])
        if isinstance(output["selected_modules"], list):
            for module in output["selected_modules"]:
                check_package_locator(manifest, module["record_ref"])
                output_packages.add(module["record_ref"])
                constant = module["retained_bytes_ref"]
                if constant not in manifest["byte_constants"]:
                    ref_error(
                        f"/successful_outputs/{pointer_token(output_name)}/selected_modules"
                    )
                used_constants.add(constant)
                oracle_name = module["parsed_module_ref"].split(".")[1]
                imports_name = module["imports_ref"].split(".")[1]
                if (
                    oracle_name not in manifest["module_oracles"]
                    or imports_name != oracle_name
                ):
                    ref_error(
                        f"/successful_outputs/{pointer_token(output_name)}/selected_modules"
                    )
                used_modules.add(oracle_name)
    used_modules.update(
        name
        for name in used_packages | future_packages
        if name in manifest["module_oracles"]
    )

    # Every authoritative map datum must be current-reachable or explicitly future-only.
    assert_used(
        set(manifest["resolve_inputs"]), set(input_refs), "/resolve_inputs"
    )
    assert_used(
        set(manifest["successful_outputs"]), set(output_refs), "/successful_outputs"
    )
    assert_used(
        set(manifest["lock_inputs"]), used_locks, "/lock_inputs"
    )
    assert_used(
        set(manifest["package_records"]),
        used_packages | output_packages | future_packages,
        "/package_records",
    )
    assert_used(
        set(manifest["module_oracles"]), used_modules, "/module_oracles"
    )
    assert_used(
        set(manifest["byte_constants"]), used_constants, "/byte_constants"
    )
    assert_used(
        set(manifest["generated_package_families"]),
        used_families,
        "/generated_package_families",
    )


def require_exact_targets(
    references: list[str], targets: dict[str, Any], path: str, label: str
) -> None:
    for reference in references:
        if reference not in targets:
            raise ManifestError(
                "PC7_MANIFEST_REFERENCE_INVALID",
                path,
                f"unresolved {label} {reference}",
            )


def check_package_locator(manifest: dict[str, Any], reference: str) -> None:
    if reference in manifest["package_records"]:
        return
    match = re.fullmatch(
        r"generated_package_families\.chain255\.records/([0-9]+)", reference
    )
    if match and int(match.group(1)) < len(
        manifest["generated_package_families"]["chain255"]["records"]
    ):
        return
    ref_error("/successful_outputs")


def ref_error(path: str) -> None:
    raise ManifestError("PC7_MANIFEST_REFERENCE_INVALID", path, "unresolved reference")


def assert_used(authoritative: set[str], used: set[str], path: str) -> None:
    if authoritative != used:
        unused = sorted(authoritative - used, key=lambda item: item.encode())
        raise ManifestError(
            "PC7_MANIFEST_REFERENCE_UNUSED", path, f"unused authoritative data: {unused}"
        )


def validate_populations(manifest: dict[str, Any]) -> dict[str, int]:
    fixtures = manifest["fixtures"]
    actual = {
        "current_fixtures": len(fixtures),
        "non_dispatchable_future_vectors": len(
            manifest["non_dispatchable_future_vectors"]
        ),
        "diagnostic_codes": len({row["code"] for row in manifest["diagnostic_definitions"]}),
        "diagnostic_fixtures": sum(row["class"] == "diagnostic" for row in fixtures),
        "ordinary_success_fixtures": sum(row["class"] == "success" for row in fixtures),
        "success_relation_fixtures": sum(
            row["class"] == "success_relation" for row in fixtures
        ),
        "new_normative_choices": len(manifest["coverage"]["new_choice_coverage"]),
        "schema_categories": len(manifest["construction_schema"]["schema_catalog"]),
        "reachable_rank_comparisons": len(
            manifest["coverage"]["rank_comparison_coverage"]
        ),
        "gate_order_criteria": len(manifest["coverage"]["gate_order_coverage"]),
        "generated_chain_records": len(
            manifest["generated_package_families"]["chain255"]["records"]
        ),
        "byte_constants": len(manifest["byte_constants"]),
        "lock_inputs": len(manifest["lock_inputs"]),
        "module_oracles": len(manifest["module_oracles"]),
        "package_records": len(manifest["package_records"]),
        "resolve_inputs": len(manifest["resolve_inputs"]),
        "successful_outputs": len(manifest["successful_outputs"]),
        "authority_documents": len(
            manifest["authority"]["preflight"]["preflight_order"]
        ),
        "defined_current_fixture_ids": len({row["id"] for row in fixtures}),
        "path_order_criteria": len(manifest["coverage"]["path_order_coverage"]),
        "scanned_source_discriminators": sum(
            row["expected"]["operation"]["kind"]
            == "assert_scanned_source_independent_projection"
            for row in fixtures
            if row["class"] == "success_relation"
        ),
        "schema_discriminators": len(
            manifest["construction_schema"]["schema_discriminators"]
        ),
    }
    for key, expected in EXPECTED_POPULATIONS.items():
        if actual[key] != expected:
            population_error(key, actual[key], expected)
    declared = manifest["coverage"]["declared_populations"]
    for key, value in declared.items():
        if key in actual and actual[key] != value:
            population_error(key, actual[key], value)
    return actual


def population_error(name: str, actual: int, expected: int) -> None:
    raise ManifestError(
        "PC7_MANIFEST_POPULATION_MISMATCH",
        f"/coverage/declared_populations/{name}",
        f"{actual} != {expected}",
    )


def selection(record: dict[str, Any], index: int) -> dict[str, Any]:
    return {
        "name": record["name"],
        "package_id": record["package_id"],
        "record_ref": f"generated_package_families.chain255.records/{index}",
        "version": record["version"],
    }


def decision(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "lock_entry": None,
        "package": record["name"],
        "selected_by": "greatest",
        "selected_package_id": record["package_id"],
        "selected_version": record["version"],
        "status": "no_lock_input",
    }


def requirement(records: list[dict[str, Any]], index: int) -> dict[str, Any]:
    record = records[index]
    if index == 0:
        contributor = {"kind": "root", "module": "root_app"}
        path = "root#/imports/0"
    else:
        previous = records[index - 1]
        contributor = {
            "kind": "package",
            "package": previous["name"],
            "package_id": previous["package_id"],
            "version": previous["version"],
        }
        path = (
            f"packages/{previous['name']}/{previous['version']}"
            "/module.yaml#/imports/0"
        )
    return {
        "alias": record["name"],
        "constraint": "1.0.0",
        "contributor": contributor,
        "interval": {
            "kind": "exact",
            "lower_inclusive": "1.0.0",
            "upper_exclusive": None,
        },
        "package": record["name"],
        "source_path": path,
    }


def selected_module(record: dict[str, Any]) -> dict[str, Any]:
    inline = {"encoding": "lowercase_hex", "hex": record["module_hex"]}
    verified = {
        "bytes": copy.deepcopy(inline),
        "path": record["descriptor"]["module_file"],
        "sha256": record["module_sha256"],
    }
    return {
        "imports": copy.deepcopy(record["imports"]),
        "module_file": record["descriptor"]["module_file"],
        "node": node(record),
        "package_id": record["package_id"],
        "parsed_module": copy.deepcopy(record["parsed_module"]),
        "record": {
            "descriptor": copy.deepcopy(record["descriptor"]),
            "package_id": record["package_id"],
            "verified_files": [verified],
        },
        "retained_bytes": copy.deepcopy(inline),
        "retained_bytes_sha256": record["module_sha256"],
    }


def node(record: dict[str, Any]) -> str:
    return (
        f"package:{record['name']}@{record['version']}#{record['package_id']}"
    )


def graph(records: list[dict[str, Any]]) -> dict[str, Any]:
    nodes = [{"kind": "root", "module": "root_app", "node": "root"}]
    nodes.extend(
        {
            "kind": "package",
            "name": record["name"],
            "node": node(record),
            "package_id": record["package_id"],
            "version": record["version"],
        }
        for record in records
    )
    edges = []
    for index in range(len(records) - 1):
        current = records[index]
        target = records[index + 1]
        edges.append(
            {
                "alias": target["name"],
                "constraint": "1.0.0",
                "from": node(current),
                "source_path": (
                    f"packages/{current['name']}/{current['version']}"
                    "/module.yaml#/imports/0"
                ),
                "to": node(target),
            }
        )
    first = records[0]
    edges.append(
        {
            "alias": first["name"],
            "constraint": "1.0.0",
            "from": "root",
            "source_path": "root#/imports/0",
            "to": node(first),
        }
    )
    return {"edges": edges, "nodes": nodes}


def expand_chain_field_first(manifest: dict[str, Any]) -> dict[str, Any]:
    records = manifest["generated_package_families"]["chain255"]["records"]
    selections = [selection(record, index) for index, record in enumerate(records)]
    decisions = [decision(record) for record in records]
    requirements = [requirement(records, index) for index in range(len(records))]
    passes = []
    for count in range(1, len(records) + 1):
        passes.append(
            {
                "active_requirements": copy.deepcopy(requirements[:count]),
                "changes": {
                    records[count - 1]["name"]: {
                        "from": None,
                        "to": records[count - 1]["package_id"],
                    }
                },
                "input_selection": copy.deepcopy(selections[: count - 1]),
                "output_selection": copy.deepcopy(selections[:count]),
                "pass": count,
                "selection_decisions": copy.deepcopy(decisions[:count]),
                "unchanged": False,
            }
        )
    passes.append(
        {
            "active_requirements": copy.deepcopy(requirements),
            "changes": {},
            "input_selection": copy.deepcopy(selections),
            "output_selection": copy.deepcopy(selections),
            "pass": 256,
            "selection_decisions": copy.deepcopy(decisions),
            "unchanged": True,
        }
    )
    output = copy.deepcopy(manifest["successful_outputs"]["output_chain_255"])
    output["existing_lock"] = {
        "input_ref": None,
        "input_sha256": None,
        "package_decisions": copy.deepcopy(decisions),
        "unreferenced_entries": [],
    }
    output["resolution_passes"] = passes
    output["selected_packages"] = selections
    output["selected_modules"] = [selected_module(record) for record in records]
    output["applicable_requirements"] = requirements
    output["import_graph"] = graph(records)
    return output


def expand_chain_pass_first(manifest: dict[str, Any]) -> dict[str, Any]:
    records = manifest["generated_package_families"]["chain255"]["records"]
    output = copy.deepcopy(manifest["successful_outputs"]["output_chain_255"])
    passes: list[dict[str, Any]] = []
    all_selections: list[dict[str, Any]] = []
    all_decisions: list[dict[str, Any]] = []
    all_requirements: list[dict[str, Any]] = []
    for index, record in enumerate(records):
        current_selection = {
            "name": record["name"],
            "package_id": record["package_id"],
            "record_ref": (
                "generated_package_families.chain255.records/" + str(index)
            ),
            "version": record["version"],
        }
        current_decision = {
            "lock_entry": None,
            "package": record["name"],
            "selected_by": "greatest",
            "selected_package_id": record["package_id"],
            "selected_version": record["version"],
            "status": "no_lock_input",
        }
        if index == 0:
            source_path = "root#/imports/0"
            contributor = {"kind": "root", "module": "root_app"}
        else:
            previous = records[index - 1]
            source_path = (
                "packages/"
                + previous["name"]
                + "/"
                + previous["version"]
                + "/module.yaml#/imports/0"
            )
            contributor = {
                "kind": "package",
                "package": previous["name"],
                "package_id": previous["package_id"],
                "version": previous["version"],
            }
        current_requirement = {
            "alias": record["name"],
            "constraint": "1.0.0",
            "contributor": contributor,
            "interval": {
                "kind": "exact",
                "lower_inclusive": "1.0.0",
                "upper_exclusive": None,
            },
            "package": record["name"],
            "source_path": source_path,
        }
        previous_selection = copy.deepcopy(all_selections)
        all_selections.append(current_selection)
        all_decisions.append(current_decision)
        all_requirements.append(current_requirement)
        passes.append(
            {
                "active_requirements": copy.deepcopy(all_requirements),
                "changes": {
                    record["name"]: {"from": None, "to": record["package_id"]}
                },
                "input_selection": previous_selection,
                "output_selection": copy.deepcopy(all_selections),
                "pass": index + 1,
                "selection_decisions": copy.deepcopy(all_decisions),
                "unchanged": False,
            }
        )
    passes.append(
        {
            "active_requirements": copy.deepcopy(all_requirements),
            "changes": {},
            "input_selection": copy.deepcopy(all_selections),
            "output_selection": copy.deepcopy(all_selections),
            "pass": 256,
            "selection_decisions": copy.deepcopy(all_decisions),
            "unchanged": True,
        }
    )
    output["existing_lock"] = {
        "input_ref": None,
        "input_sha256": None,
        "package_decisions": copy.deepcopy(all_decisions),
        "unreferenced_entries": [],
    }
    output["resolution_passes"] = passes
    output["selected_packages"] = all_selections
    output["selected_modules"] = [selected_module(record) for record in records]
    output["applicable_requirements"] = all_requirements
    output["import_graph"] = graph(records)
    return output


def verify_chain_preimages(manifest: dict[str, Any]) -> dict[str, Any]:
    first = expand_chain_field_first(manifest)
    second = expand_chain_pass_first(manifest)
    first_bytes = canonical_bytes_a(first)
    second_bytes = canonical_bytes_b(second)
    if first_bytes != second_bytes:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "/successful_outputs/output_chain_255",
            "independent chain constructions differ",
        )
    if len(first_bytes) != CHAIN_OUTPUT_BYTES:
        constructor_error("canonical_expanded_output_bytes", len(first_bytes))
    if hashlib.sha256(first_bytes).hexdigest() != CHAIN_OUTPUT_SHA256:
        constructor_error(
            "canonical_expanded_output_sha256",
            hashlib.sha256(first_bytes).hexdigest(),
        )
    plan = {
        "expected": first,
        "fixture_id": "RES-S-PASS-256",
        "input_ref": "chain_255",
    }
    plan_a = canonical_bytes_a(plan)
    plan_b = canonical_bytes_b(
        {
            "input_ref": "chain_255",
            "fixture_id": "RES-S-PASS-256",
            "expected": second,
        }
    )
    if plan_a != plan_b:
        constructor_error("canonical_generated_plan_root", "encoders differ")
    if len(plan_a) != CHAIN_PLAN_BYTES:
        constructor_error("canonical_generated_plan_bytes", len(plan_a))
    if hashlib.sha256(plan_a).hexdigest() != CHAIN_PLAN_SHA256:
        constructor_error(
            "canonical_generated_plan_sha256", hashlib.sha256(plan_a).hexdigest()
        )
    return first


def constructor_error(field: str, actual: Any) -> None:
    raise ManifestError(
        "PC7_MANIFEST_CONSTRUCTOR_INVALID",
        f"/construction_schema/chain255_expansion/{field}",
        f"unexpected {actual}",
    )


def expand_output(
    name: str, output: dict[str, Any], chain_output: dict[str, Any]
) -> dict[str, Any]:
    if name == "output_chain_255":
        return copy.deepcopy(chain_output)
    if any(
        isinstance(output[field], dict) and "constructor" in output[field]
        for field in [
            "existing_lock",
            "resolution_passes",
            "selected_packages",
            "selected_modules",
            "applicable_requirements",
            "import_graph",
        ]
    ):
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            f"/successful_outputs/{pointer_token(name)}",
            "generator marker outside output_chain_255",
        )
    return copy.deepcopy(output)


def validate_relation_operations(
    manifest: dict[str, Any], expanded_outputs: dict[str, dict[str, Any]]
) -> None:
    vocabulary = manifest["construction_schema"]["relation_operation_vocabulary"]
    for index, fixture in enumerate(manifest["fixtures"]):
        if fixture["class"] != "success_relation":
            continue
        operation = fixture["expected"]["operation"]
        kind = operation.get("kind")
        path = f"/fixtures/{index}/expected/operation"
        if kind not in vocabulary:
            relation_error(f"{path}/kind", "unknown operation")
        rule = vocabulary[kind]
        if list(operation.keys()) != list(operation.keys()):
            raise AssertionError
        if set(operation) != set(rule["required_members"]):
            relation_error(path, "operation members differ")
        if len(fixture["input_refs"]) != rule["input_operand_count"]:
            relation_error(f"/fixtures/{index}/input_refs", "input operand count")
        refs = fixture["expected"]["successful_output_refs"]
        if len(refs) != rule["successful_output_operand_count"]:
            relation_error(
                f"/fixtures/{index}/expected/successful_output_refs",
                "output operand count",
            )
        for member, allowed in rule["selector_arguments"].items():
            for selector_index, selector in enumerate(operation[member]):
                if selector_index >= len(allowed) or selector != allowed[selector_index]:
                    relation_error(
                        f"{path}/{member}/{selector_index}",
                        "selector allowlist mismatch",
                    )
            if len(operation[member]) != len(allowed):
                relation_error(f"{path}/{member}", "selector allowlist mismatch")
        operands = [expanded_outputs[reference] for reference in refs]
        execute_relation(operation, operands, fixture["input_refs"], manifest, path)


def relation_error(path: str, message: str) -> None:
    raise ManifestError("PC7_MANIFEST_RELATION_OPERATION_INVALID", path, message)


def execute_relation(
    operation: dict[str, Any],
    operands: list[dict[str, Any]],
    input_refs: list[str],
    manifest: dict[str, Any],
    path: str,
) -> None:
    kind = operation["kind"]
    if kind == "canonical_output_bytes_equal":
        if canonical_bytes_a(operands[0]) != canonical_bytes_a(operands[1]):
            relation_error(f"{path}/kind", "canonical operands differ")
    elif kind == "compare_fields":
        for member, equal in [("equal_fields", True), ("different_fields", False)]:
            for index, selector in enumerate(operation[member]):
                selector_path = f"{path}/{member}/{index}"
                same = projection_bytes(
                    operands[0], selector, selector_path
                ) == projection_bytes(operands[1], selector, selector_path)
                if same != equal:
                    relation_error(selector_path, "comparison failed")
    elif kind == "compare_after_source_path_erasure":
        erased = [erase_source_paths(copy.deepcopy(value)) for value in operands]
        for index, selector in enumerate(operation["equal_fields"]):
            selector_path = f"{path}/equal_fields/{index}"
            if projection_bytes(
                erased[0], selector, selector_path
            ) != projection_bytes(erased[1], selector, selector_path):
                relation_error(selector_path, "comparison failed")
    elif kind == "assert_no_later_artifacts":
        for index, selector in enumerate(operation["required_empty_fields"]):
            selector_path = f"{path}/required_empty_fields/{index}"
            values = relation_projection(operands[0], selector, selector_path)
            if values != [[]]:
                relation_error(selector_path, "field not empty")
        if operands[0]["authority"] != operation["required_authority"]:
            relation_error(f"{path}/required_authority", "authority differs")
    elif kind == "retained_boundary_repeatability":
        for input_ref in input_refs:
            if manifest["resolve_inputs"][input_ref]["host_capabilities"] != []:
                relation_error(
                    f"{path}/required_empty_host_capabilities",
                    "host capabilities present",
                )
        for index, selector in enumerate(operation["required_equal_fields"]):
            selector_path = f"{path}/required_equal_fields/{index}"
            if projection_bytes(
                operands[0], selector, selector_path
            ) != projection_bytes(operands[1], selector, selector_path):
                relation_error(selector_path, "comparison failed")
    elif kind == "assert_scanned_source_independent_projection":
        if operation["correct_expected_source"] != "pre_resolve_pc2_through_pc6_projection":
            relation_error(f"{path}/correct_expected_source", "wrong expected source")
        if operation["required_correct_comparison"] != "equal":
            relation_error(f"{path}/required_correct_comparison", "wrong comparison")
        if operation["required_wrong_comparison"] != "different":
            relation_error(f"{path}/required_wrong_comparison", "wrong comparison")
        if operation["wrong_scanned_source_field"] != "scanned_source":
            relation_error(f"{path}/wrong_scanned_source_field", "wrong target field")
        if operands[0].get("scanned_source_ref") != input_refs[0]:
            relation_error(f"{path}/kind", "stored source locator differs")
        if canonical_bytes_a(operation["wrong_scanned_source"]) == canonical_bytes_a(
            {"scanned_source_ref": input_refs[0]}
        ):
            relation_error(f"{path}/wrong_scanned_source", "wrong value is not discriminating")
    else:
        relation_error(f"{path}/kind", "unknown operation")


SELECTOR = re.compile(r"^(?:\$|[a-z][a-z0-9_]*(?:(?:\.[a-z][a-z0-9_]*)|(?:\[\*\]))*)$")


def project(root: Any, selector: str) -> list[Any]:
    if not SELECTOR.fullmatch(selector):
        raise ValueError("invalid selector")
    if selector == "$":
        return [root]
    tokens = re.findall(r"^[a-z][a-z0-9_]*|\.[a-z][a-z0-9_]*|\[\*\]", selector)
    projection = [root]
    for token in tokens:
        next_projection = []
        if token == "[*]":
            for value in projection:
                if not isinstance(value, list):
                    raise ValueError("wildcard on non-array")
                next_projection.extend(value)
        else:
            member = token.lstrip(".")
            for value in projection:
                if not isinstance(value, dict) or member not in value:
                    raise ValueError("missing member")
                next_projection.append(value[member])
        projection = next_projection
    return projection


def relation_projection(root: Any, selector: str, path: str) -> list[Any]:
    try:
        return project(root, selector)
    except ValueError as error:
        raise ManifestError(
            "PC7_MANIFEST_RELATION_OPERATION_INVALID", path, str(error)
        ) from error


def projection_bytes(root: Any, selector: str, path: str = "") -> bytes:
    return canonical_bytes_a(relation_projection(root, selector, path))


def erase_source_paths(value: Any) -> Any:
    if isinstance(value, dict):
        for key in sorted(value, key=lambda item: item.encode("utf-8")):
            if key == "source_path" and isinstance(value[key], str):
                value[key] = erase_import_index(value[key])
            else:
                erase_source_paths(value[key])
    elif isinstance(value, list):
        for child in value:
            erase_source_paths(child)
    return value


def erase_import_index(path: str) -> str:
    if path.count("#") != 1:
        return path
    prefix, pointer = path.split("#")
    raw = pointer.split("/")
    decoded = [token.replace("~1", "/").replace("~0", "~") for token in raw]
    for index in range(len(decoded) - 1):
        if decoded[index] == "imports" and re.fullmatch(r"0|[1-9][0-9]*", decoded[index + 1]):
            raw[index + 1] = "*"
    return prefix + "#" + "/".join(raw)


def generate_plan(
    manifest: dict[str, Any], chain_output: dict[str, Any], registry_bytes: bytes
) -> dict[str, Any]:
    expanded_outputs = {
        name: expand_output(name, output, chain_output)
        for name, output in manifest["successful_outputs"].items()
    }
    validate_relation_operations(manifest, expanded_outputs)
    cases = []
    for fixture in sorted(manifest["fixtures"], key=lambda row: row["id"].encode("utf-8")):
        if fixture["class"] == "diagnostic":
            cases.append(
                {
                    "class": "diagnostic",
                    "expected": copy.deepcopy(fixture["expected"]),
                    "fixture_id": fixture["id"],
                    "input_ref": fixture["input_ref"],
                }
            )
        elif fixture["class"] == "success":
            cases.append(
                {
                    "class": "success",
                    "expected": expanded_outputs[
                        fixture["expected"]["successful_output_ref"]
                    ],
                    "fixture_id": fixture["id"],
                    "input_ref": fixture["input_ref"],
                }
            )
        elif fixture["class"] == "success_relation":
            cases.append(
                {
                    "class": "success_relation",
                    "expected": {
                        "operation": copy.deepcopy(fixture["expected"]["operation"]),
                        "outputs": [
                            expanded_outputs[name]
                            for name in fixture["expected"]["successful_output_refs"]
                        ],
                    },
                    "fixture_id": fixture["id"],
                    "input_refs": copy.deepcopy(fixture["input_refs"]),
                }
            )
        else:
            raise ManifestError(
                "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
                "/fixtures",
                f"unknown fixture class {fixture['class']}",
            )
    defined = {fixture["id"] for fixture in manifest["fixtures"]}
    generated = {case["fixture_id"] for case in cases}
    if defined != generated or len(cases) != len(generated):
        raise ManifestError(
            "PC7_MANIFEST_POPULATION_MISMATCH",
            "/fixtures",
            "defined and generated fixture IDs differ",
        )
    return {
        "authority": {
            "manifest_path": "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json",
            "manifest_sha256": EXPECTED_MANIFEST_SHA256,
            "registry_bytes": len(registry_bytes),
            "registry_sha256": hashlib.sha256(registry_bytes).hexdigest(),
        },
        "cases": cases,
        "fixture_plan_version": "threadsmith-pc7-resolve-executable-plan-0.1",
        "future_vector_ids": sorted(
            (
                vector["vector_id"]
                for vector in manifest["non_dispatchable_future_vectors"].values()
            ),
            key=lambda value: value.encode("utf-8"),
        ),
    }


def expect_rejection(
    operation: Any, code: str, path: str, label: str
) -> None:
    try:
        operation()
    except ManifestError as error:
        if error.code != code or error.path != path:
            raise ManifestError(
                "PC7_MANIFEST_CONSTRUCTOR_INVALID",
                "",
                f"{label} rejected as {error.code} at {error.path}",
            ) from error
    else:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "",
            f"{label} mutation was admitted",
        )


def expect_preflight_rejection(
    operation: Any,
    gate: str,
    path: str,
    reason: str,
    label: str,
) -> None:
    try:
        operation()
    except AuthorityPreflightError as error:
        if (
            error.code != "PC7_AUTHORITY_PREFLIGHT_REJECTED"
            or error.gate != gate
            or error.path != path
            or error.reason != reason
            or error.fixture_dispatch_started
        ):
            raise ManifestError(
                "PC7_MANIFEST_CONSTRUCTOR_INVALID",
                "",
                f"{label} rejected as {error}",
            ) from error
    else:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "",
            f"{label} mutation was admitted",
        )


def run_authority_rejection_self_tests(inputs: PC7AuthorityInputsV1) -> None:
    source = b'  "format": "threadsmith-pc7-authority-registry-1",\n'
    replacement = b'  "format": "\\ud800",\n'
    if inputs.registry_bytes.count(source) != 1:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "",
            "raw surrogate source line not unique",
        )
    surrogate = inputs.registry_bytes.replace(source, replacement, 1)
    if len(surrogate) != 2011:
        raise ManifestError(
            "PC7_MANIFEST_CONSTRUCTOR_INVALID",
            "",
            "raw surrogate mutation is not 2,011 bytes",
        )
    expect_preflight_rejection(
        lambda: authority_preflight(
            PC7AuthorityInputsV1(
                inputs.authority_root, inputs.registry_path, surrogate
            )
        ),
        "registry_strict_json_parse",
        "authority#/registry",
        "UTF-8/BOM/JSON/duplicate failure",
        "raw unpaired surrogate",
    )

    unknown = inputs.registry_bytes[:-2] + b',\n  "zzz": true\n}\n'
    expect_preflight_rejection(
        lambda: authority_preflight(
            PC7AuthorityInputsV1(inputs.authority_root, inputs.registry_path, unknown)
        ),
        "registry_unknown_members",
        "authority#/registry/zzz",
        "unknown registry member",
        "raw unknown registry member",
    )

    with tempfile.TemporaryDirectory(prefix="threadsmith-pc7-authority-") as directory:
        root = Path(directory)
        for _, relative in AUTHORITY_DOCUMENTS:
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(inputs.authority_root / relative, target)
        target = root / REGISTRY_PATH
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(inputs.registry_bytes)
        resolve_path = root / dict(AUTHORITY_DOCUMENTS)["resolve_semantics_erratum"]
        original = resolve_path.read_text(encoding="utf-8")
        source_sentence = "The first failing gate returns its primary diagnostic"
        changed_sentence = "The last failing gate returns its primary diagnostic"
        if original.count(source_sentence) < 1:
            raise ManifestError(
                "PC7_MANIFEST_CONSTRUCTOR_INVALID",
                "",
                "Resolve authority discriminator sentence absent",
            )
        resolve_path.write_text(
            original.replace(source_sentence, changed_sentence, 1),
            encoding="utf-8",
            newline="",
        )
        expect_preflight_rejection(
            lambda: authority_preflight(
                PC7AuthorityInputsV1(root, root / REGISTRY_PATH, inputs.registry_bytes)
            ),
            "authority_document_bytes",
            "authority#/resolve_semantics_erratum",
            "authority document byte count mismatch",
            "changed Resolve authority sentence",
        )


def run_rejection_self_tests(
    manifest: dict[str, Any], chain_output: dict[str, Any]
) -> None:
    def find_fixture(
        candidate: dict[str, Any], fixture_id: str, required_index: int
    ) -> tuple[int, dict[str, Any]]:
        fixture = next(
            row for row in candidate["fixtures"] if row["id"] == fixture_id
        )
        index = candidate["fixtures"].index(fixture)
        if index != required_index:
            raise ManifestError(
                "PC7_MANIFEST_CONSTRUCTOR_INVALID",
                "/fixtures",
                f"{fixture_id} stored at {index}, not {required_index}",
            )
        return index, fixture

    def expanded_outputs(
        candidate: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        return {
            name: expand_output(name, output, chain_output)
            for name, output in candidate["successful_outputs"].items()
        }

    def relation_stage_operation(
        candidate: dict[str, Any],
        fixture_id: str,
        required_index: int,
        mutate: Any,
    ) -> None:
        index, fixture = find_fixture(candidate, fixture_id, required_index)
        expanded = expanded_outputs(candidate)
        operands = [
            copy.deepcopy(expanded[reference])
            for reference in fixture["expected"]["successful_output_refs"]
        ]
        mutate(operands)
        execute_relation(
            fixture["expected"]["operation"],
            operands,
            fixture["input_refs"],
            candidate,
            f"/fixtures/{index}/expected/operation",
        )

    nested_unknown = copy.deepcopy(manifest)
    nested_unknown["fixtures"][0]["expected"]["typo"] = True
    expect_rejection(
        lambda: SchemaValidator(nested_unknown).validate(),
        "PC7_MANIFEST_SCHEMA_UNKNOWN_MEMBER",
        "/fixtures/0/expected/typo",
        "nested unknown member",
    )

    population = copy.deepcopy(manifest)
    population["coverage"]["declared_populations"]["current_fixtures"] += 1
    expect_rejection(
        lambda: validate_populations(population),
        "PC7_MANIFEST_POPULATION_MISMATCH",
        "/coverage/declared_populations/current_fixtures",
        "population mismatch",
    )

    unresolved = copy.deepcopy(manifest)
    unresolved["fixtures"][0]["input_ref"] = "absent_target"
    expect_rejection(
        lambda: validate_references(unresolved),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/fixtures/0/input_ref",
        "unresolved fixture input",
    )

    duplicate = copy.deepcopy(manifest)
    duplicate["fixtures"][1]["id"] = duplicate["fixtures"][0]["id"]
    expect_rejection(
        lambda: validate_references(duplicate),
        "PC7_MANIFEST_DUPLICATE_ID",
        "/fixtures/1/id",
        "duplicate fixture id",
    )

    unresolved_coverage = copy.deepcopy(manifest)
    unresolved_coverage["coverage"]["required_behavior_coverage"][
        "arbitrary_size_numeric"
    ][0] = "NOT-A-DEFINED-FIXTURE"
    expect_rejection(
        lambda: validate_references(unresolved_coverage),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/coverage/required_behavior_coverage/arbitrary_size_numeric/0",
        "unresolved coverage fixture",
    )

    future_population_coverage = copy.deepcopy(manifest)
    future_population_coverage["coverage"]["required_behavior_coverage"][
        "arbitrary_size_numeric"
    ][0] = "PC7-FV-IDENTICAL-DUPLICATE"
    expect_rejection(
        lambda: validate_references(future_population_coverage),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/coverage/required_behavior_coverage/arbitrary_size_numeric/0",
        "future vector in current fixture coverage",
    )

    invalid_diagnostic_population = copy.deepcopy(manifest)
    invalid_diagnostic_population["coverage"]["diagnostic_definition_coverage"][
        "RESOLVE_DUPLICATE_VERSION"
    ].append("RES-S-EMPTY")
    expect_rejection(
        lambda: validate_references(invalid_diagnostic_population),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/coverage/diagnostic_definition_coverage/RESOLVE_DUPLICATE_VERSION/0",
        "success fixture in diagnostic coverage",
    )

    duplicate_coverage = copy.deepcopy(manifest)
    duplicate_coverage["coverage"]["required_behavior_coverage"][
        "arbitrary_size_numeric"
    ].append("RES-S-ARBITRARY-SIZE")
    expect_rejection(
        lambda: SchemaValidator(duplicate_coverage).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/coverage/required_behavior_coverage/arbitrary_size_numeric/3",
        "duplicate coverage fixture id",
    )

    reversed_coverage = copy.deepcopy(manifest)
    reversed_coverage["coverage"]["required_behavior_coverage"][
        "binding_repeatability_non_authority"
    ].reverse()
    expect_rejection(
        lambda: SchemaValidator(reversed_coverage).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/coverage/required_behavior_coverage/binding_repeatability_non_authority/1",
        "reversed semantic coverage order",
    )

    misclassified_rank_relationship = copy.deepcopy(manifest)
    relationship_fixtures = misclassified_rank_relationship["coverage"][
        "rank_comparison_coverage"
    ].pop("2>3")
    misclassified_rank_relationship["coverage"]["rank_comparison_coverage"][
        "4>5"
    ] = relationship_fixtures
    expect_rejection(
        lambda: validate_references(misclassified_rank_relationship),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/coverage/rank_comparison_coverage/4>5",
        "rank relationship in the gate-order category",
    )

    missing_rank_relationship = copy.deepcopy(manifest)
    missing_rank_relationship["coverage"]["rank_comparison_coverage"].pop("2>3")
    expect_rejection(
        lambda: validate_references(missing_rank_relationship),
        "PC7_MANIFEST_REFERENCE_INVALID",
        "/coverage/rank_comparison_coverage/2>3",
        "missing rank relationship",
    )

    discontinuous_rank_relationship = copy.deepcopy(manifest)
    relationship_fixtures = discontinuous_rank_relationship["coverage"][
        "rank_comparison_coverage"
    ].pop("2>3")
    discontinuous_rank_relationship["coverage"]["rank_comparison_coverage"][
        "2>4"
    ] = relationship_fixtures
    expect_rejection(
        lambda: SchemaValidator(discontinuous_rank_relationship).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/fixtures/43/rank_comparison",
        "discontinuous rank relationship",
    )

    swapped_diagnostic_ranks = copy.deepcopy(manifest)
    definitions = swapped_diagnostic_ranks["diagnostic_definitions"]
    definitions[0]["rank"], definitions[1]["rank"] = (
        definitions[1]["rank"],
        definitions[0]["rank"],
    )
    expect_rejection(
        lambda: SchemaValidator(swapped_diagnostic_ranks).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/diagnostic_definitions/0/rank",
        "non-increasing diagnostic ranks",
    )

    duplicate_diagnostic_rank = copy.deepcopy(manifest)
    duplicate_diagnostic_rank["diagnostic_definitions"][1]["rank"] = 1
    expect_rejection(
        lambda: SchemaValidator(duplicate_diagnostic_rank).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/diagnostic_definitions/1/rank",
        "duplicate diagnostic rank",
    )

    discontinuous_diagnostic_rank = copy.deepcopy(manifest)
    discontinuous_diagnostic_rank["diagnostic_definitions"][-1]["rank"] = 22
    expect_rejection(
        lambda: SchemaValidator(discontinuous_diagnostic_rank).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/diagnostic_definitions/20/rank",
        "missing diagnostic rank",
    )

    duplicate_diagnostic_code = copy.deepcopy(manifest)
    duplicate_diagnostic_code["diagnostic_definitions"][1]["code"] = (
        duplicate_diagnostic_code["diagnostic_definitions"][0]["code"]
    )
    diagnostic_array_validator = SchemaValidator(duplicate_diagnostic_code)
    expect_rejection(
        lambda: diagnostic_array_validator.validate_schema(
            "diagnostic_definitions_array",
            duplicate_diagnostic_code["diagnostic_definitions"],
            "/diagnostic_definitions",
        ),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/diagnostic_definitions/1/code",
        "duplicate diagnostic code",
    )

    unknown_class = copy.deepcopy(manifest)
    unknown_class["fixtures"][0]["class"] = "unknown_class"
    expect_rejection(
        lambda: SchemaValidator(unknown_class).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/fixtures/0",
        "unknown fixture class",
    )

    relation = copy.deepcopy(manifest)
    relation_index, relation_fixture = find_fixture(
        relation, "RES-S-LOCK-REQUESTED-BY-RELATION", 78
    )
    relation_fixture["expected"]["operation"]["kind"] = "unknown_operation"
    expect_rejection(
        lambda: validate_relation_operations(relation, expanded_outputs(relation)),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/78/expected/operation/kind",
        "unknown relation operation",
    )

    cycle_endpoint = copy.deepcopy(manifest)
    _, cycle_fixture = find_fixture(
        cycle_endpoint, "RES-D-CYCLE-SELF", 7
    )
    cycle_fixture["expected"]["primary_diagnostic"]["canonical_cycle"][0][
        "from"
    ] = (
        "package:self_cycle@1.0.0#"
        "lattice:package:sha256:"
        "f7447e65581ee37aead7b57617fab7f784bc5616c70fd381e96f070bcc9ac109"
    )
    expect_rejection(
        lambda: SchemaValidator(cycle_endpoint).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/fixtures/7/expected/primary_diagnostic/canonical_cycle/0/from",
        "cycle edge package-name terminal",
    )

    for label, replacement in [
        ("wildcard selector syntax", "resolution_passes[].output_selection"),
        ("numeric selector index", "resolution_passes[0].output_selection"),
    ]:
        selector = copy.deepcopy(manifest)
        _, fixture = find_fixture(selector, "RES-S-ORDER-RELATION", 87)
        fixture["expected"]["operation"]["equal_fields"][2] = replacement
        expect_rejection(
            lambda selector=selector: validate_relation_operations(
                selector, expanded_outputs(selector)
            ),
            "PC7_MANIFEST_RELATION_OPERATION_INVALID",
            "/fixtures/87/expected/operation/equal_fields/2",
            label,
        )

    missing_member = copy.deepcopy(manifest)
    expect_rejection(
        lambda: relation_stage_operation(
            missing_member,
            "RES-S-LOCK-REQUESTED-BY-RELATION",
            78,
            lambda operands: operands[0].pop("selected_packages"),
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/78/expected/operation/equal_fields/0",
        "missing projected member",
    )

    ordered_projection = copy.deepcopy(manifest)
    expect_rejection(
        lambda: relation_stage_operation(
            ordered_projection,
            "RES-S-ORDER-RELATION",
            87,
            lambda operands: operands[1]["selected_packages"].reverse(),
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/87/expected/operation/equal_fields/0",
        "ordered projection reversal",
    )

    projection_multiplicity = copy.deepcopy(manifest)

    def append_duplicate_projection(operands: list[dict[str, Any]]) -> None:
        operands[1]["selected_modules"].append(
            copy.deepcopy(operands[1]["selected_modules"][0])
        )

    expect_rejection(
        lambda: relation_stage_operation(
            projection_multiplicity,
            "RES-S-RETAINED-BYTES",
            92,
            append_duplicate_projection,
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/92/expected/operation/required_equal_fields/0",
        "projection multiplicity",
    )

    wrong_container = copy.deepcopy(manifest)

    def replace_projection_container(
        operands: list[dict[str, Any]],
    ) -> None:
        operands[0]["resolution_passes"] = {}

    expect_rejection(
        lambda: relation_stage_operation(
            wrong_container,
            "RES-S-ORDER-RELATION",
            87,
            replace_projection_container,
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/87/expected/operation/equal_fields/2",
        "wrong projection container",
    )

    erasure_scope = copy.deepcopy(manifest)

    def mutate_erasure_scope(operands: list[dict[str, Any]]) -> None:
        operands[0]["resolution_passes"][0]["active_requirements"][0][
            "source_path"
        ] = "packages/pkg2/10.0.0/module.yaml#/imports/0"
        operands[1]["resolution_passes"][0]["active_requirements"][0][
            "source_path"
        ] = "packages/pkg3/11.0.0/module.yaml#/imports/1"

    expect_rejection(
        lambda: relation_stage_operation(
            erasure_scope,
            "RES-S-ORDER-RELATION",
            87,
            mutate_erasure_scope,
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        "/fixtures/87/expected/operation/equal_fields/3",
        "source-path erasure scope",
    )

    fixture_order = copy.deepcopy(manifest)
    ordered = fixture_order["coverage"]["required_behavior_coverage"][
        "constraint_intersection"
    ]
    ordered[0], ordered[1] = ordered[1], ordered[0]
    expect_rejection(
        lambda: SchemaValidator(fixture_order).validate(),
        "PC7_MANIFEST_SCHEMA_VALUE_INVALID",
        "/coverage/required_behavior_coverage/constraint_intersection/1",
        "fixture-id array adjacent inversion",
    )

    scanned_relation = copy.deepcopy(manifest)
    scanned_index, scanned_fixture = find_fixture(
        scanned_relation, "RES-S-SCANNED-SOURCE-INDEPENDENT", 117
    )
    scanned_fixture["expected"]["operation"]["required_wrong_comparison"] = "equal"
    expect_rejection(
        lambda: validate_relation_operations(
            scanned_relation, expanded_outputs(scanned_relation)
        ),
        "PC7_MANIFEST_RELATION_OPERATION_INVALID",
        f"/fixtures/{scanned_index}/expected/operation/required_wrong_comparison",
        "scanned-source wrong-comparison discriminator",
    )


def load_and_validate(
    inputs: PC7AuthorityInputsV1,
) -> tuple[dict[str, Any], dict[str, int], dict[str, Any], bytes]:
    global _ACCEPTED_MANIFEST_CACHE
    _, raw = authority_preflight(inputs)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_MANIFEST_SHA256:
        byte_error("")
    manifest = strict_loads(raw)
    _ACCEPTED_MANIFEST_CACHE = manifest
    SchemaValidator(manifest).validate()
    validate_bytes_and_identities(manifest)
    validate_references(manifest)
    populations = validate_populations(manifest)
    chain_output = verify_chain_preimages(manifest)
    return manifest, populations, chain_output, inputs.registry_bytes


class UniqueStore(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Any,
        option_string: str | None = None,
    ) -> None:
        if getattr(namespace, self.dest, None) is not None:
            if self.dest == "pc7_authority_root":
                preflight_error(
                    "invocation_authority_root",
                    "authority#/root",
                    "authority root input repeated",
                )
            preflight_error(
                "invocation_registry_binding",
                "authority#/registry",
                "registry input repeated",
            )
        setattr(namespace, self.dest, values)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pc7-authority-root",
        action=UniqueStore,
        default=None,
        metavar="DIRECTORY",
    )
    parser.add_argument(
        "--pc7-authority-registry",
        action=UniqueStore,
        default=None,
        metavar="FILE",
    )
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-summary", action="store_true")
    try:
        args = parser.parse_args()
        if args.pc7_authority_root is None:
            preflight_error(
                "invocation_authority_root",
                "authority#/root",
                "authority root input missing",
            )
        if args.pc7_authority_registry is None:
            preflight_error(
                "invocation_registry_binding",
                "authority#/registry",
                "registry input missing",
            )
        authority_root = Path(args.pc7_authority_root)
        registry_path = Path(args.pc7_authority_registry)
        if not authority_root.is_dir():
            preflight_error(
                "invocation_authority_root",
                "authority#/root",
                "authority root invalid",
            )
        if registry_path != authority_root / REGISTRY_PATH:
            preflight_error(
                "invocation_registry_binding",
                "authority#/registry",
                "registry path is not the fixed V1 path",
            )
        try:
            registry_bytes = registry_path.read_bytes()
        except OSError:
            preflight_error(
                "registry_read", "authority#/registry", "registry unreadable"
            )
        inputs = PC7AuthorityInputsV1(
            authority_root=authority_root,
            registry_path=registry_path,
            registry_bytes=registry_bytes,
        )
        manifest, populations, chain_output, registry_bytes = load_and_validate(inputs)
        run_authority_rejection_self_tests(inputs)
        run_rejection_self_tests(manifest, chain_output)
        plan = generate_plan(manifest, chain_output, registry_bytes)
        plan_bytes = canonical_bytes_a(plan) + b"\n"
        if args.check:
            if not PLAN_PATH.exists() or PLAN_PATH.read_bytes() != plan_bytes:
                raise ManifestError(
                    "PC7_MANIFEST_CONSTRUCTOR_INVALID",
                    "",
                    "checked-in executable plan differs",
                )
        else:
            PLAN_PATH.parent.mkdir(parents=True, exist_ok=True)
            PLAN_PATH.write_bytes(plan_bytes)
        if args.print_summary:
            summary = {
                "canonical_fixture_root_bytes": CHAIN_OUTPUT_BYTES,
                "canonical_fixture_root_sha256": CHAIN_OUTPUT_SHA256,
                "canonical_generated_plan_bytes": CHAIN_PLAN_BYTES,
                "canonical_generated_plan_sha256": CHAIN_PLAN_SHA256,
                "defined_current_fixture_ids": len(manifest["fixtures"]),
                "generated_current_plan_ids": len(plan["cases"]),
                "populations": populations,
            }
            print(json.dumps(summary, sort_keys=True))
        return 0
    except (ManifestError, AuthorityPreflightError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
