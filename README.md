# PMO Skills for Real Project Managers

By **Justin Scoville, PMP, PgMP**. Published by [Ondatrace](https://ondatrace.com).

Agent skills for project managers, sponsors and PMO leaders: the checks I run on a meeting, a status report, a slipped date or a steering agenda before anything goes in front of a sponsor.

AI assistants are quick to write a status report and quick to raise a risk. They are much worse at the part of the job that matters: telling a forecast from a commitment, a suggestion from a decision, and a slip that still has ten days of buffer from one that collides. These skills are small, plain-language methods that hold an assistant to that standard. They work with whatever you paste in. No connectors, no code, no account.

Use them, adapt them, pass them to a colleague. If you hit a case they get wrong, [tell me](#contributing).

## Try one in five minutes (no install)

1. Open a chat with Claude (or whichever assistant your company approves).
2. Open an exercise below, copy the whole box, and paste it in.
3. Compare the answer with the worked answer underneath.

| Exercise | The question |
| --- | --- |
| [The vendor slipped](./examples/trace-the-impact.md) | There are still ten days of buffer. Would you escalate? |
| [Did anyone approve the new date?](./examples/challenge-my-status.md) | A vendor forecast crept into the status draft. |
| [Who actually owns that?](./examples/debrief-the-meeting.md) | A decision, a suggestion, and an action nobody accepted. |

All examples use fictional projects and people.

## Install

<details open>
<summary><strong>Claude (claude.ai, desktop or mobile)</strong></summary>

1. Pick a skill below and click **Download** to get its ZIP. Or take [all of them in one ZIP](https://github.com/jsconu/pmo-skills/releases/latest/download/pmo-skills-all.zip) and unzip it to upload the ones you want.
2. In Claude, open **Settings > Capabilities**, make sure code execution and file creation are on, then upload the ZIP under **Skills**.
3. Start a new chat and paste your material. Claude picks up the skill when it fits.

Skills work on Free and paid plans. On Team and Enterprise plans an admin may need to allow them. If upload isn't available in your workspace, paste the skill's `SKILL.md` text into the chat instead. [Claude's instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

</details>

<details>
<summary><strong>Claude Code</strong> (installs straight from this GitHub repo)</summary>

PMO Skills isn't in Anthropic's official plugin directory. Claude Code can install it directly from this repository instead. Run these two commands in your terminal:

```bash
# 1. Tell Claude Code where to find the plugin (this GitHub repo)
claude plugin marketplace add jsconu/pmo-skills

# 2. Install it
claude plugin install pmo-skills@jsconu
```

Claude Code calls any repo that offers plugins a "marketplace", which is why the first command uses that word. Nothing is bought, and no account is needed beyond Claude Code itself.

Start a new session afterwards and the skills are available. To update later, run `claude plugin marketplace update jsconu` and then `claude plugin update pmo-skills@jsconu`. To remove it, run `claude plugin uninstall pmo-skills@jsconu`.

</details>

<details>
<summary><strong>Any other agent, or editable files</strong></summary>

```bash
npx skills@latest add jsconu/pmo-skills
```

</details>

Not sure where to start? In Claude Code, run `/ask-justin`. Anywhere else, start with [the moment you're in](#reference).

## Why these skills exist

### #1: The recap says it was decided. It wasn't.

> "The great enemy of communication, we find, is the illusion of it."
>
> William H. Whyte, "Is Anybody Listening?", Fortune, 1950

**The problem.** An assistant summarising a meeting rounds everything up. "Maybe we should" becomes a decision. "Priya, can you chase the vendor?" becomes Priya's action, even though Priya had already dropped off the call.

**The fix.** [`debrief-the-meeting`](./skills/run-the-week/debrief-the-meeting/SKILL.md) separates what was said, what was decided and by whom, and what someone actually accepted. [`plan-the-handoff`](./skills/follow-the-decision/plan-the-handoff/SKILL.md) applies the same discipline to ownership: assigned is not acknowledged, and acknowledged is not done.

### #2: The status report quietly moved the date.

> "How does a project get to be a year late? ... One day at a time."
>
> Frederick P. Brooks Jr., The Mythical Man-Month

**The problem.** A vendor emails a new forecast. It ends up in this week's draft as the date, the colour stays green, and the approved baseline disappears. Nobody approved anything.

**The fix.** [`challenge-my-status`](./skills/test-the-status/challenge-my-status/SKILL.md) reads your draft against the last approved report and hands back the claims a sponsor would challenge, with wording you can paste. [`reconcile-the-dates`](./skills/test-the-status/reconcile-the-dates/SKILL.md) lines up the plan, the commitment and the forecast without picking a winner.

### #3: Every slip gets escalated, so none of them land.

**The problem.** Ask an assistant whether a slip is a risk and it will usually say yes. A PM who escalates a slip with ten days of buffer spends credibility they'll need for the real collision.

**The fix.** [`trace-the-impact`](./skills/test-the-status/trace-the-impact/SKILL.md) finds the need date, shows the buffer arithmetic, separates work that can proceed from work that genuinely waits, and escalates only the collisions. [`triage-the-risks`](./skills/run-the-week/triage-the-risks/SKILL.md) holds every risk to a specific trigger and a real response.

### #4: The decision was approved. Nobody checked whether it worked.

**The problem.** Steering approves a workaround and moves on. A month later nobody can say whether it helped, and half the plans still show the old date.

**The fix.** [`prep-the-portfolio-review`](./skills/run-the-portfolio/prep-the-portfolio-review/SKILL.md) puts decisions first and ships with a one-page decision log. [`check-the-decision`](./skills/follow-the-decision/check-the-decision/SKILL.md) compares the expected outcome with fresh evidence at the next review, and [`trace-a-decision`](./skills/follow-the-decision/trace-a-decision/SKILL.md) finds the plans and promises that never caught up.

## Reference

Organised by the moment you need help. Every skill can be picked up automatically when the task fits, except `ask-justin`, which you run by name.

<!-- skills:start -->

### Frame the work

Starting something new: the sponsor, the charter, the project list, the backlog.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[draft-the-charter](./skills/frame-the-work/draft-the-charter/SKILL.md)** | Turn kickoff notes, a sponsor interview or a request email into a project charter that labels every field as confirmed, inferred or unconfirmed and lists who can close each gap. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/draft-the-charter.zip) |
| **[find-the-projects](./skills/frame-the-work/find-the-projects/SKILL.md)** | Sort a messy batch of notes, emails, tickets or chat exports into the candidate projects and initiatives they describe, with aliases and the boundaries that need a PMO lead to confirm. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/find-the-projects.zip) |
| **[interview-the-sponsor](./skills/frame-the-work/interview-the-sponsor/SKILL.md)** | Interview a sponsor or requester about a new project, one question at a time, until the problem, authority, scope and success criteria are clear enough to charter. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/interview-the-sponsor.zip) |
| **[prioritize-the-backlog](./skills/frame-the-work/prioritize-the-backlog/SKILL.md)** | Put a backlog or list of candidate work into a reasoned order while keeping pinned items and fixed commitments exactly where they are, and show what moved and why. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/prioritize-the-backlog.zip) |

### Run the week

The weekly rhythm of one project: meetings, status, risks and messages.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[debrief-the-meeting](./skills/run-the-week/debrief-the-meeting/SKILL.md)** | Turn a meeting transcript or notes into a handoff that separates what was said, what was decided and what was accepted, with owners and dates left blank where nobody gave them. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/debrief-the-meeting.zip) |
| **[draft-the-stakeholder-update](./skills/run-the-week/draft-the-stakeholder-update/SKILL.md)** | Draft an escalation, customer update or stakeholder message from agreed facts, keeping every material risk, off-track status or open high-severity issue visible rather than softened. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/draft-the-stakeholder-update.zip) |
| **[triage-the-risks](./skills/run-the-week/triage-the-risks/SKILL.md)** | Read a task list, dependency export and current risk log and find the emerging exposures, each with its trigger, the work affected and a response worth considering (avoid, mitigate, transfer or accept). | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/triage-the-risks.zip) |
| **[write-the-weekly-update](./skills/run-the-week/write-the-weekly-update/SKILL.md)** | Write this week's project status update from last week's report and current evidence, covering what was finished, which milestones moved, which blockers persist and how long, and what decisions are needed. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/write-the-weekly-update.zip) |

