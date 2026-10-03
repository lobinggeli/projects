#!/usr/bin/env python3
"""
Porsche 911 GTS Tracker
Scrapes mobile.de and AutoScout24 for new listings.
Saves a local HTML report and sends a Gmail notification for new listings.

Setup:
  pip install -r requirements.txt
  Edit config.json with your Gmail app password
  Run: python3 tracker.py
  Schedule: crontab -e  →  0 9 * * * cd /path/to/tracker && python3 tracker.py
"""

import json
import re
import smtplib
import subprocess
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import requests
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).parent
SEEN_FILE = SCRIPT_DIR / "seen.json"
REPORT_FILE = SCRIPT_DIR / "report.html"
CONFIG_FILE = SCRIPT_DIR / "config.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "de-DE,de;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ── Search parameters ──────────────────────────────────────────────────────────
# Porsche (20100) · 911 series (21) · GTS trim · Targa body · 2017–2019 · max 40,000 km
MOBILE_DE_URL = (
    "https://suchen.mobile.de/fahrzeuge/search.html"
    "?ms=20100%3B21%3B%3Bgts"
    "&fr=2017%3A2019"
    "&ml=%3A40000"
    "&s=Car&sb=p&vc=Car"
    "&pageNumber={page}"
)

# Porsche 911 Targa GTS · 2016–2019 · max 40,000 km · DE, AT, CH, FR, IT, BE, NL
AUTOSCOUT24_URL = (
    "https://www.autoscout24.com/lst/porsche/911"
    "?sort=age&desc=1&atype=C&ustate=N,U"
    "&fregfrom=2016&fregto=2019"
    "&kmto=60000"
    "&cy=D,A,CH,F,I,B,NL"
    "&q=targa+gts"
    "&page={page}"
)

TARGA_GTS_FILTER = True   # require "targa" AND "gts" in title
MAX_KM = 60000            # post-filter: skip listings above this mileage


# ── Persistence ────────────────────────────────────────────────────────────────

def load_seen() -> dict:
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text())
    return {}


def save_seen(seen: dict):
    SEEN_FILE.write_text(json.dumps(seen, indent=2, ensure_ascii=False))


def load_config() -> dict:
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


# ── mobile.de scraper ──────────────────────────────────────────────────────────

def fetch_mobile_de():
    listings = []
    session = requests.Session()
    session.headers.update({
        **HEADERS,
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    })

    # Establish session by visiting homepage first (required for cookies)
    try:
        session.get("https://www.mobile.de/", timeout=15)
    except Exception:
        pass

    for page in range(1, 6):
        try:
            session.headers.update({"Referer": "https://www.mobile.de/"})
            resp = session.get(MOBILE_DE_URL.format(page=page), timeout=15)
            if resp.status_code != 200:
                print(f"  mobile.de page {page}: HTTP {resp.status_code}")
                break

            soup = BeautifulSoup(resp.text, "lxml")
            items = (
                soup.select("article.cBox")
                or soup.select("[data-ad-id]")
                or soup.select("div.cBox-body--resultitem")
                or soup.select("article")
            )

            if not items:
                # Check if we got a valid page at all
                if "mobile.de" not in resp.text:
                    print(f"  mobile.de page {page}: unexpected response")
                    break
                break

            for item in items:
                listing = _parse_mobile_de_item(item)
                if listing:
                    listings.append(listing)

            session.headers.update({"Referer": MOBILE_DE_URL.format(page=page)})

        except Exception as e:
            print(f"  mobile.de page {page} error: {e}")
            break

    return listings


