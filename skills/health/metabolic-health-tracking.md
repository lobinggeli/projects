# Metabolic Health Tracking Framework

Use this framework to monitor and optimize metabolic health through biomarker tracking, focusing on glucose regulation, energy production, and metabolic flexibility.

## Core Concept

Metabolic health is your body's ability to efficiently produce and regulate energy. Good metabolic health means stable blood sugar, efficient fat burning, healthy insulin sensitivity, and metabolic flexibility (switching between fuel sources). This framework helps track key biomarkers that reveal metabolic function and guide optimization.

### The Metabolic Health Pillars

1. **Glucose Regulation**: Blood sugar stability and insulin sensitivity
2. **Lipid Metabolism**: Fat burning, ketone production, cholesterol health
3. **Energy Production**: Mitochondrial function and cellular energy
4. **Metabolic Flexibility**: Ability to switch between glucose and fat burning
5. **Inflammatory Status**: Chronic inflammation impairs metabolism

## When to Apply

- When tracking weight loss or body composition progress
- To prevent or reverse type 2 diabetes and metabolic syndrome
- For optimizing energy levels and cognitive function
- When implementing dietary changes (keto, low-carb, fasting)
- To monitor cardiovascular disease risk
- For athletic performance optimization
- When addressing fatigue or "brain fog"

## Key Metabolic Biomarkers

### Tier 1: Essential Markers (Start Here)

#### Fasting Glucose
**What it measures:** Blood sugar after 8-12 hour fast
**Sample:** Blood (finger stick or venous)
**Optimal:** 70-85 mg/dL (3.9-4.7 mmol/L)
**Standard "normal":** <100 mg/dL
**Prediabetes:** 100-125 mg/dL
**Diabetes:** ≥126 mg/dL (on two separate tests)

**Interpretation:**
- <70: Possible hypoglycemia (investigate)
- 70-85: Optimal metabolic health
- 86-99: Functional hyperglycemia (early dysfunction)
- 100-125: Prediabetes (insulin resistance present)
- >125: Diabetes

#### HbA1c (Glycated Hemoglobin)
**What it measures:** Average blood sugar over past 2-3 months
**Sample:** Blood
**Optimal:** <5.3%
**Standard "normal":** <5.7%
**Prediabetes:** 5.7-6.4%
**Diabetes:** ≥6.5%

**Why it matters:**
- Fasting glucose = snapshot
- HbA1c = 3-month average
- More stable, less affected by recent meals or stress
- Predicts diabetes and cardiovascular risk

**Limitations:**
- Can be falsely low with anemia or rapid RBC turnover
- Can be falsely high with iron deficiency
- Doesn't show glucose variability

#### Fasting Insulin
**What it measures:** Insulin levels after overnight fast
**Sample:** Blood
**Optimal:** <5 μIU/mL (some sources <6)
**Functional range:** 2-5 μIU/mL
**Concerning:** >10 μIU/mL
**Insulin resistance:** >15 μIU/mL

**Why it matters:**
- Elevated insulin precedes elevated glucose by years
- Early marker of insulin resistance
- Can be high even with "normal" glucose

**Insight:**
High insulin + normal glucose = Your pancreas is working overtime to keep glucose normal. Insulin resistance is developing.

#### HOMA-IR (Insulin Resistance Index)
**Calculation:**
```
HOMA-IR = (Fasting Glucose × Fasting Insulin) / 405
```
(If glucose in mg/dL and insulin in μIU/mL)

**Optimal:** <1.0
**Insulin resistant:** >1.9
**Significant resistance:** >2.9

**Example:**
- Glucose: 90 mg/dL
- Insulin: 8 μIU/mL
- HOMA-IR = (90 × 8) / 405 = 1.78 (mild insulin resistance)

---

### Tier 2: Advanced Glucose Monitoring

#### Continuous Glucose Monitor (CGM)
**What it measures:** Real-time glucose every 5-15 minutes
**Sample:** Interstitial fluid (small sensor under skin)
**Duration:** 10-14 days per sensor

**Key metrics:**
- **Average glucose**: Optimal <100 mg/dL
- **Glucose variability**: Lower is better (SD <20)
- **Time in range (70-120)**: Optimal >90%
- **Postprandial spikes**: <30 mg/dL rise, <140 mg/dL peak

**Benefits:**
- See real-time impact of food, exercise, sleep, stress
- Identify hidden spikes (even with normal HbA1c)
- Optimize meal timing and composition
- Track fasting and dietary interventions

