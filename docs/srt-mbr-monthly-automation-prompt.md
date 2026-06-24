# SRT MBR Data Pull — Monthly Cursor Automation Prompt

> **How to use:** Copy everything below the `---` line into your Cursor Cloud Agent / Automation prompt body.  
> **Schedule:** Run monthly on the 1st calendar day (or first business day after month-end).  
> **Output:** New Notion child page each run — never overwrite prior runs.

---

## Mission

Pull Monthly Business Review (MBR) data for the **SRT / Salesforce Engineering** team for the **last full calendar month**. Source data from **Jira** (`trr-prod.atlassian.net`). Write results to a **new child page** under the Notion parent below.

**Team:** SRT (Sales Revenue Technology) / Salesforce Engineering  
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
| `quarter_tags` | Start with `[quarter_tag]`. If reporting month is **January, April, July, or October**, also include `prior_quarter_tag` (quarter-boundary carryover rule) |
| `page_title` | `MBR Data - {reporting_month_name} {reporting_year} (run {run_date})` |

**Example:** Run on `2026-07-01` → reporting month = June 2026 → title = `MBR Data - June 2026 (run 2026-07-01)`.

**Label format:** Jira labels have **no `#` prefix**. Use `2026Q2`, not `#2026Q2`.

---

## Step 1 — Idempotency check (Notion)

**Parent page ID:** `388d553c3a2e803597ebf5ee2265a3e7`  
**Parent page title:** `2026 MBR data Output from Cursor`

Before creating anything:

1. Fetch the parent page and list its child pages.
2. Search for an existing child with title **exactly** equal to `page_title`.
3. **If found:** Stop. Report the existing page URL. Do **not** create or overwrite.
4. **If not found:** Create a **new child page** under this parent.

Use Notion MCP `notion-create-pages` with:
```json
{
  "parent": { "type": "page_id", "page_id": "388d553c3a2e803597ebf5ee2265a3e7" },
  "pages": [{ "properties": { "title": "{page_title}" }, "content": "..." }]
}
```

**Never** update a prior run's page. Each month = new child page.

---

## Step 2 — Jira connection & query rules

### Connection
1. Call `getAccessibleAtlassianResources` to get `cloudId` for `trr-prod.atlassian.net`.
2. Use **`searchJiraIssuesUsingJql`** for all data pulls (deterministic). Do **not** use semantic/Rovo search for counts or metrics.
3. **Paginate** every JQL query: pass `nextPageToken` until `isLast = true`. Jira returns max 100 issues per page.
4. **Never guess.** If a value is missing or a field is unavailable, write **`TBD`** with a one-line reason.

### Story points field
- Field ID: `customfield_10016`
- Always request it explicitly in JQL `fields` array.

### SRT engineer roster (for per-person metrics)
Count only tickets assigned to these engineers. Map display names via Jira `assignee`. Anyone else → bucket as `Out of team`:

| Name |
|---|
| David Garcia |
| Navinchandra Gupta |
| Gustavo Silva |
| Grace Saint |
| Jummy Sanni |

Also look up active assignees matching `Chris` and `Mike` on the SRT team if tickets are assigned to them; include their full Jira display names in the roster once resolved.

### Work classification (labels + epic fallback)

Use **label first**, then parent epic/project. If neither matches → `Unclassified`.

| Category | Jira label | Anchor epic / project |
|---|---|---|
| **Product** | `SRT-RO` | Product epics under `PT-869` and related product projects |
| **KTLO** | `SRT-KTLO` | Epic `SALES-8534` (`[26Q2] SRT KTLO`) |
| **Domain Tech Debt** | `SRT-Domain-Tech-Debt` | `PT-1119` / epic `SALES-9039` |
| **Software Upgrades** | `SRT-Software-Upgrades` | `PT-1118` / epic `SALES-9041` |
| **Unclassified** | (none) | List separately |

### Capacity targets (compare actuals — do not invent)

From SRT capacity model:

| Bucket | Gross % | Notes |
|---|---|---|
| Product | 48% | Of total capacity |
| Tech Health | 32% | KTLO + Tech Debt + Upgrades combined |
| Buffer | 20% | Meetings, Zendesk, ad hoc |

Within Tech Health (quarterly average target):

| Sub-bucket | Target % |
|---|---|
| KTLO | 40% |
| Domain Tech Debt | 50% |
| Software Upgrades | 10% |

Compute **actual** split from completed story points in the reporting month. Show delta vs target.

### Clone ticket handling
The team uses clone-and-carry at sprint close. For velocity and release counts:
- Prefer counting the ticket that reached `Done` in the reporting month.
- If summary starts with `CLONE -`, note it in the table.
- Do not double-count a clone and its original if both resolved in the same month (dedupe by epic + similar summary or issue link if present).

