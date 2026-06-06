#!/usr/bin/env python3
"""Persist MCP Jira JSON from a file path to sprint-8591-issues.json and optional chunks."""

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/data/chunks")
OUT = Path("/workspace/data/sprint-8591-issues.json")
RAW = Path("/workspace/data/mcp-raw-8591.json")


def chunk_num(key: str) -> int:
    if key.startswith("SELLTECH-"):
        return 5
    num = int(key.split("-", 1)[1])
    if num < 8900:
        return 1
    if num < 9000:
        return 2
    if num < 9060:
        return 3
    return 4


def normalize_issue(raw):
    f = raw.get("fields", {})
    assignee = f.get("assignee")
    return {
        "key": raw["key"],
        "fields": {
            "summary": f.get("summary"),
            "status": {"name": f.get("status", {}).get("name")},
            "issuetype": {"name": f.get("issuetype", {}).get("name")},
            "assignee": {"displayName": assignee["displayName"]} if assignee else None,
            "customfield_10026": f.get("customfield_10026"),
            "customfield_10142": f.get("customfield_10142"),
            "labels": f.get("labels") or [],
            "created": f.get("created"),
            "resolutiondate": f.get("resolutiondate"),
        },
    }


def write_chunks(data: dict) -> None:
    buckets = {i: [] for i in range(1, 6)}
    for issue in data.get("issues", []):
        buckets[chunk_num(issue["key"])].append(issue)
    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    for i in range(1, 6):
        path = CHUNK_DIR / f"chunk-{i}.json"
        chunk = {"issues": buckets[i], "isLast": True}
        path.write_text(json.dumps(chunk, indent=2))
        keys = [x["key"] for x in buckets[i]]
        print(
            f"chunk-{i}: {len(keys)} issues | "
            f"first={keys[0] if keys else None} last={keys[-1] if keys else None}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: persist_mcp_json_path.py <mcp_json_file>", file=sys.stderr)
        sys.exit(1)
    src = Path(sys.argv[1])
    data = json.loads(src.read_text())
    RAW.parent.mkdir(parents=True, exist_ok=True)
    RAW.write_text(json.dumps(data, indent=2))
    issues = [normalize_issue(i) for i in data.get("issues", [])]
    OUT.write_text(json.dumps({"issues": issues, "total": len(issues)}, indent=2))
    write_chunks(data)
    print(f"Wrote {len(issues)} issues to {OUT}")


if __name__ == "__main__":
    main()
