# SRT Sprint Retrospective — SALES board (Sprint 8591)

**Data source:** Jira project `SALES`, sprint **Sales 5/14 - 5/27** (ID `8591`, board ID `10`). Snapshot reflects issues as queried after sprint closure (**2026-06-05**). **PT-** tickets: **none** in sprint `8591`. **SELLTECH-** tickets in sprint: **`SELLTECH-1050`** (3 pts, Done, Gustavo Silva), **`SELLTECH-1051`** (2 pts, Done, Gustavo Silva).

---

### Executive Summary

The sprint closed **cleanly with zero carry-over** while delivering **very high throughput**: **75** issues reached **Done** totaling **113** story points across **88** sprint issues. The biggest win was **successful Summer '26 release QA execution** (large batch of `SALES-8980`–`SALES-9000` tickets) alongside **6/1 compensation/quota changes** and **Salesforce Security Phase 2** spikes. The biggest concern remains **SRT label discipline**: only **33** of **118** sprint points (**28.0%**) carry **`SRT-Product`**, so capacity reporting against SRT buckets is **mostly unclassified**. **Committed points at sprint start**, **full mid-sprint add/remove inventory**, and **scope change %** are **Unavailable without batch changelog replay**.

---

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 5/14 - 5/27 |
| Sprint Dates | **2026-05-14** 16:37 UTC → **2026-05-28** 06:30 UTC (completed **2026-05-28** 15:03 UTC) |
| Sprint Goal | 1. 6/1 Comp/Quota Changes 2. Summer Release 2026 3. Outreach Automation 4. Voice Recognition |
| Committed Points | **Unavailable without batch changelog replay at sprint start** |
| Completed Points | **113** (75 Done issues) |
| Carry-Over (tickets / points) | **0** / **0** |
| Removed (tickets / points) | **Unavailable** (requires parsing sprint removal events from each issue changelog) |
| Added Mid-Sprint (tickets / points) | **18** tickets created after sprint start (**20** pts where estimated; full add-to-sprint inventory not computed) |
| Scope Change % | **Unavailable** (depends on committed-at-start baseline and net adds/removes) |
| Won't Do (tickets / points) | **13** / **5** |
| Spikes Closed | **8** (`SALES-8935`, `SALES-8936`, `SALES-8957`, `SALES-8978`, `SALES-9001`, `SALES-9003`, `SALES-9004`, `SALES-9016`) |
| Bugs Closed | **19** |

---

### Capacity Allocation Breakdown

**Method:** Each sprint issue counted **once**. **Product** if labels contain `SRT-product`, `SRT-Product`, or `SRT-RO`. **Tech Health** if `SRT-Domain-Tech-Debt` or `SRT-Software-Upgrades`. **KTLO** if `SRT-KTLO`. Otherwise **Buffer / Unplanned**. Denominator = **118** (sum of story points on all **88** sprint issues, treating `null` as **0**).

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|-----------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | **33** | **28.0%** | **-1 pts vs target** |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | **0** | **0.0%** | **-11 pts vs target** |
| KTLO (SRT-KTLO) | 16% | ~11 | **0** | **0.0%** | **-11 pts vs target** |
| Buffer / Unplanned | 20% | ~14 | **85** | **72.0%** | **+71 pts vs target** |

**KTLO > 30% flag:** **No** — **0.0%** of sprint points carried `SRT-KTLO`.

**Interpretation:** Substantial product, release-QA, and KTLO-class work likely occurred without SRT labels. This table reflects **labels in Jira**, not intent.

---

### Key Findings

#### Scope Creep & Mid-Sprint Changes

