# Product Vision

## Overview

A health intelligence platform that bridges the gap between clinical lab testing and continuous wearable monitoring, providing users with comprehensive analysis and daily AI-powered recommendations.

---

## Phase 1: Comprehensive Health Analysis (Months 1-6)

### What Users Do

1. **Upload Lab Reports** - Any format (PDF/photo) from any lab
2. **Connect Wearables** - Oura Ring, Apple Watch, Whoop, CGM
3. **Receive Analysis** - Comprehensive report correlating biomarkers with wearable trends

### What The Platform Delivers

#### Lab Data Interpretation
- Uses 17 proprietary health frameworks to explain results in plain language
- Severity classification (optimal/borderline/deficient/elevated)
- Contextual explanations of what each biomarker measures and why it matters

#### Wearable Correlation Analysis
- Cross-reference biomarkers with wearable trends
- Examples:
  - "Your elevated cortisol correlates with declining HRV over past 3 weeks"
  - "Vitamin D deficiency + 22% decline in sleep quality over 8 weeks"
  - "Low iron + elevated resting heart rate suggests compensatory response"

#### Prioritized Action Plan
- Top 3-5 interventions ranked by impact
- Supplement protocols (doses, timing, duration, retest schedule)
- Lifestyle interventions (sleep hygiene, stress management, exercise modifications)
- Further testing recommendations

#### Visual Dashboard
- Biomarker trends over time
- Wearable data visualizations (HRV, sleep, activity, glucose)
- Correlation charts showing biomarker + wearable relationships

### Example Output

> **Critical Finding**: Your vitamin D is 18 ng/mL (deficient) AND your sleep quality has declined 22% over 8 weeks
>
> **Recommendation**: Start 4,000 IU vitamin D3 daily with breakfast (fat-soluble vitamin). Based on your weight (75kg), expect 8-12 week correction period. We'll track your sleep quality improvement.
>
> **What to Monitor**:
> - HRV trend (expect +5-10% improvement)
> - Deep sleep minutes (target: +15-20 min/night)
> - Morning energy (self-reported via daily check-in)
>
> **Retest Schedule**: 8-12 weeks (target range: 30-50 ng/mL)
>
> **Cofactors**: Consider adding magnesium glycinate 400mg + vitamin K2 100mcg for optimal D3 absorption

---

## Phase 2: Daily AI Coach (Months 4-12)

### Morning Readiness Brief (Delivered 6-7am)

**Inputs Analyzed:**
- Last night's sleep data (duration, quality, deep sleep, REM)
- HRV vs. 7-day average and 30-day baseline
- Resting heart rate vs. baseline
- Cumulative sleep debt (past 7 days)
- Glucose stability (if CGM connected)
- Optional: User-reported energy, soreness, stress

**Readiness Classification:**
- **High** - All systems go, optimal for intense training
- **Moderate** - Good for moderate intensity work
- **Low** - Active recovery recommended
- **Recovery Day** - Rest or very light activity only

### Personalized Daily Recommendations

#### Training Guidance

**High Readiness Example:**
> "HRV +12% above baseline, sleep quality 95%, resting HR normal
>
> **Today's Training**: Optimal day for HIIT or heavy strength training
>
> **Workout Suggestion**: 30-min HIIT protocol - [link to workout]
>
> **Notes**: Your cortisol levels are well-managed, you've recovered fully from Tuesday's session"

**Low Readiness Example:**
> "HRV -18% below baseline, sleep debt 90 minutes, resting HR +5 bpm
>
> **Today's Training**: Active recovery only
>
> **Workout Suggestion**: Yoga or Zone 2 walk (max 45 min, HR <130 bpm)
>
> **Priority**: Focus on recovery - aim for 8.5 hours sleep tonight"

#### Supplement Protocol Management

- Daily reminders with context:
  - "Take ashwagandha 300mg + magnesium glycinate 400mg today (cortisol management protocol - Day 14/60)"
  - "Your vitamin D protocol: Today is rest day for vitamin D (3 days on, 1 day off cycle)"

- Progress tracking:
  - "Since starting magnesium 30 days ago: HRV +8%, sleep quality +12%"

- Dynamic adjustments:
  - "Your sleep has normalized - consider reducing magnesium to 200mg and monitor for 2 weeks"

#### Nutrition Recommendations

**CGM-Based:**
- "Glucose spiked to 160 mg/dL after oats yesterday → try this alternative breakfast: 3 eggs + avocado + mixed berries (predicted spike: <120 mg/dL)"

**Macro Targeting:**
- "High intensity training today → target 150g protein, 250g carbs, 70g fat"
- "Protein intake 15g below target yesterday → add whey shake (25g protein) or 200g Greek yogurt"

**Meal Timing:**
- "Your glucose control is best in morning hours → schedule carb-heavy meals before 2pm"

#### Recovery Optimization

**Sleep Interventions:**
- "Deep sleep only 45 min last night (-38% vs baseline) → priorities for tonight:"
  - "8.5 hours in bed (lights out by 10pm)"
  - "No alcohol (reduces REM by 30%)"
  - "Room temp 17-19°C"
  - "Magnesium glycinate 400mg 1 hour before bed"

**Stress Management:**
- "HRV declining 3 days in a row despite good sleep → elevated stress likely:"
  - "10-min meditation this morning (Waking Up app)"
  - "20-min walk at lunch"
  - "Consider postponing Thursday's intense workout"

**Illness Detection:**
- "Body temp +0.5°C, resting HR +8 bpm, HRV -25% → early illness signals:"
  - "Rest day today (cancel planned workout)"
  - "Prioritize sleep (target 9+ hours)"
  - "Increase vitamin C to 2,000mg, add zinc 30mg"
  - "Monitor symptoms - if fever develops, see doctor"

