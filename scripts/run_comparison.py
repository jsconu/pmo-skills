"""Run the skill arm and the plain arm on every case for one skill, in fresh headless Claude Code sessions.

Usage: python scripts/run_comparison.py --skill trace-the-impact --model <model-id> [--repeats 2] [--case 01-collision]

Runs bill the Claude plan that Claude Code is signed in to. The script refuses to run if ANTHROPIC_API_KEY is set.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUCKETS = ("frame-the-work", "run-the-week", "test-the-status", "run-the-portfolio", "follow-the-decision", "measure-and-learn", "start-here")
BLOCKED_TOOLS = ("Bash", "PowerShell", "Read", "Edit", "Write", "Glob", "Grep", "NotebookEdit", "WebFetch",
                 "WebSearch", "Agent", "Task", "TodoWrite", "Skill")


def find_skill(name: str) -> pathlib.Path:
    for bucket in BUCKETS:
        path = ROOT / "plugins" / "ondatrace-pmo-skills" / "skills" / bucket / name / "SKILL.md"
        if path.exists():
            return path
    sys.exit(f"No SKILL.md for {name} in {', '.join(BUCKETS)}")


def body_of(skill_md: pathlib.Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    return text.strip()


def prompt_for(request: str, material: str) -> str:
    return f"{request.strip()}\n\n--- MATERIAL ---\n\n{material.strip()}\n"


def run_once(prompt: str, model: str, system_extra: str | None, env: dict) -> str:
    claude = shutil.which("claude")
    if not claude:
        sys.exit("claude (Claude Code) is not on PATH")
    cmd = [
        claude, "-p", "--model", model, "--output-format", "text",
        # `--tools ""` does not remove the built-in tools in -p mode, so block them by name.
        "--disallowedTools", *BLOCKED_TOOLS,
        "--strict-mcp-config", "--disable-slash-commands", "--no-session-persistence",
    ]
    if system_extra:
        cmd += ["--append-system-prompt", system_extra]
    # A fresh empty working directory per run, so no project files or instructions leak in.
    with tempfile.TemporaryDirectory(prefix="pmo-eval-") as cwd:
        done = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
                              cwd=cwd, env=env, timeout=600)
    if done.returncode != 0:
        raise RuntimeError(f"claude exited {done.returncode}: {done.stderr.strip()[:500]}")
    return done.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", required=True)
    parser.add_argument("--model", required=True, help="Same model for both arms, for example the one you will recommend")
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--case", action="append", help="Run only these case folders")
    parser.add_argument("--out", help="Run folder (default evals/runs/<today>)")
    args = parser.parse_args()

    if os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is set. Unset it so runs use the Claude plan, not API billing.")
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}

    skill_text = body_of(find_skill(args.skill))
    skill_dir = ROOT / "evals" / args.skill
    request = (skill_dir / "request.md").read_text(encoding="utf-8")
    cases = sorted(p for p in (skill_dir / "cases").iterdir() if p.is_dir())
    if args.case:
        cases = [c for c in cases if c.name in args.case]

    out = pathlib.Path(args.out) if args.out else ROOT / "evals" / "runs" / dt.date.today().isoformat()
    total = len(cases) * 2 * args.repeats
    print(f"{args.skill}: {len(cases)} cases x 2 arms x {args.repeats} repeats = {total} runs on {args.model}")

    for case in cases:
        prompt = prompt_for(request, (case / "input.md").read_text(encoding="utf-8"))
        target = out / "raw" / args.skill / case.name
        target.mkdir(parents=True, exist_ok=True)
        (target / "prompt.md").write_text(prompt, encoding="utf-8")
        for rep in range(1, args.repeats + 1):
            for arm, extra in (("skill", skill_text), ("plain", None)):
                path = target / f"{arm}-{rep}.md"
                if path.exists():
                    print(f"  skip {path.relative_to(out)} (exists)")
                    continue
                print(f"  run  {case.name} {arm} {rep}")
                path.write_text(run_once(prompt, args.model, extra, env) + "\n", encoding="utf-8")

    meta = out / "runs.json"
    record = json.loads(meta.read_text(encoding="utf-8")) if meta.exists() else []
    record.append({"skill": args.skill, "model": args.model, "repeats": args.repeats,
                   "cases": [c.name for c in cases], "at": dt.datetime.now().isoformat(timespec="seconds")})
    meta.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"Done. Next: python scripts/blind.py {out}")


if __name__ == "__main__":
    main()
