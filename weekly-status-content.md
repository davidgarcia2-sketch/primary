# Collection metadata
- Collected: 2026-07-09 (automation cron trigger 2026-07-09T17:40:29Z)
- Movement window: since 2026-07-03 (previous Thursday)
- Prior week reference: Weekly Status Raw Data — 2026-07-01 (PT-869, PT-947, PT-952)
- Jira filter: https://trr-prod.atlassian.net/issues/?filter=15396
- Jira filter items this week: PT-1118, PT-1119 (prior week filter returned PT-869, PT-947, PT-952)
- Jira site: https://trr-prod.atlassian.net
- Notion parent: Thursday Updates
---
# 7. Weekly Project Updates SOP (Casey Gould)
- URL: Weekly Project Updates SOP
- Owner: Casey Gould (Portfolio & Program Management)
- Last fetched: 2026-07-09
## Current process (no changes detected vs prior fetch 2026-07-01)
- Updates due every Thursday; Tech Health updates bi-weekly.
- Required weekly fields: Comments for Status, Status RYG.
- Review fields: Status, Start Date, Due Date.
- Jira sends Project details including Comments for Status to P&T leaders at 4pm Pacific on Thursdays.
- Comments for Status: field (not comment thread); format `[MM/DD]` prefix; remove prior week text each week; up to 400 chars displayed to stakeholders (SOP callout: January 2025).
- Status RYG definitions in SOP: Red/Yellow/Green per SOP.
## Past process changes (documented in SOP)
- June 2024: alternating weeks introduced
- July 2025: Epics → Projects
- August 2025: weekly again
- January 2026: additional fields; Comments for Status to stakeholders
---
# 8. P&T Ways of Working / Key Jira Fields
## P&T Jira Documentation Hub
- URL: P&T Jira Documentation Hub
## Key Jira Fields database
- URL: Key Jira Fields
- Last queried: 2026-07-09
### Field definitions (live query 2026-07-09; no changes detected vs prior fetch 2026-06-25)
**Comments for Status** — Item Types: Project; Field Type: Long Text; Format: `[MM/DD]` prefix; Description: powers stakeholder weekly status display
**Development End Date** — Item Types: Project; Field Type: Date; Description: CAPDEV end date (may differ from Due Date)
**Status RYG** — Item Types: Project; Field Type: Dropdown; Format: Red, Yellow, Green; Red = in flight + critical issue threatening scope/timeline; Yellow = leadership review of blockers/major changes; Green = on track for committed scope and timelines
## P&T Ways of Working page
- URL: Ways of working
- Note: Page content covers Data Engineering sprint ceremonies, not Jira field definitions.
---
# 1–6. JIRA — PT-1119 — SRT - Salesforce Tech Debt
## Project fields
| Field | Value |
|-------|-------|
| Key | PT-1119 |
| Summary | SRT - Salesforce Tech Debt |
| Jira Status | In Progress |
| Status RYG | Green |
| Target end date (Due Date) | 2026-12-31 |
| Development End Date | 2026-06-01 |
| Parent Initiative | PT-811 — Tech Lifecycle & Security — In Progress |
| Labels | 2026Q4, SRT-Domain-Tech-Debt, capitalized-children, squad-SALES |
| Product Manager | Navinchandra Gupta |
| Size | M |
## Comments for Status (full text)
```
[07/01] The Q2 domain tech debt sprint continues with remaining items in active development and ready for deployment, and the Q2 epic closes once those complete. The Q3 tech debt epic kicked off the week of 6/30 with the backlog prepared and work beginning.
```
- Field last updated: 2026-07-01 (project updated 2026-07-01)
## Direct child epics (parent = PT-1119)
| Key | Summary | Status | Epic SP | Due date |
|-----|---------|--------|---------|----------|
| SALES-9039 | [26Q2] SRT: Domain Tech Debt | Done | 20 | 2026-06-30 |
| SALES-9206 | [26Q3] SRT: Domain Tech Debt | In Progress | 92 | 2026-09-30 |
## Child stories/tasks
### SALES-9039 — [26Q2] SRT: Domain Tech Debt
- Parent: PT-1119 | Epic Status: Done | Epic SP: 20 | Due: 2026-06-30
- Child rollup: Open SP=0 | Closed SP=0 | 26 children

