# Sizing

Snapshot of Confluence [T-Shirt Size](https://trr-prod.atlassian.net/wiki/spaces/WOW/pages/13369348/T-Shirt+Size), version 3 (April 2026).

## Scale (person-weeks)

| Size | Min | Median | Max |
|---|---|---|---|
| Below S (ticket-level) | 0 | — | < 2 |
| Small | 2 | 7 | 12 |
| Medium | 13 | 19 | 24 |
| Large | 25 | 49 | 72 |
| Extra-Large | 73 | 108 | 144 |

Over 144 person-weeks: recommend splitting into multiple projects.

`Below S` is not on the Confluence page. Many SRT requests (one field, one picklist, one report) are days of work, not weeks. Report them as `Below S (ticket-level)` and send them straight to a story rather than forcing a Small.

Capacity reference: 11 available person-weeks per engineer per quarter.

## Confidence and range width

| Confidence | Typical input | Range allowed |
|---|---|---|
| Low | 1–3 sentences, no systems or volumes named | Up to two adjacent sizes (`S–M`) or "S or larger" |
| Medium | Systems, objects, users, and rough volumes known; some TBDs | One size, or two adjacent sizes with a stated lean (`M, could be L`) |
| High | Requirements reviewed, scope and AC locked | One size |

If the input is too vague to size at all (no system, no user, no outcome), say `Not sizable yet` and ask the two or three questions that would make it sizable.

## Salesforce size drivers

Use these to place the request and to write the "what could change it" lines. Each item is a reason to move up, not an automatic jump.

**Usually keeps it small (often Below S)**
- Config only: field, picklist value, page layout, list view, report or dashboard tile
- Permission set assignment for named users
- One record type or one object

**Pushes it up**
- An integration: a new external system, a new connected app, bidirectional sync, or real-time requirements
- Data backfill or migration, especially across past periods or with no single locked source
- Compensation, commissions, or past-period restatement
- Routing or assignment changes (LeanData, SUMO, Omni-Channel), including test data for every route
- A new LWC or custom UI, especially with callouts or mobile support
- Automation that fires in bulk, has recursion risk, or needs rollback behavior
- Tool or channel switches (phone, SMS, dialer) where day-one parity with the old tool is expected
- Multiple teams, objects, or business units affected
- SOX or compliance approval paths
- An abstract rule ("anyone on Adam's team") that has no Salesforce structure behind it yet

**Unknowns that most often blow up an estimate**
- "Make it automatic" with no defined criteria
- An unnamed source system or data owner
- Unknown record volumes
- Whether historical data must change
- Whether reports and dashboards downstream must change