---

## Step 3 — JQL scope definitions

Substitute `{quarter_tags}` with comma-separated quoted labels, e.g. `"2026Q2", "2026Q1"`.

### A. SALES execution scope (Stories, Tasks, Bugs, Spikes)
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
```

### B. PT portfolio project scope (Projects in Flight)
```jql
project = PT
AND issuetype = Project
AND labels = squad-SALES
AND labels in ({quarter_tags})
AND status not in ("Won't Do", Cancelled)
```

### C. SALES epic scope (supporting detail under projects)
```jql
project = SALES
AND issuetype = Epic
AND labels in ({quarter_tags})
```

### D. Optional cross-project (SELLTECH linked to in-scope SALES work)
```jql
project = SELLTECH
AND issue in linkedIssues("project = SALES AND labels in ({quarter_tags})")
```
If no useful results, note `SELLTECH: none in scope` — do not force-include.

---

## Step 4 — Pull five sections

For every table: include a **Source** column or footnote citing the Jira key or JQL query + result count.  
Ticket links: `https://trr-prod.atlassian.net/browse/{KEY}`

---

### Section 1: Projects in Flight

**What:** Active portfolio projects and their in-flight epics.

**PT Projects query:**
```jql
project = PT
AND issuetype = Project
AND labels = squad-SALES
AND labels in ({quarter_tags})
AND status NOT IN (Done, "Won't Do", Cancelled, "Not Started")
ORDER BY updated DESC
```

**In-flight definition (PT):** status in (`Discovery`, `Definition`, `Reqs Locked`, `Ready for Dev`, `In Progress`) or any status not in terminal/idle states above.

**Table — Projects in Flight:**

| PT Key | Summary | Status | Owner | Due Date | Quarter Labels | Last Updated | Linked SALES Epics | Jira URL | Source |

For each PT project, also list child **SALES Epics** (via parent link) that are not `Done`.

**Fields to pull:** `summary`, `status`, `assignee`, `duedate`, `labels`, `updated`, `parent`

---

### Section 2: Development Readiness

**What:** Work pointed and ready to start next month (groomed backlog).

**Query:**
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status = "To Do"
AND "Story Points" is not EMPTY
AND parent is not EMPTY
ORDER BY priority DESC, "Story Points" DESC
```

**Readiness filters (ticket must pass all):**
- Story points (`customfield_10016`) is set
- Parent epic is set
- NOT blocked: status != `Blocked` and flagged != Impediment
- ARB gate passed: has label `ARB_Approved` OR `ARB_Not_Required` OR `ARB_Approved_Not_required` OR `ARB_Approved_Not required` (check which variant exists in data)
- If none of the ARB labels exist on any ticket in scope, note `ARB gate: TBD — no ARB labels found in scope` and list all pointed To Do tickets anyway

**Table — Development Readiness:**

| Key | Summary | Points | Epic | Category | Assignee | ARB Label | Priority | Jira URL | Source |

Group rows by category (Product / KTLO / Domain Tech Debt / Software Upgrades / Unclassified).

---

### Section 3: Backlog Status

**What:** Open work inventory by category and health signals.

**Base open backlog query:**
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status != Done
AND status != "Won't Do"
AND status != Cancelled
```

**Provide these sub-tables:**

**3a. Open backlog by category**

| Category | Open Count | Total Points | Oldest Ticket (Key + Age in Days) | Source JQL |

**3b. Open backlog by issue type**

| Issue Type | Count | Points | Source JQL |

**3c. Backlog health signals**

| Signal | Count | Source JQL |
|---|---|---|
| Unpointed (no story points) | | `"Story Points" is EMPTY` |
| No epic (orphan) | | `parent is EMPTY` |
| Blocked | | `status = Blocked` |
| Flagged (Impediment) | | `flagged = Impediment` |
| Overdue (due date < reporting_end, still open) | | `duedate < {reporting_end}` |

If product vs technology split is available via labels/epic, show it. Otherwise write `Product vs Tech split: derived from classification table above`.

---

### Section 4: Velocity / Tech Performance

#### 4a. Monthly throughput trend (3 months)

For each month — reporting month, prior month, two months prior — run:

```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status changed to Done DURING ("{month_start}", "{month_end}")
ORDER BY resolutiondate DESC
```

**Table — Throughput trend:**

| Month | Tickets Done | Story Points Done | Avg Points per Ticket | Source JQL |

#### 4b. Per-engineer performance (reporting month only)

Using the same Done query for the reporting month, group by assignee (SRT roster only).

**Table — Per engineer:**

| Engineer | Tickets Done | Points Done | Avg Points per Ticket | Source |