| Key | Summary | Status | SP |
|-----|---------|--------|-----|
| SALES-9306 | Nag - Zendesk Bucket - Tech Debt - 06/25-7/8 | Won't Do | null |
| SALES-8392 | Cleanup Unused Reports and Dashboards | Done | null |
| SALES-8843 | Change the help text/description for Total Retail Price on Opportunity object | Done | null |
| SALES-9045 | push_topic.cls not running on mac when finalizing the deploy.sh script | Done | null |
| SALES-9071 | Related Real Partner Not Tagging on New Referral Records | Done | null |
| SALES-9075 | Create SUMO Calendar Knowledge Article Staging | Done | null |
| SALES-9076 | Analysis on recurring sumo issues  | Done | null |
| SALES-9078 | Review and Rationalization of Salesforce Distribution Lists | Done | null |
| SALES-9105 | Alex Zendesk Ticket 5/28 - 6/10 | Done | null |
| SALES-9124 | Migrate sfConvertLeadSumoCal.test.js to use new createSGOLead method | Done | null |
| SALES-9163 | Can we create manually contact vendors with international addresses and how? | Done | null |
| SALES-9175 | CLONE - Create SUMO Calendar Knowledge Article | Done | null |
| SALES-9189 | Adjust Sales Role Field on User Record for New Sales Titles | Done | null |
| SALES-9190 | TD: Alex Zendesk Ticket 6/11 - 6/25 | Done | null |
| SALES-9195 | Nag - Zendesk Bucket - Tech Debt - 06/11-6/24 | Done | null |
| SALES-9200 | CLONE - Tech Debt: ZD tickets 6/11-6/24 | Done | null |
| SALES-9201 | CLONE - SFTW Upgrade: ZD tickets 6/11-6/24 | Done | null |
| SALES-9210 | Activate field history on Payment__c object | Done | null |
| SALES-9222 | Optimize how new vendor opportunities are created in SF | Done | null |
| SALES-9231 | Retry oban job of inquiries that failed because of the unknown field error in Production | Done | null |
| SALES-9236 | LeadConvertProcessor.processLeadAddresses exceptions being notified by email | Done | null |
| SALES-9269 | CLONE - Change the help text/description for Total Retail Price on Opportunity object | Done | null |
| SALES-9315 | DevQA: SALES-9236 LeadConvertProcessor.processLeadAddresses exceptions being notified by e | Done | null |
| SALES-9329 | Backfill the COIs that are missing Available_Date__c  | Done | null |
| SALES-9384 | DevQA: SALES-9075 Create SUMO Calendar Knowledge Article | Done | null |
| SELLTECH-799 | Make SF PEs agnostic to the extra data being passed by Supply | Done | null |

### SALES-9206 — [26Q3] SRT: Domain Tech Debt
- Parent: PT-1119 | Epic Status: In Progress | Epic SP: 92 | Due: 2026-09-30
- Child rollup: Open SP=2 | Closed SP=1 | 76 children

