# Add-on prompt — Self-improvement recommendations (.md)

> Append this block to the end of your SRT MBR monthly automation prompt (after the Notion URL response step).

---

## Step 8 — Draft prompt improvement recommendations (required)

After completing the MBR data pull (or after a partial/failed run), review what you learned during execution. Draft a **recommendations markdown file** so future runs can be more efficient.

**Do not edit the live automation prompt yourself.** Only produce a recommendations file for human review and merge.

---

### When to write recommendations

Always create a recommendations file at the end of every run.

| Situation | What to capture |
|---|---|
| JQL returned unexpected empty results | Propose revised JQL or broader/narrower scope |
| Field ID or label name differed from prompt | Record the actual value found in Jira |
| Pagination or API limits caused incomplete data | Propose batching strategy or slimmer `fields` list |
| Classification logic mis-bucketed tickets | Propose label/epic rule updates |
| Duplicate detection or clone handling was ambiguous | Propose dedup rule |
| Notion create/formatting failed or was slow | Propose content structure changes |
| A query could be combined or eliminated | Propose fewer round-trips |
| You discovered a better data source (filter, board, epic) | Propose scope change with evidence |
| Run completed with no issues | Write `No prompt changes recommended this run` in the summary — still create the file |

---

### Output file

Create **one new file per run**. Never overwrite prior recommendation files.

#### Option A — Notion (preferred for monthly automation)

Create a **new child page** under parent `388d553c3a2e803597ebf5ee2265a3e7` with:

- **Title:** `MBR Prompt Recommendations - run {run_date}.md`
- **Content:** full markdown from the template below (Notion markdown)

#### Option B — Repository (if git write access is available)

Write to:

```
docs/srt-mbr-prompt-recommendations/{run_date}.md
```

Use `YYYY-MM-DD` for `{run_date}`. Commit with message: `MBR agent prompt recommendations {run_date}`

If both Notion and git are available, do **both**. If only one is available, use that one.

---

### Recommendations file template

Use this structure exactly:

```markdown
# MBR Agent Prompt Recommendations — run {run_date}

**Reporting period:** {reporting_start} – {reporting_end}  
**MBR data page:** {link to MBR Notion page created this run, or "TBD / skipped"}  
**Run outcome:** Success | Partial | Failed  
**Generated:** {UTC timestamp}

---

## Executive summary

(2–4 sentences: overall run health and whether prompt changes are recommended.)

**Recommendation count:** {N} proposed changes ({H} high / {M} medium / {L} low)  
**Bottom line:** Adopt now | Review later | No changes needed

---

## Proposed prompt changes

(Repeat this block for each recommendation.)

### REC-{NNN}: {Short title}

| Field | Value |
|---|---|
| **Priority** | High / Medium / Low |
| **Section affected** | e.g. Section 4c, Step 0, JQL scope B |
| **Problem observed** | What happened this run |
| **Evidence** | Jira keys, JQL result counts, error text, or field values |
| **Proposed change** | Exact text to add, replace, or remove in the prompt |
| **Expected benefit** | e.g. fewer API calls, accurate counts, less TBD |
| **Risk if adopted** | e.g. broader scope, may include non-SRT work |

**Current prompt text (if applicable):**
```
{quote the relevant snippet from the prompt, or "n/a"}
```

**Proposed prompt text:**
```
{exact replacement or addition}
```

---

## Discovered constants (update prompt lookup tables)

Record anything that differed from the prompt assumptions:

| Constant | Prompt assumed | Actual value this run | Recommend |
|---|---|---|---|
| Story points field | customfield_10016 | | Keep / Update |
| ARB label variants | ARB_Approved, ... | | Keep / Update |
| Quarter labels | 2026Q2 | | Keep / Update |
| Engineer roster | {names} | Assignees seen in data | Keep / Update |
| Incident search | 3-tier | Results from tier used | Keep / Update |

---

## Query efficiency log

| Query purpose | JQL (abbreviated) | Issues returned | Pages fetched | Slow or redundant? | Suggestion |
|---|---|---|---|---|---|
| | | | | Yes / No | |

---

## Data gaps that blocked accuracy

| Gap | Impact on MBR | Suggested prompt or process fix |
|---|---|---|
| | | |

---

## Items reviewed — no change recommended

- {List things you verified worked correctly, to avoid re-litigating next run}

---

## For the human reviewer

- [ ] Recommendations reviewed
- [ ] Changes merged into `docs/srt-mbr-monthly-automation-prompt.md`
- [ ] Add-on prompts updated if needed
- [ ] Rejected recommendations noted below

**Reviewer notes:**

_(leave blank for human)_
```

---

### Rules for writing good recommendations

1. **Be specific.** Propose exact JQL, field IDs, label strings, or prompt sentences — not vague advice.
2. **Show evidence.** Every recommendation must cite data from this run (ticket key, count, error message).
3. **One concern per REC item.** Do not bundle unrelated fixes.
4. **Prioritize:**
   - **High** — wrong numbers, missed scope, or run failure
   - **Medium** — inefficiency, extra API calls, frequent TBD
   - **Low** — formatting, optional optimizations
5. **Do not recommend changes** that require secrets, new MCP servers, or permissions the agent does not have — flag those as `Blocked: needs human setup`.
6. **Reference the canonical prompt file:** `docs/srt-mbr-monthly-automation-prompt.md`

---

### Include recommendations URL in final user response

Append to the Step 7 user response (after the MBR data page URL):

```
**Prompt recommendations:** {Notion URL or git file path to recommendations .md}
```

Example complete closing message:

```
## MBR Data Ready

**Notion page:** https://www.notion.so/...

- **Title:** MBR Data - June 2026 (run 2026-07-01)
- **Reporting period:** 2026-06-01 – 2026-06-30
- **Status:** Created

**Prompt recommendations:** https://www.notion.so/MBR-Prompt-Recommendations-run-2026-07-01-...

Open the MBR link for the full report. Review the recommendations file before the next run.
```

If recommendations file could not be created, write:

```
**Prompt recommendations:** TBD — {reason}
```

---

### What NOT to do

- Do **not** modify `docs/srt-mbr-monthly-automation-prompt.md` or any add-on prompt during the run
- Do **not** overwrite a prior run's recommendations file
- Do **not** recommend changes without evidence from this run
- Do **not** skip creating the file when the MBR run fails — failures often produce the most valuable recommendations
