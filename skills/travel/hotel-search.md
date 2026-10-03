# Hotel Search Framework

Use this framework when looking for hotels in any city. The priority source is always **Time Out** — their editorial picks carry more signal than aggregator star counts. Booking.com and Google reviews supplement, never replace.

## User Profile — Default Preferences

Unless told otherwise, apply these defaults for every hotel search:

| Preference | Default |
|------------|---------|
| **Budget** | $300–$400/night — flag anything above as a splurge, below as a steal |
| **Gym** | Strong plus — always note whether a gym is available, but don't exclude top-ranked hotels that lack one |
| **Style** | Design or boutique hotel strongly preferred over chains |
| **Vibe** | Curated, independently run, aesthetically considered spaces |
| **Metro/subway access** | Must be close to a metro/subway station — always note the nearest station and walking time |

Always note gym availability in the output. If a hotel has no gym but ranks highly, keep it in the list and flag it — don't exclude it.
Always include for each hotel: nearest metro/subway station, subway lines, distance in meters, and approximate walking time. Also always include both Booking.com score (X/10) and Google Maps rating (X/5) with number of reviews for each.

---

## Core Principle

**Time Out first.** Time Out editors live in the cities they cover and write opinionated, updated shortlists of the best hotels. Always start there to anchor the search, then cross-reference pricing and reviews on booking platforms.

---

## Step 1 — Clarify the Brief

Before searching, confirm:
- **City** (and neighbourhood preference if any)
- **Dates** (check-in / check-out)
- **Budget range** (per night, CHF or local currency)
- **Vibe / use case** (default: design or boutique — override if needed)
- **Must-haves** (gym is always required by default; note any other must-haves)

---

## Step 2 — Time Out Editorial Search (Primary Source)

Run these **in parallel**:

Time Out city URLs follow the pattern `https://www.timeout.com/[cityname]` (e.g. `https://www.timeout.com/newyork`, `https://www.timeout.com/london`, `https://www.timeout.com/barcelona`).

### Query 1 — Time Out best hotels shortlist
```
site:timeout.com best hotels [city]
```
Example: `site:timeout.com best hotels Lisbon`

Alternatively, construct the direct URL:
`https://www.timeout.com/[cityname]/hotels/best-hotels-in-[city]`

### Query 2 — Time Out neighbourhood guide (for context)
```
site:timeout.com [city] [neighbourhood OR hotels] guide
```
Example: `site:timeout.com Barcelona hotels guide`

> For extracting Google Maps ratings, use the [Google Maps Rating skill](../travel/google-maps-rating.md).

### Query 3 — Time Out with vibe filter
```
timeout.com best [boutique / design / luxury / cheap] hotels [city]
```
Example: `timeout.com best boutique hotels Tokyo`

**Fetch the top Time Out result** using WebFetch to extract:
- The ranked shortlist of hotels
- Their editorial comments (the "why" behind each pick)
- Any neighbourhood context or caveats

---

## Step 3 — Cross-Reference Pricing & Guest Reviews

For each hotel surfaced by Time Out, run parallel searches to gather:

### Booking.com
```
[hotel name] [city] booking.com
```
Extract: price per night, guest score, review highlights

### Google Hotels / Google Reviews
```
[hotel name] [city] reviews
```
Extract: overall rating, recurring praise/complaints, recent comments

### Optional — additional editorial sources
```
[hotel name] [city] Condé Nast Traveller OR Wallpaper* OR Monocle
```
Use when the hotel is design-forward or boutique — these publications often cover properties Time Out doesn't reach.

---

## Step 4 — Synthesize and Present

### Output format

```markdown
## Hotels in [City] | [Dates if known] | [Budget if known]

### Time Out Picks

#### 1. [Hotel Name]
**Time Out says:** "[Direct editorial quote or close paraphrase]"
**Neighbourhood:** [Area name + 1-line context]
**Metro:** [Nearest station + line + ~Xm walk + X min]
**Gym:** Yes / No / Spa only
**Price:** ~[$X]/night — [within budget $300–400 / splurge / steal]
**Booking.com:** [X/10] ([# reviews]) — [link]
**Google Maps:** [X/5 stars] ([# reviews])
**What guests say:** [1–2 sentence synthesis of recurring themes]
**Book:** [Booking.com link] | [Hotel direct site if known]

#### 2. [Hotel Name]
...

---

### Also Worth Knowing
- [Any Time Out honourable mentions not in the main shortlist]
- [Neighbourhood notes relevant to the user's brief]

### Booking Tips
- [Price patterns, best time to book, direct vs. OTA advice]
```

---

## Step 5 — Direct Booking Links

Always provide both OTA and direct hotel links:

| Platform | Link format |
|----------|------------|
| Booking.com | `https://www.booking.com/searchresults.html?ss=[city]&checkin=[YYYY-MM-DD]&checkout=[YYYY-MM-DD]` |
| Google Hotels | `https://www.google.com/travel/hotels/[city]` |
| Hotel direct | Search `[hotel name] official site` — direct bookings often 5–10% cheaper |

---

## Source Hierarchy

| Source | Role | Trust level |
|--------|------|-------------|
| Time Out | Primary editorial shortlist + neighbourhood context | High — editorial, updated, opinionated |
| Condé Nast Traveller / Wallpaper* / Monocle | Design/luxury editorial supplement | High for design-forward stays |
| Booking.com guest reviews | Pricing + crowd-sourced experience | Medium — volume gives signal, filter for recency |
| Google reviews | Supplementary crowd-sourced | Medium — good for recent complaints |
| TripAdvisor | Last resort only | Lower signal-to-noise ratio |

---

## Limitations

- **Time Out coverage varies**: Major cities (London, NYC, Paris, Tokyo, Lisbon, Barcelona, etc.) have deep coverage. Smaller cities may have thinner shortlists — flag this and lean more on editorial travel press.
- **No live pricing**: Prices sourced from search results are indicative. Always send user to booking platform for final confirmation.
- **Time Out articles date**: Check when the article was last updated — hotel quality can shift. Prefer articles updated within the last 12–18 months.
- **WebFetch may not load dynamic pages**: If Time Out content is behind a JS wall, fall back to the cached Google snippet + WebSearch to reconstruct the shortlist.
