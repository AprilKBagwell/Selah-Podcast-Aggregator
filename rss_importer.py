import sqlite3
import feedparser

def import_episodes():
    conn = sqlite3.connect('podcasts.db')
    c = conn.cursor()

    c.execute("SELECT id, name, rss_url FROM podcasts")
    podcasts = c.fetchall()

    for podcast_id, name, rss_url in podcasts:
        print(f"Importing episodes from: {name}")
        feed = feedparser.parse(rss_url)

        if not feed.entries:
            print(f"❌ No entries found for {name}")
            continue

        imported = 0
        for entry in feed.entries:
            title = entry.get("title", "No title")
            description = entry.get("description", "No description")
            pub_date = entry.get("published", "")
            audio_url = (
                entry.enclosures[0].href
                if entry.get("enclosures")
                else entry.get("link", "")
            )
            image_url = (
                entry.get("image", {}).get("href", "")
                if entry.get("image")
                else entry.get("itunes_image", {}).get("href", "")
            )

            c.execute("""
                INSERT INTO episodes (podcast_id, title, description, pub_date, audio_url, image_url)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (podcast_id, title, description, pub_date, audio_url, image_url))
            imported += 1

        print(f"✅ Imported {imported} episodes from {name}\n")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    import_episodes()
