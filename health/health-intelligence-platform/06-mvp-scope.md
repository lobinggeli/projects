# MVP Scope & Development Plan

**Last Updated**: February 9, 2026

## Overview

This document defines the Minimum Viable Product (MVP) scope for the health intelligence platform, including must-have features, out-of-scope items, technical implementation details, and a 16-week development timeline.

**MVP Philosophy**: Build the smallest viable product that delivers the core value proposition (lab + wearable analysis → actionable insights) and validates product-market fit.

---

## MVP Success Criteria

Before launching publicly, the MVP must achieve:

1. **20 beta users** successfully onboard and receive analysis
2. **80%+ satisfaction** (NPS > 50)
3. **70%+ conversion** from one-time analysis to Daily Coach subscription (within 90 days)
4. **CHF 6-15 variable cost** per analysis (sustainable unit economics)
5. **<24 hour** average time from upload to report delivery

---

## In-Scope: Must-Have Features

### 1. User Authentication & Onboarding

**Features**:
- Email + password signup
- OAuth (Google, Apple Sign-In)
- Email verification
- Password reset flow
- Basic profile setup (name, date of birth, weight, gender)

**User Flow**:
```
1. User lands on homepage → "Get Started"
2. Sign up with email or OAuth
3. Email verification (if email/password)
4. Welcome screen → "Upload your first lab report"
5. Quick tutorial (3-step: Upload → Connect → Analyze)
```

**Technical Implementation**:
- Supabase Auth (handles all auth logic)
- Next.js protected routes (middleware)
- Profile stored in `users` table

**Timeline**: Week 1-2 (4 days)

---

### 2. Lab Report Upload & OCR

**Features**:
- Drag & drop file upload (PDF, JPEG, PNG)
- Multi-file upload (up to 10 files, max 50MB total)
- Upload progress indicator
- File preview (thumbnails)
- Manual biomarker entry (fallback if OCR fails)

**User Flow**:
```
1. User clicks "Upload Lab Report"
2. Drag & drop files OR click to browse
3. Files upload to Supabase Storage (progress bar)
4. OCR processing begins (status: "Processing...")
5. Email notification when complete (24-48h)
6. User returns to view results
```

**OCR Pipeline**:
```typescript
// Simplified MVP OCR flow
async function processLabReport(fileUrl: string, userId: string) {
  // Step 1: Extract text using Google Cloud Vision
  const ocrText = await extractTextWithGoogleVision(fileUrl);

  // Step 2: Parse biomarkers using GPT-4
  const biomarkers = await parseBiomarkersWithGPT4(ocrText);

  // Step 3: Validate & normalize
  const validated = validateBiomarkers(biomarkers);

  // Step 4: Store in database
  await saveBiomarkers(userId, validated);

  // Step 5: Trigger analysis
  await triggerAnalysisJob(userId);

  return validated;
}
```

**Fallback**: If OCR confidence < 80%, email user to manually enter biomarkers (admin panel)

**Technical Implementation**:
- Google Cloud Vision API (OCR)
- OpenAI GPT-4 Turbo (biomarker parsing)
- Supabase Storage (file storage)
- Inngest (background job orchestration)

**Timeline**: Week 3-4 (8 days)

---

### 3. Wearable Integration (Oura Ring Only for MVP)

**Features**:
- OAuth connection to Oura Ring
- Fetch last 90 days of data
- Daily sync (automatic)
- Disconnect wearable
- View sync status

**User Flow**:
```
1. User clicks "Connect Oura Ring"
2. Redirected to Oura OAuth page
3. User authorizes access
4. Redirected back to app
5. Background sync begins (fetch 90 days)
6. Confirmation: "Oura Ring connected successfully"
```

**Data Retrieved**:
- Daily sleep (duration, efficiency, deep sleep, REM)
- Daily readiness score
- HRV (nocturnal average)
- Resting heart rate
- Activity (steps, calories)

