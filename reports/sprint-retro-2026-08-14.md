# Sales 7/23 - 8/5 (July 23, 2026 - August 5, 2026)

[OPEN QUESTION: As of August 14, 2026, the active sprint is Sales 8/6 - 8/19 (closes August 19). No new sprint has closed since August 5. This report locks the most recently completed sprint per Jira board 10.]

## Part A: Metrics Report

### Executive Summary

Sales 7/23 - 8/5 was a high-output, high-chaos sprint that ran straight into ALRA Stage 1 go-live on August 3 and the first hypercare week. The team shipped 130 completed story points (manual sum, Sales 7/23 - 8/5) against 96 committed at sprint start, with ALRA routing live, SUMO and LeanData configured at 100% round-robin, High Value escalation enabled, and zero carry-over at sprint close. The sprint was not clean: a SUMO booking outage on August 3 morning (SALES-9522), a separate SUMO calendar sync outage on August 4 (SUMO RTC received August 6), hypercare noise around leads without appointments (count grew from ~27 to ~45 by August 6), and 32 mid-sprint ticket adds (38 points, 39.6% scope change). Biggest win: ALRA go-live with rollback plan, hypercare roster, and stakeholder FAQ in place (SALES-9131, SALES-9192, SALES-9217, SALES-9316, SALES-9452, SALES-9499, SALES-9507). Biggest concern: reactive hypercare and mid-sprint adds consumed buffer, and all 15 closed bugs still have no "Reason for Bug" value populated.

### Sprint Metrics Table

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 7/23 - 8/5 |
| Sprint Dates | July 23, 2026 - August 5, 2026 |
| Committed Points | 96 (manual: tickets in sprint at start, story-level, Sales 7/23 - 8/5) [OPEN QUESTION: Jira Sprint Report committed figure not accessible via API; reconcile in UI before meeting] |
| Completed Points | 130 (manual sum, Sales 7/23 - 8/5) [OPEN QUESTION: Jira Sprint Report completed figure not accessible via API] |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | TBD / TBD [Need Jira sprint report; not exposed via API] |
| Added Mid-Sprint (tickets / points) | 32 / 38 |
| Scope Change % | +39.6% (38 pts added / 96 pts original commitment, Sales 7/23 - 8/5) |
| Spikes Closed | 7 |
| Bugs Closed | 15 |

Cross-check: manual completed sum is 130 points across 87 resolved story-level tickets (Sales 7/23 - 8/5). Four tickets show Done status but resolved before sprint start (SALES-9370, SALES-9457, SALES-9464, SALES-9465) and are excluded from the 130. SALES-9522 resolved August 3 and is now Done in Jira (was In Progress at the August 7 retro run). No gap over 1 point between sprint report and manual sum could be verified because the sprint report was not available via API.

### Capacity Allocation Table (Sales 7/23 - 8/5, completed points only)

SRT capacity labels were sparse on most tickets. Buckets below use label-first logic, then Zendesk bucket naming (KTLO / TD / SU&TC), then summary keyword inference. DevQA companion tickets inherit the bucket of their parent ticket referenced in the summary.

| Bucket | Target % | Target Points | Actual Points | Actual % | Delta |
|--------|----------|---------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | 61 | 46.9% | +27 |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | 20 | 15.4% | +9 |
| KTLO (SRT-KTLO) | 16% | ~11 | 2 | 1.5% | -9 |
| Buffer / Unplanned | 20% | ~14 | 47 | 36.2% | +33 |

KTLO did not exceed 30%. Product ran above target, driven by ALRA/SUMO/LeanData delivery. Buffer is inflated because many completed tickets (campaign updates, Sailpoint admin, LOB deliverability, retail dashboard) lack SRT labels or clear bucket keywords. [ASSUMPTION: attributing DevQA tickets to parent ticket buckets; tickets without a parseable parent stay in buffer.]

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
| Sales 6/25 - 7/8 | 109 [ASSUMPTION: prior retro manual sum] | |
| Sales 7/9 - 7/22 | 123 [ASSUMPTION: prior retro manual sum] | |
| Sales 7/23 - 8/5 | 130 | Up |

Velocity is trending up four sprints in a row. Obvious factors this sprint: ALRA go-live pressure, hypercare roster Aug 3-7, Jummy PTO Jul 27 through Aug 6, Chris out Aug 3-4, and Grace Saint already off the team (last day July 15). The 130 figure includes 38 points completed from mid-sprint adds; original-commitment throughput was 92 points.

#### Burndown shape

Late-heavy. Only 3 points (2%) closed on July 24 (sprint day 1). By July 31 the team was at 74 of 130 points (57%). The last three days (Aug 3-5) closed 50 points (38% of total), with a spike of 25 points on August 4 alone. That matches ALRA go-live on August 3 and hypercare ticket creation through August 5. Not a flatline week one, but definitely a rush at the end.

#### Bug analysis

15 bugs closed in Sales 7/23 - 8/5. "Reason for Bug" (customfield_10142) was unpopulated on all 15.

