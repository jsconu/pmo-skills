---
name: review-the-budget
description: From a budget, logged hours, rate assumptions and expenses, calculate actual spend, variance against budget and any unexplained gaps, with every figure traceable. Use when the user pastes a budget, timesheets, a cost report or expenses and asks about burn, spend to date, variance, forecast to complete or whether a project is over budget.
---

# Review the Budget

Budget conversations go wrong when nobody can see where a number came from. Show every calculation, keep currencies and assumptions visible, and flag what doesn't add up rather than smoothing it over.

## Inputs to ask for

- The approved budget: the figure, the currency, and what it covers.
- Hours logged, by person or role, for the period.
- The rate or rates to apply. If the user gives one blended rate, use it and say so. Don't invent per-person rates.
- Non-labour expenses.
- The period, and how much of the project's time has passed.

## Rules

- **Spend = hours x rate + expenses.** Show each line.
- **Keep the currency.** "$500k" and "USD 500,000" are the same; a bare "500,000" with no currency isn't assumed to be either. Never add figures in different currencies without a stated rate.
- **A budget range stays a range.** If the budget is "about 100 to 150k", compare against both ends, or ask which is approved.
- **Variance = budget - spend to date.** Also show percent of budget spent beside percent of time elapsed, since spending 60% of the budget at 40% of the schedule is the early warning.
- **Flag gaps:** hours with no rate, expenses with no category, people logging time who aren't on the plan, months with no entries at all.
- **Forecast only with a stated basis.** If you project to completion, say the assumption ("at the last four weeks' burn rate").

## Output

```
**<Project> budget, as of <date>** (<currency>)

| Line | Calculation | Amount |
| --- | --- | --- |
| Labour | <hours> h x <rate> = | ... |
| Expenses | <items> | ... |
| **Spend to date** | | ... |
| Approved budget | | ... |
| **Remaining** | budget - spend = | ... |

**Burn vs time:** <x>% of budget spent, <y>% of schedule elapsed.
**Forecast at completion:** <figure>, assuming <basis> (or "not enough information").
**Unexplained or missing:** ...
```

## Learn from corrections (user-controlled)

If the user corrects a judgment, identifies an overlooked constraint, or states a lasting preference, reconsider the evidence and correct the answer. Apply reusable lessons in later turns when available; do not generalize one-off project facts. Ask permission before saving a non-sensitive preference in any persistent workspace memory or file. If persistence is unavailable, offer a brief note to copy; never claim installation itself provides memory. Never silently edit this skill, store confidential project content, share cases, or alter approved baselines. Do not solicit feedback after every successful answer. Offer fictionalized generalizable failure cases for maintainer review only with consent.
