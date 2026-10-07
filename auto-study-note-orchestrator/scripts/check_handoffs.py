#!/usr/bin/env python3
"""Check unit handoff JSON against body fragments and the source inventory.

This is the only check that reads both sides of the handoff contract at once.
`validate_study_note.py` sees the merged document and the unit fragments but never
the JSON; `collect_formula_candidates.py` sees the JSON but never the LaTeX.
A body_label that points at no \\label therefore passes both and rots silently.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


KINDS = ("definition", "notation", "result")
CANDIDATE_FIELDS = ("key", "name", "formula", "conditions", "body_label")
UPDATE_FIELDS = ("kind", "name", "meaning", "body_label")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
ID_HEADERS = {"id", "coverage id", "gap id"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def body_labels(paths: list[Path]) -> dict[str, list[str]]:
    """Map every \\label in the supplied bodies to the files that declare it."""
    owners: dict[str, set[str]] = {}
    for path in paths:
        for label in LABEL_RE.findall(strip_comments(read_text(path.resolve()))):
            label = label.strip()
            if label:
                owners.setdefault(label, set()).add(path.name)
    return {label: sorted(names) for label, names in sorted(owners.items())}


def inventory_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for line in read_text(path.resolve()).splitlines():
        value = line.strip()
        if not (value.startswith("|") and value.endswith("|")):
            continue
        if re.fullmatch(r"[|:\-\s]+", value):
            continue
        first = value.strip("|").split("|")[0].strip()
        if first and first.lower() not in ID_HEADERS:
            ids.add(first)
    return ids


def _text_field(record: dict[str, Any], field: str) -> str:
    value = record.get(field)
    return value.strip() if isinstance(value, str) else ""


def check(handoffs: list[Path], bodies: list[Path], inventory: Path | None = None) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, Any] = {}

    labels = body_labels(bodies)
    metrics["known_labels"] = len(labels)
    metrics["bodies_read"] = len(bodies)

    known_ids = inventory_ids(inventory) if inventory else None
    if known_ids is not None:
        metrics["inventory_ids"] = len(known_ids)

    units: list[str] = []
    referenced: dict[str, set[str]] = {}

    for path in handoffs:
        name = path.name
        try:
            record = json.loads(read_text(path))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{name}: unreadable handoff ({exc})")
            continue
        if not isinstance(record, dict):
            failures.append(f"{name}: handoff root must be a JSON object")
            continue

        unit_id = record.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            failures.append(f"{name}: missing unit_id")
            continue
        unit_id = unit_id.strip()
        if unit_id in units:
            failures.append(f"{name}: duplicate unit_id {unit_id!r}")
        units.append(unit_id)

        coverage = record.get("coverage_ids")
        if not isinstance(coverage, list) or not coverage:
            failures.append(f"{name}: coverage_ids must be a non-empty list")
        elif not all(isinstance(item, str) and item.strip() for item in coverage):
            failures.append(f"{name}: coverage_ids entries must be non-empty strings")
        elif known_ids is not None:
            for coverage_id in coverage:
                if coverage_id.strip() not in known_ids:
                    failures.append(
                        f"{name}: coverage id {coverage_id.strip()!r} is not in the source inventory"
                    )

        if not isinstance(record.get("unresolved"), list):
            failures.append(f"{name}: unresolved must be a list (use [] when there is none)")

        candidates = record.get("formula_candidates")
        if not isinstance(candidates, list):
            failures.append(f"{name}: formula_candidates must be a list (use [] when empty)")
            candidates = []
        updates = record.get("continuity_updates")
        if not isinstance(updates, list):
            failures.append(f"{name}: continuity_updates must be a list (use [] when empty)")
            updates = []

        def resolve(where: str, label: str) -> None:
            if label not in labels:
                failures.append(
                    f"{where}: body_label {label!r} resolves to no \\label in the supplied bodies"
                )
            else:
                referenced.setdefault(label, set()).add(unit_id)

        seen_keys: dict[str, int] = {}
        for index, item in enumerate(candidates, 1):
            where = f"{name}: formula candidate {index}"
            if not isinstance(item, dict):
                failures.append(f"{where} must be an object")
                continue
            missing = [field for field in CANDIDATE_FIELDS if not _text_field(item, field)]
            if missing:
                failures.append(f"{where} lacks {missing}")
                continue
            key = _text_field(item, "key")
            if key in seen_keys:
                failures.append(f"{where}: duplicate result key {key!r} (first at candidate {seen_keys[key]})")
            else:
                seen_keys[key] = index
            resolve(where, _text_field(item, "body_label"))

        seen_names: dict[str, int] = {}
        for index, item in enumerate(updates, 1):
            where = f"{name}: continuity update {index}"
            if not isinstance(item, dict):
                failures.append(f"{where} must be an object")
                continue
            missing = [field for field in UPDATE_FIELDS if not _text_field(item, field)]
            if missing:
                failures.append(f"{where} lacks {missing}")
                continue
            kind = _text_field(item, "kind")
            if kind not in KINDS:
                failures.append(f"{where}: kind {kind!r} is not one of {list(KINDS)}")
            identity = f"{kind}:{_text_field(item, 'name')}"
            if identity in seen_names:
                failures.append(f"{where}: duplicate continuity entry {identity!r}")
            else:
                seen_names[identity] = index
            resolve(where, _text_field(item, "body_label"))

    # A result cited by a unit other than the one that declares it is the intended
    # reuse pattern; surface it so the merge step keeps a single explanation.
    reused = sorted(label for label, unit_ids in referenced.items() if len(unit_ids) > 1)

    metrics["handoffs_checked"] = len(handoffs)
    metrics["units"] = units
    metrics["referenced_labels"] = len(referenced)
    metrics["reused_results"] = reused

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "warnings": warnings,
        "metrics": metrics,
        "reused_results": [
            {"body_label": label, "referenced_by": sorted(referenced[label]), "declared_in": labels[label]}
            for label in reused
        ],
        "label_owners": labels,
    }


def main() -> int:
    # Windows consoles often default to a legacy code page (GBK here) that cannot
    # encode characters such as U+015C, so printing a report could crash the run.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--handoff", type=Path, action="append", required=True, help="unit handoff JSON; repeatable")
    parser.add_argument("--body", type=Path, action="append", default=[], help="unit body fragment; repeatable")
    parser.add_argument("--inventory", type=Path, help="source inventory markdown")
    parser.add_argument("--out", type=Path, help="optional JSON report path")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    report = check(args.handoff, args.body, args.inventory)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    if args.format == "json":
        print(output)
    else:
        print(f"status: {report['status']}")
        for failure in report["failures"]:
            print(f"  FAIL {failure}")
        for warning in report["warnings"]:
            print(f"  warn {warning}")
        for item in report["reused_results"]:
            print(
                f"  reuse {item['body_label']} declared in {', '.join(item['declared_in'])}"
                f" and cited by {', '.join(item['referenced_by'])}"
            )
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
