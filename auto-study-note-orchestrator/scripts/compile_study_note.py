#!/usr/bin/env python3
"""Compile a study note with XeLaTeX, rerunning only while references change."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


RERUN_WARNING = re.compile(
    r"Rerun to get (?:cross-references|outlines|citations) right|"
    r"Label\(s\) may have changed|"
    r"Package rerunfilecheck Warning: File .* has changed|"
    r"Please rerun LaTeX",
    re.IGNORECASE,
)
UNRESOLVED = re.compile(
    r"There were undefined (?:references|citations)|Reference [`'].+?[`'] on page .* undefined|"
    r"Citation [`'].+?[`'] on page .* undefined",
    re.IGNORECASE,
)


def read_sidecar(path: Path) -> bytes | None:
    return path.read_bytes() if path.is_file() else None


def compile_note(tex_path: Path, max_passes: int) -> tuple[bool, int, str]:
    engine = shutil.which("xelatex")
    if engine is None:
        return False, 0, "xelatex is not available on PATH"

    source = tex_path.read_text(encoding="utf-8", errors="replace")
    has_toc = r"\tableofcontents" in source
    has_refs = bool(re.search(r"\\(?:ref|eqref|pageref|autoref|cref|label|cite)\b", source))
    tracked = [tex_path.with_suffix(".out")]
    if has_toc:
        tracked.append(tex_path.with_suffix(".toc"))
    if has_refs:
        tracked.append(tex_path.with_suffix(".aux"))

    for pass_number in range(1, max_passes + 1):
        before = {path: read_sidecar(path) for path in tracked}
        result = subprocess.run(
            [engine, "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        log_path = tex_path.with_suffix(".log")
        log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.is_file() else result.stdout
        if result.returncode != 0:
            tail = "\n".join((result.stdout + "\n" + result.stderr).splitlines()[-12:])
            return False, pass_number, f"XeLaTeX failed (exit {result.returncode}):\n{tail}"

        changed = [path.suffix for path in tracked if before[path] != read_sidecar(path)]
        rerun_warning = bool(RERUN_WARNING.search(log))
        unresolved = bool(UNRESOLVED.search(log))
        if not changed and not rerun_warning and not unresolved:
            return True, pass_number, "directory, bookmarks, and references are stable"
        if pass_number == max_passes:
            reasons = []
            if changed:
                reasons.append("changed sidecars: " + ", ".join(changed))
            if rerun_warning:
                reasons.append("rerun warning remains")
            if unresolved:
                reasons.append("unresolved reference or citation remains")
            return False, pass_number, "; ".join(reasons)

    raise AssertionError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", type=Path, required=True, help="LaTeX entrypoint")
    parser.add_argument("--max-passes", type=int, default=4, help="maximum runs (default: 4)")
    args = parser.parse_args()
    if not args.tex.is_file():
        parser.error(f"not a file: {args.tex}")
    if args.max_passes < 1:
        parser.error("--max-passes must be positive")
    success, passes, detail = compile_note(args.tex.resolve(), args.max_passes)
    print(f"{'PASS' if success else 'FAIL'}: {passes} XeLaTeX pass(es); {detail}")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
