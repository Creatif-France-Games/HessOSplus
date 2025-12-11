import feedparser

def run(args):
    print("Fetching the latest tech news...")

    feed_url = "https://www.theverge.com/rss/index.xml"
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        print("Error: could not fetch news.")
        return

    for entry in feed.entries[:5]:
        print(f"\n {entry.title}")
        print(f"{entry.link}")
