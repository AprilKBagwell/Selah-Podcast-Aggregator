import sqlite3

PODCASTS = [
    ("Faith Baptist Church", "https://api.sermonaudio.com/v2/rss/broadcasters/faithbaptistavon"),
    ("Focus on the Family", "https://www.omnycontent.com/d/playlist/6b62b447-e557-44a9-ae88-af6300da5440/89194dc4-3e99-4afa-b386-af88014d8e14/482a21be-8b10-4add-a481-af88014d8e1d/podcast.rss"),
    ("Teis Talks", "https://feeds.soundcloud.com/users/soundcloud:users:774099040/sounds.rss"),
    ("Liberty Baptist Church", "https://api.sermonaudio.com/v2/rss/broadcasters/experienceliberty"),
    ("Pensacola Christian College", "https://api.sermonaudio.com/v2/rss/broadcasters/pcc"),
    ("Southern Hills Church", "https://media.rss.com/josh-teis-preaching/feed.xml"),
    ("Biblical Worldview Show", "https://www.kaltura.com/api_v3/getFeed.php?partnerId=2903361&feedId=1_py9vby7p"),
    ("Elisabeth Elliot", "https://podnews.net/podcast/i8fbu"),
    ("Unashamed", "https://feeds.megaphone.fm/BMDC9083048104"),
    ("Relatable with Allie Beth Stuckey", "https://feeds.megaphone.fm/BMDC9964487814"),
    ("Duck Call Room", "https://podnews.net/podcast/i6za0"),
    ("BibleProject", "https://feeds.simplecast.com/3NVmUWZO"),
    ("Strength for Life Pensacola", "https://anchor.fm/s/ec8f4ae8/podcast/rss"),
    ("Wallbuilders", "https://feeds.buzzsprout.com/2077254.rss"),
    ("Seeking Him", "https://cdn.reviveourhearts.com/podcasts/seeking-him.rss"),
    ("Castleview Baptist Church", "https://anchor.fm/s/fbb1fe58/podcast/rss"),
    ("Bubba on the Lake", "https://feeds.simplecast.com/GgyjgRb0"),
    ("Lancaster Baptist Church", "https://feeds-origin.podtrac.com/2kW40nLGkY_a"),
    ("Recovering Fundamentalist Podcast", "https://feeds.castos.com/d5jnq"),
    ("Therapy and Theology", "https://feeds.transistor.fm/therapy-and-theology")
]

def insert_sample_podcasts():
    conn = sqlite3.connect('selah.db')
    c = conn.cursor()

    for name, rss in PODCASTS:
        c.execute("INSERT INTO podcasts (name, rss_url) VALUES (?, ?)", (name, rss))

    conn.commit()
    conn.close()
    print("✅ Podcasts inserted successfully.")

if __name__ == '__main__':
    insert_sample_podcasts()
