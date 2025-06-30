# create_episodes_table.py

import sqlite3

# Connect to the database
conn = sqlite3.connect('podcasts.db')
cursor = conn.cursor()

# Drop the old episodes table if it exists
cursor.execute("DROP TABLE IF EXISTS episodes")

# Create a new episodes table with the correct schema
cursor.execute("""
CREATE TABLE episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    podcast_id INTEGER,
    title TEXT,
    pub_date TEXT,
    audio_url TEXT,
    image_url TEXT
)
""")

conn.commit()
conn.close()

print("✅ episodes table recreated successfully.")
