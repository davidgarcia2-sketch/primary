# Collection metadata
- Collected: 2026-08-13 (automation cron trigger 2026-08-13T14:02:32Z)
- Movement window: since 2026-08-06 (previous Thursday)
- Prior week reference: Weekly Status Raw Data — 2026-08-06 (PT-1118, PT-1119)
- Jira filter: https://trr-prod.atlassian.net/issues/?filter=15396
- Jira filter items (live query): PT-1118, PT-1119
- Jira site: https://trr-prod.atlassian.net
- Total child issues under project epics (live count): 270
- Notion parent: Thursday Updates
---
# 7. Weekly Project Updates SOP (Casey Gould)
- URL: https://www.notion.so/therealreal/Weekly-Project-Updates-6c79210f3b5a48d1baa741adbe427196
- Owner: Casey Gould (Portfolio & Program Management)
- Last fetched: 2026-08-13
## Current process (no changes detected vs prior fetch 2026-08-06)
- Updates due every Thursday; Tech Health updates bi-weekly.
- Required weekly fields: Comments for Status, Status RYG.
- Review fields: Status, Start Date, Due Date.
- Jira sends Project details including Comments for Status to P&T leaders at 4pm Pacific on Thursdays.
- Comments for Status: field (not comment thread); format `[MM/DD]` prefix; remove prior week text each week; up to 400 chars displayed to stakeholders (SOP callout: January 2025).
## Past process changes (documented in SOP)
- June 2024: alternating weeks introduced
- July 2025: Epics → Projects
- August 2025: weekly again
- January 2026: additional fields; Comments for Status to stakeholders
---
# 8. P&T Ways of Working / Key Jira Fields
## P&T Jira Documentation Hub
- URL: https://www.notion.so/therealreal/P-T-Jira-Documentation-Hub-a57807556cec43739274facb32527e29
## Way of Working (2025 edition)
- URL: https://www.notion.so/therealreal/Way-of-Working-2025-edition-232d553c3a2e80f99946e456e35ebc18
- Last fetched: 2026-08-13
- Verification status: expired
- No field definition updates detected vs prior fetch 2026-08-06
## Key Jira Fields database
- URL: https://www.notion.so/therealreal/Key-Jira-Fields-296d553c3a2e8090b7d0d48ae9ab3238
- Last queried: 2026-08-13
### Field definitions (live fetch 2026-08-13; no changes detected vs prior fetch 2026-08-06)
**Comments for Status** — Item Types: Project; Field Type: Long Text; Format: `[MM/DD]` prefix; Description: powers stakeholder weekly status display
**Development End Date** — Item Types: Project; Field Type: Date; Description: CAPDEV end date (may differ from Due Date)
**Status RYG** — Item Types: Project; Field Type: Dropdown; Format: Red, Yellow, Green; Red = in flight + critical issue threatening scope/timeline; Yellow = leadership review of blockers/major changes; Green = on track for committed scope and timelines
**OKR Summary** — Item Types: Initiative, Project; Field Type: Short Text; Format: Max 200 characters
**Primary KPI** — Item Types: Initiative, Project; Field Type: Short Text; Format: +# KPI
**Financial Impact** — Item Types: Initiative, Project, Epic; Field Type: Short Text; Format: $ #M Unit
---
# 1–6. JIRA — PT-1119 — SRT - Salesforce Tech Debt
## Project fields (live 2026-08-13)
| Field | Value |
| --- | --- |
| Key | PT-1119 |
| Summary | SRT - Salesforce Tech Debt |
| Jira Status | In Progress |
| Status RYG | Green |
| Target end date (Due Date) | 2026-12-31 |
| Start Date | 2026-06-01 |
| Assignee | Navinchandra Gupta |
| Last updated | 2026-08-06T08:43:04.845-0700 |
## Comments for Status (full text)
```
[08/06] The storage optimization spike was completed during the week of 8/3, and new tickets for orphan comp calcs, merging comp calcs with COI, and zipcode discovery are being prepared. The multi calendar issue is in progress, with a resolution being prepared for the upcoming sprint.
```
## Direct child epics
| Key | Summary | Status | Epic SP | Due date | Child open SP | Child closed SP | Child count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SALES-9039 | [26Q2] SRT: Domain Tech Debt | Done | 20 | 2026-06-30 | 0 | 32 | 26 |
| SALES-9206 | [26Q3] SRT: Domain Tech Debt | In Progress | 92 | 2026-09-30 | 106 | 105 | 129 |
### Child stories — SALES-9039 (26 issues)
| Key | Summary | Status | SP |
| --- | --- | --- | --- |
| SALES-8392 | Cleanup Unused Reports and Dashboards | Done | 1 |
| SALES-8843 | Change the help text/description for Total Retail Price on Opportunity object | Done | 1 |
| SALES-9045 | push_topic.cls not running on mac when finalizing the deploy.sh script | Done | 1 |
| SALES-9071 | Related Real Partner Not Tagging on New Referral Records | Done | 1 |
| SALES-9075 | Create SUMO Calendar Knowledge Article Staging | Done | 3 |
| SALES-9076 | Analysis on recurring sumo issues  | Done | 2 |
| SALES-9078 | Review and Rationalization of Salesforce Distribution Lists | Done | 2 |
| SALES-9105 | Alex Zendesk Ticket 5/28 - 6/10 | Done | 2 |
| SALES-9124 | Migrate sfConvertLeadSumoCal.test.js to use new createSGOLead method | Done | 3 |
| SALES-9163 | Can we create manually contact vendors with international addresses and how? | Done | 2 |
| SALES-9175 | CLONE - Create SUMO Calendar Knowledge Article | Done | 1 |
| SALES-9189 | Adjust Sales Role Field on User Record for New Sales Titles | Done | 1 |
| SALES-9190 | TD: Alex Zendesk Ticket 6/11 - 6/25 | Done | 1 |
| SALES-9195 | Nag - Zendesk Bucket - Tech Debt - 06/11-6/24 | Done | 0 |
| SALES-9200 | CLONE - Tech Debt: ZD tickets 6/11-6/24 | Done | 1 |
| SALES-9201 | CLONE - SFTW Upgrade: ZD tickets 6/11-6/24 | Done | 1 |
| SALES-9210 | Activate field history on Payment__c object | Done | 1 |
| SALES-9222 | Optimize how new vendor opportunities are created in SF | Done | 1 |
| SALES-9231 | Retry oban job of inquiries that failed because of the unknown field error in Production | Done | 1 |
| SALES-9236 | LeadConvertProcessor.processLeadAddresses exceptions being notified by email | Done | 1 |
| SALES-9269 | CLONE - Change the help text/description for Total Retail Price on Opportunity object | Done | 1 |
| SALES-9306 | Nag - Zendesk Bucket - Tech Debt - 06/25-7/8 | Won't Do | 0 |
| SALES-9315 | DevQA: SALES-9236 LeadConvertProcessor.processLeadAddresses exceptions being notified by email | Done | 1 |
| SALES-9329 | Backfill the COIs that are missing Available_Date__c  | Done | 1 |
| SALES-9384 | DevQA: SALES-9075 Create SUMO Calendar Knowledge Article | Done | 1 |
| SELLTECH-799 | Make SF PEs agnostic to the extra data being passed by Supply | Done | 1 |
### Child stories — SALES-9206 (129 issues)
| Key | Summary | Status | SP |
| --- | --- | --- | --- |
| SALES-5993 | Contact was created in Salesforce to be given certain opportunities "TheRealReal1 Real Real * $$ | Won't Do | 0 |
| SALES-6015 | To convert a lead as an admin you have to login as a vendor user - this is to give admins access to convert leads for... | Won't Do | 0 |
| SALES-6058 | Update Zip codes quarterly | Done | 3 |
| SALES-6747 | Dropbox Signature Request Template Name Error | Done | 1 |
| SALES-7254 | Update the label names on the lead button so it is consistent across the lwc and the lead page. | Done | 1 |
| SALES-7759 | Address issue when client is self-booking an at home from CLP. | To Do | 1 |
| SALES-8393 | Persona based entitlement framework for Internal Data access for our users | To Do | 5 |
| SALES-8396 | Establish security oriented development practices across the enterprise | Won't Do | 3 |
| SALES-8398 | Conduct code review to ascertain the presence of unknown vunerabilities | To Do | 5 |
| SALES-8402 | Ensure Secure and Governed User Access Changes with Executive Approval | To Do | 2 |
| SALES-8403 | Create Elevated Analyst Profile to Minimize Full Admin Access | To Do | 4 |
| SALES-8404 | Clean Up and Standardize Roles, Profiles, and Permission Sets | Won't Do | 5 |
| SALES-8405 | Automate Deactivation of Inactive Users After 90 Days | To Do | 2 |
| SALES-8406 | Implement Monitoring for Admin and Privileged User Actions | To Do | 5 |
| SALES-8407 | Maintain SSO Requirement for Salesforce users | Won't Do | 2 |
| SALES-8408 | Establish baseline Session Settings requirements for all Orgs | To Do | 0 |
| SALES-8409 | Establish baseline Password Settings for all Orgs | To Do | 0 |
| SALES-8410 | Establish baseline Authentication protocols for System and Integration users | To Do | 1 |
| SALES-8412 | Implement Biometric Secure Login | To Do | 2 |
| SALES-8413 | Salesforce Org Health Optimization | To Do | 0 |
| SALES-8416 | Create a process to have a security audit for Salesforce and all the managed packaged | To Do | 0 |
| SALES-8542 | Bump classes from API Version 57 to 65 | Done | 2 |
| SALES-8543 | Bump classes from API Version 58 to 65 | Done | 1 |
| SALES-8544 | Bump classes from API Version 61 to 65 | Done | 1 |
| SALES-8545 | Bump classes from API Version 62 to 65 | Done | 2 |
| SALES-8546 | Bump classes from API Version 63 to 65 | Done | 1 |
| SALES-8547 | Bump classes from API Version 64 to 65 | Done | 1 |
| SALES-8554 | Bump Handler and Helper classes from API Version 54 to 65 - Ticket 1 of 2 | Done | 3 |
| SALES-8555 | Bump Handler and Helper classes from API Version 54 to 65 - Ticket 2 of 2 | Done | 3 |
| SALES-8556 | Bump Client and Service classes from API Version 54 to 65 | Done | 2 |
| SALES-8557 | Bump rest of the classes from API Version 54 to 65 - Ticket 1 of 4 | Done | 2 |
| SALES-8558 | Bump rest of the classes from API Version 54 to 65 - Ticket 2 of 4 | Code Review | 2 |
| SALES-8559 | Bump rest of the classes from API Version 54 to 65 - Ticket 3 of 4 | In Progress | 2 |
| SALES-8560 | Bump rest of the classes from API Version 54 to 65 - Ticket 4 of 4 | To Do | 3 |
| SALES-8561 | Bump classes from API Version 59 to 65 - Ticket 1 of 2 | To Do | 3 |
| SALES-8562 | Bump classes from API Version 59 to 65 - Ticket 2 of 2 | To Do | 3 |
| SALES-8850 | Data Parity: Contact's Last Consignment Date field | Done | 1 |
| SALES-8937 | Investigate how many duplicate opportunities are being created by contact | Done | 2 |
| SALES-9194 | Determine What Automation Updates Are Needed for Sales Role Value Updates | To Do | 2 |
| SALES-9228 | Fix the consignor contacts that don't have a user_external_id__c in the last 90 days | Done | 2 |
| SALES-9250 | Fix sfAssignToMeQuickCreate.test.js | To Do | 2 |
| SALES-9251 | Fix sfDeleteLead.test.js | To Do | 2 |
| SALES-9252 | Fix sfDupLeadMatchedContact.test.js | To Do | 2 |
| SALES-9253 | Fix sfEditLead.test.js | To Do | 2 |
| SALES-9254 | Fix sfMergeLead.test.js | To Do | 2 |
| SALES-9255 | Fix sfConvertLeadToContact.test.js | To Do | 2 |
| SALES-9256 | Fix sfCloneOpportunity.test.js | To Do | 2 |
| SALES-9257 | Fix sfNPLFlow.test.js | To Do | 2 |
| SALES-9258 | Fix sfQuickCreateDropOff.test.js | To Do | 2 |
| SALES-9259 | Fix sfQuickCreate.test.js | To Do | 2 |
| SALES-9260 | Fix sfQuickCreateLCO.test.js | To Do | 2 |
| SALES-9261 | Fix sfEditContactAddress.test.js | To Do | 2 |
| SALES-9262 | Fix sfQuickCreateExistingUser.test.js | To Do | 2 |
| SALES-9272 | TD: Alex Zendesk Ticket 6/25 - 7/8 | Done | 1 |
| SALES-9276 | TD: Alex Zendesk Ticket 7/9/26 7/22/26 | Done | 1 |
| SALES-9280 | TD: Alex Zendesk Ticket 7/23/26 - 8/5/26 | Done | 1 |
| SALES-9283 | DevQA: SALES-7254 Update the label names on the lead button so it is consistent across the lwc and the lead page. | Done | 1 |
| SALES-9322 | Add Account Owner Email field in the Salesforce Report | Done | 1 |
| SALES-9325 | Why can BDRs book an appt in lead status without all of the consignor info? | To Do | 0 |
| SALES-9326 | Why can a Consignor self schedule if they are a previously unconverted contacts? | To Do | 0 |
| SALES-9327 | Buyers not consignors accidentally hit reconsign button and it creates multiple opps that go to multiple users. | To Do | 0 |
| SALES-9328 | Requesting a shipping label at checkout creates multiple opps that go to multiple users | To Do | 0 |
| SALES-9331 | Clean up unused Profiles, Permission Sets, and Permission Set Groups in Salesforce | Won't Do | 1 |
| SALES-9332 | [Spike] Discover & validate unused Profiles, PS, and PSG (Weeks 1–2) | In Progress | 3 |
| SALES-9333 | [Story] Cleanup unused Profiles, PS, and PSG — sandbox through production (Weeks 3–5+) | To Do | 3 |
| SALES-9334 | [Spike] Optimize Salesforce storage for COI and Comp Calculations objects | Done | 3 |
| SALES-9337 | Record-Trigger: Territory Roster- After Create Failure | Done | 1 |
| SALES-9357 | Helped Developing SELL-4934 | Done | 2 |
| SALES-9369 | DevQA: SALES-6747 Dropbox Signature Request Template Name Error | Done | 1 |
| SALES-9372 | Remove NAV Van Automated Tracking Functionality | Done | 2 |
| SALES-9379 | DevQA: SALES-9333 [Story] Cleanup unused Profiles, PS, and PSG — sandbox through production (Weeks 3–5+) | To Do | 0 |
| SALES-9381 | Helped Developing SELL-4934 | Done | 2 |
| SALES-9383 | Multi Calendar Issue: Opp not linking to appt record  | In Progress | 2 |
| SALES-9394 | ZD Tickets 7/9-7/22: KTLO | Done | 2 |
| SALES-9395 | CLONE - ZD Tickets 7/9-7/22: Domain Tech Debt | Done | 2 |
| SALES-9397 | Enable Quick Create option for Vendor users | Done | 1 |
| SALES-9401 | Remove funnel memory tests from Postman | Done | 1 |
| SALES-9402 | Change the visibility of the Quick Create tab in Prod | Done | 1 |
| SALES-9403 | DevQA: SALES-9401 Remove funnel memory tests from Postman | Done | 1 |
| SALES-9405 | Events, Site Setup for: San Jose, CA 9/25-9/26 | Code Review | 2 |
| SALES-9406 | Event Site Setup for: Alexandria, VA 9/24-9/26 | Done | 1 |
| SALES-9414 | DevQA: SALES-9372 Remove NAV Van Automated Tracking Functionality | Done | 1 |
| SALES-9417 | Remove MFA_Exempt Permission Set From Repo | Done | 1 |
| SALES-9418 | DevQA: SALES-9417 Remove MFA_Exempt Permission Set From Repo | Done | 1 |
| SALES-9430 | DevQA: SALES-9337 Record-Trigger: Territory Roster- After Create Failure | Done | 1 |
| SALES-9434 | Email Opt Out Pardot Issue Fix | Done | 2 |
| SALES-9442 | Improve Event Sync flow (Record_Trigger_Sumo_Appt_After_Save_Event_Sync2)  | Done | 3 |
| SALES-9443 | Optimize EventTriggerHandler.updateSumoAppointments | Done | 2 |
| SALES-9444 | Helped Developing SELL-4934[07-09 to -7-22] | Done | 2 |
| SALES-9449 | Discovery: SalesOps Migrating Off of Zendesk to JSM | To Do | 5 |
| SALES-9451 | Improve DataDog visibility building a new Dashboard | Done | 1 |
| SALES-9462 | Sell Funnel Leads are being created without a zip code | Done | 1 |
| SALES-9468 | ZD Tickets 7/23-8/5: KTLO | Done | 1 |
| SALES-9470 | CLONE - Multi Calendar Issue: Opp not linking to appt record | Done | 2 |
| SALES-9481 | DevQA: SALES-9443 Optimize EventTriggerHandler.updateSumoAppointments | Done | 1 |
| SALES-9482 | DevQA: SALES-8542 Bump classes from API Version 57 to 65 | Done | 1 |
| SALES-9488 | DevQA: SALES-9442 Improve Event Sync flow (Record_Trigger_Sumo_Appt_After_Save_Event_Sync2)  | Done | 1 |
| SALES-9489 | Re-authenticating Rippit x Zoom / Zoom Phone Integration | Done | 2 |
| SALES-9494 | DevQA: SALES-9381 Helped Developing SELL-4934 | Done | 1 |
| SALES-9497 | Nag - ZD - Domain Tech Debt - 7/23-8/5 | Done | 1 |
| SALES-9503 | DevQA: SALES-8543 Bump classes from API Version 58 to 65 | Done | 1 |
| SALES-9510 | Add a Direct Manager Field to Leads for reports in the BDR Dashboard | In Progress | 1 |
| SALES-9512 | DevQA: SALES-8545 Bump classes from API Version 62 to 65 | Done | 1 |
| SALES-9513 | DevQA: SALES-8544 Bump classes from API Version 61 to 65 | Done | 1 |
| SALES-9525 | Opportunities, Units, and Value Incorrectly Credited to BDR Team | To Do | 2 |
| SALES-9532 | Orphan Comp Calcs | In Progress | 2 |
| SALES-9533 | Merging Comp Calcs with COI | In Progress | 5 |
| SALES-9538 | Investigate how we can have one slug to match related inquiries(leads/opportunities) | Done | 3 |
| SALES-9540 | TD: Alex Zendesk Ticket 8/6/26 - 8/19/26 | Done | 1 |
| SALES-9541 | TD: Alex Zendesk Ticket 8/20/26 - 9/2/26 | To Do | 1 |
| SALES-9542 | TD: Alex Zendesk Ticket 9/3/26 - 9/16/26 | To Do | 1 |
| SALES-9543 | TD: Alex Zendesk Ticket 9/17/26 - 9/30/26 | To Do | 1 |
| SALES-9562 | DevQA: SALES-8546 Bump classes from API Version 63 to 65 | Done | 1 |
| SALES-9566 | DevQA: SALES-8547 Bump classes from API Version 64 to 65 | Done | 1 |
| SALES-9567 | Discovery ticket for Zipcodes | Done | 1 |
| SALES-9573 | POC - Google Gemini - Connect Salesforce Sandbox | In Progress | 2 |
| SALES-9574 | DevQA: SALES-8554 Bump Handler and Helper classes from API Version 54 to 65 - Ticket 1 of 2 | Done | 1 |
| SALES-9576 | DevQA: SALES-8555 Bump Handler and Helper classes from API Version 54 to 65 - Ticket 2 of 2 | Done | 1 |
| SALES-9578 | Zoom Phone Caller ID Mislabeling & Rep Number Provisioning Strategy | To Do | 0 |
| SALES-9581 | Lead Created Separately Instead of Converting to Opportunity Under Existing Contact Owner  | To Do | 0 |
| SALES-9588 | DevQA: SALES-8556 Bump Client and Service classes from API Version 54 to 65 | Done | 1 |
| SALES-9589 | DevQA: SALES-8557 Bump rest of the classes from API Version 54 to 65 - Ticket 1 of 4 | Done | 1 |
| SALES-9590 | Salesforce System Administrator Access Review | To Do | 3 |
| SALES-9591 | Spike - Evaluate custom MCP server vs native Salesforce connector for Gemini integration | To Do | 3 |
| SALES-9598 | Leads with fake firstname, lastname, and emails | Done | 1 |
| SALES-9601 | DevQA: SALES-8558 Bump rest of the classes from API Version 54 to 65 - Ticket 2 of 4 | To Do | 1 |
| SALES-9607 | DevQA: SALES-9510 Add a Direct Manager Field to Leads for reports in the BDR Dashboard | To Do | 0 |
| SALES-9608 | DevQA: SALES-8559 Bump rest of the classes from API Version 54 to 65 - Ticket 3 of 4 | To Do | 1 |
| SALES-9609 | DevQA: SALES-9434 Email Opt Out Pardot Issue Fix | Done | 1 |
## Blocked / At Risk / overdue
- Blocked: none
- At Risk labels: none found
- Overdue (duedate < 2026-08-13, not Done/Won't Do): none open under PT-1119 tree
## Net new movement since 2026-08-06
- PT-1119: Comments for Status still shows `[08/06]` (unchanged since prior week); Status RYG unchanged (Green); Jira Status unchanged (In Progress); project last updated 2026-08-06
### Child issue movement since 2026-08-06
**New additions:**
- SALES-9573 (created 2026-08-06, status=In Progress) — POC - Google Gemini - Connect Salesforce Sandbox
- SALES-9574 (created 2026-08-06, status=Done) — DevQA: SALES-8554 Bump Handler and Helper classes from API Version 54 to 65 - Ticket 1 of 2
- SALES-9576 (created 2026-08-07, status=Done) — DevQA: SALES-8555 Bump Handler and Helper classes from API Version 54 to 65 - Ticket 2 of 2
- SALES-9578 (created 2026-08-07, status=To Do) — Zoom Phone Caller ID Mislabeling & Rep Number Provisioning Strategy
- SALES-9581 (created 2026-08-10, status=To Do) — Lead Created Separately Instead of Converting to Opportunity Under Existing Contact Owner 
- SALES-9588 (created 2026-08-10, status=Done) — DevQA: SALES-8556 Bump Client and Service classes from API Version 54 to 65
- SALES-9589 (created 2026-08-10, status=Done) — DevQA: SALES-8557 Bump rest of the classes from API Version 54 to 65 - Ticket 1 of 4
- SALES-9590 (created 2026-08-10, status=To Do) — Salesforce System Administrator Access Review
- SALES-9591 (created 2026-08-11, status=To Do) — Spike - Evaluate custom MCP server vs native Salesforce connector for Gemini integration
- SALES-9598 (created 2026-08-11, status=Done) — Leads with fake firstname, lastname, and emails
- SALES-9601 (created 2026-08-11, status=To Do) — DevQA: SALES-8558 Bump rest of the classes from API Version 54 to 65 - Ticket 2 of 4
- SALES-9607 (created 2026-08-12, status=To Do) — DevQA: SALES-9510 Add a Direct Manager Field to Leads for reports in the BDR Dashboard
- SALES-9608 (created 2026-08-12, status=To Do) — DevQA: SALES-8559 Bump rest of the classes from API Version 54 to 65 - Ticket 3 of 4
- SALES-9609 (created 2026-08-12, status=Done) — DevQA: SALES-9434 Email Opt Out Pardot Issue Fix
**Completions / status changes to Done/Won't Do:**
- SALES-6058 (Done, updated 2026-08-11) — Update Zip codes quarterly
- SALES-8396 (Won't Do, updated 2026-08-11) — Establish security oriented development practices across the enterprise
- SALES-8407 (Won't Do, updated 2026-08-11) — Maintain SSO Requirement for Salesforce users
- SALES-8546 (Done, updated 2026-08-06) — Bump classes from API Version 63 to 65
- SALES-8547 (Done, updated 2026-08-10) — Bump classes from API Version 64 to 65
- SALES-8554 (Done, updated 2026-08-10) — Bump Handler and Helper classes from API Version 54 to 65 - Ticket 1 of 2
- SALES-8555 (Done, updated 2026-08-10) — Bump Handler and Helper classes from API Version 54 to 65 - Ticket 2 of 2
- SALES-8556 (Done, updated 2026-08-12) — Bump Client and Service classes from API Version 54 to 65
- SALES-8557 (Done, updated 2026-08-12) — Bump rest of the classes from API Version 54 to 65 - Ticket 1 of 4
- SALES-9406 (Done, updated 2026-08-11) — Event Site Setup for: Alexandria, VA 9/24-9/26
- SALES-9434 (Done, updated 2026-08-12) — Email Opt Out Pardot Issue Fix
- SALES-9538 (Done, updated 2026-08-11) — Investigate how we can have one slug to match related inquiries(leads/opportunities)
- SALES-9540 (Done, updated 2026-08-10) — TD: Alex Zendesk Ticket 8/6/26 - 8/19/26
- SALES-9562 (Done, updated 2026-08-06) — DevQA: SALES-8546 Bump classes from API Version 63 to 65
- SALES-9566 (Done, updated 2026-08-07) — DevQA: SALES-8547 Bump classes from API Version 64 to 65
- SALES-9567 (Done, updated 2026-08-11) — Discovery ticket for Zipcodes
**Status changes (non-completion):**
- SALES-7759 (To Do, updated 2026-08-06) — Address issue when client is self-booking an at home from CLP.
- SALES-8402 (To Do, updated 2026-08-11) — Ensure Secure and Governed User Access Changes with Executive Approval
- SALES-8403 (To Do, updated 2026-08-10) — Create Elevated Analyst Profile to Minimize Full Admin Access
- SALES-8405 (To Do, updated 2026-08-12) — Automate Deactivation of Inactive Users After 90 Days
- SALES-8558 (Code Review, updated 2026-08-12) — Bump rest of the classes from API Version 54 to 65 - Ticket 2 of 4
- SALES-8559 (In Progress, updated 2026-08-12) — Bump rest of the classes from API Version 54 to 65 - Ticket 3 of 4
- SALES-8560 (To Do, updated 2026-08-11) — Bump rest of the classes from API Version 54 to 65 - Ticket 4 of 4
- SALES-8561 (To Do, updated 2026-08-11) — Bump classes from API Version 59 to 65 - Ticket 1 of 2
- SALES-8562 (To Do, updated 2026-08-11) — Bump classes from API Version 59 to 65 - Ticket 2 of 2
- SALES-9332 (In Progress, updated 2026-08-12) — [Spike] Discover & validate unused Profiles, PS, and PSG (Weeks 1–2)
- SALES-9333 (To Do, updated 2026-08-10) — [Story] Cleanup unused Profiles, PS, and PSG — sandbox through production (Weeks 3–5+)
- SALES-9383 (In Progress, updated 2026-08-11) — Multi Calendar Issue: Opp not linking to appt record 
- SALES-9405 (Code Review, updated 2026-08-12) — Events, Site Setup for: San Jose, CA 9/25-9/26
- SALES-9449 (To Do, updated 2026-08-12) — Discovery: SalesOps Migrating Off of Zendesk to JSM
- SALES-9510 (In Progress, updated 2026-08-12) — Add a Direct Manager Field to Leads for reports in the BDR Dashboard
- SALES-9525 (To Do, updated 2026-08-10) — Opportunities, Units, and Value Incorrectly Credited to BDR Team
- SALES-9532 (In Progress, updated 2026-08-07) — Orphan Comp Calcs
- SALES-9533 (In Progress, updated 2026-08-10) — Merging Comp Calcs with COI
---
# 1–6. JIRA — PT-1118 — SRT - Software Upgrades & Technical Compliance
## Project fields (live 2026-08-13)
| Field | Value |
| --- | --- |
| Key | PT-1118 |
| Summary | SRT - Software Upgrades & Technical Compliance |
| Jira Status | In Progress |
| Status RYG | Green |
| Target end date (Due Date) | 2026-11-30 |
| Start Date | 2026-05-01 |
| Assignee | Navinchandra Gupta |
| Last updated | 2026-08-06T08:42:32.078-0700 |
## Comments for Status (full text)
```
[08/06] Major update to permanently fix the recurring SailPoint ECA authorization issue. Two SUMO page loadtime configuration items are in progress, and the remaining Salesforce release update backlog is being prepared for upcoming sprints.
```
## Direct child epics
| Key | Summary | Status | Epic SP | Due date | Child open SP | Child closed SP | Child count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SALES-9021 | Salesforce Summer '26 Release Coordination | Done | 20 | 2026-06-30 | 0 | 17 | 26 |
| SALES-9041 | [26Q2] SRT: Software Upgrades and Technical Compliance Epic | Done | 20 | 2026-07-09 | 0 | 27 | 27 |
| SALES-9205 | [26Q3] SRT: Software Upgrades and Technical Compliance Epic | In Progress | 18 | 2026-09-30 | 17 | 58 | 62 |
### Child stories — SALES-9021 (26 issues)
| Key | Summary | Status | SP |
| --- | --- | --- | --- |
| SALES-8955 | Releases: Enable Accessibility Enhancements for Date Pickers, Popovers, Bottom Utility Bars, Record Headers | Done | 1 |
| SALES-8956 | Releases: Salesforce-Managed X (Formerly Twitter) Authentication Provider Retirement | Won't Do | 1 |
| SALES-8957 | Releases: Use Visualforce PDF Rendering Service with Apex Blob.toPdf() | Done | 1 |
| SALES-8958 | Releases: Enable Accessibility Enhancements for Page Headers and Modal Windows When Zoom Is Greater Than 200% | Done | 1 |
| SALES-8959 | Releases: Sort Apex Batch Action Results by Request Order | Won't Do | 0 |
| SALES-8980 | Summer 26 Release \| Zoom, Address Validation, Lead Assignment, Lead Conversion | Done | 1 |
| SALES-8981 | Summer 26 Release\| Real Partners | Done | 1 |
| SALES-8982 | Summer 26 Release \| SF - Admin Sync | Done | 1 |
| SALES-8983 | Summer 26 Release \| Shipping Happy Path | Done | 1 |
| SALES-8984 | Summer 26 Release \| Vendor Bulk Upload | Done | 1 |
| SALES-8985 | Summer 26 Release - Funnel testing in staging after the css fix | Done | 1 |
| SALES-8986 | Summer 26 Release \| Add Item | Done | 1 |
| SALES-8987 | Summer 26 Release \| Lead Conversion Self Gen Referrals | Won't Do | 0 |
| SALES-8988 | Summer 26 Release \| VO Doc Test | Done | 1 |
| SALES-8989 | Summer 26 Release \| SUMO Scheduling on Lead | Done | 1 |
| SALES-8990 | Summer 26 Release \| Commissions | Done | 1 |
| SALES-8991 | Summer 26 Release \| As a sales rep create a self-generated referral and convert it to an opportunity. - using the st... | Won't Do | 0 |
| SALES-8992 | Summer 26 Release \| VO Doc Process | Won't Do | 0 |
| SALES-8993 | Summer 26 Release \| Slack - HelloSign | Done | 1 |
| SALES-8994 | Summer 26 Release \| Zoom | Won't Do | 0 |
| SALES-8995 | Summer 26 Release \| Address Validation | Won't Do | 0 |
| SALES-8996 | Summer 26 Release \| HelloSign | Won't Do | 0 |
| SALES-8997 | Summer 26 Release \| SUMO Scheduling on CLP and Cancelling | Done | 1 |
| SALES-8998 | Summer 26 Release \| SUMO QA- Book SGO Retail Appt | Won't Do | 0 |
| SALES-8999 | Summer 26 Release \| SUMO Scheduling, Update & Cancel on Opp | Done | 1 |
| SALES-9000 | Summer 26 Release \| SUMO and Commissions Quick test | Won't Do | 0 |
### Child stories — SALES-9041 (27 issues)
| Key | Summary | Status | SP |
| --- | --- | --- | --- |
| SALES-8507 | Upgrade Zoom in Production  to version 2.38 | Done | 1 |
| SALES-9029 | Security Update: Verify all Salesforce email-sending domains (Phase 1) | Done | 0 |
| SALES-9030 | Security Update: Prepare allowlisted email domains for Phase 2 verification | Done | 0 |
| SALES-9031 | Security Update: Remediate Connected App and API access for VPN/proxy blocking | Done | 1 |
| SALES-9035 | Security Update: Implement step-up authentication for Salesforce report activities | Done | 1 |
| SALES-9064 | bump GitHub Actions pins for Node 20 deprecation on setup-sfdx action | Done | 1 |
| SALES-9070 | CLONE - Summer 26 Release \| Vendor Bulk Upload | Done | 1 |
| SALES-9072 | Deployer Access for Salesforce-CRM Repo - May 2026 | Done | 1 |
| SALES-9083 | Add a realreal.com Authorized Email Domain in Production | Done | 2 |
| SALES-9119 | Change deploy-to-staging skill to be able to deploy to any sandbox | Done | 1 |
| SALES-9145 | Remove Data Mask package | Done | 1 |
| SALES-9164 | Zoom Upgrade Production | Done | 1 |
| SALES-9165 | Hellosign contract Signature is not displaying properly on iPad | Done | 1 |
| SALES-9169 | ARB Transition Plan | Done | 2 |
| SALES-9179 | Salescloud Q2 2026 Manual Remediation | Done | 1 |
| SALES-9180 | SRT Q3 Capacity Planning  | Done | 3 |
| SALES-9186 | Nag - Zendesk Bucket - S/w Upgrade - 06/11-6/24 | Done | 0 |
| SALES-9196 | SU&TC: Alex Zendesk Ticket 6/11 - 6/25 | Done | 1 |
| SALES-9197 | SOX SF-CM-01 (Change Management) Control Task | Done | 1 |
| SALES-9227 | CLONE - Update Sailpoint Connect from Basic Auth to OAuth connection | Done | 2 |
| SALES-9232 | CLONE - Security Update: Implement step-up authentication for Salesforce report activities | Done | 1 |
| SALES-9308 | Nag - Zendesk - S/w Upgrades - 06/25 - 7/8 | Won't Do | 0 |
| SALES-9310 | Assign Records to Inactive User permission set assignment to Gustavo Silva | Done | 1 |
| SALES-9319 | Change COI PE to search records by crm_id or slug | Done | 2 |
| SALES-9321 | Manage Public List Views Access in Salesforce Staging and Production | Done | 1 |
| SALES-9323 | DevQA: SALES-9319 Change COI PE to search records by crm_id or slug | Won't Do | 0 |
| SELLTECH-578 | ICU Locale not enabled  due to the API version below 45 used in the org[Managed Packages] | Won't Do | 0 |
### Child stories — SALES-9205 (62 issues)
| Key | Summary | Status | SP |
| --- | --- | --- | --- |
| SALES-8414 | User training for Admin and Non Admin Salesforce | To Do | 3 |
| SALES-8960 | Update Sailpoint Connect from Basic Auth to OAuth connection | Won't Do | 2 |
| SALES-9032 | Security Update: Review extended login anomaly detection and containment impact | Done | 1 |
| SALES-9033 | Security Update: Enforce phishing-resistant MFA for privileged users (including admins) | Won't Do | 1 |
| SALES-9034 | Security Update: Enforce MFA for all employee Salesforce users | Done | 3 |
| SALES-9036 | Security Update: Prepare step-up authentication for anomalous report export | Done | 1 |
| SALES-9037 | Security Update: Adopt Transaction Security policy enhancements | Won't Do | 1 |
| SALES-9038 | Security Update: Communicate June 2026 Salesforce security changes to end users | Done | 1 |
| SALES-9107 | Change SF Shipping Label button to generate as many shipping labels as number of boxes specified | To Do | 0 |
| SALES-9112 | Security: SUMO Guest User Access Issue | To Do | 1 |
| SALES-9143 | Software license management, management & auditing | To Do | 0 |
| SALES-9229 | Agentforce Co-worker Introduction and Features | Done | 2 |
| SALES-9238 | Figma Diagram for ZD process | To Do | 2 |
| SALES-9239 | SUMO Page loadtime improvements configuration | Done | 2 |
| SALES-9277 | SU&TC: Alex Zendesk Ticket 7/9/26 - 7/22/26 | Done | 1 |
| SALES-9281 | SU&TC: Alex Zendesk Ticket 7/23/26 8/5/26 | Done | 1 |
| SALES-9285 | DevQA: SALES-9032 Security Update: Review extended login anomaly detection and containment impact | Done | 1 |
| SALES-9286 | DevQA: SALES-9033 Security Update: Enforce phishing-resistant MFA for privileged users (including admins) | Won't Do | 1 |
| SALES-9287 | DevQA: SALES-9035 Security Update: Implement step-up authentication for Salesforce report activities | Done | 1 |
| SALES-9288 | DevQA: SALES-9037 Security Update: Adopt Transaction Security policy enhancements | Won't Do | 1 |
| SALES-9302 | DevQA: SALES-9239 SUMO Page loadtime improvements configuration | Won't Do | 1 |
| SALES-9324 | DevQA: SALES-9319 Change COI PE to search records by crm_id or slug | Done | 1 |
| SALES-9330 | Revoke the Installer Permission set for Bryan | Done | 1 |
| SALES-9335 | Determine additional storage capacity required to enable Einstein Activity Capture (EAC) and Inbox | Done | 2 |
| SALES-9338 | DevQA: SALES-9036 Security Update: Prepare step-up authentication for anomalous report export | Done | 1 |
| SALES-9340 | [SF RU] Enable Profile Filtering — assess, test & activate | Done | 2 |
| SALES-9342 | Report Export > 10k rows is taking the users to classic version | Done | 1 |
| SALES-9358 | CLONE - Agentforce Co-worker Introduction and Features | Done | 2 |
| SALES-9359 | CLONE - Figma Diagram for ZD process | Done | 2 |
| SALES-9366 | DevQA: SALES-9034 Security Update: Enforce MFA for all employee Salesforce users | Done | 1 |
| SALES-9380 | CLONE - Report Export > 10k rows is taking the users to classic version | Done | 1 |
| SALES-9386 | CLONE - SUMO Page loadtime improvements configuration | Won't Do | 1 |
| SALES-9399 | Assign High Value Designer Admin permission set to Grace Saint | Done | 1 |
| SALES-9408 | Install Sailpoint Managed Package in Salesforce Staging | Done | 2 |
| SALES-9412 | Update the PagerDuty Schedule and participants for SRT | Done | 1 |
| SALES-9419 | [SF RU] Retirement of OAuth 2.0 Username-Password Flow for Connected Apps — assess & migrate | To Do | 2 |
| SALES-9420 | [SF RU] Enable Accessibility Enhancements for To Do Lists & Lightning Dual Listboxes (Zoom > 200%) | Done | 3 |
| SALES-9421 | [SF RU] Remove Non-Public Fields from Custom Object Data in Aura Action Responses — assess & activate | Done | 3 |
| SALES-9422 | [SF RU] Salesforce to Salesforce Retirement — assess usage & migrate before Spring '27 | To Do | 0 |
| SALES-9423 | [SF RU] Update Apex Code and Flows for Changed Sharing Recalculation Behavior — assess & remediate | To Do | 0 |
| SALES-9424 | [SF RU] Block Apex Anonymous Code Execution from Managed Packages — assess & activate | To Do | 0 |
| SALES-9425 | [SF RU] SOAP API login() Retirement — migrate auth to External Client Applications | To Do | 0 |
| SALES-9426 | [SF RU] Salesforce Platform API Versions 31.0–40.0 Retirement — upgrade integrations | To Do | 0 |
| SALES-9428 | Create read-only Permission Set Group for Sales Ops, Product & Sales Leadership (from Engineers profile + existing Re... | Won't Do | 0 |
| SALES-9448 | SOC 1 Type II Request (s) - Salesforce Corp and Services | Done | 1 |
| SALES-9453 | DevQA: SALES-9340 [SF RU] Enable Profile Filtering — assess, test & activate | Done | 1 |
| SALES-9469 | CLONE - SUMO Page loadtime improvements configuration | Won't Do | 2 |
| SALES-9472 | Salesforce Entitlements Missing Description - Sailpoint | Done | 1 |
| SALES-9474 | Install Sailpoint Managed Package in Salesforce Production | Done | 2 |
| SALES-9496 | Nag - ZD - S/W Upgrades - 7/23 - 8/5 | Done | 1 |
| SALES-9544 | SU&TC: Alex Zendesk Ticket 8/6/26 - 8/19/26 | Done | 1 |
| SALES-9545 | SU&TC: Alex Zendesk Ticket 8/20/26 - 9/2/26 | To Do | 1 |
| SALES-9546 | SU&TC: Alex Zendesk Ticket 9/3/26 - 9/16/26 | To Do | 1 |
| SALES-9547 | SU&TC: Alex Zendesk Ticket 9/17/26 - 9/30/26 | To Do | 1 |
| SALES-9557 | Sailpoint - Salesforce ECA Authorization permanent fix | Blocked | 1 |
| SALES-9569 | CLONE - Figma Diagram for ZD process | Won't Do | 2 |
| SALES-9571 | #ITGC.AS.S20.SF-AS-01: Salesforce Access Provisioning - Interim | In Progress | 2 |
| SALES-9583 | SUMO Flow Audit for Sales Role Updates | Won't Do | 1 |
| SALES-9584 | DevQA: SALES-9583 SUMO Flow Audit for Sales Role Updates | To Do | 0 |
| SALES-9602 | Winter 27 Preview Sandbox | To Do | 1 |
| SALES-9610 | Retroactive Approval – Salesforce System Administrator Access for David | In Progress | 1 |
| SALES-9612 | Retroactive approval - Salesforce System Admin Access for Gustavo | In Progress | 1 |
## Blocked / At Risk / overdue
- Blocked:
  - SALES-9557 — Sailpoint - Salesforce ECA Authorization permanent fix (SP=1)
- At Risk labels: none found
- Overdue (duedate < 2026-08-13, not Done/Won't Do): none open under PT-1118 tree
## Net new movement since 2026-08-06
- PT-1118: Comments for Status still shows `[08/06]` (unchanged since prior week); Status RYG unchanged (Green); Jira Status unchanged (In Progress); project last updated 2026-08-06
### Child issue movement since 2026-08-06
**New additions:**
- SALES-9569 (created 2026-08-05, status=Won't Do) — CLONE - Figma Diagram for ZD process
- SALES-9571 (created 2026-08-06, status=In Progress) — #ITGC.AS.S20.SF-AS-01: Salesforce Access Provisioning - Interim
- SALES-9583 (created 2026-08-10, status=Won't Do) — SUMO Flow Audit for Sales Role Updates
- SALES-9584 (created 2026-08-10, status=To Do) — DevQA: SALES-9583 SUMO Flow Audit for Sales Role Updates
- SALES-9602 (created 2026-08-11, status=To Do) — Winter 27 Preview Sandbox
- SALES-9610 (created 2026-08-12, status=In Progress) — Retroactive Approval – Salesforce System Administrator Access for David
- SALES-9612 (created 2026-08-12, status=In Progress) — Retroactive approval - Salesforce System Admin Access for Gustavo
**Completions / status changes to Done/Won't Do:**
- SALES-9302 (Won't Do, updated 2026-08-11) — DevQA: SALES-9239 SUMO Page loadtime improvements configuration
- SALES-9428 (Won't Do, updated 2026-08-10) — Create read-only Permission Set Group for Sales Ops, Product & Sales Leadership (from Engineers profile + existing Read Only PS)
- SALES-9469 (Won't Do, updated 2026-08-10) — CLONE - SUMO Page loadtime improvements configuration
- SALES-9544 (Done, updated 2026-08-11) — SU&TC: Alex Zendesk Ticket 8/6/26 - 8/19/26
**Status changes (non-completion):**
- SALES-9112 (To Do, updated 2026-08-11) — Security: SUMO Guest User Access Issue
- SALES-9419 (To Do, updated 2026-08-11) — [SF RU] Retirement of OAuth 2.0 Username-Password Flow for Connected Apps — assess & migrate
- SALES-9557 (Blocked, updated 2026-08-11) — Sailpoint - Salesforce ECA Authorization permanent fix
---
# 9–10. SLACK
## Search: PT-1118 OR PT-1119 OR "Salesforce Tech Debt" OR "Software Upgrades" (after 2026-08-06)
- No results in slack_search_public.
## Search: Sailpoint OR SUMO OR "tech debt" OR SALES-9383 OR multi calendar (after 2026-08-06)
- No results in slack_search_public.
## Search: from:Casey Gould weekly update (after 2026-08-06)
- No results in slack_search_public.
## Search: from:Bryan Claggett weekly update (after 2026-08-06)
- No results in slack_search_public.
## Search: from:Casey Gould (after 2026-08-06)
- No results in slack_search_public.
## Search: from:Bryan Claggett (after 2026-08-06)
- No results in slack_search_public.
## #pt-squad-leads — messages since 2026-08-06
### 2026-08-13 — Weekly Project Status Updates (BOT)
> It's Thursday again – please provide weekly Project status updates sometime today. :thank-yellow:
> *Reminder: Please remove previous updates from the field. Past updates can be reviewed under the ticket history.*
> See more details in Notion.
- Permalink ts: 1786629661.863299
### 2026-08-06 — Weekly Project Status Updates (BOT)
> It's Thursday again – please provide weekly Project status updates sometime today. :thank-yellow:
> *Reminder: Please remove previous updates from the field. Past updates can be reviewed under the ticket history.*
> See more details in Notion.
- Permalink ts: 1786024862.842729
## #srt_squadleads — messages since 2026-08-06
### 2026-08-12 — Devon Novotnak
> Okay this should all be routing directly through product. Can we have Dora reach out to @Jenn Kleinfeld directly?
> Nothing from the stakeholder side should come to the team without coming through product first, think of them as the bouncers at a club lol.
> If you need us to take on any other requests from anyone let us know!!!
### 2026-08-12 — Navinchandra Gupta
> I work with the CR team on integrating and maintaining the Salesforce and Rippit integration. They brought up a new request while I was helping them troubleshoot an integration failure some time ago.
> I didn't want to create a Jira ticket directly without first understanding which process or bucket this request falls under. That's why I asked them to use an intake form, but I'm not sure which intake form would be the appropriate one to share with them.
> The person I'm currently working with on this request is *Dora Santos*.
### 2026-08-12 — Devon Novotnak
> And where are you pulling this from Navin? is this in Zendesk?
### 2026-08-12 — Navinchandra Gupta
> Rippit is the new name for MaestroQA, is a Rep Quality scoring app.
### 2026-08-12 — Devon Novotnak
> I honestly don't know what Rippit is - any idea?
### 2026-08-12 — Navinchandra Gupta
> <!here> do we know which intake form is used for such requirements:
> The requirement is to update the SMS/Text interactions view in Rippit so the Author field displays the consignor's name from their Salesforce contact record instead of their phone number. This would make it easier for the QA team to identify who sent each message while reviewing conversations.
### 2026-08-12 — Navinchandra Gupta
> Good Morning and Welcome back!! @Devon Novotnak Will look into this today!
### 2026-08-12 — Devon Novotnak
> https://trr-techissues.zendesk.com/agent/tickets/133589 - the internal audit team needs SF permissions. Can we take a look?
### 2026-08-12 — Devon Novotnak
> Hey Crew! Slowly coming back and catching up!!!
### 2026-08-07 — Jenn Kleinfeld
> re: Zoom phone numbers
> Hi @David Garcia it was reported to me that one of the ALRA reps was issued a phone number where the phone number was associated with a bank name. She and sales is worried that it may be happening to others and wants to make sure that all our zoom phone numbers are cleansed before they are issued and that there is a subsequent check on them to make sure there is no re-attribution. This feels to me like some discovery is needed as it is process driven. What is the best way for me to handle this? Spike ticket? (Obviously this would be great to automate but I realize we might not be there yet as we are dealing with vendors).
- Thread: 4 replies (latest: 2026-08-07 14:03:26 PDT)
### 2026-08-07 — Bryan Claggett
> Hey Jenn, from what I recall from Casey, the reason they're changing the timing of the MBR is to keep the focus on prior month, not current month. You may want to confirm with her, just in case. As for cloning, that is actually encouraged. That way your JIRA connection will stay accurate to pull in SRT's project information.
### 2026-08-07 — Jenn Kleinfeld
> Hi @Bryan Claggett I wanted to create the new MBR doc for next week for David and I. Are they updating to just reflect the past month or is that more directional? Also, can I just clone it? I thought there was something about we could not clone, so just checking in on it. Thanks in advance for your help.
## #srt-team — messages since 2026-08-06
### 2026-08-12 — Jenn Kleinfeld
> Question for Alex or anyone who knows the answer.
> _How does SRT become aware if a person is back from LOA leave?_
- Thread: 3 replies (latest: 2026-08-12 17:18:10 PDT)
### 2026-08-12 — Jummy Sanni
> Going to be offline for about an hour, going to pick my son up! Cc @Navinchandra Gupta
### 2026-08-12 — Michael Criswell
> My internet is back. I'm online now.
### 2026-08-12 — Michael Criswell
> I might be late or miss standup. I have someone at my house working on fixing the internet.
### 2026-08-12 — David Garcia
> Anyone know what this means? <!here>
- Thread: 6 replies (latest: 2026-08-12 17:21:34 PDT)
- Forwarded message from Tori Parker: [August 12th, 2026 6:51 AM] tori.parker: image.png
### 2026-08-10 — Sai Deepika Kanuri
> Hi Team, I'm out 12-2 PST - I have my car appointment and have to go to DMV.
### 2026-08-10 — Jummy Sanni
> Hey team! I'm experiencing a power outage in my area and limited with connection. I'll join standup via mobile and will be monitoring slack @Navinchandra Gupta
### 2026-08-07 — Jenn Kleinfeld
> David, quick question. A stakeholder reached out about if we capture emails that reps send to clients. I know we capture the pardot, but have we migrated to the gmail sync yet and are we capturing those now or is that still on the roadmap to be done? I know the memory thing was waiting on it.
- Thread: 4 replies (latest: 2026-08-11 10:55:31 PDT)
### 2026-08-07 — Jenn Kleinfeld
> I have a conflict, will not be at the standup this morning. Please reach out on the jira tickets or in slack if you need me.
### 2026-08-06 — Navinchandra Gupta
> <!here> Github status update:
> https://www.githubstatus.com/
### 2026-08-06 — REMINDER - Weekly Status Update (BOT)
> +++++++++++++++++++++++++++++++++++++
> REMINDER - Please update Weekly Status
> +++++++++++++++++++++++++++++++++++++
### 2026-08-06 — David Garcia
> Do we need to notify anyone?
- Thread: 1 reply (latest: 2026-08-06 10:55:20 PDT)
### 2026-08-06 — Michael Criswell
> <!here> Heads up with the github outage ci/cd jobs aren't running.
### 2026-08-06 — Jummy Sanni
> Hey everyone! I'm back in the States, but my travel ended up being more tedious than expected, and I didn't get in until late last night. I'm going to get some rest and then log back in later today. If anything urgent comes up in the meantime, feel free to slack me!
## #seller-salestech — messages since 2026-08-06
- No messages returned.
## #bdr-salesforce-escalations — messages since 2026-08-06
- Not queried this run.
## #releases — messages since 2026-08-06
- Not queried this run.
## #qe-regression — messages since 2026-08-06
- Not queried this run.
---
# Data gaps / query notes
- Jira filter 15396 live query executed 2026-08-13; returns PT-1118, PT-1119
- Total child issues under project epics: 270 (prior week: 253)
- Child open/closed SP totals computed from full paginated fetch per epic (2026-08-13)
- Story points on child tickets use customfield_10026 (sprint); epic-level SP uses customfield_10016
- Key Jira Fields database fetched 2026-08-13; no field definition updates detected vs prior fetch 2026-08-06
- PT-1118 and PT-1119 Comments for Status not updated since 2026-08-06 (still show [08/06] prefix)
- SALES-9383 status changed from Blocked to In Progress (updated 2026-08-11)
- SALES-9469 and SALES-9302 SUMO page loadtime items changed to Won't Do (updated 2026-08-10 and 2026-08-11)
- SALES-9557 Sailpoint ECA permanent fix added and marked Blocked (updated 2026-08-11)
- No Slack messages from Casey Gould about weekly update process since 2026-08-06
- Bryan Claggett posted in #srt_squadleads 2026-08-07 about MBR doc cloning and Casey Gould MBR timing (not weekly update process announcement)