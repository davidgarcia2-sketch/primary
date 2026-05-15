# SRT Sprint Retrospective — SALES board (Sprint 8190)

**Data source:** Jira project `SALES`, sprint **SALES 4/30 - 5/13** (ID `8190`, board ID `10`). Snapshot reflects issues as queried after sprint closure. **PT-** and **SELLTECH-** issues were also checked for membership in sprint `8190` via JQL; **no issues in those projects were on this sprint**. Cross-project links do exist on some SALES tickets (example: `SALES-8878` changelog shows links to `SELLTECH-1051`, `SELLTECH-1036`).

---

### Executive Summary

The sprint delivered **high throughput** against a **very large, refresh-heavy scope**: **55** issues reached **Done** totaling **90** story points, with the sprint goal explicitly centered on **Salesforce staging refresh**, **June 1 commission work**, **data parity**, and **intake automation**. The biggest win is **clean execution of the staging-refresh workstream** (many parallel sub-items closed early in the sprint). The biggest concern is **portfolio hygiene**: only **6** of **102** currently estimated sprint points carry an **`SRT-Product`** label, so **capacity reporting against SRT buckets is mostly “unclassified”** unless labeling discipline improves. **Committed points at sprint start**, **full mid-sprint add/remove inventory**, and **scope change %** require a **changelog pass across all sprint issues** (not fully automated in this run); one illustrative deep dive is documented for **`SALES-8878`**.

---

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | SALES 4/30 - 5/13 |
| Sprint Dates | **2026-04-30** 16:40 UTC → **2026-05-13** 07:00 UTC (per Jira sprint object on `SALES-8709`; completed date recorded **2026-05-14** 15:59 UTC) |
| Committed Points | **Unavailable without batch changelog replay at sprint start** (see Key Findings). |
| Completed Points | **90** (sum of `customfield_10026` for `sprint = 8190 AND status = Done`; **55** Done issues) |
| Carry-Over (tickets / points) | **5** / **11** counted points (**`SALES-8968`** is **unestimated**) — tickets: **`SALES-8831`** (Code Review, 2), **`SALES-8920`** (To Do, 3), **`SALES-8926`** (Code Review, 5), **`SALES-8954`** (Code Review, 1), **`SALES-8968`** (To Do, unestimated). *Won’t Do items are excluded from carry-over.* |
| Removed (tickets / points) | **Unavailable** from search alone (requires parsing sprint removal events from each issue changelog). Jira does not expose a single “Removed” status in this dataset. |
| Added Mid-Sprint (tickets / points) | **Partially available via changelog** — not exhaustively computed for all **56** sprint issues in this run. |
| Scope Change % | **Unavailable** (depends on committed-at-start baseline and net adds/removes). |
| Spikes Closed | **3** (`SALES-8829`, `SALES-8933`, `SALES-8967`) |
| Bugs Closed | **14** (`issuetype = Bug` and `status = Done` in sprint `8190`) |

---

### Capacity Allocation Breakdown

**Method:** Each sprint issue counted **once**. **Product** if labels contain `SRT-product`, `SRT-Product`, or `SRT-RO` (case-sensitive match to observed `SRT-Product`). **Tech Health** if `SRT-Domain-Tech-Debt` or `SRT-Software-Upgrades`. **KTLO** if `SRT-KTLO`. Otherwise **Buffer / Unplanned**. Denominator = **102** (sum of story points on all **56** sprint issues, treating `null` as **0**).

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|-----------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | **6** | **5.9%** | **−28.1 pts vs target** |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | **0** | **0%** | **−11 pts** |
| KTLO (SRT-KTLO) | 16% | ~11 | **0** | **0%** | **−11 pts** |
| Buffer / Unplanned | 20% | ~14 | **96** | **94.1%** | **+82 pts vs target** |

**KTLO > 30% flag:** **No** — **0%** of sprint points carried `SRT-KTLO` in Jira labels for this sprint.

**Interpretation:** The team likely performed substantial **product and KTLO-class work** that is **not labeled** for SRT capacity tracking. This table reflects **labels in Jira**, not intent.

---

### Key Findings

#### Scope Creep & Mid-Sprint Changes

- **Full list (all tickets):** **Not produced in this run** (requires `getJiraIssue` + `expand=changelog` for all **56** keys, then filtering `fieldId=customfield_10020` and `customfield_10026` after `2026-04-30T16:40:43.772Z`).
- **Illustrative verified example — `SALES-8878` (“Update List Price to TRR Price in Commission Calculations”):**
  - **Added to sprint mid-flight:** Changelog shows sprint set to **`SALES 4/30 - 5/13`** on **2026-05-04** (after sprint start on **2026-04-30**), moved from **Parking Lot Sprint** (`fromString` empty in one entry; paired entry shows move from Parking Lot).
  - **Story point changes after sprint start:** On **2026-05-06**, **Michael Criswell** changed story points **4 → 1**, then **1 → 2** (net **4 → 2** vs earlier estimate), with author **Michael Criswell**.
  - **Also rolled into next sprint:** On **2026-05-14**, **Navinchandra Gupta** updated sprint from **`8190`** to **`8190, 8591`** (“Sales 5/14 - 5/27”) while still completing the ticket **Done** on **2026-05-15** (after the sprint’s nominal end timestamp).
