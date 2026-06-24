# SRT MBR Monthly Automation — Complete Agent Prompt

**Version:** 1.0  
**Schedule:** Run monthly on the 1st calendar day (or first business day after month-end)  
**Team:** SRT / Salesforce Engineering  
**Outputs:** (1) MBR data Notion page, (2) Prompt recommendations `.md`, (3) Final message with both URLs

> Copy this entire file into your Cursor Cloud Agent / Automation prompt body.

---

## Mission

Pull Monthly Business Review (MBR) data for the **SRT / Salesforce Engineering** team for the **last full calendar month**. Source data from **Jira** (`trr-prod.atlassian.net`). Write results to a **new child page** under the Notion parent below.

**Jira execution project:** `SALES`  
**Jira portfolio project:** `PT` (issue type `Project`)  
**Team filter on PT projects:** label `squad-SALES`

---

## Step 0 — Compute run parameters

Use timezone **`America/Los_Angeles`** for all date boundaries.

| Variable | Rule |
|---|---|
| `run_date` | Today's date as `YYYY-MM-DD` |
| `reporting_month_name` | Full month name of the **previous calendar month** (e.g. `June`) |
| `reporting_year` | Year of the reporting month |
| `reporting_start` | First day of reporting month (`YYYY-MM-DD`) |
| `reporting_end` | Last day of reporting month (`YYYY-MM-DD`) |
| `quarter_tag` | `YYYYQ#` from reporting month: Jan–Mar → `Q1`, Apr–Jun → `Q2`, Jul–Sep → `Q3`, Oct–Dec → `Q4`. Example: June 2026 → `2026Q2` |
| `prior_quarter_tag` | Previous quarter in same format. Example: `2026Q2` → `2026Q1` |
| `quarter_tags` | Start with `[quarter_tag]`. If reporting month is **January, April, July, or October**, also include `prior_quarter_tag` |
| `page_title` | `MBR Data - {reporting_month_name} {reporting_year} (run {run_date})` |
| `recommendations_title` | `MBR Prompt Recommendations - run {run_date}.md` |

**Example:** Run on `2026-07-01` → reporting month = June 2026 → `page_title` = `MBR Data - June 2026 (run 2026-07-01)`.

**Label format:** Jira labels have **no `#` prefix**. Use `2026Q2`, not `#2026Q2`.

---

## Step 1 — Idempotency check (Notion)

**Parent page ID:** `388d553c3a2e803597ebf5ee2265a3e7`  
**Parent page title:** `2026 MBR data Output from Cursor`

Before creating the MBR page:

1. Fetch the parent page and list its child pages.
2. Search for an existing child with title **exactly** equal to `page_title`.
3. **If found:** Skip MBR page creation. Use the existing page URL in later steps.
4. **If not found:** Create a **new child page** under this parent.

Use Notion MCP `notion-create-pages` with:
```json
{
  "parent": { "type": "page_id", "page_id": "388d553c3a2e803597ebf5ee2265a3e7" },
  "pages": [{ "properties": { "title": "{page_title}" }, "content": "..." }]
}
```

**Never** update a prior run's MBR page. Each month = new child page.

---

## Step 2 — Jira connection & query rules

### Connection
1. Call `getAccessibleAtlassianResources` to get `cloudId` for `trr-prod.atlassian.net`.
2. Use **`searchJiraIssuesUsingJql`** for all data pulls (deterministic). Do **not** use semantic/Rovo search for counts or metrics.
3. **Paginate** every JQL query: pass `nextPageToken` until `isLast = true`. Max 100 issues per page.
4. **Never guess.** If a value is missing, write **`TBD`** with a one-line reason.

### Story points field
- Field ID: `customfield_10016`
- Always request it explicitly in JQL `fields` array.

### SRT engineer roster
Count only tickets assigned to these engineers. Anyone else → `Out of team`:

| Name |
|---|
| David Garcia |
| Navinchandra Gupta |
| Gustavo Silva |
| Grace Saint |
| Jummy Sanni |

Also resolve full Jira display names for active assignees matching `Chris` and `Mike` on the SRT team.

