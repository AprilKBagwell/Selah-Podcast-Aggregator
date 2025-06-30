import sqlite3

conn = sqlite3.connect('selah.db')
cursor = conn.cursor()

try:
    cursor.execute('ALTER TABLE Episode ADD COLUMN description TEXT')
    print("Added description column.")
except sqlite3.OperationalError as e:
    print(f"Description: {e}")

try:
    cursor.execute('ALTER TABLE Episode ADD COLUMN pub_date TEXT')
    print("Added pub_date column.")
except sqlite3.OperationalError as e:
    print(f"Pub_date: {e}")

try:
    cursor.execute('ALTER TABLE Episode ADD COLUMN audio_url TEXT')
    print("Added audio_url column.")
except sqlite3.OperationalError as e:
    print(f"Audio_url: {e}")

conn.commit()
conn.close()
