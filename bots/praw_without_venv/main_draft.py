import os
# from timeit import default_timer as timer

import praw
from settings import client_id, client_secret, password

# start = timer()

username = "steadylearner_p"

# https://www.reddit.com/prefs/apps/
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=f"/u/{username}",
    username=username,
)

target = input("Which subreddit you want to scrap?\n")

if not target:
    target = "forhire"

subreddit = reddit.subreddit(target)

limit = input("How many you want?\n")

if not limit:
    limit = 50
else:
    limit = int(limit)

content = f"# Latest {limit} posts from {target} subreddit. \n\n"

# Handle when url starts with /r/
# For example, /r/learnrust/comments/fchl5c/bindgen_wont_bindgen_cant_find_stdlibh/

index = 1  # The code below is not iterable object so use this
for submission in subreddit.new(limit=limit):
    # print(dir(submission)) # Use this to write more features.

    # It(visted) doesn't update fast? Remove it if you think it unnecessary.
    if not submission.visited:

        payload = f"{index}. [{submission.title}]({submission.url})"
        print(payload)

        content += payload + "\n"

        index += 1

# https://github.com/steadylearner/Rust-Full-Stack/blob/master/blog/post_log/create.py
# filename = f"new_{target}_posts.md"
filename = f"{target}.md"

with open(filename, "w") as f:
    f.write(content)
    print(f"\nThe {filename} was built.") 
   
    # end = timer()
    # time_passed = end - start
    # print(f"\nThe {filename} was built in {round(time_passed, 1)} seconds.")