### Work classification (label first, then epic fallback)

| Category | Jira label | Anchor epic / project |
|---|---|---|
| **Product** | `SRT-RO` | Product epics under `PT-869` and related |
| **KTLO** | `SRT-KTLO` | Epic `SALES-8534` |
| **Domain Tech Debt** | `SRT-Domain-Tech-Debt` | `PT-1119` / `SALES-9039` |
| **Software Upgrades** | `SRT-Software-Upgrades` | `PT-1118` / `SALES-9041` |
| **Unclassified** | (none) | List separately |

### Capacity targets (compare actuals — do not invent)

| Bucket | Gross % |
|---|---|
| Product | 48% |
| Tech Health | 32% |
| Buffer | 20% |

Within Tech Health: KTLO 40% / Domain Tech Debt 50% / Software Upgrades 10%.

### Clone ticket handling
- Prefer the ticket that reached `Done` in the reporting month.
- Note `CLONE -` in summary column.
- Do not double-count clone + original in the same month.

---

## Step 3 — JQL scope definitions

Substitute `{quarter_tags}` with comma-separated quoted labels, e.g. `"2026Q2", "2026Q1"`.

### A. SALES execution scope
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
```

### B. PT portfolio project scope
```jql
project = PT
AND issuetype = Project
AND labels = squad-SALES
AND labels in ({quarter_tags})
AND status not in ("Won't Do", Cancelled)
```

### C. SALES epic scope
```jql
project = SALES
AND issuetype = Epic
AND labels in ({quarter_tags})
```

### D. Optional SELLTECH cross-project
```jql
project = SELLTECH
AND issue in linkedIssues("project = SALES AND labels in ({quarter_tags})")
```

---

## Step 4 — Pull five MBR sections

For every table: include a **Source** column citing Jira key or JQL + result count.  
Ticket links: `https://trr-prod.atlassian.net/browse/{KEY}`

### Section 1: Projects in Flight

```jql
project = PT
AND issuetype = Project
AND labels = squad-SALES
AND labels in ({quarter_tags})
AND status NOT IN (Done, "Won't Do", Cancelled, "Not Started")
ORDER BY updated DESC
```

| PT Key | Summary | Status | Owner | Due Date | Quarter Labels | Last Updated | Linked SALES Epics | Jira URL | Source |

List child SALES Epics (parent link) that are not `Done`.

### Section 2: Development Readiness

```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status = "To Do"
AND "Story Points" is not EMPTY
AND parent is not EMPTY
ORDER BY priority DESC, "Story Points" DESC
```

**Filters:** pointed, has epic, not blocked/flagged, ARB label present (`ARB_Approved`, `ARB_Not_Required`, `ARB_Approved_Not_required`, or variant found in data). If no ARB labels in scope, note `ARB gate: TBD` and list all pointed To Do tickets.

| Key | Summary | Points | Epic | Category | Assignee | ARB Label | Priority | Jira URL | Source |

Group by category.

### Section 3: Backlog Status

```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status != Done
AND status != "Won't Do"
AND status != Cancelled
```

Provide:
- **3a.** Open backlog by category (count, points, oldest ticket)
- **3b.** Open backlog by issue type
- **3c.** Health signals: unpointed, no epic, blocked, flagged, overdue

### Section 4: Velocity / Tech Performance

**4a. Throughput (3 months):**
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status changed to Done DURING ("{month_start}", "{month_end}")
ORDER BY resolutiondate DESC
```

| Month | Tickets Done | Story Points Done | Avg Points/Ticket | Source JQL |

**4b. Per engineer (reporting month):** group by SRT roster.

**4c. Capacity split (reporting month):** actual points % vs targets.

**4d. Sprint overlap:** if sprint field available; else `TBD`.

### Section 5: Releases & Incidents

**5a. Releases:**
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status = Done
AND resolved >= {reporting_start}
AND resolved <= {reporting_end}
ORDER BY resolved DESC
```

Include if: `CAB_Approved` label, changelog shows `Ready for Deploy` → `Done`, or `PR_created` + resolved in month.

