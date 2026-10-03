# Flight Search Framework

Use this framework to find flight options and prices for a given route and dates, working around the limitation that major booking sites (Google Flights, Kayak, Skyscanner) render prices dynamically and cannot be scraped directly.

## Core Approach

Since live booking pages require JavaScript, use a **three-layer strategy**:
1. **WebSearch** with optimized queries to surface prices from aggregators and airline sites
2. **Direct links** to pre-filled search pages on major platforms (ready to open)
3. **Contextual guidance** on best time to book and what to expect

## Step 1 — Gather Route Parameters

Before searching, confirm:
- **Origin airport** (IATA code, e.g. GVA)
- **Destination airport** (IATA code, e.g. IBZ)
- **Outbound date** (or range)
- **Return date** (or range, if round-trip)
- **Passenger count** (default: 1 adult)
- **Currency preference** (default: CHF for Swiss-based user)

## Step 2 — Run WebSearch Queries

Run these searches **in parallel** to maximize coverage:

### Query 1 — Airline-specific with dates
```
[airline] [origin city] [destination city] [day month year] price [currency]
```
Example: `easyJet Geneva Ibiza 18 September 2026 price CHF`

### Query 2 — Aggregator with route + month
```
cheapest flights [origin] to [destination] [month year] [currency]
```
Example: `cheapest flights Geneva Ibiza September 2026 CHF round trip`

### Query 3 — French-language search (often surfaces Swiss/French aggregators)
```
vol [origin city] [destination city] [day] [month] [year] prix
```
Example: `vol Genève Ibiza 18 septembre 2026 prix`

### Query 4 — Weekend comparison (if flexible)
```
flights [origin] [destination] [month] 2026 cheapest weekend
```

## Step 3 — Generate Direct Booking Links

Construct and present these ready-to-open links for the user:

### Google Flights
```
https://www.google.com/travel/flights/search?tfs=CBwQAhoeEgoyMDI2LTA5LTE4agcIARIDR1ZBcgcIARIDSUJaGh4SCjIwMjYtMDktMjBqBwgBEgNJQlpyBwgBEgNHVkE
```
> Note: Google Flights URLs encode search params — provide a plain-language link description and manual instructions when the encoded URL is complex.

Better approach — provide the Google Flights explore URL:
`https://www.google.com/travel/flights?q=Flights+from+[ORIGIN]+to+[DESTINATION]+on+[DATE]+returning+[RETURN_DATE]`

### easyJet (direct airline, often cheapest on this route)
`https://www.easyjet.com/en/cheap-flights/[origin-city]/[destination-city]`

### Vueling
`https://www.vueling.com/en/flights-from-[origin-city]-to-[destination-city]`

### Kayak (calendar view — best for comparing multiple weekends)
`https://www.kayak.com/flights/[ORIGIN]-[DEST]/[YYYY-MM-DD]/[YYYY-MM-DD]`
Example: `https://www.kayak.com/flights/GVA-IBZ/2026-09-18/2026-09-20`

### Skyscanner
`https://www.skyscanner.fr/transport/flights/[gva]/[ibz]/[YYMMDD]/[YYMMDD]/`
Example: `https://www.skyscanner.fr/transport/flights/gva/ibz/260918/260920/`

## Step 4 — Synthesize and Present Results

### Output format

```markdown
## Flights [ORIGIN] → [DESTINATION] | [DATE RANGE]

### What we found
| Source | Price (indicative) | Notes |
|--------|-------------------|-------|
| [Airline/site] | [CHF/EUR X] | [one-way / round-trip, direct] |
| ... | ... | ... |

### Direct booking links (click to search live prices)
- [Google Flights – [dates]](URL)
- [easyJet – [dates]](URL)
- [Kayak – [dates]](URL)
- [Skyscanner – [dates]](URL)

### Booking tips
- [Relevant advice: book by X, prices spike on Y weekend, etc.]
```

## Limitations

- **No live prices**: WebSearch returns general/historical ranges, not real-time fares. Prices shown are indicative only.
- **Dynamic rendering**: Kayak, Skyscanner, Google Flights, and most airline sites use JavaScript — direct page fetching returns no pricing data.
- **Exceptions**: Occasionally a news article, travel blog, or price alert service indexed by Google will contain specific recent prices — flag these clearly when found.
- **Always verify**: Direct user to booking site for final price confirmation before committing.

## Airline Quick Reference — GVA Routes

| Airline | Typical direct routes from GVA | Booking site |
|---------|-------------------------------|--------------|
| easyJet | IBZ, BCN, MAD, AMS, LIS, LGW | easyjet.com |
| Vueling | IBZ, BCN, MAD, FCO, CDG | vueling.com |
| SWISS | Most European + long-haul | swiss.com |
| Iberia | IBZ, MAD (via BCN) | iberia.com |
| Air France | CDG hub (connections) | airfrance.com |

## Booking Timing Rules of Thumb

| Season | How far in advance to book | Expected premium vs. off-peak |
|--------|---------------------------|-------------------------------|
| Peak (Jul–Aug Ibiza) | 3–4 months | +50–100% |
| Closing parties (late Sep) | 2–3 months | +30–60% |
| Shoulder (May, early Jun, early Sep) | 4–6 weeks | Baseline |
| Off-peak | 2–4 weeks | Discounts possible |
