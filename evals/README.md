# How a skill earns its place

No skill leaves `in-progress/` on my say-so. Each one is compared blind against a plain assistant on fictional cases, and an experienced PM picks the answer they'd take into a meeting.

## The cases

Each skill has four fictional cases in `evals/<skill>/cases/`:

| Case | What it tests |
| --- | --- |
| Genuine exception | There is a real problem. Does it get caught, with evidence? |
| Clean | Nothing is wrong. Does it stay quiet? |
| Ambiguous | The evidence conflicts. Does it name the question instead of guessing? |
| Shortcut trap | A plausible shortcut gives the wrong answer. Does it avoid it? |

Each case has `input.md` (what the PM pastes) and `expected.md` (the answer key). Answer keys never go into a skill folder, an exercise or a prompt. A PM validates each key, including every date calculation, before the case is run.

Every skill also has one `request.md`: the same well-written PM request, used in both arms.

## Running a comparison

```bash
python scripts/run_comparison.py --skill trace-the-impact --model <model-id>
```

For each case it runs **two arms, twice each**, in fresh headless Claude Code sessions with no tools, no MCP servers, no other skills and no saved session:

- **skill arm**: the request and material, with the skill's `SKILL.md` added to the system prompt.
- **plain arm**: the same request and material, nothing added.

Runs use your Claude plan through Claude Code (`claude -p`). The script refuses to start if `ANTHROPIC_API_KEY` is set, so nothing bills an API key. Outputs land in `evals/runs/<date>/` (git-ignored).

The claude.ai upload path (the ZIP) is checked separately by hand: upload `dist/<skill>.zip`, paste one case, and confirm the skill fires and the answer matches the headless one in substance.

## Blinding

```bash
python scripts/blind.py evals/runs/<date>
```

For each case and repeat it shuffles the two answers into **Answer A** and **Answer B** and writes a review packet to `evals/runs/<date>/review/`, plus a `scores.csv` to fill in. The key that maps A and B back to the arms goes in `evals/runs/<date>/key.json`. Don't open it, and don't give it to the reviewer.

Send the reviewer the `review/` folder and the answer keys only.

## What the reviewer records

For each packet, in `scores.csv`, per answer:

- missed material issues
- false escalations
- unsupported claims (including invented approvals, dependencies or citations)
- arithmetic errors
- edits needed before they'd use it (none, light, heavy)

And per packet: which answer they'd take into the meeting (A, B or tie), and why, in one sentence.

## The release gate

```bash
python scripts/tally.py evals/runs/<date>
```

A skill passes the first round when all of these hold:

1. The reviewer prefers the skill arm on **at least three of the four cases** (both repeats of a case must lean the same way, or the case counts as a tie).
2. Each preference comes with a **specific improvement** the reviewer can name.
3. **No missed critical issue** in any skill-arm run.
4. **Zero** invented approvals, fabricated citations, unsupported dependencies or material arithmetic errors across the skill arm's runs.

If both answers are equally accurate, less editing or a better handoff can count, when the reviewer names the difference. Inconsistent repeats are a reason to investigate, not to average. A tie or failure means revising the skill privately and retesting on **fresh** cases, never the same ones.
