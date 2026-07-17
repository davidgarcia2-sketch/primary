#!/usr/bin/env python3
"""Save sprint + historical data using Jira REST (requires MCP agent to populate token)."""
import json
import os
import sys
import urllib.request
import urllib.parse
import base64

CLOUD_ID = "f9205a83-ba29-431b-9196-acc0dbc49e4e"
BASE = f"https://api.atlassian.com/ex/jira/{CLOUD_ID}/rest/api/3/search"
DATA_DIR = "/workspace/data"


def search(jql, fields, auth_header):
    issues = []
    start_at = 0
    while True:
        body = json.dumps({
            "jql": jql,
            "fields": fields.split(","),
            "maxResults": 100,
            "startAt": start_at,
        }).encode()
        req = urllib.request.Request(
            BASE,
            data=body,
            headers={
                "Authorization": auth_header,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.load(resp)
        batch = data.get("issues", [])
        issues.extend(batch)
        total = data.get("total", len(issues))
        start_at += len(batch)
        if start_at >= total or not batch:
            break
    return issues


def sp(v):
    return v if v is not None else 0


def main():
    token = os.environ.get("JIRA_AUTH_BEARER") or os.environ.get("ATLASSIAN_BEARER")
    if not token:
        print("Set JIRA_AUTH_BEARER", file=sys.stderr)
        sys.exit(1)
    auth = f"Bearer {token}"

    os.makedirs(DATA_DIR, exist_ok=True)
    fields = "summary,status,issuetype,labels,assignee,created,resolutiondate,customfield_10026,customfield_10142"

    current = search('project = SALES AND sprint = "Sales 6/11 - 6/24" ORDER BY key ASC', fields, auth)
    with open(f"{DATA_DIR}/sprint_issues.json", "w") as f:
        json.dump({"issues": current}, f)
    print(f"Saved {len(current)} issues")

    hist = {}
    for name, jql in [
        ("Sales 5/28 - 6/10", 'project = SALES AND sprint = "Sales 5/28 - 6/10" AND status = Done'),
        ("Sales 5/14 - 5/27", 'project = SALES AND sprint = "Sales 5/14 - 5/27" AND status = Done'),
        ("SALES 4/30 - 5/13", 'project = SALES AND sprint = "SALES 4/30 - 5/13" AND status = Done'),
    ]:
        issues = search(jql, "customfield_10026", auth)
        pts = sum(sp(i["fields"].get("customfield_10026")) for i in issues)
        hist[name] = pts
        print(f"{name}: {pts}")

    with open(f"{DATA_DIR}/historical_sprints.json", "w") as f:
        json.dump(hist, f, indent=2)


if __name__ == "__main__":
    main()
