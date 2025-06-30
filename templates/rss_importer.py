import feedparser
import sqlite3

def import_episodes_for_podcast(podcast_id, rss_url):
    feed = feedparser.parse(rss_url)

    conn = sqlite3.connect('selah.db')
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        pub_date = entry.get("published", "")
        audio_url = ""
        image_url = ""

        # Get audio URL
        for link in entry.get("links", []):
            if link.get("type") == "audio/mpeg":
                audio_url = link.get("href")
                break

        # Try to get image
        if 'image' in entry:
            image_url = entry.image.get('href')
        elif 'itunes_image' in entry:
            image_url = entry.itunes_image.get('href')
        elif 'media_thumbnail' in entry:
            image_url = entry.media_thumbnail[0]['url']
        elif 'media_content' in entry:
            image_url = entry.media_content[0]['url']

        cursor.execute("""
            INSERT INTO episodes (podcast_id, title, pub_date, audio_url, image_url)
            VALUES (?, ?, ?, ?, ?)
        """, (podcast_id, title, pub_date, audio_url, image_url))

    conn.commit()
    conn.close()

# Example usage:
# import_episodes_for_podcast(12, 'https://feeds.simplecast.com/3NVmUWZO')  # BibleProject