def _parse_mobile_de_item(item):
    try:
        # ID from link href
        link = item.find("a", href=re.compile(r"id=\d+"))
        if not link:
            return None
        href = link["href"]
        id_match = re.search(r"id=(\d+)", href)
        if not id_match:
            return None
        listing_id = "mde_" + id_match.group(1)
        url = ("https://suchen.mobile.de" + href) if href.startswith("/") else href
        url = url.split("&")[0] + "&id=" + id_match.group(1)

        title_el = item.select_one("h2, .headline-result, [class*='title']")
        title = title_el.get_text(" ", strip=True) if title_el else ""

        price_el = item.select_one("[class*='price'], [class*='Price']")
        price = price_el.get_text(strip=True) if price_el else ""

        # Key specs: mileage and registration date are in small text blocks
        specs = item.select(".specsFirstRow li, .specsSecondRow li, [class*='spec'] li")
        km = next((s.get_text(strip=True) for s in specs if "km" in s.get_text()), "")
        year = next((s.get_text(strip=True) for s in specs if re.search(r"\d{2}/20\d{2}", s.get_text())), "")

        location_el = item.select_one("[class*='location'], [class*='seller']")
        location = location_el.get_text(strip=True) if location_el else ""

        return {
            "id": listing_id,
            "source": "mobile.de",
            "title": title,
            "price": price,
            "km": km,
            "year": year,
            "location": location,
            "url": url,
            "found_at": datetime.now().isoformat(),
        }
    except Exception:
        return None


# ── AutoScout24 scraper ────────────────────────────────────────────────────────

def fetch_autoscout24():
    listings = []
    session = requests.Session()
    session.headers.update(HEADERS)

    for page in range(1, 4):
        try:
            resp = session.get(AUTOSCOUT24_URL.format(page=page), timeout=15)
            if resp.status_code != 200:
                print(f"  AutoScout24 page {page}: HTTP {resp.status_code}")
                break

            soup = BeautifulSoup(resp.text, "lxml")

            # AutoScout24 (Next.js) embeds all data in __NEXT_DATA__
            next_data_tag = soup.find("script", {"id": "__NEXT_DATA__"})
            if next_data_tag:
                data = json.loads(next_data_tag.string)
                raw_listings = (
                    data.get("props", {})
                        .get("pageProps", {})
                        .get("listings", [])
                    or data.get("props", {})
                        .get("pageProps", {})
                        .get("data", {})
                        .get("listings", [])
                )
                for item in raw_listings:
                    listing = _parse_autoscout24_json(item)
                    if listing:
                        listings.append(listing)
                if raw_listings:
                    continue  # got data from JSON, move to next page

            # Fallback: parse HTML article elements
            for article in soup.select("article[data-guid], article[id^='listing-']"):
                listing = _parse_autoscout24_html(article)
                if listing:
                    listings.append(listing)

        except Exception as e:
            print(f"  AutoScout24 page {page} error: {e}")
            break

    return listings


def _parse_autoscout24_json(item):
    try:
        guid = item.get("id") or item.get("guid")
        if not guid:
            return None

        vehicle = item.get("vehicle", item)
        prices = item.get("prices", {}).get("public", {}) or item.get("price", {})
        price_raw = prices.get("priceRaw") or prices.get("value")
        price = f"€{price_raw:,}" if isinstance(price_raw, (int, float)) else str(price_raw or "—")

        make = vehicle.get("make", "")
        model = vehicle.get("model", "")
        version = vehicle.get("modelVersionInput") or vehicle.get("version", "")
        title = f"{make} {model} {version}".strip()

        mileage = vehicle.get("mileage") or item.get("mileage")
        km = f"{mileage:,} km" if isinstance(mileage, (int, float)) else str(mileage or "—")

        reg = vehicle.get("firstRegistration") or item.get("firstRegistration", {})
        year = str(reg.get("year", "")) if isinstance(reg, dict) else str(reg or "")

        location = (item.get("seller") or {}).get("address", {}).get("country", "") or \
                   (item.get("location") or {}).get("countryCode", "")

        return {
            "id": f"as24_{guid}",
            "source": "autoscout24",
            "title": title,
            "price": price,
            "km": km,
            "year": year,
            "location": location,
            "url": f"https://www.autoscout24.com/offers/{guid}",
            "found_at": datetime.now().isoformat(),
        }
    except Exception:
        return None


