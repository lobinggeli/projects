# CLAUDE.md

This file defines how Claude should structure and proceed when gathering information.

## Information Gathering Process

### 1. Initial Assessment

Before gathering information:
- Identify the core question or objective
- Determine the scope and boundaries of the inquiry
- Clarify any ambiguous terms or requirements with the user

### 2. Source Identification

When identifying sources:
- Prioritize authoritative and reliable sources
- Consider multiple perspectives when applicable
- Note the recency and relevance of information

### 3. Structured Collection

Organize gathered information using:
- **Categories**: Group related information logically
- **Hierarchies**: Structure from general to specific
- **Cross-references**: Link related concepts

### 4. Verification Steps

For each piece of information:
- Assess credibility of the source
- Check for consistency across sources
- Flag uncertainties or conflicting data

### 5. Synthesis and Presentation

When presenting findings:
- Summarize key points first
- Provide supporting details in structured sections
- Highlight gaps or limitations in available information
- Offer actionable conclusions when appropriate

## Output Format

### Standard Structure

```
## Overview
[Brief summary of findings]

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Detailed Analysis
[Expanded information organized by topic]

## Limitations
[Known gaps or uncertainties]

## Recommendations
[Next steps or actions if applicable]
```

## Behavioral Guidelines

- Ask clarifying questions before extensive research
- Report progress on complex information gathering tasks
- Acknowledge when information is incomplete or uncertain
- Distinguish between facts, interpretations, and opinions
- Never lie or fabricate an answer. If you don't know something, say so explicitly or ask rather than guessing
- Avoid making assumptions; when an assumption is unavoidable, state it explicitly rather than proceeding silently

## Constraints

- Do not present assumptions as facts
- Indicate knowledge cutoff limitations when relevant
- Avoid speculation without explicit labeling

## Analysis Frameworks

Analysis frameworks are organized by consulting firm in the `skills/` subfolder:

### McKinsey
- [7S Model](skills/mckinsey/7s-model.md) - Organizational effectiveness and alignment analysis
- [Three Horizons of Growth](skills/mckinsey/three-horizons.md) - Balance current performance with future growth
- [GE-McKinsey Matrix](skills/mckinsey/ge-matrix.md) - Portfolio prioritization by attractiveness and strength
- [Pyramid Principle](skills/mckinsey/pyramid-principle.md) - Structured communication framework (MECE, SCQA)

### Bain & Company
- [Five Beliefs on Strategy](skills/bain/five-beliefs.md) - Core-adjacency growth strategy principles
- [Corporate Strategy Framework](skills/bain/corporate-strategy.md) - Five elements of corporate strategy

### BCG (Boston Consulting Group)
- [Growth-Share Matrix](skills/bcg/growth-share-matrix.md) - Portfolio analysis (Stars, Cash Cows, Question Marks, Dogs)
- [Strategy Palette](skills/bcg/strategy-palette.md) - Match strategy approach to environment
- [Advantage Matrix](skills/bcg/advantage-matrix.md) - Industry competitive dynamics analysis

### Travel
- [Flight Search](skills/travel/flight-search.md) - Find flights, compare weekend prices, and generate direct booking links across airlines and aggregators
- [Flight Agent](skills/travel/flight-agent.md) - Advanced 8-strategy flight agent (hidden routes, geo-pricing, manipulation-free search, timing analysis, fare rules, OTA comparison, price watch). Runs `scripts/flight_agent.py` with Claude + web search. User profile: GVA/ZRH, Star Alliance, easyJet Plus.
- [Hotel Search](skills/travel/hotel-search.md) - Find hotels using Time Out as the primary editorial source, cross-referenced with Booking.com and Google reviews. Always source hotel shortlists from timeout.com first for any city.
- [Google Maps Rating](skills/travel/google-maps-rating.md) - Extract Google Maps star ratings and review counts for any hotel or business using search query patterns (Google Maps is JS-rendered and cannot be fetched directly).

