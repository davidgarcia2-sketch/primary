#!/usr/bin/env python3
"""Analyze SRT sprint retrospective data from Jira JSON exports."""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone

SPRINT_START = datetime(2026, 6, 11, 17, 20, 59, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 6, 24, 7, 0, 0, tzinfo=timezone.utc)
SPRINT_NAME = "Sales 6/11 - 6/24"

TEAM = [
    "Alex Burton", "Jummy Sanni", "Michael Criswell", "Chris Burns",
    "Grace Saint", "Navinchandra Gupta", "Nag Malluru", "Gustavo Silva",
    "Sai Deepika Kanuri"
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
    # Infer from summary patterns used by team
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
    return "buffer"

def parse_date(s):
    if not s:
        return None
    # Handle Jira date formats
    for fmt in ["%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"]:
        try:
            return datetime.strptime(s.replace("+0000", "+00:00").replace("-0700", "-0700"), fmt)
        except ValueError:
            continue
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
    
    done_statuses = {"Done", "Won't Do"}
    
    total_points = 0
    done_points = 0
    carry_over = []
    removed = []
    added_mid = []
    point_changes = []
    by_engineer = defaultdict(lambda: {"done": [], "carry": []})
    by_day = defaultdict(float)
    buckets = defaultdict(float)
    spikes = 0
    bugs = 0
    
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
        
        total_points += sp_val
        
        bucket = categorize_bucket(labels, summary)
        if status in done_statuses:
            done_points += sp_val
            buckets[bucket] += sp_val
            if assignee in TEAM or assignee != "Unassigned":
                by_engineer[assignee]["done"].append((key, summary, sp_val))
            if resolved:
                day = resolved.strftime("%Y-%m-%d")
                by_day[day] += sp_val
        else:
            carry_over.append((key, summary, sp_val, assignee))
            by_engineer[assignee]["carry"].append((key, summary, sp_val))
        
        if itype == "Spike" and status in done_statuses:
            spikes += 1
        if itype == "Bug" and status in done_statuses:
            bugs += 1
        
        if created and created > SPRINT_START:
            added_mid.append((key, summary, sp_val, assignee, created.strftime("%Y-%m-%d")))
    
    print(json.dumps({
        "total_tickets": len(issues),
        "total_points": total_points,
        "done_points": done_points,
        "carry_over_count": len(carry_over),
        "carry_over_points": sum(x[2] for x in carry_over),
        "added_mid_count": len(added_mid),
        "added_mid_points": sum(x[2] for x in added_mid),
        "spikes": spikes,
        "bugs": bugs,
        "buckets": dict(buckets),
        "by_day": dict(sorted(by_day.items())),
        "by_engineer": {k: {"done_pts": sum(x[2] for x in v["done"]), "done_count": len(v["done"])} for k, v in by_engineer.items()},
    }, indent=2))

if __name__ == "__main__":
    main()
