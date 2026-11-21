"""Unblind a filled-in scores.csv and apply the release gate from evals/README.md.

Usage: python scripts/tally.py evals/runs/<date>
"""
from __future__ import annotations

import collections
import csv
import json
import pathlib
import sys

HARD = ("unsupported_claims", "arithmetic_errors")


def num(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        sys.exit(f"Not a number in scores.csv: {value!r}")


def main() -> None:
    run = pathlib.Path(sys.argv[1])
    key = json.loads((run / "key.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((run / "review" / "scores.csv").open(encoding="utf-8")))

    by_skill = collections.defaultdict(lambda: collections.defaultdict(list))
    problems = collections.defaultdict(list)
    for row in rows:
        k = key[row["packet"]]
        if not row.get("preferred"):
            sys.exit(f"{row['packet']} has no preference recorded yet")
        skill_side = k["A"] == "skill" and "A" or "B"
        pref = row["preferred"].strip().upper()
        winner = "tie" if pref == "TIE" else ("skill" if pref == skill_side else "plain")
        by_skill[k["skill"]][k["case"]].append((winner, row.get("reason", "").strip(), row["packet"]))
        s = skill_side
        hard = sum(num(row[f"{s}_{f}"]) for f in HARD)
        if hard:
            problems[k["skill"]].append(f"{row['packet']} ({k['case']}): {hard} unsupported claim(s) or arithmetic error(s)")
        if row.get(f"missed_critical_{s}", "").strip().lower() == "yes":
            problems[k["skill"]].append(f"{row['packet']} ({k['case']}): missed a critical issue")

    for skill, cases in sorted(by_skill.items()):
        print(f"\n== {skill}")
        wins = 0
        for case, results in sorted(cases.items()):
            verdicts = {w for w, _, _ in results}
            if verdicts == {"skill"} and all(reason for _, reason, _ in results):
                wins += 1
                call = "skill preferred"
            elif len(verdicts) > 1:
                call = "INCONSISTENT across repeats: investigate"
            else:
                call = f"{verdicts.pop()} (or skill without a stated reason)"
            print(f"  {case}: {call}")
            for winner, reason, packet in results:
                print(f"    {packet} {winner}: {reason or '(no reason given)'}")
        for p in problems[skill]:
            print(f"  ! {p}")
        passed = wins >= 3 and not problems[skill]
        print(f"  Skill preferred on {wins} of {len(cases)} cases. {'PASS' if passed else 'DOES NOT PASS'} the first-round gate.")


if __name__ == "__main__":
    main()