**Technical Implementation**:
```typescript
// Oura OAuth callback
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const code = searchParams.get('code');

  // Exchange code for access token
  const { access_token, refresh_token } = await exchangeOuraCode(code);

  // Save tokens (encrypted)
  await saveWearableConnection({
    user_id: getCurrentUserId(),
    device_type: 'oura',
    access_token: encrypt(access_token),
    refresh_token: encrypt(refresh_token)
  });

  // Trigger initial sync
  await inngest.send({
    name: 'wearable/sync',
    data: { userId: getCurrentUserId(), deviceType: 'oura' }
  });

  return redirect('/dashboard?connected=oura');
}
```

**Out of Scope for MVP**:
- Apple Health (Phase 2)
- Whoop (Phase 2)
- CGM (Phase 2)

**Timeline**: Week 5-6 (7 days)

---

### 4. AI Analysis Engine

**Features**:
- Biomarker interpretation (using 17 frameworks)
- Severity classification (optimal/borderline/deficient/elevated/critical)
- Wearable correlation analysis
- Supplement protocol generation
- Lifestyle recommendations
- Prioritized action plan (top 3-5 interventions)

**Analysis Pipeline**:
```python
# Simplified MVP analysis flow
class AnalysisEngine:
    def generate_analysis(self, user_id: str) -> Dict:
        # Step 1: Fetch biomarkers
        biomarkers = fetch_biomarkers(user_id)

        # Step 2: Fetch wearable data (last 90 days)
        wearable_data = fetch_wearable_data(user_id, days=90)

        # Step 3: Interpret each biomarker
        interpretations = []
        for biomarker in biomarkers:
            interpretation = self.interpret_biomarker(biomarker)
            interpretations.append(interpretation)

        # Step 4: Find correlations
        correlations = self.find_correlations(biomarkers, wearable_data)

        # Step 5: Generate protocols
        protocols = []
        for biomarker in biomarkers:
            if biomarker['severity'] in ['deficient', 'critical']:
                protocol = self.generate_protocol(biomarker)
                protocols.append(protocol)

        # Step 6: Prioritize interventions
        prioritized = self.prioritize_protocols(protocols, correlations)

        # Step 7: Generate report
        report = {
            'user_id': user_id,
            'biomarkers': interpretations,
            'correlations': correlations,
            'protocols': prioritized,
            'executive_summary': self.generate_summary(interpretations, correlations)
        }

        return report
```

**AI Models Used**:
- **Claude 3.5 Sonnet** (primary) - Biomarker interpretation, protocol generation
- **GPT-4 Turbo** (fallback) - If Claude API fails

**Prompting Strategy**:
```python
INTERPRETATION_PROMPT = """
You are a functional medicine AI analyst. Analyze this biomarker using the following frameworks:

{frameworks}

Biomarker Data:
- Name: {biomarker_name}
- Value: {value} {unit}
- Reference Range: {ref_range}
- User Age: {age}, Gender: {gender}, Weight: {weight}kg

Provide:
1. **Severity**: Optimal / Borderline / Deficient / Elevated / Critical
2. **Context**: What this biomarker measures (1-2 sentences)
3. **Clinical Significance**: Why this matters for health/performance
4. **Root Causes**: 3-5 potential reasons for out-of-range value
5. **Downstream Effects**: How this impacts other systems
6. **Intervention Priority**: 1-5 (5 = highest priority)

Return as structured JSON.
"""
```

**Quality Control**:
- Human review for first 50 analyses (validate AI output)
- User feedback loop ("Was this analysis helpful?")
- Flag low-confidence results for manual review

**Timeline**: Week 7-10 (15 days)

---

### 5. Report Generation (PDF + Web Dashboard)

**Features**:

