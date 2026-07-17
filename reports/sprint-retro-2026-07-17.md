# Sales 6/25 - 7/8 (2026-06-25 to 2026-07-08)

**Sprint:** Sales 6/25 - 7/8  
**Board:** SALES (ID 10)  
**Report date:** 2026-07-17

---

# Part A: Metrics Report

## Executive Summary

Sprint **Sales 6/25 - 7/8** closed clean on the board: **81 tickets** completed with **zero carry-over**, and the team shipped the core ALRA routing chain (SALES-9129, SALES-9135, SALES-9140, SALES-9224) plus the Apex CPU timeout fix (SALES-6726). Delivery was **late-heavy**, with roughly half of completed points landing in the final three days (7/7 through 7/9). The biggest concern is measurement hygiene: only 3 of 90 sprint tickets carried `SRT-*` labels, the **Reason for Bug** field was empty on all 10 closed bugs, and [OPEN QUESTION: Jira Sprint Report committed/completed figures could not be pulled live on 2026-07-17 because Atlassian MCP requires authentication; manual issue analysis from 2026-07-10 shows 109 completed points vs. a 43-point changelog-verified commitment].

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 6/25 - 7/8 |
| Sprint Dates | 2026-06-25 to 2026-07-08 |
| Committed Points | [OPEN QUESTION: Jira Sprint Report not reachable on 2026-07-17. Changelog-verified commitment: 43 pts across 27 tickets at sprint start. Creation-date proxy: 53 pts across 33 pre-sprint tickets.] |
| Completed Points | 109 (manual sum, 2026-07-10 Jira query). [OPEN QUESTION: reconcile against Jira Sprint Report velocity view before the meeting.] |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | 9 / 6 (Won't Do) |
| Added Mid-Sprint (tickets / points) | 10 / 17 (changelog-verified); 55 tickets created during sprint window (includes DevQA clones) |
| Scope Change % | +37% net points added vs. changelog commitment (adds minus removals) |
| Spikes Closed | 5 |
| Bugs Closed | 10 |

*Estimation level: story-level `customfield_10026`. Sub-task points excluded from manual sum. Done and Won't Do counted as resolved per board config.*

## Capacity Allocation

*Based on 109 completed story points (Sales 6/25 - 7/8). Only SALES-9075, SALES-9249, and SALES-9336 carried explicit `SRT-Product`. Remaining buckets inferred from summary keywords and Zendesk bucket naming.*

| Bucket | Target % | Target Points | Actual Points | Actual % | Delta |
|--------|----------|---------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 28 | 26% | -6 pts vs target |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 4 | 4% | -7 pts vs target |
| KTLO (SRT-KTLO) | 16% | ~11 | 9 | 8% | -2 pts vs target |
| Buffer / Unplanned | 20% | ~14 | 68 | 62% | +48 pts vs target |

KTLO at 8% is below the 30% danger threshold. The real signal is the 62% buffer bucket, which reflects missing labels more than true unplanned work.

## Key Findings

### Scope creep and mid-sprint changes

**Added after 2026-06-25 (changelog-verified):**

| Ticket | Summary | Points | Added By | Date |
|--------|---------|--------|----------|------|
| SALES-9311 | Update the reports for shipped to launch price | 2 | Sai Deepika Kanuri | 2026-06-25 |
| SALES-9314 | Research why Available At Date is not syncing from Admin to Salesforce | 2 | Bryan Claggett | 2026-06-26 |
| SALES-9324 | DevQA: SALES-9319 Change COI PE to search records by crm_id or slug | 1 | Gustavo Silva | 2026-06-29 |
| SALES-9312 | Backfills and Sync needed/ Sales Quota Monthly uploads | 2 | Sai Deepika Kanuri | 2026-06-30 |
| SALES-9320 | DevQA: SALES-9146 Agentforce: Look into prompt errors | 1 | Chris Burns | 2026-06-30 |
| SELLTECH-636 | Salesforce / Deprecate old funnel memory feature | 2 | Michael Criswell | 2026-07-01 |
| SALES-9358 | CLONE - Agentforce Co-worker Introduction and Features | 2 | Navinchandra Gupta | 2026-07-07 |
| SALES-9359 | CLONE - Figma Diagram for ZD process | 2 | Navinchandra Gupta | 2026-07-07 |
| SALES-9298 | DevQA: SALES-9216 Selection-lwc component permission | 1 | Gustavo Silva | 2026-07-07 |
| SALES-9392 | CLONE - Scalable weighting of MGOs by rep type for round robin pools | 2 | Navinchandra Gupta | 2026-07-09 |

**Removed mid-sprint (Won't Do):** SALES-9298 (1 pt, removed same day it was added), plus 8 other tickets totaling 6 pts including SALES-9306, SALES-9308 (Zendesk placeholder buckets zeroed by Nag Malluru).

**Re-pointed after sprint start:**

| Ticket | Change | Changed By | Date |
|--------|--------|------------|------|
| SALES-9037 | 2 → 1 | Nag Malluru | 2026-06-29 |
| SALES-9075 | 1 → 2 → 3 | Jummy Sanni | 2026-07-02 |
| SALES-9306 | 1 → 0 | Nag Malluru | 2026-07-07 |
| SALES-9308 | 1 → 0 | Nag Malluru | 2026-07-07 |

The pattern mixes legitimate priority shifts (SELLTECH-636 cross-team deprecation, Agentforce clones on 7/7) with reactive support (SALES-9314 data sync research, SALES-9347 null-pointer bug) and sprint-close accounting (SALES-9392 added 7/9, moved from Sales 7/9-7/22, closed same day).

### Velocity and throughput

| Sprint | Completed Points | Source |
|--------|-----------------|--------|
| Sales 5/14 - 5/27 | 108 | Jira query 2026-07-10 |
| Sales 5/28 - 6/10 | 86 | Jira query 2026-07-10 |
| Sales 6/11 - 6/24 | 102 | Jira query 2026-07-10 |
| **Sales 6/25 - 7/8** | **109** | Jira query 2026-07-10 |

Velocity recovered from the 86-point dip in Sales 5/28 - 6/10 and sits flat to slightly up vs. the prior three sprints. Grace Saint was active through this sprint (last day 2026-07-15). No team-wide PTO pattern visible in assignee throughput.

### Burndown shape

| Period | Points Completed | % of Sprint Total |
|--------|-----------------|-------------------|
| Week 1 (6/25-6/30) | 26 | 24% |
| Week 2 (7/1-7/8) | 78 | 72% |
| Final 3 days (7/7-7/9) | 52 | 48% |

**Late-heavy.** Only 24% of points in week one. The burndown flatlined early (5 pts on 6/25, 4 on 6/26), then accelerated from 7/6 onward. ALRA stories (SALES-9135, SALES-9140) sat in progress for 10+ days before closing with their DevQA children batched at sprint end.

### Bug analysis

10 bugs closed. **Reason for Bug (`customfield_10142`) was unpopulated on all 10.**

| Ticket | Summary | Points |
|--------|---------|--------|
| SALES-6726 | Apex CPU Timeout With Opps with 1000+ COI's | 3 |
| SALES-9146 | Agentforce: Look into prompt errors | 1 |
| SALES-9237 | Commissions: Priced units are more than the Shipped items | 3 |
| SALES-9244 | Fix failing QE Mocha Automation tests | 1 |
| SALES-9289 | Fix wrongfully contact merged | 1 |
| SALES-9304 | Nag - Zendesk KTLO Bucket - 06/25-7/8 | 1 |
| SALES-9313 | Vendor SKUs removed from COIs | 1 |
| SALES-9339 | Troubleshoot qe-regression failures | 2 |
| SALES-9347 | InquiriesService.updateLead null dereference | 1 |
| SALES-9380 | CLONE - Report Export > 10k rows classic redirect | 1 |

Without Reason for Bug data, we cannot tell if broken code, configuration gaps, or data integrity drove the volume. Process target: populate the field before Done.

### Cross-project tickets

| Ticket | Summary | Points | Status | Assignee |
|--------|---------|--------|--------|----------|
| SELLTECH-636 | Salesforce / Deprecate old funnel memory feature | 2 | Done | Michael Criswell |
| SELLTECH-1054 | DevQA: SELLTECH-636 | 1 | Done | Gustavo Silva |

No PT- tickets were in this sprint. SELLTECH-636 was added mid-sprint (7/1).

## Per-Engineer Summary

### Alex Burton

**Total points completed: 11**

Completed: SALES-9140 Territory Level distinction for ALRA (2), SALES-9224 Route Escalated Leads (2), SALES-9266 June EOM Updates (1), SALES-9270 Cohorts 6/29-7/6 (1), SALES-9271 KTLO Zendesk 6/25-7/8 (1), SALES-9272 TD Zendesk 6/25-7/8 (1), SALES-9296 DevQA SALES-9203 (1), SALES-9392 CLONE Scalable MGO weighting (2).

Carry-over: None.

### Jummy Sanni

**Total points completed: 11**

Completed: SALES-8843 Total Retail Price help text (1), SALES-9075 SUMO Calendar Knowledge Article Staging (3), SALES-9132 MGO/SGO routing (2), SALES-9290 KTLO Zendesk (1), SALES-9295 DevQA SALES-9139 (1), SALES-9297 DevQA SALES-9209 (1), SALES-9305 CLONE Tech Debt Zendesk (1), SALES-9307 CLONE Software Upgrades Zendesk (1).

Carry-over: None.

### Michael Criswell

**Total points completed: 8**

Completed: SALES-9033 Security MFA privileged users (1), SALES-9202 Job Profile quota backfill (1), SALES-9247 DNC contact name backfill (1), SALES-9282 COI AUR backfill (1), SALES-9300 DevQA SALES-9146 (1), SALES-9315 DevQA SALES-9236 (1), SALES-9344 DevQA SALES-9140 (0), SALES-9348 DevQA SALES-9347 (0), SELLTECH-636 Deprecate funnel memory (2).

Carry-over: None.

### Chris Burns

**Total points completed: 14**

Completed: SALES-6726 Apex CPU timeout (3), SALES-7254 Lead button label consistency (1), SALES-9129 Escalation Criteria HV leads (3), SALES-9249 Loss Reason picklist (1), SALES-9291 DevQA SALES-9132 (1), SALES-9293 DevQA SALES-9135 (1), SALES-9299 DevQA SALES-9223 (1), SALES-9320 DevQA SALES-9146 (1), SALES-9324 DevQA SALES-9319 (1), SALES-9349 Test 2 DevQA SALES-9223 (1).

Carry-over: None.

### Grace Saint

**Total points completed: 14**

Completed: SALES-9135 High Value Matrix LWC (4), SALES-9146 Agentforce prompt errors (1), SALES-9203 Automate quota job profile updates (2), SALES-9209 Opportunity trigger van pickups (1), SALES-9216 Selection-lwc permissions (1), SALES-9223 HV Designer/Category Matrix (2), SALES-9292 DevQA SALES-9129 (1), SALES-9317 July Campaign Member Upload (1), SALES-9343 July Real Partners reports (1).

Carry-over: None. Grace's last day was 2026-07-15; she was fully active this sprint.

### Navinchandra Gupta

**Total points completed: 13**

Completed: SALES-9144 ALRA license procurement (1), SALES-9287 DevQA SALES-9035 (1), SALES-9288 DevQA SALES-9037 (1), SALES-9309 Comp Admin permission set (1), SALES-9310 Assign Records to Inactive User PS (1), SALES-9321 Public List Views access (1), SALES-9338 DevQA SALES-9036 (1), SALES-9341 DevQA SALES-9336 (1), SALES-9358 CLONE Agentforce Co-worker (2), SALES-9359 CLONE Figma ZD process (2), SALES-9384 DevQA SALES-9075 (1).

Carry-over: None.

### Nag Malluru

**Total points completed: 10**

Completed: SALES-8392 Cleanup unused reports (1), SALES-9032 through SALES-9038 security updates (5), SALES-9283 DevQA SALES-7254 (1), SALES-9286 DevQA SALES-9033 (1), SALES-9304 Zendesk KTLO bucket (1), SALES-9306 Zendesk Tech Debt bucket (0), SALES-9308 Zendesk S/w Upgrades bucket (0), SALES-9380 CLONE Report Export (1).

Carry-over: None.

### Gustavo Silva

**Total points completed: 22**

Completed: SALES-8951 Decommission termed user licenses (2), SALES-9228 Fix consignor user_external_id (2), SALES-9236 LeadConvertProcessor exceptions (1), SALES-9244 Fix QE Mocha tests (1), SALES-9284 DevQA SALES-6726 (1), SALES-9289 Fix wrongfully merged contact (1), SALES-9298 DevQA SALES-9216 (1), SALES-9303 DevQA SALES-9249 (1), SALES-9313 Vendor SKUs removed from COIs (1), SALES-9314 Available At Date sync research (2), SALES-9319 COI PE search by crm_id (2), SALES-9329 Backfill COI Available_Date (1), SALES-9339 QE regression failures (2), SALES-9347 InquiriesService null dereference (1), SALES-9357 Helped Developing SELL-4934 (2), SELLTECH-1054 DevQA SELLTECH-636 (1).

Carry-over: None.

### Sai Deepika Kanuri

**Total points completed: 10**

Completed: SALES-9237 Commissions priced units mismatch (3), SALES-9248 CLONE Weighted Routing design eval (3), SALES-9311 Shipped to launch price reports (2), SALES-9312 Quota monthly uploads backfill (2).

Carry-over: None.

### Jenn Kleinfeld

**Total points completed: 0**

No SALES sprint tickets assigned or completed in Sales 6/25 - 7/8. Jenn was active on ALRA product questions (weighted table routing by rep name vs. role type, confirmed by Alex Burton on 2026-07-15 in #prod-srt-alra-expansion-h2-2026) and coordinated with Deepika on SUMO distribution testing during the sprint window.

Carry-over: None.

---

# Part B: The Retro (45 minutes)

## Shoutouts

Chris Burns and Grace Saint paired on the ALRA escalation chain. Chris closed SALES-9129 (escalation criteria, 3 pts) and Grace delivered SALES-9135 (High Value Matrix LWC, 4 pts) and SALES-9223 (designer/category matrix, 2 pts). That work unblocked Alex Burton's territory routing (SALES-9140, SALES-9224) and Deepika's weighted pool testing.

Gustavo Silva carried the highest individual load at 22 points, including the cross-team SELLTECH-636 deprecation, SALES-9319 COI search fix, and SALES-9314 Available At Date sync research that Bryan Claggett pulled in on 6/26.

Jummy Sanni landed SALES-9075 (SUMO Calendar Knowledge Article, 3 pts) after re-pointing it twice during the sprint, and closed the MGO/SGO routing story SALES-9132 that ALRA staging depended on.

Navinchandra Gupta shipped five tickets on 7/7 alone (SALES-9358, SALES-9359, SALES-9380, plus DevQA children), including the Agentforce and ZD process clones that let incomplete parent work count toward sprint close.

Nag Malluru closed the full Salesforce security communication batch (SALES-9032 through SALES-9038) in a single sprint while keeping Zendesk bucket hygiene honest by zeroing placeholder tickets SALES-9306 and SALES-9308 instead of carrying fake capacity.

## What went well

Zero carry-over. Navin posted on 6/24 (prior sprint close) that the board was clean, and Sales 6/25 - 7/8 repeated that: every ticket reached Done or Won't Do. That is the sprint hygiene target from the process reset doc.

ALRA routing shipped to staging. The escalation criteria, HV matrix LWC, territory distinction, and escalated-lead routing stories (SALES-9129, SALES-9135, SALES-9140, SALES-9224) all closed. Weekly status on 7/6-7/10 noted staging tests completed, with routing bugs surfaced before a go-live call.

Q2 bucket epics closed. SALES-9039 (Domain Tech Debt) and SALES-9041 (Software Upgrades) both moved to Done on 2026-07-09, closing out the Q2 tech health containers on schedule.

Cross-team decoupling landed. SELLTECH-636 (deprecate funnel memory) and its DevQA child SELLTECH-1054 both closed, reducing Salesforce coupling with the seller funnel.

Production stayed moving. Navin ran Salesforce-CRM releases on 7/7 and 7/15 per #releases, including SALES-9351 High Value Designer Viewer and SALES-9417 MFA exempt cleanup.

## What needs work

Late-heavy burndown is becoming the default. 48% of points closed in the last three days. ALRA work in particular sat in progress while DevQA clones piled up at the end. That makes sprint metrics look healthier than the daily flow actually was.

SRT capacity labels are effectively unused. Three tickets out of 90 had `SRT-*` labels, which pushed 62% of work into the buffer bucket and makes the capacity table above unreliable for staffing decisions.

Reason for Bug is still blank on every closed bug. Ten bugs closed, zero categorized. We cannot target process improvements without that field.

Reactive mid-sprint intake continues. SELLTECH-636 (7/1), SALES-9314 (6/26), and the 7/7 Agentforce clones were legitimate, but the volume of CLONE tickets created at sprint close (SALES-9358, SALES-9359, SALES-9392) suggests we are still accounting for in-flight work at the deadline instead of planning it in.

Staging environment instability ate engineering time. QA regression bots flagged critical Salesforce UI failures (waffle button not rendering, 7/7 and 7/14) and widespread API 500s across the sprint window. Gustavo, Mike, and Chris spent cycles on SALES-9244 and SALES-9339 automation fixes that may have been environment-driven.

Grace's exit on 7/15 leaves a gap on campaign operations and Real Partners reporting (SALES-9317, SALES-9343 were her last sprint deliveries). Handoff coverage is still flagged as medium risk in the 7/6-7/10 weekly status.

[OPEN QUESTION: confirm current manager. User notes list Prashanth Patlolla on leave; weekly status addendum references Kishore handing storage procurement to Prashanth before 6/26.]

## Discussion Topics

1. SALES-9392 was added on 7/9, moved back from Sales 7/9-7/22, and closed within minutes. Is that sprint-close hygiene inflating velocity, and should we block same-day add-and-close moves?

2. SALES-9075 was re-pointed from 1 to 3 by Jummy Sanni on 7/2. The work shipped, but the commitment at sprint start did not reflect the true size. How do we catch estimate drift earlier?

3. Four security stories (SALES-9033, SALES-9037 and DevQA children) were marked Won't Do mid-sprint while five other security tickets closed. Were the Won't Do items descoped or deferred, and do they need a dedicated Q3 security slot?

4. SALES-6726 (Apex CPU timeout, 3 pts) and SALES-9146 (Agentforce prompt errors) both closed without Reason for Bug. If we had to pick one process fix for next sprint, is mandatory bug categorization or mandatory SRT labels higher priority?

5. Deepika told Jenn on 7/7 she was still testing SUMO distribution logic in sandbox. Alex confirmed weighted routing worked in Minneapolis on 7/14. What blocked earlier validation, and does the DevQA-at-sprint-end pattern explain the late burndown?

## Action Items

| Item | Owner | Due date |
|------|-------|----------|
| Pull committed and completed points from Jira Sprint Report velocity view and reconcile against the 109-point manual sum | David Garcia | Before retro meeting |
| Enforce Reason for Bug (`customfield_10142`) on all bugs before Done transition | Nag Malluru | Next sprint start |
| Require `SRT-Product`, `SRT-KTLO`, `SRT-Domain-Tech-Debt`, or `SRT-Software-Upgrades` label at sprint planning for every story 1 pt or larger | David Garcia / Navinchandra Gupta | Sales 7/9-7/22 planning retro |
| Document ticket cloning process and demo at standup (carry-forward from prior sprint) | Navinchandra Gupta | TBD |
| Complete Grace Saint handoff for campaign uploads and Real Partners reporting | David Garcia / team | TBD (Grace last day 7/15) |
| Follow up on HelloSign RCA completion (Navin drafted; Samuel review never completed) | Navinchandra Gupta | TBD |
| Create Q3 capacity document with PTO and holidays | Navinchandra Gupta | TBD |
| Get Zendesk-to-JSM migration dates from Patrick Palmer for Q3 capacity model | Navinchandra Gupta | TBD |

---

*Data sources: Jira SALES board (ID 10) sprint Sales 6/25 - 7/8, queried 2026-07-10; Notion Weekly Status Raw Data 2026-07-09; Notion Slack Sweeps 2026-07-07 and 2026-07-10; Weekly Status Report 2026-07-06 to 2026-07-10; SRT Action Items Tracker (Notion). Atlassian MCP unavailable for live re-query on 2026-07-17.*
