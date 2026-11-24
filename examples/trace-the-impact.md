# The vendor slipped. There are still ten days of buffer. Would you escalate?

A five-minute exercise for [`trace-the-impact`](../plugins/ondatrace-pmo-skills/skills/test-the-status/trace-the-impact/SKILL.md). No install needed. Everything here is fictional.

## Copy everything in this box into a new chat

```text
Act as an experienced project manager reviewing a slipped dependency. Work only from the material below.

Method:
1. State what moved, from which date to which date, and whether the new date is a forecast, a commitment or an approved change.
2. For each piece of downstream work, say whether it really depends on the slipped item, quoting the evidence. Work that uses a stub, an existing system or a workaround can proceed.
3. Find each dependent item's need date: the last day it can receive the input without moving its own commitment. This is often earlier than its milestone.
4. Show the arithmetic: buffer = need date minus the new delivery date, in calendar days.
5. Call each item: Proceeds, Watch (name the trigger that would change your call), or Collision (escalate with the dates, the quote and the knock-on effect).
6. Don't escalate a slip that still has buffer. Don't invent dependencies or dates.

Answer with a one-line bottom line, a table (work, depends on it?, need date, buffer, call), then what to escalate, what to watch and what to verify.

--- MATERIAL ---

Today is Monday 8 February 2027. Project: Harbor warehouse system.

Email from Kestrel Integrations, Friday 5 February:
"The order-routing interface we promised for Tuesday 9 February is now forecast for Friday 19 February. We'll confirm by Friday 12 February."

Test plan v3, section 4:
"Smoke tests start Tuesday 9 February using the order-routing stub. They do not need the live interface."
"The full regression suite needs the live order-routing interface in the test environment by Monday 1 March. Installing it takes half a day. Regression runs 1 to 5 March, ahead of go/no-go on Monday 8 March."

Label printing work plan:
"Integration test with the live order-routing interface on Tuesday 16 February. The label vendor's engineer is on site that day only."
```

## Worked answer

**Bottom line:** Smoke tests start Tuesday as planned and full regression still has 10 days of buffer, so neither needs escalating. The label printing integration test on 16 February collides with the new forecast and does need raising now.

| Work | Depends on it? | Need date | Buffer | Call |
| --- | --- | --- | --- | --- |
| Smoke tests | No. "using the order-routing stub. They do not need the live interface." | n/a | n/a | **Proceeds** Tuesday 9 Feb |
| Full regression | Yes. "needs the live order-routing interface ... by Monday 1 March" | Mon 1 Mar | 1 Mar - 19 Feb = **10 days** | **Watch** |
| Label printing integration test | Yes. "Integration test with the live order-routing interface" | Tue 16 Feb | 16 Feb - 19 Feb = **-3 days** | **Collision** |

**Escalate:** the label printing test. It needs the live interface on 16 Feb, and Kestrel now forecasts 19 Feb, three days later. The label vendor's engineer is on site that day only, so this can't just slide. Options to put to the label vendor and Kestrel: rebook the engineer after 19 Feb, ask Kestrel for an early partial drop before 16 Feb, or run the label test against the stub and repeat it live later.

**Watch:** full regression. The trigger is Kestrel's confirmation on Friday 12 Feb. If the forecast moves past Monday 1 March (or past about 26 Feb, if you want a margin for a failed install), escalate then.

**Verify:** 19 Feb is a forecast, not a commitment. Ask Kestrel on 12 Feb whether it's confirmed.

### Why this is the right call

A plain assistant will usually call the whole slip a risk. That's the shortcut to avoid: two of the three pieces of work are fine, and escalating them would bury the one real collision. The other trap is to look only at go/no-go on 8 March, see plenty of time, and miss that the label test needs the interface three weeks earlier.

**Your turn:** what would make you escalate full regression before the 12 February confirmation?