- **Label change:** **2026-05-14**, **Bryan Claggett** added **`SRT-Product`** to `SALES-8878`.

**Pattern (tentative):** The sample points to **legitimate scope refinement** (estimate tightening) and **cross-sprint continuity** for a high-priority commission item, not random churn.

#### Velocity & Throughput

| Sprint | Jira sprint id | Done points (SALES, `status = Done`) |
|--------|----------------|--------------------------------------|
| **Current** | **8190** | **90** |
| Prior | **7949** | **108** (62 tickets with points; `SALES-7065` has **null** points) |
| Prior | **7548** | **83** (48 Done tickets) |

**Trend:** **Down** from **108 → 90** vs the immediately prior sprint, **up** vs **7548** (**83**). A **third** comparison sprint was not reliably retrieved in this environment (older sprint query returned empty). **PTO / holidays / staffing** were **not** pulled from HR systems.

#### Burndown Analysis

Using **`resolutiondate`** on **`status = Done`** issues in sprint **8190**:

- **Early progress:** Multiple staging-refresh and operational items closed **2026-04-30 through 2026-05-06** (for example `SALES-8908` on **2026-04-30**, several **May 4** closures).
- **Mid sprint:** Steady closures **May 5–May 8** (for example `SALES-8964` on **May 8**).
- **Late-heavy:** A **concentrated cluster** of closures **May 11–May 13** (for example multiple items for **Jummy Sanni** and **Gustavo Silva** on **May 11–May 12**, **Grace Saint** on **May 12–May 13**).
- **Post–sprint-end Done timestamps:** **`SALES-8878`** and **`SALES-8919`** show **`resolutiondate` on 2026-05-15** (after the sprint’s configured **endDate** of **2026-05-13**), which **flattens a classic burndown** if the chart strictly uses sprint boundaries.

**Shape:** Mixed — **not a pure flatline first week**, but **material “finish line” clustering in the last ~3 days**, with **some administrative tail after sprint end**.

#### Bug Analysis

- **Bugs closed (Done):** **14** issues.
- **Reason for Bug (`customfield_10142`):** **Unavailable / not populated** — Jira returned **`null`** for **all 14** closed bugs queried in sprint **8190**.

---

### Per-Engineer Summary

Counts below are **`status = Done`** in sprint **8190** only. **Carry-over** = **`Code Review`** or **`To Do`** at query time (excludes **Won’t Do**).

#### Alex Burton

- **Completed (key — summary — pts):** `SALES-8890` — Update First Date Received into Warehouse Validation for GPN Opportunities — **1**; `SALES-8902` — Salesforce Staging Refresh | Zoom, Address Validation, Lead Assignment, Lead Conversion — **3**; `SALES-8929` — April EOM Updates — **2**; `SALES-8930` — 5/4/26 - 5/11/26 Cohorts — **1**; `SALES-8934` — Alex Zendesk Ticket 4/30 - 5/13 — **2**. **Total: 9 pts.**
- **Carried over:** `SALES-8968` — May.'26 SUMO Sync Issue — **unestimated** (To Do).
- **Total points completed:** **9**

#### Jummy Sanni

- **Completed:** `SALES-8898` — Salesforce Staging Refresh | SUMO Config & Scheduling on Lead — **3**; `SALES-8899` — Salesforce Staging Refresh | SUMO Scheduling on Opportunity — **1**; `SALES-8952` — Salesforce Staging Refresh | SUMO Scheduling Cancels & Reschedule — **1**; `SALES-8972` — SF Staging Refresh | Stabilize SUMO Stage Setup After Refresh & Capture Notes — **1**. **Total: 6 pts.**
- **Carried over:** None in the carry-over set above.
- **Total points completed:** **6**

#### Michael Criswell

- **Completed:** `SALES-8709` — Referral Data Backfill & Cleanup (Post–Referral Types Implementation) — **2**; `SALES-8878` — Update List Price to TRR Price in Commission Calculations — **2**; `SALES-8891` — Salesforce Staging Refresh | Vendor Bulk Upload — **1**; `SALES-8895` — Salesforce Staging Refresh | Add Item — **1**; `SALES-8896` — VO Doc Test — **1**; `SALES-8914` — Add Custom Setting To Disable Logging For RestReturnSumoProviders — **1**; `SALES-8919` — Update Email Template Referencing List Price — **1**; `SALES-8927` — Create RT: AS Trigger to update Opp. Intake Method to Nav Van Pickup — **2**; `SALES-8928` — Add bypass setting for bugsnag logging of ZoomSyncPlatformEventTriggerHandlerException — **2**. **Total: 13 pts.**
- **Carried over:** None.
- **Total points completed:** **13**

#### Chris Burns

- **Completed:** `SALES-8911` — T334482 - As a sales rep create a self-generated referral… — **1**. **Total: 1 pt.**
- **Carried over:** `SALES-8926` — Create a 90 Day expiration on Referral Records… — **5** (Code Review).
- **Total points completed:** **1**

