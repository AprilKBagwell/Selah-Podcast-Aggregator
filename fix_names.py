import sqlite3

# Connect to the database
conn = sqlite3.connect('podcasts.db')
cursor = conn.cursor()

# These updates will remove the word "Podcast" from specific entries
updates = [
    ("Elisabeth Elliot Podcast", "Elisabeth Elliot"),
    ("Unashamed Podcast", "Unashamed")
]

for old_name, new_name in updates:
    cursor.execute("UPDATE podcasts SET name = ? WHERE name = ?", (new_name, old_name))

# Save changes
conn.commit()
conn.close()

print("✅ Removed 'Podcast' from selected titles.")

