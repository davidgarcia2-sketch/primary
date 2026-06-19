#!/usr/bin/env python3
"""Analyze SALES sprint data for retrospective report - outputs JSON for report generation."""
import json
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone

CLOUD_ID = "f9205a83-ba29-431b-9196-acc0dbc49e4e"
SPRINT_NAME = "Sales 5/28 - 6/10"
SPRINT_START = datetime(2026, 5, 28, 16, 39, 12, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 6, 10, 7, 0, 0, tzinfo=timezone.utc)

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


if __name__ == "__main__":
    # Read issues from stdin JSON array
    issues = json.load(sys.stdin)
    
    sprint_start_ts = SPRINT_START.timestamp()
    
    stats = {
        "sprint_name": SPRINT_NAME,
        "total_tickets": len(issues),
        "by_status": defaultdict(int),
        "by_type": defaultdict(int),
        "points_total": 0,
        "points_done": 0,
        "carry_over": [],
        "removed": [],
        "added_mid_sprint": [],
        "point_changes": [],
        "bugs_closed": [],
        "spikes_closed": [],
        "by_engineer": {name: {"completed": [], "carry_over": []} for name in TEAM},
        "label_buckets": defaultdict(int),
        "resolutions_by_day": defaultdict(int),
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
        if points:
            stats["label_buckets"][bucket] += points
        else:
            stats["label_buckets"][bucket] += 0  # count tickets without points
        
        # Mid-sprint adds
        if created and created.timestamp() > sprint_start_ts:
            stats["added_mid_sprint"].append({
                "key": key, "summary": summary, "points": points,
                "created": f.get("created"), "assignee": assignee
            })
        
        # Carry-over
        if status not in ("Done", "Won't Do"):
            stats["carry_over"].append({"key": key, "summary": summary, "points": points, "status": status, "assignee": assignee})
        
        # Removed
        if status == "Won't Do":
            stats["removed"].append({"key": key, "summary": summary, "points": points, "assignee": assignee})
        
        # Bugs
        if itype == "Bug" and status == "Done":
            reason = f.get("customfield_10142")
            reason_val = reason.get("value") if isinstance(reason, dict) else reason
            stats["bugs_closed"].append({
                "key": key, "summary": summary, "reason": reason_val, "assignee": assignee
            })
        
        # Spikes
        if itype == "Spike" and status == "Done":
            stats["spikes_closed"].append({"key": key, "summary": summary, "points": points, "assignee": assignee})
        
        # Engineer breakdown
        if assignee in stats["by_engineer"]:
            entry = {"key": key, "summary": summary, "points": points}
            if status == "Done":
                stats["by_engineer"][assignee]["completed"].append(entry)
            elif status not in ("Won't Do",):
                stats["by_engineer"][assignee]["carry_over"].append(entry)
        
        # Burndown by resolution day
        if resolved and status in ("Done", "Won't Do"):
            day = resolved.strftime("%Y-%m-%d")
            stats["resolutions_by_day"][day] += 1
    
    # Convert defaultdicts
    stats["by_status"] = dict(stats["by_status"])
    stats["by_type"] = dict(stats["by_type"])
    stats["label_buckets"] = dict(stats["label_buckets"])
    stats["resolutions_by_day"] = dict(sorted(stats["resolutions_by_day"].items()))
    
    print(json.dumps(stats, indent=2, default=str))
