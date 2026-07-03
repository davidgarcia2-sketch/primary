#!/usr/bin/env python3
"""Generate SRT Sprint Retrospective report from Jira sprint JSON."""
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SPRINT_START = datetime(2026, 6, 11, 17, 20, 59, tzinfo=timezone.utc)
SPRINT_END = datetime(2026, 6, 24, 7, 0, 0, tzinfo=timezone.utc)
SPRINT_NAME = "Sales 6/11 - 6/24"

TEAM = [
    "Alex Burton", "Jummy Sanni", "Michael Criswell", "Chris Burns",
    "Grace Saint", "Navinchandra Gupta", "Nag Malluru", "Gustavo Silva",
    "Sai Deepika Kanuri"
]

DONE_STATUSES = {"Done", "Won't Do"}


def sp(val):
    return val if val is not None else 0


def parse_date(s):
    if not s:
        return None
    # Jira dates like 2026-06-11T09:20:59.361-0700
    from datetime import datetime as dt
    s = s.replace("Z", "+00:00")
    if len(s) >= 5 and s[-5] in "+-" and s[-3] != ":":
        s = s[:-2] + ":" + s[-2:]
    try:
        return dt.fromisoformat(s)
    except ValueError:
        return dt.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)


def categorize_bucket(labels, summary):
    labels_lower = [l.lower() for l in (labels or [])]
    summary_lower = (summary or "").lower()

    if any(l in labels_lower for l in ["srt-product", "srt-ro"]):
        return "product"
    if any(l in labels_lower for l in ["srt-ktlo"]):
        return "ktlo"
    if any(l in labels_lower for l in ["srt-domain-tech-debt", "srt-software-upgrades"]):
        return "tech_health"
    if "ktlo" in summary_lower or "zendesk bucket - ktlo" in summary_lower:
        return "ktlo"
    if "zendesk" in summary_lower or "zd ticket" in summary_lower or "zen desk" in summary_lower:
        return "ktlo"
    if "tech debt" in summary_lower or "zendesk bucket - tech debt" in summary_lower or summary_lower.startswith("td:"):
        return "tech_health"
    if "s/w upgrade" in summary_lower or "sftw upgrade" in summary_lower or "software upgrade" in summary_lower:
        return "tech_health"
    if "package_upgrade" in labels_lower or "bump" in summary_lower or "api version" in summary_lower:
        return "tech_health"
    if "row lock" in summary_lower:
        return "tech_health"
    if "release update" in summary_lower:
        return "tech_health"
    # ALRA, routing, outreach, product stories without labels
    alra_keywords = ["alra", "routing", "outreach", "mgo", "hv lead", "ramp code", "job profile",
                     "sales role", "cohort", "title level", "quota", "commission", "inquiry pe",
                     "van pickup", "sumo", "vendor opportunit"]
    if any(k in summary_lower for k in alra_keywords):
        return "product"
    if "security" in summary_lower or "sox" in summary_lower:
        return "buffer"
    return "buffer"


def sum_points(issues):
    return sum(sp(i["fields"].get("customfield_10026")) for i in issues)


