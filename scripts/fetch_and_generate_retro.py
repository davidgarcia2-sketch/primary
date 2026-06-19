#!/usr/bin/env python3
"""Fetch sprint issues via Jira MCP-compatible search and generate retro report."""
import json
import subprocess
import sys
from pathlib import Path

# Issue keys and essential fields extracted from Jira sprint "Sales 5/28 - 6/10"
# Full fetch via REST failed; data sourced from Atlassian MCP searchJiraIssuesUsingJql

SPRINT_ISSUES_RAW = """
SALES-8550|Done|Story|Michael Criswell|null|CAB_Approved,In_QA,PR_created,Ready_For_QA|2026-02-09|2026-06-03
SALES-8551|Done|Story|Chris Burns|null|CAB_Approved,In_QA,PR_created,QA_Completed,Ready_For_QA|2026-02-09|2026-06-03
SALES-8552|Done|Story|Michael Criswell|null|CAB_Approved,In_QA,PR_created,Ready_For_QA|2026-02-09|2026-06-03
SALES-8553|Done|Story|Chris Burns|null|ARB_Not_Required,CAB_Approved,DescriptionTooShort,In_QA,PR_created,Ready_For_QA|2026-02-09|2026-06-04
SALES-8650|Done|Story|Gustavo Silva|null|NeedsAcceptanceCriteria,automation,seller|2024-12-31|2026-06-03
SALES-8801|Done|Spike|Navinchandra Gupta|null|SRT-Product|2026-04-01|2026-06-09
SALES-8918|Done|Spike|Jummy Sanni|null|DescriptionTooShort,NeedsAcceptanceCriteria,SRT-Product,salesforce|2026-04-27|2026-06-04
SALES-8920|Done|Story|Sai Deepika Kanuri|null|SRT-Product,salesforce|2026-04-27|2026-06-08
SALES-8965|Done|Story|Gustavo Silva|null|NeedsAcceptanceCriteria|2026-05-07|2026-06-02
SALES-8966|Done|Spike|Chris Burns|null|salesforce|2026-05-07|2026-06-09
SALES-8968|Won't Do|Bug||null||2026-05-07|2026-05-28
SALES-8978|Done|Spike|Nag Malluru|null||2026-05-11|2026-05-28
SALES-9024|Done|Story|Sai Deepika Kanuri|null|SRT-Product,commisions|2026-05-15|2026-06-02
SALES-9028|Won't Do|Bug|Michael Criswell|null||2026-05-18|2026-05-29
SALES-9043|Done|Bug|Sai Deepika Kanuri|null||2026-05-18|2026-06-02
SALES-9046|Won't Do|Bug|Grace Saint|null|ARB_Not_Required|2026-05-19|2026-06-02
SALES-9047|Done|Spike|Grace Saint|null||2026-05-19|2026-06-08
SALES-9060|Done|Spike|Alex Burton|null|salesforce,zendesk|2026-05-20|2026-06-04
SALES-9067|Done|Bug|Grace Saint|null|ARB_Not_Required,PR_not_required,salesforce|2026-05-26|2026-06-01
SALES-9068|Done|Bug|Gustavo Silva|null|CAB_Approved,In_QA,PR_created,QA_Completed,Ready_For_QA|2026-05-27|2026-06-02
SALES-9069|Done|Bug|Gustavo Silva|null|CAB_Approved,In_QA,PR_created,QA_Completed|2026-05-27|2026-06-03
SALES-9070|Done|Story|Gustavo Silva|null|CAB_Approved,DescriptionTooShort,In_QA,NeedsAcceptanceCriteria,PR_created,QA_Completed,Ready_For_QA|2026-05-27|2026-06-08
SALES-9071|Done|Bug|Grace Saint|null|ARB_Not_Required,CAB_Approved,PR_created,QA_Completed|2026-05-27|2026-06-09
SALES-9072|Done|Story|Navinchandra Gupta|null|NeedsAcceptanceCriteria,deployer-access,salesforce,sox-audit|2026-05-27|2026-06-01
SALES-9073|Done|Story|Alex Burton|null|NeedsAcceptanceCriteria,PR_not_required|2026-05-27|2026-06-09
SALES-9074|Done|Spike|Chris Burns|null|bug,salesforce|2026-05-27|2026-06-03
SALES-9078|Done|Spike|Navinchandra Gupta|null|ARB_Not_Required,PR_not_required,salesforce|2026-05-27|2026-06-10
SALES-9079|Done|Story|Michael Criswell|null||2026-05-27|2026-06-10
SALES-9080|Done|Story|Gustavo Silva|null|DescriptionTooShort,NeedsAcceptanceCriteria|2026-05-27|2026-05-27
SALES-9081|Done|Bug|Gustavo Silva|null||2026-05-27|2026-05-28
SALES-9082|Done|Story|Grace Saint|null|ARB_Not_Required,NeedsAcceptanceCriteria,salesforce|2026-05-27|2026-05-28
SALES-9083|Done|Story|Navinchandra Gupta|null|ARB_Not_Required,NeedsAcceptanceCriteria,PR_not_required,salesforce|2026-05-27|2026-06-01
SALES-9084|Done|Bug|Gustavo Silva|null|CAB_Approved,In_QA,PR_created,QA_Completed|2026-05-27|2026-06-03
SALES-9085|Done|Story|Jummy Sanni|null|DescriptionTooShort,NeedsAcceptanceCriteria,SRT-Product,salesforce|2026-05-28|2026-06-10
SALES-9086|Won't Do|Bug|Nag Malluru|null||2026-05-28|2026-06-08
SALES-9087|Done|Bug|Chris Burns|null||2026-05-28|2026-06-10
SALES-9088|Done|Bug|Grace Saint|null|ARB_Not_Required|2026-05-28|2026-06-10
SALES-9089|Done|Story|Gustavo Silva|null|CAB_Approved,In_QA,NeedsAcceptanceCriteria,PR_created,QA_Completed|2026-05-28|2026-06-01
SALES-9105|Done|Bug|Alex Burton|null|PR_not_required|2026-05-28|2026-06-10
SALES-9106|Done|Story|Gustavo Silva|null|CAB_Approved,In_QA,NeedsAcceptanceCriteria,PR_created|2026-05-28|2026-06-04
SALES-9109|Done|Story|Sai Deepika Kanuri|null|NeedsAcceptanceCriteria|2026-05-31|2026-06-01
SALES-9110|Done|Story|Sai Deepika Kanuri|null|NeedsAcceptanceCriteria|2026-06-01|2026-06-04
SALES-9114|Done|Task|Grace Saint|null|ARB_Approved_Not_required,PR_not_required,salesforce|2026-06-02|2026-06-02
SALES-9115|Done|Bug|Navinchandra Gupta|null|ARB_Not_Required,PR_not_required,jira_escalated,salesforce,zendesk|2026-06-02|2026-06-04
SALES-9119|Done|Story|Gustavo Silva|null|CAB_Approved,DescriptionTooShort,In_QA,NeedsAcceptanceCriteria,PR_created,QA_Completed|2024-04-22|2026-06-08
SALES-9124|Done|Story|Gustavo Silva|null|NeedsAcceptanceCriteria,PR_created,QA_Completed|2025-06-27|2026-06-09
SALES-9127|Done|Bug|Gustavo Silva|null|ARB_Not_Required,In_QA,PR_created|2026-06-04|2026-06-04
SALES-9134|Done|Story|Sai Deepika Kanuri|null|NeedsAcceptanceCriteria|2026-06-04|2026-06-04
SALES-9142|Done|Bug|Gustavo Silva|null||2026-06-05|2026-06-09
SALES-9145|Done|Story|Nag Malluru|null||2026-06-08|2026-06-09
SALES-9165|Done|Bug|Nag Malluru|null||2026-06-09|2026-06-10
SALES-9174|Done|Task|Michael Criswell|null||2026-06-10|2026-06-10
SALES-9175|Done|Story|Jummy Sanni|null|NeedsAcceptanceCriteria,SRT-Product,salesforce|2026-06-10|2026-06-10
SALES-9177|Done|Story|Nag Malluru|null||2026-06-10|2026-06-10
SALES-9185|Done|Spike|Jummy Sanni|null|SRT-Product|2026-06-10|2026-06-10
"""


