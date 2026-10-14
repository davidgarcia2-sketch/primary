# Examples

Illustrative only. The requests are invented.

## Stage 1: Intake

**PM input:** "Sales reps should be able to text customers from Salesforce instead of using their phones."

**Response:**

**Stage:** Intake
**Request type:** Tool or Channel Switch, likely New Integration
**Size:** M–L · **Confidence:** low
**Why this size:** Texting from Salesforce needs an SMS provider connected to Salesforce, message logging on records, and opt-out handling. Replacing a current tool adds parity work.

**What could change it**
- If we already license an SMS product that plugs into Salesforce and only need setup for one team, this drops to S.
- If reps need to see or reply to past texts from their phones, this moves to L.
- If texting must also update opportunity stages or dispositions automatically, add roughly a size.

**Questions to take to stakeholders**
1. Is this replacing a tool reps use today, or adding one? Which tool? — Sales ops
2. Which teams and roughly how many reps? — Sales leadership
3. What must work on day one: logging, templates, opt-outs, stage updates? — Sales ops
4. Do reps need history from texts already sent? — Sales leadership
5. Are there legal or compliance rules for texting customers (consent, quiet hours)? — Legal
6. Do any reports or dashboards need to show text activity? — RevOps

**Risks with what we know today**
- Customer consent and opt-out rules can add compliance work.
- "Instead of their phones" implies parity with personal texting, which may not be possible.

**Next step:** Answer questions 1–3 and we can narrow this to one size.

## Stage 3: Requirements review (excerpt)

**PM input:** a story titled "SMS improvements" with AC "Texting works for all reps."

**Response:**

**Stage:** Requirements review
**Verdict:** Needs changes
**Size check:** M stays, confidence medium. Unchanged until the provider is named.

**Must fix before engineering**
- Title: "SMS improvements" is a placeholder → "Let Retail reps send and log customer texts from Contact records".
- Scope: does not say what stays the same → add "Personal phone texting is not blocked or monitored."
- Dependencies: provider is unnamed → "TBD — decision needed from Sales Ops: SMS provider."

**Acceptance criteria review**
- "Texting works for all reps" → rewrite: "Given a Retail rep on a Contact with an opted-in mobile number. When the rep sends a text. Then the message is delivered and logged on the Contact activity timeline."
- Missing: edge case (no mobile number), negative test (opted-out contact), rollback.