| Reason for Bug | Count | Tickets |
|----------------|-------|---------|
| Unpopulated | 15 | SALES-9522, SALES-9523, SALES-9511, SALES-9536, SALES-9568, SALES-8886, SALES-9462, and 8 others |

Process target: populate Reason for Bug at close. Without it, we cannot tell whether August's bug load was broken code, configuration gaps, or user error. Given ALRA go-live, configuration gap is the likely dominant category, but that is [ASSUMPTION] until the field is filled.

### Per-Engineer Summary (Sales 7/23 - 8/5)

**Alex Burton** (21 pts completed, 0 carry-over)

Completed: SALES-9452 (2pt, pre-go-live routing validation), SALES-9396 (2pt, territory accuracy), SALES-9278 (2pt, cohorts), SALES-9273 (2pt, July EOM), SALES-9240 (2pt, pressure test), SALES-9198 (2pt, RevOps LeanData/SUMO access), SALES-9131 (1pt, NY LM drip off), SALES-9536 (1pt, hypercare login issue), SALES-9499 (1pt, change process FAQ), plus 6 DevQA/Zendesk bucket tickets.

**Jummy Sanni** (2 pts completed, 0 carry-over)

Completed: SALES-9468 (1pt, ZD KTLO), SALES-9346 (1pt, retail SGO dashboard tile). PTO Jul 27 through Aug 6 limited sprint output.

**Michael Criswell** (23 pts completed, 0 carry-over)

Completed: SALES-9523 (3pt, AutoConvertLead DmlException), SALES-9421 (3pt, SF RU non-public fields), SALES-9420 (3pt, SF RU accessibility), SALES-8886 (2pt, lead SGO validation), SALES-8545 (2pt, API v62-65 bump), SALES-8542 (2pt, API v57-65 bump), plus 7 DevQA companions.

**Chris Burns** (14 pts completed, 0 carry-over)

Completed: SALES-9245 (3pt, SLDS 2 discovery), SALES-9511 (2pt, HV Designer LWC prod access), SALES-9213 (2pt, LOB deliverability 503), SALES-8937 (2pt, duplicate opp investigation), SALES-7930 (2pt, packing list visibility), SALES-9500 (1pt, HV designer opp association), SALES-9487 (1pt, mobile HV indicator), SALES-9354 (1pt, designer/category capture).

**Grace Saint** (0 pts completed, 0 carry-over)

No tickets completed. Last day was July 15, 2026, before this sprint closed.

**Navinchandra Gupta** (17 pts completed, 0 carry-over)

Completed: SALES-9217 (2pt, HV Matrix permission set, Aug 3 rollout), SALES-9489 (2pt, Rippit x Zoom re-auth), SALES-9474 (2pt, Sailpoint prod package), SALES-9473 (2pt, August TCO campaign), SALES-9436 (1pt, change process docs), SALES-9427 (1pt, HV designer list view), SALES-9410 (1pt, referral link permission), plus 5 more.

**Nag Malluru** (8 pts completed, 0 carry-over)

Completed: SALES-9334 (3pt, COI/comp storage spike), SALES-8931 (2pt, contact duplicate discovery), SALES-9495 (1pt, ZD KTLO), SALES-9496 (1pt, ZD S/W upgrades), SALES-9497 (1pt, ZD tech debt).

**Gustavo Silva** (32 pts completed, 0 carry-over)

Completed: SALES-9507 (5pt, ALRA testing support), SALES-9442 (3pt, event sync flow), SALES-9267 (3pt, pre-go-live test staging), SALES-6058 (3pt, zip code quarterly update), SALES-9443 (2pt, EventTriggerHandler optimization), SALES-9381 (2pt, SELL-4934 support), SALES-9498 (1pt, lead autoconvert on booking), plus 9 DevQA and support tickets.

**Sai Deepika Kanuri** (13 pts completed, 0 carry-over)

Completed: SALES-9463 (3pt, HV opp escalation SUMO), SALES-9445 (2pt, L2/L3 pool upload), SALES-9316 (2pt, SUMO software update for ALRA), SALES-9356 (1pt, HV lead escalation), SALES-9192 (1pt, SUMO ALRA table weighting), SALES-9522 (1pt, SUMO booking error Aug 3), SALES-9568 (1pt, SUMO booking clone), SALES-9514 (1pt, quota uploads), plus 1 DevQA.

**Jenn Kleinfeld** (0 pts completed, 0 carry-over)

No SALES tickets assigned. Project lead for ALRA go-live communications and hypercare coordination per Notion ALRA Go-Live Implementation Plan.

---

## Part B: The Retro (45 minutes)

### 1. Shoutouts

Alex and Deepika owned the August 3 cutover sequence end to end. Deepika staged and activated SUMO at 6:00 AM Pacific (SALES-9316), Alex turned on LeanData weighted tables and the NY drip off (SALES-9131, SALES-9136 deployed pre-sprint), and Navin rolled the BDR HV Matrix permission set at 9:00 AM Eastern (SALES-9217). When SALES-9522 hit that morning, Deepika had it diagnosed and fixed within about an hour with SUMO vendor support.