- **Full list (all tickets):** **Not produced in this run** (requires `getJiraIssue` + `expand=changelog` for all **88** keys).
- **Observed mid-sprint creation pattern:** **0** tickets in the **Summer '26 Release** family were **created 2026-05-12** (before official sprint start on **2026-05-14**) — keys **`SALES-8980`** through **`SALES-9000`** plus security spikes **`SALES-9001`**, **`SALES-9003`**, **`SALES-9004`**. This represents a **large scope injection** tied to release validation, not ad-hoc churn.
- **Illustrative example — `SALES-8980`:** Created **2026-05-12**, added to sprint before start; story points adjusted **null → 1 → 2 → 1** by Navinchandra Gupta / Alex Burton before/during sprint start (per prior changelog review).
- **Won't Do de-scoping:** **13** tickets closed as **Won't Do** (mostly duplicate Summer '26 sub-tickets consolidated into parent work).

#### Velocity & Throughput

| Sprint | Jira sprint id | Done points (`status = Done`) |
|--------|----------------|-------------------------------|
| **Current** | **8591** | **113** (75 Done tickets) |
| Prior | **8190** | **90** (55 Done tickets) |
| Prior | **7949** | **108** (62 tickets with points) |
| Prior | **7548** | **83** (50 Done tickets) |

**Trend:** **Up sharply** from **90 → 113** vs immediately prior sprint (**+23** pts), and **above** both **7949** (**108**) and **7548** (**83**). Memorial Day (**2026-05-26**) may have reduced final-week capacity; throughput still exceeded prior sprint.

#### Burndown Analysis

Using **`resolutiondate`** on **`status = Done`** issues in sprint **8591**:

- **Early sprint (through 2026-05-18):** **25** pts closed.
- **Mid sprint (2026-05-19 – 2026-05-22):** **36** pts closed.
- **Late sprint (2026-05-23+):** **52** pts closed — includes Memorial Day week (**2026-05-26** US holiday).
- **Peak closure day:** **2026-05-27** with **29** pts.
- **Post–sprint-end Done timestamps:** **2026-06-03** (2 pts) (after nominal end **2026-05-28**).
- **Shape:** **late-heavy** — finish-line clustering.

#### Bug Analysis

- **Bugs closed (Done):** **19** issues.
- **Reason for Bug (`customfield_10142`):** **Unavailable / not populated** — Jira returned **`null`** for **all 19** closed bugs in sprint **8591** (same data gap as sprint **8190**).
- **Zendesk bucket tickets:** Multiple per-engineer Zendesk holder tickets (`SALES-8975`, `SALES-9013`, `SALES-9014`, `SALES-9015`, `SALES-9017`, `SALES-9042`) account for ongoing support load.

---

### Per-Engineer Summary

Counts below are **`status = Done`** in sprint **8591** only.

#### Alex Burton

- **Completed (key — summary — pts):** `SALES-8810` — Backfill NAV VAN on OppIntakeMethod — **1**; `SALES-8962` — Referral In-Territory Validation Error for Address Change Process — **1**; `SALES-8974` — 5/15/26 - 5/25/26 Cohorts — **1**; `SALES-8975` — Alex Zendesk Ticket 5/14 - 5/27 — **2**; `SALES-8980` — Summer 26 Release | Zoom, Address Validation, Lead Assignment, Lead Conversion — **1**; `SALES-9011` — Audit and Update reps missing Zoom URLs — **1**; `SALES-9016` — ALRA Lead Routing — **3**. **Total: 10 pts.**
- **Carried over:** None.
- **Total points completed:** **10**

#### Jummy Sanni

- **Completed (key — summary — pts):** `SALES-8715` — PROD BUG: Cannot Edit Past Appts — **1**; `SALES-8989` — Summer 26 Release | SUMO Scheduling on Lead — **1**; `SALES-8997` — Summer 26 Release | SUMO Scheduling on CLP and Cancelling — **1**; `SALES-8999` — Summer 26 Release | SUMO Scheduling, Update & Cancel on Opp — **1**; `SALES-9010` — SUMO: Enable Create/Edit Past Appt Feature (Staging&PROD) — **2**; `SALES-9015` — Zendesk Tickets 5/14-5/27 — **2**. **Total: 8 pts.**
- **Carried over:** None.
- **Total points completed:** **8**

#### Michael Criswell

- **Completed (key — summary — pts):** `SALES-8876` — Count As New Consignor Formula Field Update — **3**; `SALES-8878` — Update List Price to TRR Price in Commission Calculations — **2**; `SALES-8879` — Keep AUR Accurate for Ship Dates < and > 6/1 — **3**; `SALES-8919` — Update Email Template Referencing List Price — **1**; `SALES-8932` — Create Unit Factor field and update Fractional HC Logic — **1**; `SALES-8958` — Releases: Enable Accessibility Enhancements for Page Headers and Modal Windows When Zoom Is Greater Than 200% — **1**; `SALES-8986` — Summer 26 Release | Add Item — **1**; `SALES-8988` — Summer 26 Release | VO Doc Test — **1**; `SALES-9001` — Upgrade the Security of Your Salesforce Experience — **2**; `SALES-9005` — Incorrect Referral Type Tagging — **2**; `SALES-9062` — Backfill Sales Quota Records — **1**. **Total: 18 pts.**
- **Carried over:** None.
- **Total points completed:** **18**

#### Chris Burns

- **Completed (key — summary — pts):** `SALES-8548` — Bump Builder and Factory classes from API Version 54 to 66 — **2**; `SALES-8551` — Bump Batch classes from API Version 54 to 66 - Ticket 1 of 2 — **2**; `SALES-8800` — Create base LWC for OA — **3**; `SALES-8926` — Create a 90 Day expiration on Referral Records when an opportunity is not closed won — **5**; `SALES-8957` — Releases: Use Visualforce PDF Rendering Service with Apex Blob.toPdf() — **1**; `SALES-9003` — Verify Your Domains for Email Security — **2**; `SALES-9012` — Add Integration Bypass to Address Postal Code Length Validation — **1**; `SALES-9014` — zendesk tickets 5/14 sprint — **2**. **Total: 18 pts.**
- **Carried over:** None.
- **Total points completed:** **18**

#### Grace Saint

- **Completed (key — summary — pts):** `SALES-8831` — Investigate Sumo Batch for not assigning license — **2**; `SALES-8912` — Salesforce Staging Refresh | Real Partners — **1**; `SALES-8936` — Review What Alternate Platforms can Enable Voice Agents — **3**; `SALES-8954` — Update ContactTriggerHandler to set Phone on Open Opps — **1**; `SALES-8955` — Releases: Enable Accessibility Enhancements for Date Pickers, Popovers, Bottom Utility Bars, Record Headers — **1**; `SALES-8981` — Summer 26 Release| Real Partners — **1**; `SALES-9006` — Salesforce Validations Part II — **1**; `SALES-9017` — Grace Zendesk Tickets 5/14 - 5/27 — **1**; `SALES-9023` — SGO IS Leads Not Populating Correctly — **1**; `SALES-9040` — Pull 20th of Month Real Partner Reports — **1**. **Total: 13 pts.**
- **Carried over:** None.
- **Total points completed:** **13**

#### Navinchandra Gupta

- **Completed (key — summary — pts):** `SALES-8875` — Clean up Q1 Epics — **2**; `SALES-9004` — Update Unsupported Platform SOAP API login() — **2**; `SALES-9018` — Q2-2026 User Access Reviews (UAR): May 29, 2026 — **2**; `SALES-9019` — Certification:   Sales Cloud Uncorrelated User Access Review Q2 2026 — **1**; `SALES-9020` — Certification:   Manager's User Access Review - Q2 2026 — **1**; `SALES-9042` — Zendesk Bug Ticket Holder (May 14 - May 27) — **2**. **Total: 10 pts.**
- **Carried over:** None.
- **Total points completed:** **10**

#### Nag Malluru

- **Completed (key — summary — pts):** `SALES-8935` — Update Voice Agent Design to Account for Requirements — **2**; `SALES-8978` — Integration Landscape and Data Flow Diagrams — **3**; `SALES-8983` — Summer 26 Release | Shipping Happy Path — **1**; `SALES-8993` — Summer 26 Release | Slack - HelloSign — **1**; `SALES-9013` — Nag - Zendesk Tickets 5/14-5/27 — **2**. **Total: 9 pts.**
- **Carried over:** None.
- **Total points completed:** **9**

#### Gustavo Silva

- **Completed (key — summary — pts):** `SALES-8976` — SlackPlatformEventTriggerHandler | An unhandled fault has occurred in this flow — **1**; `SALES-8982` — Summer 26 Release | SF - Admin Sync — **1**; `SALES-8984` — Summer 26 Release | Vendor Bulk Upload — **1**; `SALES-8985` — Summer 26 Release - Funnel testing in staging after the css fix — **1**; `SALES-9008` — Multiple duplicate opportunities being created using the New Opportunity button on the contact — **1**; `SALES-9009` — [2026-05-14]Force Sync of Consignment Items from Admin to Salesforce — **1**; `SALES-9022` — [2026-05-15]Force Sync of Consignment Items from Admin to Salesforce — **1**; `SALES-9026` — [2026-05-19]Force Sync of Consignment Items from Admin to Salesforce — **1**; `SALES-9044` — [2026-05-20]Force Sync of Consignment Items from Admin to Salesforce — **1**; `SALES-9045` — push_topic.cls not running on mac when finalizing the deploy.sh script — **1**; `SALES-9059` — Troubleshoot and fix sfConvertLeadApptWizard.test.js in the qe-mocha-automation repo — **1**; `SALES-9061` — Retry oban jobs of leads that failed to convert from supply from 2026-05-19 — **1**; `SALES-9063` — Addresses not being saved correctly when using the edit button on the layout — **1**; `SALES-9064` — bump GitHub Actions pins for Node 20 deprecation on setup-sfdx action — **1**; `SALES-9065` — Improve error handling of OpportunityTriggerHelper.updateContactOwner — **1**; `SALES-9066` — InquiryFinalize exceptions being sent through email and not to bugsnag — **1**; `SELLTECH-1050` — Create a batch job to calculate Booster NC Credit on Opportunity — **3**; `SELLTECH-1051` — Update Record Trigger: Consignment Order Items Object (Comp Calc) to use new logic — **2**. **Total: 21 pts.**
- **Carried over:** None.
- **Total points completed:** **21**

#### Sai Deepika Kanuri

- **Completed (key — summary — pts):** `SALES-8877` — Update the Retail Value Credit Formula on Comp Calculation Record for Boosted NC Credit — **2**; `SALES-8950` — GM Quota Discount — **2**; `SALES-8990` — Summer 26 Release | Commissions — **1**; `SALES-9027` — Backfill NC Count data and Recalculate value credit — **1**. **Total: 6 pts.**
- **Carried over:** None.
- **Total points completed:** **6**

---

### Discussion Prompts

1. **Velocity jumped from 90 → 113 pts while sprint issue count grew to 88.** How much of that uplift was **Summer '26 release QA tickets** (`SALES-8980`–`SALES-9000`) vs **net-new product work**, and should release validation be **pre-planned as its own capacity lane**?
2. **Only 33 / 118 sprint points carry `SRT-Product` (28.0%).** Which completed comp/quota items (`SALES-8876`–`SALES-8879`, `SELLTECH-1050`/`1051`) were true product work but **missing labels**?
3. **Zero carry-over despite 75 completions — but `SALES-8551` resolved 2026-06-03 and `SALES-8978` resolved 2026-05-28 after sprint end.** Should the team adopt a **hard rule** that sprint closure requires resolution within sprint boundaries, or accept **administrative tail** for multi-sprint items?
4. **19 bugs closed with zero “Reason for Bug” in Jira.** Do we gate **Done** transitions on `customfield_10142` for bugs (same gap as sprint 8190)?
5. **0 Summer '26 tickets were bulk-created 2026-05-12, two days before sprint start.** Could **release checklists** be templated earlier so QA scope does not appear as a **surprise batch** at sprint boundary?
