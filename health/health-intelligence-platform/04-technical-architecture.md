# Technical Architecture

**Last Updated**: February 9, 2026

## Overview

This document outlines the technical architecture for the health intelligence platform, covering both Phase 1 (Comprehensive Analysis) and Phase 2 (Daily AI Coach) implementation.

**Design Principles:**
- Modular architecture for rapid iteration
- Leverage managed services to minimize DevOps overhead
- API-first design for future mobile app integration
- Privacy-first data handling (GDPR compliant)
- Cost-efficient scaling (optimize for CHF 1-2 variable cost per user)

---

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         Frontend Layer                          │
│  (Next.js 14 + React + TypeScript + TailwindCSS)               │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Dashboard  │  │  Lab Upload  │  │  Daily Coach │         │
│  │  Biomarkers  │  │  & Analysis  │  │  Readiness   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   API Gateway     │
                    │  (Next.js API)    │
                    └─────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼────────┐   ┌────────▼────────┐   ┌───────▼────────┐
│   Auth Layer   │   │  Analysis Engine│   │  Data Pipeline │
│  (Supabase)    │   │  (Python + AI)  │   │  (Background)  │
└────────────────┘   └─────────────────┘   └────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼────────┐   ┌────────▼────────┐   ┌───────▼────────┐
│   PostgreSQL   │   │  External APIs  │   │  File Storage  │
│  (Supabase)    │   │  Oura, Apple,   │   │  (Supabase)    │
│  + TimescaleDB │   │  Whoop, OpenAI  │   │  (S3-compat)   │
└────────────────┘   └─────────────────┘   └────────────────┘
```

---

## Phase 1: Core Platform (Months 1-6)

### 1. Lab Report Ingestion

#### Components

**Frontend Upload Interface:**
- Drag & drop file upload (PDF, JPEG, PNG)
- Multi-file support (upload full panel history)
- Preview uploaded files before submission
- Progress indicators during upload & processing

**OCR Processing Pipeline:**
```typescript
// Service: /lib/ocr/process-lab-report.ts

interface LabReportUpload {
  userId: string;
  files: File[];
  labProvider?: string; // Optional: "biostarks", "medisyn", etc.
}

async function processLabReport(upload: LabReportUpload) {
  // Step 1: Upload to storage
  const fileUrls = await uploadToStorage(upload.files);

  // Step 2: OCR extraction
  const ocrResults = await extractTextFromPDFs(fileUrls);

  // Step 3: Biomarker parsing
  const biomarkers = await parseBiomarkers(ocrResults);

  // Step 4: Validation & normalization
  const validated = await validateBiomarkers(biomarkers);

  // Step 5: Store in database
  await saveBiomarkersToDb(upload.userId, validated);

  return validated;
}
```

**OCR Technology Stack:**

| Provider | Use Case | Cost | Accuracy |
|----------|----------|------|----------|
| **Google Cloud Vision API** | Primary OCR engine | CHF 1.50 per 1,000 pages | 95-98% |
| **OpenAI GPT-4 Vision** | Fallback + structured extraction | CHF 3-5 per report | 90-95% |
| **Claude 3.5 Sonnet** | Complex reports (if GPT-4 fails) | CHF 3-4 per report | 92-96% |

**Strategy**: Use Google Vision first (cheapest), fall back to GPT-4 Vision if confidence < 85%

**Biomarker Parsing:**
```python
# Service: /python/ocr/biomarker_parser.py

import openai
from typing import List, Dict

