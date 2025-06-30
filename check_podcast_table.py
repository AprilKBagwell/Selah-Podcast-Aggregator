import sqlite3
conn = sqlite3.connect('selah.db')
cursor = conn.cursor()
cursor.execute('PRAGMA table_info(Episode)')
print(cursor.fetchall())
conn.close()
