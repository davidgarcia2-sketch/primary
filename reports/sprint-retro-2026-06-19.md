# SRT Sprint Retrospective Report

**Sprint:** Sales 5/28 - 6/10  
**Report Date:** June 19, 2026  
**Team:** Salesforce Release Technology (SRT)  
**Data Source:** SALES Jira board (board ID 10), sprint closed June 10, 2026

---

## Executive Summary

Sprint **Sales 5/28 - 6/10** was a **high-throughput sprint with clean closure** — 51 of 55 tickets reached Done status with **zero carry-over**. The biggest win was completing the long-running API version bump initiative (SALES-8550 through SALES-8553) alongside strong bug resolution across Real Partners, consignment, and Zendesk support queues. The biggest concern is **continued reactive scope injection**: 20 tickets were created after sprint start (mostly Zendesk buckets, clone tickets, and production firefighting), and story points remain unpopulated across the board, making capacity planning and velocity tracking impossible.

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 5/28 - 6/10 |
| Sprint Dates | May 28, 2026 – June 10, 2026 |
| Committed Points | Unavailable — story points not populated in Jira for sprint tickets |
| Completed Points | Unavailable — story points not populated in Jira for sprint tickets |
| Carry-Over (tickets / points) | 0 / N/A |
| Removed (tickets / points) | 4 / N/A |
| Added Mid-Sprint (tickets / points) | 20 / N/A |
| Scope Change % | Unavailable — cannot compute without story points |
| Spikes Closed | 9 |
| Bugs Closed | 14 |

**Status breakdown:** Done: 51, Won't Do: 4  
**Type breakdown:** Bug: 18, Spike: 9, Story: 26, Task: 2  
**Total tickets in sprint:** 55

---

## Capacity Allocation Breakdown

> **Data limitation:** Story points are not populated on SALES sprint tickets. SRT capacity labels (`SRT-KTLO`, `SRT-Domain-Tech-Debt`, `SRT-Software-Upgrades`) are largely absent — only `SRT-Product` appears on 7 tickets. Below shows **ticket-count-based allocation** as a proxy; point-based targets cannot be computed.

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % (tickets) | Delta |
|--------|----------|------------------------|---------------|-------------------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | Unavailable | 13% (7 tickets) | Cannot compute |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | Unavailable | 0% (0 tickets) | Cannot compute |
| KTLO (SRT-KTLO) | 16% | ~11 | Unavailable | 0% (0 tickets) | Cannot compute |
| Buffer / Unplanned | 20% | ~14 | Unavailable | 87% (48 tickets) | Cannot compute |

**KTLO flag:** Cannot assess against 30% threshold — no tickets carry the `SRT-KTLO` label. However, Zendesk bucket tickets (6 tickets referencing Zendesk) and operational tasks suggest significant unlabeled KTLO work in the buffer bucket.

**Tickets with SRT-Product label:** SALES-8801, SALES-8918, SALES-8920, SALES-9024, SALES-9085, SALES-9175, SALES-9185

---

## Key Findings

### Scope Creep & Mid-Sprint Changes

**Tickets added after sprint start (20 total):**

| Key | Summary | Type | Assignee | Created |
|-----|---------|------|----------|---------|
| SALES-9085 | ZD Tickets: 5/28 - 6/10 | Story | Jummy Sanni | 2026-05-28 |
| SALES-9086 | Nag - Zendesk Bucket - 05/28-6/10 | Bug | Nag Malluru | 2026-05-28 |
| SALES-9087 | Zendesk 5/28 Sprint | Bug | Chris Burns | 2026-05-28 |
| SALES-9088 | Zendesk Tickets 5/28-6/10 | Bug | Grace Saint | 2026-05-28 |
| SALES-9089 | CI/CD pipeline breaking because of Enabling Deliverability Substitute Email step | Story | Gustavo Silva | 2026-05-28 |
| SALES-9105 | Alex Zendesk Ticket 5/28 - 6/10 | Bug | Alex Burton | 2026-05-28 |
| SALES-9106 | Salesforce | Accept referral_code and advocate_user_id on inquiry platform event | Story | Gustavo Silva | 2026-05-28 |
| SALES-9109 | June Sales Quota uploads | Story | Sai Deepika Kanuri | 2026-05-31 |
| SALES-9110 | Upload Double Point Matrix and Point Matrix new uploads | Story | Sai Deepika Kanuri | 2026-06-01 |
| SALES-9114 | Send 5th of Month CSVs to Real Partners Marketing Team | Task | Grace Saint | 2026-06-02 |
| SALES-9115 | Zendesk Bug Ticket Holder (May 28 - June 10) | Bug | Navinchandra Gupta | 2026-06-02 |
| SALES-9127 | Fix COI Comp Flow to only trigger if New Consignor Multiplier changes and Available Date is populated | Bug | Gustavo Silva | 2026-06-04 |
| SALES-9134 | Backfill for the bug in Production for comp | Story | Sai Deepika Kanuri | 2026-06-04 |
| SALES-9142 | Duplicate COIs | Bug | Gustavo Silva | 2026-06-05 |
| SALES-9145 | Remove Data Mask package | Story | Nag Malluru | 2026-06-08 |
| SALES-9165 | Hellosign contract Signature is not displaying properly on iPad | Bug | Nag Malluru | 2026-06-09 |
| SALES-9174 | CLONE - Backfill AUR_Contributing_Price__c field | Task | Michael Criswell | 2026-06-10 |
| SALES-9175 | CLONE - Create SUMO Calendar Knowledge Article | Story | Jummy Sanni | 2026-06-10 |
| SALES-9177 | CLONE - Technical Design for Outreach Optimization | Story | Nag Malluru | 2026-06-10 |
| SALES-9185 | CLONE - SMS/Phone Automation | Spike | Jummy Sanni | 2026-06-10 |

