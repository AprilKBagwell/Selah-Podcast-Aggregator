import sqlite3

conn = sqlite3.connect("selah.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS episodes")

conn.commit()
conn.close()
print("✅ episodes table dropped.")
