import sqlite3

def cleanup_orphaned_episodes():
    conn = sqlite3.connect("podcasts.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM episodes
        WHERE podcast_id NOT IN (SELECT id FROM podcasts)
    """)
    conn.commit()
    conn.close()
    print("Orphaned episodes cleaned up.")

if __name__ == "__main__":
    cleanup_orphaned_episodes()