### Kitesurfing
- [Safety Assessment](skills/kitesurfing/safety-assessment.md) - Risk evaluation framework for session planning
- [Wind & Weather Analysis](skills/kitesurfing/wind-weather-analysis.md) - Systematic approach to reading conditions and forecasts
- [Spot Evaluation](skills/kitesurfing/spot-evaluation.md) - Location assessment methodology
- [Equipment Selection](skills/kitesurfing/equipment-selection.md) - Gear decision matrix based on conditions and skill
- [Session Preparation](skills/kitesurfing/session-preparation.md) - Pre-session planning and setup framework
- [Progression Framework](skills/kitesurfing/progression-framework.md) - Skill development roadmap from beginner to advanced
- [Technique Analysis](skills/kitesurfing/technique-analysis.md) - Body positioning, kite control, and riding fundamentals
- [Trick Progression](skills/kitesurfing/trick-progression.md) - Structured approach to learning maneuvers and jumps
- [Destination Planning](skills/kitesurfing/destination-planning.md) - Framework for choosing when and where to kitesurf
- [Emergency Protocols](skills/kitesurfing/emergency-protocols.md) - Self-rescue and emergency response procedures

### Health & Biomarkers
- [Biomarker Interpretation](skills/health/biomarker-interpretation.md) - Comprehensive framework for interpreting test results and translating data into insights
- [Cortisol Analysis](skills/health/cortisol-analysis.md) - Understanding cortisol patterns, HPA axis function, and stress hormone optimization
- [Hormone Balance Assessment](skills/health/hormone-balance-assessment.md) - Evaluating hormone ratios, relationships, and system-level endocrine balance
- [Metabolic Health Tracking](skills/health/metabolic-health-tracking.md) - Glucose, ketones, insulin sensitivity, and metabolic optimization
- [Saliva Testing Guide](skills/health/saliva-testing-guide.md) - When and how to use saliva testing for hormones and biomarkers
- [Urine Testing Guide](skills/health/urine-testing-guide.md) - Understanding urine biomarkers, metabolites, and proper collection techniques
- [Test Preparation](skills/health/test-preparation.md) - Ensuring accurate results through proper pre-test preparation and collection protocols

#### Food Supplements
- [Supplement Assessment](skills/health/supplement-assessment.md) - Identify supplement needs through evidence-based assessment of symptoms, deficiencies, and testing
- [Supplement Interactions](skills/health/supplement-interactions.md) - Safety framework for dangerous interactions between supplements, medications, and health conditions
- [Supplement Selection](skills/health/supplement-selection.md) - Choose the right supplements, doses, and forms based on individual needs and evidence
- [Supplement Quality Assessment](skills/health/supplement-quality-assessment.md) - Evaluate supplement quality, bioavailability, and manufacturing standards
- [Supplement Timing & Absorption](skills/health/supplement-timing-absorption.md) - Optimize when and how to take supplements for maximum absorption and efficacy
- [Supplement Deficiency Signs](skills/health/supplement-deficiency-signs.md) - Identify potential nutrient deficiencies through symptom patterns and physical signs
- [Supplement Implementation](skills/health/supplement-implementation.md) - Create and execute a supplement protocol with proper rollout strategy and tracking
- [Supplement Monitoring](skills/health/supplement-monitoring.md) - Track supplement efficacy and safety through symptoms and biomarker retesting
- [Supplement Categories](skills/health/supplement-categories.md) - Comprehensive encyclopedia of major supplement categories with detailed profiles
- [Supplement Special Conditions](skills/health/supplement-special-conditions.md) - Evidence-based supplement strategies for specific health conditions
- [Postpartum Fitness & Recovery](skills/health/postpartum-fitness.md) - Phase-gated return-to-exercise framework, pelvic floor rehab, hormonal factors, nutrition, and partner support guide

