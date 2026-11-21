"""Shuffle each skill/plain pair into Answer A and Answer B and write review packets and a score sheet.

Usage: python scripts/blind.py evals/runs/<date> [--seed N]
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import random
import re

FIELDS = ["packet", "skill", "case", "preferred", "reason",
          "A_missed_issues", "A_false_escalations", "A_unsupported_claims", "A_arithmetic_errors", "A_edits",
          "B_missed_issues", "B_false_escalations", "B_unsupported_claims", "B_arithmetic_errors", "B_edits",
          "missed_critical_A", "missed_critical_B", "notes"]

PACKET = """# Review packet {packet}

Case: {case}. One answer used the skill and one did not; which is which is hidden.

Read the PM's request and material, then both answers. Score each answer in scores.csv (row {packet}), using the
answer key for this case. Then say which answer you'd take into the meeting, and why, in one sentence.

## What the PM pasted

{prompt}

---

## Answer A

{a}

---

## Answer B

{b}
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    run = pathlib.Path(args.run_dir)
    rng = random.Random(args.seed)
    review = run / "review"
    review.mkdir(exist_ok=True)

    pairs = []
    for case_dir in sorted((run / "raw").glob("*/*")):
        for skill_file in sorted(case_dir.glob("skill-*.md")):
            rep = re.search(r"skill-(\d+)", skill_file.name).group(1)
            plain_file = case_dir / f"plain-{rep}.md"
            if plain_file.exists():
                pairs.append((case_dir.parent.name, case_dir.name, rep, skill_file, plain_file))
    rng.shuffle(pairs)  # packet numbers carry no order information

    key, rows = {}, []
    for n, (skill, case, rep, skill_file, plain_file) in enumerate(pairs, 1):
        packet = f"P{n:02d}"
        skill_is_a = rng.random() < 0.5
        a, b = (skill_file, plain_file) if skill_is_a else (plain_file, skill_file)
        prompt = (skill_file.parent / "prompt.md").read_text(encoding="utf-8")
        (review / f"{packet}.md").write_text(PACKET.format(
            packet=packet, case=f"{skill}/{case}", prompt=prompt.strip(),
            a=a.read_text(encoding="utf-8").strip(), b=b.read_text(encoding="utf-8").strip()), encoding="utf-8")
        key[packet] = {"skill": skill, "case": case, "repeat": rep, "A": "skill" if skill_is_a else "plain"}
        rows.append({"packet": packet, "skill": skill, "case": case})

    with (review / "scores.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in sorted(rows, key=lambda r: r["packet"]):
            writer.writerow(row)
    (run / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    print(f"{len(pairs)} packets in {review}. Key in {run / 'key.json'} (keep it from the reviewer).")
    print("Scores: preferred = A, B or tie. Counts are numbers. Edits = none, light or heavy. missed_critical = yes or no.")


if __name__ == "__main__":
    main()
