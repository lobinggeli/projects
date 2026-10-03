#!/usr/bin/env python3
"""
Spotify Album Notifier — Daily checker
Checks for new albums from your top/followed artists and sends macOS notifications.
Run via cron — set up with spotify_setup.py first.
"""

import json
import os
import subprocess
import urllib.parse
import urllib.request
import base64
import time
from datetime import datetime, timedelta

CONFIG_PATH = os.path.expanduser("~/.spotify_notifier.json")
NEW_RELEASE_DAYS = 14  # alert on albums released in the last N days


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def get_access_token(config):
    credentials = base64.b64encode(
        f"{config['client_id']}:{config['client_secret']}".encode()
    ).decode()
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": config["refresh_token"],
    }).encode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=data,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["access_token"]


def spotify_get(url, token, retries=3):
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req) as resp:
                time.sleep(0.3)  # polite delay between requests
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                retry_after = int(e.headers.get("Retry-After", 5))
                print(f"Rate limited. Waiting {retry_after}s...")
                time.sleep(retry_after)
            else:
                raise
    raise Exception(f"Failed after {retries} retries: {url}")


def get_artists(token):
    artists = {}

    # Top artists (short, medium, long term)
    for term in ["short_term", "medium_term", "long_term"]:
        url = f"https://api.spotify.com/v1/me/top/artists?limit=50&time_range={term}"
        data = spotify_get(url, token)
        for a in data.get("items", []):
            artists[a["id"]] = a["name"]

    # Followed artists
    url = "https://api.spotify.com/v1/me/following?type=artist&limit=50"
    while url:
        data = spotify_get(url, token)
        artists_data = data.get("artists", {})
        for a in artists_data.get("items", []):
            artists[a["id"]] = a["name"]
        cursor = artists_data.get("cursors", {}).get("after")
        url = f"https://api.spotify.com/v1/me/following?type=artist&limit=50&after={cursor}" if cursor else None

    return artists


def get_recent_albums(artist_id, artist_name, token, since_date):
    url = (
        f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        f"?include_groups=album,single&limit=10&market=CH"
    )
    data = spotify_get(url, token)
    recent = []
    for album in data.get("items", []):
        release = album.get("release_date", "")
        if len(release) == 10:  # full date YYYY-MM-DD
            try:
                release_dt = datetime.strptime(release, "%Y-%m-%d")
                if release_dt >= since_date:
                    recent.append({
                        "id": album["id"],
                        "name": album["name"],
                        "artist": artist_name,
                        "release_date": release,
                        "type": album["album_type"],
                        "url": album["external_urls"].get("spotify", ""),
                    })
            except ValueError:
                pass
    return recent


def notify(title, message):
    script = f'display notification "{message}" with title "{title}" sound name "default"'
    subprocess.run(["osascript", "-e", script])


def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"Config not found at {CONFIG_PATH}. Run spotify_setup.py first.")
        return

    config = load_config()
    token = get_access_token(config)
    seen = set(config.get("seen_albums", []))
    since = datetime.now() - timedelta(days=NEW_RELEASE_DAYS)

    print(f"Fetching your artists...")
    artists = get_artists(token)
    print(f"Tracking {len(artists)} artists.")

    new_releases = []
    for artist_id, artist_name in artists.items():
        albums = get_recent_albums(artist_id, artist_name, token, since)
        for album in albums:
            if album["id"] not in seen:
                new_releases.append(album)
                seen.add(album["id"])

    if new_releases:
        print(f"Found {len(new_releases)} new release(s)!")
        for album in new_releases:
            label = "album" if album["type"] == "album" else "single"
            msg = f"New {label}: {album['name']} — released {album['release_date']}"
            notify(f"{album['artist']}", msg)
            print(f"  Notified: {album['artist']} — {album['name']} ({album['release_date']})")
    else:
        print("No new releases found.")

    config["seen_albums"] = list(seen)
    save_config(config)


if __name__ == "__main__":
    main()