Gus carried ALRA testing load under pressure. SALES-9507 (5 points, added mid-sprint) plus SALES-9267 staging work and a pile of DevQA companions kept the pre-go-live validation path moving while Alex was on LeanData config and hypercare triage.

Mike closed three API version bump stories (SALES-8542, SALES-8544, SALES-8545) and the AutoConvertLead production bug (SALES-9523) in the same sprint as ALRA go-live. That is a lot of release risk in one window, and it landed.

Chris shipped SALES-9511, SALES-9500, and SALES-9487 on July 31 so BDRs could see the High Value Designer screen before Navin's permission rollout on August 3. That sequencing mattered.

Navin got Sailpoint into production (SALES-9474), closed the Zoom re-auth gap (SALES-9489), and posted the rollback procedure to #alra-hypercare before go-live.

### 2. What went well

ALRA Stage 1 went live August 3 with a documented deployment sequence, rollback owners, and a hypercare roster for August 3-7. The Notion ALRA Go-Live Implementation Plan had exact activation times and ticket references, and the team hit the window.

Pre-go-live staging validation (SALES-9452) produced a reviewable export for RevOps before Laura's Go/No-Go. Gustavo's testing support (SALES-9507) and Alex's territory accuracy work (SALES-9396) fed that directly.

Zero carry-over at sprint close. Every committed story-level ticket either completed or was added and completed within the sprint window. SALES-9522, which was still In Progress at the August 7 retro snapshot, is now Done.

High output with a reduced roster. Grace was already gone, Jummy was on PTO, and Chris was out August 3-4. The team still closed 130 points.

Tech health work did not stall. Mike's SF release upgrade tickets and Nag's storage optimization spike (SALES-9334) both closed alongside the launch.

### 3. What needs work

Two separate SUMO incidents in three days, and we initially treated them as one story. August 3 (SALES-9522): null secondary assignment method during ALRA import, booking failures, ~27 leads without appointments in the first report window, ~45 in the wider 6 AM PST window by August 6. August 4: separate calendar sync outage (SUMO RTC: Linux OS upgrade broke health check, 9:15 AM ET to 2:10 PM ET). These need distinct timelines in every status update going forward.

Affected-lead count for SALES-9522 never fully closed the loop. Deepika's report counts leads created in the window with no appointment, not leads that hit a SUMO error in sumoapp__Log__c (SUMO confirmed logs cannot be tied to specific leads). As of sprint close, the count of how many of the ~45 still had no appointment was still open in ticket comments.

39.6% scope change is a lot. Most of it was justified hypercare, but it means the original 96-point plan was not what the sprint actually ran on. We need a clearer line between "planned hypercare capacity" and "surprise adds."

Reason for Bug is empty on all 15 closed bugs. We cannot run a meaningful bug retro without it.

SRT capacity labels are still sparse. Three Zendesk bucket tickets from Nag and three from Alex carried the KTLO/tech debt signal; everything else was inferred from summary text. Labeling at sprint planning would make capacity reporting trustworthy.

### 4. Discussion topics

1. SALES-9507 came in mid-sprint for 5 points of ALRA testing support. Was that scoped during planning and just added late, or was it genuinely unplanned? If unplanned, should we reserve a fixed hypercare block on every launch sprint?

2. SALES-9522 and the August 4 calendar sync outage were reported and discussed as related SUMO problems. How do we separate vendor incidents in hypercare updates so leadership gets accurate timelines?

3. Buffer/unplanned hit 36% of completed points (Sales 7/23 - 8/5) because SRT labels are missing on most tickets. Do we enforce labels at sprint commit, or accept inferred buckets and stop reporting against the 48/16/16/20 targets?

4. Mike closed three API version bump stories in the same sprint as ALRA go-live. Should release upgrade work be frozen in launch sprints, or was the timing acceptable given the RU deadline?

5. Grace is gone and Jummy was out most of the sprint. Gus carried 32 points. Is that sustainable for Sales 8/6 - 8/19, or do we need to rebalance before the next launch milestone?

### 5. Action items

| Item | Owner | Due date |
|------|-------|----------|
| Populate "Reason for Bug" on all 15 closed bugs from Sales 7/23 - 8/5 | Nag Malluru | August 21, 2026 |
| Close the SALES-9522 loop: confirm how many of the ~45 affected leads still have no appointment as of sprint close | Sai Deepika Kanuri | TBD |
| Add SRT capacity labels (SRT-product, SRT-KTLO, SRT-Domain-Tech-Debt, SRT-Software-Upgrades) at sprint planning for Sales 8/6 - 8/19 | David Garcia | August 20, 2026 |
| Document separate incident timelines for Aug 3 booking outage (SALES-9522) and Aug 4 calendar sync outage in hypercare postmortem | Sai Deepika Kanuri | August 21, 2026 |
| Establish weekly unassigned Jira ticket queue rotation (prerequisite for ticket-first support policy) | David Garcia | August 17, 2026 |
| Bring Navin chain set production deployment to David for approval (tracker item open since July 10) | Navinchandra Gupta | TBD |
| Reconcile committed/completed points against Jira Sprint Report for Sales 7/23 - 8/5 | David Garcia | Before retro meeting |
