#!/usr/bin/env python3
"""Generate SRT sprint retrospective markdown from sprint-8591-metrics.json."""

import json
from pathlib import Path

METRICS_PATH = Path("/workspace/data/sprint-8591-metrics.json")
REPORT_PATH = Path("/workspace/reports/srt-sprint-retrospective-SALES-8591-2026-06-05.md")

TARGETS = {"product": 48, "tech": 16, "ktlo": 16, "buffer": 20}
TARGET_PTS = 70  # ~70 pt planning baseline per prior reports


def fmt_engineer(name, data):
    done = data.get("done", [])
    carry = data.get("carry", [])
    total = sum(p for _, _, p in done)
    lines = [f"#### {name}", ""]
    if done:
        items = "; ".join(f"`{k}` — {s} — **{p}**" for k, s, p in sorted(done, key=lambda x: x[0]))
        lines.append(f"- **Completed (key — summary — pts):** {items}. **Total: {total} pts.**")
    else:
        lines.append("- **Completed:** None.")
    if carry:
        items = "; ".join(f"`{k}` — {s} — **{p}**" for k, s, p in carry)
        lines.append(f"- **Carried over:** {items}")
    else:
        lines.append("- **Carried over:** None.")
    lines.append(f"- **Total points completed:** **{total}**")
    lines.append("")
    return "\n".join(lines)


def burndown_narrative(daily):
    if not daily:
        return "- **Unavailable** (no resolution dates on Done issues)."
    lines = []
    early = sum(v for d, v in daily.items() if d <= "2026-05-18")
    mid = sum(v for d, v in daily.items() if "2026-05-19" <= d <= "2026-05-22")
    late = sum(v for d, v in daily.items() if d >= "2026-05-23")
    lines.append(f"- **Early sprint (through 2026-05-18):** **{early}** pts closed.")
    lines.append(f"- **Mid sprint (2026-05-19 – 2026-05-22):** **{mid}** pts closed.")
    lines.append(f"- **Late sprint (2026-05-23+):** **{late}** pts closed — includes Memorial Day week (**2026-05-26** US holiday).")
    peak = max(daily.items(), key=lambda x: x[1])
    lines.append(f"- **Peak closure day:** **{peak[0]}** with **{peak[1]}** pts.")
    post = [(d, v) for d, v in daily.items() if d > "2026-05-28"]
    if post:
        items = ", ".join(f"**{d}** ({v} pts)" for d, v in post)
        lines.append(f"- **Post–sprint-end Done timestamps:** {items} (after nominal end **2026-05-28**).")
    shape = "late-heavy" if late > early else "front-loaded" if early > late * 1.5 else "mixed"
    lines.append(f"- **Shape:** **{shape}** — {'finish-line clustering' if late >= mid else 'steady throughput'}.")
    return "\n".join(lines)


def capacity_table(buckets, total_pts):
    rows = []
    labels = [
        ("product", "Product (SRT-product / SRT-RO)"),
        ("tech", "Tech Health (SRT-Domain-Tech-Debt, SRT-Software-Upgrades)"),
        ("ktlo", "KTLO (SRT-KTLO)"),
        ("buffer", "Buffer / Unplanned"),
    ]
    for key, label in labels:
        pts = buckets.get(key, 0)
        pct = (pts / total_pts * 100) if total_pts else 0
        tgt_pts = round(TARGET_PTS * TARGETS[key] / 100)
        delta = pts - tgt_pts
        rows.append(f"| {label} | {TARGETS[key]}% | ~{tgt_pts} | **{pts}** | **{pct:.1f}%** | **{delta:+.0f} pts vs target** |")
    return "\n".join(rows)


