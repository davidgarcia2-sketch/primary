#!/usr/bin/env python3
"""Analyze sprint 8591 Jira data and emit metrics JSON + report inputs."""

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

SPRINT_START = datetime.fromisoformat("2026-05-14T16:37:29.332+00:00")
SPRINT_END = datetime.fromisoformat("2026-05-28T06:30:00.000+00:00")

PRODUCT_LABELS = {"SRT-Product", "SRT-product", "SRT-RO"}
KTLO_LABELS = {"SRT-KTLO"}
TECH_LABELS = {"SRT-Domain-Tech-Debt", "SRT-Software-Upgrades"}

TEAM = [
    "Alex Burton",
    "Jummy Sanni",
    "Michael Criswell",
    "Chris Burns",
    "Grace Saint",
    "Navinchandra Gupta",
    "Nag Malluru",
    "Gustavo Silva",
    "Sai Deepika Kanuri",
]


def pts(v):
    return v if v is not None else 0


def bucket(labels):
    s = set(labels or [])
    if s & PRODUCT_LABELS:
        return "product"
    if s & KTLO_LABELS:
        return "ktlo"
    if s & TECH_LABELS:
        return "tech"
    return "buffer"


def parse_dt(s):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main():
    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/workspace/data/sprint-8591-issues.json")
    issues = json.loads(data_path.read_text())["issues"]

    total_pts = sum(pts(i["fields"].get("customfield_10026")) for i in issues)
    done = [i for i in issues if i["fields"]["status"]["name"] == "Done"]
    wont = [i for i in issues if i["fields"]["status"]["name"] == "Won't Do"]
    carry = [i for i in issues if i["fields"]["status"]["name"] not in ("Done", "Won't Do")]

    done_pts = sum(pts(i["fields"].get("customfield_10026")) for i in done)
    wont_pts = sum(pts(i["fields"].get("customfield_10026")) for i in wont)
    carry_pts = sum(pts(i["fields"].get("customfield_10026")) for i in carry)

    spikes = [i for i in done if i["fields"]["issuetype"]["name"] == "Spike"]
    bugs = [i for i in done if i["fields"]["issuetype"]["name"] == "Bug"]

    buckets = defaultdict(int)
    for i in issues:
        buckets[bucket(i["fields"].get("labels"))] += pts(i["fields"].get("customfield_10026"))

    # Burndown by resolution date (Done only)
    daily = defaultdict(int)
    for i in done:
        rd = parse_dt(i["fields"].get("resolutiondate"))
        if rd:
            daily[rd.date().isoformat()] += pts(i["fields"].get("customfield_10026"))

  # Per engineer
    eng = {n: {"done": [], "carry": []} for n in TEAM}
    for i in issues:
        assignee = (i["fields"].get("assignee") or {}).get("displayName")
        if assignee not in eng:
            continue
        entry = (i["key"], i["fields"]["summary"], pts(i["fields"].get("customfield_10026")))
        if i["fields"]["status"]["name"] == "Done":
            eng[assignee]["done"].append(entry)
        elif i["fields"]["status"]["name"] not in ("Won't Do",):
            eng[assignee]["carry"].append(entry)

    # Mid-sprint created (after sprint start)
    mid_created = []
    for i in issues:
        created = parse_dt(i["fields"].get("created"))
        if created and created > SPRINT_START:
            mid_created.append({
                "key": i["key"],
                "summary": i["fields"]["summary"],
                "points": i["fields"].get("customfield_10026"),
                "created": i["fields"].get("created"),
            })

    # Summer '26 release batch created before sprint start (2026-05-12)
    summer_keys = {f"SALES-{n}" for n in range(8980, 9001)}
    summer_may12_created = [
        {
            "key": i["key"],
            "summary": i["fields"]["summary"],
            "points": i["fields"].get("customfield_10026"),
            "created": i["fields"].get("created"),
        }
        for i in issues
        if i["key"] in summer_keys
        and (i["fields"].get("created") or "").startswith("2026-05-12")
    ]

    out = {
        "sprint_name": "Sales 5/14 - 5/27",
        "sprint_id": 8591,
        "sprint_dates": "2026-05-14 16:37 UTC → 2026-05-28 06:30 UTC",
        "total_issues": len(issues),
        "total_points": total_pts,
        "done_issues": len(done),
        "done_points": done_pts,
        "wont_do_issues": len(wont),
        "wont_do_points": wont_pts,
        "carry_issues": len(carry),
        "carry_points": carry_pts,
        "spikes_closed": len(spikes),
        "bugs_closed": len(bugs),
        "buckets": dict(buckets),
        "daily_done_points": dict(sorted(daily.items())),
        "mid_sprint_created": mid_created,
        "summer_may12_created": summer_may12_created,
        "per_engineer": eng,
        "committed_points": None,
        "removed_mid_sprint": None,
        "scope_change_pct": None,
    }

    out_path = Path("/workspace/data/sprint-8591-metrics.json")
    out_path.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
