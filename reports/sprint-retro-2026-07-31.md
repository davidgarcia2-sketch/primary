# Sales 7/9 - 7/22

**Sprint:** Sales 7/9 - 7/22  
**Sprint Dates:** July 9, 2026 - July 22, 2026  
**Report Date:** July 31, 2026  
**Team:** Salesforce Release Technology (SRT)  
**Data Sources:** SALES Jira board (board ID 10), Weekly Status Report July 13-17 (Notion), #srt_squadleads / #sales-pt-squad-leads Slack, SRT Action Items Tracker (Notion), Google Drive Meet Recordings folder

[OPEN QUESTION: Sales 7/23 - 8/5 remains active in Jira as of July 31. This report covers the most recently closed sprint per board state.]

---

## Part A: Metrics Report

### Executive Summary

Sprint **Sales 7/9 - 7/22** closed clean on the board (zero carry-over as of July 31) but the delivery shape was late-heavy and scope-heavy. The team shipped ALRA routing foundations (SALES-9136, SALES-9471), High Value Matrix permissions and capture (SALES-9351, SALES-9385, SALES-9435, SALES-9478), Salesforce security compliance (SALES-9034, SALES-9340), and a production push-topic fix (SALES-9475). The biggest concern is sustained mid-sprint injection (35 tickets, 48 points added after sprint start), Gus carrying 30 of 123 completed points, and all closed bugs still missing Reason for Bug values.

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 7/9 - 7/22 |
| Sprint Dates | July 9, 2026 - July 22, 2026 |
| Committed Points | 127 (manual sum at sprint close, Sales 7/9 - 7/22) [OPEN QUESTION: confirm committed in Jira Sprint Report velocity view; API does not expose sprint report figures] |
| Completed Points | 123 (manual sum, Done tickets, Sales 7/9 - 7/22). Cross-check: 86 Done tickets, story-level `customfield_10026`, sub-task points excluded. [OPEN QUESTION: sprint report may count Won't Do toward completed; reconcile before meeting if report shows 127] |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | 6 / 4 (Won't Do) |
| Added Mid-Sprint (tickets / points) | 35 / 48 (created after 2026-07-09 17:19 UTC sprint start) |
| Scope Change % | +61% net points added vs. ~79 pts at sprint start (48 added / 79 original) |
| Spikes Closed | 9 |
| Bugs Closed | 15 (Done status; 2 bugs Won't Do: SALES-9350, SALES-9387) |

**Sprint goal (Jira):** ALRA Routing; SUMO Bugs; Salesforce Security tickets; Voice Recognition Design

**Status breakdown:** Done: 86, Won't Do: 6  
**Type breakdown:** Story: 29, Task: 36, Bug: 17, Spike: 10  
**Total tickets in sprint:** 92 (story-level; no sub-task points counted)

*Estimation level: story-level `customfield_10026`. Board closed statuses: Done, Won't Do. Won't Do excluded from completed points manual sum.*

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

35 tickets (48 points) were created after sprint start (2026-07-09 17:19 UTC). Highlights:

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
| SALES-9475 | Duplicate push topics on funnel finalize | 2 | Gustavo Silva | 2026-07-23 | Production bug, resolved after sprint end |
| SALES-9478 | CLONE - Designer/Category Capture Summary | 2 | Chris Burns | 2026-07-23 | Late clone, resolved after sprint end |

Removed from sprint (Won't Do, 6 tickets / 4 points): SALES-9116, SALES-9350, SALES-9355, SALES-9375, SALES-9376, SALES-9387.

Overall pattern: mix of reactive production support (Gus), late ALRA/RevOps clones (Alex, Jummy, Chris on 7/22-7/23), and compliance-adjacent work (Navin). Weak grooming at sprint boundary plus same-day clones on 7/22.

#### Velocity and throughput

| Sprint | Completed Points (Done, manual) |
|--------|--------------------------------|
| Sales 6/11 - 6/24 | 103 (prior retro) |
| Sales 6/25 - 7/8 | 108 |
| **Sales 7/9 - 7/22** | **123** |

Trending up across the last three sprints. Drivers this sprint: Grace Saint's partial sprint (last day July 15 per user context; Notion weekly status also references July 27 for KT, [OPEN QUESTION: confirm exact last day]), heavy Gus load (30 pts, 23 tickets), Nag Malluru PTO starting July 20 (Weekly Status Report July 13-17, Notion), and a sprint-end push (17 closures on 2026-07-22 per resolution dates).

#### Burndown shape

Late-heavy. Resolution dates within the sprint window:

| Date | Closures |
|------|----------|
| 2026-07-09 | 5 |
| 2026-07-10 | 4 |
| 2026-07-13 | 6 |
| 2026-07-14 | 7 |
| 2026-07-15 | 15 |
| 2026-07-16 | 5 |
| 2026-07-17 | 3 |
| 2026-07-20 | 13 |
| 2026-07-21 | 9 |
| 2026-07-22 | 17 |

Week one (7/9-7/13) had steady but modest progress. The sprint surged 7/15, went quiet 7/17 (Nag PTO start), then closed hard 7/20-7/22. Not a flatline, but clearly end-loaded.

#### Bug analysis

15 bugs closed Done. Reason for Bug (`customfield_10142`): all 15 unpopulated.

| Reason for Bug | Count |
|----------------|-------|
| (unpopulated) | 15 |

Notable bugs closed:

- SALES-9475 (2 pt): duplicate push topics overwriting mm notes on reconsign finalize (Gus; production)
- SALES-9439 (2 pt): BatchCalcBoostedNewConsignorCredit UNABLE_TO_ROW_LOCK (Gus; 2026-07-16)
- SALES-9470 (2 pt): Multi Calendar Issue, Opp not linking to appt (Jummy)
- SALES-6747 (1 pt): Dropbox signature template name error (Chris)
- SALES-9337 (1 pt): Territory Roster After Create failure (Alex)

Process target: populate Reason for Bug on every closed bug. Zero compliance this sprint despite the field being introduced at sprint planning (Weekly Status Report July 13-17).

### Per-Engineer Summary (Sales 7/9 - 7/22)

#### Alex Burton (13 pts done, 0 carry)

Completed: SALES-8505 (1), SALES-8506 (1), SALES-9136 (2), SALES-9274 (1), SALES-9275 (1), SALES-9276 (1), SALES-9277 (1), SALES-9337 (1), SALES-9365 (1), SALES-9416 (1), SALES-9471 (1)  
Carry-over: none

#### Jummy Sanni (15 pts done, 0 carry)

Completed: SALES-9239 (2), SALES-9294 (1), SALES-9391 (1), SALES-9393 (1), SALES-9394 (2), SALES-9395 (2), SALES-9430 (1), SALES-9466 (3), SALES-9470 (2)  
Carry-over: none

#### Michael Criswell (15 pts done, 0 carry)

Completed: SALES-9034 (3), SALES-9139 (1), SALES-9225 (3), SALES-9340 (2), SALES-9372 (2), SALES-9403 (1), SALES-9417 (1), SALES-9432 (1), SALES-9438 (1)  
Carry-over: none

#### Chris Burns (12 pts done, 0 carry)

Completed: SALES-6747 (1), SALES-8518 (2), SALES-9226 (1), SALES-9264 (3), SALES-9361 (2), SALES-9400 (1), SALES-9478 (2)  
Carry-over: none

#### Grace Saint (3 pts done, 0 carry)

Completed: SALES-9263 (1), SALES-9351 (2)  
Carry-over: none  
Note: partial sprint; last day July 15 per sprint context.

#### Navinchandra Gupta (19 pts done, 0 carry)

Completed: SALES-8963 (2), SALES-9229 (2), SALES-9330 (1), SALES-9362 (1), SALES-9366 (1), SALES-9373 (1), SALES-9385 (2), SALES-9399 (1), SALES-9402 (1), SALES-9408 (2), SALES-9412 (1), SALES-9413 (1), SALES-9435 (1), SALES-9448 (1), SALES-9454 (1)  
Carry-over: none

#### Nag Malluru (11 pts done, 0 carry)

Completed: SALES-9335 (2), SALES-9342 (1), SALES-9364 (2), SALES-9367 (3), SALES-9369 (1), SALES-9374 (1), SALES-9378 (1)  
Carry-over: none  
Note: PTO July 20-27 per Weekly Status Report July 13-17.

#### Gustavo Silva (30 pts done, 0 carry)

Completed: SALES-8850 (1), SALES-9285 (1), SALES-9301 (1), SALES-9382 (1), SALES-9388 (1), SALES-9397 (1), SALES-9398 (1), SALES-9401 (1), SALES-9404 (1), SALES-9411 (3), SALES-9414 (1), SALES-9415 (1), SALES-9418 (1), SALES-9433 (1), SALES-9437 (1), SALES-9439 (2), SALES-9441 (3), SALES-9444 (2), SALES-9451 (1), SALES-9453 (1), SALES-9455 (1), SALES-9456 (1), SALES-9475 (2)  
Carry-over: none

#### Sai Deepika Kanuri (5 pts done, 0 carry)

Completed: SALES-9389 (2), SALES-9407 (2), SALES-9440 (1)  
Carry-over: none

#### Jenn Kleinfeld (0 pts done, 0 carry)

No sprint tickets assigned. Product work tracked outside Jira sprint board (ALRA BRD escalation thread in #srt_squadleads, July 16).

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

Gustavo Silva closed 30 points across 23 tickets while absorbing the bulk of reactive production work: SALES-9439 (row lock, 7/16), SALES-9411 (Available_Date__c, 7/14), SALES-9441 (self-scheduling latency spike, 7/17), and SALES-9475 (duplicate push topics, 7/23). That is a full engineer's sprint worth of unplanned work on top of DevQA load.

Navinchandra Gupta shipped 19 points including the High Value Matrix permission chain (SALES-9385, SALES-9435), SailPoint package install (SALES-9408), and SOC 1 request (SALES-9448), all while covering on-call rotation updates (SALES-9412).

Alex Burton and Jummy Sanni closed the ALRA routing table work (SALES-9136) and the sprint-end clone batch (SALES-9466, SALES-9470, SALES-9471) that unblocked RevOps weighted table testing.

Grace Saint landed SALES-9351 (High Value Designers view/edit permissions) in her final partial sprint before departure.

Chris Burns delivered SALES-9400 (ALRA architecture diagram) and SALES-9478 (Designer/Category capture summary) while holding org test coverage (SALES-8518).

### 2. What went well

Zero carry-over. Every ticket in the sprint reached Done or Won't Do. That is the third consecutive sprint with no carry-over per Jira state.

ALRA routing foundations shipped. SALES-9136 (scalable MGO weighting), SALES-9471 (RevOps LeanData/Sumo access), and SALES-9400 (architecture documentation) give RevOps a testable routing layer ahead of the August 3 High Value target (Weekly Status Report July 13-17).

Security compliance closed. SALES-9034 (MFA enforcement) and SALES-9340 (profile filtering) both reached Done, hitting a sprint goal item.

Process improvements landed at sprint start. T-shirt sizing, dev-qa tags, and Reason for Bug field were introduced at the July 14 team meeting (Weekly Status Report July 13-17). ARB-before-dev rule is in place.

High Value Matrix went live for permissions. SALES-9351, SALES-9385, SALES-9435 closed the view/edit permission chain for RevOps and Sales Leadership.

### 3. What needs work

Reason for Bug is empty on all 15 closed bugs. We introduced the field at sprint planning and nobody used it. That kills our ability to target process fixes.

Gus is a single point of failure for production incidents. 30 of 123 points (24%) went to one contractor, mostly reactive. If he is out, KTLO spikes immediately.

Mid-sprint injection is the norm, not the exception. 35 tickets and 48 points added after sprint start. The 7/22 clone batch (SALES-9466, SALES-9470, SALES-9471, SALES-9478) was same-day work that should have been in the prior sprint or the next one.

SRT labels are not being applied. Only 4 tickets carried `SRT-Product`. Capacity reporting defaults to a 51% buffer bucket, which makes the allocation conversation with leadership meaningless.

Grace Saint transition created a knowledge gap. Gus still needs Agentforce/Data Cloud KT per Weekly Status Report July 13-17. Two open reqs (Miranda backfill, Grace replacement) are blocked on H1 visa policy from Prashanth.

Agentforce FDE engagement is at risk. Voice Agent was put on hold by Product the same week the FDE kicked off (July 13). Devon is inclined to defer the engagement without Product sign-off on the 15 engineering-owned use cases David compiled.

### 4. Discussion topics

1. SALES-9439 and SALES-9475 both came from production and ate 4 points combined. Gus resolved both, but they were not in the sprint at planning. Should production incidents get a dedicated KTLO buffer ticket at sprint start instead of landing as ad hoc stories?

2. The 7/22 clone batch added 8 points on the last day of the sprint (SALES-9466, SALES-9470, SALES-9471, SALES-9478). Who requested these and could they have been groomed into Sales 7/23 - 8/5?

3. Reason for Bug is zero for 15 closed bugs. Is the field too hard to find in Jira, or do we need a workflow validator before Done?

4. Jenn raised in #srt_squadleads (July 16) that Sales is centralizing the BRD escalation channel, which could cut SRT visibility into recurring issues. What is our input mechanism if bugs no longer flow through the team directly?

5. Buffer bucket hit 51% of completed points. Is that real unplanned work, or a labeling failure? If we tagged DevQA clones and Zendesk bucket tickets correctly, what would the actual KTLO % be?

### 5. Action items

| Item | Owner | Due date |
|------|-------|----------|
| Populate Reason for Bug on all bugs closed in Sales 7/9 - 7/22 (retroactive) and enforce on new closures | All engineers | 2026-08-08 |
| Apply SRT-Product / SRT-KTLO / SRT-Domain-Tech-Debt labels at ticket creation per bucket system proposal | David Garcia | 2026-08-05 |
| Complete Grace Saint KT sessions with Gus (Agentforce/Data Cloud) | Nag Malluru, Gus | TBD |
| Confirm H1 visa hiring policy with Prashanth for two open reqs | David Garcia | TBD |
| Schedule BRD escalation visibility sync per Jenn's #srt_squadleads thread (July 16) | David Garcia, Jenn Kleinfeld | TBD |
| Share FDE use case list with Eli and Devon to decide on engagement continuation | David Garcia | 2026-08-01 |
| Consult Casey at July 27 office hours on ticket bucket point caps before finalizing | David Garcia | 2026-07-27 |
| Confirm weighted table go-live date with RevOps (Jenn thread, July 23) | Jenn Kleinfeld, Devon Novotnak | TBD |
