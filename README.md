# PMO Skills for Real Project Managers

By **Justin Scoville, PMP, PgMP**. Published by [Ondatrace](https://ondatrace.com).

Agent skills for project managers, sponsors and PMO leaders: the checks I run on a meeting, a status report or a slipped date before anything goes to steering.

AI assistants are quick to write a status report and quick to raise a risk. They are much worse at the part of the job that matters: telling a forecast from a commitment, a suggestion from a decision, and a slip that still has ten days of buffer from one that collides. These skills are small, plain-language methods that hold an assistant to that standard. They work with whatever you paste in. No connectors, no code, no account.

Use them, adapt them, pass them to a colleague. If you hit a case they get wrong, [tell me](#contributing).

## Try one in five minutes (no install)

1. Open a chat with Claude (or whichever assistant your company approves).
2. Open an exercise below, copy the whole thing, and paste it in.
3. Read the answer, then compare it with the worked answer underneath the exercise.

| Exercise | The question |
| --- | --- |
| [The vendor slipped](./examples/trace-the-impact.md) | There are still ten days of buffer. Would you escalate? |
| [Did anyone approve the new date?](./examples/challenge-my-status.md) | A vendor forecast crept into the status draft. |
| [Who actually owns that?](./examples/debrief-the-meeting.md) | A decision, a suggestion, and an action nobody accepted. |

Each exercise uses fictional projects and people.

## Install for repeat use

<details>
<summary><strong>Claude (claude.ai, desktop or mobile)</strong></summary>

1. Download a skill ZIP from the [latest release](https://github.com/jsconu/pmo-skills/releases/latest).
2. In Claude, open **Settings > Capabilities**, make sure code execution and file creation are on, then upload the ZIP under **Skills**.
3. Start a new chat and paste your material. Claude picks up the skill when it fits.

Skills work on Free and paid plans. On Team and Enterprise plans an admin may need to allow them. If upload isn't available in your workspace, use the paste-in exercises above instead. [Claude's instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

</details>

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add jsconu/pmo-skills
claude plugin install pmo-skills@jsconu
```

</details>

<details>
<summary><strong>Any other agent, or editable files</strong></summary>

```bash
npx skills@latest add jsconu/pmo-skills
```

</details>

## Why these skills exist

### #1: The recap says it was decided. It wasn't.

> "The great enemy of communication, we find, is the illusion of it."
>
> William H. Whyte, "Is Anybody Listening?", Fortune, 1950

**The problem.** An assistant summarising a meeting rounds everything up. "Maybe we should" becomes a decision. "Priya, can you chase the vendor?" becomes Priya's action, even though Priya had already dropped off the call. A week later nobody did it, and the recap says they agreed to.

**The fix.** [`debrief-the-meeting`](./skills/in-progress/debrief-the-meeting/SKILL.md) separates what was said, what was decided and by whom, and what someone actually accepted in their own words. Missing owners and dates stay visibly missing, so you know exactly who to chase.

### #2: The status report quietly moved the date.

> "How does a project get to be a year late? ... One day at a time."
>
> Frederick P. Brooks Jr., The Mythical Man-Month

**The problem.** A vendor emails a new forecast. It ends up in this week's draft as the date, the colour stays green, and the approved baseline disappears. Nobody approved anything, and the sponsor finds out at steering.

**The fix.** [`challenge-my-status`](./skills/in-progress/challenge-my-status/SKILL.md) reads your draft against the last approved report and the evidence, matches claims by milestone rather than by similar-looking dates, and hands back the one or two claims a sponsor would challenge, with wording you can paste.

### #3: Every slip gets escalated, so none of them land.

**The problem.** Ask an assistant whether a slip is a risk and it will usually say yes. That sounds safe, but a PM who escalates a slip with ten days of buffer spends credibility they'll need for the real collision. The opposite failure exists too: a date that looks fine until you notice the work needed the input a week before its own milestone.

**The fix.** [`trace-the-impact`](./skills/in-progress/trace-the-impact/SKILL.md) finds the need date, shows the buffer arithmetic, separates work that can proceed (a stub, loaner kit, local accounts) from work that genuinely waits, and escalates only the collisions, with the evidence.

## Reference

**User-invoked** skills run only when you type their name. **Model-invoked** skills can also be picked up automatically when the task fits.

### In progress

Public on purpose and under test. Each is being compared blind against a plain assistant on fictional cases before it graduates. See [evals/](./evals/README.md).

**User-invoked**

- **[ask-justin](./skills/in-progress/ask-justin/SKILL.md)**: Ask which skill fits the moment you're in.

**Model-invoked**

- **[debrief-the-meeting](./skills/in-progress/debrief-the-meeting/SKILL.md)**: Turn a transcript into decisions, actions and owners, keeping suggestions, requests and acceptances apart.
- **[challenge-my-status](./skills/in-progress/challenge-my-status/SKILL.md)**: Find the few claims in a status draft a sponsor would challenge, with both sources and replacement wording.
- **[trace-the-impact](./skills/in-progress/trace-the-impact/SKILL.md)**: Trace an upstream slip to what's exposed, what can proceed and how much buffer is left.

## Contributing

The most useful thing you can send is a **case**: a fictional situation where a skill (or a plain assistant) got the call wrong, with what you'd have done instead. [Open a case](https://github.com/jsconu/pmo-skills/issues/new?template=case.yml). Have a skill you wish existed? [Suggest it](https://github.com/jsconu/pmo-skills/issues/new?template=idea.yml). Read [SCOPE.md](./SCOPE.md) first.

Please never paste real project material, names or client details into an issue.

## License

[MIT](./LICENSE). Maintained by Justin Scoville. Published by [Ondatrace](https://ondatrace.com).
