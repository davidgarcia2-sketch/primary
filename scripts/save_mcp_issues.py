#!/usr/bin/env python3
"""Save issues JSON from stdin (MCP tool output) to sprint data file."""
import json
import sys

data = json.load(sys.stdin)
issues = data.get("issues", data if isinstance(data, list) else [])
out = sys.argv[1] if len(sys.argv) > 1 else "/workspace/data/sprint-5-28-6-10.json"
with open(out, "w") as f:
    json.dump(issues, f, indent=2)
print(f"Saved {len(issues)} issues to {out}")
