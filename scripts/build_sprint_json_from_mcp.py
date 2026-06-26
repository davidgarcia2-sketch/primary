#!/usr/bin/env python3
"""Build sprint_issues.json from compact ticket records (sourced from Jira MCP)."""
import json
from pathlib import Path

# Compact records: key, summary, status, type, sp, assignee, created, resolved, labels (pipe-sep), bug_reason
RECORDS = """SALES-5940|Missing User External IDs on Contact - Why is this happening?|Done|Bug|1|Gustavo Silva|2024-09-30T12:33:05.047-0700|2026-06-22T09:50:06.347-0700|Sales_Bug_Filter_SF_ext_id,salesforce|
SALES-8415|Create a process to check and implement Release updates in Salesforce|Done|Story|2|Nag Malluru|2026-01-22T22:12:46.010-0800|2026-06-24T13:32:19.032-0700|salesforce,security|
SALES-8507|Upgrade Zoom in Production  to version 2.38|Done|Task|1|Navinchandra Gupta|2026-02-04T12:59:56.858-0800|2026-06-13T11:59:05.317-0700|package_upgrade,salesforce,zoom|
SALES-8541|Bump classes from API Version 56 to 65|Done|Story|3|Michael Criswell|2026-02-09T13:44:47.380-0800|2026-06-23T09:50:22.494-0700|ARB_Approved,CAB_Approved,In_QA,PR_created,Ready_For_QA|
SALES-8549|Bump Controller classes from API Version 54 to 65 - Ticket 1 of 2|Done|Story|2|Gustavo Silva|2026-02-09T14:21:40.988-0800|2026-06-16T11:45:46.375-0700|ARB_Approved,CAB_Approved,In_QA,PR_created,QA_Completed|
SALES-8744|Duplicate id in list error|Done|Bug|2|Gustavo Silva|2026-03-24T10:38:32.065-0700|2026-06-17T11:58:06.609-0700|ARB_Approved_Not_required,In_QA,PR_created|
SALES-9031|Security Update: Remediate Connected App and API access for VPN/proxy blocking|Done|Story|1|Nag Malluru|2026-05-18T11:00:22.757-0700|2026-06-18T10:44:07.201-0700|005317465,network-access,salesforce-security|
SALES-9048|Outreach Automation: SMS/Phone Automation|Done|Spike|2|Jummy Sanni|2026-05-19T13:27:44.148-0700|2026-06-12T10:27:13.879-0700|SRT-Product|
SALES-9076|Analysis on recurring sumo issues |Done|Story|2|Jummy Sanni|2026-05-27T10:04:22.513-0700|2026-06-23T08:53:52.703-0700|NeedsAcceptanceCriteria|
SALES-9077|Technical Design for Outreach Optimization|Done|Story|1|Nag Malluru|2026-05-27T10:44:22.182-0700|2026-06-17T15:18:52.773-0700||
SALES-9108|Sync Errors From Coi - Inventory unit not consignable|Done|Spike|3|Chris Burns|2026-05-30T12:45:13.402-0700|2026-06-23T11:27:36.182-0700||
SALES-9117|Reconnect Slack and Salesforce for all the users|Done|Bug|1|Nag Malluru|2026-06-02T15:02:15.264-0700|2026-06-16T09:06:38.455-0700||
SALES-9120|Backfill AUR_Contributing_Price__c field |Done|Task|2|Michael Criswell|2026-06-03T09:03:33.342-0700|2026-06-18T08:50:06.156-0700|PR_created|
SALES-9121|Resolve Row Lock 1/3 : Opportunity/COI|Done|Story|2|Michael Criswell|2026-06-03T13:10:43.747-0700|2026-06-18T10:02:45.808-0700|ARB_Approved,CAB_Approved,In_QA,NeedsAcceptanceCriteria,PR_created,Ready_For_QA|
SALES-9122|Resolve Row Lock 2/3 : Opportunity/Lead|Done|Story|2|Chris Burns|2026-06-03T13:11:44.043-0700|2026-06-23T09:50:15.686-0700|ARB_Not_Required,NeedsAcceptanceCriteria,PR_created,QA_Completed|
SALES-9123|Resolve Row Lock 3/3 : Opportunity/Contact|Done|Story|2|Grace Saint|2026-06-03T13:12:40.202-0700|2026-06-17T11:57:49.601-0700|ARB_Not_Required,CAB_Approved,NeedsAcceptanceCriteria,PR_created,QA_Completed|
SALES-9125|What user license counts do we have available for the current count need and eoy need for sales reps? -1|Done|Spike|1|Navinchandra Gupta|2026-06-04T07:47:36.620-0700|2026-06-10T15:03:31.088-0700|salesforce|
SALES-9126|Create New ALRA Sales Role -1|Done|Story|1|Alex Burton|2026-06-04T08:25:33.816-0700|2026-06-16T13:52:12.171-0700|ARB_Approved,CAB_Approved,In_QA,NeedsAcceptanceCriteria,PR_created,salesforce|
SALES-9128|Automatic Set up ALRA to assign the proper Sales software and permissions to the new reps when they are onboarded. -1|Done|Story|1|Alex Burton|2026-06-04T10:00:19.047-0700|2026-06-17T11:57:34.159-0700|ARB_Not_Required,CAB_Approved,In_QA,PR_created,salesforce|
SALES-9130|Update the TP capture so that it captures when someone uses zoom from the conversation panel -1|Done|Spike|1|Grace Saint|2026-06-04T10:37:44.872-0700|2026-06-12T13:15:30.577-0700|salesforce|
SALES-9133|New fields: Ramp Code and Job Profile -1|Done|Story|2|Navinchandra Gupta|2026-06-04T11:56:32.283-0700|2026-06-17T10:11:01.525-0700|ARB_Approved,CAB_Approved,PR_created,QA_Completed,salesforce|
SALES-9137|What is our current state for Routing of Leads and Opportunities for new and repeat? -1|Done|Spike|3|Alex Burton|2026-06-04T14:23:35.281-0700|2026-06-24T14:23:43.681-0700||
SALES-9138|MGO high value lead is identified it will be marked as a HV Lead - 1|Done|Story|2|Chris Burns|2026-06-04T14:37:36.906-0700|2026-06-24T10:58:20.643-0700|ARB_Not_Required,CAB_Approved,In_QA,PR_created|
SALES-9141|For the assignment of the mgos by % what would be involved in assessing the cost benefit of build vs buy -1 or 2|Done|Spike|1|Navinchandra Gupta|2026-06-04T16:30:31.906-0700|2026-06-22T09:15:30.366-0700|salesforce|
SALES-9149|Available Data is not being synced from Admin|Done|Bug|1|Gustavo Silva|2026-06-08T15:19:51.537-0700|2026-06-10T12:06:27.855-0700||
SALES-9161|Title levels on user record and sales quota records -1|Done|Story|2|Chris Burns|2026-06-08T18:07:11.578-0700|2026-06-24T10:58:13.098-0700|ARB_Approved,CAB_Approved,In_QA,PR_created,salesforce|
SALES-9162|Evaluate Design for Weighted Routing, Escalation and Lead Scoring -1|Done|Spike|3|Sai Deepika Kanuri|2026-06-08T21:28:34.436-0700|2026-06-24T11:22:18.494-0700||
SALES-9163|Can we create manually contact vendors with international addresses and how?|Done|Spike|2|Gustavo Silva|2026-06-09T08:55:28.331-0700|2026-06-19T07:04:38.986-0700|PR_created|
SALES-9164|Zoom Upgrade Production|Done|Story|1|Alex Burton|2026-06-09T09:15:22.274-0700|2026-06-16T08:03:26.477-0700|ARB_Not_Required,NeedsAcceptanceCriteria,PR_not_required,QA_Completed,salesforce,zoom|
SALES-9166|How to automate blocklisting and removal of blocklisting in Zoom|Done|Spike|1|Alex Burton|2026-06-09T11:44:10.960-0700|2026-06-24T14:31:08.491-0700||
SALES-9167|Change Inquiry PE to receive shipping label information and bypass creation inside Salesforce|Done|Story|3|Gustavo Silva|2026-06-09T14:41:54.990-0700|2026-06-16T11:44:59.914-0700|ARB_Approved,In_QA,PR_created|
SALES-9168|Update Inquiry PE to receive funnel consignment  qualification responses for reps visibility|Done|Story|5|Gustavo Silva|2026-06-09T14:46:23.873-0700|2026-06-22T08:58:31.188-0700|ARB_Approved,CAB_Approved,In_QA,PR_created,QA_Completed|
SALES-9169|ARB Transition Plan|Done|Spike|2|Nag Malluru|2026-06-09T15:34:03.914-0700|2026-06-17T09:07:08.613-0700||
SALES-9170|Update the Apex logic to add available date filter for opp Shipped after June 1|Done|Story|2|Michael Criswell|2026-06-09T16:21:35.595-0700|2026-06-23T11:59:31.429-0700|ARB_Approved,CAB_Approved,In_QA,PR_created|
SALES-9171|SUMO - Page timeout and Bugsnag Issue |Done|Spike|3|Sai Deepika Kanuri|2026-06-09T17:04:02.423-0700|2026-06-23T11:11:08.847-0700||
SALES-9172|Backfill NC Credit and refresh COI to calculate the credi|Done|Task|2|Sai Deepika Kanuri|2026-06-09T17:08:02.342-0700|2026-06-24T11:21:32.429-0700||
SALES-9173|6/15/26 - 6/22/26 Cohorts|Done|Story|1|Alex Burton|2026-06-10T08:08:53.363-0700|2026-06-22T12:02:52.237-0700|NeedsAcceptanceCriteria,PR_not_required|
SALES-9178|[2026-06-10]Force Sync of Consignment Items from Admin to Salesforce|Done|Story|1|Gustavo Silva|2026-06-10T10:37:55.585-0700|2026-06-10T11:51:36.194-0700|ARB_Approved_Not_required,NeedsAcceptanceCriteria,PR_not_required|
SALES-9179|Salescloud Q2 2026 Manual Remediation|Done|Story|1|Navinchandra Gupta|2026-06-10T11:16:48.138-0700|2026-06-14T19:04:44.321-0700|ARB_Not_Required,NeedsAcceptanceCriteria,PR_not_required,salesforce,sox-audit|
SALES-9180|SRT Q3 Capacity Planning |Done|Story|3|Navinchandra Gupta|2026-06-10T11:20:58.030-0700|2026-06-23T14:27:27.962-0700|ARB_Not_Required,NeedsAcceptanceCriteria,PR_not_required,salesforce|
SALES-9186|Nag - Zendesk Bucket - S/w Upgrade - 06/11-6/24|Done|Bug|0|Nag Malluru|2026-06-10T15:24:41.006-0700|2026-06-17T15:20:21.335-0700||
SALES-9187|KTLO: ZD tickets 6/11-6/24|Won't Do|Story|1|Jummy Sanni|2026-06-11T09:20:59.361-0700|2026-06-24T15:03:48.839-0700|DescriptionTooShort,NeedsAcceptanceCriteria|
SALES-9188|zen desk|Won't Do|Bug||Chris Burns|2026-06-11T09:21:58.346-0700|2026-06-11T09:55:09.248-0700||
SALES-9189|Adjust Sales Role Field on User Record for New Sales Titles|Done|Story|1|Alex Burton|2026-06-11T09:33:59.031-0700|2026-06-17T08:37:32.244-0700|ARB_Approved,CAB_Approved,In_QA,PR_created|
SALES-9190|TD: Alex Zendesk Ticket 6/11 - 6/25|Done|Bug|1|Alex Burton|2026-06-11T09:52:55.672-0700|2026-06-24T14:24:03.244-0700|DescriptionTooShort,PR_not_required|
SALES-9191|Real Partners: June 20th Data Export|Done|Task|1|Grace Saint|2026-06-11T09:55:50.847-0700|2026-06-18T10:58:07.069-0700|ARB_Not_Required|
SALES-9193|Nag - Zendesk Bucket - KTLO - 06/11-6/24|Done|Bug|1|Nag Malluru|2026-06-11T10:11:20.424-0700|2026-06-23T11:00:43.279-0700||
SALES-9195|Nag - Zendesk Bucket - Tech Debt - 06/11-6/24|Done|Bug|0|Nag Malluru|2026-06-11T10:12:32.468-0700|2026-06-17T15:19:55.224-0700||
SALES-9196|SU&TC: Alex Zendesk Ticket 6/11 - 6/25|Done|Bug|1|Alex Burton|2026-06-11T10:13:26.155-0700|2026-06-24T14:24:20.373-0700|PR_not_required|
SALES-9197|SOX SF-CM-01 (Change Management) Control Task|Done|Task|1|Navinchandra Gupta|2026-06-11T11:38:34.700-0700|2026-06-16T08:40:23.872-0700|salesforce,sox-audit|
SALES-9199|ALRA Solutioning and Review - 1|Done|Task|2|Grace Saint|2026-06-15T06:19:02.791-0700|2026-06-22T07:56:40.148-0700|ARB_Approved_Not_required,PR_not_required|
SALES-9200|CLONE - Tech Debt: ZD tickets 6/11-6/24|Done|Story|1|Jummy Sanni|2026-06-15T09:03:14.708-0700|2026-06-24T14:41:42.603-0700|DescriptionTooShort,NeedsAcceptanceCriteria|
SALES-9201|CLONE - SFTW Upgrade: ZD tickets 6/11-6/24|Done|Story|1|Jummy Sanni|2026-06-15T09:07:21.640-0700|2026-06-24T14:41:31.243-0700|DescriptionTooShort,NeedsAcceptanceCriteria|
SALES-9207|CID 16146775 - New Rolex Item getting added to COI by TRR CRM Service user|Done|Bug|1|Gustavo Silva|2026-06-15T12:17:13.490-0700|2026-06-16T10:13:11.594-0700|ARB_Not_Required|
SALES-9208|OpportunityTriggerHelper.setContactContractComplete | Contact.Contract_Complete__c missing from SOQL|Done|Bug|1|Gustavo Silva|2026-06-16T10:52:14.439-0700|2026-06-17T11:57:56.357-0700|ARB_Approved_Not_required,CAB_Approved,In_QA,PR_created,QA_Completed|
SALES-9210|Activate field history on Payment__c object|Done|Story|1|Gustavo Silva|2026-06-17T09:41:51.344-0700|2026-06-22T08:58:22.775-0700|ARB_Approved,CAB_Approved,In_QA,NeedsAcceptanceCriteria,PR_created,QA_Completed|
SALES-9214|Vendor Price Update Errors|Done|Bug|1|Gustavo Silva|2026-06-18T10:18:16.101-0700|2026-06-18T12:12:24.214-0700||
SALES-9218|Backfill of field: Ramp Code on quota object - 1|Done|Story|1|Navinchandra Gupta|2026-06-18T11:43:24.354-0700|2026-06-22T15:39:31.630-0700|ARB_Not_Required,NeedsAcceptanceCriteria,salesforce|
SALES-9219|Create Permission Set to Bypass MFA Enforcement for Test Automation Users|Done|Story|1|Michael Criswell|2026-06-18T13:06:03.889-0700|2026-06-23T09:49:31.152-0700|ARB_Approved,CAB_Approved,In_QA,PR_created|
SALES-9222|Optimize how new vendor opportunities are created in SF|Done|Story|1|Gustavo Silva|2026-06-19T07:34:44.808-0700|2026-06-23T09:48:59.216-0700|ARB_Approved,CAB_Approved,In_QA,PR_created,QA_Completed|
SALES-9231|Retry oban job of inquiries that failed because of the unknown field error in Production|Done|Task||Gustavo Silva|2026-06-22T10:58:59.690-0700|2026-06-22T11:06:50.034-0700||
SALES-9232|CLONE - Security Update: Implement step-up authentication for Salesforce report activities|Done|Story|1|Nag Malluru|2026-06-22T13:17:08.892-0700|2026-06-22T13:17:36.628-0700|005317465,reports,salesforce-security,step-up-auth|
SALES-9233|CLONE - Cleanup Unused Reports and Dashboards|Done|Spike|1|Nag Malluru|2026-06-22T13:20:41.203-0700|2026-06-22T13:20:58.946-0700|NeedsAcceptanceCriteria|
SALES-9234|CLONE - ZoomSyncPlatformEventTriggerHandler.ZoomSyncPlatformEventTriggerHandlerException From Invalid First Name On Contact|Done|Spike|2|Michael Criswell|2026-06-22T14:24:04.112-0700|2026-06-24T10:42:00.214-0700||
SALES-9235|Investigate why the BatchUpdateContactUserExternalIds is not processing recent records created|Won't Do|Spike||Gustavo Silva|2025-06-05T19:47:01.857-0700|2026-06-23T06:52:39.818-0700||
SALES-9241|CLONE - Agentforce: Look into prompt errors|Done|Bug|1|Grace Saint|2026-06-23T12:10:16.247-0700|2026-06-23T12:10:35.279-0700|ARB_Approved_Not_required,salesforce|
SALES-9242|Backfill Total Price and Total Priced Units for Opps Shipped After June 1 with Null Available Date|Done|Task|1|Michael Criswell|2026-06-23T13:39:17.331-0700|2026-06-23T19:16:01.131-0700||
SALES-9243|CLONE - Order the necessary software licenses for the ALRA expansion 1|Done|Task|1|Navinchandra Gupta|2026-06-23T14:27:54.639-0700|2026-06-23T14:28:34.075-0700|salesforce|
SALES-9265|CLONE - Update Opportunity Apex Trigger to Capture Scheduled Van Pickups|Done|Story|2|Grace Saint|2026-06-24T14:15:37.442-0700|2026-06-24T14:15:53.347-0700|ARB_Approved,In_QA,PR_created,Ready_For_QA|
SALES-9268|CLONE - This is an MGO this is an SGO -1|Done|Story|1|Jummy Sanni|2026-06-24T15:01:30.298-0700|2026-06-24T15:03:16.868-0700|ARB_Approved,In_QA,PR_created,salesforce|
SALES-9269|CLONE - Change the help text/description for Total Retail Price on Opportunity object|Done|Story|1|Jummy Sanni|2026-06-24T15:03:57.278-0700|2026-06-24T15:04:52.981-0700|In_QA,PR_created|
"""


