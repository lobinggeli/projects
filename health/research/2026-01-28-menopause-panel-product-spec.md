# Menopause Panel Product Specification

**Date:** 2026-01-28
**Version:** 1.0
**Status:** Draft

---

## 1. Panel Overview

### Product Line

| Panel | Price | Biomarkers | Target User | Sample Timing |
|-------|-------|------------|-------------|---------------|
| **Essential Menopause** | €69 | 10 | Post-menopause (12+ months no period) | Any time |
| **Comprehensive Menopause** | €89 | 18 | Post-menopause wanting full picture | Any time |
| **Perimenopause** | €99 | 10 x 2 | Still menstruating, irregular cycles | Day 14 + Day 21 (dual kit) |
| **HRT Monitoring Add-on** | +€29 | 5 | Women on hormone therapy | Per HRT schedule |

---

## 2. Biomarker Panel Design

### Essential Panel (€69) — 10 Biomarkers

| Biomarker | Clinical Rationale | Optimal Range | Flag Threshold |
|-----------|-------------------|---------------|----------------|
| **FSH** | Primary menopause marker | <10 mIU/mL (pre) | >30 = menopause |
| **Estradiol (E2)** | Declining levels cause symptoms | 30-400 pg/mL (pre) | <30 = post-meno |
| **LH** | Ovarian function indicator | 2-15 mIU/mL (pre) | >30 = menopause |
| **Progesterone** | Cycle regularity, HRT monitoring | Varies by cycle day | <0.5 ng/mL post-meno |
| **TSH** | Thyroid dysfunction mimics menopause | 0.4-4.0 mIU/L | >4.0 = investigate |
| **Free T4** | Thyroid function | 0.8-1.8 ng/dL | <0.8 = hypothyroid |
| **Vitamin D** | Bone health (30% osteoporosis post-meno) | 30-50 ng/mL | <20 = deficient |
| **Ferritin** | Fatigue investigation | 30-150 ng/mL | <30 = low iron |
| **HbA1c** | Metabolic risk (insulin resistance rises) | <5.7% | >5.7% = prediabetes |
| **Total Cholesterol** | CV risk (50% increase post-meno) | <200 mg/dL | >240 = high |

### Comprehensive Panel (€89) — 18 Biomarkers

Includes all Essential markers **plus:**

| Biomarker | Clinical Rationale | Optimal Range |
|-----------|-------------------|---------------|
| **Free T3** | Active thyroid hormone | 2.3-4.2 pg/mL |
| **Testosterone** | Libido, energy, muscle mass | 15-70 ng/dL (women) |
| **SHBG** | Hormone binding; affects free hormone levels | 40-120 nmol/L |
| **DHEA-S** | Adrenal function, energy | 65-380 μg/dL |
| **ApoB** | Advanced CV risk marker | <90 mg/dL |
| **hsCRP** | Inflammation marker (CV risk) | <1.0 mg/L |
| **Vitamin B12** | Energy, neurological health | 300-900 pg/mL |
| **Calcium** | Bone health | 8.5-10.5 mg/dL |

### HRT Monitoring Add-on (+€29) — 5 Biomarkers

| Biomarker | Clinical Rationale |
|-----------|-------------------|
| **Estradiol (trough)** | Verify HRT is achieving target levels |
| **Progesterone** | For combined HRT users |
| **ALT** | Liver function (oral HRT metabolized by liver) |
| **AST** | Liver function |
| **Triglycerides** | Oral estrogen can raise triglycerides |

**Note:** HRT add-on requires specific timing instructions based on HRT type (oral vs transdermal, continuous vs cyclic).

---

## 3. Perimenopause vs Menopause Differentiation

### Why Two Approaches?

Perimenopause is characterized by **fluctuating** hormones — a single snapshot is often misleading. Menopause has **stable low** hormone levels — single sample sufficient.

### Comparison Table