### Progress Tracking

#### Weekly Summary Email

> **Your Week in Review (Jan 29 - Feb 4)**
>
> **Overall Trend**: ↗️ Improving
> - HRV average: 58 (+5% vs last week, +8% vs 4-week average)
> - Sleep quality: 82 (+12% vs last week)
> - Protocol compliance: 6/7 days
>
> **Key Insights**:
> - Your best HRV days (Mon, Wed, Fri) correlate with <7 hours screen time
> - Sunday's low HRV (-22%) followed Saturday's alcohol + late bedtime
> - Deep sleep improved 18 minutes/night on average since starting magnesium
>
> **Recommendations**:
> - Continue magnesium protocol (30 more days before retest)
> - Consider screen time limit of 7 hours (seems to be your HRV threshold)
> - Maintain alcohol-free weekdays (HRV impact too significant)
>
> **Next Milestone**: Vitamin D retest in 6 weeks (Feb 15) - current protocol on track

#### Intervention Efficacy Tracking

Visualize before/after for each intervention:

**Example: Magnesium Protocol**
- **Start Date**: Jan 1
- **Dosage**: 400mg magnesium glycinate before bed
- **Target**: Improve sleep quality + HRV
- **Results (30 days)**:
  - HRV: 52 → 58 (+11.5%) ✅
  - Deep sleep: 62 min → 78 min (+26%) ✅
  - Sleep efficiency: 79% → 87% (+10%) ✅
- **Recommendation**: Continue protocol, retest in 30 days to confirm sustainability

#### Biomarker Predictions

Based on protocol compliance + wearable improvements, predict retest results:

> **Vitamin D Retest Prediction (Feb 15)**
>
> **Baseline**: 18 ng/mL (deficient)
> **Protocol**: 4,000 IU/day for 8 weeks
> **Compliance**: 95% (53/56 days)
>
> **Predicted Range**: 32-38 ng/mL (based on weight, compliance, cofactors)
>
> **Supporting Data**:
> - Sleep quality improved 18% (strong correlation with D3 correction)
> - HRV improved 12% (moderate correlation with D3 correction)
> - No adverse effects reported
>
> **Confidence**: High (85%)
>
> **Action**: Schedule retest for week of Feb 15

---

## Key Differentiators

### vs. Traditional Lab Testing
- **Traditional**: Get results, "everything looks normal" (even if suboptimal)
- **Our Platform**: Detailed interpretation, severity classification, personalized protocols

### vs. InsideTracker / Everlywell
- **Competitors**: Quarterly snapshots, static recommendations
- **Our Platform**: Continuous wearable integration, daily adaptive coaching, protocol tracking

### vs. Oura / Whoop Apps
- **Competitors**: Provide data, basic insights ("your readiness is 75")
- **Our Platform**: Contextualize with biomarkers, explain *why* readiness is low, provide specific interventions

### vs. Human Health Coaches
- **Human Coaches**: CHF 200-500/session, subjective, availability limited
- **Our Platform**: CHF 79/month, 24/7 available, objective data-driven, continuous learning

---

## User Journey Example

### Sarah, 34, Zürich-based Consultant

**Month 0 (January)**: Signs up, uploads Q4 blood work (vitamin D: 18 ng/mL, ferritin: 22 ng/mL, cortisol: 28 mcg/dL), connects Oura Ring

**Week 1**: Receives comprehensive analysis:
- Priority 1: Vitamin D deficiency → 4,000 IU/day protocol
- Priority 2: Low ferritin → 30mg iron bisglycinate + vitamin C
- Priority 3: Elevated cortisol + poor HRV → stress management protocol (ashwagandha 300mg, meditation, reduce training intensity)

**Month 1-3**: Daily AI Coach
- Morning readiness briefs adapt training recommendations
- Supplement reminders with progress tracking
- Weekly summaries show HRV improving (+12%), sleep quality improving (+18%)

**Month 3 (April)**: Retest
- Vitamin D: 18 → 36 ng/mL ✅
- Ferritin: 22 → 48 ng/mL ✅
- Cortisol: 28 → 18 mcg/dL ✅
- HRV baseline: 52 → 62 (+19%)

**Outcome**: Sarah becomes power user, refers 3 friends (CHF 150 referral credit), upgrades to Premium tier

---

## Feature Roadmap

### MVP (Months 1-4)
- ✅ Lab upload + OCR
- ✅ Oura Ring + Apple Watch integration
- ✅ Comprehensive analysis report (PDF + web)
- ✅ Payment processing
- ✅ Basic daily coach (readiness + training recs)

### Phase 1.5 (Months 5-6)
- ✅ Whoop integration
- ✅ Advanced supplement protocol tracking
- ✅ Weekly summary emails
- ✅ Intervention efficacy tracking

### Phase 2 (Months 7-9)
- ✅ CGM integration (Freestyle Libre)
- ✅ Nutrition recommendations (meal swaps, macro targeting)
- ✅ Biomarker prediction algorithm
- ✅ Shareable doctor reports

### Phase 3 (Months 10-12)
- ✅ Mobile app (iOS first)
- ✅ Community features (forum, user sharing)
- ✅ Advanced visualizations (multi-biomarker correlations)
- ✅ Goal setting + tracking

### Future (Year 2+)
- Lab partnerships (automated data import)
- Germany/Austria expansion
- B2B model (employers)
- Genetic data integration (23andMe, etc.)
- Coaching marketplace (connect with human experts)
