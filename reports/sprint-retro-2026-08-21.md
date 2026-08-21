# Sales 8/6 - 8/19 (Aug 6, 2026 - Aug 19, 2026)

---

## Part A: Metrics Report

### Executive Summary

Sales 8/6 - 8/19 closed clean. Zero carry-over tickets, 109 of 109 resolved in sprint, and Navin confirmed a spotless board on Aug 19 in #srt-core-team. The biggest win is the first fully clean sprint close since the process reset, with 153 completed points (manual) while the team ran post-ALRA hypercare, API version bumps, and ongoing SUMO support. The biggest concern is capacity inversion: Tech Health landed at 55% of completed work against a 16% target, driven by the API 54-to-65 bump batch and a mid-sprint DevQA clone wave that added 39 tickets and 42% scope change.

### Sprint Metrics Table

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 8/6 - 8/19 |
| Sprint Dates | Aug 6, 2026 - Aug 19, 2026 |
| Committed Points | [OPEN QUESTION: Jira sprint report not available via API. Aug 3-7 weekly status cited 93 points committed for this sprint. Manual count of 70 tickets created before sprint start shows 111 points. Reconcile in sprint report before the meeting.] |
| Completed Points | 153 (Sales 8/6 - 8/19). Manual cross-check: 144 Done + 9 Won't Do resolved in sprint window. [OPEN QUESTION: confirm against Jira sprint report velocity view.] |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | TBD / TBD [OPEN QUESTION: sprint changelog not available via API. Verify in Jira sprint report.] |
| Added Mid-Sprint (tickets / points) | 39 / 47 |
| Scope Change % | 42.3% (47 pts added / 111 pts at sprint start) |
| Spikes Closed | 11 |
| Bugs Closed | 21 |

### Capacity Allocation (Sales 8/6 - 8/19, based on 153 completed points vs ~70 pt capacity target)

| Bucket | Target % | Target Points | Actual Points | Actual % | Delta |
|--------|----------|---------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 22 | 14.4% | -12 |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 84 | 54.9% | +73 |
| KTLO (SRT-KTLO) | 16% | ~11 | 45 | 29.4% | +34 |
| Buffer / Unplanned | 20% | ~14 | 2 | 1.3% | -12 |

KTLO at 29.4% is just under the 30% alert threshold, but combined with Tech Health at 55%, only 14% of completed work was product-facing. SRT labels were sparse on most tickets; bucket assignment inferred from Zendesk bucket naming (KTLO/TD/SU&TC), parent epic keywords, and ALRA/SUMO ticket titles. [ASSUMPTION: DevQA clone tickets inherit parent bucket.]

### Key Findings

#### Scope creep and mid-sprint changes

39 tickets (47 points) were created after sprint start on Aug 6. The dominant pattern was reactive process, not priority shifts.

**DevQA clone batch (Aug 12-19):** After the API version bump tickets (SALES-8554 through SALES-8562) moved through dev, a batch of DevQA clones landed mid-sprint: SALES-9574, SALES-9576, SALES-9587, SALES-9588, SALES-9592, SALES-9600, SALES-9601, SALES-9607, SALES-9608, SALES-9609, SALES-9618, SALES-9619, SALES-9621, SALES-9626, SALES-9627, SALES-9632, SALES-9636, SALES-9642 (1 pt each, 18 tickets). These were predictable at planning if the team standard is one DevQA ticket per parent. Creating them after parent completion inflated scope by ~18 points after Aug 12.

**Reactive support and KTLO:**
- SALES-9603 (2 pts, Jummy): ZD Support bucket 8/6-8/19, added mid-sprint
- SALES-9606 (1 pt, Gus): Inquiries not syncing from supply
- SALES-9633 (1 pt, Gus): Commission may be wrong
- SALES-9637 (4 pts, Nag): CLONE - Zendesk to JSM Discovery
- SALES-9656 (5 pts, Nag): CLONE - Lean Data and Sumo Redesign engineering assessment

**Product/ALRA mid-sprint:**
- SALES-9580 (1 pt, Alex): ALRA Test Scenarios Retest
- SALES-9585 (1 pt, Gus): Boosted NC Credit flag bug
- SALES-9643 (2 pts, Gus): Required fields for funnel lead creation

**Removed tickets:** TBD. [OPEN QUESTION: verify in Jira sprint report.]

