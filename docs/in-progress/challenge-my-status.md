## What it does

`challenge-my-status` reads your draft status report the way a skeptical sponsor would. It lines up the draft against the last **approved** report and the evidence you have (vendor emails, tracker exports, change logs), matches each claim to the same milestone, and returns only the few claims that wouldn't survive a question. For each one you get both sources and wording you can paste.

The approved baseline stays the reference. A vendor forecast never quietly replaces it.

## When to reach for it

Right before you send the report. Paste three things: last week's approved report, this week's draft, and anything new since then. The more the draft has changed, the more useful it is.

## It's working if

- It flags a **few** claims, sometimes none, not a page of edits.
- A date that moved without approval comes back with the approved date kept and the forecast beside it.
- "Confirmed", "complete" and "on track" get checked against what the evidence actually says.
- It doesn't confuse two milestones that happen to share a date.

## Common questions

**It told me to send as is. Did it check anything?**
It lists the claims it checked and found fine, so you can see.

**I don't have last week's approved report.**
It will still check the draft against the evidence, but it can't tell you whether a date moved. It says so.

**Does it rewrite the whole report?**
No. It gives replacement wording for the claims it challenges and leaves the rest alone.
