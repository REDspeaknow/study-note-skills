#!/usr/bin/env python3
"""Read-only structural and PDF QA for study-note-style-v1 outputs."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


STYLE_VERSION = "study-note-style-v1"
A4_WIDTH_PT = 595.28
A4_HEIGHT_PT = 841.89


def read_text(path: Path | None) -> str:
    if path is None:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def count_inventory_rows(text: str) -> int:
    rows = 0
    for line in text.splitlines():
        value = line.strip()
        if not (value.startswith("|") and value.endswith("|")):
            continue
        if re.fullmatch(r"[|:\-\s]+", value):
            continue
        cells = [cell.strip().lower() for cell in value.strip("|").split("|")]
        if cells and cells[0] in {"id", "gap id", "coverage id"}:
            continue
        rows += 1
    return rows


def dereference(value: Any) -> Any:
    return value.get_object() if hasattr(value, "get_object") else value


def pdf_checks(pdf_path: Path, failures: list[str], warnings: list[str], metrics: dict[str, Any]) -> None:
    try:
        from pypdf import PdfReader
    except ImportError:
        failures.append("pypdf is unavailable; PDF font and link checks could not run")
        return

    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:  # pragma: no cover - tool-facing error path
        failures.append(f"PDF could not be opened: {exc}")
        return

    metrics["pdf_pages"] = len(reader.pages)
    if not reader.pages:
        failures.append("PDF has no pages")
        return

    fonts: set[str] = set()
    link_count = 0
    visible_link_borders = 0
    page_sizes: list[tuple[float, float]] = []

    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        page_sizes.append((round(width, 2), round(height, 2)))

        resources = dereference(page.get("/Resources", {})) or {}
        font_dict = dereference(resources.get("/Font", {})) or {}
        for font_ref in font_dict.values():
            font = dereference(font_ref) or {}
            base_font = font.get("/BaseFont")
            if base_font:
                fonts.add(str(base_font).lstrip("/"))

        for annotation_ref in page.get("/Annots", []) or []:
            annotation = dereference(annotation_ref) or {}
            if str(annotation.get("/Subtype")) != "/Link":
                continue
            link_count += 1
            border = dereference(annotation.get("/Border"))
            border_width = 0.0
            if border and len(border) >= 3:
                border_width = float(border[2])
            border_style = dereference(annotation.get("/BS")) or {}
            if border_style.get("/W") is not None:
                border_width = max(border_width, float(border_style.get("/W")))
            if border_width > 0:
                visible_link_borders += 1

    metrics["fonts"] = sorted(fonts)
    metrics["link_annotations"] = link_count
    metrics["visible_link_borders"] = visible_link_borders
    metrics["page_sizes_pt"] = sorted(set(page_sizes))

    normalized_fonts = " ".join(fonts).lower().replace("-", "")
    if "timesnewroman" not in normalized_fonts:
        failures.append("Times New Roman was not found in PDF font resources")
    if "xitsmath" not in normalized_fonts:
        failures.append("XITS Math was not found in PDF font resources")
    if visible_link_borders:
        failures.append(f"{visible_link_borders} link annotations have visible borders")

    for width, height in page_sizes:
        portrait_match = abs(width - A4_WIDTH_PT) <= 3 and abs(height - A4_HEIGHT_PT) <= 3
        landscape_match = abs(width - A4_HEIGHT_PT) <= 3 and abs(height - A4_WIDTH_PT) <= 3
        if not (portrait_match or landscape_match):
            failures.append(f"non-A4 page size detected: {width} x {height} pt")

    extracted = ""
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        result = subprocess.run(
            [pdftotext, "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if result.returncode == 0:
            extracted = result.stdout
        else:
            warnings.append(f"pdftotext returned exit code {result.returncode}")
    if not extracted.strip():
        try:
            extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception as exc:  # pragma: no cover - tool-facing error path
            warnings.append(f"fallback PDF text extraction failed: {exc}")
    metrics["extracted_text_chars"] = len(extracted.strip())
    if len(extracted.strip()) < 20:
        failures.append("PDF text is empty or not meaningfully extractable")


def validate(args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, Any] = {}

    tex_path = args.tex.resolve()
    raw_tex = read_text(tex_path)
    tex = strip_comments(raw_tex)
    style_path = tex_path.parent / "study-note-style.sty"
    style = read_text(style_path) if style_path.exists() else ""

    if not re.search(r"\\usepackage(?:\[[^]]*\])?\{study-note-style\}", tex):
        failures.append("TeX does not load the canonical study-note-style package")
    if not style_path.exists():
        failures.append("study-note-style.sty is not beside the TeX entrypoint")
    elif STYLE_VERSION not in style:
        failures.append(f"style package does not declare {STYLE_VERSION}")
    else:
        required_style_tokens = {
            "Times New Roman main font": r"\setmainfont{Times New Roman}",
            "Times New Roman sans font": r"\setsansfont{Times New Roman}",
            "XITS Math": r"\setmathfont{XITS Math}",
            "borderless links": "hidelinks",
            "must-know priority macro": r"\PriorityMust",
            "important priority macro": r"\PriorityImportant",
            "know priority macro": r"\PriorityKnow",
            "chapter map styles": "study map core",
            "formula summary table": r"\newenvironment{FormulaSummaryTable}",
            "formula summary row": r"\FormulaSummaryRow",
        }
        for label, token in required_style_tokens.items():
            if token not in style:
                failures.append(f"style package is missing {label}")

    formula_match = re.search(r"\\section\{公式速查手册\}", tex)
    section_matches = list(re.finditer(r"\\section(\*?)\{([^{}]+)\}", tex))
    special_titles = {"核心知识关系导图", "各章节关系导图", "公式速查手册", "背诵优先级速览", "全局易错点"}
    main_sections = [
        match for match in section_matches
        if not match.group(1) and match.group(2) not in special_titles
        and (formula_match is None or match.start() < formula_match.start())
    ]
    main_count = len(main_sections)
    # A compact regression fixture can generate many sections via \foreach.
    for match in re.finditer(r"\\foreach\s+\\\w+\s+in\s+\{(\d+),\.\.\.,(\d+)\}\s*\{\s*\\section\{", tex):
        main_count += max(0, int(match.group(2)) - int(match.group(1)))
    metrics["main_sections"] = main_count

    maps = {
        "knowledge": list(re.finditer(r"\\section\*?\{核心知识关系导图\}", tex)),
        "chapter": list(re.finditer(r"\\section\*?\{各章节关系导图\}", tex)),
    }
    metrics["knowledge_relationship_maps"] = len(maps["knowledge"])
    metrics["chapter_relationship_maps"] = len(maps["chapter"])
    omission = re.search(r"(?m)^\s*%\s*study-map-omitted:\s*(\S.*)$", raw_tex)
    metrics["map_omission_reason"] = omission.group(1).strip() if omission else None
    map_matches = maps["knowledge"] + maps["chapter"]
    if len(map_matches) > 1:
        failures.append("document contains multiple relationship maps")
    if omission and map_matches:
        failures.append("map omission reason is present alongside a relationship map")
    if main_count >= 1 and not map_matches and not omission:
        failures.append("relationship map is missing without a specific omission reason")
    if map_matches:
        expected = "knowledge" if main_count <= 3 else "chapter"
        if not maps[expected]:
            failures.append(f"{main_count} main section(s) require the {expected} relationship map")

    required_order = [r"\\tableofcontents"]
    if map_matches:
        required_order.append(r"\\section\*?\{(?:核心知识关系导图|各章节关系导图)\}")
    required_order.extend(
        [
            r"\\section\{公式速查手册\}",
            r"\\section\{背诵优先级速览\}",
            r"\\section\{全局易错点\}",
        ]
    )
    positions = [re.search(pattern, tex) for pattern in required_order]
    if any(match is None for match in positions):
        failures.append("required document order sections are missing")
    elif [match.start() for match in positions if match] != sorted(match.start() for match in positions if match):
        failures.append("required document sections are out of order")

    if map_matches:
        map_position = min(match.start() for match in map_matches)
        toc_match = re.search(r"\\tableofcontents", tex)
        if toc_match is not None and map_position < toc_match.start():
            failures.append("relationship map must appear after the table of contents")
        if main_sections and map_position > main_sections[0].start():
            failures.append("relationship map must appear before the main chapters")
        if formula_match is not None and map_position > formula_match.start():
            failures.append("relationship map appears after the formula summary")

    formula_tables = len(re.findall(r"\\begin\{FormulaSummaryTable\}", tex))
    formula_rows = len(re.findall(r"\\FormulaSummaryRow\b", tex))
    metrics["formula_summary_tables"] = formula_tables
    metrics["formula_summary_rows"] = formula_rows
    if formula_tables == 0:
        failures.append("formula summary does not use FormulaSummaryTable")
    if formula_rows == 0:
        failures.append("formula summary has no FormulaSummaryRow entries")

    metrics["concept_priority_markers"] = len(
        re.findall(r"\\Priority(?:Must|Important|Know)\b", tex)
    )
    metrics["tables"] = len(
        re.findall(r"\\begin\{(?:tabular|tabularx|longtable)\}", tex)
    )
    metrics["tikz_diagrams"] = len(re.findall(r"\\begin\{tikzpicture\}", tex))
    metrics["figures"] = len(re.findall(r"\\begin\{figure\*?\}", tex))
    metrics["included_graphics"] = len(re.findall(r"\\includegraphics\b", tex))
    metrics["content_boxes"] = len(
        re.findall(
            r"\\begin\{(?:definitionbox|takeawaybox|keypointbox|formulabox|proofbox|mistakebox)\}",
            tex,
        )
    )
    metrics["visual_blocks"] = (
        metrics["tables"]
        + metrics["tikz_diagrams"]
        + metrics["figures"]
        + metrics["included_graphics"]
    )

    inventory = read_text(args.inventory.resolve()) if args.inventory else ""
    if args.inventory:
        metrics["inventory_rows"] = count_inventory_rows(inventory)

    log = read_text(args.log.resolve()) if args.log else ""
    blocking_log_patterns = {
        "LaTeX error": r"! LaTeX Error|Package .* Error",
        "undefined control sequence": r"Undefined control sequence",
        "missing font": r"fontspec error|The font .* cannot be found",
        "font substitution": r"Font shape .* undefined|Some font shapes were not available",
        "undefined references": r"There were undefined references|Reference .* undefined",
    }
    for label, pattern in blocking_log_patterns.items():
        if re.search(pattern, log, flags=re.IGNORECASE):
            failures.append(f"compile log contains {label}")
    overfull = len(re.findall(r"Overfull \\hbox|Overfull \\vbox", log))
    underfull = len(re.findall(r"Underfull \\hbox|Underfull \\vbox", log))
    metrics["overfull_boxes"] = overfull
    metrics["underfull_boxes"] = underfull
    if overfull:
        warnings.append(f"compile log contains {overfull} overfull box warning(s)")
    if underfull:
        warnings.append(f"compile log contains {underfull} underfull box warning(s)")

    if args.pdf:
        pdf_checks(args.pdf.resolve(), failures, warnings, metrics)

    return {
        "status": "pass" if not failures else "fail",
        "style_contract": STYLE_VERSION,
        "failures": failures,
        "warnings": warnings,
        "metrics": metrics,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", type=Path, required=True, help="LaTeX entrypoint")
    parser.add_argument("--pdf", type=Path, help="compiled PDF")
    parser.add_argument("--log", type=Path, help="XeLaTeX log")
    parser.add_argument("--inventory", type=Path, help="source inventory markdown")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    for label in ("tex", "pdf", "log", "inventory"):
        path = getattr(args, label)
        if path is not None and not path.is_file():
            parser.error(f"--{label} is not a file: {path}")

    report = validate(args)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"status: {report['status']}")
        print(f"style contract: {report['style_contract']}")
        for failure in report["failures"]:
            print(f"FAIL: {failure}")
        for warning in report["warnings"]:
            print(f"WARN: {warning}")
        for key, value in report["metrics"].items():
            print(f"{key}: {value}")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
