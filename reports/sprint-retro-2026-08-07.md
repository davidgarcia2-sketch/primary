# Sales 7/23 - 8/5 (July 23, 2026 - August 5, 2026)

## Part A: Metrics Report

### Executive Summary

Sales 7/23 - 8/5 was a high-output sprint that ran straight into ALRA go-live on August 3 and the first hypercare week. The team shipped 129 completed story points (manual sum) against 96 committed at sprint start, with ALRA Stage 1 and Southeast Stage 2 routing live, SUMO and LeanData configured, and High Value escalation enabled. The sprint was not clean: a ~23-minute SUMO booking outage on August 3 (SALES-9522), hypercare noise around leads without appointments (count grew from ~27 to ~46 by August 5), and 32 mid-sprint ticket adds (38 points, 39.6% scope change) pulled capacity away from planned work. Biggest win: ALRA go-live with rollback plan, hypercare roster, and stakeholder FAQ all in place (SALES-9131, SALES-9136, SALES-9192, SALES-9217, SALES-9316, SALES-9452, SALES-9499). Biggest concern: reactive hypercare and mid-sprint adds consumed buffer, and SALES-9522 is still In Progress in Jira as of sprint close despite an August 3 resolution date.

### Sprint Metrics Table

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 7/23 - 8/5 |
| Sprint Dates | July 23, 2026 - August 5, 2026 |
| Committed Points | 96 (manual: tickets in sprint at start, story-level, Sales 7/23 - 8/5) [OPEN QUESTION: Jira Sprint Report committed figure not accessible via API; reconcile in UI before meeting] |
| Completed Points | 129 (manual sum, Sales 7/23 - 8/5) [OPEN QUESTION: Jira Sprint Report completed figure not accessible via API] |
| Carry-Over (tickets / points) | 1 / 1 (SALES-9522) |
| Removed (tickets / points) | TBD / TBD [Need Jira sprint report; not exposed via API] |
| Added Mid-Sprint (tickets / points) | 32 / 38 |
| Scope Change % | +39.6% (38 pts added / 96 pts original commitment, Sales 7/23 - 8/5) |
| Spikes Closed | 7 |
| Bugs Closed | 14 |

Cross-check: manual completed sum is 129 points across 86 resolved story-level tickets. Four tickets show Done status but resolved before sprint start (SALES-9370, SALES-9457, SALES-9464, SALES-9465) and are excluded from the 129. No gap over 1 point between sprint report and manual sum could be verified because the sprint report was not available.

### Capacity Allocation Table (Sales 7/23 - 8/5, completed points only)

SRT capacity labels were sparse on most tickets. Buckets below use label-first logic, then Zendesk bucket naming (KTLO / TD / SU&TC), then summary keyword inference. DevQA tickets count as buffer/overhead.

| Bucket | Target % | Target Points | Actual Points | Actual % | Delta |
|--------|----------|---------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 67 | 51.9% | +33 |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 31 | 24.0% | +20 |
| KTLO (SRT-KTLO) | 16% | ~11 | 6 | 4.7% | -5 |
| Buffer / Unplanned | 20% | ~14 | 25 | 19.4% | +11 |

KTLO did not exceed 30%. Product and tech health both ran well above target, driven by ALRA/SUMO/LeanData delivery and API version bump work (SALES-8542 through SALES-8545, SALES-9420, SALES-9421).

### Key Findings

#### Scope creep and mid-sprint changes

32 tickets (38 points) were added after sprint start on July 23. The pattern was mostly reactive hypercare and launch support, not weak grooming on committed ALRA work.

Notable mid-sprint adds:

| Key | Summary | Points | Pattern |
|-----|---------|--------|---------|
| SALES-9507 | Help with ALRA Testing | 5 | Launch validation, requested mid-sprint |
| SALES-9489 | Re-authenticating Rippit x Zoom / Zoom Phone Integration | 2 | KTLO/config gap |
| SALES-9511 | High Value Designer LWC Not Accessible on Lead Record in Production | 2 | Reactive prod bug |
| SALES-9498 | Leads not being autoconverted when booking an appointment | 1 | Hypercare follow-up |
| SALES-9522 | SUMO Appointments booking error after ALRA changes on SUMO | 1 | P1 incident, Aug 3 |
| SALES-9536 | ALRA Hypercare: Login/Deactivated User Issue | 1 | Hypercare, not routing |
| SALES-9568 | CLONE - SUMO Appointment Booking error and calendar sync issue | 1 | Hypercare clone |
| SALES-9495 | Nag - ZD - KTLO - 7/25-8/5 | 1 | Planned Zendesk bucket |
| SALES-9496 | Nag - ZD - S/W Upgrades - 7/23 - 8/5 | 1 | Planned Zendesk bucket |
| SALES-9497 | Nag - ZD - Domain Tech Debt - 7/23-8/5 | 1 | Planned Zendesk bucket |

