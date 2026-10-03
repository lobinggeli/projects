# Swiss Car Import Cost Calculator (EU/EFTA → CH, Used Cars)

Use this skill to calculate the total landed cost of importing a used car from the EU/EFTA into Switzerland.

---

## Step 1 — Gather Parameters

Before calculating, collect:

| Parameter | Details |
|-----------|---------|
| **Purchase price** | Amount + currency (EUR, GBP, etc.) |
| **Seller type** | Private individual or registered dealer |
| **Country of purchase** | Determines local VAT rate and proof-of-origin docs |
| **Transport method** | Self-drive, hire a driver, or transport company |
| **Transport cost** | Estimated CHF amount to the Swiss border |
| **EUR/CHF rate** | Use current spot rate; warn user of ±2–3% bank spread |
| **Canton of registration** | Determines annual road tax |

---

## Step 2 — Purchase Price Adjustment

### Dealer purchase
EU dealers can issue an **export/VAT-free invoice** when the car leaves the EU permanently. If so:
- Deduct the local VAT from the list price (buyer pays Swiss VAT instead)
- Confirm with the dealer they can issue a VAT-exempt export invoice

**Common EU VAT rates:**
| Country | VAT rate |
|---------|----------|
| Germany (DE) | 19% |
| France (FR) | 20% |
| Italy (IT) | 22% |
| Austria (AT) | 20% |
| Netherlands (NL) | 21% |
| Belgium (BE) | 21% |
| Spain (ES) | 21% |

Net export price = List price ÷ (1 + local VAT rate)

### Private purchase
No VAT to reclaim. Swiss VAT is applied on the full purchase price.

### Currency conversion
CHF equivalent = Purchase price (EUR) × spot rate
> Flag: banks and brokers apply a 1–3% spread over mid-market rate. For large amounts, use a currency broker (Wise, Revolut, etc.) to save hundreds of CHF.

---

## Step 3 — Swiss Import Taxes

**CIF value** (customs value) = CHF purchase price + transport to Swiss border

| Tax | Rate | Basis | Notes |
|-----|------|-------|-------|
| **Customs duty** | **0%** | CIF value | Applies when car has proof of EU/EFTA origin (EUR.1 form or invoice declaration). Without proof: weight-based duty ~CHF 6–15 per 100 kg net weight |
| **Swiss VAT (MWST/TVA)** | **8.1%** | CIF value | Always applies |
| ~~Automobile tax~~ | n/a | — | Only applies to **new cars**. Not levied on used car imports. |

**Critical document:** Request an **EUR.1 movement certificate** or **invoice declaration** from the EU seller to prove EU origin and qualify for 0% customs duty.

### Import tax calculation
```
CIF value                    CHF XX,000
× 8.1%  Swiss VAT            CHF  X,XXX
──────────────────────────────────────
Total import taxes           CHF  X,XXX
```

---

## Step 4 — Homologation (Type Approval)

| Situation | Action | Cost |
|-----------|--------|------|
| EU-spec car with EU e-mark type approval | Accepted by Swiss authorities with minimal checks | CHF 0–200 |
| Minor modifications needed (fog lamp, DRL, speedometer) | Workshop adjustment | CHF 100–500 |
| Non-EU spec (US, JDM) | Full individual approval (Einzelgenehmigung) — **out of scope** | CHF 800–2,000+ |

For most EU imports, budget **CHF 0–300** for any homologation adjustments.

---

## Step 5 — Swiss Registration (Immatriculation)

| Item | Cost |
|------|------|
| MFK (technical inspection / contrôle technique) | CHF 100–200 |
| Number plates | CHF 30–50 |
| Registration document (Fahrzeugausweis) | CHF 50–100 |
| **Registration subtotal** | **~CHF 200–350** |

### Annual cantonal road tax (indicative, varies by engine/CO2/weight)

| Canton | Annual range |
|--------|-------------|
| Zug (ZG) | CHF 200–400 |
| Schwyz (SZ) | CHF 200–450 |
| Geneva (GE) | CHF 300–800 |
| Vaud (VD) | CHF 400–900 |
| Zurich (ZH) | CHF 300–700 |
| Bern (BE) | CHF 350–800 |

> Use the canton's official motor vehicle office (Strassenverkehrsamt / Office des automobiles) website for exact rates — they depend on engine displacement, CO2 emissions, and vehicle weight.

---

## Step 6 — Total Cost Summary

Present results in this format:

```
PURCHASE
  Purchase price (local)         EUR XX,000
  – EU VAT reclaim (if dealer)   – EUR  X,XXX    (÷ 1.19 for DE, ÷ 1.20 for FR…)
  = Net export price             EUR XX,000
  × EUR/CHF rate                 × 0.9X
  = CHF purchase price           CHF XX,000

TRANSPORT
  + Transport to CH border       CHF    XXX

  = CIF value (customs base)     CHF XX,000

SWISS IMPORT TAXES
  + Swiss VAT (8.1%)             CHF  X,XXX
  + Customs duty                 CHF      0      (0% with EUR.1 proof)

REGISTRATION
  + Homologation (if needed)     CHF    0–300
  + MFK + plates + doc           CHF   ~300

══════════════════════════════════════════
  TOTAL LANDED COST              CHF XX,000
══════════════════════════════════════════

  Annual road tax ([Canton])     CHF XXX–XXX / year  (not included above)
  Insurance                      not included — arrange before MFK
```

---

## Common Pitfalls

- **No EUR.1 certificate**: Without proof of EU origin, customs duty applies (small but avoidable)
- **Dealer won't do export invoice**: Some dealers refuse — factor in full local VAT if so
- **Bank FX spread**: On EUR 30k, a 2% spread = CHF 600 lost. Use a currency broker.
- **Automobile tax uncertainty**: Some sources omit it for private imports. Confirm via BAZG or a customs agent before finalizing budget.
- **Insurance required before MFK**: You cannot legally drive to MFK without Swiss plates/insurance. Arrange temporary plates (Händlerschilder) or transport the car.
- **Cantonal road tax varies widely**: Zug is ~4× cheaper than Vaud for the same car.
