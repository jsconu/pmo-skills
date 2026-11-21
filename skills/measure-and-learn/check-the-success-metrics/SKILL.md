---
name: check-the-success-metrics
description: Compare success metric definitions, targets and direction with the latest observations, showing movement against each target, missing measures and questions to ask. Use when the user pastes KPIs, OKRs, benefits, success criteria or metric readings and asks whether the project is delivering, how metrics are tracking, or for a benefits review.
---

# Check the Success Metrics

Success criteria get written at kickoff and checked at the end, if ever. Check them now: is each one moving the right way, and is it even being measured?

## Inputs to ask for

- Each metric: name, definition, target, and which direction is good (up or down). Some metrics have no target; that's fine, they're tracked, not judged.
- Observations: values with dates.
- The baseline, if there is one.

## Method

For each metric:

1. **Latest value and date.** If the latest reading is old, say how old.
2. **Movement**: change since baseline and since the last reading, with the subtraction.
3. **Against target**: met, on course, off course, or no target. "On course" needs a trend, not one good reading. Respect the direction: for a metric where lower is better, a fall is good.
4. **Gaps**: metrics with no readings, readings with no definition, a definition that changed partway.

Don't compute values the data doesn't give (for example, a percentage from vague text). Don't claim the project caused a movement; say the movement is consistent with it, or not.

## Output

```
| Metric | Target (direction) | Baseline | Latest (date) | Change | Status |
| --- | --- | --- | --- | --- | --- |
| <name> | <target> (lower is better) | <value> | <value> (<date>) | latest - baseline = <n> | Met / On course / Off course / No target / No data |

**Not being measured:** ...
**Questions to ask:** <for each off-course or missing metric, the one question for its owner>
```
