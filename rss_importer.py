import feedparser
import sqlite3
from datetime import datetime
import os

DB_FILE = 'selah.db'

def parse_rss_feed(rss_url):
    feed = feedparser.parse(rss_url)
    episodes = []

    for entry in feed.entries:
        title = entry.get('title', 'Untitled Episode')

        # Handle audio
        audio_url = None
        for link in entry.get('links', []):
            if link.get('type', '').startswith('audio'):
                audio_url = link.get('href')
                break

        if not audio_url:
            continue  # skip episodes without audio

        # Handle image
        image_url = entry.get('image', {}).get('href')
        if not image_url:
            image_url = entry.get('itunes_image', {}).get('href')
        if not image_url and 'media_thumbnail' in entry:
            image_url = entry['media_thumbnail'][0].get('url')

        # Handle pub_date
        pub_date = entry.get('published', '') or entry.get('updated', '')
        try:
            pub_date_obj = datetime(*entry.published_parsed[:6])
            pub_date = pub_date_obj.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            pub_date = None

        episodes.append({
            'title': title,
            'audio_url': audio_url,
            'image_url': image_url,
            'pub_date': pub_date
        })

    return episodes

def insert_episodes(podcast_id, episodes):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for ep in episodes:
        cursor.execute('''
            INSERT INTO episodes (podcast_id, title, audio_url, image_url, pub_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (podcast_id, ep['title'], ep['audio_url'], ep['image_url'], ep['pub_date']))

    conn.commit()
    conn.close()

def import_all_podcasts():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, rss_url FROM podcasts')
    podcasts = cursor.fetchall()
    conn.close()

    for podcast_id, rss_url in podcasts:
        print(f'Importing podcast {podcast_id}: {rss_url}')
        episodes = parse_rss_feed(rss_url)
        insert_episodes(podcast_id, episodes)

if __name__ == '__main__':
    import_all_podcasts()