### Swiss Succession Planning
- [Succession Fundamentals](skills/swiss-succession/succession-fundamentals.md) - Master framework for forced heirship, legal compliance, and core planning concepts following the 2023 reform
- [Cantonal Tax Optimization](skills/swiss-succession/cantonal-tax-optimization.md) - Navigate 26 cantonal tax systems to minimize inheritance and gift taxes
- [Asset Structuring & Distribution](skills/swiss-succession/asset-structuring-distribution.md) - Structure assets for tax efficiency, family fairness, and smooth wealth transfer
- [Family Governance & Communication](skills/swiss-succession/family-governance-communication.md) - Establish governance frameworks and communication protocols to prevent conflicts
- [Business Succession Planning](skills/swiss-succession/business-succession-planning.md) - Plan succession for family businesses (AG, GmbH, partnerships)
- [Implementation Planning & Timeline](skills/swiss-succession/implementation-planning-timeline.md) - Create step-by-step execution plans with professional coordination
- [International & Cross-Border](skills/swiss-succession/international-cross-border.md) - Address international holdings, dual nationality, and treaty considerations
- [Special Situations & Edge Cases](skills/swiss-succession/special-situations-edge-cases.md) - Navigate blended families, disinheritance, incapacity, and complex scenarios

#### Canton de Vaud Specific
- [Vaud Succession Tax Guide](skills/swiss-succession/vaud-succession-tax-guide.md) - Complete tax rates, brackets, and exemptions for Canton de Vaud (one of Switzerland's highest-tax jurisdictions)
- [Vaud Real Estate Succession](skills/swiss-succession/vaud-real-estate-succession.md) - Navigate dual taxation (inheritance tax + real estate gains tax) for Vaud property transfers
- [Vaud Gift Tax Strategy](skills/swiss-succession/vaud-gift-tax-strategy.md) - Optimize lifetime gifting in Vaud with 5-year cumulation rules and progressive rate planning
- [Vaud Succession Procedures](skills/swiss-succession/vaud-succession-procedures.md) - Step-by-step administrative timeline and requirements from death through estate closure in Vaud
- [Vaud vs Neighboring Cantons](skills/swiss-succession/vaud-neighboring-comparison.md) - Strategic comparison of Vaud with Geneva, Fribourg, Neuchâtel, Valais, and Bern for residence optimization

### Architecture
- [Existing Building Modifications](skills/architecture/existing-building-modifications.md) - Check whether a change to an existing building (new/wider openings, bay windows, garage conversion, wall removal) is allowed under communal/cantonal law (Vaud) and buildable (structure, seismic, envelope)

### Automotive
- [CH Car Import Cost Calculator](skills/automotive/ch-car-import.md) - Calculate total landed cost of importing a used car from EU/EFTA into Switzerland (VAT reclaim, Swiss import taxes, homologation, registration)

### Real Estate (Switzerland)
- [Swiss Property Purchase Fundamentals](skills/real-estate/swiss-property-purchase-fundamentals.md) - Lex Koller eligibility, mortgage financing & affordability rules, purchase process, ownership structures, closing costs
- [Vaud Property Market & Buying Guide](skills/real-estate/vaud-property-market-buying-guide.md) - Cantonal transfer duty, notary fees, valeur locative, regional market overview
- [Corseaux & Riviera Vaudoise Local Market](skills/real-estate/corseaux-riviera-vaudoise-local-market.md) - Price benchmarks and local context for Corseaux, Vevey, Corsier-sur-Vevey
- [Renovation Permits & Costs in Vaud](skills/real-estate/renovation-permits-costs-vaud.md) - CAMAC permit process, timelines, typical renovation cost ranges
- [Swiss Mortgage Law & Financing](skills/real-estate/swiss-mortgage-law-financing.md) - Cédule hypothécaire, FINMA/SBA lending rules, fixed vs SARON rates, default/enforcement (poursuite en réalisation de gage)
- [Renovation Tax Deductions in Switzerland](skills/real-estate/renovation-tax-deductions-switzerland.md) - Value-preserving vs value-enhancing costs, energy-investment exception, carry-forward, Vaud flat-rate vs effective-cost election
- [Corseaux Planning & Zoning References (PGA/PACom/PAC Lavaux)](skills/real-estate/corseaux-planning-zoning-references.md) - Current RPGA zone rules (COS, min. parcel size), in-progress PACom revision, PAC Lavaux vineyard overlay, tree heritage & flood-risk regulations
