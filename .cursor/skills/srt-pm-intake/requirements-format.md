# Requirements format

The canonical story shape is Jira [SALES-9926](https://trr-prod.atlassian.net/browse/SALES-9926). It is an idealized example: small stories can drop sections that truly do not apply, but never the Problem Statement, Scope, or Acceptance Criteria.

For bugs, spikes, data backfills, DevQA, and capacity buckets, use the matching template in Notion [How to Write a SALES Ticket](https://app.notion.com/p/3bbd553c3a2e8173a5cbced7aa4d9da1).

## Story template

Title: **verb + object + constraint**. It must make sense on a sprint board with the description closed.

Every section describes the problem, the users, the rules, and the outcome. None of them describe how to build it; that belongs in engineering's design doc. See [solution-check.md](solution-check.md).

Description:

```markdown
[One sentence: the outcome and who it is for.]

## Background
[How it works today. Systems, users, and process involved.]

## Problem Statement
[What goes wrong today, for whom, and evidence (counts, examples, Zendesk links with a one-line summary).]

## Business Rules
1. [Rule the system must enforce, stated as a fact.]

## Scope
* [What changes for users or the business.]
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

Acceptance Criteria field (put AC in the Jira field, not the description). Each AC describes what a user, manager, customer, or report can observe:

```markdown
**Happy path.** Given [state]. When [action]. Then [observable result].

**Edge case.** Given [unusual but valid state]. When [action]. Then [result].

**Negative test.** Given [state where the change must not apply]. When [action]. Then [unchanged behavior].

**Rollback.** Given [the change is live and in use]. When [it is turned off]. Then [what happens to new and existing records].
```

## Review checklist

Mark each item pass or fail. Any **must** failure means the verdict is `Needs changes`. Undefined design or approach means `Needs a spike first`.

**Must**
- [ ] No proposed solutions in the description or AC (see [solution-check.md](solution-check.md)). Engineering owns the design.
- [ ] Title is verb + object + constraint, describes an outcome, and is not a placeholder.
- [ ] Problem Statement says who is affected and what goes wrong today, with evidence.
- [ ] Scope lists what changes for users and what stays the same.
- [ ] One task only. Otherwise propose a split.
- [ ] Existing records, reports, and dashboards referenced as context are named exactly or linked.
- [ ] Every TBD has an owner role.
- [ ] Acceptance criteria are in Given/When/Then, each is binary pass/fail, and each describes something a user or the business can observe.
- [ ] AC cover happy path, at least one edge case, and a negative test.
- [ ] No learning-outcome language in AC ("understand", "explore", "investigate whether", "works", "complete").
- [ ] Groups of users are defined in business terms someone can check (title, department, team), not "anyone like Adam's team" (drafting rule 7). Engineering maps them to the system.

**Should**
- [ ] Business Rules are separate from Scope and stated as facts.
- [ ] Rollback AC exists for anything touching live data, automation, routing, or integrations.
- [ ] Definition of Done names who tests and where it ships first.
- [ ] Cross-cutting impacts addressed: reports and dashboards, compensation and past periods.
- [ ] Links are specific and summarized, not a URL dump.

Do not fail a ticket for missing build detail (data types, field visibility, labels). Engineering asks for that during grooming.

## Sprint-ready bar

Someone who was not in the Slack thread can pick it up and know:
1. What to change
2. How to know it is done
3. What not to touch