#### PDF Report (Comprehensive, 20-30 pages)
- Title page (user name, date)
- Executive summary (1 page)
- Critical findings (2-3 pages)
- All biomarkers (interpretation for each)
- Wearable correlations (charts + explanations)
- Prioritized action plan (protocols)
- Retest schedule
- Footer: "Generated by Health Intelligence Platform"

#### Web Dashboard
- Overview page (key metrics, readiness score)
- Biomarkers page (list all with trends)
- Wearables page (HRV, sleep, activity charts)
- Protocols page (active protocols with progress)
- Reports page (download past PDFs)

**User Flow**:
```
1. Analysis completes (email notification)
2. User clicks "View Report"
3. Lands on web dashboard (overview page)
4. Can download PDF report
5. Can view individual biomarkers (detailed view)
6. Can view wearable trends (charts)
7. Can view protocols (supplement recommendations)
```

**Technical Implementation**:
```typescript
// PDF generation using PDFKit
import PDFDocument from 'pdfkit';

async function generatePDF(analysisData: AnalysisReport) {
  const doc = new PDFDocument({ size: 'A4' });

  // Title Page
  doc.fontSize(24).text('Comprehensive Health Analysis');
  doc.fontSize(12).text(`Prepared for: ${analysisData.user.name}`);

  // Executive Summary
  doc.addPage();
  doc.fontSize(18).text('Executive Summary');
  doc.fontSize(11).text(analysisData.executive_summary);

  // Biomarkers Section
  doc.addPage();
  doc.fontSize(18).text('Biomarker Analysis');
  analysisData.biomarkers.forEach(b => {
    doc.fontSize(14).text(b.name);
    doc.fontSize(11).text(b.interpretation);
    doc.moveDown();
  });

  // Action Plan
  doc.addPage();
  doc.fontSize(18).text('Prioritized Action Plan');
  analysisData.protocols.forEach((p, i) => {
    doc.fontSize(14).text(`Priority ${i + 1}: ${p.biomarker_name}`);
    doc.fontSize(11).text(p.protocol_description);
    doc.moveDown();
  });

  // Save to Supabase Storage
  const pdfBuffer = await streamToBuffer(doc);
  const fileName = `reports/${analysisData.user_id}/${Date.now()}-analysis.pdf`;
  await supabase.storage.from('reports').upload(fileName, pdfBuffer);

  return fileName;
}
```

**Charts** (Web Dashboard):
- Recharts library (React)
- HRV trend (line chart)
- Sleep quality trend (line chart)
- Biomarker trends over time (line chart)

**Timeline**: Week 11-12 (8 days)

---

### 6. Payment Processing (Stripe)

**Features**:
- One-time payment (CHF 149 analysis)
- Subscription payment (CHF 79/month Daily Coach)
- Upgrade/downgrade flow
- Cancel subscription
- Payment history
- Invoice generation

**Pricing Tiers** (MVP):
1. **Comprehensive Analysis**: CHF 149 (one-time)
2. **Daily AI Coach**: CHF 79/month (subscription)

**User Flow**:
```
1. User completes signup
2. "Choose Your Plan" page
3. Select plan → Redirected to Stripe Checkout
4. Enter payment details
5. Payment confirmed → Redirected to dashboard
6. Analysis begins
```

**Technical Implementation**:
```typescript
// Stripe Checkout Session
import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function createCheckoutSession(userId: string, priceId: string) {
  const session = await stripe.checkout.sessions.create({
    customer_email: getUserEmail(userId),
    payment_method_types: ['card'],
    line_items: [{ price: priceId, quantity: 1 }],
    mode: priceId.includes('subscription') ? 'subscription' : 'payment',
    success_url: `${process.env.APP_URL}/payment/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.APP_URL}/payment/canceled`,
    metadata: { user_id: userId }
  });

  return session.url;
}

// Webhook handler (payment confirmation)
export async function handleStripeWebhook(event: Stripe.Event) {
  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object;
      await activateUserSubscription(session.metadata.user_id, session.subscription);
      break;

    case 'invoice.payment_succeeded':
      // Handle recurring payment success
      break;

    case 'customer.subscription.deleted':
      // Handle subscription cancellation
      await deactivateUserSubscription(event.data.object.id);
      break;
  }
}
```

