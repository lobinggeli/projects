# Swiss Mortgage Law & Financing Framework

Use this framework to understand the *legal* machinery behind Swiss property financing — the security instrument that makes mortgages possible, the regulatory rules that constrain what banks can lend, and what happens legally if a loan goes into default. This complements the practical financing rules in [Swiss Property Purchase Fundamentals](swiss-property-purchase-fundamentals.md).

## Core Concept

Swiss mortgage lending is **not primarily governed by a "mortgage law" in the way common-law systems have one** — it rests on three separate legal layers that combine:

```
Swiss Property Financing — Three Legal Layers

[1. Security instrument]      [2. Lending rules]        [3. Default mechanism]
Cédule hypothécaire           FINMA-recognized SBA       Poursuite en réalisation
(Swiss Civil Code             self-regulation             de gage (SchKG/LP
Art. 842–865)                 (not statute — quasi-       Art. 151–158)
= the pledge + the debt       binding minimum
  in one registered title      standards)
```

Layer 1 is what makes the loan enforceable against the property. Layer 2 is what determines how much you can actually borrow (covered in depth in the Fundamentals skill; this file adds the regulatory *source* of those rules). Layer 3 is what happens if you stop paying.

## When to Apply

- You want to understand what a **cédule hypothécaire** actually is when your notary or bank mentions it
- You're comparing **fixed-rate vs. SARON** mortgage structures
- You want to understand why banks enforce the 20%/10%-hard-equity and 15-year amortization rules even though they aren't written in a statute
- You want to understand the legal consequence of missing mortgage payments (what a bank can and can't do)
- You're negotiating mortgage note terms with a notary or bank and want to know your legal position

## The Security Instrument: Cédule Hypothécaire

**Legal basis**: Swiss Civil Code (Code civil / ZGB), **Articles 842–865**.

**What it is**: a hybrid instrument that combines (a) a **personal debt claim** against the borrower with (b) a **real property pledge** securing it, registered in the Land Registry (Registre foncier). Unlike a simple mortgage registration, the cédule is itself a transferable title.

**Two forms**:
| Form | Description |
|---|---|
| **Register cédule** (cédule hypothécaire de registre) | Exists only as an electronic entry in the Land Registry — no physical paper document; nominative only (cannot be a bearer instrument) |
| **Paper cédule** (cédule hypothécaire sur papier) | Physical certificate; can be issued to a named holder (nominative) or to bearer |

**Why banks prefer it over a simple registered loan**: the cédule is flexible and reusable — it isn't tied to one specific loan. A bank can hold a CHF 800,000 cédule against your property and use it to secure a current mortgage, then later re-use the same cédule (partially or wholly) to secure a refinanced or additional loan, without a fresh Land Registry transaction each time. If you switch banks, the cédule can often be transferred/assigned rather than re-created — though this involves its own notary and registration steps.

**Vendor's statutory lien** (hypothèque légale du vendeur, **Art. 837 CC**): a seller who hasn't been fully paid gets an automatic legal pledge right over the property for a limited period post-sale — relevant mainly in seller-financed or staged-payment transactions, rarely in a standard bank-financed purchase.

**Practical note**: setting up or transferring a cédule requires a notarized deed and Land Registry registration — this is part of why closing costs include a "mortgage note setup fee" (see [Vaud Property Market & Buying Guide](vaud-property-market-buying-guide.md) for the cost breakdown).

## The Lending Rules: FINMA-Recognized Self-Regulation

**Critical distinction**: the 20% equity / 10% hard-equity / 15-year amortization rules are **not written into a federal statute**. They come from **Swiss Bankers Association (SBA) guidelines**, which FINMA (the Swiss financial regulator) has formally **recognized as minimum supervisory standards** for regulated banks. This makes them binding in practice on every FINMA-supervised lender, even though a private lender or non-bank financing arrangement is not legally bound by them the same way.

**The two governing SBA/FINMA guideline sets**:
1. **Guidelines on minimum requirements for mortgage loans** — the equity and amortization rules
2. **Guidelines on assessing, valuing and processing loans secured against property** — how banks must value collateral and process applications

**Key standards currently in force**:
- Minimum **20% equity**, of which **at least 10 percentage points must be "hard" equity** (savings, securities, gifts, pillar 3a) — pension fund (2nd pillar) money cannot cover more than the remaining 10 points.
- **Owner-occupied property**: amortize the 2nd mortgage tranche (above 65% loan-to-value) down to two-thirds LTV **within 15 years**.
- **Investment/rental property**: tightened in **2019** — amortize to two-thirds LTV within a **shorter window (moving toward 10 years)**, reflecting higher risk tolerance concerns for buy-to-let financing.
- **Basel III Final** implementation (ongoing through the mid-2020s) has prompted further SBA adjustments to capital treatment of mortgage risk-weighting, which indirectly affects how aggressively banks price and ration mortgage credit — this is a live area to check with your bank/broker rather than treat as fixed.

**Why this matters practically**: because these are self-regulatory standards enforced via FINMA recognition rather than hard statute, a bank has some discretion at the margins (e.g., exact affordability stress-test assumptions, treatment of bonus income, willingness to lend to self-employed borrowers) even while the core 20%/10%/15-year skeleton is effectively universal across licensed banks.

## Interest Rate Structures

| Structure | How it works | Indicative rate band, 10-yr CHF 750k loan (Sept 2026) |
|---|---|---|
| **Fixed-rate mortgage** | Rate locked for the term (often 2–10+ years); payment certainty, early-exit penalties can be significant | ~1.55%–2.15% |
| **SARON mortgage** | Floating, tracks the Swiss Average Rate Overnight (replaced LIBOR); recalculated continuously, payment can move up or down through the term | ~0.70%–1.20% |

**Context (September 2026)**: the SNB policy rate has been held at **0.0%** through its fourth consecutive review (18 June 2026), keeping SARON pricing well below fixed rates — though the spread between SARON and fixed has **narrowed** materially in 2026, meaning the "security premium" for locking a fixed rate is cheaper than it has been in recent years. This is a live market condition, not a structural rule — re-check current spreads when actually pricing a mortgage.

**Early repayment**: breaking a fixed-rate mortgage before term-end typically triggers a penalty (prépaiement/Vorfälligkeitsentschädigung) calculated on the bank's reinvestment loss — this can be substantial in a falling-rate environment. SARON mortgages are generally more flexible to exit but expose you to rate variability.

## Default & Enforcement: Poursuite en Réalisation de Gage

**Legal basis**: Federal Debt Enforcement and Bankruptcy Act (LP/SchKG), **Articles 151–158**, specifically the pledge-realization procedure (as opposed to ordinary debt enforcement, which targets unsecured claims).

**Three governing principles**:
1. **Specialty (spécialité)**: the enforcement action is limited to the pledged property itself — the creditor's pledge-based claim is satisfied from that asset.
2. **Priority (priorité)**: pledge-holders are paid in rank order (first mortgage/cédule ranks ahead of a second, etc.) from the sale proceeds.
3. **Accessoriness (accessorité)**: the pledge right is legally tied to the underlying debt — if the debt is extinguished or transferred, the pledge follows it.

**Jurisdiction**: the competent debt enforcement office (office des poursuites) is the one where the property is physically located — relevant if you own property in a different canton from your residence.

**Creditor (bank) rights in this procedure**:
- **Preferential claim** on the sale proceeds ahead of unsecured creditors.
- Right to request **early/anticipated realization** of the pledge if the property's value is depreciating (protecting the creditor from further collateral erosion during a drawn-out process).
- Participation rights in decisions about managing or realizing the encumbered property during the procedure.

**Practical sequence if a borrower defaults**: missed payments → bank issues formal notice/reminder → continued default triggers a formal debt enforcement filing (réquisition de poursuite) specifically in the pledge-realization track → if unresolved, the office des poursuites proceeds toward a forced sale (vente aux enchères) of the property, with proceeds distributed by creditor rank. This is a multi-month, formally staged legal process — not an immediate seizure — but it is a real and enforceable outcome, and interest/penalties continue accruing throughout.

## Common Pitfalls

**Confusing the cédule hypothécaire with the loan itself.** The cédule is the *security title*; the actual loan agreement (credit contract) with the bank is separate. You can have one cédule securing a loan that later gets refinanced or restructured without re-issuing the cédule.

**Treating SBA/FINMA lending guidelines as negotiable "bank policy."** They function as hard minimums across regulated banks precisely because FINMA recognizes them as supervisory standards — shopping between banks will not find you a licensed lender willing to go below 20%/10% equity in normal circumstances (non-bank or specialty financing is a different, higher-risk conversation).

**Ignoring early-repayment penalty exposure when choosing fixed-rate terms.** A long fixed term feels safe but can be expensive to exit if your plans change (sale, refinance) — model the penalty scenario before locking a 10-year fixed rate.

**Assuming default leads to instant loss of the property.** The pledge-realization procedure (Art. 151–158 LP) is a formal, staged legal process with defined steps — but it is also a real and eventually enforceable path to forced sale, so missed-payment situations should be addressed with the bank early (restructuring, payment holiday) rather than left to run.

## Limitations

This is an educational overview of the legal and regulatory architecture, not legal or financial advice. SBA/FINMA self-regulation standards, Basel III implementation details, and current interest rate levels all change — verify current terms with your bank, a mortgage broker, and (for the security instrument and enforcement mechanics) a notary or lawyer before relying on specifics here for an actual transaction or default situation.

---

**Use in conjunction with**:
- [Swiss Property Purchase Fundamentals](swiss-property-purchase-fundamentals.md) — practical financing/affordability rules this framework's Layer 2 produces
- [Vaud Property Market & Buying Guide](vaud-property-market-buying-guide.md) — notary/registration costs for setting up a cédule
- [Renovation Tax Deductions in Switzerland](renovation-tax-deductions-switzerland.md) — how renovation spending interacts with mortgage interest deductibility

**Sources**:
- [Wikipédia — Cédule hypothécaire](https://fr.wikipedia.org/wiki/C%C3%A9dule_hypoth%C3%A9caire)
- [Hausinfo — Cédule hypothécaire, hypothèque et contrat de gage](https://hausinfo.ch/fr/financer-acheter/financement-propriete-logement/financement-propriete-fonds-propres-etrangers/hypotheques/cedule-hypothecaire-contrat-de-gage.html)
- [État de Vaud — Les gages immobiliers](https://www.vd.ch/fileadmin/user_upload/organisation/dfin/sg-dfin/rf/fichiers_pdf/Gages_immobiliers.pdf)
- [Juriup — Hypothèque légale du vendeur (Art. 837 CC)](https://juriup.ch/terme-juridique/hypotheque-legale-du-vendeur/)
- [FINMA — Mortgages for investment properties: self-regulation adjustments (2019)](https://www.finma.ch/en/news/2019/08/20190828-mm-selbstregulierung/)
- [FINMA — Mortgage financing: new minimum standards (2012)](https://www.finma.ch/en/news/2012/06/mm-hypo-richtlinien-20120601/)
- [UBS — How much equity for a house purchase](https://www.ubs.com/ch/en/services/guide/mortgages-and-financing/articles/how-much-equity-for-house-purchase.html)
- [Swiss Bankers Association — Basel III Final: self-regulation updates](https://www.swissbanking.ch/en/media-politics/news/basel-iii-final-sbvg-passt-selbstregulierungen-im-hypothekarbereich-an)
- [Droit pour la pratique — Saisie et poursuite en réalisation du gage](https://droitpourlapratique.ch/subtheme/saisie-et-poursuite-en-realisation-du-gage)
- [PBM Avocats — Poursuite en réalisation de gage](https://www.pbm-avocats.ch/poursuite-realisation-gage/)
- [UBS — Taux hypothécaires actuels](https://www.ubs.com/ch/fr/services/mortgages-and-financing/mortgages/interest-rates.html)
- [Comparis — Baromètre des hypothèques 2026](https://en.comparis.ch/hypotheken/hypothekarzinsen/hypobarometer)

**Framework version**: 1.0 (September 2026) — interest rate figures are a snapshot; re-check current spreads before pricing a mortgage.
