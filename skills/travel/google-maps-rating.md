# Google Maps Rating Extractor

Use this skill to retrieve Google Maps ratings (X/5 stars + review count) for hotels or any business. Google Maps pages are JavaScript-rendered and cannot be fetched directly — use the search query approach below instead.

## Core Approach

Google Search snippets frequently surface the Google Maps rating (stars + review count) directly in results when the right query pattern is used. This avoids the need to fetch dynamic pages.

## Step 1 — Run the Rating Query

For each hotel/business, run this WebSearch query:

```
[Business Name] [City] Google Maps rating stars
```

Examples:
- `Arlo SoHo New York Google Maps rating stars`
- `Nine Orchard hotel New York Google Maps rating stars`
- `The Beekman New York Google Maps rating stars`

This query pattern reliably triggers Google's knowledge panel data in search snippets, which includes the star rating and review count.

## Step 2 — Fallback Query (if Step 1 returns no rating)

If the first query doesn't surface a star rating, try:

```
[Business Name] [City] "X." stars reviews
```

Or search for the Google Maps place directly:
```
[Business Name] [City] site:google.com/maps
```

The snippet for a Maps result often includes the rating inline.

## Step 3 — Extract and Validate

From the search snippet, extract:
- **Star rating** (X.X / 5)
- **Number of reviews** (e.g. 2,571 reviews)
- **Source confirmation** — confirm it's Google Maps, not TripAdvisor or Booking.com

If the rating does not appear in any snippet after both queries, report: `Google Maps: not retrieved — check directly at google.com/maps`

## Step 4 — Batch Multiple Hotels

When looking up ratings for multiple hotels, run all WebSearch queries **in parallel** — one query per hotel — to maximize speed.

Example batch for NYC hotels:
```
Query 1: Arlo SoHo New York Google Maps rating stars
Query 2: Nine Orchard hotel New York Google Maps rating stars
Query 3: Smyth Tribeca New York Google Maps rating stars
Query 4: The Beekman New York Google Maps rating stars
```

## Output Format

Inline in hotel cards:
```
**Google Maps:** 4.2/5 (2,571 reviews)
```

Or in a comparison table:
| Hotel | Google Maps | Booking.com |
|-------|------------|-------------|
| Arlo SoHo | 4.2/5 (2,571) | 8.1/10 (1,691) |
| 11 Howard | 3.9/5 | 7.6/10 (421) |

## Limitations

- **Dynamic rendering**: Google Maps pages cannot be fetched directly with WebFetch — always use the search query approach.
- **Snippet availability**: Ratings appear in snippets ~80% of the time. Lesser-known properties may not surface.
- **Freshness**: Search snippets may lag a few days behind the live Google Maps page. For critical decisions, verify directly on Google Maps.
- **Direct link format**: Google Maps place URLs for hotels follow the pattern `https://www.google.com/maps/search/[Hotel+Name]+[City]` — provide this as a fallback link when the rating is not retrieved.
