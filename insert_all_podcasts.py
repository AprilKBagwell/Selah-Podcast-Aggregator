import sqlite3

# Connect to selah.db
conn = sqlite3.connect('selah.db')
cur = conn.cursor()

# List of podcasts to insert
podcasts = [
    ("Faith Baptist Church", "https://api.sermonaudio.com/v2/rss/broadcasters/faithbaptistavon", "static/images/faith-baptist-church.png"),
    ("Focus on the Family", "https://www.omnycontent.com/d/playlist/6b62b447-e557-44a9-ae88-af6300da5440/89194dc4-3e99-4afa-b386-af88014d8e14/482a21be-8b10-4add-a481-af88014d8e1d/podcast.rss", "static/images/focus-on-the-family.png"),
    ("Teis Talks", "https://feeds.soundcloud.com/users/soundcloud:users:774099040/sounds.rss", "static/images/teis-talks.png"),
    ("Liberty Baptist Church", "https://api.sermonaudio.com/v2/rss/broadcasters/experienceliberty", "static/images/liberty-baptist-church.png"),
    ("Pensacola Christian College", "https://api.sermonaudio.com/v2/rss/broadcasters/pcc", "static/images/pensacola-christian-college.png"),
    ("Southern Hills Church", "https://media.rss.com/josh-teis-preaching/feed.xml", "static/images/southern-hills-church.png"),
    ("Biblical Worldview Show", "https://www.kaltura.com/api_v3/getFeed.php?partnerId=2903361&feedId=1_py9vby7p", "static/images/biblical-worldview-show.png"),
    ("Elisabeth Elliot", "https://podnews.net/podcast/i8fbu", "static/images/elisabeth-elliot.png"),
    ("Unashamed", "https://feeds.megaphone.fm/BMDC9083048104", "static/images/unashamed.png"),
    ("Relatable with Allie Beth Stuckey", "https://feeds.megaphone.fm/BMDC9964487814", "static/images/relatable-with-allie-beth-stuckey.png"),
    ("Duck Call Room", "https://podnews.net/podcast/i6za0", "static/images/duck-call-room.png"),
    ("BibleProject", "https://feeds.simplecast.com/3NVmUWZO", "static/images/bibleproject.png"),
    ("Strength for Life Pensacola", "https://anchor.fm/s/ec8f4ae8/podcast/rss", "static/images/strength-for-life-pensacola.png"),
    ("Wallbuilders", "https://feeds.buzzsprout.com/2077254.rss", "static/images/wallbuilders.png"),
    ("Seeking Him", "https://cdn.reviveourhearts.com/podcasts/seeking-him.rss", "static/images/seeking-him.png"),
    ("Castleview Baptist Church", "https://anchor.fm/s/fbb1fe58/podcast/rss", "static/images/castleview-baptist-church.png"),
    ("Bubba on the Lake", "https://feeds.simplecast.com/GgyjgRb0", "static/images/bubba-on-the-lake.png"),
    ("Lancaster Baptist Church", "https://feeds-origin.podtrac.com/2kW40nLGkY_a", "static/images/lancaster-baptist-church.png"),
    ("Recovering Fundamentalist Podcast", "https://feeds.castos.com/d5jnq", "static/images/recovering-fundamentalist-podcast.png"),
    ("Therapy and Theology", "https://feeds.transistor.fm/therapy-and-theology", "static/images/therapy-and-theology.png")
]

# Insert podcasts safely
for name, rss_url, image_url in podcasts:
    print(f"Inserting: {name}")
    cur.execute("""
        INSERT INTO podcasts (name, rss_url, image_url)
        VALUES (?, ?, ?)
    """, (name, rss_url, image_url))

conn.commit()
conn.close()
print("✅ All podcasts inserted successfully.")