**Re-pointed tickets:** TBD. [OPEN QUESTION: no changelog access via API. Spot-check any tickets whose current points differ from planning notes.]

**Pattern assessment:** Mostly weak grooming on DevQA clones (should exist at sprint start) plus reactive KTLO/support. The Nag discovery clones (SALES-9637, SALES-9656) reflect legitimate mid-sprint priority additions tied to sprint goal #6 (Zendesk to JSM Discovery) and Flexible Sales Routing research.

#### Velocity and throughput

| Sprint | Completed Points (manual/API) | Notes |
|--------|-------------------------------|-------|
| Sales 6/25 - 7/8 | 109 [OPEN QUESTION: confirm in sprint report] | Pre-ALRA baseline |
| Sales 7/9 - 7/22 | 124 (SRT Team Development Process doc) | 104 committed per same doc |
| Sales 7/23 - 8/5 | 132 (Weekly Status Report Aug 3-7) | ALRA go-live sprint, 12-sprint record at the time |
| Sales 8/6 - 8/19 | 153 (manual) | New high, zero carry-over |

Trending up across four sprints (+44 points over eight weeks). Factors: team hitting stride on process hygiene, Mike and Gus clearing the API bump batch, and Won't Do used to close out descoped work (11 tickets, 9 pts) rather than carrying it forward. Offsetting factors: Grace departed Jul 15 (not in this sprint), mid-year talent reviews consumed David's bandwidth Aug 14-19, and DevQA clone inflation makes raw point totals harder to compare sprint to sprint.

#### Burndown shape

Late-heavy. Only 5 points closed on sprint day Aug 6. Steady middle weeks (10-15 pts/day Aug 7-14). Then a rush: 14 pts Aug 17, 27 pts Aug 18, 34 pts Aug 19 (22% of all completed points on the last day).

