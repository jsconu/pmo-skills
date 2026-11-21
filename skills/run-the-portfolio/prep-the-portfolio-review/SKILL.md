---
name: prep-the-portfolio-review
description: Turn project briefs and the actions from the last review into a decision-first steering agenda, with the evidence behind each ask, the items the PM can handle without the committee, and a decision log to fill in at the close. Use when the user is preparing a portfolio review, steering committee, governance board, QBR or programme board.
---

# Prep the Portfolio Review

A steering meeting that walks through every project in turn spends its time on updates and runs out before the decisions. Put the decisions first, back each one with evidence, and keep everything else out of the room.

Work from the briefs the user gives you. Material that's changed or missing since it was saved doesn't count as evidence. An empty section doesn't prove nothing is wrong; say "nothing raised" rather than "no risks".

## Method

1. **Last time's actions first.** For each action from the previous review: done, not done, or no evidence either way. Don't mark something done without evidence.
2. **Find the asks.** From the briefs, list the decisions only this group can make: approving a change to a committed date, budget or scope; resolving a conflict between projects; accepting a risk; stopping or starting work.
3. **Back each ask.** For each: the decision requested, the alternatives, the evidence (quoted, with source), and the expected effect of each option. If a decision depends on a disputed link between projects, check it first with trace-the-impact.
4. **Leave the decision and approver blank.** You're preparing the room, not deciding.
5. **Move the rest out.** Anything a PM can handle, or that's just an update, goes in a short "for information" list or to the PM directly.

## Output

```
# <Portfolio> review, <date>: agenda

## Actions from last time
| Action | Owner | Status | Evidence |

## Decisions needed (in priority order)
### 1. <decision>
- Asked by: <project / PM>
- Options: A) ... B) ... C) ...
- Evidence: "<quote>" (<source>)
- Expected effect: A) ... B) ...
- Decision: ________  Approved by: ________

## For information (no discussion)
- ...

## Handled outside the meeting
- <item> -> <PM>
```

Then attach the decision log in [decision-log.md](decision-log.md) and remind the user: at the close of the meeting, fill one row per decision from the chair's recap or approved minutes, and leave any unanswered request open rather than recording it as decided.
