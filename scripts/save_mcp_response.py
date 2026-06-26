#!/usr/bin/env python3
"""Save Jira MCP search response JSON from stdin to data files."""
import json
import sys
from pathlib import Path

DATA = Path("/workspace/data")


def sp(val):
    return val if val is not None else 0


def main():
    if len(sys.argv) < 2:
        print("Usage: save_mcp_response.py <sprint|historical> [json_file]", file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1]
    if len(sys.argv) > 2:
        raw = Path(sys.argv[2]).read_text()
    else:
        raw = sys.stdin.read()

    data = json.loads(raw)
    DATA.mkdir(parents=True, exist_ok=True)

    if mode == "sprint":
        issues = data.get("issues", data)
        out = DATA / "sprint_issues.json"
        with open(out, "w") as f:
            json.dump({"issues": issues}, f)
        print(f"Saved {len(issues)} issues to {out}")
    elif mode == "historical":
        # data: dict sprint_name -> issues list OR dict sprint_name -> points
        hist = {}
        for name, val in data.items():
            if isinstance(val, list):
                hist[name] = sum(sp(i.get("fields", {}).get("customfield_10026")) for i in val)
            else:
                hist[name] = val
        out = DATA / "historical_sprints.json"
        with open(out, "w") as f:
            json.dump(hist, f, indent=2)
        print(f"Saved historical: {hist}")
    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
