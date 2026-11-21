## What it does

`trace-the-impact` takes one upstream change (a vendor slip, a late environment, a moved milestone) and works out what it really touches. For each piece of downstream work it asks three things: does this genuinely depend on the change, what is its **need date**, and how much **buffer** is left. Then it makes one of three calls: proceeds, watch, or collision.

It shows the date arithmetic, so you can check it in ten seconds.

## When to reach for it

Paste the change and whatever tells you what depends on it: a test plan, a cutover plan, a dependency list, an email. It works best when you include the downstream dates, even rough ones.

Reach for it before you write the status line or raise the risk. It is most useful when your instinct says "this is bad" or "this is fine" and you haven't checked either.

## It's working if

- Some work comes back as **proceeds**, because it uses a stub, existing kit or a workaround.
- Every buffer shows its subtraction, and the need date is earlier than the milestone where the plan says so.
- A slip with plenty of buffer comes back as **watch**, with a named trigger, not as a risk.
- When the evidence conflicts, it says so and asks the question, instead of picking a side.

## Common questions

**It didn't escalate a slip I was worried about. Is it wrong?**
Check the need date and the subtraction. If both are right and the buffer is positive, it's telling you that you have time. The trigger it names is the point where that changes.

**Calendar days or working days?**
Calendar days unless your material uses working days. It says which it used.

**Can it follow a chain of dependencies?**
One hop at a time. Each downstream item that feeds another gets its own line with its own evidence.
