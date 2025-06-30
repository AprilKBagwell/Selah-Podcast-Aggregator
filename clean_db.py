import sqlite3

conn = sqlite3.connect("selah_db.sqlite")
cur = conn.cursor()
cur.execute("DELETE FROM podcasts WHERE rss_url LIKE 'Enter podcast RSS URL:%'")
conn.commit()
print("Incorrect data removed")
cur.close()
conn.close()
