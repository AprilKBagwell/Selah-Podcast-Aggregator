import sqlite3

def init_db():
    conn = sqlite3.connect('selah.db')
    c = conn.cursor()

    # Drop tables if they exist (optional during development)
    c.execute('DROP TABLE IF EXISTS episodes')
    c.execute('DROP TABLE IF EXISTS podcasts')

    # Create podcasts table
    c.execute('''
        CREATE TABLE podcasts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rss_url TEXT
        )
    ''')

    # Create episodes table
    c.execute('''
        CREATE TABLE episodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            podcast_id INTEGER,
            title TEXT,
            description TEXT,
            pub_date TEXT,
            audio_url TEXT,
            image_url TEXT,
            FOREIGN KEY(podcast_id) REFERENCES podcasts(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database initialized.")

if __name__ == '__main__':
    init_db()
