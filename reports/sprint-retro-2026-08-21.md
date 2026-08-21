# Sales 8/6 - 8/19 | Aug 6, 2026 - Aug 19, 2026

## Part A: Metrics Report

### Executive Summary

Sales 8/6 - 8/19 closed clean with zero carry-over, which is the first fully cleared sprint board in recent memory. Velocity jumped to 153 completed points (manual sum), up from 132 in Sales 7/23 - 8/5, driven mostly by the batched API version 54 to 65 upgrade work (SALES-8554 through SALES-8562) and the DevQA wave that followed. The biggest concern is capacity shape: Tech Health consumed 52% of completed points and Product landed at 9% against a 48% target, while mid-sprint scope adds hit 42% of original commitment.

### Sprint Metrics Table

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 8/6 - 8/19 |
| Sprint Dates | 2026-08-06 - 2026-08-19 |
| Committed Points | [OPEN QUESTION: Jira Sprint Report not reachable via API. Manual estimate at sprint start: 111 pts across 70 tickets created before 2026-08-06. Confirm committed figure from board Sprint Report before the meeting.] |
| Completed Points | 153 pts (Sales 8/6 - 8/19). Manual sum: 144 pts Done + 9 pts Won't Do resolved in-window. [OPEN QUESTION: confirm against Jira Sprint Report committed/completed view.] |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | 0 / 0 [ASSUMPTION: no tickets removed from sprint detected in final roster of 109 parent tickets. Confirm via Sprint Report removed-items section.] |
| Added Mid-Sprint (tickets / points) | 39 / 47 |
| Scope Change % | +42.3% net points added after sprint start (47 added / 111 original commitment estimate) |
| Spikes Closed | 10 |
| Bugs Closed | 19 |

Estimation level: story/task level on parent tickets. Zero sub-tasks carried points in this sprint (109 parent tickets, 0 sub-tasks in sprint).

### Capacity Allocation Table (Sales 8/6 - 8/19, based on 153 completed points)

Buckets inferred from ticket summary patterns (KTLO:/TD:/SU&TC:, Zendesk bucket tickets, API bump titles, ALRA/SUMO keywords, parent epic names). SRT-* labels were sparse (only 2 tickets carried SRT-Product).

| Bucket | Target % | Target Points | Actual Points | Actual % | Delta |
|--------|----------|---------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 14 | 9.2% | -20 |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 79 | 51.6% | +68 |
| KTLO (SRT-KTLO) | 16% | ~11 | 41 | 26.8% | +30 |
| Buffer / Unplanned | 20% | ~14 | 19 | 12.4% | +5 |

KTLO at 26.8% is below the 30% alert threshold, but Product at 9.2% is a structural miss, not a rounding issue.

Label breakdown across sprint tickets: SRT-Product label on 2 tickets (SALES-9527, SALES-9526). No tickets carried SRT-KTLO, SRT-Domain-Tech-Debt, or SRT-Software-Upgrades labels. Zendesk bucket tickets (SALES-9540, SALES-9544, SALES-9548, SALES-9563, SALES-9564, SALES-9565, SALES-9603) account for most KTLO/Tech Health signal.

### Key Findings

#### Scope creep and mid-sprint changes

39 tickets totaling 47 points were created after sprint start on 2026-08-06. The dominant pattern is reactive DevQA ticket creation, not product priority shifts. Once Mike and Gus closed API bump parents, DevQA clones appeared in batches:

- Aug 6-7: SALES-9574, SALES-9576, SALES-9577 (DevQA and history object follow-up)
- Aug 10-11: SALES-9585 through SALES-9609 (DevQA wave for API bumps, Pardot fix, buyer profile)
- Aug 12-14: SALES-9606 through SALES-9621 (supply sync inquiry, more DevQA)
- Aug 17-19: SALES-9626 through SALES-9656 (final DevQA batch, ZD-to-JSM discovery clone, LeanData/SUMO assessment clone)

Priority-shift adds (not DevQA):

- SALES-9603 (2 pts, Jummy, Aug 11): ZD Support 8/6-8/19
- SALES-9637 (4 pts, Nag, Aug 18): CLONE - Discovery: SalesOps Migrating Off of Zendesk to JSM
- SALES-9656 (5 pts, Nag, Aug 19): CLONE - Engineering Assessment for Lean Data and Sumo Redesign

SALES-9656 and SALES-9637 alone added 9 points on the last two days of the sprint. [OPEN QUESTION: who requested SALES-9656 mid-sprint vs planning it at sprint start with SALES-9559?]

Point re-estimates after sprint start: not systematically detected via API changelog scan. [OPEN QUESTION: confirm no re-pointing in Sprint Report.]

