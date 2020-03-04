# https://www.reddit.com/prefs/apps/

import praw

reddit = praw.Reddit(client_id='?',
                     client_secret='?',
                     password='?',
                     user_agent='praw bot by www.steadylearner.com/blog/search/Python',
                     username='www.steadylearner.com')

print(reddit.read_only)
