# Flight Agent Skill

Advanced flight pricing skill combining real-time web search with expert strategies to find the lowest fares. Use this when searching for flights, not just browsing options.

## User Context

- **Home airports**: Geneva (GVA), Zurich (ZRH)
- **Alliance preference**: Star Alliance (SWISS, Lufthansa, United, Singapore Airlines, etc.)
- **Budget carrier membership**: easyJet Plus (priority boarding, extra legroom, free cabin bag)
- **Default currency**: CHF

## How to Use

Run the agent script:
```bash
# Interactive
python scripts/flight_agent.py

# One-way
python scripts/flight_agent.py GVA IBZ 2026-09-18

# Round-trip with strategy
python scripts/flight_agent.py GVA JFK 2026-05-04 2026-05-08 1 geo_pricing
```

Available strategies: `standard`, `hidden_routes`, `manipulation_free`, `geo_pricing`, `timing`, `fare_rules`, `ota_vs_airline`, `price_watch`

---

## The 8 Search Strategies

### 1. Standard Search
Multi-source search with direct booking links. Default for most queries.

**Run when**: Quick price check needed, known dates.

### 2. Hidden Route Scanner
**Prompt**: Act as a professional flight pricing analyst. Break my route into hidden city tickets, nearby departure and arrival airports, and multi-leg combinations airlines don't surface. Compare direct vs split routes, explain the price gap, and rank the cheapest legal options.

**Run when**: Route seems expensive, flexible on exact airports. GVA vs ZRH comparisons, BSL as an alternative.

**Note for user**: SWISS is Star Alliance — compare SWISS via GVA vs ZRH vs via Lufthansa hub (FRA/MUC).

### 3. Price Manipulation Detector
**Prompt**: Analyze how airlines raise prices using repeated searches, cookies, browser data, device type, IP location, and time-based demand signals. Explain exactly which behaviors trigger price inflation and give a precise step-by-step search method to avoid it.

**Run when**: Prices seem to rise after each search, planning multiple search sessions.

**Key tactics**: Incognito + VPN, clear cookies between searches, use Google Flights first (doesn't trigger airline cookies), book direct on airline site.

### 4. Geo-Pricing Bypass
**Prompt**: Simulate flight prices for the same route across different countries, currencies, and regional booking markets. Identify where the ticket is priced lowest, explain why geo-pricing differs, and outline legal ways travelers can access those fares.

**Run when**: Long-haul or intercontinental (transatlantic, Asia). Example: booking GVA-JFK from a US IP vs Swiss IP often yields different fares on the same SWISS/United codeshare.

**Legal methods**: Use a VPN to browse from destination country, pay in local currency if card has no FX fees.

### 5. Timing Sweet Spot Finder
**Prompt**: Use historical airline pricing behavior to identify the cheapest booking days, booking windows, and departure periods for this route. Explain how demand cycles, inventory release, and fare resets influence these price drops.

**Run when**: Flexible on exact dates, planning trip more than 3 weeks out.

**General rules of thumb**:
- Midweek departures (Tue/Wed) typically cheaper
- 6-8 weeks ahead for European leisure routes
- 3-4 months ahead for peak summer (Jul-Aug)
- Tuesday/Wednesday fare releases by airlines (midnight local time)

### 6. Fare Rule Exploiter
**Prompt**: Break down airline fare rules, ticket classes, routing logic, and pricing conditions in simple terms. Show how airlines structure these rules to price flights differently and how travelers can select options that quietly reduce total cost.

**Run when**: Comparing fare classes on SWISS/Lufthansa (Economy Light vs Saver vs Flex), understanding Star Alliance award availability logic.

**Relevant fare classes**: SWISS Economy Light (no changes), Saver (CHF 50 change fee), Flex (full changes). easyJet Plus gives free seat selection and Flexi fare perks.

### 7. Airline vs OTA Comparison
**Prompt**: Compare pricing between airlines, major OTAs, regional booking sites, and lesser-known platforms. Identify where service fees, markups, and hidden discounts appear, and explain which platforms usually reveal lower base fares.

**Run when**: Not sure where to book, checking if an OTA is worth using over direct.

**Platform hierarchy for this user**:
1. Google Flights (price discovery, no booking fees)
2. Direct on airline site (SWISS.com, easyJet.com with Plus benefits)
3. Kayak / Skyscanner (comparison only)
4. Avoid: Expedia, Booking.com flights (fees + no airline benefits)

### 8. Price Drop Watch Strategy
**Prompt**: Create a detailed fare-tracking strategy that monitors price drops without triggering price increases. Include search frequency, timing resets, alert setup, behavioral rules, and practical examples to keep prices stable while tracking over time.

**Run when**: Route identified but not booking yet, watching for a price drop.

**Recommended tools**:
- Google Flights price alerts (set from incognito, use Gmail for alerts)
- Kayak price predictor
- Skyscanner "cheapest month" calendar
- easyJet low fare finder (for easyJet routes, Plus membership shows extra discounts)

---

## Star Alliance Priority Rules

When multiple airlines serve a route, prefer this order:
1. **SWISS** (home carrier, GVA/ZRH based, Miles & More)
2. **Lufthansa** (FRA/MUC hub, same Miles & More)
3. **Austrian Airlines** (VIE hub)
4. **United / Singapore / Air New Zealand** (for transatlantic/transpacific)

For easyJet routes: easyJet Plus membership gives free cabin bag (55x40x20cm) + extra legroom seat — calculate this into total cost vs SWISS Economy Light.

---

## Booking Links Template

| Platform | URL pattern |
|----------|-------------|
| Google Flights | `https://www.google.com/travel/flights?q=Flights+from+[ORIGIN]+to+[DESTINATION]+on+[DATE]` |
| SWISS | `https://www.swiss.com/ch/en/fly/flights/[ORIGIN]-[DESTINATION]` |
| easyJet | `https://www.easyjet.com/en/cheap-flights/[origin]/[destination]` |
| Kayak | `https://www.kayak.com/flights/[ORIGIN]-[DEST]/[YYYY-MM-DD]/[YYYY-MM-DD]` |
| Skyscanner | `https://www.skyscanner.fr/transport/flights/[gva]/[ibz]/[YYMMDD]/[YYMMDD]/` |

---

## Limitations

- Prices from web search are **indicative only** — always confirm on the booking site before purchasing
- The agent cannot book tickets — it finds and links
- easyJet Plus benefits (seat, bag) apply only when booking directly on easyJet.com
- Star Alliance miles accrual requires booking on a Star Alliance carrier or eligible fare class