Removed tickets: none detected.

Pattern summary: weak upfront DevQA planning for the API upgrade batch, plus late discovery clones. Not classic weak grooming on product stories, but the DevQA spawn pattern inflated scope 42% above start commitment.

#### Velocity and throughput

| Sprint | Completed Points (manual) |
|--------|--------------------------|
| Sales 6/25 - 7/8 | 109 |
| Sales 7/9 - 7/22 | 123 |
| Sales 7/23 - 8/5 | 132 |
| Sales 8/6 - 8/19 | 153 |

Trending up four sprints in a row. Sales 8/6 - 8/19 jump is explained by the API version bump batch (18 parent tickets across SALES-8546 through SALES-8562 plus DevQA), zero carry-over, and a 7-person team post-Grace departure (Grace last day 2026-07-15). No major PTO/holiday compression this sprint.

#### Burndown shape

Late-heavy. Resolution distribution (PT):

| Date | Tickets | Points |
|------|---------|--------|
| Aug 6 | 4 | 5 |
| Aug 7 | 8 | 10 |
| Aug 10 | 9 | 12 |
| Aug 11 | 12 | 14 |
| Aug 12 | 10 | 15 |
| Aug 13 | 5 | 7 |
| Aug 14 | 11 | 15 |
| Aug 17 | 10 | 14 |
| Aug 18 | 18 | 27 |
| Aug 19 | 17 | 34 |

61 of 153 points (39.9%) closed on Aug 18-19 alone. Aug 6-7 combined only 15 points (9.8%). This is a sprint-end rush, not steady throughput.

#### Bug analysis

19 bugs closed (Done status, resolved in-window). Reason for Bug (customfield_10142) was unpopulated on all 19.

| Reason for Bug | Count | Tickets |
|----------------|-------|---------|
| Unpopulated | 19 | All closed bugs |

