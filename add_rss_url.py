import feedparser
import sqlite3
from datetime import datetime
import re

def clean_text(text):
    if text:
        text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
        text = re.sub(r'\s+', ' ', text).strip()  # Normalize spaces
    return text or "No description available"

def parse_pub_date(date_str):
    try:
        parsed_date = feedparser.parse(date_str).entries[0].published
        return parsed_date
    except:
        return datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

def add_rss_feed(rss_url, podcast_name):
    print(f"Processing feed: {rss_url} for {podcast_name}")
    feed = feedparser.parse(rss_url)
    if not feed.entries:
        print(f"No episodes found for {podcast_name}")
        return

    conn = sqlite3.connect("selah_db.sqlite")
    cursor = conn.cursor()

    for entry in feed.entries:
        title = clean_text(entry.get("title", "Untitled"))
        url = entry.get("enclosures", [{}])[0].get("url", "")
        description = clean_text(entry.get("description", "No description"))
        pub_date = parse_pub_date(entry.get("published", ""))

        try:
            cursor.execute("""
                INSERT INTO episodes (podcast, title, url, description, pub_date)
                VALUES (?, ?, ?, ?, ?)
            """, (podcast_name, title, url, description, pub_date))
        except sqlite3.IntegrityError:
            print(f"Duplicate episode skipped: {title}")
        except Exception as e:
            print(f"Error inserting {title}: {e}")

    conn.commit()
    conn.close()
    print(f"Added episodes for {podcast_name}")

if __name__ == "__main__":
    rss_feeds = [
        {"url": "https://mcdn.podbean.com/mf/feed/c2cv9s/Biblical_Worldview_Show.xml", "name": "Biblical Worldview Show"},
        {"url": "https://media.rss.com/josh-teis-preaching/feed.xml", "name": "Southern Hills LV Church"},
        {"url": "https://cloud.sermonaudio.net/api/v2/rss/broadcasters/faith-baptist", "name": "Faith Baptist Church"},
        {"url": "https://www.focusonthefamily.com/feed/podcast/daily-broadcast/", "name": "Focus on the Family"},
        {"url": "https://media.rss.com/liberty-baptist-church/feed.xml", "name": "Liberty Baptist Church"},
        {"url": "https://api.sermonaudio.com/v2/rss/broadcasters/pcc", "name": "Pensacola Christian College"},
        {"url": "https://feeds.soundcloud.com/users/soundcloud:users:774099040/sounds.rss", "name": "Teis Talks"}
    ]

    for feed in rss_feeds:
        add_rss_feed(feed["url"], feed["name"])

