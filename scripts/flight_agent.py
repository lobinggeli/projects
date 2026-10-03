#!/usr/bin/env python3
"""
Flight Agent — finds best flight rates using Claude + real-time web search.

Usage:
  python flight_agent.py                               # interactive mode
  python flight_agent.py GVA IBZ 2026-09-18           # one-way
  python flight_agent.py GVA IBZ 2026-09-18 2026-09-20  # round-trip

Requires: pip install anthropic
          ANTHROPIC_API_KEY env var set
"""

import anthropic
import sys

SYSTEM_PROMPT = """You are an expert flight pricing analyst with deep knowledge of:
- Airline pricing structures, fare classes, and routing logic
- Hidden city ticketing, split routes, and nearby airport alternatives
- Price manipulation tactics (cookies, repeated searches, device tracking) and how to avoid them
- Geo-pricing differences across booking markets and currencies
- Optimal booking timing, fare reset windows, and demand cycles
- OTA vs direct airline pricing, fees, and hidden discounts

USER PROFILE (apply automatically):
- Home airports: Geneva (GVA) and Zurich (ZRH) — always compare both when relevant
- Alliance preference: Star Alliance — prioritize SWISS, Lufthansa, Austrian Airlines
- easyJet Plus member — when easyJet operates the route, include it and note Plus benefits:
  free cabin bag (55x40x20cm), upfront/extra legroom seat selection, priority boarding
- Currency: CHF
- Booking principle: always compare direct airline (swiss.com, easyjet.com) vs OTAs;
  easyJet Plus benefits only apply when booking directly on easyjet.com

When asked to find flights, always run multiple web search queries covering:
1. SWISS / Lufthansa specific: "SWISS [origin] [destination] [date] price CHF"
2. easyJet (if applicable): "easyJet [origin] [destination] [date] CHF"
3. Aggregator: "cheapest flights [origin] to [destination] [month year] CHF"
4. French-language: "vol [origin] [destination] [date] prix" (surfaces Swiss/French platforms)
5. ZRH alternative if origin is GVA (or vice versa): compare both departure airports

Present results in this format:

## Flights [ORIGIN] → [DESTINATION] | [DATES]

### Indicative Prices Found
| Source | Price | Type | Notes |
|--------|-------|------|-------|
| ... | ... | ... | ... |

### Direct Booking Links (live prices — click to confirm)
- [Google Flights](URL)
- [Kayak](URL)
- [Skyscanner](URL)
- [easyJet / Vueling / SWISS](URL) — whichever serves this route

### Smart Booking Tips
[3-5 actionable tips: best booking window, price patterns, alternatives, fare watch advice]

Default currency: CHF. Always note that prices shown are indicative — user must confirm on booking site."""


STRATEGY_PROMPTS = {
    "standard": (
        "Search multiple sources and give me direct booking links with smart booking tips."
    ),
    "hidden_routes": (
        "Act as a professional flight pricing analyst. Break this route into hidden city tickets, "
        "nearby departure and arrival airports, and multi-leg combinations airlines don't surface. "
        "Compare direct vs split routes, explain the price gap, and rank the cheapest legal options."
    ),
    "manipulation_free": (
        "Analyze how airlines raise prices using repeated searches, cookies, browser data, device "
        "type, IP location, and time-based demand signals. Explain exactly which behaviors trigger "
        "price inflation and give a precise step-by-step search method to avoid it for this route."
    ),
    "geo_pricing": (
        "Simulate flight prices for this route across different countries, currencies, and regional "
        "booking markets (CH, FR, DE, UK, US). Identify where the ticket is priced lowest, explain "
        "why geo-pricing differs, and outline legal ways to access those fares."
    ),
    "timing": (
        "Use historical airline pricing behavior to identify the cheapest booking days, booking "
        "windows, and departure periods for this route. Explain how demand cycles, inventory release, "
        "and fare resets influence price drops."
    ),
    "fare_rules": (
        "Break down airline fare rules, ticket classes, routing logic, and pricing conditions for "
        "this route in simple terms. Show how airlines structure these rules to price flights "
        "differently and how I can select options that quietly reduce total cost."
    ),
    "ota_vs_airline": (
        "Compare pricing between airlines, major OTAs, regional booking sites, and lesser-known "
        "platforms for this route. Identify where service fees, markups, and hidden discounts appear, "
        "and explain which platforms usually reveal the lowest base fares."
    ),
    "price_watch": (
        "Create a detailed fare-tracking strategy for this route that monitors price drops without "
        "triggering price increases. Include search frequency, timing resets, alert setup, behavioral "
        "rules, and practical examples to keep prices stable while tracking over time."
    ),
}