| Key | Summary | Status | SP |
|-----|---------|--------|-----|
| SALES-7254 | Update the label names on the lead button so it is consistent across the lwc and the lead  | Done | 1 |
| SALES-8850 | Data Parity: Contact's Last Consignment Date field | Done | null |
| SALES-9228 | Fix the consignor contacts that don't have a user_external_id__c in the last 90 days | Done | null |
| SALES-9272 | TD: Alex Zendesk Ticket 6/25 - 7/8 | Done | null |
| SALES-9283 | DevQA: SALES-7254 Update the label names on the lead button so it is consistent across the | Done | null |
| SALES-9357 | Helped Developing SELL-4934 | Done | null |
| SELLTECH-636 | Salesforce / Deprecate old funnel memory feature | Done | null |
| SELLTECH-1054 | DevQA: SELLTECH-636 Salesforce / Deprecate old funnel memory feature | Done | null |
| SALES-9381 | Helped Developing SELL-4934 | Code Review | null |
| SALES-9397 | Enable Quick Create option for Vendor users | In Progress | null |
| SALES-5993 | Contact was created in Salesforce to be given certain opportunities "TheRealReal1 Real Rea | To Do | null |
| SALES-6015 | To convert a lead as an admin you have to login as a vendor user - this is to give admins  | To Do | null |
| SALES-6058 | Update Zip codes quarterly | To Do | null |
| SALES-6747 | Dropbox Signature Request Template Name Error | To Do | null |
| SALES-7759 | Address issue when client is self-booking an at home from CLP. | To Do | null |
| SALES-8393 | Persona based entitlement framework for Internal Data access for our users | To Do | null |
| SALES-8396 | Establish security oriented development practices across the enterprise | To Do | null |
| SALES-8398 | Conduct code review to ascertain the presence of unknown vunerabilities | To Do | null |
| SALES-8402 | Ensure Secure and Governed User Access Changes with Executive Approval | To Do | null |
| SALES-8403 | Create Elevated Analyst Profile to Minimize Full Admin Access | To Do | null |
| SALES-8404 | Clean Up and Standardize Roles, Profiles, and Permission Sets | To Do | null |
| SALES-8405 | Automate Deactivation of Inactive Users After 90 Days | To Do | null |
| SALES-8406 | Implement Monitoring for Admin and Privileged User Actions | To Do | null |
| SALES-8407 | Maintain SSO Requirement for Salesforce users | To Do | null |
| SALES-8408 | Establish baseline Session Settings requirements for all Orgs | To Do | null |
| SALES-8409 | Establish baseline Password Settings for all Orgs | To Do | null |
| SALES-8410 | Establish baseline Authentication protocols for System and Integration users | To Do | null |
| SALES-8412 | Implement Biometric Secure Login | To Do | null |
| SALES-8413 | Salesforce Org Health Optimization | To Do | null |
| SALES-8416 | Create a process to have a security audit for Salesforce and all the managed packaged | To Do | null |
| SALES-8542 | Bump classes from API Version 57 to 65 | To Do | null |
| SALES-8543 | Bump classes from API Version 58 to 65 | To Do | null |
| SALES-8544 | Bump classes from API Version 61 to 65 | To Do | null |
| SALES-8545 | Bump classes from API Version 62 to 65 | To Do | null |
| SALES-8546 | Bump classes from API Version 63 to 65 | To Do | null |
| SALES-8547 | Bump classes from API Version 64 to 65 | To Do | null |
| SALES-8554 | Bump Handler and Helper classes from API Version 54 to 65 - Ticket 1 of 2 | To Do | null |
| SALES-8555 | Bump Handler and Helper classes from API Version 54 to 65 - Ticket 2 of 2 | To Do | null |
| SALES-8556 | Bump Client and Service classes from API Version 54 to 65 | To Do | null |
| SALES-8557 | Bump rest of the classes from API Version 54 to 65 - Ticket 1 of 4 | To Do | null |
| SALES-8558 | Bump rest of the classes from API Version 54 to 65 - Ticket 2 of 4 | To Do | null |
| SALES-8559 | Bump rest of the classes from API Version 54 to 65 - Ticket 3 of 4 | To Do | null |
| SALES-8560 | Bump rest of the classes from API Version 54 to 65 - Ticket 4 of 4 | To Do | null |
| SALES-8561 | Bump classes from API Version 59 to 65 - Ticket 1 of 2 | To Do | null |
| SALES-8562 | Bump classes from API Version 59 to 65 - Ticket 2 of 2 | To Do | null |
| SALES-8937 | Investigate how many duplicate opportunities are being created by contact | To Do | null |
| SALES-9194 | Determine What Automation Updates Are Needed for Sales Role Value Updates | To Do | null |
| SALES-9250 | Fix sfAssignToMeQuickCreate.test.js | To Do | null |
| SALES-9251 | Fix sfDeleteLead.test.js | To Do | null |
| SALES-9252 | Fix sfDupLeadMatchedContact.test.js | To Do | null |
| SALES-9253 | Fix sfEditLead.test.js | To Do | null |
| SALES-9254 | Fix sfMergeLead.test.js | To Do | null |
| SALES-9255 | Fix sfConvertLeadToContact.test.js | To Do | null |
| SALES-9256 | Fix sfCloneOpportunity.test.js | To Do | null |
| SALES-9257 | Fix sfNPLFlow.test.js | To Do | null |
| SALES-9258 | Fix sfQuickCreateDropOff.test.js | To Do | null |
| SALES-9259 | Fix sfQuickCreate.test.js | To Do | null |
| SALES-9260 | Fix sfQuickCreateLCO.test.js | To Do | null |
| SALES-9261 | Fix sfEditContactAddress.test.js | To Do | null |
| SALES-9262 | Fix sfQuickCreateExistingUser.test.js | To Do | null |
| SALES-9276 | TD: Alex Zendesk Ticket 7/9/26 7/22/26 | To Do | null |
| SALES-9280 | TD: Alex Zendesk Ticket 7/23/26 - 8/5/26 | To Do | null |
| SALES-9322 | Add Account Owner Email field in the Salesforce Report | To Do | null |
| SALES-9325 | Why can BDRs book an appt in lead status without all of the consignor info? | To Do | null |
| SALES-9326 | Why can a Consignor self schedule if they are a previously unconverted contacts? | To Do | null |
| SALES-9327 | Buyers not consignors accidentally hit reconsign button and it creates multiple opps that  | To Do | null |
| SALES-9328 | Requesting a shipping label at checkout creates multiple opps that go to multiple users | To Do | null |
| SALES-9331 | Clean up unused Profiles, Permission Sets, and Permission Set Groups in Salesforce | To Do | null |
| SALES-9333 | [Story] Cleanup unused Profiles, PS, and PSG — sandbox through production (Weeks 3–5+) | To Do | null |
| SALES-9334 | [Spike] Optimize Salesforce storage for COI and Comp Calculations objects | To Do | null |
| SALES-9369 | DevQA: SALES-6747 Dropbox Signature Request Template Name Error | To Do | null |
| SALES-9379 | DevQA: SALES-9333 [Story] Cleanup unused Profiles, PS, and PSG — sandbox through productio | To Do | null |
| SALES-9383 | Multi Calendar Issue: Opp not linking to appt record  | To Do | null |
| SALES-9394 | ZD Tickets 7/9-7/22: KTLO | To Do | 1 |
| SALES-9395 | CLONE - ZD Tickets 7/9-7/22: Domain Tech Debt | To Do | 1 |
| SELLTECH-501 | Change scratchOrg hack to retry more than one time when installing managed packages | To Do | null |