| Feature | Perimenopause Panel | Menopause Panel |
|---------|---------------------|-----------------|
| **Target User** | Still menstruating, irregular cycles, age 40-52 | 12+ months no period, age 45-58 |
| **Sample Timing** | Day 14 (ovulation) + Day 21 (luteal) | Any time |
| **Kit Contents** | 2 finger-prick kits, 2 return envelopes | 1 finger-prick kit |
| **Key Insight** | Hormone fluctuation pattern (still ovulating?) | Baseline menopausal levels |
| **FSH Interpretation** | Track variation between samples | Single elevated reading diagnostic |
| **Price** | €99 (dual sample) | €69-89 |
| **Turnaround** | 72h per sample (results combined) | 72h |

### Perimenopause Sample Timing Guide

```
Cycle Day 1 = First day of period

Day 14 (±2 days): Ovulation Sample
├── FSH should dip if ovulation occurring
├── E2 should peak
└── LH surge indicates ovulation

Day 21 (±2 days): Luteal Sample
├── Progesterone should rise if ovulation occurred
├── E2 moderately elevated
└── FSH should be lower than Day 14
```

If cycles are very irregular (>35 days or <21 days), provide alternative timing guidance in quiz flow.

---

## 4. AI Insights Specifications

### Insight Categories

**1. Menopause Stage Assessment**
```
Output: "Based on your FSH (42 mIU/mL) and estradiol (18 pg/mL),
combined with your reported 14 months without a period, your
results are consistent with postmenopause."

Stages: Early Perimenopause → Late Perimenopause →
        Early Postmenopause → Established Postmenopause
```

**2. Symptom-Biomarker Correlation**
```
Input: User logs hot flashes (severe), sleep issues (moderate)
Output: "Your FSH/E2 ratio of 2.3 is associated with more
frequent vasomotor symptoms. Women with similar profiles
report improvement with lifestyle modifications or HRT."
```

**3. Thyroid Ruling**
```
If TSH normal + Free T4 normal:
Output: "Your thyroid function is normal. This suggests your
fatigue and mood changes are more likely related to hormonal
menopause transition rather than thyroid dysfunction."

If TSH elevated:
Output: "Your TSH is elevated (5.2 mIU/L), which may be
contributing to your fatigue symptoms. We recommend discussing
thyroid testing with your doctor."
```

**4. Cardiovascular Risk Contextualization**
```
Output: "Your total cholesterol has increased from 185 to
218 mg/dL over the past year. This 18% increase is common
during menopause due to declining estrogen. Consider discussing
cardiovascular prevention strategies with your doctor."
```

**5. HRT Optimization Suggestions (for HRT users)**
```
Output: "Your estradiol trough level (28 pg/mL) is at the
lower end of the therapeutic range. If you're still
experiencing symptoms, your doctor may consider adjusting
your HRT dose."
```

**6. Lifestyle Recommendations**
```
Based on: Vitamin D deficiency + elevated HbA1c
Output:
- "Increase vitamin D intake: 2000-4000 IU daily or 15 min
  sun exposure"
- "Your HbA1c (5.9%) suggests prediabetes. Consider reducing
  refined carbohydrates and increasing physical activity."
```

### AI Model Requirements

- **Language:** French (native, not translated)
- **Tone:** Empathetic, clear, empowering
- **Medical Disclaimer:** Always included — "These insights are educational and do not replace medical advice"
- **Citations:** Reference ranges from lab partner; guidelines from HAS/NAMS
- **Personalization:** Use first name, reference specific symptoms logged

---

## 5. UX Flow

### Complete User Journey

