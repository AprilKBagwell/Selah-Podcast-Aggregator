import sqlite3

conn = sqlite3.connect("selah_db.sqlite")
cur = conn.cursor()
cur.execute("SELECT title, rss_url FROM podcasts")
for row in cur.fetchall():
    print(row)
conn.close()
