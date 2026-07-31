#!/usr/bin/env python3
"""Analyze SRT sprint retrospective data from Jira JSON exports."""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone

SPRINT_START = datetime(2026, 7, 9, 17, 19, 20, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 7, 22, 7, 0, 0, tzinfo=timezone.utc)
SPRINT_NAME = "Sales 7/9 - 7/22"

TEAM = [
    "Alex Burton", "Jummy Sanni", "Michael Criswell", "Chris Burns",
    "Grace Saint", "Navinchandra Gupta", "Nag Malluru", "Gustavo Silva",
    "Sai Deepika Kanuri", "Jenn Kleinfeld"
]


def sp(val):
    return val if val is not None else 0


def categorize_bucket(labels, summary):
    labels_lower = [l.lower() for l in (labels or [])]
    summary_lower = (summary or "").lower()

    if any(l in labels_lower for l in ["srt-product", "srt-ro"]):
        return "product"
    if any(l in labels_lower for l in ["srt-ktlo"]):
        return "ktlo"
    if any(l in labels_lower for l in ["srt-domain-tech-debt", "srt-software-upgrades"]):
        return "tech_health"
    if "ktlo" in summary_lower or "zendesk bucket - ktlo" in summary_lower:
        return "ktlo"
    if "tech debt" in summary_lower or "zendesk bucket - tech debt" in summary_lower or "td:" in summary_lower:
        return "tech_health"
    if "s/w upgrade" in summary_lower or "sftw upgrade" in summary_lower or "software upgrade" in summary_lower:
        return "tech_health"
    if "zendesk" in summary_lower or "zd ticket" in summary_lower or "zen desk" in summary_lower:
        return "ktlo"
    if "package_upgrade" in labels_lower or "zoom" in labels_lower:
        return "tech_health"
    if any(k in summary_lower for k in ["alra", "high value", "hv designer", "routing", "retail dashboard", "voice recognition"]):
        return "product"
    if any(k in summary_lower for k in ["security", "sox", "sailpoint", "compliance"]):
        return "tech_health"
    return "buffer"


def parse_date(s):
    if not s:
        return None
    try:
        from dateutil import parser
        return parser.parse(s)
    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_sprint.py <sprint_issues.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = json.load(f)

    issues = data.get("issues", data) if isinstance(data, dict) else data

    done_statuses = {"Done", "Won't Do", "Closed", "Released", "Deployed"}

    total_points = 0
    done_points = 0
    wont_do_points = 0
    carry_over = []
    added_mid = []
    by_engineer = defaultdict(lambda: {"done": [], "carry": []})
    by_day = defaultdict(int)
    buckets = defaultdict(float)
    spikes = 0
    bugs = 0
    bugs_by_reason = defaultdict(int)
    status_counts = defaultdict(int)
    type_counts = defaultdict(int)
    removed = []

    for issue in issues:
        key = issue["key"]
        fields = issue["fields"]
        summary = fields.get("summary", "")
        status = fields.get("status", {}).get("name", "")
        sp_val = sp(fields.get("customfield_10026"))
        assignee = (fields.get("assignee") or {}).get("displayName", "Unassigned")
        labels = fields.get("labels", [])
        itype = fields.get("issuetype", {}).get("name", "")
        created = parse_date(fields.get("created"))
        resolved = parse_date(fields.get("resolutiondate"))
        parent = fields.get("parent")
        reason = fields.get("customfield_10142")

        if parent and itype == "Sub-task":
            continue

        status_counts[status] += 1
        type_counts[itype] += 1
        total_points += sp_val

        if created and created > SPRINT_START:
            added_mid.append({
                "key": key, "summary": summary, "points": sp_val,
                "assignee": assignee, "created": str(created)[:10]
            })

        if status == "Won't Do":
            wont_do_points += sp_val
            removed.append({"key": key, "summary": summary, "points": sp_val})

        if status in done_statuses:
            if status == "Done":
                done_points += sp_val
                bucket = categorize_bucket(labels, summary)
                buckets[bucket] += sp_val
                by_engineer[assignee]["done"].append({"key": key, "summary": summary, "points": sp_val})
                if itype == "Spike":
                    spikes += 1
                if itype == "Bug":
                    bugs += 1
                    reason_val = reason.get("value") if isinstance(reason, dict) else (reason or "(unpopulated)")
                    bugs_by_reason[reason_val or "(unpopulated)"] += 1
                if resolved:
                    day = resolved.strftime("%Y-%m-%d")
                    by_day[day] += 1
            elif status == "Won't Do":
                pass
        else:
            carry_over.append({"key": key, "summary": summary, "points": sp_val, "assignee": assignee, "status": status})
            by_engineer[assignee]["carry"].append({"key": key, "summary": summary, "points": sp_val})

    added_pts = sum(x["points"] for x in added_mid)
    carry_pts = sum(x["points"] for x in carry_over)
    removed_pts = sum(x["points"] for x in removed)

    print(f"SPRINT: {SPRINT_NAME}")
    print(f"TOTAL_TICKETS: {len(issues)}")
    print(f"TOTAL_POINTS: {total_points}")
    print(f"DONE_POINTS: {done_points}")
    print(f"WONT_DO_POINTS: {wont_do_points}")
    print(f"CARRY_OVER: {len(carry_over)} tickets / {carry_pts} pts")
    print(f"REMOVED: {len(removed)} tickets / {removed_pts} pts")
    print(f"ADDED_MID: {len(added_mid)} tickets / {added_pts} pts")
    print(f"SPIKES: {spikes}")
    print(f"BUGS: {bugs}")
    print()
    print("STATUS:", dict(status_counts))
    print("TYPES:", dict(type_counts))
    print()
    print("BUCKETS:")
    for b, v in sorted(buckets.items(), key=lambda x: -x[1]):
        pct = (v / done_points * 100) if done_points else 0
        print(f"  {b}: {v} ({pct:.1f}%)")
    print()
    print("BUGS_BY_REASON:", dict(bugs_by_reason))
    print()
    print("BURNDOWN_BY_DAY:")
    for day in sorted(by_day.keys()):
        print(f"  {day}: {by_day[day]}")
    print()
    print("PER_ENGINEER:")
    for eng in TEAM:
        done = by_engineer.get(eng, {}).get("done", [])
        carry = by_engineer.get(eng, {}).get("carry", [])
        done_pts = sum(t["points"] for t in done)
        carry_pts_e = sum(t["points"] for t in carry)
        print(f"\n{eng}: {done_pts} pts done, {carry_pts_e} pts carry ({len(done)} done, {len(carry)} carry)")
        for t in done:
            print(f"  DONE {t['key']} ({t['points']}pt) {t['summary'][:60]}")
        for t in carry:
            print(f"  CARRY {t['key']} ({t['points']}pt) {t['summary'][:60]}")


if __name__ == "__main__":
    main()