Plus 21 DevQA companion tickets (1 point each) for fixes already in flight. The DevQA pattern is normal for this team but it inflates ticket count without adding net scope.

No re-pointing after sprint start was detected via created-date analysis. [OPEN QUESTION: confirm in Jira changelog if any estimates changed without ticket creation.]

Overall: real priority shift for ALRA go-live and hypercare, not grooming failure on the original 96-point commit.

#### Velocity and throughput

| Sprint | Completed Points (manual) | Trend |
|--------|---------------------------|-------|
| Sales 6/11 - 6/24 | 103 [ASSUMPTION: prior retro manual sum, not re-verified this run] | |
| Sales 6/25 - 7/8 | 108 [ASSUMPTION: prior retro manual sum] | |
| Sales 7/9 - 7/22 | 123 [ASSUMPTION: prior retro manual sum] | |
| Sales 7/23 - 8/5 | 129 | Up |

Velocity is trending up four sprints in a row. Obvious factors this sprint: ALRA go-live pressure, hypercare roster Aug 3-7, Jummy PTO Jul 27 through Aug 6, Chris out Aug 3-4, and Grace Saint already off the team (last day July 15). The 129 figure includes 37 points completed from mid-sprint adds; original-commitment throughput was 92 points.

#### Burndown shape

Late-heavy. Only 3 points (2%) closed on July 24 (sprint day 1). By July 31 the team was at 74 of 129 points (57%). The last three days (Aug 3-5) closed 49 points (38% of total), with a spike of 25 points on August 4 alone. That matches ALRA go-live on August 3 and hypercare ticket creation through August 5. Not a flatline week one, but definitely a rush at the end.

#### Bug analysis

14 bugs closed in Sales 7/23 - 8/5. Reason for Bug (customfield_10142) was unpopulated on all 14:

SALES-8886, SALES-9442, SALES-9443, SALES-9462, SALES-9489, SALES-9495, SALES-9496, SALES-9497, SALES-9498, SALES-9500, SALES-9511, SALES-9523, SALES-9536, SALES-9568

Process target: populate Reason for Bug on close. Without it, we cannot tell if Broken Code, Configuration Gap, or User Error dominates.

### Per-Engineer Summary (Sales 7/23 - 8/5)

#### Alex Burton — 21 pts completed, 0 carry

Completed: SALES-9131 (1), SALES-9198 (2), SALES-9240 (2), SALES-9273 (2), SALES-9278 (2), SALES-9279 (1), SALES-9280 (1), SALES-9281 (1), SALES-9371 (1), SALES-9396 (2), SALES-9450 (1), SALES-9452 (2), SALES-9499 (1), SALES-9536 (1), SALES-9539 (1)

Carry-over: none

#### Jummy Sanni — 2 pts completed, 0 carry

Completed: SALES-9346 (1), SALES-9468 (1)

Carry-over: none. Was on PTO Jul 27 through Aug 6 per hypercare schedule.

#### Michael Criswell (Mike) — 23 pts completed, 0 carry

Completed: SALES-8542 (2), SALES-8545 (2), SALES-8886 (2), SALES-9377 (1), SALES-9420 (3), SALES-9421 (3), SALES-9481 (1), SALES-9488 (1), SALES-9494 (1), SALES-9503 (1), SALES-9504 (1), SALES-9513 (1), SALES-9523 (3), SALES-9524 (1)

Carry-over: none

#### Chris Burns — 14 pts completed, 0 carry

Completed: SALES-7930 (2), SALES-8937 (2), SALES-9213 (2), SALES-9245 (3), SALES-9354 (1), SALES-9487 (1), SALES-9500 (1), SALES-9511 (2)

Carry-over: none. Out Aug 3-4 during go-live; Navin/David covered HV screen rollback path.

#### Grace Saint — 0 pts completed, 0 carry

No tickets in this sprint. Last day was July 15, 2026.

