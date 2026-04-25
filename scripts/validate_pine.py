#!/usr/bin/env python3
"""
Pine Script Validator
Checks Pine Script files for common syntax patterns and version declarations.
"""

import os
import sys
import re
from pathlib import Path


def check_pine_file(filepath: str) -> list[str]:
    """Check a single Pine Script file for common issues."""
    issues = []
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()

    # Check for version declaration
    has_version = any(re.match(r"^\s*//@version=\d+", line) for line in lines)
    if not has_version:
        issues.append(f"  [WARN] {filepath}: Missing //@version declaration")

    # Check for indicator or strategy declaration
    has_indicator = any(re.match(r"^\s*(indicator|strategy|library)\s*\(", line) for line in lines)
    if not has_indicator:
        issues.append(f"  [WARN] {filepath}: Missing indicator/strategy/library declaration")

    # Check for trailing whitespace
    for i, line in enumerate(lines, 1):
        if line != line.rstrip():
            issues.append(f"  [WARN] Trailing whitespace on line {i}")

    return issues


def validate_directory(directory: str) -> int:
    """Validate all Pine Script files in a directory tree."""
    error_count = 0
    pine_files = list(Path(directory).rglob("*.pine"))

    if not pine_files:
        print("No .pine files found.")
        return 0

    print(f"Validating {len(pine_files)} Pine Script file(s)...\n")

    for pine_file in sorted(pine_files):
        rel_path = pine_file.relative_to(directory)
        issues = check_pine_file(str(pine_file))
        if issues:
            print(f"[{rel_path}]")
            for issue in issues:
                print(issue)
            print()
            error_count += len(issues)
        else:
            print(f"[OK] {rel_path}")

    print(f"\nDone. {error_count} issue(s) found in {len(pine_files)} file(s).")
    return error_count


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(min(validate_directory(target), 1))
