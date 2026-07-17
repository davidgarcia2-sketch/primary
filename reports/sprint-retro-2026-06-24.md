# SRT Sprint Retrospective — Sales 6/11 - 6/24

*Generated: 2026-06-26 | Source: SALES Jira Board (ID 10)*

---

## Executive Summary

Sprint **Sales 6/11 - 6/24** closed with **100% ticket completion** — all 71 sprint tickets reached Done or Won't Do status with **zero carry-over**. The team delivered strong execution on the ALRA routing initiative (14 spikes closed, extensive routing/MGO/outreach discovery) and completed Salesforce Security Phase 2 work (SALES-9031, SALES-9232). The biggest win was closing the full sprint scope including late-added ALRA clones (SALES-9265, SALES-9268, SALES-9269) on the final day. The biggest concern is **continued scope creep**: 21 tickets were created after sprint start, pushing total completed points to 103 against an initial commitment of 80 points. KTLO allocation remains a concern, and **all 13 closed bugs lack "Reason for Bug" data** in Jira — blocking root-cause analysis.

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 6/11 - 6/24 |
| Sprint Dates | 2026-06-11 — 2026-06-24 |
| Committed Points | 80 (50 tickets at sprint start) |
| Completed Points | 103 |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | 3 / 1 |
| Added Mid-Sprint (tickets / points) | 21 / 23 |
| Scope Change % | +28% |
| Spikes Closed | 14 |
| Bugs Closed | 13 |

---

## Capacity Allocation Breakdown

*Note: SRT labels are sparsely applied (only SALES-9048 has `SRT-Product`). Allocation below is inferred from ticket summaries and Zendesk bucket naming conventions.*

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 41 | 40% | -8% |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 14 | 14% | -2% |
| KTLO (SRT-KTLO) | 16% | ~11 | 6 | 6% | -10% |
| Buffer / Unplanned | 20% | ~14 | 42 | 41% | +21% |

---

## Key Findings

### Scope Creep & Mid-Sprint Changes

**Tickets added after sprint start (2026-06-11):**

- **SALES-9199** (2 pt) — ALRA Solutioning and Review - 1 — added 2026-06-15, assignee: Grace Saint
- **SALES-9241** (1 pt) — CLONE - Agentforce: Look into prompt errors — added 2026-06-23, assignee: Grace Saint
- **SALES-9265** (2 pt) — CLONE - Update Opportunity Apex Trigger to Capture Scheduled Van Pickups — added 2026-06-24, assignee: Grace Saint
- **SALES-9207** (1 pt) — CID 16146775 - New Rolex Item getting added to COI by TRR CRM Service user — added 2026-06-15, assignee: Gustavo Silva
- **SALES-9208** (1 pt) — OpportunityTriggerHelper.setContactContractComplete | Contact.Contract_Complete__c missing from SOQL — added 2026-06-16, assignee: Gustavo Silva
- **SALES-9210** (1 pt) — Activate field history on Payment__c object — added 2026-06-17, assignee: Gustavo Silva
- **SALES-9214** (1 pt) — Vendor Price Update Errors — added 2026-06-18, assignee: Gustavo Silva
- **SALES-9222** (1 pt) — Optimize how new vendor opportunities are created in SF — added 2026-06-19, assignee: Gustavo Silva
- **SALES-9231** (0 pt) — Retry oban job of inquiries that failed because of the unknown field error in Production — added 2026-06-22, assignee: Gustavo Silva
- **SALES-9200** (1 pt) — CLONE - Tech Debt: ZD tickets 6/11-6/24 — added 2026-06-15, assignee: Jummy Sanni
- **SALES-9201** (1 pt) — CLONE - SFTW Upgrade: ZD tickets 6/11-6/24 — added 2026-06-15, assignee: Jummy Sanni
- **SALES-9268** (1 pt) — CLONE - This is an MGO this is an SGO -1 — added 2026-06-24, assignee: Jummy Sanni
- **SALES-9269** (1 pt) — CLONE - Change the help text/description for Total Retail Price on Opportunity object — added 2026-06-24, assignee: Jummy Sanni
- **SALES-9219** (1 pt) — Create Permission Set to Bypass MFA Enforcement for Test Automation Users — added 2026-06-18, assignee: Michael Criswell
- **SALES-9234** (2 pt) — CLONE - ZoomSyncPlatformEventTriggerHandler.ZoomSyncPlatformEventTriggerHandlerException From Invalid First Name On Contact — added 2026-06-22, assignee: Michael Criswell
- **SALES-9242** (1 pt) — Backfill Total Price and Total Priced Units for Opps Shipped After June 1 with Null Available Date — added 2026-06-23, assignee: Michael Criswell
- **SALES-9232** (1 pt) — CLONE - Security Update: Implement step-up authentication for Salesforce report activities — added 2026-06-22, assignee: Nag Malluru
- **SALES-9233** (1 pt) — CLONE - Cleanup Unused Reports and Dashboards — added 2026-06-22, assignee: Nag Malluru
- **SALES-9197** (1 pt) — SOX SF-CM-01 (Change Management) Control Task — added 2026-06-11, assignee: Navinchandra Gupta
- **SALES-9218** (1 pt) — Backfill of field: Ramp Code on quota object - 1 — added 2026-06-18, assignee: Navinchandra Gupta
- **SALES-9243** (1 pt) — CLONE - Order the necessary software licenses for the ALRA expansion 1 — added 2026-06-23, assignee: Navinchandra Gupta

