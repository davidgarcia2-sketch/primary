# Solution check

PMs own **what** and **why**. Engineering owns **how**. When requirements prescribe a design, engineering inherits a solution that may not be the best one, and the real need gets lost.

## What counts as a solution

Flag the input when it tells engineering what to build or how the system should do it:

- Names a mechanism: Flow, trigger, Apex, batch job, validation rule, formula, integration pattern, LWC, button, checkbox, new field, new object, new report type, record type, permission set group
- Describes system internals: "when the field updates, a Flow sets X", "add a lookup to Y", "the batch job should check Z"
- Picks a tool or vendor without a stated reason: "use LeanData for this", "build it in Omni"
- Prescribes UI layout: "add a tab with a dropdown on the left"

## What is fine

- Naming **existing** things as context: "the Boosted New Consignor Credit on the rep comp dashboard is wrong for ALRA reps"
- A business rule stated as a fact: "ALRA reps do not receive the 1.5x booster"
- A real constraint with a reason: "must stay in Salesforce because reps are not licensed for other tools"
- A wireframe offered as an illustration of the outcome, labeled as such

## How to restate it

Ask "what would be true for the user or the business if this were built?" and write that.

| PM wrote (solution) | Restated (need) |
|---|---|
| Add a checkbox on Opportunity to exclude it from the booster | Some opportunities should not receive the New Consignor booster. Which ones, and who decides? |
| Create a Flow that emails the manager when a deal closes | Managers need to know when their team closes a deal, within [time]. |
| Add a role picklist on User and check it in the batch job | The booster depends on the rep's role. Which roles get which treatment? |
| Build a report type joining Leads and Activities | RevOps needs to see activity counts per lead by [period]. |
| Make it automatic for anyone on Adam's team | Everyone in [business-defined group] gets this. How is that group defined in business terms (title, department, team)? Engineering will map it to the system. |

## Acceptance criteria

AC describe what a user or the business can **observe**, not what the system does internally.

- Bad: "Given the role field is ALRA, When the batch job runs, Then the booster credit field is not populated." (names a job and a field)
- Good: "Given an ALRA rep closes a new consignor's first shipment, When the rep views their comp credit for that period, Then the credit is shown without the 1.5x booster."

Signs an AC is a solution: it names a field API name to create, a Flow, a job, a component, or a step inside the system. Rewrite it from the point of view of the rep, manager, customer, or report that would notice the difference.

## Tone

Coach, do not scold. One line per item: what they wrote, the need behind it, and that engineering will decide the approach. If a design choice is a real business constraint, ask for the reason and keep it as a constraint.
