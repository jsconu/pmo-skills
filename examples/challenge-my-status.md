# Did anyone approve the new date?

A five-minute exercise for [`challenge-my-status`](../skills/test-the-status/challenge-my-status/SKILL.md). No install needed. Everything here is fictional.

## Copy everything in this box into a new chat

```text
Act as a skeptical sponsor reading my status draft before I send it. Work only from the material below.

Method:
1. Treat last week's approved report as the baseline. It stays the reference until someone with authority approves a change.
2. Match each claim in the draft to the same milestone in the baseline and the evidence. Match by milestone name, not because two dates look alike.
3. Classify each claim: supported, approved change, silent re-baseline (changed with no approval shown), overstated (for example a forecast reported as confirmed), contradicted, or unsupported.
4. A vendor forecast is not an approved date. Never delete the approved date: show the forecast beside it and say what approval is needed.
5. Status colour must follow the variance against the approved date.
6. Pick only the claims a sponsor would challenge. If everything holds up, say so.

For each claim to challenge: quote the draft, quote the baseline and the evidence, say why it matters in one sentence, and give replacement wording I can paste. Then list the claims you checked that are fine.

--- MATERIAL ---

APPROVED REPORT, 1 February 2027 (approved at steering)
- Data migration complete: Friday 26 February
- Training materials ready: Friday 12 March
- Go-live: Monday 22 March
- Overall status: Green

EMAIL from Northwind Data Services, Friday 5 February 2027
"Following the extra cleansing work, we now forecast the final migration load completing on Friday 12 March."

DRAFT REPORT, 8 February 2027 (not yet sent)
- Data migration complete: Friday 12 March (on track)
- Training materials ready: Friday 12 March
- Go-live: Monday 22 March
- Overall status: Green

CHANGE LOG
No change requests raised since 1 February. Next steering: Monday 15 February.
```

## Worked answer

**Verdict:** fix two claims before sending. The draft has quietly replaced the approved migration date with the vendor's forecast and kept the status green.

**1. "Data migration complete: Friday 12 March (on track)"** (silent re-baseline)
- Baseline says: "Data migration complete: Friday 26 February" (approved report, 1 Feb)
- Evidence says: "we now forecast the final migration load completing on Friday 12 March" (Northwind, 5 Feb)
- Why it matters: nobody approved the new date, and "on track" hides a 14-day slip (26 Feb to 12 Mar).
- Replace with: "Data migration remains baselined for 26 February. Northwind now forecasts 12 March, 14 days late. We have not approved a new date; I'll bring options to steering on 15 February."

**2. "Overall status: Green"** (overstated)
- Baseline says: Green, with 24 days between migration and go-live (26 Feb to 22 Mar).
- Evidence says: on the forecast, that gap is 10 days (12 Mar to 22 Mar).
- Why it matters: a key milestone is forecast to miss its approved date and the go-live margin has more than halved.
- Replace with: "Overall status: Amber. Migration is forecast 14 days late; go-live on 22 March holds for now with 10 days of margin instead of 24."

**Checked and fine:** training materials ready, 12 March (same as baseline; the matching date in the vendor email is about migration, not training). Go-live, 22 March (unchanged and still achievable on the forecast).

### Why this is the right call

The trap here is the matching date. "12 March" appears in the baseline (training), the email (migration) and twice in the draft, so the draft looks consistent at a glance. Matching by milestone rather than by date is what exposes the change.

**Your turn:** would you keep go-live at 22 March in the report, or flag it as at risk too? What evidence would decide it?
