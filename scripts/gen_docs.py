"""Usage: python scripts/gen_docs.py .

Generate README.md, bucket READMEs, plugin.json skills array and the ask-justin router from skills/."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1])
PLUGIN = ROOT / "plugins" / "ondatrace-pmo-skills"
SKILLS = PLUGIN / "skills"
LINK = "./plugins/ondatrace-pmo-skills/skills"
DL = "https://github.com/jsconu/pmo-skills/releases/latest/download"
BUCKETS = [
    ("frame-the-work", "Frame the work", "Starting something new: the sponsor, the charter, the project list, the backlog."),
    ("run-the-week", "Run the week", "The weekly rhythm of one project: meetings, status, risks and messages."),
    ("test-the-status", "Test the status", "Before anything goes to a sponsor: check the claims, the dates, the impact of a slip, and whether a change needs approval."),
    ("run-the-portfolio", "Run the portfolio", "Across projects: steering, capacity, shared risks and where to spend today."),
    ("follow-the-decision", "Follow the decision", "After the decision: did it work, did it land, who owns what, and are people ready."),
    ("measure-and-learn", "Measure and learn", "Money, metrics and lessons."),
]


def skill_info(md):
    text = md.read_text(encoding="utf-8")
    desc = re.search(r"^description: (.*)$", text, re.M).group(1)
    user = "disable-model-invocation: true" in text
    return desc.split(". Use when")[0].rstrip(".") + ".", user


def rows(bucket, link_prefix):
    out = []
    for md in sorted((SKILLS / bucket).glob("*/SKILL.md")):
        name = md.parent.name
        summary, _ = skill_info(md)
        out.append(f"| **[{name}]({link_prefix}{name}/SKILL.md)** | {summary} | [Download]({DL}/{name}.zip) |")
    return out


# Bucket READMEs
for bucket, title, blurb in BUCKETS:
    lines = [f"# {title}", "", blurb, "", "| Skill | What it does | Claude upload |", "| --- | --- | --- |"]
    lines += rows(bucket, "./")
    (SKILLS / bucket / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

# plugin.json skills array
plugin = PLUGIN / ".claude-plugin" / "plugin.json"
data = json.loads(plugin.read_text(encoding="utf-8"))
data["skills"] = ["./skills/start-here/ask-justin"] + [
    f"./skills/{b}/{md.parent.name}" for b, _, _ in BUCKETS for md in sorted((SKILLS / b).glob("*/SKILL.md"))]
plugin.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

# README reference section
ref = []
for bucket, title, blurb in BUCKETS:
    ref += [f"### {title}", "", blurb, "", "| Skill | What it does | Claude upload |", "| --- | --- | --- |"]
    ref += rows(bucket, f"{LINK}/{bucket}/")
    ref.append("")
readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
start, end = "<!-- skills:start -->", "<!-- skills:end -->"
text = text.split(start)[0] + start + "\n\n" + "\n".join(ref) + "\n" + end + text.split(end)[1]
readme.write_text(text, encoding="utf-8")

# Router map
router = SKILLS / "start-here" / "ask-justin" / "SKILL.md"
rt = router.read_text(encoding="utf-8")
m = []
for bucket, title, blurb in BUCKETS:
    m += [f"## {title}", "", blurb, ""]
    for md in sorted((SKILLS / bucket).glob("*/SKILL.md")):
        m.append(f"- **{md.parent.name}**: {skill_info(md)[0]}")
    m.append("")
rt = rt.split("<!-- map:start -->")[0] + "<!-- map:start -->\n\n" + "\n".join(m) + "<!-- map:end -->" + rt.split("<!-- map:end -->")[1]
router.write_text(rt, encoding="utf-8")
print("generated", len(data["skills"]), "plugin skills")
