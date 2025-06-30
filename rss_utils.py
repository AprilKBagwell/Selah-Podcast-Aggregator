import sqlite3
import feedparser

def fetch_and_store_episodes():
    conn = sqlite3.connect('selah.db')
    cursor = conn.cursor()

    cursor.execute("SELECT podcast_id, title, rss_url FROM Podcast WHERE rss_url IS NOT NULL AND rss_url != ''")
    podcasts = cursor.fetchall()

    print(f"Found {len(podcasts)} podcasts with RSS URLs.\n")

    for podcast_id, podcast_title, rss_url in podcasts:
        print(f"Fetching: {podcast_title} - {rss_url}")

        try:
            feed = feedparser.parse(rss_url)
            print(f"  Found {len(feed.entries)} entries.")

            for entry in feed.entries:
                title = entry.get('title', 'No title')
                description = entry.get('description', '')
                pub_date = entry.get('published', '')

                audio_url = ''
                if 'enclosures' in entry and len(entry.enclosures) > 0:
                    audio_url = entry.enclosures[0].get('href', '')

                print(f"    Adding episode: {title}")
                cursor.execute('''
                    INSERT INTO Episode (podcast_id, title, description, pub_date, audio_url)
                    VALUES (?, ?, ?, ?, ?)
                ''', (podcast_id, title, description, pub_date, audio_url))

        except Exception as e:
            print(f"  Error parsing feed for {podcast_title}: {e}")

    conn.commit()
    conn.close()
    print("\nAll episodes updated.")

