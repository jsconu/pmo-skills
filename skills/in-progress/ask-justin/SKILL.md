---
name: ask-justin
description: Ask which PMO skill fits the moment you're in. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask Justin

You won't remember every skill, so ask. Describe where you are in the week and what's in front of you.

Before saying what a skill does, read its SKILL.md. The summaries here are for orientation only.

Skills are organised by the **moment** you need help, not by PM knowledge area.

## You just came out of a meeting

- **debrief-the-meeting**: paste the transcript or your notes. You get decisions, actions and owners, with anything nobody actually accepted marked as open.

## You're about to send a status report

- **challenge-my-status**: paste last week's approved report, this week's draft and anything new (vendor emails, tracker exports). You get the few claims a sponsor would challenge, with wording to replace them.

## Something upstream slipped

- **trace-the-impact**: paste the change, what depends on it and the downstream dates. You get what can proceed, the buffer that's left, and what to escalate.

## Chaining them

A common week runs: **debrief-the-meeting** after the vendor call turns up a slip, **trace-the-impact** on that slip, then **challenge-my-status** on the report that has to mention it. Each skill works from what you paste, so carry the output of one into the next.

## Nothing fits

Say what you were trying to do. If no skill covers it, answer directly and suggest the user open a "skill request" issue at https://github.com/jsconu/pmo-skills/issues with a fictional example of the situation.
