#!/usr/bin/env python3
"""Generate SRT sprint retrospective report from Jira sprint data JSON.

Usage:
  python3 scripts/generate_sprint_retro.py \\
    --sprint-data /path/to/sprint_issues.json \\
    --changelog /path/to/sprint_changelog_analysis.json \\
    --output reports/sprint-retro-YYYY-MM-DD.md

This script is invoked by the Cursor automation after Jira data is fetched via MCP.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


TARGETS = {"product": 48, "tech_health": 16, "ktlo": 16, "buffer": 20}
TARGET_PTS = {"product": 34, "tech_health": 11, "ktlo": 11, "buffer": 14}


def categorize(labels: list[str], summary: str) -> str:
    labs = [l.lower() for l in (labels or [])]
    s = summary.lower()
    if any(l in labs for l in ["srt-product", "srt-ro"]):
        return "product"
    if "srt-ktlo" in labs:
        return "ktlo"
    if "srt-domain-tech-debt" in labs:
        return "tech_debt"
    if "srt-software-upgrades" in labs:
        return "upgrades"
    if "ktlo" in s:
        return "ktlo"
    if "tech debt" in s or s.startswith("td:"):
        return "tech_debt"
    if "s/w upgrade" in s or "softwareupgrade" in s:
        return "upgrades"
    if "security update" in s or "salesforce-security" in labs:
        return "ktlo"
    if any(
        k in s
        for k in [
            "alra",
            "agentforce",
            "real partner",
            "voice",
            "sumo calendar",
            "bdr list",
            "escalat",
            "routing",
            "lead scoring",
            "weighted",
        ]
    ):
        return "product"
    return "buffer"


def bucket_points(done_issues: list[dict]) -> dict[str, float]:
    buckets = {"product": 0.0, "tech_health": 0.0, "ktlo": 0.0, "buffer": 0.0}
    for issue in done_issues:
        b = issue["bucket"]
        if b in ("tech_debt", "upgrades"):
            buckets["tech_health"] += issue["points"]
        elif b == "ktlo":
            buckets["ktlo"] += issue["points"]
        elif b == "product":
            buckets["product"] += issue["points"]
        else:
            buckets["buffer"] += issue["points"]
    return buckets


def parse_issues(raw: dict, sprint_start: str) -> list[dict]:
    issues = []
    for issue in raw["issues"]:
        f = issue["fields"]
        pts = f.get("customfield_10026")
        points = pts if pts is not None else 0
        issues.append(
            {
                "key": issue["key"],
                "summary": f["summary"],
                "status": f["status"]["name"],
                "points": points,
                "labels": f.get("labels") or [],
                "type": f["issuetype"]["name"],
                "assignee": (f.get("assignee") or {}).get("displayName", "Unassigned"),
                "created": f["created"][:10],
                "reason_for_bug": f.get("customfield_10142"),
                "bucket": categorize(f.get("labels"), f["summary"]),
            }
        )
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate SRT sprint retro report")
    parser.add_argument("--sprint-data", required=True, type=Path)
    parser.add_argument("--changelog", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--report-date", default=datetime.utcnow().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    with args.sprint_data.open() as f:
        sprint_raw = json.load(f)
    with args.changelog.open() as f:
        changelog = json.load(f)

    sprint_name = changelog["sprint_name"]
    sprint_start = changelog["sprint_start"][:10]
    sprint_end = changelog["sprint_end"][:10]

    issues = parse_issues(sprint_raw, sprint_start)
    done = [i for i in issues if i["status"] == "Done"]
    wont_do = [i for i in issues if i["status"] == "Won't Do"]
    done_pts = sum(i["points"] for i in done)
    buckets = bucket_points(done)

    pre_sprint = [i for i in issues if i["created"] < sprint_start]
    created_during = [i for i in issues if i["created"] >= sprint_start]

    added_pts = sum(a["points"] for a in changelog["added_mid_sprint"])
    removed_pts = sum(r["points"] for r in changelog["removed_mid_sprint"])
    committed = changelog["committed_points_at_start"]
    scope_pct = ((added_pts - removed_pts) / committed * 100) if committed else 0

    print(f"Generated metrics for {sprint_name}: {done_pts} pts done, {len(done)} tickets")
    print(f"Output: {args.output}")
    print(f"Scope change: {scope_pct:+.0f}%")


if __name__ == "__main__":
    main()
