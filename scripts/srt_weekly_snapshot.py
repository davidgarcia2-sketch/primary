#!/usr/bin/env python3
"""Generate SRT Weekly Jira Snapshot markdown for Notion."""

from __future__ import annotations

import json
import os
import sys
from datetime import date
from pathlib import Path

SNAPSHOT_DATE = date(2026, 6, 1)
MOVEMENT_START = date(2026, 5, 25)  # since last Thursday before collection

def adf_text(text: str) -> dict:
    return {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": text}]}]}


def extract_comments(doc: dict | None) -> str:
    if not doc or not doc.get("content"):
        return ""
    parts = []
    for block in doc.get("content", []):
        for inline in block.get("content", []):
            if inline.get("type") == "text":
                parts.append(inline.get("text", ""))
    return "".join(parts).strip()


def main() -> int:
    out_dir = Path(__file__).resolve().parent.parent / "output" / f"srt-weekly-jira-snapshot-{SNAPSHOT_DATE.isoformat()}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Static sections 7-8 from reference (abbreviated for automation)
    header = f"""# Collection metadata
- Collected: {SNAPSHOT_DATE.isoformat()} (automation)
- Movement window: since {MOVEMENT_START.isoformat()} (last Thursday)
- Jira site: https://trr-prod.atlassian.net
- Notion parent (Sales Revenue Technology): 64152ced-2fb9-4080-8adf-3a99e2f4a8c3
- Weekly meeting parent: 372d553c3a2e805e9883fbbb9a548161

---

"""

    projects = {
        "PT-869": {
            "summary": "Stabilize Salesforce-Based Lead Conversion",
            "status": "In Progress",
            "ryg": "Green",
            "due": "2026-06-30",
            "dev_end": "2026-03-27",
            "parent": "PT-793 — Upgraded UX & Secure Customer Data (SRT) — In Progress",
            "comments": "[05/28] Stabilization work continued into the week of 5/25, with a new production validation error identified 5/27 and in active remediation. Guardrail implementation is underway; the outstanding item is a formal decision on the deployment review gate (ARB review vs. ticket checklist) before project close.",
            "epics": [
                ("SALES-8065", "Stabilize Salesforce-Based Lead Conversion", "Done", "30", "2026-03-27"),
            ],
        },
        "PT-947": {
            "summary": "Salesforce Security features",
            "status": "In Progress",
            "ryg": "Green",
            "due": "2026-06-30",
            "dev_end": "2026-03-27",
            "parent": "PT-811 — Tech Lifecycle & Security — In Progress",
            "comments": "[05/28] Phase 2 security work continued into the week of 5/25, with API class versioning advancing and two new requirements added to scope. Persona-based access controls are next in sequence. Leadership should validate Phase 2 backlog volume and pace against the June 30 end date.",
            "epics": [
                ("SALES-8106", "Salesforce Security features Phase 1", "Done", "35", "2026-03-27"),
                ("SALES-8429", "Salesforce Security features Phase 2", "In Progress", "40", "2026-06-30"),
                ("SALES-8925", "Salesforce Security features Phase 3", "To Do", "null", "null"),
            ],
        },
        "PT-1118": {
            "summary": "SRT - Software Upgrades & Technical Compliance",
            "status": "Definition",
            "ryg": "Green",
            "due": "2026-12-31",
            "dev_end": "2026-12-31",
            "parent": "PT-1089 — Foundational Sales Data Structure — Not Started",
            "comments": "[05/28] Summer '26 Release coordination completed during the week of 5/25 with zero defects; production enforcement confirmed for June 5. Q2 compliance backlog has had no sprint movement since 5/19. Leadership attention needed to confirm priority and resource assignment for the compliance queue.",
            "epics": [
                ("SALES-9041", "[26Q2] SRT: Software Upgrades and Technical Compliance Epic", "In Progress", "null", "null"),
                ("SALES-9021", "Salesforce Summer '26 Release Coordination", "Done", "20", "2026-12-31"),
            ],
        },
        "PT-1119": {
            "summary": "Salesforce Tech Debt",
            "status": "Not Started",
            "ryg": "Green",
            "due": "2026-12-31",
            "dev_end": "2026-12-31",
            "parent": "PT-1095 — Optimized Salesforce Experience — Not Started",
            "comments": "[05/28] Domain Tech Debt track active during the week of 5/25, with license cleanup and Zendesk ticket triage in sprint. Legacy KTLO sub-ticket reclassification in progress, feeding the formal tech debt backlog. Parent initiative alignment is pending a structural review to improve Tech Health allocation visibility.",
            "epics": [
                ("SALES-9039", "[26Q2] SRT: Domain Tech Debt", "In Progress", "null", "null"),
            ],
        },
    }

    body = header
    for key, p in projects.items():
        body += f"""# 1–6. JIRA — {key} — {p['summary']}

## Project fields
| Field | Value |
|-------|-------|
| Key | {key} |
| Summary | {p['summary']} |
| Jira Status | {p['status']} |
| Status RYG | {p['ryg']} |
| Target end date (Due Date) | {p['due']} |
| Development End Date | {p['dev_end']} |
| Parent Initiative | {p['parent']} |
| Labels | 2026H1, 2026Q1, 2026Q2 |

## Comments for Status (full text)
```
{p['comments']}
```

## Direct child epics (parent = {key})
| Key | Summary | Status | Epic SP | Due date |
|-----|---------|--------|--------|----------|
"""
        for ek, es, st, sp, dd in p["epics"]:
            body += f"| {ek} | {es} | {st} | {sp if sp else 'null'} | {dd or 'null'} |\n"
        body += "\n---\n\n"

    body += """# 5. Open SRT Action Items (Notion)

See SRT Action Items Tracker database. Query run 2026-06-01: 15 open items (Status not Done/Cancelled), sorted by priority.

| Action Item | Status | Priority | Due date | Project | Notes (abbrev) |
|-------------|--------|----------|----------|---------|------------------|
| Triple-check Tech Health Project Fields | Not Started | High | — | Other | Missing AI Size, Product Brief, Financial Impact |
| Provide formal ALRA project scope and SRT resource requirements | Not Started | High | 2026-06-05 | Other | ALRA PM Jenn Kleinfeld; July 21 prod deadline |
| Review compliance backlog and resource assignment | Not Started | High | — | PT-1118 | Q2 compliance queue |
| Provide confirmed Q3 SRT priority commitments | Not Started | High | 2026-06-15 | Other | Owner Devon Novotnak |
| Respond to sumo issue with virtual appointments | In Progress | High | — | Other | Sumo virtual appts blocked item |
| Manual triage of Zendesk backlog tickets | In Progress | Medium | — | KTLO | ~320 unassigned srt-team tickets |
| Complete Zendesk process diagram in Figma | Not Started | High | — | KTLO | Zendesk triage process doc |
| Research Zoom integration for conversational summaries | In Progress | Medium | — | Other | SALES-9048 / Outreach Optimization |
| Confirm SELL team assignment for SELL-4931 | Not Started | Medium | — | SALES-8845 | UPS webhook / shipping labels |
| Share GPN Salesforce reporting materials | Not Started | Medium | — | Other | Jim Menard / Asset Protection |
| Add required fields to Zendesk submission form | Not Started | Medium | — | KTLO | Form hardening |
| Build knowledge articles for top 10 Zendesk ticket types | Not Started | Medium | — | KTLO | Co-owned with Jummy Sanni |
| Send written suggestions on team problems | Not Started | Low | — | Other | Alex Burton 1:1 follow-up |

---

# 6. Net new movement (sample — status changed / created since 2026-05-25)

| Key | Event | Detail |
|-----|-------|--------|
| PT-1118 | status | Not Started → Discovery → Definition (2026-05-29) |
| PT-869 | updated | Comments for Status updated 2026-05-29 |
| PT-947 | updated | Comments for Status updated 2026-05-29 |
| SALES-9021 | status | Done (2026-05-27) — under PT-1118 |
| SALES-9074, SALES-9079 | created | 2026-05-27 under SALES-8429 |
| SALES-8551 | status | In Progress; SALES-8550 Code Review (2026-05-29) |
| SALES-9089 | status | Done (2026-06-01) |
| SALES-9072 | status | Done (2026-06-01) |
| SALES-9110, SALES-9113, SALES-9112, SALES-9111 | created | 2026-06-01 |

(Full movement tables populated from live Jira queries in Notion publish step.)

---

# Blocked / At Risk

| Key | Summary | Status | Due date | Parent |
|-----|---------|--------|----------|--------|
| SALES-8508 | Appt.Location field blank on SUMO virtual appts in PROD | Blocked | null | SALES-8201 (Sumo Upgrade epic Done) |

---

# Data gaps
- Child story lists under large epics (SALES-8065, SALES-8429) summarized at epic level in this run; full child lists available via Jira.
- Story points on Story/Bug children predominantly null in API (customfield_10016).
- Slack search not executed in this automation pass (see prior week reference for DM Navin/Bryan context on PT-1118 parent initiative discussion).
"""

    (out_dir / "snapshot.md").write_text(body, encoding="utf-8")
    print(f"Wrote {out_dir / 'snapshot.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
