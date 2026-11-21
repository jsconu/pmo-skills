---
name: find-capacity-conflicts
description: Add up each person's allocated hours across projects and find who is over capacity, in which weeks and by how much, with a trade-off for the director to decide. Use when the user pastes resource allocations, a staffing plan, a capacity sheet or timesheets across projects and asks who is overloaded, about resource conflicts or whether a plan is staffable.
---

# Find Capacity Conflicts

Someone can be badly over-committed across two projects while each project looks fine on its own. Add it up per person, per week.

## Inputs to ask for

- Allocations: person, project, hours per week (or percentage), start and end dates.
- Each person's available hours per week, if not the standard. Ask what the standard is; use 40 only if the user confirms it.
- Planned leave, if known.

## Method

1. **One row per person per period.** Sum their allocations for every week (or month, if that's the grain given) where allocations overlap. Two projects is enough to conflict.
2. **Compare with available hours.** Over-allocation = allocated - available. Show the sum.
3. **Report the window.** The first and last week the conflict applies, and the peak.
4. **Don't infer.** If a person's name appears in two forms, ask whether they're the same person. If dates or hours are missing for an allocation, list it separately and leave it out of the sums.
5. **Offer trade-offs,** labelled as options for the director: move dates, reduce hours on one project, bring in someone else, accept the overload for a short, named period.

## Output

```
| Person | Weeks | Allocated (sum) | Available | Over by | Projects |
| --- | --- | --- | --- | --- | --- |
| <name> | <from> to <to> | 30 + 20 = 50 | 40 | 10 h/week | A (30), B (20) |

**Trade-offs for the director:**
- <person>: <option A / option B, and what each costs>

**Couldn't include:** <allocations with missing dates or hours; possible duplicate names>
```
