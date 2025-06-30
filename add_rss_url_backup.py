import psycopg2
import feedparser
import sys

def ensure_rss_url_column(cursor):
    cursor.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'podcasts' AND column_name = 'rss_url'
    """)
    if not cursor.fetchone():
        cursor.execute("ALTER TABLE podcasts ADD COLUMN rss_url TEXT UNIQUE")
        print("Added rss_url column")
    else:
        print("rss_url column already exists")

def add_rss_url(podcast_url):
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            dbname="selah_db",
            user="postgres",  # Change to your PostgreSQL username (likely 'postgres')
            password="your_postgres_password",  # Replace with the password set during install
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Check/create podcasts table
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'podcasts'
            )
        """)
        if not cursor.fetchone()[0]:
            cursor.execute("""
                CREATE TABLE podcasts (
                    id SERIAL PRIMARY KEY,
                    rss_url TEXT UNIQUE,
                    title TEXT
                )
            """)
            print("Created podcasts table")

        # Ensure rss_url column exists
        ensure_rss_url_column(cursor)

        # Parse and validate RSS feed
        feed = feedparser.parse(podcast_url)
        if feed.bozo:
            print(f"Invalid RSS feed: {podcast_url}")
            return

        # Insert RSS URL
        cursor.execute(
            "INSERT INTO podcasts (rss_url, title) VALUES (%s, %s) ON CONFLICT (rss_url) DO NOTHING",
            (podcast_url, feed.feed.get('title', 'Unknown'))
        )
        conn.commit()
        print(f"Added {podcast_url} to database")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        add_rss_url(sys.argv[1])
    else:
        rss_url = input("Enter podcast RSS URL: ")
        add_rss_url(rss_url)
        


