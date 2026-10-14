# Drafting rules

Snapshot of the Google Doc [AI Drafting Guidance](https://docs.google.com/document/d/1HUJuwzSjrgVWlrkaWnfARzWNCz21KCI_gdTnvvx5L7M). These apply at every stage.

1. **One ticket, one task.** If the request asks for more than one distinct piece of work, say so, name each task, and suggest a title and scope for each. Never blend two tasks into one answer.
   - Example: "grant access to these users" (do it now) and "make access automatic in the future" (design problem: permission set groups, title or department rules, SailPoint, a Freshservice exception flow) are two tickets. The second starts as a spike.
2. **Separate the now from the forever.** An immediate action gets an owner and a quick path. Ongoing process change is scoped on its own, even if it starts as a spike.
3. **State unknowns as unknowns.** Missing owner, date, number, or field name is written `TBD` or listed as an open question. Never fill gaps with plausible guesses. Label inferences.
4. **Never present discussion as a decision.** Keep decisions, open items with owners, and discussion-only points separate. Commitments capture who, what, and when; a missing date is written "date TBD".
5. **Copy identifiers exactly.** Ticket keys, Salesforce object and field names, API names, and versions are copied, never reconstructed.
6. **Flag work that is not sprint-ready.** If requirements are undefined or the design is still open, do not draft a solution that implies readiness. Recommend a spike to work out the approach.
7. **Push abstract criteria to concrete system fields.** "Anyone who joins Adam's team" is not implementable until someone names the Salesforce structure that enforces it (title, department, role, call center). Ask which one, or say no one has defined it.
8. **Newest info wins, flag conflicts.** When sources disagree, report the latest and note that it changed. Never quietly pick a side.

## Additions for this skill

9. **Size honestly.** The range width must match the confidence in [sizing.md](sizing.md). Say what would narrow it.
10. **No story points.** T-shirt sizes only. Story points belong to engineering after requirements are locked.
11. **Plain language for PMs.** Explain technical risks in business terms ("past commission payouts may need recalculating"), and keep Salesforce jargon to what the PM needs to repeat to a stakeholder.
