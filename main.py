import feedparser

def get_latest_news():
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml' # or use this link: http://feeds.bbci.co.uk/news/world/rss.xml
    
    feed = feedparser.parse(url)
    latest_news = []
    
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        latest_news.append({'title': title, 'link': link})
    
    return latest_news

print(get_latest_news())