```
┌─────────────────────────────────────────────────────────────┐
│  1. DISCOVERY                                                │
│     └── Lands on segment-menopause.html                     │
│     └── Sees biomarker explanation, competitor comparison   │
│     └── CTA: "Commencez votre bilan"                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. QUIZ (5 min)                                             │
│     ├── Q1: Age                                              │
│     ├── Q2: When was your last period?                       │
│     │       • <3 months ago (irregular)                     │
│     │       • 3-12 months ago                               │
│     │       • 12+ months ago                                │
│     │       • Surgical menopause / Hysterectomy             │
│     ├── Q3: Symptoms checklist (multi-select)               │
│     │       □ Hot flashes / night sweats                    │
│     │       □ Sleep problems                                │
│     │       □ Mood changes / anxiety                        │
│     │       □ Fatigue                                       │
│     │       □ Brain fog / memory issues                     │
│     │       □ Joint pain                                    │
│     │       □ Vaginal dryness                               │
│     │       □ Weight changes                                │
│     ├── Q4: Are you currently on HRT?                       │
│     │       • No                                            │
│     │       • Yes - pills                                   │
│     │       • Yes - patches/gel                             │
│     │       • Yes - other                                   │
│     └── Q5: Have you had thyroid issues?                    │
│                                                              │
│     → OUTPUT: Panel recommendation                          │
│       "Based on your answers, we recommend the              │
│        Comprehensive Menopause Panel (€89)"                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. ORDER                                                    │
│     ├── Panel selection (pre-selected from quiz)            │
│     ├── Optional: HRT Monitoring Add-on (+€29)              │
│     ├── Subscription option:                                │
│     │       • One-time (€69/89/99)                          │
│     │       • Every 6 months (-10%)                         │
│     │       • Every 3 months (-15%) [HRT users]             │
│     ├── Shipping address                                    │
│     ├── Payment (Stripe: CB, Apple Pay, PayPal)            │
│     └── Order confirmation + tracking                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. SAMPLE COLLECTION                                        │
│     ├── Kit arrives 2-3 business days (Colissimo)          │
│     ├── Kit contents:                                       │
│     │       • Lancets (3x)                                  │
│     │       • Blood collection tube                         │
│     │       • Alcohol wipes                                 │
│     │       • Bandages                                      │
│     │       • Instruction card (QR to video)               │
│     │       • Prepaid return envelope                       │
│     │       • Biohazard bag                                 │
│     ├── Collection time: ~15 minutes                        │
│     ├── App guides through process with video               │
│     ├── User scans kit barcode to link sample               │
│     └── Drops in any La Poste mailbox                       │
│                                                              │
│     [For Perimenopause: Repeat Day 14 + Day 21]            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. RESULTS (72h from lab receipt)                           │
│     ├── Push notification: "Vos résultats sont prêts"       │
│     ├── App opens to Results Dashboard                      │
│     │                                                        │
│     │   ┌─────────────────────────────────────┐            │
│     │   │  HORMONE WHEEL                       │            │
│     │   │  [FSH] [E2] [LH] [Prog]              │            │
│     │   │  Visual: color-coded quadrants       │            │
│     │   └─────────────────────────────────────┘            │
│     │                                                        │
│     │   ┌─────────────────────────────────────┐            │
│     │   │  YOUR MENOPAUSE STAGE               │            │
│     │   │  ●───────────○───────────○          │            │
│     │   │  Peri    Early Post   Established   │            │
│     │   └─────────────────────────────────────┘            │
│     │                                                        │
│     │   ┌─────────────────────────────────────┐            │
│     │   │  BIOMARKER CARDS                    │            │
│     │   │  Each shows: value, range, status   │            │
│     │   │  Traffic light: 🟢 🟡 🔴             │            │
│     │   └─────────────────────────────────────┘            │
│     │                                                        │
│     ├── AI-generated insights (French)                      │
│     ├── PDF download for GP sharing                         │
│     └── Optional: Book consultation (€49)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. ONGOING ENGAGEMENT                                       │
│     ├── Symptom tracker (daily/weekly logging)              │
│     │       • Hot flash frequency & severity                │
│     │       • Sleep quality score                           │
│     │       • Mood rating                                   │
│     │       • Energy level                                  │
│     ├── Trend charts (if repeat customer)                   │
│     ├── Retest reminders (6 months)                         │
│     ├── Educational content (menopause articles)            │
│     └── Community features (Phase 2)                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Results Visualization

### Dashboard Elements

**1. Hormone Wheel**
```
        FSH
         ●
    ╱         ╲
Prog ●         ● E2
    ╲         ╱
         ●
        LH

