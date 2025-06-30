import sqlite3

conn = sqlite3.connect("podcasts.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE episodes ADD COLUMN published TEXT")
    print("Column 'published' added successfully.")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("Column 'published' already exists.")
    else:
        print("Error:", e)

conn.commit()
conn.close()