| Key | Summary | Resolved Date | Points | Epic | Category | Deploy Labels | Jira URL | Source |

**5b. Incidents** (try in order, cite which tier used):

1. Bugs under `SALES-8534`, priority Highest/High, resolved in month
2. Labels `incident`, `pagerduty`, `PagerDuty`
3. Summary ~ incident / outage / "production incident"

**Sev-1 reference:** inaccurate TRR Price >1k items; lead conversion failure; incentive dashboard downtime.

If none match: `None matched scope — manual PagerDuty / #sales-tech-incidents review required`.

---

## Step 5 — Notion MBR page structure

**Title (exact):** `{page_title}`

```
# MBR Data — {reporting_month_name} {reporting_year}

**Generated:** {UTC timestamp}
**Reporting period:** {reporting_start} – {reporting_end} (America/Los_Angeles)
**Quarter scope:** {quarter_tags}
**Jira site:** https://trr-prod.atlassian.net

## Executive Summary
(max 5 bullets — numbers must match tables)

## 1. Projects in Flight
## 2. Development Readiness
## 3. Backlog Status
## 4. Velocity / Tech Performance
## 5. Releases & Incidents
## Appendix A: Query Log
## Appendix B: Data Gaps
```

**Formatting:** link ticket keys, use tables, `TBD` never guessed, mirror SRT Weekly Jira Snapshot style.

---

## Step 6 — Validation checklist

- [ ] `page_title` format correct
- [ ] New MBR child page (not overwrite) OR existing duplicate reported
- [ ] All 5 sections present
- [ ] Quarter boundary rule applied
- [ ] All JQL paginated to completion
- [ ] No hallucinated ticket keys
- [ ] Appendix A + B complete
- [ ] Executive Summary matches tables
- [ ] Recommendations file created (Step 8)
- [ ] Final message includes both URLs (Step 7)

---

## Step 7 — Final response to user (required)

Your **last message** must lead with URLs. Do not end with only a data summary.

### If MBR page was created

```
## MBR Data Ready

**Notion page:** {full MBR child page URL}

- **Title:** {page_title}
- **Reporting period:** {reporting_start} – {reporting_end}
- **Status:** Created

**Prompt recommendations:** {recommendations file URL or path}

Open the MBR link for the full report. Review recommendations before the next run.
```

### If MBR page already existed

```
## MBR Data Already Exists

**Notion page:** {existing MBR page URL}

- **Title:** {page_title}
- **Status:** Skipped — page already exists

**Prompt recommendations:** {recommendations file URL or path}
```

### If MBR Notion create failed

```
## MBR Data — Notion Create Failed

**Notion page:** TBD — page was not created
**Prompt recommendations:** {URL or TBD — reason}

- **Error:** {brief error}
```

### Response rules

- Full `https://` URLs on their own lines after `**Notion page:**` and `**Prompt recommendations:**`
- MBR URL = child page created, **not** the parent `388d553c3a2e803597ebf5ee2265a3e7`
- Never say "I've created the page" without the URL

---

## Step 8 — Draft prompt improvement recommendations (required)

After the MBR pull (success, partial, or failed), draft a **recommendations markdown file**.  
**Do not edit this prompt file during the run.** Only produce recommendations for human review.

### Always create — every run

Including failures and duplicate-skip runs. If clean: write `No prompt changes recommended this run`.

### Capture when you learn

- Empty/unexpected JQL results
- Wrong field IDs or label names
- Pagination/API limits
- Mis-classification
- Clone dedup ambiguity
- Notion formatting issues
- Redundant queries or better data sources

### Output (one per run — never overwrite)

| Destination | Path / title |
|---|---|
| **Notion (preferred)** | Child of `388d553c3a2e803597ebf5ee2265a3e7`, title `{recommendations_title}` |
| **Repository (if git write)** | `docs/srt-mbr-prompt-recommendations/{run_date}.md` |

If both available, write both. Commit message: `MBR agent prompt recommendations {run_date}`

### Recommendations file — use this template