def _parse_autoscout24_html(article):
    try:
        guid = article.get("data-guid") or re.sub(r"^listing-", "", article.get("id", ""))
        if not guid:
            return None

        link = article.select_one("a[href*='/offers/']")
        url = f"https://www.autoscout24.com{link['href']}" if link else f"https://www.autoscout24.com/offers/{guid}"

        title_el = article.select_one("h2, [class*='Title'], [class*='title']")
        title = title_el.get_text(" ", strip=True) if title_el else ""

        price_el = article.select_one("[class*='Price'], [class*='price']")
        price = price_el.get_text(strip=True) if price_el else ""

        full_text = article.get_text(" ")
        km_match = re.search(r"(?<!\d)([\d.,]+)\s*km\b", full_text)
        km = (km_match.group(1) + " km") if km_match else ""

        year_match = re.search(r"\b(0[1-9]|1[0-2])/20(1[7-9]|2\d)\b", full_text)
        year = year_match.group(0) if year_match else ""

        return {
            "id": f"as24_{guid}",
            "source": "autoscout24",
            "title": title,
            "price": price,
            "km": km,
            "year": year,
            "location": "",
            "url": url,
            "found_at": datetime.now().isoformat(),
        }
    except Exception:
        return None


# ── HTML report ────────────────────────────────────────────────────────────────

