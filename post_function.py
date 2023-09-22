from mastodon import Mastodon
import feedparser

def post_new_article():

    # Set up Mastodon
    mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space')

    myFeed = feedparser.parse('http://feeds.feedburner.com/EEJournalFeatureArticles.xml')

    mastodon.status_post("A new article has been posted from EEJournal:\n"\
        + "\"" + myFeed.entries[0].title + "\"\n\n"\
        + myFeed.entries[0].link + "\n\n"
        + "#eeJournal")