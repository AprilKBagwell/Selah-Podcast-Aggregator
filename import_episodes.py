import sqlite3
import feedparser

def import_episodes():
    conn = sqlite3.connect('selah.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT id, rss_url FROM podcasts")
    podcasts = cur.fetchall()

    for podcast in podcasts:
        podcast_id = podcast['id']
        rss_url = podcast['rss_url']
        print(f"Importing from: {rss_url}")

        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            title = entry.get("title", "No title")
            pub_date = entry.get("published", "")
            audio_url = ""
            image_url = ""

            # Try to extract audio URL
            if "enclosures" in entry and entry.enclosures:
                for enclosure in entry.enclosures:
                    if "audio" in enclosure.type:
                        audio_url = enclosure.href
                        break

            # Try to extract image URL
            image_url = (
                entry.get("image", {}).get("href") or
                entry.get("itunes_image", {}).get("href") or
                entry.get("media_thumbnail", [{}])[0].get("url") or
                entry.get("media_content", [{}])[0].get("url") or
                "static/images/default-podcast.png"
            )

            cur.execute("""
                INSERT INTO episodes (podcast_id, title, pub_date, audio_url, image_url)
                VALUES (?, ?, ?, ?, ?)
            """, (podcast_id, title, pub_date, audio_url, image_url))

    conn.commit()
    conn.close()
    print("✅ All episodes imported.")

if __name__ == "__main__":
    import_episodes()