**Out of Scope for MVP**:
- Annual subscription discounts (Phase 2)
- Premium tier (Phase 2)
- Referral credits (Phase 2)

**Timeline**: Week 13-14 (6 days)

---

### 7. Email Notifications

**Features**:
- Welcome email (signup)
- Analysis complete notification
- Report ready notification
- Weekly summary (if subscribed to Daily Coach)
- Payment receipts

**Email Templates** (Resend + React Email):
```typescript
// Welcome Email
export function WelcomeEmail({ userName }: { userName: string }) {
  return (
    <Html>
      <Head />
      <Body>
        <Container>
          <Heading>Welcome to Health Intelligence, {userName}!</Heading>
          <Text>
            You're just 2 steps away from getting your comprehensive health analysis:
          </Text>
          <ol>
            <li>Upload your lab reports (PDF or photo)</li>
            <li>Connect your Oura Ring</li>
          </ol>
          <Button href="https://app.healthintelligence.ch/upload">
            Upload Lab Report Now
          </Button>
        </Container>
      </Body>
    </Html>
  );
}

// Analysis Complete Email
export function AnalysisCompleteEmail({ userName, reportUrl }: Props) {
  return (
    <Html>
      <Head />
      <Body>
        <Container>
          <Heading>Your Health Analysis is Ready, {userName}!</Heading>
          <Text>
            We've analyzed your lab data + Oura Ring data and generated your
            comprehensive report with personalized recommendations.
          </Text>
          <Button href={reportUrl}>View Your Report</Button>
        </Container>
      </Body>
    </Html>
  );
}
```

**Timeline**: Week 14 (2 days)

---

## Out of Scope: Phase 2+ Features

### Not in MVP (Build Later)

1. **Daily AI Coach** (Phase 2, Month 4-6)
   - Morning readiness briefs
   - Personalized training recommendations
   - Dynamic supplement reminders
   - Nutrition guidance

2. **Apple Health Integration** (Phase 2)
   - HealthKit integration
   - XML upload fallback

3. **Whoop Integration** (Phase 2)

4. **CGM Integration** (Phase 2)

5. **Mobile App** (Phase 3)
   - iOS app (Month 10-12)
   - Android app (Year 2)

6. **Advanced Features** (Phase 3+)
   - Biomarker predictions
   - Doctor-sharable reports
   - Community features (forum, user sharing)
   - Goal setting & tracking
   - Genetic data integration

7. **Premium Tier** (Phase 2)
   - CHF 129/month with quarterly analysis included
   - Priority support
   - Advanced protocols

8. **Referral Program** (Phase 2, Month 4)

9. **Multilingual Support** (Phase 3)
   - German translations
   - French translations

---

## MVP Tech Stack

### Frontend
```json
{
  "framework": "Next.js 14 (App Router)",
  "language": "TypeScript",
  "styling": "TailwindCSS + shadcn/ui",
  "charts": "Recharts",
  "forms": "React Hook Form + Zod",
  "state": "React Context + Server Components",
  "deployment": "Vercel"
}
```

### Backend
```json
{
  "api": "Next.js API Routes (App Router)",
  "database": "PostgreSQL 15 (Supabase)",
  "auth": "Supabase Auth",
  "storage": "Supabase Storage (S3-compatible)",
  "background_jobs": "Inngest",
  "python_engine": "FastAPI (deployed on Railway)"
}
```

### AI & External Services
```json
{
  "ocr": "Google Cloud Vision API",
  "ai_primary": "Anthropic Claude 3.5 Sonnet",
  "ai_fallback": "OpenAI GPT-4 Turbo",
  "wearable_api": "Oura Ring API v2",
  "payments": "Stripe",
  "email": "Resend"
}
```

