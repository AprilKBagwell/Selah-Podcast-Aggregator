import feedparser

def inspect_feed(rss_url):
    print(f"\nInspecting RSS feed: {rss_url}")
    feed = feedparser.parse(rss_url)

    if feed.bozo:
        print("❌ Feed parse error (bozo):", feed.bozo_exception)
        return

    print(f"\n📡 Feed Title: {feed.feed.get('title', 'Unknown')}")
    print(f"🔗 Link: {feed.feed.get('link', 'N/A')}")
    print(f"📦 Total Entries Found: {len(feed.entries)}")

    if not feed.entries:
        print("❌ No episodes found.")
        return

    # Show preview of first episode
    first = feed.entries[0]
    print("\n🎙️ First Episode:")
    print("  • Title:", first.get("title", "No title"))
    print("  • Published:", first.get("published", "No date"))

    # Try finding the audio file
    audio_url = None
    if "enclosures" in first and first.enclosures:
        audio_url = first.enclosures[0].get("href")
    elif "media_content" in first:
        audio_url = first.media_content[0].get("url")
    elif "links" in first:
        for link in first.links:
            if link.get("type", "").startswith("audio"):
                audio_url = link.get("href")
                break

    if audio_url:
        print("  • Audio URL:", audio_url)
    else:
        print("  • ❌ Audio URL not found in first entry.")

# Example usage
if __name__ == "__main__":
    test_feeds = [
        "https://feeds.megaphone.fm/duckcallroom",
        "https://feedpress.me/ee-podcast"
    ]
    for url in test_feeds:
        inspect_feed(url)