def generate_html_report(new_listings, all_listings):
    run_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    def card(l, is_new=False):
        border = "#22c55e" if is_new else "#e5e7eb"
        bg = "#f0fdf4" if is_new else "white"
        badge = (
            '<span style="background:#22c55e;color:white;padding:2px 8px;'
            'border-radius:4px;font-size:11px;margin-left:8px;vertical-align:middle;">NEW</span>'
            if is_new else ""
        )
        source_logo = "🇩🇪" if l["source"] == "mobile.de" else "🌍"
        return f"""
        <div style="border:1px solid {border};border-radius:8px;padding:14px 16px;margin:8px 0;background:{bg}">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px">
            <div>
              <a href="{l['url']}" target="_blank"
                 style="font-weight:600;font-size:14px;color:#1e40af;text-decoration:none">
                {l['title'] or 'View listing'}{badge}
              </a>
              <div style="color:#6b7280;font-size:12px;margin-top:4px">
                {source_logo} {l['source']} &nbsp;·&nbsp;
                📍 {l['location'] or '—'} &nbsp;·&nbsp;
                🗓 {l['year'] or '—'} &nbsp;·&nbsp;
                📏 {l['km'] or '—'}
              </div>
            </div>
            <div style="font-size:18px;font-weight:700;color:#111827;white-space:nowrap">
              {l['price'] or '—'}
            </div>
          </div>
        </div>"""

    new_section = (
        f'<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;'
        f'padding:16px;margin-bottom:24px">'
        f'<h2 style="margin:0 0 12px;color:#15803d">🆕 {len(new_listings)} New Listing'
        f'{"s" if len(new_listings) > 1 else ""}</h2>'
        + "".join(card(l, True) for l in new_listings)
        + "</div>"
        if new_listings
        else '<p style="color:#6b7280;font-style:italic">No new listings since last run.</p>'
    )

    all_cards = "".join(card(l) for l in sorted(all_listings, key=lambda x: x.get("price") or ""))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Porsche 911 GTS Tracker</title>
  <style>
    body {{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           max-width:820px;margin:40px auto;padding:0 20px;color:#111827;background:#f9fafb}}
    h1 {{border-bottom:2px solid #e5e7eb;padding-bottom:12px;margin-bottom:4px}}
  </style>
</head>
<body>
  <h1>🏎 Porsche 911 GTS Tracker
    <span style="font-size:13px;font-weight:400;color:#6b7280;margin-left:10px">Last run: {run_time}</span>
  </h1>
  <p style="color:#6b7280;margin-top:4px;margin-bottom:24px">
    2017–2019 · max 40,000 km · mobile.de + AutoScout24
  </p>
  {new_section}
  <h2 style="color:#374151;margin-top:32px">All Active Listings ({len(all_listings)})</h2>
  {all_cards}
</body>
</html>"""


# ── Email notification ─────────────────────────────────────────────────────────

def send_email(new_listings, config):
    gmail_user = config.get("gmail_user")
    app_password = config.get("gmail_app_password")
    recipient = config.get("recipient", gmail_user)

    if not gmail_user or not app_password or app_password == "YOUR_APP_PASSWORD_HERE":
        print("  Email skipped — add gmail_app_password to config.json")
        return

    rows = "".join(
        f"""<tr>
          <td style="padding:8px;border-bottom:1px solid #e5e7eb">
            <a href="{l['url']}">{l['title'] or 'View listing'}</a>
          </td>
          <td style="padding:8px;border-bottom:1px solid #e5e7eb;font-weight:600">{l['price'] or '—'}</td>
          <td style="padding:8px;border-bottom:1px solid #e5e7eb">{l['km'] or '—'}</td>
          <td style="padding:8px;border-bottom:1px solid #e5e7eb">{l['year'] or '—'}</td>
          <td style="padding:8px;border-bottom:1px solid #e5e7eb;color:#6b7280">{l['source']}</td>
        </tr>"""
        for l in new_listings
    )

    body = f"""<html><body style="font-family:sans-serif;max-width:700px">
      <h2>🏎 {len(new_listings)} New Porsche 911 GTS Listing{'s' if len(new_listings) > 1 else ''}</h2>
      <table style="border-collapse:collapse;width:100%">
        <thead>
          <tr style="background:#f3f4f6">
            <th style="padding:8px;text-align:left">Listing</th>
            <th style="padding:8px;text-align:left">Price</th>
            <th style="padding:8px;text-align:left">km</th>
            <th style="padding:8px;text-align:left">Year</th>
            <th style="padding:8px;text-align:left">Source</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    </body></html>"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🏎 {len(new_listings)} New Porsche 911 GTS Listing{'s' if len(new_listings) > 1 else ''}"
    msg["From"] = gmail_user
    msg["To"] = recipient
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, app_password)
            server.sendmail(gmail_user, recipient, msg.as_string())
        print(f"  Email sent → {recipient}")
    except Exception as e:
        print(f"  Email failed: {e}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    config = load_config()
    seen = load_seen()

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching mobile.de...")
    mobile_listings = fetch_mobile_de()
    print(f"  {len(mobile_listings)} listings found")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching AutoScout24...")
    as24_listings = fetch_autoscout24()
    print(f"  {len(as24_listings)} listings found")

    # Deduplicate by ID and post-filter for Targa GTS
    seen_this_run = set()
    all_listings = []
    for l in mobile_listings + as24_listings:
        if l["id"] not in seen_this_run:
            seen_this_run.add(l["id"])
            if TARGA_GTS_FILTER:
                title_lower = (l.get("title") or "").lower()
                if "targa" not in title_lower or "gts" not in title_lower:
                    continue
            km_digits = re.sub(r"[^\d]", "", re.split(r"km", l.get("km") or "", flags=re.I)[0])
            km_val = int(km_digits) if km_digits else 0
            if km_val > MAX_KM:
                continue
            all_listings.append(l)

    new_listings = [l for l in all_listings if l["id"] not in seen]
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {len(new_listings)} new · {len(all_listings)} total")

    # Persist seen IDs
    for l in all_listings:
        seen[l["id"]] = {
            "title": l["title"],
            "price": l["price"],
            "found_at": l["found_at"],
        }
    save_seen(seen)

    # Generate report
    html = generate_html_report(new_listings, all_listings)
    REPORT_FILE.write_text(html, encoding="utf-8")
    print(f"  Report → {REPORT_FILE}")

    # Open report in browser
    subprocess.run(["open", str(REPORT_FILE)], check=False)

    # Email
    if new_listings:
        send_email(new_listings, config)
        print("\nNew listings:")
        for l in new_listings:
            print(f"  {l['source']:12} {l['price']:15} {l['km']:12} {l['title']}")
            print(f"               {l['url']}")


if __name__ == "__main__":
    main()