def main():
    m = json.loads(METRICS_PATH.read_text())
    buckets = m["buckets"]
    total_pts = m["total_points"]
    ktlo_pct = (buckets.get("ktlo", 0) / total_pts * 100) if total_pts else 0
    product_pts = buckets.get("product", 0)
    product_pct = (product_pts / total_pts * 100) if total_pts else 0

    # Summer '26 batch created 2026-05-12 (before sprint start)
    summer_may12 = m.get("summer_may12_created", [])

    eng_sections = "\n".join(fmt_engineer(n, m["per_engineer"][n]) for n in m["per_engineer"])

    report = f"""# SRT Sprint Retrospective — SALES board (Sprint 8591)

**Data source:** Jira project `SALES`, sprint **Sales 5/14 - 5/27** (ID `8591`, board ID `10`). Snapshot reflects issues as queried after sprint closure (**2026-06-05**). **PT-** tickets: **none** in sprint `8591`. **SELLTECH-** tickets in sprint: **`SELLTECH-1050`** (3 pts, Done, Gustavo Silva), **`SELLTECH-1051`** (2 pts, Done, Gustavo Silva).

---

### Executive Summary

The sprint closed **cleanly with zero carry-over** while delivering **very high throughput**: **{m['done_issues']}** issues reached **Done** totaling **{m['done_points']}** story points across **{m['total_issues']}** sprint issues. The biggest win was **successful Summer '26 release QA execution** (large batch of `SALES-8980`–`SALES-9000` tickets) alongside **6/1 compensation/quota changes** and **Salesforce Security Phase 2** spikes. The biggest concern remains **SRT label discipline**: only **{product_pts}** of **{total_pts}** sprint points (**{product_pct:.1f}%**) carry **`SRT-Product`**, so capacity reporting against SRT buckets is **mostly unclassified**. **Committed points at sprint start**, **full mid-sprint add/remove inventory**, and **scope change %** are **Unavailable without batch changelog replay**.

---

### Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Name | Sales 5/14 - 5/27 |
| Sprint Dates | **2026-05-14** 16:37 UTC → **2026-05-28** 06:30 UTC (completed **2026-05-28** 15:03 UTC) |
| Sprint Goal | 1. 6/1 Comp/Quota Changes 2. Summer Release 2026 3. Outreach Automation 4. Voice Recognition |
| Committed Points | **Unavailable without batch changelog replay at sprint start** |
| Completed Points | **{m['done_points']}** ({m['done_issues']} Done issues) |
| Carry-Over (tickets / points) | **{m['carry_issues']}** / **{m['carry_points']}** |
| Removed (tickets / points) | **Unavailable** (requires parsing sprint removal events from each issue changelog) |
| Added Mid-Sprint (tickets / points) | **{len(m['mid_sprint_created'])}** tickets created after sprint start (**{sum(x['points'] or 0 for x in m['mid_sprint_created'])}** pts where estimated; full add-to-sprint inventory not computed) |
| Scope Change % | **Unavailable** (depends on committed-at-start baseline and net adds/removes) |
| Won't Do (tickets / points) | **{m['wont_do_issues']}** / **{m['wont_do_points']}** |
| Spikes Closed | **{m['spikes_closed']}** (`SALES-8935`, `SALES-8936`, `SALES-8957`, `SALES-8978`, `SALES-9001`, `SALES-9003`, `SALES-9004`, `SALES-9016`) |
| Bugs Closed | **{m['bugs_closed']}** |

---

### Capacity Allocation Breakdown

**Method:** Each sprint issue counted **once**. **Product** if labels contain `SRT-product`, `SRT-Product`, or `SRT-RO`. **Tech Health** if `SRT-Domain-Tech-Debt` or `SRT-Software-Upgrades`. **KTLO** if `SRT-KTLO`. Otherwise **Buffer / Unplanned**. Denominator = **{total_pts}** (sum of story points on all **{m['total_issues']}** sprint issues, treating `null` as **0**).

| Bucket | Target % | Target Points (of ~70) | Actual Points | Actual % | Delta |
|--------|----------|------------------------|-----------------|----------|-------|
{capacity_table(buckets, total_pts)}

**KTLO > 30% flag:** **{"Yes" if ktlo_pct > 30 else "No"}** — **{ktlo_pct:.1f}%** of sprint points carried `SRT-KTLO`.

**Interpretation:** Substantial product, release-QA, and KTLO-class work likely occurred without SRT labels. This table reflects **labels in Jira**, not intent.

---

### Key Findings

#### Scope Creep & Mid-Sprint Changes

- **Full list (all tickets):** **Not produced in this run** (requires `getJiraIssue` + `expand=changelog` for all **{m['total_issues']}** keys).
- **Observed mid-sprint creation pattern:** **{len(summer_may12)}** tickets in the **Summer '26 Release** family were **created 2026-05-12** (before official sprint start on **2026-05-14**) — keys **`SALES-8980`** through **`SALES-9000`** plus security spikes **`SALES-9001`**, **`SALES-9003`**, **`SALES-9004`**. This represents a **large scope injection** tied to release validation, not ad-hoc churn.
- **Illustrative example — `SALES-8980`:** Created **2026-05-12**, added to sprint before start; story points adjusted **null → 1 → 2 → 1** by Navinchandra Gupta / Alex Burton before/during sprint start (per prior changelog review).
- **Won't Do de-scoping:** **{m['wont_do_issues']}** tickets closed as **Won't Do** (mostly duplicate Summer '26 sub-tickets consolidated into parent work).

#### Velocity & Throughput

| Sprint | Jira sprint id | Done points (`status = Done`) |
|--------|----------------|-------------------------------|
| **Current** | **8591** | **{m['done_points']}** ({m['done_issues']} Done tickets) |
| Prior | **8190** | **90** (55 Done tickets) |
| Prior | **7949** | **108** (62 tickets with points) |
| Prior | **7548** | **83** (50 Done tickets) |

**Trend:** **Up sharply** from **90 → {m['done_points']}** vs immediately prior sprint (**+{m['done_points'] - 90}** pts), and **above** both **7949** (**108**) and **7548** (**83**). Memorial Day (**2026-05-26**) may have reduced final-week capacity; throughput still exceeded prior sprint.

#### Burndown Analysis

Using **`resolutiondate`** on **`status = Done`** issues in sprint **8591**:

{burndown_narrative(m['daily_done_points'])}

#### Bug Analysis

- **Bugs closed (Done):** **{m['bugs_closed']}** issues.
- **Reason for Bug (`customfield_10142`):** **Unavailable / not populated** — Jira returned **`null`** for **all {m['bugs_closed']}** closed bugs in sprint **8591** (same data gap as sprint **8190**).
- **Zendesk bucket tickets:** Multiple per-engineer Zendesk holder tickets (`SALES-8975`, `SALES-9013`, `SALES-9014`, `SALES-9015`, `SALES-9017`, `SALES-9042`) account for ongoing support load.

---

### Per-Engineer Summary

Counts below are **`status = Done`** in sprint **8591** only.

{eng_sections}
---

### Discussion Prompts

1. **Velocity jumped from 90 → {m['done_points']} pts while sprint issue count grew to {m['total_issues']}.** How much of that uplift was **Summer '26 release QA tickets** (`SALES-8980`–`SALES-9000`) vs **net-new product work**, and should release validation be **pre-planned as its own capacity lane**?
2. **Only {product_pts} / {total_pts} sprint points carry `SRT-Product` ({product_pct:.1f}%).** Which completed comp/quota items (`SALES-8876`–`SALES-8879`, `SELLTECH-1050`/`1051`) were true product work but **missing labels**?
3. **Zero carry-over despite {m['done_issues']} completions — but `SALES-8551` resolved 2026-06-03 and `SALES-8978` resolved 2026-05-28 after sprint end.** Should the team adopt a **hard rule** that sprint closure requires resolution within sprint boundaries, or accept **administrative tail** for multi-sprint items?
4. **{m['bugs_closed']} bugs closed with zero “Reason for Bug” in Jira.** Do we gate **Done** transitions on `customfield_10142` for bugs (same gap as sprint 8190)?
5. **{len(summer_may12)} Summer '26 tickets were bulk-created 2026-05-12, two days before sprint start.** Could **release checklists** be templated earlier so QA scope does not appear as a **surprise batch** at sprint boundary?
"""
    REPORT_PATH.write_text(report)
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