#### Navinchandra Gupta (Navin) — 17 pts completed, 0 carry

Completed: SALES-9217 (2), SALES-9410 (1), SALES-9427 (1), SALES-9436 (1), SALES-9472 (1), SALES-9473 (2), SALES-9474 (2), SALES-9486 (1), SALES-9489 (2), SALES-9505 (1), SALES-9506 (1), SALES-9515 (1), SALES-9517 (1)

Carry-over: none. Deployed SALES-9346 retail dashboard and SALES-9523 AutoConvertLead fix to prod Aug 5 per #releases.

#### Nag Malluru — 8 pts completed, 0 carry

Completed: SALES-8931 (2), SALES-9334 (3), SALES-9495 (1), SALES-9496 (1), SALES-9497 (1)

Carry-over: none

#### Gustavo Silva (Gus) — 32 pts completed, 0 carry

Completed: SALES-6058 (3), SALES-8543 (1), SALES-8544 (1), SALES-9267 (3), SALES-9322 (1), SALES-9368 (1), SALES-9381 (2), SALES-9442 (3), SALES-9443 (2), SALES-9446 (1), SALES-9459 (1), SALES-9462 (1), SALES-9482 (1), SALES-9498 (1), SALES-9507 (5), SALES-9508 (1), SALES-9512 (1), SALES-9516 (1), SALES-9518 (1), SALES-9521 (1)

Carry-over: none. Highest point total on the team.

#### Sai Deepika Kanuri (Deepika) — 12 pts completed, 1 carry

Completed: SALES-9192 (1), SALES-9316 (2), SALES-9356 (1), SALES-9445 (2), SALES-9463 (3), SALES-9480 (1), SALES-9514 (1), SALES-9568 (1)

Carry-over: SALES-9522 (1) SUMO Appointments booking error after ALRA changes on SUMO. Jira shows In Progress at sprint close despite resolutiondate Aug 3.

#### Jenn Kleinfeld — 0 pts completed, 0 carry

No SALES tickets assigned in this sprint. Active in hypercare coordination, stakeholder messaging, and product decisions (ALRA Risk Assessment, SALES-9559 routing redesign opened Aug 5 per Slack sweep).

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

Alex Burton owned LeanData confirmation on go-live morning (~9:24am CT, SALES-9136), ran the pre-go-live routing validation package (SALES-9452), confirmed territory/rep accuracy (SALES-9396), and closed hypercare items SALES-9536 and SALES-9499 under pressure. He was on hypercare AM shifts Aug 3-4.

Sai Deepika Kanuri ran SUMO config, caught and fixed the HV smoke-test booking error (~6:45-7am PT Aug 3), resolved the Aug 3 P1 booking outage root cause with SUMO (SALES-9522, null secondary assignment field), and shipped ALRA table weighting work (SALES-9192) plus HV escalation pools (SALES-9356, SALES-9445, SALES-9463).

Navinchandra Gupta got BDR High Value screen access live by ~5:30am PT Aug 3 (SALES-9217), deployed the retail SGO dashboard (SALES-9346) and AutoConvertLead fix (SALES-9523) to production Aug 5, and handled Sailpoint production install (SALES-9474).

Gustavo Silva carried the heaviest load at 32 points, including SUMO event sync improvements (SALES-9442, SALES-9443), ALRA test support (SALES-9507, 5 pts), and lead autoconversion fixes (SALES-9498).

Michael Criswell closed the Summer '26 release readiness work (SALES-9420, SALES-9421) and the AutoConvertLead DML exception (SALES-9523, 3 pts) while covering DevQA load.

Chris Burns shipped the High Value Designer LWC prod fix (SALES-9511) and mobile HV indicator (SALES-9487) while out part of go-live week.

### 2. What went well

ALRA Stage 1 equal round-robin went live August 3 across all markets. Southeast Stage 2 ALRA-heavy weighting followed the same day (~11:50am CT) after Laura directed the flip. SUMO, LeanData, and HV escalation were all confirmed live per the ALRA Go-Live Risk Assessment.

Hypercare had a real operating model: roster Aug 3-7, severity definitions, Jira ticket requirement, Jenn as first filter, Navin and David on backup. Navin posted "Sprint completed successfully" in #srt-core-team Aug 5.

Pre-launch testing package (SALES-9452) and stakeholder FAQ (SALES-9499) landed before go-live. Rollback owners were named per component.

