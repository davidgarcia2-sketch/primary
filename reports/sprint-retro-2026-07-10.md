# SRT Sprint Retrospective — 2026-07-10

**Sprint:** Sales 6/25 - 7/8  
**Team:** Sales Revenue Technology (SRT)  
**Board:** SALES (ID 10)  
**Report generated:** 2026-07-10

---

## Executive Summary

Sprint **Sales 6/25 - 7/8** closed with strong throughput — **109 story points** completed across **81 tickets** with **zero carry-over**. Execution was front-loaded on ALRA routing and security work early in the sprint, but delivery was **late-heavy**: nearly half of completed points landed in the final three days (7/7–7/9), indicating a sprint-end push rather than steady daily flow. The biggest win was closing the full ALRA routing epic chain (SALES-9129, SALES-9135, SALES-9140, SALES-9224) plus the Apex CPU timeout fix (SALES-6726). The biggest concern is **capacity misalignment**: only 3 tickets carried explicit `SRT-*` labels, pushing 62% of completed work into the buffer/unplanned bucket vs. a 20% target — and the **Reason for Bug** field was unpopulated on all 10 closed bugs.

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 6/25 - 7/8 |
| Sprint Dates | 2026-06-25 – 2026-07-08 |
| Committed Points | 43 (changelog-verified at sprint start, 27 tickets); 53 pts across 33 tickets existed pre-sprint by creation date |
| Completed Points | 109 |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | 9 / 6 (Won't Do) |
| Added Mid-Sprint (tickets / points) | 10 / 17 (changelog-verified); 55 / 59 created during sprint (includes DevQA clones) |
| Scope Change % | +37% net points added (changelog-verified adds minus removals vs. changelog commitment) |
| Spikes Closed | 5 |
| Bugs Closed | 10 |

*Note: 63 of 90 sprint tickets had no Sprint field changes in changelog history; committed-point estimates use creation-date proxy supplemented by changelog analysis where available.*

---

## Capacity Allocation Breakdown

*Based on completed story points (109 total). SRT labels were applied to only 3 tickets (`SRT-Product` on SALES-9075, SALES-9249, SALES-9336); remaining categorization uses summary keywords and Zendesk bucket naming conventions.*

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 28 | 26% | -22 pts vs target |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 4 | 4% | -12 pts vs target |
| KTLO (SRT-KTLO) | 16% | ~11 | 9 | 8% | -8 pts vs target |
| Buffer / Unplanned | 20% | ~14 | 68 | 62% | +42 pts vs target |

**KTLO flag:** KTLO at 8% is below the 30% danger threshold, but the buffer bucket at 62% signals that most work lacks SRT capacity labels — making true allocation tracking unreliable.

---

## Key Findings

### Scope Creep & Mid-Sprint Changes

**Changelog-verified sprint additions (after 6/25 sprint start):**

| Ticket | Summary | Points | Added By | Date |
|--------|---------|--------|----------|------|
| SALES-9311 | Update the reports for shipped to launch price  | 2.0 | Sai Deepika Kanuri | 2026-06-25 |
| SALES-9314 | Research why Available At Date is not syncing from Admi... | 2.0 | Bryan Claggett | 2026-06-26 |
| SALES-9324 | DevQA: SALES-9319 Change COI PE to search records by cr... | 1.0 | Gustavo Silva | 2026-06-29 |
| SALES-9312 | Backfills and Sync needed/ Sales Quota Monthly uploads | 2.0 | Sai Deepika Kanuri | 2026-06-30 |
| SALES-9320 | DevQA: SALES-9146 Agentforce: Look into prompt errors | 1.0 | Chris Burns | 2026-06-30 |
| SELLTECH-636 | Salesforce | Deprecate old funnel memory feature | 2.0 | Michael Criswell | 2026-07-01 |
| SALES-9358 | CLONE - Agentforce Co-worker Introduction and Features | 2.0 | Navinchandra Gupta | 2026-07-07 |
| SALES-9359 | CLONE - Figma Diagram for ZD process | 2.0 | Navinchandra Gupta | 2026-07-07 |
| SALES-9298 | DevQA: SALES-9216 Selection-lwc component permission (c... | 1.0 | Gustavo Silva | 2026-07-07 |
| SALES-9392 | CLONE - Scalable weighting of MGOs by rep type for roun... | 2.0 | Navinchandra Gupta | 2026-07-09 |

**Removed mid-sprint:**

| Ticket | Summary | Points | Removed By | Date |
|--------|---------|--------|------------|------|
| SALES-9298 | DevQA: SALES-9216 Selection-lwc component permission (c | 1.0 | Gustavo Silva | 2026-07-07 |

**Story point changes after sprint start:**

| Ticket | Change | Changed By | Date |
|--------|--------|------------|------|
| SALES-9037 | 2.0 → 1.0 | Nag Malluru | 2026-06-29 |
| SALES-9075 | 1.0 → 2.0 | Jummy Sanni | 2026-07-02 |
| SALES-9075 | 2.0 → 3.0 | Jummy Sanni | 2026-07-02 |
| SALES-9306 | 1.0 → 0.0 | Nag Malluru | 2026-07-07 |
| SALES-9308 | 1.0 → 0.0 | Nag Malluru | 2026-07-07 |

**Pattern:** Mid-sprint additions were a mix of legitimate priority shifts (SELLTECH-636 cross-team deprecation, SALES-9358/9359 Agentforce design clones added 7/7) and reactive work (SALES-9314 data sync research, SALES-9347 null-pointer bug). The late addition of SALES-9392 on 7/9 — moved back from the next sprint and closed same-day — suggests sprint-close accounting rather than new scope. Point inflation on SALES-9075 (1→2→3) by Jummy Sanni indicates estimation refinement mid-sprint. Nag Malluru zeroed out placeholder Zendesk bucket tickets (SALES-9306, SALES-9308), converting planned capacity buckets to Won't Do.

### Velocity & Throughput

| Sprint | Completed Points | Tickets Done |
|--------|-----------------|--------------|
| Sales 5/14 – 5/27 | 108 | 73 |
| Sales 5/28 – 6/10 | 86 | 51 |
| Sales 6/11 – 6/24 | 102 | 68 |
| **Sales 6/25 – 7/8** | **109** | **81** |

Velocity is **flat to slightly up** compared to the prior three sprints, recovering from the 86-point dip in Sales 5/28 – 6/10. The 5/28 sprint dip may correlate with the Summer Release 2026 push overlapping that period. No major team composition changes noted in ticket assignment patterns.

### Burndown Analysis

| Period | Points Completed | % of Sprint Total |
|--------|-----------------|-------------------|
| Week 1 (6/25–6/30) | 26 | 24% |
| Week 2 (7/1–7/8) | 78 | 72% |
| Final 3 days (7/7–7/9) | 52 | 48% |

**Pattern: Late-heavy.** Only 24% of points completed in the first week. The burndown flatlined early (5 pts on 6/25, 4 on 6/26) then accelerated sharply from 7/6 onward (14 + 23 + 24 + 5 pts). This is not a steady burndown — the team relied on a sprint-end delivery push, with 7/7–7/8 alone accounting for 43% of all completions.

### Bug Analysis

10 bugs closed this sprint. **Reason for Bug field (`customfield_10142`) was unpopulated on all 10** — no categorization available.

| Ticket | Summary | Points | Reason for Bug |
|--------|---------|--------|----------------|
| SALES-6726 | Apex CPU Timeout With Opps with 1000+ COI's | 3 | *Not populated* |
| SALES-9146 | Agentforce: Look into prompt errors | 1 | *Not populated* |
| SALES-9237 | Commissions: Priced units are more than the Shippe... | 3 | *Not populated* |
| SALES-9244 | Fix failing QE Mocha Automation tests | 1 | *Not populated* |
| SALES-9289 | Fix wrongfully contact merged | 1 | *Not populated* |
| SALES-9304 | Nag - Zendesk KTLO Bucket - 06/25-7/8 | 1 | *Not populated* |
| SALES-9313 | Vendor SKUs removed from COIs | 1 | *Not populated* |
| SALES-9339 | Troubleshoot qe-regression failures | 2 | *Not populated* |
| SALES-9347 | InquiriesService.updateLead | Attempt to de-refere... | 1 | *Not populated* |
| SALES-9380 | CLONE - Report Export > 10k rows is taking the use... | 1 | *Not populated* |

**Process gap:** Without Reason for Bug data, the team cannot identify whether bugs stem from broken code, configuration gaps, or data integrity issues. This should be a retro action item.

---

## Per-Engineer Summary

### Alex Burton

**Total points completed:** 11.0

**Tickets completed:**
- SALES-9140 — Territory Level distinction for new role: ALRA -2 (2.0 pts)
- SALES-9224 — Route Escalated Leads to a Higher Tier LD - 2 (2.0 pts)
- SALES-9266 — June EOM Updates (1.0 pts)
- SALES-9270 — Cohorts 6/29/26 - 7/6/26 (1.0 pts)
- SALES-9271 — KTLO: Alex Zendesk Ticket 6/25 - 7/8 (1.0 pts)
- SALES-9272 — TD: Alex Zendesk Ticket 6/25 - 7/8 (1.0 pts)
- SALES-9296 — DevQA: SALES-9203 Automate the updating of each months quota records for job profile -  2 (1.0 pts)
- SALES-9392 — CLONE - Scalable weighting of MGOs by rep type for round robin pools in ALRA identified territories. -2 (2.0 pts)

**Tickets carried over:** None

### Jummy Sanni

**Total points completed:** 11.0

**Tickets completed:**
- SALES-8843 — Change the help text/description for Total Retail Price on Opportunity object (1.0 pts)
- SALES-9075 — Create SUMO Calendar Knowledge Article Staging (3.0 pts)
- SALES-9132 — This is an MGO this is an SGO -1 (2.0 pts)
- SALES-9290 — KTLO: Zendesk Support (1.0 pts)
- SALES-9295 — DevQA: SALES-9139 Count of MGO by Rep in ALRA markets - 2 (1.0 pts)
- SALES-9297 — DevQA: SALES-9209 Update Opportunity Apex Trigger to Capture Scheduled Van Pickups (1.0 pts)
- SALES-9305 — CLONE - Tech Debt: Zendesk Support (1.0 pts)
- SALES-9307 — CLONE - SoftwareUpdates: Zendesk Support (1.0 pts)

**Tickets carried over:** None

### Michael Criswell

**Total points completed:** 8.0

**Tickets completed:**
- SALES-9033 — Security Update: Enforce phishing-resistant MFA for privileged users (including admins) (1.0 pts)
- SALES-9202 — Backfill of field: Job Profile on quota object for June 2026 -1 or 2 (1.0 pts)
- SALES-9247 — Backfill: Remove "+" from Contact First Names Where DNC = True and Ownership Reassigned to Sales Ops (1.0 pts)
- SALES-9282 — Backfill COI AUR Contributing Price Field (1.0 pts)
- SALES-9300 — DevQA: SALES-9146 Agentforce: Look into prompt errors (1.0 pts)
- SALES-9315 — DevQA: SALES-9236 LeadConvertProcessor.processLeadAddresses exceptions being notified by email (1.0 pts)
- SALES-9344 — DevQA: SALES-9140 Territory Level distinction for new role: ALRA -2 (0 pts)
- SALES-9348 — DevQA: SALES-9347 InquiriesService.updateLead | Attempt to de-reference a null object (0 pts)
- SELLTECH-636 — Salesforce | Deprecate old funnel memory feature (2.0 pts)

**Tickets carried over:** None

### Chris Burns

**Total points completed:** 14.0

**Tickets completed:**
- SALES-6726 — Apex CPU Timeout With Opps with 1000+ COI's (3.0 pts)
- SALES-7254 — Update the label names on the lead button so it is consistent across the lwc and the lead page. (1.0 pts)
- SALES-9129 — Define the Escalation Criteria for high-value designer leads and set high value flag - 2 (3.0 pts)
- SALES-9249 — Update Loss Reason Picklist: Add Unable to Reach (1.0 pts)
- SALES-9291 — DevQA: SALES-9132 This is an MGO this is an SGO -1 (1.0 pts)
- SALES-9293 — DevQA: SALES-9135 High Value Matrix Selection LWC Component -2 (1.0 pts)
- SALES-9299 — DevQA: SALES-9223 High-Value Designer/Category Matrix - 2 (1.0 pts)
- SALES-9320 — DevQA: SALES-9146 Agentforce: Look into prompt errors (1.0 pts)
- SALES-9324 — DevQA: SALES-9319 Change COI PE to search records by crm_id or slug (1.0 pts)
- SALES-9349 — Test 2:  DevQA: SALES-9223 High-Value Designer/Category Matrix - 2 (1.0 pts)

**Tickets carried over:** None

### Grace Saint

**Total points completed:** 14.0

**Tickets completed:**
- SALES-9135 — High Value Matrix Selection LWC Component -2 (4.0 pts)
- SALES-9146 — Agentforce: Look into prompt errors (1.0 pts)
- SALES-9203 — Automate the updating of each months quota records for job profile -  2 (2.0 pts)
- SALES-9209 — Update Opportunity Apex Trigger to Capture Scheduled Van Pickups (1.0 pts)
- SALES-9216 — Selection-lwc component permission (create & grant to internal users). 2 (1.0 pts)
- SALES-9223 — High-Value Designer/Category Matrix - 2 (2.0 pts)
- SALES-9292 — DevQA: SALES-9129 Define the Escalation Criteria for high-value designer leads and set high value flag - 2 (1.0 pts)
- SALES-9317 — July Campaign Member Upload (1.0 pts)
- SALES-9343 — July 5th Real Partners Monthly Reports (1.0 pts)

**Tickets carried over:** None

### Navinchandra Gupta

**Total points completed:** 13.0

**Tickets completed:**
- SALES-9144 — Order the necessary software licenses for the ALRA expansion 1 (1.0 pts)
- SALES-9287 — DevQA: SALES-9035 Security Update: Implement step-up authentication for Salesforce report activities (1.0 pts)
- SALES-9288 — DevQA: SALES-9037 Security Update: Adopt Transaction Security policy enhancements (1.0 pts)
- SALES-9309 — Assign Sales Compensation Comp Admin Permission Set to Michael Criswell (1.0 pts)
- SALES-9310 — Assign Records to Inactive User permission set assignment to Gustavo Silva (1.0 pts)
- SALES-9321 — Manage Public List Views Access in Salesforce Staging and Production (1.0 pts)
- SALES-9338 — DevQA: SALES-9036 Security Update: Prepare step-up authentication for anomalous report export (1.0 pts)
- SALES-9341 — DevQA: SALES-9336 Create BDR List Views for New Process (1.0 pts)
- SALES-9358 — CLONE - Agentforce Co-worker Introduction and Features (2.0 pts)
- SALES-9359 — CLONE - Figma Diagram for ZD process (2.0 pts)
- SALES-9384 — DevQA: SALES-9075 Create SUMO Calendar Knowledge Article (1.0 pts)

**Tickets carried over:** None

### Nag Malluru

**Total points completed:** 10.0

**Tickets completed:**
- SALES-8392 — Cleanup Unused Reports and Dashboards (1.0 pts)
- SALES-9032 — Security Update: Review extended login anomaly detection and containment impact (1.0 pts)
- SALES-9035 — Security Update: Implement step-up authentication for Salesforce report activities (1.0 pts)
- SALES-9036 — Security Update: Prepare step-up authentication for anomalous report export (1.0 pts)
- SALES-9037 — Security Update: Adopt Transaction Security policy enhancements (1.0 pts)
- SALES-9038 — Security Update: Communicate June 2026 Salesforce security changes to end users (1.0 pts)
- SALES-9283 — DevQA: SALES-7254 Update the label names on the lead button so it is consistent across the lwc and the lead page. (1.0 pts)
- SALES-9286 — DevQA: SALES-9033 Security Update: Enforce phishing-resistant MFA for privileged users (including admins) (1.0 pts)
- SALES-9304 — Nag - Zendesk KTLO Bucket - 06/25-7/8 (1.0 pts)
- SALES-9306 — Nag - Zendesk Bucket - Tech Debt - 06/25-7/8 (0.0 pts)
- SALES-9308 — Nag - Zendesk - S/w Upgrades - 06/25 - 7/8 (0.0 pts)
- SALES-9380 — CLONE - Report Export > 10k rows is taking the users to classic version (1.0 pts)

**Tickets carried over:** None

### Gustavo Silva

**Total points completed:** 22.0

**Tickets completed:**
- SALES-8951 — Decommissioning termed users licenses and permissions for zoom and sumo users (2.0 pts)
- SALES-9228 — Fix the consignor contacts that don't have a user_external_id__c in the last 90 days (2.0 pts)
- SALES-9236 — LeadConvertProcessor.processLeadAddresses exceptions being notified by email (1.0 pts)
- SALES-9244 — Fix failing QE Mocha Automation tests (1.0 pts)
- SALES-9284 — DevQA: SALES-6726 Apex CPU Timeout With Opps with 1000+ COI's (1.0 pts)
- SALES-9289 — Fix wrongfully contact merged (1.0 pts)
- SALES-9298 — DevQA: SALES-9216 Selection-lwc component permission (create & grant to internal users). 2 (1.0 pts)
- SALES-9303 — DevQA: SALES-9249 Update Loss Reason Picklist: Add Unable to Reach (1.0 pts)
- SALES-9313 — Vendor SKUs removed from COIs (1.0 pts)
- SALES-9314 — Research why Available At Date is not syncing from Admin to Salesforce (2.0 pts)
- SALES-9319 — Change COI PE to search records by crm_id or slug (2.0 pts)
- SALES-9329 — Backfill the COIs that are missing Available_Date__c  (1.0 pts)
- SALES-9339 — Troubleshoot qe-regression failures (2.0 pts)
- SALES-9347 — InquiriesService.updateLead | Attempt to de-reference a null object (1.0 pts)
- SALES-9357 — Helped Developing SELL-4934 (2.0 pts)
- SELLTECH-1054 — DevQA: SELLTECH-636 Salesforce | Deprecate old funnel memory feature (1.0 pts)

**Tickets carried over:** None

### Sai Deepika Kanuri

**Total points completed:** 10.0

**Tickets completed:**
- SALES-9237 — Commissions: Priced units are more than the Shipped items/ Duplicate Opps are marking NC as true (3.0 pts)
- SALES-9248 — CLONE - Evaluate Design for Weighted Routing, Escalation and Lead Scoring -1 (3.0 pts)
- SALES-9311 — Update the reports for shipped to launch price  (2.0 pts)
- SALES-9312 — Backfills and Sync needed/ Sales Quota Monthly uploads (2.0 pts)

**Tickets carried over:** None

---

## Cross-Project Tickets (PT- / SELLTECH-)

| Ticket | Summary | Points | Status | Assignee |
|--------|---------|--------|--------|----------|
| SELLTECH-636 | Salesforce \| Deprecate old funnel memory feature | 2 | Done | Michael Criswell |
| SELLTECH-1054 | DevQA: SELLTECH-636 | 1 | Done | Gustavo Silva |

No PT- tickets were in this sprint. SELLTECH-636 was added mid-sprint (7/1) as cross-team Salesforce decoupling work.

---

## Discussion Prompts

1. **SALES-9392 was added on 7/9 (sprint close day), moved from Sales 7/9–7/22, and marked Done within minutes** — is this sprint-close hygiene inflating completion metrics, and should end-of-sprint ticket moves be discouraged?

2. **62% of completed points landed in the buffer/unlabeled bucket** because only 3 of 90 tickets had `SRT-*` labels. Should we enforce label application at sprint planning, or accept keyword-based inference for retro reporting?

3. **48% of all points completed in the final 3 days (7/7–7/9)** — what blocked earlier delivery on ALRA stories (SALES-9135, SALES-9140) that sat in progress for 10+ days before closing? Is DevQA batching at sprint end creating artificial late-heavy burndowns?

4. **All 10 closed bugs lack Reason for Bug categorization** — can we agree to populate `customfield_10142` before moving bugs to Done, starting next sprint?

5. **9 tickets marked Won't Do (6 pts), including 4 security updates (SALES-9033, SALES-9037) and 2 Zendesk placeholder buckets (SALES-9306, SALES-9308)** — were these descoped due to priority shifts or incomplete grooming? Should security tickets descoped mid-sprint roll to a dedicated security sprint?

---

*Data sources: Jira SALES board (ID 10), sprint "Sales 6/25 - 7/8", queried 2026-07-10. Includes SELLTECH-636 and SELLTECH-1054.*
