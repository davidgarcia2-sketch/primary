# Question bank

Snapshot of Confluence [Intake Questions by Request Type](https://trr-prod.atlassian.net/wiki/spaces/SRT/pages/398753794/Intake+Questions+by+Request+Type), version 5.

These are examples of what engineering may ask. They are not a form. Ask only what this request needs, and put the questions that change the size first. At Stage 1, pick at most six.

## Always check: cross-cutting groups

Ask when the request touches the group's data, process, or outputs, even if it does not say so.

- Reports, dashboards, or list views: do those views need to change, or only the data underneath?
- Compensation: do past periods need a backfill, does launch have to wait until a comp period closes, and do commissions already calculated on the old data need restating?

## New Custom Field
- What object? What is the name of the object you want?
- Data type (text, number, date, checkbox, lookup)?
- Required or optional?
- Who enters the data: user, Flow, integration, or system?
- Validation rules: min/max, format, or dependent on other fields?
- Which profiles can see it? Which can edit?
- Do we need a mass update or population of the new field? If yes, see Data Backfill.

## Picklist or Dropdown Changes
- Existing field or brand new?
- Complete list of values. Which is default?
- Is it record-type dependent?
- Do old values get retired? What happens to records using retired values?
- Does any integration, report, or dashboard filter on these values?

## New Automation (Flow, Trigger, Validation Rule)
- What event starts it? Record create, update, delete, or schedule?
- What are the exact entry criteria (field X changed to Y)?
- What actions happen? Update fields, send email, create task, callout?
- What happens if it fails mid-run? Roll back or partial save?
- How many records could fire at once?
- Any recursion risk?

## New Integration or API Work
- Source system name and contact.
- Direction: inbound, outbound, or bidirectional?
- Frequency: real-time, hourly, daily, or one-time migration?
- Volume: how many records per batch?
- Error handling: where do failed records go? Who gets notified?
- Field mapping: is there a draft mapping spreadsheet?
- Authentication: existing connected app or new setup?

## Data Backfill or Mass Update
- Which records are in scope, and what date range or filter defines them? Is the end date included, and in which timezone?
- Where does the corrected value come from, and what happens to records with no source value?
- If several source records match one target, which wins: earliest, latest, or something else?
- Do triggers, flows, and validation rules need bypassing during the load? What re-runs afterward?
- Is the cause of the bad data fixed, or will this need doing again?
- Have downstream calculations already run on the bad data, and do they need redoing?
- Who validates a sample before the full run, and what does a good sample look like?
- How do source timestamps map onto the target field without shifting dates?
- If a query or script is provided: can it return more than one row per record, and which column holds the value to load?

## New Report or Dashboard
- Who needs to see it and how often?
- Filters: by user, team, date range, record type?
- Existing report to clone, or build from scratch?
- Does it need a subscription or email?
- Who owns keeping it accurate after launch?

## New LWC or UI Component
- Is there a wireframe or screenshot?
- Desktop only, or mobile too?
- What object or record does it sit on?
- What data does it pull? Real-time or cached?
- What happens when data is missing or the callout fails?

## Routing or Assignment Changes (LeanData, SUMO, Omni)
- What are the exact matching rules?
- What are the pools or queues?
- Weighting: round-robin, load-based, or skill-based?
- What is the fallback if nothing matches?
- Is there test data that should route each way?

## Permission or Security Changes
- Which profiles or permission sets?
- Read, create, edit, or delete?
- Does this change field-level security, object access, or app visibility?
- Any compliance or data privacy requirement driving it?
- Written supervisor approval is required for all enhanced access requests (SOX).
- One-time grant for named users, or an ongoing process? If both, split them (see drafting rules 1 and 2).

## Tool or Channel Switch (phone, SMS, dialer, and similar)
Treat comments about parity, wrap-up, dispositions, stage updates, notes, timestamps, texts, or old activity as part of the request.
- Is this replacing a current tool, or adding one next to it?
- What does the team do today in the old tool that has to work the same on day one?
- Which of those are must-have for launch, and which can wait?
- If comments name a required behavior the description leaves out, is it in scope?
- Was the team told the new tool works differently? Who heard that, and when?
- Do they need to see or reply to activity that already happened in the old tool?

## Zoom Phone numbers
- Each user needs a Zoom license and the end user's zip code.
- Will they also need a Zoom ZRA license? Retail users do not use ZRA.

## Process or Workflow Change (no build)
- Current state: who does what, in what order, using what tool?
- Future state: what changes?
- Is training or enablement needed?
- How do we know it worked?