Add row: **Team total** and **Out of team** (if any).

#### 4c. Capacity split — actual vs target (reporting month)

Sum story points completed in reporting month by category (classification rules above).

**Table — Capacity split:**

| Bucket | Points Done | % of Total | Target % | Delta (pp) |
|---|---|---|---|---|
| Product | | | 48% | |
| KTLO | | | (32% × 40% = 12.8% of gross) | |
| Domain Tech Debt | | | (32% × 50% = 16.0% of gross) | |
| Software Upgrades | | | (32% × 10% = 3.2% of gross) | |
| Unclassified | | | — | |
| **Tech Health subtotal** | | | 32% | |

Note methodology in a footnote. Buffer (20%) is not directly observable from Jira — write `Buffer: not measurable from Jira (target 20%)`.

#### 4d. Sprint overlap (if available)

If Jira sprint field is returned in issue data, list sprints overlapping the reporting month and points completed per sprint.  
If sprint data is unavailable: `Sprint breakdown: TBD — sprint field not returned`.

---

### Section 5: Releases & Incidents

#### 5a. Releases (shipped in reporting month)

**Query:**
```jql
project = SALES
AND labels in ({quarter_tags})
AND issuetype in (Story, Task, Bug, Spike)
AND status = Done
AND resolved >= {reporting_start}
AND resolved <= {reporting_end}
ORDER BY resolved DESC
```

**Release filter:** Include ticket if ANY of:
- Has label `CAB_Approved`
- Status changelog shows transition through `Ready for Deploy` before `Done`
- Has label `PR_created` and resolution in reporting month (note as "deployed / completed")

If changelog is too expensive to pull for every ticket, pull changelog for candidates with `CAB_Approved` or `PR_created` labels only and note `Release filter: partial — changelog sampled for CAB/PR tickets`.

**Table — Releases:**

| Key | Summary | Resolved Date | Points | Epic | Category | Deploy Labels | Jira URL | Source |

#### 5b. Production incidents

Search in order; use the first approach that returns data. Cite which approach was used.

**Attempt 1 — High-severity KTLO bugs resolved in month:**
```jql
project = SALES
AND issuetype = Bug
AND parent = SALES-8534
AND status = Done
AND resolved >= {reporting_start}
AND resolved <= {reporting_end}
AND priority in (Highest, High)
ORDER BY resolved DESC
```

**Attempt 2 — Incident/pagerduty labels:**
```jql
project = SALES
AND labels in (incident, pagerduty, PagerDuty)
AND resolved >= {reporting_start}
AND resolved <= {reporting_end}
ORDER BY resolved DESC
```

**Attempt 3 — Keyword in summary:**
```jql
project = SALES
AND (summary ~ incident OR summary ~ outage OR summary ~ "production incident")
AND resolved >= {reporting_start}
AND resolved <= {reporting_end}
ORDER BY resolved DESC
```

**Table — Incidents:**

| Key | Summary | Resolved Date | Impact | Severity/Priority | Category | Jira URL | Source |

Extract impact from description or most recent comment if available; else `TBD`.

If no incidents match any query: keep the section and write `None matched scope — manual PagerDuty / #sales-tech-incidents review required`.

**Sev-1 reference (from SRT Incident Management Plan):**
- Inaccurate TRR Price for >1k items
- Lead Conversion failure
- Incentive dashboard downtime

---

## Step 5 — Notion page structure

**Title (exact):** `{page_title}`

### Page content layout (in this order)

```
# MBR Data — {reporting_month_name} {reporting_year}

**Generated:** {UTC timestamp}
**Reporting period:** {reporting_start} – {reporting_end} (America/Los_Angeles)
**Quarter scope:** {quarter_tags, comma-separated}
**Jira site:** https://trr-prod.atlassian.net
**Parent:** 2026 MBR data Output from Cursor

---

## Executive Summary
(Max 5 bullets. Every number must match a table below.)
- Projects in flight: {count}
- Dev readiness (pointed To Do): {count} tickets / {points} points
- Open backlog: {count} tickets / {points} points
- Completed this month: {count} tickets / {points} points
- Releases shipped: {count} | Incidents: {count or TBD}

---

## 1. Projects in Flight
{table}

## 2. Development Readiness
{table, grouped by category}

## 3. Backlog Status
{3a, 3b, 3c tables}

## 4. Velocity / Tech Performance
{4a, 4b, 4c, 4d tables}

## 5. Releases & Incidents
### 5a. Releases
{table}
### 5b. Production Incidents
{table or TBD note}

---

## Appendix A: Query Log
| # | Section | JQL | Issues Returned |
|---|---|---|---|
| 1 | ... | ... | ... |

## Appendix B: Data Gaps
| Item | Reason |
|---|---|
| ... | TBD — {reason} |
```

