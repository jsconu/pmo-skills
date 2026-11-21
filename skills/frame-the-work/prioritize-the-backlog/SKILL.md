---
name: prioritize-the-backlog
description: Put a backlog or list of candidate work into a reasoned order while keeping pinned items and fixed commitments exactly where they are, and show what moved and why. Use when the user asks to prioritise, rank, sequence, groom or re-order a backlog, feature list or set of requests.
---

# Prioritize the Backlog

A ranking is only useful if people trust it. Two things destroy that trust: silently moving something a stakeholder was promised, and an order nobody can explain. This skill avoids both.

## Inputs to ask for

- The items, with whatever is known about each: value, urgency, effort, risk, dependencies, who asked for it.
- Which items are **pinned**: committed to a customer, tied to a dated milestone, or fixed by a decision. Ask if it isn't stated.
- The current order, if there is one.
- What matters most right now, if the user can say (for example, "unblock the launch" or "reduce support load").

## Rules

- **Pinned items keep their exact position.** Never move one, even if it scores badly. If you think a pinned item is in the wrong place, say so separately as a question for whoever pinned it.
- **Rank the rest around them**, in the remaining slots.
- **Use the information given.** If an item has no effort or value estimate, say so and place it on what is known. Don't invent estimates.
- **Dependencies win ties.** An item that unblocks others goes ahead of an equally valued item that doesn't.
- **Flag stale items.** Something that has sat near the bottom through several rounds is a candidate to drop, not to keep carrying.
- **Say what changed.** Compare with the current order and call out anything that moved more than a couple of places.

## Output

```
| Rank | Item | Pinned? | Why here | Moved |
| --- | --- | --- | --- | --- |
| 1 | ... | Pinned (customer commitment, <date>) | Fixed | - |
| 2 | ... | | <one clause: value, urgency, unblocks X> | up 3 |

**Biggest moves:** <item: from N to M, because ...>
**Missing information:** <items ranked on partial information, and what would firm them up>
**Questions for owners:** <pinned items that may be in the wrong place; stale items to consider dropping>
```
