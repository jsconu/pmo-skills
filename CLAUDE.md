Skills are organized into folders under `skills/`, named for the moment a PM needs help:

- `frame-the-work/`: starting something new (sponsor, charter, project list, backlog)
- `run-the-week/`: one project's weekly rhythm (meetings, status, risks, messages)
- `test-the-status/`: checks before anything goes to a sponsor (claims, dates, slips, change requests)
- `run-the-portfolio/`: across projects (steering, capacity, shared risks, today's focus)
- `follow-the-decision/`: after a decision (outcome, adoption, ownership, change management)
- `measure-and-learn/`: money, metrics and lessons
- `start-here/`: the `ask-justin` router

Every skill must have an entry in `.claude-plugin/plugin.json`'s `skills` array, a row in the top-level `README.md` and a row in its folder's `README.md`. Don't edit those by hand: run `python scripts/gen_docs.py .` after adding, renaming or re-describing a skill. It rebuilds the README tables, the folder READMEs, the plugin list and the map in `ask-justin`.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`) or model-invoked (neither). Only `ask-justin` is user-invoked. Every skill folder has an `agents/openai.yaml` with a display name and short description.

A skill folder holds its `SKILL.md` and any files it references (templates such as `decision-log.md`). Each skill must work on its own when uploaded as a ZIP, so copy a shared template into each skill that uses it rather than linking across folders.

Pasteable exercises live in `examples/<skill-name>.md`: instructions plus a short fictional packet, usable in a plain chat with no install, followed by a worked answer. Optional test cases live in `evals/<skill-name>/`.

All examples, cases and exercises are fictional. No real client, employer, project or person, and nothing copied from a private source. No private repository links.

No em-dashes anywhere in this repo's prose. Rewrite the sentence with a comma, colon, period, parentheses or conjunction instead.

Write in plain PM language. No jargon a sponsor wouldn't use, no AI-sounding phrasing.

Releases: build with `python scripts/build_zips.py`, which writes `dist/<skill>.zip` for every skill plus `dist/pmo-skills-all.zip` and `dist/pmo-skills-all.md` (every skill in one text file for non-Claude assistants), then attach them to a GitHub release. The README download links point at `releases/latest/download/<skill>.zip`, so asset names must stay the same. Run `claude plugin validate . --strict` after touching either manifest, and bump `version` in `plugin.json` with each release.
