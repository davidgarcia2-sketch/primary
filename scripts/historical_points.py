#!/usr/bin/env python3
"""Compute historical sprint point totals from Jira issue point values."""
import json

# Done-ticket story points per sprint (from Jira JQL queries 2026-06-26)
HISTORICAL = {
    "SALES 4/30 - 5/13": [
        1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 2, 5, 1, 1, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2
    ],
    "Sales 5/14 - 5/27": [
        1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 3, 2, 1, 1, 3, 2, 2, 2, 3, 2, 2, 1, 3, 2, 2
    ],
    "Sales 5/28 - 6/10": [
        1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 2, 3, 3, 3, 3, 3, 1, 2, 2, 2, 2, 2, 2, 2, 1
    ],
}

if __name__ == "__main__":
    out = {k: sum(v) for k, v in HISTORICAL.items()}
    print(json.dumps(out, indent=2))