**Interpretation patterns:**
- Frequent spikes >140: Insulin resistance or poor food choices
- Overnight elevation: Dawn phenomenon or late eating
- Fasting rise: Stress, cortisol, gluconeogenesis
- Crashes <70: Reactive hypoglycemia (insulin overshoot)

#### Postprandial Glucose (2-hour post-meal)
**What it measures:** Glucose response to food
**Sample:** Finger stick 2 hours after first bite of meal
**Optimal:** <120 mg/dL
**Acceptable:** <140 mg/dL
**Impaired:** 140-199 mg/dL
**Diabetes:** ≥200 mg/dL

**When to test:**
- After standardized meal (e.g., 75g carbs)
- Or after typical meals to assess personal tolerance

---

### Tier 3: Ketone Monitoring (For Low-Carb/Keto/Fasting)

#### Blood Ketones (Beta-Hydroxybutyrate - BHB)
**What it measures:** Primary ketone body in blood
**Sample:** Blood (finger stick ketone meter)
**Ranges:**
- <0.5 mmol/L: Not in ketosis
- 0.5-1.0: Light nutritional ketosis
- 1.0-3.0: Optimal nutritional ketosis
- 3.0-5.0: High ketosis (fasting, therapeutic)
- >5.0: Investigate (risk of ketoacidosis if diabetic)

**When to test:**
- Morning fasted (lowest levels)
- Pre-meal (shows metabolic state)
- After fat-heavy meal (shows fat-burning capacity)

**Interpretation:**
- Rising ketones = Increasing fat oxidation
- Stable low ketones despite low-carb = Metabolic inflexibility or excess protein
- High ketones + high glucose (>200) in diabetics = DANGER (DKA risk)

#### Urine Ketones (Acetoacetate)
**What it measures:** Ketones being excreted
**Sample:** Urine dipstick
**Ranges:**
- Negative: No ketones
- Trace - Small: Early ketosis
- Moderate: Ketosis
- Large: Deep ketosis

