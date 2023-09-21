import feedparser
import post_function

myFeed = feedparser.parse('http://feeds.feedburner.com/EEJournalFeatureArticles.xml')
new_id = myFeed.entries[0]['post-id']


# Read the post-id of the most recently posted article
f = open('most_recent_post.txt', 'r')
old_id = f.read()
f.close()
print("Old post-id: " + old_id)
print("New post-id: " + new_id)


if old_id != new_id:
    f = open('most_recent_post.txt', 'w')
    f.write(new_id)
    f.close()
    print('post new article')
    post_function.post_new_article()
else:
    print('No new article to post')


