# Requirements format

The canonical story shape is Jira [SALES-9926](https://trr-prod.atlassian.net/browse/SALES-9926). It is an idealized example: small stories can drop sections that truly do not apply, but never the Problem Statement, Scope, or Acceptance Criteria.

For bugs, spikes, data backfills, DevQA, and capacity buckets, use the matching template in Notion [How to Write a SALES Ticket](https://app.notion.com/p/3bbd553c3a2e8173a5cbced7aa4d9da1).

## Story template

Title: **verb + object + constraint**. It must make sense on a sprint board with the description closed.

Description:

```markdown
[One sentence: the change and who it is for.]

## Background
[How it works today. Systems, users, and process involved.]

## Problem Statement
[What goes wrong today, for whom, and evidence (counts, examples, Zendesk links with a one-line summary).]

## Business Rules
1. [Rule the system must enforce, stated as a fact.]

## Scope
* [What changes.]
* [What explicitly stays the same (out of scope).]

## Dependencies
* **TBD — decision needed from [role]:** [decision]
* [Test data, environments, or other teams needed.]

## Definition of Done
* **Available** [where and when, e.g. sandbox, then production after AC pass]
* **Tested** by [named role] running the acceptance criteria and marking each pass or fail
* **Offered** to [which users only]
* **Written** [where users and support will find the documentation]
```

Acceptance Criteria field (put AC in the Jira field, not the description):

```markdown
**Happy path.** Given [state]. When [action]. Then [observable result].

**Edge case.** Given [unusual but valid state]. When [action]. Then [result].

**Negative test.** Given [state where the change must not apply]. When [action]. Then [unchanged behavior].

**Rollback.** Given [the change is live and in use]. When [it is turned off]. Then [what happens to new and existing records].
```

## Review checklist

Mark each item pass or fail. Any **must** failure means the verdict is `Needs changes`. Undefined design or approach means `Needs a spike first`.

**Must**
- [ ] Title is verb + object + constraint, not a placeholder.
- [ ] Problem Statement says who is affected and what goes wrong today, with evidence.
- [ ] Scope lists what changes and what stays the same.
- [ ] One task only. Otherwise propose a split.
- [ ] Salesforce objects, fields, reports, and records are named exactly, or marked `TBD`.
- [ ] Every TBD has an owner role.
- [ ] Acceptance criteria are in Given/When/Then and each is binary pass/fail.
- [ ] AC cover happy path, at least one edge case, and a negative test.
- [ ] No learning-outcome language in AC ("understand", "explore", "investigate whether", "works", "complete").
- [ ] No abstract groupings without a system field behind them (drafting rule 7).

**Should**
- [ ] Business Rules are separate from Scope and stated as facts.
- [ ] Rollback AC exists for anything touching live data, automation, routing, or integrations.
- [ ] Definition of Done names who tests and where it ships first.
- [ ] Cross-cutting impacts addressed: reports and dashboards, compensation and past periods.
- [ ] Type-specific questions from [question-bank.md](question-bank.md) are answered or listed as TBD.
- [ ] Links are specific and summarized, not a URL dump.
- [ ] Describes the outcome, not a solution design. Engineering owns the design doc.

## Sprint-ready bar

Someone who was not in the Slack thread can pick it up and know:
1. What to change
2. How to know it is done
3. What not to touch