STRATEGY_LABELS = {
    "1": ("standard",         "Standard search"),
    "2": ("hidden_routes",    "Hidden routes & nearby airports"),
    "3": ("manipulation_free","Manipulation-free search method"),
    "4": ("geo_pricing",      "Geo-pricing bypass"),
    "5": ("timing",           "Optimal timing analysis"),
    "6": ("fare_rules",       "Fare rule exploiter"),
    "7": ("ota_vs_airline",   "Airline vs OTA comparison"),
    "8": ("price_watch",      "Price drop watch strategy"),
}


def run_agent(origin: str, destination: str, outbound: str,
              return_date: str = None, passengers: int = 1,
              strategy: str = "standard") -> None:
    """Run the flight search agent."""
    client = anthropic.Anthropic()

    trip_type = "round-trip" if return_date else "one-way"
    dates = f"{outbound} → {return_date}" if return_date else outbound

    user_message = (
        f"Find me the best {trip_type} flight rates from {origin} to {destination}.\n"
        f"Dates: {dates}\n"
        f"Passengers: {passengers}\n"
        f"Currency: CHF\n\n"
        + STRATEGY_PROMPTS.get(strategy, STRATEGY_PROMPTS["standard"])
    )

    label = next((v[1] for v in STRATEGY_LABELS.values() if v[0] == strategy), "Standard")
    print(f"\n{origin} → {destination} | {dates} | {passengers} pax | {label}")
    print("─" * 64)

    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=[{"type": "web_search_20260209", "name": "web_search"}],
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for event in stream:
            if event.type == "content_block_delta" and event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)

    print("\n")


def interactive_mode() -> None:
    """Interactive mode — prompts for all route details."""
    print("╔══════════════════════════════════╗")
    print("║        Flight Rate Agent          ║")
    print("║   Powered by Claude + Web Search  ║")
    print("╚══════════════════════════════════╝\n")

    origin      = input("Origin      (e.g. GVA, Geneva): ").strip()
    destination = input("Destination (e.g. IBZ, Ibiza):  ").strip()
    outbound    = input("Outbound date   (YYYY-MM-DD):   ").strip()
    ret         = input("Return date     (blank=one-way): ").strip() or None
    pax         = input("Passengers      [1]:             ").strip()
    passengers  = int(pax) if pax else 1

    print("\nSearch strategy:")
    for k, (_, label) in STRATEGY_LABELS.items():
        print(f"  {k}. {label}")

    choice   = input("\nStrategy [1]: ").strip() or "1"
    strategy = STRATEGY_LABELS.get(choice, ("standard", ""))[0]

    run_agent(origin, destination, outbound, ret, passengers, strategy)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) >= 3:
        # CLI: flight_agent.py GVA IBZ 2026-09-18 [2026-09-20] [1] [strategy]
        run_agent(
            origin=args[0],
            destination=args[1],
            outbound=args[2],
            return_date=args[3] if len(args) > 3 else None,
            passengers=int(args[4]) if len(args) > 4 else 1,
            strategy=args[5] if len(args) > 5 else "standard",
        )
    else:
        interactive_mode()