Color coding:
- Green: Optimal range
- Yellow: Watch (borderline)
- Red: Action needed
```

**2. Menopause Stage Indicator**
```
YOUR STAGE: Late Perimenopause
○────●────○────○
Early   Late   Early   Est.
Peri    Peri   Post    Post

Based on: FSH 28, E2 45, irregular cycles
```

**3. Traffic Light System (per biomarker)**
```
┌─────────────────────────────────┐
│ FSH                    42 mIU/mL │
│ ████████████████░░░░   🟢        │
│ Optimal for postmenopause        │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Vitamin D              18 ng/mL  │
│ ██████░░░░░░░░░░░░░░   🔴        │
│ Deficient - action recommended   │
└─────────────────────────────────┘
```

**4. Trend Chart (repeat customers)**
```
FSH Trend (12 months)
50 │         ●
40 │    ●         ●
30 │ ●
   └──────────────────
     Jan  Apr  Jul  Oct

"Your FSH has stabilized, indicating you've
 likely transitioned to postmenopause"
```

**5. Symptom Tracker Integration**
```
SYMPTOM LOG (Past 30 days)
─────────────────────────
Hot Flashes:  ████████░░  12 events
Sleep Issues: ██████████  18 nights
Mood Changes: ████░░░░░░   6 days

Correlation: Your hot flash frequency
decreased 40% since your last test
when E2 was lower.
```

---

## 7. Technical Requirements

### Sample Stability
- Finger-prick blood collected in EDTA microtainer
- Stable for 72h at room temperature (validated)
- Return shipping via La Poste (next-day to lab)

### Lab Partner Requirements
- ISO 15189 accredited
- Turnaround: <48h from sample receipt
- Batch processing with AM/PM cutoffs
- Digital results API (HL7 FHIR preferred)

### Data Storage
- HDS-certified hosting (French health data requirement)
- GDPR compliant
- Results retained 10 years (French medical records law)
- User can request deletion (right to be forgotten)

### App Requirements
- iOS 14+ / Android 10+
- Offline mode for symptom logging
- Push notifications
- PDF generation for results
- Barcode scanning for kit linking

---

## 8. Pricing Strategy

### Price Positioning

| Our Panel | Price | Competitor Equivalent | Competitor Price | Savings |
|-----------|-------|----------------------|------------------|---------|
| Essential | €69 | Hertility Basic | €175 | 61% |
| Comprehensive | €89 | Hertility Full | €275 | 68% |
| Perimenopause | €99 | Forth MyFORM | €140 | 29% |
| HRT Add-on | +€29 | Hertility (included) | — | — |

### Subscription Pricing
- One-time: Full price
- Every 6 months: 10% discount (€62 / €80 / €89)
- Every 3 months: 15% discount (€59 / €76 / €84) — HRT users

### Bundle Options (Future)
- Menopause + Partner (€149): Add testosterone panel for partner
- Annual Wellness (€199): 2 comprehensive panels + unlimited symptom tracking

---

## 9. Success Metrics

### Key Performance Indicators

| Metric | Target (Year 1) |
|--------|-----------------|
| Panel completion rate | >85% (kit sent → results delivered) |
| Time to results | <72h (95th percentile) |
| Repeat purchase rate | >40% within 12 months |
| NPS | >50 |
| Symptom tracker DAU | >25% of customers |
| Consultation conversion | >10% |
| Subscription uptake | >30% |

### Quality Metrics
- Sample rejection rate: <3%
- Result accuracy (vs venous reference): r² >0.95 for FSH, E2
- App crash rate: <0.1%
- Support ticket rate: <5% of orders

---

## 10. Launch Checklist

- [ ] Lab partner contract signed (ISO 15189)
- [ ] HDS certification obtained
- [ ] Kit design finalized (French instructions)
- [ ] AI insight prompts validated by gynecologist
- [ ] App development complete (iOS + Android)
- [ ] Stripe payment integration
- [ ] La Poste return shipping contract
- [ ] GDPR/privacy policy finalized
- [ ] Customer support team trained
- [ ] Landing page live (segment-menopause.html)
- [ ] Marketing materials ready (French)
