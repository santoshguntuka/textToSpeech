import feedparser

def fetch_articles(rss_url):
    print(f"Fetching RSS feed from: {rss_url}")
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        print("No articles found in the feed.")
        return []
    
    articles = []
    for entry in feed.entries:
        print(f"Found article: {entry.title}")
        articles.append({
            'title': entry.title,
            'summary': entry.summary,
            'link': entry.link
        })
    
    return articles


if __name__ == "__main__":
    rss_url = 'https://abcnews.go.com/abcnews/usheadlines'  # Make sure this is a valid RSS feed URL
    articles = fetch_articles(rss_url)
    if articles:
        for article in articles:
            print(f"Title: {article['title']}\nSummary: {article['summary']}\nLink: {article['link']}\n")
    else:
        print("No articles to display.")