### Test the status

Before anything goes to a sponsor: check the claims, the dates, the impact of a slip, and whether a change needs approval.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[challenge-my-status](./skills/test-the-status/challenge-my-status/SKILL.md)** | Check a draft status report against the last approved report and the supporting evidence, and pick out the few claims a PM should challenge before sending, with both sources and replacement wording. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/challenge-my-status.zip) |
| **[reconcile-the-dates](./skills/test-the-status/reconcile-the-dates/SKILL.md)** | Line up the dates in a schedule, a customer commitment and a delivery forecast, work out which refer to the same milestone, show the gap, and say what still needs approval. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/reconcile-the-dates.zip) |
| **[review-a-change-request](./skills/test-the-status/review-a-change-request/SKILL.md)** | Review a proposed scope, backlog or schedule change against the baseline, identify which committed deliverables and milestones it touches, and route the decision to the right approver. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/review-a-change-request.zip) |
| **[trace-the-impact](./skills/test-the-status/trace-the-impact/SKILL.md)** | Trace an upstream slip or change through its dependencies to find which downstream work is exposed, which can still proceed, and how much buffer is left. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/trace-the-impact.zip) |

### Run the portfolio

Across projects: steering, capacity, shared risks and where to spend today.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[build-the-portfolio-report](./skills/run-the-portfolio/build-the-portfolio-report/SKILL.md)** | Combine several project status reports into one portfolio report for leadership, with a like-for-like view of every project, the decisions leadership needs to make, the risks and dependencies that cross projects, and the reports that are stale or don't hold up. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/build-the-portfolio-report.zip) |
| **[choose-todays-focus](./skills/run-the-portfolio/choose-todays-focus/SKILL.md)** | From current project briefs and pending decisions, pick the single most useful next action per project and order them for a leader's attention today. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/choose-todays-focus.zip) |
| **[find-capacity-conflicts](./skills/run-the-portfolio/find-capacity-conflicts/SKILL.md)** | Add up each person's allocated hours across projects and find who is over capacity, in which weeks and by how much, with a trade-off for the director to decide. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/find-capacity-conflicts.zip) |
| **[group-portfolio-risks](./skills/run-the-portfolio/group-portfolio-risks/SKILL.md)** | Read risk registers from several projects and group similar exposures, with supporting examples, separating a genuinely shared cause from risks that only sound alike. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/group-portfolio-risks.zip) |
| **[prep-the-portfolio-review](./skills/run-the-portfolio/prep-the-portfolio-review/SKILL.md)** | Turn project briefs and the actions from the last review into a decision-first steering agenda, with the evidence behind each ask, the items the PM can handle without the committee, and a decision log to fill in at the close. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/prep-the-portfolio-review.zip) |

