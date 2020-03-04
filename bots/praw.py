import os
import praw

reddit = praw.Reddit(client_id='?',
                     client_secret='?',
                     password='?',
                     user_agent='www.steadylearner.com/blog/search/Rust',
                     username='steadylearner_p')

target = "rust"
subreddit = reddit.subreddit(target)

limit = 20

content = ""

index = 1  # The code below is not iterable object so use this
for submission in subreddit.new(limit = limit):
    payload = f"{index}. [{submission.title}]({submission.url})"
    print(payload)

    content += payload

    index += 1

# https://github.com/steadylearner/Rust-Full-Stack/blob/master/blog/post_log/create.py
filename = f"new_{target}_posts.md"

with open(filename, "w") as f:
    f.write(content)

