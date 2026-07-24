# Sales 7/9 - 7/22

**Sprint:** Sales 7/9 - 7/22  
**Sprint Dates:** July 9, 2026 - July 22, 2026  
**Report Date:** July 24, 2026  
**Team:** Salesforce Release Technology (SRT)  
**Data Sources:** SALES Jira board (board ID 10), Weekly Status Raw Data (2026-07-16, 2026-07-23), #srt-team / #seller-salestech Slack, SRT Action Items Tracker (Notion)

---

## Part A: Metrics Report

### Executive Summary

Sprint **Sales 7/9 - 7/22** closed with full ticket closure (zero carry-over in Jira as of 2026-07-24) but the shape was late-heavy and scope-heavy. The team shipped ALRA routing foundations (SALES-9136, SALES-9471), High Value Matrix permissions and capture work (SALES-9351, SALES-9385, SALES-9435, SALES-9478), Salesforce security compliance (SALES-9034, SALES-9340), and a production push-topic fix (SALES-9475). The biggest concern is sustained mid-sprint injection: 38 tickets and 51 points added after sprint start, plus a large buffer/DevQA load that masked true product vs. KTLO allocation. All 17 closed bugs still have empty Reason for Bug fields.

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 7/9 - 7/22 |
| Sprint Dates | July 9, 2026 - July 22, 2026 |
| Committed Points | 127 (manual sum at sprint close; mid-sprint snapshot on 2026-07-13 showed 115) [OPEN QUESTION: confirm committed in Jira sprint report velocity view] |
| Completed Points | 123 (manual sum, Done tickets excluding Won't Do, Sales 7/9 - 7/22) [OPEN QUESTION: sprint report may show 127 if Won't Do counts toward completed; reconcile before meeting] |
| Carry-Over (tickets / points) | 0 / 0 (current Jira state; SALES-9475 and SALES-9478 resolved 2026-07-23, hours after sprint end) |
| Removed (tickets / points) | 6 / 4 (Won't Do) |
| Added Mid-Sprint (tickets / points) | 38 / 51 (created after 2026-07-09 17:19 UTC sprint start) |
| Scope Change % | +67% net points added vs. ~76 pts at sprint start (51 added / 76 original) |
| Spikes Closed | 10 |
| Bugs Closed | 17 (Done status; excludes 4 Won't Do bugs) |

**Sprint goal (Jira):** ALRA Routing; SUMO Bugs; Salesforce Security tickets; Voice Recognition Design

**Status breakdown:** Done: 86, Won't Do: 6  
**Type breakdown:** Story: 29, Task: 36, Bug: 17, Spike: 10  
**Total tickets in sprint:** 92 (story-level; no sub-task points counted)

### Capacity Allocation (completed Done points, Sales 7/9 - 7/22)

SRT labels remain sparse (only 4 tickets carried `SRT-Product`). Buckets below use label plus summary keyword inference per SRT Tech Health taxonomy guidance.

| Bucket | Target % | Target Points (~70 cap) | Actual Points | Actual % | Delta |
|--------|----------|---------------------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 45 | 36.6% | +11 pts vs target count, -11.4 pts vs target % |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 7 | 5.7% | -4 pts |
| KTLO (SRT-KTLO) | 16% | ~11 | 8 | 6.5% | -3 pts |
| Buffer / Unplanned | 20% | ~14 | 63 | 51.2% | +49 pts |

KTLO did not exceed 30% of completed points. The real allocation risk is the 51% buffer bucket, driven by DevQA clones, cross-team SELL work, and reactive tickets added after sprint start.

### Key Findings

#### Scope creep and mid-sprint changes

38 tickets (51 points) were created after sprint start (2026-07-09 17:19 UTC). Highlights:

| Key | Summary | Points | Assignee | Created | Pattern |
|-----|---------|--------|----------|---------|---------|
| SALES-9398 | Title field missing from Vendor Layout | 1 | Gustavo Silva | 2026-07-09 | Reactive vendor support |
| SALES-9400 | ALRA Architecture Diagram and Documentation | 1 | Chris Burns | 2026-07-09 | ALRA priority shift |
| SALES-9411 | Investigate Available_Date__c not populated | 3 | Gustavo Silva | 2026-07-14 | Production data issue |
| SALES-9439 | BatchCalcBoostedNewConsignorCredit UNABLE_TO_ROW_LOCK | 2 | Gustavo Silva | 2026-07-16 | Production incident |
| SALES-9441 | Self-scheduling appointment latency spike | 3 | Gustavo Silva | 2026-07-17 | Performance investigation |
| SALES-9466 | CLONE - Retail SGO Homepage Dashboard Tile | 3 | Jummy Sanni | 2026-07-22 | Late clone, sprint end |
| SALES-9470 | CLONE - Multi Calendar Issue | 2 | Jummy Sanni | 2026-07-22 | Late clone, sprint end |
| SALES-9471 | CLONE - RevOps LeanData & Sumo Access | 1 | Alex Burton | 2026-07-22 | Late clone, sprint end |
| SALES-9475 | Duplicate push topics on funnel finalize | 2 | Gustavo Silva | 2026-07-23 | Production bug, closed after sprint end |
| SALES-9478 | CLONE - Designer/Category Capture Summary | 2 | Chris Burns | 2026-07-23 | Late clone, closed after sprint end |

Removed from sprint (Won't Do, 6 tickets / 4 points): SALES-9116, SALES-9350, SALES-9355, SALES-9375, SALES-9376, SALES-9387.

[OPEN QUESTION: point re-estimates after sprint start not pulled from changelog; verify in Jira if any committed tickets were re-pointed]

Overall pattern: mix of reactive production support (Gus), late ALRA/RevOps clones (Alex, Jummy, Chris), and compliance-adjacent work (Navin). Weak grooming on sprint boundary plus same-day clones on 2026-07-22.

#### Velocity and throughput

| Sprint | Completed Points (Done, manual) |
|--------|--------------------------------|
| Sales 6/11 - 6/24 | 103 (prior retro) |
| Sales 6/25 - 7/8 | 108 |
| **Sales 7/9 - 7/22** | **123** |

Trending up across the last three sprints. Drivers this sprint: Grace Saint's last partial sprint (departed 2026-07-15 per Slack), heavy Gus load (30 pts, 23 tickets), and a sprint-end push (14+ closures on 2026-07-22 per resolution dates). Nag Malluru was out 2026-07-20 through 2026-07-27 (Slack, #srt-team 2026-07-17).

#### Burndown shape

Late-heavy. Resolution dates within the sprint window:

| Date | Closures |
|------|----------|
| 2026-07-09 | 6 |
| 2026-07-10 | 5 |
| 2026-07-13 | 6 |
| 2026-07-14 | 7 |
| 2026-07-15 | 15 |
| 2026-07-16 | 7 |
| 2026-07-17 | 3 |
| 2026-07-20 | 13 |
| 2026-07-21 | 9 |
| 2026-07-22 | 14 |

Week one (7/9-7/13) had steady but modest progress. The sprint surged 7/15, went quiet 7/17 (Nag PTO start, multiple standup absences), then closed hard 7/20-7/22. Not a flatline, but clearly end-loaded.

#### Bug analysis

17 bugs closed Done. Reason for Bug (`customfield_10142`): **all 17 unpopulated**.

| Reason for Bug | Count |
|----------------|-------|
| (unpopulated) | 17 |

Notable bugs closed:

- SALES-9475 (2 pt): duplicate push topics overwriting mm notes on reconsign finalize (Gus; reported via Gabriel Cisneros)
- SALES-9439 (2 pt): BatchCalcBoostedNewConsignorCredit UNABLE_TO_ROW_LOCK (Gus)
- SALES-9470 (2 pt): Multi Calendar Issue, Opp not linking to appt (Jummy)
- SALES-6747 (1 pt): Dropbox signature template name error (Chris)
- SALES-9337 (1 pt): Territory Roster After Create failure (Alex)

Process target: populate Reason for Bug on every closed bug before the next sprint retro. Without it, root-cause trending is blind.

### Per-Engineer Summary (Sales 7/9 - 7/22)

#### Alex Burton: 13 pts completed, 0 carry-over

Completed: SALES-8505 (1), SALES-8506 (1), SALES-9136 (2), SALES-9274 (1), SALES-9275 (1), SALES-9276 (1), SALES-9277 (1), SALES-9337 (1), SALES-9365 (2), SALES-9416 (1), SALES-9471 (1)

#### Jummy Sanni: 15 pts completed, 0 carry-over

Completed: SALES-9239 (2), SALES-9294 (1), SALES-9391 (1), SALES-9393 (1), SALES-9394 (2), SALES-9395 (2), SALES-9430 (1), SALES-9466 (3), SALES-9470 (2)

#### Michael Criswell: 15 pts completed, 0 carry-over

Completed: SALES-9034 (3), SALES-9139 (1), SALES-9225 (3), SALES-9340 (2), SALES-9372 (2), SALES-9403 (1), SALES-9417 (1), SALES-9432 (1), SALES-9438 (1)

#### Chris Burns: 12 pts completed, 0 carry-over

Completed: SALES-6747 (1), SALES-8518 (2), SALES-9226 (1), SALES-9264 (3), SALES-9361 (2), SALES-9400 (1), SALES-9478 (2)

#### Grace Saint: 3 pts completed, 0 carry-over

Completed: SALES-9263 (1), SALES-9351 (2). Grace departed 2026-07-15 (#srt-team farewell thread). SALES-9387 (1 pt) moved to Won't Do.

#### Navinchandra Gupta: 19 pts completed, 0 carry-over

Completed: SALES-8963 (2), SALES-9229 (2), SALES-9330 (1), SALES-9362 (1), SALES-9366 (1), SALES-9373 (1), SALES-9385 (2), SALES-9399 (1), SALES-9402 (1), SALES-9408 (2), SALES-9412 (1), SALES-9413 (1), SALES-9435 (1), SALES-9448 (1), SALES-9454 (1)

#### Nag Malluru: 11 pts completed, 0 carry-over

Completed: SALES-9335 (2), SALES-9342 (1), SALES-9364 (2), SALES-9367 (3), SALES-9369 (1), SALES-9374 (1), SALES-9378 (1). Zendesk bucket placeholders SALES-9375 and SALES-9376 closed Won't Do.

#### Gustavo Silva: 30 pts completed, 0 carry-over

Completed: SALES-8850 (1), SALES-9285 (1), SALES-9301 (1), SALES-9382 (1), SALES-9388 (1), SALES-9397 (1), SALES-9398 (1), SALES-9401 (1), SALES-9404 (1), SALES-9411 (3), SALES-9414 (1), SALES-9415 (1), SALES-9418 (1), SALES-9433 (1), SALES-9437 (1), SALES-9439 (2), SALES-9441 (3), SALES-9444 (2), SALES-9451 (1), SALES-9453 (1), SALES-9455 (1), SALES-9456 (1), SALES-9475 (2)

#### Sai Deepika Kanuri: 5 pts completed, 0 carry-over

Completed: SALES-9389 (2), SALES-9407 (2), SALES-9440 (1). SALES-9355 scope-change story closed Won't Do.

#### Jenn Kleinfeld: 0 pts completed, 0 carry-over

No SALES sprint tickets assigned this sprint. Active in Slack on ALRA RevOps configuration, Sell team triage (SALES-9462), and Grace farewell thread.

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

Alex Burton closed SALES-9136 (ALRA MGO weighting in round robin pools) with documented QA in SALES-9294, then still absorbed three Zendesk bucket tickets and late clone SALES-9471 on 2026-07-22.

Chris Burns shipped the High Value Matrix title-level mapping (SALES-9361) and the Opportunity designer/category capture summary (SALES-9478) in the same final sprint push, plus the ALRA architecture diagram (SALES-9400).

Gustavo Silva carried the heaviest load (30 points, 23 tickets) and still landed SALES-9475, fixing duplicate push topics that were wiping mm notes on reconsign finalize. That was a real production pain point from Gabriel Cisneros's report.

Navinchandra Gupta ran a clean compliance and permissions sprint: MFA enforcement DevQA (SALES-9366), Sailpoint staging install (SALES-9408), PagerDuty schedule update (SALES-9412), and the full High Value Matrix permission set rollout (SALES-9385, SALES-9435, SALES-9399).

Michael Criswell closed the Salesforce security tranche (SALES-9034 MFA, SALES-9340 Profile Filtering, SALES-9417 MFA_Exempt removal) and kept QE regression unblock work moving (SALES-9432, SALES-9438).

Jummy Sanni unblocked SUMO page load work (SALES-9239, previously blocked) and closed two last-day clones (SALES-9466, SALES-9470).

Grace Saint closed SALES-9351 (High Value Designers view/edit permissions) and SALES-9263 (Consignor Referral Link) before her 2026-07-15 departure. The team sent her off in #srt-team.

Nag Malluru delivered outreach wireframe review (SALES-9367), EAC storage spike (SALES-9335), and voice-to-text design options (SALES-9364) before PTO.

### 2. What went well

ALRA routing made tangible progress. SALES-9136 is done with test evidence, SALES-9471 gives RevOps LeanData/Sumo access for routing weight management, and Chris's SALES-9400 architecture doc gives the team a shared picture.

High Value Matrix moved from build to operational. Permissions (SALES-9351, SALES-9385, SALES-9435), title-level mapping (SALES-9361), capture (SALES-9226), and the Opportunity summary (SALES-9478) all closed in this sprint.

Salesforce security and compliance items landed. SALES-9034 (MFA for employees), SALES-9340 (Profile Filtering), SALES-9417 (MFA_Exempt removed from repo), and SALES-9408 (Sailpoint package in staging) are concrete steps on PT-1118.

Production response was fast when it mattered. SALES-9439 (BatchCalc row lock), SALES-9475 (push topics), and SALES-9337 (Territory Roster trigger) all got attention and closure within the sprint window.

Cross-team coordination on consignment kit volume held up. Gustavo's 2026-07-13 analysis in #seller-salestech confirmed Salesforce data matched Supply payloads, which helped narrow the June drop investigation.

PagerDuty and on-call hygiene improved. Navin updated escalation policies (SALES-9412) and posted the change in #srt-team on 2026-07-14.

### 3. What needs work

Reason for Bug is still empty on every closed bug. This is the third sprint in a row we have called it out. Without it, we cannot tell Broken Code from Configuration Gap.

Mid-sprint scope injection remains high. 51 points added after sprint start is a 67% swell on top of the original ~76 point plan. Too many 2026-07-22 clones (SALES-9466, SALES-9470, SALES-9471) that could have been groomed earlier or pushed to Sales 7/23 - 8/5.

Late-heavy burndown is becoming a habit. 14 closures on 2026-07-22 and two tickets finished on 2026-07-23 after sprint end. Navin's 2026-07-22 #srt-core-team reminder to clean the board on sprint close day signals the team knows this.

ALRA configuration scalability is a live stakeholder concern. Devon Novotnak's 2026-07-21 to 2026-07-22 messages in the group DM with Jenn, Bryan, and David flagged individual-level rep weighting as not sustainable for RevOps. That tension showed up after SALES-9136 and SALES-9471 closed.

Gus concentration risk. 30 points on one engineer, many production-adjacent items. If Gus is out, KTLO and incident response capacity drops sharply.

Permission set workflow is still manual and PM-driven. Jenn's comment on SALES-9435 asked for developers to create permission sets as part of delivery, not as a follow-up PM ticket.

Documentation gaps create sprint interrupts. Bryan Claggett's 2026-07-13 #seller-salestech thread on lead expiration and Channel field editability is the pattern: business questions become spikes because process docs do not exist.

SRT label hygiene is still poor. Only 4 tickets had `SRT-Product`. Capacity reporting depends on inference, not labels.

[OPEN QUESTION: confirm current engineering manager. Prompt references Prashanth Patlolla on leave; older notes reference Kishore Kumar Mohan.]

### 4. Discussion Topics

1. SALES-9475 and SALES-9478 closed on 2026-07-23, after the sprint end timestamp. Should the team treat post-midnight closures as carry-over in planning even when Jira marks the sprint complete? What is our cutoff rule?

2. SALES-9136 and SALES-9471 delivered individual rep weighting, but Devon's 2026-07-22 feedback says RevOps needs territory/level-based configuration, not per-rep tuning. Do we pause ALRA go-live work to redesign, or ship and iterate?

3. 38 mid-sprint adds (51 points) vs. ~76 at sprint start. Which of the 2026-07-22 clones (SALES-9466, SALES-9470, SALES-9471, SALES-9478) were truly urgent for the 7/22 close vs. able to wait for Sales 7/23 - 8/5?

4. Gus closed 30 points including SALES-9439, SALES-9441, SALES-9475, and SELL-4934 cross-team work (SALES-9444). How do we cap per-engineer load and protect against a single point of failure on production support?

5. All 17 bugs lack Reason for Bug. Can we make that field required on transition to Done for Bug issue types, starting next sprint?

6. Grace is out. SALES-9387 (SumoAdditionalInfoTriggerHandlerTest) went Won't Do. Who owns her remaining SUMO/Marketing Cloud threads, and is SALES-9469 (SUMO clone, Blocked in next sprint) the right home?

### 5. Action Items

| Item | Owner | Due Date |
|------|-------|----------|
| Confirm Jira sprint report committed/completed for Sales 7/9 - 7/22 and reconcile with manual sum (123 Done pts) | David Garcia | 2026-07-25 |
| Require Reason for Bug on all Bug → Done transitions; backfill SALES-9475, SALES-9439, SALES-9470, SALES-6747, SALES-9337 as pilot | David Garcia | 2026-07-31 |
| Schedule 30-min ALRA configuration review with Devon, Jenn, Bryan, Alex, and Nag on territory/level vs. individual weighting (per 2026-07-22 group DM) | Jenn Kleinfeld | 2026-07-29 |
| Document permission set creation as a standard dev deliverable (per SALES-9435 thread); add to SRT Engineering Process Reference | Navinchandra Gupta | 2026-08-05 |
| Publish Grace Saint handoff: SUMO/Marketing Cloud, Real Partner onboarding (SALES-9264), remaining Blocked SALES-9469 | David Garcia | 2026-07-29 |
| Enforce SRT bucket labels on all new sprint tickets at grooming (SRT-Product, SRT-KTLO, SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | All engineers | Next grooming (2026-07-30) |
| Cap mid-sprint adds: anything added after sprint start needs David or Jenn approval with urgency note in ticket | David Garcia | 2026-07-31 |
| Create SALES-9409 lead expiration spike answer for Bryan (promised 2026-07-13 in #seller-salestech) | Navinchandra Gupta | TBD |

---

## Cross-Project Notes (SRT-tied work outside SALES sprint)

| Key | Project | Summary | Sprint relevance |
|-----|---------|---------|------------------|
| PT-1118 | PT | Software Upgrades & Technical Compliance | SALES-9034, SALES-9340, SALES-9408, SALES-9448 closed this sprint |
| PT-1119 | PT | Salesforce Tech Debt | SALES-6747, SALES-9394, SALES-9395, SALES-9439 closed this sprint |
| SALES-9462 | SALES | Sell Funnel Leads missing zip code | Created 2026-07-21; Gus found SELL-side fix needed (#bdr-salesforce-escalations) |
| SELL-4934 | SELL | Cross-team dev | SALES-9444 tracked Gus support hours |

## Incidents and Escalations (dated)

| Date | Source | Issue | Ticket |
|------|--------|-------|--------|
| 2026-07-13 | Salesforce maintenance | Org down for maintenance | SALES-9437 (documentation) |
| 2026-07-16 | Jira / production | BatchCalcBoostedNewConsignorCredit UNABLE_TO_ROW_LOCK | SALES-9439 |
| 2026-07-16 | #srt-team / Zendesk 130523 | SUMO performance issue | SALES-9239 (unblocked and closed 2026-07-22) |
| 2026-07-17 | #qe-regression | Critical Salesforce UI automation failures (MFA/login) | SALES-9432, SALES-9433, SALES-9438 |
| 2026-07-21 | #bdr-salesforce-escalations | Funnel not sending postalCode | SALES-9462 (SELL-side) |
| 2026-07-23 | Gabriel Cisneros report | Duplicate push topics nulling mm notes on reconsign | SALES-9475 |

## Recording Reference

Sprint planning, standups, and stakeholder threads from this window are in the Google Drive "Meet Recordings" folder.