### Follow the decision

After the decision: did it work, did it land, who owns what, and are people ready.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[check-the-decision](./skills/follow-the-decision/check-the-decision/SKILL.md)** | Take a past decision, its expected result and fresh evidence, and say whether the intervention worked, what is still unknown and when to check again. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/check-the-decision.zip) |
| **[plan-change-adoption](./skills/follow-the-decision/plan-change-adoption/SKILL.md)** | For a delivery change (a new system, process, date or scope change) and the groups it affects, propose the communications, training and adoption checks needed, labelled as recommendations. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/plan-change-adoption.zip) |
| **[plan-the-handoff](./skills/follow-the-decision/plan-the-handoff/SKILL.md)** | Turn open reviews, follow-ups, owners and dates into a handoff that separates work that is assigned, work that is acknowledged by its owner and work that is actually done. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/plan-the-handoff.zip) |
| **[trace-a-decision](./skills/follow-the-decision/trace-a-decision/SKILL.md)** | Take an approved change and the team artifacts that should reflect it (plans, tickets, schedules, customer commitments, messages) and show where the decision appears, where the evidence still shows the old position, and who should verify adoption. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/trace-a-decision.zip) |

### Measure and learn

Money, metrics and lessons.

| Skill | What it does | Claude upload |
| --- | --- | --- |
| **[check-the-success-metrics](./skills/measure-and-learn/check-the-success-metrics/SKILL.md)** | Compare success metric definitions, targets and direction with the latest observations, showing movement against each target, missing measures and questions to ask. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/check-the-success-metrics.zip) |
| **[find-recurring-lessons](./skills/measure-and-learn/find-recurring-lessons/SKILL.md)** | Compare decisions and their outcomes across comparable projects to find candidate lessons, the counterexamples, and the limits on applying them elsewhere. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/find-recurring-lessons.zip) |
| **[review-the-budget](./skills/measure-and-learn/review-the-budget/SKILL.md)** | From a budget, logged hours, rate assumptions and expenses, calculate actual spend, variance against budget and any unexplained gaps, with every figure traceable. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/review-the-budget.zip) |
| **[run-the-retrospective](./skills/measure-and-learn/run-the-retrospective/SKILL.md)** | From a project's charter, decision history, delivery evidence and closeout notes, write a retrospective covering what happened, which interventions helped and what to repeat, with lessons specific enough for the next PM to use. | [Download](https://github.com/jsconu/pmo-skills/releases/latest/download/run-the-retrospective.zip) |

<!-- skills:end -->

## Contributing

The most useful thing you can send is a **case**: a fictional situation where a skill got the call wrong, with what you'd have done instead. [Open a case](https://github.com/jsconu/pmo-skills/issues/new?template=case.yml). Want a skill that isn't here? [Suggest it](https://github.com/jsconu/pmo-skills/issues/new?template=idea.yml). Read [SCOPE.md](./SCOPE.md) first.

Please never paste real project material, names or client details into an issue.

## License

[MIT](./LICENSE). Maintained by Justin Scoville. Published by [Ondatrace](https://ondatrace.com).
