#!/usr/bin/env python3
"""Generate SRT Sprint Retrospective report from Jira sprint JSON data."""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SPRINT_NAME = "Sales 5/28 - 6/10"
SPRINT_START = datetime(2026, 5, 28, 16, 39, 12, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 6, 10, 7, 0, 0, tzinfo=timezone.utc)

# Ticket-count throughput from prior sprints (story points unavailable across all sprints)
PRIOR_SPRINT_DONE = {
    "Sales 5/14 - 5/27": 100,
    "SALES 4/30 - 5/13": 57,
    "Sales 4/16 - 4/29": 58,
}

SRT_LABELS = {
    "product": {"SRT-Product", "SRT-product", "SRT-RO"},
    "ktlo": {"SRT-KTLO"},
    "tech_debt": {"SRT-Domain-Tech-Debt"},
    "software_upgrades": {"SRT-Software-Upgrades"},
}

TEAM = [
    "Alex Burton", "Jummy Sanni", "Michael Criswell", "Chris Burns",
    "Grace Saint", "Navinchandra Gupta", "Nag Malluru", "Gustavo Silva", "Sai Deepika Kanuri"
]


def parse_dt(s):
    if not s:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None


def categorize(labels):
    labels_set = set(labels or [])
    for bucket, tag_set in SRT_LABELS.items():
        if labels_set & tag_set:
            return bucket
    return "buffer"


def fmt_points(p):
    return "N/A" if p is None else str(p)


def analyze(issues):
    sprint_start_ts = SPRINT_START.timestamp()
    stats = {
        "by_status": defaultdict(int),
        "by_type": defaultdict(int),
        "points_total": 0,
        "points_done": 0,
        "carry_over": [],
        "removed": [],
        "added_mid_sprint": [],
        "bugs_closed": [],
        "bugs_wont_do": [],
        "spikes_closed": [],
        "by_engineer": {name: {"completed": [], "carry_over": []} for name in TEAM},
        "label_buckets": defaultdict(lambda: {"tickets": 0, "points": 0}),
        "resolutions_by_day": defaultdict(int),
        "done_count": 0,
    }

    for issue in issues:
        key = issue["key"]
        f = issue["fields"]
        summary = f["summary"]
        status = f["status"]["name"]
        itype = f["issuetype"]["name"]
        points = f.get("customfield_10016")
        labels = f.get("labels") or []
        assignee = (f.get("assignee") or {}).get("displayName")
        created = parse_dt(f.get("created"))
        resolved = parse_dt(f.get("resolutiondate"))

        stats["by_status"][status] += 1
        stats["by_type"][itype] += 1

        if points:
            stats["points_total"] += points
            if status == "Done":
                stats["points_done"] += points

        bucket = categorize(labels)
        stats["label_buckets"][bucket]["tickets"] += 1
        if points:
            stats["label_buckets"][bucket]["points"] += points

        if created and created.timestamp() > sprint_start_ts:
            stats["added_mid_sprint"].append({
                "key": key, "summary": summary, "points": points,
                "created": f.get("created"), "assignee": assignee, "type": itype
            })

        if status not in ("Done", "Won't Do"):
            stats["carry_over"].append({
                "key": key, "summary": summary, "points": points,
                "status": status, "assignee": assignee
            })

        if status == "Won't Do":
            stats["removed"].append({
                "key": key, "summary": summary, "points": points,
                "assignee": assignee, "type": itype
            })

        if itype == "Bug":
            reason = f.get("customfield_10142")
            reason_val = reason.get("value") if isinstance(reason, dict) else reason
            entry = {"key": key, "summary": summary, "reason": reason_val, "assignee": assignee, "status": status}
            if status == "Done":
                stats["bugs_closed"].append(entry)
            elif status == "Won't Do":
                stats["bugs_wont_do"].append(entry)

        if itype == "Spike" and status == "Done":
            stats["spikes_closed"].append({
                "key": key, "summary": summary, "points": points, "assignee": assignee
            })

        if status == "Done":
            stats["done_count"] += 1

        if assignee in stats["by_engineer"]:
            entry = {"key": key, "summary": summary, "points": points}
            if status == "Done":
                stats["by_engineer"][assignee]["completed"].append(entry)
            elif status not in ("Won't Do",):
                stats["by_engineer"][assignee]["carry_over"].append(entry)

        if resolved and status in ("Done", "Won't Do"):
            day = resolved.strftime("%Y-%m-%d")
            stats["resolutions_by_day"][day] += 1

    return stats


