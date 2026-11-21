Skills are organized into bucket folders under `skills/`, named for the moment a PM needs help:

- `delivery/`: running one project's week (meetings, status, slips)
- `portfolio/`: steering, decisions and cross-project work
- `in-progress/`: beta: public on purpose, under blind test, not shipped in the plugin
- `deprecated/`: no longer used

A skill moves from `in-progress/` to a promoted bucket (`delivery/` or `portfolio/`) only after it passes the release gate in [`evals/README.md`](./evals/README.md). Record the review result in `CHANGELOG.md` when it moves.

Every skill in a promoted bucket must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`'s `skills` array (the plugin ships exactly the promoted set). Skills in `in-progress/` and `deprecated/` must not appear in `plugin.json`. The top-level `README.md` lists `in-progress/` skills under their own heading.

Each skill entry in the top-level `README.md` links the skill name to its `SKILL.md`. Each bucket folder has a `README.md` listing every skill in it with a one-line description.

Promoted skills have a human-facing docs page at `docs/<bucket>/<skill-name>.md` with four sections in this order: **What it does**, **When to reach for it**, **It's working if**, **Common questions**. Pages for `in-progress/` skills may be drafted ahead under `docs/in-progress/`, and move with the skill.

Every promoted skill has a pasteable exercise at `examples/<skill-name>.md`: instructions plus a short fictional packet, usable in a plain chat with no install, followed by a worked answer. Eval cases live in `evals/<skill-name>/` and are never copied into a skill folder or an exercise.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`) or model-invoked (neither). `ask-justin` is the router: whenever you add, rename, remove or change how a user-reachable skill fits a moment, update it.

All examples, cases and exercises are fictional. No real client, employer, project or person, and nothing copied from a private source. No private repository links.

No em-dashes anywhere in this repo's prose. Rewrite the sentence with a comma, colon, period, parentheses or conjunction instead.

Write in plain PM language. No jargon a sponsor wouldn't use, no AI-sounding phrasing.

Build the Claude upload ZIPs with `python scripts/build_zips.py`; it writes `dist/<skill>.zip` for every skill outside `deprecated/`. Run `claude plugin validate . --strict` after touching either manifest.