**Tickets removed from sprint (4 total — Won't Do):**

| Key | Summary | Type | Assignee |
|-----|---------|------|----------|
| SALES-8968 | May.'26 SUMO Sync Issue | Bug | Unassigned |
| SALES-9028 | Real Partners W-9 Link Errors | Bug | Michael Criswell |
| SALES-9046 | Real Partners: Two referral records being created when a RP Consignor signs up through Affiliate link | Bug | Grace Saint |
| SALES-9086 | Nag - Zendesk Bucket - 05/28-6/10 | Bug | Nag Malluru |

**Story point changes:** Unavailable — no story points populated on sprint tickets; changelog analysis for point changes not performed.

**Pattern analysis:** The mid-sprint additions fall into three categories:
1. **Reactive support (Zendesk buckets):** SALES-9085, SALES-9086, SALES-9087, SALES-9088, SALES-9105, SALES-9115 — created at sprint start or within days, representing ongoing support work not fully groomed before commitment.
2. **Production firefighting:** SALES-9089 (CI/CD pipeline break), SALES-9127 (COI comp flow bug), SALES-9134 (backfill), SALES-9142 (duplicate COIs) — legitimate urgent production issues.
3. **End-of-sprint clones:** SALES-9174, SALES-9175, SALES-9177, SALES-9185 — cloned into sprint on June 10, likely carry-forward prep for next sprint.

Four tickets were marked Won't Do (SALES-8968, SALES-9028, SALES-9046, SALES-9086), reducing scope without delivery.

### Velocity & Throughput

**Completed points vs. prior 3 sprints:** Unavailable — story points are not populated on SALES sprint tickets.

**Ticket throughput (Done count) — trending down:**

| Sprint | Done Tickets |
|--------|-------------|
| Sales 5/28 – 6/10 (current) | 51 |
| Sales 5/14 – 5/27 | 100 |
| SALES 4/30 – 5/13 | 57 |
| Sales 4/16 – 4/29 | 58 |

Throughput dropped sharply from 100 Done tickets last sprint to 51 this sprint. The prior sprint included a large Summer 26 release validation batch (SALES-8980 through SALES-8999); this sprint shifted to API version bumps, consignment/COI firefighting, and Zendesk support. Zero carry-over this sprint indicates clean closure despite lower volume.

**PT- and SELLTECH- cross-project tickets:** No PT- or SELLTECH- tickets with SRT labels were found updated during the sprint window (May 28 – June 11, 2026).

**Contributing factors:** Memorial Day (May 26, just before sprint start) may have compressed grooming. Heavy Zendesk and production bug load consumed capacity across multiple engineers.

### Burndown Analysis

- **Daily closures:** 2026-05-28: 4, 2026-05-29: 1, 2026-06-01: 5, 2026-06-02: 6, 2026-06-03: 7, 2026-06-04: 8, 2026-06-08: 5, 2026-06-09: 7, 2026-06-10: 11
- **Week 1 (May 28 – Jun 3):** 23 closures (43% of total)
- **Week 2 (Jun 4 – Jun 10):** 31 closures (57% of total)
- **Final 3 days (Jun 8–10):** 23 closures (43% of total)
- **Pattern classification:** **Late-heavy** (43%+ of closures in final 3 days)

Closure activity was distributed across both weeks (43% week 1, 57% week 2), but **43% of all closures landed in the final 3 days** (June 8–10), including Zendesk buckets (SALES-9087, SALES-9088, SALES-9105) and four clone tickets closed on sprint day 13. Memorial Day (May 26) may have compressed early-week momentum; May 30–31 and June 5–7 show zero closures in Jira resolution dates.

### Bug Analysis

**Reason for Bug field:** Unavailable — `customfield_10142` (Reason for Bug) is null on all closed bugs in this sprint.

**Bugs closed (Done):** 14 tickets

| Key | Summary | Assignee |
|-----|---------|----------|
| SALES-9043 | SUMO Service Rooms | Sai Deepika Kanuri |
| SALES-9067 | SGO LWC: Referral Not Saving for Certain Users | Grace Saint |
| SALES-9068 | OpportunityTriggerHelper.populateMatchedAdvocateContact | Missing Contact.Owner from SOQL | Gustavo Silva |
| SALES-9069 | SumoEmailScheduler.getConsignor | consignor not found. Appt Id: XXXX | Gustavo Silva |
| SALES-9071 | Related Real Partner Not Tagging on New Referral Records | Grace Saint |
| SALES-9081 | Consignment First Available Date Inaccuracies | Gustavo Silva |
| SALES-9084 | SFMC email: Consignment Received with Item List Summary Email Sent | Gustavo Silva |
| SALES-9087 | Zendesk 5/28 Sprint | Chris Burns |
| SALES-9088 | Zendesk Tickets 5/28-6/10 | Grace Saint |
| SALES-9105 | Alex Zendesk Ticket 5/28 - 6/10 | Alex Burton |
| SALES-9115 | Zendesk Bug Ticket Holder (May 28 - June 10) | Navinchandra Gupta |
| SALES-9127 | Fix COI Comp Flow to only trigger if New Consignor Multiplier changes and Available Date is populated | Gustavo Silva |
| SALES-9142 | Duplicate COIs | Gustavo Silva |
| SALES-9165 | Hellosign contract Signature is not displaying properly on iPad | Nag Malluru |

**Bugs removed (Won't Do):** 4 tickets — SALES-8968, SALES-9028, SALES-9046, SALES-9086

**Dominant themes (from summaries, not Reason for Bug field):**
- Real Partners / referral issues: SALES-9067, SALES-9071, SALES-9043 (SUMO Service Rooms)
- Consignment / COI data: SALES-9081, SALES-9127, SALES-9142
- Zendesk support buckets: SALES-9087, SALES-9088, SALES-9105, SALES-9115
- Integration / platform: SALES-9068, SALES-9069, SALES-9084

Without Reason for Bug data, process improvement recommendations cannot be tied to root-cause categories. **Recommend enforcing Reason for Bug on all bug closures.**

---

## Per-Engineer Summary

### Alex Burton

**Tickets completed (3):**
- SALES-9060: Review and Categorization of Remaining Zendesk Tickets (N/A pts)
- SALES-9073: 6/1/26 - 6/8/26 Cohorts (N/A pts)
- SALES-9105: Alex Zendesk Ticket 5/28 - 6/10 (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Jummy Sanni

**Tickets completed (4):**
- SALES-8918: Turn on Inbox (N/A pts)
- SALES-9085: ZD Tickets: 5/28 - 6/10 (N/A pts)
- SALES-9175: CLONE - Create SUMO Calendar Knowledge Article (N/A pts)
- SALES-9185: CLONE - SMS/Phone Automation (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Michael Criswell

**Tickets completed (4):**
- SALES-8550: Bump Controller classes from API Version 54 to 65 - Ticket 2 of 2 (N/A pts)
- SALES-8552: Bump Batch classes from API Version 54 to 65 - Ticket 2 of 2 (N/A pts)
- SALES-9079: Phishing-Resistant Multi-Factor Authentication (MFA) for Privileged Users, including Admins (N/A pts)
- SALES-9174: CLONE - Backfill AUR_Contributing_Price__c field (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Chris Burns

**Tickets completed (5):**
- SALES-8551: Bump Batch classes from API Version 54 to 66 - Ticket 1 of 2 (N/A pts)
- SALES-8553: Bump Mock classes from API Version 54 to 66 (N/A pts)
- SALES-8966: T&C Acceptance Tracking (N/A pts)
- SALES-9074: [UNABLE_TO_LOCK_ROW] SFDC Error Developer script exception from The RealReal (N/A pts)
- SALES-9087: Zendesk 5/28 Sprint (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Grace Saint

**Tickets completed (6):**
- SALES-9047: Research how we can create conversational consignor summaries (N/A pts)
- SALES-9067: SGO LWC: Referral Not Saving for Certain Users (N/A pts)
- SALES-9071: Related Real Partner Not Tagging on New Referral Records (N/A pts)
- SALES-9082: June: Campaign Member Uploads (N/A pts)
- SALES-9088: Zendesk Tickets 5/28-6/10 (N/A pts)
- SALES-9114: Send 5th of Month CSVs to Real Partners Marketing Team (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Navinchandra Gupta

**Tickets completed (5):**
- SALES-8801: Identify all fields in Salesforce without a Description (N/A pts)
- SALES-9072: Deployer Access for Salesforce-CRM Repo - May 2026 (N/A pts)
- SALES-9078: Review and Rationalization of Salesforce Distribution Lists (N/A pts)
- SALES-9083: Add a realreal.com Authorized Email Domain in Production (N/A pts)
- SALES-9115: Zendesk Bug Ticket Holder (May 28 - June 10) (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Nag Malluru

**Tickets completed (4):**
- SALES-8978: Integration Landscape and Data Flow Diagrams (N/A pts)
- SALES-9145: Remove Data Mask package (N/A pts)
- SALES-9165: Hellosign contract Signature is not displaying properly on iPad (N/A pts)
- SALES-9177: CLONE - Technical Design for Outreach Optimization (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Gustavo Silva

**Tickets completed (14):**
- SALES-8650: Update sumo tests regarding Dec 27 warning (N/A pts)
- SALES-8965: Backfill price differences between SF and Admin (N/A pts)
- SALES-9068: OpportunityTriggerHelper.populateMatchedAdvocateContact | Missing Contact.Owner from SOQL (N/A pts)
- SALES-9069: SumoEmailScheduler.getConsignor | consignor not found. Appt Id: XXXX (N/A pts)
- SALES-9070: CLONE - Summer 26 Release | Vendor Bulk Upload (N/A pts)
- SALES-9080: Backfill Consignment_Order_Item__c.Available_Date__c from 05/06 until 05/27 (N/A pts)
- SALES-9081: Consignment First Available Date Inaccuracies (N/A pts)
- SALES-9084: SFMC email: Consignment Received with Item List Summary Email Sent (N/A pts)
- SALES-9089: CI/CD pipeline breaking because of Enabling Deliverability Substitute Email step (N/A pts)
- SALES-9106: Salesforce | Accept referral_code and advocate_user_id on inquiry platform event (N/A pts)
- SALES-9119: Change deploy-to-staging skill to be able to deploy to any sandbox (N/A pts)
- SALES-9124: Migrate sfConvertLeadSumoCal.test.js to use new createSGOLead method (N/A pts)
- SALES-9127: Fix COI Comp Flow to only trigger if New Consignor Multiplier changes and Available Date is populated (N/A pts)
- SALES-9142: Duplicate COIs (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

### Sai Deepika Kanuri

**Tickets completed (6):**
- SALES-8920: Update reporting to reflect TRR Price instead of List Price (N/A pts)
- SALES-9024: Q2 Incentive Changes Deployment Placeholder (N/A pts)
- SALES-9043: SUMO Service Rooms (N/A pts)
- SALES-9109: June Sales Quota uploads (N/A pts)
- SALES-9110: Upload Double Point Matrix and Point Matrix new uploads (N/A pts)
- SALES-9134: Backfill for the bug in Production for comp (N/A pts)

**Tickets carried over (0):**
- None

**Total points completed:** N/A (no story points in Jira)

---

## Discussion Prompts

1. **Story points are blank on all 55 sprint tickets** — how do we enforce point estimation at grooming so capacity allocation and velocity tracking become possible? Should we block sprint commitment without points?

2. **Six Zendesk bucket tickets** (SALES-9085, SALES-9087, SALES-9088, SALES-9105, SALES-9115, plus SALES-9086 Won't Do) were added at or after sprint start — is the current Zendesk triage process feeding too much reactive work into the sprint? What can we deflect to KTLO capacity or defer?

3. **Four tickets were cloned into the sprint on June 10** (SALES-9174, SALES-9175, SALES-9177, SALES-9185) and immediately closed — are we using clones to inflate sprint completion, or is this a grooming gap from the prior sprint?

4. **SRT labels are missing on 48 of 55 tickets** — only 7 tickets carry `SRT-Product` and zero carry `SRT-KTLO`, `SRT-Domain-Tech-Debt`, or `SRT-Software-Upgrades`. How do we make label assignment part of the sprint planning checklist?

5. **Done ticket count dropped from 100 to 51** while Gustavo Silva closed 14 tickets alone — is the throughput decline a post-release normalization, and does the team need to rebalance load across engineers?

---

*Report generated automatically from Jira SALES board data. PT-/SELLTECH- cross-project query returned no SRT-labeled tickets for this sprint window.*
