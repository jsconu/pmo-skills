# Personal learning from feedback

Each installed PMO skill may improve its **behavior for the current user** without editing the public skill or uploading their data. This is a feedback-and-preferences overlay, not autonomous model training.

## When a skill is used

1. Complete the PM task using the skill's existing rules. Never delay the answer to collect feedback.
2. If the user corrects a factual judgment, disputes an escalation, supplies an overlooked constraint, or explicitly requests a different format, acknowledge the correction and reconsider the actual evidence. Do not blindly accept a mistaken correction.
3. Distinguish **case facts** (only for this task) from **reusable preferences** (e.g. concise sponsor-ready output, escalation threshold) and **candidate method defects** (e.g. treating a vendor forecast as approval).
4. Apply confirmed preferences and corrected reasoning on subsequent turns **when the assistant has access to them**. Explicit user instructions and evidence take precedence. A preference never licenses fabricated decisions, owners, dates, or hidden risks.
5. If the host supports durable workspace instructions or user-owned files, ask before saving a distilled, non-sensitive preference or regression lesson. Store a short rule and the scope, not a transcript, client data, contact names or project details. If storage is unavailable, offer a brief copyable learning note instead; do not claim persistence across chats.
6. Never silently edit an installed SKILL.md, user's project data, GitHub repo, or published bundle. In writable local development environments, offer a proposed diff or a project-local preference file **after consent**. Do not modify skill source without explicit approval and testing.
7. For repeated, generalizable skill defects, ask whether the user wants to contribute a **fictionalized** failure case to the public repository; never send project inputs to GitHub automatically.
8. Do not append a feedback prompt to every successful output. Only ask a brief question when a correction, uncertainty or unusual case makes it useful.

## Optional durable note format

If the user agrees to saving and the host actually offers a durable mechanism, use this short pattern:

```markdown
# My PMO Skills preferences
- Skill: <skill or all>
- Preference / corrected rule: <one sentence; no project-specific facts>
- Scope: <which situations it applies to>
- Verified by: user confirmation, <date if available>
- Do not override: evidence, approved baselines, explicit user instructions, skill safety rules
```

For Claude Projects, use project instructions/knowledge that the user controls; for other workspaces, use equivalent user-owned instructions. Claude skill ZIP uploads alone do not guarantee memory or writes between sessions. Claude Code or a coding agent may have files, but must ask before writing. No SaaS account, telemetry or API key is required.

## Example

User: "You're escalating a two-day slip, but the downstream milestone has ten days of buffer."

Good response: Recompute the buffer and correct the present answer. If evidence confirms no collision, explain why escalation is unwarranted. A reusable preference might be "For date slips, calculate need date and buffer before suggesting escalation." Request permission before retaining it for future chats. Do not add that user's real schedule to a shared test suite.

## Relation to repository improvement

Personal preference and correction notes belong to the user's environment and are never collected centrally. The [maintainer improvement process](CONTINUOUS_IMPROVEMENT.md) uses only voluntarily submitted, fictional examples and reviewed PRs. Personal learning is not a claim that the model weights update or that every installation automatically synchronizes.