### DevOps & Monitoring
```json
{
  "hosting_frontend": "Vercel",
  "hosting_backend": "Railway",
  "database": "Supabase (managed PostgreSQL)",
  "monitoring": "Sentry",
  "analytics": "PostHog",
  "error_tracking": "Sentry"
}
```

---

## Development Timeline (16 Weeks)

### Week 1-2: Foundation (10 days)
**Deliverables**:
- Project setup (Next.js, TypeScript, TailwindCSS)
- Supabase setup (database, auth, storage)
- Database schema (users, lab_reports, biomarkers, wearable_metrics)
- Authentication flows (signup, login, password reset)
- Basic dashboard layout

**Team**: 1 full-stack developer

---

### Week 3-4: Lab Upload & OCR (10 days)
**Deliverables**:
- File upload component (drag & drop)
- Supabase Storage integration
- Google Cloud Vision OCR integration
- GPT-4 biomarker parsing
- Background job setup (Inngest)
- Manual biomarker entry (admin panel fallback)

**Team**: 1 full-stack developer + contract OCR specialist (optional)

---

### Week 5-6: Oura Integration (8 days)
**Deliverables**:
- Oura OAuth flow
- Oura API client (fetch sleep, HRV, readiness)
- Background sync job (daily)
- Wearable data storage (TimescaleDB tables)
- Connection status UI

**Team**: 1 full-stack developer

---

### Week 7-10: AI Analysis Engine (20 days)
**Deliverables**:
- Python FastAPI service (hosted on Railway)
- Claude 3.5 integration (biomarker interpretation)
- Correlation analysis algorithm
- Protocol generation logic
- 17 health frameworks implementation
- Prioritization algorithm
- Quality control (human review for first 50)

**Team**: 1 full-stack developer + 1 health/data analyst (contract)

---

### Week 11-12: Report Generation (10 days)
**Deliverables**:
- PDF generation (PDFKit)
- Web dashboard (overview, biomarkers, wearables, protocols)
- Charts (Recharts - HRV, sleep trends)
- Report download functionality
- Report history page

**Team**: 1 full-stack developer + 1 designer (contract, 3 days)

---

### Week 13-14: Payments & Onboarding (8 days)
**Deliverables**:
- Stripe integration (one-time + subscription)
- Checkout flows
- Webhook handling (payment confirmation)
- Subscription management (upgrade, cancel)
- Payment history page
- Onboarding flow (welcome tutorial)

**Team**: 1 full-stack developer

---

### Week 15-16: Testing & Beta Launch (10 days)
**Deliverables**:
- End-to-end testing (user flows)
- Bug fixes
- Performance optimization
- Beta user recruitment (20-30 users)
- Beta launch (invite-only)
- Feedback collection
- Iteration based on feedback

**Team**: 1 full-stack developer + founder (user interviews)

---

## MVP Development Cost Estimate

### Team (Assuming Founder Does Development)

**Scenario 1: Founder Builds (Technical Founder)**
- **Cost**: CHF 0 (opportunity cost only)
- **Timeline**: 16 weeks (full-time)
- **Recommended if**: Founder has full-stack experience

**Scenario 2: Contract Developer**
- **Cost**: CHF 60-80K (CHF 10-13K/month × 6 months)
- **Timeline**: 20 weeks (account for communication overhead)
- **Recommended if**: Founder non-technical or lacks time

**Scenario 3: Hybrid (Founder + Contract Developer)**
- **Cost**: CHF 30-40K (contract developer part-time, 20 hours/week)
- **Timeline**: 18 weeks
- **Recommended if**: Founder technical but needs velocity

---

### External Services (MVP Phase, Months 1-4)

