# Infinity Gauntlet

import praw
import time
import random

# reddit api login
reddit = praw.Reddit(client_id='API INFO',
                     client_secret='API INFO',
                     username='ThanosBanBot',
                     password='PASSWORD',
                     user_agent='ThanosBot 1.1')

Subreddit = reddit.subreddit("modabuse")
maximum = Subreddit.subscribers

def banHalf():
    counter = 0;
    while True:
        for comment in Subreddit.comments(limit=1):
            if comment.author_flair_text != 'survived' and comment.author_flair_text != 'perished':
                Random = random.randint(0,1)
                if Random == 0:
                    Subreddit.flair.set(comment.author.name,'survived')
                if Random == 1:
                    Subreddit.flair.set(comment.author.name,'perished')
                    Subreddit.banned.add(comment.author.name, ban_reason='The universe needs balance')
                time.sleep(3)
                counter+= 1
                if counter == maximum:
                    return
banHalf()
