import sqlite3

def check_episode_counts():
    conn = sqlite3.connect('selah.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Podcast.title, COUNT(Episode.episode_id) as episode_count
        FROM Podcast
        LEFT JOIN Episode ON Podcast.podcast_id = Episode.podcast_id
        GROUP BY Podcast.title
        ORDER BY Podcast.title
    """)

    results = cursor.fetchall()
    print("\n🎧 Episode Counts by Podcast:\n")
    for row in results:
        title, count = row
        print(f"{title}: {count} episodes")

    conn.close()

if __name__ == '__main__':
    check_episode_counts()