| Service | Cost (CHF/month) | Annual (CHF) |
|---------|------------------|--------------|
| **Vercel** (Pro plan) | 20 | 240 |
| **Railway** (Python backend) | 20-50 | 360 |
| **Supabase** (Pro plan) | 25 | 300 |
| **Google Cloud** (OCR) | 50-150 | 900 |
| **Anthropic API** (Claude) | 100-300 | 1,800 |
| **OpenAI API** (GPT-4 fallback) | 50-150 | 900 |
| **Stripe** (fees, 2.5%) | ~100-200 | 1,500 |
| **Resend** (email) | 20 | 240 |
| **Inngest** (background jobs) | 0-50 | 300 |
| **Sentry** (monitoring) | 0 (free tier) | 0 |
| **PostHog** (analytics) | 0 (free tier) | 0 |
| **Total** | **CHF 385-965/month** | **CHF 6,540** |

**Note**: Variable costs (API usage) scale with users but remain low per user (CHF 6-15)

---

### One-Time Costs

| Item | Cost (CHF) |
|------|------------|
| **Designer** (contract, 3 days) | 3,000 |
| **Legal** (terms of service, privacy policy) | 2,000 |
| **Domain & branding** | 500 |
| **Health analyst** (contract, review frameworks) | 3,000 |
| **Total** | **CHF 8,500** |

---

### Total MVP Cost Summary

| Scenario | Development | Services | One-Time | Total |
|----------|-------------|----------|----------|-------|
| **Founder Builds** | CHF 0 | CHF 6,540 | CHF 8,500 | **CHF 15,040** |
| **Contract Dev (Full)** | CHF 60,000 | CHF 6,540 | CHF 8,500 | **CHF 75,040** |
| **Hybrid** | CHF 30,000 | CHF 6,540 | CHF 8,500 | **CHF 45,040** |

**Recommended**: Founder builds if technical (CHF 15K investment)

---

## Beta Launch Plan (Week 15-16)

### Objectives
- Validate core value proposition
- Collect feedback for iteration
- Build case studies for marketing
- Convert beta users to paying customers

### Beta User Profile
- Swiss-based
- Currently doing quarterly blood work
- Own Oura Ring or Apple Watch
- Active in biohacking communities
- Willing to provide detailed feedback

### Recruitment Channels
- Reddit r/Biohackers: "I'm building a health intelligence platform - looking for 20 beta testers"
- Facebook "Biohacking Schweiz"
- LinkedIn (personal outreach to 50 Swiss biohackers)
- Oura Ring community forums

### Beta Offer
- **Free comprehensive analysis** (CHF 149 value)
- **3 months free Daily Coach** when Phase 2 launches
- **Lifetime 30% discount** (CHF 55/month vs CHF 79)
- **Influence roadmap** (feedback shapes product)

### Beta Launch Checklist

**Week 15**:
- [ ] Recruit 20-30 beta users (email list)
- [ ] Send beta invite email with instructions
- [ ] Schedule 15-min onboarding calls (optional)
- [ ] Set up feedback collection (Typeform survey)

**Week 16**:
- [ ] Users upload labs + connect Oura
- [ ] Monitor OCR success rate (target: >80%)
- [ ] Generate first 10 analyses (manual QA)
- [ ] Collect feedback (survey + 1-on-1 calls)
- [ ] Iterate based on feedback
- [ ] Prepare for public launch (Month 4)

### Success Metrics (Beta)
- [ ] 80%+ users complete onboarding
- [ ] NPS > 50
- [ ] 3+ testimonials for marketing
- [ ] <24h average analysis turnaround
- [ ] <10% OCR failure rate
- [ ] 70%+ users say they'd pay CHF 149

---

## Post-MVP: Phase 2 Roadmap (Months 5-6)

### Daily AI Coach (Build After MVP Validation)

**Timeline**: 8 weeks (concurrent with MVP growth)

**Features**:
- Morning readiness calculation (HRV, sleep, recovery)
- Personalized training recommendations
- Supplement protocol reminders
- Weekly progress summaries

