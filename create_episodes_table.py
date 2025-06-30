import sqlite3

conn = sqlite3.connect('podcasts.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS episodes')
cursor.execute('''
CREATE TABLE episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    podcast_id INTEGER,
    title TEXT,
    description TEXT,
    pub_date TEXT,
    published TEXT,
    audio_url TEXT,
    image_url TEXT
)
''')

conn.commit()
conn.close()

print("Episodes table created successfully.")