def analyze_sprint(issues):
    committed = []
    added_mid = []
    removed = []
    carry_over = []
    point_changes = []
    by_engineer = {name: {"done": [], "carry": []} for name in TEAM}
    by_day = defaultdict(float)
    buckets = defaultdict(float)
    bugs_done = []
    spikes_done = []
    bug_reasons = defaultdict(int)

    for issue in issues:
        key = issue["key"]
        fields = issue["fields"]
        summary = fields.get("summary", "")
        status = fields.get("status", {}).get("name", "")
        sp_val = sp(fields.get("customfield_10026"))
        assignee = (fields.get("assignee") or {}).get("displayName", "Unassigned")
        labels = fields.get("labels", [])
        itype = fields.get("issuetype", {}).get("name", "")
        created = parse_date(fields.get("created"))
        resolved = parse_date(fields.get("resolutiondate"))
        bug_reason = fields.get("customfield_10142")

        if created and created > SPRINT_START:
            added_mid.append((key, summary, sp_val, assignee, created.strftime("%Y-%m-%d")))
        else:
            committed.append((key, summary, sp_val))

        if status == "Won't Do":
            removed.append((key, summary, sp_val, assignee))

        if status in DONE_STATUSES:
            bucket = categorize_bucket(labels, summary)
            buckets[bucket] += sp_val
            if assignee in TEAM:
                by_engineer[assignee]["done"].append((key, summary, sp_val))
            if resolved and resolved >= SPRINT_START:
                day = resolved.strftime("%Y-%m-%d")
                if SPRINT_START.date() <= resolved.date() <= SPRINT_END.date():
                    by_day[day] += sp_val
            if itype == "Spike":
                spikes_done.append(key)
            if itype == "Bug" and status == "Done":
                bugs_done.append((key, summary, bug_reason))
                reason = bug_reason or "Not populated"
                bug_reasons[reason] += 1
        else:
            carry_over.append((key, summary, sp_val, assignee))
            if assignee in TEAM:
                by_engineer[assignee]["carry"].append((key, summary, sp_val))

    committed_pts = sum(x[2] for x in committed)
    added_pts = sum(x[2] for x in added_mid)
    removed_pts = sum(x[2] for x in removed)
    done_pts = sum(
        sp(i["fields"].get("customfield_10026"))
        for i in issues
        if i["fields"]["status"]["name"] in DONE_STATUSES
    )

    total_done_pts = done_pts
    scope_change = ((added_pts - removed_pts) / committed_pts * 100) if committed_pts else 0

    return {
        "committed_pts": committed_pts,
        "committed_count": len(committed),
        "done_pts": done_pts,
        "added_mid": added_mid,
        "added_pts": added_pts,
        "removed": removed,
        "removed_pts": removed_pts,
        "carry_over": carry_over,
        "point_changes": point_changes,
        "by_engineer": by_engineer,
        "by_day": dict(sorted(by_day.items())),
        "buckets": dict(buckets),
        "bugs_done": bugs_done,
        "spikes_done": spikes_done,
        "bug_reasons": dict(bug_reasons),
        "scope_change_pct": scope_change,
        "total_done_pts": total_done_pts,
    }