def parse_biomarkers_with_llm(ocr_text: str) -> List[Dict]:
    """
    Extract structured biomarker data from OCR text using GPT-4
    """
    prompt = f"""
    Extract all biomarkers from the following lab report.
    For each biomarker, provide:
    - name (standardized, e.g., "Vitamin D (25-OH)")
    - value (numeric)
    - unit (e.g., "ng/mL")
    - reference_range (e.g., "30-100")
    - date_tested (ISO format)

    OCR Text:
    {ocr_text}

    Return as JSON array.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content
```

---

### 2. Wearable Integration

#### Supported Devices (Priority Order)

1. **Oura Ring** (Highest priority - most popular among Swiss biohackers)
2. **Apple Health** (Broad reach - Apple Watch, Health app data)
3. **Whoop** (Popular among athletes)
4. **CGM (Freestyle Libre, Dexcom)** (Phase 2 priority)

#### Oura Ring Integration

**API Endpoint**: `https://api.ouraring.com/v2`

**Authentication**: OAuth 2.0

**Data Retrieved:**
- Daily sleep metrics (duration, efficiency, deep sleep, REM, latency)
- Daily readiness score + contributing factors
- Daily activity (steps, calories, active time)
- Heart rate variability (HRV) - nocturnal average
- Resting heart rate
- Body temperature deviation

**Implementation:**
```typescript
// Service: /lib/wearables/oura.ts

import { OuraClient } from '@oura/api';

interface OuraMetrics {
  date: string;
  sleep: {
    total_sleep_duration: number; // seconds
    deep_sleep_duration: number;
    rem_sleep_duration: number;
    sleep_efficiency: number; // percentage
    sleep_latency: number; // seconds
  };
  readiness: {
    score: number; // 0-100
    hrv_balance: number;
    recovery_index: number;
  };
  activity: {
    steps: number;
    calories_total: number;
    inactive_time: number;
  };
  hrv: {
    avg_hrv: number; // ms
    hrv_baseline: number; // 30-day baseline
  };
}

async function fetchOuraData(
  userId: string,
  startDate: string,
  endDate: string
): Promise<OuraMetrics[]> {
  const client = new OuraClient(getUserAccessToken(userId));

  const [sleep, readiness, activity, hrv] = await Promise.all([
    client.sleep.list({ start_date: startDate, end_date: endDate }),
    client.readiness.list({ start_date: startDate, end_date: endDate }),
    client.activity.list({ start_date: startDate, end_date: endDate }),
    client.heartrate.list({ start_date: startDate, end_date: endDate })
  ]);

  return mergeDailyData(sleep, readiness, activity, hrv);
}
```

#### Apple Health Integration

**Implementation Options:**
1. **Health Auto Export** (Third-party app) - User exports XML file
2. **HealthKit Bridge API** (Custom iOS app in Phase 3)

**Phase 1 Approach**: Manual XML upload via Health Auto Export
- Pros: No iOS app needed, works immediately
- Cons: Manual export required (acceptable for MVP)

**Data Retrieved:**
- Steps, distance, active energy
- Heart rate (resting, average, variability)
- Sleep analysis (if Apple Watch worn)
- Workouts (type, duration, intensity)

```typescript
// Service: /lib/wearables/apple-health.ts

import xml2js from 'xml2js';

async function parseAppleHealthXML(xmlFile: string) {
  const parser = new xml2js.Parser();
  const data = await parser.parseStringPromise(xmlFile);

  const records = data.HealthData.Record;

  return {
    steps: extractMetric(records, 'HKQuantityTypeIdentifierStepCount'),
    heartRate: extractMetric(records, 'HKQuantityTypeIdentifierHeartRate'),
    hrv: extractMetric(records, 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN'),
    sleep: extractMetric(records, 'HKCategoryTypeIdentifierSleepAnalysis')
  };
}
```

#### Whoop Integration

**API Endpoint**: `https://api.whoop.com/v1`

**Authentication**: OAuth 2.0

**Data Retrieved:**
- Recovery score (0-100%)
- HRV (ms)
- Resting heart rate (bpm)
- Sleep performance (duration, quality, stages)
- Strain score (daily exertion)

---

### 3. Analysis Engine

#### Core Analysis Components

**1. Biomarker Interpretation**
```python
# Service: /python/analysis/biomarker_interpreter.py

from typing import Dict, List
import anthropic

class BiomarkerInterpreter:
    """
    Uses Claude 3.5 Sonnet to interpret biomarkers using 17 proprietary frameworks
    """

    def __init__(self):
        self.client = anthropic.Client()
        self.frameworks = self._load_frameworks()

    def interpret(self, biomarkers: List[Dict]) -> Dict:
        """
        Generate comprehensive interpretation for all biomarkers
        """
        prompt = self._build_interpretation_prompt(biomarkers)

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        return self._parse_interpretation(response.content)

    def _build_interpretation_prompt(self, biomarkers: List[Dict]) -> str:
        return f"""
        You are a functional medicine AI analyst. Analyze the following biomarkers
        using these 17 health frameworks:

        {self._format_frameworks()}

        Biomarkers:
        {self._format_biomarkers(biomarkers)}

        For each biomarker, provide:
        1. **Severity Classification**: Optimal / Borderline / Deficient / Elevated / Critical
        2. **Context**: What this biomarker measures and why it matters
        3. **Root Causes**: Potential reasons for out-of-range values
        4. **Downstream Effects**: How this impacts other systems
        5. **Intervention Priority**: 1-5 (5 = highest priority)

        Return structured JSON.
        """
```

**2. Wearable Correlation Analysis**
```python
# Service: /python/analysis/correlation_analyzer.py

import pandas as pd
import numpy as np
from scipy.stats import pearsonr

class CorrelationAnalyzer:
    """
    Correlates biomarker levels with wearable trends
    """

    def analyze_correlations(
        self,
        biomarkers: Dict,
        wearable_data: pd.DataFrame
    ) -> List[Dict]:
        """
        Find significant correlations between biomarkers and wearable metrics
        """
        correlations = []

        # Example: Vitamin D deficiency + Sleep quality decline
        if biomarkers.get('vitamin_d', {}).get('value', 100) < 30:
            sleep_trend = self._calculate_trend(
                wearable_data['sleep_quality'],
                days=56  # 8 weeks
            )

            if sleep_trend['change_percent'] < -15:  # >15% decline
                correlations.append({
                    'biomarker': 'vitamin_d',
                    'wearable_metric': 'sleep_quality',
                    'finding': f"Vitamin D deficiency ({biomarkers['vitamin_d']['value']} ng/mL) "
                               f"correlates with {sleep_trend['change_percent']:.1f}% decline "
                               f"in sleep quality over 8 weeks",
                    'strength': 'strong',
                    'clinical_significance': 'high'
                })

        # Example: Low iron + Elevated resting HR
        if biomarkers.get('ferritin', {}).get('value', 100) < 30:
            rhr_trend = self._calculate_trend(
                wearable_data['resting_heart_rate'],
                days=30
            )

            if rhr_trend['change_bpm'] > 3:
                correlations.append({
                    'biomarker': 'ferritin',
                    'wearable_metric': 'resting_heart_rate',
                    'finding': f"Low ferritin ({biomarkers['ferritin']['value']} ng/mL) "
                               f"correlates with +{rhr_trend['change_bpm']:.1f} bpm increase "
                               f"in resting heart rate (compensatory response)",
                    'strength': 'moderate',
                    'clinical_significance': 'medium'
                })

        return correlations
```

**3. Protocol Generator**
```python
# Service: /python/analysis/protocol_generator.py

class ProtocolGenerator:
    """
    Generates personalized supplement and lifestyle protocols
    """

    def generate_supplement_protocol(
        self,
        biomarker: str,
        value: float,
        user_weight_kg: float
    ) -> Dict:
        """
        Generate personalized supplement protocol based on biomarker deficiency
        """
        protocols = {
            'vitamin_d': self._vitamin_d_protocol,
            'magnesium': self._magnesium_protocol,
            'iron': self._iron_protocol,
            # ... 20+ biomarker protocols
        }

        if biomarker in protocols:
            return protocols[biomarker](value, user_weight_kg)

        return None

    def _vitamin_d_protocol(self, value_ng_ml: float, weight_kg: float) -> Dict:
        """
        Vitamin D supplementation protocol based on current level and body weight
        """
        # Target: 40-60 ng/mL optimal range
        deficit = 50 - value_ng_ml  # Target midpoint of optimal range

        # Estimation: 100 IU per day raises levels by ~1 ng/mL over 2-3 months
        # Adjust for body weight (higher weight = higher dose needed)
        base_dose = deficit * 100
        weight_adjustment = 1 + ((weight_kg - 70) * 0.01)  # Adjust for non-70kg

        daily_dose = min(10000, max(2000, base_dose * weight_adjustment))

        return {
            'supplement': 'Vitamin D3 (cholecalciferol)',
            'dose': f"{int(daily_dose)} IU",
            'frequency': 'Daily with breakfast (fat-soluble vitamin)',
            'duration': '8-12 weeks',
            'cofactors': [
                'Magnesium glycinate 400mg (required for D3 activation)',
                'Vitamin K2 (MK-7) 100mcg (prevents calcium misallocation)'
            ],
            'retest_schedule': '8-12 weeks',
            'target_range': '40-60 ng/mL',
            'expected_improvement': f"{deficit * 0.7:.1f}-{deficit * 0.9:.1f} ng/mL increase",
            'monitoring': [
                'Track sleep quality (expect +10-15% improvement)',
                'Track HRV (expect +5-10% improvement)',
                'Track energy levels (expect improvement in 4-6 weeks)'
            ],
            'warnings': [
                'Do not exceed 10,000 IU/day without medical supervision',
                'Take with fatty meal for optimal absorption',
                'Must supplement with magnesium to avoid depletion'
            ]
        }
```

**4. Report Generator**
```typescript
// Service: /lib/reports/generate-pdf.ts

import PDFDocument from 'pdfkit';
import { Storage } from '@supabase/storage-js';

interface ReportData {
  user: UserProfile;
  biomarkers: BiomarkerResults[];
  wearableCorrelations: Correlation[];
  protocols: Protocol[];
  visualizations: Chart[];
}

async function generateComprehensiveReport(data: ReportData): Promise<string> {
  const doc = new PDFDocument({ size: 'A4', margin: 50 });

  // Title Page
  doc.fontSize(24).text('Comprehensive Health Analysis', { align: 'center' });
  doc.fontSize(12).text(`Prepared for: ${data.user.name}`, { align: 'center' });
  doc.fontSize(10).text(`Date: ${new Date().toLocaleDateString()}`, { align: 'center' });

  // Executive Summary (Page 2)
  doc.addPage();
  doc.fontSize(18).text('Executive Summary');
  doc.fontSize(11).text(generateExecutiveSummary(data));

  // Critical Findings (Page 3)
  doc.addPage();
  doc.fontSize(18).text('Critical Findings');
  data.biomarkers
    .filter(b => b.severity === 'critical' || b.severity === 'deficient')
    .forEach(biomarker => {
      doc.fontSize(14).text(biomarker.name, { underline: true });
      doc.fontSize(11).text(biomarker.interpretation);
      doc.moveDown();
    });

  // Wearable Correlations (Page 4-5)
  doc.addPage();
  doc.fontSize(18).text('Biomarker + Wearable Correlations');
  data.wearableCorrelations.forEach(corr => {
    doc.fontSize(12).text(corr.finding);
    doc.fontSize(10).text(`Clinical Significance: ${corr.clinical_significance}`);
    doc.moveDown();
  });

  // Action Plan (Page 6-8)
  doc.addPage();
  doc.fontSize(18).text('Prioritized Action Plan');
  data.protocols
    .sort((a, b) => b.priority - a.priority)
    .forEach((protocol, index) => {
      doc.fontSize(14).text(`Priority ${index + 1}: ${protocol.biomarker}`);
      doc.fontSize(11).text(`Protocol: ${protocol.supplement} - ${protocol.dose}`);
      doc.fontSize(10).text(`Duration: ${protocol.duration} | Retest: ${protocol.retest_schedule}`);
      doc.moveDown();
    });

  // Save to storage
  const pdfBuffer = await streamToBuffer(doc);
  const fileName = `reports/${data.user.id}/${Date.now()}-analysis.pdf`;

  const storage = new Storage({ url: process.env.SUPABASE_URL });
  await storage.from('reports').upload(fileName, pdfBuffer);

  return fileName;
}
```

---

### 4. Database Schema

**Technology**: PostgreSQL 15 + TimescaleDB (for time-series wearable data)

```sql
-- Users & Authentication (managed by Supabase Auth)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  subscription_tier TEXT DEFAULT 'none', -- 'none', 'analysis', 'daily_coach', 'premium'
  subscription_status TEXT DEFAULT 'inactive', -- 'active', 'inactive', 'canceled'
  stripe_customer_id TEXT,
  weight_kg NUMERIC(5,2), -- For protocol personalization
  date_of_birth DATE,
  gender TEXT
);

-- Lab Reports (raw uploads)
CREATE TABLE lab_reports (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  uploaded_at TIMESTAMPTZ DEFAULT NOW(),
  file_url TEXT NOT NULL,
  lab_provider TEXT, -- 'biostarks', 'medisyn', etc.
  test_date DATE,
  ocr_status TEXT DEFAULT 'pending', -- 'pending', 'processing', 'completed', 'failed'
  ocr_confidence NUMERIC(3,2) -- 0.00-1.00
);

-- Biomarkers (extracted from lab reports)
CREATE TABLE biomarkers (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  lab_report_id UUID REFERENCES lab_reports(id) ON DELETE CASCADE,
  test_date DATE NOT NULL,
  biomarker_name TEXT NOT NULL, -- Standardized name
  value NUMERIC(10,4) NOT NULL,
  unit TEXT NOT NULL,
  reference_range_min NUMERIC(10,4),
  reference_range_max NUMERIC(10,4),
  severity TEXT, -- 'optimal', 'borderline', 'deficient', 'elevated', 'critical'
  interpretation TEXT, -- AI-generated explanation
  created_at TIMESTAMPTZ DEFAULT NOW(),

  INDEX idx_user_biomarker (user_id, biomarker_name, test_date),
  INDEX idx_test_date (test_date DESC)
);

-- Wearable Connections
CREATE TABLE wearable_connections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  device_type TEXT NOT NULL, -- 'oura', 'apple_health', 'whoop', 'cgm'
  access_token TEXT NOT NULL, -- Encrypted
  refresh_token TEXT,
  token_expires_at TIMESTAMPTZ,
  connected_at TIMESTAMPTZ DEFAULT NOW(),
  last_sync_at TIMESTAMPTZ,
  sync_status TEXT DEFAULT 'active', -- 'active', 'expired', 'error'

  UNIQUE(user_id, device_type)
);

-- Wearable Data (time-series - uses TimescaleDB)
CREATE TABLE wearable_metrics (
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  device_type TEXT NOT NULL,
  metric_date DATE NOT NULL,
  metric_type TEXT NOT NULL, -- 'sleep_duration', 'hrv', 'resting_hr', etc.
  value NUMERIC(10,4) NOT NULL,
  unit TEXT,
  metadata JSONB, -- Device-specific extra data
  recorded_at TIMESTAMPTZ DEFAULT NOW(),

  PRIMARY KEY (user_id, metric_date, device_type, metric_type)
);

-- Convert to TimescaleDB hypertable for efficient time-series queries
SELECT create_hypertable('wearable_metrics', 'metric_date');

-- Analysis Reports
CREATE TABLE analysis_reports (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  report_type TEXT DEFAULT 'comprehensive', -- 'comprehensive', 'retest', 'quarterly'
  pdf_url TEXT,
  biomarker_summary JSONB, -- Structured summary of findings
  correlations JSONB, -- Biomarker + wearable correlations
  protocols JSONB, -- Generated protocols
  status TEXT DEFAULT 'generating' -- 'generating', 'ready', 'failed'
);

-- Supplement Protocols
CREATE TABLE protocols (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  analysis_report_id UUID REFERENCES analysis_reports(id),
  biomarker_name TEXT NOT NULL,
  supplement_name TEXT NOT NULL,
  dose TEXT NOT NULL,
  frequency TEXT NOT NULL,
  start_date DATE DEFAULT CURRENT_DATE,
  end_date DATE, -- Expected completion date
  retest_date DATE, -- When to retest biomarker
  status TEXT DEFAULT 'active', -- 'active', 'completed', 'discontinued'
  compliance_rate NUMERIC(3,2), -- 0.00-1.00 (tracked via check-ins)
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Daily Readiness (for Phase 2)
CREATE TABLE daily_readiness (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  readiness_date DATE NOT NULL,
  readiness_score INTEGER, -- 0-100
  readiness_category TEXT, -- 'high', 'moderate', 'low', 'recovery'
  hrv_status TEXT, -- 'above_baseline', 'normal', 'below_baseline'
  sleep_quality INTEGER, -- 0-100
  training_recommendation TEXT,
  generated_at TIMESTAMPTZ DEFAULT NOW(),

  UNIQUE(user_id, readiness_date)
);
```

---

## Phase 2: Daily AI Coach (Months 4-12)

### 1. Morning Readiness Algorithm

```python
# Service: /python/coach/readiness_calculator.py

from datetime import datetime, timedelta
import pandas as pd

class ReadinessCalculator:
    """
    Calculates daily readiness score based on overnight recovery data
    """

    def calculate_readiness(
        self,
        user_id: str,
        date: datetime
    ) -> Dict:
        """
        Generate readiness score and recommendations
        """
        # Fetch last night's data
        last_night = self._get_sleep_data(user_id, date)
        yesterday = self._get_activity_data(user_id, date - timedelta(days=1))

        # Fetch baselines (7-day and 30-day averages)
        hrv_baseline_7d = self._get_hrv_baseline(user_id, days=7)
        hrv_baseline_30d = self._get_hrv_baseline(user_id, days=30)

        # Calculate component scores
        sleep_score = self._score_sleep(last_night)
        hrv_score = self._score_hrv(last_night['hrv'], hrv_baseline_7d, hrv_baseline_30d)
        recovery_score = self._score_recovery(yesterday['strain'], last_night['recovery_index'])

        # Calculate cumulative sleep debt
        sleep_debt = self._calculate_sleep_debt(user_id, days=7)

        # Weighted readiness score
        readiness_score = (
            sleep_score * 0.35 +
            hrv_score * 0.35 +
            recovery_score * 0.20 +
            (100 - sleep_debt) * 0.10
        )

        # Classify readiness
        if readiness_score >= 85:
            category = 'high'
            recommendation = 'Optimal for intense training (HIIT, heavy lifting)'
        elif readiness_score >= 70:
            category = 'moderate'
            recommendation = 'Good for moderate intensity work'
        elif readiness_score >= 50:
            category = 'low'
            recommendation = 'Active recovery recommended'
        else:
            category = 'recovery'
            recommendation = 'Rest or very light activity only'

        return {
            'date': date.isoformat(),
            'readiness_score': int(readiness_score),
            'category': category,
            'recommendation': recommendation,
            'components': {
                'sleep_score': sleep_score,
                'hrv_score': hrv_score,
                'recovery_score': recovery_score,
                'sleep_debt': sleep_debt
            },
            'detailed_insights': self._generate_insights(
                last_night, hrv_baseline_7d, sleep_debt
            )
        }
```

### 2. Personalized Daily Recommendations

```python
# Service: /python/coach/recommendation_engine.py

class RecommendationEngine:
    """
    Generates personalized daily recommendations based on readiness + protocols
    """

    def generate_daily_brief(
        self,
        user_id: str,
        date: datetime
    ) -> Dict:
        """
        Generate morning readiness brief with all recommendations
        """
        # Get readiness
        readiness = ReadinessCalculator().calculate_readiness(user_id, date)

        # Get active protocols
        protocols = self._get_active_protocols(user_id)

        # Get biomarker context
        biomarker_context = self._get_biomarker_context(user_id)

        # Generate training recommendations
        training = self._generate_training_recs(readiness, biomarker_context)

        # Generate supplement reminders
        supplements = self._generate_supplement_reminders(protocols, date)

        # Generate nutrition guidance
        nutrition = self._generate_nutrition_recs(readiness, biomarker_context)

        # Generate recovery tips
        recovery = self._generate_recovery_tips(readiness)

        return {
            'date': date.isoformat(),
            'readiness': readiness,
            'training': training,
            'supplements': supplements,
            'nutrition': nutrition,
            'recovery': recovery,
            'timestamp': datetime.now().isoformat()
        }

    def _generate_training_recs(self, readiness: Dict, context: Dict) -> Dict:
        """
        Generate training recommendations based on readiness and biomarker context
        """
        category = readiness['category']

        if category == 'high':
            return {
                'type': 'intense',
                'recommendation': 'Optimal day for HIIT or heavy strength training',
                'workout_suggestions': [
                    '30-min HIIT protocol (sprints, burpees, box jumps)',
                    '5x5 heavy compound lifts (squat, bench, deadlift)',
                    '45-min tempo run (85-90% max HR)'
                ],
                'reasoning': f"HRV +{readiness['components']['hrv_score']}% above baseline, "
                            f"sleep quality {readiness['components']['sleep_score']}/100"
            }

        elif category == 'low':
            return {
                'type': 'recovery',
                'recommendation': 'Active recovery only',
                'workout_suggestions': [
                    '20-30 min yoga or stretching',
                    'Zone 2 walk (HR <130 bpm)',
                    'Light swimming (20-30 min)'
                ],
                'reasoning': f"HRV -{100 - readiness['components']['hrv_score']}% below baseline, "
                            f"sleep debt {readiness['components']['sleep_debt']} minutes"
            }

        # ... other categories
```

### 3. Email Delivery System

**Technology**: Resend (email API)

```typescript
// Service: /lib/email/send-daily-brief.ts

import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

interface DailyBrief {
  user: UserProfile;
  readiness: ReadinessData;
  training: TrainingRec;
  supplements: SupplementReminder[];
  nutrition: NutritionRec;
}

async function sendDailyBrief(brief: DailyBrief) {
  const html = generateEmailHTML(brief);

  await resend.emails.send({
    from: 'Daily Coach <coach@healthintelligence.ch>',
    to: brief.user.email,
    subject: `Your Readiness: ${brief.readiness.category.toUpperCase()} (${brief.readiness.readiness_score}/100)`,
    html: html,
    scheduledAt: getTomorrowAt6AM() // Schedule for 6am local time
  });
}

function generateEmailHTML(brief: DailyBrief): string {
  return `
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .readiness-high { background: #10b981; color: white; }
        .readiness-moderate { background: #f59e0b; color: white; }
        .readiness-low { background: #ef4444; color: white; }
        .section { margin: 20px 0; padding: 15px; background: #f9fafb; border-radius: 8px; }
      </style>
    </head>
    <body>
      <div class="readiness-${brief.readiness.category}">
        <h1>Your Readiness: ${brief.readiness.readiness_score}/100</h1>
        <p>${brief.readiness.recommendation}</p>
      </div>

      <div class="section">
        <h2>🏋️ Training Guidance</h2>
        <p><strong>${brief.training.recommendation}</strong></p>
        <ul>
          ${brief.training.workout_suggestions.map(w => `<li>${w}</li>`).join('')}
        </ul>
        <p><em>${brief.training.reasoning}</em></p>
      </div>

      <div class="section">
        <h2>💊 Supplement Reminders</h2>
        ${brief.supplements.map(s => `
          <p><strong>${s.supplement_name}</strong> - ${s.dose}<br/>
          <em>${s.timing} | Day ${s.day_number}/${s.total_days}</em></p>
        `).join('')}
      </div>

      <div class="section">
        <h2>🥗 Nutrition Focus</h2>
        <p>${brief.nutrition.recommendation}</p>
      </div>

      <a href="https://app.healthintelligence.ch/dashboard"
         style="display: inline-block; padding: 12px 24px; background: #3b82f6;
                color: white; text-decoration: none; border-radius: 6px; margin-top: 20px;">
        View Full Dashboard
      </a>
    </body>
    </html>
  `;
}
```

### 4. Background Jobs & Scheduling

**Technology**: Inngest (background job orchestration)

```typescript
// Service: /lib/jobs/daily-coach-jobs.ts

import { Inngest } from 'inngest';

const inngest = new Inngest({ name: 'Health Intelligence' });

// Job 1: Sync wearable data (runs every 2 hours)
export const syncWearables = inngest.createFunction(
  { name: 'Sync Wearable Data' },
  { cron: '0 */2 * * *' }, // Every 2 hours
  async ({ step }) => {
    const users = await step.run('fetch-active-users', async () => {
      return getActiveCoachUsers();
    });

    for (const user of users) {
      await step.run(`sync-${user.id}`, async () => {
        await syncUserWearableData(user.id);
      });
    }
  }
);

// Job 2: Generate daily briefs (runs at 5:30am Swiss time)
export const generateDailyBriefs = inngest.createFunction(
  { name: 'Generate Daily Briefs' },
  { cron: '30 5 * * *' }, // 5:30am UTC+1 (Swiss time)
  async ({ step }) => {
    const users = await step.run('fetch-coach-users', async () => {
      return getActiveCoachUsers();
    });

    for (const user of users) {
      await step.run(`generate-brief-${user.id}`, async () => {
        const brief = await generateDailyBrief(user.id, new Date());
        await sendDailyBrief(brief);
        await saveDailyReadiness(user.id, brief.readiness);
      });
    }
  }
);

// Job 3: Protocol compliance tracking (runs daily at 9pm)
export const trackProtocolCompliance = inngest.createFunction(
  { name: 'Track Protocol Compliance' },
  { cron: '0 21 * * *' }, // 9pm daily
  async ({ step }) => {
    const protocols = await step.run('fetch-active-protocols', async () => {
      return getActiveProtocols();
    });

    for (const protocol of protocols) {
      await step.run(`check-compliance-${protocol.id}`, async () => {
        const didTake = await checkSupplementTaken(protocol.id, new Date());
        await updateProtocolCompliance(protocol.id, didTake);
      });
    }
  }
);
```

---

## Tech Stack Summary

### Frontend
| Technology | Purpose | Rationale |
|------------|---------|-----------|
| **Next.js 14** | React framework (App Router) | Server components, API routes, SEO-friendly |
| **TypeScript** | Type safety | Fewer bugs, better DX |
| **TailwindCSS** | Styling | Rapid UI development |
| **shadcn/ui** | Component library | High-quality, accessible components |
| **Recharts** | Data visualization | Beautiful charts for biomarker trends |

### Backend
| Technology | Purpose | Rationale |
|------------|---------|-----------|
| **Next.js API Routes** | API layer | Collocated with frontend, simpler deployment |
| **Supabase** | Auth + Database + Storage | Batteries-included, great DX |
| **PostgreSQL 15** | Relational database | Rock-solid, ACID compliance |
| **TimescaleDB** | Time-series extension | Efficient wearable data queries |
| **Python (FastAPI)** | Analysis engine | Better ML/data libraries than Node.js |

### AI & Analysis
| Technology | Purpose | Cost per User |
|------------|---------|---------------|
| **Anthropic Claude 3.5 Sonnet** | Biomarker interpretation | CHF 3-5 per report |
| **OpenAI GPT-4 Turbo** | OCR parsing fallback | CHF 2-4 per report |
| **Google Cloud Vision** | Primary OCR | CHF 1.50 per report |

### Infrastructure
| Technology | Purpose | Cost |
|------------|---------|------|
| **Vercel** | Frontend hosting | CHF 20/month (Pro plan) |
| **Railway** | Python backend hosting | CHF 20-50/month |
| **Supabase** | Database + Auth + Storage | CHF 25/month (Pro plan) |
| **Inngest** | Background jobs | CHF 0-50/month (usage-based) |

### Integrations
| Service | Purpose | Cost |
|---------|---------|------|
| **Oura API** | Wearable data | Free (users need Oura subscription) |
| **Apple HealthKit** | Wearable data | Free |
| **Whoop API** | Wearable data | Free (users need Whoop subscription) |
| **Stripe** | Payments | 2.5% + CHF 0.30 per transaction |
| **Resend** | Email delivery | CHF 20/month (10K emails) |

**Total Monthly Infrastructure**: CHF 100-200 (scales with users)

---

## Data Security & Privacy

### GDPR Compliance

**Data Storage**:
- All user data stored in EU region (Supabase Frankfurt datacenter)
- Encrypted at rest (AES-256)
- Encrypted in transit (TLS 1.3)

**Data Retention**:
- Lab reports: Retained indefinitely (user can delete)
- Wearable data: 2 years rolling window
- Analysis reports: Retained indefinitely
- Deleted users: All data purged within 30 days

**User Rights**:
- Data export (JSON format)
- Data deletion (immediate + 30-day grace period)
- Data portability (export to PDF/CSV)

### API Security

**Authentication**:
- JWT tokens (Supabase Auth)
- Row-level security (RLS) policies on all tables
- API rate limiting (100 requests/minute per user)

**Wearable OAuth Tokens**:
- Stored encrypted in database (AES-256)
- Rotated automatically when near expiration
- Revoked immediately on user disconnect

---

## Monitoring & Observability

### Application Monitoring

**Tool**: Sentry (error tracking)
- Real-time error alerts
- Performance monitoring
- User session replay

**Metrics**:
- API response times (P50, P95, P99)
- Database query performance
- OCR processing success rate
- AI analysis quality (user feedback)

### Business Metrics

**Tool**: PostHog (product analytics)
- User activation funnel
- Feature usage tracking
- Retention cohorts
- A/B testing framework

---

## Scalability Considerations

### Current Architecture (0-5K users)
- Vercel (serverless, auto-scales)
- Supabase (scales to 100GB DB)
- Railway (Python backend, 2-4 vCPU)

**Cost**: CHF 200-500/month

### Future Architecture (5K-50K users)
- Migrate Python backend to AWS Lambda (lower cost at scale)
- Add Redis for caching (reduce DB load)
- CDN for PDF reports (CloudFlare)
- Queue system for OCR jobs (AWS SQS)

**Cost**: CHF 1,000-3,000/month

---

## Development Workflow

### Local Development

```bash
# Frontend (Next.js)
cd frontend
npm install
npm run dev # Runs on http://localhost:3000

# Backend (Python)
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload # Runs on http://localhost:8000

# Database (Supabase local)
npx supabase start
npx supabase db reset # Reset with seed data
```

### Deployment

**Frontend**: Vercel (Git push → auto-deploy)
**Backend**: Railway (Git push → auto-deploy)
**Database**: Supabase (managed, auto-backups)

### CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run build
      - run: npm run test
      - uses: amondnet/vercel-action@v20 # Deploy to Vercel

  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install -r requirements.txt
      - run: pytest
      - run: railway up # Deploy to Railway
```

---

## Next Steps

See [06-mvp-scope.md](./06-mvp-scope.md) for detailed MVP feature breakdown and development timeline.
