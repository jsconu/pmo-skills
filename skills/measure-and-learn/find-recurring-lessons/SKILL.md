---
name: find-recurring-lessons
description: Compare decisions and their outcomes across comparable projects to find candidate lessons, the counterexamples, and the limits on applying them elsewhere. Use when the user pastes several retrospectives, decision logs or project histories and asks for patterns, recurring lessons, what usually works, or how a past approach would apply to a new project.
---

# Find Recurring Lessons

"Last time we did X and it worked" is how organisations learn and how they repeat mistakes. A lesson that holds across several projects is worth something. Check that it really holds, find where it didn't, and be clear about when it applies.

## Method

1. **Line up comparable decisions.** Same kind of decision (for example, "used a stub to start testing before the interface arrived"), across projects. List each with its context and recorded outcome.
2. **Count only recorded outcomes.** A decision with no recorded outcome doesn't count for or against.
3. **Find the counterexamples.** Where the same kind of decision didn't work, or worked in one setting and not another. These are the most useful part.
4. **Name the conditions.** What was true where it worked and not where it didn't: team size, vendor, timeline pressure, technology.
5. **Don't claim cause.** Several successes after the same decision show a pattern, not proof. Say how many cases support it.
6. **State the limits.** When should the next PM not apply this lesson?

## Output

```
**Candidate lesson:** <in one sentence>
- Supported by: <n> cases (<project: decision, outcome>)
- Counterexamples: <n> (<project: what was different>)
- Holds when: <conditions>
- Don't apply when: <conditions>
- Confidence: <strong pattern / weak pattern / not enough cases>

**Decisions with no recorded outcome:** <list, so they can be followed up>
```

## Learn from corrections (user-controlled)

If the user corrects a judgment, identifies an overlooked constraint, or states a lasting preference, reconsider the evidence and correct the answer. Apply reusable lessons in later turns when available; do not generalize one-off project facts. Ask permission before saving a non-sensitive preference in any persistent workspace memory or file. If persistence is unavailable, offer a brief note to copy; never claim installation itself provides memory. Never silently edit this skill, store confidential project content, share cases, or alter approved baselines. Do not solicit feedback after every successful answer. Offer fictionalized generalizable failure cases for maintainer review only with consent.