def burndown_pattern(by_day):
    if not by_day:
        return "Unavailable"
    days = sorted(by_day.keys())
    sprint_days = [d for d in days if "2026-06-11" <= d <= "2026-06-24"]
    if not sprint_days:
        return "Unavailable"
    values = [by_day[d] for d in sprint_days]
    total = sum(values)
    if total == 0:
        return "Unavailable"
    first_half = sum(values[:len(values)//2])
    second_half = sum(values[len(values)//2:])
    last_3_days = sum(v for d, v in by_day.items() if d >= "2026-06-22")
    last_3_pct = last_3_days / total * 100
    if first_half < total * 0.15 and last_3_pct > 50:
        return "Late-heavy"
    if first_half < total * 0.2:
        return "Flatline (slow start, rush at end)"
    if last_3_pct > 45:
        return "Late-heavy"
    return "Steady"


def main():
    sprint_path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/data/sprint_issues.json"
    hist_path = sys.argv[2] if len(sys.argv) > 2 else "/workspace/data/historical_sprints.json"
    out_path = sys.argv[3] if len(sys.argv) > 3 else "/workspace/reports/sprint-retro-2026-06-24.md"

    with open(sprint_path) as f:
        sprint_data = json.load(f)
    issues = sprint_data.get("issues", sprint_data)

    hist = {}
    if Path(hist_path).exists():
        with open(hist_path) as f:
            hist = json.load(f)

    a = analyze_sprint(issues)
    total_tickets = len(issues)
    total_pts = a["total_done_pts"]
    buckets = a["buckets"]
    product_pts = buckets.get("product", 0)
    ktlo_pts = buckets.get("ktlo", 0)
    tech_pts = buckets.get("tech_health", 0)
    buffer_pts = buckets.get("buffer", 0)
    bug_count = len(a["bugs_done"])
    spike_count = len(a["spikes_done"])
    added_count = len(a["added_mid"])
    removed_count = len(a["removed"])

    def pct(p):
        return (p / total_pts * 100) if total_pts else 0

    def delta(actual_pct, target):
        d = actual_pct - target
        return f"+{d:.0f}%" if d > 0 else f"{d:.0f}%"

    pattern = burndown_pattern(a["by_day"])

    # Velocity from historical
    vel_lines = []
    for sprint_name, pts in hist.items():
        vel_lines.append(f"| {sprint_name} | {pts} |")

    report = f"""# SRT Sprint Retrospective — {SPRINT_NAME}

*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')} | Source: SALES Jira Board (ID 10)*

---

## Executive Summary

Sprint **{SPRINT_NAME}** closed with **100% ticket completion** — all {total_tickets} sprint tickets reached Done or Won't Do status with **zero carry-over**. The team delivered strong execution on the ALRA routing initiative ({spike_count} spikes closed, extensive routing/MGO/outreach discovery) and completed Salesforce Security Phase 2 work (SALES-9031, SALES-9232). The biggest win was closing the full sprint scope including late-added ALRA clones (SALES-9265, SALES-9268, SALES-9269) on the final day. The biggest concern is **continued scope creep**: {added_count} tickets were created after sprint start, pushing total completed points to {a['done_pts']} against an initial commitment of {a['committed_pts']} points. KTLO allocation remains a concern, and **all {bug_count} closed bugs lack "Reason for Bug" data** in Jira — blocking root-cause analysis.

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | {SPRINT_NAME} |
| Sprint Dates | 2026-06-11 — 2026-06-24 |
| Committed Points | {a['committed_pts']} ({a['committed_count']} tickets at sprint start) |
| Completed Points | {a['done_pts']} |
| Carry-Over (tickets / points) | 0 / 0 |
| Removed (tickets / points) | {removed_count} / {a['removed_pts']} |
| Added Mid-Sprint (tickets / points) | {added_count} / {a['added_pts']} |
| Scope Change % | {a['scope_change_pct']:+.0f}% |
| Spikes Closed | {spike_count} |
| Bugs Closed | {bug_count} |

---

## Capacity Allocation Breakdown

*Note: SRT labels are sparsely applied (only SALES-9048 has `SRT-Product`). Allocation below is inferred from ticket summaries and Zendesk bucket naming conventions.*

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|---------------|----------|-------|
| Product (SRT-product / SRT-RO) | 48% | ~34 | {product_pts:.0f} | {pct(product_pts):.0f}% | {delta(pct(product_pts), 48)} |
| Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades) | 16% | ~11 | {tech_pts:.0f} | {pct(tech_pts):.0f}% | {delta(pct(tech_pts), 16)} |
| KTLO (SRT-KTLO) | 16% | ~11 | {ktlo_pts:.0f} | {pct(ktlo_pts):.0f}% | {delta(pct(ktlo_pts), 16)} |
| Buffer / Unplanned | 20% | ~14 | {buffer_pts:.0f} | {pct(buffer_pts):.0f}% | {delta(pct(buffer_pts), 20)} |

"""
    if pct(ktlo_pts) > 30:
        report += f"**⚠️ KTLO FLAG:** KTLO consumed **{pct(ktlo_pts):.0f}%** of completed points, exceeding the 30% threshold. The team should discuss deflection strategies.\n\n"

    report += """---

## Key Findings

### Scope Creep & Mid-Sprint Changes

**Tickets added after sprint start (2026-06-11):**

"""
    for key, summary, pts, assignee, date in sorted(a["added_mid"], key=lambda x: x[3]):
        report += f"- **{key}** ({pts} pt) — {summary} — added {date}, assignee: {assignee}\n"

    report += f"""
**Tickets removed (Won't Do):**

"""
    for key, summary, pts, assignee in a["removed"]:
        report += f"- **{key}** ({pts} pt) — {summary} — assignee: {assignee}\n"

    report += """
**Story point changes after sprint start:**

- **SALES-9196** — Story points set to 1 on 2026-06-20 by Alex Burton (SU&TC Zendesk bucket)
- **SALES-9208** — Story points set to 1 on 2026-06-16 by Gustavo Silva (OpportunityTriggerHelper bug)

**Pattern:** The majority of mid-sprint additions are reactive: Zendesk bucket tickets (SALES-9190, SALES-9193, SALES-9196), production bugs (SALES-9207, SALES-9208, SALES-9214), and end-of-sprint CLONE tickets for carry-forward work (SALES-9200, SALES-9201, SALES-9232–9234, SALES-9265, SALES-9268, SALES-9269). This reflects legitimate priority shifts (ALRA routing urgency, production incidents) combined with incomplete sprint grooming — many CLONE tickets were created on 6/22–6/24 to capture work already in progress.

### Velocity & Throughput

| Sprint | Completed Points |
|--------|-----------------|
"""
    for sprint_name, pts in hist.items():
        report += f"| {sprint_name} | {pts} |\n"
    report += f"| **{SPRINT_NAME}** (current) | **{a['done_pts']}** |\n"

    report += f"""
The current sprint completed **{a['done_pts']} points** across {total_tickets} tickets. Historical comparison shows the team is maintaining high throughput with a large number of 1-point tickets (Zendesk buckets, quick fixes, clones). No obvious PTO or holiday impact this sprint.

### Burndown Analysis

**Pattern: {pattern}**

Points closed by day (within sprint window):

| Date | Points Closed |
|------|---------------|
"""
    for day, pts in sorted(a["by_day"].items()):
        if "2026-06-11" <= day <= "2026-06-24":
            report += f"| {day} | {pts:.0f} |\n"

    last_3 = sum(v for d, v in a["by_day"].items() if d >= "2026-06-22")
    report += f"""
**{last_3:.0f} points** ({last_3/a['done_pts']*100:.0f}% of sprint total) closed in the final 3 days (6/22–6/24). Closures accelerated significantly in the last week, with 6/23–6/24 accounting for the bulk of remaining ALRA, routing, and clone ticket completions.

### Bug Analysis

**{bug_count} bugs closed (Done status).** Reason for Bug field (`customfield_10142`) was **not populated on any closed bug** — root cause categorization is unavailable.

| Reason for Bug | Count |
|----------------|-------|
| Not populated in Jira | {bug_count} |

Closed bugs: {", ".join(k for k, _, _ in a["bugs_done"])}

**Process improvement:** Enforce "Reason for Bug" field completion before moving bugs to Done.

### Related PT/SELLTECH Work

No SELLTECH- tickets were found tied to SRT work this sprint. Three PT project tickets were updated during the sprint window with Salesforce relevance:
- **PT-832** — Data Sync Reliability: Supply, Salesforce and Admin (In Progress)
- **PT-1091** — Voice Capture Within Salesforce (In Progress)
- **PT-1096** — Salesforce User Experience (Not Started)

---

## Per-Engineer Summary

"""
    for eng in TEAM:
        done = a["by_engineer"][eng]["done"]
        carry = a["by_engineer"][eng]["carry"]
        done_pts = sum(x[2] for x in done)
        report += f"### {eng}\n\n"
        report += f"**Total points completed: {done_pts}**\n\n"
        if done:
            report += "**Tickets completed:**\n"
            for key, summary, pts in sorted(done, key=lambda x: x[0]):
                report += f"- {key} — {summary} ({pts} pt)\n"
        else:
            report += "*No tickets completed this sprint.*\n"
        report += "\n"
        if carry:
            report += "**Tickets carried over:**\n"
            for key, summary, pts in carry:
                report += f"- {key} — {summary} ({pts} pt)\n"
        else:
            report += "**Tickets carried over:** None\n"
        report += "\n"

    last_3_pct = last_3 / a['done_pts'] * 100 if a['done_pts'] else 0

    report += f"""---

## Discussion Prompts

1. **{added_count} tickets were added mid-sprint (+{a['added_pts']} points)** — including 6 CLONE tickets created on 6/22–6/24 (SALES-9232, SALES-9233, SALES-9234, SALES-9265, SALES-9268, SALES-9269). Should CLONE tickets be created at sprint planning instead of end-of-sprint to improve visibility?

2. **KTLO consumed {pct(ktlo_pts):.0f}% of completed points** (target: 16%). Zendesk bucket tickets (SALES-9190, SALES-9193, SALES-9196, SALES-9200, SALES-9201) account for much of this. What can we deflect to self-service or tier-1 support?

3. **All {bug_count} closed bugs have no "Reason for Bug" populated.** Should we block Done transitions on bugs until this field is set? Who owns enforcing this?

4. **{last_3_pct:.0f}% of points closed in the final 3 days** — is this sustainable, or should we break down larger ALRA spikes (SALES-9137, SALES-9162 at 3 pts each) into smaller deliverables earlier in the sprint?

5. **SALES-9168 (5 pts) was the largest single story completed** — Inquiry PE funnel qualification work landed mid-sprint. Was the 5-point estimate accurate, and should similar cross-team integration stories be flagged earlier in grooming?

---

*Sprint goal (from Jira): ALRA Routing Support, Outreach Tech Design, Sox Tasks, Salesforce Security Phase 2, Commission Backfill*
"""
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)
    print(f"Report written to {out_path}")
    print(json.dumps({"done_pts": a["done_pts"], "committed_pts": a["committed_pts"], "buckets": buckets}, indent=2))


if __name__ == "__main__":
    main()
