"""Fast, offline checks for the published PMO Skills package."""
from __future__ import annotations

import json
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
ERRORS: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> int:
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    declared = manifest["skills"]
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])), "Invalid semantic version")
    check(len(declared) == len(set(declared)), "Duplicate skill in plugin manifest")
    actual = sorted(ROOT.glob("skills/*/*/SKILL.md"))
    expected = {str(p.parent.relative_to(ROOT)).replace("\\", "/") for p in actual}
    declared_set = {p.removeprefix("./") for p in declared}
    check(declared_set == expected, f"Manifest mismatch: missing={sorted(expected-declared_set)}, extra={sorted(declared_set-expected)}")

    names: set[str] = set()
    for skill in actual:
        raw = skill.read_text(encoding="utf-8")
        rel = skill.relative_to(ROOT)
        name = skill.parent.name
        check(name not in names, f"Duplicate skill name: {name}")
        names.add(name)
        check(raw.startswith("---\n"), f"{rel}: missing YAML frontmatter")
        head = raw.split("---", 2)[1] if raw.startswith("---\n") and raw.count("---") >= 2 else ""
        match = re.search(r"^name:\s*(.+)$", head, re.M)
        check(bool(match) and match.group(1).strip() == name, f"{rel}: frontmatter name mismatch")
        check(bool(re.search(r"^description:\s*\S", head, re.M)), f"{rel}: missing description")
        check("## Learn from corrections (user-controlled)" in raw, f"{rel}: missing personal learning guidance")
        if name == "ask-justin":
            continue
        package = DIST / f"{name}.zip"
        check(package.is_file(), f"Missing package {package.name}")
        if package.is_file():
            with zipfile.ZipFile(package) as z:
                check(z.testzip() is None, f"Corrupted ZIP {package.name}")
                check(f"{name}/SKILL.md" in z.namelist(), f"Missing SKILL.md in {package.name}")
                if f"{name}/SKILL.md" in z.namelist():
                    check(z.read(f"{name}/SKILL.md") == skill.read_bytes(), f"Stale skill contents in {package.name}")

    packages = {p.name for p in DIST.glob("*.zip")} - {"pmo-skills-all.zip"}
    expected_packages = {f"{p.parent.name}.zip" for p in actual if p.parent.name != "ask-justin"}
    check(packages == expected_packages, "Individual ZIP files do not match source skill list")
    bundle = DIST / "pmo-skills-all.zip"
    check(bundle.is_file(), "Missing all-skills ZIP")
    if bundle.is_file():
        with zipfile.ZipFile(bundle) as z:
            check(set(z.namelist()) == expected_packages, "All-skills ZIP is incomplete")
            check(z.testzip() is None, "All-skills ZIP failed integrity check")
    combined = DIST / "pmo-skills-all.md"
    check(combined.is_file(), "Missing combined Markdown")
    if combined.is_file():
        text = combined.read_text(encoding="utf-8")
        check(f"Version {manifest['version']}." in text, "Combined Markdown has wrong version")
        for name in sorted(names - {"ask-justin"}):
            check(f"SKILL: {name}" in text, f"Combined Markdown missing {name}")

    if ERRORS:
        for error in ERRORS:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print(f"PASS: {len(actual)} skill sources, {len(expected_packages)} upload ZIPs, bundle and combined Markdown")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