**Development**:
- Readiness algorithm (Python)
- Email generation & scheduling (Resend)
- Background jobs (Inngest, runs at 6am daily)

**Launch**: Month 5 (offer 14-day free trial to existing customers)

---

## Risk Mitigation

### Risk 1: OCR Accuracy Too Low

**Mitigation**:
- Start with manual review (first 50 analyses)
- Build admin panel for manual biomarker entry
- Iterate prompts to improve parsing
- Add confidence scoring (flag low-confidence results)

**Fallback**: Offer "manual entry" option for users (CHF 129 vs CHF 149)

---

### Risk 2: AI Analysis Quality Issues

**Mitigation**:
- Health analyst reviews first 50 analyses
- User feedback loop ("Was this helpful?")
- A/B test Claude vs GPT-4 (track satisfaction)
- Build prompt library (tested prompts for each biomarker)

**Fallback**: Human review for complex cases (charge premium, CHF 199)

---

### Risk 3: Low Oura Connection Rate

**Mitigation**:
- Clear instructions (video tutorial)
- Support chat (Intercom)
- Offer manual data entry (CSV upload)

**Fallback**: Support Apple Health XML upload (manual process for MVP)

---

### Risk 4: Slow Analysis Turnaround (>48h)

**Mitigation**:
- Optimize OCR pipeline (parallel processing)
- Pre-compute wearable trends (nightly batch job)
- Scale infrastructure (Railway, vertical scaling)

**Fallback**: Set expectations ("48-72h for first analysis, <24h for retest")

---

## Success Metrics (MVP)

### Product Metrics

| Metric | Target |
|--------|--------|
| **User Activation** (upload + connect) | 80%+ |
| **Analysis Completion Rate** | 95%+ |
| **Average Turnaround Time** | <24h |
| **OCR Success Rate** | >80% |
| **User Satisfaction (NPS)** | >50 |
| **Analysis → Daily Coach Conversion** | 60-70% (within 90 days) |

### Technical Metrics

| Metric | Target |
|--------|--------|
| **API Response Time (P95)** | <500ms |
| **OCR Processing Time** | <5 min |
| **Analysis Generation Time** | <30 min |
| **Uptime** | >99.5% |
| **Error Rate** | <1% |

### Business Metrics

| Metric | Target (Month 4) |
|--------|------------------|
| **Total Users** | 100-150 |
| **Paying Customers** | 70-100 |
| **MRR** | CHF 3,000-5,000 |
| **Variable Cost per User** | CHF 6-15 |
| **Gross Margin** | >85% |

---

## Tools & Resources

### Design Resources
- **Figma**: UI/UX design (free tier)
- **shadcn/ui**: Component library (open source)
- **Lucide Icons**: Icon set (free)
- **Unsplash**: Stock photos (free)

### Development Tools
- **VS Code**: IDE
- **GitHub**: Version control
- **Cursor**: AI-powered code editor (optional)
- **Postman**: API testing

### Documentation
- **Notion**: Internal docs, roadmap
- **GitHub Wiki**: Technical docs
- **Loom**: Video tutorials for users

### Communication
- **Intercom**: Support chat (free tier)
- **Cal.com**: Meeting scheduling (free)
- **Discord**: Beta user community (free)

---

## Next Steps

### Week 0 (Pre-Development)
1. [ ] Set up development environment
2. [ ] Purchase domain (healthintelligence.ch)
3. [ ] Create Supabase project
4. [ ] Create Vercel project
5. [ ] Create Stripe account
6. [ ] Set up API keys (Google Cloud, Anthropic, OpenAI, Oura)
7. [ ] Design initial mockups (Figma)

### Week 1 (Kickoff)
1. [ ] Initialize Next.js project
2. [ ] Set up database schema
3. [ ] Implement authentication
4. [ ] Build basic dashboard layout
5. [ ] Deploy to Vercel (staging environment)

