---
name: check-the-decision
description: Take a past decision, its expected result and fresh evidence, and say whether the intervention worked, what is still unknown and when to check again. Use when the user asks whether a decision worked, to follow up on a steering decision, review a decision log, or check the outcome of a workaround, change or approval.
---

# Check the Decision

A decision being approved is not the same as it working. This skill closes the loop: what did we expect, what actually happened, and what do we do now.

## Inputs to ask for

- The decision as recorded: what was decided, by whom, when, and the expected outcome. A row from the [decision log](decision-log.md) is ideal.
- Fresh evidence from after the decision: test reports, delivery dates, metrics, messages.

## Rules

- **Compare against the expected outcome as written.** If none was recorded, say so, and propose one before judging.
- **Evidence, not approval.** The approval only shows what was authorised. Only later evidence shows what happened.
- **Don't claim cause.** If the outcome happened, say the evidence is consistent with the decision working. Other things may have changed too; name any you can see.
- **"Outcome unknown" is a valid answer** when the evidence doesn't cover it. Say what evidence would settle it and who has it.
- **Silence isn't success.** No complaints is not evidence that something worked.

## Output

```
**Decision:** <what, by whom, when>
**Expected:** <the outcome as recorded>
**Observed:** <what the evidence shows> ("<quote>", <source, date>)
**Verdict:** Worked / Partly / Didn't work / Outcome unknown
**Other factors:** <anything else that changed>
**Recommendation:** Close / Adjust (<how>) / Revisit (<what to bring back to the group>)
**Next check:** <date, and what evidence to bring>
```

Then give the updated decision log row, filling Observed outcome, Outcome source and Close / adjust / revisit.

## Learn from corrections (user-controlled)

If the user corrects a judgment, identifies an overlooked constraint, or states a lasting preference, reconsider the evidence and correct the answer. Apply reusable lessons in later turns when available; do not generalize one-off project facts. Ask permission before saving a non-sensitive preference in any persistent workspace memory or file. If persistence is unavailable, offer a brief note to copy; never claim installation itself provides memory. Never silently edit this skill, store confidential project content, share cases, or alter approved baselines. Do not solicit feedback after every successful answer. Offer fictionalized generalizable failure cases for maintainer review only with consent.