def sp(val):
    if val == "" or val is None:
        return None
    return int(val)


def parse_record(line):
    """Parse pipe-delimited record; summary may contain '|' characters."""
    tail = line.rsplit("|", 8)
    if len(tail) != 9:
        raise ValueError(f"Expected 9 fields, got {len(tail)}: {line[:80]}...")
    head, status, itype, sp_val, assignee, created, resolved, labels, bug_reason = tail
    key, summary = head.split("|", 1)
    return key, summary, status, itype, sp_val, assignee, created, resolved, labels, bug_reason


def build_issue(parts):
    key, summary, status, itype, sp_val, assignee, created, resolved, labels, bug_reason = parts
    labels_list = [l for l in labels.split(",") if l]
    return {
        "key": key,
        "fields": {
            "summary": summary,
            "status": {"name": status},
            "issuetype": {"name": itype},
            "labels": labels_list,
            "assignee": {"displayName": assignee},
            "created": created,
            "resolutiondate": resolved,
            "customfield_10026": sp(sp_val),
            "customfield_10142": bug_reason or None,
        },
    }


def main():
    issues = []
    for line in RECORDS.strip().split("\n"):
        issues.append(build_issue(parse_record(line)))

    out = Path("/workspace/data/sprint_issues.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump({"issues": issues}, f, indent=2)
    total_sp = sum(p["fields"]["customfield_10026"] or 0 for p in issues)
    print(f"Wrote {len(issues)} issues, {total_sp} total story points to {out}")


if __name__ == "__main__":
    main()