def build_issues():
    issues = []
    for line in SPRINT_ISSUES_RAW.strip().split("\n"):
        parts = line.split("|")
        key, status, itype, assignee, points, labels, created, resolved = parts
        labels_list = [l.strip() for l in labels.split(",") if l.strip()] if labels else []
        issues.append({
            "key": key,
            "fields": {
                "summary": key,  # placeholder; generator uses key
                "status": {"name": status},
                "issuetype": {"name": itype},
                "assignee": {"displayName": assignee} if assignee else None,
                "customfield_10016": float(points) if points and points != "null" else None,
                "customfield_10142": None,
                "labels": labels_list,
                "created": created + "T12:00:00.000-0700",
                "resolutiondate": resolved + "T12:00:00.000-0700" if resolved else None,
            }
        })
    return issues


if __name__ == "__main__":
    issues = build_issues()
    out_json = Path("/workspace/data/sprint-5-28-6-10.json")
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w") as f:
        json.dump(issues, f, indent=2)
    print(f"Wrote {len(issues)} issues to {out_json}")

    # Patch summaries from known data
    SUMMARIES = {
        "SALES-8550": "Bump Controller classes from API Version 54 to 65 - Ticket 2 of 2",
        "SALES-8551": "Bump Batch classes from API Version 54 to 66 - Ticket 1 of 2",
        "SALES-8552": "Bump Batch classes from API Version 54 to 65 - Ticket 2 of 2",
        "SALES-8553": "Bump Mock classes from API Version 54 to 66",
        "SALES-8650": "Update sumo tests regarding Dec 27 warning",
        "SALES-8801": "Identify all fields in Salesforce without a Description",
        "SALES-8918": "Turn on Inbox",
        "SALES-8920": "Update reporting to reflect TRR Price instead of List Price",
        "SALES-8965": "Backfill price differences between SF and Admin",
        "SALES-8966": "T&C Acceptance Tracking",
        "SALES-8968": "May.'26 SUMO Sync Issue",
        "SALES-8978": "Integration Landscape and Data Flow Diagrams",
        "SALES-9024": "Q2 Incentive Changes Deployment Placeholder",
        "SALES-9028": "Real Partners W-9 Link Errors",
        "SALES-9043": "SUMO Service Rooms",
        "SALES-9046": "Real Partners: Two referral records being created when a RP Consignor signs up through Affiliate link",
        "SALES-9047": "Research how we can create conversational consignor summaries",
        "SALES-9060": "Review and Categorization of Remaining Zendesk Tickets",
        "SALES-9067": "SGO LWC: Referral Not Saving for Certain Users",
        "SALES-9068": "OpportunityTriggerHelper.populateMatchedAdvocateContact | Missing Contact.Owner from SOQL",
        "SALES-9069": "SumoEmailScheduler.getConsignor | consignor not found. Appt Id: XXXX",
        "SALES-9070": "CLONE - Summer 26 Release | Vendor Bulk Upload",
        "SALES-9071": "Related Real Partner Not Tagging on New Referral Records",
        "SALES-9072": "Deployer Access for Salesforce-CRM Repo - May 2026",
        "SALES-9073": "6/1/26 - 6/8/26 Cohorts",
        "SALES-9074": "[UNABLE_TO_LOCK_ROW] SFDC Error Developer script exception from The RealReal",
        "SALES-9078": "Review and Rationalization of Salesforce Distribution Lists",
        "SALES-9079": "Phishing-Resistant Multi-Factor Authentication (MFA) for Privileged Users, including Admins",
        "SALES-9080": "Backfill Consignment_Order_Item__c.Available_Date__c from 05/06 until 05/27",
        "SALES-9081": "Consignment First Available Date Inaccuracies",
        "SALES-9082": "June: Campaign Member Uploads",
        "SALES-9083": "Add a realreal.com Authorized Email Domain in Production",
        "SALES-9084": "SFMC email: Consignment Received with Item List Summary Email Sent",
        "SALES-9085": "ZD Tickets: 5/28 - 6/10",
        "SALES-9086": "Nag - Zendesk Bucket - 05/28-6/10",
        "SALES-9087": "Zendesk 5/28 Sprint",
        "SALES-9088": "Zendesk Tickets 5/28-6/10",
        "SALES-9089": "CI/CD pipeline breaking because of Enabling Deliverability Substitute Email step",
        "SALES-9105": "Alex Zendesk Ticket 5/28 - 6/10",
        "SALES-9106": "Salesforce | Accept referral_code and advocate_user_id on inquiry platform event",
        "SALES-9109": "June Sales Quota uploads",
        "SALES-9110": "Upload Double Point Matrix and Point Matrix new uploads",
        "SALES-9114": "Send 5th of Month CSVs to Real Partners Marketing Team",
        "SALES-9115": "Zendesk Bug Ticket Holder (May 28 - June 10)",
        "SALES-9119": "Change deploy-to-staging skill to be able to deploy to any sandbox",
        "SALES-9124": "Migrate sfConvertLeadSumoCal.test.js to use new createSGOLead method",
        "SALES-9127": "Fix COI Comp Flow to only trigger if New Consignor Multiplier changes and Available Date is populated",
        "SALES-9134": "Backfill for the bug in Production for comp",
        "SALES-9142": "Duplicate COIs",
        "SALES-9145": "Remove Data Mask package",
        "SALES-9165": "Hellosign contract Signature is not displaying properly on iPad",
        "SALES-9174": "CLONE - Backfill AUR_Contributing_Price__c field",
        "SALES-9175": "CLONE - Create SUMO Calendar Knowledge Article",
        "SALES-9177": "CLONE - Technical Design for Outreach Optimization",
        "SALES-9185": "CLONE - SMS/Phone Automation",
    }
    for issue in issues:
        issue["fields"]["summary"] = SUMMARIES.get(issue["key"], issue["key"])

    with open(out_json, "w") as f:
        json.dump(issues, f, indent=2)

    # Run generator
    sys.path.insert(0, str(Path(__file__).parent))
    from generate_sprint_retro import generate_report
    generate_report(issues, "/workspace/reports/sprint-retro-2026-06-19.md")
