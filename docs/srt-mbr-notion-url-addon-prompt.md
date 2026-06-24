# Add-on prompt — Return Notion page URL

> Append this block to the end of your SRT MBR monthly automation prompt.

---

## Final response to user (required)

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

### Response rules

- The **first line after the heading** must be the Notion page URL (or `TBD` with reason).
- Do not bury the URL in a paragraph or bullet list without the `**Notion page:**` label.
- Do not reply with "I've created the page" without including the URL.
- Do not link to the parent page (`388d553c3a2e803597ebf5ee2265a3e7`) as the deliverable.