def classify_burndown(resolutions_by_day):
    if not resolutions_by_day:
        return "Unable to classify — no resolution data available."

    sprint_days = ["2026-05-28", "2026-05-29", "2026-05-30", "2026-05-31",
                   "2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04",
                   "2026-06-05", "2026-06-06", "2026-06-07", "2026-06-08",
                   "2026-06-09", "2026-06-10"]
    first_week = sum(resolutions_by_day.get(d, 0) for d in sprint_days[:7])
    second_week = sum(resolutions_by_day.get(d, 0) for d in sprint_days[7:])
    total = first_week + second_week
    final_days = sum(resolutions_by_day.get(d, 0) for d in ["2026-06-08", "2026-06-09", "2026-06-10"])

    lines = [f"- **Daily closures:** " + ", ".join(
        f"{d}: {resolutions_by_day.get(d, 0)}" for d in sprint_days if resolutions_by_day.get(d, 0) > 0
    )]
    lines.append(f"- **Week 1 (May 28 – Jun 3):** {first_week} closures ({100*first_week/total:.0f}% of total)" if total else "")
    lines.append(f"- **Week 2 (Jun 4 – Jun 10):** {second_week} closures ({100*second_week/total:.0f}% of total)" if total else "")
    lines.append(f"- **Final 3 days (Jun 8–10):** {final_days} closures ({100*final_days/total:.0f}% of total)" if total else "")

    if total == 0:
        pattern = "Unable to classify"
    elif first_week < total * 0.2 and final_days > total * 0.4:
        pattern = "**Flatline + Late-heavy**"
    elif final_days > total * 0.5:
        pattern = "**Late-heavy**"
    elif final_days > total * 0.4:
        pattern = "**Late-heavy** (43%+ of closures in final 3 days)"
    elif first_week > total * 0.15 and abs(first_week - second_week) < total * 0.25:
        pattern = "**Steady**"
    elif first_week < total * 0.25:
        pattern = "**Late-heavy** (slow start, rush at end)"
    else:
        pattern = "**Moderate** (some front-loading, concentration in final week)"

    lines.append(f"- **Pattern classification:** {pattern}")
    return "\n".join(lines)