Navin flagged 58% completion on Aug 17 (#srt-core-team). The team closed the remaining 42% in two days, which is impressive throughput but confirms the flatline-then-rush pattern the process reset was meant to fix.

#### Bug analysis

21 bugs closed. Reason for Bug (`customfield_10142`) was **Not Set on all 21**. No grouping possible.

Closed bugs include: SALES-6448, SALES-6818, SALES-6877, SALES-9211, SALES-9250, SALES-9251, SALES-9252, SALES-9253, SALES-9383, SALES-9519, SALES-9522, SALES-9531, SALES-9537, SALES-9552, SALES-9563, SALES-9564, SALES-9565, SALES-9572, SALES-9585, SALES-9606, SALES-9633.

Process target: populate Reason for Bug before closing. The field has been unpopulated across multiple sprints. [ASSUMPTION: team skips the field because it is optional in the workflow.]

Notable bugs:
- SALES-9531 (Deepika, Done Aug 11): SUMO appointment booking error and Google calendar sync failure. Multiple Zendesk tickets linked. Sprint goal #2 item.
- SALES-9537 (Navin, Done Aug 14): SailPoint ECA authorization failure in production. Tied to Jul 31-8/1 lockout incident.
- SALES-9522 (Deepika, Done Aug 3): Pre-sprint resolution but ticket was in this sprint board.

### Per-Engineer Summary (Sales 8/6 - 8/19)

#### Alex Burton: 15 pts completed, 0 carry-over

Completed: SALES-9458 (2 pts, RevOps Demo LeanData/Sumo routing), SALES-9483 (2 pts, HV Escalation reporting), SALES-9502 (1 pt, BDR Dashboard hierarchy), SALES-9510 (1 pt, Direct Manager field on Leads), SALES-9525 (2 pts, BDR credit misattribution), SALES-9526 (1 pt, ALRA for SGO metadata), SALES-9540 (1 pt, Tech Debt ZD bucket), SALES-9544 (1 pt, SW Upgrades ZD bucket), SALES-9548 (2 pts, KTLO ZD bucket), SALES-9553 (1 pt, Cohorts 8/10-8/17), SALES-9580 (1 pt, ALRA Test Scenarios Retest, Won't Do).

Carry-over: none.

#### Jummy Sanni: 12 pts completed, 0 carry-over

Completed: SALES-6818 (1 pt, SUMO confirmation emails), SALES-8461 (2 pts, Opp close error), SALES-9383 (2 pts, Multi Calendar Issue), SALES-9469 (2 pts, SUMO page loadtime clone), SALES-9583 (1 pt, SUMO Flow Audit, Won't Do), SALES-9600 (1 pt, DevQA Buyer Profile picklist), SALES-9603 (2 pts, ZD Support 8/6-8/19), SALES-9642 (1 pt, DevQA HV Escalation reporting).

Carry-over: none.

#### Michael Criswell: 33 pts completed, 0 carry-over

Completed: SALES-8554 through SALES-8562 (2 pts each, API version bump batch, 9 tickets), SALES-9211 (2 pts, ContractTrigger PDF error), SALES-9252 (2 pts, sfDupLeadMatchedContact test fix), SALES-9253 (2 pts, sfEditLead test fix), SALES-9529 (1 pt, LCO NAV backfill), SALES-9558, SALES-9560, SALES-9562, SALES-9566, SALES-9592, SALES-9609, SALES-9626, SALES-9632 (1 pt each, DevQA clones).

Carry-over: none.

#### Chris Burns: 13 pts completed, 0 carry-over

Completed: SALES-6448 (2 pts, Incorrect Owner Post Conversion, Won't Do), SALES-6877 (2 pts, Lead Convert Dupe Contact, Won't Do), SALES-9332 (3 pts, Profiles/PS/PSG spike), SALES-9492 (1 pt, Buyer Profile picklist), SALES-9493 (2 pts, High Value LWC null indicator), SALES-9552 (1 pt, Skip Loss Reason for Buyer), SALES-9573 (2 pts, Gemini sandbox POC).

Carry-over: none.

#### Grace Saint: 0 pts completed, 0 carry-over

No tickets assigned in this sprint. Last day was Jul 15, 2026.

#### Navinchandra Gupta: 17 pts completed, 0 carry-over

Completed: SALES-9345 (2 pts, Palm Beach relocation), SALES-9405 (2 pts, San Jose event site), SALES-9406 (1 pt, Alexandria event site), SALES-9434 (2 pts, Email Opt Out Pardot fix), SALES-9528 (2 pts, Real Partner Reports), SALES-9537 (2 pts, SailPoint ECA failure), SALES-9586 (1 pt, HV Designer list view), SALES-9594 (1 pt, DevQA Loss Reason skip), SALES-9605 (1 pt, HV Designer admin permission), SALES-9620 (1 pt, Consign Offers campaign), SALES-9631 (1 pt, QA 6448), SALES-9647 (1 pt, SOX access provisioning clone).

Carry-over: none.

#### Nag Malluru: 16 pts completed, 0 carry-over

Completed: SALES-9527 (2 pts, Retail Gifting sizing), SALES-9563 (1 pt, ZD KTLO bucket), SALES-9564 (1 pt, ZD Tech Debt bucket), SALES-9565 (1 pt, ZD SW Upgrades bucket), SALES-9572 (1 pt, Google Sheets connector), SALES-9577 (1 pt, History Objects follow-up), SALES-9637 (4 pts, Zendesk to JSM Discovery clone), SALES-9656 (5 pts, LeanData/Sumo redesign assessment clone).

Carry-over: none.

#### Gustavo Silva: 36 pts completed, 0 carry-over

Completed: SALES-8546, SALES-8547 (1 pt each, API 63/64 to 65 bump), SALES-9250, SALES-9251 (2 pts, 1 pt, test fixes), SALES-9302 (1 pt, DevQA SUMO loadtime, Won't Do), SALES-9409 (2 pts, Lead expiry research), SALES-9538 (3 pts, Slug matching research), SALES-9561 (2 pts, SF store phone leads), SALES-9567 (1 pt, Zipcode discovery), SALES-9574, SALES-9576, SALES-9587, SALES-9588, SALES-9601, SALES-9607, SALES-9608, SALES-9618, SALES-9619, SALES-9621, SALES-9627, SALES-9636 (1 pt each, DevQA clones), SALES-9575 (2 pts, Deprecate CreateVanPickup, Won't Do), SALES-9585 (1 pt, Boosted NC Credit), SALES-9593 (1 pt, Available_Date backfill), SALES-9598 (1 pt, Fake lead data), SALES-9606 (1 pt, Supply inquiry sync), SALES-9614 (1 pt, Boosted NC backfill), SALES-9633 (1 pt, Commission error), SALES-9643 (2 pts, Funnel lead required fields).

Carry-over: none.

#### Sai Deepika Kanuri: 11 pts completed, 0 carry-over

Completed: SALES-7924 (1 pt, SUMO workflow check), SALES-9531 (1 pt, SUMO booking/calendar sync incident), SALES-9532 (2 pts, Orphan Comp Calcs), SALES-9533 (5 pts, Merging Comp Calcs with COI), SALES-9570 (1 pt, ALRA Phase 2 placeholder), SALES-9582 (1 pt, Comp Credit Backfills).

Carry-over: none.

#### Jenn Kleinfeld: 0 pts completed, 0 carry-over

No SALES sprint tickets assigned. Product partner work tracked outside sprint board (SALES-9625 access discussion, ALRA docs, Flexible Sales Routing meetings).

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

**Navin and the full team for the clean sprint close.** Zero carry-over, 109/109 resolved, and Navin posted the clean board screenshot in #srt-core-team on Aug 19. This is the outcome the process reset has been driving toward since June.

**Mike for the API bump marathon.** SALES-8554 through SALES-8562 plus test fixes (SALES-9252, SALES-9253) and 8 DevQA clones. 33 points, all closed. This was the bulk of the Tech Health overrun and he carried it without dropping KTLO work.

**Gus for volume and test automation.** 36 points across API bumps, DevQA, backfills, and research spikes. His routing test automation (100+ records in hours) was called out in the Aug 3-7 weekly status as a team standard going forward.

**Deepika for SUMO incident response.** SALES-9531 (booking errors + calendar sync) resolved Aug 11 with multiple Zendesk tickets attached. She also closed SALES-9533 (5 pts, Comp Calcs merge) and kept ALRA Phase 2 discussions moving (SALES-9570).

**Alex for the RevOps demo and LeanData routing analysis.** SALES-9458 (RevOps Demo) closed Aug 19. When the LeanData routing escalation hit on Aug 10 (#srt-core-team), Alex pulled assignment data from report 00OUv000002xZBtMAM and answered Bryan's questions with rep-level distribution detail inside two hours.

**Nag for discovery work under pressure.** SALES-9637 (Zendesk to JSM, 4 pts) and SALES-9656 (LeanData/Sumo redesign assessment, 5 pts) were both mid-sprint adds that closed before sprint end. He also got ALRA docs into David's folder on Aug 19 before signing off early.

### 2. What went well

**First zero carry-over sprint.** Every ticket on the board is Done or Won't Do. No In Progress, no To Do left behind. Navin's Aug 19 message in #srt-core-team called this out explicitly.

**Post-ALRA hypercare stayed stable.** Sprint goal #1 (ALRA Project Work) continued without a production rollback. SALES-9580 (ALRA retest) was descoped to Won't Do, which is honest scope management rather than carry-over.

**SailPoint production fix landed.** SALES-9537 (SailPoint ECA authorization failure) closed Aug 14. Navin tied the Jul 31-8/1 lockout incident to a known SailPoint bug in #srt-core-team on Aug 10 and pointed to SALES-9557 for the permanent fix still in progress.

**Process docs consolidated.** 14 SRT process documents merged into 3 living docs (per Aug 3-7 weekly status). Pre-Sprint Ticket Review Funnel published Aug 13 in Notion.

**Developer access restored quickly.** Chris flagged removal from GitHub, Cursor, and Jira on Aug 19 (#srt-core-team). Access was restored same day after SR ticket.

### 3. What needs work

**Capacity model is inverted.** Product at 14% vs 48% target. Tech Health at 55% vs 16% target. The API bump was planned, but the DevQA clone wave was not counted at planning time, which makes the sprint look like a Tech Health sprint when the team intended mixed work.

**42% scope change.** 39 mid-sprint adds, mostly DevQA clones created Aug 12-19 after parent tickets finished. This is the same pattern flagged in prior retros. The Pre-Sprint Ticket Review Funnel (published Aug 13) exists to prevent this, but it was not enforced for DevQA pairs in this sprint.

**Late-heavy burndown.** 61 of 153 points (40%) closed in the last three days. Navin flagged 58% on Monday Aug 17. The team delivered, but the shape means standup progress metrics are misleading until sprint end.

**Reason for Bug is blank on every closed bug.** 21 bugs closed, zero populated. We cannot do root cause trending until this field is mandatory.

**KTLO near the alert line at 29.4%.** Zendesk bucket tickets (SALES-9548, SALES-9563, SALES-9564, SALES-9565, SALES-9603) plus reactive bugs (SALES-9531, SALES-9606, SALES-9633) kept support load high while the team also ran Tech Health work.

**Incident response still reactive.** SUMO booking/calendar sync (SALES-9531, Aug 11), SailPoint lockout fallout (Jul 31-8/1, SALES-9557 still open), and LeanData routing imbalance (Aug 9-10, Zendesk 134163) all arrived as escalations rather than planned sprint work.

**Manager confirmation pending.** [OPEN QUESTION: Prashanth Patlolla is listed as Director on leave in the template. SRT Team Development Process and action items reference Prashanth. Confirm whether Kishore Kumar Mohan or another interim manager is active.]

### 4. Discussion Topics

1. **DevQA clones added 18+ points mid-sprint (SALES-9574 through SALES-9642).** The retro agreed last sprint to create DevQA tickets at planning. Mike closed 9 parent API bump tickets, then 8 DevQA clones appeared Aug 12-19. Should we block parent ticket closure until the DevQA pair exists, or accept the scope inflation?

2. **Tech Health at 55% vs 16% target.** SALES-8554 through SALES-8562 alone are 18 points of API bump work. Is the 16% Tech Health target realistic while SOX, SailPoint, and API compliance tickets run concurrently, or do we need to re-baseline the capacity model for a 7-person team?

3. **KTLO at 29.4%, trending toward the 30% alert.** SALES-9603 (ZD Support), SALES-9563-9565 (Nag ZD buckets), and reactive bugs SALES-9531 and SALES-9606 drove this. Does the weekly unassigned ticket queue rotation (SRT Action Items Tracker, first handoff Aug 28) actually reduce sprint KTLO, or just triage faster?

4. **SALES-9531 SUMO incident vs sprint goal #2.** The SUMO guest user and multi-calendar work was a stated sprint goal, and SALES-9531 (booking + calendar sync) ate unplanned capacity Aug 7-11. Sumo was flagged for replacement in the prior retro. Does this sprint's data strengthen the case to pull Flexible Sales Routing research forward?

5. **Zero carry-over at the cost of 11 Won't Do tickets (9 pts).** SALES-9580 (ALRA retest), SALES-9583 (SUMO Flow Audit), SALES-9575 (CreateVanPickup deprecation), and SALES-6877 (Lead Convert Dupe) were descoped rather than carried. Is Won't Do the right mechanism, or should some of these have moved to the next sprint with points adjusted?

### 5. Action Items

| Item | Owner | Due Date |
|------|-------|----------|
| Reconcile committed/completed points against Jira sprint report (111 vs 93 vs 153 discrepancy) | David Garcia | Aug 22, 2026 |
| Create DevQA clone tickets at sprint planning, not after parent completion | Navinchandra Gupta | Next sprint planning (Aug 22) |
| Make Reason for Bug mandatory before bug closure; backfill SALES-6448 through SALES-9633 | All engineers | Aug 29, 2026 |
| First weekly unassigned Jira ticket queue rotation handoff in #srt-team | Navinchandra Gupta | Aug 28, 2026 |
| Review SALES-9623 September ALRA regional expansion epic and create child tickets | David Garcia | Aug 22, 2026 |
| Reply to Prashanth on Capdev % targets and escalation triage policy | David Garcia | Aug 21, 2026 |
| Share Flexible Sales Routing research (buy/build/optimize, decoupling LeanData and Sumo) | David Garcia | TBD (was Aug 11, still In Progress per tracker) |
| Establish proactive product alignment cadence with Jen | Jenn Kleinfeld | Aug 21, 2026 |
| Plan to move support requests off Slack DMs into Zendesk/JSM | David Garcia | TBD (tracker shows Aug 14, In Progress) |
| Complete SALES-9557 permanent SailPoint fix (follow-up to Jul 31-8/1 lockout) | Navinchandra Gupta | TBD |
| [OPEN QUESTION: confirm current engineering manager with HR/Prashanth] | David Garcia | TBD |

---

*Sources: Jira SALES board 10 sprint 9367 (109 tickets), Notion SRT Action Items Tracker, Notion 2026-08-19 Slack Sweep, #srt-core-team and #srt-team Slack Aug 6-19, Weekly Status Report Aug 3-7, SRT Team Development Process doc.*
