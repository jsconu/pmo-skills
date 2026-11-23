# Changelog

## 0.4.0 (2026-11-22)

- Skills can respond to user corrections and apply preferences when the assistant's memory or workspace supports it. They never silently save or upload project details.
- Added an evidence-gated weekly shared improvement process for maintainer-reviewed fixes.
- Added CI checks for skill metadata, complete ZIP builds and the combined Markdown download.
- Publish a new versioned release only after GitHub Actions validation passes.

## 0.3.0 (2026-11-21)

- Added `pmo-skills-all.md` to each release: every skill in one text file, for ChatGPT, Grok, Gemini, Copilot and other assistants that don't install Claude skills.
- README: setup steps for those assistants (attach the file to a project, GPT or Gem with the given instructions, or paste one skill into a chat).

## 0.2.0 (2026-11-21)

- Added `build-the-portfolio-report` to Run the portfolio: combine several project status reports into one portfolio report, with like-for-like project lines, decisions for leadership, cross-project dependencies and causes, and stale or inconsistent reports flagged.
- `ask-justin` now chains it: write-the-weekly-update per project, then build-the-portfolio-report across them.

## 0.1.0 (2026-11-20)

First public release: 24 skills in six folders, plus the `ask-justin` router.

- **Frame the work:** interview-the-sponsor, draft-the-charter, find-the-projects, prioritize-the-backlog
- **Run the week:** debrief-the-meeting, write-the-weekly-update, triage-the-risks, draft-the-stakeholder-update
- **Test the status:** challenge-my-status, reconcile-the-dates, trace-the-impact, review-a-change-request
- **Run the portfolio:** prep-the-portfolio-review (with a decision log template), find-capacity-conflicts, group-portfolio-risks, choose-todays-focus
- **Follow the decision:** check-the-decision (with the decision log), trace-a-decision, plan-the-handoff, plan-change-adoption
- **Measure and learn:** review-the-budget, check-the-success-metrics, run-the-retrospective, find-recurring-lessons

Three pasteable exercises with worked answers, and a comparison harness in `evals/`.
