---
name: group-portfolio-risks
description: Read risk registers from several projects and group similar exposures, with supporting examples, separating a genuinely shared cause from risks that only sound alike. Use when the user pastes multiple project risk logs or RAID logs and asks for portfolio risks, common themes, top risks across projects or a risk heat map.
---

# Group Portfolio Risks

A portfolio risk report that lists every project's risks is just a longer list. The useful part is spotting the exposures that repeat, and being honest about which share a cause and which just share a word.

## Method

1. **Flatten and sort.** List every open risk with its project, description, severity and owner. Start from the highest severity.
2. **Group by similarity of the risk itself,** not of the label. "Vendor delay" on two projects is a group only if the descriptions point at the same kind of exposure.
3. **For each group, decide the kind:**
   - **Shared cause**: the same vendor, team, system, budget pool or decision sits behind each. This is a portfolio risk; one action can address all of them.
   - **Similar description, separate causes**: the same type of problem arising independently. Useful as a pattern, but each project still needs its own response.
   Say which, and quote the evidence that makes it shared.
4. **Name the theme in plain words** ("one integration vendor is late on three projects"), not a category ("third-party risk").
5. **Keep singletons.** A high-severity risk that doesn't group with anything still belongs in the top risks.

## Output

```
**Top portfolio risks**

1. <theme> (<shared cause / similar, separate causes>), highest severity <High>
   - <Project A>: "<risk description>" (<severity>, owner <name>)
   - <Project B>: "<risk description>" (<severity>, owner <name>)
   - Why grouped: <the shared vendor/team/system, quoted>, or <only the type of problem is shared>
   - Portfolio action to consider: <one action that addresses the group, if the cause is shared>

**High-severity risks that stand alone**
- ...
```