API version bump work progressed (SALES-8542 through SALES-8545) alongside launch work.

Retail SGO Homepage Dashboard Tile (SALES-9346) shipped to prod Aug 5.

### 3. What needs work

Mid-sprint adds hit 32 tickets / 38 points (39.6% scope change). Hypercare issues that were not in the original sprint plan (SALES-9522, SALES-9536, SALES-9568, SALES-9511) consumed buffer that was supposed to stay at ~20%.

Reason for Bug was blank on all 14 closed bugs. We cannot run a real defect analysis until the field is filled.

SALES-9522 status is messy: resolved Aug 3 per Jira resolutiondate, but In Progress at sprint close, and leadership communications lagged the confirmed SUMO root cause (per Aug 5-6 Slack sweeps). One source of truth for incident state matters.

Leads without appointments reporting lacked a BDR-facing tagged list. Deepika's report became the workaround. SUMO error logs do not tie back to the failed lead (confirmed in Aug 6 #alra-hypercare thread). That is a system gap, not just a hypercare process gap.

QA regression flaked on SUMO lead conversion tests Aug 5-6 (#qe-regression, sfConvertLeadSumoCal.test.js). Not a prod incident, but noise during hypercare week.

RevOps wants faster weighting changes (Emily Rourke, Aug 5 #alra-sales-revops-technical-updates-decisions). David committed to mid-sprint updates when territories and percentages are provided, but the underlying process is still engineer-driven across LeanData and SUMO.

[OPEN QUESTION: confirm current manager. Context says Prashanth Patlolla, Director of Engineering, on leave. Older notes reference Kishore Kumar Mohan.]

### 4. Discussion topics

1. SALES-9507 (5 pts, added mid-sprint) for ALRA testing: was that the right place for launch validation hours, or should go-live testing sit outside sprint capacity with a fixed hypercare budget?

2. SALES-9522 is In Progress in Jira at sprint close but was treated as resolved in hypercare and the Risk Assessment. Do we reopen, close properly, or split follow-up (error log to lead ID) into a new ticket?

3. Product allocation hit 52% of completed points vs 48% target, but 25 points (19%) landed in buffer, mostly DevQA. Should DevQA count against buffer permanently, or do we need a fifth bucket?

4. Deepika's unbooked-lead count went from ~27 to ~46 between Aug 4 and Aug 5 hypercare threads, with 1 duplicate. What is the acceptance threshold before we escalate to SUMO vs handle as hypercare cleanup?

5. Emily and Paige are asking for ad-hoc weighting changes without a 3-week lead time (Aug 5-6 Slack). SALES-9559 is open for routing redesign. What is the minimum viable RevOps self-service path, and what stays engineer-only?

### 5. Action items

| Item | Owner | Due date |
|------|-------|----------|
| Reconcile SALES-9522 Jira status with hypercare resolution and document final RCA | Sai Deepika Kanuri | TBD |
| Populate Reason for Bug on all 14 bugs closed in Sales 7/23 - 8/5 | Ticket assignees | Next sprint grooming |
| Create sized ticket for SUMO error log to lead/appointment ID linkage (raised Aug 6 hypercare) | David Garcia | TBD |
| Confirm whether calendar/login hypercare items have Jira tickets beyond SALES-9536 | Alex Burton | TBD |
| File or confirm ticket for retail multi-calendar appointment delete (Zendesk 133913) | Jenn Kleinfeld / Alex Burton | TBD |
| Reconcile Jira Sprint Report committed/completed vs manual 96/129 | David Garcia | Before retro meeting |
| Review DevQA overhead pattern (21 one-point tickets added mid-sprint) | David Garcia | TBD |
| Size supply identifier linkage spike (Gus/Lucas, per Aug 4 Sandeep thread) | Gustavo Silva | Before Monday pros/cons discussion |
| Send ALRA sales go-live message (cleared ~11:55am CT Aug 4) | Jenn Kleinfeld | [ASSUMPTION: sent post-sprint; confirm] |

---

Sources: Jira SALES board 10 sprint 9366 (91 story-level tickets), ALRA Go-Live Risk Assessment (Notion), ALRA Hypercare Schedule (Notion), Slack sweeps Aug 5-6 (Notion), #alra-hypercare and #srt-core-team (Slack). Notion meeting notes query unavailable (Business plan required). Google Drive Meet Recordings not searched this run.
