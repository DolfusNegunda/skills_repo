# Worked Example: Contract Excerpt → Summary, Risks, and Q&A

This example shows the expected output shape for a contract review: an
executive summary, a risks/obligations table with clause anchors, and grounded
answers to targeted questions — including one the document does not answer.

## Input: contract excerpt provided by the user

> **MANAGED IT SERVICES AGREEMENT**
> between **Northgate Logistics Ltd** ("Customer") and **Corvid Systems Inc.**
> ("Provider"), effective 1 March 2026.
>
> **3. Term.** Initial term of twenty-four (24) months. This Agreement renews
> automatically for successive twelve (12) month periods unless either party
> gives written notice of non-renewal at least ninety (90) days before the end
> of the then-current term.
>
> **4. Fees.** Customer shall pay a monthly service fee of USD 18,000, invoiced
> monthly in advance, payable within thirty (30) days. Provider may increase
> fees once per renewal term by no more than five percent (5%) on sixty (60)
> days' written notice. Late amounts accrue interest at 1.5% per month.
>
> **6. Service Levels.** Provider shall maintain 99.5% monthly uptime for the
> Hosted Services. For each full 0.5% below the target, Customer receives a
> service credit of 5% of that month's fee, capped at 20% of the monthly fee.
> Service credits are Customer's sole remedy for availability failures.
>
> **8. Liability.** Neither party's aggregate liability shall exceed the fees
> paid in the twelve (12) months preceding the claim, except for breaches of
> Section 10 (Confidentiality), which are capped at three (3) times that amount.
>
> **9. Termination.** Either party may terminate for material breach uncured
> within thirty (30) days of written notice. Customer may terminate for
> convenience on one hundred eighty (180) days' notice, subject to an early
> termination fee equal to fifty percent (50%) of the fees remaining in the
> then-current term.
>
> **10. Confidentiality.** Each party shall protect the other's Confidential
> Information for five (5) years after termination.

## Output 1: executive summary (one-paragraph, as requested)

This is a 24-month managed IT services agreement between Northgate Logistics
(Customer) and Corvid Systems (Provider), effective 1 March 2026, at USD 18,000
per month (§4). It auto-renews in 12-month increments unless either party gives
90 days' non-renewal notice (§3), and exiting early for convenience costs 180
days' notice plus 50% of the remaining term's fees (§9). Liability is capped at
12 months of fees — raised to 3x for confidentiality breaches (§8) — and the
99.5% uptime commitment is backed only by service credits capped at 20% of a
month's fee, stated as the sole remedy for availability failures (§6).

## Output 2: key risks and obligations

| Who | What | When / trigger | Or else | Where |
| --- | --- | --- | --- | --- |
| Customer | Give non-renewal notice or the contract renews for 12 months | ≥90 days before term end | Locked into another year | §3 |
| Customer | Pay USD 18,000/month, invoiced in advance | Within 30 days of invoice | 1.5%/month interest on late amounts | §4 |
| Provider | May raise fees up to 5% per renewal term | 60 days' notice | Budget exposure at each renewal | §4 |
| Provider | Maintain 99.5% monthly uptime | Monthly | Credits of 5% per 0.5% shortfall, capped at 20%; sole remedy | §6 |
| Customer | Early exit for convenience | 180 days' notice | Fee of 50% of remaining term | §9 |
| Both | Protect Confidential Information | 5 years post-termination | Liability up to 3x the 12-month fee cap | §8, §10 |

Points worth flagging:

- **Sole-remedy language (§6)**: service credits, capped at 20% of one month's
  fee, are the only remedy for downtime — even a severe outage yields at most
  USD 3,600.
- **Auto-renewal (§3)**: the 90-day notice window is easy to miss; the
  effective decision date for a term ending 28 Feb 2028 is ~30 Nov 2027.
- **Not addressed in the excerpt**: indemnities, data protection/security
  obligations, assignment restrictions, and governing law do not appear in the
  provided sections. The excerpt may be partial — confirm against the full
  document before relying on their absence.

## Output 3: targeted Q&A

**Q: Can we get out of this contract if the service is bad?**
A: Only through the material-breach route: if Provider materially breaches and
fails to cure within 30 days of written notice, Customer may terminate (§9).
Poor uptime alone is unlikely to qualify easily, because §6 makes service
credits the "sole remedy" for availability failures. Otherwise, exit for
convenience requires 180 days' notice plus 50% of the remaining term's fees
(§9).

**Q: What is the most we could recover if Provider leaks our data?**
A: For breaches of the confidentiality clause (§10), liability is capped at
three times the fees paid in the preceding 12 months (§8) — at the current
USD 18,000/month rate, up to USD 648,000. Note this cap applies to
confidentiality breaches specifically; the excerpt contains no separate data
protection or indemnity clause.

**Q: Which law governs this agreement?**
A: The provided excerpt does not address governing law. No answer can be given
from this document — check the full agreement (governing-law clauses typically
appear in the general/miscellaneous provisions) rather than assuming a
jurisdiction.
