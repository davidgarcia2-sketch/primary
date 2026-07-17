#!/usr/bin/env python3
"""Fetch SALES sprint data from Jira REST API and save JSON for report generation."""
import json
import os
import sys
import urllib.request
import urllib.parse

CLOUD_ID = "f9205a83-ba29-431b-9196-acc0dbc49e4e"
BASE = f"https://api.atlassian.com/ex/jira/{CLOUD_ID}/rest/api/3"
FIELDS = "summary,status,issuetype,labels,assignee,created,resolutiondate,customfield_10026,customfield_10142"

SPRINTS = {
    "Sales 6/11 - 6/24": "project = SALES AND sprint = \"Sales 6/11 - 6/24\" ORDER BY key ASC",
    "Sales 5/28 - 6/10": "project = SALES AND sprint = \"Sales 5/28 - 6/10\" AND status = Done",
    "Sales 5/14 - 5/27": "project = SALES AND sprint = \"Sales 5/14 - 5/27\" AND status = Done",
    "SALES 4/30 - 5/13": "project = SALES AND sprint = \"SALES 4/30 - 5/13\" AND status = Done",
}


def get_auth():
    email = os.environ.get("ATLASSIAN_EMAIL") or os.environ.get("JIRA_EMAIL")
    token = os.environ.get("ATLASSIAN_API_TOKEN") or os.environ.get("JIRA_API_TOKEN")
    if email and token:
        import base64
        cred = base64.b64encode(f"{email}:{token}".encode()).decode()
        return {"Authorization": f"Basic {cred}", "Accept": "application/json"}
    return None


def jql_search(jql, fields=FIELDS, max_results=100):
    headers = get_auth()
    if not headers:
        return None
    issues = []
    start_at = 0
    while True:
        params = urllib.parse.urlencode({
            "jql": jql,
            "fields": fields,
            "maxResults": max_results,
            "startAt": start_at,
        })
        req = urllib.request.Request(f"{BASE}/search/jql?{params}", headers=headers)
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        batch = data.get("issues", [])
        issues.extend(batch)
        if data.get("isLast", True) or len(batch) < max_results:
            break
        start_at += len(batch)
    return issues


def sp(val):
    return val if val is not None else 0


def main():
    out_dir = "/workspace/data"
    os.makedirs(out_dir, exist_ok=True)

    headers = get_auth()
    if not headers:
        print("No Jira credentials; expecting pre-saved data files.", file=sys.stderr)
        sys.exit(1)

    current = jql_search(SPRINTS["Sales 6/11 - 6/24"])
    if not current:
        print("Failed to fetch current sprint", file=sys.stderr)
        sys.exit(1)

    with open(f"{out_dir}/sprint_issues.json", "w") as f:
        json.dump({"issues": current}, f, indent=2)
    print(f"Saved {len(current)} sprint issues")

    hist = {}
    for name, jql in SPRINTS.items():
        if name == "Sales 6/11 - 6/24":
            continue
        issues = jql_search(jql, fields="customfield_10026")
        pts = sum(sp(i["fields"].get("customfield_10026")) for i in (issues or []))
        hist[name] = pts
        print(f"  {name}: {pts} pts ({len(issues or [])} tickets)")

    with open(f"{out_dir}/historical_sprints.json", "w") as f:
        json.dump(hist, f, indent=2)


if __name__ == "__main__":
    main()
