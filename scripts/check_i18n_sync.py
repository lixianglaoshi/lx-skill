#!/usr/bin/env python3
"""Check that localized README files track the current Chinese source README."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_FILES = (
    "README.md",
    "README.en.md",
    "README.es.md",
    "README.de.md",
    "README.ja.md",
    "README.ko.md",
)
SKILL_IDS = (
    "lx-education-diagnosis",
    "lx-parent-learning-environment",
    "lx-ai-learning-coach",
    "lx-institutional-social-coach",
)
MARKER_PATTERN = re.compile(
    r"<!-- i18n-source-sha256: (?P<hash>[0-9a-f]{64}|PLACEHOLDER) -->"
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def normalized_source(text: str) -> str:
    without_marker = MARKER_PATTERN.sub("", text, count=1)
    return without_marker.strip() + "\n"


def source_hash() -> str:
    source = read_text(ROOT / "README.md")
    return hashlib.sha256(normalized_source(source).encode("utf-8")).hexdigest()


def update_markers(expected_hash: str) -> None:
    for name in README_FILES:
        path = ROOT / name
        if not path.exists():
            raise FileNotFoundError(f"Missing localized README: {name}")
        text = read_text(path)
        if not MARKER_PATTERN.search(text):
            raise ValueError(f"Missing i18n marker in {name}")
        updated = MARKER_PATTERN.sub(
            f"<!-- i18n-source-sha256: {expected_hash} -->", text, count=1
        )
        path.write_text(updated, encoding="utf-8")


def validate(expected_hash: str) -> list[str]:
    errors: list[str] = []
    for name in README_FILES:
        path = ROOT / name
        if not path.exists():
            errors.append(f"Missing localized README: {name}")
            continue

        text = read_text(path)
        marker = MARKER_PATTERN.search(text)
        if marker is None:
            errors.append(f"{name}: missing i18n source marker")
        elif marker.group("hash") != expected_hash:
            errors.append(
                f"{name}: stale marker {marker.group('hash')}; expected {expected_hash}"
            )

        for other in README_FILES:
            if other != name and other not in text:
                errors.append(f"{name}: language navigation is missing {other}")

        for skill_id in SKILL_IDS:
            if skill_id not in text:
                errors.append(f"{name}: missing skill id {skill_id}")

        if "https://github.com/lixianglaoshi/lx-skill.git" not in text:
            errors.append(f"{name}: missing canonical clone URL")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify localized README synchronization."
    )
    parser.add_argument(
        "--update-markers",
        action="store_true",
        help="Record the current Chinese README fingerprint in all localized READMEs.",
    )
    args = parser.parse_args()

    expected_hash = source_hash()
    if args.update_markers:
        update_markers(expected_hash)
        print(f"Updated i18n markers to {expected_hash}")

    errors = validate(expected_hash)
    if errors:
        print("README localization check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"README localization check passed for {len(README_FILES)} languages "
        f"at source {expected_hash}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
