# SRT Sprint Retrospective Automation

Automated sprint retrospective report generator for the Salesforce Release Technology (SRT) team at The RealReal.

## Usage

```bash
# Build sprint data from embedded Jira records (or save MCP response to data/sprint_issues.json)
python3 scripts/build_sprint_json_from_mcp.py

# Generate the retrospective report
python3 scripts/generate_sprint_report.py
```

Output: `reports/sprint-retro-2026-06-24.md`

## Data Sources

- **Sprint tickets:** SALES Jira board (ID 10), sprint `Sales 6/11 - 6/24`
- **Historical velocity:** `data/historical_sprints.json`
- **Jira fields:** Story points (`customfield_10026`), Reason for Bug (`customfield_10142`)
