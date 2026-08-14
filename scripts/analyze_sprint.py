#!/usr/bin/env python3
"""Analyze Jira sprint JSON export for SRT sprint retrospectives."""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta

SPRINT_ID = 9366
SPRINT_NAME = "Sales 7/23 - 8/5"
SPRINT_START = datetime(2026, 7, 23, 19, 17, 46, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 8, 5, 7, 0, 0, tzinfo=timezone.utc)

TEAM = {
    "Alex Burton", "Jummy Sanni", "Michael Criswell", "Chris Burns", "Grace Saint",
    "Navinchandra Gupta", "Nag Malluru", "Gustavo Silva", "Sai Deepika Kanuri", "Jenn Kleinfeld",
}


def parse_dt(s):
    if not s:
        return None
    if s.endswith("Z"):
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    if len(s) >= 5 and s[-5] in "+-" and s[-4:].isdigit():
        base = s[:-5]
        offset_h = int(s[-5:-2])
        offset_m = int(s[-2:])
        sign = 1 if s[-5] == "+" else -1
        tz = timezone(timedelta(hours=sign * offset_h, minutes=sign * offset_m))
        return datetime.fromisoformat(base).replace(tzinfo=tz).astimezone(timezone.utc)
    return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)


def bucket(labels, summary):
    labels = labels or []
    s = (summary or "").lower()
    if any(l in labels for l in ["SRT-product", "SRT-RO"]):
        return "product"
    if any(l in labels for l in ["SRT-KTLO"]):
        return "ktlo"
    if any(l in labels for l in ["SRT-Domain-Tech-Debt", "SRT-Software-Upgrades"]):
        return "tech_health"
    if "ktlo:" in s or "zd - ktlo" in s:
        return "ktlo"
    if "td:" in s or "domain tech debt" in s:
        return "tech_health"
    if "su&tc:" in s or "s/w upgrades" in s or "bump classes" in s or "sf ru" in s:
        return "tech_health"
    if "devqa:" in s:
        return "buffer"
    product_kw = ["alra", "sumo", "lean data", "routing", "retail", "high value", "campaign", "sailpoint", "zoom"]
    if any(k in s for k in product_kw):
        return "product"
    return "buffer"


def main(path):
    with open(path) as f:
        data = json.load(f)
    issues = data["issues"]
    tickets = []
    for iss in issues:
        f = iss["fields"]
        if f.get("issuetype", {}).get("subtask"):
            continue
        created = parse_dt(f.get("created"))
        resolved = parse_dt(f.get("resolutiondate"))
        done = f.get("status", {}).get("statusCategory", {}).get("key") == "done"
        pts = float(f.get("customfield_10026") or 0)
        mid_add = bool(created and created > SPRINT_START)
        completed = done and resolved and SPRINT_START <= resolved <= datetime(2026, 8, 6, tzinfo=timezone.utc)
        tickets.append({
            "key": iss["key"],
            "summary": f.get("summary", ""),
            "assignee": (f.get("assignee") or {}).get("displayName", "Unassigned"),
            "points": pts,
            "done": done,
            "mid_add": mid_add,
            "completed": completed,
            "labels": f.get("labels") or [],
            "type": f.get("issuetype", {}).get("name", ""),
        })

    committed = [t for t in tickets if not t["mid_add"]]
    added = [t for t in tickets if t["mid_add"]]
    completed = [t for t in tickets if t["completed"]]
    carry = [t for t in tickets if not t["completed"] and not t["done"]]

    print(f"Sprint: {SPRINT_NAME}")
    print(f"Committed: {sum(t['points'] for t in committed):.0f} pts / {len(committed)} tickets")
    print(f"Completed: {sum(t['points'] for t in completed):.0f} pts / {len(completed)} tickets")
    print(f"Added mid-sprint: {sum(t['points'] for t in added):.0f} pts / {len(added)} tickets")
    print(f"Carry-over (not done): {sum(t['points'] for t in carry):.0f} pts / {len(carry)} tickets")
    cap = defaultdict(float)
    for t in completed:
        cap[bucket(t["labels"], t["summary"])] += t["points"]
    total = sum(cap.values()) or 1
    print("Capacity (completed):")
    for b in ["product", "tech_health", "ktlo", "buffer"]:
        print(f"  {b}: {cap[b]:.0f} ({cap[b]/total*100:.1f}%)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "/workspace/reports/sprint-data-9366.json")