**Limitations:**
- Less accurate than blood
- Shows excess ketones being dumped, not what's being used
- Becomes negative as keto-adaptation improves (you're using ketones efficiently)
- Hydration affects concentration

**Best use:**
- Quick check for ketosis entry
- Not reliable for tracking long-term keto adaptation

#### Breath Ketones (Acetone)
**What it measures:** Acetone in breath
**Sample:** Breath analyzer
**Ranges:** Device-specific (usually 0-50+ ACE)

**Pros:**
- Non-invasive
- Unlimited testing (no strips)
- Correlates with fat oxidation

**Cons:**
- Expensive initial investment
- Less standardized than blood
- Can be affected by alcohol

---

### Tier 4: Lipid Panel (Cardiovascular & Metabolic Health)

#### Standard Lipid Panel
**Sample:** Blood (fasting preferred but not always required)

**Biomarkers:**

| Marker | Optimal | Standard Range | Risk Level |
|--------|---------|----------------|------------|
| **Total Cholesterol** | 150-200 mg/dL | <200 | >240 high |
| **LDL-C** | <100 mg/dL | <100 | >160 high |
| **HDL-C** | >60 mg/dL | >40 (M), >50 (F) | <40 risk |
| **Triglycerides** | <70 mg/dL | <150 | >200 high |
| **VLDL** | <10 mg/dL | <30 | Higher = metabolic dysfunction |

#### Advanced Lipid Markers

**Triglyceride:HDL Ratio**
**Calculation:** Triglycerides / HDL
**Optimal:** <1.0
**Good:** <2.0
**Insulin resistant:** >3.0

**Why it matters:**
- Best predictor of insulin resistance from standard lipid panel
- Better than LDL for cardiovascular risk
- Inversely correlates with LDL particle size

**ApoB (Apolipoprotein B)**
**Optimal:** <80 mg/dL
**What it measures:** Number of atherogenic particles (LDL, VLDL, Lp(a))
**Why superior to LDL-C:** Counts particles, not cholesterol content

**LDL Particle Size & Number**
- **Small dense LDL (Pattern B)**: Atherogenic, correlates with insulin resistance
- **Large fluffy LDL (Pattern A)**: Less atherogenic
- **LDL-P (particle count)**: More predictive than LDL-C

---

### Tier 5: Inflammation & Other Metabolic Markers

#### hsCRP (High-Sensitivity C-Reactive Protein)
**Optimal:** <1.0 mg/L
**Moderate risk:** 1.0-3.0
**High risk:** >3.0
**Acute inflammation:** >10

**Why it matters:**
- Chronic inflammation drives insulin resistance
- Cardiovascular risk marker
- Elevated in metabolic syndrome

#### Homocysteine
**Optimal:** <7 μmol/L
**Acceptable:** 7-10
**Elevated:** >10
**High risk:** >15

**Why it matters:**
- Methylation status
- B vitamin status (B6, B12, folate)
- Cardiovascular risk
- Insulin resistance marker

#### Uric Acid
**Optimal:** 3.0-5.5 mg/dL
**High:** >7.0 (M), >6.0 (F)

**Why it matters:**
- Elevated in metabolic syndrome and gout
- Marker of fructose metabolism issues
- Inhibits nitric oxide (endothelial dysfunction)

#### Liver Enzymes (ALT, AST)
**Why for metabolism:**
- Elevated ALT often indicates fatty liver (NAFLD)
- NAFLD strongly associated with insulin resistance
- ALT >25 (F) or >30 (M) may indicate metabolic dysfunction

---

## Metabolic Health Assessment Template

```markdown
## Metabolic Health Assessment: [Date]

### Current Biomarkers

#### Glucose Regulation
| Marker | Value | Unit | Optimal | Status |
|--------|-------|------|---------|--------|
| Fasting Glucose | | mg/dL | 70-85 | |
| HbA1c | | % | <5.3 | |
| Fasting Insulin | | μIU/mL | 2-5 | |
| HOMA-IR | [Calculate] | | <1.0 | |
| 2hr Postprandial | | mg/dL | <120 | |

**HOMA-IR Calculation:**
```
([Fasting Glucose] × [Fasting Insulin]) / 405 = [X]
```

#### Ketone Status (if applicable)
| Marker | Value | Unit | Target Range | Status |
|--------|-------|------|--------------|--------|
| Blood BHB | | mmol/L | 0.5-3.0 (if keto) | |
| Urine Ketones | | | Moderate (if keto) | |

#### Lipid Panel
| Marker | Value | Unit | Optimal | Status |
|--------|-------|------|---------|--------|
| Total Cholesterol | | mg/dL | 150-200 | |
| LDL-C | | mg/dL | <100 | |
| HDL-C | | mg/dL | >60 | |
| Triglycerides | | mg/dL | <70 | |
| TG:HDL Ratio | [Calculate] | | <1.0 | |
| ApoB | | mg/dL | <80 | (if tested) |

**TG:HDL Ratio Calculation:**
```
[Triglycerides] / [HDL] = [X]
```

#### Inflammation
| Marker | Value | Unit | Optimal | Status |
|--------|-------|------|---------|--------|
| hsCRP | | mg/L | <1.0 | |
| Homocysteine | | μmol/L | <7 | |
| Uric Acid | | mg/dL | 3.0-5.5 | |

#### Liver Function
| Marker | Value | Unit | Optimal | Status |
|--------|-------|------|---------|--------|
| ALT | | U/L | <25 (F), <30 (M) | |
| AST | | U/L | <25 | |
| AST:ALT Ratio | | | ~1.0 | |

---

### Metabolic Health Score

**Scoring system** (1 point for each optimal marker):

- [ ] Fasting glucose 70-85 mg/dL
- [ ] HbA1c <5.3%
- [ ] Fasting insulin <5 μIU/mL
- [ ] HOMA-IR <1.0
- [ ] TG:HDL ratio <1.0
- [ ] Triglycerides <70 mg/dL
- [ ] HDL >60 mg/dL
- [ ] hsCRP <1.0 mg/L
- [ ] Waist:Height ratio <0.5
- [ ] Blood pressure <120/80

**Your score**: [X] / 10

**Interpretation:**
- 9-10: Excellent metabolic health
- 7-8: Good metabolic health
- 5-6: Mild metabolic dysfunction
- 3-4: Moderate metabolic dysfunction (prediabetes range)
- 0-2: Significant metabolic dysfunction (diabetes range)

---

### Pattern Recognition

#### Primary Metabolic Pattern

**Select dominant pattern:**

- [ ] **Optimal Metabolic Health**
  - All markers in optimal range
  - High metabolic flexibility

- [ ] **Early Insulin Resistance**
  - Elevated fasting insulin (>5)
  - Normal or mildly elevated glucose
  - HOMA-IR 1-2
  - TG:HDL ratio 1-2

- [ ] **Established Insulin Resistance**
  - Elevated insulin (>10)
  - Elevated fasting glucose (>100)
  - HOMA-IR >2
  - TG:HDL >2
  - Low HDL, high triglycerides

- [ ] **Metabolic Syndrome**
  - Meets 3+ criteria:
    - Waist >40" (M) or >35" (F)
    - Triglycerides ≥150
    - HDL <40 (M) or <50 (F)
    - BP ≥130/85
    - Fasting glucose ≥100

- [ ] **Prediabetes**
  - Fasting glucose 100-125 mg/dL
  - HbA1c 5.7-6.4%
  - Insulin resistance present

- [ ] **Type 2 Diabetes**
  - Fasting glucose ≥126 mg/dL
  - HbA1c ≥6.5%
  - Postprandial >200 mg/dL

- [ ] **Lean Metabolic Dysfunction**
  - Normal BMI but elevated insulin/HOMA-IR
  - "Thin on the outside, fat on the inside" (TOFI)
  - Visceral adiposity despite normal weight

- [ ] **Poor Metabolic Flexibility**
  - Difficulty entering ketosis despite low-carb
  - Frequent hunger/energy crashes
  - Low ketones despite fasting

**Supporting evidence:**
1. [Key biomarker or ratio]
2. [Symptom correlation]
3. [Lifestyle factor]

---

### CGM Insights (if using)

**Summary statistics** (from [X] days of data):
- Average glucose: [X] mg/dL (Target: <100)
- Standard deviation: [X] (Target: <20)
- Coefficient of variation: [X]% (Target: <20%)
- Time in range (70-120): [X]% (Target: >90%)
- Time above 140: [X]% (Target: <1%)
- Time below 70: [X]% (Target: <1%)

**Patterns observed:**
- **Fasting glucose trend**: [Stable / Rising / Variable]
- **Postprandial spikes**: [Foods that spike]
- **Dawn phenomenon**: [Yes/No - rise between 4-8 AM]
- **Exercise response**: [Glucose rises/falls/stable]
- **Stress response**: [Glucose rises during stress]
- **Sleep correlation**: [Poor sleep → higher glucose]

**Actionable insights:**
1. [Foods to avoid or modify]
2. [Optimal eating windows]
3. [Exercise timing effects]

---

### Root Cause Analysis

**Primary drivers of dysfunction** (if present):

1. **[Driver 1]**: [e.g., Diet - excess refined carbs]
   - Evidence: [High postprandial spikes on CGM]
   - Impact: [Insulin resistance, elevated TG]

2. **[Driver 2]**: [e.g., Sedentary lifestyle]
   - Evidence: [Low muscle mass, high body fat %]
   - Impact: [Reduced insulin sensitivity]

3. **[Driver 3]**: [e.g., Chronic stress]
   - Evidence: [Elevated cortisol, poor sleep]
   - Impact: [Drives glucose production, insulin resistance]

**Timeline hypothesis:**
- [How long has dysfunction been developing]
- [Triggering events or lifestyle changes]
- [Current trajectory: worsening / stable / improving]

---

### Intervention Strategy

#### Phase 1: Foundation (Weeks 1-4)

**Dietary:**
- [ ] **Carbohydrate quality & quantity**
  - Eliminate: [Refined carbs, sugars, processed foods]
  - Emphasize: [Non-starchy vegetables, quality protein, healthy fats]
  - Target total carbs: [<150g/day initially, potentially <50g for therapeutic ketosis]

- [ ] **Protein adequacy**
  - Target: [0.8-1.2g per kg bodyweight]
  - Distribute across meals

- [ ] **Healthy fats**
  - Include: [Olive oil, avocado, nuts, fatty fish]
  - Avoid: [Trans fats, excess omega-6 oils]

- [ ] **Meal timing**
  - Strategy: [3 meals, no snacking / Time-restricted eating / Intermittent fasting]
  - Eating window: [X hours]

**Movement:**
- [ ] **Resistance training**: 3x/week (builds insulin-sensitive muscle)
- [ ] **Walking**: Post-meal walks (blunts glucose spikes)
- [ ] **Daily movement**: [Target steps or activity]

**Sleep:**
- [ ] **Target: 7-9 hours**
- [ ] **Consistent schedule**
- [ ] **Optimize environment** (dark, cool, quiet)

**Stress Management:**
- [ ] **Daily practice**: [Meditation, breathwork, etc.]
- [ ] **Cortisol reduction** (improves insulin sensitivity)

#### Phase 2: Optimization (Weeks 5-12)

**Advanced dietary strategies:**
- [ ] Therapeutic ketosis (if appropriate): <50g carbs/day
- [ ] Extended fasting protocols (24-72 hour fasts)
- [ ] Targeted carb timing (around workouts)

**Targeted supplementation:**

| Supplement | Dose | Timing | Mechanism |
|------------|------|--------|-----------|
| Berberine | 500mg 2-3x/day | Before meals | Improves insulin sensitivity |
| Chromium | 200-400mcg | With meals | Enhances insulin action |
| Magnesium | 300-400mg | Evening | Insulin sensitivity, glucose metabolism |
| Omega-3 (EPA/DHA) | 2-3g/day | With food | Reduces inflammation, improves lipids |
| Vitamin D | [Per testing] | Morning | If deficient; improves insulin sensitivity |
| Alpha-lipoic acid | 300-600mg | Daily | Antioxidant, glucose disposal |

**Medications** (if needed - medical supervision):
- Metformin (for prediabetes/diabetes)
- GLP-1 agonists (semaglutide, etc.)
- SGLT2 inhibitors

#### Phase 3: Metabolic Flexibility Training (Ongoing)

**Goal**: Ability to efficiently switch between glucose and fat burning

**Strategies:**
- [ ] Alternate carb cycling (low-carb days with occasional refeeds)
- [ ] Fasted training sessions
- [ ] Post-workout carb timing
- [ ] Monitor ketone and glucose flexibility (Glucose-Ketone Index)

**Glucose-Ketone Index (GKI):**
```
GKI = [Glucose (mg/dL)] / [Ketones (mmol/L)] / 18
```
- GKI <3: Therapeutic ketosis
- GKI 3-6: Weight loss/metabolic therapy zone
- GKI 6-9: Moderate ketosis
- GKI >9: Not in ketosis

---

### Tracking & Monitoring Plan

**Daily tracking:**
- Fasting glucose (if not using CGM)
- Blood ketones (if keto)
- Weight (optional, same time daily)
- Food intake and macros
- Exercise and sleep

**Weekly tracking:**
- Body measurements (waist, body composition)
- Symptom log (energy, hunger, cravings)
- Performance metrics

**Biomarker retesting schedule:**

| Timeframe | Markers to Retest | Purpose |
|-----------|-------------------|---------|
| 4-6 weeks | Fasting glucose, ketones | Early response check |
| 3 months | Full panel (glucose, insulin, HbA1c, lipids) | Comprehensive reassessment |
| 6 months | Full panel + advanced (ApoB, hsCRP) | Long-term tracking |
| Annually | Complete metabolic panel | Maintenance monitoring |

**Success metrics:**
- [ ] Fasting glucose: Target <85 mg/dL
- [ ] HbA1c: Target <5.3%
- [ ] Fasting insulin: Target <5 μIU/mL
- [ ] HOMA-IR: Target <1.0
- [ ] TG:HDL: Target <1.0
- [ ] CGM time in range: Target >90%
- [ ] Waist circumference: Reduce by [X] inches
- [ ] Symptom improvement: [Energy, mental clarity, etc.]

---

### Questions for Healthcare Provider

1. **About current status:**
   - [How concerned should we be about [specific marker]?]
   - [Am I at risk for diabetes given these markers?]

2. **About interventions:**
   - [Is metformin appropriate at this stage?]
   - [Which supplements are evidence-based for my situation?]

3. **About monitoring:**
   - [How often should we retest?]
   - [Should I be using a CGM given my risk level?]

4. **About complications:**
   - [Should we screen for complications (neuropathy, retinopathy)?]

```

## Special Populations & Considerations

### Athletic Performance
- Higher glucose and insulin tolerance
- May maintain ketosis at higher carb intakes
- Targeted carb timing around training
- Monitor for relative energy deficiency (RED-S)

### Pregnancy
- Gestational diabetes screening
- Different glucose targets
- Avoid aggressive interventions
- Medical supervision required

### Type 1 Diabetes
- Ketones + high glucose = DKA risk
- Different targets and monitoring
- Insulin dosing calculations
- Medical management essential

### Elderly
- Age-adjusted reference ranges
- Balance metabolic optimization with quality of life
- Medication interactions
- Sarcopenia prevention priority

## Limitations

- Biomarkers are snapshots; can vary day-to-day
- Reference ranges are population-based, not personalized
- Doesn't account for genetic variants affecting metabolism
- Some tests expensive and not covered by insurance
- CGMs not 100% accurate (lag time vs. blood)
- Interventions affect multiple systems; hard to isolate effects
- Optimal ranges debated; evidence evolves

**Remember**: Metabolic health is foundational to overall health. Insulin resistance develops silently for years before glucose rises. Early detection and intervention through biomarker tracking can prevent or reverse progression to diabetes and reduce cardiovascular risk.
