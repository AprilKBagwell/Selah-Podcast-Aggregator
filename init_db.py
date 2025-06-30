import sqlite3

conn = sqlite3.connect('podcasts.db')
cursor = conn.cursor()

# Drop tables if they already exist
cursor.execute('DROP TABLE IF EXISTS podcasts')
cursor.execute('DROP TABLE IF EXISTS episodes')

# Create podcasts table
cursor.execute('''
    CREATE TABLE podcasts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rss_url TEXT NOT NULL,
        image TEXT,
        image_url TEXT
    )
''')

# Create episodes table
cursor.execute('''
    CREATE TABLE episodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        podcast_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        pub_date TEXT,
        audio_url TEXT,
        image_url TEXT,
        FOREIGN KEY (podcast_id) REFERENCES podcasts(id)
    )
''')

conn.commit()
conn.close()

print("Database and tables created successfully.")
