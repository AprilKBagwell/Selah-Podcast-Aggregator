import sqlite3

# Connect to the correct database
conn = sqlite3.connect("selah.db")
c = conn.cursor()

# Sample podcast details
name = "Selah Podcast Aggregator"
rss_url = "https://example.com/sample-feed.xml"
image_url = "static/images/default-podcast.png"

# Insert into the correct table and columns
c.execute("""
    INSERT INTO podcasts (name, rss_url, image_url)
    VALUES (?, ?, ?)
""", (name, rss_url, image_url))

conn.commit()
conn.close()

print("Sample podcast inserted successfully.")