**Tickets removed (Won't Do):**

- **SALES-9187** (1 pt) — KTLO: ZD tickets 6/11-6/24 — assignee: Jummy Sanni
- **SALES-9188** (0 pt) — zen desk — assignee: Chris Burns
- **SALES-9235** (0 pt) — Investigate why the BatchUpdateContactUserExternalIds is not processing recent records created — assignee: Gustavo Silva

**Story point changes after sprint start:**

- **SALES-9196** — Story points set to 1 on 2026-06-20 by Alex Burton (SU&TC Zendesk bucket)
- **SALES-9208** — Story points set to 1 on 2026-06-16 by Gustavo Silva (OpportunityTriggerHelper bug)

**Pattern:** The majority of mid-sprint additions are reactive: Zendesk bucket tickets (SALES-9190, SALES-9193, SALES-9196), production bugs (SALES-9207, SALES-9208, SALES-9214), and end-of-sprint CLONE tickets for carry-forward work (SALES-9200, SALES-9201, SALES-9232–9234, SALES-9265, SALES-9268, SALES-9269). This reflects legitimate priority shifts (ALRA routing urgency, production incidents) combined with incomplete sprint grooming — many CLONE tickets were created on 6/22–6/24 to capture work already in progress.

### Velocity & Throughput

| Sprint | Completed Points |
|--------|-----------------|
| Sales 5/28 - 6/10 | 86 |
| Sales 5/14 - 5/27 | 100 |
| SALES 4/30 - 5/13 | 85 |
| **Sales 6/11 - 6/24** (current) | **103** |

The current sprint completed **103 points** across 71 tickets. Historical comparison shows the team is maintaining high throughput with a large number of 1-point tickets (Zendesk buckets, quick fixes, clones). No obvious PTO or holiday impact this sprint.

### Burndown Analysis

**Pattern: Late-heavy**

Points closed by day (within sprint window):

| Date | Points Closed |
|------|---------------|
| 2026-06-12 | 3 |
| 2026-06-13 | 1 |
| 2026-06-14 | 1 |
| 2026-06-16 | 10 |
| 2026-06-17 | 12 |
| 2026-06-18 | 7 |
| 2026-06-19 | 2 |
| 2026-06-22 | 14 |
| 2026-06-23 | 24 |
| 2026-06-24 | 26 |

**64 points** (62% of sprint total) closed in the final 3 days (6/22–6/24). Closures accelerated significantly in the last week, with 6/23–6/24 accounting for the bulk of remaining ALRA, routing, and clone ticket completions.

### Bug Analysis

**13 bugs closed (Done status).** Reason for Bug field (`customfield_10142`) was **not populated on any closed bug** — root cause categorization is unavailable.

| Reason for Bug | Count |
|----------------|-------|
| Not populated in Jira | 13 |

Closed bugs: SALES-5940, SALES-8744, SALES-9117, SALES-9149, SALES-9186, SALES-9190, SALES-9193, SALES-9195, SALES-9196, SALES-9207, SALES-9208, SALES-9214, SALES-9241

**Process improvement:** Enforce "Reason for Bug" field completion before moving bugs to Done.

### Related PT/SELLTECH Work

No SELLTECH- tickets were found tied to SRT work this sprint. Three PT project tickets were updated during the sprint window with Salesforce relevance:
- **PT-832** — Data Sync Reliability: Supply, Salesforce and Admin (In Progress)
- **PT-1091** — Voice Capture Within Salesforce (In Progress)
- **PT-1096** — Salesforce User Experience (Not Started)

---

## Per-Engineer Summary

### Alex Burton

**Total points completed: 11**

**Tickets completed:**
- SALES-9126 — Create New ALRA Sales Role -1 (1 pt)
- SALES-9128 — Automatic Set up ALRA to assign the proper Sales software and permissions to the new reps when they are onboarded. -1 (1 pt)
- SALES-9137 — What is our current state for Routing of Leads and Opportunities for new and repeat? -1 (3 pt)
- SALES-9164 — Zoom Upgrade Production (1 pt)
- SALES-9166 — How to automate blocklisting and removal of blocklisting in Zoom (1 pt)
- SALES-9173 — 6/15/26 - 6/22/26 Cohorts (1 pt)
- SALES-9189 — Adjust Sales Role Field on User Record for New Sales Titles (1 pt)
- SALES-9190 — TD: Alex Zendesk Ticket 6/11 - 6/25 (1 pt)
- SALES-9196 — SU&TC: Alex Zendesk Ticket 6/11 - 6/25 (1 pt)

**Tickets carried over:** None

### Jummy Sanni

**Total points completed: 9**

**Tickets completed:**
- SALES-9048 — Outreach Automation: SMS/Phone Automation (2 pt)
- SALES-9076 — Analysis on recurring sumo issues  (2 pt)
- SALES-9187 — KTLO: ZD tickets 6/11-6/24 (1 pt)
- SALES-9200 — CLONE - Tech Debt: ZD tickets 6/11-6/24 (1 pt)
- SALES-9201 — CLONE - SFTW Upgrade: ZD tickets 6/11-6/24 (1 pt)
- SALES-9268 — CLONE - This is an MGO this is an SGO -1 (1 pt)
- SALES-9269 — CLONE - Change the help text/description for Total Retail Price on Opportunity object (1 pt)

**Tickets carried over:** None

### Michael Criswell

**Total points completed: 13**

**Tickets completed:**
- SALES-8541 — Bump classes from API Version 56 to 65 (3 pt)
- SALES-9120 — Backfill AUR_Contributing_Price__c field  (2 pt)
- SALES-9121 — Resolve Row Lock 1/3 : Opportunity/COI (2 pt)
- SALES-9170 — Update the Apex logic to add available date filter for opp Shipped after June 1 (2 pt)
- SALES-9219 — Create Permission Set to Bypass MFA Enforcement for Test Automation Users (1 pt)
- SALES-9234 — CLONE - ZoomSyncPlatformEventTriggerHandler.ZoomSyncPlatformEventTriggerHandlerException From Invalid First Name On Contact (2 pt)
- SALES-9242 — Backfill Total Price and Total Priced Units for Opps Shipped After June 1 with Null Available Date (1 pt)

**Tickets carried over:** None

### Chris Burns

**Total points completed: 9**

**Tickets completed:**
- SALES-9108 — Sync Errors From Coi - Inventory unit not consignable (3 pt)
- SALES-9122 — Resolve Row Lock 2/3 : Opportunity/Lead (2 pt)
- SALES-9138 — MGO high value lead is identified it will be marked as a HV Lead - 1 (2 pt)
- SALES-9161 — Title levels on user record and sales quota records -1 (2 pt)
- SALES-9188 — zen desk (0 pt)

**Tickets carried over:** None

### Grace Saint

**Total points completed: 9**

**Tickets completed:**
- SALES-9123 — Resolve Row Lock 3/3 : Opportunity/Contact (2 pt)
- SALES-9130 — Update the TP capture so that it captures when someone uses zoom from the conversation panel -1 (1 pt)
- SALES-9191 — Real Partners: June 20th Data Export (1 pt)
- SALES-9199 — ALRA Solutioning and Review - 1 (2 pt)
- SALES-9241 — CLONE - Agentforce: Look into prompt errors (1 pt)
- SALES-9265 — CLONE - Update Opportunity Apex Trigger to Capture Scheduled Van Pickups (2 pt)

**Tickets carried over:** None

### Navinchandra Gupta

**Total points completed: 12**

**Tickets completed:**
- SALES-8507 — Upgrade Zoom in Production  to version 2.38 (1 pt)
- SALES-9125 — What user license counts do we have available for the current count need and eoy need for sales reps? -1 (1 pt)
- SALES-9133 — New fields: Ramp Code and Job Profile -1 (2 pt)
- SALES-9141 — For the assignment of the mgos by % what would be involved in assessing the cost benefit of build vs buy -1 or 2 (1 pt)
- SALES-9179 — Salescloud Q2 2026 Manual Remediation (1 pt)
- SALES-9180 — SRT Q3 Capacity Planning  (3 pt)
- SALES-9197 — SOX SF-CM-01 (Change Management) Control Task (1 pt)
- SALES-9218 — Backfill of field: Ramp Code on quota object - 1 (1 pt)
- SALES-9243 — CLONE - Order the necessary software licenses for the ALRA expansion 1 (1 pt)

**Tickets carried over:** None

### Nag Malluru

**Total points completed: 10**

**Tickets completed:**
- SALES-8415 — Create a process to check and implement Release updates in Salesforce (2 pt)
- SALES-9031 — Security Update: Remediate Connected App and API access for VPN/proxy blocking (1 pt)
- SALES-9077 — Technical Design for Outreach Optimization (1 pt)
- SALES-9117 — Reconnect Slack and Salesforce for all the users (1 pt)
- SALES-9169 — ARB Transition Plan (2 pt)
- SALES-9186 — Nag - Zendesk Bucket - S/w Upgrade - 06/11-6/24 (0 pt)
- SALES-9193 — Nag - Zendesk Bucket - KTLO - 06/11-6/24 (1 pt)
- SALES-9195 — Nag - Zendesk Bucket - Tech Debt - 06/11-6/24 (0 pt)
- SALES-9232 — CLONE - Security Update: Implement step-up authentication for Salesforce report activities (1 pt)
- SALES-9233 — CLONE - Cleanup Unused Reports and Dashboards (1 pt)

**Tickets carried over:** None

### Gustavo Silva

**Total points completed: 22**

**Tickets completed:**
- SALES-5940 — Missing User External IDs on Contact - Why is this happening? (1 pt)
- SALES-8549 — Bump Controller classes from API Version 54 to 65 - Ticket 1 of 2 (2 pt)
- SALES-8744 — Duplicate id in list error (2 pt)
- SALES-9149 — Available Data is not being synced from Admin (1 pt)
- SALES-9163 — Can we create manually contact vendors with international addresses and how? (2 pt)
- SALES-9167 — Change Inquiry PE to receive shipping label information and bypass creation inside Salesforce (3 pt)
- SALES-9168 — Update Inquiry PE to receive funnel consignment  qualification responses for reps visibility (5 pt)
- SALES-9178 — [2026-06-10]Force Sync of Consignment Items from Admin to Salesforce (1 pt)
- SALES-9207 — CID 16146775 - New Rolex Item getting added to COI by TRR CRM Service user (1 pt)
- SALES-9208 — OpportunityTriggerHelper.setContactContractComplete | Contact.Contract_Complete__c missing from SOQL (1 pt)
- SALES-9210 — Activate field history on Payment__c object (1 pt)
- SALES-9214 — Vendor Price Update Errors (1 pt)
- SALES-9222 — Optimize how new vendor opportunities are created in SF (1 pt)
- SALES-9231 — Retry oban job of inquiries that failed because of the unknown field error in Production (0 pt)
- SALES-9235 — Investigate why the BatchUpdateContactUserExternalIds is not processing recent records created (0 pt)

**Tickets carried over:** None

### Sai Deepika Kanuri

**Total points completed: 8**

**Tickets completed:**
- SALES-9162 — Evaluate Design for Weighted Routing, Escalation and Lead Scoring -1 (3 pt)
- SALES-9171 — SUMO - Page timeout and Bugsnag Issue  (3 pt)
- SALES-9172 — Backfill NC Credit and refresh COI to calculate the credi (2 pt)

**Tickets carried over:** None

---

## Discussion Prompts

1. **21 tickets were added mid-sprint (+23 points)** — including 6 CLONE tickets created on 6/22–6/24 (SALES-9232, SALES-9233, SALES-9234, SALES-9265, SALES-9268, SALES-9269). Should CLONE tickets be created at sprint planning instead of end-of-sprint to improve visibility?

2. **KTLO consumed 6% of completed points** (target: 16%). Zendesk bucket tickets (SALES-9190, SALES-9193, SALES-9196, SALES-9200, SALES-9201) account for much of this. What can we deflect to self-service or tier-1 support?

3. **All 13 closed bugs have no "Reason for Bug" populated.** Should we block Done transitions on bugs until this field is set? Who owns enforcing this?

4. **62% of points closed in the final 3 days** — is this sustainable, or should we break down larger ALRA spikes (SALES-9137, SALES-9162 at 3 pts each) into smaller deliverables earlier in the sprint?

5. **SALES-9168 (5 pts) was the largest single story completed** — Inquiry PE funnel qualification work landed mid-sprint. Was the 5-point estimate accurate, and should similar cross-team integration stories be flagged earlier in grooming?

---

*Sprint goal (from Jira): ALRA Routing Support, Outreach Tech Design, Sox Tasks, Salesforce Security Phase 2, Commission Backfill*