### Week 2-16 (Execution)
Follow timeline above, focusing on:
- Weekly demos (show progress)
- Daily standups (if team)
- Bi-weekly retros (iterate process)
- Code reviews (quality control)

### Week 17+ (Post-MVP)
1. [ ] Beta launch (20-30 users)
2. [ ] Collect feedback
3. [ ] Iterate based on feedback
4. [ ] Prepare for public launch (Month 4)
5. [ ] Start Phase 2 development (Daily Coach)

---

## Appendix: MVP Database Schema

```sql
-- Core tables for MVP

-- Users (managed by Supabase Auth + extended profile)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  subscription_tier TEXT DEFAULT 'none', -- 'none', 'analysis', 'daily_coach'
  subscription_status TEXT DEFAULT 'inactive',
  stripe_customer_id TEXT,
  weight_kg NUMERIC(5,2),
  date_of_birth DATE,
  gender TEXT
);

-- Lab Reports
CREATE TABLE lab_reports (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  uploaded_at TIMESTAMPTZ DEFAULT NOW(),
  file_url TEXT NOT NULL,
  test_date DATE,
  ocr_status TEXT DEFAULT 'pending',
  ocr_confidence NUMERIC(3,2)
);

-- Biomarkers
CREATE TABLE biomarkers (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  lab_report_id UUID REFERENCES lab_reports(id),
  test_date DATE NOT NULL,
  biomarker_name TEXT NOT NULL,
  value NUMERIC(10,4) NOT NULL,
  unit TEXT NOT NULL,
  reference_range_min NUMERIC(10,4),
  reference_range_max NUMERIC(10,4),
  severity TEXT, -- 'optimal', 'borderline', 'deficient', 'elevated', 'critical'
  interpretation TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Wearable Connections
CREATE TABLE wearable_connections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  device_type TEXT NOT NULL, -- 'oura' only for MVP
  access_token TEXT NOT NULL,
  refresh_token TEXT,
  connected_at TIMESTAMPTZ DEFAULT NOW(),
  last_sync_at TIMESTAMPTZ,
  UNIQUE(user_id, device_type)
);

-- Wearable Data (time-series)
CREATE TABLE wearable_metrics (
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  device_type TEXT NOT NULL,
  metric_date DATE NOT NULL,
  metric_type TEXT NOT NULL, -- 'sleep_duration', 'hrv', 'resting_hr', etc.
  value NUMERIC(10,4) NOT NULL,
  unit TEXT,
  metadata JSONB,
  PRIMARY KEY (user_id, metric_date, device_type, metric_type)
);

-- Analysis Reports
CREATE TABLE analysis_reports (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  pdf_url TEXT,
  biomarker_summary JSONB,
  correlations JSONB,
  protocols JSONB,
  status TEXT DEFAULT 'generating' -- 'generating', 'ready', 'failed'
);

-- Protocols
CREATE TABLE protocols (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  analysis_report_id UUID REFERENCES analysis_reports(id),
  biomarker_name TEXT NOT NULL,
  supplement_name TEXT NOT NULL,
  dose TEXT NOT NULL,
  start_date DATE DEFAULT CURRENT_DATE,
  retest_date DATE,
  status TEXT DEFAULT 'active'
);
```

---

## Summary

**MVP Timeline**: 16 weeks from start to beta launch

**MVP Cost**: CHF 15K-75K (depending on development approach)

**Core Features**:
1. Lab upload + OCR (any format)
2. Oura Ring integration
3. AI-powered analysis (17 frameworks)
4. PDF + web dashboard reports
5. Supplement protocols
6. Payment processing (one-time + subscription)

**Success Criteria**: 20 beta users, 80%+ satisfaction, <24h turnaround, CHF 6-15 variable cost

**Phase 2** (Months 5-6): Daily AI Coach with morning readiness briefs

**Launch Strategy**: Beta (Month 4) → Public Launch (Month 5) → Daily Coach (Month 6)
