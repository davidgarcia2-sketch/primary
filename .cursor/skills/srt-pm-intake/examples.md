# Examples

Illustrative only. The requests are invented.

## Stage 1: Intake

**PM input:** "Sales reps should be able to text customers from Salesforce instead of using their phones. Add a Send SMS button on the Contact page."

**Response:**

**Stage:** Intake
**Request type:** Tool or Channel Switch
**The need:** Reps want to text customers without leaving Salesforce, so conversations are visible to the team instead of living on personal phones.
**Size:** M–L · **Confidence:** low
**Why this size:** A new communication channel for a whole sales team, with customer consent rules, and possibly replacing a tool reps already rely on.

**What could change it**
- If it is for one small team and nothing is being replaced, this drops to S.
- If reps need their past texts brought over, this moves to L.

**Questions to take to stakeholders**
1. Is this replacing a tool reps use today, or adding one? — Sales Ops — replacing means day-one parity, which can add a size.
2. Do reps need history from texts already sent? — Sales leadership — bringing old messages over moves this to L.
3. Which teams, and roughly how many reps? — Sales leadership — one team versus all of Sales is the difference between S and M.

**Engineering will confirm**
- Whether we already license a texting product that works with Salesforce.

**Solution check**
- "Add a Send SMS button on the Contact page" → the need: reps can text a customer while looking at that customer's record. Engineering will decide how.

**Risks with what we know today**
- Customer consent and opt-out rules can add compliance work.

**Next step:** Answer questions 1 and 3 and we can narrow this to one size.

## Stage 3: Requirements review (excerpt)

**PM input:** a story titled "SMS improvements". Scope says "Create a Flow that logs each text as a Task and add an Opted_Out checkbox to Contact." AC: "Texting works for all reps."

**Response:**

**Stage:** Requirements review
**Verdict:** Needs changes
**Size check:** M stays, confidence medium.

**Solution check**
- Scope: "Create a Flow that logs each text as a Task" → rewrite as: "Every text sent or received is visible on the customer's record to anyone who can see that customer." (Describes what people see, not how it is stored.)
- Scope: "add an Opted_Out checkbox to Contact" → rewrite as a business rule: "Customers who opt out of texts are never texted." (Engineering decides how opt-out is tracked.)

**Must fix before engineering**
- Title: "SMS improvements" is a placeholder → "Let Retail reps text customers from Salesforce with conversations visible on the customer record".
- Scope: does not say what stays the same → add "Personal phone texting is not blocked or monitored."

**Acceptance criteria coaching**
- "Texting works for all reps" → rewrite: "Given a Retail rep viewing a customer who has agreed to texts. When the rep sends a text. Then the customer receives it and the rep's teammates can see it on that customer's record." (Pass/fail, and describes what people observe.)
- Missing: edge case (customer with no mobile number), negative test (customer who opted out), rollback.

**Open TBDs for stakeholders**
- Which teams get texting at launch — Sales leadership

**Engineering will confirm**
- Whether an existing licensed product covers this.
