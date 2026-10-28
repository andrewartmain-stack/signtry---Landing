# SignTry pricing spec (for the dashboard + Stripe)

Source: the public pricing page https://signtry.com/pricing.html (generated from `TIERS` in `tools/site/p_pricing.py` in the landing repo). The dashboard and Stripe must match these numbers and promises exactly.

## Model

- **Subscription only.** No one-time purchases, no free paid-feature tier.
- **Priced by signature quota.** A plan = the maximum number of signatures an account can have. No per-seat pricing, no seat minimums.
- **Every feature on every plan.** Plans differ only in signature quota and price.
- **Two billing periods:** monthly, or yearly (about 25% cheaper, billed once a year).
- **Currency:** USD, prices exclude tax.

## Plans

| Plan (signatures) | Yearly: shown per month | Yearly: charged per year | Monthly: charged per month | Per signature (yearly) |
|---|---|---|---|---|
| 1 | $3 | **$36** | **$4** | $3.00 |
| 5 | $7 | **$84** | **$10** | $1.40 |
| 10 | $10 | **$120** | **$14** | $1.00 |
| 25 | $22 | **$264** | **$29** | $0.88 |
| 50 | $39 | **$468** | **$52** | $0.78 |
| 100 | $69 | **$828** | **$92** | $0.69 |
| 250 | $149 | **$1,788** | **$199** | $0.60 |
| 500+ | Custom | Custom | Custom | Volume pricing |

500+ is sales-led: the site links to `mailto:support@signtry.com?subject=SignTry%20for%20500%2B%20signatures` and promises volume pricing, invoice billing, help importing the team and priority support. Not self-serve.

## What counts as a signature (as stated on the site)

- One signature = one finished design for one person (e.g. "Jane Cooper, Head of Sales").
- Editing a signature is unlimited and free; it does not use up quota.
- A teammate with their own details is another signature.
- Quota = number of saved signatures on the account (CSV bulk generation counts one per row created).

## Features included on every plan (promised on the site)

- All templates (all industries and layouts)
- Bulk generation from a CSV ("For my team")
- Link-click analytics dashboard (per month, last 7 days, per link, per signature, monthly goal)
- Verified badge, photo, company logo, banner, handwritten signature
- Booking / call-to-action button, social icons
- Hosted, optimized images
- Copy signature + HTML code export
- Works in Gmail, Outlook, Apple Mail, Yahoo Mail and others
- Unlimited edits

Do not gate any of these by plan.

## Account and billing rules (promised on the site)

- Sign-up needs **no credit card**; users can start building before paying. (What an unpaid user can do inside the app is not defined yet. See open decisions.)
- Users can **change plan size at any time** from **Billing** in the dashboard.
- **Cancel any time**; access continues until the end of the paid period.
- Payment by card through **Stripe**.
- Yearly billing is labelled **"Save 25%"** on the site.

## Suggested Stripe setup

- One Product: `SignTry`.
- 14 recurring Prices (7 sizes × 2 periods), each with:
  - `lookup_key`: `sig_{n}_month` / `sig_{n}_year` (e.g. `sig_25_year`)
  - `metadata.signature_limit`: `1`, `5`, `10`, `25`, `50`, `100`, `250`
  - `unit_amount` in cents from the table above (e.g. `sig_25_year` = 26400, `sig_25_month` = 2900)
- Read the quota from the active subscription price's `metadata.signature_limit`, not from hard-coded amounts.
- Plan changes: `subscriptions.update` swapping the price. Proration behaviour is not promised on the site, so pick one (Stripe default proration is fine).
- Use Stripe Checkout for new subscriptions and the Customer Portal for card updates, invoices and cancellation.
- Webhooks to handle at minimum: `checkout.session.completed`, `customer.subscription.created|updated|deleted`, `invoice.paid`, `invoice.payment_failed`.

## Quota enforcement

- Block creating or generating signatures beyond `signature_limit` and show an upgrade prompt to the next size.
- CSV import: if rows > remaining quota, show how many fit and offer the plan that covers all rows.
- Downgrade below current usage: decide whether to block it until signatures are deleted, or keep extras read-only.

## Legacy pricing (old site, must be migrated or grandfathered)

| Old plan | Price | Limit |
|---|---|---|
| Single Signature | $10 one-time (Stripe Payment Link `https://buy.stripe.com/cNi6oGeER2vo0NU1Ng93y00`) | 1 signature, lifetime |
| Basic | $9/month, or $6.30/month billed yearly ($75.60) | up to 5 signatures |
| Professional | $29/month, or $20.30/month billed yearly ($243.60) | up to 50 signatures, "advanced analytics", priority support |

The website no longer links to the one-time Payment Link. Deactivate it in Stripe once existing buyers are handled.

## Open decisions

1. What a signed-up but unpaid user can do (build and preview only? one saved draft?).
2. What happens to existing $10 one-time buyers and Basic/Professional subscribers (grandfather or migrate).
3. Downgrade below current signature count: block or read-only.
4. Proration on upgrade and downgrade.
5. Free trial length, if any (the site doesn't promise one).