Sample closed bugs: SALES-6448, SALES-6877 (Won't Do), SALES-9211, SALES-9250, SALES-9251, SALES-9252, SALES-9253, SALES-9383, SALES-9434, SALES-9492, SALES-9493, SALES-9510, SALES-9525, SALES-9526, SALES-9531, SALES-9552, SALES-9585, SALES-9598, SALES-9606.

Without Reason for Bug data, no category dominates. Process target: populate the field at bug close starting next sprint.

### Incidents (Sales 8/6 - 8/19 only)

1. **SALES-9531** (Aug 11): SUMO Appointment Booking error and calendar sync issue. Assignee: Deepika. #sumoupdates thread Aug 11: users could not see booking slots; Deepika confirmed slots visible after hard refresh (Cmd+Shift+R). Resolved Aug 11.
2. **SALES-9537** (Aug 13-14): Sailpoint Salesforce ECA authorization failure, Production. Assignee: Navin. Closed in sprint.
3. **Aug 19 developer app access** (#srt-core-team): Chris Burns flagged removal from GitHub, Cursor, and Jira. Resolved same day ("I got it created, they are working on it" per Slack sweep Aug 19).

Not this sprint: SALES-9522 (SUMO booking error after ALRA changes) resolved Aug 3, before sprint start. Do not attribute to Sales 8/6 - 8/19.

### Per-Engineer Summary (Sales 8/6 - 8/19)

Points below are Done-status tickets resolved within the sprint window.

**Alex Burton** | 10 tickets | 14 pts completed | 0 carry-over

Completed: SALES-9458 (2) RevOps Demo Lean Data & Sumo Weighted Routing; SALES-9483 (2) Title Level/Territory/HV Escalation Reporting; SALES-9502 (1) BDR Dashboard Hierarchy; SALES-9510 (1) Direct Manager Field on Leads; SALES-9525 (2) BDR credit issue; SALES-9526 (1) ALRA SGO Lead Create Metadata; SALES-9540 (1) TD Zendesk bucket; SALES-9544 (1) SU&TC Zendesk bucket; SALES-9548 (2) KTLO Zendesk bucket; SALES-9553 (1) Cohorts 8/10-8/17.

**Jummy Sanni** | 6 tickets | 9 pts | 0 carry-over

Completed: SALES-6818 (1) SUMO confirmation emails; SALES-8461 (2) error closing opp; SALES-9383 (2) Multi Calendar opp/appt linking; SALES-9583 (1) SUMO Flow Audit; SALES-9600 (1) DevQA SALES-9492; SALES-9603 (2) ZD Support 8/6-8/19.

**Michael Criswell** | 21 tickets | 33 pts | 0 carry-over

Completed: SALES-8554 through SALES-8562 (9 tickets, 18 pts) API version 54-65 bumps; SALES-9211 (2) ContractTrigger PD delete; SALES-9252 (2) sfDupLeadMatchedContact.test.js; SALES-9253 (2) sfEditLead.test.js; SALES-9529 (1) LCO NAV Van backfill; SALES-9558, SALES-9560, SALES-9562, SALES-9566, SALES-9592, SALES-9609, SALES-9626, SALES-9632 (8 DevQA tickets, 8 pts).

**Chris Burns** | 6 tickets | 11 pts | 0 carry-over

Completed: SALES-6448 (2) Incorrect Owner Post Conversion; SALES-9332 (3) Profiles/PS/PSG spike; SALES-9492 (1) Buyer Profile Picklist; SALES-9493 (2) High Value LWC null indicator; SALES-9552 (1) Skip Loss Reason Validation; SALES-9573 (2) POC Google Gemini sandbox.

**Grace Saint** | 0 tickets | 0 pts | 0 carry-over

Grace last day was 2026-07-15. No sprint assignments.

**Navinchandra Gupta** | 12 tickets | 17 pts | 0 carry-over

Completed: SALES-9345 (2) Palm Beach retail relocation; SALES-9405 (2) San Jose event site; SALES-9406 (1) Alexandria event site; SALES-9434 (2) Email Opt Out Pardot fix; SALES-9528 (2) Real Partner Reports Aug 5; SALES-9537 (2) Sailpoint ECA auth failure; SALES-9586 (1) High Value Designer list view; SALES-9594 (1) DevQA SALES-9552; SALES-9605 (1) Alyssa Hayes HV Designer admin; SALES-9620 (1) August Targeted Consign Offers; SALES-9631 (1) QA 6448; SALES-9647 (1) SOX access provisioning clone.

**Nag Malluru** | 8 tickets | 16 pts | 0 carry-over

Completed: SALES-9527 (2) Retail Gifting sizing; SALES-9563 (1) ZD KTLO bucket; SALES-9564 (1) ZD Tech Debt bucket; SALES-9565 (1) ZD S/W Upgrades bucket; SALES-9572 (1) Google Sheets connector; SALES-9577 (1) History Objects follow-up; SALES-9637 (4) ZD to JSM Discovery clone; SALES-9656 (5) LeanData/SUMO redesign assessment clone.

**Gustavo Silva** | 27 tickets | 33 pts | 0 carry-over

Completed: SALES-8546, SALES-8547 (API bumps); SALES-9250, SALES-9251 (test fixes); SALES-9409 (2) lead expiry research; SALES-9538 (3) slug matching; SALES-9561 (2) SF store phone leads; SALES-9567 (1) zipcode discovery; SALES-9574 through SALES-9621 (DevQA batch, 14 tickets); SALES-9633 (1) commission issue; SALES-9636 (1) DevQA SALES-9253; SALES-9643 (2) required lead fields research.

**Sai Deepika Kanuri** | 6 tickets | 11 pts | 0 carry-over

Completed: SALES-7924 (1) SUMO workflow audit; SALES-9531 (1) SUMO booking/calendar sync; SALES-9532 (2) Orphan Comp Calcs; SALES-9533 (5) Merging Comp Calcs with COI; SALES-9570 (1) ALRA Phase 2 placeholder; SALES-9582 (1) Comp Credit Backfills.

**Jenn Kleinfeld** | 0 tickets | 0 pts | 0 carry-over

Jenn is PM/RevOps partner, not a sprint assignee.

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

Mike and Gus closed the full API version 54 to 65 upgrade chain (SALES-8554 through SALES-8562) plus the DevQA wave behind it. That is 33 points each in Done work, and it removes a long-standing tech debt backlog item.

Nag closed SALES-9656 (LeanData/SUMO redesign assessment) and SALES-9637 (ZD to JSM discovery) on Aug 19, the last day of the sprint, with Confluence links attached. That unblocks September ALRA expansion planning (SALES-9625 already rolling in the next sprint).

Deepika resolved SALES-9531 on Aug 11 during active #sumoupdates escalation. She also carried SALES-9533 (5 pt COI/comp merge spike) while supporting ALRA go-live.

Navin shipped retail site updates for Palm Beach, San Jose, and Alexandria pop-ups (SALES-9345, SALES-9405, SALES-9406), fixed the Sailpoint ECA production auth failure (SALES-9537), and closed the Pardot opt-out bug (SALES-9434).

Chris fixed two lead conversion bugs (SALES-6448, SALES-9493) and ran the Google Gemini sandbox POC (SALES-9573).

Alex delivered the RevOps demo (SALES-9458) and the BDR dashboard reporting fixes (SALES-9483, SALES-9502, SALES-9510, SALES-9525).

Jummy closed the multi-calendar opp/appt linking bug (SALES-9383), a sprint goal item from day one.

The whole team closed with zero carry-over. Navin's Aug 19 #srt-core-team reminder worked.

### 2. What went well

Every one of 109 parent tickets reached Done or Won't Do by sprint close. No carry-over for the first time in the velocity trend window.

The API upgrade batch landed. Nine parent bump tickets plus DevQA closed in one sprint instead of dragging across quarters.

ALRA support work stayed contained: SALES-9526, SALES-9458, SALES-9580 (Won't Do after retest), and SUMO fixes tied to go-live.

Real Partner and retail event site work shipped on schedule (SALES-9528, SALES-9345, SALES-9405, SALES-9406).

Jenn and David held the line on intake: Zoom phone cleansing (Aug 7 #srt_squadleads) and Rippit SMS request (Aug 12) both got routed through product before opening engineering spikes.

### 3. What needs work

Product capacity was 9% against a 48% target. ALRA, SUMO, and comp work happened, but most of it landed in KTLO, Buffer, or Tech Health buckets because labels and epics do not reflect product intent.

Mid-sprint DevQA clones added 47 points (42% scope change). The API bump parents did not have DevQA tickets pre-created at sprint planning, so completions triggered a ticket factory in the second week.

Reason for Bug was blank on all 19 closed bugs. We cannot run root cause analysis or target process fixes without that field.

Burndown was late-heavy: 40% of points closed Aug 18-19. That creates deploy risk and QA compression at sprint end.

Aug 10 retro commitments still open in the SRT Action Items Tracker: design doc template share, testing doc template share, and stakeholder request process walkthrough all remain Not Started as of Aug 20.

Jenn flagged Aug 19 (#srt_squadleads) that she lacks clarity on which dashboard/report changes require a PR vs prod-only edits. That gap creates stakeholder confusion.

[OPEN QUESTION: confirm current manager. Template notes Prashanth Patlolla on leave; older notes reference Kishore Kumar Mohan.]

### 4. Discussion Topics

1. SALES-8554 through SALES-8562 consumed ~18 committed points and spawned ~14 DevQA tickets mid-sprint. Should we pre-create DevQA tickets at planning for batch tech health work, or accept the scope spike as normal?

2. Product allocation was 14 of 153 completed points (9.2%). ALRA Phase 1.25 and September expansion (SALES-9623, SALES-9625) are already in the next sprint. Did we under-commit product work in Sales 8/6 - 8/19, or mis-tag it?

3. SALES-9637 (4 pts) and SALES-9656 (5 pts) entered Aug 18-19. Were these truly urgent, or could discovery have been committed at sprint start alongside SALES-9559 and SALES-9449?

4. KTLO landed at 26.8%, just under the 30% alert. Zendesk bucket tickets (SALES-9540, SALES-9544, SALES-9548, SALES-9563-9565, SALES-9603) totaled significant points. Is the Zendesk bucket measurement working, or are we still absorbing support volume silently?

5. All 19 closed bugs lack Reason for Bug. Do we enforce it at transition, or accept perpetual blank data?

### 5. Action Items

| Item | Owner | Due Date |
|------|-------|----------|
| Confirm Sales 8/6 - 8/19 committed/completed points against Jira Sprint Report and reconcile with manual 153 completed | David Garcia | Before retro meeting |
| Share design document template with SRT team (Aug 10 retro commitment) | David Garcia | TBD |
| Share testing documentation templates and guidelines (Aug 10 retro commitment) | David Garcia | TBD |
| Schedule team walkthrough of stakeholder request process (Aug 10 retro commitment) | David Garcia | TBD |
| Document which report/dashboard changes require PR vs prod-only deployment; reply to Jenn | David Garcia / Navin Gupta | TBD |
| Pre-create DevQA tickets at sprint planning for batch tech health parents (API bumps, etc.) | David Garcia / Michael Criswell | Next sprint planning |
| Enforce Reason for Bug field on all bug closures | All engineers | Next sprint |
| Deepika: send consolidated Angela appointment failure data for SUMO booking analysis | Sai Deepika Kanuri | TBD |
| Review SALES-9623 September ALRA epic and create child tickets before Sep 1 expansion | David Garcia / Nag Malluru | 2026-08-28 |
| Establish proactive product alignment cadence with Jen | David Garcia | TBD |

---

Sources: Jira SALES board 10 (sprint ID 9367, closed 2026-08-20), Slack (#srt-core-team, #srt_squadleads, #srt-team, #sumoupdates), Notion SRT Action Items Tracker and Aug 19 Slack Sweep, Google Drive Meet Recordings folder (referenced in Action Items Tracker for Aug 10 retro transcript).