### Formatting rules
1. Every numeric figure must trace to a Jira key or JQL query in Appendix A.
2. Ticket keys must be markdown links: `[SALES-1234](https://trr-prod.atlassian.net/browse/SALES-1234)`
3. Use Notion markdown tables with header rows.
4. Missing data → `TBD` — never estimate or infer.
5. Mirror the table style of the existing **SRT Weekly Jira Snapshot** Notion pages.

---

## Step 6 — Validation checklist (run before finishing)

Confirm all of the following before marking the task complete:

- [ ] `page_title` matches format exactly: `MBR Data - {Month} {Year} (run YYYY-MM-DD)`
- [ ] New child page created under parent `388d553c3a2e803597ebf5ee2265a3e7` (not an overwrite)
- [ ] All 5 sections present (even if empty — use "None matched scope")
- [ ] Quarter boundary rule applied (prior quarter tag included in Jan/Apr/Jul/Oct runs)
- [ ] All JQL queries paginated to completion
- [ ] Every ticket key in the report was returned by Jira (no hallucinated keys)
- [ ] Appendix A lists every JQL with result counts
- [ ] Appendix B lists every `TBD` with reason
- [ ] Executive Summary numbers match section tables

**On completion:** Return the new Notion page URL to the user.

---

## Reference context (read-only — do not write to these)

| Resource | Purpose |
|---|---|
| Notion: `SRT Tech Health & KTLO Taxonomy - Team Reference` | Label/epic classification |
| Notion: `SRT Engineering Process Reference` | Capacity model, workflow states |
| Notion: `SRT Weekly Jira Snapshot` | Output format template |
| Notion: `SRT Incident Management Plan` | Sev-1 definitions, incident process |
| Notion parent: `388d553c3a2e803597ebf5ee2265a3e7` | Output destination |

---

## MCP tools to use

| Step | Tool |
|---|---|
| Jira cloud ID | Atlassian: `getAccessibleAtlassianResources` |
| All Jira queries | Atlassian: `searchJiraIssuesUsingJql` (paginate) |
| Issue detail (if needed) | Atlassian: `getJiraIssue` with `fields: ["*all"]` |
| Parent page check | Notion: `notion-fetch` on parent ID |
| Duplicate check | Notion: `notion-search` under parent for `page_title` |
| Create output | Notion: `notion-create-pages` |

---

## Error handling

| Situation | Action |
|---|---|
| Jira auth fails | Stop. Report error. Do not create Notion page. |
| Notion auth fails | Stop after pulling Jira data. Return data as markdown in chat. |
| Duplicate page title exists | Stop. Return existing page URL. |
| JQL returns 0 for a section | Keep section. Write `None matched scope` + JQL used. |
| Field not available | Write `TBD` in cell + add row to Appendix B. |
| Query timeout | Retry once. If still failing, note partial data in Appendix B. |

---

## Step 7 — Final response to user (required)

When the run finishes, your **last message to the user** must be short and must lead with the Notion page URL. Do not end with only a summary of the data — the deliverable is the link.

### If a new page was created

1. After `notion-create-pages`, capture the returned page URL from the tool response.
2. If the tool returns only a page ID, fetch the page with `notion-fetch` to get the canonical URL.
3. Reply using this exact format:

```
## MBR Data Ready

**Notion page:** {full Notion URL}

- **Title:** {page_title}
- **Reporting period:** {reporting_start} – {reporting_end}
- **Status:** Created

Open the link above for the full report.
```

The Notion URL must be:
- A full clickable link starting with `https://`
- The URL of the **child page you created**, not the parent page
- On its own line immediately after `**Notion page:**`

### If a duplicate page already exists (idempotency)

Do not create a new page. Reply:

```
## MBR Data Already Exists

**Notion page:** {existing page URL}

- **Title:** {page_title}
- **Status:** Skipped — page already exists for this reporting period
```

### If Notion create failed

Reply:

```
## MBR Data — Notion Create Failed

**Notion page:** TBD — page was not created

- **Error:** {brief error}
- **Action:** Re-run after fixing Notion auth or permissions
```

Include a brief summary of what was pulled from Jira only if the page could not be created.

### Response rules

- The **first line after the heading** must be the Notion page URL (or `TBD` with reason).
- Do not bury the URL in a paragraph or bullet list without the `**Notion page:**` label.
- Do not reply with "I've created the page" without including the URL.
- Do not link to the parent page (`388d553c3a2e803597ebf5ee2265a3e7`) as the deliverable.

---

*End of prompt. Copy from "Mission" through "Step 7" into your Cursor Automation agent instructions.*