## Blocked / At Risk / overdue (project tree)
- Blocked: SALES-8960 (under SALES-9205/PT-1118 tree, reparented from Q2); none directly under PT-1119 epics
- At Risk labels: none found
- Overdue (duedate < 2026-07-09, not Done/Won't Do): none open
## Net new movement since 2026-07-03
| Key | Updated | Event | Detail |
|-----|---------|-------|--------|
| PT-1119 | — | — | No project-level updates since 2026-07-03 |
| SALES-9039 | 2026-07-09 | In Progress → Done | Q2 domain tech debt epic closed |
| SALES-9041 | 2026-07-09 | In Progress → Done | Q2 compliance epic closed (child of PT-1118) |
| SALES-8850 | 2026-07-09 | — | Data Parity: Contact's Last Consignment Date field — Done |
| SALES-8392 | 2026-07-07 | — | Cleanup Unused Reports and Dashboards — Done |
| SALES-9381 | 2026-07-09 | created | Helped Developing SELL-4934 — Code Review |
| SALES-9397 | 2026-07-09 | created | Enable Quick Create option for Vendor users — In Progress |
| SALES-9394 | 2026-07-09 | created | ZD Tickets 7/9-7/22: KTLO — To Do |
| SALES-9395 | 2026-07-09 | created | CLONE - ZD Tickets 7/9-7/22: Domain Tech Debt — To Do |
| SALES-9383 | 2026-07-08 | created | Multi Calendar Issue: Opp not linking to appt record — To Do |
| SALES-9325 | 2026-07-07 | created/updated | Why can BDRs book an appt in lead status without all of the consignor info? — To Do |
| SALES-9326 | 2026-07-07 | created/updated | Why can a Consignor self schedule if they are a previously unconverted contacts? — To Do |
| SALES-9327 | 2026-07-07 | created/updated | Buyers not consignors accidentally hit reconsign button — To Do |
| SALES-9328 | 2026-07-07 | created/updated | Requesting a shipping label at checkout creates multiple opps — To Do |
| (tree) | — | — | 53 total issues updated since 2026-07-03 |
---
# 1–6. JIRA — PT-1118 — SRT - Software Upgrades & Technical Compliance
## Project fields
| Field | Value |
|-------|-------|
| Key | PT-1118 |
| Summary | SRT - Software Upgrades & Technical Compliance |
| Jira Status | In Progress |
| Status RYG | Green |
| Target end date (Due Date) | 2026-11-30 |
| Development End Date | 2026-05-01 |
| Parent Initiative | PT-811 — Tech Lifecycle & Security — In Progress |
| Labels | 2026H2, 2026Q4, SRT-Software-Upgrades, capitalized-children, squad-SALES |
| Product Manager | David Garcia |
## Comments for Status (full text)
```
[07/01] The Q2 compliance sprint is wrapping active development on the SailPoint OAuth migration and Zoom upgrade, and the Q2 epic closes once those items complete. The Q3 compliance epic kicked off the week of 6/30 with scope already in place and active development beginning.
```
- Field last updated: 2026-07-01 (project updated 2026-07-01)
## Direct child epics (parent = PT-1118)
| Key | Summary | Status | Epic SP | Due date |
|-----|---------|--------|---------|----------|
| SALES-9021 | Salesforce Summer '26 Release Coordination | Done | 20 | 2026-06-30 |
| SALES-9041 | [26Q2] SRT: Software Upgrades and Technical Compliance Epic | Done | 20 | 2026-07-09 |
| SALES-9205 | [26Q3] SRT: Software Upgrades and Technical Compliance Epic | In Progress | 18 | 2026-09-30 |
## Child stories/tasks
### SALES-9021 — Salesforce Summer '26 Release Coordination
- Parent: PT-1118 | Epic Status: Done | Epic SP: 20 | Due: 2026-06-30
- Child rollup: Open SP=0 | Closed SP=0 | 26 children

| Key | Summary | Status | SP |
|-----|---------|--------|-----|
| SALES-8956 | Releases: Salesforce-Managed X (Formerly Twitter) Authentication Provider Retirement | Won't Do | null |
| SALES-8959 | Releases: Sort Apex Batch Action Results by Request Order | Won't Do | null |
| SALES-8987 | Summer 26 Release / Lead Conversion Self Gen Referrals | Won't Do | null |
| SALES-8991 | Summer 26 Release / As a sales rep create a self-generated referral and convert it to an o | Won't Do | null |
| SALES-8992 | Summer 26 Release / VO Doc Process | Won't Do | null |
| SALES-8994 | Summer 26 Release / Zoom | Won't Do | null |
| SALES-8995 | Summer 26 Release / Address Validation | Won't Do | null |
| SALES-8996 | Summer 26 Release / HelloSign | Won't Do | null |
| SALES-8998 | Summer 26 Release / SUMO QA- Book SGO Retail Appt | Won't Do | null |
| SALES-9000 | Summer 26 Release / SUMO and Commissions Quick test | Won't Do | null |
| SALES-8955 | Releases: Enable Accessibility Enhancements for Date Pickers, Popovers, Bottom Utility Bar | Done | null |
| SALES-8957 | Releases: Use Visualforce PDF Rendering Service with Apex Blob.toPdf() | Done | null |
| SALES-8958 | Releases: Enable Accessibility Enhancements for Page Headers and Modal Windows When Zoom I | Done | null |
| SALES-8980 | Summer 26 Release / Zoom, Address Validation, Lead Assignment, Lead Conversion | Done | null |
| SALES-8981 | Summer 26 Release/ Real Partners | Done | null |
| SALES-8982 | Summer 26 Release / SF - Admin Sync | Done | null |
| SALES-8983 | Summer 26 Release / Shipping Happy Path | Done | null |
| SALES-8984 | Summer 26 Release / Vendor Bulk Upload | Done | null |
| SALES-8985 | Summer 26 Release - Funnel testing in staging after the css fix | Done | null |
| SALES-8986 | Summer 26 Release / Add Item | Done | null |
| SALES-8988 | Summer 26 Release / VO Doc Test | Done | null |
| SALES-8989 | Summer 26 Release / SUMO Scheduling on Lead | Done | null |
| SALES-8990 | Summer 26 Release / Commissions | Done | null |
| SALES-8993 | Summer 26 Release / Slack - HelloSign | Done | null |
| SALES-8997 | Summer 26 Release / SUMO Scheduling on CLP and Cancelling | Done | null |
| SALES-8999 | Summer 26 Release / SUMO Scheduling, Update & Cancel on Opp | Done | null |

### SALES-9041 — [26Q2] SRT: Software Upgrades and Technical Compliance Epic
- Parent: PT-1118 | Epic Status: Done | Epic SP: 20 | Due: 2026-07-09
- Child rollup: Open SP=0 | Closed SP=0 | 27 children

| Key | Summary | Status | SP |
|-----|---------|--------|-----|
| SALES-9308 | Nag - Zendesk - S/w Upgrades - 06/25 - 7/8 | Won't Do | null |
| SALES-9323 | DevQA: SALES-9319 Change COI PE to search records by crm_id or slug | Won't Do | null |
| SELLTECH-578 | ICU Locale not enabled  due to the API version below 45 used in the org[Managed Packages] | Won't Do | null |
| SALES-8507 | Upgrade Zoom in Production  to version 2.38 | Done | null |
| SALES-9029 | Security Update: Verify all Salesforce email-sending domains (Phase 1) | Done | null |
| SALES-9030 | Security Update: Prepare allowlisted email domains for Phase 2 verification | Done | null |
| SALES-9031 | Security Update: Remediate Connected App and API access for VPN/proxy blocking | Done | null |
| SALES-9035 | Security Update: Implement step-up authentication for Salesforce report activities | Done | null |
| SALES-9064 | bump GitHub Actions pins for Node 20 deprecation on setup-sfdx action | Done | null |
| SALES-9070 | CLONE - Summer 26 Release / Vendor Bulk Upload | Done | null |
| SALES-9072 | Deployer Access for Salesforce-CRM Repo - May 2026 | Done | null |
| SALES-9083 | Add a realreal.com Authorized Email Domain in Production | Done | null |
| SALES-9119 | Change deploy-to-staging skill to be able to deploy to any sandbox | Done | null |
| SALES-9145 | Remove Data Mask package | Done | null |
| SALES-9164 | Zoom Upgrade Production | Done | null |
| SALES-9165 | Hellosign contract Signature is not displaying properly on iPad | Done | null |
| SALES-9169 | ARB Transition Plan | Done | null |
| SALES-9179 | Salescloud Q2 2026 Manual Remediation | Done | null |
| SALES-9180 | SRT Q3 Capacity Planning  | Done | null |
| SALES-9186 | Nag - Zendesk Bucket - S/w Upgrade - 06/11-6/24 | Done | null |
| SALES-9196 | SU&TC: Alex Zendesk Ticket 6/11 - 6/25 | Done | null |
| SALES-9197 | SOX SF-CM-01 (Change Management) Control Task | Done | null |
| SALES-9227 | CLONE - Update Sailpoint Connect from Basic Auth to OAuth connection | Done | null |
| SALES-9232 | CLONE - Security Update: Implement step-up authentication for Salesforce report activities | Done | null |
| SALES-9310 | Assign Records to Inactive User permission set assignment to Gustavo Silva | Done | null |
| SALES-9319 | Change COI PE to search records by crm_id or slug | Done | null |
| SALES-9321 | Manage Public List Views Access in Salesforce Staging and Production | Done | null |

### SALES-9205 — [26Q3] SRT: Software Upgrades and Technical Compliance Epic
- Parent: PT-1118 | Epic Status: In Progress | Epic SP: 18 | Due: 2026-09-30
- Child rollup: Open SP=0 | Closed SP=0 | 31 children

| Key | Summary | Status | SP |
|-----|---------|--------|-----|
| SALES-9033 | Security Update: Enforce phishing-resistant MFA for privileged users (including admins) | Won't Do | null |
| SALES-9037 | Security Update: Adopt Transaction Security policy enhancements | Won't Do | null |
| SALES-9286 | DevQA: SALES-9033 Security Update: Enforce phishing-resistant MFA for privileged users (in | Won't Do | null |
| SALES-9288 | DevQA: SALES-9037 Security Update: Adopt Transaction Security policy enhancements | Won't Do | null |
| SALES-9032 | Security Update: Review extended login anomaly detection and containment impact | Done | null |
| SALES-9036 | Security Update: Prepare step-up authentication for anomalous report export | Done | null |
| SALES-9038 | Security Update: Communicate June 2026 Salesforce security changes to end users | Done | null |
| SALES-9287 | DevQA: SALES-9035 Security Update: Implement step-up authentication for Salesforce report  | Done | null |
| SALES-9324 | DevQA: SALES-9319 Change COI PE to search records by crm_id or slug | Done | null |
| SALES-9338 | DevQA: SALES-9036 Security Update: Prepare step-up authentication for anomalous report exp | Done | null |
| SALES-9358 | CLONE - Agentforce Co-worker Introduction and Features | Done | null |
| SALES-9359 | CLONE - Figma Diagram for ZD process | Done | null |
| SALES-9380 | CLONE - Report Export > 10k rows is taking the users to classic version | Done | null |
| SALES-9386 | CLONE - SUMO Page loadtime improvements configuration | Done | null |
| SALES-8960 | Update Sailpoint Connect from Basic Auth to OAuth connection | Blocked | null |
| SALES-9239 | SUMO Page loadtime improvements configuration | Blocked | null |
| SALES-9229 | Agentforce Co-worker Introduction and Features | In Progress | null |
| SALES-9238 | Figma Diagram for ZD process | In Progress | null |
| SALES-9342 | Report Export > 10k rows is taking the users to classic version | In Progress | null |
| SALES-8414 | User training for Admin and Non Admin Salesforce | To Do | null |
| SALES-9034 | Security Update: Enforce MFA for all employee Salesforce users | To Do | null |
| SALES-9107 | Change SF Shipping Label button to generate as many shipping labels as number of boxes spe | To Do | null |
| SALES-9143 | Software license management, management & auditing | To Do | null |
| SALES-9277 | SU&TC: Alex Zendesk Ticket 7/9/26 - 7/22/26 | To Do | null |
| SALES-9281 | SU&TC: Alex Zendesk Ticket 7/23/26 8/5/26 | To Do | null |
| SALES-9285 | DevQA: SALES-9032 Security Update: Review extended login anomaly detection and containment | To Do | null |
| SALES-9302 | DevQA: SALES-9239 SUMO Page loadtime improvements configuration | To Do | null |
| SALES-9330 | Revoke the Installer Permission set for Bryan | To Do | null |
| SALES-9335 | Determine additional storage capacity required to enable Einstein Activity Capture (EAC) a | To Do | null |
| SALES-9340 | [SF RU] Enable Profile Filtering — assess, test & activate | To Do | null |
| SALES-9366 | DevQA: SALES-9034 Security Update: Enforce MFA for all employee Salesforce users | To Do | null |

## Blocked / At Risk / overdue (project tree)
- Blocked: SALES-8960 — Update Sailpoint Connect from Basic Auth to OAuth connection (parent SALES-9205); SALES-9239 — SUMO Page loadtime improvements configuration (parent SALES-9205)
- At Risk labels: none found
- Overdue (duedate < 2026-07-09, not Done/Won't Do): none open
## Net new movement since 2026-07-03
| Key | Updated | Event | Detail |
|-----|---------|-------|--------|
| PT-1118 | — | — | No project-level updates since 2026-07-03 |
| SALES-9041 | 2026-07-09 | → Done | Q2 compliance epic closed |
| SALES-8960 | 2026-07-09 | — | Blocked (status unchanged) |
| SALES-9239 | 2026-07-08 | — | Blocked (status unchanged) |
| SALES-9386 | 2026-07-08 | → Done | CLONE - SUMO Page loadtime improvements configuration |
| SALES-9075 | 2026-07-08 | → Done | Create SUMO Calendar Knowledge Article Staging |
| SALES-9342 | 2026-07-07 | — | Report Export > 10k rows — In Progress |
| SALES-9229 | 2026-07-07 | — | Agentforce Co-worker Introduction and Features — In Progress |
| SALES-9238 | 2026-07-07 | — | Figma Diagram for ZD process — In Progress |
| SALES-9358 | 2026-07-07 | → Done | CLONE - Agentforce Co-worker Introduction and Features |
| SALES-9359 | 2026-07-07 | → Done | CLONE - Figma Diagram for ZD process |
| SALES-9380 | 2026-07-07 | → Done | CLONE - Report Export > 10k rows |
| SALES-9036 | 2026-07-07 | → Done | Security Update: Prepare step-up authentication for anomalous report export |
---
# 9–10. SLACK
## Search: PT-1118 OR PT-1119 OR SALES-9039 OR SALES-9206 OR SALES-9041 OR SALES-9205 (after 2026-07-03)
- No direct mentions of PT-1118, PT-1119, or epic keys found in Slack search.
## Search: from:Casey Gould (weekly update OR project update OR Thursday update) (after 2026-07-03)
- No results.
## Search: from:Bryan Claggett (weekly update OR project update OR Thursday update) (after 2026-07-03)
- No results.
## #srt_squadleads — messages since 2026-07-03
- No messages since 2026-07-03.
## #seller-salestech — messages since 2026-07-03
### 2026-07-09 — Devon Novotnak
> @Navinchandra Gupta @David Garcia @Gustavo Silva
>
> We're seeing really low drops in Consignment Kits -> MGOs
>
> Can we look on the SF side this morning to ensure that consignment kit inquiries are routing to SF and within SF properly?
>
> This would be since about June 12th
### 2026-07-09 — Gustavo Silva (reply)
> @Devon Novotnak checking supply in BQ, seems like the last inquiry with leadsource = 'consignment_kit' was created on 2026-07-09 and that matches what we have in Salesforce
### 2026-07-09 — Devon Novotnak (reply)
> @David Garcia report here too — this is just basic but you can drill down - you can see the sharp drop in June — https://therealreal.looker.com/explore/trr_analytics/supply_opportunities?qid=xF6IfF7G3tj6XmTZoPpplx&origin_space=58&toggle=pik
### 2026-07-09 — David Garcia (reply)
> We sure will thanks Devon. What leads you to believe they're unusually low? Is there a report you use to check on these?
### 2026-07-07 — Devon Novotnak
> Hey Crew - Any insight here?
> Forwarded message from Samantha Selario: hey team! one of our bdr reps says they are not receiving any pq or ss since 7/1 her name is Alyssa Estrada, is someone able to assist?
### 2026-07-06 — Grace Saint
> hi good afternoon! as part of a new project we are creating 2 new category__c records in salesforce. External_ID__c is a required field on that object. can someone tell me what the 2 new external id's should be? guessing it should be 12 and 13 but wanted to confirm
## Group DM (Gustavo Silva, Matias Morales, Diego Watanabe, David Garcia) — 2026-07-09
### Gustavo Silva
> I might need to do a change on our side to support this. The quick create option is not visible for vendors. @David Garcia
> Ticket: https://trr-prod.atlassian.net/browse/SALES-9397
### David Garcia
> @Gustavo Silva let me know what change you're thinking. and if it includes enhancing someone access, let's make sure we get approval from their supervisor in a ticket documented.
---
# Data gaps / query notes
- Jira filter 15396 now returns PT-1118, PT-1119 (prior week returned PT-869, PT-947, PT-952).
- Comments for Status on PT-1118 and PT-1119 not updated since 2026-07-01 (today is 2026-07-09).
- Story points on Story/Bug/Spike children predominantly null (customfield_10016); epic-level SP on parent epics.
- Key Jira Fields database row query succeeded 2026-07-09; no field definition updates detected vs prior fetch 2026-06-25.
- SALES-8960 (SailPoint OAuth) and SALES-9239 (SUMO page loadtime) remain Blocked under SALES-9205.
- Q2 epics SALES-9039 and SALES-9041 marked Done on 2026-07-09.
- #srt_squadleads: no messages since 2026-07-03.