```markdown
# MBR Agent Prompt Recommendations — run {run_date}

**Reporting period:** {reporting_start} – {reporting_end}
**MBR data page:** {link or TBD / skipped}
**Run outcome:** Success | Partial | Failed
**Generated:** {UTC timestamp}

---

## Executive summary

(2–4 sentences: run health and whether prompt changes are recommended.)

**Recommendation count:** {N} proposed changes ({H} high / {M} medium / {L} low)
**Bottom line:** Adopt now | Review later | No changes needed

---

## Proposed prompt changes

### REC-001: {Short title}

| Field | Value |
|---|---|
| **Priority** | High / Medium / Low |
| **Section affected** | e.g. Section 4c, JQL scope B |
| **Problem observed** | What happened this run |
| **Evidence** | Jira keys, counts, errors, field values |
| **Proposed change** | Exact text to add, replace, or remove |
| **Expected benefit** | e.g. fewer API calls, accurate counts |
| **Risk if adopted** | e.g. broader scope |

**Current prompt text:**
{quote or n/a}

**Proposed prompt text:**
{exact replacement or addition}

---

## Discovered constants

| Constant | Prompt assumed | Actual this run | Recommend |
|---|---|---|---|
| Story points field | customfield_10016 | | Keep / Update |
| ARB label variants | ARB_Approved, ... | | Keep / Update |
| Quarter labels | 2026Q2 | | Keep / Update |
| Engineer roster | (see Step 2) | Assignees seen | Keep / Update |
| Incident search | 3-tier | Tier used | Keep / Update |

---

## Query efficiency log

| Query purpose | JQL (abbreviated) | Issues returned | Pages fetched | Redundant? | Suggestion |
|---|---|---|---|---|---|

---

## Data gaps that blocked accuracy

| Gap | Impact on MBR | Suggested fix |
|---|---|---|

---

## Items reviewed — no change recommended

- {what worked correctly}

---

## For the human reviewer

- [ ] Recommendations reviewed
- [ ] Changes merged into `docs/srt-mbr-complete-automation-prompt.md`
- [ ] Rejected recommendations noted below

**Reviewer notes:**

_(leave blank for human)_
```

### Recommendation rules

1. Be specific — exact JQL, field IDs, labels, prompt sentences
2. Every REC must cite evidence from this run
3. One concern per REC item
4. **High** = wrong data/failure; **Medium** = inefficiency/TBD; **Low** = cosmetic
5. Flag blocked ideas as `Blocked: needs human setup`

### What NOT to do

- Do not modify the live prompt during the run
- Do not overwrite prior recommendations files
- Do not recommend without evidence
- Do not skip recommendations when MBR fails

---

## MCP tools

| Step | Tool |
|---|---|
| Jira cloud ID | Atlassian: `getAccessibleAtlassianResources` |
| Jira queries | Atlassian: `searchJiraIssuesUsingJql` (paginate) |
| Issue detail | Atlassian: `getJiraIssue` |
| Notion read | Notion: `notion-fetch`, `notion-search` |
| Notion write | Notion: `notion-create-pages` |

---

## Error handling

| Situation | Action |
|---|---|
| Jira auth fails | Stop. No Notion pages. Report error. |
| MBR Notion fails | Pull Jira data if possible. Still write recommendations if able. |
| Duplicate MBR page | Skip create. Use existing URL. Still write recommendations. |
| JQL returns 0 | Keep section. `None matched scope` + JQL. |
| Field missing | `TBD` + Appendix B / Data gaps. |
| Recommendations write fails | MBR URL still required. `Prompt recommendations: TBD — {reason}` |

---

## Reference context (read-only)

| Resource | Purpose |
|---|---|
| Notion: SRT Tech Health & KTLO Taxonomy | Label/epic classification |
| Notion: SRT Engineering Process Reference | Capacity model, workflow |
| Notion: SRT Weekly Jira Snapshot | Output format template |
| Notion: SRT Incident Management Plan | Sev-1 definitions |
| Notion parent `388d553c3a2e803597ebf5ee2265a3e7` | Output destination |

---

*End of complete automation prompt.*