#### Grace Saint

- **Completed:** `SALES-8824` — Salesforce Data Cleanliness: Validations — **2**; `SALES-8923` — Upload Campaign Members for May Monthly Promos — **1**; `SALES-8939` — Zendesk Ticket 4/30 - 5/13 — **2**. **Total: 5 pts.**
- **Carried over:** `SALES-8831` — Investigate Sumo Batch for not assigning license — **2** (Code Review); `SALES-8954` — Update ContactTriggerHandler to set Phone on Open Opps — **1** (Code Review).
- **Total points completed:** **5**

#### Navinchandra Gupta

- **Completed:** `SALES-8829` — Research the Capabilities of In-Person Meeting Assistant — **2**; `SALES-8882` — Pasadena, CA Site Setup for 5/14-5/15 — **1**; `SALES-8885` — Retail Site Creation - Pop up stores: Alexandria, VA 5/14-5/16 — **1**; `SALES-8897` — Salesforce Staging Sandbox Refresh April 25th 2026 — **3**; `SALES-8907` — Salesforce Staging Configurations — **2**; `SALES-8940` — Zendesk Tickets — **2**; `SALES-8944` — Grant Sys Admin Access to Michael Criswell to do Referral Backfill — **1**; `SALES-8947` — Salesforce Login Issue Production — **1**; `SALES-8949` — Update Pager Duty Schedules for Salesforce tickets — **1**. **Total: 14 pts.**
- **Carried over:** None.
- **Total points completed:** **14**

#### Nag Malluru

- **Completed:** `SALES-8901` — Salesforce Staging Refresh | Slack — **1**; `SALES-8906` — Salesforce Staging Refresh | HelloSign — **1**; `SALES-8922` — Pardot Automation Sync/Custom Field Failure — **2**; `SALES-8933` — Discovery: Design for Heavily Computed Fields in Big Query — **2**; `SALES-8942` — Nag - Zendesk Bucket — **2**. **Total: 8 pts.**
- **Carried over:** None.
- **Total points completed:** **8**

#### Gustavo Silva

- **Completed:** `SALES-8892` — Salesforce Staging Refresh | Shipping Happy Path — **1**; `SALES-8894` — Salesforce Staging Refresh | SF - Admin Sync — **1**; `SALES-8908` — Salesforce Staging Anonymization — **5**; `SALES-8909` — Salesforce Staging Refresh | SUMO Scheduling on CLP — **1**; `SALES-8938` — TRR Price Inaccuracy — **5**; `SALES-8946` — Perform changes to batch_anonymize_data.sh and setupSandbox.sh scripts — **1**; `SALES-8948` — Opportunity and COIs are not syncing with admin… — **1**; `SALES-8953` — Opp Sync Error spree user cannot be found… — **1**; `SALES-8964` — Re-enable Salesforce tests — **2**; `SALES-8967` — How can we activate and use the L4 Taxon in Salesforce — **2**; `SALES-8970` — Create Cursor skills folder in salesforce-crm repo — **2**; `SALES-8971` — Fix sfConvertLeadApptWizard.test.js — **2**; `SALES-8977` — List of Active Consignors from our Duplicates found — **2**; `SALES-8979` — Sumo Calendar not rendering correctly in Funnel Staging after SF Staging Refresh — **1**. **Total: 29 pts.**
- **Carried over:** None.
- **Total points completed:** **29**

#### Sai Deepika Kanuri

- **Completed:** `SALES-8903` — Salesforce Staging Refresh | Commissions — **1**; `SALES-8943` — Deepika Zendesk Ticket 4/30 - 5/13 — **2**; `SALES-8945` — Sales Quota mOnthly upload — **1**. **Total: 4 pts.**
- **Carried over:** `SALES-8920` — Update reporting to reflect TRR Price instead of List Price — **3** (To Do).
- **Total points completed:** **4**

---

### Discussion Prompts

1. **`SALES-8878` was added on 2026-05-04 and estimates moved 4 → 2 during the sprint (Michael Criswell).** Was the **Parking Lot → sprint promotion** the right timing, or should commission work have been **pre-planned into sprint planning** to avoid mid-sprint board motion?
2. **Only 6 / 102 sprint points carry `SRT-Product`.** Which **completed** items this sprint were **true product roadmap work** but missing labels, and can we **backfill + enforce** at sprint planning going forward?
3. **Carry-over is concentrated in multi-point items (`SALES-8926` 5 pts, `SALES-8920` 3 pts) plus an unestimated `SALES-8968`.** What **specific blockers** prevented **`SALES-8926`** and **`SALES-8831`** from leaving Code Review before sprint end?
4. **14 bugs closed with zero “Reason for Bug” data in Jira.** Do we want to **gate Done transitions** on `customfield_10142` for bugs so retro analytics stay actionable?
5. **Velocity dipped 108 → 90 vs sprint `7949` while scope included a major refresh program.** Should the team treat **staging refresh programs** as a **separate reporting lane** so product velocity comparisons stay meaningful sprint-to-sprint?