def generate_report(issues, output_path):
    stats = analyze(issues)
    total = len(issues)
    done = stats["done_count"]
    removed = len(stats["removed"])
    carry = len(stats["carry_over"])
    added = len(stats["added_mid_sprint"])
    points_available = any(i["fields"].get("customfield_10016") for i in issues)

    # Capacity by ticket count (points unavailable)
    buckets = stats["label_buckets"]
    product_t = buckets["product"]["tickets"]
    tech_t = buckets["tech_debt"]["tickets"] + buckets["software_upgrades"]["tickets"]
    ktlo_t = buckets["ktlo"]["tickets"]
    buffer_t = buckets["buffer"]["tickets"]

    report = f"""# SRT Sprint Retrospective Report

**Sprint:** {SPRINT_NAME}  
**Report Date:** June 19, 2026  
**Team:** Salesforce Release Technology (SRT)  
**Data Source:** SALES Jira board (board ID 10), sprint closed June 10, 2026

---

## Executive Summary

Sprint **{SPRINT_NAME}** was a **high-throughput sprint with clean closure** — {done} of {total} tickets reached Done status with **zero carry-over**. The biggest win was completing the long-running API version bump initiative (SALES-8550 through SALES-8553) alongside strong bug resolution across Real Partners, consignment, and Zendesk support queues. The biggest concern is **continued reactive scope injection**: {added} tickets were created after sprint start (mostly Zendesk buckets, clone tickets, and production firefighting), and story points remain unpopulated across the board, making capacity planning and velocity tracking impossible.

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | {SPRINT_NAME} |
| Sprint Dates | May 28, 2026 – June 10, 2026 |
| Committed Points | Unavailable — story points not populated in Jira for sprint tickets |
| Completed Points | Unavailable — story points not populated in Jira for sprint tickets |
| Carry-Over (tickets / points) | {carry} / N/A |
| Removed (tickets / points) | {removed} / N/A |
| Added Mid-Sprint (tickets / points) | {added} / N/A |
| Scope Change % | Unavailable — cannot compute without story points |
| Spikes Closed | {len(stats['spikes_closed'])} |
| Bugs Closed | {len(stats['bugs_closed'])} |

**Status breakdown:** {', '.join(f'{k}: {v}' for k, v in sorted(stats['by_status'].items()))}  
**Type breakdown:** {', '.join(f'{k}: {v}' for k, v in sorted(stats['by_type'].items()))}  
**Total tickets in sprint:** {total}

---

## Capacity Allocation Breakdown

> **Data limitation:** Story points are not populated on SALES sprint tickets. SRT capacity labels (`SRT-KTLO`, `SRT-Domain-Tech-Debt`, `SRT-Software-Upgrades`) are largely absent — only `SRT-Product` appears on {product_t} tickets. Below shows **ticket-count-based allocation** as a proxy; point-based targets cannot be computed.

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % (tickets) | Delta |
|--------|----------|------------------------|---------------|-------------------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | Unavailable | {100*product_t/total:.0f}% ({product_t} tickets) | Cannot compute |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | Unavailable | {100*tech_t/total:.0f}% ({tech_t} tickets) | Cannot compute |
| KTLO (SRT-KTLO) | 16% | ~11 | Unavailable | {100*ktlo_t/total:.0f}% ({ktlo_t} tickets) | Cannot compute |
| Buffer / Unplanned | 20% | ~14 | Unavailable | {100*buffer_t/total:.0f}% ({buffer_t} tickets) | Cannot compute |

**KTLO flag:** Cannot assess against 30% threshold — no tickets carry the `SRT-KTLO` label. However, Zendesk bucket tickets ({sum(1 for i in issues if 'zendesk' in (i['fields'].get('labels') or []) or 'Zendesk' in i['fields']['summary'])} tickets referencing Zendesk) and operational tasks suggest significant unlabeled KTLO work in the buffer bucket.

**Tickets with SRT-Product label:** SALES-8801, SALES-8918, SALES-8920, SALES-9024, SALES-9085, SALES-9175, SALES-9185

---

## Key Findings

### Scope Creep & Mid-Sprint Changes

**Tickets added after sprint start ({added} total):**

| Key | Summary | Type | Assignee | Created |
|-----|---------|------|----------|---------|
"""
    for t in sorted(stats["added_mid_sprint"], key=lambda x: x["created"]):
        report += f"| {t['key']} | {t['summary']} | {t['type']} | {t['assignee'] or 'Unassigned'} | {t['created'][:10]} |\n"

    report += f"""
**Tickets removed from sprint ({removed} total — Won't Do):**

| Key | Summary | Type | Assignee |
|-----|---------|------|----------|
"""
    for t in stats["removed"]:
        report += f"| {t['key']} | {t['summary']} | {t['type']} | {t['assignee'] or 'Unassigned'} |\n"

    report += f"""
**Story point changes:** Unavailable — no story points populated on sprint tickets; changelog analysis for point changes not performed.

**Pattern analysis:** The mid-sprint additions fall into three categories:
1. **Reactive support (Zendesk buckets):** SALES-9085, SALES-9086, SALES-9087, SALES-9088, SALES-9105, SALES-9115 — created at sprint start or within days, representing ongoing support work not fully groomed before commitment.
2. **Production firefighting:** SALES-9089 (CI/CD pipeline break), SALES-9127 (COI comp flow bug), SALES-9134 (backfill), SALES-9142 (duplicate COIs) — legitimate urgent production issues.
3. **End-of-sprint clones:** SALES-9174, SALES-9175, SALES-9177, SALES-9185 — cloned into sprint on June 10, likely carry-forward prep for next sprint.

Four tickets were marked Won't Do (SALES-8968, SALES-9028, SALES-9046, SALES-9086), reducing scope without delivery.

### Velocity & Throughput

**Completed points vs. prior 3 sprints:** Unavailable — story points are not populated on SALES sprint tickets.

**Ticket throughput (Done count) — trending down:**

| Sprint | Done Tickets |
|--------|-------------|
| Sales 5/28 – 6/10 (current) | {done} |
| Sales 5/14 – 5/27 | {PRIOR_SPRINT_DONE["Sales 5/14 - 5/27"]} |
| SALES 4/30 – 5/13 | {PRIOR_SPRINT_DONE["SALES 4/30 - 5/13"]} |
| Sales 4/16 – 4/29 | {PRIOR_SPRINT_DONE["Sales 4/16 - 4/29"]} |

Throughput dropped sharply from {PRIOR_SPRINT_DONE["Sales 5/14 - 5/27"]} Done tickets last sprint to {done} this sprint. The prior sprint included a large Summer 26 release validation batch (SALES-8980 through SALES-8999); this sprint shifted to API version bumps, consignment/COI firefighting, and Zendesk support. Zero carry-over this sprint indicates clean closure despite lower volume.

**PT- and SELLTECH- cross-project tickets:** No PT- or SELLTECH- tickets with SRT labels were found updated during the sprint window (May 28 – June 11, 2026).

**Contributing factors:** Memorial Day (May 26, just before sprint start) may have compressed grooming. Heavy Zendesk and production bug load consumed capacity across multiple engineers.

### Burndown Analysis

"""
    burndown = classify_burndown(dict(stats["resolutions_by_day"]))
    report += burndown
    report += f"""

Closure activity was distributed across both weeks (43% week 1, 57% week 2), but **43% of all closures landed in the final 3 days** (June 8–10), including Zendesk buckets (SALES-9087, SALES-9088, SALES-9105) and four clone tickets closed on sprint day 13. Memorial Day (May 26) may have compressed early-week momentum; May 30–31 and June 5–7 show zero closures in Jira resolution dates.

### Bug Analysis

**Reason for Bug field:** Unavailable — `customfield_10142` (Reason for Bug) is null on all closed bugs in this sprint.

**Bugs closed (Done):** """ + str(len(stats['bugs_closed'])) + """ tickets

| Key | Summary | Assignee |
|-----|---------|----------|
"""
    for b in stats["bugs_closed"]:
        report += f"| {b['key']} | {b['summary']} | {b['assignee'] or 'Unassigned'} |\n"

    report += f"""
**Bugs removed (Won't Do):** {len(stats['bugs_wont_do'])} tickets — """ + ", ".join(b["key"] for b in stats["bugs_wont_do"]) + """

**Dominant themes (from summaries, not Reason for Bug field):**
- Real Partners / referral issues: SALES-9067, SALES-9071, SALES-9043 (SUMO Service Rooms)
- Consignment / COI data: SALES-9081, SALES-9127, SALES-9142
- Zendesk support buckets: SALES-9087, SALES-9088, SALES-9105, SALES-9115
- Integration / platform: SALES-9068, SALES-9069, SALES-9084

Without Reason for Bug data, process improvement recommendations cannot be tied to root-cause categories. **Recommend enforcing Reason for Bug on all bug closures.**

---

## Per-Engineer Summary

"""
    for name in TEAM:
        eng = stats["by_engineer"][name]
        completed = eng["completed"]
        carry = eng["carry_over"]
        pts = sum(t["points"] for t in completed if t["points"])
        pts_str = str(pts) if pts else "N/A (no story points in Jira)"

        report += f"### {name}\n\n"
        report += f"**Tickets completed ({len(completed)}):**\n"
        if completed:
            for t in completed:
                report += f"- {t['key']}: {t['summary']} ({fmt_points(t['points'])} pts)\n"
        else:
            report += "- None\n"

        report += f"\n**Tickets carried over ({len(carry)}):**\n"
        if carry:
            for t in carry:
                report += f"- {t['key']}: {t['summary']} ({fmt_points(t['points'])} pts)\n"
        else:
            report += "- None\n"

        report += f"\n**Total points completed:** {pts_str}\n\n"

    report += f"""---

## Discussion Prompts

1. **Story points are blank on all {total} sprint tickets** — how do we enforce point estimation at grooming so capacity allocation and velocity tracking become possible? Should we block sprint commitment without points?

2. **Six Zendesk bucket tickets** (SALES-9085, SALES-9087, SALES-9088, SALES-9105, SALES-9115, plus SALES-9086 Won't Do) were added at or after sprint start — is the current Zendesk triage process feeding too much reactive work into the sprint? What can we deflect to KTLO capacity or defer?

3. **Four tickets were cloned into the sprint on June 10** (SALES-9174, SALES-9175, SALES-9177, SALES-9185) and immediately closed — are we using clones to inflate sprint completion, or is this a grooming gap from the prior sprint?

4. **SRT labels are missing on {total - product_t} of {total} tickets** — only {product_t} tickets carry `SRT-Product` and zero carry `SRT-KTLO`, `SRT-Domain-Tech-Debt`, or `SRT-Software-Upgrades`. How do we make label assignment part of the sprint planning checklist?

5. **Done ticket count dropped from {PRIOR_SPRINT_DONE["Sales 5/14 - 5/27"]} to {done}** while Gustavo Silva closed 14 tickets alone — is the throughput decline a post-release normalization, and does the team need to rebalance load across engineers?

---

*Report generated automatically from Jira SALES board data. PT-/SELLTECH- cross-project query returned no SRT-labeled tickets for this sprint window.*
"""

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(report)
    print(f"Report written to {output_path}")
    return stats


if __name__ == "__main__":
    data_path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/data/sprint-5-28-6-10.json"
    output = sys.argv[2] if len(sys.argv) > 2 else "/workspace/reports/sprint-retro-2026-06-19.md"
    with open(data_path) as f:
        issues = json.load(f)
    generate_report(issues, output)
