"""Build one Claude upload ZIP per skill: dist/<skill>.zip containing <skill>/SKILL.md and its files.

Usage: python scripts/build_zips.py [--only name ...]

Excludes deprecated skills, the user-invoked router (it needs the other skills installed beside it) and agents/
metadata, which claude.ai doesn't use.
"""
from __future__ import annotations

import argparse
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {"ask-justin"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="*")
    args = parser.parse_args()
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for skill_md in sorted(ROOT.glob("skills/*/*/SKILL.md")):
        folder = skill_md.parent
        if folder.parent.name == "deprecated" or folder.name in SKIP:
            continue
        if args.only and folder.name not in args.only:
            continue
        target = dist / f"{folder.name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(folder.rglob("*")):
                rel = path.relative_to(folder)
                if path.is_file() and rel.parts[0] != "agents":
                    zf.write(path, pathlib.PurePosixPath(folder.name, *rel.parts))
        print(f"{target.relative_to(ROOT)}  ({', '.join(zipfile.ZipFile(target).namelist())})")


if __name__ == "__main__":
    main()
