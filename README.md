# SRT Weekly Jira Snapshot

Automation to collect live Jira data for SRT Tech Health projects (PT-869, PT-947, PT-1118, PT-1119), query the Notion SRT Action Items Tracker, and publish structured weekly snapshots to Notion.

## Script

```bash
python3 scripts/srt_weekly_snapshot.py
```

Writes markdown to `output/srt-weekly-jira-snapshot-YYYY-MM-DD/snapshot.md`.

## Notion destinations

- **SRT Weekly Jira Snapshot** — under [Sales Revenue Technology](https://www.notion.so/64152ced2fb940808adf3a99e2f4a8c3)
- **SRT Weekly Jira Snapshot — {date}** — under [Weekly Team Meeting Jira Research](https://www.notion.so/372d553c3a2e805e9883fbbb9a548161)

## 2026-06-01 run

- Hub: https://www.notion.so/372d553c3a2e8125972af06503d27075
- Dated snapshot: https://www.notion.so/372d553c3a2e81239b10c732f8df19f2
